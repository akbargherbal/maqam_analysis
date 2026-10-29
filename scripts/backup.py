#!/usr/bin/env python3
"""Durable checkpoints to GCS and a private GitHub repo, plus safe restore.

    python3 scripts/backup.py flush              # GCS first, then git commit/push
    python3 scripts/backup.py flush --dry-run
    python3 scripts/backup.py restore            # git pull + GCS overlay, merge labels
    python3 scripts/backup.py check              # last backup ages

Safety: git push is refused when the GitHub remote is public (the ABCs and
labels are derived from copyrighted recordings). GCS remains the real-time
durability layer, so a blocked git push never loses a label.
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
import time
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (  # noqa: E402
    ROOT,
    atomic_write_json,
    gcs_cp,
    gcs_rsync,
    gcloud_available,
    github_visibility,
    human_bytes,
    load_config,
    path,
    read_json,
    run_cmd,
    utc_now,
)
from progress import compute_progress, write_progress  # noqa: E402

GCS_DIRS = ("state", "labels", "work", "exports", "qc")
GCS_FILES = ("data/manifest.jsonl", "data/transcripts_index.json", "state/ledger.jsonl")
GIT_PATHS = ("labels", "state", "work", "exports", "qc", "data/manifest.jsonl", "data/transcripts_index.json")


def git(*args: str, check: bool = False, timeout: float = 120):
    return run_cmd(["git", *args], check=check, timeout=timeout)


def git_ok() -> bool:
    proc = git("rev-parse", "--is-inside-work-tree", check=False, timeout=10)
    return proc.returncode == 0 and proc.stdout.strip() == "true"


def remote_url(remote: str) -> str | None:
    proc = git("remote", "get-url", remote, check=False, timeout=10)
    if proc.returncode != 0:
        return None
    return proc.stdout.strip() or None


def tree_stats(rel_paths) -> tuple[int, int]:
    files = 0
    size = 0
    for rel in rel_paths:
        p = path(rel)
        if p.is_dir():
            for f in p.rglob("*"):
                if f.is_file():
                    files += 1
                    size += f.stat().st_size
        elif p.is_file():
            files += 1
            size += p.stat().st_size
    return files, size


# --------------------------------------------------------------------------- flush
def cmd_flush(args) -> int:
    cfg = load_config(args.config)
    backup_cfg = cfg.get("backup", {})
    prefix = (backup_cfg.get("gcs_prefix") or "").rstrip("/")
    now = utc_now()
    previous = read_json(path("state") / "backup.json", {}) or {}
    report: dict[str, Any] = {"run_id": cfg["run_id"], "updated_at": now}
    progress = compute_progress(cfg) if path(cfg["manifest"]).exists() else {}
    errors = []

    # ------------------------------------------------------------------ GCS
    if args.no_gcs or not prefix:
        report["last_gcs"] = previous.get("last_gcs", {})
        print("gcs: skipped")
    elif not gcloud_available():
        report["last_gcs"] = {**previous.get("last_gcs", {}), "ok": False, "error": "gcloud not found", "at": now}
        errors.append("gcloud not found")
        print("gcs: skipped (gcloud not found)", file=sys.stderr)
    else:
        files, size = tree_stats(GCS_DIRS + GCS_FILES)
        print(f"gcs: {files} files, {human_bytes(size)} -> {prefix}")
        try:
            for rel in GCS_DIRS:
                if path(rel).exists():
                    gcs_rsync(str(path(rel)), f"{prefix}/{rel}", dry_run=args.dry_run, timeout=900)
            for rel in GCS_FILES:
                if not path(rel).exists():
                    continue
                if args.dry_run:
                    print(f"  [dry-run] cp {rel} -> {prefix}/{rel}")
                else:
                    gcs_cp(str(path(rel)), f"{prefix}/{rel}", timeout=300)
            report["last_gcs"] = {
                "at": now,
                "ok": True,
                "prefix": prefix,
                "files": files,
                "bytes": size,
                "dry_run": bool(args.dry_run),
            }
            print("gcs: ok")
        except Exception as exc:
            report["last_gcs"] = {"at": now, "ok": False, "prefix": prefix, "error": str(exc)}
            errors.append(f"gcs: {exc}")
            print(f"gcs: FAILED: {exc}", file=sys.stderr)

    # ------------------------------------------------------------------ git
    git_cfg = backup_cfg.get("git", {})
    if args.no_git or not git_cfg.get("enabled", True) or not git_ok():
        report["last_git"] = previous.get("last_git", {})
        print("git: skipped")
    elif args.dry_run:
        report["last_git"] = {**previous.get("last_git", {}), "dry_run": True, "at": now}
        print("git: [dry-run] would commit and push")
    else:
        try:
            status = git("status", "--porcelain", check=False, timeout=30)
            dirty = bool(status.stdout.strip())
            commit_hash = ""
            if dirty or args.force:
                for rel in GIT_PATHS:
                    if path(rel).exists():
                        git("add", "-A", rel, check=True)
                # Do not commit huge/derived trees even if a broad add occurred.
                git("reset", "-q", "data/abc", "data/abc_melody", "cache", "logs", check=False)
                msg = (
                    f"checkpoint: {progress.get('labeled', 0)}/{progress.get('abc_ok', 0)} labels "
                    f"({cfg['run_id']})"
                )
                proc = git("commit", "-m", msg, check=False, timeout=120)
                if proc.returncode != 0 and "nothing to commit" not in (proc.stdout + proc.stderr).lower():
                    raise RuntimeError((proc.stderr or proc.stdout).strip())
                commit_hash = git("rev-parse", "--short", "HEAD", check=False, timeout=10).stdout.strip()
                print(f"git: committed {commit_hash} ({msg})")
            else:
                commit_hash = git("rev-parse", "--short", "HEAD", check=False, timeout=10).stdout.strip()
                print("git: no changes to commit")

            pushed = False
            remote = git_cfg.get("remote", "origin")
            branch = git_cfg.get("branch", "main")
            url = remote_url(remote)
            if not url:
                print(f"git: no remote '{remote}' (commit kept locally)", file=sys.stderr)
            elif not git_cfg.get("push", True):
                print("git: push disabled in config")
            else:
                private = github_visibility(url)
                requires_private = bool(backup_cfg.get("require_private_github", True))
                if requires_private and private is False:
                    print(
                        "git: PUSH REFUSED — the GitHub remote is PUBLIC. Make it private before pushing "
                        "labels/ABC-derived data. GCS backup is still active.",
                        file=sys.stderr,
                    )
                    errors.append("git push refused: public repository")
                elif requires_private and private is None and not args.allow_unknown_visibility:
                    print(
                        "git: push skipped — could not verify repository visibility (set GITHUB_TOKEN or "
                        "pass --allow-unknown-visibility). GCS backup is still active.",
                        file=sys.stderr,
                    )
                    errors.append("git push skipped: visibility unknown")
                else:
                    proc = git("push", remote, branch, check=False, timeout=300)
                    if proc.returncode == 0:
                        pushed = True
                        print(f"git: pushed {commit_hash} -> {remote}/{branch}")
                    else:
                        errors.append(f"git push: {(proc.stderr or proc.stdout).strip()[:500]}")
                        print(f"git: push FAILED: {(proc.stderr or proc.stdout).strip()}", file=sys.stderr)
            report["last_git"] = {
                "at": now,
                "ok": True,
                "commit": commit_hash,
                "pushed": pushed,
                "remote": url or "",
                "branch": branch,
            }
        except Exception as exc:
            report["last_git"] = {"at": now, "ok": False, "error": str(exc)}
            errors.append(f"git: {exc}")
            print(f"git: FAILED: {exc}", file=sys.stderr)

    if args.dry_run:
        print("backup: dry-run complete (no state/backup.json written)")
        return 1 if errors else 0

    atomic_write_json(path("state") / "backup.json", report)
    if report.get("last_gcs", {}).get("ok") and prefix and not args.no_gcs and gcloud_available():
        try:
            gcs_cp(str(path("state") / "backup.json"), f"{prefix}/state/backup.json", timeout=120)
        except Exception as exc:
            print(f"WARNING: could not upload backup.json: {exc}", file=sys.stderr)

    if not args.quiet:
        gcs = report.get("last_gcs") or {}
        g = report.get("last_git") or {}
        print(
            f"backup summary: gcs={'ok' if gcs.get('ok') else 'no'} "
            f"git={g.get('commit') or '-'} pushed={bool(g.get('pushed'))}"
        )

    # GCS is the durable layer. A blocked git push is a warning, not data loss.
    durable = bool((report.get("last_gcs") or {}).get("ok")) or bool((report.get("last_git") or {}).get("pushed"))
    return 0 if durable else 1


# ------------------------------------------------------------------------- restore
def _label_sort_key(label: dict[str, Any]) -> tuple[int, str]:
    prov = label.get("provenance") or {}
    return int(prov.get("revision") or 0), str(prov.get("updated_at") or "")


def merge_labels(remote_dir: Path, local_dir: Path, conflicts_dir: Path) -> tuple[int, int]:
    copied = 0
    conflicts = 0
    if not remote_dir.exists():
        return copied, conflicts
    local_dir.mkdir(parents=True, exist_ok=True)
    for rp in sorted(remote_dir.glob("*.json")):
        if rp.name.startswith("_"):
            continue
        remote = read_json(rp, None)
        if not isinstance(remote, dict) or not remote.get("song_id"):
            continue
        lp = local_dir / rp.name
        local = read_json(lp, None)
        if not isinstance(local, dict):
            shutil.copy2(rp, lp)
            copied += 1
            continue
        if _label_sort_key(remote) > _label_sort_key(local):
            conflicts_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(lp, conflicts_dir / f"{rp.stem}.local.json")
            shutil.copy2(rp, lp)
            copied += 1
            conflicts += 1
        elif _label_sort_key(remote) < _label_sort_key(local):
            conflicts_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(rp, conflicts_dir / f"{rp.stem}.remote.json")
            conflicts += 1
    return copied, conflicts


def copy_missing_tree(src: Path, dst: Path) -> int:
    copied = 0
    if not src.exists():
        return 0
    for sp in src.rglob("*"):
        if not sp.is_file():
            continue
        rel = sp.relative_to(src)
        dp = dst / rel
        if not dp.exists():
            dp.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(sp, dp)
            copied += 1
    return copied


def cmd_restore(args) -> int:
    cfg = load_config(args.config)
    backup_cfg = cfg.get("backup", {})
    prefix = (backup_cfg.get("gcs_prefix") or "").rstrip("/")
    source = args.source

    if source in ("auto", "git") and args.git_pull and git_ok():
        proc = git("pull", "--ff-only", check=False, timeout=120)
        if proc.returncode == 0:
            print("git: pulled")
        else:
            print(f"git: pull skipped/failed: {(proc.stderr or proc.stdout).strip()[:300]}", file=sys.stderr)

    if source in ("auto", "gcs"):
        if not prefix:
            print("restore: no GCS prefix configured; relying on git", file=sys.stderr)
        elif not gcloud_available():
            print("restore: gcloud not found; relying on git", file=sys.stderr)
        elif not args.dry_run:
            tmp = path("cache/restore")
            if tmp.exists():
                shutil.rmtree(tmp)
            tmp.mkdir(parents=True, exist_ok=True)
            restored_any = False
            for rel in ("labels", "state", "work", "exports", "qc"):
                print(f"restore: gs://.../{rel} -> {tmp}/{rel}")
                try:
                    gcs_rsync(f"{prefix}/{rel}", str(tmp / rel), timeout=900)
                    restored_any = True
                except Exception as exc:
                    print(f"restore: {rel} not restored: {exc}", file=sys.stderr)
            if (tmp / "labels").exists():
                copied, conflicts = merge_labels(tmp / "labels", path("labels"), path("labels/_conflicts"))
                print(f"restore: labels copied={copied}, conflicts={conflicts}")
            for rel in ("state", "work", "exports", "qc"):
                n = copy_missing_tree(tmp / rel, path(rel))
                if n:
                    print(f"restore: {rel} missing files copied={n}")
            if source == "gcs" and not restored_any:
                return 1

    if path(cfg["manifest"]).exists():
        progress = write_progress(cfg)
        print(
            f"restore: {progress['labeled']}/{progress['abc_ok']} labels present, "
            f"{progress['remaining']} remaining"
        )
        print("next: python3 scripts/status.py")
    else:
        print("restore: manifest missing; run python3 scripts/prepare.py", file=sys.stderr)
    return 0


# --------------------------------------------------------------------------- check
def cmd_check(args) -> int:
    cfg = load_config(args.config)
    report = read_json(path("state") / "backup.json", {}) or {}
    progress = compute_progress(cfg) if path(cfg["manifest"]).exists() else {}
    print(f"run: {cfg['run_id']} | labels {progress.get('labeled', 0)}/{progress.get('abc_ok', 0)}")
    for key, label in (("last_gcs", "GCS"), ("last_git", "git")):
        item = report.get(key) or {}
        if not item:
            print(f"{label}: never")
            continue
        age = item.get("at")
        print(
            f"{label}: at={age} ok={item.get('ok')} "
            f"commit={item.get('commit') or '-'} pushed={item.get('pushed')} "
            f"error={item.get('error') or '-'}"
        )
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", default=None)
    sub = ap.add_subparsers(dest="cmd", required=True)

    f = sub.add_parser("flush")
    f.add_argument("--no-gcs", action="store_true")
    f.add_argument("--no-git", action="store_true")
    f.add_argument("--force", action="store_true", help="commit even when git sees no changes")
    f.add_argument("--allow-unknown-visibility", action="store_true")
    f.add_argument("--dry-run", action="store_true")
    f.add_argument("--quiet", action="store_true")
    f.set_defaults(func=cmd_flush)

    r = sub.add_parser("restore")
    r.add_argument("--source", choices=["auto", "gcs", "git"], default="auto")
    r.add_argument("--git-pull", action="store_true", default=True)
    r.add_argument("--no-git-pull", dest="git_pull", action="store_false")
    r.add_argument("--dry-run", action="store_true")
    r.set_defaults(func=cmd_restore)

    c = sub.add_parser("check")
    c.set_defaults(func=cmd_check)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())

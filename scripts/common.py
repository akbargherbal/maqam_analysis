#!/usr/bin/env python3
"""Shared helpers for the maqam-167 labeling pipeline.

Stdlib only. Every write that matters is atomic (temp file + fsync + rename), and
every label is appended to an append-only ledger so a lost Colab VM can always be
reconstructed from the backup.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
PIPELINE_VERSION = "1.0.0"
DEFAULT_CONFIG = ROOT / "config" / "config.json"


# --------------------------------------------------------------------------- time
def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def parse_utc(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def age_hours(value: str | None) -> float | None:
    dt = parse_utc(value)
    if dt is None:
        return None
    return (datetime.now(timezone.utc) - dt).total_seconds() / 3600.0


# ------------------------------------------------------------------------- config
def load_config(path: str | os.PathLike | None = None) -> dict[str, Any]:
    """Load config/config.json and apply the small set of env overrides used in Colab."""
    cfg_path = Path(path or os.environ.get("MAQAM_CONFIG", DEFAULT_CONFIG))
    if not cfg_path.exists():
        raise SystemExit(f"config not found: {cfg_path}")
    with open(cfg_path, encoding="utf-8") as f:
        cfg = json.load(f)

    if os.environ.get("MAQAM_RUN_ID"):
        cfg["run_id"] = os.environ["MAQAM_RUN_ID"]
    if os.environ.get("MAQAM_GCS_BACKUP"):
        cfg.setdefault("backup", {})["gcs_prefix"] = os.environ["MAQAM_GCS_BACKUP"]
    if os.environ.get("MAQAM_GIT_REMOTE"):
        cfg.setdefault("backup", {}).setdefault("git", {})["remote"] = os.environ["MAQAM_GIT_REMOTE"]
    if os.environ.get("MAQAM_AUDIO_ROOT"):
        cfg.setdefault("audio", {})["root"] = os.environ["MAQAM_AUDIO_ROOT"]
    if os.environ.get("MAQAM_BATCH_SIZE"):
        cfg.setdefault("labeling", {})["batch_size"] = int(os.environ["MAQAM_BATCH_SIZE"])

    cfg["_config_path"] = str(cfg_path)
    return cfg


def path(rel: str | os.PathLike) -> Path:
    p = Path(rel)
    return p if p.is_absolute() else ROOT / p


def ensure_layout(cfg: dict[str, Any]) -> None:
    for rel in (
        "config",
        "data",
        "labels",
        "state",
        "work",
        "logs",
        "exports",
        "cache",
        cfg["transcripts"]["cache_dir"],
        cfg["transcripts"]["abc_dir"],
        cfg["transcripts"].get("abc_melody_dir", "data/abc_melody"),
    ):
        path(rel).mkdir(parents=True, exist_ok=True)


# ------------------------------------------------------------------------ hashing
def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(file_path: str | os.PathLike, chunk: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        while True:
            block = f.read(chunk)
            if not block:
                break
            h.update(block)
    return h.hexdigest()


def stable_json(obj: Any) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def object_hash(obj: Any) -> str:
    return sha256_text(stable_json(obj))


# ------------------------------------------------------------------------- files
def read_json(file_path: str | os.PathLike, default: Any = None) -> Any:
    p = Path(file_path)
    if not p.exists():
        return default
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def read_text(file_path: str | os.PathLike, default: str | None = None) -> str | None:
    p = Path(file_path)
    if not p.exists():
        return default
    return p.read_text(encoding="utf-8")


def dumps_json(obj: Any) -> str:
    return json.dumps(obj, ensure_ascii=False, indent=2) + "\n"


def atomic_write_text(file_path: str | os.PathLike, text: str) -> None:
    p = Path(file_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=p.parent, prefix=".tmp-", text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, p)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def atomic_write_json(file_path: str | os.PathLike, obj: Any) -> None:
    atomic_write_text(file_path, dumps_json(obj))


def append_jsonl(file_path: str | os.PathLike, obj: dict[str, Any]) -> None:
    p = Path(file_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    line = json.dumps(obj, ensure_ascii=False, sort_keys=True)
    with open(p, "a", encoding="utf-8") as f:
        f.write(line + "\n")
        f.flush()
        os.fsync(f.fileno())


def read_jsonl(file_path: str | os.PathLike) -> list[dict[str, Any]]:
    p = Path(file_path)
    if not p.exists():
        return []
    rows = []
    with open(p, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


# ------------------------------------------------------------------------ naming
def normalize_text(value: str) -> str:
    value = unicodedata.normalize("NFKC", value or "")
    value = value.replace("’", "'").replace("‘", "'").replace("–", "-").replace("—", "-")
    value = re.sub(r"\s+", " ", value).strip().lower()
    return value


def slugify(value: str, max_len: int = 100) -> str:
    value = unicodedata.normalize("NFKD", value or "")
    value = value.encode("ascii", "ignore").decode("ascii")
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    value = re.sub(r"-{2,}", "-", value)
    return (value[:max_len].rstrip("-") or "x")


def make_song_id(row: dict[str, Any], used: set[str] | None = None) -> str:
    artist = slugify(row.get("artist", ""))
    album = slugify(row.get("album", ""))
    if album.startswith(artist + "-"):
        album = album[len(artist) + 1 :]
    stem = slugify(Path(row.get("file", "track")).stem)
    base = "-".join(part for part in (artist, album, stem) if part)
    if len(base) > 110:
        base = base[:110].rstrip("-")
    if used is not None and base in used:
        base = f"{base}-{sha256_text(row.get('track_id', base))[:8]}"
    return base


# --------------------------------------------------------------------- manifest
def manifest_path(cfg: dict[str, Any]) -> Path:
    return path(cfg["manifest"])


def load_manifest(cfg: dict[str, Any]) -> list[dict[str, Any]]:
    rows = read_jsonl(manifest_path(cfg))
    if not rows:
        raise SystemExit(
            "data/manifest.jsonl is missing or empty. Run: python3 scripts/prepare.py"
        )
    return rows


def load_labels(cfg: dict[str, Any]) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    labels_dir = path("labels")
    if not labels_dir.exists():
        return out
    for p in sorted(labels_dir.glob("*.json")):
        if p.name.startswith("_"):
            continue
        try:
            obj = read_json(p)
        except json.JSONDecodeError as exc:
            print(f"WARNING: unreadable label {p}: {exc}", file=sys.stderr)
            continue
        if isinstance(obj, dict) and obj.get("song_id"):
            out[obj["song_id"]] = obj
    return out


def label_path(song_id: str) -> Path:
    return path("labels") / f"{song_id}.json"


def evidence_path(cfg: dict[str, Any], song_id: str) -> Path:
    return path("work") / song_id / "evidence.json"


def work_dir(song_id: str) -> Path:
    return path("work") / song_id


# ------------------------------------------------------------------------ ledger
def ledger_event(cfg: dict[str, Any], event: str, **fields: Any) -> dict[str, Any]:
    row = {"ts": utc_now(), "run_id": cfg["run_id"], "event": event, **fields}
    append_jsonl(path("state") / "ledger.jsonl", row)
    return row


# ---------------------------------------------------------------------- commands
def run_cmd(
    cmd: list[str],
    *,
    check: bool = True,
    timeout: float | None = None,
    capture: bool = True,
    env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess:
    try:
        proc = subprocess.run(
            cmd,
            text=True,
            capture_output=capture,
            timeout=timeout,
            env={**os.environ, **env} if env else None,
        )
    except FileNotFoundError:
        raise SystemExit(f"command not found: {cmd[0]}")
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"command timed out after {timeout}s: {' '.join(cmd)}")
    if check and proc.returncode != 0:
        detail = ((proc.stderr or "") + "\n" + (proc.stdout or "")).strip()
        raise RuntimeError(f"command failed ({proc.returncode}): {' '.join(cmd)}\n{detail}")
    return proc


def gcloud_available() -> bool:
    return shutil.which("gcloud") is not None


def gcs_cp(src: str, dst: str, *, recursive: bool = False, timeout: float = 600) -> None:
    cmd = ["gcloud", "storage", "cp"]
    if recursive:
        cmd.append("-r")
    cmd += [src, dst]
    run_cmd(cmd, timeout=timeout)


def gcs_rsync(src: str, dst: str, *, dry_run: bool = False, timeout: float = 900) -> None:
    cmd = ["gcloud", "storage", "rsync", "-r"]
    if dry_run:
        cmd.append("--dry-run")
    cmd += [src, dst]
    run_cmd(cmd, timeout=timeout)


def gcs_exists(uri: str) -> bool:
    if not gcloud_available():
        return False
    proc = run_cmd(["gcloud", "storage", "ls", uri], check=False, timeout=60)
    return proc.returncode == 0


# ------------------------------------------------------------------------- github
def github_slug(remote_url: str) -> tuple[str, str] | None:
    m = re.search(r"github\.com[:/]+([^/]+)/([^/]+?)(?:\.git)?/?$", remote_url.strip())
    if not m:
        return None
    owner, repo = m.group(1), m.group(2)
    return owner, repo


def github_visibility(remote_url: str, timeout: float = 10) -> bool | None:
    """True if private, False if public, None if unknown."""
    slug = github_slug(remote_url)
    if not slug:
        return None
    owner, repo = slug
    req = urllib.request.Request(
        f"https://api.github.com/repos/{owner}/{repo}",
        headers={"User-Agent": "maqam-analysis-pipeline", "Accept": "application/vnd.github+json"},
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        return bool(data.get("private"))
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError):
        return None


# -------------------------------------------------------------------------- misc
def human_bytes(n: int) -> str:
    units = ["B", "KB", "MB", "GB"]
    value = float(n)
    for unit in units:
        if value < 1024 or unit == units[-1]:
            return f"{value:.1f} {unit}"
        value /= 1024
    return f"{value:.1f} GB"


def fmt_pct(num: int, den: int) -> str:
    return f"{100.0 * num / den:.1f}%" if den else "n/a"


def chunked(items: Iterable, size: int):
    bucket = []
    for item in items:
        bucket.append(item)
        if len(bucket) == size:
            yield bucket
            bucket = []
    if bucket:
        yield bucket

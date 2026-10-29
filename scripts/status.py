#!/usr/bin/env python3
"""One-shot progress report. Never blocks, never tails a log.

    python3 scripts/status.py
    python3 scripts/status.py --json
    python3 scripts/status.py --reconcile     # rewrite state/progress.json
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import load_config, path, read_json, utc_now  # noqa: E402
from progress import compute_progress, write_progress  # noqa: E402


def running_jobs() -> list[dict]:
    jobs = []
    for pid_file in sorted(path("state").glob("*.pid")):
        try:
            pid = int(pid_file.read_text().strip())
        except (ValueError, OSError):
            continue
        alive = False
        try:
            os.kill(pid, 0)
            alive = True
        except OSError:
            alive = False
        if not alive:
            continue
        etime = ""
        try:
            proc = subprocess.run(
                ["ps", "-o", "etime=", "-p", str(pid)], text=True, capture_output=True, timeout=3
            )
            etime = proc.stdout.strip()
        except Exception:
            pass
        jobs.append(
            {
                "name": pid_file.stem,
                "pid": pid,
                "etime": etime,
                "log": f"logs/{pid_file.stem}.log",
            }
        )
    return jobs


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", default=None)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--reconcile", action="store_true", help="rewrite state/progress.json")
    args = ap.parse_args()

    cfg = load_config(args.config)
    if not path(cfg["manifest"]).exists():
        print("No manifest yet. Run: python3 scripts/prepare.py")
        return 1

    progress = compute_progress(cfg)
    if args.reconcile:
        write_progress(cfg)

    backup = read_json(path("state") / "backup.json", {}) or {}
    jobs = running_jobs()

    if args.json:
        print(json.dumps({"progress": progress, "backup": backup, "jobs": jobs}, ensure_ascii=False, indent=2))
        return 0

    total = progress["abc_ok"]
    labeled = progress["labeled"]
    pct = (100.0 * labeled / total) if total else 0.0
    print(f"run: {progress['run_id']}   (maqam-analysis pipeline {progress.get('pipeline_version', '')})".rstrip())
    print(
        f"labels: {labeled}/{total} ({pct:.1f}%)   remaining: {progress['remaining']}   "
        f"needs human review: {progress['needs_human_review']}"
    )
    print(
        f"pipeline: prepared {progress['prepared']}/{total} | analyzed {progress['analyzed']}/{total} | "
        f"parse<95% {progress['parse_low']} | stale labels {len(progress['stale_labels'])}"
    )
    print(
        f"ABC gaps: {progress['no_abc']} no_abc | {progress['missing_transcript']} missing transcript"
    )
    conf = progress["confidence"]
    mstat = progress["maqam_status"]
    print(
        "confidence: "
        + " | ".join(f"{k} {conf.get(k, 0)}" for k in ("high", "medium", "low", "unknown"))
        + "   withheld: "
        + str(mstat.get("withheld", 0))
    )
    if progress["maqam_counts"]:
        top = list(progress["maqam_counts"].items())[:8]
        print("top maqamat: " + ", ".join(f"{k} {v}" for k, v in top))
    last = progress.get("last_label")
    if last:
        print(
            f"last label: {last['track_id']} -> {last.get('maqam') or '(withheld)'} "
            f"at {last.get('reviewed_at')}"
        )
    print(f"next batch: {progress['next_batch']:03d} (size from config.labeling.batch_size)")

    gcs = backup.get("last_gcs") or {}
    git = backup.get("last_git") or {}
    print(
        "backup: "
        f"GCS {'ok ' + str(gcs.get('at')) if gcs.get('ok') else 'not yet'} | "
        f"git {(git.get('commit') or '-')[:8]} {'pushed' if git.get('pushed') else 'not pushed'}"
        + (f" at {git.get('at')}" if git.get('at') else "")
    )
    if jobs:
        print("jobs: " + "; ".join(f"{j['name']} pid {j['pid']} ({j['etime']}) log {j['log']}" for j in jobs))
    else:
        print("jobs: none running")

    if progress["stale_labels"]:
        print("STALE LABELS (evidence changed): " + ", ".join(progress["stale_labels"][:5]))
    if progress["no_abc_tracks"]:
        print("no_abc tracks: " + ", ".join(t["track_id"] for t in progress["no_abc_tracks"]))
    print("")
    print("next: python3 scripts/review.py packet --limit 8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

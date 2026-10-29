#!/usr/bin/env python3
"""Recompute progress from the files on disk.

The manifest + labels + work/evidence are the source of truth. state/progress.json
is only a cache for fast status reads; it is always safe to rebuild.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (  # noqa: E402
    atomic_write_json,
    evidence_path,
    load_config,
    load_labels,
    load_manifest,
    path,
    read_json,
    utc_now,
)


def compute_progress(cfg: dict[str, Any]) -> dict[str, Any]:
    manifest = load_manifest(cfg)
    labels = load_labels(cfg)

    total = len(manifest)
    ok_rows = [r for r in manifest if r["status"] == "ok"]
    no_abc_rows = [r for r in manifest if r["status"] == "no_abc"]
    missing_rows = [r for r in manifest if r["status"] == "missing_transcript"]

    prepared = 0
    analyzed = 0
    parse_low = 0
    analyzed_ids: set[str] = set()
    for row in ok_rows:
        if row.get("abc_path") and path(row["abc_path"]).exists():
            prepared += 1
        ev = evidence_path(cfg, row["song_id"])
        if ev.exists():
            analyzed += 1
            analyzed_ids.add(row["song_id"])
            try:
                evidence = read_json(ev, {})
                if float((evidence.get("analyzer") or {}).get("bar_match_ratio") or 1.0) < 0.95:
                    parse_low += 1
            except Exception:
                pass

    labeled_rows = [r for r in manifest if r["song_id"] in labels]
    confidence = {"high": 0, "medium": 0, "low": 0, "unknown": 0}
    status_counts: dict[str, int] = {}
    maqam_counts: dict[str, int] = {}
    flag_counts: dict[str, int] = {}
    needs_review = 0
    stale = []
    for row in labeled_rows:
        label = labels[row["song_id"]]
        lab = label.get("label") or {}
        conf = lab.get("overall_confidence") or "unknown"
        confidence[conf] = confidence.get(conf, 0) + 1
        mstatus = lab.get("maqam_status") or "unknown"
        status_counts[mstatus] = status_counts.get(mstatus, 0) + 1
        maqam = lab.get("maqam") or "(withheld)"
        maqam_counts[maqam] = maqam_counts.get(maqam, 0) + 1
        if (label.get("review") or {}).get("needs_human_review"):
            needs_review += 1
        for flag in (label.get("evidence") or {}).get("primary", {}).get("flags", []):
            key = flag.split(":")[0].split("->")[0].strip()[:80]
            flag_counts[key] = flag_counts.get(key, 0) + 1
        ev = evidence_path(cfg, row["song_id"])
        if ev.exists():
            current = (read_json(ev, {}) or {}).get("evidence_sha256")
            recorded = (label.get("evidence") or {}).get("evidence_sha256")
            if current and recorded and current != recorded:
                stale.append(row["song_id"])

    last_label = None
    if labeled_rows:
        def reviewed_at(r):
            lab = labels[r["song_id"]]
            return (lab.get("review") or {}).get("reviewed_at") or ""

        last = max(labeled_rows, key=reviewed_at)
        last_label = {
            "song_id": last["song_id"],
            "track_id": last["track_id"],
            "reviewed_at": reviewed_at(last),
            "maqam": (labels[last["song_id"]].get("label") or {}).get("maqam"),
        }

    batch_files = sorted(
        p for p in path("work/review").glob("batch-*.json") if not p.name.endswith(".labels.json")
    )
    batch_ids = [p.stem.replace("batch-", "") for p in batch_files]
    next_batch = 1
    if batch_ids:
        try:
            next_batch = max(int(b) for b in batch_ids) + 1
        except ValueError:
            next_batch = len(batch_files) + 1

    remaining = len(ok_rows) - len(labeled_rows)
    run_state = read_json(path("state") / "run.json", {}) or {}
    return {
        "run_id": cfg["run_id"],
        "pipeline_version": run_state.get("pipeline_version", ""),
        "updated_at": utc_now(),
        "total": total,
        "abc_ok": len(ok_rows),
        "no_abc": len(no_abc_rows),
        "missing_transcript": len(missing_rows),
        "prepared": prepared,
        "analyzed": analyzed,
        "labeled": len(labeled_rows),
        "remaining": remaining,
        "needs_human_review": needs_review,
        "parse_low": parse_low,
        "stale_labels": stale,
        "confidence": confidence,
        "maqam_status": status_counts,
        "maqam_counts": dict(sorted(maqam_counts.items(), key=lambda kv: (-kv[1], kv[0]))),
        "flag_counts": dict(sorted(flag_counts.items(), key=lambda kv: (-kv[1], kv[0]))),
        "last_label": last_label,
        "next_batch": next_batch,
        "no_abc_tracks": [
            {"song_id": r["song_id"], "track_id": r["track_id"], "reason": r["status_reason"]}
            for r in no_abc_rows
        ],
        "missing_tracks": [
            {"song_id": r["song_id"], "track_id": r["track_id"], "reason": r["status_reason"]}
            for r in missing_rows
        ],
    }


def write_progress(cfg: dict[str, Any]) -> dict[str, Any]:
    progress = compute_progress(cfg)
    atomic_write_json(path("state") / "progress.json", progress)
    return progress


if __name__ == "__main__":
    cfg = load_config()
    print(json.dumps(write_progress(cfg), ensure_ascii=False, indent=2))

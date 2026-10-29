#!/usr/bin/env python3
"""Export labels to CSV/JSONL plus an honest summary.

    python3 scripts/export_dataset.py
    python3 scripts/export_dataset.py --labeled-only
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (  # noqa: E402
    atomic_write_json,
    atomic_write_text,
    dumps_json,
    load_config,
    load_labels,
    load_manifest,
    normalize_text,
    path,
    utc_now,
)
from progress import compute_progress  # noqa: E402

CSV_FIELDS = [
    "song_id",
    "track_id",
    "artist",
    "album",
    "file",
    "lyric_title",
    "label_status",
    "maqam",
    "maqam_status",
    "tonic",
    "tonic_confidence",
    "scale_family",
    "overall_confidence",
    "alternatives",
    "tonic_alternatives",
    "ghammaz_candidate",
    "withheld_reason",
    "needs_human_review",
    "rationale",
    "parse_check",
    "flags",
    "abc_sha256",
    "model",
    "model_revision",
    "reviewed_at",
    "revision",
]


def row_from_label(row: dict[str, Any], label: dict[str, Any]) -> dict[str, Any]:
    lab = label.get("label") or {}
    ev = label.get("evidence") or {}
    src = label.get("source") or {}
    rev = label.get("review") or {}
    prov = label.get("provenance") or {}
    primary = ev.get("primary") or {}
    return {
        "song_id": row["song_id"],
        "track_id": row["track_id"],
        "artist": row["artist"],
        "album": row["album"],
        "file": row["file"],
        "lyric_title": row.get("lyric_title", ""),
        "label_status": "labeled",
        "maqam": lab.get("maqam") or "",
        "maqam_status": lab.get("maqam_status") or "",
        "tonic": lab.get("tonic") or "",
        "tonic_confidence": lab.get("tonic_confidence") or "",
        "scale_family": lab.get("scale_family") or "",
        "overall_confidence": lab.get("overall_confidence") or "",
        "alternatives": "; ".join(lab.get("alternatives") or []),
        "tonic_alternatives": "; ".join(lab.get("tonic_alternatives") or []),
        "ghammaz_candidate": lab.get("ghammaz_candidate") or "",
        "withheld_reason": lab.get("withheld_reason") or "",
        "needs_human_review": bool(lab.get("needs_human_review")),
        "rationale": lab.get("rationale") or "",
        "parse_check": ev.get("parse_check"),
        "flags": " | ".join(primary.get("flags") or []),
        "abc_sha256": src.get("abc_sha256") or "",
        "model": src.get("model") or "",
        "model_revision": src.get("model_revision") or "",
        "reviewed_at": rev.get("reviewed_at") or "",
        "revision": prov.get("revision") or "",
    }


def row_unlabeled(row: dict[str, Any], status: str) -> dict[str, Any]:
    return {
        "song_id": row["song_id"],
        "track_id": row["track_id"],
        "artist": row["artist"],
        "album": row["album"],
        "file": row["file"],
        "lyric_title": row.get("lyric_title", ""),
        "label_status": status,
        "maqam": "",
        "maqam_status": "",
        "tonic": "",
        "tonic_confidence": "",
        "scale_family": "",
        "overall_confidence": "",
        "alternatives": "",
        "tonic_alternatives": "",
        "ghammaz_candidate": "",
        "withheld_reason": "",
        "needs_human_review": "",
        "rationale": "",
        "parse_check": "",
        "flags": "",
        "abc_sha256": "",
        "model": "",
        "model_revision": "",
        "reviewed_at": "",
        "revision": "",
    }


def build_summary(rows: list[dict[str, Any]], progress: dict[str, Any]) -> dict[str, Any]:
    labeled = [r for r in rows if r["label_status"] == "labeled"]
    by_artist = Counter(r["artist"] for r in labeled)
    by_maqam = Counter((r["maqam"] or "(withheld)") for r in labeled)
    by_status = Counter(r["maqam_status"] for r in labeled)
    by_conf = Counter(r["overall_confidence"] for r in labeled)
    by_tonic_conf = Counter(r["tonic_confidence"] for r in labeled)
    by_album = Counter(r["album"] for r in labeled)

    # Duplicate groups (same normalized title) are useful for a consistency check.
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for r in labeled:
        key = normalize_text(r["lyric_title"] or Path(r["file"]).stem)
        groups[key].append(r)
    dup_groups = {k: v for k, v in groups.items() if len(v) > 1}
    dup_agreement = []
    for key, members in dup_groups.items():
        labels = {m["maqam"] or "(withheld)" for m in members}
        dup_agreement.append(
            {
                "title": key,
                "songs": [m["song_id"] for m in members],
                "labels": [m["maqam"] or "(withheld)" for m in members],
                "agree": len(labels) == 1,
            }
        )

    return {
        "generated_at": utc_now(),
        "run_id": progress.get("run_id"),
        "counts": {
            "total": len(rows),
            "labeled": len(labeled),
            "pending": sum(r["label_status"] == "pending" for r in rows),
            "no_abc": sum(r["label_status"] == "no_abc" for r in rows),
            "missing_transcript": sum(r["label_status"] == "missing_transcript" for r in rows),
            "needs_human_review": sum(bool(r["needs_human_review"]) for r in labeled),
        },
        "by_artist": dict(by_artist),
        "by_album": dict(sorted(by_album.items())),
        "by_maqam": dict(sorted(by_maqam.items(), key=lambda kv: (-kv[1], kv[0]))),
        "by_maqam_status": dict(by_status),
        "by_overall_confidence": dict(by_conf),
        "by_tonic_confidence": dict(by_tonic_conf),
        "duplicate_groups": dup_agreement,
        "caveats": [
            "Weak labels from SheetSage2 ABC scores. No ground truth exists for this corpus.",
            "ABC input is 12-TET, so quarter-tone maqamat can only be 'possible', never facts.",
            "Tonic confidence is a consistency measure between cues, not a probability.",
            "Four corpus tracks have no ABC and are exported with label_status=no_abc.",
            "Do not report accuracy without a blind re-review or human labels.",
        ],
    }


def write_summary_md(summary: dict[str, Any], out: Path) -> None:
    c = summary["counts"]
    lines = [
        "# Maqam label export",
        "",
        f"Generated: {summary['generated_at']}  |  run: `{summary['run_id']}`",
        "",
        "This is a **weak-label** dataset derived from SheetSage2 ABC transcriptions. "
        "It is not ground truth. Quarter-tone maqamat are marked `possible`, not stated as fact.",
        "",
        "## Counts",
        "",
        "| status | count |",
        "|---|---:|",
        f"| labeled | {c['labeled']} |",
        f"| pending | {c['pending']} |",
        f"| no ABC | {c['no_abc']} |",
        f"| missing transcript | {c['missing_transcript']} |",
        f"| needs human review | {c['needs_human_review']} |",
        "",
        "## Maqam distribution",
        "",
        "| maqam | count |",
        "|---|---:|",
    ]
    lines += [f"| {k} | {v} |" for k, v in summary["by_maqam"].items()]
    lines += [
        "",
        "## Confidence",
        "",
        "| overall confidence | count |",
        "|---|---:|",
    ]
    lines += [f"| {k or '(blank)'} | {v} |" for k, v in sorted(summary["by_overall_confidence"].items())]
    lines += [
        "",
        "## Caveats",
        "",
    ]
    lines += [f"- {x}" for x in summary["caveats"]]
    if summary["duplicate_groups"]:
        disagree = [g for g in summary["duplicate_groups"] if not g["agree"]]
        lines += [
            "",
            f"## Duplicate-title consistency",
            "",
            f"{len(summary['duplicate_groups'])} duplicate-title groups; "
            f"{len(disagree)} disagree. Disagreements are worth a human look.",
        ]
        for g in disagree[:10]:
            lines.append(f"- {g['title']}: {', '.join(g['labels'])}")
    atomic_write_text(out, "\n".join(lines) + "\n")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", default=None)
    ap.add_argument("--labeled-only", action="store_true")
    ap.add_argument("--out-dir", default=None)
    args = ap.parse_args()

    cfg = load_config(args.config)
    manifest = load_manifest(cfg)
    labels = load_labels(cfg)
    out_dir = path(args.out_dir or cfg.get("export", {}).get("dir", "exports"))
    out_dir.mkdir(parents=True, exist_ok=True)

    rows = []
    json_rows = []
    for row in manifest:
        label = labels.get(row["song_id"])
        if label:
            r = row_from_label(row, label)
            rows.append(r)
            json_rows.append(label)
        elif args.labeled_only:
            continue
        else:
            status = "no_abc" if row["status"] == "no_abc" else (
                "missing_transcript" if row["status"] == "missing_transcript" else "pending"
            )
            r = row_unlabeled(row, status)
            rows.append(r)
            json_rows.append(
                {
                    "song_id": row["song_id"],
                    "track_id": row["track_id"],
                    "artist": row["artist"],
                    "album": row["album"],
                    "file": row["file"],
                    "lyric_title": row.get("lyric_title", ""),
                    "label_status": status,
                    "status_reason": row.get("status_reason", ""),
                }
            )

    csv_path = out_dir / "maqam_labels.csv"
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows({k: r.get(k, "") for k in CSV_FIELDS} for r in rows)
    jsonl_path = out_dir / "maqam_labels.jsonl"
    atomic_write_text(jsonl_path, "".join(dumps_json(r) for r in json_rows))

    progress = compute_progress(cfg)
    summary = build_summary(rows, progress)
    atomic_write_json(out_dir / "summary.json", summary)
    write_summary_md(summary, out_dir / "SUMMARY.md")

    print(f"wrote {csv_path} ({len(rows)} rows)")
    print(f"wrote {jsonl_path}")
    print(f"wrote {out_dir / 'summary.json'}")
    print(f"wrote {out_dir / 'SUMMARY.md'}")
    print(
        f"labeled {summary['counts']['labeled']}/{summary['counts']['total']} | "
        f"withheld {summary['by_maqam_status'].get('withheld', 0)} | "
        f"needs human review {summary['counts']['needs_human_review']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

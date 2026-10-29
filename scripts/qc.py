#!/usr/bin/env python3
"""Blind re-review agreement (the only quality signal without ground truth).

    python3 scripts/review.py packet --qc --limit 20
    # agent fills work/qc/qc-001.labels.json without looking at labels/
    python3 scripts/review.py record --qc --batch work/qc/qc-001.json \
        --labels work/qc/qc-001.labels.json
    python3 scripts/qc.py compare
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import atomic_write_json, atomic_write_text, load_config, load_labels, path, utc_now  # noqa: E402


def read_qc_labels() -> dict[str, dict[str, Any]]:
    out = {}
    qc_dir = path("qc/labels")
    if not qc_dir.exists():
        return out
    for p in sorted(qc_dir.glob("*.json")):
        try:
            obj = json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        if isinstance(obj, dict) and obj.get("song_id"):
            out[obj["song_id"]] = obj
    return out


def compare(cfg: dict[str, Any] | None = None) -> dict[str, Any]:
    main = load_labels(cfg or load_config())
    qc = read_qc_labels()
    common = sorted(set(main) & set(qc))
    if not common:
        return {"generated_at": utc_now(), "compared": 0, "error": "no QC labels found"}

    rows = []
    for sid in common:
        ml = (main[sid].get("label") or {})
        ql = (qc[sid].get("label") or {})
        m_maqam = ml.get("maqam") or "(withheld)"
        q_maqam = ql.get("maqam") or "(withheld)"
        m_tonic = ml.get("tonic")
        q_tonic = ql.get("tonic")
        rows.append(
            {
                "song_id": sid,
                "pass1_maqam": m_maqam,
                "pass2_maqam": q_maqam,
                "pass1_status": ml.get("maqam_status"),
                "pass2_status": ql.get("maqam_status"),
                "pass1_tonic": m_tonic,
                "pass2_tonic": q_tonic,
                "pass1_confidence": ml.get("overall_confidence"),
                "maqam_agree": m_maqam == q_maqam,
                "status_agree": ml.get("maqam_status") == ql.get("maqam_status"),
                "tonic_agree": m_tonic == q_tonic,
                "coarse_agree": (m_maqam == "(withheld)") == (q_maqam == "(withheld)")
                or m_maqam == q_maqam,
            }
        )

    by_conf: dict[str, dict[str, Any]] = {}
    for conf in ("low", "medium", "high"):
        subset = [r for r in rows if (r.get("pass1_confidence") or "low") == conf]
        if not subset:
            continue
        by_conf[conf] = {
            "n": len(subset),
            "maqam_agree": sum(r["maqam_agree"] for r in subset),
            "tonic_agree": sum(r["tonic_agree"] for r in subset),
            "coarse_agree": sum(r["coarse_agree"] for r in subset),
        }

    return {
        "generated_at": utc_now(),
        "compared": len(rows),
        "maqam_agreement": sum(r["maqam_agree"] for r in rows) / len(rows),
        "status_agreement": sum(r["status_agree"] for r in rows) / len(rows),
        "tonic_agreement": sum(r["tonic_agree"] for r in rows) / len(rows),
        "coarse_agreement": sum(r["coarse_agree"] for r in rows) / len(rows),
        "by_pass1_confidence": by_conf,
        "rows": rows,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", nargs="?", default="compare", choices=["compare"])
    ap.add_argument("--config", default=None)
    ap.add_argument("--out-dir", default=None)
    args = ap.parse_args()

    cfg = load_config(args.config)
    result = compare(cfg)
    out_dir = path(args.out_dir or cfg.get("export", {}).get("dir", "exports"))
    out_dir.mkdir(parents=True, exist_ok=True)
    atomic_write_json(out_dir / "qc_report.json", result)
    if result.get("error"):
        print(result["error"])
        return 1

    lines = [
        "# Blind QC agreement",
        "",
        f"Compared {result['compared']} songs. Agreement is **not accuracy**: there is no ground truth.",
        "",
        "| measure | agreement |",
        "|---|---:|",
        f"| maqam (exact, withheld counts as a value) | {100 * result['maqam_agreement']:.1f}% |",
        f"| maqam_status | {100 * result['status_agreement']:.1f}% |",
        f"| tonic | {100 * result['tonic_agreement']:.1f}% |",
        f"| coarse (both named vs both withheld) | {100 * result['coarse_agreement']:.1f}% |",
        "",
        "## By pass-1 confidence",
        "",
        "| confidence | n | maqam | tonic | coarse |",
        "|---|---:|---:|---:|---:|",
    ]
    for conf, s in result["by_pass1_confidence"].items():
        lines.append(
            f"| {conf} | {s['n']} | {100 * s['maqam_agree'] / s['n']:.0f}% | "
            f"{100 * s['tonic_agree'] / s['n']:.0f}% | {100 * s['coarse_agree'] / s['n']:.0f}% |"
        )
    lines += ["", "## Disagreements", "", "| song | pass 1 | pass 2 |", "|---|---|---|"]
    for r in result["rows"]:
        if not r["maqam_agree"]:
            lines.append(f"| {r['song_id']} | {r['pass1_maqam']} | {r['pass2_maqam']} |")
    atomic_write_text(out_dir / "qc_report.md", "\n".join(lines) + "\n")
    print(f"compared {result['compared']} songs")
    print(f"maqam agreement {100 * result['maqam_agreement']:.1f}% | tonic {100 * result['tonic_agreement']:.1f}%")
    print(f"wrote {out_dir / 'qc_report.json'} and {out_dir / 'qc_report.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

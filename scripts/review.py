#!/usr/bin/env python3
"""Agent review loop: make a compact packet, validate labels, record them.

    python3 scripts/review.py packet --limit 8
    # agent edits work/review/batch-006.labels.json
    python3 scripts/review.py validate --batch work/review/batch-006.json \
        --labels work/review/batch-006.labels.json
    python3 scripts/review.py record --batch work/review/batch-006.json \
        --labels work/review/batch-006.labels.json --revise --reason "..."

`packet --qc` builds a blind re-review packet from already-labeled songs.
"""
from __future__ import annotations

import argparse
import json
import random
import subprocess
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (  # noqa: E402
    ROOT,
    atomic_write_json,
    atomic_write_text,
    evidence_path,
    gcs_cp,
    load_config,
    load_labels,
    load_manifest,
    object_hash,
    path,
    read_json,
    sha256_file,
    utc_now,
)
from labels import (  # noqa: E402
    CONF_RANK,
    MAQAMAT,
    build_label,
    canonical_maqam,
    validate_input,
)
from progress import compute_progress, write_progress  # noqa: E402

SKILL_MD = ROOT / "skills" / "maqam-analysis" / "SKILL.md"
SKILL_HASH = sha256_file(SKILL_MD) if SKILL_MD.exists() else ""


# ------------------------------------------------------------------------- format
def _qn(value: float | int | None) -> str:
    return f"{float(value or 0):.0f} qn"


def format_primary(ev: dict[str, Any]) -> list[str]:
    p = ev.get("primary") or {}
    lines = []
    pcs = p.get("present_pcs") or []
    if pcs:
        top = ", ".join(f"{n} {100 * float(s):.0f}%" for n, s in pcs[:6])
        lines.append(f"- pitch classes: {top}")
    gh = p.get("ghammaz")
    gh_txt = ""
    if isinstance(gh, dict) and gh.get("note"):
        gh_txt = (
            f"{gh.get('note')} ({gh.get('interval_cents')}c, "
            f"{100 * float(gh.get('final_share') or 0):.0f}% of phrase endings)"
        )
    cues = p.get("cues") or {}
    cues_txt = "; ".join(f"{k} -> {v}" for k, v in cues.items())
    lines.append(
        f"- tonic: {p.get('tonic')} ({p.get('tonic_confidence')}, margin {p.get('tonic_margin')})"
        + (f" | cues: {cues_txt}" if cues_txt else "")
    )
    shadow = p.get("shadow_of") or []
    tied = p.get("tied_shapes") or []
    lines.append(
        f"- scale: {p.get('scale_shape')}"
        + (f" [{p.get('scale_western')}]" if p.get("scale_western") else "")
        + f" (fit {p.get('fit')}, shape confidence {p.get('shape_confidence')}, "
        f"name_allowed={p.get('name_allowed')})"
        + (f" | tied: {', '.join(tied)}" if tied else "")
        + (f" | 12-TET shadow of: {', '.join(shadow)}" if shadow else "")
    )
    if gh_txt:
        lines.append(f"- candidate ghammaz: {gh_txt}")
    flags = p.get("flags") or []
    if flags:
        lines.append("- flags: " + " | ".join(flags))
    return lines


def format_sections(ev: dict[str, Any]) -> list[str]:
    out = []
    for sec in ev.get("sections") or []:
        if float(sec.get("total_dur") or 0) < 24:
            continue
        flag = (sec.get("flags") or [None])[0]
        out.append(
            f"  - {sec.get('label')}: {sec.get('tonic')} {sec.get('tonic_confidence')} / "
            f"{sec.get('scale_shape')} {sec.get('shape_confidence')} (fit {sec.get('fit')})"
            + (f"  [!] {flag}" if flag else "")
        )
    return out[:6]


def format_song(idx: int, row: dict[str, Any], ev: dict[str, Any]) -> str:
    meta = read_json(path("work") / row["song_id"] / "meta.json", {}) or {}
    report = ev.get("report") or {}
    lines = [
        f"## {idx}. `{row['song_id']}` — {row['artist']} — {row['album']} — \"{row.get('lyric_title') or row['file']}\"",
        f"- file: `{row['file']}` | duration {row.get('duration_s')}s | declared key {row.get('declared_key')} "
        f"| tempo {row.get('tempo_bpm')} | voice {(ev.get('analyzer') or {}).get('voice_analysed') or 'auto'}",
        f"- parse: {100 * float((ev.get('analyzer') or {}).get('bar_match_ratio') or 0):.0f}% of bars"
        + (f" | warnings: {'; '.join(report.get('warnings') or [])}" if report.get("warnings") else ""),
    ]
    lines += format_primary(ev)
    secs = format_sections(ev)
    if secs:
        lines.append("- sections:")
        lines += secs
    mv = ev.get("melody_variant") or {}
    mvp = mv.get("primary") or {}
    if mvp:
        lines.append(
            f"- melody-only cross-check (chords removed): {mvp.get('tonic')} {mvp.get('tonic_confidence')} / "
            f"{mvp.get('scale_shape')} {mvp.get('shape_confidence')} (fit {mvp.get('fit')})"
        )
    lines.append(f"- full report: `work/{row['song_id']}/report.md`")
    return "\n".join(lines)


# -------------------------------------------------------------------------- packet
def select_pending(cfg, manifest, labels, limit, order):
    pending = [
        r
        for r in manifest
        if r["status"] == "ok"
        and r["song_id"] not in labels
        and evidence_path(cfg, r["song_id"]).exists()
    ]
    if order == "uncertainty":
        def key(r):
            ev = read_json(evidence_path(cfg, r["song_id"]), {}) or {}
            p = ev.get("primary") or {}
            return (
                CONF_RANK.get((p.get("tonic_confidence") or "low").lower(), -1),
                CONF_RANK.get((p.get("shape_confidence") or "low").lower(), -1),
                -len(p.get("flags") or []),
                r["song_id"],
            )
        pending.sort(key=key)
    return pending[:limit]


def select_qc(manifest, labels, limit, seed):
    labeled = [r for r in manifest if r["song_id"] in labels]
    if not labeled:
        return []
    rng = random.Random(seed)
    # Stratify by overall confidence where possible.
    buckets: dict[str, list] = {"low": [], "medium": [], "high": []}
    for r in labeled:
        conf = (labels[r["song_id"]].get("label") or {}).get("overall_confidence") or "low"
        buckets.setdefault(conf, []).append(r)
    for b in buckets.values():
        rng.shuffle(b)
    out = []
    order = ["low", "medium", "high"]
    while len(out) < limit and any(buckets[k] for k in order):
        for k in order:
            if buckets.get(k):
                out.append(buckets[k].pop())
                if len(out) >= limit:
                    break
    return out


def cmd_packet(args) -> int:
    cfg = load_config(args.config)
    manifest = load_manifest(cfg)
    labels = load_labels(cfg)
    qc = args.qc
    limit = args.limit or int(cfg["labeling"].get("batch_size", 8))

    if qc:
        rows = select_qc(manifest, labels, limit, args.seed)
        batch_id = args.batch_id or f"qc-{len(list(path('work/qc').glob('qc-*.json'))) + 1:03d}"
        out_dir = path("work/qc")
    else:
        rows = select_pending(cfg, manifest, labels, limit, args.order)
        batch_id = args.batch_id or f"batch-{int(compute_progress(cfg)['next_batch']):03d}"
        out_dir = path("work/review")
    out_dir.mkdir(parents=True, exist_ok=True)
    if not rows:
        prog = compute_progress(cfg)
        if qc:
            print("nothing to QC: no main labels yet.")
        elif prog.get("analyzed", 0) < prog.get("abc_ok", 0):
            print("no reviewable evidence yet. Run: bash scripts/ops.sh prepare")
        else:
            print("nothing to review: every usable song already has a label.")
            print("next: bash scripts/ops.sh export")
        return 0

    sections = []
    template_labels = []
    evidence_hashes = {}
    for i, row in enumerate(rows, 1):
        ev = read_json(evidence_path(cfg, row["song_id"]), {}) or {}
        evidence_hashes[row["song_id"]] = ev.get("evidence_sha256", "")
        sections.append(format_song(i, row, ev))
        p = ev.get("primary") or {}
        gh = p.get("ghammaz")
        template_labels.append(
            {
                "song_id": row["song_id"],
                "maqam": None,
                "maqam_status": "withheld",
                "tonic": p.get("tonic"),
                "tonic_confidence": p.get("tonic_confidence") or "low",
                "tonic_alternatives": [],
                "scale_family": p.get("scale_western") or "",
                "overall_confidence": "low",
                "alternatives": [],
                "ghammaz_candidate": gh.get("note") if isinstance(gh, dict) else None,
                "withheld_reason": "",
                "rationale": "",
                "needs_human_review": True,
                "override_reason": None,
            }
        )

    batch_meta = {
        "batch_id": batch_id,
        "kind": "qc" if qc else "label",
        "created_at": utc_now(),
        "song_ids": [r["song_id"] for r in rows],
        "evidence_sha256": evidence_hashes,
        "packet": f"{out_dir.relative_to(ROOT)}/{batch_id}.md",
        "labels_template": f"{out_dir.relative_to(ROOT)}/{batch_id}.labels.json",
    }
    header = [
        f"# Maqam review — {batch_id} ({len(rows)} songs)",
        "",
        "Read `skills/maqam-analysis/SKILL.md` before deciding. Hard rules:",
        "- 12-TET ABC cannot prove quarter tones. Quarter-tone maqamat "
        "(Rast, Bayati, Saba, Sikah, Huzam, Iraq, Awj Ara, Suznek, Jiharkah, Bastanikar) "
        "are status `possible`, never `consistent`.",
        "- If the analyzer says `name_allowed=false`, a scale is not identified, "
        "parse <95%, or pitch classes are too few: use `maqam_status=\"withheld\"`.",
        "- Confidence can be lowered, never raised above the tool's evidence.",
        "- A tonic/dominant split must name the other tonic in `tonic_alternatives`.",
        "- Never import outside knowledge of the song. Evidence is the ABC only.",
        "",
        "Fill the sibling template, then run:",
        f"```bash",
        f"python3 scripts/review.py record --batch {out_dir.relative_to(ROOT)}/{batch_id}.json \\",
        f"  --labels {out_dir.relative_to(ROOT)}/{batch_id}.labels.json",
        f"```",
        "",
    ]
    packet = "\n".join(header + sections) + "\n"
    template = {
        "_instructions": (
            "Set maqam_status to consistent|possible|withheld. "
            "Use null maqam + a withheld_reason when withholding. "
            "Keep rationale to 2-4 sentences. Do not edit song_id."
        ),
        "batch_id": batch_id,
        "labels": template_labels,
    }
    atomic_write_text(out_dir / f"{batch_id}.md", packet)
    atomic_write_json(out_dir / f"{batch_id}.json", batch_meta)
    atomic_write_json(out_dir / f"{batch_id}.labels.json", template)

    print(f"packet: {out_dir.relative_to(ROOT)}/{batch_id}.md")
    print(f"template: {out_dir.relative_to(ROOT)}/{batch_id}.labels.json")
    print(f"songs: {', '.join(r['song_id'] for r in rows)}")
    print(f"next: edit the template, then run review.py record --batch ... --labels ...")
    return 0


# ------------------------------------------------------------------------- record
def cmd_validate_or_record(args, record: bool) -> int:
    cfg = load_config(args.config)
    manifest = {r["song_id"]: r for r in load_manifest(cfg)}
    batch = read_json(args.batch, None)
    if not isinstance(batch, dict):
        raise SystemExit(f"batch file not found or invalid: {args.batch}")
    payload = read_json(args.labels, None)
    if not isinstance(payload, dict) or not isinstance(payload.get("labels"), list):
        raise SystemExit(f"labels file must be a JSON object with a 'labels' array: {args.labels}")

    batch_ids = list(batch.get("song_ids") or [])
    raw_labels = payload["labels"]
    by_id = {}
    duplicate_ids = []
    for raw in raw_labels:
        sid = raw.get("song_id")
        if sid in by_id:
            duplicate_ids.append(sid)
        by_id[sid] = raw
    unknown = [sid for sid in by_id if sid not in batch_ids]
    missing = [sid for sid in batch_ids if sid not in by_id]
    errors_all: list[str] = []
    if duplicate_ids:
        errors_all.append(f"duplicate song_id in labels file: {duplicate_ids}")
    if unknown:
        errors_all.append(f"labels contain song_ids not in this batch: {unknown}")
    if missing and not args.allow_subset:
        errors_all.append(f"missing labels for: {missing} (use --allow-subset to accept a partial batch)")

    prepared: list[tuple[dict, dict, dict]] = []
    warnings_all: list[str] = []
    for sid in batch_ids:
        raw = by_id.get(sid)
        if raw is None:
            continue
        row = manifest.get(sid)
        if row is None:
            errors_all.append(f"{sid}: not in manifest")
            continue
        ev_file = evidence_path(cfg, sid)
        ev = read_json(ev_file, None)
        if not isinstance(ev, dict):
            errors_all.append(f"{sid}: evidence.json missing; run prepare")
            continue
        normalized, errors, warnings = validate_input(raw, row, ev, batch_id=batch["batch_id"])
        for e in errors:
            errors_all.append(f"{sid}: {e}")
        warnings_all += [f"{sid}: {w}" for w in warnings]
        if not errors:
            meta = read_json(path("work") / sid / "meta.json", {}) or {}
            prepared.append((row, ev, {"normalized": normalized, "meta": meta}))

    for w in warnings_all:
        print(f"WARNING: {w}")
    if errors_all:
        print(f"\n{len(errors_all)} validation error(s):", file=sys.stderr)
        for e in errors_all:
            print(f"  - {e}", file=sys.stderr)
        return 2
    if not record:
        print(f"OK: {len(prepared)} labels valid for {batch['batch_id']}")
        return 0

    # Validate revisions before writing anything. QC labels live in a separate
    # directory, so the main labels do not count as "already labeled" there.
    qc = bool(args.qc) or batch.get("kind") == "qc"
    existing = {} if qc else load_labels(cfg)
    for row, ev, pack in prepared:
        sid = row["song_id"]
        if sid in existing and not args.revise:
            errors_all.append(f"{sid}: already labeled; use --revise --reason '...' to replace it")
        if sid in existing and args.revise and not (args.reason or "").strip():
            errors_all.append(f"{sid}: --revise needs --reason")
    if errors_all:
        print(f"\n{len(errors_all)} error(s), nothing written:", file=sys.stderr)
        for e in errors_all:
            print(f"  - {e}", file=sys.stderr)
        return 2

    out_dir = path("qc/labels") if qc else path("labels")
    out_dir.mkdir(parents=True, exist_ok=True)
    recorded = []
    for row, ev, pack in prepared:
        sid = row["song_id"]
        previous = existing.get(sid)
        if previous and args.revise:
            hist = path("labels/_history") / sid
            hist.mkdir(parents=True, exist_ok=True)
            rev = (previous.get("provenance") or {}).get("revision", 1)
            atomic_write_text(hist / f"rev-{rev:03d}-{utc_now().replace(':','').replace('-','')}.json",
                              json.dumps(previous, ensure_ascii=False, indent=2) + "\n")
        label = build_label(
            cfg,
            row,
            ev,
            pack["normalized"],
            pack["meta"],
            reviewed_by=args.reviewed_by,
            skill_sha256=SKILL_HASH,
            previous=previous if args.revise else None,
            revision_reason=args.reason if args.revise else None,
        )
        target = out_dir / f"{sid}.json"
        atomic_write_json(target, label)
        atomic_write_json(path("work") / sid / "label.json", label)
        recorded.append((sid, target, label))

    remote_subdir = "qc/labels" if qc else "labels"
    for sid, target, label in recorded:
        try:
            from common import ledger_event
            ledger_event(
                cfg,
                "qc_label_recorded" if qc else "label_recorded",
                song_id=sid,
                batch_id=batch["batch_id"],
                revision=(label.get("provenance") or {}).get("revision"),
                label_sha256=object_hash(label),
                evidence_sha256=(label.get("evidence") or {}).get("evidence_sha256"),
                maqam=(label.get("label") or {}).get("maqam"),
                status=(label.get("label") or {}).get("maqam_status"),
            )
        except Exception as exc:
            print(f"WARNING: ledger append failed for {sid}: {exc}", file=sys.stderr)
        if cfg.get("backup", {}).get("auto_upload_labels", True) and not args.no_backup:
            try:
                gcs_cp(
                    str(target),
                    f"{cfg['backup']['gcs_prefix'].rstrip('/')}/{remote_subdir}/{sid}.json",
                    timeout=120,
                )
            except Exception as exc:
                print(f"WARNING: GCS upload failed for {sid}: {exc}", file=sys.stderr)
    progress = write_progress(cfg) if not qc else None

    # Optional batch-level commit; per-label GCS upload already happened.
    # Default is off: the agent runs `ops.sh start backup` so the chat is not blocked.
    if args.backup and not args.no_backup and not qc:
        try:
            cmd = [sys.executable, str(ROOT / "scripts" / "backup.py"), "flush", "--quiet"]
            proc = subprocess.run(cmd, text=True, capture_output=True, timeout=300)
            if proc.returncode != 0:
                print(f"WARNING: batch backup failed:\n{proc.stderr.strip()}", file=sys.stderr)
            else:
                print("backup: flushed")
        except Exception as exc:
            print(f"WARNING: batch backup failed: {exc}", file=sys.stderr)

    print(f"recorded {len(recorded)} labels in {batch['batch_id']}" + (" (QC pass)" if qc else ""))
    for sid, target, label in recorded:
        lab = label.get("label") or {}
        print(
            f"  {sid}: {lab.get('maqam') or '(withheld)'} [{lab.get('maqam_status')}] "
            f"tonic {lab.get('tonic')} ({lab.get('tonic_confidence')}) "
            f"overall {lab.get('overall_confidence')}"
        )
    if progress:
        print(f"progress: {progress['labeled']}/{progress['abc_ok']} labeled, {progress['remaining']} remaining")
        print("next: python3 scripts/review.py packet --limit 8")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", default=None)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("packet")
    p.add_argument("--limit", type=int, default=0)
    p.add_argument("--batch-id", default=None)
    p.add_argument("--order", choices=["manifest", "uncertainty"], default="manifest")
    p.add_argument("--qc", action="store_true", help="blind re-review of already-labeled songs")
    p.add_argument("--seed", type=int, default=7)
    p.set_defaults(func=cmd_packet)

    v = sub.add_parser("validate")
    v.add_argument("--batch", required=True)
    v.add_argument("--labels", required=True)
    v.add_argument("--allow-subset", action="store_true")
    v.set_defaults(func=lambda a: cmd_validate_or_record(a, False))

    r = sub.add_parser("record")
    r.add_argument("--batch", required=True)
    r.add_argument("--labels", required=True)
    r.add_argument("--revise", action="store_true")
    r.add_argument("--reason", default=None)
    r.add_argument("--reviewed-by", default="ai-agent")
    r.add_argument("--allow-subset", action="store_true")
    r.add_argument("--qc", action="store_true")
    r.add_argument("--backup", action="store_true", help="also flush GCS+git at the end of the batch")
    r.add_argument("--no-backup", action="store_true", help="skip per-label GCS upload too")
    r.add_argument("--dry-run", action="store_true")
    r.set_defaults(func=lambda a: cmd_validate_or_record(a, not a.dry_run))

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())

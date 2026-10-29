#!/usr/bin/env python3
"""Fetch the existing SheetSage2 album JSONs, build the manifest, extract ABCs,
and run the maqam-analysis skill's analyzer for every song.

    python3 scripts/prepare.py                 # normal run (idempotent)
    python3 scripts/prepare.py --refresh       # re-download the 23 album JSONs
    python3 scripts/prepare.py --force         # re-extract + re-analyze
    python3 scripts/prepare.py --limit 3       # smoke test
    python3 scripts/prepare.py --offline       # use cache/transcripts only

Nothing here labels a song. It only produces evidence under work/<song_id>/.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (  # noqa: E402
    PIPELINE_VERSION,
    ROOT,
    atomic_write_json,
    atomic_write_text,
    ensure_layout,
    gcs_cp,
    gcloud_available,
    load_config,
    make_song_id,
    normalize_text,
    object_hash,
    path,
    read_json,
    sha256_file,
    sha256_text,
    utc_now,
)

ANALYZER = ROOT / "skills" / "maqam-analysis" / "scripts" / "analyze_abc.py"
SKILL_MD = ROOT / "skills" / "maqam-analysis" / "SKILL.md"


# --------------------------------------------------------------------------- fetch
def fetch_transcripts(cfg: dict[str, Any], args: argparse.Namespace) -> Path:
    cache = path(cfg["transcripts"]["cache_dir"])
    cache.mkdir(parents=True, exist_ok=True)

    if args.transcripts_dir:
        src = Path(args.transcripts_dir)
        if not src.exists():
            raise SystemExit(f"--transcripts-dir not found: {src}")
        count = 0
        for f in sorted(src.glob("*.json")):
            data = read_json(f, {})
            if isinstance(data, dict) and data.get("tracks"):
                shutil.copy2(f, cache / f.name)
                count += 1
        print(f"[fetch] copied {count} album JSONs from {src} -> {cache}")
        return cache

    existing = []
    for p in cache.glob("*.json"):
        try:
            if isinstance(read_json(p, {}), dict):
                existing.append(p)
        except json.JSONDecodeError:
            print(f"WARNING: ignoring unreadable cache file {p}", file=sys.stderr)
    if args.offline:
        print(f"[fetch] offline: using {len(existing)} cached album JSONs")
        return cache
    if existing and not args.refresh:
        print(f"[fetch] {len(existing)} album JSONs already cached (use --refresh to re-download)")
        return cache
    if not gcloud_available():
        raise SystemExit(
            "gcloud not found. In Colab run `from google.colab import auth; auth.authenticate_user()` "
            "and install the SDK, or pass --transcripts-dir with a local copy."
        )

    prefix = cfg["transcripts"]["gcs_prefix"].rstrip("/")
    for code in sorted(set(cfg["transcripts"]["artists"].values())):
        uri = f"{prefix}/{code}/abc/*.json"
        print(f"[fetch] {uri}")
        gcs_cp(uri, str(cache) + "/", recursive=True, timeout=600)
    print(f"[fetch] {len(list(cache.glob('*.json')))} album JSONs in {cache}")
    return cache


# ------------------------------------------------------------------------ manifest
def load_album_json(cache: Path) -> tuple[dict, list[dict[str, Any]]]:
    """Return exact/normalized lookup maps and a flat index of all transcript tracks."""
    exact: dict[tuple[str, str, str], tuple[dict, dict]] = {}
    normalized: dict[tuple[str, str, str], tuple[dict, dict]] = {}
    index: list[dict[str, Any]] = []

    for p in sorted(cache.glob("*.json")):
        data = read_json(p, {})
        if not isinstance(data, dict) or not data.get("tracks"):
            continue
        artist = data.get("artist", "")
        album = data.get("album", "")
        for track in data["tracks"]:
            key = (artist, album, track.get("file", ""))
            if key in exact:
                print(f"WARNING: duplicate transcript row {key}; keeping the first", file=sys.stderr)
                continue
            exact[key] = (data, track)
            normalized[(normalize_text(artist), normalize_text(album), normalize_text(track.get("file", "")))] = (
                data,
                track,
            )
            index.append(
                {
                    "artist": artist,
                    "album": album,
                    "file": track.get("file", ""),
                    "track_id": track.get("track_id", ""),
                    "title": track.get("title", ""),
                    "track_no": track.get("track_no"),
                    "duration_s": track.get("duration_s"),
                    "transcribe_status": track.get("transcribe_status"),
                    "abc_chars": len(track.get("abc") or ""),
                    "abc_sha256": track.get("abc_sha256"),
                    "abc_melody_sha256": track.get("abc_melody_sha256"),
                    "declared_key": track.get("key"),
                    "tempo_bpm": track.get("tempo_bpm"),
                    "meters": track.get("meters"),
                    "sections": track.get("sections"),
                    "notes_vocal": track.get("notes_vocal"),
                    "notes_ins": track.get("notes_ins"),
                    "has_chords": track.get("has_chords"),
                    "duplicate_of": track.get("duplicate_of"),
                    "qc": track.get("qc"),
                    "audio_sha256": track.get("audio_sha256"),
                    "source_uri": track.get("source_uri"),
                    "album_json": p.name,
                }
            )
    return {"exact": exact, "normalized": normalized}, index


def lookup_track(maps: dict, code: str, album: str, file: str):
    hit = maps["exact"].get((code, album, file))
    if hit:
        return hit
    return maps["normalized"].get((normalize_text(code), normalize_text(album), normalize_text(file)))


def natural_key(row: dict[str, Any]):
    file_name = row.get("file", "")
    digits = "".join(ch for ch in file_name.split(".")[0] if ch.isdigit())
    return (row.get("artist", ""), row.get("album", ""), int(digits) if digits else 999, file_name)


def build_manifest(cfg: dict[str, Any], maps: dict, index: list[dict[str, Any]]) -> list[dict[str, Any]]:
    corpus = read_json(path(cfg["corpus"]), None)
    if not isinstance(corpus, list):
        raise SystemExit(f"corpus not found or not a list: {path(cfg['corpus'])}")
    artists = cfg["transcripts"]["artists"]
    prefix = cfg["transcripts"]["gcs_prefix"].rstrip("/")
    audio_prefix = cfg["audio"]["gcs_prefix"].rstrip("/")
    audio_root = cfg["audio"].get("root", "").rstrip("/")
    abc_dir = cfg["transcripts"]["abc_dir"]
    abc_melody_dir = cfg["transcripts"].get("abc_melody_dir", "data/abc_melody")

    rows: list[dict[str, Any]] = []
    for item in corpus:
        code = artists.get(item.get("artist", ""))
        if not code:
            raise SystemExit(f"unknown artist in corpus: {item.get('artist')!r}")
        hit = lookup_track(maps, code, item.get("album", ""), item.get("file", ""))
        row: dict[str, Any] = {
            "song_id": "",
            "track_id": item.get("track_id", ""),
            "artist": item.get("artist", ""),
            "album": item.get("album", ""),
            "file": item.get("file", ""),
            "lyric_title": item.get("lyric_title", ""),
            "transcript_artist": code,
            "transcript_album": item.get("album", ""),
            "transcript_file": item.get("file", ""),
            "transcript_track_id": "",
            "transcript_json": "",
            "transcript_sha256": "",
            "status": "missing_transcript",
            "status_reason": "",
            "abc_path": "",
            "abc_melody_path": "",
            "abc_sha256": "",
            "abc_melody_sha256": "",
            "abc_sha256_expected": "",
            "abc_chars": 0,
            "audio_uri": f"{audio_prefix}/{code}/{item.get('album','')}/{item.get('file','')}",
            "audio_local": f"{audio_root}/{code}/{item.get('album','')}/{item.get('file','')}" if audio_root else "",
            "declared_key": "",
            "tempo_bpm": None,
            "meters": [],
            "sections": [],
            "notes_vocal": None,
            "notes_ins": None,
            "has_chords": None,
            "duplicate_of": None,
            "qc": None,
            "duration_s": None,
            "audio_sha256": None,
        }
        if hit:
            album_obj, track = hit
            row.update(
                {
                    "transcript_album": album_obj.get("album", row["album"]),
                    "transcript_track_id": track.get("track_id", ""),
                    "transcript_json": f"{prefix}/{code}/abc/{album_obj.get('album','')}.json",
                    "transcript_sha256": sha256_file(
                        path(cfg["transcripts"]["cache_dir"]) / f"{album_obj.get('album','')}.json"
                    ),
                    "abc_sha256_expected": track.get("abc_sha256") or "",
                    "duration_s": track.get("duration_s"),
                    "declared_key": track.get("key") or "",
                    "tempo_bpm": track.get("tempo_bpm"),
                    "meters": track.get("meters") or [],
                    "sections": track.get("sections") or [],
                    "notes_vocal": track.get("notes_vocal"),
                    "notes_ins": track.get("notes_ins"),
                    "has_chords": track.get("has_chords"),
                    "duplicate_of": track.get("duplicate_of"),
                    "qc": track.get("qc"),
                    "audio_sha256": track.get("audio_sha256"),
                }
            )
            if track.get("transcribe_status") == "ok" and track.get("abc"):
                row["status"] = "ok"
                row["abc_chars"] = len(track["abc"])
                row["abc_sha256"] = track.get("abc_sha256") or sha256_text(track["abc"])
                row["abc_melody_sha256"] = track.get("abc_melody_sha256") or (
                    sha256_text(track["abc_melody"]) if track.get("abc_melody") else ""
                )
            else:
                row["status"] = "no_abc"
                row["status_reason"] = track.get("transcribe_status") or "no abc field"
        else:
            row["status_reason"] = "not found in transcript archive"
        rows.append(row)

    rows.sort(key=natural_key)

    used: set[str] = set()
    for row in rows:
        song_id = make_song_id(row, used)
        used.add(song_id)
        row["song_id"] = song_id
        if row["status"] == "ok":
            row["abc_path"] = f"{abc_dir}/{song_id}.abc"
            row["abc_melody_path"] = f"{abc_melody_dir}/{song_id}.abc"

    # Add in_corpus/song_id to the flat transcript index.
    by_key = {(r["transcript_artist"], r["transcript_album"], r["transcript_file"]): r for r in rows}
    for item in index:
        row = by_key.get((item["artist"], item["album"], item["file"]))
        item["in_corpus"] = bool(row)
        item["song_id"] = row["song_id"] if row else ""

    atomic_write_text(path(cfg["manifest"]), "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
    atomic_write_json(path(cfg["transcripts_index"]), {"generated_at": utc_now(), "rows": index})

    counts = {
        "total": len(rows),
        "ok": sum(r["status"] == "ok" for r in rows),
        "no_abc": sum(r["status"] == "no_abc" for r in rows),
        "missing_transcript": sum(r["status"] == "missing_transcript" for r in rows),
    }
    if counts["missing_transcript"]:
        missing = [r["track_id"] for r in rows if r["status"] == "missing_transcript"]
        raise SystemExit(
            f"[manifest] {len(missing)} corpus rows have no transcript row. "
            "The cache is probably partial; re-run with --refresh. Missing:\n  "
            + "\n  ".join(missing[:20])
        )
    print(
        f"[manifest] {counts['total']} corpus rows -> "
        f"{counts['ok']} ok, {counts['no_abc']} no_abc, {counts['missing_transcript']} missing_transcript"
    )
    if counts["no_abc"]:
        for r in rows:
            if r["status"] == "no_abc":
                print(f"  no_abc: {r['track_id']}  ({r['status_reason']})")
    write_run_state(cfg, counts)
    return rows


def write_run_state(cfg: dict[str, Any], counts: dict[str, int]) -> None:
    run_path = path("state") / "run.json"
    previous = read_json(run_path, {}) or {}
    skill_hash = sha256_file(SKILL_MD) if SKILL_MD.exists() else ""
    cfg_hash = object_hash({k: v for k, v in cfg.items() if not k.startswith("_")})
    config_path = Path(cfg["_config_path"])
    try:
        config_rel = str(config_path.resolve().relative_to(ROOT))
    except ValueError:
        config_rel = str(config_path)
    state = {
        "run_id": cfg["run_id"],
        "created_at": previous.get("created_at", utc_now()),
        "updated_at": utc_now(),
        "pipeline_version": PIPELINE_VERSION,
        "corpus": cfg["corpus"],
        "corpus_sha256": sha256_file(path(cfg["corpus"])),
        "config": config_rel,
        "config_sha256": cfg_hash,
        "skill_sha256": skill_hash,
        "skill_commit": previous.get("skill_commit", ""),
        **counts,
    }
    atomic_write_json(run_path, state)


# -------------------------------------------------------------------------- extract
def extract_one(cfg: dict[str, Any], row: dict[str, Any], force: bool = False) -> str:
    song_id = row["song_id"]
    work = path("work") / song_id
    work.mkdir(parents=True, exist_ok=True)
    if row["status"] != "ok":
        atomic_write_json(
            work / "meta.json",
            {
                "song_id": song_id,
                "track_id": row["track_id"],
                "status": row["status"],
                "reason": row["status_reason"],
                "recorded_at": utc_now(),
            },
        )
        return "skipped"

    album_json = path(cfg["transcripts"]["cache_dir"]) / f"{row['transcript_album']}.json"
    album_obj = read_json(album_json, {})
    track = None
    for candidate in album_obj.get("tracks", []):
        if candidate.get("track_id") == row["transcript_track_id"] or (
            candidate.get("file") == row["file"] and album_obj.get("album") == row["transcript_album"]
        ):
            track = candidate
            break
    if track is None:
        raise RuntimeError(f"track disappeared from {album_json}: {row['track_id']}")

    abc = track.get("abc") or ""
    abc_path = path(row["abc_path"])
    abc_hash = sha256_text(abc)
    if force or not abc_path.exists():
        atomic_write_text(abc_path, abc)
    elif sha256_file(abc_path) != abc_hash:
        atomic_write_text(abc_path, abc)

    melody = track.get("abc_melody") or ""
    melody_path = path(row["abc_melody_path"]) if row.get("abc_melody_path") else None
    melody_hash = sha256_text(melody) if melody else ""
    if melody_path and melody:
        if force or not melody_path.exists():
            atomic_write_text(melody_path, melody)
        elif sha256_file(melody_path) != melody_hash:
            atomic_write_text(melody_path, melody)

    expected = row.get("abc_sha256_expected") or ""
    hash_ok = (not expected) or (expected == abc_hash)
    meta = {
        "song_id": song_id,
        "track_id": row["track_id"],
        "status": "ok",
        "extracted_at": utc_now(),
        "abc_path": row["abc_path"],
        "abc_sha256": abc_hash,
        "abc_sha256_expected": expected,
        "abc_sha256_ok": hash_ok,
        "abc_melody_path": row.get("abc_melody_path", ""),
        "abc_melody_sha256": melody_hash,
        "transcript": {
            "json_uri": row["transcript_json"],
            "track_id": row["transcript_track_id"],
            "album": row["transcript_album"],
            "model": album_obj.get("model"),
            "model_revision": album_obj.get("model_revision"),
            "mode": album_obj.get("mode"),
            "status": track.get("transcribe_status"),
        },
        "audio": {"uri": row["audio_uri"], "sha256": row.get("audio_sha256")},
    }
    atomic_write_json(work / "meta.json", meta)
    if not hash_ok:
        print(f"WARNING: abc sha256 mismatch for {row['track_id']} (archive vs recomputed)", file=sys.stderr)
    return "extracted"


# ------------------------------------------------------------------------- analyze
def run_analyzer(abc_path: Path, voice: str, as_json: bool, min_dur: float, timeout: float):
    cmd = [sys.executable, str(ANALYZER), str(abc_path), "--min-dur", str(min_dur)]
    if voice:
        cmd += ["--voice", voice]
    if as_json:
        cmd.append("--json")
    proc = subprocess.run(cmd, text=True, capture_output=True, timeout=timeout)
    if proc.returncode != 0:
        # Fall back to the analyzer's automatic voice choice if the named voice is absent.
        if voice:
            cmd = [c for c in cmd if c not in ("--voice", voice)]
            proc = subprocess.run(cmd, text=True, capture_output=True, timeout=timeout)
    return proc


def summarize_group(g: dict[str, Any]) -> dict[str, Any]:
    hypotheses = g.get("hypotheses") or []
    hyp = hypotheses[0] if hypotheses else {}
    fits = hyp.get("fits") or []
    tied = [f for f in fits if f.get("tied_with_best")] or fits[:1]
    # Match the skill's display rule: prefer an exact 12-TET shape over a
    # quarter-tone shadow (Nahawand over Bayati, Kurd over Bayati, ...).
    exact = [f for f in tied if not f.get("has_quarter_tone")]
    top = exact[0] if exact else (tied[0] if tied else {})
    shadow = [f for f in tied if f.get("has_quarter_tone")]
    return {
        "label": g.get("label"),
        "section": g.get("section"),
        "microtonal_input": bool(g.get("microtonal_input")),
        "tonic": hyp.get("tonic"),
        "tonic_confidence": g.get("tonic_confidence"),
        "tonic_margin": round(float(g.get("tonic_margin") or 0.0), 3),
        "cues": {k: v.get("points_to") for k, v in (g.get("cues") or {}).items()},
        "scale_shape": top.get("label"),
        "scale_id": top.get("id"),
        "scale_western": top.get("west", ""),
        "fit": round(float(g.get("best_fit") or 0.0), 3),
        "shape_confidence": g.get("shape_confidence"),
        "name_allowed": bool(g.get("name_allowed")),
        "shadow_of": [f.get("label") for f in shadow],
        "tied_shapes": [f.get("label") for f in tied],
        "flags": g.get("flags") or [],
        "ghammaz": g.get("ghammaz"),
        "total_dur": round(float(g.get("total_dur") or 0.0), 1),
        "present_pcs": g.get("present_pcs") or [],
        "alt_tonics": g.get("alt_tonics") or [],
    }


def summarize_report(report: dict[str, Any]) -> dict[str, Any] | None:
    groups = report.get("groups") or []
    if not groups:
        return None
    primary = summarize_group(groups[0])
    return {
        "declared_key": report.get("declared_key"),
        "tempo": report.get("tempo"),
        "voice_analysed": report.get("voice_analysed"),
        "bar_match_ratio": report.get("bar_match_ratio"),
        "warnings": report.get("warnings") or [],
        "primary": primary,
    }


def analyze_one(cfg: dict[str, Any], row: dict[str, Any], force: bool = False) -> str:
    song_id = row["song_id"]
    work = path("work") / song_id
    ev_path = work / "evidence.json"
    if ev_path.exists() and not force:
        return "skipped"

    abc_path = path(row["abc_path"])
    if not abc_path.exists():
        return "missing_abc"
    voice = cfg["analysis"].get("voice", "Vocal")
    min_dur = cfg["analysis"].get("min_dur", 24)
    timeout = cfg["analysis"].get("timeout_seconds", 120)

    try:
        proc = run_analyzer(abc_path, voice, True, min_dur, timeout)
        if proc.returncode != 0:
            raise RuntimeError((proc.stderr or proc.stdout or "").strip()[:2000])
        report = json.loads(proc.stdout)
        if isinstance(report, list):
            report = report[0] if report else {}
        if not report.get("groups"):
            raise RuntimeError("analyzer returned no groups")
        md_proc = run_analyzer(abc_path, voice, False, min_dur, timeout)
        markdown = md_proc.stdout if md_proc.returncode == 0 else ""

        melody_report = None
        melody_path = path(row["abc_melody_path"]) if row.get("abc_melody_path") else None
        if cfg["analysis"].get("run_melody_variant", True) and melody_path and melody_path.exists():
            m_proc = run_analyzer(melody_path, voice, True, min_dur, timeout)
            if m_proc.returncode == 0:
                melody_report = json.loads(m_proc.stdout)
                if isinstance(melody_report, list):
                    melody_report = melody_report[0] if melody_report else None
                if melody_report:
                    atomic_write_json(work / "analysis_melody.json", melody_report)
    except Exception as exc:  # one bad ABC must not stop the batch
        atomic_write_json(
            work / "analysis_error.json",
            {"song_id": song_id, "track_id": row["track_id"], "error": str(exc), "failed_at": utc_now()},
        )
        return f"failed: {exc}"

    atomic_write_json(work / "analysis.json", report)
    if markdown:
        atomic_write_text(work / "report.md", markdown)

    evidence = {
        "schema_version": 1,
        "song_id": song_id,
        "track_id": row["track_id"],
        "abc_sha256": sha256_file(abc_path),
        "analyzed_at": utc_now(),
        "analyzer": {
            "skill": "maqam-analysis",
            "skill_sha256": sha256_file(SKILL_MD) if SKILL_MD.exists() else "",
            "script": "skills/maqam-analysis/scripts/analyze_abc.py",
            "voice_requested": voice,
            "voice_analysed": report.get("voice_analysed"),
            "bar_match_ratio": report.get("bar_match_ratio"),
        },
        "report": {
            "declared_key": report.get("declared_key"),
            "tempo": report.get("tempo"),
            "voices": report.get("voices"),
            "warnings": report.get("warnings") or [],
            "key_changes": report.get("key_changes") or [],
            "source": report.get("source"),
        },
        "primary": summarize_group(report["groups"][0]),
        "sections": [summarize_group(g) for g in report["groups"][1:]],
        "melody_variant": summarize_report(melody_report) if melody_report else None,
        "report_path": f"work/{song_id}/report.md",
    }
    evidence["evidence_sha256"] = object_hash(evidence)
    atomic_write_json(ev_path, evidence)
    return "analyzed"


# ---------------------------------------------------------------------------- main
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", default=None)
    ap.add_argument("--transcripts-dir", default=None, help="local directory of album JSONs (offline/testing)")
    ap.add_argument("--offline", action="store_true", help="do not call gcloud; use cache/transcripts")
    ap.add_argument("--refresh", action="store_true", help="re-download album JSONs even if cached")
    ap.add_argument("--force", action="store_true", help="re-extract ABCs and re-run analysis")
    ap.add_argument("--skip-analyze", action="store_true")
    ap.add_argument("--limit", type=int, default=0, help="process only the first N songs (smoke test)")
    ap.add_argument("--only-song-id", action="append", default=[])
    ap.add_argument("--fail-fast", action="store_true")
    args = ap.parse_args()

    cfg = load_config(args.config)
    ensure_layout(cfg)
    print(f"maqam-167 prepare | run_id={cfg['run_id']} | pipeline={PIPELINE_VERSION}")
    print(f"root={ROOT}")

    cache = fetch_transcripts(cfg, args)
    maps, index = load_album_json(cache)
    if not maps["exact"]:
        raise SystemExit(
            f"no album JSONs in {cache}. Run with network access, or pass --transcripts-dir."
        )
    rows = build_manifest(cfg, maps, index)
    if args.only_song_id:
        wanted = set(args.only_song_id)
        rows = [r for r in rows if r["song_id"] in wanted]
        if not rows:
            raise SystemExit(f"no manifest rows match --only-song-id {sorted(wanted)}")
    if args.limit:
        rows = rows[: args.limit]

    extracted = skipped = failed = 0
    for i, row in enumerate(rows, 1):
        try:
            result = extract_one(cfg, row, force=args.force)
        except Exception as exc:
            failed += 1
            print(f"[extract] FAILED {row['song_id']}: {exc}", file=sys.stderr)
            if args.fail_fast:
                raise
            continue
        if result == "extracted":
            extracted += 1
        else:
            skipped += 1
        if i % 25 == 0 or i == len(rows):
            print(f"[extract] {i}/{len(rows)} (extracted={extracted}, skipped={skipped}, failed={failed})")

    if not args.skip_analyze:
        analyzed = skipped_a = failed_a = 0
        for i, row in enumerate(rows, 1):
            if row["status"] != "ok":
                continue
            try:
                result = analyze_one(cfg, row, force=args.force)
            except Exception as exc:
                failed_a += 1
                print(f"[analyze] FAILED {row['song_id']}: {exc}", file=sys.stderr)
                if args.fail_fast:
                    raise
                continue
            if result == "analyzed":
                analyzed += 1
            elif result.startswith("failed"):
                failed_a += 1
            else:
                skipped_a += 1
            if i % 10 == 0 or i == len(rows):
                print(
                    f"[analyze] {i}/{len(rows)} "
                    f"(analyzed={analyzed}, skipped={skipped_a}, failed={failed_a})"
                )
        print(f"[analyze] done: {analyzed} new, {skipped_a} already present, {failed_a} failed")

    print("")
    print("Prepare complete. Next:")
    print("  python3 scripts/status.py")
    print("  python3 scripts/review.py packet --limit 8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

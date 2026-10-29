#!/usr/bin/env python3
"""Label schema, normalization and the skill's hard safety rules.

The agent supplies a small, human-friendly label object. This module enriches it
with provenance and refuses labels that contradict the maqam-analysis skill
(e.g. naming a quarter-tone maqam as a fact from 12-TET ABC input).
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import PIPELINE_VERSION, utc_now  # noqa: E402

SCHEMA_VERSION = "1.0"

CONF_RANK = {"low": 0, "medium": 1, "high": 2}
STATUSES = {"consistent", "possible", "withheld", "unknown"}

# Canonical names used in this dataset. Aliases are normalized below.
MAQAMAT = [
    "Rast",
    "Ajam",
    "Bayati",
    "Nahawand",
    "Nahawand (raised 7th)",
    "Kurd",
    "Hijaz",
    "Hijaz (Rast upper)",
    "Hijaz Kar",
    "Saba",
    "Nikriz",
    "Nawa Athar",
    "Sikah",
    "Huzam",
    "Iraq",
    "Awj Ara",
    "Suznek",
    "Jiharkah",
    "Farahfaza",
    "Shawq Afza",
    "Bastanikar",
]

# Maqamat whose defining degrees include a quarter tone (150/350/1050 cents) or
# whose tonic itself is a quarter tone. From 12-TET ABC these can only be "possible".
QUARTER_TONE = {
    "Rast",
    "Bayati",
    "Saba",
    "Sikah",
    "Huzam",
    "Iraq",
    "Awj Ara",
    "Suznek",
    "Jiharkah",
    "Bastanikar",
}

_ALIASES = {
    "rast": "Rast",
    "ajam": "Ajam",
    "ajam ushshiran": "Ajam",
    "bayati": "Bayati",
    "bayyati": "Bayati",
    "nahawand": "Nahawand",
    "nahawand (raised 7th)": "Nahawand (raised 7th)",
    "nahawand raised 7th": "Nahawand (raised 7th)",
    "nahawand harmonic": "Nahawand (raised 7th)",
    "kurd": "Kurd",
    "hijaz": "Hijaz",
    "hijaz (rast upper)": "Hijaz (Rast upper)",
    "hijaz rast upper": "Hijaz (Rast upper)",
    "hijaz kar": "Hijaz Kar",
    "hijazkar": "Hijaz Kar",
    "saba": "Saba",
    "nikriz": "Nikriz",
    "nawa athar": "Nawa Athar",
    "nawaathar": "Nawa Athar",
    "sikah": "Sikah",
    "sika": "Sikah",
    "huzam": "Huzam",
    "iraq": "Iraq",
    "awj ara": "Awj Ara",
    "awjara": "Awj Ara",
    "suznek": "Suznek",
    "suznak": "Suznek",
    "jiharkah": "Jiharkah",
    "farahfaza": "Farahfaza",
    "shawq afza": "Shawq Afza",
    "bastanikar": "Bastanikar",
}


def _key(value: str) -> str:
    value = (value or "").strip().lower()
    value = re.sub(r"^maqam\s+", "", value)
    value = re.sub(r"[_-]+", " ", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def canonical_maqam(value: str | None) -> str | None:
    if value is None:
        return None
    key = _key(value)
    if not key or key in {"withheld", "none", "unknown", "n/a"}:
        return None
    if key in _ALIASES:
        return _ALIASES[key]
    for alias, canonical in _ALIASES.items():
        if key.startswith(alias + " "):
            return canonical
    return None


def normalize_tonic(value: str | None) -> str | None:
    if not value:
        return None
    value = value.strip()
    m = re.match(r"^([A-Ga-g])([#b]?)$", value)
    if not m:
        return None
    return m.group(1).upper() + m.group(2)


def conf_rank(value: str | None) -> int:
    return CONF_RANK.get((value or "").lower(), -1)


def is_quarter_tone(maqam: str | None) -> bool:
    return canonical_maqam(maqam) in QUARTER_TONE


def _list_of_strings(value: Any) -> list[str]:
    if not value:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        out = []
        for item in value:
            if isinstance(item, str):
                out.append(item)
            elif isinstance(item, dict):
                cand = item.get("maqam") or item.get("name") or item.get("tonic")
                if cand:
                    out.append(str(cand))
        return out
    return []


def validate_input(
    raw: dict[str, Any],
    row: dict[str, Any],
    evidence: dict[str, Any],
    *,
    batch_id: str,
) -> tuple[dict[str, Any], list[str], list[str]]:
    """Validate the agent's compact label. Returns (normalized, errors, warnings)."""
    errors: list[str] = []
    warnings: list[str] = []

    if raw.get("song_id") != row["song_id"]:
        errors.append(f"song_id mismatch: {raw.get('song_id')!r} != {row['song_id']!r}")

    primary = evidence.get("primary") or {}
    parse = float((evidence.get("analyzer") or {}).get("bar_match_ratio") or 1.0)
    name_allowed = bool(primary.get("name_allowed"))
    flags = primary.get("flags") or []
    flag_text = " | ".join(flags)
    tied_shapes = set(primary.get("tied_shapes") or []) | set(primary.get("shadow_of") or [])

    status = (raw.get("maqam_status") or "").lower().strip()
    if status not in STATUSES:
        errors.append(f"maqam_status must be one of {sorted(STATUSES)}, got {raw.get('maqam_status')!r}")
    elif status == "unknown":
        errors.append("use maqam_status='withheld' with a reason instead of 'unknown'")

    maqam = canonical_maqam(raw.get("maqam"))
    if status == "withheld":
        if raw.get("maqam") not in (None, "", "withheld", "none", "unknown"):
            errors.append("withheld label must have maqam=null")
        if not (raw.get("withheld_reason") or "").strip():
            errors.append("withheld label needs a withheld_reason")
        maqam = None
    elif status in {"consistent", "possible"}:
        if not maqam:
            errors.append(
                f"maqam must be a known name (one of {', '.join(MAQAMAT)}) for status {status!r}"
            )
        if not (raw.get("rationale") or "").strip():
            errors.append("a named label needs a rationale")
        elif len(raw.get("rationale", "").strip()) < 40:
            errors.append("rationale is too short; write at least one full sentence (40+ chars)")
        if is_quarter_tone(maqam) and status == "consistent":
            errors.append(
                f"{maqam} has a quarter-tone degree; from 12-TET ABC it can only be "
                "'possible', never 'consistent' (see SKILL.md)"
            )
        if name_allowed is False and status != "withheld":
            errors.append(
                "the analyzer withheld a scale name (poor fit / too few pitch classes / quarter-tone tonic); "
                "use maqam_status='withheld'"
            )
        if maqam and tied_shapes and maqam not in tied_shapes:
            if not (raw.get("override_reason") or "").strip():
                errors.append(
                    f"{maqam} is not among the analyzer's best-fit shapes "
                    f"({', '.join(sorted(tied_shapes))}); set override_reason to justify it"
                )
            else:
                warnings.append(f"{maqam} is outside the analyzer's tied shapes; override_reason recorded")

    if parse < 0.95:
        errors.append(
            f"parse check is {parse:.0%}; the skill says do not trust the numbers. "
            "Use maqam_status='withheld'."
        )

    tonic = normalize_tonic(raw.get("tonic"))
    if not tonic:
        errors.append(f"tonic must be a note name like C, F#, Bb; got {raw.get('tonic')!r}")
    tonic_conf = (raw.get("tonic_confidence") or "").lower()
    if tonic_conf not in CONF_RANK:
        errors.append("tonic_confidence must be high, medium or low")
    overall = (raw.get("overall_confidence") or "").lower()
    if overall not in CONF_RANK:
        errors.append("overall_confidence must be high, medium or low")

    # The agent may lower confidence, never raise it above the tool's evidence.
    tool_tonic_conf = (primary.get("tonic_confidence") or "low").lower()
    if conf_rank(tonic_conf) > conf_rank(tool_tonic_conf):
        if not (raw.get("override_reason") or "").strip():
            errors.append(
                f"tonic_confidence {tonic_conf!r} is higher than the analyzer's {tool_tonic_conf!r}; "
                "lower it or set override_reason"
            )
    tool_shape_conf = (primary.get("shape_confidence") or "low").lower()
    cap = min(conf_rank(tonic_conf), conf_rank(tool_shape_conf))
    if overall and conf_rank(overall) > cap:
        if not (raw.get("override_reason") or "").strip():
            errors.append(
                f"overall_confidence {overall!r} exceeds min(tonic={tonic_conf}, shape={tool_shape_conf}); "
                "lower it or set override_reason"
            )

    if tonic and primary.get("tonic") and tonic != primary["tonic"]:
        alt_tonics = set(_list_of_strings(primary.get("alt_tonics")) + _list_of_strings(raw.get("tonic_alternatives")))
        if tonic not in alt_tonics:
            warnings.append(
                f"chosen tonic {tonic} differs from the analyzer's {primary['tonic']} and is not listed "
                "as an alternative; make sure the rationale explains the section evidence"
            )

    tonic_alts = [normalize_tonic(t) for t in _list_of_strings(raw.get("tonic_alternatives"))]
    tonic_alts = [t for t in tonic_alts if t]
    if "tonic/dominant split" in flag_text and not tonic_alts:
        errors.append(
            "flag 'tonic/dominant split' is present; list at least one tonic_alternatives note "
            "(do not pick silently)"
        )
    if "same notes also fit other tonics" in flag_text and not (
        tonic_alts or _list_of_strings(raw.get("alternatives"))
    ):
        warnings.append("relative-mode ambiguity flag present; alternatives should say which other tonics/shapes fit")

    alternatives = [canonical_maqam(a) or a for a in _list_of_strings(raw.get("alternatives"))]

    needs_review = bool(raw.get("needs_human_review", False))
    auto_review = (
        conf_rank(overall) <= 0
        or conf_rank(tonic_conf) <= 0
        or bool(flags)
        or status == "withheld"
        or parse < 0.95
    )
    if auto_review and not needs_review:
        warnings.append("needs_human_review forced to true (low confidence, flag, or withheld label)")
        needs_review = True

    normalized = {
        "song_id": row["song_id"],
        "maqam": maqam,
        "maqam_status": status,
        "tonic": tonic,
        "tonic_confidence": tonic_conf,
        "tonic_alternatives": sorted(set(tonic_alts)),
        "scale_family": (raw.get("scale_family") or primary.get("scale_western") or "").strip(),
        "overall_confidence": overall,
        "alternatives": sorted(set(a for a in alternatives if a)),
        "ghammaz_candidate": normalize_tonic(raw.get("ghammaz_candidate"))
        or ((primary.get("ghammaz") or {}).get("note") if isinstance(primary.get("ghammaz"), dict) else None),
        "withheld_reason": (raw.get("withheld_reason") or "").strip() or None,
        "rationale": (raw.get("rationale") or "").strip(),
        "needs_human_review": needs_review,
        "override_reason": (raw.get("override_reason") or "").strip() or None,
        "batch_id": batch_id,
    }
    return normalized, errors, warnings


def build_label(
    cfg: dict[str, Any],
    row: dict[str, Any],
    evidence: dict[str, Any],
    normalized: dict[str, Any],
    meta: dict[str, Any],
    *,
    reviewed_by: str,
    skill_sha256: str,
    previous: dict[str, Any] | None = None,
    revision_reason: str | None = None,
) -> dict[str, Any]:
    now = utc_now()
    previous = previous or {}
    revision = int((previous.get("provenance") or {}).get("revision") or 0) + 1
    created_at = (previous.get("provenance") or {}).get("created_at") or now
    transcript = meta.get("transcript") or {}

    return {
        "schema_version": SCHEMA_VERSION,
        "song_id": row["song_id"],
        "track_id": row["track_id"],
        "artist": row["artist"],
        "album": row["album"],
        "file": row["file"],
        "lyric_title": row.get("lyric_title", ""),
        "source": {
            "kind": "sheetsage2_abc",
            "transcript_json": row.get("transcript_json", ""),
            "transcript_track_id": row.get("transcript_track_id", ""),
            "transcript_sha256": row.get("transcript_sha256", ""),
            "model": transcript.get("model", ""),
            "model_revision": transcript.get("model_revision", ""),
            "mode": transcript.get("mode", ""),
            "audio_uri": row.get("audio_uri", ""),
            "audio_sha256": row.get("audio_sha256"),
            "abc_sha256": row.get("abc_sha256", ""),
            "abc_melody_sha256": row.get("abc_melody_sha256", ""),
            "duration_s": row.get("duration_s"),
            "declared_key": row.get("declared_key", ""),
            "tempo_bpm": row.get("tempo_bpm"),
        },
        "evidence": {
            "evidence_sha256": evidence.get("evidence_sha256", ""),
            "parse_check": (evidence.get("analyzer") or {}).get("bar_match_ratio"),
            "parser_warnings": (evidence.get("report") or {}).get("warnings") or [],
            "voice": (evidence.get("analyzer") or {}).get("voice_analysed"),
            "primary": evidence.get("primary") or {},
            "sections": evidence.get("sections") or [],
            "melody_variant": evidence.get("melody_variant"),
            "report_path": evidence.get("report_path", f"work/{row['song_id']}/report.md"),
        },
        "label": normalized,
        "review": {
            "reviewed_by": reviewed_by,
            "reviewed_at": now,
            "batch_id": normalized.get("batch_id", ""),
            "skill_version": f"maqam-analysis@{skill_sha256[:12]}",
            "skill_sha256": skill_sha256,
            "needs_human_review": normalized["needs_human_review"],
            "qc_status": (previous.get("review") or {}).get("qc_status", "not_reviewed"),
        },
        "provenance": {
            "run_id": cfg["run_id"],
            "pipeline_version": PIPELINE_VERSION,
            "created_at": created_at,
            "updated_at": now,
            "revision": revision,
            "revision_reason": revision_reason if revision > 1 else None,
            "previous_revision": (previous.get("provenance") or {}).get("revision"),
        },
    }

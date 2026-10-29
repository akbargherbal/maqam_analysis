"""Fast, network-free tests for the maqam labeling pipeline."""
from __future__ import annotations

import copy
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from common import make_song_id, normalize_text, sha256_text, slugify  # noqa: E402
from labels import build_label, canonical_maqam, validate_input  # noqa: E402

FIXTURES = ROOT / "tests" / "fixtures"
ANALYZER = ROOT / "skills" / "maqam-analysis" / "scripts" / "analyze_abc.py"


# --------------------------------------------------------------------- analyzer
@pytest.mark.parametrize("name", ["synthetic-nahawand.abc", "synthetic-kurd.abc"])
def test_analyzer_parses_fixture(name):
    proc = subprocess.run(
        [sys.executable, str(ANALYZER), str(FIXTURES / name), "--voice", "Vocal", "--json"],
        text=True,
        capture_output=True,
        timeout=60,
    )
    assert proc.returncode == 0, proc.stderr
    report = json.loads(proc.stdout)
    assert report["bar_match_ratio"] >= 0.95
    assert report["groups"]
    group = report["groups"][0]
    assert group["tonic_confidence"] in {"low", "medium", "high"}
    assert group["hypotheses"][0]["tonic"]
    # 12-TET input must never be marked microtonal.
    assert group["microtonal_input"] is False


# ------------------------------------------------------------------------ naming
def test_slug_and_song_id_are_stable():
    assert slugify("Elissa - 1998 Baddy Doub / 01. Baddy Doub") == "elissa-1998-baddy-doub-01-baddy-doub"
    row = {"artist": "Elissa", "album": "Elissa - 1998 Baddy Doub", "file": "01. Baddy Doub.mp3", "track_id": "a"}
    first = make_song_id(row)
    second = make_song_id(row)
    assert first == second
    assert first.startswith("elissa-1998-baddy-doub-01-baddy-doub")


def test_normalize_text_handles_apostrophes():
    assert normalize_text("Ba’da Aalbal") == normalize_text("Ba'da Aalbal")
    assert sha256_text("abc") == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"


# ----------------------------------------------------------------- label rules
def base_evidence():
    return {
        "evidence_sha256": "evhash",
        "analyzer": {"bar_match_ratio": 1.0, "voice_analysed": "Vocal"},
        "report": {"warnings": []},
        "primary": {
            "tonic": "E",
            "tonic_confidence": "low",
            "shape_confidence": "medium",
            "name_allowed": True,
            "tied_shapes": ["Bayati", "Nahawand"],
            "shadow_of": ["Bayati"],
            "scale_western": "natural minor / Aeolian",
            "flags": [],
            "ghammaz": {"note": "B"},
            "alt_tonics": [{"tonic": "B", "fit": 0.98}],
        },
    }


def base_raw():
    return {
        "song_id": "song-1",
        "maqam": "Nahawand",
        "maqam_status": "consistent",
        "tonic": "E",
        "tonic_confidence": "low",
        "tonic_alternatives": [],
        "overall_confidence": "low",
        "alternatives": ["Bayati"],
        "ghammaz_candidate": "B",
        "withheld_reason": None,
        "rationale": "The notes fit a natural-minor shape on E and the tool key agrees. "
        "This is consistent with Nahawand, but the ABC cannot separate it from Bayati.",
        "needs_human_review": True,
    }


ROW = {
    "song_id": "song-1",
    "track_id": "Elissa/Album/01. Song.mp3",
    "artist": "Elissa",
    "album": "Album",
    "file": "01. Song.mp3",
    "lyric_title": "song",
}


def test_valid_label_passes():
    norm, errors, warnings = validate_input(base_raw(), ROW, base_evidence(), batch_id="batch-001")
    assert errors == []
    assert norm["maqam"] == "Nahawand"
    assert norm["maqam_status"] == "consistent"


def test_quarter_tone_maqam_must_be_possible():
    raw = base_raw()
    raw.update(maqam="Bayati", maqam_status="consistent")
    _, errors, _ = validate_input(raw, ROW, base_evidence(), batch_id="batch-001")
    assert any("quarter-tone" in e for e in errors)


def test_quarter_tone_maqam_possible_passes():
    raw = base_raw()
    raw.update(maqam="Bayati", maqam_status="possible", rationale="The shape is a 12-TET shadow of Bayati; the quarter-tone second cannot be confirmed.")
    _, errors, _ = validate_input(raw, ROW, base_evidence(), batch_id="batch-001")
    assert errors == []


def test_withheld_needs_reason():
    raw = base_raw()
    raw.update(maqam=None, maqam_status="withheld", withheld_reason="")
    _, errors, _ = validate_input(raw, ROW, base_evidence(), batch_id="batch-001")
    assert any("withheld_reason" in e for e in errors)

    raw["withheld_reason"] = "No single scale fits (fit 0.77)."
    _, errors, _ = validate_input(raw, ROW, base_evidence(), batch_id="batch-001")
    assert errors == []


def test_name_allowed_false_forces_withheld():
    ev = base_evidence()
    ev["primary"]["name_allowed"] = False
    _, errors, _ = validate_input(base_raw(), ROW, ev, batch_id="batch-001")
    assert any("name_allowed" in e or "withheld" in e for e in errors)


def test_low_parse_forces_withheld():
    ev = base_evidence()
    ev["analyzer"]["bar_match_ratio"] = 0.80
    _, errors, _ = validate_input(base_raw(), ROW, ev, batch_id="batch-001")
    assert any("parse check" in e for e in errors)


def test_confidence_cannot_exceed_evidence():
    raw = base_raw()
    raw["overall_confidence"] = "high"
    _, errors, _ = validate_input(raw, ROW, base_evidence(), batch_id="batch-001")
    assert any("overall_confidence" in e for e in errors)


def test_tonic_dominant_split_needs_alternatives():
    ev = base_evidence()
    ev["primary"]["flags"] = [
        "tonic/dominant split: E and B (a 4th/5th apart) score almost equally; the true tonic could be either"
    ]
    _, errors, _ = validate_input(base_raw(), ROW, ev, batch_id="batch-001")
    assert any("tonic/dominant split" in e for e in errors)

    raw = base_raw()
    raw["tonic_alternatives"] = ["B"]
    _, errors, _ = validate_input(raw, ROW, ev, batch_id="batch-001")
    assert errors == []


def test_unknown_maqam_rejected():
    raw = base_raw()
    raw["maqam"] = "Made Up Maqam"
    _, errors, _ = validate_input(raw, ROW, base_evidence(), batch_id="batch-001")
    assert any("known name" in e for e in errors)


def test_maqam_outside_tied_shapes_needs_override():
    raw = base_raw()
    raw.update(maqam="Hijaz", rationale="The augmented second is clear in the ABC and phrases rest on E, so this is read as Hijaz despite the tied Nahawand fit.")
    _, errors, _ = validate_input(raw, ROW, base_evidence(), batch_id="batch-001")
    assert any("override_reason" in e for e in errors)

    raw["override_reason"] = "Section-level evidence favours the Hijaz colour."
    _, errors, _ = validate_input(raw, ROW, base_evidence(), batch_id="batch-001")
    assert errors == []


# ------------------------------------------------------------------- enrichment
def test_build_label_enriches_provenance():
    cfg = {"run_id": "test-run"}
    ev = base_evidence()
    norm, errors, _ = validate_input(base_raw(), ROW, ev, batch_id="batch-001")
    assert errors == []
    meta = {"transcript": {"model": "m-a-p/SheetSage2", "model_revision": "rev", "mode": "full"}}
    label = build_label(cfg, ROW, ev, norm, meta, reviewed_by="ai-agent", skill_sha256="a" * 64)
    assert label["schema_version"] == "1.0"
    assert label["source"]["model"] == "m-a-p/SheetSage2"
    assert label["evidence"]["evidence_sha256"] == "evhash"
    assert label["provenance"]["revision"] == 1
    assert label["review"]["reviewed_by"] == "ai-agent"

    revised = build_label(
        cfg, ROW, ev, norm, meta, reviewed_by="ai-agent", skill_sha256="a" * 64,
        previous=label, revision_reason="QC correction",
    )
    assert revised["provenance"]["revision"] == 2
    assert revised["provenance"]["previous_revision"] == 1
    assert revised["provenance"]["revision_reason"] == "QC correction"


def test_canonical_aliases():
    assert canonical_maqam("bayati") == "Bayati"
    assert canonical_maqam("Nahawand (Raised 7th)") == "Nahawand (raised 7th)"
    assert canonical_maqam("hijaz kar") == "Hijaz Kar"
    assert canonical_maqam("bogus") is None

# Label schema (v1.0)

One JSON file per song: `labels/<song_id>.json`. The agent fills a compact
object; `scripts/review.py record` enriches it and validates it. Never write
the final file by hand.

## 1. What the agent fills

`work/review/batch-NNN.labels.json`:

```json
{
  "batch_id": "batch-001",
  "labels": [
    {
      "song_id": "elissa-1998-baddy-doub-01-baddy-doub",
      "maqam": "Nahawand",
      "maqam_status": "consistent",
      "tonic": "E",
      "tonic_confidence": "low",
      "tonic_alternatives": ["F#", "B"],
      "scale_family": "natural minor / Aeolian",
      "overall_confidence": "low",
      "alternatives": ["Bayati", "Kurd"],
      "ghammaz_candidate": "B",
      "withheld_reason": null,
      "rationale": "The vocal line uses the natural-minor set with phrases starting on E and resting on B; the tool key and chords agree on E. Consistent with Nahawand, but 12-TET cannot separate it from Bayati.",
      "needs_human_review": true,
      "override_reason": null
    }
  ]
}
```

### Field rules

| Field | Values | Rule |
|---|---|---|
| `song_id` | manifest id | must match the batch; do not edit |
| `maqam` | a name from the list below, or `null` | `null` iff withheld |
| `maqam_status` | `consistent`, `possible`, `withheld`, `unknown` | see below |
| `tonic` | note name (`C`, `F#`, `Bb`) | the tonic, not the maqam |
| `tonic_confidence` | `low`, `medium`, `high` | cannot exceed the analyzer's |
| `tonic_alternatives` | list of note names | required for a tonic/dominant split |
| `scale_family` | text | derived from the shape, e.g. `natural minor / Aeolian` |
| `overall_confidence` | `low`, `medium`, `high` | ≤ min(tonic, shape) |
| `alternatives` | list of maqam names | tied shapes / plausible readings |
| `ghammaz_candidate` | note name or null | descriptive, not a finding |
| `withheld_reason` | text | required iff withheld |
| `rationale` | 2-4 sentences | required for every label; ≥40 chars |
| `needs_human_review` | bool | forced true for low confidence/flags/withheld |
| `override_reason` | text or null | required if you depart from the evidence |

### `maqam_status` semantics

- **`consistent`** — the notes fit this shape, but the input is 12-TET. It is
  still not a fact. Allowed only for non-quarter-tone maqamat.
- **`possible`** — the reading requires a quarter tone that the ABC cannot
  show. Required for Rast, Bayati, Saba, Sikah, Huzam, Iraq, Awj Ara, Suznek,
  Jiharkah, Bastanikar. Also acceptable for a weaker non-quarter reading.
- **`withheld`** — no scale is identified, parse is unreliable, too few pitch
  classes, or the evidence is contradictory. `maqam` must be `null` and
  `withheld_reason` must be set.
- **`unknown`** — reserved; do not use unless the evidence is unreadable. Prefer
  `withheld`.

### Allowed maqam names

Modelled by the skill:

`Rast`, `Ajam`, `Bayati`, `Nahawand`, `Nahawand (raised 7th)`, `Kurd`, `Hijaz`,
`Hijaz (Rast upper)`, `Hijaz Kar`, `Saba`, `Nikriz`, `Nawa Athar`.

Unmodelled but accepted as a reading (must be `possible` or withheld):
`Sikah`, `Huzam`, `Iraq`, `Awj Ara`, `Suznek`, `Jiharkah`, `Farahfaza`,
`Shawq Afza`, `Bastanikar`.

## 2. What `record` adds

The final file:

```json
{
  "schema_version": "1.0",
  "song_id": "...",
  "track_id": "Elissa/Elissa - 1998 Baddy Doub/01. Baddy Doub.mp3",
  "artist": "Elissa",
  "album": "Elissa - 1998 Baddy Doub",
  "file": "01. Baddy Doub.mp3",
  "lyric_title": "بدي دوب",
  "source": {
    "kind": "sheetsage2_abc",
    "transcript_json": "gs://.../TRANSCRIPTS/ELISSA/abc/....json",
    "transcript_track_id": "ELISSA/.../01-baddy-doub",
    "transcript_sha256": "...",
    "model": "m-a-p/SheetSage2",
    "model_revision": "b83c3d...",
    "mode": "full",
    "audio_uri": "gs://.../DISCOGRAPHY/ELISSA/.../01. Baddy Doub.mp3",
    "audio_sha256": "...",
    "abc_sha256": "...",
    "abc_melody_sha256": "...",
    "duration_s": 236.8,
    "declared_key": "Em",
    "tempo_bpm": 101.0
  },
  "evidence": {
    "evidence_sha256": "...",
    "parse_check": 1.0,
    "parser_warnings": [],
    "voice": "Vocal",
    "primary": { "...": "tonic, cues, scale_shape, fit, flags, ghammaz, ..." },
    "sections": [ "...": "per-section summaries" ],
    "melody_variant": { "...": "chords removed cross-check" },
    "report_path": "work/<song_id>/report.md"
  },
  "label": { "...": "the normalized input fields above" },
  "review": {
    "reviewed_by": "ai-agent",
    "reviewed_at": "2026-10-29T07:04:58Z",
    "batch_id": "batch-001",
    "skill_version": "maqam-analysis@38fc847e6522",
    "skill_sha256": "...",
    "needs_human_review": true,
    "qc_status": "not_reviewed"
  },
  "provenance": {
    "run_id": "maqam-167-v1",
    "pipeline_version": "1.0.0",
    "created_at": "...",
    "updated_at": "...",
    "revision": 1,
    "revision_reason": null,
    "previous_revision": null
  }
}
```

## 3. Revision and history

- Re-labeling requires `review.py record --revise --reason "..."`.
- The previous file is copied to
  `labels/_history/<song_id>/rev-NNN-<timestamp>.json`.
- `provenance.revision` increments; `previous_revision` is recorded.
- A restore conflict is copied to `labels/_conflicts/`; the newer
  `(revision, updated_at)` wins.

## 4. Validation errors you will see

| Error | Fix |
|---|---|
| `parse check is 87%; ... use withheld` | withdraw the name |
| `... name_allowed=False` | withdraw the name |
| `Bayati ... can only be 'possible'` | set `maqam_status="possible"` |
| `overall_confidence high exceeds min(...)` | lower it |
| `tonic/dominant split ... list tonic_alternatives` | add the other note |
| `... not among the analyzer's best-fit shapes` | add `override_reason` or use a tied shape |
| `withheld label needs a withheld_reason` | write the reason |
| `already labeled; use --revise` | revise with a reason, or skip |

## 5. What not to put in a label

- no probability numbers;
- no claims about how the song sounds;
- no artist/song trivia;
- no maqam name that the evidence does not support;
- no "Sikah/Huzam" as a finding when the tonic itself is a quarter tone (the
  tool does not model it; withhold).

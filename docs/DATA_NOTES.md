# Data notes — corpus, transcripts, and limits

Measured on 2026-10-29 against the real GCS archive.

## 1. Corpus

`data/corpus.json` — 167 rows.

| Artist | Rows | Usable ABC |
|---|---:|---:|
| Elissa | 89 | 88 |
| Fadl Shaker | 78 | 75 |
| **Total** | **167** | **163** |

Each row: `track_id` (`Artist/Album/File.mp3`), `artist`, `album`, `file`,
`lyric_title`.

## 2. Transcript archive

`gs://akbar-december-2024-backup/TRANSCRIPTS/`

- 23 album JSONs: 8 under `ELISSA/abc/`, 15 under `FADL_SHAKER/abc/`.
- 236 transcript rows total; 227 have `transcribe_status=ok` and an `abc`.
- Source model: `m-a-p/SheetSage2`, revision
  `b83c3d79a6d98bcffaf8f9ed112c90aa887887bc`, mode `full`.
- ABC uses two voices, `Vocal` and `Ins`, with chord symbols and `% section`
  comments. Parse check is 100% on the sampled files.
- Each row carries `audio_sha256`, `abc_sha256`, `key`, `tempo_bpm`, `meters`,
  `sections`, `notes_vocal`, `notes_ins`, `has_chords`, `qc`.
- The full upstream log is in
  `gs://akbar-december-2024-backup/TRANSCRIPTS/_logs/TRANSCRIPTION_RESULTS_20261028.md`.

The corpus maps to the archive by `(artist code, album, file)` with a
normalized fallback (case, whitespace, apostrophes). **167/167 matched.**

## 3. The four `no_abc` tracks

These are upstream SheetSage2 failures: every side artifact was written except
`score.abc`. They are not a pipeline bug. The plan does not invent or hand-edit
an ABC.

| Track | Corpus file |
|---|---|
| `ELISSA/Elissa - 2012  As3ad Wa7da` | `05. Te3ebt Minnak.mp3` |
| `FADL_SHAKER/08.Hafla 2004` | `05.Hobbak Khayal.mp3` |
| `FADL_SHAKER/10.Saharni El Shoq.2005` | `04.Tadri Lieh.mp3` |
| `FADL_SHAKER/15.The Best Of (Al Rawae3).2010` | `01.Rouh.mp3` |

They appear in `data/manifest.jsonl` with `status=no_abc` and in the export with
`label_status=no_abc`. A later GPU + SheetSage2 retry is a separate task.

## 4. Why the audio/f0 route is not used

The user has no vocal stems. `analyze_f0.py` needs an isolated vocal (full mixes
are refused or misled by accompaniment). Running Demucs would add GPU time and
a new failure mode without a validated accuracy gain. The ABC route is the
skill's native route and is already available for 163 songs.

If audio ever becomes available, the f0 route can be added later and compared
against these labels, especially for the Nahawand/Bayati and Ajam/Rast
ambiguities.

## 5. What the ABC can and cannot show

- **Can show:** pitch-class set, tonic cues (duration, phrase endings, starts,
  last note, tool key/chords, other voice), scale fit, sections, candidate
  ghammaz.
- **Cannot show:** quarter tones. The 150-cent 2nd of Bayati/Saba and the
  350-cent 3rd of Rast are rounded to 12-TET. Therefore:
  - natural minor can be Nahawand or Bayati;
  - Phrygian can be Kurd or Bayati;
  - major can be Ajam or Rast;
  - Dorian can be Rast rounded down or Western Dorian.
- **Tool-made evidence:** chord symbols and the `K:` line come from SheetSage2,
  not from the melody. They count as one vote. The melody-only analysis in
  `evidence.melody_variant` shows what happens when they are removed.
- **Sections:** verse/chorus can have different tonics. The packet shows the
  per-section calls; the label should mention a real disagreement.

## 6. Duplicate titles

The archive has 11 duplicate titles / 25 rows (e.g. original album tracks and
"The Best Of" copies). The corpus keeps one row per release, so a song can
appear more than once. The plan labels every row independently and
`exports/summary.json` reports duplicate-title agreement; disagreements are
flagged for a human look. No automatic deduplication is done.

## 7. Measured pre-label evidence distribution

A dry run of `prepare.py` on all 163 usable ABCs (no labels written) took 31 s
and produced 163 evidence files, **0 analysis failures, 0 parse checks below
95%**.

| Measure | Count |
|---|---:|
| `name_allowed=false` (must be withheld) | 19 |
| tonic confidence low / medium / high | 124 / 4 / 35 |
| shape confidence medium / low | 130 / 33 |
| relative-mode ambiguity flag | 114 |
| tonic/dominant split flag | 48 |
| songs with >=2 sections on different top tonics | 93 |

Top shape readings (before any agent judgment):

| Shape | Count |
|---|---:|
| Kurd | 79 |
| Nahawand | 64 |
| no standard maqam (Western mode) | 8 |
| Ajam | 6 |
| Rast | 2 |
| Nahawand (raised 7th) | 2 |
| Hijaz | 2 |

This is expected, not a failure. Shape confidence is capped at `medium` because
the input is 12-TET; tonic confidence is often `low` because pop phrases rest on
the 3rd/5th and relative-mode ambiguity is real. The dataset is useful precisely
because it records that ambiguity instead of forcing names. The 19
`name_allowed=false` songs are the first candidates for `withheld`.

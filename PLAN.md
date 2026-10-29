# Implementation plan — maqam labels for 167 Elissa / Fadl Shaker songs

Status: **planning complete, ready for Colab execution.**
Run id: `maqam-167-v1`
Pipeline: `1.0.0`
Skill: `skills/maqam-analysis` (maqam-analysis)

---

## 1. Executive summary

The hard part of this project is already done. The 167-song corpus maps 1:1 to
an existing archive of **SheetSage2 ABC transcriptions** in
`gs://akbar-december-2024-backup/TRANSCRIPTS/` (23 album JSONs, full mode with
vocal + instrument voices and chord symbols). There is therefore **no audio
processing, no Demucs, no GPU, and no SheetSage2 rerun** in this plan.

Inventory result:

| Item | Count |
|---|---:|
| Songs in `data/corpus.json` | 167 |
| Matched to a transcript row | 167 |
| Usable ABC (`status=ok`) | **163** |
| No ABC (transcription failed upstream) | **4** |
| Missing transcript rows | 0 |
| Albums represented | 23 (8 Elissa + 15 Fadl Shaker) |
| Transcript archive rows (all artists) | 236 (227 with ABC) |

The four unusable tracks are:

- `Elissa/Elissa - 2012  As3ad Wa7da/05. Te3ebt Minnak.mp3`
- `Fadl Shaker/08.Hafla 2004/05.Hobbak Khayal.mp3`
- `Fadl Shaker/10.Saharni El Shoq.2005/04.Tadri Lieh.mp3`
- `Fadl Shaker/15.The Best Of (Al Rawae3).2010/01.Rouh.mp3`

A dry run of the analyzer on all 163 usable ABCs (no labels written) completed
in **31 s** with **0 failures and 0 parse checks below 95%**. The evidence
already shows why the task needs judgment rather than a one-line script:

- 19 songs have `name_allowed=false` and must be withheld;
- tonic confidence is low 124 / medium 4 / high 35;
- shape confidence is medium 130 / low 33 (12-TET caps it);
- 114 songs carry a relative-mode ambiguity flag, 48 a tonic/dominant split;
- 93 songs have at least two sections whose top tonic differs.

The deliverable is **163 weak labels** (one validated JSON per song) plus a
167-row export that explicitly marks the four gaps. No accuracy claim is
possible: there is no ground truth, and the ABC input is 12-TET, so
quarter-tone maqamat can only ever be labeled `possible`. A blind re-review
sample is the only quality signal.

---

## 2. Inputs and provenance

### 2.1 Corpus

`data/corpus.json` — 167 rows: `track_id`, `artist`, `album`, `file`,
`lyric_title`. This is the label target list.

### 2.2 Transcript archive

`gs://akbar-december-2024-backup/TRANSCRIPTS/`

```
ELISSA/abc/<album>.json                 8 files
FADL_SHAKER/abc/<album>.json           15 files
ELISSA/<album>.tar.gz                  raw artifacts (not needed)
FADL_SHAKER/<album>.tar.gz             raw artifacts (not needed)
_logs/TRANSCRIPTION_RESULTS_20261028.md
```

Each album JSON contains a `tracks[]` array. Relevant fields:

| Field | Use |
|---|---|
| `file`, `track_id`, `audio_sha256`, `source_uri` | mapping and provenance |
| `transcribe_status`, `abc`, `abc_melody` | analysis input |
| `abc_sha256`, `abc_melody_sha256` | integrity check |
| `key`, `tempo_bpm`, `meters`, `sections` | cross-checks |
| `duration_s`, `notes_vocal`, `notes_ins`, `has_chords`, `qc` | inventory/QC |
| `model`, `model_revision` (album level) | provenance |

Model: `m-a-p/SheetSage2`, revision
`b83c3d79a6d98bcffaf8f9ed112c90aa887887bc`, mode `full`, device `cuda` at
transcription time. The ABC is UTF-8 text; the plan never edits it.

### 2.3 Audio (not used)

The user will have `/content/DISCOGRAPHY/` (from
`gs://akbar-december-2024-backup/DISCOGRAPHY/`). It is **not required**. It is
recorded in each label's `source.audio_uri` / `audio_sha256` for provenance and
for a possible future f0 cross-check. Do not download it to run this plan.

---

## 3. Scope and non-goals

In scope:

- join the corpus to the transcript archive;
- extract the 163 ABCs and the 163 melody-only variants;
- run the skill's `analyze_abc.py` on both variants;
- have the agent adjudicate each song against the skill's rules;
- write one validated, versioned label per song;
- checkpoint every label to GCS and every batch to the GitHub repo;
- resume from any disconnect without relabeling;
- export CSV/JSONL/summary and a blind QC agreement report.

Out of scope:

- audio stem separation, f0 tracking, Demucs, GPU work;
- rerunning SheetSage2 or hand-editing ABCs;
- human ground truth or claims of accuracy;
- fixing the 4 upstream `no_abc` failures (could be retried separately with a
  GPU + SheetSage2, but that is a different project);
- maqam theory beyond the skill's template model (seyir, jins-level analysis,
  modulation inside a section).

---

## 4. Architecture

```
gs://.../TRANSCRIPTS/*.json
        │  prepare.py --refresh
        ▼
cache/transcripts/*.json
        │  join on (artist, album, file)
        ▼
data/manifest.jsonl (167 rows) ──► data/transcripts_index.json (236 rows)
        │  extract
        ▼
data/abc/<song_id>.abc + data/abc_melody/<song_id>.abc   (gitignored, immutable)
        │  analyze_abc.py --voice Vocal --json  (x2: full + melody-only)
        ▼
work/<song_id>/{meta,analysis,analysis_melody,evidence}.json + report.md
        │  review.py packet --limit 8
        ▼
work/review/batch-NNN.md + .json + .labels.json
        │  agent fills labels, review.py validate
        ▼
review.py record ──► labels/<song_id>.json ──► GCS (per label)
        │                    │
        │                    └──► state/ledger.jsonl + state/progress.json
        ▼
backup.py flush ──► GCS mirror + GitHub commit/push
        │
        ▼
export_dataset.py ──► exports/maqam_labels.{csv,jsonl}, summary, SUMMARY.md
qc.py compare     ──► exports/qc_report.{json,md}
```

The deterministic compute is cheap (163 × 2 analyses, seconds each). The
expensive part is agent judgment, so it is chunked into 8-song batches with a
checkpoint after every label.

---

## 5. Repository layout

```
AGENTS.md                     operating contract for the Colab agent
PLAN.md                       this plan
COLAB_KICKSTART.md            copy-paste first message for the agent
README.md                     quickstart and command reference
opencode.json                 registers ./skills and AGENTS.md
config/config.json            paths, GCS prefixes, batch size, backup policy
data/
  corpus.json                 167 target rows (source of truth)
  manifest.jsonl              generated join, 167 rows
  transcripts_index.json      generated metadata for all 236 transcript rows
  truth.csv                   header only (no ground truth)
  abc/                        generated ABCs (gitignored)
  abc_melody/                 generated melody-only ABCs (gitignored)
labels/
  <song_id>.json              final validated labels (committed/backed up)
  _history/<song_id>/         previous revisions
  _conflicts/                 restore conflict copies
state/
  run.json                    run id, corpus/config/skill hashes
  ledger.jsonl                append-only events (label_recorded, ...)
  progress.json               derived cache (safe to rebuild)
  backup.json                 last GCS/git checkpoint (gitignored)
work/
  <song_id>/meta.json         source hashes, model, audio URI
  <song_id>/analysis.json     raw full-report JSON
  <song_id>/analysis_melody.json
  <song_id>/evidence.json     compact evidence + evidence_sha256
  <song_id>/report.md         full human-readable report
  <song_id>/label.json        copy of the label
  review/batch-NNN.*          packet, template, recorded labels
  qc/qc-NNN.*                 blind re-review packets
qc/labels/<song_id>.json      blind second-pass labels (not in main labels/)
scripts/
  common.py                   atomic writes, hashes, config, GCS/git helpers
  prepare.py                  fetch + manifest + extract + analyze
  progress.py                 rebuild progress from disk
  status.py                   one-shot status (never blocks)
  labels.py                   schema + hard-rule validator
  review.py                   packet / validate / record
  backup.py                   flush / restore / check
  export_dataset.py           CSV/JSONL + summary
  qc.py                       blind-agreement report
  ops.sh                      background-first command wrapper
  bootstrap_colab.sh          Colab environment checks
tests/                        stdlib/pytest tests + two ABC fixtures
notebooks/00_colab_bootstrap.ipynb
docs/LABEL_SCHEMA.md
docs/RUNBOOK.md
docs/DATA_NOTES.md
skills/maqam-analysis/        unchanged skill
```

---

## 6. Label schema and state machine

The authoritative schema is in `docs/LABEL_SCHEMA.md`. The compact input the
agent fills is only 12 fields; `record` enriches it with source hashes, the
evidence snapshot, the skill hash, timestamps and revision.

Per-song states:

```
no_abc / missing_transcript        terminal; exported with a reason
pending                            in manifest, no ABC extracted
prepared                           ABC extracted, no evidence
analyzed                           evidence.json exists
labeled                            labels/<song_id>.json validates
```

`needs_human_review` is a flag on a label, not a separate state. A song is
**done** when a validated label exists; a withheld label is still done.

### Hard validation gates (enforced by `scripts/labels.py`)

1. `parse_check < 0.95` → must be `withheld`.
2. `name_allowed == false` → must be `withheld`.
3. Quarter-tone maqam + status `consistent` → rejected; use `possible`.
4. `overall_confidence` > `min(tonic_confidence, shape_confidence)` → rejected.
5. Named maqam outside the analyzer's tied shapes → requires `override_reason`.
6. `tonic/dominant split` flag → requires `tonic_alternatives`.
7. Withheld label without `withheld_reason` → rejected.
8. Rationale shorter than one sentence → rejected.
9. Re-labeling without `--revise --reason` → rejected; history is kept.

---

## 7. Phases

### Phase 0 — Colab bootstrap (5-10 min)

```bash
# In /content
git clone https://github.com/akbargherbal/maqam_analysis.git
cd maqam_analysis
bash scripts/bootstrap_colab.sh
```

Bootstrap checks Python, installs `pytest`, verifies `gcloud` and GCS access,
sets a local git identity if missing, and runs the skill analyzer on a synthetic
fixture.

Acceptance: `gcloud storage ls gs://akbar-december-2024-backup/TRANSCRIPTS/`
succeeds; `python3 scripts/status.py` prints "No manifest yet".

### Phase 1 — Prepare evidence (2-5 min, background)

```bash
bash scripts/ops.sh prepare
bash scripts/ops.sh log prepare 80     # poll only on user turn
python3 scripts/status.py
```

`prepare` downloads 23 JSONs (2.3 MB), builds the manifest, extracts 163 ABCs
+ 163 melody variants, and runs the analyzer twice per song. It is idempotent:
existing evidence is skipped unless `--force`.

Expected output:

```
[manifest] 167 corpus rows -> 163 ok, 4 no_abc, 0 missing_transcript
[extract] ... extracted=163
[analyze] ... analyzed=163, failed=0
```

Acceptance: `status.py` shows `prepared 163/163 | analyzed 163/163`; no
`analysis_error.json` except a documented exception.

### Phase 2 — Label in batches (1-3 h active, 21 batches)

For each batch:

```bash
python3 scripts/review.py packet --limit 8
# read work/review/batch-NNN.md, fill batch-NNN.labels.json
python3 scripts/review.py validate --batch ... --labels ...
python3 scripts/review.py record   --batch ... --labels ...
bash scripts/ops.sh backup
```

Batch policy:

- 8 songs per batch; never more than 10 in one turn.
- Review in `manifest` order by default; optionally
  `--order uncertainty` to front-load low-confidence songs.
- After each batch, report progress and ask whether to continue.
- Each `record` writes the label atomically, appends to the ledger, updates
  progress, and uploads the label JSON to GCS.
- `ops.sh backup` then mirrors state and commits/pushes.

Acceptance per batch: all 8 labels validate; GCS uploads succeed or are
reported; `status.py` increments by 8; no duplicate `song_id`.

### Phase 3 — Resume drill (10 min, once)

Simulate a disconnect: stop the session, start a fresh Colab runtime, clone the
repo, authenticate, then:

```bash
bash scripts/ops.sh restore
python3 scripts/status.py
```

Acceptance: the labeled count and next batch match the pre-disconnect state;
no label is lost; no song is reprocessed. Document the observed count in the
session log.

### Phase 4 — Finish and blind QC (30-60 min)

When `status.py` shows `163/163`:

```bash
bash scripts/ops.sh export
python3 scripts/review.py packet --qc --limit 20
# fill work/qc/qc-001.labels.json without looking at labels/
python3 scripts/review.py record --qc --batch work/qc/qc-001.json \
  --labels work/qc/qc-001.labels.json
python3 scripts/qc.py compare
```

QC is a **blind second pass** on a stratified sample (low/medium/high). Report
exact maqam agreement, tonic agreement and coarse named-vs-withheld agreement.
Do not call it accuracy.

Acceptance: `exports/qc_report.md` exists with `compared >= 15`; disagreements
are listed; no claim of ground-truth accuracy.

### Phase 5 — Handoff (5 min)

```bash
bash scripts/ops.sh export
bash scripts/ops.sh backup
python3 scripts/status.py --json > /tmp/final_status.json
```

Deliverables:

- `labels/*.json` (163)
- `exports/maqam_labels.csv` (167 rows, 4 `no_abc`)
- `exports/maqam_labels.jsonl`
- `exports/summary.json`, `exports/SUMMARY.md`
- `exports/qc_report.{json,md}` (if QC run)
- `state/ledger.jsonl`, `state/progress.json`
- GCS checkpoint + GitHub commit

---

## 8. Backup and resume design

### 8.1 Durability ladder

| Layer | What | When | Loss window |
|---|---|---|---|
| Local Colab disk | label JSON, ledger, work | every write | VM death |
| GCS label object | `labels/<song_id>.json` | after every `record` | ~0 |
| GCS mirror | `state/`, `labels/`, `work/`, `exports/` | after every `backup` | one batch |
| GitHub | text artifacts + commit history | after every `backup` | one batch |
| Transcript archive | ABC source of truth | pre-existing | none |

GCS is the primary durable store. GitHub is the versioned, human-readable
mirror. A failed git push (auth or network) does not lose labels
because each label was already uploaded.

### 8.2 GCS layout

```
gs://akbar-december-2024-backup/MAQAM_ANALYSIS/maqam-167-v1/
  state/{run,progress,ledger,backup}.json
  labels/<song_id>.json
  work/<song_id>/{meta,analysis,analysis_melody,evidence,report,label}.json/md
  work/review/batch-NNN.{md,json,labels.json}
  work/qc/...
  exports/...
  data/manifest.jsonl
  data/transcripts_index.json
```

`gcloud storage rsync -r` is used without `--delete`, so a bad local state
cannot erase a good remote state.

### 8.3 Restore algorithm

1. Optional `git pull --ff-only`.
2. Download remote `labels/`, `state/`, `work/`, `exports/` to `cache/restore/`.
3. Merge labels by `(provenance.revision, provenance.updated_at)`:
   - remote newer → copy local to `labels/_conflicts/`, install remote;
   - local newer → keep local, save remote to `_conflicts/`;
   - identical → nothing.
4. Copy missing `state/` and `work/` files; never overwrite a newer local label.
5. Rebuild `state/progress.json` from disk.
6. Print labeled/remaining and the next batch.

### 8.4 Resume scenarios

| Scenario | Result |
|---|---|
| Disconnect after 47 labels, all backed up | restore → 47/163, packet starts at song 48 |
| Disconnect mid-batch after 3 of 8 | those 3 labels are in GCS; restore merges; packet selects the other 5 (already-labeled songs are filtered) |
| Disconnect before `backup` | per-label GCS objects survive; git may be one batch behind; restore prefers GCS |
| GCS auth lost | git labels are the fallback; keep labeling locally; retry GCS |
| ABC/evidence missing | `prepare` re-extracts/analyzes only missing work; labels untouched |
| Evidence changed | `status` lists stale labels; revise with a reason, never delete |

---

## 9. Live-chat protocol

The chat must stay responsive. The following are policy, not suggestions:

1. `prepare`, `restore`, `backup` run via `scripts/ops.sh` with `setsid nohup`.
   The tool returns in <1 s with a PID and log path.
2. The agent reports the PID/log and returns to the user. It checks with
   `ops.sh status` or `ops.sh log <name> <lines>` only on a user turn or after
   a bounded batch.
3. No `sleep`, `tail -f`, `watch`, or unbounded loops.
4. Labeling is chunked into 8-song batches; each batch ends with `record`,
   `backup`, and a progress line.
5. If a background job fails, the log is the source of truth; the agent reports
   the tail, not a guess.

`ops.sh` commands:

```
prepare | restore | backup | status | packet | validate | record | export | qc
log <name> [lines] | jobs | stop <name> | help
```

---

## 10. Quality controls

### 10.1 Evidence cross-checks

For every song, `prepare` stores:

- the full ABC analysis (chords + `K:` + other voice);
- the melody-only analysis (chords stripped), so the agent can see whether the
  tool's chord/key vote is driving the tonic;
- per-section results (verse / pre-chorus / chorus), which expose modulation
  and tonic drift;
- parser warnings and bar-match ratio.

The review packet shows the full and melody-only results side by side.

### 10.2 Label gates

The validator enforces the skill's hard rules (section 6). The most important
is that **a 12-TET ABC can never produce a factual quarter-tone maqam name**.

### 10.3 No-ground-truth QC

- Blind second pass on 20 stratified songs.
- Report agreement, not accuracy.
- Check duplicate-title groups for contradictory labels
  (`summary.json.duplicate_groups`).
- Human spot-check the `needs_human_review=true` subset if the user wants.

### 10.4 What the final dataset can and cannot support

Can support:

- a distribution of "consistent with" / "possible" maqam readings;
- a tonic + scale-family label with explicit confidence;
- research on ambiguity, modulation and quarter-tone candidates;
- retrieval/filtering by maqam hypothesis with a confidence field.

Cannot support:

- claims that a song "is" maqam X;
- accuracy metrics against ground truth;
- fine seyir/jins analysis;
- distinguishing Nahawand from Bayati, or Ajam from Rast, without audio/f0.

---

## 11. Effort and timeline

| Phase | Wall time | Notes |
|---|---|---|
| 0 bootstrap | 5-10 min | network + auth |
| 1 prepare | 2-5 min | mostly download; analysis is seconds |
| 2 label 163 songs | 1-3 h active | 21 batches × 8; model-dependent |
| 3 resume drill | 10 min | once |
| 4 QC + export | 30-60 min | 20-song blind pass + report |
| 5 handoff | 5 min | backup + summary |
| **Total** | **~2-4 h active** | can be split across Colab sessions |

Colab session limits are not a risk because every label is durable and the
queue is resumable.

---

## 12. Risks and mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Colab disconnect loses work | high | high | per-label GCS upload + per-batch git; restore drill |
| Labels overstate quarter-tone maqamat | medium | high | validator rejects `consistent` for quarter-tone set; packet rules |
| Agent forces a name when `name_allowed=false` | medium | high | hard validation gate; withheld reason required |
| Tonic ambiguity (relative modes / 5th) | high | medium | `tonic_alternatives`; low confidence; melody-only cross-check |
| 4 no_abc tracks | certain | low | export as `no_abc`; document; optional GPU retry later |
| Duplicate titles disagree | medium | low | duplicate-group report; human spot-check |
| GCS auth expires mid-run | medium | medium | labels stay local; retry; git fallback |
| Agent context bloat | medium | medium | 8-song packets, compact evidence, full report on demand |
| Agent labels from outside knowledge | medium | high | AGENTS.md rule; evidence-only packet; rationale required |

---

## 13. Acceptance checklist

- [ ] `python3 scripts/prepare.py` completes with 163 ok / 4 no_abc / 0 missing.
- [ ] `python3 scripts/status.py` shows `prepared 163/163`, `analyzed 163/163`.
- [ ] 163 labels exist and all pass `review.py validate`.
- [ ] Every label has `source`, `evidence`, `label`, `review`, `provenance`.
- [ ] No quarter-tone maqam has status `consistent`.
- [ ] All withheld labels have a `withheld_reason`.
- [ ] 4 `no_abc` tracks are exported with `label_status=no_abc`.
- [ ] `bash scripts/ops.sh restore` on a fresh runtime reproduces the labeled count.
- [ ] GCS checkpoint exists; GitHub commit exists.
- [ ] `exports/maqam_labels.csv` has 167 rows; `SUMMARY.md` states the caveats.
- [ ] `exports/qc_report.md` exists with a blind sample and agreement numbers.
- [ ] No audio, ABC, cache, or log file is committed to git.

---

## 14. Decisions already made

- **ABC-only route.** The transcripts exist; no audio/GPU work.
- **Hybrid evidence per song.** Full ABC (chords + other voice) and melody-only
  variant; the agent sees both.
- **GCS + GitHub.** GCS is primary durability; GitHub is the versioned mirror.
- **Batch size 8.** Small enough for context and fast checkpoints; 21 batches.
- **No forced labels.** Withheld is a valid, first-class outcome.
- **4 no_abc tracks excluded from labeling.** They remain in the export with a
  reason. A later GPU/SheetSage2 retry is a separate task.

## 15. Open items for the user

1. Confirm the GCS backup prefix
   `gs://akbar-december-2024-backup/MAQAM_ANALYSIS/maqam-167-v1` is acceptable
   (it is configurable in `config/config.json`).
2. Decide whether the final deliverable should merge duplicate-title groups
   (e.g. original vs "Best Of" copies) or keep one label per corpus row. The
   current plan keeps one label per row and reports duplicate agreement.
3. Optional: provide a small `truth.csv` for a handful of songs later for a
   separate evaluation. The skill's `evaluate.py` expects ABC/MIDI inputs, not
   label JSON, so that evaluation is a different script/task. No accuracy is
   claimed now.

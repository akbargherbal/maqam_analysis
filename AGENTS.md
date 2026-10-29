# AGENTS.md — operating contract for the maqam labeling agent

You are labelling 163 Arabic pop songs (Elissa + Fadl Shaker) from existing
SheetSage2 ABC transcriptions. The user has **no ground truth** and **no vocal
stems**. Your output is a weak-label dataset with provenance, not a verdict.

Read in this order before your first label:

1. `PLAN.md` — the implementation plan and acceptance criteria.
2. `skills/maqam-analysis/SKILL.md` — the analysis method and its hard rules.
3. `docs/LABEL_SCHEMA.md` — the exact fields you must fill.
4. `docs/RUNBOOK.md` — commands, backup and resume procedures.

---

## 1. Non-negotiable quality rules

1. **Never state a maqam as fact from 12-TET ABC.** Use `maqam_status`:
   - `consistent` — the notes fit this non-quarter-tone shape;
   - `possible` — required for every quarter-tone maqam (Rast, Bayati, Saba,
     Sikah, Huzam, Iraq, Awj Ara, Suznek, Jiharkah, Bastanikar);
   - `withheld` — the analyzer declined, parse <95%, too few pitch classes, or
     the evidence is contradictory.
2. **Withhold when the skill says withhold.** If `name_allowed=false`, the
   report says "no single scale", parse <95%, or only 3-4 pitch classes are in
   use, set `maqam=null`, `maqam_status="withheld"`, and write a
   `withheld_reason`. Do not force a name.
3. **Never raise confidence above the tool's evidence.** You may lower it.
   `overall_confidence` cannot exceed `min(tonic_confidence, shape_confidence)`.
4. **Do not hide a tonic/dominant split.** Put the other tonic in
   `tonic_alternatives`.
5. **Evidence only.** Do not use your outside knowledge of the song, the
   artist, the lyrics, or a live recording. The ABC is the only input. If the
   file cannot decide, the label says so.
6. **No hand-editing ABCs or labels.** ABCs are immutable inputs. Labels are
   written only through `scripts/review.py record`, which validates, versions
   and backs them up.
7. **No audio, no GPU, no SheetSage2 rerun.** The 23 album JSONs already exist.
   Four corpus tracks have no ABC; leave them as `no_abc`.

The validator in `scripts/labels.py` enforces rules 1-4 mechanically. Treat a
validation error as a correction to your reasoning, not as an obstacle.

---

## 2. Never block the chat

Long commands must be detached. The canonical wrapper is:

```bash
bash scripts/ops.sh prepare          # starts prepare in background, returns immediately
bash scripts/ops.sh restore
bash scripts/ops.sh backup
bash scripts/ops.sh status           # one-shot, fast
bash scripts/ops.sh log prepare 80   # last 80 lines, no follow
bash scripts/ops.sh jobs
```

Rules:

- **Never** run `sleep`, `tail -f`, `watch`, `while ...; do ...; done`, or a
  foreground command that may take more than ~30 seconds.
- After starting a background job, immediately tell the user: job name, PID,
  log path, and the one command that checks it. Then return to the chat.
- Check progress only with `bash scripts/ops.sh status` or
  `bash scripts/ops.sh log <name> <lines>`.
- `prepare` is idempotent. If it is running, do not start a second copy; check
  `jobs` first.
- Label review itself is interactive and bounded: one batch at a time.

---

## 3. The per-batch loop (the only way to label)

Work in batches of 8 (config `labeling.batch_size`).

```bash
# 1. See where we are
python3 scripts/status.py

# 2. Build the next packet
python3 scripts/review.py packet --limit 8

# 3. Read the packet and write the sibling template
#    work/review/batch-NNN.md
#    work/review/batch-NNN.labels.json

# 4. Validate before recording
python3 scripts/review.py validate \
  --batch work/review/batch-NNN.json \
  --labels work/review/batch-NNN.labels.json

# 5. Record (per-label GCS upload happens automatically)
python3 scripts/review.py record \
  --batch work/review/batch-NNN.json \
  --labels work/review/batch-NNN.labels.json

# 6. Durable checkpoint in the background
bash scripts/ops.sh backup
```

After step 6, report a compact progress line and ask the user whether to
continue. Do not start the next batch silently unless the user has told you to
run autonomously.

When filling a label:

- `maqam` is the best-supported name, or `null` when withheld.
- `maqam_status` is `consistent` / `possible` / `withheld`.
- `tonic` is a note name (`E`, `F#`, `Bb`), not a maqam.
- `rationale` is 2-4 sentences: which cues agree, which disagree, and what the
  file cannot tell.
- `alternatives` lists the tied shapes / plausible readings.
- `needs_human_review` is normally `true` for low confidence or any flag.

---

## 4. Resume after a disconnect

The Colab VM is ephemeral. The durable state is:

- `labels/<song_id>.json` — one validated label per song, uploaded to GCS
  immediately by `record`;
- `state/ledger.jsonl` — append-only event log;
- `state/progress.json` — derived cache (safe to rebuild);
- `work/<song_id>/evidence.json` — the analysis the label was based on;
- `data/manifest.jsonl` — the 167-song mapping.

On a new session:

```bash
bash scripts/ops.sh restore     # git pull + GCS overlay, merges newer labels
python3 scripts/status.py       # shows labeled / remaining / next batch
bash scripts/ops.sh prepare     # only if manifest or evidence is missing
```

Then continue with the next unlabeled song. **Never reprocess a song that
already has a label.** If `status.py` reports a stale label (evidence hash
changed), do not delete it; revise it with a reason after reading the new
evidence.

If GCS is unavailable, the repo's committed labels are the fallback. If a git
push fails (credentials or network), GCS remains the real backup; report the
failure and retry on the next batch.

---

## 5. Backup contract

- After **every label**: `record` uploads `labels/<song_id>.json` to GCS.
- After **every batch**: run `bash scripts/ops.sh backup`. This mirrors
  `state/`, `labels/`, `work/`, `exports/` to GCS and commits/pushes the text
  artifacts to the GitHub repo.
- Before ending a session: `bash scripts/ops.sh backup`, then `status.py`, and
  report the commit hash and GCS checkpoint.
- Never commit audio, ABCs, `cache/`, or `logs/` (they are in `.gitignore`).

---

## 6. Failure handling

| Symptom | Action |
|---|---|
| `prepare` shows `no_abc` | Expected for 4 tracks. Do not invent an ABC. Export them as `no_abc`. |
| `prepare` shows `missing_transcript` | Stop and tell the user; the corpus/GCS mapping needs a fix. |
| `analysis_error.json` | Read the error, record the song as `withheld` only if you can still read a report; otherwise leave it pending and report. |
| `parse <95%` | Withhold, mention "parse unreliable" in `withheld_reason`. |
| `name_allowed=false` | Withhold; quote the closest partial match as a possibility only. |
| Validator rejects a label | Read the exact error; lower confidence, add `tonic_alternatives`, switch to `possible`, or withhold. |
| GCS upload warning | Continue; the label is on local disk. Retry with `ops.sh backup` and report if it persists. |
| GitHub push fails (auth/network) | GCS still has the labels; fix credentials and retry `ops.sh backup`. |
| Two workers running | `ops.sh jobs`; `ops.sh stop prepare` before restarting. |

---

## 7. Reporting format

After a batch, report exactly this shape (short):

```
batch 006: 8 recorded (5 named, 3 withheld) | 55/163 total (33.7%)
confidence: low 41 | medium 14 | high 0 | needs review 55
backup: GCS ok at 12:34Z | git abc1234 pushed
next: batch 007 (8 songs) — continue?
```

Mention any disagreement or surprising label in one line. Do not paste the whole
packet or the whole report.

---

## 8. What not to do

- Do not run the 167-song loop in one turn without checkpoints.
- Do not claim the dataset is accurate; it has no ground truth. Report
  confidence distribution and, if run, blind QC agreement.
- Do not name Sikah/Huzam/Iraq or any unmodeled maqam as a finding; if the tonic
  itself is a quarter tone, the tool cannot model it — withhold.
- Do not edit `data/corpus.json`, `data/manifest.jsonl`, or the skill scripts.
- Do not use the audio files. They are not needed and the run must stay CPU-only.

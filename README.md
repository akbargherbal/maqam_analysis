# Maqam labels for 167 Elissa / Fadl Shaker songs

A resumable, backup-first pipeline that turns the **existing SheetSage2 ABC
transcriptions** of 167 Arabic pop songs into validated maqam weak labels using
the `maqam-analysis` skill.

**No audio processing and no GPU are required.** The ABCs already exist in
`gs://akbar-december-2024-backup/TRANSCRIPTS/`.

## What you get

| Output | Meaning |
|---|---|
| `labels/<song_id>.json` | one validated label per song, with evidence + provenance |
| `exports/maqam_labels.csv` | 167 rows; 163 labeled, 4 `no_abc` |
| `exports/maqam_labels.jsonl` | full label objects / gap records |
| `exports/summary.json`, `SUMMARY.md` | distributions and honest caveats |
| `exports/qc_report.md` | blind second-pass agreement (no ground truth) |
| `state/ledger.jsonl` | append-only record of every label event |

Labels are **weak labels**, not ground truth. The 12-TET ABC cannot prove
quarter tones, so maqamat such as Bayati, Rast, Saba and Sikah are marked
`possible`, never stated as fact. `withheld` is a valid label.

## Quick start (Google Colab)

```bash
# 1. Clone into /content
cd /content
git clone https://github.com/akbargherbal/maqam_analysis.git
cd maqam_analysis

# 2. Authenticate GCS (run this in a Colab cell, not bash)
#    from google.colab import auth
#    auth.authenticate_user()
#    !gcloud config set project <YOUR_PROJECT>

# 3. Bootstrap, restore any previous state, prepare evidence
bash scripts/bootstrap_colab.sh
bash scripts/ops.sh restore
bash scripts/ops.sh prepare

# 4. Check progress (never blocks)
python3 scripts/status.py
```

Then paste the prompt in [`COLAB_KICKSTART.md`](COLAB_KICKSTART.md) into the
agent chat.

## The labeling loop

```bash
python3 scripts/review.py packet --limit 8
# agent reads work/review/batch-NNN.md and fills batch-NNN.labels.json
python3 scripts/review.py validate --batch work/review/batch-NNN.json \
  --labels work/review/batch-NNN.labels.json
python3 scripts/review.py record --batch work/review/batch-NNN.json \
  --labels work/review/batch-NNN.labels.json
bash scripts/ops.sh backup
```

Each `record`:

1. validates the label against the skill's hard rules;
2. writes `labels/<song_id>.json` atomically;
3. appends a `state/ledger.jsonl` event;
4. uploads the label to GCS immediately;
5. rebuilds `state/progress.json`.

## Commands

| Command | Purpose |
|---|---|
| `python3 scripts/prepare.py` | fetch album JSONs, build manifest, extract ABCs, run analyzer |
| `python3 scripts/status.py` | one-shot progress report |
| `python3 scripts/review.py packet --limit 8` | next review packet + template |
| `python3 scripts/review.py validate ...` | validate without writing |
| `python3 scripts/review.py record ...` | validate + write + GCS upload |
| `python3 scripts/backup.py flush` | mirror to GCS + git commit/push |
| `python3 scripts/backup.py restore` | pull GCS/git, merge newer labels |
| `python3 scripts/export_dataset.py` | CSV/JSONL + summary |
| `python3 scripts/qc.py compare` | blind re-review agreement |
| `bash scripts/ops.sh prepare` | same as prepare, detached in background |
| `bash scripts/ops.sh status` | status without blocking |
| `bash scripts/ops.sh log prepare 80` | last 80 log lines |
| `bash scripts/ops.sh jobs` | running background jobs |
| `bash scripts/ops.sh stop prepare` | stop a background job |

## Resumability

Durable state is written after **every label** (GCS) and every batch (GCS mirror
+ git). On a new Colab runtime:

```bash
git clone ... && cd maqam_analysis
bash scripts/bootstrap_colab.sh
bash scripts/ops.sh restore
python3 scripts/status.py
```

`restore` merges labels by revision/timestamp, keeps conflicts in
`labels/_conflicts/`, and never deletes a newer local label. Songs with a label
are excluded from the next packet, so a disconnect mid-batch resumes with only
the remaining songs.

## Repository map

```
AGENTS.md              operating contract for the Colab agent
PLAN.md                full implementation plan, phases, risks, acceptance
COLAB_KICKSTART.md     copy-paste first message
config/config.json     paths, GCS prefixes, batch size, backup policy
data/corpus.json       167-song target list
data/manifest.jsonl    generated join (163 ok / 4 no_abc)
scripts/               pipeline, validator, backup, export, QC
skills/maqam-analysis/ unchanged analysis skill
docs/                  label schema, runbook, data notes
```

## Known limits

- **No ground truth.** Accuracy is unknown. The only quality signal is a blind
  re-review sample (`qc.py`), which measures agreement, not correctness.
- **12-TET input.** Quarter-tone maqamat are `possible` only. Nahawand vs
  Bayati and Ajam vs Rast cannot be separated from these ABCs.
- **4 tracks have no ABC** upstream and are exported as `no_abc`.
- **Tonic confidence is a consistency measure**, not a probability.
- **Audio and stems were unavailable**, so the f0 route in the skill
  (`analyze_f0.py`) is not used.

See [`PLAN.md`](PLAN.md) for the full design and [`docs/DATA_NOTES.md`](docs/DATA_NOTES.md)
for the corpus inventory.

# Runbook — maqam-167-v1

All commands run from the repository root (`/content/maqam_analysis` in
Colab). The `ops.sh` wrapper starts long jobs in the background and returns
immediately. Never use `sleep` or `tail -f`.

## 0. GitHub push credentials

`backup.py` commits text artifacts locally and pushes them to `origin`. In
Colab, configure git credentials once so the push does not prompt:

```bash
git config --global credential.helper store
git push origin main     # enter a personal access token when prompted
```

GCS backs up every label regardless of git credentials. If a push fails, the
GCS checkpoint still preserves the work.

## 1. First session

```bash
cd /content
git clone https://github.com/akbargherbal/maqam_analysis.git
cd maqam_analysis

# In a Colab cell:
# from google.colab import auth; auth.authenticate_user()
# !gcloud config set project YOUR_PROJECT_ID
# !bash scripts/bootstrap_colab.sh

bash scripts/ops.sh restore       # safe no-op on a fresh run
bash scripts/ops.sh prepare       # fetch 23 JSONs, build manifest, analyze
```

Check without blocking:

```bash
python3 scripts/status.py
bash scripts/ops.sh log prepare 80
bash scripts/ops.sh jobs
```

Expected after prepare:

```
labels: 0/163 (0.0%)   remaining: 163
pipeline: prepared 163/163 | analyzed 163/163 | parse<95% 0
ABC gaps: 4 no_abc | 0 missing transcript
```

## 2. One labeling batch

```bash
python3 scripts/review.py packet --limit 8
```

This writes:

- `work/review/batch-NNN.md` — the evidence packet;
- `work/review/batch-NNN.json` — batch metadata and evidence hashes;
- `work/review/batch-NNN.labels.json` — the template to fill.

Fill the template, then:

```bash
python3 scripts/review.py validate \
  --batch work/review/batch-NNN.json \
  --labels work/review/batch-NNN.labels.json

python3 scripts/review.py record \
  --batch work/review/batch-NNN.json \
  --labels work/review/batch-NNN.labels.json

bash scripts/ops.sh backup
```

`record` prints per-song results and the new progress. `backup` runs in the
background; check `status` or `log backup 80` on the next turn.

## 3. Backup and restore

```bash
# mirror state/labels/work/exports to GCS and commit/push git
bash scripts/ops.sh backup

# inspect last checkpoint
python3 scripts/backup.py check

# restore on a new runtime (git pull + GCS overlay)
bash scripts/ops.sh restore
python3 scripts/status.py
```

Restore rules:

- remote label newer than local → local copied to `labels/_conflicts/`, remote
  installed;
- local newer → local kept, remote copied to `_conflicts/`;
- identical → nothing;
- missing work/state files → copied;
- `state/progress.json` is rebuilt from disk.

## 4. Resume drill (do this once)

1. Note `python3 scripts/status.py` output (e.g. 47/163, next batch 007).
2. Disconnect / restart the Colab runtime.
3. Pre-flight cells 1-3, then:
   ```bash
   bash scripts/ops.sh restore
   python3 scripts/status.py
   ```
4. Confirm the same labeled count and next batch. No song is reprocessed.
5. Record the result in the session notes.

## 5. Blind QC

```bash
python3 scripts/review.py packet --qc --limit 20
# fill work/qc/qc-001.labels.json WITHOUT reading labels/
python3 scripts/review.py record --qc \
  --batch work/qc/qc-001.json \
  --labels work/qc/qc-001.labels.json
python3 scripts/qc.py compare
```

`exports/qc_report.md` reports exact maqam agreement, tonic agreement and
coarse named-vs-withheld agreement. This is **not accuracy**.

## 6. Export and Plotly analysis

```bash
bash scripts/ops.sh export
python3 scripts/plot_labels.py
# open exports/plots/index.html
```

`plot_labels.py` writes the interactive dashboard plus individual HTML views
under `exports/plots/` and a tidy `label_data.csv`. `notebooks/02_label_analysis.ipynb`
shows the main charts inline.

Outputs:

- `exports/maqam_labels.csv` — 167 rows (163 labeled, 4 `no_abc`);
- `exports/maqam_labels.jsonl` — full objects / gap records;
- `exports/summary.json` — distributions, duplicate groups, caveats;
- `exports/SUMMARY.md` — human-readable summary.

## 7. Failure handling

| Symptom | Cause | Action |
|---|---|---|
| `status` says "No manifest yet" | prepare not run | `ops.sh prepare` |
| `prepare` exits with GCS error | Colab auth expired | re-run `auth.authenticate_user()`, `gcloud config set project`, retry |
| `[manifest] ... missing_transcript` | corpus/GCS mismatch | stop; inspect `data/transcripts_index.json`; report |
| `no_abc` for 4 tracks | upstream transcription failure | expected; export as `no_abc` |
| `work/<id>/analysis_error.json` | analyzer failed on an ABC | read the error; leave pending or withhold with a reason; report |
| validator: parse <95% | broken ABC | withhold |
| validator: `name_allowed=False` | no single scale | withhold |
| validator: quarter-tone `consistent` | rule violation | use `possible` |
| validator: confidence too high | rule violation | lower it |
| `record` says "already labeled" | duplicate attempt | skip, or `--revise --reason` |
| GCS upload warning | network/auth | label is local; retry `ops.sh backup`; report if persistent |
| git push fails | credentials or network | GCS still has the labels; retry `ops.sh backup` after fixing credentials |
| two prepares running | double start | `ops.sh jobs`, `ops.sh stop prepare`, restart |
| status shows stale labels | evidence hash changed | revise with a reason; do not delete |

## 8. State files

| Path | Role |
|---|---|
| `data/manifest.jsonl` | 167-song source of truth |
| `labels/<song_id>.json` | durable label |
| `state/ledger.jsonl` | append-only event log |
| `state/progress.json` | derived cache; rebuild with `status.py --reconcile` |
| `state/run.json` | run id, corpus/config/skill hashes |
| `state/backup.json` | last GCS/git checkpoint (gitignored) |
| `work/<song_id>/evidence.json` | the evidence a label was based on |
| `work/review/batch-NNN.*` | packet/template/recorded batch |

## 9. Command index

```bash
python3 scripts/prepare.py [--refresh] [--force] [--limit N] [--offline]
python3 scripts/status.py [--json] [--reconcile]
python3 scripts/review.py packet [--limit N] [--order uncertainty] [--qc]
python3 scripts/review.py validate --batch F --labels F
python3 scripts/review.py record   --batch F --labels F [--revise --reason S] [--backup]
python3 scripts/backup.py flush [--dry-run] [--no-git] [--no-gcs]
python3 scripts/backup.py restore [--source auto|gcs|git]
python3 scripts/backup.py check
python3 scripts/export_dataset.py [--labeled-only]
python3 scripts/qc.py compare
bash scripts/ops.sh {prepare|restore|backup|status|packet|validate|record|export|qc|log|jobs|stop}
```

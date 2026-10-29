# Colab kickstart

## 1. Pre-flight (run these once, in Colab)

```python
# Cell 1 — get the repo
%cd /content
!git clone https://github.com/akbargherbal/maqam_analysis.git
%cd /content/maqam_analysis
```

To let `backup.py` push checkpoints from Colab, configure GitHub credentials
once (a personal access token with repo write access):

```bash
git config --global credential.helper store
git push origin main     # enter the token when prompted; it is cached
```

GCS backs up every label even if git push is not configured.

```python
# Cell 2 — authenticate Google Cloud Storage
from google.colab import auth
auth.authenticate_user()
!gcloud config set project YOUR_PROJECT_ID
```

```bash
# Cell 3 — install/check everything and run a smoke test
!bash scripts/bootstrap_colab.sh
```

You do **not** need to download `DISCOGRAPHY/` or any audio. The 23 existing
SheetSage2 album JSONs are the input.

---

## 2. Paste this into the agent chat

Copy everything in the block below as your first message. It works for a fresh
run and for a resume after a disconnect.

```text
You are the labeling agent for the maqam-167-v1 run in /content/maqam_analysis.
Read AGENTS.md and PLAN.md in full before doing anything, then load/read
skills/maqam-analysis/SKILL.md and references/maqamat.md.

Mission: produce one validated maqam label for each of the 163 songs that has a
usable ABC. Four tracks have no ABC upstream; they stay `no_abc` and are not
labeled. There is no ground truth and no audio. This is a weak-label dataset:
never present a maqam as a fact from 12-TET ABC, and use `possible` for every
quarter-tone maqam (Rast, Bayati, Saba, Sikah, Huzam, Iraq, Awj Ara, Suznek,
Jiharkah, Bastanikar). Withhold when the analyzer says `name_allowed=false`,
parse <95%, too few pitch classes, or no single scale. Evidence is the ABC only;
do not use outside knowledge of the song or artist.

Operating rules:
1. The Colab VM is ephemeral. Durability comes from a GCS upload after every
   label (`review.py record` does this) and `bash scripts/ops.sh backup` after
   every batch. Never end a session without a backup and a status report.
2. Never block the chat. Do not use sleep, tail -f, watch, or long foreground
   commands. Long jobs go through `bash scripts/ops.sh prepare|restore|backup`,
   which returns immediately with a PID and a log path. Check with
   `bash scripts/ops.sh status`, `jobs`, or `log <name> 80`.
3. Work in batches of 8. For each batch: `review.py packet --limit 8`, read
   work/review/batch-NNN.md, fill the sibling .labels.json, run
   `review.py validate`, then `review.py record`, then `ops.sh backup`. Report
   progress and ask me before starting the next batch unless I say "run
   autonomously".
4. Never edit ABCs or label JSON by hand. Labels are written only through
   `scripts/review.py record`, which validates, versions and backs them up.
5. Never reprocess a song that already has a label. If status reports a stale
   label, revise it with a reason; do not delete it.

Start now:
- Run `bash scripts/ops.sh restore` first (safe even on a fresh run), then
  `python3 scripts/status.py`.
- If status says the manifest is missing, start `bash scripts/ops.sh prepare`
  and check `bash scripts/ops.sh log prepare 80` plus status on the next turn.
  If prepare is already running, do not start a second copy.
- Report in one compact block: labeled/163, remaining, prepared/analyzed,
  next batch, backup state, any no_abc or analysis failures.
- Then build the first packet, summarise the 8 songs in a few lines, and begin
  labeling. Stop and ask me before batch 2.
```

---

## 3. What a good turn looks like

```
status: 47/163 labeled | prepared 163 | analyzed 163 | next batch 007
backup: GCS ok at 12:34Z | git a1b2c3d pushed
batch 007: 8 recorded (5 named, 2 possible, 1 withheld) | 55/163 total (33.7%)
confidence: low 41 | medium 14 | high 0 | needs review 55
note: three songs have a tonic/dominant split; all three list both tonics.
next: batch 008 — continue?
```

## 4. If the session dies

Start a new Colab runtime, run pre-flight cells 1-3, then paste the same prompt.
`ops.sh restore` merges the GCS labels and the next packet automatically skips
already-labeled songs. Nothing is reprocessed.

## 5. If `gcloud` is not authenticated

The bootstrap exits with instructions. Run:

```python
from google.colab import auth
auth.authenticate_user()
!gcloud config set project YOUR_PROJECT_ID
!gcloud storage ls gs://akbar-december-2024-backup/TRANSCRIPTS/
```

Then rerun `bash scripts/bootstrap_colab.sh`.

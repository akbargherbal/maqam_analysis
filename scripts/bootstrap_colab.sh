#!/usr/bin/env bash
# One-time Colab bootstrap. Run from /content/maqam_analysis.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."

echo "== maqam-167 bootstrap =="
echo "repo: $PWD"
python3 --version

echo "== Python deps =="
python3 -m pip install -q -r requirements.txt

chmod +x scripts/ops.sh scripts/bootstrap_colab.sh

echo "== gcloud =="
if ! command -v gcloud >/dev/null 2>&1; then
  echo "ERROR: gcloud not found. In Colab run:" >&2
  echo "  from google.colab import auth; auth.authenticate_user()" >&2
  echo "  !gcloud config set project <YOUR_PROJECT>" >&2
  exit 1
fi
PROJECT="$(gcloud config get-value project 2>/dev/null || true)"
echo "project: ${PROJECT:-(unset)}"
if [[ -z "${PROJECT:-}" || "$PROJECT" == "(unset)" ]]; then
  echo "WARNING: no gcloud project. Set one before prepare." >&2
fi

echo "== GCS access =="
if ! gcloud storage ls "gs://akbar-december-2024-backup/TRANSCRIPTS/" >/dev/null 2>&1; then
  echo "ERROR: cannot list gs://akbar-december-2024-backup/TRANSCRIPTS/" >&2
  echo "Run in a Colab cell first:" >&2
  echo "  from google.colab import auth; auth.authenticate_user()" >&2
  echo "  !gcloud config set project <YOUR_PROJECT>" >&2
  exit 1
fi
echo "transcripts: reachable"
if gcloud storage ls "gs://akbar-december-2024-backup/DISCOGRAPHY/" >/dev/null 2>&1; then
  echo "discography: reachable (not needed for this run)"
fi

echo "== git identity =="
if ! git config user.name >/dev/null 2>&1; then
  git config user.name "maqam-agent"
  echo "set local git user.name=maqam-agent"
fi
if ! git config user.email >/dev/null 2>&1; then
  git config user.email "maqam-agent@localhost"
  echo "set local git user.email=maqam-agent@localhost"
fi

echo "== repository visibility =="
python3 - <<'PY'
import sys
from pathlib import Path
sys.path.insert(0, str(Path("scripts").resolve()))
from backup import remote_url
from common import github_visibility
url = remote_url("origin")
if not url:
    print("WARNING: no git remote 'origin'")
else:
    private = github_visibility(url)
    if private is False:
        print("WARNING: the GitHub remote is PUBLIC. git push will be refused.")
        print("         Make it private before relying on GitHub as a backup.")
    elif private is True:
        print("github: private (ok)")
    else:
        print("github: visibility unknown (API limit or no network); GCS is still the primary backup")
PY

echo "== directory layout =="
mkdir -p cache state labels work logs exports data/abc data/abc_melody

echo "== local smoke test (skill analyzer) =="
python3 skills/maqam-analysis/scripts/analyze_abc.py \
  tests/fixtures/elissa-baddy-doub.abc --voice Vocal --brief --no-sections >/tmp/maqam_smoke.txt
head -n 8 /tmp/maqam_smoke.txt

echo ""
echo "Bootstrap complete."
echo "Next: bash scripts/ops.sh restore"
echo "Then: bash scripts/ops.sh prepare"
echo "Then: python3 scripts/status.py"

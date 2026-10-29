#!/usr/bin/env bash
# Background-first operations for the Colab agent.
#
#   bash scripts/ops.sh prepare
#   bash scripts/ops.sh status
#   bash scripts/ops.sh log prepare 80
#   bash scripts/ops.sh packet --limit 8
#   bash scripts/ops.sh backup
#   bash scripts/ops.sh restore
#
# Long jobs (prepare, restore, backup) are detached with setsid+nohup. The
# command returns immediately with a PID and a log path. Never tail -f; read
# the log with `log <name> [lines]` or check `status`.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
mkdir -p logs state cache

COMMAND="${1:-help}"
if [[ $# -gt 0 ]]; then shift; fi

start_bg() {
  local name="$1"; shift
  local pid_file="state/${name}.pid"
  if [[ -f "$pid_file" ]]; then
    local old
    old="$(cat "$pid_file" 2>/dev/null || true)"
    if [[ -n "${old:-}" ]] && kill -0 "$old" 2>/dev/null; then
      echo "already running: $name pid $old (log logs/${name}.log)"
      return 0
    fi
    rm -f "$pid_file"
  fi
  setsid nohup "$@" >"logs/${name}.log" 2>&1 < /dev/null &
  local pid=$!
  echo "$pid" >"$pid_file"
  echo "started $name pid $pid"
  echo "log: logs/${name}.log"
  echo "check: bash scripts/ops.sh status"
}

case "$COMMAND" in
  prepare)
    start_bg prepare python3 scripts/prepare.py "$@"
    ;;
  restore)
    start_bg restore python3 scripts/backup.py restore "$@"
    ;;
  backup)
    start_bg backup python3 scripts/backup.py flush "$@"
    ;;
  status)
    python3 scripts/status.py "$@"
    ;;
  packet)
    python3 scripts/review.py packet "$@"
    ;;
  validate)
    python3 scripts/review.py validate "$@"
    ;;
  record)
    python3 scripts/review.py record "$@"
    ;;
  export)
    python3 scripts/export_dataset.py "$@"
    ;;
  qc)
    python3 scripts/qc.py "$@"
    ;;
  log)
    name="${1:-prepare}"
    lines="${2:-80}"
    if [[ ! -f "logs/${name}.log" ]]; then
      echo "no log: logs/${name}.log" >&2
      exit 2
    fi
    tail -n "$lines" "logs/${name}.log"
    ;;
  jobs)
    python3 - <<'PY'
import os
from pathlib import Path
found = False
for p in sorted(Path("state").glob("*.pid")):
    try:
        pid = int(p.read_text().strip())
        os.kill(pid, 0)
    except Exception:
        continue
    found = True
    print(f"{p.stem}: pid {pid} (log logs/{p.stem}.log)")
if not found:
    print("no background jobs running")
PY
    ;;
  stop)
    name="${1:?usage: ops.sh stop <name>}"
    pid_file="state/${name}.pid"
    if [[ ! -f "$pid_file" ]]; then echo "no pid file: $pid_file" >&2; exit 2; fi
    pid="$(cat "$pid_file")"
    kill "$pid" 2>/dev/null || true
    rm -f "$pid_file"
    echo "stopped $name (pid $pid)"
    ;;
  help|--help|-h)
    sed -n '1,20p' "$0" | grep '^#' | sed 's/^# \{0,1\}//'
    ;;
  *)
    echo "unknown command: $COMMAND" >&2
    echo "try: bash scripts/ops.sh help" >&2
    exit 2
    ;;
esac

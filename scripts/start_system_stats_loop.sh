#!/bin/zsh
set -euo pipefail
cd /Users/bob/.openclaw/workspace
mkdir -p .runtime
if [[ -f .runtime/system_stats_loop.pid ]]; then
  pid=$(cat .runtime/system_stats_loop.pid 2>/dev/null || true)
  if [[ -n "${pid}" ]] && kill -0 "$pid" 2>/dev/null; then
    echo "already running: $pid"
    exit 0
  fi
fi
nohup zsh -lc 'cd /Users/bob/.openclaw/workspace; while true; do /usr/bin/python3 scripts/update_system_stats.py >/dev/null 2>&1; sleep 2; done' > .runtime/system_stats_loop.log 2>&1 &
echo $! > .runtime/system_stats_loop.pid
echo "started: $(cat .runtime/system_stats_loop.pid)"
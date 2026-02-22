#!/bin/zsh
set -euo pipefail
cd /Users/bob/.openclaw/workspace
if [[ ! -f .runtime/system_stats_loop.pid ]]; then
  echo "not running"
  exit 0
fi
pid=$(cat .runtime/system_stats_loop.pid 2>/dev/null || true)
if [[ -n "${pid}" ]] && kill -0 "$pid" 2>/dev/null; then
  kill "$pid" || true
  sleep 0.2
fi
rm -f .runtime/system_stats_loop.pid
echo "stopped"
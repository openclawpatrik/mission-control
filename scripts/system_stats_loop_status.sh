#!/bin/zsh
set -euo pipefail
cd /Users/bob/.openclaw/workspace
if [[ -f .runtime/system_stats_loop.pid ]]; then
  pid=$(cat .runtime/system_stats_loop.pid 2>/dev/null || true)
  if [[ -n "${pid}" ]] && kill -0 "$pid" 2>/dev/null; then
    echo "running: $pid"
    exit 0
  fi
fi
echo "stopped"
#!/bin/zsh
set -euo pipefail
cd /Users/bob/.openclaw/workspace
if [[ -f .runtime/stats_api.pid ]]; then
  pid=$(cat .runtime/stats_api.pid 2>/dev/null || true)
  if [[ -n "${pid}" ]] && kill -0 "$pid" 2>/dev/null; then
    echo "running: $pid"
    exit 0
  fi
fi
echo "stopped"
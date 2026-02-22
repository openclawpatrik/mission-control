#!/bin/zsh
set -euo pipefail
cd /Users/bob/.openclaw/workspace
if [[ ! -f .runtime/stats_api.pid ]]; then
  echo "not running"
  exit 0
fi
pid=$(cat .runtime/stats_api.pid 2>/dev/null || true)
if [[ -n "${pid}" ]] && kill -0 "$pid" 2>/dev/null; then
  kill "$pid" || true
  sleep 0.2
fi
rm -f .runtime/stats_api.pid
echo "stopped"
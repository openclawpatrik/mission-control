#!/bin/zsh
set -euo pipefail
cd /Users/bob/.openclaw/workspace
mkdir -p .runtime
if [[ -f .runtime/stats_api.pid ]]; then
  pid=$(cat .runtime/stats_api.pid 2>/dev/null || true)
  if [[ -n "${pid}" ]] && kill -0 "$pid" 2>/dev/null; then
    echo "already running: $pid"
    exit 0
  fi
fi
export STATS_API_HOST="${STATS_API_HOST:-127.0.0.1}"
export STATS_API_PORT="${STATS_API_PORT:-8787}"
export STATS_API_KEY="${STATS_API_KEY:-}"
export STATS_API_CORS="${STATS_API_CORS:-*}"
nohup /usr/bin/python3 scripts/stats_api_server.py > .runtime/stats_api.log 2>&1 &
echo $! > .runtime/stats_api.pid
echo "started: $(cat .runtime/stats_api.pid)"
#!/bin/zsh
set -euo pipefail
cd /Users/bob/.openclaw/workspace
if [[ $# -lt 1 ]]; then
  echo "Usage: ./scripts/analyze_youtube.sh <youtube-url>"
  exit 1
fi
URL="$1"
MODEL="${2:-base}"
/Users/bob/.openclaw/workspace/scripts/youtube_fitzworks_analyzer.py "$URL" --model "$MODEL"

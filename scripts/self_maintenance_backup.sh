#!/usr/bin/env bash
set -euo pipefail

ROOT="/Users/bob/.openclaw/workspace"
TS="$(date +%F_%H%M%S)"
OUT="$ROOT/backups/$TS"
mkdir -p "$OUT"

copy_if_exists () {
  local src="$1"
  if [ -e "$src" ]; then
    cp -R "$src" "$OUT/"
  fi
}

copy_if_exists "$ROOT/AGENTS.md"
copy_if_exists "$ROOT/BOOTSTRAP.md"
copy_if_exists "$ROOT/SOUL.md"
copy_if_exists "$ROOT/MEMORY.md"
copy_if_exists "$ROOT/KANBAN.json"
copy_if_exists "$ROOT/KANBAN_ARCHIVE.json"
copy_if_exists "$ROOT/NOTES.md"
copy_if_exists "$ROOT/USER.md"
copy_if_exists "$ROOT/USER_PROFILE.md"
copy_if_exists "$ROOT/memory"
copy_if_exists "$ROOT/scripts"

# lightweight manifest
{
  echo "timestamp=$TS"
  echo "host=$(hostname)"
  echo "pwd=$ROOT"
} > "$OUT/manifest.txt"

echo "backup_done:$OUT"

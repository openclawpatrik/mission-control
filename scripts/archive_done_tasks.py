#!/usr/bin/env python3
import json
from datetime import datetime, timedelta
from pathlib import Path

KANBAN = Path('KANBAN.json')
ARCHIVE = Path('KANBAN_ARCHIVE.json')


def parse_iso(s):
    if not s:
        return None
    try:
        return datetime.fromisoformat(s)
    except Exception:
        return None


def main():
    if not KANBAN.exists():
        print('KANBAN.json missing')
        return

    board = json.loads(KANBAN.read_text(encoding='utf-8'))
    archive = {"version": "1.0", "archived": []}
    if ARCHIVE.exists():
        archive = json.loads(ARCHIVE.read_text(encoding='utf-8'))
        archive.setdefault('archived', [])

    done = board.get('columns', {}).get('done', [])
    keep = []
    moved = []
    now = datetime.now().astimezone()
    cutoff = now - timedelta(days=3)

    for task in done:
      stamp = parse_iso(task.get('updated_at')) or parse_iso(task.get('created_at'))
      if stamp and stamp < cutoff:
          moved_task = dict(task)
          moved_task['archived_at'] = now.isoformat()
          archive['archived'].append(moved_task)
          moved.append(task.get('id'))
      else:
          keep.append(task)

    board['columns']['done'] = keep
    board['updated_at'] = now.isoformat()

    KANBAN.write_text(json.dumps(board, ensure_ascii=False, indent=2), encoding='utf-8')
    ARCHIVE.write_text(json.dumps(archive, ensure_ascii=False, indent=2), encoding='utf-8')

    print(f'archived={len(moved)}')


if __name__ == '__main__':
    main()

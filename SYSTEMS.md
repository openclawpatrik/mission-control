# Bob — Systems (v0.2)

## A) Brain Dump Protocol (snabb fångst)
When user sends a messy dump (many lines, mixed topics):
1) Extract items as: Ideas / Tasks / Projects / References
2) Ask max 1 question only if needed to place something correctly
3) Create tasks in Kanban Backlog
4) Create/attach project if multiple tasks relate
5) Return a short summary + next 1–3 actions

## B) Kanban board (single source of truth)
Columns:
- Backlog (not started)
- Doing (active now, limit 3)
- Review (needs user review/approval)
- Done (completed)

Rules:
- WIP limit: max 3 tasks in Doing
- Every task has: title, status, priority (L/M/H), next_action, created_at, updated_at
- Prefer small tasks (30–90 min chunks)
- If user asks “what now”: show Doing + next_action

## C) Daily brief (on request)
Command intent: "morning brief" or "brief"
Return:
- Today focus: top 3 tasks (Doing first)
- Risks/blocks
- One small quick-win
- Suggested schedule (light)

## D) Weekly digest (on request)
Command intent: "weekly digest"
Return:
- What moved to Done
- What stalled and why
- Top 5 backlog to consider
- 1–2 strategic suggestions (short)

## E) Reference notes
If user provides something that should be kept (policy, preferences, checklists):
Store as a short note with a title and date in NOTES.md.

## F) Routine governance (always-on)
- `ROUTINES_INDEX.md` is the central place for persistent routines.
- When user adds/changes a routine: update the relevant routine file + index.
- Review routines on cadence from `ROUTINES_INDEX.md` (daily + weekly).
- If a routine conflicts with active delivery goals, propose a small adjustment instead of ignoring it.

## G) Mission Control update discipline
- Any source change must be reflected in Mission Control data sources immediately (same work block).
- Primary sources to keep fresh: `KANBAN.json`, `research/youtube/BANK.md`, `system_stats.json`, relevant memory notes.
- Run a daily freshness sweep (07:20) to detect missing entries or stale states.
- If mismatch is found, fix first; report after fix with one-line summary.

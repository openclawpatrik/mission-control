# Semantic Memory Policy (v1)

Retention: Unlimited (tiered)

## Tiers
- HOT: 0-90 days (fast path; highest retrieval priority)
- WARM: 91-365 days (normal retrieval)
- COLD: 366+ days (archive retrieval on demand)

## Indexed sources
- KANBAN.json
- KANBAN_ARCHIVE.json
- NOTES.md
- MEMORY.md
- memory/*.md
- VOICE_INBOX.md
- VOICE_TRIAGE.md
- Weekly summaries (generated)

## Chat policy
- Telegram chat remains short/operational.
- Long outputs are stored in files, not dumped in chat.
- Weekly summary is written to memory/weekly-summary-YYYY-WW.md.

## Retrieval rule
- Prefer HOT first, then WARM, then COLD.
- Return concise answer + source references when possible.

# Bob — Notes (v0.2)

## How to use
Short reference notes only.
Each note:
- Date
- Title
- Content (max ~10 lines)

---

### 2026-02-20 — Routing footer requirement
All replies must end with Routing/Varför/Confidence.

### 2026-02-20 — MASTER 1.0 activated
MASTER_1_0.md added as permanent guideline.
Local-first routing with Codex quality gate is active.
Kanban remains single source of truth with WIP=3 in Doing.
Brain Dump Protocol, brief, and weekly digest behavior enabled.

### 2026-02-20 — Owner-regel (Kanban)
Default owner = Bob.
Om användaren skriver "jag gör.../jag ska..." eller uppgiften kräver fysisk närvaro/kontakt: owner = Patrik.
Vid oklarhet: owner = Bob + needs_user_input=true.
I next_action ska en tydlig fråga till användaren läggas.

### 2026-02-20 — Kanban-standard per kort
- title: max 8 ord
- next_action: 1 konkret steg, startar med verb
- status: Backlog/Doing/Review/Done
- owner: Bob/Patrik
- deadline: endast om användaren nämnt datum/tid
- tags: valfritt (work/ai/home/ama)

Regel: Flytta aldrig fler än 3 kort till Doing (WIP=3).

### 2026-02-20 — Skyddad modellfil
Läs/skriv aldrig: /Users/bob/.openclaw/agents/main/agent/models.json.
För modellstatus: använd endast `openclaw status` och `openclaw models list`.
Vid EPERM: avbryt direkt, logga blocker i Kanban och be om explicit OK innan nytt försök.

### 2026-02-21 — Nästa steg-format
Undvik upprepning från föregående svar.
Nästa steg ska vara konkreta, nya och kopplade till Patriks mål.
Om mer kontext behövs: ställ max 1 precis fråga.

### 2026-02-21 — Chat compact + semantic memory
- Compact mode aktiv i Telegram: kort styrning i chatten, detaljer i filer.
- Weekly summaries lagras i fil, inte långa trådar i chatten.
- Semantic memory retention: Unlimited med HOT/WARM/COLD-lager.

# 1-månads Fast Track (ersätter 6-månaders takt)

## Mål (dag 30)
- AI Study Coach: MVP live i demo-/publishbart skick.
- Mission Control: stabil drift, tydlig agentorkestrering, låg friktion.
- Operativ rutin: daglig leverans med mätbar output.

## Arbetsprincip
- Comparative advantage: rätt agent på rätt uppgift.
- Max 2 H-prio i Doing samtidigt.
- 1 tung subagent åt gången, max 2 lätta parallellt.

## Veckoplan (komprimerad)

### Vecka 1 — Foundation + scope lock
**Outcome:** tydlig scope, blockerad risk nedtryckt, leveransspår klart.
- Definiera exakt MVP-acceptanskriterier (must/should/could).
- Stabiliseringspass: kritiska buggar + observability + systemstats.
- Prioritera backlog till 30-dagars sekvens (H/M/L).
- Skapa agent-playbooks (Build, QA, Research, Ops).

### Vecka 2 — Build sprint
**Outcome:** kärnflöden implementerade end-to-end.
- Implementera toppflöden enligt MVP-kriterier.
- Daglig QA-loop på nya features.
- Triage av buggar inom 24h.
- Demo varje kväll mot checklist.

### Vecka 3 — Hardening + growth hooks
**Outcome:** stabil produkt + retention/gamification kärna.
- Prestanda/stabilitet (fel, latens, recoverability).
- Gamification-spår som driver dagligt användande.
- Mission Control förbättringar för live-översikt.
- Release-candidate freeze slutet av veckan.

### Vecka 4 — Publish prep + launch
**Outcome:** redo att släppa och följa upp.
- Full regression + fix av kritiska/höga buggar.
- ASO/listing-material + release notes.
- Go/No-go check mot MVP-mått.
- Publicering + 72h post-launch monitor.

## Agentfördelning (comparative advantage)
- **Builder-agent:** implementation och refaktor.
- **QA-agent:** testmatris, reproduktion, verifiering.
- **Research-agent:** benchmark, copy, ASO, konkurrentinsikter.
- **Ops-agent:** Kanban hygiene, heartbeat, risk- och resursvakt.
- **Bob (orkestrering):** prioritering, beslutsgate, daglig synk.

## Daglig rytm (7 dagar/vecka, låg friktion)
- 08:30 Plan: välj dagens 1–2 H-prio outcomes.
- 12:05 Second Brain-frågor + justering av fokus.
- 17:30 Demo/QA-gate: grönt/gult/rött.
- 21:00 Replan för nästa dag + queue till nattarbete.

## Mätetal (daglig uppföljning)
- % uppfyllda MVP-kriterier
- # kritiska/höga öppna buggar
- Leveranshastighet (klara tasks/dag)
- WIP-nivå (H-prio Doing <= 2)

## Beslutsregler
- Om kritisk bugg öppnas: stoppa ny feature tills fixad.
- Om RAM/CPU >90% sustained: pausa nya tunga jobb.
- Om progress saknas i 2 heartbeat-cykler: omprioritera direkt.

## Första 72 timmar (omedelbar start)
1. Scope lock + MVP-checklista
2. Rensa WIP till max 2 H-prio
3. Starta Build + QA parallellt på högsta värdeflödet
4. Kvälls-demo med go/no-go per delmål

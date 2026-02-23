# HEARTBEAT.md
# FitzWorks heartbeat v2 (högsignal + låg resursrisk)

## Körschema
- Dagtid (08:00–22:00 Europe/Stockholm): heartbeat var 30:e minut.
- Natt (22:00–08:00): var 60:e minut, endast viktiga checks + progress.
- Om inget viktigt: svara endast `HEARTBEAT_OK`.
- Skicka inte löpande heartbeat-rapporter i chatten. Samla normal progress/förbättringar till morning daily brief.
- Skicka endast heartbeat-alert i realtid vid kritiskt läge (säkerhet, dataförlustrisk, ihållande resursrisk, blocker som kräver ägarbeslut).

## 1) Execution check (KANBAN + agentprogress)
Vid varje heartbeat:
1. Kolla KANBAN/KANBAN.json för H-prio arbete.
2. Flagga om:
   - >2 H-prio tasks i Doing (WIP-risk)
   - blockerad H-prio task utan recovery-plan
   - ingen mätbar progress sedan senaste kontroll
3. Föreslå max 1 konkret next action per flagga.

## 2) AI Study Coach quality gate (inför publishing)
Rapportera kort i 3 rader:
- Krav uppfyllda (% mot MVP-acceptanskriterier)
- Kritiska/Hög buggar (antal)
- Publishing readiness: RÖD / GUL / GRÖN

## 3) Agentarbete när Patrik sover/jobbar (asynk progression)
Mål: kontinuerligt arbete 24/7 utan att överbelasta Mac Mini.

Regler:
- Ha alltid minst 1 aktiv uppgift i kö/utförande över dygnet (24/7 täckning).
- Kör max 1 tung subagent i taget (research/coding med stor kontext).
- Lätta uppgifter kan köras parallellt max 2 st.
- Undvik att starta flera lokala modelljobb samtidigt.
- Om RAM/CPU är högt: pausa nya jobb, prioritera kö-ordning.

Prioriterad nattkö:
1. Research/brief-underlag
2. Test/QA-rapportering
3. Backlog-förberedelser för nästa dag

## 4) Resurs-/stabilitetsvakt
Om sustained usage >90% i 10 min (CPU/RAM/Disk/Net):
- Skicka alert med:
  1) vad som är högt,
  2) sannolik orsak,
  3) 1 rekommenderad åtgärd.
- Starta inte nya tunga körningar förrän läget stabiliserats.

## 5) Auto-update check för OpenClaw (officiell GitHub)
1 gång per dag (förslag 06:30):
1. Kolla senaste release från officiella OpenClaw GitHub.
2. Om ny version finns:
   - jämför med installerad version,
   - skicka kort changelog-sammanfattning,
   - ge rekommendation: uppdatera nu / vänta.
3. Auto-uppdatera INTE utan explicit godkännande från Patrik.

## 6) Vecko-avstämning (HEARTBEAT-förbättring)
1 gång per vecka:
1. Gå igenom HEARTBEAT-regler och utfall (signal vs brus).
2. Föreslå max 3 förbättringar för bättre effekt mot FitzWorks-mål.
3. Kontrollera att 24/7 arbetsflöde hålls utan resursöverbelastning.

## 7) GitHub sync (Mission Control)
Vid heartbeat:
1. Kontrollera om Mission Control-relaterade filer är ändrade lokalt.
2. Om ändringar finns: påminn/flagga att pusha till GitHub så remote är uppdaterad.
3. Prioritera att hålla repo i synk inför demo/publishing.

## Alert-format (alltid kort)
- Rubrik
- Varför det spelar roll
- 1 konkret next action
- Undvik upprepning: skicka inte samma alert igen om läget är oförändrat.

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
   - task med passerad deadline/ETA (overdue)
3. Vid overdue (alltid):
   - skicka omedelbar alert med antal + vilka tasks,
   - sätt recovery-plan (ägare + ny mini-deadline inom 24h),
   - prioritera om så högst 2 kritiska overdue åtgärdas först.
4. Föreslå max 1 konkret next action per flagga.

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
   - skapa backup först (status + version + workspace snapshot + ~/.openclaw snapshot),
   - kör uppdatering automatiskt,
   - verifiera med `openclaw status`,
   - skicka kort uppdateringsrapport med version före/efter + backup-sökväg.
3. Vid uppdateringsfel: behåll backup och skicka rollback-förslag som nästa action.

## 6) Vecko-avstämning (HEARTBEAT-förbättring)
1 gång per vecka:
1. Gå igenom HEARTBEAT-regler och utfall (signal vs brus).
2. Föreslå max 3 förbättringar för bättre effekt mot FitzWorks-mål.
3. Kontrollera att 24/7 arbetsflöde hålls utan resursöverbelastning.
4. Skicka kort rapport om Codex-tokenanvändning vs lokala modeller (trend + ev. åtgärd).

## 7) Mission Control freshness + GitHub sync
Vid heartbeat:
1. Kontrollera om Mission Control-relaterade filer är ändrade lokalt.
2. Om ändringar finns: uppdatera relevanta källfiler direkt (t.ex. KANBAN.json, research/youtube/BANK.md, notes) så Mission Control visar senaste läget.
3. Verifiera snabb freshness-check: att senaste ändring syns i datakällorna som Mission Control läser.
4. Om ändringar finns kvar lokalt: påminn/flagga att pusha till GitHub så remote är uppdaterad.

Daglig kontroll (förslag 07:20):
1. Kör en full genomgång av Mission Control-datakällor (tasks, stats, YouTube-bank, minnesreferenser).
2. Rätta avvikelser direkt (saknade poster, fel status, dubbletter).
3. Rapportera endast om något kräver beslut från Patrik.

## 8) Daily Second Brain dump (12:05 Europe/Stockholm)
Mål: förbättra förståelsen av Patrik för bättre beslut i FitzWorks.

Regler:
1. Skicka exakt kl 12:05 (lokal tid) 3 korta frågor i Telegram.
2. Frågorna ska rotera mellan: mål, energi/fokus, beslut, hinder, idéer, risk, värderingar, arbetsstil.
3. Frågorna ska vara olika från föregående dag (ingen repetitiv loop).
4. Spara svaren i minne/idébank och återanvänd i planering/agentstyrning.
5. Om dagens frågor redan skickats: skicka inte igen samma dag.

### Dagens frågor (2026-02-27):
1. Vad är en konkret mål som du vill uppnå under nästa 7 dagar?
2. Vilka arbetsmetoder ger dig bäst fokus när du löser komplexa problem?
3. Vilka tre hinder har du upplevt under senaste veckan som påverkade ditt arbete?

## 9) OpenHome DevKit svarspåminnelse (2 gånger/vecka)
Mål: säkra uppföljning på devkit-ansökan utan att skapa spam.

Regler:
1. Påminn Patrik tisdag + fredag dagtid om han fått svar på OpenHome DevKit-ansökan.
2. Om Patrik redan bekräftat svar samma vecka: skicka inte igen.
3. Om avslag/uteblivet svar >7 dagar: föreslå nästa steg (egen hårdvara + plan).

## Alert-format (alltid kort)
- Rubrik
- Varför det spelar roll
- 1 konkret next action
- Undvik upprepning: skicka inte samma alert igen om läget är oförändrat.

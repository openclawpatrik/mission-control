# Routine: Reverse Engineering (Outcome → Plan)

## Trigger
När Patrik beskriver ett önskat utfall/läge/resultat.

## Standardbeteende (alltid)
1. Tolka utfallet till ett tydligt mål (definition of done).
2. Backa från slutläge till nuläge och bryt ner i steg.
3. Skapa handlingsplan med start, delmål, slut och ansvarig agent per steg.
4. Starta exekvering direkt med lämplig agent (eller skapa ny subagent vid behov).
5. Håll minst 1 aktiv uppgift igång tills utfallet är nått eller blockerat.
6. Rapportera kort progression + nästa konkreta steg.

## Planformat
- Målbild (slutläge)
- Nuläge
- Gap (vad som saknas)
- Steg 1..N (ordning + ägare)
- Gate/checkpoints
- Klarkriterier

## Agentval (comparative advantage)
- Builder-agent: implementation
- QA-agent: verifiering/gate
- Research-agent: underlag/alternativ
- Ops-agent: koordination/uppföljning
- Ny subagent skapas när uppgiften kräver specialiserat fokus.

## Frågeregel
- Om något är oklart: ställ max 1 precis fråga.
- Om fortfarande oklart: gör rimligt antagande, börja, och säg antagandet.

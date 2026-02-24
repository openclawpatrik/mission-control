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

## Teori (från tanke → praktik)
Reverse engineering här betyder att vi utgår från önskat slutläge och arbetar baklänges till minsta möjliga startsteg.

Kärnprinciper:
- Slutbild först: definiera vad "klart" betyder i observerbara termer.
- Backcasting: identifiera milstolpar bakåt från målet till idag.
- Constraints first: synliggör begränsningar tidigt (tid, teknik, data, resurser).
- Risk-first sequencing: ta osäkerhet tidigt, skala det säkra efteråt.
- Smallest next action: varje steg ska kunna startas direkt.

## Praktisk tillämpning per typ av input
### 1) Idé ("det vore bra om...")
- Översätt till testbar hypotes + mini-experiment (24–72h).
- Mät: signal som visar om idén har bäring.
- Beslut: fortsätt / parkera / pivot.

### 2) Önskat resultat ("jag vill att X ska vara klart")
- Definiera DoD + deadline.
- Bryt ner till leverabler med ägare och checkpoints.
- Kör exekveringskedja tills DoD är uppnådd.

### 3) Problem/läge ("det här funkar inte")
- Definiera rotorsak-hypoteser.
- Prioritera åtgärder efter effekt/insats.
- Verifiera fix med tydligt acceptanskriterium.

### 4) Vision/strategi ("på sikt vill jag...")
- Bryt till 30-dagars outcome + veckodelmål.
- Knyt till KPI och beslutsgates.
- Starta med första konkretiserade arbetsstråket.

## Frågeregel
- Om något är oklart: ställ max 1 precis fråga.
- Om fortfarande oklart: gör rimligt antagande, börja, och säg antagandet.

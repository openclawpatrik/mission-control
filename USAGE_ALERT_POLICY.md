# Usage Alert Policy (Telegram)

## Trigger (sustained load)
Skicka alert om något av följande håller i sig under minst 10 minuter:
- CPU >= 90%
- RAM >= 90%
- Disk used >= 92%
- Network RX eller TX >= 8 MB/s (ihållande)

## Alert-innehåll
1) Vad som är högt (värde + duration)
2) Trolig orsak (process/top contributor)
3) Om det är planerat arbete (agentjobb) eller avvikelse/problem
4) Rekommenderad åtgärd (nu + nästa steg)

## Escalation
- Om samma trigger kvarstår >30 min: skicka uppföljningsalert
- Om flera triggers samtidigt: markera som hög prioritet

## Investigation hints
- Top process CPU/RAM via Activity Monitor / `top`
- Senaste aktiva tasks i Kanban för korrelation
- Kontrollera loops/hängning: ovanligt konstant CPU utan progress i tasks

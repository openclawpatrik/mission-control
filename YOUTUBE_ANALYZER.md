# YouTube Analyzer (FitzWorks)

## Syfte
Klistra in en YouTube-länk och få en svensk FitzWorks-analys:
- TLDR
- viktiga idéer
- konkret applicering i FitzWorks
- risker
- nästa steg idag

## Körning
```bash
cd /Users/bob/.openclaw/workspace
./scripts/analyze_youtube.sh "https://www.youtube.com/watch?v=..."
```

Valfri whisper-modell (snabbare/långsammare):
```bash
./scripts/analyze_youtube.sh "<url>" base
```

## Output
Sparas till:
- `research/youtube/<timestamp>_<title>_<id>.md`
- `research/youtube/BANK.md` (index över alla analyser, inkl NOW/BANK-status)

## Telegram-flöde
Skicka YouTube-länken i chatten så kör jag analysen och återkommer med applicerbar summary.

## Notering
- Kör lokalt med `yt-dlp` + `faster_whisper` + `ollama`.
- För långa videos kan körningen ta några minuter.

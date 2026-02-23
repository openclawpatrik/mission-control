# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.

## Web Search Ops (2026-02-23)

### Brave Search API — praktiska limits

- Vi fick live 429-svar med metadata:
  - plan: `Free`
  - `rate_limit`: `1` req/s
  - `quota_limit`: `2000` / månad
- Brave rate limiting guide beskriver:
  - 1-sekunders sliding window
  - 429 vid överskridning
  - headers för styrning: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`

### Arbetssätt för agenter (för att undvika 429)

1. Kör inte parallella `web_search`-anrop i onödan på Free-plan.
2. Lägg minst ~1.1–1.3 s mellan Brave-sökningar i samma flöde.
3. Återanvänd svar (cache-first) innan ny sökning.
4. Vid 429: backoff + retry (vänta enligt reset-header, annars 2s/4s/8s).
5. Begränsa `count` till minsta möjliga (ofta 3–5 räcker).

### Alternativa sökvägar i OpenClaw

- `web_search` provider kan sättas till **Perplexity** (direkt API eller via OpenRouter) i stället för Brave.
- `web_fetch` fungerar bra för att hämta kända URL:er direkt utan ny sökning.
- `browser` används när JS-tunga sidor eller inlogg krävs.

### Snabb routingregel

- Snabba länklistor: Brave.
- Syntetiserad research med källor: Perplexity.
- Direkt sidläsning: web_fetch.
- Komplex UI/inloggning: browser.

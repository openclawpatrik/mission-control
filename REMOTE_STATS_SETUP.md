# Remote live system usage for Mission Control (GitHub + mobile)

## Goal
Show real-time Mac mini usage in the GitHub-hosted Mission Control UI.

## How it works
- `system_stats.json` updates locally every 2s
- `stats_api_server.py` exposes that JSON over HTTP
- GitHub UI reads from `?stats_api=<URL>`

## 1) Start local producers
```bash
cd /Users/bob/.openclaw/workspace
./scripts/start_system_stats_loop.sh
./scripts/start_stats_api.sh
```

## 2) Verify locally
```bash
curl http://127.0.0.1:8787/healthz
curl http://127.0.0.1:8787/system_stats
```

## 3) Expose safely for mobile (recommended: Tailscale Funnel)
1. Install/login Tailscale on Mac mini
2. Start API bound on all interfaces with API key:
```bash
cd /Users/bob/.openclaw/workspace
./scripts/stop_stats_api.sh
STATS_API_HOST=0.0.0.0 STATS_API_PORT=8787 STATS_API_KEY='CHANGE_ME_LONG_RANDOM' STATS_API_CORS='*' ./scripts/start_stats_api.sh
```
3. Expose with funnel:
```bash
tailscale funnel 8787
```
4. Copy funnel URL (example `https://abc123.ts.net`)

## 4) Open Mission Control from GitHub with remote stats source
Use URL:
```
https://<your-github-pages-or-raw-view>/mission_control.html?stats_api=https://abc123.ts.net/system_stats
```

Then set token once in browser console:
```js
localStorage.setItem('mc_stats_token','CHANGE_ME_LONG_RANDOM')
```
Reload page.

## Stop commands
```bash
./scripts/stop_stats_api.sh
./scripts/stop_system_stats_loop.sh
```

## Notes
- If stats are stale, check `scripts/stats_api_status.sh` and `scripts/system_stats_loop_status.sh`
- For stricter CORS, replace `*` with your exact Mission Control origin.

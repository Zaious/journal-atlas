# Deploying the demo

Written for `journal-atlas.chroniclecore.com` behind Cloudflare. Substitute your
own hostnames if you fork this.

## Shape

Two hostnames, not one:

```
journal-atlas.chroniclecore.com      → static frontend (Cloudflare Pages)
api.journal-atlas.chroniclecore.com  → FastAPI backend (your own host, proxied)
```

The split is forced rather than chosen: Cloudflare Pages and Workers cannot run
this backend. It is FastAPI with long-lived SSE streams and the `google-genai`
SDK, and it reads the 399-entry corpus off disk at request time. It needs a
normal Python process.

Serving both from one hostname would mean a Worker or Pages Function proxying
`/api/*` to the origin — an extra hop that adds another place for SSE to get
buffered, for no gain. Two hostnames also let CORS name exactly one origin
instead of a wildcard.

## Backend

Any host that runs a long-lived Python process works: your own VPS behind
Caddy or nginx, Fly.io, Render, Railway. It needs roughly 512 MB and no
persistent disk — the corpus ships in the repo and nothing is written at
runtime.

```sh
python -m venv .venv && .venv/bin/pip install -r demo/backend/requirements.txt
.venv/bin/python demo/backend/build_topic_vocabulary.py
.venv/bin/python -m uvicorn main:app --app-dir demo/backend --host 127.0.0.1 --port 8000 --workers 1
```

**One worker, deliberately.** The rate-limit counters are in-memory and
per-process, so N workers means the global daily cap is really N × the
configured number. One worker handles this load easily — the only slow part of a
request is waiting on the model, which is `await`ed and does not block the loop.
If you ever need more, move the counters to Redis first.

### `demo/backend/.env`

```ini
LLM_PROVIDER=gemini
GEMINI_API_KEY=...

CORS_ORIGINS=https://journal-atlas.chroniclecore.com
TRUST_PROXY=1

RATE_LIMIT_PER_HOUR=10
RATE_LIMIT_PER_DAY=30
GLOBAL_DAILY_LIMIT=250
```

`TRUST_PROXY=1` is **required** here. Without it every visitor is seen as the
Cloudflare edge IP and shares a single per-client bucket, so the tenth search of
the hour by anyone locks out everyone. Only set it when something you control
actually terminates the connection in front of the app — otherwise a caller can
forge `X-Forwarded-For` and get a fresh bucket per request.

Confirm both after deploy:

```sh
curl -s https://api.journal-atlas.chroniclecore.com/api/health
```

`provider_ready: true` and a `limits` block means the key loaded and the limiter
is live.

## Frontend

Cloudflare Pages, pointed at this repo:

| Setting | Value |
|---|---|
| Build command | `npm run build` |
| Build output directory | `dist` |
| Root directory | `demo/frontend` |
| Environment variable | `VITE_API_BASE=https://api.journal-atlas.chroniclecore.com` |

`VITE_API_BASE` is read at **build** time, not runtime — changing it means
redeploying, not restarting.

`VITE_SUPPORT_URL` does not need setting; the Buy Me a Coffee link is compiled
in as a default. Set it to an empty string to hide the link.

## The Cloudflare-specific part

**Cloudflare buffers `text/event-stream` by default.** A backend that streams
perfectly on localhost will appear to hang, then dump the whole recommendation
at once, or time out. The backend already sends the headers that turn this off
(`X-Accel-Buffering: no`, `Cache-Control: no-cache, no-transform` — see
`SSE_HEADERS` in `backend/main.py`, pinned by a test), but check the proxy too:

- Add a **Cache Rule** for `api.journal-atlas.chroniclecore.com/api/*` set to
  **Bypass cache**. Streaming responses must never be cached, and a cached SSE
  response is a broken one.
- Leave **Auto Minify** and **Rocket Loader** off for the API hostname. Both
  reintroduce buffering by transforming the response.
- If you use Cloudflare Tunnel rather than a public origin, note that
  `cloudflared` has its own history of buffering SSE — verify streaming through
  the tunnel specifically, not just against the origin.

Error **524** is a different failure and not a risk here: it fires when the
origin sends nothing for 100 seconds, and this pipeline emits its first `stage`
event before any model call. If you ever see one, the cause is the origin being
down, not the stream being slow.

### Verifying the stream actually streams

The only test that matters, run against the deployed URL rather than localhost:

```sh
curl -N -sS https://api.journal-atlas.chroniclecore.com/api/recommend \
  -H 'Content-Type: application/json' \
  -d '{"paper_description":"A qualitative autoethnographic study of embodied cognition, about 9000 words, no funding for publication fees."}'
```

`-N` disables curl's own buffering. Events must appear **progressively over
several seconds**. If everything lands at once at the end, something between you
and the app is still buffering — that is the bug, and it will look identical to
"the demo is slow" in a browser.

## Before announcing

- [ ] `/api/health` reports `provider_ready: true`
- [ ] `curl -N` shows events arriving progressively, through Cloudflare
- [ ] A search from the browser streams and renders a recommendation
- [ ] The 11th search in an hour returns a readable 429, not a raw error
- [ ] A spending cap is set on the provider key itself — the app's limits are
      defence in depth, not a substitute for the provider's own ceiling

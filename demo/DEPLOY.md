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

`TRUST_PROXY` is a **hop count, not a boolean**, and it has to match the
topology exactly:

| Setup | Value |
|---|---|
| `client → Caddy` (DNS-only / grey cloud) | `TRUST_PROXY=1` |
| `client → Cloudflare → Caddy` (proxied / orange cloud) | `TRUST_PROXY=2` |

`X-Forwarded-For` is *appended* to, so entries the caller controls sit on the
left and the ones infrastructure added sit on the right. The limiter counts in
from the right by this many hops, which is what makes the value unforgeable.

**Raise it to 2 in the same change that switches Cloudflare to orange cloud.**
Leave it at 1 and every visitor is bucketed by Cloudflare's edge IP, so the
tenth search of the hour by anyone locks out everyone. Set it to 2 while still
on grey cloud and the chain is too short, the fallback puts everyone in one
bucket, and you get the same symptom. Both directions fail strict rather than
open, which is why this is a support ticket rather than a breach.

Confirm both after deploy:

```sh
curl -s https://api.journal-atlas.chroniclecore.com/api/health
```

`provider_ready: true` and a `limits` block means the key loaded and the limiter
is live.

## Frontend

Deployed to Cloudflare Pages as project `journal-atlas` by **direct upload**,
not the Git integration:

```sh
cd demo/frontend
npm run build
npx wrangler pages deploy dist --project-name journal-atlas --branch main
```

`VITE_API_BASE` is read at **build** time, not runtime, and lives in the
committed [`.env.production`](frontend/.env.production) rather than in whoever's
shell ran the deploy — a public URL is not a secret, and a build that only
reproduces on one machine is a build nobody else can ship. Changing it means
rebuilding and redeploying, not restarting.

`VITE_SUPPORT_URL` does not need setting; the Buy Me a Coffee link is compiled
in as a default. Set it to an empty string to hide the link.

**Direct upload means pushing to `main` does not redeploy the site.** That is a
real cost and it is the one thing to fix first if this gets more than occasional
changes: connecting the Git integration needs the Cloudflare dashboard (wrangler
cannot configure it), after which the settings are root directory
`demo/frontend`, build `npm run build`, output `dist`. Until then, run the three
lines above after any frontend change.

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

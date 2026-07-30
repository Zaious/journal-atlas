# Work order — deploy the backend to Outpost

Written to be executed by a session that has the `outpost-deploy` skill and
access to the factory at `M:\ChronicleCore-Forge\infra\outpost\`. Everything
below was decided and verified in the repo session on 2026-07-30; nothing here
needs re-deriving.

Read [DEPLOY.md](DEPLOY.md) first for *why* the architecture is shaped this way.
This file is the *how*, specific to Outpost.

## What is being deployed

Only the **backend**. The frontend is static and goes to Cloudflare Pages — do
not put it on Outpost, it would spend VPS resources to serve files a CDN serves
for free.

| | |
|---|---|
| Service name | `journal-atlas-api` |
| Public URL | `https://api.journal-atlas.chroniclecore.com` |
| Port | leave `PORT=` blank — the factory assigns from 8080–8999 |
| Runtime | Python venv (FastAPI + uvicorn), **not** the stdlib skeleton |
| Data | none — no SQLite, nothing written at runtime |

**Constitution check (§2.2): this is clean.** The service serves a public
recommendation API over an open-source corpus that is already on GitHub. No
soul/, no bundle, no canon. Outward-facing consular data only, exactly what
Outpost is for.

## Before touching the factory

1. **DNS.** In Cloudflare, `A` record `api.journal-atlas` → `161.97.96.65`,
   proxied (orange cloud). The apex `journal-atlas.chroniclecore.com` points at
   Cloudflare Pages separately and is not Outpost's concern.
2. **Check the ledger** — `infra/outpost/SERVICES.md`. As of 2026-07-17: 8080
   relaweb, 8081 ats-cv, 8082 catalog-service, 8083 book-search-mcp. Leaving
   `PORT=` blank avoids guessing.
3. **RAM.** Outpost has 8 GB with four services already resident. This one is a
   single uvicorn worker holding FastAPI plus the `google-genai` SDK —
   roughly 200–300 MB. It reads corpus files per request rather than holding
   them in memory, so it does not grow with traffic. It will not squeeze
   tinyproxy.

## service.conf

Create `M:\ChronicleCore-Forge\infra\outpost\services\journal-atlas-api\service.conf`.
Do **not** run `scaffold.sh` — that generates a stdlib skeleton this would only
have to be deleted from.

```ini
PORT=
DOMAIN=api.journal-atlas.chroniclecore.com
DESC=Journal Atlas demo API — cited journal recommendations over a curated corpus

SOURCE=P:/MyOpenSource/JournalMatchEvaluator/journal-atlas
REQUIREMENTS=demo/backend/requirements.txt
RUNTIME=venv
ENTRY=demo/backend/run.py
```

Three things about this that will bite if changed:

- **`SOURCE` is the repo root, not `demo/backend`.** The backend resolves the
  corpus with `Path(__file__).parents[2] / "skills" / ...`. Push only the
  backend directory and it comes up fine, then returns zero candidates for
  every query — a failure that looks like a scoring bug, not a deploy bug.
- **`SOURCE` is a `P:` path**, not the `M:` Forge drive the factory usually
  sources from. If `deploy.sh` cannot tar from another drive, clone the repo
  onto `M:` and source from there instead — do not work around it by copying
  only part of the tree.
- **`ENTRY=demo/backend/run.py`** rather than a uvicorn command line. That file
  pins loopback binding and a single worker, and the single worker matters:
  the rate-limit counters are per-process, so two workers means the global
  daily spending cap is silently doubled.

Exclusions are automatic (`.git`, `__pycache__`, `venv`), but confirm
`demo/frontend/node_modules` does not get pushed — it is large and useless on
the VPS. If `deploy.sh` does not exclude it, add it to the exclusion list rather
than deleting it locally.

## Secrets

Never in the repo, never in plaintext in conversation. Write directly on the
VPS:

```sh
sudo tee /etc/outpost/journal-atlas-api.env >/dev/null <<'EOF'
LLM_PROVIDER=gemini
GEMINI_API_KEY=<paste on the box, not here>
CORS_ORIGINS=https://journal-atlas.chroniclecore.com
TRUST_PROXY=1
RATE_LIMIT_PER_HOUR=10
RATE_LIMIT_PER_DAY=30
GLOBAL_DAILY_LIMIT=250
EOF
sudo chmod 600 /etc/outpost/journal-atlas-api.env
```

`TRUST_PROXY=1` is **required** and only safe here. Caddy terminates the
connection, so `X-Forwarded-For` is trustworthy. Without it every visitor is
seen as the proxy's own address and shares one bucket — the tenth search of the
hour by anyone locks out everyone. Set on a service reachable directly from the
internet, it would be forgeable and the limiter worthless.

The corpus is public, so `GEMINI_API_KEY` is the only real secret. It is also
the only thing standing between this service and an unbounded bill, which is
what `GLOBAL_DAILY_LIMIT` exists to bound. **Set a spending cap in Google AI
Studio as well** — the app's limits are defence in depth, not a substitute.

## Deploy

```sh
cd M:/ChronicleCore-Forge/infra/outpost
./deploy.sh journal-atlas-api
```

The build step needs the venv to install `google-genai`, `anthropic`, `fastapi`
and `uvicorn` — the first deploy is slower than a stdlib service. Re-running
`deploy.sh` after a code change is idempotent.

`build_topic_vocabulary.py` does **not** need running on the VPS:
`topic_vocabulary.json` is committed and ships with the source. Regenerate it
in the repo and redeploy if the corpus changes.

## Verify — in this order

```sh
# 1. Alive at all
curl -s https://api.journal-atlas.chroniclecore.com/healthz

# 2. Key loaded, limiter live, corpus found
curl -s https://api.journal-atlas.chroniclecore.com/api/health
#    want: provider_ready true, journals_root_exists true, a limits block

# 3. Corpus actually readable — 399 across 13 fields
curl -s https://api.journal-atlas.chroniclecore.com/api/coverage
```

Then the one that matters, and the only one that cannot be checked from
localhost:

```sh
curl -N -sS https://api.journal-atlas.chroniclecore.com/api/recommend \
  -H 'Content-Type: application/json' \
  -d '{"paper_description":"A qualitative autoethnographic study of embodied cognition, about 9000 words, no funding for publication fees."}'
```

Events must arrive **progressively over several seconds**. If they all land at
once at the end, something is buffering the stream. The app already sends
`X-Accel-Buffering: no` and `Cache-Control: no-cache, no-transform`, so look at
Caddy and Cloudflare:

- Cloudflare **Cache Rule** on `api.journal-atlas.chroniclecore.com/api/*` →
  **Bypass cache**
- Cloudflare **Auto Minify** and **Rocket Loader** off for this hostname
- Caddy `reverse_proxy` needs `flush_interval -1` for SSE. If the factory's
  template does not set it, add via `PROXY_EXTRA="flush_interval -1"`.

A buffered stream is indistinguishable from "the demo is slow" in a browser,
which is why this is a curl check and not an eyeball check.

Last, confirm the limiter refuses cleanly rather than erroring: eleven requests
in an hour, and the eleventh should be a readable 429 naming the limit.

## Rollback

```sh
./remove.sh journal-atlas-api          # keep the env file
./remove.sh journal-atlas-api --purge  # also delete /etc/outpost/journal-atlas-api.env
```

Nothing is persisted, so removal loses nothing. To take the demo down without
undeploying, set `GLOBAL_DAILY_LIMIT=1` and restart — callers then get the
refusal message pointing them at the locally-run skill, which is a better
experience than a dead hostname.

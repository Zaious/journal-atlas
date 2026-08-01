# Journal Atlas — web demo

A throwaway-simple web front end for the [Journal Atlas skill](../skills/journal-atlas/SKILL.md):
paste a paper description, get a cited journal recommendation. No account,
no database — every request is stateless.

## Architecture

Three stages per request, streamed to the browser over SSE (see
[`backend/main.py`](backend/main.py) for the full pipeline docstring), with a
clarification round before them and up to two follow-ups after:

**0. Clarify (once, deterministic, no LLM call).** If the description leaves a
constraint unstated that would actually change the answer — publication-fee
budget, length, ethics approval, whether conferences count — the demo asks
once rather than guessing, and the user can answer or skip. Guessing is what
produced the worst bug this pipeline has had: an unstated IRB read as "no
IRB" eliminated 33 journals for a theoretical paper, invisibly.

1. **Extract** (cheap model, schema-constrained) — freeform text → the same `Paper`
   dataclass `fit_score.py` scores against. Topic phrasing is guided by
   [`topic_vocabulary.json`](backend/topic_vocabulary.json) (built by
   `build_topic_vocabulary.py`) so it aligns with the real OpenAlex topic
   names `fit_score.py`'s topic-density scoring matches against.
2. **Screen** (`fit_score.py`, no LLM) — deterministic pre-ranking across the
   curated 399 entries, reused unmodified from the skill itself. Each
   candidate's tier (Tier 1 / Tier 2 / AI-Researched / Skeleton) and top
   cited topic counts ride along in this stage's SSE event, so the frontend
   can render an expandable evidence card per candidate instead of a bare
   score — real, checkable receipts, not just a number.
3. **Synthesize** (streamed) — inlines
   [`CONSUMPTION_CONTRACT.md`](../skills/journal-atlas/CONSUMPTION_CONTRACT.md)
   (the same tier/evidence rules `SKILL.md` points real skill sessions to)
   plus a trimmed excerpt (policy digest + Subject Density + Soft Metadata +
   Strategic Notes, not the full file) of
   the top 10 candidates and writes a reasoned recommendation.
4. **Follow up** (up to two questions) — answered against the same curated
   entries, under the same consumption contract. The prior turn's context is
   sent back by the browser rather than held server-side, so the no-database
   property survives and the conversation stays somewhere the user can see and
   discard. The cap is enforced server-side too: the client is not trusted to
   limit its own use of a key the server pays for.

## Prerequisites

- Python 3.11+
- Node 18+
- An API key for one LLM provider. The backend runs on either, selected by
  `LLM_PROVIDER` in `.env`:
  - **Gemini** (default) — [Google AI Studio](https://aistudio.google.com/apikey)
  - **Anthropic** — a **Console** key (`platform.claude.com`), **not** a
    personal Claude.ai Pro/Max login. Anthropic's terms prohibit routing
    other users' requests through a personal subscription; a Console key
    billed under Commercial Terms is the supported way to serve multiple end
    users from one backend.

  Adding a provider means implementing two methods in
  [`backend/providers.py`](backend/providers.py) — `extract()` and
  `stream()` — plus a smoke test asserting its calls reach the API rather
  than failing locally on a bad argument.

## Setup

### Backend

```sh
cd demo/backend
python -m venv .venv
.venv/Scripts/activate      # Windows; use `source .venv/bin/activate` on macOS/Linux
pip install -r requirements.txt
cp .env.example .env        # then fill in the key for your chosen provider
python build_topic_vocabulary.py   # generates topic_vocabulary.json — re-run whenever
                                     # references/journals/**/*.md changes
```

### Frontend

```sh
cd demo/frontend
npm install
cp .env.example .env         # VITE_API_BASE, only needed if the backend isn't on :8000
```

## Running it

### Option A — plain terminal

```sh
# terminal 1
cd demo/backend && .venv/Scripts/python.exe -m uvicorn main:app --reload --port 8000

# terminal 2
cd demo/frontend && npm run dev
```

Vite will print the actual URL it bound to — read that from the terminal
rather than assuming a fixed port (see the note below).

### Option B — Claude Code's `preview_start` / `.claude/launch.json`

The repo root's **parent** directory (one level above this git repo) has a
`.claude/launch.json` with `demo-backend` and `demo-frontend` configurations,
paths prefixed `journal-atlas/...` — `preview_start` resolves `launch.json`
relative to Claude Code's actual working directory, which is that parent
directory, not this repo's root. If you're driving this repo through Claude
Code, that file already exists; if it doesn't, recreate it there (not inside
this repo) with `demo-backend` running
`uvicorn main:app --reload --port 8000 --app-dir journal-atlas/demo/backend`
and `demo-frontend` running `npm run dev --prefix journal-atlas/demo/frontend`.

**Port note:** `launch.json` asks Vite for port 5174, but Vite auto-increments
to the next free port if that one's taken (in local testing it landed on
5175 because both 5173 and 5174 were already in use by unrelated processes).
The configured port is a request, not a guarantee — always confirm the real
one from the dev server's own log output. The backend's `CORS_ORIGINS`
default already covers 5173/5174/5175; if you land on a different port, add
it to `CORS_ORIGINS` in `.env` or requests will fail CORS with no other
symptom.

## Verifying it works

```sh
curl http://localhost:8000/api/health
# {"status":"ok","journals_root_exists":true,"provider":"gemini",...,"provider_ready":true}
```

If `provider_ready` is `false`, `provider_error` says exactly why — usually
the key isn't set, or `.env` isn't being picked up. Confirm the file is at
`demo/backend/.env` (**not** `.env.local`, which is the Vite convention and
applies to the frontend only; `load_dotenv()` reads `.env`) and that uvicorn
was started from `demo/backend` or with `--app-dir` pointing there.

Then open the frontend URL and submit a paper description. The three stage
dots should light up in sequence (parsing → screening → synthesis) and the
recommendation should stream in as markdown.

## Deploying it

Local setup is above. Putting it on a public hostname behind Cloudflare has its
own set of traps — chiefly that Cloudflare buffers `text/event-stream`, which
makes a correctly-streaming backend look like it hangs. See
[DEPLOY.md](DEPLOY.md).

## Abuse and cost controls

Every `/api/recommend` is two LLM calls carrying text the caller chose, paid
for by whoever's key is in `.env`. Unprotected, that is a free LLM proxy with
an unbounded bill. Three layers, in
[`backend/ratelimit.py`](backend/ratelimit.py), each failing differently:

| Control | What it bounds | Default | Env var |
|---|---|---|---|
| Input size caps | The cost of **one** request | 12,000 chars description / 2,000 answer / 20,000 follow-up context | — (constants in `main.py`) |
| Per-client rate limit | Casual repeated use | 10/hour, 30/day | `RATE_LIMIT_PER_HOUR`, `RATE_LIMIT_PER_DAY` |
| Global daily cap | **The bill** | 250 requests/day | `GLOBAL_DAILY_LIMIT` |

At roughly 31,600 input and 1,500 output tokens per recommendation (measured,
not estimated — build the prompts and count), gemini-3.5-flash-lite costs about
**$0.013 per recommendation**. So the cap converts directly into a worst-case
bill: 250/day is ~$3.30/day, 500/day is ~$6.60/day, and those are only reached
on days the cap is actually exhausted.

**The provider enforces its own daily ceiling, independently of this one.** If
it is lower than `GLOBAL_DAILY_LIMIT`, the provider runs out first and this
app's cap never fires — and note that each recommendation is **two** provider
calls (extract + synthesize), so a provider quota of N requests/day allows N/2
recommendations. Check the real number before raising the cap here; raising it
past what the provider allows only converts a readable refusal into an error.

The size caps come first deliberately: rate limits are useless if a single
request can carry 500 KB into a prompt. The global cap comes last and matters
most — it is the only one that holds regardless of how requests are spread
across clients, so it is what actually turns an unbounded bill into a bounded
one. When it trips the demo stops calling the provider and says so, pointing
at the skill, which runs locally with no such limit.

`/api/coverage` and `/api/health` are not counted: they cost nothing, and
blocking them would hide the message explaining the block.

**What these do not do**, stated plainly:

- **Per-IP limiting is friction, not a wall.** IPs are shared behind NAT and
  cheap behind a VPN. It stops casual abuse and nothing more; the global cap
  is what stops the rest.
- **Counters are in-memory and per-process.** They reset on restart, and each
  worker holds its own — so the true ceiling is `GLOBAL_DAILY_LIMIT × workers`.
  Run one worker, or move the counter to Redis. This is the price of the
  demo's no-database property, taken deliberately.
- **`X-Forwarded-For` is trusted only when `TRUST_PROXY=1`**, because any
  client can send that header. Behind a proxy you must set it, or every caller
  shares the proxy's IP and therefore one bucket. That failure is in the safe
  direction — stricter than intended, not looser.

**No login, deliberately.** Requiring Google sign-in would cost the demo its
one distinguishing property — no account, no install, paste and go — and buy
little: a determined abuser makes accounts. It would also mean handling PII, a
privacy policy, and OAuth infrastructure for a stateless demo that stores
nothing. If the demo is ever hammered past what the caps absorb, the escalation
path is to set `GLOBAL_DAILY_LIMIT=1` and let the refusal message point people
at the skill — not to build an auth system.

**Set a spending cap on the API key regardless.** These controls are
defence in depth, not a substitute for the provider's own limit.

## What this isn't

- No persistent storage of any kind — nothing survives past a single request,
  including the rate-limit counters.
- No auth — the API key lives only in the backend's process env, never sent
  to the browser.

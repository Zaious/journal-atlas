# Journal Atlas — web demo

A throwaway-simple web front end for the [Journal Atlas skill](../skills/journal-atlas/SKILL.md):
paste a paper description, get a cited journal recommendation. No account,
no database — every request is stateless.

## Architecture

Three stages per request, streamed to the browser over SSE (see
[`backend/main.py`](backend/main.py) for the full pipeline docstring):

1. **Extract** (Haiku, forced tool-use) — freeform text → the same `Paper`
   dataclass `fit_score.py` scores against. Topic phrasing is guided by
   [`topic_vocabulary.json`](backend/topic_vocabulary.json) (built by
   `build_topic_vocabulary.py`) so it aligns with the real OpenAlex topic
   names `fit_score.py`'s topic-density scoring matches against.
2. **Screen** (`fit_score.py`, no LLM) — deterministic pre-ranking across the
   curated 399 entries, reused unmodified from the skill itself.
3. **Synthesize** (Sonnet, streamed) — reads a trimmed excerpt (policy digest
   + Subject Density + Soft Metadata + Strategic Notes, not the full file) of
   the top 10 candidates and writes a reasoned recommendation.

## Prerequisites

- Python 3.11+
- Node 18+
- An Anthropic **Console** API key (`platform.claude.com`) — **not** a
  personal Claude.ai Pro/Max login. See
  [`backend/.env.example`](backend/.env.example) for why: Anthropic's terms
  prohibit routing other users' requests through a personal subscription;
  a Console key billed under Commercial Terms is the supported way to serve
  multiple end users from one backend.

## Setup

### Backend

```sh
cd demo/backend
python -m venv .venv
.venv/Scripts/activate      # Windows; use `source .venv/bin/activate` on macOS/Linux
pip install -r requirements.txt
cp .env.example .env        # then fill in ANTHROPIC_API_KEY
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
# {"status":"ok","journals_root_exists":true,"api_key_configured":true}
```

If `api_key_configured` is `false`, `.env` isn't being picked up — confirm
it's at `demo/backend/.env` (not `.env.example`) and uvicorn was started
from `demo/backend` (or with `--app-dir` pointing there).

Then open the frontend URL and submit a paper description. The three stage
dots should light up in sequence (parsing → screening → synthesis) and the
recommendation should stream in as markdown.

## What this isn't

This is a local-dev architecture scaffold, not a deployable service:

- No rate-limiting or abuse prevention — anyone who can reach `/api/recommend`
  can spend your API key's budget.
- No persistent storage of any kind — nothing survives past a single request.
- No auth — the API key lives only in the backend's process env, never sent
  to the browser.

Set a spending cap on the API key regardless of how this is deployed.

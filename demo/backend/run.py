#!/usr/bin/env python3
"""Production entry point.

Deployment tooling generally runs a script rather than composing a uvicorn
command line, so this exists to be that script and to make three choices
explicitly rather than leaving them to whoever writes the unit file:

  * **Bind to loopback only.** The process must never be directly reachable
    from the internet; a reverse proxy in front of it terminates TLS and is
    the only thing that should be listening publicly.
  * **One worker.** The rate-limit counters in ratelimit.py are in-memory and
    per-process, so N workers means the global daily cap is really N times the
    configured number — the one control that is supposed to bound the bill,
    silently multiplied. One worker is also sufficient: the slow part of a
    request is waiting on the model, which is awaited and does not block the
    event loop.
  * **No --reload.** Reload watches the filesystem, and this app reads 399
    corpus files per request.

For local development use `uvicorn main:app --reload` directly instead.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

import uvicorn

# Running this file as a script puts its directory on sys.path, so `main`
# resolves regardless of the working directory the service manager chose.
sys.path.insert(0, str(Path(__file__).resolve().parent))


def main() -> None:
    port = int(os.environ.get("PORT", "8000"))
    host = os.environ.get("BIND_HOST", "127.0.0.1")
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        workers=1,
        log_level=os.environ.get("LOG_LEVEL", "info"),
        # Trust nothing about forwarded headers at the ASGI layer — whether
        # X-Forwarded-For is believed is decided in ratelimit.py by TRUST_PROXY,
        # and having two places make that call independently is how a limiter
        # ends up bypassable.
        proxy_headers=False,
    )


if __name__ == "__main__":
    main()

"""The limits are wired into the actual endpoints, not merely implemented.

`test_ratelimit.py` tests the limiter in isolation; these assert that a request
arriving at the API is really subject to it, and that oversized input is
rejected before it can reach a prompt. A control that exists but is not called
is worse than no control, because it reads as protection.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import main  # noqa: E402
import ratelimit  # noqa: E402


@pytest.fixture
def client(monkeypatch):
    """A client whose limiter starts empty, so tests do not leak into each
    other through the module-level counter the running server shares.

    The provider is forced to None as well. A developer running this with a
    populated `.env` would otherwise spend real API calls to prove that
    requests are being counted — and the counting happens in the handler,
    before the stream opens, so unplugging the provider tests exactly the same
    path while making the suite safe to run anywhere.
    """
    monkeypatch.setattr(main, "LIMITER",
                        ratelimit.RateLimiter(per_hour=3, per_day=10, global_per_day=100))
    monkeypatch.setattr(main, "PROVIDER", None)
    monkeypatch.setattr(main, "PROVIDER_ERROR", "provider disabled for tests")
    return TestClient(main.app)


VALID = {"paper_description": "A qualitative study of embodied cognition."}


def test_recommend_is_rate_limited(client):
    for _ in range(3):
        assert client.post("/api/recommend", json=VALID).status_code != 429
    res = client.post("/api/recommend", json=VALID)
    assert res.status_code == 429
    assert "Hourly limit" in res.json()["message"]


def test_recommend_and_followup_share_one_budget(client):
    """Otherwise the cheapest bypass is to alternate between the two
    endpoints and get double the intended allowance."""
    client.post("/api/recommend", json=VALID)
    client.post("/api/recommend", json=VALID)
    followup = {"paper_description": "x", "recommendation": "y", "question": "why?"}
    assert client.post("/api/followup", json=followup).status_code != 429
    assert client.post("/api/followup", json=followup).status_code == 429


def test_oversized_description_is_rejected_before_any_llm_call(client):
    res = client.post("/api/recommend",
                      json={"paper_description": "x" * (main.MAX_DESCRIPTION_CHARS + 1)})
    assert res.status_code == 422


def test_oversized_followup_context_is_rejected(client):
    """`recommendation` comes back from the browser, so it is attacker-
    controlled text heading straight into a prompt the demo pays for."""
    res = client.post("/api/followup", json={
        "paper_description": "x", "question": "why?",
        "recommendation": "y" * (main.MAX_RECOMMENDATION_CHARS + 1),
    })
    assert res.status_code == 422


def test_rejected_oversized_requests_do_not_consume_the_budget(client):
    """Pydantic rejects before the handler runs, so a flood of oversized
    requests must not be able to exhaust a legitimate user's allowance."""
    for _ in range(20):
        client.post("/api/recommend", json={"paper_description": "x" * 99_999})
    assert client.post("/api/recommend", json=VALID).status_code != 429


def test_coverage_and_health_are_not_rate_limited(client):
    """Blocking these would hide the message explaining the block, and they
    cost nothing to serve."""
    for _ in range(30):
        assert client.get("/api/coverage").status_code == 200
        assert client.get("/api/health").status_code == 200


def test_coverage_counts_are_read_from_the_corpus(client):
    body = client.get("/api/coverage").json()
    assert body["total"] == sum(f["total"] for f in body["fields"])
    assert body["total"] > 300, "corpus should be the full curated set"
    for field in body["fields"]:
        assert field["tier1"] + field["tier2"] + field["ai"] == field["total"]
    # The concentration the disclosure is about must be computable from it,
    # and every named core field must exist — a typo in core_fields would
    # silently understate the concentration rather than fail.
    core = [f for f in body["fields"] if f["field"] in body["core_fields"]]
    assert len(core) == len(body["core_fields"])
    assert sum(f["total"] for f in core) / body["total"] > 0.85


def test_frontend_and_readme_report_the_same_concentration():
    """The README states this figure in prose and the demo computes it. Two
    numbers for one claim is exactly the kind of drift this project exists to
    argue against."""
    readme = (Path(__file__).resolve().parents[3] / "README.md").read_text(encoding="utf-8")
    body = main.compute_coverage()
    core = [f for f in body["fields"] if f["field"] in body["core_fields"]]
    pct = round(sum(f["total"] for f in core) / body["total"] * 100)
    total = sum(f["total"] for f in core)
    assert f"{pct}% of the corpus ({total} of {body['total']})" in readme


def test_health_reports_limits_without_leaking_client_addresses(client):
    client.post("/api/recommend", json=VALID)
    limits = client.get("/api/health").json()["limits"]
    assert limits["global_used_today"] >= 1
    assert limits["per_client_hourly_limit"] == 3
    assert "testclient" not in str(limits).lower()


# ---------- streaming headers ----------


@pytest.mark.parametrize("path,body", [
    ("/api/recommend", VALID),
    ("/api/followup", {"paper_description": "x", "recommendation": "y", "question": "z"}),
])
def test_sse_responses_tell_proxies_not_to_buffer(client, path, body):
    """Cloudflare and nginx buffer text/event-stream by default, which makes a
    correctly-streaming backend appear to hang once it is behind a CDN — the
    worst place to discover it. Pinned here because nothing in local
    development can catch its absence."""
    res = client.post(path, json=body)
    assert res.headers["x-accel-buffering"] == "no"
    assert "no-transform" in res.headers["cache-control"]
    assert res.headers["content-type"].startswith("text/event-stream")


def test_rate_limit_refusal_is_json_not_a_stream(client):
    """The refusal happens before the stream opens, so it must arrive as a 429
    the browser can act on rather than a 200 carrying bad news."""
    for _ in range(3):
        client.post("/api/recommend", json=VALID)
    res = client.post("/api/recommend", json=VALID)
    assert res.status_code == 429
    assert res.headers["content-type"].startswith("application/json")


def test_healthz_is_a_cheap_unauthenticated_liveness_probe(client):
    """Deployment tooling probes /healthz by convention. It must not be rate
    limited and must not depend on the provider being configured, or a missing
    key would read as a dead process and trigger a restart loop."""
    monkeypatched_away = main.PROVIDER is None
    assert monkeypatched_away, "fixture should have unplugged the provider"
    for _ in range(30):
        res = client.get("/healthz")
        assert res.status_code == 200
        assert res.json()["status"] == "ok"

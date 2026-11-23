"""Anonymous usage totals: what they count, and what they must never hold.

Decision 4 of docs/status/SITE_SPEC.md lets the maintainer see whether the demo
is used, on the condition that nothing identifying or free-form is kept. These
tests are the condition: a closed set of outcomes, a closed set of field names,
and a full run that proves the pasted text and the client address do not end up
in what `/api/usage` serves.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import main  # noqa: E402
import ratelimit  # noqa: E402
import usage  # noqa: E402

SECRET_TEXT = "ZEBRA-MANUSCRIPT-9431 an autoethnography of embodied cognition in design teams"


def test_unknown_outcomes_are_refused_so_text_cannot_be_smuggled_in():
    counter = usage.UsageCounter()
    with pytest.raises(ValueError):
        counter.record("whatever the visitor typed")


def test_days_roll_over_at_utc_midnight_and_old_days_are_dropped():
    counter = usage.UsageCounter()
    day = 86400
    counter.record("completed", "psychology", now=0)
    counter.record("refused", now=day + 5)
    for i in range(2, usage.KEEP_DAYS + 5):
        counter.record("completed", now=i * day)
    dates = [row["date"] for row in counter.snapshot(days=100)["days"]]
    assert len(dates) == usage.KEEP_DAYS
    assert "1970-01-01" not in dates


def test_overlong_field_names_are_ignored():
    counter = usage.UsageCounter()
    counter.record("completed", "x" * 500, now=0)
    row = counter.snapshot()["days"][0]
    assert row["top_field"] == {}


class _FakeProvider:
    name = "fake"
    extraction_model = "fake-extract"
    synthesis_model = "fake-synth"

    async def extract(self, prompt, schema):
        return {"topics": ["qualitative research", "embodied cognition"],
                "methodology": "qualitative", "word_count": 8000}

    async def stream(self, prompt):
        yield "A recommendation."


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setattr(main, "LIMITER",
                        ratelimit.RateLimiter(per_hour=50, per_day=50, global_per_day=100))
    monkeypatch.setattr(main, "USAGE", usage.UsageCounter())
    monkeypatch.setattr(main, "PROVIDER", _FakeProvider())
    return TestClient(main.app)


def test_a_full_run_is_counted_without_the_text_or_the_address(client):
    res = client.post("/api/recommend",
                      json={"paper_description": SECRET_TEXT, "skip_clarify": True})
    assert res.status_code == 200
    assert "event: text" in res.text

    served = client.get("/api/usage")
    assert served.status_code == 200
    body = served.json()
    today = body["days"][-1]
    assert today["searches"] == 1
    assert today["outcomes"]["completed"] == 1
    assert set(today["top_field"]) <= set(main.FIELD_LABELS) | {"other"}

    blob = json.dumps(body)
    assert "ZEBRA" not in blob and "autoethnography" not in blob
    assert "testclient" not in blob.lower()


def test_a_refusal_is_counted_as_refused(client, monkeypatch):
    monkeypatch.setattr(main, "LIMITER", ratelimit.RateLimiter(per_hour=0, per_day=0, global_per_day=1))
    client.post("/api/recommend", json={"paper_description": "first", "skip_clarify": True})
    res = client.post("/api/recommend", json={"paper_description": "second"})
    assert res.status_code == 429
    today = client.get("/api/usage").json()["days"][-1]
    assert today["outcomes"]["refused"] == 1


def test_a_dropped_connection_is_counted_as_abandoned(monkeypatch):
    """The visitor closing the tab mid-stream must not vanish from the totals."""
    import asyncio

    monkeypatch.setattr(main, "USAGE", usage.UsageCounter())
    monkeypatch.setattr(main, "PROVIDER", _FakeProvider())

    async def run():
        gen = main.sse_recommend(main.RecommendRequest(paper_description=SECRET_TEXT, skip_clarify=True))
        await gen.__anext__()  # first event only, then the client goes away
        await gen.aclose()

    asyncio.run(run())
    today = main.USAGE.snapshot()["days"][-1]
    assert today["outcomes"]["abandoned"] == 1

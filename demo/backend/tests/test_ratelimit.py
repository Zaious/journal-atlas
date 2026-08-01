"""Tests for the demo's abuse and cost controls.

Time is injected rather than slept through, so these run instantly and can
assert on window boundaries that would otherwise take a day to reach.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import ratelimit  # noqa: E402

HOUR = ratelimit.HOUR
DAY = ratelimit.DAY


def test_requests_under_the_limit_are_allowed():
    limiter = ratelimit.RateLimiter(per_hour=3, per_day=10, global_per_day=100)
    for i in range(3):
        assert limiter.check("1.2.3.4", now=1000 + i) is None


def test_hourly_limit_refuses_and_says_how_long_to_wait():
    limiter = ratelimit.RateLimiter(per_hour=2, per_day=10, global_per_day=100)
    limiter.check("1.2.3.4", now=1000)
    limiter.check("1.2.3.4", now=1001)
    refusal = limiter.check("1.2.3.4", now=1002)
    assert refusal is not None
    assert "Hourly limit" in refusal
    assert "minutes" in refusal


def test_the_hourly_window_slides_rather_than_resetting_on_the_hour():
    """A fixed window lets a client spend a full allowance twice across a
    boundary a second apart, which is the exact shape a script produces."""
    limiter = ratelimit.RateLimiter(per_hour=2, per_day=10, global_per_day=100)
    limiter.check("1.2.3.4", now=1000)
    limiter.check("1.2.3.4", now=1500)
    assert limiter.check("1.2.3.4", now=2000) is not None
    # The first request ages out; one slot opens, and only one.
    assert limiter.check("1.2.3.4", now=1000 + HOUR + 1) is None
    assert limiter.check("1.2.3.4", now=1000 + HOUR + 2) is not None


def test_daily_limit_holds_even_when_requests_are_spread_across_hours():
    limiter = ratelimit.RateLimiter(per_hour=100, per_day=3, global_per_day=1000)
    for i in range(3):
        assert limiter.check("1.2.3.4", now=1000 + i * HOUR) is None
    refusal = limiter.check("1.2.3.4", now=1000 + 4 * HOUR)
    assert refusal is not None
    assert "Daily limit" in refusal


def test_clients_are_limited_independently():
    limiter = ratelimit.RateLimiter(per_hour=1, per_day=10, global_per_day=100)
    assert limiter.check("1.1.1.1", now=1000) is None
    assert limiter.check("2.2.2.2", now=1000) is None
    assert limiter.check("1.1.1.1", now=1001) is not None


def test_global_cap_holds_no_matter_how_requests_are_distributed():
    """Per-client limits are friction; this is the control that bounds the
    bill, because it does not care that every request came from a new IP."""
    limiter = ratelimit.RateLimiter(per_hour=100, per_day=100, global_per_day=5)
    for i in range(5):
        assert limiter.check(f"10.0.0.{i}", now=1000 + i) is None
    refusal = limiter.check("10.0.0.99", now=1006)
    assert refusal is not None
    assert "daily budget" in refusal
    # It must point somewhere: the knowledge base is public and runs locally.
    assert "open source" in refusal


def test_a_refused_request_is_not_counted():
    """Otherwise a client hammering a closed door pushes its own reopening
    further away, and burns the global budget it was just denied."""
    limiter = ratelimit.RateLimiter(per_hour=1, per_day=10, global_per_day=100)
    limiter.check("1.2.3.4", now=1000)
    for i in range(50):
        limiter.check("1.2.3.4", now=1001 + i)
    assert limiter.snapshot(now=1051)["global_used_today"] == 1
    # One hour after the single successful request, the slot is free again.
    assert limiter.check("1.2.3.4", now=1000 + HOUR + 1) is None


def test_global_window_also_slides():
    limiter = ratelimit.RateLimiter(per_hour=100, per_day=100, global_per_day=2)
    limiter.check("a", now=1000)
    limiter.check("b", now=1001)
    assert limiter.check("c", now=1002) is not None
    assert limiter.check("c", now=1000 + DAY + 1) is None


def test_snapshot_reports_usage_without_leaking_client_addresses():
    limiter = ratelimit.RateLimiter(per_hour=5, per_day=10, global_per_day=50)
    limiter.check("192.168.1.50", now=1000)
    snap = limiter.snapshot(now=1001)
    assert snap["global_used_today"] == 1
    assert snap["tracked_clients"] == 1
    assert "192.168.1.50" not in str(snap)


# ---------- client identification ----------


class _FakeRequest:
    def __init__(self, host, headers=None):
        self.client = type("C", (), {"host": host})()
        self.headers = headers or {}


def test_forwarded_header_is_ignored_unless_a_proxy_is_trusted(monkeypatch):
    """Any client can set X-Forwarded-For. A limiter that believes it is a
    limiter that anyone can bypass by setting a string."""
    monkeypatch.delenv("TRUST_PROXY", raising=False)
    req = _FakeRequest("10.0.0.1", {"x-forwarded-for": "1.2.3.4"})
    assert ratelimit.client_key(req) == "10.0.0.1"


def test_one_trusted_hop_reads_the_entry_that_proxy_appended(monkeypatch):
    """X-Forwarded-For is appended to, so client-controlled entries are on the
    LEFT. An earlier version of this read chain[0] and was bypassable by
    sending the header — counting in from the right is what makes the value
    unforgeable."""
    monkeypatch.setenv("TRUST_PROXY", "1")
    forged = _FakeRequest("10.0.0.1", {"x-forwarded-for": "1.2.3.4, 203.0.113.9"})
    assert ratelimit.client_key(forged) == "203.0.113.9"
    clean = _FakeRequest("10.0.0.1", {"x-forwarded-for": "203.0.113.9"})
    assert ratelimit.client_key(clean) == "203.0.113.9"


def test_two_trusted_hops_skip_the_cdn_and_find_the_real_client(monkeypatch):
    """client -> Cloudflare -> Caddy. Cloudflare appends the client IP to
    whatever the client sent rather than replacing it, so with two hops the
    real caller is second from the right and the forged prefix is inert."""
    monkeypatch.setenv("TRUST_PROXY", "2")
    req = _FakeRequest("10.0.0.1",
                       {"x-forwarded-for": "1.2.3.4, 203.0.113.9, 172.16.0.5"})
    assert ratelimit.client_key(req) == "203.0.113.9"


def test_no_number_of_forged_entries_changes_the_bucket(monkeypatch):
    """The property that matters: a caller cannot manufacture fresh buckets by
    varying what it sends, however much it sends."""
    monkeypatch.setenv("TRUST_PROXY", "1")
    keys = {
        ratelimit.client_key(_FakeRequest(
            "10.0.0.1", {"x-forwarded-for": f"{i}.{i}.{i}.{i}, 203.0.113.9"}))
        for i in range(1, 20)
    }
    assert keys == {"203.0.113.9"}


def test_a_chain_shorter_than_the_hop_count_falls_back_to_the_peer(monkeypatch):
    """Means the deployment is misconfigured. One shared bucket is the right
    way to be wrong — stricter than intended, never bypassable."""
    monkeypatch.setenv("TRUST_PROXY", "2")
    req = _FakeRequest("10.0.0.1", {"x-forwarded-for": "1.2.3.4"})
    assert ratelimit.client_key(req) == "10.0.0.1"


@pytest.mark.parametrize("value,expected", [
    ("1", 1), ("2", 2), ("true", 1), ("yes", 1), ("on", 1),
    ("", 0), ("0", 0), ("nonsense", 0), ("-3", 0),
])
def test_trust_proxy_parsing_fails_closed(monkeypatch, value, expected):
    monkeypatch.setenv("TRUST_PROXY", value)
    assert ratelimit.trusted_hops() == expected


def test_client_key_survives_a_request_with_no_client():
    assert ratelimit.client_key(_FakeRequest(None)) == "unknown"


def test_env_overrides_are_read_but_bad_values_fall_back(monkeypatch):
    monkeypatch.setenv("RATE_LIMIT_PER_HOUR", "42")
    monkeypatch.setenv("GLOBAL_DAILY_LIMIT", "not-a-number")
    limiter = ratelimit.RateLimiter()
    assert limiter.per_hour == 42
    assert limiter.global_per_day == 250


@pytest.mark.parametrize("limit_kwargs", [
    {"per_hour": 0}, {"per_day": 0}, {"global_per_day": 0},
])
def test_a_limit_of_zero_means_unlimited_not_blocked(limit_kwargs):
    """0 reads as 'no limit configured' so an operator who wants the demo shut
    off sets the global cap deliberately rather than by leaving a var blank."""
    limiter = ratelimit.RateLimiter(per_hour=100, per_day=100, global_per_day=100)
    for key, value in limit_kwargs.items():
        setattr(limiter, key, value)
    for i in range(30):
        assert limiter.check("1.2.3.4", now=1000 + i) is None

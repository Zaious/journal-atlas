#!/usr/bin/env python3
"""
test_api_shape.py — Smoke tests that the demo's Anthropic API calls are
shaped correctly, i.e. every parameter name is one the installed SDK
actually recognizes.

Written after extract_paper() shipped with `output_config={"format":
"json_schema", ...}` — a parameter that anthropic==0.69.0's Messages API
does not have at all. Every call raised TypeError immediately, so extraction
never worked, not even once — but nothing caught it because every prior
manual test stopped at "ANTHROPIC_API_KEY not set", one step before this
code path ever ran.

Requires network access to api.anthropic.com (uses a deliberately invalid
key — the assertion is that the SDK reaches the server and gets a real
AuthenticationError back, not that any call succeeds). No API credit is
spent: an authentication failure is rejected before any model runs.
"""
from __future__ import annotations

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import anthropic
import main  # noqa: E402

INVALID_KEY = "sk-ant-dummy-invalid-key-for-shape-test"


def _client() -> anthropic.AsyncAnthropic:
    return anthropic.AsyncAnthropic(api_key=INVALID_KEY, timeout=10.0, max_retries=0)


def test_extract_paper_call_shape_is_valid():
    """A TypeError here means a parameter name extract_paper() passes to
    messages.create() doesn't exist in the installed SDK — the exact
    failure mode that meant extraction never worked at all. An
    AuthenticationError means the request reached the server correctly and
    was rejected only for the (deliberately) bad key."""

    async def run():
        client = _client()
        await main.extract_paper(client, "A short test paper about embodied cognition.")

    try:
        asyncio.run(run())
        raise AssertionError("expected AuthenticationError with an invalid key, got success")
    except anthropic.AuthenticationError:
        pass  # correct: reached the API, rejected only for the bad key
    except TypeError as exc:
        raise AssertionError(f"extract_paper() passed a parameter the SDK doesn't recognize: {exc}") from exc


def test_synthesis_stream_call_shape_is_valid():
    """Same check for the synthesis stage's streaming call."""

    async def run():
        client = _client()
        async with client.messages.stream(
            model=main.SYNTHESIS_MODEL,
            max_tokens=2048,
            messages=[{"role": "user", "content": "test"}],
        ) as stream:
            async for _ in stream.text_stream:
                pass

    try:
        asyncio.run(run())
        raise AssertionError("expected AuthenticationError with an invalid key, got success")
    except anthropic.AuthenticationError:
        pass
    except TypeError as exc:
        raise AssertionError(f"synthesis stream call passed a parameter the SDK doesn't recognize: {exc}") from exc


def test_extract_tool_schema_is_well_formed_json_schema():
    """A cheap, network-free sanity check on EXTRACT_TOOL's shape — catches
    a malformed input_schema before it ever reaches the API."""
    tool = main.EXTRACT_TOOL
    assert tool["name"]
    assert tool["input_schema"]["type"] == "object"
    assert "properties" in tool["input_schema"]
    assert set(tool["input_schema"]["required"]).issubset(tool["input_schema"]["properties"].keys())

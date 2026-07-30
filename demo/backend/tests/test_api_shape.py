#!/usr/bin/env python3
"""
test_api_shape.py — Assert every provider's API calls are shaped correctly,
i.e. every parameter and schema we pass is one the installed SDK actually
accepts.

Written after extract_paper() shipped with `output_config={"format":
"json_schema", ...}` — a parameter anthropic 0.69.0's Messages API does not
have. Every call raised TypeError, so extraction never worked once, and
nothing caught it because manual testing always stopped at "API key not set",
one step before this code path ran.

Adding a second provider doubles that surface, and the Gemini port hit the
same class of bug immediately: `types.GenerateContentConfig(...)` accepts a
JSON Schema with a `["string", "null"]` union at construction time and only
rejects it when the request is actually made. A test that merely built the
config would have passed while every real request failed.

So each test drives the real call path with a deliberately invalid key and
asserts the failure is an *authentication* failure — proof the request was
well-formed enough to reach the server and be rejected only for the key.
Needs network access to the providers' endpoints; spends no credit, since an
auth rejection happens before any model runs.
"""
from __future__ import annotations

import asyncio
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import main  # noqa: E402
import providers  # noqa: E402

INVALID_KEY = "dummy-invalid-key-for-shape-test"


def _assert_reached_api(exc: Exception, what: str) -> None:
    """An auth/permission rejection means the call was well-formed. A
    TypeError or a schema ValidationError means we passed something the SDK
    doesn't accept — the bug class this file exists to catch."""
    name = type(exc).__name__
    if name in ("TypeError", "ValidationError"):
        raise AssertionError(f"{what} passed something the SDK rejects locally: {name}: {exc}")
    text = str(exc).lower()
    if not any(m in text for m in ("api key", "authentication", "unauthorized", "401", "invalid_argument")):
        raise AssertionError(f"{what} failed for an unexpected reason ({name}): {exc}")


# ---------- Gemini ----------


def _gemini() -> providers.GeminiProvider:
    return providers.GeminiProvider(INVALID_KEY, "gemini-3.5-flash-lite",
                                    "gemini-3.5-flash-lite", 15.0, 0)


def test_gemini_extract_call_shape_is_valid():
    async def run():
        await _gemini().extract("A theoretical paper on embodied cognition.", main.PAPER_SCHEMA)
    try:
        asyncio.run(run())
        raise AssertionError("expected an auth failure with an invalid key, got success")
    except AssertionError:
        raise
    except Exception as exc:
        _assert_reached_api(exc, "GeminiProvider.extract()")


def test_gemini_stream_call_shape_is_valid():
    async def run():
        async for _ in _gemini().stream("test"):
            pass
    try:
        asyncio.run(run())
        raise AssertionError("expected an auth failure with an invalid key, got success")
    except AssertionError:
        raise
    except Exception as exc:
        _assert_reached_api(exc, "GeminiProvider.stream()")


# ---------- Anthropic ----------


def _anthropic():
    try:
        return providers.AnthropicProvider("sk-ant-" + INVALID_KEY, "claude-haiku-4-5",
                                           "claude-sonnet-5", 15.0, 0)
    except ImportError:
        pytest.skip("anthropic SDK not installed")


def test_anthropic_extract_call_shape_is_valid():
    async def run():
        await _anthropic().extract("A theoretical paper on embodied cognition.", main.PAPER_SCHEMA)
    try:
        asyncio.run(run())
        raise AssertionError("expected an auth failure with an invalid key, got success")
    except AssertionError:
        raise
    except Exception as exc:
        _assert_reached_api(exc, "AnthropicProvider.extract()")


def test_anthropic_stream_call_shape_is_valid():
    async def run():
        async for _ in _anthropic().stream("test"):
            pass
    try:
        asyncio.run(run())
        raise AssertionError("expected an auth failure with an invalid key, got success")
    except AssertionError:
        raise
    except Exception as exc:
        _assert_reached_api(exc, "AnthropicProvider.stream()")


# ---------- Schema translation (offline) ----------


def test_gemini_schema_drops_union_types():
    """The exact shape that passes config construction and then fails the
    real request."""
    out = providers.to_gemini_schema({"type": "object", "properties": {
        "methodology": {"type": ["string", "null"], "description": "x"},
    }, "additionalProperties": False})
    assert out["properties"]["methodology"]["type"] == "string"
    assert out["properties"]["methodology"]["nullable"] is True
    assert out["properties"]["methodology"]["description"] == "x"
    assert "additionalProperties" not in out


def test_gemini_schema_recurses_into_arrays():
    out = providers.to_gemini_schema({"type": "array", "items": {"type": ["integer", "null"]}})
    assert out["items"] == {"type": "integer", "nullable": True}


def test_gemini_schema_leaves_plain_types_alone():
    out = providers.to_gemini_schema({"type": "string", "enum": ["fast", "normal"]})
    assert out == {"type": "string", "enum": ["fast", "normal"]}


def test_real_paper_schema_survives_translation():
    out = providers.to_gemini_schema(main.PAPER_SCHEMA)
    assert set(out["properties"]) == set(main.PAPER_SCHEMA["properties"])
    for field in out["properties"].values():
        assert not isinstance(field.get("type"), list), "no union types may survive"


# ---------- Provider selection ----------


def test_unknown_provider_is_reported_not_raised(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "nonesuch")
    provider, error = providers.build_provider(15.0, 0)
    assert provider is None and "nonesuch" in error


def test_missing_key_names_the_right_env_var(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "gemini")
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    provider, error = providers.build_provider(15.0, 0)
    assert provider is None and "GEMINI_API_KEY" in error


def test_blank_model_id_falls_back_to_default(monkeypatch):
    """.env.example ships `EXTRACTION_MODEL=` for the user to leave alone,
    which sets the variable to "". That must mean "use the default", not
    "send an empty model name" — which surfaces as a confusing
    "model is required" error from deep inside the SDK."""
    monkeypatch.setenv("LLM_PROVIDER", "gemini")
    monkeypatch.setenv("GEMINI_API_KEY", INVALID_KEY)
    monkeypatch.setenv("EXTRACTION_MODEL", "")
    monkeypatch.setenv("SYNTHESIS_MODEL", "")
    provider, error = providers.build_provider(15.0, 0)
    assert error is None
    assert provider.extraction_model == providers.DEFAULTS["gemini"][0]
    assert provider.synthesis_model == providers.DEFAULTS["gemini"][1]


def test_model_ids_are_env_overridable(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "gemini")
    monkeypatch.setenv("GEMINI_API_KEY", INVALID_KEY)
    monkeypatch.setenv("EXTRACTION_MODEL", "custom-extract")
    monkeypatch.setenv("SYNTHESIS_MODEL", "custom-synth")
    provider, error = providers.build_provider(15.0, 0)
    assert error is None
    assert provider.extraction_model == "custom-extract"
    assert provider.synthesis_model == "custom-synth"

#!/usr/bin/env python3
"""
providers.py — One interface over the LLM backends the demo can run on.

The pipeline needs exactly two things from a provider, and the rest of
main.py should not care which vendor is behind them:

  * `extract(prompt, schema)` — schema-conforming JSON in one shot
  * `stream(prompt)` — text chunks as they arrive

Both are verified against the installed SDKs rather than written from
memory. That matters here specifically: an earlier version of this backend
called Anthropic with an `output_config=` parameter that does not exist in
anthropic 0.69.0, so extraction raised TypeError on every single request and
nobody noticed, because every manual test stopped at "API key not set" one
step earlier. Porting to a second vendor doubles the surface for that class
of mistake, so `tests/test_api_shape.py` asserts each provider's calls reach
the API and fail on auth — not on a bad argument.
"""
from __future__ import annotations

import json
import os
from typing import AsyncIterator, Protocol


class Provider(Protocol):
    name: str
    extraction_model: str
    synthesis_model: str

    async def extract(self, prompt: str, schema: dict) -> dict: ...
    def stream(self, prompt: str) -> AsyncIterator[str]: ...


# ---------- Anthropic ----------


class AnthropicProvider:
    name = "anthropic"

    def __init__(self, api_key: str, extraction_model: str, synthesis_model: str,
                 timeout: float, max_retries: int):
        import anthropic
        self._anthropic = anthropic
        self.extraction_model = extraction_model
        self.synthesis_model = synthesis_model
        self._client = anthropic.AsyncAnthropic(
            api_key=api_key, timeout=timeout, max_retries=max_retries,
        )

    async def extract(self, prompt: str, schema: dict) -> dict:
        # Forced single-tool call, not a JSON response-format parameter:
        # anthropic 0.69.0's Messages API has no such top-level option, and
        # passing one raises TypeError before the request is ever sent.
        response = await self._client.messages.create(
            model=self.extraction_model,
            max_tokens=1024,
            tools=[{
                "name": "extract_paper_attributes",
                "description": "Extract structured attributes from a paper description.",
                "input_schema": schema,
            }],
            tool_choice={"type": "tool", "name": "extract_paper_attributes"},
            messages=[{"role": "user", "content": prompt}],
        )
        return next(b for b in response.content if b.type == "tool_use").input

    async def stream(self, prompt: str) -> AsyncIterator[str]:
        async with self._client.messages.stream(
            model=self.synthesis_model,
            max_tokens=2048,
            messages=[{"role": "user", "content": prompt}],
        ) as stream:
            async for text in stream.text_stream:
                yield text


# ---------- Gemini ----------


def to_gemini_schema(schema: dict) -> dict:
    """Rewrite a JSON Schema into the subset Gemini's response_schema accepts.

    Gemini's Schema takes one type per field plus a `nullable` flag, where
    JSON Schema allows a union: `{"type": ["string", "null"]}`. Passing the
    union through raises a pydantic ValidationError — and notably, it raises
    it at call time, NOT when GenerateContentConfig is constructed, so a
    config object that looks fine still blows up on the first real request.
    Verified against google-genai 2.15.0.

    Also drops `additionalProperties`, which Gemini's Schema has no field for.
    """
    if not isinstance(schema, dict):
        return schema
    out: dict = {}
    for key, value in schema.items():
        if key == "additionalProperties":
            continue
        if key == "type" and isinstance(value, list):
            non_null = [t for t in value if t != "null"]
            out["type"] = non_null[0] if non_null else "string"
            if "null" in value:
                out["nullable"] = True
        elif key == "properties" and isinstance(value, dict):
            out["properties"] = {k: to_gemini_schema(v) for k, v in value.items()}
        elif key == "items":
            out["items"] = to_gemini_schema(value)
        else:
            out[key] = value
    return out


class GeminiProvider:
    name = "gemini"

    def __init__(self, api_key: str, extraction_model: str, synthesis_model: str,
                 timeout: float, max_retries: int):
        from google import genai
        from google.genai import types
        self._types = types
        self.extraction_model = extraction_model
        self.synthesis_model = synthesis_model
        # timeout is milliseconds here, unlike the Anthropic client's seconds.
        self._client = genai.Client(
            api_key=api_key,
            http_options=types.HttpOptions(timeout=int(timeout * 1000)),
        )

    async def extract(self, prompt: str, schema: dict) -> dict:
        response = await self._client.aio.models.generate_content(
            model=self.extraction_model,
            contents=prompt,
            config=self._types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=to_gemini_schema(schema),
                temperature=0,
            ),
        )
        return json.loads(response.text)

    async def stream(self, prompt: str) -> AsyncIterator[str]:
        stream = await self._client.aio.models.generate_content_stream(
            model=self.synthesis_model,
            contents=prompt,
            config=self._types.GenerateContentConfig(max_output_tokens=2048),
        )
        async for chunk in stream:
            if chunk.text:
                yield chunk.text


# ---------- Selection ----------

DEFAULTS = {
    "anthropic": ("claude-haiku-4-5", "claude-sonnet-5"),
    # Model IDs are env-overridable on purpose: these are recent releases and
    # the exact ID strings should be confirmed against the provider's own
    # model list rather than trusted from a changelog.
    "gemini": ("gemini-3.5-flash-lite", "gemini-3.5-flash-lite"),
}

KEY_ENV = {"anthropic": "ANTHROPIC_API_KEY", "gemini": "GEMINI_API_KEY"}


def build_provider(timeout: float, max_retries: int) -> tuple[Provider | None, str | None]:
    """(provider, error). Exactly one is None."""
    name = os.environ.get("LLM_PROVIDER", "gemini").strip().lower()
    if name not in DEFAULTS:
        return None, f"LLM_PROVIDER={name!r} is not one of: {', '.join(DEFAULTS)}"

    api_key = os.environ.get(KEY_ENV[name])
    if not api_key:
        return None, (f"{KEY_ENV[name]} not set on the server (LLM_PROVIDER={name}) "
                      "— see demo/backend/.env.example")

    default_extract, default_synth = DEFAULTS[name]
    extraction_model = os.environ.get("EXTRACTION_MODEL", default_extract)
    synthesis_model = os.environ.get("SYNTHESIS_MODEL", default_synth)

    cls = {"anthropic": AnthropicProvider, "gemini": GeminiProvider}[name]
    try:
        return cls(api_key, extraction_model, synthesis_model, timeout, max_retries), None
    except ImportError as exc:
        return None, (f"the {name} SDK is not installed: {exc}. "
                      "Run: pip install -r demo/backend/requirements.txt")

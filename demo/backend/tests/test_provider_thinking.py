#!/usr/bin/env python3
"""
test_provider_thinking.py — Which `thinking` value switches thinking off, per Claude model.

Pure functions, no network. The mapping exists because the answer differs by model and a
wrong one is a 400 from the API (Claude Sonnet 5.5 rejects {"type": "disabled"} and wants
"between_tools"), while leaving thinking on makes Claude Haiku 5.5 spend the whole
max_tokens budget thinking and return an empty recommendation. Both were observed on
2026-10-16 against the real API; this pins the table so a refactor cannot quietly lose it.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import providers  # noqa: E402


def test_haiku_55_is_switched_off_with_disabled():
    assert providers.thinking_off("claude-haiku-5-5") == {"type": "disabled"}


def test_sonnet_55_needs_between_tools_not_disabled():
    off = providers.thinking_off("claude-sonnet-5-5")
    assert off == {"type": "between_tools"}
    assert off != {"type": "disabled"}  # the API answers 400 to this one for this model


def test_a_model_that_is_not_listed_gets_no_thinking_parameter():
    # claude-haiku-4-5 (the default extraction model) only thinks when asked to, so
    # sending nothing is correct; and an unknown ID must not be sent a guess.
    assert providers.thinking_off("claude-haiku-4-5") is None
    assert providers.thinking_off("some-future-model") is None


def test_ids_are_matched_exactly_not_by_prefix():
    # "claude-sonnet-5" is a prefix of "claude-sonnet-5-5"; they need different values.
    assert providers.thinking_off("claude-sonnet-5") != providers.thinking_off("claude-sonnet-5-5")


def test_every_table_entry_is_a_plain_thinking_object():
    for model, value in providers.THINKING_OFF.items():
        assert set(value) == {"type"}, f"{model}: only `type` may be sent when switching thinking off"

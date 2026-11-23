#!/usr/bin/env python3
"""
test_tier1_gate.py — what counts as an evidence line for the Sourced gate (tier1_gate.py).

A line that records a gap (blocked page, zero results) is a recorded blank and
must not count as evidence, even when it carries a URL. The first version of the
rule also matched any bare "405", so a row stating a denominator of 405
abstracts was dropped as if it were an HTTP error. Fixtures are inline strings.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import tier1_gate as gate  # noqa: E402


def _ev(text: str) -> int:
    return len(gate.evidence_lines(text))


def test_a_count_that_looks_like_an_http_status_is_still_a_count():
    row = "| ethnography | 41 of 405 abstracts (10.1%) | https://api.crossref.org/works?x=1 |"
    assert _ev(row) == 1


def test_an_http_error_line_is_a_gap_even_with_a_url():
    assert _ev("The live page returned HTTP 403: https://example.org/guidelines") == 0
    assert _ev("https://example.org/about returned 403") == 0
    assert _ev("403 forbidden at https://example.org/board") == 0


def test_zero_result_and_unreadable_lines_are_gaps():
    assert _ev("SciRev: 0 reviews https://scirev.org/x") == 0
    assert _ev("Board page unreadable (no archive copy): https://example.org/board") == 0


def test_a_cited_fact_counts():
    assert _ev("Word limit 8,000 words including references: https://example.org/guidelines") == 1


def test_two_evidence_lines_make_a_subsection_backed_and_one_does_not():
    two = "Aims: https://example.org/aims is clear about scope here.\nBoard: 25 entries, https://example.org/board lists them."
    one = "Aims: https://example.org/aims is clear about scope here, and nothing else is stated for this heading."
    assert gate.subsection_state(two) == "backed"
    assert gate.subsection_state(one) == "estimate"

#!/usr/bin/env python3
"""
test_update_metrics.py — the monthly refresh rewrites a metric's number and its
date, and nothing else in the row.

The first scheduled run (2026-11-01) rewrote the whole date/source cell of every
metric row it touched. That deleted 161 "(OpenAlex, via spine)" provenance notes
and a hand-written caveat on Frontiers in Psychology's h-index ("whole
megajournal, not just PSP section"). Nothing in CI could have caught it: the
output validated and linted clean, because a missing note is not a violation.

Fixtures are small inline markdown snippets, not the real corpus.
"""
from __future__ import annotations

import importlib
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import update_metrics as um  # noqa: E402


TODAY = "2026-11-22"
CAVEAT = "(OpenAlex — whole Frontiers in Psychology megajournal, not just PSP section)"


# ---------- refresh_date_cell ----------


def test_plain_date_is_replaced():
    assert um.refresh_date_cell("2026-05-16", TODAY) == TODAY


def test_hand_written_caveat_after_the_date_is_kept_verbatim():
    assert um.refresh_date_cell(f"2026-05-13 {CAVEAT}", TODAY) == f"{TODAY} {CAVEAT}"


def test_spine_tag_is_replaced_not_carried_over():
    # The value now comes from the API, so "via spine" would be a false provenance claim.
    assert um.refresh_date_cell("2026-05-16 (OpenAlex, via spine)", TODAY) == f"{TODAY} (OpenAlex)"


def test_spine_tag_match_ignores_case_and_spacing():
    assert um.refresh_date_cell("2026-07-13 ( openalex ,  via Spine )", TODAY) == f"{TODAY} (OpenAlex)"


def test_cell_without_a_date_still_gets_one_and_keeps_its_text():
    out = um.refresh_date_cell("(OpenAlex)", TODAY)
    assert out.startswith(TODAY) and "(OpenAlex)" in out


def test_refreshing_twice_does_not_accumulate_notes():
    once = um.refresh_date_cell(f"2026-05-13 {CAVEAT}", "2026-11-01")
    twice = um.refresh_date_cell(once, "2026-12-01")
    assert twice == f"2026-12-01 {CAVEAT}"


# ---------- apply_file_diff, end to end on one small file ----------

ENTRY = f"""# Example Journal

> **Last verified**: 2026-05-16

## Metrics

| Metric | Value | Source / date |
|---|---|---|
| **h-index** | 302 | 2026-05-13 {CAVEAT} |
| **2-yr Mean Citedness (OpenAlex IF proxy)** | 4.10 | 2026-05-16 (OpenAlex, via spine) |
| **i10-index** | 500 | 2026-05-16 |
| **Total Works** | 9000 | 2026-05-16 |

## Changelog
| Date | Change | By |
|------|--------|----|
| 2026-05-16 | Created | @maintainer |
"""


def _apply(tmp_path: Path, diffs: list[um.MetricDiff]) -> str:
    path = tmp_path / "example-journal.md"
    path.write_text(ENTRY, encoding="utf-8")
    um.apply_file_diff(um.FileDiff(path=path, issn="1234-5678", diffs=diffs), TODAY)
    return path.read_text(encoding="utf-8")


def test_apply_changes_number_and_date_but_keeps_the_rest_of_the_row(tmp_path):
    out = _apply(tmp_path, [
        um.MetricDiff("h_index", "302", "313"),
        um.MetricDiff("two_yr_citedness", "4.10", "4.25"),
        um.MetricDiff("i10_index", "500", "500"),          # unchanged: row must stay as it was
        um.MetricDiff("works_count", "9000", "9120"),
    ])
    assert f"| **h-index** | 313 | {TODAY} {CAVEAT} |" in out
    assert f"| **2-yr Mean Citedness (OpenAlex IF proxy)** | 4.25 | {TODAY} (OpenAlex) |" in out
    assert "| **i10-index** | 500 | 2026-05-16 |" in out
    assert f"| **Total Works** | 9120 | {TODAY} |" in out


def test_apply_bumps_last_verified_and_adds_one_changelog_row(tmp_path):
    out = _apply(tmp_path, [um.MetricDiff("h_index", "302", "313")])
    assert f"> **Last verified**: {TODAY}" in out
    assert f"| {TODAY} | Refreshed metrics from OpenAlex (h_index) | @bot |" in out
    assert out.count("Refreshed metrics from OpenAlex") == 1


def test_apply_with_nothing_changed_leaves_the_file_alone(tmp_path):
    out = _apply(tmp_path, [um.MetricDiff("h_index", "302", "302")])
    assert out == ENTRY


# ---------- the helpers must be importable, and main() must say why, without pyalex ----------


def test_module_imports_without_pyalex_and_main_reports_it(monkeypatch, capsys):
    monkeypatch.setitem(sys.modules, "pyalex", None)       # "from pyalex import ..." now raises ImportError
    monkeypatch.setattr(sys, "argv", ["update_metrics.py"])
    sys.modules.pop("update_metrics", None)
    try:
        fresh = importlib.import_module("update_metrics")
        assert fresh.Sources is None
        assert fresh.main() == 1
        assert "pyalex not installed" in capsys.readouterr().err
    finally:
        sys.modules.pop("update_metrics", None)

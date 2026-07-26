#!/usr/bin/env python3
"""Tests for lint_content.py's own checks — a linter that silently passes
everything is as bad as no linter."""
from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lint_content  # noqa: E402


def test_uncited_high_methodology_score_flagged():
    content = """
## Soft Metadata

### Methodological Preferences

| Method | Receptiveness (0-5) | Evidence |
|--------|---------------------|----------|
| Autoethnography | 5 | Family norm |
"""
    violations = lint_content.check_uncited_high_scores(content)
    assert len(violations) == 1
    assert "Autoethnography" in violations[0]


def test_cited_high_methodology_score_not_flagged():
    content = """
## Soft Metadata

### Methodological Preferences

| Method | Receptiveness (0-5) | Evidence |
|--------|---------------------|----------|
| Meta-analysis | 4 | 12 articles found 2020-2025, https://example.com |
"""
    assert lint_content.check_uncited_high_scores(content) == []


def test_substantive_prose_justification_not_flagged():
    """The false-positive class that made the first version of this check
    unusable: a hand-authored justification naming a specific, checkable
    thing about the journal has no digit and no URL, but is nothing like a
    "Family norm" template default. Flagging it trains people to ignore
    the linter."""
    content = """
## Soft Metadata

### Sensitive Topics

| Topic Category | Receptiveness | Evidence |
|----------------|---------------|----------|
| Methodology critique | High | Methodology and Research Practice section explicitly welcomes critical work |
"""
    assert lint_content.check_uncited_high_scores(content) == []


def test_is_contentless_boundary():
    assert lint_content.is_contentless("Family norm")
    assert lint_content.is_contentless("Welcomed")
    assert lint_content.is_contentless("Core method")
    assert not lint_content.is_contentless("Core method — controlled cognitive experiments on memory")
    assert not lint_content.is_contentless("5 articles 2020-2025")  # has a digit -> cited


def test_low_score_never_flagged_even_if_uncited():
    """The whole point is asymmetric: only HIGH uncited claims are a problem."""
    content = """
## Soft Metadata

### Methodological Preferences

| Method | Receptiveness (0-5) | Evidence |
|--------|---------------------|----------|
| Autoethnography | 1 | |
"""
    assert lint_content.check_uncited_high_scores(content) == []


def test_uncited_high_sensitive_topic_flagged():
    content = """
## Soft Metadata

### Sensitive Topics

| Topic Category | Receptiveness | Evidence |
|-----------------|---------------|----------|
| BDSM / Kink | High | Family norm |
"""
    violations = lint_content.check_uncited_high_scores(content)
    assert any("BDSM" in v for v in violations)


def test_separator_row_not_treated_as_a_sensitive_topic():
    content = """
## Soft Metadata

### Sensitive Topics

| Topic Category | Receptiveness | Evidence |
|-----------------|---------------|----------|
| Drug use | Low | 0 articles |
"""
    assert lint_content.check_uncited_high_scores(content) == []


def test_tier1_with_placeholder_flagged():
    content = """
## Soft Metadata

### Framing Requirements

*(fill manually)*
"""
    violations = lint_content.check_tier1_placeholders(content)
    assert len(violations) == 1


def test_tier2_with_placeholder_not_flagged():
    """Tier 2's whole point is family-level, not-yet-per-journal content —
    an unfilled cell there isn't a defect, it's the honest default state."""
    content = """
## Soft Metadata

> [!WARNING]
> **Tier 2 (community estimate)** — family-level adaptation.

### Framing Requirements

*(fill manually)*
"""
    assert lint_content.check_tier1_placeholders(content) == []


def test_ai_researched_without_signal_quality_flagged():
    content = """
## Soft Metadata

> [!NOTE]
> **AI-Researched (2026-07-13)** — per-journal sourced facts.

### AI-Research Notes

Some findings, no score mentioned anywhere.
"""
    assert lint_content.check_ai_researched_has_signal_quality(content) != []


def test_ai_researched_with_signal_quality_not_flagged():
    content = """
## Soft Metadata

> [!NOTE]
> **AI-Researched (2026-07-13)** — per-journal sourced facts. Overall
> `signal_quality` for this pass: **2/5**.
"""
    assert lint_content.check_ai_researched_has_signal_quality(content) == []


def test_tier1_entry_unaffected_by_ai_researched_check():
    content = "## Soft Metadata\n\n### Epistemological & Political Leanings\n"
    assert lint_content.check_ai_researched_has_signal_quality(content) == []


# ---------- baseline mechanism (freezes pre-existing debt, blocks new/worse) ----------


def test_baseline_missing_file_treated_as_empty():
    assert lint_content._load_baseline("/does/not/exist.json") == {}


def test_relkey_is_relative_and_forward_slashed():
    p = os.path.join(lint_content.JOURNALS_ROOT, "hci", "acm-chi.md")
    key = lint_content.relkey(p)
    assert key == "hci/acm-chi.md"
    assert "\\" not in key

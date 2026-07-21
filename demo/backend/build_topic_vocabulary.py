#!/usr/bin/env python3
"""Build the demo's topic vocabulary from the curated corpus.

fit_score.py's score_topic_density() matches Paper.topics against each
journal's Subject Density > Top Topics table via bidirectional substring
containment (not fuzzy/token overlap) — so an extracted topic phrase only
scores non-neutral when it is near-verbatim to a real OpenAlex topic name
that appears in a candidate's table. The demo's extraction stage never
reads journal files (unlike a real skill session, where the assisting
model reads Top Topics tables directly before phrasing --topics), so
without this vocabulary it has zero chance of aligning its phrasing to
real topic names.

Run manually whenever references/journals/**/*.md changes:
    python build_topic_vocabulary.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

SKILL_SCRIPTS = Path(__file__).resolve().parents[2] / "skills" / "journal-atlas" / "scripts"
sys.path.insert(0, str(SKILL_SCRIPTS))
import fit_score  # noqa: E402 - reuse its Top Topics parser, don't reimplement

JOURNALS_ROOT = SKILL_SCRIPTS.parent / "references" / "journals"
OUTPUT_PATH = Path(__file__).resolve().parent / "topic_vocabulary.json"


def collect_topics() -> list[str]:
    names: set[str] = set()
    for path in sorted(JOURNALS_ROOT.rglob("*.md")):
        if path.name == "TEMPLATE.md":
            continue
        content = path.read_text(encoding="utf-8")
        for topic, _count in fit_score._extract_top_topics(content):
            names.add(topic)
    return sorted(names)


def main() -> None:
    topics = collect_topics()
    OUTPUT_PATH.write_text(json.dumps(topics, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {len(topics)} unique topics to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

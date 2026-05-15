---
name: ja-query
description: "Structured filter query over the journal knowledge base. Ask for journals by criteria like Q1, Sage publisher, h-index >= 100, no AI permission gate, zero embargo, OA model, etc."
---

Run Query Mode from `skills/journal-atlas/SKILL.md`.

Map $ARGUMENTS to `scripts/query_journals.py` flags and run the script. Present the result table directly. If the user follows up wanting a recommendation among the filtered set, switch to `/ja-recommend` with those journals as the candidate set.

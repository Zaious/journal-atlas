---
name: ja-recommend
description: "Recommend journals for your paper. Describe your paper (topic, methodology, word count, APC budget, OA need, AI usage, IRB status, sensitive content) and get a ranked recommendation with evidence, fallback chains, and strategic notes."
---

Run the full journal recommendation workflow from `skills/journal-atlas/SKILL.md` (Steps 1–5).

If the user provides $ARGUMENTS, treat them as the paper description and skip the attribute-extraction prompt. Otherwise, ask for the 10 paper attributes per Step 1.

---
name: ja-related
description: "Find recent papers within a target journal that match your research keywords. Useful for cover-letter prep ('we engage with your recent X, Y, Z') or verifying a journal is still active on your topic."
---

Run `scripts/related_papers.py` with the journal and keywords from $ARGUMENTS.

If $ARGUMENTS contains a journal name and keywords (e.g. "PCS embodied cognition self-state"), parse them and run the script. If ambiguous, ask the user to clarify which is the journal and which are keywords.

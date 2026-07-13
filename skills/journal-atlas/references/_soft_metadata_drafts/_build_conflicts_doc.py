import json

proposals = json.load(open("_merge_patch_proposals.json", encoding="utf-8"))
total_conflicts = sum(len(r.get("conflicts") or []) for r in proposals)
total_journals = sum(1 for r in proposals if r.get("conflicts"))

lines = [
    "# Existing-Entry Merge — Flagged Conflicts (Human Review Needed)",
    "",
    "> Generated 2026-07-13 from the 112-file careful comparison merge (see GAPS_AND_NOTES.md).",
    "> These are cases where the existing curated entry already had real content in an",
    "> in-scope field, and the WO2 research draft found something different or additional.",
    '> Per the "不粗填不覆蓋" instruction, none of these were auto-resolved — each needs a',
    "> maintainer to read both sides and decide.",
    "",
    f"**Total: {total_conflicts} conflicts across {total_journals} journals.**",
    "",
]

for r in proposals:
    conflicts = r.get("conflicts") or []
    if not conflicts:
        continue
    lines.append(f"## {r['name']}")
    lines.append(f"`{r['md_path']}`")
    lines.append("")
    for c in conflicts:
        lines.append(f"- **{c.get('field', '?')}**")
        lines.append(f"  - Existing: {c.get('existing_value', '')}")
        lines.append(f"  - WO2 finding: {c.get('wo2_value', '')}")
        lines.append(f"  - Why flagged: {c.get('why_flagged', '')}")
        lines.append("")
    lines.append("---")
    lines.append("")

open("EXISTING_ENTRY_CONFLICTS.md", "w", encoding="utf-8").write("\n".join(lines))
print(f"wrote EXISTING_ENTRY_CONFLICTS.md: {total_conflicts} conflicts across {total_journals} journals")

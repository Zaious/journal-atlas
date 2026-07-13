#!/usr/bin/env python3
"""
Additive-only patch: for the 114 journals that already have a curated .md entry
AND also got a WO2 soft-metadata research draft, insert a new "AI-Research Notes
(WO2 supplement)" subsection under the existing "## Soft Metadata" section, and
append one Changelog row. Never touches existing Tier 1 / Tier 2 content — this
is deliberately conservative (see GAPS_AND_NOTES.md "Not yet done").

Idempotent: skips files that already have the WO2-supplement marker.

Usage:
    python patch_existing_entries.py --dry-run [--sample 3]
    python patch_existing_entries.py --write
"""
from __future__ import annotations
import argparse, json, re, sys, glob, os
from datetime import date

for _s in (sys.stdout, sys.stderr):
    try: _s.reconfigure(encoding="utf-8")
    except Exception: pass

SKILL_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
JOURNALS_DIR = os.path.join(SKILL_ROOT, "references", "journals")
CONSOLIDATED = os.path.join(SKILL_ROOT, "references", "_soft_metadata_drafts", "consolidated_all.json")

MARKER = "AI-Research Notes (WO2 supplement"
PIPELINE_GENERATED_MARKER = "AI-researched entry (WO2 pipeline)"  # written by merge_soft_metadata.py — skip, not a hand-curated entry to supplement


def normissn(s):
    if not s: return None
    s = re.sub(r"[^0-9Xx]", "", str(s)).upper()
    return s if len(s) == 8 else None


def index_existing():
    existing = {}
    for fp in glob.glob(os.path.join(JOURNALS_DIR, "**", "*.md"), recursive=True):
        txt = open(fp, encoding="utf-8").read()
        for i in re.findall(r"\*\*ISSN \((?:Print|Online)\)\*\*\s*\|\s*([0-9]{4}-[0-9]{3}[0-9Xx])", txt):
            n = normissn(i)
            if n:
                existing[n] = fp
    return existing


def fmt(v, fallback="*(not researched)*"):
    if v is None or v == "" or v == []:
        return fallback
    if isinstance(v, list):
        return "; ".join(str(x) for x in v)
    return str(v)


def build_supplement_block(e: dict, today: str) -> str:
    ai = e.get("ai_policy") or {}
    pos = e.get("positioning") or {}
    exp = e.get("experiential") or {}
    blanks = e.get("blanks") or []
    xlang = e.get("cross_language_checked") or []
    sq = e.get("overall_signal_quality")

    pos_sources = pos.get("sources") or []
    exp_sources = exp.get("sources") or []
    ai_src = [ai["source_url"]] if ai.get("source_url") else []
    all_sources = sorted(set(pos_sources) | set(exp_sources) | set(ai_src))
    sources_md = "\n".join(f"- {u}" for u in all_sources) or "*(none)*"
    blanks_md = "\n".join(f"- **{b.get('field','?')}**: {b.get('why','')}" for b in blanks) or "*(none recorded)*"
    xlang_md = "\n".join(f"- {x}" for x in xlang) or "*(not recorded)*"

    return f"""
### {MARKER}, {today})

> Added by `scripts/spine/patch_existing_entries.py` as a **supplementary, independent research pass** — it does NOT overwrite or supersede the Tier assessment above. Treat conflicts as a signal to re-verify, not as an automatic correction. Overall WO2 `signal_quality` for this pass: **{fmt(sq, "0")}/5**.

**WO2 AI policy finding:** {fmt(ai.get("summary"))}

**WO2 positioning finding (what the journal accepts now):** {fmt(pos.get("accepts_now"))}

**WO2 experiential finding:** {fmt(exp.get("acceptance_note"))} {fmt(exp.get("reviewer_culture"), "")}

**Sources cited in this pass:**
{sources_md}

**Fields WO2 could not find evidence for:**
{blanks_md}

**Cross-language checks performed:**
{xlang_md}
"""


def patch_file(path: str, e: dict, today: str) -> str | None:
    """Return patched content, or None if already patched / pipeline-generated / no anchor found."""
    txt = open(path, encoding="utf-8").read()
    if MARKER in txt or PIPELINE_GENERATED_MARKER in txt:
        return None
    anchor = "\n---\n\n## Strategic Notes"
    if anchor not in txt:
        # fallback anchor without leading --- separator
        anchor = "\n## Strategic Notes"
        if anchor not in txt:
            return None
    block = build_supplement_block(e, today)
    patched = txt.replace(anchor, block + anchor, 1)

    # append a Changelog row (find the last markdown table row under '## Changelog')
    changelog_marker = "## Changelog"
    if changelog_marker in patched:
        idx = patched.rindex(changelog_marker)
        # insert a new row right after the header row of the table (first '|---' line after idx)
        after = patched[idx:]
        m = re.search(r"\|[-\s|]+\|\n", after)
        if m:
            insert_at = idx + m.end()
            new_row = f"| {today} | Added WO2 AI-research supplement (see Soft Metadata > AI-Research Notes) — independent research pass, does not alter existing Tier assessment. | @Zaious |\n"
            patched = patched[:insert_at] + new_row + patched[insert_at:]
    return patched


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--sample", type=int, default=3)
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    if not args.dry_run and not args.write:
        ap.error("specify --dry-run or --write")

    consolidated = json.load(open(CONSOLIDATED, encoding="utf-8"))
    existing = index_existing()
    today = date.today().isoformat()

    matches = []
    for e in consolidated["entries"]:
        issn = normissn(e.get("issn"))
        if issn and issn in existing:
            matches.append((existing[issn], e))

    print(f"{len(matches)} existing files matched to a WO2 draft", file=sys.stderr)

    patched_count, skipped_already, skipped_pipeline, skipped_no_anchor = 0, 0, 0, 0
    previews = []
    for path, e in matches:
        result = patch_file(path, e, today)
        if result is None:
            txt = open(path, encoding="utf-8").read()
            if PIPELINE_GENERATED_MARKER in txt:
                skipped_pipeline += 1
            elif MARKER in txt:
                skipped_already += 1
            else:
                skipped_no_anchor += 1
            continue
        patched_count += 1
        if args.dry_run and len(previews) < args.sample:
            previews.append((path, result))
        if args.write:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(result)

    print(f"would patch / patched: {patched_count}", file=sys.stderr)
    print(f"skipped (pipeline-generated, not a hand-curated entry): {skipped_pipeline}", file=sys.stderr)
    print(f"skipped (already patched): {skipped_already}", file=sys.stderr)
    print(f"skipped (no Strategic Notes anchor found): {skipped_no_anchor}", file=sys.stderr)

    if args.dry_run:
        for path, content in previews:
            print(f"\n{'='*100}\n{path}\n{'='*100}")
            # show only the inserted block + a bit of context
            i = content.find(MARKER)
            print(content[max(0, i - 50):i + 1800])


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
cite_uncited_high_scores.py — Attach real OpenAlex counts to high scores
(4-5 / "High") whose Evidence cell is a contentless template default.

lint_content.py flags 373 such cells (2026-07-27). Only a subset can be
fixed by automation, and this script deliberately handles only that subset:

  * RELIABLE rows only — Autoethnography, Qualitative interviews,
    Meta-analysis, and the 5 standard Sensitive Topics. These are the exact
    categories enrich_methodology_evidence.py verified as reliably countable
    by keyword search. "Quantitative experimental", "Mixed methods" and
    "Theoretical / Conceptual" are excluded on the same empirical grounds it
    documents: papers rarely self-tag with those labels, so a count
    undercounts badly and would manufacture false corrections.
  * Entries with an ISSN only — conference entries have none by design.

Asymmetric, exactly as the existing evidence pass is:

  hits == 0  -> a 4-5 / "High" is contradicted by an actual zero count.
                Downgrade, citing the count.
  hits > 0   -> cite the count as CORROBORATION. The 0-5 level itself stays
                a family-level estimate; a count can show the journal does
                publish the method, but cannot by itself justify a 5 over a
                4. That still needs editorial-statement-level evidence.

Two-phase, like its sibling scripts:
    python cite_uncited_high_scores.py --dry-run
    python cite_uncited_high_scores.py --write
"""
from __future__ import annotations
import argparse, json, os, re, sys
from datetime import date

for _s in (sys.stdout, sys.stderr):
    try: _s.reconfigure(encoding="utf-8")
    except Exception: pass

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import fit_score  # noqa: E402
import lint_content  # noqa: E402
from enrich_methodology_evidence import (  # noqa: E402 - reuse, don't reimplement
    extract_issn, fetch_or_cache, category_hits, score_methodology, score_sensitive,
    METHODOLOGY_KEYWORDS, SENSITIVE_KEYWORDS, MIN_SAMPLE_FOR_CORRECTION,
    find_section, parse_table_row, insert_changelog_row,
)

SKILL_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
REPORT_PATH = os.path.join(SKILL_ROOT, "references", "_soft_metadata_drafts", "_cite_uncited_report.json")


def corroboration_text(hits: int, total: int, ws: str, we: str) -> str:
    """Say what the count actually shows, which is not the same at every rate.

    A 4-5 backed by 1 article in 699 is not corroborated by that article —
    calling it so would be exactly the kind of confident-sounding filler this
    pass exists to remove. But a low count doesn't disprove receptiveness
    either: counts measure published output, not what an editor would accept,
    and low output can mean low submission volume. So state the rate plainly
    and let the reader weigh it, rather than overclaiming in either
    direction.
    """
    ratio = hits / total if total else 0
    if ratio >= 0.02:
        verdict = "confirms the journal publishes this at a meaningful rate"
    elif ratio >= 0.005:
        verdict = ("shows the journal does publish this, but uncommonly — the high rating is a "
                   "family-level estimate that this output rate does not by itself support")
    else:
        verdict = ("a very low rate — this count does NOT support the high rating, which remains an "
                   "uncorroborated family-level estimate; note that counts measure published output, "
                   "not what an editor would accept")
    return (f"{hits} article(s) found (OpenAlex keyword search, {ws[:4]}-{we[:4]}, {total} total in window; "
            f"{ratio:.1%}) — {verdict}")


def contradiction_text(total: int, ws: str, we: str) -> str:
    return (f"0 article(s) found (OpenAlex keyword search, {ws[:4]}-{we[:4]}, {total} total in window) "
            f"— an actual zero count contradicts the previous high rating, which carried no evidence")


def has_verifiable_violation(path: str) -> bool:
    """Offline pre-filter: does this file have a contentless 4-5 / "High" in
    a row this script can actually verify? Saves a network fetch per file
    whose violations are all in unreliable or bespoke rows."""
    content = open(path, encoding="utf-8").read()
    if not extract_issn(content):
        return False
    for section, keyword_map, is_methodology in (
        ("Methodological Preferences", METHODOLOGY_KEYWORDS, True),
        ("Sensitive Topics", SENSITIVE_KEYWORDS, False),
    ):
        sec = find_section(content, section)
        if not sec:
            continue
        for row in keyword_map:
            existing = parse_table_row(sec[2], row)
            if not existing:
                continue
            score_cell, evidence_cell = existing
            if not lint_content.is_contentless(evidence_cell):
                continue
            if is_methodology:
                m = re.match(r"\s*([0-5])\s*$", score_cell)
                if m and int(m.group(1)) >= 4:
                    return True
            elif score_cell.strip().lower() == "high":
                return True
    return False


def process_file(path: str) -> dict:
    content = open(path, encoding="utf-8").read()
    name = (re.search(r"^# +(.+?)\s*$", content, re.MULTILINE) or [None, os.path.basename(path)])[1]
    rel = lint_content.relkey(path)

    issn = extract_issn(content)
    if not issn:
        return {"path": path, "rel": rel, "name": name, "skip": "no ISSN (conference entry)"}

    scan = fetch_or_cache(issn)
    if not scan or "error" in scan:
        return {"path": path, "rel": rel, "name": name, "skip": f"OpenAlex lookup failed: {scan.get('error') if scan else '?'}"}
    total = scan["total_works"]
    if total < MIN_SAMPLE_FOR_CORRECTION:
        return {"path": path, "rel": rel, "name": name, "skip": f"only {total} works in window — too thin to judge"}

    actions = []
    for section, keyword_map, is_methodology in (
        ("Methodological Preferences", METHODOLOGY_KEYWORDS, True),
        ("Sensitive Topics", SENSITIVE_KEYWORDS, False),
    ):
        sec = find_section(content, section)
        if not sec:
            continue
        for row, keywords in keyword_map.items():
            existing = parse_table_row(sec[2], row)
            if not existing:
                continue
            score_cell, evidence_cell = existing
            if not lint_content.is_contentless(evidence_cell):
                continue  # already cited, or a substantive hand-authored justification
            if is_methodology:
                m = re.match(r"\s*([0-5])\s*$", score_cell)
                if not m or int(m.group(1)) < 4:
                    continue
            elif score_cell.strip().lower() != "high":
                continue

            hits = category_hits(scan, keywords)
            if hits == 0:
                new_score = str(score_methodology(0, total)) if is_methodology else score_sensitive(0, total)
                actions.append({"section": section, "row": row, "action": "DOWNGRADE",
                                "old_score": score_cell.strip(), "new_score": new_score,
                                "new_evidence": contradiction_text(total, scan["window_start"], scan["window_end"]),
                                "hits": 0, "total": total})
            else:
                actions.append({"section": section, "row": row, "action": "CITE",
                                "old_score": score_cell.strip(), "new_score": score_cell.strip(),
                                "new_evidence": corroboration_text(hits, total, scan["window_start"], scan["window_end"]),
                                "hits": hits, "total": total})
    return {"path": path, "rel": rel, "name": name, "issn": issn, "actions": actions}


def replace_row(content: str, section: str, action: dict) -> str:
    sec = find_section(content, section)
    if not sec:
        return content
    start, end, body = sec
    pattern = re.compile(rf"^\|\s*{re.escape(action['row'])}\s*\|[^|]*\|[^|]*\|", re.MULTILINE)
    m = pattern.search(body)
    if not m:
        return content
    new_row = f"| {action['row']} | {action['new_score']} | {action['new_evidence']} |"
    return content[:start] + body[:m.start()] + new_row + body[m.end():] + content[end:]


def apply_results(results: list[dict]) -> None:
    today = date.today().isoformat()
    applied = noop = 0
    for r in results:
        actions = r.get("actions") or []
        if not actions:
            continue
        original = open(r["path"], encoding="utf-8").read()
        content = original
        for a in actions:
            content = replace_row(content, a["section"], a)
        if content == original:
            noop += 1
            continue
        cites = [a for a in actions if a["action"] == "CITE"]
        downs = [a for a in actions if a["action"] == "DOWNGRADE"]
        parts = []
        if cites:
            parts.append(f"attached OpenAlex counts to {len(cites)} previously uncited high score(s) "
                         f"({', '.join(a['row'] for a in cites)})")
        if downs:
            parts.append("downgraded " + "; ".join(
                f"{a['row']} {a['old_score']}->{a['new_score']} (0 articles found)" for a in downs))
        row = (f"| {today} | Evidence-citation pass: {'; '.join(parts)}. Counts corroborate presence only — "
               f"the 0-5 level remains a family-level estimate. Restricted to categories verified as reliably "
               f"keyword-countable; see scripts/spine/cite_uncited_high_scores.py. | @Zaious (AI-assisted) |\n")
        content = insert_changelog_row(content, row)
        open(r["path"], "w", encoding="utf-8").write(content)
        applied += 1
    print(f"Applied to {applied} files ({noop} no-op)", file=sys.stderr)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--sample", type=int, default=0)
    args = ap.parse_args()
    if not args.dry_run and not args.write:
        ap.error("specify --dry-run or --write")

    if args.write:
        if not os.path.exists(REPORT_PATH):
            ap.error(f"no report at {REPORT_PATH} — run --dry-run first")
        apply_results(json.load(open(REPORT_PATH, encoding="utf-8")))
        return

    # Only files that actually have a contentless high score in a row this
    # script can verify. Checked before any network call — a flagged file
    # whose violations are all in unreliable/bespoke rows would otherwise
    # cost a full works-pagination fetch just to produce zero actions.
    targets = [p for p in lint_content.collect_files([]) if has_verifiable_violation(p)]
    if args.sample:
        targets = targets[:args.sample]

    import time as _time
    results = []
    for i, path in enumerate(targets, 1):
        r = process_file(path)
        results.append(r)
        status = f"SKIP: {r['skip']}" if "skip" in r else f"{len(r['actions'])} action(s)"
        print(f"[{i}/{len(targets)}] {r['name'][:48]:48s} {status}", file=sys.stderr)
        _time.sleep(0.2)

    cites = sum(len([a for a in r.get("actions", []) if a["action"] == "CITE"]) for r in results)
    downs = sum(len([a for a in r.get("actions", []) if a["action"] == "DOWNGRADE"]) for r in results)
    print(f"\n=== {len(targets)} files | {cites} citations | {downs} downgrades | "
          f"{len([r for r in results if 'skip' in r])} skipped ===", file=sys.stderr)
    json.dump(results, open(REPORT_PATH, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print(f"Report -> {REPORT_PATH}", file=sys.stderr)


if __name__ == "__main__":
    main()

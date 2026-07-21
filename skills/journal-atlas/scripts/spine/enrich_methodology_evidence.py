#!/usr/bin/env python3
"""
enrich_methodology_evidence.py — Fill Methodological Preferences / Sensitive
Topics cells with OpenAlex keyword-count evidence, for psychology/hci/
cognitive-science entries.

Scope, deliberately narrow (see docs/ATLAS_V2_DESIGN.md discussion 2026-07-20):
keyword-substring counting against recent OpenAlex output is a RELIABLE signal
for narrow, specific categories (autoethnography, mixed methods, meta-analysis,
qualitative interviews, and all 5 Sensitive Topics rows) but an UNRELIABLE one
for broad categories (Quantitative experimental, Theoretical / Conceptual) —
those routinely undercount because the literal keyword doesn't appear in
OpenAlex's topic/title text even when the category is clearly dominant.

Asymmetric scoring, by design: this pass can only prove ABSENCE/RARITY
(→ scores 0-3), never confirm high receptiveness (4-5 / "High" are never
auto-assigned — those require editorial-statement-level evidence, a
different and more expensive research step). This makes it good at:
  (a) filling AI-Researched honest-blanks with real low/moderate evidence
  (b) catching existing high-scored, uncited claims contradicted by an
      actual 0-hit count (the TOCHI autoethnography pattern from
      SEED_DATA_QUALITY.md's self-critique story, which was flagged in
      2026-05 but never actually corrected in the file)

Never touches cells that already carry a specific, checkable citation
(a number or URL in the Evidence column) — only blanks, and high/uncited
claims flatly contradicted by a 0-hit count.

Usage:
    python enrich_methodology_evidence.py --dry-run [--sample 5]
    python enrich_methodology_evidence.py --write
"""
from __future__ import annotations
import argparse, json, os, re, sys, glob
from datetime import date

for _s in (sys.stdout, sys.stderr):
    try: _s.reconfigure(encoding="utf-8")
    except Exception: pass

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from topic_trend_scan import resolve_source, fetch_works_in_window, check_keywords  # noqa: E402
# Set the OPENALEX_EMAIL env var before running for polite-pool access (higher rate
# limit) — see topic_trend_scan.py's own handling of this same env var.

SKILL_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
JOURNALS_DIR = os.path.join(SKILL_ROOT, "references", "journals")
CACHE_DIR = os.path.join(os.path.dirname(__file__), "..", ".cache", "methodology-evidence")
TARGET_DIRS = ["psychology", "hci", "cognitive-science"]
YEARS_WINDOW = 5

# Template row label -> OpenAlex search keyword(s) (OR'd — hit if any matches)
METHODOLOGY_KEYWORDS: dict[str, list[str]] = {
    "Autoethnography": ["autoethnography"],
    "Qualitative interviews": ["qualitative"],
    "Meta-analysis": ["meta-analysis"],
}
# Deliberately NOT automated: "Quantitative experimental", "Theoretical / Conceptual",
# "Mixed methods" — all three undercount badly via keyword-substring matching (verified
# empirically 2026-07-20: TOCHI, a journal whose own hand-authored entry describes it as
# routinely mixed-methods, returned 0 literal "mixed methods" hits across 381 works —
# these are methodology LABELS that papers rarely self-tag with, unlike distinctive
# terms like "autoethnography" or "meta-analysis"; see module docstring)

SENSITIVE_KEYWORDS: dict[str, list[str]] = {
    "BDSM / Kink": ["BDSM", "kink"],
    "Drug use": ["drug use", "substance use"],
    "Sex work": ["sex work"],
    "Suicide / Self-harm": ["suicide", "self-harm"],
    "Political extremism": ["political extremism", "radicalization"],
}

MIN_SAMPLE_FOR_FILL = 10       # below this, evidence too thin even for a blank-fill
MIN_SAMPLE_FOR_CORRECTION = 20  # below this, don't second-guess existing content


def normissn(s):
    if not s: return None
    s = re.sub(r"[^0-9Xx]", "", str(s)).upper()
    return s if len(s) == 8 else None


def extract_issn(content: str) -> str | None:
    for pat in [r"\*\*ISSN \(Print\)\*\*\s*\|\s*([0-9]{4}-[0-9]{3}[0-9Xx])",
                r"\*\*ISSN \(Online\)\*\*\s*\|\s*([0-9]{4}-[0-9]{3}[0-9Xx])"]:
        m = re.search(pat, content)
        if m:
            n = normissn(m.group(1))
            if n:
                return f"{n[:4]}-{n[4:]}"
    return None


def collect_target_files() -> list[str]:
    files = []
    for d in TARGET_DIRS:
        files.extend(sorted(glob.glob(os.path.join(JOURNALS_DIR, d, "*.md"))))
    return [f for f in files if not f.endswith("TEMPLATE.md")]


# ---------- OpenAlex fetch + local cache ----------


TRANSIENT_MARKERS = ("429", "too many", "ssl", "eof occurred", "max retries", "timeout", "connection")


def _is_transient(exc: Exception) -> bool:
    return any(m in str(exc).lower() for m in TRANSIENT_MARKERS)


def _retry(fn, attempts=5, base_delay=8):
    """Retry fn() with backoff on transient errors. Returns (result, exc) —
    exactly one of which is None. A non-transient exception re-raises immediately
    (it's a real, permanent failure — no point retrying)."""
    import time as _time
    last_exc = None
    for attempt in range(attempts):
        try:
            return fn(), None
        except Exception as exc:
            if not _is_transient(exc):
                raise
            last_exc = exc
            _time.sleep(base_delay * (attempt + 1))
    return None, last_exc


def fetch_or_cache(issn: str) -> dict | None:
    os.makedirs(CACHE_DIR, exist_ok=True)
    cache_path = os.path.join(CACHE_DIR, f"{normissn(issn)}.json")
    if os.path.exists(cache_path):
        return json.loads(open(cache_path, encoding="utf-8").read())

    all_keywords = [kw for kws in {**METHODOLOGY_KEYWORDS, **SENSITIVE_KEYWORDS}.values() for kw in kws]
    try:
        source, exc = _retry(lambda: resolve_source(issn, None))
    except Exception as exc:
        # Permanent (bad/unknown ISSN, or some other non-transient failure) — safe to
        # cache, no point retrying.
        result = {"error": str(exc)}
        with open(cache_path, "w", encoding="utf-8") as f:
            json.dump(result, f)
        return result
    if source is None:
        # Transient (rate-limited/network) even after retries with backoff — do NOT
        # cache, so a later run retries it.
        return {"error": f"transient source-lookup failure after retries: {exc}", "transient": True}

    from datetime import date as _date, timedelta as _timedelta
    today = _date.today()
    start_date = (today - _timedelta(days=365 * YEARS_WINDOW)).isoformat()
    end_date = today.isoformat()

    try:
        works, exc = _retry(lambda: fetch_works_in_window(source["id"], start_date, end_date))
    except Exception as exc:
        result = {"error": str(exc)}
        with open(cache_path, "w", encoding="utf-8") as f:
            json.dump(result, f)
        return result
    if works is None:
        return {"error": f"transient works-fetch failure after retries: {exc}", "transient": True}

    hits = check_keywords(works, all_keywords)
    result = {
        "total_works": len(works),
        "hits": hits,
        "window_start": start_date,
        "window_end": end_date,
        "years": YEARS_WINDOW,
    }
    with open(cache_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
    return result


def category_hits(scan: dict, keywords: list[str]) -> int:
    return sum(scan["hits"].get(kw, 0) for kw in keywords)


# ---------- Scoring (asymmetric: cap low, never manufacture high) ----------


def score_methodology(hits: int, total_works: int) -> int:
    if hits == 0:
        return 0
    ratio = hits / total_works
    if ratio < 0.005:
        return 1
    if ratio < 0.02:
        return 2
    return 3  # capped — 4-5 never auto-assigned


def score_sensitive(hits: int, total_works: int) -> str:
    if hits == 0:
        return "Low"
    ratio = hits / total_works
    if ratio < 0.02:
        return "Low"
    return "Medium"  # capped — "High" never auto-assigned


def citation_text(hits: int, total_works: int, window_start: str, window_end: str) -> str:
    return (f"{hits} article(s) found (OpenAlex keyword search, {window_start[:4]}-{window_end[:4]}, "
            f"{total_works} total in window) — automated evidence-only estimate, capped conservatively; "
            f"does not confirm higher receptiveness, only rules out near-absence")


# ---------- Table parsing ----------


def find_section(content: str, heading: str) -> tuple[int, int, str] | None:
    """Return (start_idx, end_idx, body) for an H3 section by name."""
    m = re.search(rf"^### {re.escape(heading)}\s*\n", content, re.MULTILINE)
    if not m:
        return None
    start = m.end()
    m2 = re.search(r"^###? ", content[start:], re.MULTILINE)
    end = start + m2.start() if m2 else len(content)
    return start, end, content[start:end]


def parse_table_row(body: str, row_label: str) -> tuple[str, str] | None:
    """Return (score_cell, evidence_cell) for a table row, or None if row not found."""
    m = re.search(rf"^\|\s*{re.escape(row_label)}\s*\|([^|]*)\|([^|]*)\|", body, re.MULTILINE)
    if not m:
        return None
    return m.group(1).strip(), m.group(2).strip()


def is_uncited(evidence_cell: str) -> bool:
    """True if the evidence cell has no checkable citation (no digit, no URL)."""
    if not evidence_cell or evidence_cell in ("", "*(pending)*", "(pending)"):
        return True
    return not re.search(r"\d", evidence_cell) and "http" not in evidence_cell.lower()


# ---------- Main pass ----------


def process_file(path: str) -> dict:
    content = open(path, encoding="utf-8").read()
    name_m = re.search(r"^# +(.+?)\s*$", content, re.MULTILINE)
    name = name_m.group(1).strip() if name_m else os.path.basename(path)

    issn = extract_issn(content)
    if not issn:
        return {"path": path, "name": name, "skip_reason": "no ISSN found"}

    scan = fetch_or_cache(issn)
    if not scan or "error" in scan:
        return {"path": path, "name": name, "issn": issn,
                "skip_reason": f"OpenAlex lookup failed: {scan.get('error') if scan else 'unknown'}"}

    total_works = scan["total_works"]
    actions = []

    is_ai_researched = "AI-researched entry" in content
    is_tier2 = "[!WARNING]" in content
    # CORRECT actions only ever apply to Tier 2 (community-estimate, uncited-by-design)
    # entries — never Tier 1. A Tier 1 entry's prose evidence (e.g. "framed as historical/
    # theoretical review") can describe a specific, plausible, checkable claim without
    # containing a raw digit or URL; is_uncited()'s crude heuristic can't distinguish that
    # from a genuinely empty hand-wave, and keyword-search term/window mismatches are a more
    # likely explanation for a disagreement with hand-curated Tier 1 content than the human
    # being wrong. Verified empirically 2026-07-20: naive thresholds flagged 3 correction
    # candidates on Review of General Psychology (Tier 1) that were real human reasoning,
    # not fabrication — restricting to Tier 2 avoids relitigating gold-standard entries.
    allow_correction = is_tier2
    methodology_section = find_section(content, "Methodological Preferences")
    sensitive_section = find_section(content, "Sensitive Topics")

    for row_label, keywords in METHODOLOGY_KEYWORDS.items():
        hits = category_hits(scan, keywords)
        new_score = score_methodology(hits, total_works)
        new_evidence = citation_text(hits, total_works, scan["window_start"], scan["window_end"])

        if is_ai_researched or methodology_section is None:
            if total_works < MIN_SAMPLE_FOR_FILL:
                continue
            actions.append({"section": "Methodological Preferences", "row": row_label,
                             "action": "FILL_NEW_TABLE", "new_score": new_score, "new_evidence": new_evidence,
                             "hits": hits, "total_works": total_works})
            continue

        existing = parse_table_row(methodology_section[2], row_label)
        if existing is None:
            continue
        existing_score, existing_evidence = existing
        existing_score_num = None
        m = re.match(r"\s*([0-5])\s*", existing_score)
        if m:
            existing_score_num = int(m.group(1))

        if existing_score_num is None or existing_score in ("", "*(pending)*", "(pending)"):
            if total_works < MIN_SAMPLE_FOR_FILL:
                continue
            actions.append({"section": "Methodological Preferences", "row": row_label,
                             "action": "FILL_BLANK", "new_score": new_score, "new_evidence": new_evidence,
                             "hits": hits, "total_works": total_works})
        elif (allow_correction and existing_score_num >= 3 and hits == 0
              and is_uncited(existing_evidence) and total_works >= MIN_SAMPLE_FOR_CORRECTION):
            actions.append({"section": "Methodological Preferences", "row": row_label,
                             "action": "CORRECT", "old_score": existing_score_num, "old_evidence": existing_evidence,
                             "new_score": new_score, "new_evidence": new_evidence,
                             "hits": hits, "total_works": total_works})

    for row_label, keywords in SENSITIVE_KEYWORDS.items():
        hits = category_hits(scan, keywords)
        new_label = score_sensitive(hits, total_works)
        new_evidence = citation_text(hits, total_works, scan["window_start"], scan["window_end"])

        if is_ai_researched or sensitive_section is None:
            if total_works < MIN_SAMPLE_FOR_FILL:
                continue
            actions.append({"section": "Sensitive Topics", "row": row_label,
                             "action": "FILL_NEW_TABLE", "new_score": new_label, "new_evidence": new_evidence,
                             "hits": hits, "total_works": total_works})
            continue

        existing = parse_table_row(sensitive_section[2], row_label)
        if existing is None:
            continue
        existing_label, existing_evidence = existing
        existing_label_norm = existing_label.strip()

        if existing_label_norm in ("", "*(pending)*", "(pending)", "Untested"):
            if total_works < MIN_SAMPLE_FOR_FILL:
                continue
            actions.append({"section": "Sensitive Topics", "row": row_label,
                             "action": "FILL_BLANK", "new_score": new_label, "new_evidence": new_evidence,
                             "hits": hits, "total_works": total_works})
        elif (allow_correction and existing_label_norm in ("Medium", "High") and hits == 0
              and is_uncited(existing_evidence) and total_works >= MIN_SAMPLE_FOR_CORRECTION):
            actions.append({"section": "Sensitive Topics", "row": row_label,
                             "action": "CORRECT", "old_score": existing_label_norm, "old_evidence": existing_evidence,
                             "new_score": new_label, "new_evidence": new_evidence,
                             "hits": hits, "total_works": total_works})

    return {"path": path, "name": name, "issn": issn, "total_works": total_works, "actions": actions}


REPORT_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "references", "_soft_metadata_drafts", "_methodology_evidence_report.json")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="scan (fetch+score) and write the report; does not touch journal files")
    ap.add_argument("--sample", type=int, default=0, help="limit to first N files (0 = all)")
    ap.add_argument("--write", action="store_true", help="apply the EXISTING report (from a prior --dry-run) to journal files — does not re-scan")
    args = ap.parse_args()
    if not args.dry_run and not args.write:
        ap.error("specify --dry-run (scan) or --write (apply existing report)")

    if args.write:
        if not os.path.exists(REPORT_PATH):
            ap.error(f"no report found at {REPORT_PATH} — run --dry-run first")
        with open(REPORT_PATH, encoding="utf-8") as f:
            results = json.load(f)
        apply_results(results)
        return

    files = collect_target_files()
    if args.sample:
        files = files[:args.sample]

    import time as _time
    results = []
    for i, path in enumerate(files, 1):
        r = process_file(path)
        results.append(r)
        n_actions = len(r.get("actions", []))
        print(f"[{i}/{len(files)}] {r['name'][:50]:50s} "
              f"{'SKIP: ' + r['skip_reason'] if 'skip_reason' in r else f'{n_actions} action(s)'}",
              file=sys.stderr)
        _time.sleep(0.5)  # pace requests — avoid re-triggering rate limits (no-op cost on cache hits)

    fills = sum(len([a for a in r.get("actions", []) if a["action"] in ("FILL_BLANK", "FILL_NEW_TABLE")]) for r in results)
    corrections = sum(len([a for a in r.get("actions", []) if a["action"] == "CORRECT"]) for r in results)
    skipped = len([r for r in results if "skip_reason" in r])
    print(f"\n=== Summary: {len(files)} files | {fills} fills | {corrections} corrections | {skipped} skipped ===", file=sys.stderr)

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"Report written to {REPORT_PATH}", file=sys.stderr)


def apply_results(results: list[dict]):
    today = date.today().isoformat()
    applied_files = 0
    for r in results:
        actions = r.get("actions", [])
        if not actions:
            continue
        path = r["path"]
        content = open(path, encoding="utf-8").read()
        content = apply_to_content(content, actions)
        changelog_row = build_changelog_row(actions, today)
        content = insert_changelog_row(content, changelog_row)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        applied_files += 1
    print(f"Applied to {applied_files} files", file=sys.stderr)


def apply_to_content(content: str, actions: list[dict]) -> str:
    by_section: dict[str, list[dict]] = {}
    for a in actions:
        by_section.setdefault(a["section"], []).append(a)

    for section_name, section_actions in by_section.items():
        new_table_actions = [a for a in section_actions if a["action"] == "FILL_NEW_TABLE"]
        if new_table_actions:
            content = build_new_table(content, section_name, section_actions)
        else:
            for a in section_actions:
                content = replace_table_row(content, section_name, a)
    return content


def build_new_table(content: str, section_name: str, section_actions: list[dict]) -> str:
    by_row = {a["row"]: a for a in section_actions}
    if section_name == "Methodological Preferences":
        header = "| Method | Receptiveness (0-5) | Evidence |\n|--------|---------------------|----------|\n"
        rows_order = ["Quantitative experimental", "Qualitative interviews", "Autoethnography",
                      "Theoretical / Conceptual", "Mixed methods", "Meta-analysis"]
        lines = []
        for row in rows_order:
            if row in by_row:
                a = by_row[row]
                lines.append(f"| {row} | {a['new_score']} | {a['new_evidence']} |")
            else:
                lines.append(f"| {row} | *(pending)* | |")
        table = header + "\n".join(lines) + "\n"
        old_pattern = re.compile(r"^### Methodological Preferences\s*\n\n\*\(pending[^\n]*\n", re.MULTILINE)
    else:  # Sensitive Topics
        header = "| Topic Category | Receptiveness | Evidence |\n|----------------|---------------|----------|\n"
        rows_order = ["BDSM / Kink", "Drug use", "Sex work", "Suicide / Self-harm", "Political extremism"]
        lines = []
        for row in rows_order:
            if row in by_row:
                a = by_row[row]
                lines.append(f"| {row} | {a['new_score']} | {a['new_evidence']} |")
            else:
                lines.append(f"| {row} | *(pending)* | |")
        lines.append("| Other: _______ | | |")
        table = header + "\n".join(lines) + "\n"
        old_pattern = re.compile(r"^### Sensitive Topics\s*\n\n\*\(pending[^\n]*\n", re.MULTILINE)

    heading = f"### {section_name}\n\n"
    match = old_pattern.search(content)
    if not match:
        return content  # safety: don't touch if the expected collapsed-pending pattern isn't found verbatim
    return content[:match.start()] + heading + table + content[match.end():]


def replace_table_row(content: str, section_name: str, action: dict) -> str:
    section = find_section(content, section_name)
    if section is None:
        return content
    start, end, body = section
    row_label = action["row"]
    pattern = re.compile(rf"^\|\s*{re.escape(row_label)}\s*\|[^|]*\|[^|]*\|", re.MULTILINE)
    m = pattern.search(body)
    if not m:
        return content
    new_row = f"| {row_label} | {action['new_score']} | {action['new_evidence']} |"
    new_body = body[:m.start()] + new_row + body[m.end():]
    return content[:start] + new_body + content[end:]


def build_changelog_row(actions: list[dict], today: str) -> str:
    fills = [a for a in actions if a["action"] in ("FILL_BLANK", "FILL_NEW_TABLE")]
    corrections = [a for a in actions if a["action"] == "CORRECT"]
    parts = []
    if fills:
        parts.append(f"filled {len(fills)} field(s) with OpenAlex keyword-count evidence ({', '.join(a['row'] for a in fills)})")
    if corrections:
        detail = "; ".join(f"{a['row']} {a['old_score']}->{a['new_score']} (0 articles found, was uncited)" for a in corrections)
        parts.append(f"corrected {len(corrections)} unsupported high score(s): {detail}")
    return (f"| {today} | Methodology/Sensitive-Topics evidence pass: {'; '.join(parts)}. "
            f"Automated, evidence-capped (never assigns 4-5/High from count alone) — see docs/ATLAS_V2_DESIGN.md. "
            f"| @Zaious (AI-assisted) |\n")


def insert_changelog_row(content: str, row: str) -> str:
    marker = "## Changelog"
    if marker not in content:
        return content
    idx = content.rindex(marker)
    after = content[idx:]
    m = re.search(r"\|[-\s|]+\|\n", after)
    if not m:
        return content
    insert_at = idx + m.end()
    return content[:insert_at] + row + content[insert_at:]


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
fix_top_topics_format.py — Convert prose-only "Top Topics" sections to the
standard numeric table, for entries where fit_score._extract_top_topics()
currently finds zero rows (confirmed 57/399 files this way 2026-07-21).

Without a numeric table, fit_score.score_topic_density() silently returns
the neutral default (50.0) for these candidates regardless of how well a
paper's topics actually match — not because there's no evidence, but because
the evidence is in the wrong format for the parser. Affects both real skill
sessions and the web demo's evidence cards.

Scope: journal entries only (need an extractable ISSN). Of the 57, 20 are
conference entries with no ISSN by design (proceedings, not journals — see
their Identity table's "*(N/A — conference proceedings)*") and need a
different fix (CFP topic areas), not this OpenAlex-per-ISSN method — they
are reported as skipped, not silently forced into a shape that doesn't fit.

Reuses import_openalex.py's exact method (Sources().filter(issn=...).get(),
then source["topics"][:10]) rather than topic_trend_scan.py's 5-year-windowed
Works aggregation: the corpus's 342 already-populated files overwhelmingly
(327/342) use this Source-level, all-time-count, 10-row convention with a
plain "Article Count" header (no date range) — matching it keeps these
entries consistent with the rest of the corpus rather than introducing a
second, incompatible convention.

Preserves any existing hand-written prose (e.g. theoretical-framing notes)
below the new table rather than deleting it — often genuine qualitative
context, not just a "go check OpenAlex yourself" placeholder.

Two-phase like enrich_methodology_evidence.py:
    python fix_top_topics_format.py --dry-run [--sample 5]
    python fix_top_topics_format.py --write
"""
from __future__ import annotations
import argparse, json, os, re, sys, glob
from datetime import date

for _s in (sys.stdout, sys.stderr):
    try: _s.reconfigure(encoding="utf-8")
    except Exception: pass

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import fit_score  # noqa: E402 - reuse its exact Top Topics detector, don't reimplement
from enrich_methodology_evidence import extract_issn, _retry  # noqa: E402 - reuse, don't reimplement

try:
    from pyalex import Sources, config
except ImportError:
    print("ERROR: pyalex not installed. Run: pip install pyalex", file=sys.stderr)
    sys.exit(1)

# Set OPENALEX_EMAIL before running for polite-pool access (higher rate limit).
if email := os.environ.get("OPENALEX_EMAIL"):
    config.email = email

SKILL_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
JOURNALS_DIR = os.path.join(SKILL_ROOT, "references", "journals")
CACHE_DIR = os.path.join(os.path.dirname(__file__), "..", ".cache", "top-topics-fix")
TOP_N = 10  # matches the dominant convention: 327/342 already-populated files use 10 rows
REPORT_PATH = os.path.join(SKILL_ROOT, "references", "_soft_metadata_drafts", "_top_topics_fix_report.json")


def collect_affected_files() -> list[str]:
    files = sorted(glob.glob(os.path.join(JOURNALS_DIR, "**", "*.md"), recursive=True))
    affected = []
    for path in files:
        if path.endswith("TEMPLATE.md"):
            continue
        content = open(path, encoding="utf-8").read()
        if not fit_score._extract_top_topics(content):
            affected.append(path)
    return affected


def fetch_or_cache(issn: str) -> dict:
    os.makedirs(CACHE_DIR, exist_ok=True)
    cache_path = os.path.join(CACHE_DIR, f"{issn}.json")
    if os.path.exists(cache_path):
        return json.loads(open(cache_path, encoding="utf-8").read())

    def _fetch():
        results = Sources().filter(issn=issn).get()
        if not results:
            raise ValueError(f"No OpenAlex source found for ISSN {issn}")
        return results[0]

    try:
        source, exc = _retry(_fetch)
    except Exception as exc:
        # Permanent (bad/unknown ISSN) — safe to cache, no point retrying.
        result = {"error": str(exc)}
        with open(cache_path, "w", encoding="utf-8") as f:
            json.dump(result, f)
        return result
    if source is None:
        # Transient (rate-limited/network) even after retries — do NOT cache.
        return {"error": f"transient lookup failure after retries: {exc}", "transient": True}

    topics = source.get("topics") or []
    result = {
        "openalex_id": source.get("id"),
        "works_count": source.get("works_count"),
        "topics": [{"name": t.get("display_name"), "count": t.get("count")} for t in topics[:TOP_N]],
    }
    with open(cache_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
    return result


def process_file(path: str) -> dict:
    content = open(path, encoding="utf-8").read()
    name_m = re.search(r"^# +(.+?)\s*$", content, re.MULTILINE)
    name = name_m.group(1).strip() if name_m else os.path.basename(path)

    issn = extract_issn(content)
    if not issn:
        return {"path": path, "name": name,
                "skip_reason": "no ISSN (likely a conference — needs a different fix, not OpenAlex-per-ISSN)"}

    result = fetch_or_cache(issn)
    if "error" in result:
        return {"path": path, "name": name, "issn": issn,
                "skip_reason": f"OpenAlex lookup failed: {result['error']}"}
    if not result["topics"]:
        return {"path": path, "name": name, "issn": issn,
                "skip_reason": "OpenAlex has no topic data for this source"}

    return {"path": path, "name": name, "issn": issn,
            "topics": result["topics"], "works_count": result.get("works_count")}


# ---------- Apply ----------


def build_table(topics: list[dict]) -> str:
    header = "| Topic | Article Count |\n|-------|--------------|\n"
    rows = "\n".join(f"| {t['name']} | {t['count']} |" for t in topics)
    return header + rows + "\n"


EXISTING_TABLE_PATTERN = re.compile(r"\|[^\n]*\|\n\|[-:\s|]+\|\n(?:\|[^\n]*\|\n?)*")


def replace_top_topics_section(content: str, table: str) -> str:
    """Swap in `table` for the "### Top Topics" section's content.

    Two shapes need different handling, both present in this corpus: some
    entries have NO table at all (hand-written prose only, e.g. "see OpenAlex
    API for full distribution... cultural psychology focus") — that prose is
    kept, with the real table inserted above it. Others already have a table
    shell with placeholder cells (`*(community estimate)*` in every row) —
    that whole placeholder table is replaced, not left duplicated alongside
    the new one.
    """
    heading_match = re.search(r"^### +Top Topics\b[^\n]*\n", content, re.MULTILINE)
    if not heading_match:
        return content  # safety: don't touch if the heading isn't found verbatim
    after_heading = heading_match.end()
    next_heading = re.search(r"^#{2,3} +", content[after_heading:], re.MULTILINE)
    section_end = after_heading + next_heading.start() if next_heading else len(content)
    section_body = content[after_heading:section_end]

    existing_table = EXISTING_TABLE_PATTERN.search(section_body)
    if existing_table:
        new_body = section_body[:existing_table.start()] + table + section_body[existing_table.end():]
    else:
        new_body = "\n" + table + section_body

    return content[:after_heading] + new_body + content[section_end:]


def build_changelog_row(topics_count: int, today: str) -> str:
    return (f"| {today} | Added a numeric Top Topics table ({topics_count} topics, OpenAlex Source "
            f"topic counts) — section previously had no numeric rows, so fit_score.py's topic-density "
            f"scoring defaulted to neutral for this entry regardless of match quality. "
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


def apply_results(results: list[dict]):
    today = date.today().isoformat()
    applied, skipped, noop = 0, 0, 0
    for r in results:
        if "topics" not in r:
            skipped += 1
            continue
        path = r["path"]
        original = open(path, encoding="utf-8").read()
        content = replace_top_topics_section(original, build_table(r["topics"]))
        if content == original:
            noop += 1
            continue
        content = insert_changelog_row(content, build_changelog_row(len(r["topics"]), today))
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        applied += 1
    print(f"Applied to {applied} files ({skipped} skipped, {noop} no-op safety-skip)", file=sys.stderr)


# ---------- CLI ----------


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="scan (fetch) and write the report; does not touch journal files")
    ap.add_argument("--sample", type=int, default=0, help="limit to first N affected files (0 = all)")
    ap.add_argument("--write", action="store_true", help="apply the EXISTING report (from a prior --dry-run) — does not re-scan")
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

    files = collect_affected_files()
    if args.sample:
        files = files[:args.sample]

    import time as _time
    results = []
    for i, path in enumerate(files, 1):
        r = process_file(path)
        results.append(r)
        status = f"SKIP: {r['skip_reason']}" if "skip_reason" in r else f"{len(r['topics'])} topics"
        print(f"[{i}/{len(files)}] {r['name'][:50]:50s} {status}", file=sys.stderr)
        _time.sleep(0.5)  # pace requests — no-op cost on cache hits

    fixable = len([r for r in results if "topics" in r])
    skipped = len([r for r in results if "skip_reason" in r])
    print(f"\n=== {len(files)} files | {fixable} fixable | {skipped} skipped ===", file=sys.stderr)

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"Report written to {REPORT_PATH}", file=sys.stderr)


if __name__ == "__main__":
    main()

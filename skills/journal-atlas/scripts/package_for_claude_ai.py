#!/usr/bin/env python3
"""
package_for_claude_ai.py — Build a claude.ai chat-mode Skill upload zip.

claude.ai's own Skills upload (Settings > Customize > Skills > Upload) is a
different surface than Claude Code's skill loading: it requires a single ZIP
with the skill folder at its root, enforces name<=64 / description<=200 char
limits on the SKILL.md frontmatter (the source SKILL.md's description is
much longer — written for Claude Code's own triggering, which has no such
limit), and its code-execution sandbox only has pre-installed packages
available (no pip install at request time) — so anything depending on
pyalex/requests (scripts/spine/*) can't run there.

This script builds a trimmed copy for that surface: curated references/
journals/ + TEMPLATE.md + the two stdlib-only query tools (fit_score.py,
query_journals.py) + a rewritten SKILL.md with a chat-mode-appropriate
description. Everything under scripts/spine/ (256MB+ journal_spine.db,
OpenAlex fetch cache, pyalex-dependent enrichment scripts) is excluded —
none of it can run in that sandbox anyway, and shipping it would blow past
undocumented but real upload size limits.

Usage:
    python package_for_claude_ai.py [--out-dir DIST_DIR]
"""
from __future__ import annotations
import argparse
import os
import re
import shutil
import sys
import zipfile

SKILL_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
SOURCE_SKILL_DIR = os.path.join(SKILL_ROOT, "journal-atlas")
NAME_MAX = 64
DESCRIPTION_MAX = 200

CHAT_DESCRIPTION = (
    "Academic journal fit assessment. Recommends journals for a paper, "
    "compares journals, and suggests fallback options after rejection. "
    "Covers 399 journals' reviewer culture, framing, and policies."
)

# Relative to SOURCE_SKILL_DIR — everything else under scripts/ is excluded
# (spine/, similar_journals.py, related_papers.py, etc. either need pyalex/
# requests, the git-ignored spine DB, or aren't part of the core chat flow).
INCLUDED_SCRIPTS = ["fit_score.py", "query_journals.py", "validate_structure.py"]

EXCLUDE_DIR_NAMES = {"__pycache__", "spine", "_soft_metadata_drafts"}
EXCLUDE_FILE_SUFFIXES = (".pyc",)


def build_chat_skill_md(source_path: str) -> str:
    content = open(source_path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", content, re.DOTALL)
    if not m:
        raise ValueError(f"{source_path}: couldn't find YAML frontmatter")
    frontmatter, body = m.group(1), m.group(2)

    name_m = re.search(r"^name:\s*(.+)$", frontmatter, re.MULTILINE)
    if not name_m:
        raise ValueError("SKILL.md frontmatter has no 'name:' field")
    name = name_m.group(1).strip()
    if len(name) > NAME_MAX:
        raise ValueError(f"name '{name}' is {len(name)} chars, exceeds claude.ai's {NAME_MAX}-char limit")

    if len(CHAT_DESCRIPTION) > DESCRIPTION_MAX:
        raise ValueError(
            f"CHAT_DESCRIPTION is {len(CHAT_DESCRIPTION)} chars, exceeds claude.ai's "
            f"{DESCRIPTION_MAX}-char limit — edit the constant in this script"
        )

    new_frontmatter = f"name: {name}\ndescription: {CHAT_DESCRIPTION}"
    note = (
        "\n> **Chat-mode package note:** this is a trimmed build for claude.ai's "
        "Skills upload (Settings > Customize > Skills). The spine breadth-query "
        "tooling (`scripts/spine/`) and the full-length skill description are "
        "Claude-Code-only — see the main repo for those. Only `fit_score.py`, "
        "`query_journals.py`, and `validate_structure.py` are included here; "
        "both are pure standard library, since claude.ai's code-execution "
        "sandbox can't `pip install` at request time.\n"
    )
    return f"---\n{new_frontmatter}\n---\n{note}{body}"


def should_skip(path: str) -> bool:
    parts = path.split(os.sep)
    if any(p in EXCLUDE_DIR_NAMES for p in parts):
        return True
    if path.endswith(EXCLUDE_FILE_SUFFIXES):
        return True
    return False


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", default=os.path.join(SKILL_ROOT, "..", "dist"))
    args = ap.parse_args()

    out_dir = os.path.normpath(args.out_dir)
    staging = os.path.join(out_dir, "journal-atlas")
    if os.path.exists(staging):
        shutil.rmtree(staging)
    os.makedirs(staging)

    # SKILL.md — rewritten with the trimmed chat-mode description
    skill_md_out = os.path.join(staging, "SKILL.md")
    with open(skill_md_out, "w", encoding="utf-8") as f:
        f.write(build_chat_skill_md(os.path.join(SOURCE_SKILL_DIR, "SKILL.md")))
    print(f"SKILL.md: name/description within claude.ai limits", file=sys.stderr)

    # TEMPLATE.md + CONSUMPTION_CONTRACT.md — SKILL.md's checklist links to the
    # latter, so it must ship alongside it or that link is dead in this package.
    shutil.copy2(os.path.join(SOURCE_SKILL_DIR, "TEMPLATE.md"), os.path.join(staging, "TEMPLATE.md"))
    shutil.copy2(os.path.join(SOURCE_SKILL_DIR, "CONSUMPTION_CONTRACT.md"), os.path.join(staging, "CONSUMPTION_CONTRACT.md"))

    # scripts/ — only the stdlib-only query tools
    scripts_out = os.path.join(staging, "scripts")
    os.makedirs(scripts_out)
    for name in INCLUDED_SCRIPTS:
        src = os.path.join(SOURCE_SKILL_DIR, "scripts", name)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(scripts_out, name))

    # references/ — the curated knowledge base, minus internal audit-trail dirs
    references_src = os.path.join(SOURCE_SKILL_DIR, "references")
    references_out = os.path.join(staging, "references")
    for root, dirs, files in os.walk(references_src):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIR_NAMES]
        rel = os.path.relpath(root, references_src)
        dest_dir = os.path.join(references_out, rel) if rel != "." else references_out
        os.makedirs(dest_dir, exist_ok=True)
        for fn in files:
            if should_skip(os.path.join(root, fn)):
                continue
            shutil.copy2(os.path.join(root, fn), os.path.join(dest_dir, fn))

    # Zip — must contain the skill folder itself at the root (claude.ai requirement)
    zip_path = os.path.join(out_dir, "journal-atlas-claude-ai-skill.zip")
    if os.path.exists(zip_path):
        os.remove(zip_path)
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, _, files in os.walk(staging):
            for fn in files:
                full = os.path.join(root, fn)
                arcname = os.path.relpath(full, out_dir)  # keeps "journal-atlas/" prefix
                zf.write(full, arcname)

    size_mb = os.path.getsize(zip_path) / (1024 * 1024)
    file_count = sum(len(files) for _, _, files in os.walk(staging))
    print(f"Built {zip_path} ({size_mb:.1f} MB, {file_count} files)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

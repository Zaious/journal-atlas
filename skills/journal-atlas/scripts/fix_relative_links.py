# -*- coding: utf-8 -*-
"""Repair relative links in the corpus that do not resolve.

Entries link back to repository-root files -- SEED_DATA_QUALITY.md,
CONTRIBUTING.md, docs/GOVERNANCE.md -- with a hand-counted number of `../`
steps. The count was wrong almost everywhere: entries at
references/journals/<field>/ used three or four steps where five reach the
root, and the generators that wrote them inherited the error. On GitHub every
one of those is a 404.

This walks every tracked Markdown file, resolves each relative link against
the filesystem, and where it does not resolve, retries the same target at
every plausible depth. A link is rewritten only when exactly one depth
resolves, so an ambiguous case is reported rather than guessed.

    python scripts/fix_relative_links.py --dry-run
    python scripts/fix_relative_links.py
"""
import argparse
import io
import os
import re
import subprocess
import sys

LINK = re.compile(r"\]\((?!https?:|#|mailto:)([^)\s#]+)([^)]*)\)")


def repo_root() -> str:
    out = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                         capture_output=True, text=True)
    if out.returncode != 0:
        sys.exit("not inside a git repository")
    return out.stdout.strip()


def tracked_markdown(root: str) -> list:
    out = subprocess.run(["git", "ls-files", "*.md"], capture_output=True,
                         text=True, cwd=root)
    return out.stdout.split()


def resolve(base: str, target: str, root: str) -> bool:
    """True only if the target exists AND lies inside the repository.

    The boundary check is not pedantry. Without it this script "repaired" a
    link in use-cases/README.md by walking it up out of the repository to a
    file in the maintainer's workspace: resolvable on one laptop, a 404 for
    every reader. A link that works only where it was written is worse than a
    broken one, because nothing reports it.
    """
    p = os.path.abspath(os.path.normpath(os.path.join(root, base, target)))
    if not os.path.exists(p):
        return False
    r = os.path.abspath(root)
    return os.path.commonpath([p, r]) == r


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    root = repo_root()
    fixed = ambiguous = unfixable = 0
    touched, missing = [], []

    # basename -> repo-relative paths, for repairing a link whose depth is
    # right and whose directory is not.
    by_basename = {}
    for rel in tracked_markdown(root):
        by_basename.setdefault(os.path.basename(rel), []).append(rel)

    for rel in tracked_markdown(root):
        path = os.path.join(root, rel)
        base = os.path.dirname(rel)
        try:
            text = io.open(path, encoding="utf-8").read()
        except UnicodeDecodeError:
            continue
        out, changed = [], False
        last = 0
        for m in LINK.finditer(text):
            target = m.group(1)
            if resolve(base, target, root):
                continue
            # GitHub-relative tricks like ../../issues/new are not filesystem
            # paths and must not be touched.
            if re.search(r"(^|/)(issues|pulls|compare|blob|tree)(/|$)", target):
                continue
            stripped = target.lstrip("./")
            while stripped.startswith("../"):
                stripped = stripped[3:]
            candidates = [n for n in range(0, 9)
                          if resolve(base, "../" * n + stripped, root)]
            new = None
            if len(candidates) == 1:
                new = "../" * candidates[0] + stripped
            elif len(candidates) > 1:
                ambiguous += 1
            else:
                # Second strategy: the depth may be right and the directory
                # wrong. Several entries cross-reference a sibling venue under
                # the wrong field -- cognition.md is filed under
                # cognitive-science but linked as psychology/cognition.md.
                # Accept a relocation only when the basename is unique in the
                # corpus, so a name collision is reported rather than guessed.
                hits = by_basename.get(os.path.basename(stripped), [])
                if len(hits) == 1:
                    new = os.path.relpath(hits[0], base).replace(os.sep, "/")
                elif len(hits) > 1:
                    ambiguous += 1
                else:
                    unfixable += 1
                    missing.append("%s -> %s" % (rel, target))
            if new:
                out.append(text[last:m.start(1)])
                out.append(new)
                last = m.end(1)
                changed = True
                fixed += 1
        if changed:
            out.append(text[last:])
            touched.append(rel)
            if not args.dry_run:
                io.open(path, "w", encoding="utf-8", newline="\n").write("".join(out))

    print("files touched : %d" % len(touched))
    print("links fixed   : %d" % fixed)
    print("ambiguous     : %d  (more than one depth resolves; left alone)" % ambiguous)
    print("unresolvable  : %d  (target is not in the repository at all)" % unfixable)
    for m in missing:
        print("     ", m)
    if args.dry_run:
        print("\n(dry run -- nothing written)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

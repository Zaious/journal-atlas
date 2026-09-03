#!/usr/bin/env python3
"""Record which corpus the demo is about to serve.

Run before deploying, like build_topic_vocabulary.py, and for the same reason:
the VPS gets a tarball of the source, not a git checkout, so anything derived
from git has to be derived here and shipped as a file.

Why this exists at all. On 2026-09-03 the deployed demo was found to be serving
a corpus two commits behind the paper: it still carried the conference AI-policy
claims that Section 4 says "have since been withdrawn", and the topic vocabulary
was 42 names short. Nothing was wrong with either the paper or the repository.
What was missing was any way to see, from the outside, which of them the running
service agreed with.

The corpus will keep growing and the paper's numbers will not. A reader who
opens the demo in a year and finds different figures should be able to conclude
"this is a later version" rather than "that paper was wrong", and that is only
possible if the page says which version it is.

version.json is a build artifact and is not committed. It is written by the
deploy's PREDEPLOY step, so it always describes the tree that actually ships and
cannot be forgotten. Committing it would guarantee it was wrong: a file cannot
record the hash of the commit that contains it, so every committed copy would
name its own parent.

What a human writes lives in paper_version.json instead, which is committed and
merged in here. A published paper's tag and DOI change roughly never, and they
must survive a fresh clone.
"""
import io
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "version.json"
PAPER = HERE / "paper_version.json"
REPO = HERE.parents[1]


def git(*args) -> str | None:
    try:
        r = subprocess.run(["git", "-C", str(REPO)] + list(args),
                           capture_output=True, text=True, timeout=15)
    except (OSError, subprocess.SubprocessError):
        return None
    out = (r.stdout or "").strip()
    return out if r.returncode == 0 and out else None


def main() -> int:
    # Whatever a human wrote about the published version, kept in its own
    # committed file so a redeploy cannot drop a DOI and a fresh clone still
    # has one.
    paper = {}
    if PAPER.exists():
        try:
            paper = {k: v for k, v in json.loads(PAPER.read_text(encoding="utf-8")).items()
                     if not k.startswith("_")}
        except ValueError:
            print("error: %s is not valid JSON" % PAPER.name, file=sys.stderr)
            return 1
    else:
        print("warning: %s missing — the page will not name a published version"
              % PAPER.name, file=sys.stderr)

    commit = git("rev-parse", "--short=7", "HEAD")
    if commit is None:
        # A recorded blank beats a stale value: the whole point of this file is
        # that the reader can trust what it says.
        print("error: not a git checkout, or git is unavailable. Refusing to write a\n"
              "       version file that would claim a commit it cannot verify.",
              file=sys.stderr)
        return 1

    dirty = bool(git("status", "--porcelain"))
    data = {
        "corpus_commit": commit,
        "corpus_committed": (git("log", "-1", "--format=%cI") or "")[:10] or None,
        "corpus_describe": git("describe", "--tags", "--always", "--dirty"),
        # True means the tree had uncommitted changes when this was built, so
        # corpus_commit does not fully describe what shipped.
        "built_from_dirty_tree": dirty,
        "built": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "paper": paper,
    }
    io.open(OUT, "w", encoding="utf-8", newline="\n").write(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n")

    print("wrote %s" % OUT.name)
    for k in ("corpus_commit", "corpus_committed", "corpus_describe", "built"):
        print("  %-18s %s" % (k, data[k]))
    if dirty:
        print("  NOTE: tree is dirty — commit before deploying, or the recorded")
        print("        commit will not describe what actually ships.")
    if not data["paper"].get("doi"):
        print("  paper.doi is null — fill it in %s after tagging and archiving." % PAPER.name)
        print("  That file is committed; this one is not, and neither needs a code change.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

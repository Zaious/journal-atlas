"""The counts the documentation states as current must match the corpus.

See sync_counts.py: a current count is wrapped in <!--n:key-->…<!--/n--> and
written by the script. This fails CI when one has gone stale after entries
were added, or when a marker names a count the script does not know.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import sync_counts  # noqa: E402


def test_marked_counts_match_the_corpus():
    problems = sync_counts.sync(check=True)
    assert not problems, "stale counts; run python skills/journal-atlas/scripts/sync_counts.py\n" + "\n".join(problems)


def test_the_documents_actually_carry_markers():
    """A gate with nothing to check passes forever; make sure it has work."""
    marked = sum(
        len(sync_counts.MARKER.findall((sync_counts.REPO / rel).read_text(encoding="utf-8")))
        for rel in sync_counts.DOCUMENTS
    )
    assert marked >= 10, f"only {marked} marked counts across {sync_counts.DOCUMENTS}"

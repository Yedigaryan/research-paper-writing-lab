#!/usr/bin/env python3
"""Check that the orchestrator's record of one evaluation round is on disk.

Usage: check_round_record.py <paper_dir> <round>

Required for round n:
- a "Round n" heading in evaluation-report.md and in reader-findings.md;
- non-empty reports/paper-author-round<n>.md (the author's final message
  for the version evaluated in round n), reports/paper-evaluator-round<n>.md,
  and reports/technician-reader-round<n>.md, each the agent's final message
  saved verbatim.

Exit 0 when all are present; 1 listing whatever is missing.
"""
import re
import sys
from pathlib import Path

AGENTS = ("paper-author", "paper-evaluator", "technician-reader")


def main() -> int:
    if len(sys.argv) != 3 or not sys.argv[2].isdigit():
        print(__doc__, file=sys.stderr)
        return 1
    paper = Path(sys.argv[1])
    n = int(sys.argv[2])
    heading = re.compile(rf"^#+\s*Round\s+{n}\b", re.MULTILINE)
    missing = []

    for name in ("evaluation-report.md", "reader-findings.md"):
        path = paper / name
        if not path.exists():
            missing.append(f"{name} does not exist")
        elif not heading.search(path.read_text(errors="replace")):
            missing.append(f"{name} has no 'Round {n}' heading")

    for agent in AGENTS:
        path = paper / "reports" / f"{agent}-round{n}.md"
        if not path.exists() or not path.read_text(errors="replace").strip():
            missing.append(f"reports/{agent}-round{n}.md is missing or empty")

    for m in missing:
        print(f"error: {m}")
    print(f"round {n} record: {len(missing)} missing")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())

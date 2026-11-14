#!/usr/bin/env python3
"""List the evidence claims that changed since the last evaluated round.

Usage: claims_changed.py <paper_dir> [--record ROUND]

Without --record: compare evidence/evidence.json with the snapshot in
evidence/checked-claims.json and print the ids of claims that are new,
changed, or removed since that snapshot, and how many are unchanged. With no
snapshot every claim counts as new. Always exits 0 unless a file is
unreadable.

With --record ROUND: write the snapshot for that round. The orchestrator
runs this after it has recorded an evaluator round, so that the next
evaluator can leave alone the source checks of claims that did not change.

A claim counts as changed when its text, kind, status, or support (source,
locator, quote) differs, or when the access status of a source it rests on
differs.
"""
import hashlib
import json
import sys
from pathlib import Path

SNAPSHOT = "checked-claims.json"


def digests(evidence: dict) -> dict:
    access = {s.get("id"): s.get("access_status") for s in evidence.get("sources", [])}
    out = {}
    for claim in evidence.get("claims", []):
        support = claim.get("support") or []
        body = {
            "text": claim.get("text"),
            "kind": claim.get("kind"),
            "status": claim.get("status"),
            "support": support,
            "access": sorted(
                (str(s.get("source")), str(access.get(s.get("source"))))
                for s in support if isinstance(s, dict)
            ),
        }
        raw = json.dumps(body, sort_keys=True, ensure_ascii=False)
        out[str(claim.get("id"))] = hashlib.sha256(raw.encode("utf-8")).hexdigest()
    return out


def compare(now: dict, before: dict) -> dict:
    return {
        "new": sorted(i for i in now if i not in before),
        "changed": sorted(i for i in now if i in before and now[i] != before[i]),
        "removed": sorted(i for i in before if i not in now),
        "unchanged": sorted(i for i in now if before.get(i) == now[i]),
    }


def main() -> int:
    args = sys.argv[1:]
    record = None
    if "--record" in args:
        i = args.index("--record")
        try:
            record = int(args[i + 1])
        except (IndexError, ValueError):
            print(__doc__, file=sys.stderr)
            return 1
        del args[i:i + 2]
    if len(args) != 1:
        print(__doc__, file=sys.stderr)
        return 1
    paper = Path(args[0])
    evidence_path = paper / "evidence" / "evidence.json"
    snapshot_path = paper / "evidence" / SNAPSHOT
    try:
        now = digests(json.loads(evidence_path.read_text()))
    except (OSError, ValueError) as exc:
        print(f"error: cannot read {evidence_path}: {exc}")
        return 1

    if record is not None:
        snapshot_path.write_text(
            json.dumps({"round": record, "claims": now}, indent=1, sort_keys=True) + "\n")
        print(f"recorded {len(now)} claims for round {record} in {snapshot_path}")
        return 0

    if not snapshot_path.exists():
        print(f"no snapshot; all {len(now)} claims count as new")
        return 0
    try:
        snap = json.loads(snapshot_path.read_text())
    except (OSError, ValueError) as exc:
        print(f"error: cannot read {snapshot_path}: {exc}")
        return 1
    diff = compare(now, snap.get("claims", {}))
    print(f"compared with the snapshot of round {snap.get('round')}")
    for name in ("new", "changed", "removed"):
        ids = diff[name]
        print(f"{name}: {', '.join(ids) if ids else 'none'}")
    print(f"unchanged: {len(diff['unchanged'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Merge evidence/modules/*.json fragments into evidence/evidence.json.

Usage: merge_evidence.py <paper_dir>

Sources are merged by id; a conflicting title or year for the same id is
an error. Claim ids that collide are prefixed with the module id. The
merged file keeps found_by for provenance. Exit 1 on any conflict.
"""
import json
import sys
from pathlib import Path


def load(path: Path) -> dict:
    with path.open() as fh:
        return json.load(fh)


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        return 1
    paper = Path(sys.argv[1])
    main_path = paper / "evidence" / "evidence.json"
    frag_dir = paper / "evidence" / "modules"
    if not main_path.exists():
        print(f"missing {main_path}", file=sys.stderr)
        return 1

    merged = load(main_path)
    merged.setdefault("sources", [])
    merged.setdefault("claims", [])
    merged.setdefault("contradictions", [])
    sources = {s["id"]: s for s in merged["sources"]}
    claim_ids = {c["id"] for c in merged["claims"]}
    errors = []
    added_sources = added_claims = 0

    for frag_path in sorted(frag_dir.glob("*.json")) if frag_dir.exists() else []:
        module = frag_path.stem
        frag = load(frag_path)
        for src in frag.get("sources", []):
            sid = src.get("id")
            if not sid:
                errors.append(f"{frag_path.name}: source without id")
                continue
            src.setdefault("found_by", f"module:{module}")
            if sid in sources:
                old = sources[sid]
                if old.get("title") != src.get("title") or old.get("year") != src.get("year"):
                    errors.append(
                        f"{frag_path.name}: source {sid} conflicts with existing "
                        f"({old.get('title')!r}, {old.get('year')}) vs "
                        f"({src.get('title')!r}, {src.get('year')})")
                continue
            sources[sid] = src
            added_sources += 1
        for claim in frag.get("claims", []):
            cid = claim.get("id")
            if not cid:
                errors.append(f"{frag_path.name}: claim without id")
                continue
            claim.setdefault("module", module)
            if cid in claim_ids:
                cid = f"{module}-{cid}"
                claim["id"] = cid
            claim_ids.add(cid)
            merged["claims"].append(claim)
            added_claims += 1
        merged["contradictions"].extend(frag.get("contradictions", []))

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    merged["sources"] = list(sources.values())
    with main_path.open("w") as fh:
        json.dump(merged, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    print(f"merged: +{added_sources} sources, +{added_claims} claims; "
          f"total {len(merged['sources'])} sources, {len(merged['claims'])} claims")
    return 0


if __name__ == "__main__":
    sys.exit(main())

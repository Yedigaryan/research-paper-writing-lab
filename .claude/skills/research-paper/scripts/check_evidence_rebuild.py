#!/usr/bin/env python3
"""Check that evidence/evidence.json is exactly the rebuild of its parts.

Usage: check_evidence_rebuild.py <paper_dir> [--init-base]

The merged file must equal evidence/evidence.base.json plus every
evidence/modules/*.json fragment, merged the way merge_evidence.py merges
them. Order of sources, claims, and contradictions is ignored. A difference
means the merged file was edited by hand or was not rebuilt after a change
to the base file or a fragment. Each difference names the record and the
file that owns it, which is where the change belongs.

--init-base: when evidence/evidence.base.json is missing, derive it once
from evidence.json by removing every source, claim, and contradiction that
a fragment contributes, write it, then run the check. It never overwrites
an existing base file.

Exit 0 when the rebuild matches; 1 on any difference, a missing base file,
or unreadable JSON. Nothing is written except by --init-base.
"""
import copy
import json
import sys
from collections import Counter
from pathlib import Path

BASE_REL = "evidence/evidence.base.json"


def load(path: Path):
    with path.open() as fh:
        return json.load(fh)


def key(obj) -> str:
    return json.dumps(obj, sort_keys=True, ensure_ascii=False)


def fragments(paper: Path) -> list:
    frag_dir = paper / "evidence" / "modules"
    if not frag_dir.exists():
        return []
    return [(p, load(p)) for p in sorted(frag_dir.glob("*.json"))]


def rebuild(base: dict, frags: list):
    """Repeat merge_evidence.py in memory. Return (merged, owner, errors)."""
    merged = copy.deepcopy(base)
    merged.setdefault("sources", [])
    merged.setdefault("claims", [])
    merged.setdefault("contradictions", [])
    owner = {}
    for s in merged["sources"]:
        owner[("source", s.get("id"))] = BASE_REL
    for c in merged["claims"]:
        owner[("claim", c.get("id"))] = BASE_REL
    sources = {s.get("id"): s for s in merged["sources"]}
    claim_ids = {c.get("id") for c in merged["claims"]}
    errors = []
    for path, frag in frags:
        frag = copy.deepcopy(frag)
        module = path.stem
        rel = f"evidence/modules/{path.name}"
        for src in frag.get("sources", []):
            sid = src.get("id")
            if not sid:
                errors.append(f"{rel}: source without id")
                continue
            src.setdefault("found_by", f"module:{module}")
            if sid in sources:
                old = sources[sid]
                if old.get("title") != src.get("title") or old.get("year") != src.get("year"):
                    errors.append(f"{rel}: source {sid} conflicts with an earlier "
                                  f"record on title or year")
                continue
            sources[sid] = src
            owner[("source", sid)] = rel
        for claim in frag.get("claims", []):
            cid = claim.get("id")
            if not cid:
                errors.append(f"{rel}: claim without id")
                continue
            claim.setdefault("module", module)
            if cid in claim_ids:
                cid = f"{module}-{cid}"
                claim["id"] = cid
            claim_ids.add(cid)
            merged["claims"].append(claim)
            owner[("claim", cid)] = rel
        merged["contradictions"].extend(frag.get("contradictions", []))
    merged["sources"] = list(sources.values())
    return merged, owner, errors


def derive_base(merged: dict, frags: list) -> dict:
    """Remove from the merged file everything a fragment contributes."""
    claim_ids = {c.get("id") for c in merged.get("claims", [])}
    drop_claims = set()
    drop_sources = set()
    drop_contra = Counter()
    for path, frag in frags:
        module = path.stem
        for c in frag.get("claims", []):
            cid = c.get("id")
            if not cid:
                continue
            prefixed = f"{module}-{cid}"
            drop_claims.add(prefixed if prefixed in claim_ids else cid)
        for s in frag.get("sources", []):
            drop_sources.add((s.get("id"), s.get("found_by", f"module:{module}")))
        for x in frag.get("contradictions", []):
            drop_contra[key(x)] += 1
    base = {k: v for k, v in merged.items()
            if k not in ("sources", "claims", "contradictions")}
    base["sources"] = [s for s in merged.get("sources", [])
                       if (s.get("id"), s.get("found_by")) not in drop_sources]
    base["claims"] = [c for c in merged.get("claims", [])
                      if c.get("id") not in drop_claims]
    contra = []
    for x in merged.get("contradictions", []):
        k = key(x)
        if drop_contra[k] > 0:
            drop_contra[k] -= 1
        else:
            contra.append(x)
    base["contradictions"] = contra
    return base


def compare(actual: dict, rebuilt: dict, owner: dict) -> list:
    diffs = []
    if actual.get("question") != rebuilt.get("question"):
        diffs.append(f"question in evidence.json differs from {BASE_REL}")
    for kind, field in (("source", "sources"), ("claim", "claims")):
        a = {x.get("id"): x for x in actual.get(field, [])}
        r = {x.get("id"): x for x in rebuilt.get(field, [])}
        for xid in sorted(set(a) | set(r), key=str):
            where = owner.get((kind, xid), "?")
            if xid not in r:
                diffs.append(f"{kind} {xid} is in evidence.json but in no base or "
                             f"fragment file; add it to the file that should own it "
                             f"(new author claims go to evidence/modules/author.json)")
            elif xid not in a:
                diffs.append(f"{kind} {xid} from {where} is missing from "
                             f"evidence.json; rebuild the merged file")
            elif a[xid] != r[xid]:
                fields = sorted(k for k in set(a[xid]) | set(r[xid])
                                if a[xid].get(k) != r[xid].get(k))
                diffs.append(f"{kind} {xid} differs in {', '.join(fields)}; put the "
                             f"intended version in {where} and rebuild")
    ac = Counter(key(x) for x in actual.get("contradictions", []))
    rc = Counter(key(x) for x in rebuilt.get("contradictions", []))
    only_a = sum((ac - rc).values())
    only_r = sum((rc - ac).values())
    if only_a or only_r:
        diffs.append(f"contradictions differ: {only_a} only in evidence.json, "
                     f"{only_r} only in the rebuild")
    return diffs


def main() -> int:
    args = sys.argv[1:]
    init = "--init-base" in args
    args = [a for a in args if a != "--init-base"]
    if len(args) != 1:
        print(__doc__, file=sys.stderr)
        return 1
    paper = Path(args[0])
    ev_path = paper / "evidence" / "evidence.json"
    base_path = paper / BASE_REL
    if not ev_path.exists():
        print(f"error: {ev_path} not found")
        return 1
    try:
        actual = load(ev_path)
        frags = fragments(paper)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"error: cannot read evidence JSON: {exc}")
        return 1

    if init:
        if base_path.exists():
            print(f"error: {base_path} exists; --init-base never overwrites it")
            return 1
        derived = derive_base(actual, frags)
        with base_path.open("w") as fh:
            json.dump(derived, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        print(f"wrote {base_path}: {len(derived['sources'])} sources, "
              f"{len(derived['claims'])} claims, "
              f"{len(derived['contradictions'])} contradictions")

    if not base_path.exists():
        print(f"error: {base_path} missing, so the merged file cannot be rebuilt. "
              f"Run this script once with --init-base, then make every later "
              f"change in the base file or a fragment.")
        return 1
    try:
        base = load(base_path)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"error: cannot read {base_path}: {exc}")
        return 1

    rebuilt, owner, errors = rebuild(base, frags)
    diffs = errors + compare(actual, rebuilt, owner)
    for d in diffs:
        print(f"error: {d}")
    print(f"rebuild from base plus {len(frags)} fragments: {len(diffs)} differences")
    if diffs:
        print(f"to rebuild: cp {base_path} {ev_path} && python3 "
              f".claude/skills/research-paper/scripts/merge_evidence.py {paper}")
    return 1 if diffs else 0


if __name__ == "__main__":
    sys.exit(main())

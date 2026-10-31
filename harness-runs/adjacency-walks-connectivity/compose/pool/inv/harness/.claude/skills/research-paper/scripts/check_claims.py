#!/usr/bin/env python3
"""Validate evidence/evidence.json against references/evidence-schema.md.

Usage: check_claims.py <paper_dir>

Errors (exit 1): missing required fields, bad enum values, a source with no
identifier, a fact or experimental claim marked supported without a
located support entry, a derived claim without a derivation, a support
entry pointing at an unknown source, a supported claim resting only on an
unavailable source. Warnings are printed but do not fail.
"""
import json
import sys
from pathlib import Path

SOURCE_TYPES = {"peer-reviewed", "book", "official-doc", "standard", "dataset",
                "preprint", "web", "local-file", "code"}
ACCESS = {"full", "partial", "abstract-only", "metadata-only", "unavailable"}
CRED = {"primary", "secondary", "tertiary"}
KINDS = {"fact", "derived", "experimental", "interpretation", "hypothesis",
         "estimate", "open-question"}
STATUS = {"supported", "qualified", "unverified", "removed"}
CONF = {"high", "medium", "low"}
WEAK_ACCESS = {"metadata-only", "unavailable"}


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        return 1
    path = Path(sys.argv[1]) / "evidence" / "evidence.json"
    if not path.exists():
        print(f"missing {path}", file=sys.stderr)
        return 1
    with path.open() as fh:
        ev = json.load(fh)

    errors, warnings = [], []
    sources = {}
    for i, s in enumerate(ev.get("sources", [])):
        tag = f"source[{i}] {s.get('id', '?')}"
        for field in ("id", "type", "title", "access_status", "credibility"):
            if not s.get(field):
                errors.append(f"{tag}: missing {field}")
        if s.get("type") not in SOURCE_TYPES:
            errors.append(f"{tag}: bad type {s.get('type')!r}")
        if s.get("access_status") not in ACCESS:
            errors.append(f"{tag}: bad access_status {s.get('access_status')!r}")
        if s.get("credibility") not in CRED:
            errors.append(f"{tag}: bad credibility {s.get('credibility')!r}")
        ident = s.get("identifier") or {}
        if not any(ident.get(k) for k in ("doi", "url", "isbn", "path")):
            errors.append(f"{tag}: no identifier (doi, url, isbn, or path)")
        if s.get("type") == "local-file" and not ident.get("path"):
            errors.append(f"{tag}: local-file source needs identifier.path")
        if not s.get("accessed"):
            warnings.append(f"{tag}: no accessed date")
        if s.get("id") in sources:
            errors.append(f"{tag}: duplicate source id")
        sources[s.get("id")] = s

    counts = {k: 0 for k in STATUS}
    for i, c in enumerate(ev.get("claims", [])):
        tag = f"claim[{i}] {c.get('id', '?')}"
        for field in ("id", "text", "kind", "status"):
            if not c.get(field):
                errors.append(f"{tag}: missing {field}")
        kind, status = c.get("kind"), c.get("status")
        if kind not in KINDS:
            errors.append(f"{tag}: bad kind {kind!r}")
        if status not in STATUS:
            errors.append(f"{tag}: bad status {status!r}")
        else:
            counts[status] += 1
        if c.get("confidence") not in CONF:
            warnings.append(f"{tag}: confidence not one of {sorted(CONF)}")
        support = c.get("support") or []
        located = []
        for s in support:
            src = s.get("source")
            if src not in sources:
                errors.append(f"{tag}: support references unknown source {src!r}")
                continue
            if not s.get("locator"):
                errors.append(f"{tag}: support from {src} has no locator")
                continue
            located.append(src)
            if sources[src].get("access_status") in WEAK_ACCESS and status == "supported":
                errors.append(f"{tag}: marked supported but source {src} is "
                              f"{sources[src].get('access_status')}; use qualified")
            if not s.get("quote") and sources[src].get("access_status") in {"full", "partial"}:
                warnings.append(f"{tag}: support from {src} has no quote")
        if status == "supported":
            if kind in {"fact", "experimental"} and not located:
                errors.append(f"{tag}: {kind} claim marked supported without located support")
            if kind == "derived" and not c.get("derivation"):
                errors.append(f"{tag}: derived claim without derivation")
            if kind in {"interpretation", "hypothesis", "estimate"} and not located:
                errors.append(f"{tag}: {kind} claim has no support for its premises")
        if status == "unverified" and not c.get("used_in"):
            warnings.append(f"{tag}: unverified claim; confirm it is qualified where used")

    for i, x in enumerate(ev.get("contradictions", [])):
        if not x.get("resolution"):
            warnings.append(f"contradiction[{i}]: no resolution recorded")

    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}")
    print(f"sources {len(sources)}; claims " +
          ", ".join(f"{k} {v}" for k, v in counts.items()) +
          f"; errors {len(errors)}; warnings {len(warnings)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

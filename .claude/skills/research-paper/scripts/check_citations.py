#!/usr/bin/env python3
"""Cross-check \\cite keys in the LaTeX source, references.bib, and evidence.json.

Usage: check_citations.py <paper_dir>

Errors (exit 1): a cited key missing from references.bib; a cited key with
no source in evidence.json; a bib entry whose key is not an evidence
source; a bib entry without title; a bib entry without year or date,
unless it is an evidence source whose own year is null (an undated source
correctly has no year or date field); a year or date that is not a year
(such as "n.d."); a web entry without url.

Warnings: unused bib entries; evidence sources never cited while a claim
that is not removed still rests on them. A source never cited whose claims
are all removed, or that supports no claim, is printed as a note only.
"""
import re
import sys
from pathlib import Path
import json

CITE_RE = re.compile(r"\\(?:cite|parencite|textcite|autocite|footcite|citep|citet|nocite)\*?"
                     r"(?:\[[^\]]*\]){0,2}\{([^}]*)\}")
ENTRY_RE = re.compile(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", re.MULTILINE)


def tex_files(paper: Path):
    for pattern in ("*.tex", "sections/*.tex", "appendices/*.tex"):
        yield from sorted(paper.glob(pattern))


def parse_bib(text: str) -> dict:
    entries = {}
    for m in ENTRY_RE.finditer(text):
        etype, key = m.group(1).lower(), m.group(2)
        start = m.end()
        depth, i = 1, start
        while i < len(text) and depth:
            depth += {"{": 1, "}": -1}.get(text[i], 0)
            i += 1
        body = text[start:i - 1]
        fields = {}
        for fm in re.finditer(r"(\w+)\s*=\s*(\{(?:[^{}]|\{[^{}]*\})*\}|\"[^\"]*\"|[^,\n]+)", body):
            fields[fm.group(1).lower()] = fm.group(2).strip().strip("{}\"").strip()
        entries[key] = (etype, fields)
    return entries


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        return 1
    paper = Path(sys.argv[1])
    errors, warnings = [], []

    cited = {}
    for f in tex_files(paper):
        for m in CITE_RE.finditer(f.read_text(errors="replace")):
            for key in m.group(1).split(","):
                key = key.strip()
                if key:
                    cited.setdefault(key, set()).add(f.relative_to(paper).as_posix())

    bib_path = paper / "references.bib"
    bib = parse_bib(bib_path.read_text(errors="replace")) if bib_path.exists() else {}
    if not bib_path.exists():
        errors.append("references.bib missing")

    ev_path = paper / "evidence" / "evidence.json"
    ev, claims = {}, []
    if ev_path.exists():
        with ev_path.open() as fh:
            data = json.load(fh)
        ev = {s.get("id"): s for s in data.get("sources", [])}
        claims = data.get("claims", [])
    else:
        errors.append("evidence/evidence.json missing")
    ev_sources = set(ev)

    live = {}
    for c in claims:
        if c.get("status") == "removed":
            continue
        for s in c.get("support") or []:
            live.setdefault(s.get("source"), []).append(str(c.get("id", "?")))

    for key, files in sorted(cited.items()):
        where = ", ".join(sorted(files))
        if key not in bib:
            errors.append(f"cited key {key} not in references.bib ({where})")
        if ev_sources and key not in ev_sources:
            errors.append(f"cited key {key} has no source in evidence.json ({where})")

    for key, (etype, fields) in sorted(bib.items()):
        if key not in cited:
            warnings.append(f"bib entry {key} is never cited")
        if ev_sources and key not in ev_sources:
            errors.append(f"bib entry {key} is not an evidence source")
        if not fields.get("title"):
            errors.append(f"bib entry {key} has no title")
        year, date = fields.get("year", ""), fields.get("date", "")
        for name, value in (("year", year), ("date", date)):
            if value and not re.match(r"\d{4}", value):
                errors.append(f"bib entry {key} has {name} {value!r}, which is not a year; "
                              f"for an undated source leave year and date out")
        undated_source = key in ev and not ev[key].get("year")
        if not (year or date) and not undated_source:
            errors.append(f"bib entry {key} has no year")
        if etype in {"online", "misc"} and not (fields.get("url") or fields.get("howpublished")
                                                or fields.get("doi")):
            errors.append(f"bib entry {key} ({etype}) has no url, doi, or howpublished")
        if fields.get("url") and not (fields.get("urldate") or fields.get("note")):
            warnings.append(f"bib entry {key} has url but no urldate")

    notes = []
    for sid in sorted(ev_sources - set(cited), key=str):
        if live.get(sid):
            warnings.append(
                f"evidence source {sid} is never cited, but claims rest on it: "
                f"{', '.join(live[sid])}. Cite it where those claims are used, drop its "
                f"support entry where another source carries the claim, or set the claim "
                f"to status removed with the reason, in the evidence file that owns it, "
                f"then rebuild")
        else:
            notes.append(f"evidence source {sid} is not cited and supports no live claim")

    for n in notes:
        print(f"note: {n}")
    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}")
    print(f"cited keys {len(cited)}; bib entries {len(bib)}; evidence sources "
          f"{len(ev_sources)}; errors {len(errors)}; warnings {len(warnings)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

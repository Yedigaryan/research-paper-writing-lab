#!/usr/bin/env python3
"""Cross-check \\cite keys in the LaTeX source, references.bib, and evidence.json.

Usage: check_citations.py <paper_dir>

Errors (exit 1): a cited key missing from references.bib; a cited key with
no source in evidence.json; a bib entry whose key is not an evidence
source; a bib entry without title or year; a web entry without url. Unused
bib entries and evidence sources never cited are warnings.
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
    ev_sources = set()
    if ev_path.exists():
        with ev_path.open() as fh:
            ev_sources = {s.get("id") for s in json.load(fh).get("sources", [])}
    else:
        errors.append("evidence/evidence.json missing")

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
        if not (fields.get("year") or fields.get("date")):
            errors.append(f"bib entry {key} has no year or date")
        if etype in {"online", "misc"} and not (fields.get("url") or fields.get("howpublished")
                                                or fields.get("doi")):
            errors.append(f"bib entry {key} ({etype}) has no url, doi, or howpublished")
        if fields.get("url") and not (fields.get("urldate") or fields.get("note")):
            warnings.append(f"bib entry {key} has url but no urldate")

    for sid in sorted(ev_sources - set(cited)):
        warnings.append(f"evidence source {sid} is never cited in the paper")

    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}")
    print(f"cited keys {len(cited)}; bib entries {len(bib)}; evidence sources "
          f"{len(ev_sources)}; errors {len(errors)}; warnings {len(warnings)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Inspect papers/<slug>/main.pdf for layout and resolution problems.

Usage: inspect_pdf.py <paper_dir>

Errors (exit 1): PDF missing or unreadable, unresolved references (??),
unresolved citations ([?] or [0]), empty pages, "To be written"
placeholders left in the text. Warnings: overfull boxes in the build log,
pages with very little text, missing figure files referenced in the log.
"""
import re
import subprocess
import sys
from pathlib import Path


def page_texts(pdf: Path) -> list:
    try:
        from pypdf import PdfReader
        return [(p.extract_text() or "") for p in PdfReader(str(pdf)).pages]
    except Exception:
        out = subprocess.run(["pdftotext", "-layout", str(pdf), "-"],
                             capture_output=True, text=True, check=True).stdout
        return out.split("\f")


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        return 1
    paper = Path(sys.argv[1])
    pdf = paper / "main.pdf"
    errors, warnings = [], []
    if not pdf.exists():
        print(f"error: {pdf} not found; run build.sh first")
        return 1
    try:
        pages = page_texts(pdf)
    except Exception as exc:
        print(f"error: cannot read {pdf}: {exc}")
        return 1

    for n, text in enumerate(pages, 1):
        stripped = text.strip()
        if not stripped:
            errors.append(f"page {n} is empty")
        elif len(stripped) < 80 and n != len(pages):
            warnings.append(f"page {n} has very little text ({len(stripped)} chars)")
        if "??" in text:
            errors.append(f"page {n}: unresolved reference '??'")
        if re.search(r"\[\?\]|\[0\]", text):
            errors.append(f"page {n}: unresolved citation")
        if "To be written" in text:
            errors.append(f"page {n}: placeholder text 'To be written'")

    log = paper / "build" / "main.log"
    if log.exists():
        logtext = log.read_text(errors="replace")
        over = len(re.findall(r"^Overfull", logtext, re.MULTILINE))
        if over:
            warnings.append(f"{over} overfull boxes in build log")
        for m in re.finditer(r"File `([^']+)' not found", logtext):
            errors.append(f"missing file {m.group(1)} per build log")
        if "Package biblatex Warning: Please (re)run Biber" in logtext:
            errors.append("bibliography not resolved; biber did not run")
    else:
        warnings.append("no build log found; log checks skipped")

    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}")
    print(f"pages {len(pages)}; errors {len(errors)}; warnings {len(warnings)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

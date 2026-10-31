#!/usr/bin/env python3
"""Check that self-evaluation.md is organised section by section.

Usage: check_self_evaluation.py <paper_dir>

Every file under sections/ that main.tex inputs must have its own heading
in self-evaluation.md: a line starting with '#' that contains the file's
path (for example "## sections/background.tex: Background"), followed by
at least one non-blank line before the next heading. Appendix files that
main.tex inputs are reported as warnings when they have no such heading. A
per-finding revision log may follow the section part; it never replaces it.

Exit 0 when every section file has a heading with text under it; 1
otherwise, listing the files that lack one.
"""
import re
import sys
from pathlib import Path

INPUT_RE = re.compile(r"\\(?:input|include)\s*\{([^}]+)\}")


def inputs(main_tex: Path) -> list:
    found = []
    for line in main_tex.read_text(errors="replace").splitlines():
        line = re.sub(r"(?<!\\)%.*", "", line)
        for m in INPUT_RE.finditer(line):
            name = m.group(1).strip()
            if name.endswith(".tex"):
                name = name[:-4]
            found.append(name)
    return found


def blocks(text: str) -> list:
    """Return [heading, has_text] for every heading outside code fences."""
    result = []
    current = None
    fenced = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            fenced = not fenced
            if current is not None:
                current[1] = True
            continue
        if not fenced and line.lstrip().startswith("#"):
            current = [line, False]
            result.append(current)
        elif current is not None and line.strip():
            current[1] = True
    return result


def covered(name: str, heads: list) -> str:
    pattern = re.compile(re.escape(name) + r"(\.tex)?(?![\w-])")
    matches = [b for b in heads if pattern.search(b[0])]
    if not matches:
        return "no heading"
    if not any(b[1] for b in matches):
        return "heading with no text under it"
    return ""


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        return 1
    paper = Path(sys.argv[1])
    main_tex = paper / "main.tex"
    selfev = paper / "self-evaluation.md"
    if not main_tex.exists():
        print(f"error: {main_tex} not found")
        return 1
    if not selfev.exists():
        print(f"error: {selfev} not found")
        return 1

    heads = blocks(selfev.read_text(errors="replace"))
    errors, warnings = [], []
    names = inputs(main_tex)
    for name in names:
        problem = covered(name, heads)
        if not problem:
            continue
        if name.startswith("sections/"):
            errors.append(f"{name}.tex: {problem} in self-evaluation.md")
        elif name.startswith("appendices/"):
            warnings.append(f"{name}.tex: {problem} in self-evaluation.md")

    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}")
    print(f"inputs {len(names)}; errors {len(errors)}; warnings {len(warnings)}")
    if errors:
        print("each section file needs a heading such as "
              "'## sections/<file>.tex: <title>' with its purpose, claims and "
              "support, and conclusions under it")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

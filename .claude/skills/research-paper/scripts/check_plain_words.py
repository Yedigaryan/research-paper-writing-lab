#!/usr/bin/env python3
"""Check the plain-words layer of a paper whose brief says Analogies: yes.

Usage: check_plain_words.py <paper_dir> [--max-words N] [--terms w1,w2,...]
                            [--marker NAME] [--envs env1,env2,...]

A plain-words paragraph starts at the literal text "In plain words" or at a
macro whose one-line definition contains that text (for example \\plain),
and runs to the next blank line, \\begin, \\end, or sectioning command.
Use --marker NAME when the paper's macro is defined over several lines.

Errors (exit 1): no plain-words paragraph found in the paper; a statement
environment (default: definition, theorem, lemma, proposition, corollary)
with no plain-words paragraph since the previous statement environment
began. Worked examples are not checked; check those by reading.

Warnings (exit 0): a sentence longer than --max-words words (default 20);
math notation inside a plain-words paragraph; a word from --terms (the
technical terms the story dictionary replaces) inside a plain-words
paragraph, plural forms included.
"""
import argparse
import re
import sys
from pathlib import Path

LITERAL = "In plain words"
DEFAULT_ENVS = "definition,theorem,lemma,proposition,corollary"
ABBREV_RE = re.compile(r"\b(?:e\.g|i\.e|etc|cf|pp|p|Fig|Sec|No|vs)\.")
END_RE = re.compile(r"\n[ \t]*\n|\\begin\{|\\end\{|\\(?:sub)*section\*?\{|\\paragraph\{|\\chapter\*?\{")
DEF_RE = re.compile(r"\\(?:re)?newcommand\*?\s*\{?\\([A-Za-z]+)\}?|\\def\s*\\([A-Za-z]+)")
REF_RE = re.compile(r"\\(?:cite|parencite|textcite|autocite|cref|Cref|ref|eqref|pageref|label)\*?"
                    r"(?:\[[^\]]*\]){0,2}\{[^}]*\}")
MATH_RE = re.compile(r"\$\$.*?\$\$|\$[^$]*\$|\\\(.*?\\\)|\\\[.*?\\\]", re.S)


def tex_files(paper: Path) -> list:
    files = []
    for pattern in ("main.tex", "sections/*.tex", "appendices/*.tex"):
        files.extend(sorted(paper.glob(pattern)))
    return files


def strip_comments(text: str) -> str:
    """Remove % comments; keep newlines so line numbers stay correct."""
    return re.sub(r"(?<!\\)%[^\n]*", "", text)


def line_of(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def line_at(text: str, pos: int) -> str:
    start = text.rfind("\n", 0, pos) + 1
    end = text.find("\n", pos)
    return text[start:end if end != -1 else len(text)]


def is_definition_line(line: str) -> bool:
    return "newcommand" in line or "\\def" in line


def find_macros(texts: dict) -> set:
    names = set()
    for text in texts.values():
        for line in text.splitlines():
            if LITERAL in line and is_definition_line(line):
                m = DEF_RE.search(line)
                if m:
                    names.add(m.group(1) or m.group(2))
    return names


def clean(par: str):
    """Return the paragraph as plain text and whether it holds math."""
    notation = bool(MATH_RE.search(par))
    s = REF_RE.sub(" ", par)
    s = MATH_RE.sub(" X ", s)
    s = re.sub(r"\\\\", " ", s)
    s = re.sub(r"\\[A-Za-z]+\*?", " ", s)
    s = s.replace("~", " ").replace("{", "").replace("}", "").replace("\\", " ")
    s = s.replace("``", '"').replace("''", '"')
    s = re.sub(r"\s+", " ", s).strip()
    return s.lstrip(".:; ").strip(), notation


def sentences(s: str) -> list:
    protected = ABBREV_RE.sub(lambda m: m.group(0).replace(".", "\x00"), s)
    parts = re.split(r"(?<=[.!?])\s+(?=[\"'(A-Z0-9])", protected)
    return [p.replace("\x00", ".").strip() for p in parts if p.strip()]


def word_count(sentence: str) -> int:
    return len(re.findall(r"[A-Za-z0-9]+(?:['-][A-Za-z0-9]+)*", sentence))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("paper")
    ap.add_argument("--max-words", type=int, default=20)
    ap.add_argument("--terms", default="")
    ap.add_argument("--marker", action="append", default=[])
    ap.add_argument("--envs", default=DEFAULT_ENVS)
    args = ap.parse_args()

    paper = Path(args.paper)
    if not (paper / "main.tex").exists():
        print(f"error: {paper}/main.tex not found")
        return 1

    texts = {f: strip_comments(f.read_text(errors="replace")) for f in tex_files(paper)}
    macros = find_macros(texts) | {m.lstrip("\\") for m in args.marker if m.strip()}
    envs = [e.strip() for e in args.envs.split(",") if e.strip()]
    terms = [t.strip() for t in args.terms.split(",") if t.strip()]
    term_res = [(t, re.compile(r"(?<![A-Za-z])" + re.escape(t) + r"(?:s|es)?(?![A-Za-z])", re.I))
                for t in terms]
    env_re = re.compile(r"\\begin\{(" + "|".join(map(re.escape, envs)) + r")\*?\}") if envs else None
    mac_re = (re.compile(r"\\(" + "|".join(map(re.escape, sorted(macros))) + r")(?![A-Za-z])")
              if macros else None)

    errors, warnings = [], []
    n_par = n_env = 0
    for f, text in texts.items():
        rel = f.relative_to(paper).as_posix()
        events = []
        starts = []
        if mac_re:
            starts += [(m.start(), m.end()) for m in mac_re.finditer(text)]
        starts += [(m.start(), m.end()) for m in re.finditer(re.escape(LITERAL), text)]
        seen = set()
        for start, end in sorted(starts):
            if is_definition_line(line_at(text, start)):
                continue
            if any(abs(start - s) < 40 for s in seen):
                continue
            seen.add(start)
            events.append((start, "plain", end))
        if env_re:
            events += [(m.start(), "env", m.group(1)) for m in env_re.finditer(text)]
        events.sort(key=lambda e: e[0])

        has_plain = False
        for pos, kind, payload in events:
            line = line_of(text, pos)
            if kind == "plain":
                has_plain = True
                n_par += 1
                stop = END_RE.search(text, payload)
                body, notation = clean(text[payload:stop.start() if stop else len(text)])
                if notation:
                    warnings.append(f"{rel}:{line}: notation inside a plain-words paragraph")
                for t, rx in term_res:
                    if rx.search(body):
                        warnings.append(f"{rel}:{line}: technical term '{t}' inside a plain-words paragraph")
                for sent in sentences(body):
                    n = word_count(sent)
                    if n > args.max_words:
                        warnings.append(f"{rel}:{line}: plain-words sentence of {n} words: {sent}")
            else:
                n_env += 1
                if not has_plain:
                    errors.append(f"{rel}:{line}: \\begin{{{payload}}} has no plain-words paragraph "
                                  f"before it (since the previous statement)")
                has_plain = False

    if n_par == 0:
        errors.append("no plain-words paragraph found; if the paper marks them with a macro "
                      "defined over several lines, pass --marker <name>")

    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}")
    print(f"plain-words paragraphs {n_par}; statements checked {n_env}; "
          f"errors {len(errors)}; warnings {len(warnings)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

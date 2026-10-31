#!/usr/bin/env python3
"""Create the folder layout for a new paper with a compilable empty shell.

Usage: new_paper.py <slug> --question "<research question>" [--root papers]
"""
import argparse
import json
import re
import sys
from pathlib import Path

MAIN_TEX = r"""\documentclass[11pt,a4paper]{article}
\usepackage[margin=2.5cm]{geometry}
\usepackage{amsmath,amsthm,amssymb}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage[hidelinks]{hyperref}
\usepackage{cleveref}
\usepackage[backend=biber,style=numeric,urldate=long]{biblatex}
\addbibresource{references.bib}
\graphicspath{{figures/}}

\theoremstyle{definition}
\newtheorem{definition}{Definition}[section]
\newtheorem{example}[definition]{Example}
\theoremstyle{plain}
\newtheorem{theorem}[definition]{Theorem}
\newtheorem{lemma}[definition]{Lemma}
\theoremstyle{remark}
\newtheorem{remark}[definition]{Remark}

\title{%(title)s}
\author{}
\date{\today}

\begin{document}
\maketitle

\begin{abstract}
To be written by the author agent.
\end{abstract}

\input{sections/introduction}
\input{sections/background}
\input{sections/analysis}
\input{sections/discussion}
\input{sections/conclusion}

\printbibliography

\appendix
\input{appendices/derivations}

\end{document}
"""

SECTIONS = {
    "introduction": "Introduction",
    "background": "Background",
    "analysis": "Analysis",
    "discussion": "Discussion",
    "conclusion": "Conclusion",
}

README = """# %(title)s

Research question: %(question)s

## Compile

    bash ../../.claude/skills/research-paper/scripts/build.sh .

Requires TeX Live with `latexmk` and `biber`. The compiled paper is
`main.pdf`. Auxiliary files go to `build/`.

## Files

- `main.tex`, `sections/`, `appendices/`: the paper.
- `references.bib`: bibliography. Keys match source ids in `evidence/evidence.json`.
- `evidence/evidence.json`: every source and claim with its support.
- `modules/`: subject-matter module reports.
- `self-evaluation.md`: the author's section by section justification.
- `evaluation-report.md`: independent evaluation rounds and release decision.
"""


def slug_ok(slug: str) -> bool:
    return re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", slug) is not None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--question", required=True)
    ap.add_argument("--root", default="papers")
    args = ap.parse_args()

    if not slug_ok(args.slug):
        print("slug must be lowercase words separated by hyphens", file=sys.stderr)
        return 1

    paper = Path(args.root) / args.slug
    if paper.exists():
        print(f"{paper} already exists", file=sys.stderr)
        return 1

    for sub in ("sources", "evidence/modules", "modules", "sections",
                "appendices", "figures", "build"):
        (paper / sub).mkdir(parents=True)

    title = args.slug.replace("-", " ").capitalize()
    (paper / "main.tex").write_text(MAIN_TEX % {"title": title})
    for name, heading in SECTIONS.items():
        (paper / "sections" / f"{name}.tex").write_text(
            f"\\section{{{heading}}}\\label{{sec:{name}}}\n\nTo be written.\n")
    (paper / "appendices" / "derivations.tex").write_text(
        "\\section{Derivations}\\label{app:derivations}\n\nTo be written.\n")
    (paper / "references.bib").write_text("")
    (paper / "README.md").write_text(README % {"title": title, "question": args.question})
    (paper / "brief.md").write_text(
        f"# Research brief\n\n1. Research question: {args.question}\n")
    (paper / "build" / ".gitignore").write_text("*\n!.gitignore\n")
    evidence = {"question": args.question, "sources": [], "claims": [], "contradictions": []}
    (paper / "evidence" / "evidence.json").write_text(json.dumps(evidence, indent=2) + "\n")

    print(f"created {paper}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

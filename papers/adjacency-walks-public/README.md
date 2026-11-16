# Adjacency walks public

Research question: For a finite simple undirected graph with N vertices and adjacency matrix A: what does the entry (A^k)_{ij} count, what is a path between two vertices, and how can one decide from A alone whether the graph is connected?

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

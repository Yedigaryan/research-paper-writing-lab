# Adjacency walks connectivity

Research question: For a simple undirected graph with N vertices given by its adjacency matrix A: what does (A^k)_{ij} represent, how can one determine from A whether the graph is connected, and what is a path between n_i and n_j?

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

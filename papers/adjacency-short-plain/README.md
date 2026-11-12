# Adjacency short plain

Research question: For a simple undirected graph with N vertices given by its adjacency matrix A: (1) what does the entry (A^k)_{ij} represent, (2) how can one determine from A whether the graph is connected, and (3) what is the definition of a path between vertices n_i and n_j?

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

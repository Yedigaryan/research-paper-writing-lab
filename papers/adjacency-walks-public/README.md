# Adjacency walks public

Research question: For a finite simple undirected graph with N vertices and adjacency matrix A: what does the entry (A^k)_{ij} count, what is a path between two vertices, and how can one decide from A alone whether the graph is connected?

## Compile

    bash ../../.claude/skills/research-paper/scripts/build.sh .

Run it from the repository root as `bash .claude/skills/research-paper/scripts/build.sh papers/adjacency-walks-public`. Requires TeX Live with `latexmk` and `biber`. The compiled paper is
`main.pdf`. Auxiliary files go to `build/`.

## Files

- `main.tex`, `sections/`, `appendices/`: the paper.
- `references.bib`: bibliography. Keys match source ids in `evidence/evidence.json`.
- `evidence/evidence.json`: every source and claim with its support.
- `scripts/`: `public_examples.py` recomputes the matrices of the examples (`python3 -I scripts/public_examples.py`); the other scripts check the long version's lemmas.
- `self-evaluation.md`: the author's section by section justification.

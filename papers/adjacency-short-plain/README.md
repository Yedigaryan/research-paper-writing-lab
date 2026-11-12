# Adjacency short plain

Research question: For a simple undirected graph with N vertices given by its adjacency matrix A: (1) what does the entry (A^k)_{ij} represent, (2) how can one determine from A whether the graph is connected, and (3) what is the definition of a path between vertices n_i and n_j?

## Compile

From the repository root:

    bash .claude/skills/research-paper/scripts/build.sh papers/adjacency-short-plain

Requires TeX Live with `latexmk` and `biber`. The compiled paper is
`main.pdf` (4 pages, references included); auxiliary files go to `build/`.

## Files

- `main.tex`, `sections/` (introduction, setting, answers, example): the paper. There is no appendix.
- `references.bib`: the seven cited sources; keys match source ids in `evidence/evidence.json`.
- `evidence/evidence.json`: every source and claim with its support (shared with the long version; not all of it is used).
- `modules/`, `scripts/`: module reports and scripts with outputs of the long version, reused as input.
- `self-evaluation.md`: the author's section by section justification.

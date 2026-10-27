# Research Paper Writing Lab

A Claude Code pipeline that turns a research question, documents, data, or
lecture photos into an evidence-based paper in LaTeX with a compiled PDF, a
BibTeX bibliography, and an independent evaluation report. The repository
also holds the papers it has produced.

## Layout

- `Grafneri_tesutyun.pdf`: the course textbook (Graph Theory, Armenian). Study-note papers cite its definition numbers and use it as the quality bar.
- `papers/<topic>/`: one folder per paper. New papers follow the layout in `.claude/skills/research-paper/references/latex-structure.md`. The first paper, written before the LaTeX pipeline, is Markdown (`paper.md`) with its source photos under `sources/`.
- `.claude/skills/research-paper/`: the skill that orchestrates the pipeline. `SKILL.md` is the workflow; `references/` holds the rubric, the evidence schema, the LaTeX conventions, the photo-input procedure, and the textbook standard; `scripts/` holds the build and check scripts.
- `.claude/agents/`: the agents the skill spawns: `research-agent`, `module-owner`, `paper-author`, `paper-evaluator`, `technician-reader`. Each file pins its model level; the ladder is in `references/model-levels.md`.
- `tests/`: a fixture paper with planted defects and the script that checks the mechanical gates catch them.

## How a paper is produced

1. The session analyses the input, writes `brief.md`, and asks the user only what changes the paper.
2. `research-agent` builds `evidence/evidence.json`: every source, its access status, every claim with a locator and quote.
3. One `module-owner` per subtopic explains it from first principles and adds evidence.
4. `paper-author` writes the LaTeX, compiles it, runs the checks, and writes a self-evaluation.
5. A fresh `paper-evaluator` on a higher model level scores twelve dimensions and lists findings; `technician-reader` reports passages a newcomer cannot follow.
6. The session records the round in `evaluation-report.md`, sends findings back to the author, and repeats until every release condition passes or three rounds are spent.

Compiling a paper needs TeX Live with `latexmk` and `biber`.

## Papers

- `papers/adjacency-matrix-connectivity/`: adjacency matrix, meaning of the entries of its powers, path definition, and the connectivity test for an undirected graph.

# Research Paper Writing Lab

A Claude Code pipeline that turns a research question, documents, data, or
lecture photos into an evidence-based paper in LaTeX with a compiled PDF, a
BibTeX bibliography, and an independent evaluation report. The repository
also holds the papers it has produced.

## Layout

- `Grafneri_tesutyun.pdf`: the course textbook (Graph Theory, Armenian). Study-note papers cite its definition numbers and use it as the quality bar.
- `papers/<topic>/`: one folder per paper. New papers follow the layout in `.claude/skills/research-paper/references/latex-structure.md`. The first paper, written before the LaTeX pipeline, is Markdown (`paper.md`) with its source photos under `sources/`.
- `.claude/skills/research-paper/`: the skill that orchestrates the pipeline. `SKILL.md` is the workflow; `references/` holds the rubric, the evidence schema, the LaTeX conventions, the photo-input procedure, and the textbook standard; `scripts/` holds the build and check scripts.
- `.claude/agents/`: the agents the skill spawns: `research-agent`, `module-owner`, `paper-author`, `paper-evaluator`, `technician-reader`. Each file pins its model level; the ladder is in `references/model-levels.md`. The three `harness-*` agents belong to the refinement skill below.
- `.claude/skills/harness-refine/`: the skill that improves the pipeline's own harness by the Harness2 loop (propose on two dimensions, probe each candidate in a fresh session, compose, select the best paper blind, reflect a lesson into a per-domain library, adopt the winner). `harness.yaml` declares what the loop may edit and what is frozen; `scripts/` validates trees and builds the evidence an improver reads; `library/` holds adopted harnesses. The adoption plan is in `docs/harness2-adoption-plan.md`; attribution in `third_party/harness2/`.
- `tests/`: a fixture paper with planted defects, the script that checks the mechanical gates catch them, and the tests of the refinement scripts. Run `bash tests/run-checks.sh`.

## How a paper is produced

1. The session analyses the input, writes `brief.md`, and asks the user only what changes the paper.
2. `research-agent` builds `evidence/evidence.json`: every source, its access status, every claim with a locator and quote.
3. One `module-owner` per subtopic explains it from first principles and adds evidence.
4. `paper-author` writes the LaTeX, compiles it, runs the checks, and writes a self-evaluation.
5. A fresh `paper-evaluator` on a higher model level scores twelve dimensions and lists findings; `technician-reader` reports passages a newcomer cannot follow.
6. The session records the round in `evaluation-report.md`, sends findings back to the author, and repeats until every release condition passes or three rounds are spent.

Compiling a paper needs TeX Live with `latexmk` and `biber`.

## How the harness is refined

Invoke `harness-refine` on a finished paper. The session exports the
editable harness, builds a context directory from the paper's git history
and reports, and spawns two proposers that edit copies of the tree from
that evidence. Each valid candidate is installed on its own branch and
probed by a fresh session. A composer merges the candidates, the composed
tree is probed, a fresh evaluator picks the best paper without knowing
which harness made it, a reflector writes what each edit did, and the
tree behind the chosen paper is adopted. Keeping the base is a normal
result. The evaluator, the reader, the rubric, and the model ladder are
never editable by the loop.

## Papers

- `papers/adjacency-matrix-connectivity/`: adjacency matrix, meaning of the entries of its powers, path definition, and the connectivity test for an undirected graph.

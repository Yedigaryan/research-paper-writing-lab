# Research brief

Paper folder: `papers/adjacency-short-plain/`. Short version of the
adjacency paper, written without analogies. Its twin,
`papers/adjacency-short-analogies/`, is the same text with analogies
added, so that the two can be compared.

## 1. Research question

For a simple undirected graph with N vertices given by its adjacency
matrix A: (1) what does the entry (A^k)_{ij} represent, (2) how can one
determine from A whether the graph is connected, and (3) what is the
definition of a path between vertices n_i and n_j?

Questions 1 and 2 are on the lecture whiteboard. Question 3 is from the
user's assignment text (`sources/user-statements.md`).

## 2. Objectives

The paper answers the three questions and nothing else:

- Define the adjacency matrix of a simple undirected graph.
- Define walk, path (course convention: no repeated vertex), and
  connected.
- State and prove that (A^k)_{ij} is the number of walks of length k
  from n_i to n_j, and warn once that it counts walks, not paths.
- Give the definition of a path between n_i and n_j.
- State and prove one test for connectivity that uses only A.
- Show all of it on the board's three-vertex graph, and show the test
  failing on one disconnected graph.

## 3. Scope and exclusions

In scope: the items in section 2.

Out of scope, and not to be written even though the evidence file covers
them: trail, cycle, closed walk, and distance as separate definitions;
the table of three naming conventions; breadth-first search beyond one
sentence; components beyond what the proof needs; directed graphs,
multigraphs, weights, eigenvalues, complexity; the board drawing and
matrix mismatch beyond one sentence; source access notes and
contradictions between sources (they stay in the evidence file).

## 4. Audience register

`technician`. No plain words layer, no story, no analogies, no
"In plain words" paragraphs. The devices of `book-style-standard.md`
after each definition (remark, example, non-example) are not required;
use one only where a reader would go wrong without it.

## 5. Input inventory

| File | Content | Reliability |
|---|---|---|
| `sources/whiteboard-1.jpg`, `sources/whiteboard-2.jpg` | Lecture board: definition of A_{ij}, a 3 by 3 matrix with rows 0 1 0 / 1 0 1 / 0 1 0, the two questions, the definition of connected. | Legible. |
| `sources/user-statements.md` | The user's assignment text and conventions. | As stated by the user. |
| `../../Grafneri_tesutyun.pdf` | Course textbook. Definitions 1.2.10 walk, 1.2.13 simple path, 2.1.1 connected. | Primary source for definitions and numbering. |
| `evidence/evidence.json`, `modules/*.md`, `scripts/` | Evidence, module reports, and scripts of the long version of this paper (branch `claude/harness/adjacency-pipeline/composed`, commit 96a36c8, 21 pages, decision PASS after three rounds). | Verified in that run. |

## 6. Allowed research sources

No new research. Use only sources and claims already in
`evidence/evidence.json`. Textbook numbers, pages, and attributions must
agree with `references/graph-sources.md`.

## 7. Assumptions

- The graph is finite, simple, and undirected (user's text; the board's
  matrix is symmetric with a zero diagonal).
- The mark above A on the board is a power k (user's text).
- The example graph is the one the board's matrix encodes: edges
  n_1 n_2 and n_2 n_3.
- "Path" means a walk with no repeated vertex, the textbook's
  Definition 1.2.13 (user's text). One sentence says that the textbook
  calls this a simple path.
- A walk of length 0 is allowed, as the paper's own convention, as in
  the long version.

## 8. Open questions for the user

None.

## 9. Proposed modules

No new modules. The module reports m1, m2, and m3 of the long version
are reused as input.

## 10. Deliverables and constraints

- `main.tex`, `sections/`, `references.bib`, compiled `main.pdf`,
  `self-evaluation.md`.
- Length: at most 5 pages in total, references included, in the
  template's format (11pt, A4, 2.5 cm margins). Aim for 4. Do not change
  the font size, margins, or line spacing to meet it, and do not move
  body text to an appendix. No appendix.
- Structure: a short introduction that states the three questions and
  the three answers in one sentence each; setting and definitions;
  answer 1 with proof; answer 3; answer 2 with proof; the worked
  example; a closing paragraph with the limits of the test. No separate
  discussion section.
- Every proof is complete. Brevity comes from leaving out side topics
  and repetition, never from skipping a proof step.
- Every number in the worked example is taken from a script output in
  `scripts/` or recomputed by script.
- Clean text, no emojis. Citation style: biblatex numeric.

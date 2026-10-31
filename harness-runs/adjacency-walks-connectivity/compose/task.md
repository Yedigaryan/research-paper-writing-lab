# Research brief

Paper folder: `papers/adjacency-walks-connectivity/`. Written by the
orchestrator from two whiteboard photos, the user's assignment text, and
the course textbook.

## 1. Research question

For a simple undirected graph with N vertices given by its adjacency
matrix A: (1) what does the entry (A^k)_{ij} represent, (2) how can one
determine from A whether the graph is connected, and (3) what is the
definition of a path between vertices n_i and n_j?

Questions 1 and 2 are written on the lecture whiteboard. Question 3 was
added by the user's assignment text.

## 2. Objectives

The paper must:

- Define the adjacency matrix and its basic properties for a simple
  undirected graph.
- State and prove that (A^k)_{ij} counts walks of length k from n_i to
  n_j, and make explicit that it counts walks, not paths.
- Define walk, trail, path, and cycle with the course textbook's numbering,
  and give the definition of a path between n_i and n_j under the course
  convention (no repeated vertices).
- Give a test for connectivity that uses only A, prove that it is correct,
  and show it on a connected and on a disconnected example.
- Follow the course textbook's presentation standard and the plain words
  layer required by the study-note register.

## 3. Scope and exclusions

In scope: finite simple undirected graphs; walks, trails, paths, cycles,
distance; connectivity and components; the matrix-power connectivity test;
a breadth-first search alternative stated for comparison; a worked example
with three vertices consistent with the board.

Out of scope: directed graphs and multigraphs beyond a one-sentence remark;
weighted graphs; eigenvalue methods; algorithmic complexity beyond a short
remark; implementation code.

## 4. Audience register

`study-note`. The reader is a student meeting these ideas for the first
time. The textbook standard in `book-style-standard.md` and the plain
words layer in `photo-input.md` apply. The technician-level standard
applies as the floor.

## 5. Input inventory

| File | Content | Reliability |
|---|---|---|
| `sources/whiteboard-1.jpg` | Lecture board: definition of A_{ij}, a three-vertex drawing, a 3 by 3 matrix, the problem statement, two questions, definition of connected. | Clearly legible for the prose; see assumptions for the marks that are not. |
| `sources/whiteboard-2.jpg` | Same board, second photo, slightly different angle. Read together with the first. | Same. |
| `../../Grafneri_tesutyun.pdf` | Course textbook, Graph Theory, Armenian, 216 pages. Chapter 1 (basic definitions, p. 9) and Chapter 2 (p. 48, connectivity in 2.1) are relevant. Definitions 1.2.10 walk, 1.2.11 closed walk, 1.2.12 path (no repeated edges, English trail), 1.2.13 simple path (no repeated vertices), 1.2.14 cycle, 1.2.16 distance, 2.1.1 connected. | Primary source for definitions and numbering. Its PDF text layer drops most symbols; quote formulas only after viewing the page as an image. |

Board transcription, reading order:

1. A_{ij} = 1 if e_{ij} in V, 0 if e_{ij} not in V. (The board writes V for
   the edge set.)
2. A drawing with vertices labelled 1, 2, 3 and a matrix labelled "adj."
   with rows 0 1 0 / 1 0 1 / 0 1 0.
3. "Problem. Given graph (G, V) with N nodes i.e. |G| = N and the graph is
   represented through its adj. matrix. So you have A matrix."
4. "1) What does A^{..}_{ij} represent" with a small mark above A.
5. "2) How to know if graph is connected or not."
6. "Def. Graph is called connected if for any n_i, n_j there exists a path
   between nodes."

Clearly visible: all prose above, the matrix entries, the vertex labels.
Likely interpretation: the mark above A is a power k. Unclear: the drawing
shows a line from 1 to 2 with an arrowhead at 2, a line from 1 to 3, and a
line from 2 to 3, which would be three edges, while the matrix encodes only
the edges 1-2 and 2-3.

## 6. Allowed research sources

- Primary for definitions, numbering, and the presentation standard: the
  course textbook, cited as a `local-file` source with page and definition
  number as locator.
- Web search for the walk-counting theorem and the connectivity test, which
  the textbook does not state: standard graph theory textbooks (for example
  Diestel, West, Bondy and Murty, Biggs) and official lecture notes. Prefer
  sources that can be fetched and quoted. Record access status honestly.
- No other user-supplied files.

## 7. Assumptions

- The graph is finite, simple, and undirected: stated in the user's
  assignment text; consistent with the symmetric zero-diagonal matrix on the
  board.
- The mark above A in question 1 is a power k: the user's text asks about
  A^k.
- The arrowhead on the 1-2 line is a stray mark: the matrix is symmetric
  and the problem says undirected.
- Where the drawing and the matrix disagree, the matrix is the example
  graph: the problem statement says the graph is given through its
  adjacency matrix. The paper reports the mismatch.
- "Path" in the course means a walk with no repeated vertices, the
  textbook's Definition 1.2.13 (simple path): stated by the user. The paper
  gives the textbook's and the English conventions beside it.
- The board's (G, V) and e_{ij} in V are the textbook's G = (V, E) and
  e_{ij} in E: notation difference only.
- Vertices are named n_1, ..., n_N as on the board; the textbook's v_i is
  mentioned once.

## 8. Open questions for the user

None that change the paper. All were settled in the earlier conversation
about this material.

## 9. Proposed modules

| Id | Module | Must establish | Depends on |
|---|---|---|---|
| m1 | Adjacency matrix and walk counting | Definition and properties of A (symmetric, zero diagonal, row sums are degrees); the theorem that (A^k)_{ij} is the number of walks of length k from n_i to n_j, with a full induction proof; the warning that walks are not paths, with a counterexample where (A^2)_{ii} > 0. | m2 for the definition of walk |
| m2 | Walks, trails, paths, cycles, and the course convention | Textbook Definitions 1.2.10 to 1.2.16 with numbers; the three naming conventions (course, textbook, English) in one table; the definition of a path between n_i and n_j; the lemma that every walk from u to v contains a path from u to v; distance. | none |
| m3 | Connectivity from the adjacency matrix | Textbook Definition 2.1.1 and components; the test: G is connected iff every off-diagonal entry of A + A^2 + ... + A^{N-1} is positive, equivalently (I + A)^{N-1} has no zero entry; proof using m1 and m2; a connected and a disconnected three-vertex example with every matrix written out; breadth-first search as the alternative in one paragraph. | m1, m2 |

Shared terms to keep consistent across modules: walk, path, length of a
walk, N, n_i, A, e_{ij}, connected, component.

## 10. Deliverables and constraints

- `main.tex`, `sections/`, `references.bib`, compiled `main.pdf`,
  `evaluation-report.md`, per `latex-structure.md`.
- Study-note register: numbered definitions in the textbook's build order,
  each followed by a remark, an example, and a non-example; a plain words
  paragraph before every definition, theorem, test, and worked example; the
  textbook's definition numbers cited.
- Clean text, no emojis. Citation style: biblatex numeric.
- Every matrix product in the worked example computed by script.

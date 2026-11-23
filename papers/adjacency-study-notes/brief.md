# Research brief

Paper folder: `papers/adjacency-study-notes/`. Study notes for the course
reader on the lecture's adjacency-matrix problem, written from the start
under the current pipeline rules.

## 1. Research question

For a simple undirected graph with N vertices given by its adjacency
matrix A: (1) what does the entry (A^k)_{ij} represent, (2) how can one
determine from A whether the graph is connected, and (3) what is the
definition of a path between vertices n_i and n_j?

Questions 1 and 2 are on the lecture whiteboard
(`sources/whiteboard-1.jpg`, `sources/whiteboard-2.jpg`). Question 3 is
from the user's assignment, known only through the summary in
`sources/user-statements.md`.

## 2. Objectives

Needed to answer:

- N1. Fix the setting and the notation: a finite simple undirected graph
  with vertices n_1, ..., n_N, and its adjacency matrix A.
- N2. Define walk and its length.
- N3. Define path in the course's sense, a walk with no repeated vertex,
  and state the definition of a path between n_i and n_j. This is the
  answer to question 3.
- N4. Define connected.
- N5. State and prove that (A^k)_{ij} is the number of walks of length k
  from n_i to n_j, and show on the board's graph one entry that counts a
  walk which is not a path. This is the answer to question 1.
- N6. State and prove that a walk from n_i to n_j contains a path from
  n_i to n_j, and that a path has length at most N - 1.
- N7. State and prove one test for connectivity that uses only A: the
  graph is connected exactly when every entry off the diagonal of
  A + A^2 + ... + A^{N-1} is positive. This is the answer to question 2.
- N8. Work the board's three-vertex graph through N5 and N7 with every
  matrix printed, and show the test failing on one disconnected graph.
- N9. Say in one short paragraph what the test does not give (it is not
  the cheapest way to test connectivity, since a graph search does the
  same job with less work, and the entries count walks, not paths).

Optional, written only if the page budget allows:

- O1. The equivalent form of the test with (I + A)^{N-1}.
- O2. The least k with (A^k)_{ij} > 0 as the distance from n_i to n_j.
- O3. A note that two of the sources state these results with the word
  "paths" where walks are meant.

## 3. Scope and exclusions

In scope: the objectives above.

Out of scope: trail, cycle, closed walk, and distance as separate
definitions (distance only under O2); components beyond what the proof of
N7 needs; graph search (depth-first or breadth-first) beyond one sentence in N9; directed graphs,
multigraphs, weights, eigenvalues, the Laplacian, complexity analysis; a
table of naming conventions; a critique of the sources beyond O3.

## 4. Audience register

`study-note`

Analogies: no

The input is lecture material and the reader is the student, so the
register is `study-note`: numbered definitions in the textbook's order
with the textbook's own numbers, and a remark or example after a
definition only where a reader would go wrong without it
(`references/photo-input.md`, `references/book-style-standard.md`). No
plain words layer: the request did not ask for analogies, and the default
is `no`.

## 5. Input inventory

| File | Content | Reliability |
|---|---|---|
| `sources/whiteboard-1.jpg`, `sources/whiteboard-2.jpg` | Two photos of the same lecture board; read together below. | Legible except where noted. |
| `sources/user-statements.md` | A summary (not verbatim) of what the user stated about the assignment and the conventions, and the verbatim request of 2026-11-23. | The summary may not be quoted as the user's words. The request may. |
| `Grafneri_tesutyun.pdf` (repository root) | Course textbook, in Armenian: Petrosyan, Mkrtchyan, Kamalyan, Graph Theory. | Primary source for definitions and their numbers. Its text layer drops symbols; formulas are checked by viewing the page as an image. |

Reading of the board, in order:

1. `A_ij = { 1, if e_ij in V ; 0, if e_ij not in V }`, where the word
   read as "if" is written in Armenian.
2. A drawing of three circled vertices 1, 2, 3 with three lines: 1 to 2
   (with an arrowhead at 2), 2 to 3, and 1 to 3.
3. A 3 by 3 grid labelled "adj." with rows 0 1 0 / 1 0 1 / 0 1 0.
4. "Problem: Given graph (G, V) with N nodes i.e. |G| = N and the graph
   is represented through its adj. matrix. So you have "A" matrix."
5. "1) What does A''_ij represent", where two small marks stand above A.
6. "2) How to know if graph is connected or not."
7. "Def. Graph is called connected if for any n_i, n_j there exists a
   path between nodes."

Clearly visible: items 1, 3, 4, 6, 7, and the three lines of the drawing.

Likely interpretation: the two marks above A in item 5 are a power, read
as A^k (the user's summary says the question is about A^k). In item 1 the
set after "in" is the edge set, although the board writes V.

Mismatches, reported and not resolved by picking a side silently: the
drawing has three edges (1-2, 2-3, 1-3) and an arrowhead; the matrix has
two edges (n_1 n_2 and n_2 n_3), is symmetric, and has a zero diagonal.
The board writes the graph as (G, V) and the edge condition as
"e_ij in V"; the textbook writes G = (V, E) and "v_i and v_j are
adjacent". The board's definition of connected says "path" without
defining it.

## 6. Allowed research sources

The course textbook is the primary source for every definition and its
number. `references/graph-sources.md` lists locators that earlier
evaluators verified; it is a list of where to look, not evidence, and
each page is viewed again before it is cited.

The textbook has no walk-counting theorem and no matrix test for
connectivity, so these two results are taken from sources on the web and
proved in the paper. Web search is allowed for them; prefer freely
readable primary texts (lecture notes with numbered statements, a
textbook on arXiv) that the reader can open. The evidence files of the
earlier papers in this repository may be used as leads to sources and
never as verification: a source supports a claim here only if it was
opened in this run.

## 7. Assumptions

- The graph is finite, simple, and undirected. Reason: the user's
  summary says so, and the board's matrix is symmetric with a zero
  diagonal.
- The marks above A on the board are a power k. Reason: the user's
  summary.
- The example graph is the one the board's matrix encodes, with edges
  n_1 n_2 and n_2 n_3; the drawing's third line is not used. Reason: the
  matrix is the object both questions are about. The mismatch is
  reported in the notes on sources.
- Vertices are written n_1, ..., n_N as on the board; the textbook's
  v_i is mentioned once.
- "Path" means a walk with no repeated vertex, which the textbook calls
  a simple path (Definition 1.2.13). Reason: the user's summary. The
  paper says in one clause where the term is defined that this is its
  meaning; who uses the other meaning goes in the notes on sources.
- A walk of length 0 is allowed, as the paper's convention. Reason: the
  proofs need it for the case i = j, and the textbook's usage agrees
  (see `graph-sources.md`).
- "New notes ... with the latest changes applied" is read as: the same
  three questions, written again as notes for the user's own reading
  under the current pipeline rules. Reason: the question has not changed
  since the last request, and the publishing version already follows the
  current rules but leaves out the course context.
- The notes are in English, like the earlier versions.

## 8. Open questions for the user

None that changes scope. If analogies are wanted, the brief line changes
to `Analogies: yes` and the paper is revised with the plain words layer.

## 9. Proposed modules

- `m1`, definitions and walk counting. Serves N1, N2, N3, N4, N5, and O2
  (optional). Establishes each definition with the textbook's number and
  page, the walk-counting theorem with a complete proof, and the entry of
  the board graph that counts a walk which is not a path.
- `m2`, the connectivity test. Serves N6, N7, N8, N9, and O1, O3 (both
  optional). Establishes the walk-contains-path lemma with the bound
  N - 1, the sum test with a complete proof, the worked board example and
  one disconnected example with every matrix computed by script, and the
  limits of the test.

Dependency: `m2` uses the definitions and the theorem of `m1` exactly as
this brief states them (sections 2 and 7), so that the two can be written
in parallel.

## 10. Deliverables and constraints

Page budget: 6. Count: five definitions or settings (N1 to N4, with the
adjacency matrix counted separately), one theorem, one lemma, and one
test at about half a page each make four pages; the worked board example
with the disconnected example takes one; the introduction, the notes on
sources, and the references take one.

- `main.tex`, `sections/`, `references.bib`, compiled `main.pdf`,
  `self-evaluation.md`.
- The budget is a ceiling. Do not change the font size, margins, or line
  spacing to meet it, and never shorten a proof to fit; report instead.
- Every proof is complete.
- Every matrix, product, sum, and count is computed by a script in
  `scripts/` before it is written, and every matrix an example uses is
  printed.
- Where the inputs came from (the board, the user's summary, the reading
  of the marks, the drawing and matrix mismatch, what the textbook lacks)
  goes in `\section*{Notes on sources}`; the body only cites.
- Clean text, no emojis. Citation style: biblatex numeric.

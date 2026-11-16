# Research brief

Paper folder: `papers/adjacency-walks-public/`. The version of the
adjacency paper for readers outside the course: it is sent to people who
have none of the context behind it.

## 1. Research question

For a finite simple undirected graph with N vertices and adjacency matrix
A: what does the entry (A^k)_{ij} count, what is a path between two
vertices, and how can one decide from A alone whether the graph is
connected?

Origin, for this brief only: the three questions of
`papers/adjacency-short-plain/`, which came from a lecture board and an
assignment. The paper itself states the questions with no origin.

## 2. Objectives

Needed to answer:

- Define the adjacency matrix, a walk and its length, a path, and a
  connected graph.
- State and prove that (A^k)_{ij} is the number of walks of length k from
  v_i to v_j, and show with one example that it does not count paths.
- State the definition of a path between two vertices.
- State and prove one test for connectivity that uses only A: the graph
  is connected if and only if every off-diagonal entry of
  A + A^2 + ... + A^{N-1} is positive. The proof includes the step that
  every walk contains a path and the bound N - 1 on the length of a path.
- One worked example on a connected graph with three vertices, the same
  test failing on one disconnected graph, and one example that shows why
  the sum must run to A^{N-1}.
- One closing paragraph on the limits of the test.

Optional, only if the page budget allows:

- One sentence that the test can also be written as "(I + A)^{N-1} has no
  zero entry", with its source.
- One sentence that two of the cited sources word the entries as counting
  "paths" where they count walks.

## 3. Scope and exclusions

In scope: the objectives above.

Out of scope: trails, cycles, closed walks, and distance as separate
definitions; breadth-first search; components beyond what a proof needs;
directed graphs, multigraphs, weights, eigenvalues, complexity; any
comparison of naming conventions between books.

## 4. Audience register

Analogies: no

`technician`. The reader knows how to multiply matrices and what a proof
by induction is, and has never studied graphs. The reader has no access to
any course material, to the textbook the earlier versions cite, or to this
repository.

## 5. Input inventory

| File | Content | Reliability |
|---|---|---|
| `evidence/evidence.json` | The claims of the long version that rest only on publicly accessible sources: Grinberg (arXiv text), Gotti (MIT lecture notes), Paramadevan and Sotheeswaran (journal article), the Galway notes, and Bai (lecture notes). | Verified in the long version's run (branch `claude/harness/adjacency-pipeline/composed`, three evaluation rounds). |
| `papers/adjacency-short-plain/sections/*.tex` | The short paper without analogies, 4 pages. Its statements and proofs are the starting text. | Passed the mechanical checks; read by the test reader; not read by an evaluator. |
| `scripts/` | Scripts and outputs for the examples, for the author's own checking. | Reran identically in the long version's run. |

## 6. Allowed research sources

No new research. The paper cites only the five sources in
`evidence/evidence.json`, each of which a reader can open from its
reference entry. It does not cite the course textbook, the board photos,
the user's statements, or any other local or unpublished material, and
there is no reference entry for any of them. Prefer the source with a
named author where two sources state the same result.

## 7. Assumptions

- The graph is finite, simple, and undirected.
- Vertices are named v_1, ..., v_N.
- A path is a walk with no repeated vertex, and a walk may have length 0,
  both as in Grinberg's Definition 2.9.1.
- The example graph has edges v_1 v_2 and v_2 v_3.

## 8. Open questions for the user

None.

## 9. Proposed modules

No new modules. The long version's evidence is reused; the module reports
are not, because they are written around the course textbook.

## 10. Deliverables and constraints

Page budget: 5. Count: four definitions, one theorem, two lemmas, and one
test at about half a page each make four pages; the worked example and the
introduction with the references take the fifth, because the definitions
are short.

- `main.tex`, `sections/`, `references.bib`, compiled `main.pdf`,
  `self-evaluation.md`.
- The paper stands alone. It does not mention a board, a lecture, a
  course, an assignment, a user, a textbook the reader cannot open, a
  search of a source, scripts, a scripts folder, or an earlier version.
  It has no notes on sources section, because nothing about its inputs is
  left to say; a result is attributed by its citation.
- Nothing is cited for a fact that the paper proves itself except to say
  who also states it. No phrase such as "this paper's own convention";
  state a convention once and cite the source that shares it.
- Every number in the examples can be checked by hand from the matrices
  printed in the paper. Print every matrix an example uses, and name the
  walks that an entry counts where the entry is used in an argument.
- Every proof is complete.
- The author field stays empty for the sender to fill in. Use a fixed
  date, not `\today`.
- Clean text, no emojis. Citation style: biblatex numeric.

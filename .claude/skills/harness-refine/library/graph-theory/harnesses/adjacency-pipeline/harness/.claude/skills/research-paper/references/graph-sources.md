# Verified facts about the sources of graph-theory papers

Read when the paper cites the course textbook `Grafneri_tesutyun.pdf` or
one of the sources listed below. Every fact here was checked against the
page image or the source text by the evaluators of the
adjacency-walks-connectivity paper (runs of 2026-10-27, 2026-11-02,
2026-11-05 and 2026-11-06). They are locators and
attributions, not evidence: a claim still needs its own quote in the
evidence file, copied from the page you viewed. Do not write what a page
contains, or list it as checked, because this file says so; view it.

If a fact here disagrees with the evidence file, view the page, follow the
page, and correct the claim in the fragment that owns it.

## Course textbook (Petrosyan, Mkrtchyan, Kamalyan, Graph Theory, Armenian)

Printed page numbers are one lower than PDF page numbers (printed p. 16 is
PDF p. 17). Cite printed pages and say once that you do.

The book's build order and locations:

| Concept | Book's number | Printed page | Book's word, where it differs from English |
|---|---|---|---|
| graph G = (V, E) | Definition 1.1.1 | 9 | |
| adjacent | Definition 1.1.4 | 11 | |
| adjacency matrix A(G) | no number of its own, after Definition 1.1.6 | 11 | |
| degree, written d_G(v) or d(v) | Definition 1.2.1 | 16 | |
| sum of all degrees equals twice the number of edges (Euler) | Theorem 1.2.1 | 16 | |
| walk | Definition 1.2.10 | 21 | |
| closed walk | Definition 1.2.11 | 22 | |
| walk with no repeated edge (English trail) | Definition 1.2.12 | 22 | "path" |
| walk with no repeated vertex (English path) | Definition 1.2.13 | 22 | "simple path" |
| cycle | Definition 1.2.14 | 22 | |
| simple cycle | Definition 1.2.15 | 22 | |
| distance | Definition 1.2.16 | 22 to 23 | |
| every (u, v)-walk contains a simple (u, v)-path, stated for u not equal to v, no length bound, proved by induction on the walk's length | Lemma 1.2.1 | 23 | |
| connected | Definition 2.1.1 | 48 | |
| connectivity components | in prose, no number | 49 | |
| connected if and only if one component | Remark 2.1.1 | 49 | |

Consequences the paper must respect:

- The book does define degree (Definition 1.2.1), and it does so after the
  adjacency matrix. A paper in the book's order puts degree after A.
- Fig. 1.2.5, the example graph for Definitions 1.2.10 to 1.2.15, is on
  printed p. 21. It also has the edge v1v5, which none of the book's
  examples uses. Say the examples "use" seven edges, not that they "force"
  them.
- A full-text search of the whole book finds the adjacency matrix only on
  printed pp. 7, 11, 12, 34, 61, and finds no walk-counting theorem and no
  matrix test for connectivity. State that absence as the result of a
  full-text search, take both results from other sources, and prove them
  in the paper. Printed p. 7 is the list of notations: A(G) is the
  adjacency matrix (հարևանության մատրից), B(G) the incidence matrix
  (կցության մատրից), so hits for կցության are incidence-matrix pages. The
  evaluators viewed pages 12 (incidence matrix), 34 (isomorphism) and 61
  (Laplacian, Kirchhoff) and found neither result there.
- Notation: p. 9 writes G = (V, E) and an edge as e = uv. The matrix rule
  on p. 11 reads "a_ij = 1 if v_i and v_j are adjacent, 0 otherwise", with
  a_ii = 0 and a_ij = a_ji. The book never writes e_ij; a rule with e_ij is
  the board's, and saying the book writes it is a misattribution.
- Length 0: Definitions 1.2.10 to 1.2.16 (pp. 21 to 23) do not say in
  words whether a walk of length 0 is allowed, but the book's usage
  assumes it: property 1 of distance on p. 23 (d(u, v) = 0 exactly when
  u = v) and the reflexivity of the relation alpha on p. 49. Never write
  that the book is silent on length 0 without this qualification. A paper
  that allows length 0 states it as its own convention and cites pp. 23
  and 49 as agreeing with it (Grinberg Definition 2.9.1(a) also has
  k >= 0).
- Definition 1.2.14 names a closed path of the book, that is a closed
  trail, "closed path or cycle" (փակ ճանապարհ or ցիկլ); the English cycle
  is the book's simple cycle, Definition 1.2.15.
- Definition 1.2.16 measures distance by a shortest path of the book, that
  is a shortest trail. A paper whose "path" is the course path either keeps
  the trail wording or defines distance as the least walk length and
  proves once that the two agree; it never writes "shortest path" with the
  word's meaning silently changed.
- Definition 2.1.1 (connected) uses the book's path, a trail. On p. 49 the
  book notes that alpha is reflexive, symmetric and transitive and gives no
  proof: write "notes", not "shows" or "proves".

## Other sources used for walk counting and connectivity

- Galway linear algebra notes, "1.1 The Adjacency Matrix"
  (maths.nuigalway.ie, file section1-1.pdf): the file carries no author
  name and no date. A name in the URL or the source id is not an
  authorship; call them the University of Galway notes. Cite printed
  pages throughout; the PDF page numbers differ. Theorem 1.1.3
  (printed p. 4) is walk counting, proved by induction on the last-but-one
  vertex; the same page says "The number of walks of length 2 from a
  vertex to itself is just the number of edges at that vertex, or the
  vertex degree." Report it as an equality, not as "related to".
- Gotti, MIT 18.211 Lecture 27 notes (no usable date): Proposition 2
  (p. 1) is walk counting, by induction; Proposition 3 (p. 2) is the
  (I_n + A)^(n-1) form of the test, proved with the binomial identity and
  the path bound n - 1.
- Grinberg, An introduction to graph theory (arXiv:2308.04512): works with
  multidigraphs, so his statements are more general than simple graphs.
  Walk is Definition 2.9.1(a), with k >= 0, and path is Definition
  2.9.1(c), both p. 36. Corollary 2.9.7
  (p. 39) covers u = v and gives the length bound that the textbook's
  Lemma 1.2.1 lacks; the bound n - 1 on a path's length is on p. 40.
  Proposition 2.9.10 (p. 42) is the equivalence of
  walks and paths only; it says nothing about trails, so cite it for the
  walk and path readings and prove the trail reading in the paper. His
  remark on circuits is about closed walks, not closed trails.
- Bai (Shuliang Bai), BIMSA lecture notes (2025-03-10): defines a path as
  having no repeated vertex. Theorem 1 (walk counting, p. 1) is stated for
  simple graphs, next to a passage saying it counts walks and not paths.
  Theorem 2 (p. 1) states the (I + A)^(n-1) form of the test; the proof
  sketch (p. 2) says "(I + A)^(n-1) aggregates all paths of length <= n - 1",
  which is incomplete. Bai has no sum form A + ... + A^(n-1): never
  attribute the sum test, or a sentence about it, to Bai.
- Lehman, Leighton, Meyer: states walk counting for digraphs. Reached only
  as metadata in the 2026-11-02 and 2026-11-06 runs; it supports nothing
  unless opened.
- Paramadevan and Sotheeswaran (2021), JSc EUSL 12(1), pp. 13-21. The
  paper never defines "path". Section 2.2 item 7 (p. 16) counts walks.
  Theorem 1 (p. 16) says the entry of A^l counts "different paths of
  length l": read as walks it is the walk-counting theorem, read with
  vertex-distinct paths it is false. Theorem 2 (p. 17) is the sum form of
  the test; its proof says "bij = number of different paths of length less
  than n from the vertex i to j" and passes from a non-zero entry to a
  path without the walk-to-path lemma. Theorem 3 (Section 3.1, p. 17)
  states that in a connected graph the distance is the least l with a
  non-zero (A^l)_ij; its proof reads a non-zero entry as a path. A paper
  that states the distance result credits Theorem 3 and proves it itself.

## When the paper says one of these sources is wrong

The brief's warning that A^k counts walks, not paths, is made by the
paper's own counterexample; a critique of the sources is extra and sits in
one discussion item, never beside a theorem statement. Quote each
statement verbatim with its page and restate it in the paper's notation.
Where the source defines the word the statement turns on (Bai's path),
refute the restatement with its own counterexample. Where it does not
(Paramadevan's path), give both readings, say which one holds, and refute
only the other; never call such a statement "false as written". Check each
counterexample against the paper's length-0 convention. For the board
graph (edges n1n2 and n2n3), verified on 2026-11-02 and 2026-11-06:

- Paramadevan Theorem 1, vertex-distinct reading: (A^2)_11 = 1, but no
  path of length 2 joins n1 to itself.
- Paramadevan sum statement, vertex-distinct reading: B = A + A^2 has
  B_22 = 2, but at most one path of length less than 3 joins n2 to itself
  (the path of length 0, if length 0 is allowed), so it fails under either
  length-0 convention. B_11 = 1 does not refute it when length 0 is
  allowed.
- Bai: R = (I + A)^2 has R_11 = 2, but only one path of length at most 2
  joins n1 to itself, the path of length 0.

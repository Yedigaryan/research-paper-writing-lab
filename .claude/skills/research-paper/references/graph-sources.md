# Verified facts about the sources of graph-theory papers

Read when the paper cites the course textbook `Grafneri_tesutyun.pdf` or
one of the sources listed below. Every fact here was checked against the
page image or the source text during the adjacency-walks-connectivity
paper (2026-10-27). They are locators and
attributions, not evidence: a claim still needs its own quote in the
evidence file, copied from the page you viewed.

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
  in the paper.

## Other sources used for walk counting and connectivity

- Galway linear algebra notes, "1.1 The Adjacency Matrix"
  (maths.nuigalway.ie, file section1-1.pdf): the file carries no author
  name and no date. A name in the URL or the source id is not an
  authorship; call them the University of Galway notes.
- Grinberg, An introduction to graph theory (arXiv:2308.04512): works with
  multidigraphs, so his statements are more general than simple graphs.
  Walk is Definition 2.9.1(a), path is Definition 2.9.1(c). Corollary 2.9.7
  (p. 39) covers u = v and gives the length bound that the textbook's
  Lemma 1.2.1 lacks; Proposition 2.9.10 (p. 42) is the walk, trail, path
  equivalence. His remark on circuits is about closed walks, not closed
  trails.
- Bai, BIMSA lecture notes (2025-03-10): Theorem 1 (walk counting) is
  stated for simple graphs. Theorem 2 states the (I + A)^(n-1) form of the
  test; its proof sketch says the power "aggregates all paths", which is
  incomplete.
- Lehman, Leighton, Meyer: states walk counting for digraphs.
- Paramadevan and Sotheeswaran (2021): Theorem 1 says the entry of A^l
  counts "different paths of length l", which is false as stated (it counts
  walks). Theorem 2 states the connectivity test; its proof passes from a
  non-zero entry to a path without the walk-to-path lemma. Cite it for the
  statement of the test only.

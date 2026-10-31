# Verified facts about the sources of graph-theory papers

Read when the paper cites the course textbook `Grafneri_tesutyun.pdf` or
one of the sources listed below. Every fact here was checked against the
page image or the source text by an evaluator during the
adjacency-walks-connectivity paper (2026-10-27 to 2026-10-31). They are
locators and attributions, not evidence: a claim still needs its own quote
in the evidence file, copied from the page you viewed.

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
  printed p. 21. Its examples use the seven edges v1v2, v1v3, v2v3, v2v4,
  v3v4, v3v5, v4v5; the figure also has the edge v1v5, which no example
  uses. Say the examples "use" these edges, not that they "force" them.
  The reader does not have the book, so list the edges in the text or draw
  the graph before the first example that uses it.
- A full-text search of the whole book finds the adjacency matrix only on
  a few pages (printed pp. 7, 11, 12, 34, and Kirchhoff's theorem, which
  evaluators placed on p. 60 in one run and p. 61 in another: view that
  page before printing the list), and finds no walk-counting theorem and
  no matrix test for connectivity. State that absence as the result of a
  full-text search, take both results from other sources, and prove them
  in the paper.

## Other sources used for walk counting and connectivity

- Galway linear algebra notes, "1.1 The Adjacency Matrix"
  (maths.nuigalway.ie, file section1-1.pdf): the file carries no author
  name and no date. A name in the URL or the source id is not an
  authorship; call them the University of Galway notes. The PDF has seven
  pages, numbered 2 to 8.
- Grinberg, An introduction to graph theory (arXiv:2308.04512): works with
  multidigraphs, so his statements are more general than simple graphs.
  Walk is Definition 2.9.1(a), path is Definition 2.9.1(c). Corollary 2.9.7
  (p. 39) covers u = v and gives the length bound that the textbook's
  Lemma 1.2.1 lacks. Proposition 2.9.10 (p. 42) is the equivalence of
  walks and paths only; it says nothing about trails, so cite it for the
  walk and path readings and prove the trail reading in the paper. His
  remark on circuits is about closed walks, not closed trails.
- Bai, BIMSA lecture notes (2025-03-10): Theorem 1 (walk counting) is
  stated for simple graphs. Theorem 2 states the (I + A)^(n-1) form of the
  test; its proof sketch says the power "aggregates all paths", which is
  incomplete.
- Lehman, Leighton, Meyer: states walk counting for digraphs.
- Paramadevan and Sotheeswaran (2021): a peer-reviewed journal article
  (JSc EUSL 12(1), pp. 13-21, DOI 10.4038/jsc.v12i1.29), not a web source,
  although module reports have called it one. Theorem 1 says the entry of
  A^l counts "different paths of length l", which is false as stated (it
  counts walks). Property 8 gives the degree as the off-diagonal entries
  plus twice the diagonal entry; it equals the row sum only because the
  diagonal is zero. Theorem 2 states the connectivity test; its proof
  passes from a non-zero entry to a path without the walk-to-path lemma.
  Cite it for the statement of the test only.
- Schost, breadth-first search slides (Winter 2026): slides 9 and 10 give
  the correctness statement (a walk from s to v exists if and only if v is
  discovered) and the O(n + m) bound for adjacency lists. Slide 3 only
  defines the matrix representation and slide 6 assumes adjacency lists.
  No slide gives the cost of the search when the input is the adjacency
  matrix; any such count is the paper's own estimate and is labelled so.

## Board photos (whiteboard-1.jpg, whiteboard-2.jpg)

- Both lines of the A_ij definition write the condition word in Armenian
  ("if"). A transcription that claims to keep the board's wording says so.
- A small scratched-out mark under vertex 1 appears on both photos; list
  it as unreadable rather than omitting it.

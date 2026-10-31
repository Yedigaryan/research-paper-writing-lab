# Deliverable `inv`

Compiled PDF, 32 pages, rendered with pdftotext -layout.

```
    Walks, Paths and Connectivity from the Adjacency Matrix:
       A Study Note on (Ak )ij and the Connectivity Test

         Study note prepared from a lecture whiteboard and the course textbook


                                                 Abstract
          A graph with N vertices can be stored as an N × N table of zeros and ones, its adjacency
      matrix A. This note answers three questions about that table. First, the entry in row i and
      column j of the matrix power Ak is the number of walks of length k from vertex ni to vertex
      nj ; it counts walks, not paths [2, 1]. Second, a graph with N ≥ 2 vertices is connected if
      and only if every entry off the diagonal of A + A2 + · · · + AN −1 is positive, or equivalently if
      and only if (I + A)N −1 has no zero entry. Third, a path between ni and nj is a walk from ni
      to nj with no repeated vertex, which is the course textbook’s simple path. Both theorems
      are proved in full, because the course textbook does not state them in the pages checked [9].
      Every matrix in the examples was computed by script.


Contents
1 Introduction                                                                                             2
  1.1 The question and where it came from . . . . . . . . . . . . . . . . . . . . . . . .                  2
  1.2 The story used throughout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                3
  1.3 What the paper shows . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .               3
  1.4 Conventions, assumptions, and kinds of statement . . . . . . . . . . . . . . . . .                   4
  1.5 Organization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .             5

2 Background: graphs, walks, and paths                                                                      5
  2.1 Graphs, adjacency, and degree . . . . . . . . . . . . . . . . . . . . . . . . . . . .                 5
  2.2 The adjacency matrix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                6
  2.3 Walks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .             7
  2.4 Cycles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .            9
  2.5 Three naming conventions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .               10
  2.6 Distance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .           10
  2.7 Every walk contains a path . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .               11

3 Q1: what the entry of a power of A counts                                                                12
  3.1 Matrix products and powers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .               12
  3.2 The walk-counting theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                13
  3.3 Consequences . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .             14
  3.4 Walks are not paths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .              15
  3.5 The answer to Q1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .               15

4 Q2: deciding connectivity from the matrix                                                                15
  4.1 Connected graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .             15
  4.2 Components . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .             16
  4.3 The sum used by the test . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .               16
  4.4 The test and its proof . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .             17
  4.5 The test as a procedure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .              18

                                                      1
    4.6    Why N − 1 powers are enough and N − 2 are not . . . . . . . . . . . . . . . . . .        19
    4.7    Breadth-first search, for comparison . . . . . . . . . . . . . . . . . . . . . . . . .   19
    4.8    The answer to Q2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   20

5 Q3: the definition of a path between ni and nj                                                    20

6 Worked examples                                                                                   20
  6.1 The board graph and its powers . . . . . . . . . . . . . . . . . . . . . . . . . . . .        21
  6.2 A connected example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       22
  6.3 A disconnected example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        22
  6.4 The bound N − 1 is needed . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         22
  6.5 Exhaustive agreement with breadth-first search . . . . . . . . . . . . . . . . . . .          23

7 Discussion: limits, disagreements, and cost                                                       23
  7.1 What is proved and what is only checked . . . . . . . . . . . . . . . . . . . . . .           23
  7.2 Conventions that change the words but not the mathematics . . . . . . . . . . .               24
  7.3 Where the sources disagree . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        24
  7.4 Cost of the matrix test and of breadth-first search . . . . . . . . . . . . . . . . .         24
  7.5 Limits and open questions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       24

8 Conclusion                                                                                        25

A Derivations and checks                                                                            26
  A.1 The distance properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       26
  A.2 The counterexample to “entries count paths” . . . . . . . . . . . . . . . . . . . .           26
  A.3 The chain of premises for the connectivity test . . . . . . . . . . . . . . . . . . .         27
  A.4 Proof of the I + A form . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       27
  A.5 Cross-checks by script . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      28

B The textbook’s terms and numbers                                                                  28

C The whiteboard photographs                                                                        29

D Reproducibility                                                                                   30


1     Introduction
1.1       The question and where it came from
A lecture whiteboard shows a small graph, its table of zeros and ones, and two questions about
that table [4, 5]. The board states the problem as follows: a graph with N nodes is given
through its adjacency matrix A; (1) what does the entry in row i and column j of a power of
A represent, and (2) how does one know whether the graph is connected [4, 5]. The board also
gives a definition of a connected graph, which uses the word “path” [4, 5]. The assignment text
added a third question: what is the definition of a path between two vertices ni and nj . That
third question comes from the assignment, not from the board. The paper therefore answers
three questions.

 Q1. What does the entry (Ak )ij of the k-th power of the adjacency matrix represent?

 Q2. How can one decide from A alone whether the graph is connected?

 Q3. What is the definition of a path between the vertices ni and nj ?



                                                   2
    Reading of the board. In question 1 the board puts a small mark above the letter A. In both
photographs the mark looks like a small n or a pair of quotation marks, not clearly a k [4, 5].
This paper reads the mark as an exponent k, because the assignment text asks about Ak . This
is an interpretation, and it is qualified: the board does not settle it. It does not change the
mathematics, because Theorem 3.5 holds for every positive whole exponent, whatever letter is
used.

1.2   The story used throughout
Every explanation marked “In plain words” uses one story. A village has a number of houses.
Each house is a point. Each road joins exactly two different houses. Every road can be driven
in both directions. No road leads from a house back to itself. No two roads join the same pair
of houses. A trip is a list of houses, one after another, where each house is at the other end of a
road from the house before. A trip may pass the same house twice and may drive the same road
twice. A clean route is a trip that never visits the same house twice. The village of the board
has three houses in a row: a road from the first house to the second, and a road from the second
house to the third. The first and third houses have no road between them. The mathematics
below uses the same village; the terms are matched in Table 1.

Table 1: The story and the mathematics. The right column names the definitions that are
introduced in Section 2.
                Story            Mathematics
                 house                  vertex
                 road                   edge
                 village                simple undirected graph (Definition 2.1)
                 trip                   walk (Definition 2.18)
                 clean route            path (Definition 2.31)
                 table of roads         adjacency matrix (Definition 2.13)
                 village in one piece   connected graph (Definition 4.1)



1.3   What the paper shows
The answers, stated briefly and proved later, are these.

  • Q1 (Section 3). For k ≥ 1, the entry (Ak )ij is the number of walks of length k from ni
    to nj . The statement appears in standard lecture notes [2, 1]; the proof in this paper
    is written out in full. The entry counts walks, not paths, and Proposition 3.11 gives a
    counterexample. One web source states the theorem with the word “paths”, which is
    wrong for the usual meanings of that word [7]; this is discussed in Section 7.3.
  • Q2 (Section 4). For N ≥ 2 vertices the graph is connected if and only if every entry off the
    diagonal of A + A2 + · · · + AN −1 is positive. A published note states this test and lecture
    notes state its second form, and both prove it loosely [7, 1]. The proof in this paper is
    complete (derived here).
  • Q3 (Section 5). A path between ni and nj is a walk from ni to nj with no repeated vertex.
    This is the course textbook’s simple path, Definition 1.2.13 [9, p. 22].

   The course textbook states neither the walk-counting theorem nor the matrix test in the
pages that were checked, and a search of the whole book found no such theorem or test; the
absence is qualified because the rest of the book was not read page by page [9]. Both results are
therefore proved here, and the text says so each time.

                                                3
1.4     Conventions, assumptions, and kinds of statement
Assumptions. The graph is finite, simple, and undirected. This is the setting of the assign-
ment, and it agrees with the symmetric matrix with zero diagonal on the board [4, 5]. The
textbook’s graphs are of this kind too [9, p. 9]. Directed graphs and graphs with repeated edges
are not treated (Section 7.5).

The example graph. The board shows a drawing of three vertices and, beside it, a matrix
with rows (0 1 0), (1 0 1), (0 1 0). The matrix encodes the two edges n1 n2 and n2 n3 only. The
drawing shows three lines: one from 1 to 2 with an arrowhead at 2, one from 1 to 3, and one
from 2 to 3 [4, 5]. So the drawing has an edge 1–3 that the matrix lacks, and an arrowhead
that a symmetric matrix does not support. The problem statement says that the graph is given
through its adjacency matrix [4, 5]. This paper therefore takes the matrix as the example graph,
calls it the board graph, and treats the extra line and the arrowhead as a mismatch that it reports
and does not resolve. When a graph with a cycle is needed, the drawing’s triangle is used and
is labelled as the triangle.

Notation. Table 2 fixes the letters. The board writes (G, V ) for the graph and eij ∈ V in its
matrix definition, where its V is the edge set; the textbook writes G = (V, E) with E the edge
set [4, 5, 9]. This is a difference of notation only. The board names the vertices ni ; the textbook
names them vi [4, 5, 9]. This paper uses the board’s ni .

                              Table 2: Notation used in this paper.
  Symbol                 Meaning
  G = (V, E)             a finite simple undirected graph with vertex set V and edge set E
                         (textbook letters)
  N                      the number of vertices, N = |V | (the board writes |G| = N )
  n1 , . . . , n N       the vertices (the board’s names; the textbook’s vi )
  uv, eij                the edge between u and v; the edge between ni and nj
  A, Aij                 the adjacency matrix and its entry in row i, column j
  Ak , (Ak )ij           the k-th power of A and its entry in row i, column j
  I                      the N × N identity matrix (ones on the diagonal, zeros elsewhere)
  k                      the length of a walk, or an exponent; a positive whole number unless
                         stated
  S                      the sum A + A2 + · · · + AN −1 (Definition 4.9)
  deg(ni )               the degree of ni (Definition 2.9)
  d(u, v)                the distance between u and v (Definition 2.41)



The word “path”. The word has more than one meaning in the sources. The textbook’s own
“path” (Definition 1.2.12) allows a repeated vertex, and it calls a path without a repeated vertex
a “simple path” (Definition 1.2.13) [9, p. 22]. Two English texts call the second kind a path and
the first kind a trail [3, 8]. The assignment states that in the course a path has no repeated
vertex; that statement comes from the assignment text and not from a file, so it is recorded as
an interpretation. This paper uses path for a walk without repeated vertices and trail for the
textbook’s Definition 1.2.12, and Table 3 gives the three conventions side by side.

Kinds of statement. A statement with a citation is taken from the cited source. A statement
marked derived is proved or computed in this paper; every number in such a statement was
computed by script (Appendix D). Statements marked interpretation, estimate, or open are


                                                 4
labelled in the same way, and the textbook’s definition numbers are always written “textbook
Definition 1.2.10” and so on, so that they cannot be mistaken for the numbers of this paper.

1.5   Organization
Section 2 builds the prerequisites in the textbook’s order: graph, adjacency, the adjacency
matrix, walk, trail, path, cycle, and distance, with the lemma that every walk contains a path.
Section 3 answers Q1, Section 4 answers Q2, and Section 5 answers Q3. Section 6 works the
board graph and three further graphs through in full. Section 7 states the limits, and Section 8
gives the direct answers. The appendices hold longer derivations, the textbook’s terms, the
transcription of the photographs, and the scripts.


2     Background: graphs, walks, and paths
Throughout, let G = (V, E) be a finite simple undirected graph with V = {n1 , . . . , nN }, let
u, v be vertices and let e, e′ be edges, as fixed in Table 2. The definitions follow the textbook’s
build order [9]. Where the textbook has a number for a definition, the number is quoted as
“textbook Definition x.y.z”. After each definition come a remark on what it allows and forbids,
an example, and a non-example.

2.1   Graphs, adjacency, and degree

In plain words. A village has a list of houses and a list of roads. A road always joins two
different houses. No two roads join the same pair of houses. Roads have no direction. The
village is small enough that we can count its houses.

Definition 2.1 (Simple undirected graph; textbook Definition 1.1.1). A simple undirected graph
is a pair G = (V, E) where V is a finite nonempty set, whose elements are the vertices, and E is
a set of unordered pairs of distinct elements of V , the edges [9, p. 9].

Remark 2.2. The definition forbids a loop, because an edge is a pair of distinct vertices. It
forbids a repeated edge, because E is a set, so a pair occurs at most once. It forbids direction,
because the pair is unordered, so ni nj and nj ni are the same edge. It allows a vertex that lies
on no edge, and any finite number of vertices.

Example 2.3. V = {n1 , n2 , n3 } and E = {n1 n2 , n2 n3 }. This is the board graph: three houses
in a row.

Non-example 2.4. Two vertices n1 , n2 joined by two roads, or a road from n1 to n1 . The first
repeats an edge and the second is a loop, so neither is a simple graph.

In plain words. Two houses are neighbours when one road joins them directly. Being neigh-
bours says nothing about longer trips.

Definition 2.5 (Adjacent vertices; textbook Definition 1.1.4). Vertices u and v are adjacent if
uv ∈ E; then u is a neighbour of v [9, p. 11].

Remark 2.6. Adjacency is symmetric, and no vertex is adjacent to itself, because there are no
loops. It describes direct roads only, not longer connections.

Example 2.7. n1 and n2 are adjacent in the board graph.

Non-example 2.8. n1 and n3 are not adjacent in the board graph, although the trip n1 , n2 , n3
joins them.

                                                5
In plain words. The degree of a house is the number of roads that touch it. A busy house has
a large degree.

Definition 2.9 (Degree). The degree deg(ni ) of a vertex ni is the number of edges that contain
ni .

    This is the usual meaning of the word, stated for example as “the number of edges at that
vertex, or the vertex degree” [2]. The textbook’s own definition of degree was not read, so no
textbook number is given.

Remark 2.10. In a simple graph the degree is also the number of neighbours, because each
neighbour is joined by exactly one edge.

Example 2.11. In the board graph deg(n1 ) = 1, deg(n2 ) = 2, and deg(n3 ) = 1.

Non-example 2.12. deg(n1 ) is not 2 in the board graph, although two other vertices can be
reached from n1 . Only roads at n1 count, and n3 is reached by passing through n2 .

2.2   The adjacency matrix

In plain words. Make a square table with one row and one column for every house. Write
a one where the row house and the column house share a road. Write a zero everywhere else.
This table describes the whole village.
    A matrix is a rectangular table of numbers; Aij is the number in row i and column j. The
transpose of a matrix swaps its rows and columns, and a matrix is symmetric if it equals its
transpose, that is, if Aij = Aji for all i, j.

Definition 2.13 (Adjacency matrix; textbook, printed p. 11, after Definition 1.1.6). The adja-
cency matrix of G is the N × N matrix A with Aij = 1 if ni and nj are adjacent, and Aij = 0
otherwise [9, p. 11].

    The textbook’s definition number for this matrix was not recorded, so only its page is given.
The board writes the same rule as Aij = 1 if eij ∈ V and Aij = 0 if eij ∈
                                                                        / V , with its V standing
for the edge set [4, 5].

Remark 2.14. The definition allows only the entries 0 and 1. It depends on how the vertices
are numbered: renumbering permutes rows and columns together.

                                    0 1 0
                                             

Example 2.15. The board matrix 1 0 1 is the adjacency matrix of the board graph of
                                          
                                    0 1 0
Example 2.3: A12 = A21 = 1, A23 = A32 = 1, and every other entry is 0.

Non-example 2.16. The matrix with rows (0 1 0), (0 0 1), (0 1 0) is not the adjacency matrix
of a simple undirected graph, because A12 = 1 but A21 = 0. A matrix with a 1 on the diagonal
(a loop) or an entry 2 (a double road) is not one either.

In plain words. The table has some easy features. It looks the same when flipped over its
diagonal. The diagonal holds only zeros. Adding up one row tells how many roads touch that
house.

Proposition 2.17 (Properties of A). For the adjacency matrix A of a simple undirected graph:

  1. every entry is 0 or 1;


                                               6
   2. A is symmetric: Aij = Aji ;

   3. the diagonal is zero: Aii = 0;

   4. the sum of row i, and of column i, equals deg(ni );

   5. the sum of all entries equals 2|E|;

   6. conversely, every N × N matrix of zeros and ones that is symmetric with zero diagonal is
      the adjacency matrix of some simple graph with numbered vertices.

    Items 1–3 and 6 are stated in the textbook [9, pp. 11–12], and items 2, 3 and 6 also appear
in other notes [2, 7]. Items 4 and 5 are derived here; a published note states item 4 in a form
that allows loops [7].

Proof. Items 1–3 follow from Definition 2.13, because adjacency is symmetric and no vertex is
adjacent to itself. For item 4, the sum of row i is the number of j with Aij = 1, which is the
number of neighbours of ni . Each neighbour is joined to ni by exactly one edge, since there are
no repeated edges, and no edge at ni joins it to itself, since there are no loops. So the number
of neighbours equals the number of edges at ni , which is deg(ni ). Column i gives the same
number by symmetry. For item 5, add item 4 over all i. Each edge ni nj adds one to deg(ni )
and one to deg(nj ), so it is counted twice. For item 6, join ni and nj exactly when the entry is
1. Symmetry makes this a set of unordered pairs, and the zero diagonal excludes loops.

   For the board matrix the row sums are 1, 2, 1, the column sums are 1, 2, 1, and the total is
4 = 2|E| with |E| = 2 (script, Appendix D).

2.3    Walks

In plain words. A walk is a trip along the roads. Start at a house and move to a neighbour,
again and again. You may pass the same house twice. You may drive the same road twice. The
length of a trip is the number of roads you drove. If you drive a road twice, you count it twice.
Staying at home is also a trip, and its length is zero.

Definition 2.18 (Walk; textbook Definition 1.2.10). A walk of length k from u0 to uk , also called
a (u0 , uk )-walk, is a sequence u0 , e1 , u1 , . . . , uk−1 , ek , uk of vertices and edges with ei = ui−1 ui
for 1 ≤ i ≤ k [9, p. 21]. The length of the walk is k, the number of edges, each edge counted as
many times as it occurs [9, p. 22].

Remark 2.19. A walk allows repeated vertices and repeated edges [9, p. 22]. It forbids one
thing only: two consecutive vertices that are not joined by an edge. A walk with k edges lists
k + 1 vertices. The textbook does not say in so many words that k = 0 is allowed. This paper
reads k = 0 as allowed, because the textbook’s property d(u, u) = 0 of distance needs a path of
length 0 from u to u [9, p. 23], and another text has a length-0 walk as an example [3, Example
2.9.2]. This is an interpretation and is qualified.

Remark 2.20 (A walk is its list of vertices). In a simple graph there is at most one edge between
two vertices, so the edge ei = ui−1 ui is forced by its two ends. Hence a walk of length k from
ni to nj is the same thing as a sequence w0 , w1 , . . . , wk of vertices with w0 = ni , wk = nj and
wt−1 , wt adjacent for each t from 1 to k (derived). Two walks are different exactly when these
sequences differ at some position. From here on a walk is written by its vertices. For a graph
with repeated edges this step would fail, which is one reason why “simple” matters.




                                                      7
Example 2.21. In the board graph the sequence n1 , n2 , n3 , n2 , written 1, 2, 3, 2, is a walk of
length 3 from n1 to n2 . So is 1, 2, 1, 2, 3, of length 4, from n1 to n3 ; it repeats the vertices 1
and 2 and the edge n1 n2 . The textbook’s example is v1 , v3 , v2 , v4 , v3 , v2 , v4 , v3 , v5 in its graph of
Fig. 1.2.5, a walk of length 8 [9, p. 22].
Non-example 2.22. 1, 3 is not a walk of the board graph, because n1 and n3 are not adjacent.
(It would be a walk of the drawing’s triangle.) The textbook’s non-example is v3 , v1 , v4 , v2 , v3 , v5
[9, p. 22].

The textbook graph. For the textbook’s examples the paper needs a graph with a cycle, and
the board graph has none. The textbook’s Fig. 1.2.5 shows a graph on five vertices v1 , . . . , v5 .
The textbook’s own examples force the seven edges v1 v2 , v1 v3 , v2 v3 , v2 v4 , v3 v4 , v3 v5 , v4 v5 [9,
p. 22]. Only these seven edges are used below, and the graph they form is called the textbook
graph; nothing depends on reading other lines of the figure. Its vertices are written 1, . . . , 5 in
the sequences below.
In plain words. A trip is closed when it ends at the house where it began. That is the only
new rule. The trip may still pass houses and roads many times.

Definition 2.23 (Closed walk; textbook Definition 1.2.11). A (u0 , uk )-walk is closed if u0 = uk
[9, p. 22].
Remark 2.24. A closed walk allows everything that a walk allows and forbids only a different
start and end. A walk of length 0 is closed. In a simple graph no closed walk has length 1, since
that would be a loop, and a closed walk of length 2 has the form u, w, u and uses one edge twice
(derived).
Example 2.25. In the board graph 2, 1, 2 is a closed walk of length 2, and so is 2, 3, 2, 1, 2 of
length 4.
Non-example 2.26. 1, 2, 3 is not closed in the board graph: it starts at 1 and ends at 3.

In plain words. Now add one rule. Never drive the same road twice. You may still pass the
same house twice, if you come back by a different road. English books call such a trip a trail.
Our textbook calls it a path. This paper says trail, so that the word path can keep one meaning.

Definition 2.27 (Trail; textbook Definition 1.2.12, which names it “path”). A (u0 , uk )-walk is
a trail if its edges u0 u1 , . . . , uk−1 uk are pairwise distinct [9, p. 22].
    The textbook calls this object a path and writes |P | for its length [9, p. 22]; English usage
calls it a trail [3, 8]. When the paper needs to point at the textbook’s word it writes “textbook
path”.
Remark 2.28. A trail allows repeated vertices and forbids repeated edges. A vertex can recur
in a trail only if the trip left it by one road and came back by another, so the trip has gone round
a loop of the graph. In the board graph every trail is also a path in the sense of Definition 2.31
for every length from 0 to 4, and the board graph has no closed trail of positive length (script,
Appendix D). So the board graph cannot show the difference between a trail and a path, and
the textbook graph is used for that (derived, checked by script for lengths up to 4).
Example 2.29. In the textbook graph, 1, 3, 2, 4, 3, 5 is a trail: its edges v1 v3 , v3 v2 , v2 v4 , v4 v3 , v3 v5
are distinct, although the vertex v3 occurs twice [9, p. 22].
Non-example 2.30. In the textbook graph, 1, 3, 2, 4, 3, 2, 4, 3, 5 is a walk but not a trail, because
the edge v3 v2 occurs twice [9, p. 22]. In the board graph 1, 2, 1, 2, 3 is not a trail, because the
edge n1 n2 occurs twice.

                                                       8
In plain words. Now add a stronger rule. Never visit the same house twice. Then you also
never drive the same road twice. A trip like this goes straight from start to end without any loop.
Our course calls it a path.

Definition 2.31 (Path; textbook Definition 1.2.13, which names it “simple path”). A (u0 , uk )-
walk is a path if all its vertices u0 , . . . , uk are pairwise distinct [9, p. 22].

    The textbook calls this a simple path and writes Pn for the simple path on n vertices [9,
p. 22]. English texts call it a path [3, 8]. The textbook defines it as a trail with distinct vertices;
Proposition 2.35 shows that distinct vertices already give distinct edges, so the two ways of
saying it agree. That the course uses the word “path” in this sense comes from the assignment
text; the board does not say which meaning it uses. So this reading is an interpretation, and it
is qualified [9, p. 22].

Remark 2.32. A path forbids repeated vertices, and therefore repeated edges. It allows length
0 (a single vertex) and length 1 (a single edge). It does not allow a closed path of positive length,
because the first and last vertices would be equal.

Example 2.33. In the board graph 1, 2, 3 is a path of length 2 from n1 to n3 . The textbook’s
example is v1 , v3 , v4 , v5 in its graph [9, p. 22].

Non-example 2.34. In the board graph 1, 2, 3, 2 is a walk but not a path, because the vertex
2 occurs twice. In the textbook graph 1, 3, 2, 4, 3, 5 is a trail but not a path, because v3 occurs
twice [9, p. 22].

In plain words. There is a quick reason why a clean route never uses a road twice. Look at
any two roads on the route. The later road ends at a house that comes after both houses of the
earlier road. That house is new, so the two roads differ.

Proposition 2.35. In a simple graph a walk with pairwise distinct vertices has pairwise distinct
edges. Hence every path is a trail.

   This is stated as an exercise in one text [3, Exercise 2.9]; the proof here is derived.

Proof. Let u0 , . . . , uk have distinct vertices and take two steps with indices a < b, that is, the
edges ua−1 ua and ub−1 ub . The vertex ub has an index larger than a, so it differs from both ua
and ua−1 . But ub is an end of the second edge and is not an end of the first. So the two edges
are different.

2.4   Cycles

In plain words. A cycle is a closed trip that never drives the same road twice. Our textbook
lets such a trip pass a house twice on the way. A simple cycle is stricter. It passes no house
twice, except the start, which is also the end. A simple cycle is a ring of houses with a road
between each pair of neighbours.

Definition 2.36 (Cycle; textbook Definition 1.2.14). A cycle (the textbook also says closed
path) is a closed trail: a (u0 , uk )-walk with u0 = uk and pairwise distinct edges [9, p. 22].

Definition 2.37 (Simple cycle; textbook Definition 1.2.15). A cycle is simple if only its first
and last vertices repeat [9, p. 22]. The textbook writes Cn for the simple cycle on n ≥ 3 vertices
[9, p. 22].



                                                  9
Remark 2.38. A cycle allows repeated vertices (a figure eight is a cycle, by the definition;
derived) and forbids repeated edges and open walks. A simple cycle forbids any repeated vertex
other than the closing one. In a simple graph a closed trail cannot have length 1 or 2, and
this paper does not count a closed walk of length 0 as a cycle; the textbook is silent on that
case (interpretation, qualified). English usage differs: one text defines a cycle as a closed walk
with k ≥ 3 and distinct vertices w0 , . . . , wk−1 , which is the textbook’s simple cycle [3, Definition
2.10.1(b)]. This paper follows the textbook for “cycle” and writes “simple cycle” where English
texts write “cycle”. Cycles are not needed for the main results; they are given because the
textbook’s list of definitions includes them.

Example 2.39. The drawing’s triangle has the edges 12, 13, 23, and 1, 2, 3, 1 is a simple cycle
of length 3 in it. The textbook’s example of a simple cycle is v1 , v3 , v4 , v2 , v1 [9, p. 22]. The
textbook’s walk v3 , v2 , v1 , v3 , v5 , v4 , v3 is a cycle in the sense of Definition 2.36 (closed, six distinct
edges) but not a simple one, since v3 occurs three times [9, p. 22].

Non-example 2.40. In the board graph 1, 2, 1 is a closed walk but not a cycle, because the
edge n1 n2 is used twice. In fact the board graph has no cycle at all: among its closed walks of
lengths 1 to 6, none has distinct edges (script, Appendix D).

2.5    Three naming conventions

In plain words. Different books use different names for the same kinds of trips. Here is one
table that puts the names side by side. Our paper follows the last column.
    Table 3 lists the same properties under the course, textbook, and English names. The course
column is the assignment’s statement for “path” only; for “cycle” the course convention is not
stated, so the paper follows the textbook.

Table 3: Naming conventions. “Textbook” gives the textbook’s word and definition number [9];
“English” gives the usage of [3, 8].
Property of the walk                Textbook                       English                   This paper
any steps along edges               walk (1.2.10)                  walk                      walk
first vertex equals last            closed walk (1.2.11)           closed walk               closed walk
no repeated edge; vertices may      “path” (1.2.12)                trail                     trail
repeat
no repeated vertex (so no re-       “simple path” (1.2.13)         path                      path
peated edge)
closed, no repeated edge; ver-      “cycle” (1.2.14)               closed trail              cycle
tices may repeat
closed, only first and last ver-    “simple cycle” (1.2.15)        cycle                     simple cycle
tex equal, k ≥ 3

    So the word “path” has three meanings across the sources: the textbook’s Definition 1.2.12,
the textbook’s Definition 1.2.13 under the name “simple path”, and the English usage. Another
text records that some authors use “path” for repeated vertices and “simple path” for distinct
vertices, which is the textbook’s pattern [8]. So the course convention is one of at least two in
use.

2.6    Distance

In plain words. The distance between two houses is the number of roads on the shortest trip
between them. If no trip exists, we say the distance is infinite. A house is at distance zero from


                                                       10
itself. The distance there equals the distance back, because any trip can be driven backwards.
Going by a third house is never shorter than the shortest trip.

Definition 2.41 (Distance; textbook Definition 1.2.16). The distance d(u, v) between vertices
u and v is the length of a shortest (u, v)-path if at least one exists, and +∞ otherwise [9,
pp. 22–23].

   The textbook’s “path” here is its Definition 1.2.12, a trail. The definition does not depend
on whether one reads trail or path, because the shortest walk, the shortest trail, and the shortest
path between two vertices have the same length (Proposition A.1, derived). The textbook lists
three properties, for all vertices u, v, w [9, p. 23].

  1. d(u, v) ≥ 0, and d(u, v) = 0 if and only if u = v;

  2. d(u, v) = d(v, u);

  3. d(u, v) ≤ d(u, w) + d(w, v).

So when every two vertices are joined by a path, the pair (V, d) is a metric space [9, p. 23].
The textbook states these properties without proof; they are derived from the definition in
Appendix A.1.

Remark 2.42. The value +∞ is not a whole number; it is how a missing path shows up. The
definition forbids negative values and any value that is not the length of an actual trip.

Example 2.43. In the board graph d(n1 , n2 ) = 1, d(n2 , n3 ) = 1, d(n1 , n3 ) = 2 and d(ni , ni ) = 0
for each i (script). The walk 1, 2, 1, 2, 3 has length 4, but the distance is the shortest length,
which is 2.

Non-example 2.44. 4 is not the distance from n1 to n3 in the board graph, even though a
walk of length 4 exists. Also, in the graph with vertices n1 , n2 , n3 and the single edge n1 n2 , the
distance d(n1 , n3 ) is not a number: it is +∞ (script).

2.7   Every walk contains a path

In plain words. Suppose you can drive from one house to another. Then you can do it without
visiting any house twice. Look at your trip. If it passes some house twice, you went round a
loop. Cut the loop out. What is left is still a trip from the same start to the same end. It is
shorter. Keep cutting until no house is repeated. The trip that remains is never longer than the
first one.

Lemma 2.45 (Walk contains path; textbook Lemma 1.2.1 for u ̸= v). Let u and v be vertices
of a simple graph, equal or not. If there is a (u, v)-walk of length k, then there is a (u, v)-path
of length at most k, and all its vertices and edges are vertices and edges of the walk.

    The textbook states the lemma only for u ̸= v and says that from any (u, v)-walk one can
extract a simple (u, v)-path, without a bound on the length [9, p. 23]. Its proof is by induction
on the length of the walk [9, p. 23], and the length bound follows from that proof. Another text
states the version with u = v allowed and with the bound [3, Corollary 2.9.7]. The case u = v
is needed here because a closed walk such as 2, 1, 2 has u = v; the path it contains is the single
vertex, of length 0. The proof below is the paper’s own (derived).

Proof. We prove by strong induction on k the statement S(k): every (u, v)-walk of length k, for
any vertices u, v, contains a (u, v)-path of length at most k.


                                                 11
    Base case, k = 0. A walk of length 0 is a single vertex u, so v = u. A single vertex has no
repeated vertex, so the walk is itself a path, of length 0 ≤ 0.
    Induction hypothesis. Let k ≥ 1 and assume S(m) for every m < k.
    Step. Let u0 , u1 , . . . , uk be a (u, v)-walk, so u0 = u and uk = v. If its vertices are pairwise
distinct, it is a path of length k ≤ k and we are done. Otherwise some vertex occurs twice, so
there are indices i < j with ui = uj . Form the sequence W ′ = u0 , . . . , ui , uj+1 , . . . , uk ; if j = k
nothing follows ui . We check that W ′ is a (u, v)-walk. (a) It starts at u0 = u. (b) It ends at
v: if j < k its last vertex is uk = v, and if j = k its last vertex is ui = uj = uk = v. (c)
Consecutive vertices are adjacent: before the cut and after the join they are consecutive vertices
of the old walk, and the join pair (ui , uj+1 ) = (uj , uj+1 ) is a step of the old walk. The length of
W ′ is i + (k − j), which is less than k because i < j. By the induction hypothesis W ′ contains
a (u, v)-path of length at most |W ′ | < k, hence at most k. Every vertex and edge of that path
is one of W ′ , hence one of the old walk.

    Why the proof is valid. Each cut removes at least one step, so the length drops by at least
one, and a walk that cannot be cut has no repeated vertex, which is the definition of a path.
As a trace, the textbook’s walk 1, 3, 2, 4, 3, 2, 4, 3, 5 of length 8 has u1 = u4 = 3; cutting gives
1, 3, 2, 4, 3, 5 of length 5; cutting again gives 1, 3, 5 of length 2, which is a path (script). In the
board graph 1, 2, 1, 2, 3 cuts to 1, 2, 3, and the closed walk 2, 1, 2 cuts to the single vertex 2.
In plain words. A clean route can have at most one road fewer than the number of houses. It
visits each house at most once. So a clean route cannot be very long. If any trip exists, a short
trip exists too.

Corollary 2.46 (Length bound). In a graph with N vertices every path has at most N − 1
edges. Hence if some walk joins u and v, then some walk of length at most N − 1 joins them.

Proof. A path of length k lists k + 1 pairwise distinct vertices, and there are only N vertices,
so k + 1 ≤ N . For the second part, apply Lemma 2.45: the path inside the walk has length at
most that of the walk and, by the first part, at most N − 1.

    The same argument is given in another text [3, Section 2.9.4]. In the board graph N = 3,
so a path has at most 2 edges, and the longest path has 2 edges (script).


3     Q1: what the entry of a power of A counts
3.1    Matrix products and powers

In plain words. To multiply two tables of the same size, take a row of the first and a column
of the second. Multiply them place by place, then add. That gives one number of the new table.
To raise a table to a power, multiply it by itself again and again.

Definition 3.1 (Matrix product and power). The product of two N × N matrices X and Y is
the matrix XY with (XY )ij = N r=1 Xir Yrj . The powers of A are A = A and A = A
                                                                  1         k    k−1 A for
                            P

k ≥ 2.

   The exponent 0 is not used for A in this section; by the usual convention A0 = I, the identity
matrix, which corresponds to one walk of length 0 from a vertex to itself [3]. It appears only in
Section 4, in (I + A)N −1 .

Remark 3.2. The definition allows a sum over all N vertices r, whether or not r is a neighbour.
It forbids multiplying entry by entry: the product is not the table of products of matching entries.



                                                     12
                                               0 1 0
                                                        

Example 3.3. For the board matrix A = 1 0 1 the entry (A2 )11 = A11 A11 + A12 A21 +
                                                    
                                               0 1 0
A13 A31 = 0 · 0 + 1 · 1 + 0 · 0 = 1 (script).
Non-example 3.4. Squaring every entry of A separately gives back A, since the entries are 0
and 1. That is not A2 : the matrix product has (A2 )22 = 1 · 1 + 0 · 0 + 1 · 1 = 2 (script), where
entry-wise squaring gives A222 = 0.

3.2   The walk-counting theorem

In plain words. Take the table of roads and multiply it by itself. Each number in the new
table counts trips of two roads. The trips run from the row house to the column house. Multiply
again, and you count trips of three roads. The count includes trips that turn back. So the table
counts trips, not clean routes.

Theorem 3.5 (Walk counting). Let A be the adjacency matrix of a simple undirected graph
with vertices n1 , . . . , nN and let k ≥ 1 be a whole number. Then (Ak )ij is the number of walks
of length k from ni to nj , for all i, j.
    The theorem is a standard one. It is stated and proved for simple undirected graphs in lecture
notes [2, Theorem 1.1.3], and for digraphs and multidigraphs, of which the simple undirected
graph is the symmetric case, in two other texts [3, Theorem 4.5.10], [6, Corollary 9.3.3]; a fourth
set of notes states it too [1, Theorem 1]. The course textbook does not state it in the pages
checked, so it is proved here (qualified, as said in Section 1). The proof below follows the route
that the standard notes use: induction on k, sorting the walks by their second-last vertex [2, 3].
Remark 3.6. The theorem allows i = j (closed walks), and it counts every walk once, with
repeats of vertices and edges permitted. It forbids reading the number as a count of paths
(Proposition 3.11).
Example 3.7. For the board graph, (A2 )13 = 1, the walk 1, 2, 3 (Section 6).
Non-example 3.8. (A2 )12 = 0 in the board graph. This does not say that n1 and n2 are
unconnected. It says that no walk of length exactly 2 joins them; walks of length 1 and 3 do
exist.
Proof (derived; induction on k). Write Wk (i, j) for the number of walks of length k from ni to
nj . We prove Wk (i, j) = (Ak )ij for all i, j, for each k ≥ 1. By Remark 2.20 we count sequences
of vertices.
     Base case, k = 1. A walk of length 1 from ni to nj is a sequence (ni , nj ) with ni , nj
adjacent. There is exactly one such sequence if ni and nj are adjacent, and none otherwise. So
W1 (i, j) = Aij = (A1 )ij .
     Induction hypothesis. Let k ≥ 2 and suppose Wk−1 (i, j) = (Ak−1 )ij for all i, j.
     Inductive step. Fix i and j. Every walk (w0 , . . . , wk ) of length k from ni to nj has a second-
last vertex wk−1 . Because k ≥ 2, deleting the last vertex leaves w0 , . . . , wk−1 , a sequence with
consecutive vertices adjacent and length k − 1 ≥ 1, so the induction hypothesis speaks about
walks of that length. Let wk−1 = nr , where r is one of 1, . . . , N . Sort the walks into N classes
by the value of r. The classes are disjoint, because each walk has exactly one second-last vertex,
and together they contain every walk. So Wk (i, j) is the sum over r = 1, . . . , N of the number
of walks of length k from ni to nj whose second-last vertex is nr .
     Fix r. We claim that the number in class r is Wk−1 (i, r) · Arj .
   • If nr and nj are not adjacent (Arj = 0), no walk can have nr followed by nj , so class r is
     empty and the count is 0 = Wk−1 (i, r) · 0.

                                                   13
  • If nr and nj are adjacent (Arj = 1), delete the last vertex of a walk in class r. What
    remains is a sequence w0 , . . . , wk−1 with w0 = ni , wk−1 = nr and consecutive vertices
    adjacent, that is, a walk of length k − 1 from ni to nr . Conversely, any walk of length k − 1
    from ni to nr , followed by nj , is a sequence of k + 1 vertices whose consecutive pairs are
    adjacent, because the new pair nr , nj is adjacent. So it is a walk of length k from ni to nj
    with second-last vertex nr . Deleting and appending undo each other, so they match the
    walks of class r one to one with the walks of length k − 1 from ni to nr , and the count is
    Wk−1 (i, r) = Wk−1 (i, r) · 1.
    Therefore Wk (i, j) =     N
                                 Wk−1 (i, r)Arj . By the induction hypothesis Wk−1 (i, r) =
                             P
                         P r=1
(A )ir , so Wk (i, j) = r (Ak−1 )ir Arj , which is the (i, j) entry of Ak−1 A = Ak by Defini-
   k−1

tion 3.1. This proves the statement for k, and by induction for all k ≥ 1.

    Why the argument is valid. Two facts are the only places where the counting could go
wrong: the sum over the second-last vertex covers each walk exactly once, and the matching
in the case Arj = 1 is one to one. Simplicity is used twice: to identify a walk with its vertex
sequence (Remark 2.20), and so that Arj , the number of edges between nr and nj , is 0 or 1.
Undirectedness is not used in the induction; it only gives the symmetry of A (interpretation; the
versions for digraphs in the cited texts agree [3, 6]). For a graph with repeated edges the same
proof counts walks with multiplicity if Arj is the number of edges, but then the properties of
Proposition 2.17 change (interpretation). A computer check supports the theorem but is not a
proof: for all labelled simple graphs on N = 2, 3, 4, 5 vertices (2, 8, 64, 1024 graphs) a brute-force
enumeration of walks agreed with the matrix entries in all 40, 360, 5120 and 76800 tested cases
of (k, i, j) (Appendix A.5).

3.3   Consequences

In plain words. A count is never negative, and it is always a whole number. A positive count
means that at least one such trip exists. Reverse a trip and you get a trip back. So the table of
trip counts also looks the same when flipped over its diagonal.

Corollary 3.9. For a simple undirected graph and k ≥ 1: (a) every entry of Ak is a non-
negative whole number, so a sum of powers of A has a positive (i, j) entry if and only if some
summand does; (b) (Ak )ij > 0 if and only if there is a walk of length exactly k from ni to nj ;
(c) Ak is symmetric.
Proof. Parts (a) and (b) hold because by Theorem 3.5 the entry is a count. For (c), (Ak )T =
(AT )k = Ak because A is symmetric. Alternatively, reversing the sequence of a walk matches
the walks from ni to nj with the walks from nj to ni .

In plain words. Take the trips of two roads that start and end at the same house. Each one
goes out along a road and comes straight back. So there is one such trip for each neighbour.
That is the number of roads at the house.

Proposition 3.10 (Diagonal of A2 ). (A2 )ii = deg(ni ) for every i. Hence the sum of the diagonal
entries of A2 is 2|E|.
    The first statement is made in lecture notes [2]; the proof below and the second statement
are derived here.

Proof. By Theorem 3.5, (A2 )ii counts the walks ni , nr , ni of length 2 from ni to ni . Such a walk
exists exactly when nr is a neighbour of ni , so there is one for each neighbour, and the number
of neighbours is deg(ni ) (Definition 2.9). Summing over i and using Proposition 2.17, item 5,
gives 2|E|.

                                                 14
    For the board graph the diagonal of A2 is (1, 2, 1), the degrees, and the sum 4 equals 2|E|
(script).

3.4    Walks are not paths

In plain words. A trip may turn back and visit the same house twice. A clean route never
visits a house twice. The table counts trips, so it counts turn-back trips too. A house with at
least one neighbour always has a two-road trip that goes out and comes back. So the table does
not count clean routes.

Proposition 3.11 (Walks are not paths). If ni has at least one neighbour, then (A2 )ii =
deg(ni ) > 0, but no path, and no trail, of length 2 from ni to ni exists. Hence (Ak )ij is in
general not the number of paths, or of trails, of length k from ni to nj .
Proof. The first inequality is Proposition 3.10. A path from ni to ni has its first and last vertices
equal, so it can only be the single vertex, of length 0. A closed walk of length 2 has the form
ni , nr , ni and uses the edge ni nr twice, so it is not a trail.
    The warning holds under both of the textbook’s readings of “path”: distinct vertices (Defi-
nition 1.2.13) and distinct edges (Definition 1.2.12) [9, p. 22]. The general fact that the theorem
counts walks and not paths is also made in the notes cited above [1, 3].
    For the board graph this is concrete: (A2 )11 = 1 > 0, and the one walk is 1, 2, 1, which
repeats the vertex n1 and the edge n1 n2 . Also (A3 )12 = 2, the walks 1, 2, 1, 2 and 1, 2, 3, 2, and
neither is a path or a trail, yet the only path from n1 to n2 has length 1. The enumeration
for k = 1, . . . , 5 finds 1, 0, 2, 0, 4 walks from n1 to n2 , of which 1, 0, 0, 0, 0 are paths (script,
Appendix A.2). So the entries grow with k while the number of paths does not.
    What a positive entry does guarantee is a walk of length k, and Lemma 2.45 then gives a
path of length at most k (derived). This is the fact that Section 4 uses.

3.5    The answer to Q1
For a simple undirected graph with adjacency matrix A and any whole number k ≥ 1, the entry
in row i and column j of Ak is the number of walks of length k from ni to nj . Walks may repeat
vertices and edges, so the entry is not a count of paths.


4     Q2: deciding connectivity from the matrix
4.1    Connected graphs

In plain words. Look at a village. Sometimes you can reach every house from every other
house. You may pass the same house twice on the way. Then the village is called connected. If
one house is cut off, the village is not connected.

Definition 4.1 (Connected graph; textbook Definition 2.1.1). A graph G = (V, E) is connected
if for any two vertices u and v of G there is a (u, v)-path in G [9, p. 48].
   The board states the same definition: a graph is called connected if for any ni , nj there exists
a path between the nodes [4, 5].
Remark 4.2.     1. In the textbook the word “path” here is Definition 1.2.12, a trail. The board
   does not say which meaning it uses, and the course convention is “no repeated vertex”. The
   definition does not depend on the choice: a walk between two different vertices contains a
   path with distinct vertices (Lemma 2.45), and a path has distinct edges (Proposition 2.35),
   so both readings accept exactly the same graphs (derived; compare the cited lemma in
   other notes [3]).

                                                  15
  2. “Any two vertices” includes u = v. For u = v the walk with one vertex and no edges is
     a (u, u)-path, so these pairs are always satisfied, and reading the definition as “any two
     different vertices” changes nothing (interpretation; the textbook does not discuss u = v).

  3. The definition forbids exactly one thing: a pair of vertices with no trip between them.
Example 4.3. The board graph is connected. The pair n1 , n3 is joined by the path 1, 2, 3, and
the pairs n1 , n2 and n2 , n3 are joined by one edge. The textbook’s own examples of connected
graphs are the complete graphs, the complete bipartite graphs, and the three graphs of its
Fig. 2.1.1 [9, p. 48].
Non-example 4.4. Three vertices n1 , n2 , n3 with only the edge n1 n2 . No walk leaves n3 , so
the pair n1 , n3 has no path. The textbook’s Fig. 2.1.2 shows a graph that is not connected and
has four components [9, p. 49].

4.2   Components

In plain words. Look at a village that is not connected. It falls into pieces. Inside one piece
every house can reach every other house. No road joins two different pieces. Each piece is called
a component. A connected village has exactly one piece.

Definition 4.5 (Connected component; textbook, printed p. 49, no number). On the vertex
set V write u ∼ v if G has a (u, v)-path. This relation is reflexive, symmetric and transitive,
so V splits into classes V1 , . . . , Vp . The subgraphs Gj = G[Vj ] that these classes induce are the
connected components of G [9, p. 49].
    The textbook gives this in a paragraph after Definition 2.1.1 without a number; the notation
G[Vj ] means the graph on Vj with all the edges of G that join two vertices of Vj . Another text
defines a connected graph as one with exactly one component, and shows that being joined by a
walk and being joined by a path are the same relation [3, Definition 2.9.12, Proposition 2.9.10].
Remark 4.6. A component cannot be enlarged: a vertex reachable from a vertex of Vj lies
in Vj . The textbook’s Remark 2.1.1 says that G is connected if and only if it has exactly one
component [9, p. 49].
Example 4.7. The graph with only the edge n1 n2 has the two components G[{n1 , n2 }] and
G[{n3 }]. The board graph has the single component G[{n1 , n2 , n3 }] (derived; Section 6).
Non-example 4.8. G[{n1 }] is not a component of the graph with the edge n1 n2 only, although
it is a connected graph: n2 can be reached from n1 , so it belongs to the same class. A component
is a whole class, not any connected piece.

4.3   The sum used by the test

In plain words. We need a name for a running total. It adds the counts of trips with one
road, with two roads, and so on. We stop one step short of the number of houses. The whole
check uses this one total.

Definition 4.9 (The sum S; new notation, not from the textbook). For a graph with N ≥ 2
vertices let S = A + A2 + · · · + AN −1 , the sum of the first N − 1 powers of A, added entry by
entry.
Remark 4.10. By Theorem 3.5, Sij is the number of walks from ni to nj whose length is
between 1 and N − 1. Hence every entry of S is a non-negative whole number (derived). The
diagonal of S counts closed walks and plays no role in the test (Remark 4.21).

                                                 16
                                                1 1 1
                                                                 

Example 4.11. For the board graph S = A + A2 = 1 2 1 (script; Section 6).
                                                    
                                                1 1 1

Non-example 4.12. A2 alone is not S for N = 3, where S = A + A2 . Either one alone gives a
wrong answer for the board graph: A2 has the zero entry (1, 2) although n1 and n2 are joined
by an edge, and A has the zero entry (1, 3) although n1 and n3 are connected (script).

4.4   The test and its proof

In plain words. We want a quick check for a village. We only have the table that says which
houses share a road. From the table we can count trips. Count the trips with one road, with
two roads, and so on. Add the counts for each pair of houses. If no pair of different houses has
a total of zero, the village is connected. We never need trips longer than one road fewer than
the number of houses. A trip that wastes time can always be shortened. So longer trips tell
us nothing new. A second form lets every house also stay put for one step. It gives the same
answer.

Proposition 4.13 (One pair at a time). Let G have N ≥ 2 vertices and let i ̸= j. The following
three statements are equivalent.

  (i) There is an (ni , nj )-path in G (in the sense of textbook Definition 2.1.1).

 (ii) There is a whole number k with 1 ≤ k ≤ N − 1 and (Ak )ij > 0.

(iii) Sij > 0.

Proposition 4.14 (The I + A form). Let   G have N ≥ 2 vertices, let m ≥ N − 1 be a whole
number, and let i ̸= j. Then (I + A)m ij > 0 if and only if Sij > 0. Every diagonal entry of
                                     

(I + A)m is at least 1.

Theorem 4.15 (The connectivity test). Let G be a graph with N ≥ 2 vertices and adjacency
matrix A. The following are equivalent.

 (a) G is connected.

 (b) Every off-diagonal entry of S = A + A2 + · · · + AN −1 is positive.

 (c) Every entry of (I + A)N −1 is positive.

    The sum form is stated in a published note and in an encyclopedia entry [7, 11], and the
second form is stated in lecture notes [1]. The encyclopedia entry gives no proof [11]. The note
applies a walk-counting statement that says “paths” where walks are meant, and passes from
a positive entry to a path without the walk-to-path lemma [7]. The lecture notes have only a
sketch that again says “paths” [1]. The statements of the test are correct. So the proofs here
are the paper’s own (derived), built on Theorem 3.5 and Lemma 2.45. The chain of premises is
listed in Appendix A.3.

Remark 4.16. The test allows any graph with at least two vertices, connected or not. It forbids
using only one power, or stopping before the power N − 1 (Proposition 4.23), or reading the
diagonal of S (Remark 4.21).

                                                      1 1 1
                                                                     

Example 4.17. For the board graph the matrix S = 1 2 1 has no zero entry, so by
                                                           
                                                      1 1 1
Theorem 4.15(b) the graph is connected (Section 6).

                                                17
                                                                1 1 0
                                                                                

Non-example 4.18. For the graph with only the edge n1 n2 , S = 1 1 0 has zeros off the
                                                                     
                                                                0 0 0
diagonal, so the graph is not connected (Section 6).

Proof of Proposition 4.13. (i) implies (ii). A path is a walk, so there is a walk from ni to nj .
By Lemma 2.45 there is a path P from ni to nj whose length k is at most the length of that
walk. P has k edges and therefore k + 1 distinct vertices, and the graph has only N vertices, so
k ≤ N − 1 (Corollary 2.46). If k were 0, P would start and end at the same vertex, but ni ̸= nj ,
so k ≥ 1. P is a walk of length k from ni to nj , so by Theorem 3.5 the number (Ak )ij is at least
1.
    (ii) implies (iii). Sij = Aij + (A2 )ij + · · · + (AN −1 )ij . Each term is a count, hence a non-
negative whole number (Corollary 3.9). A sum of non-negative numbers is at least as large as
any one of its terms, and the term with the index k from (ii) is positive, so Sij > 0.
    (iii) implies (ii). If Sij > 0, a sum of non-negative terms is positive, so at least one term
(Ak )ij with 1 ≤ k ≤ N − 1 is positive.
    (ii) implies (i). If (Ak )ij > 0 with k ≥ 1, then by Theorem 3.5 there is at least one walk
of length k from ni to nj . As ni ̸= nj , Lemma 2.45 gives a path from ni to nj with distinct
vertices. By Proposition 2.35 it also has distinct edges, so it is a (ni , nj )-path in either reading
of the word “path” (Remark 4.2).

Proof of Proposition 4.14. The proof expands (I + A)m with the binomial formula and is given
in Appendix A.4.

Proof of Theorem 4.15. Statement (a) says that for every pair of vertices there is a path between
them. For a pair with u = v this is always true (Remark 4.2). For pairs with i ̸= j it is statement
(i) of Proposition 4.13. So (a) holds if and only if (i) holds for every i ̸= j. By Proposition 4.13
this is equivalent to (iii) for every i ̸= j, which is (b). By Proposition 4.14 with m = N − 1 it
is also equivalent to the positivity of every off-diagonal entry of (I + A)N −1 . Together with the
diagonal entries, which are always positive by Proposition 4.14, this is (c).

Corollary 4.19 (Components from S). For any graph, connected or not, with N ≥ 2 vertices
and i ̸= j: Sij > 0 if and only if ni and nj lie in the same component.

Proof. Proposition 4.13 uses connectivity only through the pair (ni , nj ): statement (i) says that
ni ∼ nj , which is the definition of “same class” in Definition 4.5.

Remark 4.20 (Distance). A shortest walk between two different vertices is a path, by
Lemma 2.45 and Proposition A.1. So the smallest k with (Ak )ij > 0 is the distance d(ni , nj ) of
Definition 2.41 (derived); this is also stated in two other sources [6, 7].

Remark 4.21 (The diagonal, and N = 1, N = 2). For N = 2 and one edge, S = A has zeros on
the diagonal although the graph is connected (script). So the diagonal of S cannot be required
to be positive. For N ≥ 3 and a connected graph the diagonal of S is positive anyway, because
every vertex has a neighbour and (A2 )ii = deg(ni ) (Proposition 3.10), but the test does not
need this. For N = 1 there are no pairs of different vertices, the graph is connected, and both
forms of the test give the right answer, but S is an empty sum, so the test is stated for N ≥ 2
(derived).

4.5   The test as a procedure

In plain words. Here is the check, step by step. First write the table of the village. Then
multiply the table by itself again and again. After each step, add the new counts to a running
total. Stop after one step fewer than the number of houses. Look at every pair of different houses.

                                                 18
If any total is zero, those two houses cannot reach each other. If no total is zero, everyone can
reach everyone.

Test 4.22 (Matrix test). Input: the adjacency matrix A of a graph with N ≥ 2 vertices.
  1. Set P = A and S = A.

  2. For k = 2, 3, . . . , N − 1: replace P by the product P A (now P = Ak ) and add P to S.

  3. Look at the entries Sij with i ̸= j. If one of them is 0, the graph is not connected. If none
     is 0, the graph is connected.
An equivalent form computes (I + A)N −1 and reports “connected” if no entry is 0.
    Correctness is Theorem 4.15. A zero at (i, j) also says, by Corollary 4.19, that ni and nj lie
in different components.

4.6   Why N − 1 powers are enough and N − 2 are not
Enough: Proposition 4.13 shows that if a trip between two different vertices exists at all, a trip
of length at most N − 1 exists, because a shortest trip repeats no vertex and a repeat-free trip
has at most N vertices. So adding powers beyond N −1 cannot change which off-diagonal entries
are positive. Not fewer: the next statement shows that N − 1 cannot be lowered.
In plain words. Take four houses in a row. To go from the first house to the last, you must
pass every house in between. That takes three roads. If we counted only trips of up to two roads,
we would miss this pair. We would say the village is cut in two, and we would be wrong. The
same idea works for any row of houses.

Proposition 4.23 (N − 1 cannot be lowered to N − 2). For every N ≥ 3 there is a connected
graph with N vertices for which the sum A + · · · + AN −2 has a zero off-diagonal entry.
Proof. Take the graph with edges n1 n2 , n2 n3 , . . . , nN −1 nN . Each step of a walk changes the
vertex number by exactly 1. To go from n1 to nN the number must increase by N − 1, so at
least N − 1 steps are needed. So no walk of length k < N − 1 from n1 to nN exists, and by
Theorem 3.5 (Ak )1N = 0 for 1 ≤ k ≤ N − 2. The (1, N ) entry of A + · · · + AN −2 is therefore 0,
although the graph is connected.

   A script confirms it for N = 3, . . . , 8: the first power with a nonzero (1, N ) entry is AN −1
each time (Appendix A.5). For N = 3 the graph is the board graph and the sum is A itself,
with A13 = 0. For N = 4 the matrices are written out in Section 6.

4.7   Breadth-first search, for comparison

In plain words. There is another way, and it needs no table of counts. Stand at one house
and mark it. Then mark every house next to it. Then mark every house next to those. Keep
going until no new house appears. If every house is marked, the village is connected.

Remark 4.24 (Breadth-first search). Breadth-first search (BFS) from a start vertex s keeps
a queue of discovered vertices, and repeatedly takes the vertex at the front and discovers its
undiscovered neighbours. Its correctness statement in the source is that for every vertex v there
is a walk from s to v if and only if v is discovered when the search ends [10]. So G is connected
if and only if every vertex is discovered when BFS starts from any single vertex s (Remark 4.2
lets walks stand for paths). BFS also yields the components directly. The matrix test and BFS
agree on all 32768 labelled graphs with 6 vertices and on all smaller ones (script, Section 6); this
is a check, not a proof. The cost of the two methods is compared in Section 7.4.

                                                19
4.8    The answer to Q2
A graph with N ≥ 2 vertices and adjacency matrix A is connected if and only if every off-
diagonal entry of A + A2 + · · · + AN −1 is positive, and equivalently if and only if (I + A)N −1
has no zero entry (Theorem 4.15).


5     Q3: the definition of a path between ni and nj

In plain words. Pick two houses of the village. A path between them is a clean route. It starts
at the first house and ends at the second. It never visits any house twice. If the two houses are
the same house, the route is just staying home.

Definition 5.1 (Path between ni and nj ; course convention). Let ni and nj be vertices of G. A
path between ni and nj is a walk w0 , w1 , . . . , wk with w0 = ni and wk = nj in which the vertices
w0 , . . . , wk are pairwise distinct. Its length is k. For i = j the only such path is the single vertex
ni , of length 0.

    This is a simple path in the sense of textbook Definition 1.2.13 and a path in English usage
[9, p. 22]. It is the specialization of Definition 2.31 to the endpoints ni and nj . The statement
that the course uses “path” in this sense comes from the assignment text; the board does not
say which meaning it uses [4, 5]. The definition is therefore an interpretation, and it is qualified.

Remark 5.2. The definition allows length 0 (when i = j), length 1 (an edge), and at most
N − 1 edges (Corollary 2.46). It forbids any repeated vertex, and therefore any repeated edge
(Proposition 2.35). It does not forbid several different paths between the same two vertices; it
says only what a path is.

Example 5.3. In the board graph there is exactly one path between n1 and n3 , namely 1, 2, 3.
Every path has at most N − 1 = 2 edges, so the enumeration of walks up to length 4 finds all
of them (script). Between n1 and n1 the only path is the one of length 0.

Non-example 5.4. In the board graph 1, 2, 1, 2, 3 is a walk between n1 and n3 but not a path
between them: it repeats the vertices 1 and 2. It is not a trail either, because it repeats the
edge n1 n2 .

The two textbook readings give the same answers. If “path” is read as the textbook’s
Definition 1.2.12 (a trail), then “there is a path between ni and nj ” has the same truth value
as in Definition 5.1. A path is a trail (Proposition 2.35), so a path gives a trail. A trail is a
walk, and a walk contains a path (Lemma 2.45), so a trail gives a path. Hence every sentence
of the form “there is a path between ni and nj ”, in particular the definition of connected, has
the same meaning in both readings (derived). What changes with the reading is a count: the
number of trails between two vertices is not the number of paths, and neither is the number of
walks (Proposition 3.11).

The answer to Q3. A path between ni and nj is a walk from ni to nj in which all vertices
are pairwise distinct.


6     Worked examples
Every matrix, sum, and count in this section was computed by script (Appendix D); the matrices
are written out entry by entry so that they can be checked against the graphs.



                                                   20
6.1    The board graph and its powers

In plain words. We take the village from the board. It has three houses in a row. The first
and last houses each have one road. The middle house has two roads. We count trips of two
roads, then of three roads. We list every trip, so the reader can see that each count is right.
   The graph has the vertices n1 , n2 , n3 and the edges n1 n2 and n2 n3 ; this is the graph of the
board matrix (Section 1.4). Its adjacency matrix and the powers up to A5 are

                         0 1 0                    1 0 1                      0 2 0
                                                                             

                    A = 1 0 1 ,          A2 = 0 2 0 ,             A3 = 2 0 2 ,
                                                                              
                         0 1 0                    1 0 1                      0 2 0

                                    2 0 2                       0 4 0
                                                                         

                               A = 0 4 0 ,
                                4
                                                           A = 4 0 4 .
                                                            5
                                                                  
                                    2 0 2                       0 4 0
Also A3 = 2A and Ak+2 = 2Ak for k = 1, . . . , 5 (script). The matrix A is symmetric with zero
diagonal, and the row sums 1, 2, 1 are the degrees (Proposition 2.17).
   Explicit walks (derived by enumeration, labels 1, 2, 3 for n1 , n2 , n3 ).

   • Length 1: 1, 2 and 2, 3 and their reverses.

   • Length 2: from 1 to 1: 1, 2, 1 (one walk). From 1 to 3: 1, 2, 3 (one). From 2 to 2: 2, 1, 2
     and 2, 3, 2 (two). From 3 to 3: 3, 2, 3 (one).

   • Length 3: from 1 to 2: 1, 2, 1, 2 and 1, 2, 3, 2 (two). From 2 to 3: 2, 1, 2, 3 and 2, 3, 2, 3
     (two).

Each count equals the corresponding matrix entry, as Theorem 3.5 says; the script asserts this
for every entry of A, A2 and A3 .
    The sums from the inductive step. The step of the proof of Theorem 3.5 adds up one term
for each choice of the second-last vertex nr . For (A3 )12 the terms are (A2 )1r Ar2 for r = 1, 2, 3,
namely 1 · 1 + 0 · 0 + 1 · 1 = 2. The term for r = 1 is the walk 1, 2, 1 followed by the step to n2 ,
giving 1, 2, 1, 2; the term for r = 3 is the walk 1, 2, 3 followed by the step to n2 , giving 1, 2, 3, 2.
Likewise (A2 )22 = 1 · 1 + 0 · 0 + 1 · 1 = 2 and (A2 )11 = 0 · 0 + 1 · 1 + 0 · 0 = 1.
    Counts by walk length. Table 4 counts, over all start and end vertices, the walks, trails, paths
and closed walks of each length k by enumeration. The entries of Ak for k = 1, . . . , 5 agree with
the enumeration (script).

Table 4: Walks, trails, paths and closed walks of length k in the board graph, over all start and
end vertices (script m2_walks.py).
                              k    walks    trails    paths        closed walks
                               0     3        3            3            3
                               1     4        4            4            0
                               2     6        2            2            4
                               3     8        0            0            0
                               4    12        0            0            8

    From n1 to n3 there are three walks of length at most 4: 1, 2, 3 (length 2), and 1, 2, 1, 2, 3
and 1, 2, 3, 2, 3 (length 4); only the first is a path (script). The numbers of walks from n1 to n2
for k = 1, . . . , 5 are 1, 0, 2, 0, 4, and the numbers of paths among them are 1, 0, 0, 0, 0 (script), as
used in Proposition 3.11.

                                                      21
   The drawing. The drawing on the board also has the line 1–3 and an arrowhead on the line
1–2. If the line 1–3 were an edge, the triangle 1, 2, 3, 1 would be a simple cycle (Example 2.39),
and the matrix would have A13 = A31 = 1. It does not, and this paper follows the matrix.

6.2   A connected example

In plain words. Take three houses in a row. A road joins the first and the second house.
Another road joins the second and the third house. The first and the third house share no road.
Can you still go from one to the other? Yes, through the middle house. We expect the check to
say connected.

Example 6.1 (Connected; the board graph, N = 3, N − 1 = 2).

     0 1 0                  1 0 1                        1 1 1                         2 2 1
                                                                                          

A = 1 0 1 ,          A = 0 2 0 ,
                        2
                                           S = A + A = 1 2 1  ,
                                                    2
                                                                           (I + A) = 2 3 2 .
                                                                                  2
                                                                                      
     0 1 0                  1 0 1                        1 1 1                         1 2 2

S has no zero entry off the diagonal (it has none anywhere), so by Theorem 4.15(b) the graph is
connected. (I + A)2 has no zero entry, so by Theorem 4.15(c) the graph is connected. The two
answers agree. The entry A13 is 0, so no road joins n1 and n3 , yet (A2 )13 = 1: there isexactly
one walk of length 2 from n1 to n3 , namely 1, 2, 3. The (1, 3) entry of (I + A)2 is 1 = 22 (A2 )13 ,
since the other two terms vanish there, and (I + A)2 = I + 2A + A2 holds entry by entry (script).
BFS from vertex 1 reaches {1, 2, 3} (script).

6.3   A disconnected example

In plain words. Now take three houses again. Only one road exists, between the first and
second house. The third house stands alone. Nobody can walk to it. We expect the check to say
not connected. The check should also show that the third house is a piece by itself.

Example 6.2 (Disconnected; edge n1 n2 only, N = 3, N − 1 = 2).

           0 1 0                  1 0 0               1 1 0                     2 2 0
                                                                                      

      A = 1 0 0 ,          A = 0 1 0 ,
                              2
                                                 S = 1 1 0 ,       (I + A) = 2 2 0 .
                                                                            2
                                                                              
           0 0 0                  0 0 0               0 0 0                     0 0 1

The off-diagonal zeros of S are at (1, 3), (2, 3), (3, 1) and (3, 2), and the zeros of (I + A)2 are
at the same four places. So by Theorem 4.15 the graph is not connected, and by Corollary 4.19
the vertices n1 and n2 lie in one component and n3 in another: the components are {n1 , n2 } and
{n3 }, which agrees with BFS (script). Higher powers do not help: the entries (1, 3) and (2, 3)
of Ak are 0 for k = 1, . . . , 6, and in fact no walk reaches n3 at all.

6.4   The bound N − 1 is needed

In plain words. Now take four houses in a row. The first and the last house are three roads
apart. So a check that stops at trips of two roads cannot see that they are connected. We write
out the tables and watch what happens.

Example 6.3 (The path on four vertices, N = 4). The edges are n1 n2 , n2 n3 , n3 n4 .
                  0      1   0   0           1    0   1   0           0    2   0   1
                                                                              
                 1      0   1   0         0    2   0   1         2    0   3   0
               A=                ,   A2 =               ,   A3 =               .
                                                                               
                 0      1   0   1         1    0   2   0         0    3   0   2
                  0      0   1   0           0    1   0   1           1    0   2   0

                                                 22
           1    1   1   0                                         1      3    1   1
                                                                               
         1     2   1   1                                      3       2    4   1
A + A2 =                    (N − 2 powers),      A + A2 + A3 =                       (N − 1 powers).
                                                                                
         1     1   2   1                                      1       4    2   3
                                                                                  

           0    1   1   1                                         1      1    3   1
With N − 2 = 2 powers the (1, 4) entry is 0, and the test would wrongly say “not connected”.
With N − 1 = 3 powers every entry is positive. This is the case N = 4 of Proposition 4.23.

6.5    Exhaustive agreement with breadth-first search

In plain words. Examples on a few villages are not proof. So we also ran the check on every
possible village with up to six houses. Each time we compared it with the marking method. The
two methods always gave the same answer.
    Table 5 reports a script that built every labelled simple graph with N = 2, . . . , 6 vertices,
ran the sum test and the (I + A)N −1 test, and compared them with an independent BFS. The
last column shows what goes wrong with only N − 2 powers. This is a test of the statements
and not a replacement for the proofs in Section 4, and it covers N ≤ 6 only.

Table 5: Exhaustive check over all labelled simple graphs with N vertices (script
m3_connectivity.py). Columns “sum test” and “(I + A)N −1 test” give the number of graphs
on which the test agrees with BFS.
N     graphs   connected     sum test agrees   (I + A)N −1 test agrees       wrong with N − 2 powers
 2        2             1                 2                         2                               1
 3        8             4                 8                         8                               3
 4       64            38                64                        64                              12
 5     1024           728              1024                      1024                              60
 6    32768         26704             32768                     32768                             360

   For N = 3 the N − 2 test is wrong on 3 of the 8 graphs, the three labelled paths, and for
N = 4 on 12 of 64. For N = 2 the sum with N − 2 = 0 powers is empty and is wrong on the
one connected graph. The same script also confirmed that the statement of Corollary 4.19 and
the repeated-squaring version of the test (Section 7.4) agree with BFS on all these graphs.


7     Discussion: limits, disagreements, and cost
7.1    What is proved and what is only checked
The two main results, Theorem 3.5 and Theorem 4.15, are proved in full from the definitions,
using Lemma 2.45 for the second. The computer checks are tests of the statements and not
proofs: the walk count was compared with brute-force enumeration for all labelled simple graphs
on 2 to 5 vertices, and the test was compared with BFS for all labelled simple graphs on 2 to
6 vertices (Appendix A.5). The proof of Theorem 4.15 is only as good as Theorem 3.5 and
Lemma 2.45. The first is stated by four sources [2, 3, 6, 1]. The second combines the textbook’s
lemma, which needs u ̸= v and states no length bound, with a version from another text that
allows u = v and gives the bound [9, 3]; the paper proves the combined form itself. The
arithmetic is ordinary integer arithmetic. Entries are counts and hence non-negative, which is
what makes “a sum is positive if and only if some term is positive” valid; with subtraction or
modular arithmetic that step would fail (derived).




                                                 23
7.2   Conventions that change the words but not the mathematics
  • Path. Under the textbook’s own word, “path” allows repeated vertices (Definition 1.2.12),
    and a reader who uses it will count trails [9]. The paper states which meaning it uses
    and keeps it (Table 3). The board does not say which meaning it uses, and the course
    reading comes from the assignment text. This does not change the connectivity result
    (Remark 4.2), and it changes only counts (Proposition 3.11).

  • Cycle. The textbook’s cycle is a closed trail and the English cycle is the textbook’s simple
    cycle [9, 3]. Cycles are not needed for the main results.

  • Length 0. Whether a walk of length 0 is allowed, and whether a closed trail of length 0 is
    a cycle, is not stated in the textbook pages read (Remark 2.19, Remark 2.38). For i ̸= j
    the connectivity result needs only paths of length at least 1.

  • The mark above A. If the mark is an n and not a k, Theorem 3.5 still describes (An )ij , so
    the mathematics is unchanged; the reading of the board remains open [4, 5].

  • The drawing. The drawing and the matrix on the board disagree on the line 1–3 and on
    an arrowhead (Section 1.4). The paper follows the matrix and does not guess which one
    the lecturer intended.

7.3   Where the sources disagree
One published note states its Theorem 1 as “the entry counts different paths of length l”, while
its own property 7 speaks of walks [7]. As written, Theorem 1 is false for any definition of path
that forbids repeated vertices or repeated edges, by Proposition 3.11. This paper does not cite
that theorem as support for Theorem 3.5; it cites the notes that say walks [2, 3, 6, 1]. The
note and the lecture notes that state the connectivity test explain it by “paths” where walks are
meant, so their explanation is wrong although their statements of the test are correct (Section 4)
[7, 1]. Eigenvalue-based tests are outside the scope of this note, and nothing is claimed about
them.

7.4   Cost of the matrix test and of breadth-first search
This subsection is an estimate that counts operations and does not time programs. Take the
school method, in which one product of two N × N matrices takes N 3 scalar multiplications.
Reaching AN −1 from A takes N − 2 products, so the matrix test costs about (N − 2)N 3 mul-
tiplications: 98,000,000 for N = 100 (script). By Proposition 4.14 the exponent N − 1 may be
replaced by any larger exponent, so one can square I + A repeatedly until the exponent 2t is at
least N − 1. That takes t squarings, 7 for N = 100, costing 7,000,000 multiplications (script);
the script checked this version against BFS on every labelled graph with at most 6 vertices.
BFS takes time proportional to n + m, the numbers of vertices and edges, when the graph is
given by adjacency lists [10]. When the input is the matrix A itself, BFS reads each row once,
which is N 2 = 10,000 entries for N = 100 (derived). The entries of the powers also grow fast:
for the complete graph on 10 vertices the largest entry of A9 is 38,742,049 (script). The matrix
test is useful because its answer is a clean statement about powers of A, not because it is fast.
Faster matrix multiplication methods were not examined. The cited slides compare BFS with
no matrix test, and the count of N − 2 products is this paper’s own [10].

7.5   Limits and open questions
  • The theorems are for simple graphs. With loops or repeated edges the entry Arj may
    exceed 1 and Aii may be nonzero; the same proof then counts walks with multiplicity


                                               24
      (interpretation), but Proposition 2.17 changes. The test is not claimed for directed graphs:
      no source was checked for them, and the symmetry of A is used.

    • The textbook states no walk-counting theorem and no matrix connectivity test in the
      pages read, and a search of the book found none; the rest of the book was not read page
      by page, so this absence is qualified [9].

    • The brute-force checks cover small graphs only.

    • The test says connected or not. The sum S does not list a path; Corollary 4.19 gives the
      components and Remark 4.20 the distances.

    • Open: whether the lecturer’s intended answer to the board’s question 2 was the sum test,
      the (I + A)N −1 test, or BFS; the board shows only the question.

    • Open: the reading of the mark above A, and the mismatch between the drawing and the
      matrix. Only the user can settle these.


8     Conclusion
The three questions have direct answers.

Q1. For a simple undirected graph with adjacency matrix A and a whole number k ≥ 1, the
entry (Ak )ij is the number of walks of length k from ni to nj (Theorem 3.5, proved by induction
on k from the definition of the matrix product; the statement is standard [2, 3]). It counts walks
and not paths: in the board graph (A2 )11 = 1, the walk 1, 2, 1, which is neither a path nor a
trail (Proposition 3.11).

Q2. A graph with N ≥ 2 vertices is connected if and only if every off-diagonal entry of
A + A2 + · · · + AN −1 is positive, and equivalently if and only if (I + A)N −1 has no zero entry
(Theorem 4.15, derived here). The proof uses the walk-counting theorem and the fact that
every walk contains a path of no greater length, so powers beyond N − 1 add nothing;          the
                                                                                       1 1 1
                                                                                              

bound cannot be lowered to N − 2 (Proposition 4.23). The board graph, with S = 1 2 1,
                                                                                              
                                                                                       1 1 1
                                                                 1 1 0
                                                                        

is connected; the graph with the edge n1 n2 only, with S = 1 1 0, is not. Breadth-first
                                                                        
                                                                 0 0 0
search is an alternative that needs no matrix powers [10].

Q3. A path between ni and nj is a walk from ni to nj in which all vertices are pairwise
distinct, that is, the textbook’s simple path (Definition 1.2.13) [9, p. 22]. The textbook’s own
word “path” (Definition 1.2.12) allows repeated vertices and is called a trail here. The statement
that the course uses the first meaning comes from the assignment text and is an interpretation;
the existence of a path between two vertices is the same under both readings (Section 5).

What remains open. The reading of the mark above A on the board, the mismatch between
the board’s drawing and its matrix, and the question which test the lecturer intended are not
settled by the sources (Section 7.5).




                                               25
A     Derivations and checks
This appendix holds the proofs and computations that the main text only states. Every state-
ment here is derived in this paper, except where a citation is given.

A.1    The distance properties
Proposition A.1 (Shortest walk, trail, and path agree). For vertices u, v of a simple graph,
the length of a shortest (u, v)-walk, of a shortest (u, v)-trail, and of a shortest (u, v)-path are
equal. Each is +∞ when the corresponding set is empty, and the three sets are empty together.
So d(u, v) of Definition 2.41 is the same whether “path” in that definition is read as trail or as
path.

Proof. Every path is a trail (Proposition 2.35) and every trail is a walk. So the lengths of paths
are among the lengths of trails, which are among the lengths of walks. Hence the minimum
over walks is at most the minimum over trails, which is at most the minimum over paths. By
Lemma 2.45 a shortest walk contains a path of at most the same length, so the minimum over
paths is at most the minimum over walks. Therefore the three minima are equal. If there is no
walk, there is no trail and no path. If there is a walk, Lemma 2.45 gives a path, so the three
sets are empty together.

    Another text makes the same remark in prose: a shortest walk from u to v, if it exists, is
also a shortest path [3, Section 2.9.4].

Proposition A.2 (The distance properties). The three properties of Definition 2.41 follow from
the definition.

Proof. Use Proposition A.1 to compute d by shortest walks. (1) Lengths are 0, 1, 2, . . . or +∞,
so d ≥ 0. The walk consisting of u alone has length 0, so d(u, u) = 0. If d(u, v) = 0 there is a walk
of length 0 from u to v; it is the single vertex, so v = u. (2) If u0 , . . . , uk is a (u, v)-walk, then
uk , . . . , u0 is a (v, u)-walk of the same length, since each step is an edge and edges are unordered.
So the sets of walk lengths from u to v and from v to u are equal, and so are their minima. (3)
If d(u, w) or d(w, v) is +∞, the right side is +∞ and the inequality holds. Otherwise take a
shortest (u, w)-walk and a shortest (w, v)-walk and join them at w. The result is a (u, v)-walk
of length d(u, w) + d(w, v), and the shortest (u, v)-walk is no longer than this.

A.2    The counterexample to “entries count paths”
For the board graph the script m1_walks.py lists, for each k from 1 to 5, all walks from n1 to
n2 and tests each for distinct vertices (path) and distinct edges (trail). Its output is saved in
appendices/scripts/m1_walks_output.txt. Table 6 repeats the numbers; the author script
author_numbers.py recomputes them independently and agrees.

Table 6: Walks from n1 to n2 in the board graph, and how many of them are paths (they are
also the trails).
                                         k              1   2   3   4   5
                                 (Ak )12 = walks        1   0   2   0   4
                                paths among them        1   0   0   0   0

    For closed walks at n1 the numbers of walks of length 1, . . . , 4 are 0, 1, 0, 2, and none of them
is a path or a trail (script m1_walks.py). The general fact is Proposition 3.11.



                                                   26
A.3    The chain of premises for the connectivity test
The proof of Theorem 4.15 rests on the premises below, each marked with where it comes from.

   1. Walk counting (Theorem 3.5): the entry (Ak )ij counts walks of length k [2, 3]; proved in
      Section 3.

   2. Non-negativity (Corollary 3.9): every entry of every power is a non-negative whole number;
      derived from item 1.

   3. Walk to path (Lemma 2.45): a walk contains a path of at most its length [3, Corollary
      2.9.7]; the textbook states it for u ̸= v [9, p. 23]; proved in Section 2.

   4. Length bound (Corollary 2.46): a path has at most N − 1 edges [3, Section 2.9.4]; proved
      in Section 2.

   5. Path implies trail (Proposition 2.35): proved in Section 2.

   6. Definition of connected (Definition 4.1) [9, p. 48].

Forward direction: if G is connected and i ̸= j, items 6, 3 and 4 give a path of length k with
1 ≤ k ≤ N − 1, and items 1 and 2 give (Ak )ij ≥ 1 and hence Sij ≥ 1. Backward direction: if
Sij > 0, items 1 and 2 give a walk, and items 3 and 5 give a path in either reading, so G is
connected. These are the steps of Proposition 4.13.

A.4    Proof of the I + A form
Proof of Proposition 4.14. Put m ≥ N − 1 and expand (I + A)m = (I + A)(I + A) · · · (I + A),
with m factors. Each term of the expansion chooses I or A from each factor and multiplies the
choices in order. Because IX = XI = X for every matrix X, a product with k letters A and
m − k letters I equals A k . The number of ways to choose which k of the m factors give A is the
                     m
binomial coefficient k . Therefore
                                          !       !            !            !
                                         m    m    m 2         m m
                    (I + A)   m
                                  =        I+   A+   A + ··· +   A .
                                         0    1    2           m

Take an entry (i, j) with i ̸= j. The identity has 0 there, so
                                           !               !              !
                                         m         m                   m
                   (I + A) m
                                     =     (A)ij +   (A2 )ij + · · · +   (Am )ij .
                                ij       1         2                   m

Every coefficient m  k with 1 ≤ k ≤ m is a positive whole number, and every (A )ij is a non-
                                                                                          k
                     

negative whole number. So the sum is positive if and only if at least one (Ak )ij with 1 ≤ k ≤ m
is positive. For m = N − 1 this is exactly Sij > 0. For m > N − 1, if some (Ak )ij with k ≤ m is
positive, there is a walk from ni to nj , hence by Corollary 2.46 a walk of length at most N −1, so
          ′
some (Ak )ij with 1 ≤ k ′ ≤ N − 1 is positive,     that is, Sij > 0; the converse is immediate because
N − 1 ≤ m. On the diagonal the term m             contributes   1 and all other terms are non-negative,
                                              
                                            0   I
so every diagonal entry of (I + A)m is at least 1 whatever the graph is.

   The idea of the (I + A)N −1 form appears in lecture notes in a proof sketch [1]; the expansion
above is derived here.




                                                      27
A.5     Cross-checks by script
All checks are finite tests of statements that are proved in the text.
    • Walk counting. For every labelled simple graph on N = 2, 3, 4, 5 vertices (2, 8, 64, 1024
      graphs) the script m1_walks.py enumerated all walks by depth-first search and compared
      with Ak for k = 1, . . . , 5 when N ≤ 4 and k = 1, . . . , 3 when N = 5. All 40, 360, 5120 and
      76800 tested cases of (k, i, j) agree.
    • Lemma and propositions of Section 2. The script m2_walks.py applied the cutting con-
      struction of Lemma 2.45 to all 73 walks of length 0 to 6 in the board graph, all 381 in
      the triangle and all 4695 in the textbook graph, with 0 failures. On 300 random graphs
      with N from 2 to 7 (seed 20261027) and 192696 walks of length 0 to 5 it found 0 failures
      of the lemma, 0 failures of Proposition 2.35, 0 paths longer than N − 1 (Corollary 2.46),
      and 0 disagreements between BFS distance and the shortest walk, trail and path (Propo-
      sition A.1).
    • Connectivity test. The script m3_connectivity.py reports in Table 5 the exhaustive
      agreement with BFS for N = 2, . . . , 6, and for the path graph on N = 3, . . . , 8 vertices
      that the smallest k with (Ak )1N > 0 is N − 1, so that the (1, N ) entry of A + · · · + AN −2
      is 0 and that of A + · · · + AN −1 is 1 each time.


B      The textbook’s terms and numbers
Table 7 lists every textbook definition and result used in the paper, with its printed page, so
that each can be checked against the book [9]. Page numbers are the printed numbers of the
book; the PDF page is the printed page plus one. The textbook is in Armenian, and its text
layer drops most symbols, so formulas were checked against the page images. Only the pages
named below were read page by page, and the rest of the book was not read.

                  Table 7: Textbook definitions and results used in this paper [9].
  Textbook item            Page         Content (English)                          Paper
  Definition 1.1.1         9            graph G = (V, E), finite V , E a set of    Definition 2.1
                                        unordered pairs of distinct vertices
  Definition 1.1.4         11           adjacent vertices                          Definition 2.5
  adjacency matrix (af-    11–12        aij = 1 if adjacent, else 0; symmetric,    Definition      2.13,
  ter Definition 1.1.6;                 zero diagonal; converse                    Proposition 2.17
  number not recorded)
  Definition 1.2.10        21–22        walk; vertices and edges may repeat;       Definition 2.18
                                        length counts edges with multiplicity
  Definition 1.2.11        22           closed walk                                Definition 2.23
  Definition 1.2.12        22           “path”: distinct edges (English: trail)    Definition 2.27
  Definition 1.2.13        22           “simple path”: distinct vertices (En-      Definition 2.31
                                        glish: path)
  Definition 1.2.14        22           “closed path or cycle”: closed trail       Definition 2.36
  Definition 1.2.15        22           “simple cycle”: only first and last ver-   Definition 2.37
                                        tex repeat; Cn , n ≥ 3
  Definition 1.2.16        22–23        distance                                   Definition 2.41
  Lemma 1.2.1              23           from a walk between different vertices     Lemma 2.45
                                        one can extract a simple path
  Definition 2.1.1         48           connected graph                            Definition 4.1
  (no number)              49           connected components                       Definition 4.5
  Remark 2.1.1             49           connected if and only if one compo-        Remark 4.6
                                        nent



                                                  28
Board and textbook notation. The board writes (G, V ) for the graph, eij ∈ V for “the
edge eij belongs to the edge set”, |G| = N for the number of vertices, and ni , nj for vertices [4,
5]. The textbook writes G = (V, E), e ∈ E, n = |V |, and vi [9]. The paper uses G = (V, E) and
N for the number of vertices, and the board’s ni for vertices (Table 2).


C      The whiteboard photographs
Two photographs show the same lecture board at slightly different angles [4, 5]. They are read
together. Figure 1 reproduces both.




Figure 1: The two photographs of the lecture board [4, 5]. A reflection of a person is visible on
the right.


Transcription in reading order.

    1. Aij = 1 if eij ∈ V , and 0 if eij ∈
                                         / V ; the board’s V is the edge set [4, 5].

    2. A drawing with vertices labelled 1, 2, 3, and next to it a matrix labelled “adj.” with rows
       0 1 0 / 1 0 1 / 0 1 0.

    3. “Problem. Given graph (G, V ) with N nodes i.e. |G| = N and the graph is represented
       through it’s adj. matrix. So you have A matrix.”

    4. “1) What does Aij represent”, with a small mark above A.

    5. “2) How to know if graph is connected or not.”

    6. “Def. Graph is called connected if for any ni , nj there exists a path between nodes.”



                                                   29
Clearly visible. All the prose above, the matrix entries, and the vertex labels.

Likely interpretation. The mark above A is an exponent k (interpretation, qualified: the
assignment text asks about Ak , but in both photographs the mark looks like a small n or a
pair of quotation marks). The arrowhead on the line 1–2 is a stray mark, because the matrix is
symmetric and the problem is about undirected graphs (interpretation).

Unclear or in conflict. The drawing shows a line from 1 to 2 with an arrowhead at 2, a line
from 1 to 3, and a line from 2 to 3, which would be three edges, while the matrix encodes only
the edges 1–2 and 2–3 [4, 5]. Edge by edge: the edge 1–2 is in both; the edge 2–3 is in both; the
edge 1–3 is in the drawing only. The paper follows the matrix and reports the mismatch.


D      Reproducibility
Every number in the paper that is a matrix entry, a sum, or a count was computed by one of
the scripts below. All are pure Python with integer arithmetic, so no rounding occurs. Run
each one from the paper folder with python3 -I; the saved outputs sit beside the scripts.

appendices/scripts/author_numbers.py computes the matrices of Section 6 and writes them
     to figures/generated_numbers.tex, which the paper inputs; it also checks each power
     against a direct walk enumeration, and computes the walk and path counts of Table 6 and
     the cost counts of Section 7.4. Output: author_numbers_output.txt.

appendices/scripts/m1_walks.py board graph powers, explicit walks, walks against paths,
     brute-force check of Theorem 3.5. Output: m1_walks_output.txt.

appendices/scripts/m2_walks.py classification of sequences as walk, trail, path, cycle; the
     cutting construction of Lemma 2.45; Table 4. Output: m2_walks_output.txt.

appendices/scripts/m3_connectivity.py the tests of Section 4, the examples, the sharpness
     table, the exhaustive check of Table 5, and the cost counts. It takes about thirty seconds.
     Output: m3_connectivity.out.txt.

    The scripts are copies of the ones in the folder modules/, which are kept as the module
records.


References
 [1]   Shuliang Bai. Important Properties and Applications of the Adjacency Matrix (20250310).
       Lecture notes, BIMSA, dated 2025-03-10 in the title. 2025. url: https://bimsa.net/
       doc/notes/48535.pdf?id=0.3935315718408674 (visited on Oct. 27, 2026).
 [2] Chapter 1 Matrices and Graphs, 1.1 The Adjacency Matrix (linear algebra course notes,
     NUI Galway). Lecture notes, School of Mathematical and Statistical Sciences, University of
     Galway; author and date do not appear in the file. n.d. url: https://maths.nuigalway.
     ie/~rquinlan/linearalgebra/section1-1.pdf (visited on Oct. 27, 2026).
 [3]   Darij Grinberg. An introduction to graph theory (Text for Math 530 in Spring 2022 at
       Drexel University). arXiv:2308.04512v3 [math.HO], Spring 2025 edition, 7 June 2025;
       lecture-note text, 454 pp.; page locators are the document’s own. 2025. url: https :
       //arxiv.org/abs/2308.04512 (visited on Oct. 27, 2026).
 [4] Lecture whiteboard photo 1. File sources/whiteboard-1.jpg. Supplied by the user. Pho-
     tograph of a lecture board; author and date unknown. Accessed 2026-10-27. n.d.

                                               30
 [5] Lecture whiteboard photo 2. File sources/whiteboard-2.jpg. Supplied by the user. Sec-
     ond photograph of the same board; author and date of the board unknown. Accessed
     2026-10-27. n.d.
 [6]   Eric Lehman, F. Thomson Leighton, and Albert R. Meyer. 9.3: Adjacency Matrices (Math-
       ematics for Computer Science; MIT OpenCourseWare), Engineering LibreTexts. Engineer-
       ing LibreTexts, CC BY-NC-SA; page last modified 2021-07-02; publication year of the un-
       derlying book is not on the page. n.d. url: https://eng.libretexts.org/Bookshelves/
       Computer_Science/Programming_and_Computation_Fundamentals/Mathematics_for_
       Computer _ Science _ (Lehman _ Leighton _ and _ Meyer ) /02 % 3A _ Structures / 09 % 3A _
       Directed _ graphs _ and _ Partial _ Orders / 9 . 03 % 3A _ Adjacency _ Matrices (visited on
       Oct. 27, 2026).
 [7]   P. Paramadevan and S. Sotheeswaran. “Properties of Adjacency Matrix of a Graph and
       It’s Construction”. In: JSc EUSL (Journal of Science, Eastern University, Sri Lanka) 12.1
       (2021), pp. 13–21. doi: 10.4038/jsc.v12i1.29. url: https://www.fsc.esn.ac.lk/
       jsc/archive/12.1.2.pdf (visited on Oct. 27, 2026).
 [8] Path (graph theory). Wikipedia, English edition, revision of 5 June 2026 (oldid 1357845833)
     as fetched. n.d. url: https://en.wikipedia.org/wiki/Path_(graph_theory) (visited
     on Oct. 27, 2026).
 [9]   P. A. Petrosyan, V. V. Mkrtchyan, and R. R. Kamalyan. Grafneri tesutyun (Graph Theory:
       a study guide). File Grafneri_tesutyun.pdf, course textbook in Armenian. Supplied by
       the user. Yerevan State University Press, Yerevan. ISBN 978-5-8084-1995-7. Locators are
       printed page numbers. 2015.
[10]   Éric Schost. CS 341: Algorithms, Lecture 10: Graphs, breadth first search. Lecture slides,
       David R. Cheriton School of Computer Science, University of Waterloo, Winter 2026.
       2026. url: https://www.student.cs.uwaterloo.ca/~cs341/lectures/lecture10.pdf
       (visited on Oct. 27, 2026).
[11]   Eric W. Weisstein. Connected Graph. Wolfram MathWorld; no publication date on the
       page. n.d. url: https://mathworld.wolfram.com/ConnectedGraph.html (visited on
       Oct. 27, 2026).




                                                31
```

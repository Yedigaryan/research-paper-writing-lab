# Deliverable `dom`

Compiled PDF, 29 pages, rendered with pdftotext -layout.

```
Walks, Paths, and Connectivity Read from an Adjacency Matrix
                                            A Study Note




                                               Abstract
          A finite simple undirected graph with N vertices can be described by its adjacency matrix
      A, a square table of zeros and ones. This note answers three questions about it. First, the
      entry in row i and column j of the k-th power Ak counts the walks of length k from vertex
      ni to vertex nj . It counts walks, not paths, and the note shows by a counterexample why
      the difference matters. Second, the graph is connected if and only if every entry off the
      diagonal of A + A2 + · · · + AN −1 is positive. Both statements are proved in full. Third,
      a path between ni and nj is a walk from ni to nj in which no vertex occurs twice. The
      note follows the numbering and build order of the course textbook, sets every new idea in
      a single story about a village, and works two small examples with every matrix written out
      and computed by script.


1     Introduction
1.1   The three questions and where they came from
A graph is a set of points, called vertices, together with some lines, called edges, each joining
two vertices. When a graph has N vertices, one way to describe it completely is a square table
of N rows and N columns, the adjacency matrix A, which has a one in row i and column j
when vertices number i and number j are joined by an edge and a zero otherwise. This note
asks what such a table can tell us, and answers three questions.

 Q1 What does the entry (Ak )ij of the k-th power of A represent?

 Q2 How can one determine from A alone whether the graph is connected?

 Q3 What is the definition of a path between vertices ni and nj ?

    Questions Q1 and Q2 are written on a lecture whiteboard that was photographed twice [4,
5]. On the board, Q1 reads “What does A·ij represent” with a small mark in the place of the
exponent, and Q2 reads “How to know if graph is connected or not”. The board also gives
the definition “Graph is called connected if for any ni , nj there exists a path between nodes”, a
drawing of a graph on three vertices, and a three by three matrix labelled “adj.” [4, 5]. Question
Q3 was added by the assignment text, which we know only as it was reported to us and do not
reproduce here. Appendix B transcribes the board line by line.

1.2   One story for the whole note
Every definition, theorem, test, and worked example in this note is preceded by a paragraph
headed “In plain words”. Those paragraphs are told in one story and use no symbols. The story
is a small village. The village has houses. Roads join the houses in pairs. Each road joins two
different houses. Two houses have at most one road between them. Each road can be driven
in both directions. Table 1 fixes the story words once; each story word stands for exactly one
technical term, and the technical term is defined at the place named in the last column.


                                                   1
Table 1: The story dictionary. A story word is used only in the plain words paragraphs, and a
technical word is never used there.
            Story word                         Technical term      Defined in
            village                            graph               Definition 2.1
            house                              vertex              Definition 2.1
            road                               edge                Definition 2.1
            neighbours                         adjacent vertices   Definition 2.5
            table of roads                     adjacency matrix    Definition 2.9
            number of roads at a house         degree              Definition 2.14
            table of totals                    the sum S           Definition 4.1
            trip                               walk                Definition 2.19
            number of roads driven             length of a walk    Definition 2.19
            round trip                         closed walk         Definition 2.23
            trip with no road twice            trail               Definition 2.27
            route                              path                Definition 2.31
            round trip with no road twice      cycle               Definition 2.36
            ring                               simple cycle        Definition 2.36
            shortest trip between two houses   distance            Definition 2.40
            village in one piece               connected graph     Definition 2.48
            piece of a village                 component           Definition 2.52


   A trip may pass the same house twice and may drive the same road twice. A route never
passes a house twice. This difference is the main source of mistakes about the matrix, and the
whole note keeps the two words apart.

1.3   Conventions and assumptions
The photographs and the assignment text leave some points open. We settle each point as
follows and refer to these items by number.

  1. The graphs. The graph is finite, simple (no edge from a vertex to itself and no two edges
     with the same two ends), and undirected. The assignment text says so as reported to us,
     and it agrees with the matrix on the board, which is symmetric with zeros on the diagonal
     [4].

  2. The exponent. The mark above A in question Q1 is read as a positive integer exponent
     k, because the assignment text asks about Ak . In both photographs the mark looks like a
     small n or a pair of quotation marks, not clearly a k [4, 5]. The answer given below holds
     for every positive integer exponent, so it does not depend on which letter was written
     (Section 7.2).

  3. The example graph. On the board the drawing and the matrix disagree. The drawing
     shows three lines: between vertices 1 and 2 (with an arrowhead at 2), between 1 and
     3, and between 2 and 3. The matrix has rows 0 1 0, 1 0 1, 0 1 0, which records only the
     edges between 1 and 2 and between 2 and 3 [4, 5]. The board states that the graph is
     given through its adjacency matrix [4], so the matrix defines the example graph, and the
     arrowhead is treated as a stray mark because the matrix is symmetric. We report the
     mismatch and make no claim about which of the two the lecturer intended (Section 7.1).

  4. The word “path”. In the course, a path has no repeated vertex, as reported to us. The
     textbook calls such a walk a simple path [9, Definition 1.2.13, p. 22], and this note uses


                                               2
       “path” for it throughout. The board does not say which meaning of “path” it uses.
       The textbook’s own word “path” means something weaker, which this note calls a trail ;
       Section 5 compares the three usages.
    5. Notation. The vertices are n1 , . . . , nN as on the board, where N is the number of vertices;
       the textbook writes vi and n. The board writes (G, V ) for the graph and eij ∈ V in the
       line that defines Aij ; its V there stands for the set of edges, which the textbook writes E
       in G = (V, E) [4]. This note writes G = (V, E), calls an edge ni nj (or eij ), and writes |E|
       for the number of edges. The letters i, j, r are vertex numbers, k is an exponent or the
       length of a walk, I is the identity matrix, and S is the sum defined in Definition 4.1.
    6. Length zero. A single vertex counts as a walk of length 0. The textbook does not say
       whether this is allowed; we allow it because the textbook’s own distance property d(u, u) =
       0 needs it [9, printed p. 23]. A walk of length 0 is not counted as a cycle.
    7. Page numbers. Pages of the textbook are printed page numbers; the PDF page is one
       higher.

1.4    What the textbook contains and what it does not
The course textbook supplies the definitions and their numbers [9]. A full-text search of the
whole book for the adjacency matrix finds it only on printed pages 7, 11, 12, 34, and 61, and
finds neither a theorem that powers of the adjacency matrix count walks nor a matrix test for
connectivity [9]. We did not read every page, so this is a statement about the search and not
a proof that the book has no such result. Both results are therefore taken from other sources
and proved in full here: the walk-counting theorem from [2] and the connectivity test, whose
statement is in [7] and [1]. Where this note proves a statement itself, it says so in the first
sentence of the result and names a source that also states it.

1.5    The answers in brief
Q1 For k ≥ 1, the entry (Ak )ij is the number of walks of length k from ni to nj . It counts
    walks, not paths (Theorem 3.5 and proposition 3.10).
Q2 For N ≥ 2, the graph is connected if and only if every entry off the diagonal of A+A2 +· · ·+
    AN −1 is positive; equivalently, if and only if (I + A)N −1 has no zero entry (Theorem 4.6).
Q3 A path between ni and nj is a walk from ni to nj whose vertices are pairwise distinct
    (Definition 2.31); Section 5 compares this with the other usages.

1.6    Organisation
Section 2 builds the definitions in the textbook’s order, with its numbers. Section 3 answers Q1
and Section 4 answers Q2, including a breadth-first search alternative. Section 5 answers Q3 by
comparing conventions. Section 6 works two examples on three vertices, one connected and one
not. Section 7 states the limits, and Section 8 gives the direct answers. The appendices hold
the board transcription, a table of textbook numbers, the longer derivations, and the sources
and scripts. Directed graphs, weighted graphs, and eigenvalue methods are outside the scope of
this note.


2     Background: graphs, walks, and connectedness
This section builds the definitions in the order of the course textbook [9], with the textbook’s
numbers beside them. Each definition is followed by a remark on what it allows and forbids, an
example that satisfies it, and an example that does not.

                                                  3
2.1   Notation
Let G = (V, E) be a graph with vertex set V = {n1 , . . . , nN } and edge set E; let u, v, w denote
vertices and e, e′ denote edges. The board graph B is the graph with V = {n1 , n2 , n3 } and
E = {n1 n2 , n2 n3 }, the graph whose adjacency matrix is written on the board (Item 3). A walk
in B is written by the numbers of its vertices, so 1-2-3 means n1 , n2 , n3 .

2.2   Graphs, adjacency, and the adjacency matrix

In plain words. A village is a list of houses and a list of roads. Every road joins two different
houses. No two roads join the same two houses. A road has no direction.

Definition 2.1 (graph; textbook Definition 1.1.1, p. 9). A simple undirected graph is a pair
G = (V, E) where V is a finite nonempty set, whose elements are the vertices, and E is a set
of unordered pairs of distinct elements of V , whose elements are the edges [9, p. 9][2, Defini-
tion 1.1.1].

Remark 2.2. The definition forbids an edge from a vertex to itself (the two elements of the pair
must be distinct) and a repeated edge (E is a set). It forbids direction, because the pair is
unordered, so ni nj and nj ni are one edge. It allows a vertex with no edge at all.

Example 2.3. V = {n1 , n2 , n3 } and E = {n1 n2 , n2 n3 }: the board graph B, three houses in a
row.

Non-example 2.4. Two vertices joined by two edges, or a vertex joined to itself. The first
repeats an edge and the second is a loop, so neither is a simple graph.

In plain words. Two houses are neighbours when one road joins them directly. Nothing is
said about longer trips. A house is never its own neighbour.

Definition 2.5 (adjacent; textbook Definition 1.1.4, p. 11). Vertices u and v are adjacent if
uv ∈ E; each is then a neighbour of the other [9, p. 11].

Remark 2.6. Adjacency is symmetric, and no vertex is adjacent to itself because there are no
loops. It says nothing about connections through other vertices.

Example 2.7. In B the vertices n1 and n2 are adjacent.

Non-example 2.8. In B the vertices n1 and n3 are not adjacent, although a trip along two
edges joins them.

In plain words. Make a square table with one row and one column for every house. Write
a one where the row house and the column house share a road. Write a zero everywhere else.
This table describes the whole village.

Definition 2.9 (adjacency matrix; textbook p. 11, after Definition 1.1.6). Let G be a graph
with vertices n1 , . . . , nN . Its adjacency matrix is the N × N matrix A = (Aij ) with Aij = 1 if
ni and nj are adjacent and Aij = 0 otherwise. The textbook gives this rule without a definition
number [9, p. 11]; the board states it as Aij = 1 if eij ∈ V and 0 if eij ∈
                                                                          / V , with V standing for
the edge set (Item 5) [4, 5].

Remark 2.10. The only entries allowed are 0 and 1. The matrix depends on how the vertices
are numbered: renumbering moves rows and columns together.



                                                4
                                               
                                           0 1 0
Example 2.11. The board matrix A = 1 0 1 is the adjacency matrix of B: A12 = A21 =
                                           0 1 0
1, A23 = A32 = 1, and every other entry is 0.
                                           
                                     0 1 0
Non-example 2.12. The matrix 0 0 1 is not the adjacency matrix of any simple undi-
                                     0 1 0
rected graph, because A12 = 1 but A21 = 0. A matrix with a 1 on its diagonal (a loop) or an
entry 2 (a double edge) is not one either.

In plain words. The table of roads has easy features. It looks the same when flipped over
the line of squares from top left to bottom right. That line holds only zeros. Any such table of
zeros and ones comes from some village.

Proposition 2.13 (properties of A). The adjacency matrix A of a graph is symmetric (Aij = Aji
for all i, j) and has zero diagonal (Aii = 0 for all i). Conversely, every N ×N matrix of zeros and
ones that is symmetric with zero diagonal is the adjacency matrix of some graph with numbered
vertices.

Proof. The textbook states both parts [9, pp. 11–12]; see also [2, Section 1.1] and [7, property 9].
Adjacency is symmetric and no vertex is adjacent to itself (Remark after Definition 2.5), which
gives the first part. For the converse, join ni and nj exactly when the entry is 1. Symmetry
makes this a set of unordered pairs, and the zero diagonal excludes loops.

In plain words. The number of roads at a house tells how busy that house is.

Definition 2.14 (degree; textbook Definition 1.2.1, p. 16). The degree of a vertex ni is the
number of edges incident to ni . The textbook writes it dG (v) or d(v) [9, p. 16]; this note writes
deg(ni ) so that the letter d is kept for distance (Definition 2.40).

Remark 2.15. In a simple graph the degree is also the number of neighbours, because each
neighbour is joined to ni by exactly one edge.

Example 2.16. In B: deg(n1 ) = 1, deg(n2 ) = 2, deg(n3 ) = 1.

Non-example 2.17. deg(n1 ) ̸= 2 in B, although n2 and n3 can both be reached from n1 : only
edges at n1 count, and n3 is reached through n2 .

In plain words. Add up one row of the table. You get the number of roads at that house.
Add up the whole table. Every road has been counted twice, once from each end.

Proposition 2.18 (row sums are degrees). Row i of A, and column i, sums to deg(ni ), and the
sum of all entries of A is 2|E|.

Proof. This is proved here; [7, property 8] states the row sum for graphs that may also have
loops, and the textbook’s Theorem 1.2.1 (Euler) states that the degrees sum to 2|E| [9, p. 16].
Row i has a 1 in column j exactly when nj is a neighbour of ni . In a simple graph each
neighbour is joined to ni by exactly one edge and no edge joins ni to itself, so the number of
ones in row i is the number of edges at ni , which is deg(ni ). Column i is the same by symmetry
(Proposition 2.13). Adding the row sums over all i counts every edge twice, once from each end,
so the total is 2|E|.

   For B the row sums are 1, 2, 1 and the total is 4 = 2|E| with |E| = 2.

                                                 5
2.3    Walks, trails, paths, and cycles

In plain words. A trip is a list of houses, one after another. The next house is always at the
other end of a road from the house before. You may pass the same house twice. You may drive
the same road twice. The length of a trip is the number of roads you drove. A road driven twice
counts twice. Staying at home is also a trip, of length zero.

Definition 2.19 (walk; textbook Definition 1.2.10, p. 21). A walk of length k from u0 to uk is
a sequence u0 , e1 , u1 , . . . , uk−1 , ek , uk of vertices and edges with ei = ui−1 ui for 1 ≤ i ≤ k. It is
abbreviated by its vertex sequence u0 , u1 , . . . , uk . The length of the walk is the number k of its
edges, each edge counted as many times as it occurs [9, pp. 21–22][3, Definition 2.9.1].
Remark 2.20. Vertices and edges may repeat in a walk [9, p. 22]. The definition forbids only one
thing: two consecutive vertices that are not joined by an edge. By Item 6 the case k = 0, a single
vertex, is a walk. In a simple graph an edge is fixed by its two ends, so a walk is determined by
its vertex sequence; hence a walk of length k from ni to nj is the same as a sequence w0 , . . . , wk
of vertices with w0 = ni , wk = nj and wt−1 adjacent to wt for every t. This is a consequence of
Definition 2.1 and Definition 2.19 [3, Definition 2.9.1(a)], and the proof of Theorem 3.5 counts
such sequences.
Example 2.21. In B the sequence 1-2-1-2-3 is a walk of length 4 from n1 to n3 : its steps are
the edges n1 n2 , n2 n1 , n1 n2 , n2 n3 . The vertices n1 and n2 occur twice, and the edge n1 n2 is used
twice. The textbook’s example v1 , v3 , v2 , v4 , v3 , v2 , v4 , v3 , v5 in its Fig. 1.2.5 is a walk, of length
8 [9, p. 22].
Non-example 2.22. In B the sequence 1-3 is not a walk, because n1 n3 is not an edge of B
(A13 = 0). The textbook’s v3 , v1 , v4 , v2 , v3 , v5 is not a walk of its graph [9, p. 22].

In plain words. A round trip ends at the house where it began. That is the only new rule.

Definition 2.23 (closed walk; textbook Definition 1.2.11, p. 22). A walk u0 , . . . , uk is closed if
u0 = uk [9, p. 22].
Remark 2.24. A closed walk may repeat anything a walk may repeat. A walk of length 0 is
closed. In a simple graph no closed walk has length 1 (it would be a loop), and a closed walk of
length 2 is u, w, u, which uses one edge twice.
Example 2.25. In B the walk 2-1-2 is closed, of length 2.
Non-example 2.26. In B the walk 1-2-3 is not closed: it starts at n1 and ends at n3 .

In plain words. Now add one rule. Never drive the same road twice. You may still pass a
house twice, if you come back by a different road. Books use different words for such a trip.
Section 5 lists them.

Definition 2.27 (trail; textbook Definition 1.2.12, p. 22, where it is called “path”). A walk
u0 , . . . , uk is a trail if its edges u0 u1 , . . . , uk−1 uk are pairwise distinct [9, p. 22]. English usage
also calls this a trail [3, Definition 3.4.5][8].
Remark 2.28. A trail may repeat vertices, but not edges. A vertex can recur in a trail only if
the trip left it by one edge and returned by another. When the textbook writes “path” for this
object, this note writes “trail” or “the textbook’s path”.
Example 2.29. The textbook’s v1 , v3 , v2 , v4 , v3 , v5 is a trail: its edges are distinct, but v3 occurs
twice [9, p. 22].

                                                      6
Non-example 2.30. The textbook’s v1 , v3 , v2 , v4 , v3 , v2 , v4 , v3 , v5 is a walk but not a trail [9,
p. 22]. In B the walk 1-2-1-2-3 is not a trail, because the edge n1 n2 occurs twice.

In plain words. Now add a stronger rule. Never pass the same house twice. Then you also
never drive a road twice. Such a trip goes straight from start to end with no loop. It is called a
route.

Definition 2.31 (path, and path between ni and nj ; textbook Definition 1.2.13, p. 22, where it
is called “simple path”). A walk u0 , . . . , uk is a path if its vertices u0 , . . . , uk are pairwise distinct
[9, p. 22][3, Definition 2.9.1(c)]. A path between ni and nj is a path with u0 = ni and uk = nj ;
its length is k.
Remark 2.32. This is the answer to question Q3, under Item 4. A path forbids repeated vertices,
and therefore repeated edges (Proposition 2.35). It allows length 0 (a single vertex) and length
1 (one edge). It does not allow a closed walk of positive length, because its first and last vertices
would be equal; so for i = j the only path between ni and ni is the single vertex ni .
Example 2.33. In B the sequence 1-2-3 is a path between n1 and n3 , of length 2, and it is the
only one. The textbook’s v1 , v3 , v4 , v5 is a simple path [9, p. 22].
Non-example 2.34. In B the walk 1-2-3-2 is not a path, because n2 occurs twice, and neither
is 1-2-1-2-3 although it joins n1 to n3 . The textbook’s v1 , v3 , v2 , v4 , v3 , v5 is not a simple path
[9, p. 22].

In plain words. A route never drives a road twice. Here is why. A road driven twice would
bring you to a house for the second time.

Proposition 2.35 (every path is a trail). In a simple graph, a walk whose vertices are pairwise
distinct has pairwise distinct edges.
Proof. This is proved here; [3, Exercise 2.9] states it as an exercise. Let u0 , . . . , uk have distinct
vertices and take two steps a < b, the edges ua−1 ua and ub−1 ub . The vertex ub has an index
larger than a, so it differs from ua and from ua−1 . Thus ub is an end of the second edge and not
an end of the first, and the two edges are different.

In plain words. A ring is a round trip that passes no house twice. Only the start may appear
twice, because it is also the end. The textbook also names a looser round trip. It may pass a
house twice, but it never drives a road twice.

Definition 2.36 (cycle and simple cycle; textbook Definitions 1.2.14 and 1.2.15, p. 22). A trail
that is a closed walk is called a cycle (the textbook also says closed path) [9, Definition 1.2.14].
A cycle is simple if only its first and last vertices repeat; the simple cycle on n vertices is written
Cn , n ≥ 3 [9, Definition 1.2.15, p. 22].
Remark 2.37. A cycle in the textbook sense may repeat vertices (a figure eight is one); it forbids
repeated edges and open walks. A simple cycle forbids every repeated vertex except the closing
one. A closed trail of length 0 is not counted as a cycle (Item 6). English usage calls only the
simple cycle a “cycle” [3, Definition 2.10.1(b)], so Section 5 keeps the two senses apart. Cycles
are not needed for the main results; they are defined because the textbook’s build order includes
them.
Example 2.38. The textbook’s v1 , v3 , v4 , v2 , v1 is a simple cycle, and v3 , v2 , v1 , v3 , v5 , v4 , v3 is
a cycle in the sense of Definition 2.36 but not a simple cycle, because v3 occurs three times [9,
p. 22]. In the triangle drawn on the board (the graph T with edges n1 n2 , n1 n3 , n2 n3 ) the walk
1-2-3-1 is a simple cycle of length 3.

                                                       7
Non-example 2.39. In B the closed walk 1-2-1 is not a cycle, because the edge n1 n2 occurs
twice. In fact B has no cycle: a trail in B has at most |E| = 2 edges, a closed walk of length 1
does not exist, and a closed walk of length 2 repeats its edge (Remark after Definition 2.23); a
computer enumeration of the closed walks of length up to 6 agrees (Appendix D).

In plain words. Take two houses and look at the shortest trip between them. Count the
roads on it. That number tells how far apart the houses are. Staying at home is a trip of length
zero, so a house is zero far from itself. If no trip exists, the number is declared to be infinite.

Definition 2.40 (distance; textbook Definition 1.2.16, pp. 22–23). The distance d(u, v) between
vertices u and v is the length of a shortest (u, v)-path in the textbook’s sense (a trail) if at least
one exists, and +∞ otherwise [9, pp. 22–23]. By Proposition 2.47 the value is the same whether
trails, paths, or walks are used. The textbook lists three properties [9, p. 23]:

   1. d(u, v) ≥ 0, and d(u, v) = 0 if and only if u = v;

   2. d(u, v) = d(v, u);

   3. d(u, v) ≤ d(u, w) + d(w, v).

Hence, when any two vertices are joined by a path, the pair (V, d) is a metric space [9, p. 23].
Proposition C.2 derives the three properties from the definition.

Remark 2.41. The value +∞ is not an integer; it is how a missing connection shows up. No
value is negative, and no value is anything other than the length of an actual trip.

Example 2.42. In B: d(n1 , n2 ) = 1, d(n2 , n3 ) = 1, d(n1 , n3 ) = 2, and d(ni , ni ) = 0.

Non-example 2.43. In B the number 4 is not d(n1 , n3 ), although a walk of length 4 joins
them: distance is the minimum, not any length. In the graph with three vertices and the single
edge n1 n2 (Example 6.3) the distance d(n1 , n3 ) is not a number: it is +∞.

2.4    From a walk to a path

In plain words. Suppose you can drive from one house to another. Then you can do it
without passing any house twice. Look at your trip. If it passes some house twice, you went
round a loop. Cut the loop out. What is left is still a trip between the same two houses, and it
is shorter. Keep cutting until no loop is left.

Lemma 2.44 (every walk contains a path). Let u and v be vertices, equal or not. If there is a
walk of length k from u to v, then there is a path from u to v of length at most k, whose vertices
and edges all belong to the walk.

The textbook proves the case u ̸= v by induction on the length of the walk, without stating
the bound on the length [9, Lemma 1.2.1, p. 23]; the general statement with the bound is [3,
Corollary 2.9.7, p. 39]. The proof below follows the textbook’s method.

Proof. We prove by strong induction on k the statement S(k): every walk of length k, between
any two vertices u and v, contains a path between u and v of length at most k.
     Base case k = 0. A walk of length 0 is a single vertex, so it has no repeated vertex and is
itself a path, of length 0 ≤ 0.
     Induction hypothesis. Let k ≥ 1 and assume S(m) for every m < k.
     Step. Let u0 , . . . , uk be a walk with u0 = u and uk = v. If its vertices are pairwise distinct,
it is a path of length k, and we are done. Otherwise there are indices i < j with ui = uj . Form
W ′ = u0 , . . . , ui , uj+1 , . . . , uk (if j = k the part after ui is empty). Then W ′ starts at u. It ends

                                                      8
at v: if j < k its last vertex is uk , and if j = k it is ui = uj = uk . Every two consecutive vertices
of W ′ are consecutive in the old walk, except the pair (ui , uj+1 ) = (uj , uj+1 ), which is also a
step of the old walk. So W ′ is a walk from u to v, of length i + (k − j) < k. By S(m) with
m = i + (k − j) < k, W ′ contains a path from u to v of length at most m < k, and every vertex
and edge of W ′ belongs to the old walk. This proves S(k), and by induction the lemma.

Example 2.45. In B the walk 1-2-1-2-3 has u0 = u2 = n1 ; cutting gives the path 1-2-3. The
closed walk 2-1-2 is cut down to the single vertex n2 , a path of length 0. For the textbook’s
walk of length 8 two cuts give walks of length 5 and then 2, the path v1 , v3 , v5 (Appendix D).

In plain words. A route passes each house at most once. So a route cannot be longer than
the number of houses minus one. Hence if any trip exists, a short trip exists.

Corollary 2.46 (bound on path length). In a graph with N vertices every path has at most
N − 1 edges. Hence if some walk joins u and v, a walk of length at most N − 1 joins them.
Proof. A path of length k lists k + 1 pairwise distinct vertices, and there are only N vertices, so
k + 1 ≤ N [3, Section 2.9.4]. For the second part, apply Lemma 2.44: the path inside the walk
has length at most that of the walk and at most N − 1, and a path is a walk.

   In B we have N = 3 and the longest path has two edges.
Proposition 2.47 (shortest walk, trail, and path agree). For vertices u, v the lengths of a
shortest (u, v)-walk, of a shortest (u, v)-trail, and of a shortest (u, v)-path are equal, and all
three are infinite together.
This is proved here (Appendix C.5); the remark that a shortest walk is a shortest path is also
made in [3, Section 2.9.4].

2.5   Connected graphs and components

In plain words. Look at a village. Sometimes you can reach every house from every other
house. Then the village is in one piece. If one house is cut off, it is not in one piece.

Definition 2.48 (connected; textbook Definition 2.1.1, p. 48; board). A graph G is connected
if for any two vertices u and v of G there is a (u, v)-path in G [9, p. 48]. The board states the
same definition: “Graph is called connected if for any ni , nj there exists a path between nodes”
[4, 5].
Remark 2.49. First, the textbook’s “path” here is its Definition 1.2.12, a trail [9, p. 48]. The
definition does not depend on the choice among walk, trail, and path: if a walk joins two vertices
then a path joins them (Lemma 2.44), and a path is a trail (Proposition 2.35) and a walk, so
the three readings accept exactly the same graphs; this is also stated in [3, Proposition 2.9.10].
Second, “any two vertices” includes u = v, and such a pair is always joined by the walk of length
0; so the definition may be read as “any two different vertices” without change. The textbook
does not discuss the case u = v. Third, the definition forbids exactly one thing: a pair of vertices
with no trip between them.
Example 2.50. B is connected: n1 and n3 are joined by the path 1-2-3, and the other pairs
by one edge. The textbook’s examples are the complete graphs, the complete bipartite graphs,
and the three graphs of its Fig. 2.1.1 [9, p. 48].
Non-example 2.51. Three vertices with the single edge n1 n2 are not connected: no walk leaves
n3 , so the pair n1 , n3 has no path. The graph of the textbook’s Fig. 2.1.2 is not connected and
has four components [9, p. 49].

                                                  9
In plain words. Look at a village that is not in one piece. It falls into pieces. Inside one
piece every house can reach every other house. No road joins two different pieces. A village in
one piece has exactly one piece.

Definition 2.52 (component; textbook p. 49, in prose, and Remark 2.1.1). On V define u ∼ v
to mean that G has a (u, v)-path. This relation is reflexive, symmetric, and transitive, so V
splits into classes V1 , . . . , Vp . The subgraphs Gj = G[Vj ], consisting of the vertices in Vj and the
edges of G that join two of them, are the connected components of G [9, p. 49]. The textbook’s
Remark 2.1.1 states that G is connected if and only if it has exactly one component [9, p. 49];
see also [3, Definition 2.9.12].

Remark 2.53. A component is a whole class: a vertex that can be reached from a vertex of Vj
lies in Vj .

Example 2.54. The graph with the single edge n1 n2 on three vertices has the two components
G[{n1 , n2 }] and G[{n3 }]; B has the single component G[{n1 , n2 , n3 }].

Non-example 2.55. G[{n1 }] is not a component of the graph with the single edge n1 n2 ,
although it is connected: n2 can be reached from n1 , so n2 is in the same class.


3     Question 1: what the entry (Ak )ij represents
The answer is short and the proof is an induction. Before the proof we fix what a power of a
matrix is.

3.1    Matrix products and powers

In plain words. To multiply the table of roads by itself, take one row house and one column
house. Go along the row and down the column together. Multiply the two numbers you meet
at each step and add up the results. Repeat for every pair of houses. The result is a new table
of the same size.

Definition 3.1 (matrix product and power). For N × N matrices X and Y , the product XY
is the N × N matrix with
                                            N
                                            X
                                  (XY )ij =    Xir Yrj .                            (1)
                                                    r=1

The powers of A are A1 = A and Ak = Ak−1 A for k ≥ 2.

Remark 3.2. In this section the exponent k is a positive integer. The power A0 , which is the
identity matrix I (ones on the diagonal, zeros elsewhere), is used only in Section 4.

Example 3.3. For the board matrix A of Definition 2.9, the entry (A2 )11 is 0 · 0 + 1 · 1 + 0 · 0 = 1.

Non-example 3.4. A2 is not the matrix of squared entries. For the board matrix, (A2 )22 =
1 · 1 + 0 · 0 + 1 · 1 = 2, while A222 = 0.

3.2    The theorem

In plain words. Take the table of roads and multiply it by itself. Each number in the new
table counts trips of two roads. The trips run from the row house to the column house. Multiply
again and the numbers count trips of three roads. The count includes trips that turn back. So
the table counts trips, not routes.


                                                   10
Theorem 3.5 (walk counting). Let A be the adjacency matrix of a simple undirected graph G
with vertices n1 , . . . , nN , and let k ≥ 1 be an integer. Then (Ak )ij is the number of walks of
length k from ni to nj , for all i, j.

This answers question Q1: the entry is a number, and it counts walks. The theorem is stated for
simple graphs in [2, Theorem 1.1.3] and [1, Theorem 1], and for digraphs and multidigraphs, of
which a simple undirected graph is the symmetric case, in [3, Theorem 4.5.10, pp. 120–121] and
[6, Corollary 9.3.3]. The textbook does not contain it (Section 1). The proof below is written
here and follows the standard route of [2, proof of Theorem 1.1.3]: induction on k, splitting the
walks by their second-last vertex.
Remark 3.6. The theorem allows i = j, so it counts closed walks, and it counts every walk once,
with repeated vertices and edges allowed. It forbids reading the number as a count of paths
(Proposition 3.10).

Example 3.7. For the board graph, (A2 )13 = 1: the only walk of length 2 from n1 to n3 is
1-2-3 (Example 6.1).

Non-example 3.8. (A2 )12 = 0 does not say that n1 and n2 are unconnected. It says only that
no walk of length exactly 2 joins them; walks of length 1 and of length 3 do.

Proof. Write Wk (i, j) for the number of walks of length k from ni to nj . We prove Wk (i, j) =
(Ak )ij for all i, j, by induction on k ≥ 1. By Remark 2.20 we count vertex sequences w0 , . . . , wk
with w0 = ni , wk = nj , and wt−1 adjacent to wt for each t.
    Base case k = 1. A walk of length 1 from ni to nj is a sequence (ni , nj ) with ni and
nj adjacent. There is exactly one such sequence if they are adjacent and none otherwise. So
W1 (i, j) = Aij = (A1 )ij .
    Induction hypothesis. Let k ≥ 2 and suppose Wk−1 (i, j) = (Ak−1 )ij for all i, j.
    Inductive step. Fix i and j. Every walk w0 , . . . , wk of length k from ni to nj has a second-last
vertex wk−1 . Write wk−1 = nr with r ∈ {1, . . . , N } and sort the walks into N classes by the
value of r. Each walk has exactly one second-last vertex, so the classes are disjoint and together
contain every walk:
                  N
                  X                                                                         
    Wk (i, j) =         number of walks of length k from ni to nj with second-last vertex nr .
                  r=1

We claim that class r has exactly Wk−1 (i, r) Arj members.

    If nr and nj are not adjacent, then Arj = 0, and no walk can have nr followed by nj , so
     the class is empty.

    If nr and nj are adjacent, then Arj = 1. Deleting the last vertex of a walk in the class
     leaves w0 , . . . , wk−1 , a walk of length k − 1 ≥ 1 from ni to nr . Conversely, appending nj
     to any walk of length k − 1 from ni to nr gives a walk of length k from ni to nj , because
     the new pair nr , nj is adjacent, and its second-last vertex is nr . Deleting and appending
     undo each other, so they match the class one to one with the walks of length k − 1 from
     ni to nr , and the class has Wk−1 (i, r) members.

Therefore Wk (i, j) = r Wk−1 (i, r)Arj . By the induction hypothesis this equals r (Ak−1 )ir Arj ,
                          P                                                         P
which is (Ak−1 A)ij = (Ak )ij by (1). This proves the statement for k, and by induction for all
k ≥ 1.




                                                  11
Why the argument is valid. Counting could go wrong in two places: a walk counted
twice or missed, and a count that is not 0 or 1 where adjacency is concerned. Sorting by the
second-last vertex counts each walk exactly once, and the deleting-and-appending match is one
to one. Simplicity is used twice: it identifies a walk with its vertex sequence (Remark 2.20),
and it makes Arj , the number of edges between nr and nj , equal to 0 or 1. Undirectedness is
not used in the induction itself; it only makes A symmetric, which gives part (c) of the next
corollary. For a multigraph the same argument would count walks with multiplicity if Arj were
the number of edges, which agrees with the sources that state the theorem for multidigraphs [3,
Theorem 4.5.10].

3.3   Consequences

In plain words. A count is never negative and always a whole number. The table of trips
looks the same when flipped over the line of squares from top left to bottom right. That is
because every trip can be driven backwards. A positive number means that at least one such
trip exists. A trip of two roads from a house back to itself goes out along a road. Then it comes
back along the same road.

Corollary 3.9 (consequences of walk counting). For a simple undirected graph and k ≥ 1:

 (a) every entry of Ak is a nonnegative integer, and a sum of powers of A has a positive (i, j)
     entry if and only if some summand does;

 (b) (Ak )ij > 0 if and only if there is a walk of length exactly k from ni to nj ;

 (c) Ak is symmetric;

 (d) (A2 )ii = deg(ni ) for every i, hence trace(A2 ) = 2|E|.

Proof. Parts (a) to (c) are derived here from Theorem 3.5; part (d) is stated in [2, remark
after Theorem 1.1.3]. (a) and (b): by Theorem 3.5 the entry is a count; a sum of nonnegative
numbers is positive if and only if one of them is. (c): reversing the vertex sequence of a walk
matches the walks from ni to nj one to one with the walks from nj to ni , because edges are
unordered; so (Ak )ij = (Ak )ji . (d): a walk of length 2 from ni to ni has the form ni , nr , ni with
nr a neighbour of ni , and there is one for each neighbour, so (A2 )ii is the number of neighbours,
which is deg(ni ). The trace is the sum of the diagonal, so it is the sum of the degrees, which is
2|E| by Proposition 2.18.

3.4   The warning: walks are not paths

In plain words. A trip may turn back and pass the same house twice. A route never passes
a house twice. The table counts trips, so it counts the turn-back trips too. A house with a
neighbour always has a two-road trip that goes out and comes back. That trip is not a route.
So the table cannot be counting routes.

Proposition 3.10 (the entries do not count paths). (a) If ni has at least one neighbour, then
    (A2 )ii = deg(ni ) > 0, but there is no trail and no path from ni to ni of length 2.

 (b) In the board graph, (A3 )12 = 2, but the only path or trail from n1 to n2 has length 1. More
     fully, Table 2 lists, for k = 1, . . . , 5, the entry (Ak )12 and the number of trails and of paths
     among the walks it counts.
   In particular the entries of Ak are not counts of paths, and not counts of trails.



                                                  12
Walks, not paths, are counted also according to [1, Section 1, remark after Theorem 1] and [3,
Example 2.9.2], which gives 1, 2, 1 as a walk that is not a path. The proposition and its proof
are written here.

Proof. (a) The first claim is Corollary 3.9(d). The walks of length 2 from ni to ni are the
sequences ni , nr , ni . Each repeats the vertex ni , so it is not a path (Definition 2.31), and each
uses the edge ni nr twice, so it is not a trail (Definition 2.27). Under the course convention the
only path from ni to ni is the single vertex, of length 0 (Remark 2.32).
    (b) The walks counted by (A3 )12 are 1-2-1-2 and 1-2-3-2 (Example 6.1); the first repeats the
edge n1 n2 and the second repeats the vertex n2 , so neither is a trail or a path. Every path in
B has at most N − 1 = 2 edges (Corollary 2.46); a path of length 2 from n1 to n2 would need
a vertex adjacent to both, and there is none, so the only path from n1 to n2 is the edge. A
trail has at most |E| = 2 edges, and no walk of length 2 joins n1 to n2 because (A2 )12 = 0, so
the only trail from n1 to n2 is also the edge. The rows of Table 2 come from an enumeration
by script (Appendix D); the walk counts in them equal the entries of Ak computed by matrix
multiplication.


Table 2: Walks, trails, and paths from n1 to n2 in the board graph, by length k. The second
column is (Ak )12 .
                  k   walks = (Ak )12   trails among them     paths among them
                  1          1                   1                      1
                  2          0                   0                      0
                  3          2                   0                      0
                  4          0                   0                      0
                  5          4                   0                      0



What a positive entry does guarantee. If (Ak )ij > 0 then a walk of length k exists
(Corollary 3.9(b)), and then a path of length at most k exists (Lemma 2.44). So the warning
does no harm to the connectivity test of Section 4, but the value of an entry is not a count
of paths. The mistake of reading the entry as a count of paths is made in one of the sources
(Section 7.4).


4     Question 2: deciding connectivity from A
Connectedness is defined by paths (Definition 2.48), but powers of A count walks (Theorem 3.5).
The bridge is Lemma 2.44: a walk can always be cut down to a path. The textbook states no
matrix test for connectivity (Section 1). The test below is stated in [7, Theorem 2] and [11], and
in the form with (I + A)N −1 in [1, Theorem 2]. The two web sources that give a proof prove
it loosely, speaking of “paths” where walks are meant (Section 7.4), so the proof is written out
here. Throughout, G has N ≥ 2 vertices; Remark 4.9 treats N = 1.

4.1   The sum of the first N − 1 powers

In plain words. We need one table that gathers all the short trips. For each pair of houses,
count the trips of one road, of two roads, and so on. Stop at one road fewer than the number of
houses. Add the counts for each pair. Call the result the table of totals.




                                                 13
Definition 4.1 (the sum S). For a graph with N ≥ 2 vertices, let

                                    S = A + A2 + · · · + AN −1 ,                                (2)

the sum of the first N − 1 powers of A, added entry by entry. This notation is introduced here
and is not the textbook’s.

Remark 4.2. By Theorem 3.5, Sij is the number of walks from ni to nj whose length is between
1 and N − 1; so every entry of S is a nonnegative integer (Corollary 3.9(a)). The definition
needs N ≥ 2, since for N = 1 the sum would be empty.

Example 4.3. For the board graph (N = 3), S = A+A2 and its first row is 1 1 1 (Example 6.2).

Non-example 4.4. A2 alone is not S for N = 3, and neither is A alone. For the board graph
A2 has the zero entry (1, 2) although n1 and n2 are joined by an edge, and A has the zero
entry (1, 3) although n1 and n3 are connected; either matrix alone would wrongly report “not
connected”.

4.2   The test and its proof

In plain words. We want a quick check for a village. We only have the table of roads. From
the table we can count trips. Count the trips with one road, two roads, and so on, for each pair
of houses. If no pair of different houses has a total of zero, the village is in one piece. We never
need trips longer than one road fewer than the number of houses. A trip that wastes time can
always be shortened.

Proposition 4.5 (one pair at a time). Let G have N ≥ 2 vertices and let i ̸= j. The following
three statements are equivalent.

  (i) There is a path between ni and nj (Definition 2.31).

 (ii) There is an integer k with 1 ≤ k ≤ N − 1 and (Ak )ij > 0.

(iii) Sij > 0.

Theorem 4.6 (the connectivity test). Let G be a graph with N ≥ 2 vertices and adjacency
matrix A. The following are equivalent.

 (a) G is connected.

 (b) Every entry off the diagonal of S = A + A2 + · · · + AN −1 is positive.

 (c) Every entry of (I + A)N −1 is positive.

This answers question Q2. The equivalence of (a) and (b) is stated in [7, Theorem 2]; the
equivalence of (a) and (c) in [1, Theorem 2]. The proofs below are written here.

Proof of Proposition 4.5. (i) ⇒ (ii). A path between ni and nj is a walk, say of length ℓ. By
Corollary 2.46 there is a walk from ni to nj of length k ≤ N − 1. Since ni ̸= nj the walk has at
least one step, so k ≥ 1. By Theorem 3.5, (Ak )ij ≥ 1.
    (ii) ⇒ (iii). Each term of Sij = Aij + (A2 )ij + · · · + (AN −1 )ij is a nonnegative integer
(Corollary 3.9(a)), and the term with index k is positive, so the sum is positive.
    (iii) ⇒ (ii). A sum of nonnegative terms is positive only if some term is positive.
    (ii) ⇒ (i). If (Ak )ij > 0 then, by Theorem 3.5, some walk of length k joins ni to nj . By
Lemma 2.44 there is a path between ni and nj .



                                                14
Proof of Theorem 4.6. Statement (a) says that for every pair of vertices there is a path (in the
sense of Definition 2.48). The pairs with u = v are always joined by the walk of length 0
(Remark 2.49), so (a) holds if and only if a path joins ni and nj for every i ̸= j (by Remark 2.49
the reading of “path” does not matter). By Proposition 4.5 this holds if and only if Sij > 0 for
every i ̸= j, which is (b). By Proposition 4.17 with m = N − 1, it holds if and only if every
off-diagonal entry of (I + A)N −1 is positive; the diagonal entries are always positive there; so it
holds if and only if (c).

Corollary 4.7 (components from S). For any graph, connected or not, with N ≥ 2, and i ̸= j:
Sij > 0 if and only if ni and nj lie in the same component.

Proof. Proposition 4.5 does not use the connectivity of G; statement (i) says ni ∼ nj , which is
the definition of lying in the same class (Definition 2.52).

Remark 4.8 (by-product: distance). If ni and nj are in the same component and i ̸= j, then
d(ni , nj ) is the smallest k ≥ 1 with (Ak )ij > 0, and this k is at most N − 1. Indeed (Ak )ij > 0
exactly when a walk of length k exists (Corollary 3.9(b)), and the length of a shortest walk is
the distance (Proposition 2.47). Two sources state this [6, Section 9.3] [7, Theorem 3].
Remark 4.9 (the diagonal, and N = 1,   N =2). The test looks only at entries off the diagonal.
                                        0 1
For N = 2 and one edge, S = A =               has zeros on the diagonal although the graph is
                                        1 0
connected, so the diagonal of S cannot be required to be positive. For N ≥ 3 and G connected
the diagonal of S is positive anyway: every vertex has a neighbour, and (A2 )ii = deg(ni ) > 0
by Corollary 3.9(d). For N = 1 there is no pair of different vertices, G is connected, and
(I + A)0 = I = [1] has no zero entry; the sum S is empty, so the test is stated for N ≥ 2.

4.3   The test as a procedure

In plain words. Here is the check, step by step. First write the table of roads. Then multiply
the table by itself again and again. After each step, add the new counts to a running total. Stop
one step before the number of houses. Look at every pair of different houses. If any total is
zero, those two houses cannot reach each other. If no total is zero, everyone can reach everyone.

Test 4.10 (matrix test for connectivity). Input: the adjacency matrix A of a graph with N ≥ 2
vertices.

  1. Set P = A and S = A.

  2. For k = 2, 3, . . . , N − 1: replace P by P A (now P = Ak ) and add P to S.

  3. Look at the entries Sij with i ̸= j. If one of them is 0, the graph is not connected; if none
     is 0, it is connected.

Equivalent form: compute (I + A)N −1 and report “connected” if it has no zero entry.

Remark 4.11. The test allows any graph with N ≥ 2 vertices. It forbids stopping early (Propo-
sition 4.14) and forbids applying it to a directed graph, which this note does not treat. A zero
at (i, j) means, by Corollary 4.7, that ni and nj are in different components.

Example 4.12. The board matrix gives “connected” and the matrix with the single edge n1 n2
gives “not connected”; both are worked in Examples 6.2 and 6.3.

Non-example 4.13. Computing only AN −1 is not the test: for the board graph A2 has the
zero entry (1, 2) although the graph is connected.


                                                15
4.4       Why N − 1 is enough and N − 2 is not
Enough. If a walk between two different vertices exists at all, then a walk of length at most
N − 1 exists (Corollary 2.46), because a shortest connection repeats no vertex and a repeat-
free connection has at most N vertices. Adding powers beyond N − 1 cannot change which
off-diagonal entries are positive.
In plain words. Take four houses in a row. To go from the first house to the last, you must
pass every house in between. That takes three roads. If we counted only trips of up to two
roads, we would miss this pair. We would say the village is cut in two, and we would be wrong.
The same idea works for any row of houses.

Proposition 4.14 (N − 1 cannot be lowered to N − 2). For every N ≥ 3 there is a connected
graph with N vertices for which the sum A + · · · + AN −2 has a zero entry off the diagonal.

Proof. This is proved here. Take the graph with edges n1 n2 , n2 n3 , . . . , nN −1 nN . Each step of
a walk changes the vertex number by exactly 1, and to go from n1 to nN the number must
increase by N − 1, so every walk from n1 to nN has length at least N − 1. By Theorem 3.5,
(Ak )1N = 0 for 1 ≤ k ≤ N − 2, so the (1, N ) entry of A + · · · + AN −2 is 0, although the graph
is connected.

Example 4.15. Path graph on four vertices with edges n1 n2 , n2 n3 , n3 n4 (N = 4):
                                                                          
                0 1 0 0                 1 0 1 0                      0 2 0 1
              1 0 1 0
                           , A2 = 0 2 0 1 , A3 = 2 0 3 0 ,
                                                                            
          A= 0 1 0 1               1 0 2 0                  0 3 0 2
                0 0 1 0                 0 1 0 1                      1 0 2 0
                                                                                
                             1   1   1   0                        1       3   1   1
                             1   2   1   1                       3       2   4   1
                  A + A2 =                       A + A2 + A3 = 
                                                               
                                          ,                                       .
                           1    1   2   1                     1        4   2   3
                             0   1   1   1                        1       1   3   1
With N − 2 = 2 powers the (1, 4) entry is 0 and the test would wrongly say “not connected”;
with N − 1 = 3 powers every entry is positive.


Table 3: The path graph on N vertices: the smallest k with (Ak )1N > 0, and the (1, N ) entry
of the sum with N − 2 powers and with N − 1 powers.
      N    smallest k with (Ak )1N > 0   (1, N ) of A + · · · + AN −2   (1, N ) of A + · · · + AN −1
      3                2                              0                              1
      4                3                              0                              1
      5                4                              0                              1
      6                5                              0                              1
      7                6                              0                              1
      8                7                              0                              1


Remark 4.16. Which graphs fail with N − 2 powers? By Remark 4.8 a connected graph fails
exactly when some pair has distance N − 1. A shortest path with N − 1 edges contains all
N vertices, and an edge between two vertices of it that are not consecutive would shorten
the distance between its ends; so the graph is that path and nothing else. The failing graphs
are therefore exactly the labelled paths, of which there are N !/2 for N ≥ 3: 3, 12, 60, 360 for
N = 3, 4, 5, 6. The enumeration of Table 6 gives the same four numbers.

                                                 16
4.5    The form (I + A)m

In plain words. There is a second form of the check. Let every house also stay where it is for
one step. Then count again. The answer is the same. You may even go on past the number of
houses minus one. The pattern of zeros does not change.

Proposition 4.17 (powers of I + A). Let N ≥ 2 and let m ≥ N − 1 be an integer. Every
diagonal entry of (I + A)m is at least 1, and for i ̸= j the entry ((I + A)m )ij is positive if and
only if there is a path between ni and nj . Hence G is connected if and only if (I + A)m has no
zero entry, for any one such m, and an exponent m = 2t ≥ N − 1 is reached by t squarings of
I + A.

The case m = N − 1 is the form stated in [1, Theorem 2]. The proof, by binomial expansion, is
written in Appendix C.4.

4.6    An alternative: breadth-first search

In plain words. There is another way, and it needs no counting. Stand at one house and
mark it. Then mark every house next to it. Then mark every house next to those. Keep going
until no new house appears. If every house is marked, the village is in one piece.

Remark 4.18 (breadth-first search). Breadth-first search from a start vertex s keeps a queue of
discovered vertices and repeatedly takes the vertex at the front and discovers its undiscovered
neighbours; its correctness statement is that for every vertex v there is a walk from s to v if
and only if v is discovered when the search ends, so G is connected if and only if every vertex
is discovered from one start vertex [10, slides 6 and 10]. When the graph is given by adjacency
lists the search takes time proportional to the number of vertices plus the number of edges [10,
slides 9 and 10]. It gives the same answer as the matrix test on every labelled graph with at most
six vertices (Table 6), a computer check and not a proof, and it lists the components directly.


5     Question 3: a path between two vertices, and the three usages
      of the word
The answer to question Q3 is Definition 2.31, which sits in its place in the textbook’s build
order: a path between ni and nj is a walk from ni to nj whose vertices are pairwise distinct.
This section adds only what is new there: how that word compares with the other usages, and
what depends on the choice. The course meaning of “path” (no repeated vertex) comes from the
assignment text as reported to us (Item 4); the textbook supplies the definition under another
name, and the board does not say which meaning it uses [4, 5].

5.1    Three usages
The same two properties of a walk, “no repeated edge” and “no repeated vertex”, get different
names in different places. In the textbook, “path” means no repeated edge [9, Definition 1.2.12,
p. 22] and “simple path” means no repeated vertex [9, Definition 1.2.13, p. 22]. In the English
text used here, a path has distinct vertices and a trail has distinct edges [3, Definitions 2.9.1(c)
and 3.4.5]; an encyclopedia article gives the same two definitions and adds that a path has
distinct vertices “by most definitions” [8]. The same article records that some authors do not
require distinct vertices in a path and say “simple path” for a path with distinct vertices [8],
which is the textbook’s pattern; so the course convention is one of at least two in use. For
“cycle” the textbook’s word (Definition 2.36) allows repeated vertices, while the English text
defines a cycle as a closed walk with at least three steps whose vertices w0 , . . . , wk−1 are distinct

                                                  17
[3, Definition 2.10.1(b)], which is the textbook’s simple cycle. Table 4 puts the usages side by
side.

Table 4: The naming of walks in the textbook, in English usage, and in this note. The textbook
words are given in English translation.
      Property of the walk          Textbook (definition     English usage   This note
                                    number)
      any sequence of steps         walk (1.2.10)            walk            walk
      along edges
      first vertex equals last      closed walk (1.2.11)     closed walk     closed walk
      vertex
      no repeated edge, ver-        “path” (1.2.12)          trail           trail
      tices may repeat
      no    repeated      vertex    “simple path” (1.2.13)   path            path
      (hence     no     repeated
      edge)
      closed, no repeated edge,     “cycle” or “closed       closed trail    cycle (textbook
      vertices may repeat           path” (1.2.14)                           sense)
      closed, only first and last   “simple        cycle”    cycle           simple cycle
      vertex repeat, at least       (1.2.15)
      three steps

The word “path” therefore has three meanings across the sources: no repeated edge (textbook),
no repeated vertex (English text and course), and, in some authors, either. The last column of
Table 4 gives each meaning one name in this note and is used without exception.

5.2     What depends on the choice and what does not
Existence does not depend on it. For two different vertices, a walk, a trail, and a path between
them exist together or not at all: a walk contains a path (Lemma 2.44), and a path is a trail
(Proposition 2.35) and a walk. So every statement of the form “there is a path between ni and
nj ” has the same truth value under the textbook’s reading and under the course reading, and
so do connectivity (Remark 2.49) and distance (Proposition 2.47). The board’s definition of
connected is therefore the textbook’s Definition 2.1.1 under either reading.
    Counts do depend on it. The number of walks, of trails, and of paths from ni to nj are
different numbers in general, and only the first is given by a power of A (Proposition 3.10).
In the board graph every trail is a path (Table 5), so that graph cannot show the difference
between the two readings; it needs a graph with a cycle, such as the textbook’s own example
graph (Definition 2.27).
    Length zero. By Item 6 a single vertex is a path of length 0; this matches the English text,
which calls (5) a walk of length 0 and a path [3, Example 2.9.2]. It matters only for i = j, since
for i ̸= j a path has length at least 1.


6      Worked examples
This section works the board graph through Section 3 and Section 4, and adds one graph that
is not connected. Every matrix, sum, and count in this section and in earlier examples was
computed by a script (Appendix D) and then copied into the text by the same script.




                                                      18
                 2                                2                            2

         1                3             1                    3         1                3

         (a) board drawing             (b) board graph B                (c) one edge only

Figure 1: (a) The board drawing as read from the photographs: a line from 1 to 2 with an
arrowhead at 2, a line from 1 to 3, and a line from 2 to 3. (b) The graph B whose adjacency
matrix is the board matrix: the edges n1 n2 and n2 n3 only. (c) The graph with the single edge
n1 n2 , used as the example that is not connected. The positions of the vertices are our choice.


6.1   The powers of the board matrix

In plain words. We take the village from the board. It has three houses in a row. The first
and last houses each have one road. The middle house has two roads. We multiply the table
of roads by itself several times. Then we list every trip, so that the reader can see that each
number is right.

Example 6.1 (powers of the board matrix). The graph is B (Figure 1(b)) with
                                                                  
                  0 1 0                   1 0 1                 0 2 0
            A = 1 0 1 ,         A2 = 0 2 0 ,        A3 = 2 0 2 ,
                  0 1 0                   1 0 1                 0 2 0
                                                                
                                  2 0 2                      0 4 0
                           A4 =  0 4 0  ,            A5 = 4 0 4 .
                                  2 0 2                      0 4 0
Reading of A2 and A3 by walks. The walks of length 2 are: from n1 to n1 , 1-2-1; from n1 to n3 ,
1-2-3; from n2 to n2 , 2-1-2, 2-3-2; from n3 to n3 , 3-2-3. The walks of length 3 are: from n1 to
n2 , 1-2-1-2, 1-2-3-2; from n2 to n3 , 2-1-2-3, 2-3-2-3. Each count equals the corresponding matrix
entry (Theorem 3.5).
                                          2)                                                 3
                                                  P
     The  induction   step by  hand.   (A   22 =    r A2r Ar2 = 1 · 1 + 0 · 0 + 1 · 1 = 2. (A )12 =
       2
P
   r (A )1r Ar2 = 1 · 1 + 0 · 0 + 1 · 1 = 2, where the term r = 1 is the walk 1-2-1 extended by a
step to n2 , giving 1-2-1-2, and the term r = 3 is the walk 1-2-3 extended by a step to n2 , giving
1-2-3-2.
     Patterns. The diagonal of A2 is (1, 2, 1), the degrees, and trace(A2 ) = 4 = 2|E| (Corol-
lary 3.9(d)). Also A3 = 2A, and therefore Ak+2 = Ak−1 A3 = 2Ak−1 A = 2Ak for every k ≥ 1;
the matrices above agree with this for k = 1, 2, 3.


Table 5: Walks, trails, paths, and closed walks of each length in the board graph, counted over
all pairs of start and end vertices by enumeration. For k ≥ 1 the number of walks is the sum of
all entries of Ak .
                          length k walks trails paths closed walks
                              0       3       3          3        3
                              1       4       4          4        0
                              2       6       2          2        4
                              3       8       0          0        0
                              4       12      0          0        8



                                                  19
   Table 5 shows the effect of Proposition 3.10: the number of walks grows with k, while trails
and paths stop at length 2, because B has two edges and N − 1 = 2. It also shows that in B
every trail is a path: B has no cycle (Definition 2.36), and a trail that repeated a vertex would
contain a closed trail between the two visits.

6.2   A connected graph

In plain words. Take three houses in a row. A road joins the first and second house. Another
road joins the second and third house. The first and third house share no road. Can you still
go from one to the other? Yes, through the middle house. We expect the check to say that the
village is in one piece.

Example 6.2 (connected: the board graph, N = 3, N − 1 = 2).
                                                                                       
      0 1 0             1 0 1                       1 1 1                               2 2 1
A = 1 0 1 , A2 = 0 2 0 , S = A + A2 = 1 2 1 ,                         (I + A)2 = 2 3 2 .
      0 1 0             1 0 1                       1 1 1                               1 2 2

S has no zero entry (in particular none off the diagonal), so by Theorem 4.6(b) the graph is
connected. (I + A)2 has no zero entry, so by Theorem 4.6(c) the graph is connected; the two
answers agree. The entry A13 is 0, so no edge joins n1 and n3 , yet (A2 )13
                                                                           =21: exactly one walk
                                                          2              2
of length 2 joins them, namely 1-2-3. The entry ((I + A) )13 = 1 = 2 (A )13 , since the other
two termsof the expansion  vanish                      2                  2
                                 there; and
                                            (I + A) = I + 2A + A holds entry by entry,
             1 0 0                  0 2 0
with I = 0 1 0 and 2A = 2 0 2. Breadth-first search from n1 reaches n1 , n2 , n3 ,
             0 0 1                  0 2 0
the single component, and agrees.

6.3   A graph that is not connected

In plain words. Now take three houses again. Only one road exists, between the first and
the second house. The third house stands alone. Nobody can drive to it. We expect the check
to say that the village is not in one piece. We also expect it to show that the third house is a
piece by itself.

Example 6.3 (not connected: edge n1 n2 only, N = 3, N − 1 = 2).
                                                                                       
      0 1 0             1 0 0                         1 1 0                             2 2 0
A = 1 0 0 , A2 = 0 1 0 , S = A + A2 = 1 1 0 ,                         (I + A)2 = 2 2 0 .
      0 0 0             0 0 0                         0 0 0                             0 0 1

The entries off the diagonal of S that are 0 are at (1, 3), (2, 3), (3, 1), and (3, 2), and the zeros
of (I + A)2 are at the same four places. By Theorem 4.6 the graph is not connected, and by
Corollary 4.7 the vertices n1 and n2 lie in one component and n3 in another: the components
are G[{n1 , n2 }] and G[{n3 }]. Breadth-first search from n1 reaches only n1 and n2 , and agrees.
Higher powers do not help: the entries (1, 3) and (2, 3) of Ak are 0 for k = 1, . . . , 6, and in fact
no walk reaches n3 at all.

6.4   A computer check over all small graphs
Table 6 reports a check, not a proof. For every labelled simple graph on N = 2, . . . , 6 vertices,
the sum test, the (I + A)N −1 test, and the repeated-squaring form of Proposition 4.17 were
compared with an independent breadth-first search; the table counts the graphs on which each

                                                 20
agrees. The last column counts the graphs on which the sum with only N − 2 powers gives the
wrong answer (for N = 2 that sum is empty). The component statement of Corollary 4.7 was
checked on the same graphs by a second script (Appendix D).

Table 6: All labelled simple graphs on N vertices. Columns 4 to 6 count the graphs on which
the named test agrees with breadth-first search.
      N    graphs   connected    sum test    (I + A)N −1   squaring    N − 2 powers wrong
       2      2         1            2            2             2                 1
       3      8         4            8            8             8                 3
       4     64        38           64            64           64                12
       5    1024       728         1024          1024         1024               60
       6   32768      26704        32768        32768        32768              360



7     Discussion: readings of the board, limits, and competing ex-
      planations
7.1   Where the board and the matrix disagree
The drawing on the board has three lines and the matrix records two edges [4, 5]. Edge by edge:
the pair n1 , n2 is drawn (with an arrowhead at n2 ) and has A12 = A21 = 1; the pair n2 , n3 is
drawn and has A23 = A32 = 1; the pair n1 , n3 is drawn but has A13 = A31 = 0 (Figure 1). The
matrix is symmetric, so it gives no support to a direction on the line from n1 to n2 . Following
Item 3, this note takes the matrix as the example, because the board says that the graph is
given through
           its adjacency
                             matrix [4]. If the drawing had been meant, the adjacency matrix
            0 1 1
would be 1 0 1, which differs from the board matrix exactly at the entries (1, 3) and (3, 1).
            1 1 0
This note does not decide which of the two the lecturer intended. The choice does not affect
the answers to Q1 to Q3, which are theorems for every simple undirected graph; it changes only
the numbers in the examples. Both graphs are connected, so the test of Theorem 4.6 answers
“connected” for both.

7.2   The mark above A
In both photographs the mark above A in question Q1 resembles a small n or a pair of quotation
marks, not clearly a k [4, 5]. The board’s own letter for the number of vertices is the capital N ,
so a lower-case n as an exponent would be unusual, but it cannot be ruled out. Item 2 reads
the mark as k because the assignment text asks about Ak . Since Theorem 3.5 holds for every
positive integer exponent, it answers the board question whichever letter was written, including
an exponent equal to N .

7.3   Limits of the results
     Scope. The theorems are proved for finite simple undirected graphs. For directed
      graphs and multigraphs, the walk-counting statement is made in other sources [3, Theo-
      rem 4.5.10][6, Corollary 9.3.3], and this note makes no claim about the connectivity test
      there.

     What the entries do not say. The entries count walks; they say nothing about the number
      of paths, which needs other methods and is not treated here (Proposition 3.10).


                                                21
     What the test does not say. It answers “connected” or “not connected”; it does not list
      a path between two vertices. Corollary 4.7 gives the components and Remark 4.8 the
      distances.

     Finite checks. The computer checks of Table 6 cover graphs with at most six vertices; they
      support the statements but the proofs are the arguments of Section 4.2 and Appendix C.

     Sources. The textbook was searched in full text for the adjacency matrix and read page
      by page only where listed in Appendix D, so the statement that it contains neither result
      is a statement about the search. Several sources were read only in part, as Appendix D
      records.

7.4   Competing explanations
Reading the entry as a count of paths. Theorem 1 of one source says that (Al )ij is the number
of “different paths” of length l [7, Theorem 1]. As written it is wrong for any definition of
path that forbids repeated vertices or repeated edges, by Proposition 3.10: (A2 )ii is positive
although no such path exists. The same paper states, in its property 7, that the entry equals
the number of walks [7, property 7]. This note therefore does not use that Theorem 1 as support
for Theorem 3.5; the four sources cited there state walks.
    Explaining the test by paths. The proof of the test in the same paper applies its Theorem 1
to A + · · · + AN −1 and so counts “paths” where walks are meant, and it passes from a nonzero
entry to the existence of a path without the walk-to-path step [7, proof of Theorem 2]. The proof
sketch of the (I + A)N −1 form likewise says that the power “aggregates all paths” [1, Section 1,
Theorem 2, proof sketch]. Both statements of the test are correct, as Theorem 4.6 shows; the
explanations are incomplete, which is why the proof is written out in Section 4.2.
    A different method. Breadth-first search gives the same answer (Remark 4.18); eigenvalue
methods are outside the scope of this note and no claim is made about them.

7.5   Cost
This remark is an estimate that counts scalar multiplications with the school method, which
uses N 3 of them for one product of two N × N matrices; faster methods were not examined.
Reaching AN −1 takes N − 2 products, which is 98,000,000 multiplications for N = 100. Because
Proposition 4.17 allows any exponent m ≥ N − 1, squaring I + A repeatedly until the exponent
is at least N − 1 takes 7 squarings, or 7,000,000 multiplications, for N = 100. Breadth-first
search with adjacency lists takes time proportional to the number of vertices plus the number of
edges [10, slides 9 and 10]; when the input is the matrix A itself it reads each of the N 2 = 10,000
entries once [10, slides 3 and 6]. The entries of the powers also grow quickly: for the complete
graph on 10 vertices the largest entry of A9 is 38,742,049. The matrix test is useful because it
is a clean statement about powers of A, not because it is fast.

7.6   What this note does not settle
The board shows the question “How to know if graph is connected or not” but not its answer
[4, 5], so this note makes no claim about whether the lecturer’s intended answer was the sum
test, the (I + A)N −1 form, or a search.


8     Conclusion
Q1. For a finite simple undirected graph with adjacency matrix A and an integer k ≥ 1, the
entry (Ak )ij is the number of walks of length k from ni to nj (Theorem 3.5, proved by induction
on k). It counts walks, in which vertices and edges may repeat, and not paths: for example

                                                22
(A2 )ii equals the degree of ni , which is positive whenever ni has a neighbour, although no path
of length 2 returns to ni (Proposition 3.10).
    Q2. For N ≥ 2 vertices, the graph is connected if and only if every entry off the diagonal
of A + A2 + · · · + AN −1 is positive, and equivalently if and only if (I + A)N −1 has no zero
entry (Theorem 4.6). The proof uses the walk-counting theorem and the fact that a walk
contains a path no longer than itself (Lemma 2.44); the last power N − 1 cannot be lowered to
N − 2 (Proposition 4.14). The board matrix gives “connected” and the matrix with the single
edge n1 n2 gives “not connected” (Examples 6.2 and 6.3). Breadth-first search is an alternative
(Remark 4.18).
    Q3. Under the course convention, a path between ni and nj is a walk from ni to nj whose ver-
tices are pairwise distinct (Definition 2.31); this is the textbook’s simple path, Definition 1.2.13
[9, p. 22]. The textbook’s own word “path” (Definition 1.2.12) means a walk with distinct edges,
called a trail here; the existence of a connection does not depend on the choice, but the counts
do (Section 5).
    The assumptions on which these answers rest are listed in Section 1.3: the mark above A
read as an exponent, the matrix rather than the drawing as the example, and the course meaning
of “path”.


References
 [1]   Shuliang Bai. Important Properties and Applications of the Adjacency Matrix (20250310).
       Lecture notes, dated 2025-03-10 in the title. BIMSA. 2025. url: https://bimsa.net/do
       c/notes/48535.pdf?id=0.3935315718408674 (visited on Oct. 27, 2026).
 [2] Chapter 1 Matrices and Graphs, 1.1 The Adjacency Matrix (linear algebra course notes).
     Lecture notes. The file shows no author name and no date. School of Mathematical and
     Statistical Sciences, University of Galway. n.d. url: https://maths.nuigalway.ie/~rq
     uinlan/linearalgebra/section1-1.pdf (visited on Oct. 27, 2026).
 [3]   Darij Grinberg. An introduction to graph theory (Text for Math 530 in Spring 2022 at
       Drexel University). arXiv:2308.04512v3 [math.HO], Spring 2025 edition, 7 June 2025.
       Preprint, not peer reviewed. Page numbers cited are the document’s own page numbers.
       2025. url: https://arxiv.org/abs/2308.04512 (visited on Oct. 27, 2026).
 [4] Lecture whiteboard photo 1. Local file sources/whiteboard-1.jpg. Photograph of a lecture
     board, supplied by the user. Author and date unknown. n.d.
 [5] Lecture whiteboard photo 2. Local file sources/whiteboard-2.jpg. Second photograph of the
     same board at a slightly different angle, supplied by the user. Author and date unknown.
     n.d.
 [6]   Eric Lehman, F. Thomson Leighton, and Albert R. Meyer. 9.3: Adjacency Matrices (Math-
       ematics for Computer Science, MIT OpenCourseWare), Engineering LibreTexts. Page last
       modified 2021-07-02; the year of the underlying book is not on the page. n.d. url: https
       ://eng.libretexts.org/Bookshelves/Computer_Science/Programming_and_Computa
       tion_Fundamentals/Mathematics_for_Computer_Science_(Lehman_Leighton_and_Me
       yer)/02%5C%3A_Structures/09%5C%3A_Directed_graphs_and_Partial_Orders/9.03
       %5C%3A_Adjacency_Matrices (visited on Oct. 27, 2026).
 [7]   P. Paramadevan and S. Sotheeswaran. “Properties of Adjacency Matrix of a Graph and
       It’s Construction”. In: JSc EUSL (Journal of Science, Eastern University, Sri Lanka) 12.1
       (2021), pp. 13–21. doi: 10.4038/jsc.v12i1.29. url: https://www.fsc.esn.ac.lk/jsc
       /archive/12.1.2.pdf (visited on Oct. 27, 2026).




                                                23
 [8] Path (graph theory). Revision of 5 June 2026 (oldid 1357845833) as fetched; open to later
     edits. Wikipedia, English edition. n.d. url: https://en.wikipedia.org/wiki/Path_(g
     raph_theory) (visited on Oct. 27, 2026).
 [9]   P. A. Petrosyan, V. V. Mkrtchyan, and R. R. Kamalyan. Graph Theory: a study guide.
       Course textbook in Armenian, supplied by the user; the Armenian title is omitted here.
       Printed page numbers are cited; the PDF page is one higher. Yerevan: Yerevan State
       University Press, 2015. isbn: 978-5-8084-1995-7.
[10] Éric Schost. CS 341: Algorithms, Lecture 10: Graphs, breadth first search. Lecture slides,
     Winter 2026. David R. Cheriton School of Computer Science, University of Waterloo.
     2026. url: https://www.student.cs.uwaterloo.ca/~cs341/lectures/lecture10.pdf
     (visited on Oct. 27, 2026).
[11]   Eric W. Weisstein. Connected Graph. Wolfram MathWorld. n.d. url: https://mathworl
       d.wolfram.com/ConnectedGraph.html (visited on Oct. 27, 2026).


A      Textbook numbers and board symbols
Table 7 lists, in the textbook’s build order, each concept used in this note with the textbook’s
number and printed page, and the word the textbook uses where it differs from English usage
[9]. The textbook’s words are in Armenian script, which this note does not typeset; its words
are given in English translation. Printed page numbers are one lower than PDF page numbers
(Item 7).

         Table 7: Concepts in the textbook’s build order, with the textbook’s numbers.
    Concept                               Textbook number        Printed   Textbook     word
                                                                 page      (translated)
    graph G = (V, E)                      Definition 1.1.1       9
    adjacent                              Definition 1.1.4       11
    adjacency matrix A(G)                 no number of its       11
                                          own, after Defini-
                                          tion 1.1.6
    degree                                Definition 1.2.1       16
    sum of all degrees equals 2|E|        Theorem        1.2.1   16
                                          (Euler)
    walk                                  Definition 1.2.10      21
    closed walk                           Definition 1.2.11      22
    walk with no repeated edge (trail)    Definition 1.2.12      22        “path”
    walk with no repeated vertex (path)   Definition 1.2.13      22        “simple path”
    cycle                                 Definition 1.2.14      22        “cycle”, “closed
                                                                           path”
    simple cycle                          Definition 1.2.15      22        “simple cycle”
    distance                              Definition 1.2.16      22–23
    every (u, v)-walk contains a simple   Lemma 1.2.1            23
    (u, v)-path, u ̸= v
    connected                             Definition 2.1.1       48
    connected components                  in prose, no num-      49
                                          ber
    connected if and only if one compo-   Remark 2.1.1           49
    nent



                                               24
   Table 8 compares the board’s symbols with the textbook’s and with this note’s. The first
row records that the board’s V in the line defining Aij is the set of edges [4, 5].

            Table 8: Board symbols, textbook symbols, and the symbols of this note.
            Board                       Textbook                 This note
            (G, V ), with V the edge    G = (V, E)               G = (V, E)
            set
            eij ∈ V                     uv ∈ E                   ni nj ∈ E or eij ∈ E
            nodes ni                    vertices vi              vertices ni
            |G| = N nodes               n vertices               N vertices
            Aij                         aij in A(G)              Aij in A



B      Transcription of the whiteboard
The two photographs show the same board at slightly different angles, and they are read together
[4, 5]. The lines below follow the reading order; the board’s wording and spelling are kept.

    1. The matrix entry is defined as Aij = 1 if eij ∈ V and Aij = 0 if eij ∈
                                                                            / V [4, 5]. The board’s
       V here is the set of edges (Item 5).

    2. A drawing with vertices labelled 1, 2, 3, and next to it a grid labelled “adj.” with rows
       0 1 0, 1 0 1, 0 1 0 [4, 5]. The drawing shows a line from 1 to 2 with an arrowhead at 2, a
       line from 1 to 3, and a line from 2 to 3; the matrix records only the edges 1–2 and 2–3
       (Section 7.1).

    3. “Problem. Given graph (G, V ) with N nodes i.e. |G| = N and the graph is represented
       through it’s adj. matrix. So you have ‘A’ matrix.” [4, 5].

    4. “1) What does A·ij represent”, where · marks a small mark that looks like a small n or
       quotation marks [4, 5] (Section 7.2).

    5. “2) How to know if graph is connected or not.” [4, 5].

    6. “Def. Graph is called connected if for any ni , nj there exists a path between nodes.” [4,
       5].

Clearly visible: the prose of items 1, 3, 5 and 6, the matrix entries, and the vertex labels. Likely
interpretation: the mark in item 4 is an exponent k (Item 2); the arrowhead in item 2 is a stray
mark (Item 3). Not settled: which of the drawing and the matrix the lecturer intended, and
which meaning of “path” the board uses (Item 4).


C      Derivations
This appendix holds the arguments that the main text only states, in the order in which the
main text needs them.

C.1     Walk counting: walks and vertex sequences
The proof of Theorem 3.5 counts vertex sequences instead of walks. This is allowed by the
following fact, which is stated before the theorem in Remark 2.20.



                                                25
Proposition C.1. In a simple graph, the map that sends a walk u0 , e1 , u1 , . . . , ek , uk to its
vertex sequence u0 , u1 , . . . , uk is a one-to-one correspondence between the walks of length k and
the sequences of k + 1 vertices in which every two consecutive vertices are adjacent.

Proof. This is proved here. The vertex sequence of a walk has consecutive vertices ui−1 , ui joined
by the edge ei , so they are adjacent. The map is one to one: in a simple graph at most one edge
joins two vertices, so ei = ui−1 ui is determined by the vertices, and two walks with the same
vertex sequence are equal. The map is onto: given such a sequence, put ei = ui−1 ui ; this is an
edge because the two vertices are adjacent, and the result is a walk.

    For k = 0 the same reasoning gives one walk from each vertex to itself, which is why the
identity matrix A0 = I fits the pattern [3, Section 4.5.5]; this note uses it only in Proposition 4.17.
Where simplicity enters the proof of Theorem 3.5 is stated after that proof.

C.2    The counterexample, in full
Proposition 3.10 uses the board graph. Its entries for the walks from n1 to n2 can be found in
closed form. In B, the vertex n2 is adjacent to n1 and n3 , and these two are adjacent only to
n2 . So a walk alternates between n2 and the set {n1 , n3 }. A walk from n1 to n2 therefore has
odd length k, and its vertices in even positions w2 , w4 , . . . , wk−1 , which number (k − 1)/2, are
each n1 or n3 , freely. Hence there are 2(k−1)/2 walks of odd length k and none of even length,
which gives 1, 0, 2, 0, 4 for k = 1, . . . , 5, as in Table 2 and in the entries of A, A3 , A5 . Among
them only the walk n1 , n2 is a path or a trail, because any longer walk repeats the vertex n2 (a
walk of length 3 or more from n1 to n2 meets n2 at an earlier odd position).

C.3    The chain of premises for the connectivity test
Theorem 4.6(a)⇔(b) follows from Proposition 4.5 and the definition of connected. The premises,
in order, are the following.

   1. Theorem 3.5: (Ak )ij is the number of walks of length k.

   2. Corollary 3.9(a): all entries are nonnegative integers, so a sum is positive if and only if a
      summand is.

   3. Lemma 2.44: a walk of length k from u to v contains a path of length at most k.

   4. Corollary 2.46: a path in a graph with N vertices has at most N − 1 edges.

   5. Proposition 2.35 and Remark 2.49: “path” may be read as trail or path.

Premises 1 and 2 give (ii)⇔(iii) and the passage from a positive entry to a walk; premise 3 gives
the passage from a walk to a path; premise 4 gives the bound k ≤ N − 1 in (i)⇒(ii); premise 5
makes the equivalence independent of the reading of “path”. No other fact is used.

C.4    Powers of I + A
Proof of Proposition 4.17. This is proved here; [1, Section 1, Theorem 2, proof sketch] gives the
idea of adding a loop to every vertex. Put m ≥ N −1. Expand (I+A)m = (I+A)(I+A) · · · (I+A)
with m factors. Each term chooses I or A in each factor and multiplies the choicesin order.
Since I times a matrix X is X, a term with k letters A equals Ak , and there are m   k ways to
choose which k factors give A. Therefore
                                             m  
                                       m
                                             X  m k
                               (I + A)     =      A ,          A0 = I.                             (3)
                                                k
                                            k=0



                                                  26
Diagonal. The term k = 0 contributes 1 to every diagonal entry and all other terms are
nonnegative, so every diagonal entry
                                m
                                        Pmis at m
                                                 least
                                                     k
                                                        1. Off the diagonal. For
                                                                              m
                                                                                 i ̸= j the identity
contributes 0, so ((I + A) )ij = k=1 k (A )ij . Every coefficient k with 1 ≤ k ≤ m is
a positive integer and every (Ak )ij is a nonnegative integer (Corollary 3.9(a)), so the sum is
positive if and only if some (Ak )ij with 1 ≤ k ≤ m is positive. If a path between ni and nj
exists, it has length k with 1 ≤ k ≤ N − 1 ≤ m (Corollary 2.46) and (Ak )ij ≥ 1. Conversely,
if (Ak )ij > 0 for some k with 1 ≤ k ≤ m, a walk exists (Theorem 3.5) and hence a path
(Lemma 2.44). This proves the statement about the entries. G is connected if and only if every
pair i ̸= j has a path, that is, if and only if no off-diagonal entry is 0; since the diagonal entries
are positive, that is if and only if (I + A)m has no zero entry. Squaring I + A repeatedly gives
the exponents 2, 4, 8, . . . , so t squarings give m = 2t , and t is chosen with 2t ≥ N − 1.

   For N = 3 and the board graph, (I + A)2 = I + 2A + A2 is verified entry by entry in
Example 6.2.

C.5    Distance
Proof of Proposition 2.47. This is proved here. Every path is a trail (Proposition 2.35) and every
trail is a walk, so the lengths of paths are among the lengths of trails, which are among the
lengths of walks; hence minwalks ≤ mintrails ≤ minpaths . By Lemma 2.44 a shortest walk contains
a path of at most the same length, so minpaths ≤ minwalks . The three minima are therefore equal.
If there is no walk there is no trail and no path, and if there is a walk, Lemma 2.44 gives a path;
so the three sets are empty together.

Proposition C.2 (the distance properties). The three properties listed in Definition 2.40 follow
from the definition.

Proof. The textbook lists the properties without proof [9, p. 23]; this proof is written here. By
Proposition 2.47 we may compute d by shortest walks. (1) Lengths are 0, 1, 2, . . . or +∞, so
d ≥ 0. The walk consisting of u alone has length 0, so d(u, u) = 0. If d(u, v) = 0 there is a walk
of length 0 from u to v, which is the single vertex, so v = u. (2) If u0 , . . . , uk is a walk from u
to v then uk , . . . , u0 is a walk from v to u of the same length, since edges are unordered; so the
sets of lengths agree, and so do their minima. (3) If d(u, w) or d(w, v) is +∞ the right side is
+∞ and the inequality holds. Otherwise join a shortest (u, w)-walk and a shortest (w, v)-walk
at w: this is a (u, v)-walk of length d(u, w) + d(w, v), and a shortest (u, v)-walk is no longer.

C.6    Cross-checks by computer
Two finite checks accompany the proofs; neither replaces them. First, for every labelled simple
graph on N = 2, 3, 4, 5 vertices, the number of walks of length k enumerated by brute force
equals the corresponding entry of Ak , for k = 1, . . . , 5 when N ≤ 4 and k = 1, 2, 3 when N = 5
(Appendix D). Second, for all labelled simple graphs on 2, . . . , 6 vertices, the sum test, the
(I + A)N −1 test, the component statement of Corollary 4.7, and the repeated-squaring form of
Proposition 4.17 agree with breadth-first search (Table 6).


D     Sources read and how to reproduce the numbers
Sources and what was read. Textbook [9]: printed pages 9 to 12, 16, 21 to 23, and 48 to 49,
viewed as page images, and a full-text search of the whole book for the adjacency matrix; the
other chapters were not read. Board photographs [4, 5]: both viewed as images. Grinberg [3]:
Sections 2.9, 2.10, 3.4, and 4.5.5 of the 454-page text. Galway notes [2]: the whole eight-page
file. Lehman, Leighton, and Meyer [6]: the one page cited. Paramadevan and Sotheeswaran
[7]: the whole nine-page paper; it is an expository paper whose Theorem 1 and proofs are loose

                                                 27
(Section 7.4), so it is cited for statements and as a second witness only. Bai [1]: Section 1; the
rest concerns eigenvalues. MathWorld [11] and Wikipedia [8]: the entries cited; the Wikipedia
article is open to later edits. Schost [10]: the slides on breadth-first search and its running
time. The assignment text is known only as it was reported to us and is not a source of the
mathematics.

Scripts. All scripts are in the folder appendices/scripts/, are written in plain Python with
integer arithmetic, and are run from the paper folder.

    generate paper numbers.py computes every matrix and table printed in the examples,
     asserts the facts the text states about them, and writes numbers.tex, which this note
     inputs.

    m1 walks.py: powers of the board matrix, explicit walk lists, the hand-checkable sums,
     walks against paths and trails, and a brute-force check of Theorem 3.5 on all labelled
     simple graphs with N = 2, 3, 4, 5 vertices (2, 8, 64, 1024 graphs; 40, 360, 5120, 76800
     entries, all equal to the walk counts).

    m2 walks.py: classification of the example walks, the absence of a cycle in the board graph
     among closed walks of length up to 6, traces of Lemma 2.44, and checks of the lemma,
     Proposition 2.35, Corollary 2.46, and Proposition 2.47 on all walks of length up to 6 in
     three small graphs and on 300 random graphs (seed 20261027, 192696 walks, no failures).
     Its textbook example graph uses only seven edges that the textbook’s examples use; the
     textbook’s figure has at least one more, which no example uses.

    m3 connectivity.py: the examples of Section 6, the path graphs of Table 3, the cost
     counts, and the exhaustive comparison over all labelled graphs on up to 6 vertices, including
     the component statement of Corollary 4.7.

To reproduce, run python3 -I appendices/scripts/generate paper numbers.py and the
three other scripts the same way; their saved outputs are in the same folder. The last script
takes about twenty seconds.




                                               28
```

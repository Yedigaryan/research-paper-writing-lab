# Deliverable `base`

Compiled PDF, 39 pages, rendered with pdftotext -layout.

```
            Adjacency matrices, walks, and connectivity:
        what (Ak )ij counts, how to test connectedness from A,
              and what a path between two vertices is


                                          October 27, 2026


                                                 Abstract
          This paper starts from two photographs of a university lecture whiteboard (“the board”).
      The board gives a graph with N vertices by its adjacency matrix A and asks two questions
      about it; a short assignment text that came with the photographs adds a third. The paper
      answers all three for finite simple undirected graphs. It follows the definitions and the
      numbering of the course textbook (for example Definition 1.2.10 for a walk) [9]. First, the
      entry (Ak )ij of the k-th power of A is the number of walks of length k from vertex ni to
      vertex nj ; it does not count paths. The paper proves this by induction on k (the statement
      is also in the University of Galway lecture notes [2]), and shows on the three-vertex example
      of the board why the difference between walks and paths matters. Second, for N ≥ 2 the
      graph is connected if and only if every entry off the diagonal of A + A2 + · · · + AN −1 is
      positive, equivalently if and only if (I + A)N −1 has no zero entry. The paper proves both
      forms itself, shows that N − 1 cannot be lowered to N − 2, and states breadth-first search as
      the alternative. Third, in the course convention a path between ni and nj is a walk from ni
      to nj in which no vertex repeats; this is the textbook’s Definition 1.2.13, which the textbook
      calls a “simple path”. The textbook’s own word “path” (Definition 1.2.12) means something
      weaker, and this paper calls that object a trail. All matrices in the worked examples were
      computed by script.


1     Introduction
1.1   The three questions and where each came from
A university lecture whiteboard, photographed twice from slightly different angles, is the starting
point of this paper [4, 5]. Read from top to bottom, the board shows six things (Table 1). They
set up a graph with N vertices that is given only by its adjacency matrix A, and they ask two
questions about it. The words of the problem statement are the board’s own: “Given graph
(G, V ) with N nodes i.e. |G| = N and the graph is represented through it’s adj. matrix. So you
have A matrix” [4, 5].
    The paper answers three questions.
Q1. For a positive integer k, what does the entry (Ak )ij of the k-th power of A represent? This
    is the board’s first question [4, 5].
Q2. How can one tell from A alone whether the graph is connected? This is the board’s second
    question [4, 5].
Q3. What is the definition of a path between two vertices ni and nj ? This question is not on
    the board. It was added by the assignment text that came with the photographs. The
    assignment text is not reproduced in this paper. As reported by the user, it states that in
    the course “path” means a walk with no repeated vertices; the answer to Question 3 rests
    on this statement (Section 5).

                                                    1
       Table 1: Every line of the board, in reading order, and where this paper treats it.
      No.   What the board shows                          Where treated
       1    Aij = 1 if eij ∈ V , and 0 if eij ∈
                                              / V (the    Definition of the adjacency matrix, Sec-
            board’s V is the edge set)                    tion 2; letters in Section 1.3
       2    A drawing of three circled vertices 1, 2, 3   Mismatch reported in Section 1.3; worked
            and a grid labelled “adj.” with rows 010,     example in Section 6
            101, 010
       3    “Problem. Given graph (G, V ) with N          Setting, Section 1.3
            nodes . . . So you have A matrix”
       4    Question 1: “What does Aij represent”,        Section 3
            with a small mark above A (a power k;
            see item 2 of Section 1.3)
       5    Question 2: “How to know if graph is con-     Section 4
            nected or not”
       6    “Def. Graph is called connected if for any    Definition of connected, Section 2; the word
            ni , nj ∃ path between nodes”                 “path” in Section 5


Question 3 matters because the board’s definition of “connected” uses the word “path” without
saying which of several meanings it has (Section 1.3), so the answer to Question 2 could appear
to depend on it. It does not (proved in Section 2.4: whether a path exists does not depend on
the meaning of the word), but Question 3 still needs a definite answer.
    Statements in this paper that are not plain facts from a source carry a label in square
brackets. [derived here] marks a result that the paper proves or computes itself, so the reader
can check the proof or run the script. [interpretation] marks a reading of the photographs,
the assignment or a source that cannot be proved. [estimate] marks an operation count, not a
measurement. [qualified] marks a statement that rests on a point that was not fully checked;
the text next to it names the point. A compound label such as [interpretation, qualified] marks
a reading that also rests on such a point.
    The course textbook, Graph Theory by Petrosyan, Mkrtchyan and Kamalyan [9], supplies
the definitions and their numbers. It contains neither the walk-counting theorem nor a matrix
test for connectivity in the pages that were checked [qualified] (Section 1.6 says which pages
and how the rest was checked). So the paper proves both results itself and marks them [derived
here].

The answers in brief.         The details and the proofs follow; this list is only a map.

A1. (Ak )ij is the number of walks of length k from ni to nj (Theorem 3.5). It is not the number
    of paths: walks may repeat vertices and edges (Proposition 3.10).

A2. For N ≥ 2, the graph is connected if and only if every entry off the diagonal of A +
    A2 + · · · + AN −1 is positive (Theorem 4.6). Equivalently, (I + A)N −1 has no zero entry
    (Proposition 4.16). The exponent N − 1 cannot be lowered to N − 2 (Proposition 4.17).

A3. In the course convention, a path between ni and nj is a walk from ni to nj whose vertices are
    pairwise distinct (Definition 5.1). It is the textbook’s “simple path”, Definition 1.2.13 [9].

1.2    The story: houses and roads
      In plain words. Picture a small village. Each house is a point. Each road joins
      exactly two different houses. Every road can be driven in both directions. No road
      starts and ends at the same house. No two roads join the same pair of houses. The
      village has only finitely many houses. A trip is a list of houses, one after another.
      Each house on the list shares a road with the house before it. A trip may pass the

                                                     2
      same house twice. It may drive the same road twice. A trip may also be just one
      house, with no driving at all. A trail is a trip that never uses the same road twice.
      A route is a trip that never passes the same house twice. Every idea in this paper is
      about this village and its trips.

    The village from the board has three houses in a row. The first house and the middle house
share a road. The middle house and the last house share a road. No road joins the first house and
the last house. Figure 1 (left) shows this village. The same story is used before every definition,
theorem, test and example, so that each can be followed without the symbols. Table 2 gives the
dictionary from the story to the textbook’s words and numbers. The story words are fixed: trip
for a walk, trail for a trail, route for a path.
                                                         1                  2
                                                              u               -u
                                                              @
                     1           2               3
                     u            u              u                @
                                                                   @
                                                          the drawing @u
                                                                     @
                          the matrix                                    3
Figure 1: Left: the village of the board matrix, three houses in a row, with roads 1–2 and 2–3.
Right: the board drawing as it appears in both photographs, a line from 1 to 2 ending in an
arrowhead at 2, a line from 1 to 3, and a line from 2 to 3 [4, 5]. The two pictures do not describe
the same graph; see Section 1.3.


Table 2: The story and the technical words. Textbook numbers are from the course textbook [9];
“n.n.” means that the pages checked give no number.
 Story word                              Technical term        Textbook number     Defined in
 house                                   vertex                1.1.1               Definition 2.1
 road                                    edge                  1.1.1               Definition 2.1
 two houses share a road                 adjacent              1.1.4               Definition 2.5
 table of ones and zeros                 adjacency matrix      n.n. (p. 11)        Definition 2.9
 number of roads at a house              degree                1.2.1               Definition 2.16
 trip                                    walk                  1.2.10              Definition 2.23
 trip that ends where it began           closed walk           1.2.11              Definition 2.27
 trip that never uses a road twice       trail                 1.2.12              Definition 2.31
 route: a trip that never passes a       path                  1.2.13              Definition 2.35
 house twice
 round trip that never uses a road       cycle                 1.2.14              Definition 2.40
 twice
 round trip that passes no house twice   simple cycle          1.2.15              Definition 2.44
 but the first
 fewest roads on a trip between two      distance              1.2.16              Definition 2.48
 houses
 village in one piece                    connected graph       2.1.1               Definition 2.55
 one piece of a village                  component             n.n. (p. 49)        Definition 2.60



1.3   Conventions and assumptions
Every reading below is a choice made where the photographs, the assignment text, or the
textbook leave room. Each is stated here so that the reader can see what the rest of the paper
rests on.

  1. Setting. The graph is finite, simple (no loops, no repeated edges) and undirected. This is
     the assumption of the assignment text. It agrees with the board matrix, which is symmetric

                                                     3
      and has zeros on the diagonal (item 4 below), and with the textbook’s definition of a
      graph [9, Section 1.1, Definition 1.1.1, p. 9].

  2. The mark above A in Question 1. In both photographs the mark above A is small. It
     looks like quotation marks or a small n, and it is not clearly a k [4, 5]. This paper reads it
     as a power k, because the assignment text asks about Ak . This reading is [interpretation,
     qualified]. The mathematics does not depend on the letter: the theorem in Section 3 holds
     for every positive integer exponent, whether the board meant k or n.

  3. Quotation marks around A. Two lines lower, the board writes “A” (“So you have “A”
     matrix”) [4, 5]. This paper takes it as the name of the adjacency matrix.

  4. The drawing and the matrix disagree. The drawing shows three lines: 1–2 with
     an arrowhead at 2, 1–3, and 2–3 [4, 5]. The matrix next to it has A12 = A21 = 1 and
     A23 = A32 = 1, and A13 = A31 = 0 (Table 3). So the drawing has an edge 1–3 that the
     matrix does not have, and an arrowhead (a direction) that the symmetric matrix does
     not have. The problem statement says the graph is given by its adjacency matrix [4, 5],
     so this paper takes the matrix as the example graph and calls it B (Figure 1, left). It
     treats the arrowhead as a stray mark, since the matrix is symmetric and the problem is
     about undirected graphs. The paper reports the mismatch and does not guess which one
     the lecturer intended. The sources therefore disagree on the edge 1–3. Both graphs are
     used: B for the worked example, and T (the three-line drawing, a triangle) only where a
     graph with a cycle is needed. No result in this paper depends on the choice, since every
     statement holds for every finite simple undirected graph.

  5. The board’s letters. The board writes (G, V ) for the graph and eij ∈ V in the definition
     of Aij , so the board’s V is the edge set. The textbook writes G = (V, E), with V for vertices
     and E for edges [9]. This is a difference of notation only. The paper uses the textbook’s V
     and E. The board writes |G| = N for the number of vertices and ni for vertices; the paper
     keeps N and ni . The textbook writes vi and n; the paper keeps ni and N , except that the
     vertices of the textbook’s own example graph keep the textbook’s names v1 , . . . , v5 .

  6. The word “path”. The textbook uses “path” for a walk with no repeated edge (Defini-
     tion 1.2.12) and “simple path” for a walk with no repeated vertex (Definition 1.2.13) [9].
     English texts call the first a trail and the second a path [3, 8]. The assignment text is not
     reproduced here; as reported by the user, it says that in the course “path” means a walk
     with no repeated vertices. The board does not say which meaning it uses. This paper
     therefore writes trail for Definition 1.2.12 and path for Definition 1.2.13 everywhere, and
     shows the three conventions side by side in Table 7. That the course uses this meaning is
     [interpretation, qualified], because it rests on the user’s report of the assignment text and
     not on the board.

  7. Lengths and exponents. The exponent k is a positive integer. The case k = 0 (the
     identity matrix, one walk of length 0 from a vertex to itself) is treated by Grinberg [3]
     and is not needed for the board question. A walk of length 0, a single vertex, is allowed,
     because the textbook’s own property d(u, u) = 0 needs it. The textbook does not say so
     in words, so this is [interpretation, qualified].


1.4   Notation
The letters are fixed here, before the first definition, and used unchanged after this point. Table 4
also gives the board’s and the textbook’s letters.



                                                 4
                  Table 3: The board drawing and the board matrix, edge by edge [4, 5].
   Pair of vertices      In the drawing            In the matrix                Verdict
   1, 2                  line, arrowhead at 2      A12 = A21 = 1                edge in both; arrowhead has no
                                                                                counterpart
   2, 3                  line                      A23 = A32 = 1                edge in both
   1, 3                  line                      A13 = A31 = 0                edge in the drawing only


               Table 4: Notation of this paper, with the board’s and the textbook’s letters.
      Symbol                    Meaning                                           Board           Textbook
      G = (V, E)                a finite simple undirected graph, vertex          (G, V ), with   G = (V, E)
                                set V , edge set E                                V the edge
                                                                                  set
      N                         number of vertices                                |G| = N         n
      n1 , . . . , n N          the vertices                                      ni              vi
      u, v, w                   any vertices                                      —               u, v
      ni nj , eij               the edge joining ni and nj                        eij             uv
      A, Aij                    adjacency matrix and its entry in row i,          A, Aij          A(G), aij
                                column j
      Ak , I                    k-th power of A and the N × N identity            A with a        —
                                matrix                                            small mark
                                                                                  above
      k, m                      positive integers: lengths of walks, expo-        the    mark     —
                                nents                                             above A
      i, j, r                   indices running from 1 to N                       i, j            —
      deg(ni )                  degree of ni (Definition 1.2.1)                   —               dG (v), d(v)
      d(u, v)                   distance                                          —               d(u, v),
                                                                                                  dG (u, v)
      S                         A + A2 + · · · + AN −1 , defined in Section 4     —               —
      A0                        the identity matrix I, by convention, used        —               —
                                only in formula (3)
       m
           
       k                        binomial coefficient: the number of ways          —               —
                                to choose k of m items
      u∼v                       there is a path from u to v (Defini-              —               —
                                tion 2.60)


1.5       How the paper is organized
Section 2 gives the definitions in the textbook’s order. Each definition is followed by a remark on
what it allows and forbids, an example and a non-example. Sections 3 to 5 answer Questions 1,
2 and 3 in that order. Section 6 writes out every matrix for the board graph B and for a
graph with a single edge. Section 7 states limitations and Section 8 answers the three questions
directly. Appendix A holds derivations and the scripts, and Appendix B lists the course terms
with their textbook numbers.
    Every definition, theorem, lemma, test, and worked example is preceded by a short paragraph
marked “In plain words”. A source that is cited states the fact itself; where only the statement
is cited and the proof is the paper’s own, the text says so.

1.6       Provenance: sources, pages checked, and scripts
This subsection collects where the material comes from, so that Section 2 to Section 6 can stay
mathematical.




                                                           5
Sources. The board photographs [4, 5]; the course textbook [9]; Grinberg’s lecture-note text
on graph theory [3]; the University of Galway lecture notes on the adjacency matrix [2]; the
open textbook of Lehman, Leighton and Meyer [6]; the journal paper of Paramadevan and
Sotheeswaran [7]; Bai’s lecture notes [1]; the MathWorld and Wikipedia entries [11, 8]; and
lecture slides on breadth-first search [10]. The Galway file carries no author name or date; its
URL suggests the name Quinlan, which the file does not confirm, so this paper calls it the
University of Galway notes.

Pages of the textbook checked. The textbook definitions were taken from printed pages
9 to 12 (graphs and the adjacency matrix), 16 (degree), 21 to 23 (walks, trails, paths, cycles,
distance, Lemma 1.2.1) and 48 to 49 (connectedness). The remaining pages of Chapters 1 and 2
(13 to 15, 17 to 20, 24 to 47 and 50 to 62) and Chapters 3 to 8 were not read page by page. An
independent full-text search of the whole book for the adjacency matrix found it only on printed
pages 7, 11, 12, 34 and 61, and found no walk-counting theorem and no matrix connectivity test.
So the statement “the textbook contains neither” is [qualified] : it rests on that search and on
the pages read, not on a page-by-page reading of the whole book. Page numbers in this paper
are printed page numbers; the PDF page is one higher.

Weaknesses of some sources. Two sources that state the connectivity test prove it incom-
pletely, and one states the counting theorem with “paths” in place of walks. The offending
sentences are quoted in Section 7.2.

Scripts. Every matrix, product, sum and count in the paper was computed by script before it
was written. The scripts and their saved outputs are in the folder appendices/scripts/ of the
paper. The PDF alone cannot confirm those numbers: a reader who wants to check them must
run the scripts. Appendix A.7 gives the commands and three small cases that can be checked
by hand. Exhaustive comparisons over small graphs are checks, not proofs, and the text says so
each time.


2    Background: the definitions, in the textbook’s order
Let G = (V, E) be a finite simple undirected graph with N vertices n1 , . . . , nN ; let u, v, w be
vertices and e an edge. These are the letters of Table 4, and every definition below uses exactly
them. The definitions follow the order of the course textbook [9]: graph, adjacency, adjacency
matrix, degree, walk, closed walk, trail, path, cycle, simple cycle, distance, and then connected-
ness. Each definition cites the textbook’s number and printed page. After each definition come
a remark on what it allows and forbids, an example, and a non-example.
     The three answers need these definitions: graph, adjacent, adjacency matrix and degree
(Answer 1 and the proof of the test), walk and trail and path (all three answers), closed walk
(Answer 1), connected and component (Answer 2), and the walk-to-path lemma. Cycle, simple
cycle and distance are context: the answers use them only in remarks, examples and one by-
product (Corollary 4.10).
     Four graphs supply the examples. The first is the graph B of the board matrix: vertices
1, 2, 3 (meaning n1 , n2 , n3 ) and edges 12 and 23 (Figure 1, left). The second is the board drawing
T , a triangle with edges 12, 13, 23. The third is a small graph of this paper’s own, H: a triangle
1, 2, 3 with a fourth vertex attached to vertex 3, so its edges are 12, 13, 23 and 34 (Figure 2).
The fourth is the textbook’s own example graph, which this paper calls Gtb (Figure 3); the seven
edges used from it are v1 v2 , v1 v3 , v2 v3 , v2 v4 , v3 v4 , v3 v5 and v4 v5 , the ones that the textbook’s
own examples use. B has no cycle, and in B every trail is a path (Remark 2.32), so B cannot
show the differences between the later definitions; H and Gtb can.



                                                     6
                                          4u            u3
                                                        @
                                                           @
                                                               @
                                                        u          @u
                                                     1             2
Figure 2: The graph H defined by this paper: a triangle on the vertices 1, 2, 3 and a fourth
vertex 4 joined to 3.
                                                    v2
                                                        u          uv4
                                                    
                                                   
                                         u
                                               
                                      v1 
                                         Z
                                               Z
                                                   Z
                                                    Zu             uv5
                                                    v3
Figure 3: The graph Gtb with the seven edges that the textbook’s own examples use: v1 v2 , v1 v3 ,
v2 v3 , v2 v4 , v3 v4 , v3 v5 , v4 v5 . It is a part of the textbook’s Fig. 1.2.5 (printed p. 22) [9]. The
textbook’s figure also has the edge v1 v5 , which none of the textbook’s examples uses and which
this paper does not use.

2.1    Graphs and the adjacency matrix
      In plain words. A village is a list of houses and a list of roads. Each road joins
      two different houses. Two roads never join the same pair. Roads have no direction.
      The list of houses is finite and has at least one house.

Definition 2.1 (Simple undirected graph; textbook Definition 1.1.1, p. 9). A simple undirected
graph is a pair G = (V, E), where V is a finite nonempty set, the vertices, and E is a set of
unordered pairs of distinct vertices, the edges. The edge {u, v} is written uv [9, Section 1.1,
Definition 1.1.1, p. 9].

Remark 2.2. Because the pair must consist of distinct vertices, there is no loop (an edge from a
vertex to itself). Because E is a set, no pair occurs twice, so there is no repeated edge. Because
the pair is unordered, uv and vu are the same edge. Isolated vertices (vertices with no edge)
are allowed, since E may be any set of such pairs. An edge is fixed by its two ends. This is why
a walk can later be written by its vertices alone (Remark 2.24): two different edges would need
different pairs of ends. In this paper the word loop always means such a self-edge.

Example 2.3. V = {n1 , n2 , n3 } and E = {n1 n2 , n2 n3 }. This is the graph B of the board
matrix, three vertices in a row.

Non-example 2.4. Two vertices joined by two edges, or an edge from one vertex back to itself.
The first repeats an edge, the second is a loop. Neither is a simple graph.

      In plain words. Two houses are neighbours when one road joins them directly. A
      house is never its own neighbour. Being neighbours says nothing about longer trips.

Definition 2.5 (Adjacent; textbook Definition 1.1.4, p. 11). Vertices u and v are adjacent if
uv ∈ E [9, Definition 1.1.4, p. 11]. Then each is called a neighbour of the other.

Remark 2.6. Adjacency is symmetric (uv = vu), and no vertex is adjacent to itself, since there
are no loops. It says nothing about longer connections.

Example 2.7. In B, the vertices n1 and n2 are adjacent.

                                                        7
Non-example 2.8. In B, the vertices n1 and n3 are not adjacent, although a walk of length 2
joins them.

     In plain words. Make a square table with one row and one column for every
     house. Write a one where the row house and the column house share a road. Write
     a zero everywhere else. This table describes the whole village.

Definition 2.9 (Adjacency matrix; textbook p. 11, after Definition 1.1.6; board, first line). A
matrix is a rectangular table of numbers; its entry in row i and column j is written with the
indices i, j. The adjacency matrix of G is the N × N matrix A with Aij = 1 if ni and nj are
adjacent, and Aij = 0 otherwise [9, p. 11]. The board writes the same rule as Aij = 1 if eij ∈ V
and 0 if eij ∈/ V , with its V the edge set [4, 5].

Remark 2.10. The definition allows only the entries 0 and 1. It depends on how the vertices are
numbered: renumbering permutes rows and columns together. [derived here]

Example 2.11. The board matrix, with rows (0 1 0), (1 0 1), (0 1 0):
                                                
                                         0 1 0
                                  A = 1 0 1  ,
                                         0 1 0

is the adjacency matrix of B, since A12 = A21 = 1, A23 = A32 = 1 and all other entries are 0.

Non-example 2.12. The matrix with rows (0 1 0), (0 0 1), (0 1 0) is not the adjacency matrix
of any simple undirected graph: its entry A12 is 1 but A21 is 0, which would need a one-way
edge. A matrix with a 1 on the diagonal (a loop) or an entry 2 (a double edge) is not one either.

     In plain words. The table has some easy features. It looks the same when flipped
     over its diagonal. The diagonal holds only zeros. And any table of ones and zeros
     with these two features comes from some village.

Proposition 2.13 (Properties of A). For the adjacency matrix A of a simple undirected graph:

  1. every entry is 0 or 1;

  2. A is symmetric: Aij = Aji for all i, j;

  3. the diagonal is zero: Aii = 0 for all i;

  4. conversely, every N × N matrix of zeros and ones that is symmetric with zero diagonal is
     the adjacency matrix of some simple graph with numbered vertices.

These are stated in the textbook [9, pp. 11–12].

Proof. Items 1 to 3 are read off Definition 2.9: adjacency is symmetric and irreflexive (Re-
mark 2.6). Item 4: join ni and nj exactly when the entry is 1. Symmetry makes this a legitimate
set of unordered pairs, and the zero diagonal excludes loops.

Example 2.14. The board matrix is symmetric with zero diagonal, as items 2 and 3 require.

Non-example 2.15. The matrix with rows (0 1 0), (1 0 1), (1 1 0) is not symmetric (its entry
A31 is 1 and A13 is 0), so it is not an adjacency matrix.

     In plain words. The busy-ness of a house is the number of roads that meet there.
     We call that number the degree of the house.


                                                   8
Definition 2.16 (Degree; textbook Definition 1.2.1, p. 16). The degree of a vertex v, written
dG (v) or d(v) in the textbook, is the number of edges incident to v, that is, the number of edges
that contain v [9, Definition 1.2.1, p. 16]. This paper writes deg(ni ), to keep d for distance
(Definition 2.48).

Remark 2.17. In a simple graph the degree equals the number of neighbours, since each neighbour
is joined to ni by exactly one edge. [derived here] The textbook places the definition of degree
after the adjacency matrix, in Section 1.2, before the walks; this paper keeps that order.

Example 2.18. In B: deg(n1 ) = 1, deg(n2 ) = 2, deg(n3 ) = 1.

Non-example 2.19. deg(n1 ) is not 2 in B, although two other vertices can be reached from
n1 . Only edges at n1 count, and n3 is reached by passing through n2 .

      In plain words. Adding up one row of the table counts the roads at that house.
      Adding up the whole table counts every road twice, once from each end.

Proposition 2.20 (Row sums and the total). For the adjacency matrix A of a simple undirected
graph: (a) the sum of row i, and of column i, equals deg(n Pi ); (b) the sum of all entries equals
2|E|. Part (b) is the textbook’s Theorem 1.2.1 of Euler, v dG (v) = 2|E| [9, Theorem 1.2.1,
p. 16], read through (a). Part (a) is stated, for graphs that may have loops, by Paramadevan
and Sotheeswaran [7]. The proof here is [derived here].

Proof. (a) The sum of row i is the number of j with Aij = 1, that is, the number of neighbours
of ni . By Remark 2.17 this is deg(ni ). Column i gives the same by symmetry (Proposition 2.13).
(b) Add (a) over all i. Each edge ni nj is counted once in deg(ni ) and once in deg(nj ), so twice
in all.

Example 2.21. For the board matrix the row sums are 1, 2, 1, the degrees of Example 2.18,
and the sum of all entries is 4 = 2|E| with |E| = 2.

Non-example 2.22. The matrix of Non-example 2.15 has row sums 1, 2, 2, but it is not an
adjacency matrix, so part (a) does not apply to it.

2.2    Walks, trails, paths and cycles
The textbook uses the word “path” for a walk with no repeated edge (Definition 1.2.12) and
“simple path” for a walk with no repeated vertex (Definition 1.2.13) [9]. English texts and the
course convention use “path” for the second [3]. This paper uses trail for the first and path for
the second, as announced in Section 1.3. Table 7 in Section 5 shows the three conventions side
by side.

      In plain words. A trip is a list of houses. Each house on the list shares a road
      with the one before it. You may pass a house twice. You may drive a road twice.
      The length of a trip is the number of roads driven. A road driven twice counts twice.
      Staying at home is a trip of length zero. Books call a trip like this a walk.

Definition 2.23 (Walk; textbook Definition 1.2.10, p. 21). A walk of length k from u0 to uk ,
also called a (u0 , uk )-walk, is a sequence u0 , e1 , u1 , . . . , uk−1 , ek , uk of vertices and edges with
ei = ui−1 ui for 1 ≤ i ≤ k [9, Definition 1.2.10, p. 21]. Its length is k, the number of edges, each
edge counted as many times as it occurs [9, remark after Definition 1.2.10, p. 22].

Remark 2.24. Vertices and edges may repeat in a walk, and the length counts every use of an
edge [9, p. 22]. The only thing forbidden is a jump: two consecutive vertices must be adjacent.
In a simple graph the edge ei is fixed by its two ends (Remark 2.2), so a walk can be written

                                                     9
by its vertices alone, u0 , u1 , . . . , uk , and two walks are different exactly when these lists differ at
some position. [derived here] The textbook does not say in words that k = 0 is allowed. This
paper allows it, because the textbook’s own property d(u, u) = 0 (Definition 2.48) needs a walk
of length 0. [interpretation, qualified]

Example 2.25. In B the list 1, 2, 1, 2, 3 is a walk from n1 to n3 of length 4: its steps 12, 21, 12,
23 are all edges. Vertices 1 and 2 occur twice, and the edge 12 is used twice. The textbook’s
example is v1 , v3 , v2 , v4 , v3 , v2 , v4 , v3 , v5 in Gtb , a walk of length 8 [9, p. 22].

Non-example 2.26. In B the list 1, 3 is not a walk, because 13 is not an edge of B (the
matrix has A13 = 0). It would be a walk of the drawing T . The textbook’s non-example is
v3 , v1 , v4 , v2 , v3 , v5 , which is not a walk of Gtb [9, p. 22].

       In plain words. A trip is closed when it ends at the house where it began. That
       is the only new rule. The trip may still pass houses and roads many times.

Definition 2.27 (Closed walk; textbook Definition 1.2.11, p. 22). A (u0 , uk )-walk is closed if
u0 = uk [9, Definition 1.2.11, p. 22].

Remark 2.28. A closed walk allows everything a walk allows; it forbids only a different start and
end. A walk of length 0 is closed. In a simple graph a closed walk cannot have length 1 (that
would be a loop), and one of length 2 must be u, w, u and so uses one edge twice. [derived here]

Example 2.29. In B the walks 2, 1, 2 (length 2) and 2, 3, 2, 1, 2 (length 4) are closed.

Non-example 2.30. In B the walk 1, 2, 3 is not closed: it starts at 1 and ends at 3.

       In plain words. Now add one rule. Never drive the same road twice. You may
       still pass a house twice, if you return by another road. English books call such a trip
       a trail. Our textbook calls it a path. This paper says trail, so that the word path
       can keep one meaning.

Definition 2.31 (Trail; textbook Definition 1.2.12, p. 22, where it is called a “path”). A
(u0 , uk )-walk is a trail if its edges u0 u1 , . . . , uk−1 uk are pairwise distinct. The textbook calls
this a path [9, Definition 1.2.12, p. 22]; English usage calls it a trail [3].

Remark 2.32. A trail allows repeated vertices and forbids repeated edges. A vertex can recur
in a trail only if the walk left it by one edge and came back by another, so the trail contains a
closed trail, a detour that comes back to the same vertex. In B every trail is also a path in the
sense of Definition 2.35: a repeated vertex would need a closed trail, which needs at least three
edges (Remark 2.28), and B has two. So B cannot show the difference; H and the textbook’s
graph can. [derived here]

Example 2.33. In Gtb the list v1 , v3 , v2 , v4 , v3 , v5 is a trail: its edges v1 v3 , v3 v2 , v2 v4 , v4 v3 , v3 v5
are distinct, although v3 occurs twice [9, p. 22]. In H the list 4, 3, 1, 2, 3 is a trail: its edges 43,
31, 12, 23 are distinct, although vertex 3 occurs twice.

Non-example 2.34. The walk v1 , v3 , v2 , v4 , v3 , v2 , v4 , v3 , v5 of length 8 is not a trail: the edge
v3 v2 occurs twice [9, p. 22]. In B the walk 1, 2, 1, 2, 3 is not a trail, since the edge 12 occurs
twice; in H the walk 1, 2, 3, 2 is not a trail, since the edge 23 occurs twice.

       In plain words. Now add a stronger rule. Never pass the same house twice. Then
       you never drive a road twice either. A trip like this is a route. It goes straight from
       start to end. It has no detour in it. Our course calls it a path. The textbook calls
       it a simple path.

                                                         10
Definition 2.35 (Path; textbook Definition 1.2.13, p. 22, where it is called a “simple path”).
A (u0 , uk )-walk is a path if its vertices u0 , . . . , uk are pairwise distinct. The textbook calls this
a simple path and writes Pn for the simple path on n vertices (here n counts the vertices of that
path, not of the whole graph) [9, Definition 1.2.13, p. 22]. Its length is k.

Remark 2.36. A path forbids repeated vertices, hence also repeated edges (Proposition 2.39).
It allows length 0 (a single vertex is a path from that vertex to itself) and length 1 (one edge).
It does not allow a closed path of positive length, because the first and last vertex would be
equal. The textbook defines a simple path as a trail with distinct vertices; by Proposition 2.39
this is the same as a walk with distinct vertices, so the two ways of saying it agree. That the
course uses “path” in this sense is [interpretation, qualified] : it rests on the user’s report of the
assignment text, and the board does not say.

Example 2.37. In B the list 1, 2, 3 is a path from n1 to n3 of length 2. In H the list 4, 3, 1, 2
is a path of length 3. The textbook’s example is v1 , v3 , v4 , v5 in Gtb , a simple path [9, p. 22].

Non-example 2.38. In B the list 1, 2, 3, 2 is a walk but not a path: vertex 2 occurs twice. In
Gtb the list v1 , v3 , v2 , v4 , v3 , v5 is a trail but not a simple path, since v3 occurs twice [9, p. 22].
In H the trail 4, 3, 1, 2, 3 is not a path for the same reason.

      In plain words. A trip that never passes a house twice never drives a road twice.
      Here is why. Take two roads on the trip, an earlier one and a later one. The later
      road ends at a house that the earlier road does not touch. So the two roads are
      different.

Proposition 2.39 (A path is a trail). In a simple graph, a walk with pairwise distinct vertices
has pairwise distinct edges. So every path is a trail. [derived here]

Proof. Let u0 , . . . , uk have pairwise distinct vertices, and take two steps with indices a < b, that
is, the edges ua−1 ua and ub−1 ub . The vertex ub has an index larger than the indices a − 1 and
a, so it differs from both ua−1 and ua . But ub is an end of the second edge and is not an end of
the first. So the two edges are different. (Grinberg leaves this statement as an exercise [3].)

      In plain words. A cycle is a closed trip that never drives a road twice. It may
      pass a house twice on the way. An English book calls it a closed trail.

Definition 2.40 (Cycle; textbook Definition 1.2.14, p. 22). A trail that is a closed walk is called
a closed path or cycle [9, Definition 1.2.14, p. 22]. In the words of this paper, a cycle is a closed
trail: a (u0 , uk )-walk with u0 = uk and pairwise distinct edges. Vertices may repeat.

Remark 2.41. The definition allows repeated vertices (a figure eight is a cycle) and forbids
repeated edges and open walks. English usage differs: Grinberg’s “cycle” needs distinct vertices
and is the textbook’s simple cycle [3]. The textbook is silent on whether a closed trail of length
0 is a cycle; this paper does not count it [interpretation, qualified].

Example 2.42. In Gtb the list v3 , v2 , v1 , v3 , v5 , v4 , v3 is closed and has six distinct edges, so it
is a cycle in this sense; it is not a simple cycle, since v3 occurs three times [9, p. 22].

Non-example 2.43. In B the closed walk 1, 2, 1 is not a cycle, because the edge 12 is used
twice; in H the closed walk 4, 3, 4 is not a cycle for the same reason. In fact B has no cycle
at all: a cycle is a closed trail, in a simple graph a closed trail of positive length needs at least
three distinct edges (Remark 2.28), and B has only two edges. [derived here]

      In plain words. A simple cycle is stricter. It passes no house twice, except the
      start, which is also the end. It is a ring of houses, each joined by a road to the next.

                                                    11
Definition 2.44 (Simple cycle; textbook Definition 1.2.15, p. 22). A cycle is simple if only its
first and last vertices coincide. The simple cycle on n vertices is written Cn , with n ≥ 3 (again
n counts the vertices of the cycle) [9, Definition 1.2.15, p. 22].

Remark 2.45. A simple cycle forbids any repeated vertex other than the closing one. The con-
dition n ≥ 3 is forced in a simple graph: a closed trail cannot have length 1 or 2 (Remark 2.28).
[derived here]

Example 2.46. In Gtb the list v1 , v3 , v4 , v2 , v1 is a simple cycle [9, p. 22]. In the board drawing
T and in H the list 1, 2, 3, 1 is a simple cycle of length 3 (by script).

Non-example 2.47. The cycle v3 , v2 , v1 , v3 , v5 , v4 , v3 of Example 2.42 is not simple, because v3
occurs three times [9, p. 22].

      In plain words. The distance between two houses is the number of roads on the
      shortest trip between them. If no trip exists, the distance is called infinite. A house
      is at distance zero from itself. The distance there equals the distance back, because
      any trip can be driven backwards. Going by way of a third house is never shorter
      than the shortest trip.

Definition 2.48 (Distance; textbook Definition 1.2.16, pp. 22–23). The distance d(u, v) =
dG (u, v) between vertices u and v is the length of a shortest (u, v)-trail if at least one (u, v)-trail
exists, and +∞ otherwise [9, Definition 1.2.16, pp. 22–23]. (The textbook’s word is “path”, its
Definition 1.2.12.)

Remark 2.49. The textbook lists three properties [9, p. 23]:

   1. d(u, v) ≥ 0, and d(u, v) = 0 if and only if u = v;

   2. d(u, v) = d(v, u);

   3. d(u, v) ≤ d(u, w) + d(w, v).

So if any two vertices are joined by a trail, (V, d) is a metric space [9]; a metric space is just a
set with a distance that satisfies these three properties, and the word is not used again. The
definition allows the value +∞, which is not an integer; this is how a missing trail shows up. It
forbids negative values and any value that is not the length of an actual trail. The shortest trail,
the shortest path and the shortest walk between two vertices have the same length, because a
shortest walk contains a path that is no longer than itself (Lemma 2.52); so the definition does
not depend on whether “path” is read as trail or path (proof in Appendix A.5). [derived here]

Example 2.50. In B: d(1, 2) = 1, d(2, 3) = 1, d(1, 3) = 2, and d(i, i) = 0 for each i (by script).
The walk 1, 2, 1, 2, 3 has length 4, but d(1, 3) is 2, the shortest.

Non-example 2.51. The number 4 is not the distance from 1 to 3 in B, even though a walk
of length 4 exists: distance is the minimum, not any length. In the graph D with vertices 1, 2, 3
and the single edge 12 (Figure 4), d(1, 3) is not a number at all; it is +∞ (by script).


                                      1           2            3
                                       u           u            u



Figure 4: The graph D: three vertices and the single edge 12. Vertex 3 is isolated. It is the
board graph B with the edge 23 removed.



                                                  12
2.3    From walks to paths
      In plain words. Suppose you can drive from one house to another. Then you can
      do so without passing any house twice. Look at your trip. If it passes some house
      twice, you went on a detour that came back to the same house. Cut the detour out.
      What is left is still a trip between the same two houses. It is shorter. Keep cutting
      detours until no house repeats. The trip that remains is never longer than the first
      one.

Lemma 2.52 (Every walk contains a path; textbook Lemma 1.2.1, p. 23, for u ̸= v). Let u and
v be vertices of a simple graph, equal or different. If there is a (u, v)-walk of length k, then there
is a (u, v)-path of length at most k. All vertices and edges of this path are vertices and edges of
the walk.
    The textbook states the lemma for u ̸= v, as “from any (u, v)-walk one can extract a simple
(u, v)-path”, without a length bound, and proves it by induction on the length of the walk [9,
Lemma 1.2.1, p. 23]. Grinberg’s Corollary 2.9.7 covers u = v and gives the length bound [3,
Corollary 2.9.7, p. 39]. The case u = v is needed here, because a closed walk such as 2, 1, 2 in B
has u = v; the path it contains is the single vertex, of length 0. The proof below is the paper’s
own [derived here] ; it follows the textbook’s method.

Proof. First an example of the idea. In B the walk 1, 2, 1, 2, 3 has the vertex 1 at positions 0
and 2; removing the part between them leaves 1, 2, 3, a shorter walk with the same ends, and it
is a path.
     We prove by strong induction on k the statement P (k): every (u, v)-walk of length k, for
any vertices u and v, contains a (u, v)-path of length at most k.
     Base case, k = 0. A walk of length 0 is a single vertex u, so v = u. A single vertex has no
repeated vertex, so the walk is itself a path, of length 0 ≤ 0.
     Induction hypothesis. Let k ≥ 1 and assume P (m) holds for every m < k.
     Step. Let u0 , u1 , . . . , uk be a (u, v)-walk, so u0 = u and uk = v. Case 1: the vertices
u0 , . . . , uk are pairwise distinct. Then the walk is a path of length k ≤ k. Case 2: some vertex
occurs twice, so ui = uj for some i < j. Form the list W ′ = u0 , . . . , ui , uj+1 , . . . , uk . If j = k,
the part after ui is empty and W ′ ends at ui . We check that W ′ is a (u, v)-walk. (a) It starts
at u0 = u. (b) It ends at v: if j < k its last vertex is uk = v; if j = k its last vertex is
ui = uj = uk = v. (c) Consecutive vertices are adjacent: before the cut and after the cut they
are consecutive vertices of the old walk, and at the join the pair is (ui , uj+1 ) = (uj , uj+1 ), which
is a step of the old walk. The length of W ′ is i + (k − j), and since i < j this is less than k.
By the induction hypothesis W ′ contains a (u, v)-path of length at most that, hence at most k.
Every vertex and edge of that path is one of W ′ , and so one of the old walk.

   Why the proof is valid: each cut removes at least one step, since j − i ≥ 1, so the length
drops by at least 1 and the process stops. A walk that cannot be cut has no repeated vertex,
which is the definition of a path.
Remark 2.53. The textbook’s walk of length 8 in Gtb is 1, 3, 2, 4, 3, 2, 4, 3, 5, written by the
indices of its vertices, with positions counted from 0. Positions 1 and 4 both hold vertex 3 (so
u1 = u4 = 3). The cut removes the detour in brackets and keeps the rest:

                      1, 3, [2, 4, 3], 2, 4, 3, 5 −→ 1, 3, 2, 4, 3, 5    (length 5).

In the shorter walk positions 1 and 4 again both hold vertex 3, and the cut leaves a path:

                       1, 3, [2, 4, 3], 5 −→ 1, 3, 5     (a path of length 2 ≤ 8).

In B the walk 1, 2, 1, 2, 3 cuts to 1, [2, 1], 2, 3 → 1, 2, 3; the closed walk 2, 1, 2 cuts to the single
vertex 2. (Checked by script, Appendix A.7.)

                                                    13
      In plain words. A trip that never repeats a house can pass each house at most
      once. So when the number of houses is fixed, such a trip is short. It uses at most
      one road fewer than the number of houses.

Corollary 2.54 (Length bound). In a graph with N vertices every path has at most N − 1
edges. Hence, if there is a walk from u to v, there is a walk from u to v of length at most N − 1.
[derived here]

Proof. A path of length k lists k + 1 pairwise distinct vertices, and there are only N vertices, so
k + 1 ≤ N , that is k ≤ N − 1. For the second part, Lemma 2.52 gives a path inside the walk, of
length at most that of the walk and at most N − 1; a path is itself a walk. Grinberg gives the
same argument [3, Section 2.9.4, p. 40].

   For B, N = 3, so a path has at most 2 edges; the longest path in B has 2 edges (by script).

2.4   Connected graphs and components
      In plain words. Sometimes you can reach every house from every other house.
      Then the village is called connected. If one house is cut off, the village is not
      connected.

Definition 2.55 (Connected; textbook Definition 2.1.1, p. 48; board, last line). A graph G is
connected if for any two vertices u and v of G there is a (u, v)-path in G [9, Definition 2.1.1,
p. 48]. The board says the same: “Graph is called connected if for any ni , nj there exists a path
between nodes” [4, 5].

Remark 2.56. In the textbook the word “path” here is Definition 1.2.12, a trail; the board does
not say which meaning it uses. The next proposition shows that the choice does not change
which graphs are connected. “Any two vertices” includes u = v; for u = v the one-vertex walk is
a (u, u)-path, so these pairs are always satisfied, and reading the definition as “any two different
vertices” changes nothing. [interpretation; the textbook does not discuss u = v] The definition
forbids exactly one thing: a pair of vertices with no path between them.

Example 2.57. The board graph B is connected: the pair 1, 3 is joined by the path 1, 2, 3, and
the pairs 1, 2 and 2, 3 by one edge each. The textbook’s examples of connected graphs are the
complete graphs, the complete bipartite graphs, and the three graphs of its Fig. 2.1.1 [9, p. 48].

Non-example 2.58. The graph D (Figure 4) is not connected: no walk starts at vertex 3 and
ends elsewhere, so the pair 1, 3 has no path. The textbook’s non-example is the graph of its
Fig. 2.1.2, which has four components [9, p. 49].

      In plain words. It does not matter which kind of trip we ask for. If any trip links
      two houses, a route links them. Every route is a trail. Every trail is a trip. So all
      three questions have the same answer.

Proposition 2.59 (Three readings of “connected” agree). For vertices u, v of a simple graph
the following are equivalent: (a) there is a (u, v)-walk; (b) there is a (u, v)-trail; (c) there is a
(u, v)-path. Hence G is connected in the textbook’s sense (trails) if and only if every two vertices
are joined by a path, if and only if every two vertices are joined by a walk. [derived here from
Lemma 2.52]

Proof. (c)⇒(b): every path is a trail (Proposition 2.39). (b)⇒(a): every trail is a walk, by
definition. (a)⇒(c): Lemma 2.52. Grinberg states the equivalence of (a) and (c) as his Propo-
sition 2.9.10 [3, p. 42]; the lemma behind (a)⇒(c) is the textbook’s Lemma 1.2.1 for u ̸= v and
Grinberg’s Corollary 2.9.7 in general.

                                                 14
      In plain words. A village that is not connected falls into pieces. Inside one piece
      every house can reach every other house. No road joins two different pieces. Each
      piece is called a component. A connected village has exactly one piece.

Definition 2.60 (Connected component; textbook, p. 49, paragraph before Remark 2.1.1). On
the vertex set V write u ∼ v if there is a (u, v)-path in G. This relation is reflexive (every vertex
is related to itself), symmetric (if u ∼ v then v ∼ u) and transitive (if u ∼ v and v ∼ w then
u ∼ w) [9, p. 49]. Here is why, reading “path” as walk, which is allowed by Proposition 2.59:
the one-vertex walk gives reflexivity, reversing a walk gives symmetry, and joining a (u, v)-walk
to a (v, w)-walk gives a (u, w)-walk, which gives transitivity [derived here]. Hence V splits into
classes V1 , . . . , Vp : groups of vertices such that each vertex lies in exactly one group, and two
vertices lie in the same group exactly when they are related. The subgraphs Gj = G[Vj ] (the
vertices of Vj with every edge of G that has both ends in Vj ) are the connected components of
G [9, p. 49]. The textbook gives this in prose, without a definition number.
Remark 2.61. A component is a whole class: a vertex reachable from a vertex of Vj lies in
Vj . The textbook’s Remark 2.1.1 states that G is connected if and only if it has exactly one
connectivity component [9, Remark 2.1.1, p. 49]. By Proposition 2.59 the relation ∼ is the same
whether “path” means trail, path or walk.
Example 2.62. The graph D has the two components G[{1, 2}] and G[{3}]; the board graph
B has the single component G[{1, 2, 3}] (checked by breadth-first search in the script, Ap-
pendix A.7).
Non-example 2.63. G[{1}] is not a component of D, although it is a connected subgraph:
vertex 2 can be reached from vertex 1, so 2 lies in the same class as 1. A component is a whole
class, not any connected piece. [derived here]


3     Answer 1: what the entry of a power of A counts
Question 1 asks what (Ak )ij represents. The answer is a count of walks (Definition 2.23), and
the proof needs only the definition of the matrix product, so that product comes first.

3.1   Matrix products and powers
      In plain words. To multiply two tables, take a row from the first and a column
      from the second. Multiply the numbers in pairs. Then add the results. Do this for
      every row and every column to build the new table. Multiply the road table by itself
      again and again, and you get its powers.

Definition 3.1 (Matrix product and power). Let X and Y be N × N matrices. Their product
XY is the N × N matrix with
                                            N
                                            X
                                  (XY )ij =    Xir Yrj .                            (1)
                                                  r=1

The powers of a square matrix A are A1 = A and Ak = Ak−1 A for k ≥ 2.
Remark 3.2. Formula (1) multiplies row i of X with column j of Y entry by entry and adds. A
power is the repeated product of the whole matrix, not a power of each entry. This paper uses
exponents k ≥ 1 only.
Example 3.3. For the board matrix, (A2 )22 = A21 A12 +A22 A22 +A23 A32 = 1·1+0·0+1·1 = 2
(by script, Appendix A.7).
Non-example 3.4. A2 is not the matrix of squared entries. Squaring each entry of the board
matrix gives back A, whose entry (1, 2) is 1, while (A2 )12 = 0.

                                                 15
3.2     The walk-counting theorem
       In plain words. Take the table of roads and multiply it by itself. Each number
       in the new table counts trips of two roads. The trips run from the row house to
       the column house. Multiply again and you count trips of three roads. The count
       includes trips that turn back. So the table counts trips, not routes.

Theorem 3.5 (Walk counting). Let A be the adjacency matrix of a simple undirected graph G
with vertices n1 , . . . , nN , and let k ≥ 1 be an integer. Then (Ak )ij is the number of walks of
length k from ni to nj , for all i, j.

    The statement is Theorem 1.1.3 of the University of Galway notes, for exactly this setting [2,
Theorem 1.1.3]. Bai states it for simple graphs in his Theorem 1 [1]; Grinberg (for multidi-
graphs) and Lehman, Leighton and Meyer (for digraphs) state it in more general settings [3,
Theorem 4.5.10, pp. 120–121][6, Corollary 9.3.3]. The textbook does not state the theorem (Sec-
tion 1.6) [qualified], so the proof below is written out in full. It follows the standard approach:
induction on k, splitting the walks by their second-last vertex [2, 3]. The write-up is [derived
here]. One journal paper states a different version, with “paths” in place of walks; it is false,
and Section 3.4 shows why.
Remark 3.6. The theorem allows i = j, which counts closed walks, and it counts every walk
once, with repeated vertices and edges allowed. It forbids reading the number as a count of
paths (Proposition 3.10). It says nothing about walks of other lengths: (A2 )12 = 0 on the board
graph does not say that n1 and n2 are unconnected.

Example 3.7. On the board graph B, (A2 )13 = 1: the only walk of length 2 from n1 to n3 is
1, 2, 3. And (A3 )12 = 2: the walks of length 3 from n1 to n2 are 1, 2, 1, 2 and 1, 2, 3, 2. All entries
are written out in Section 6.

Non-example 3.8. (A2 )12 = 0 on B does not mean that no walk joins n1 and n2 . It means
only that no walk of length exactly 2 does; walks of length 1 and of length 3 exist.

Proof. We use induction on k. Write Wk (i, j) for the number of walks of length k from ni to nj .
We prove Wk (i, j) = (Ak )ij for all i, j, for each k ≥ 1. In a simple graph a walk is determined
by its list of vertices (Remark 2.24). So Wk (i, j) is the number of lists (w0 , . . . , wk ) of vertices
with w0 = ni , wk = nj , and wt−1 adjacent to wt for each t from 1 to k.
    Base case, k = 1. A walk of length 1 from ni to nj is a list (ni , nj ) with ni and nj adjacent.
There is exactly one such list if they are adjacent and none otherwise. So W1 (i, j) = Aij = (A1 )ij .
    Induction hypothesis. Let k ≥ 2 and suppose Wk−1 (i, j) = (Ak−1 )ij for all i, j.
    Induction step. Fix i and j. Every walk (w0 , . . . , wk ) of length k from ni to nj has a second-
last vertex wk−1 . Because k ≥ 2, deleting the last vertex leaves w0 , . . . , wk−1 , which still has
length k − 1 ≥ 1, so the hypothesis applies to it. (For k = 1 nothing would remain to count;
this is why k = 1 is the separate base case.) Let wk−1 = nr , where r is one of 1, . . . , N . Sort
the walks into N classes by the value of r. The classes are disjoint, since each walk has exactly
one second-last vertex, and together they contain every walk. So
                    N
                    X                                                                         
      Wk (i, j) =         number of walks of length k from ni to nj with second-last vertex nr .
                    r=1

We claim that the number in class r is Wk−1 (i, r) Arj .

    If nr and nj are not adjacent, then Arj = 0. No walk can have nr followed by nj , so class
     r is empty, and its count 0 equals Wk−1 (i, r) · 0.



                                                    16
    If nr and nj are adjacent, then Arj = 1. Delete the last vertex of a walk in class r. What
     remains is a list w0 , . . . , wk−1 with w0 = ni , wk−1 = nr and consecutive vertices adjacent,
     so it is a walk of length k − 1 from ni to nr . Conversely, take any walk of length k − 1 from
     ni to nr and append nj . The new pair nr , nj is adjacent, so the result is a walk of length
     k from ni to nj with second-last vertex nr . Deleting and appending undo each other, so
     they match the walks in class r one to one with the walks of length k − 1 from ni to nr .
     The count is Wk−1 (i, r) = Wk−1 (i, r) · 1.

Therefore Wk (i, j) = r Wk−1 (i, r) Arj . By the induction hypothesis Wk−1 (i, r) = (Ak−1 )ir , so
                      P

                                    N
                                    X
                        Wk (i, j) =   (Ak−1 )ir Arj = (Ak−1 A)ij = (Ak )ij ,
                                   r=1

by formula (1) and the definition of powers. This proves the statement for k, and so, by induction,
for every k ≥ 1.

Why the argument is valid. Two facts carry it: the sum over the second-last vertex covers
each walk exactly once, and the matching in the case Arj = 1 is one to one. Simplicity is used
twice: to identify a walk with its vertex list, and so that Arj , which is the number of edges
between nr and nj , is 0 or 1. Undirectedness is not used inside the induction; it only makes
A symmetric. [interpretation] The proof is checked, not replaced, by a finite test: a script
compared the walk count with the matrix entry for every labelled simple graph on 2, 3, 4, 5
vertices (Appendix A.6). That test is a check, not a proof.

3.3   Consequences of the theorem
      In plain words. A count is never negative and always a whole number. The table
      of trips looks the same when flipped over its diagonal. A positive number means
      that at least one such trip exists. For trips of two roads, the diagonal counts the
      roads at a house.

Corollary 3.9. For a simple undirected graph and k ≥ 1:

 (a) every entry of Ak is a non-negative integer, so a sum of such powers has a positive (i, j)
     entry if and only if at least one summand does;

 (b) (Ak )ij > 0 if and only if there is a walk of length exactly k from ni to nj ;

 (c) Ak is symmetric;

 (d) (A2 )ii = deg(ni ), so the sum of the diagonal entries of A2 equals 2|E|.

[derived here]

Proof. Parts (a) and (b) follow because by Theorem 3.5 each entry is a count. For (c), (Ak )T =
(AT )k = Ak , where the transpose X T of a matrix X is the matrix with its rows and columns
exchanged, and AT = A because A is symmetric (Proposition 2.13); alternatively, reversing a
walk matches the walks from ni to nj with the walks from nj to ni . For (d), the walks of
length 2 from ni to ni are the lists ni , nr , ni with nr a neighbour of ni , one for each neighbour,
and the number of neighbours is deg(ni ) (Remark 2.17). Summing over i and using part (b) of
Proposition 2.20 gives 2|E|. The University of Galway notes state (d) in a remark after their
theorem [2].

    On the board graph the diagonal of A2 is (1, 2, 1), the degrees, and its sum is 4 = 2|E|
(script).

                                                 17
3.4   The warning: walks are not paths
      In plain words. A trip may turn back and pass the same house twice. A route
      never passes a house twice. The table counts trips, so it also counts the trips that
      turn back. A house with at least one neighbour always has a two-road trip that goes
      out and comes home. That trip is no route.

Proposition 3.10 (The entry is not a count of paths). Let G be a simple undirected graph.

 (a) If ni has at least one neighbour, then (A2 )ii = deg(ni ) > 0, yet there is no path, and no
     trail, of length 2 from ni to ni .

 (b) On the board graph B, (A3 )12 = 2, although the only path from n1 to n2 has length 1. More
     generally, on B (and not for every graph) Ak+2 = 2Ak for k ≥ 1 (the matrix A3 = 2A is
     written out in Example 6.1). So (Ak )12 doubles each time k grows by 2, along 1, 2, 4, . . .
     for odd k, while the number of paths from n1 to n2 stays 1 for k = 1 and is 0 for every
     larger k.

[derived here]

Proof. (a) By Corollary 3.9(d), (A2 )ii = deg(ni ), which is positive. The only walks of length 2
from ni to ni are ni , nr , ni . They repeat the vertex ni , so they are not paths (Definition 2.35);
a path from a vertex to itself has pairwise distinct vertices, so its length is 0. They repeat
the edge ni nr , so they are not trails either (Definition 2.31). The textbook’s own word “path”
(Definition 1.2.12) means a trail, so the entry is not a count of the textbook’s paths either. (b)
On B the walks of length 3 from n1 to n2 are 1, 2, 1, 2 and 1, 2, 3, 2. Each repeats a vertex and
an edge, so neither is a path or a trail. The only path from n1 to n2 is the single edge 1, 2. For
the growth, A3 = 2A (script) and multiplying by Ak−1 gives Ak+2 = 2Ak .

    The sources say the same in words: Bai remarks that the entries count walks and not
paths [1], and Grinberg’s Example 2.9.2 shows a walk that is not a path [3, p. 37] . Table 5 gives
the counts from the script for k = 1, . . . , 5: the walk counts 1, 0, 2, 0, 4 against the path counts
1, 0, 0, 0, 0.

Table 5: Walks of length k from n1 to n2 on the board graph B, and how many of them are
paths and trails (by script). The walk counts equal the entries (Ak )12 of Section 6.
                           k   walks    of which paths    of which trails
                           1      1            1                 1
                           2      0            0                 0
                           3      2            0                 0
                           4      0            0                 0
                           5      4            0                 0

    Paramadevan and Sotheeswaran’s Theorem 1 reads: “the number of different paths of length
l between the i-th and j-th vertices of G is equal to the (i, j)-th entry of AlG ” [7]. As written
this is false for any definition of path that forbids repeated vertices or repeated edges, by
Proposition 3.10(a); their own property 7 says walks [7]. So the sources disagree, and the paper
follows the walk version, which four sources state (the University of Galway notes, Grinberg,
Lehman, Leighton and Meyer, and Bai [2, 3, 6, 1]) and which was proved above.
    What a positive entry does guarantee is a walk of length k, and then, by Lemma 2.52, a path
of length at most k. This is why the warning does not harm the connectivity test of Section 4;
but the value of the entry is a count of walks, not of paths. [derived here]


                                                   18
4      Answer 2: testing connectedness from A alone
Question 2 asks how to know from A whether the graph is connected (Definition 2.55). The
idea is to turn the question about paths into a question about counts. By Theorem 3.5, the
entries of the powers of A count walks. By Lemma 2.52, a walk between two vertices contains a
path between them, and by Corollary 2.54 that path is short. So it is enough to look at walks
of length at most N − 1.

Proof map. The test (Theorem 4.6) is proved from three earlier results. Theorem 3.5 says
that a positive entry of Ak is a walk of length k. Lemma 2.52 turns any walk into a path
between the same two vertices. Corollary 2.54 says that such a path has at most N − 1 edges,
so powers beyond N − 1 add nothing. Proposition 4.5 joins these into a statement about one
pair of vertices, and Theorem 4.6 collects the pairs.

4.1     The running total S
       In plain words. We need a name for the running total. It adds the counts of trips
       with one road, with two roads, and so on. We stop at the power that is one less than
       the number of houses. The whole check uses this one total.

Definition 4.1 (The matrix S; new notation, not from the textbook). For a graph with N ≥ 2
vertices, let
                                S = A + A2 + · · · + AN −1 ,                           (2)
the sum of the first N − 1 powers of A, added entry by entry.

Remark 4.2. By Theorem 3.5, Sij is the number of walks from ni to nj whose length is between
1 and N − 1. Hence every entry of S is a non-negative integer. The diagonal of S counts closed
walks and plays no part in the test (Remark 4.11). [derived here]

Example 4.3. For the board graph B, N = 3, so S = A + A2 :
                                                       
                           0 1 0        1 0 1         1 1 1
                     S = 1 0 1 + 0 2 0 = 1 2 1 .
                           0 1 0        1 0 1         1 1 1

Non-example 4.4. For N = 3, neither A alone nor A2 alone is S. The matrix A2 of B has the
zero entry (1, 2) although n1 and n2 are joined by an edge. The matrix A has the zero entry
(1, 3) although n1 and n3 are connected through n2 . Either one alone would wrongly report
“not connected”. [derived here]

4.2     The test and its proof
       In plain words. We want a quick check for a village. We only have the table of
       shared roads. From the table we can count trips. Count the trips with one road,
       with two roads, and so on. Add the counts for each pair of houses. If no pair of
       different houses has a total of zero, the village is connected. We never need trips
       longer than one road fewer than the number of houses. A trip that wastes time can
       always be shortened. So longer trips tell us nothing new.

Proposition 4.5 (One pair at a time). Let G have N ≥ 2 vertices and let i ̸= j. The following
are equivalent.

    (i) There is a path from ni to nj (distinct vertices; by Proposition 2.59 this is the same as
        asking for a trail or a walk).

                                                19
 (ii) There is an integer k with 1 ≤ k ≤ N − 1 and (Ak )ij > 0.

(iii) Sij > 0.

Proof. (i)⇒(ii). Let P be a path from ni to nj , of length k. By Corollary 2.54, k ≤ N − 1.
Because ni ̸= nj , a walk of length 0 cannot join them, so k ≥ 1. P is a walk of length k from ni
to nj , so by Theorem 3.5 the number (Ak )ij is at least 1.
    (ii)⇒(iii). Sij = Aij + (A2 )ij + · · · + (AN −1 )ij . Each term is a count, hence a non-negative
integer (Corollary 3.9(a)). A sum of non-negative numbers is at least as large as any one of its
terms. The term with the index k of (ii) is positive, so Sij > 0.
    (iii)⇒(ii). If Sij > 0, a sum of non-negative terms is positive, so at least one term (Ak )ij
with 1 ≤ k ≤ N − 1 is positive.
    (ii)⇒(i). If (Ak )ij > 0 with k ≥ 1, then by Theorem 3.5 there is at least one walk of length
k from ni to nj . Since ni ̸= nj , Lemma 2.52 gives a path from ni to nj .

      In plain words. Here is the answer in short. Pick any two different houses. Look
      for a trip between them. It never needs more roads than the number of houses, less
      one. The village is connected when every such pair has one. The table of counts lets
      us read this off.

Theorem 4.6 (The connectivity test). Let G be a graph with N ≥ 2 vertices and adjacency
matrix A. Then G is connected if and only if every entry off the diagonal of S = A + A2 + · · · +
AN −1 is positive.

    The statement appears in Paramadevan and Sotheeswaran’s Theorem 2 [7] and in Weisstein’s
entry on connected graphs [11]. The proof in the first is incomplete (Section 7.2), so the paper
proves the test itself and cites these sources for the statement only. The textbook does not state
it (Section 1.6) [qualified]. The proof is [derived here].
Remark 4.7. The test allows any graph with N ≥ 2 vertices, connected or not. It looks only
at entries with i ̸= j. It forbids requiring positive diagonal entries (Remark 4.11) and forbids
stopping at AN −2 (Proposition 4.17).

Example 4.8. The board graph B has S as in Example 4.3: no zero entry, so B is connected,
which agrees with Example 2.57.

Non-example 4.9. The graph D (one edge 12) has the matrix S written out in Section 6, with
zeros at (1, 3), (2, 3), (3, 1), (3, 2). So D is not connected, which agrees with Non-example 2.58.

Proof. By Definition 2.55 and Proposition 2.59, G is connected if and only if every two vertices
are joined by a path. For a pair with u = v this is always true, by the one-vertex path (Re-
mark 2.56). For a pair ni , nj with i ̸= j it is statement (i) of Proposition 4.5. By Proposition 4.5
that is equivalent to Sij > 0. So G is connected if and only if Sij > 0 for every i ̸= j.

Why the argument is valid. It uses three results and nothing else: the walk count (The-
orem 3.5), the walk-to-path lemma (Lemma 2.52) with its length bound (Corollary 2.54), and
the fact that a count is a non-negative integer, so a sum is positive exactly when a term is. The
last step would fail with subtraction or with arithmetic modulo a number, which can cancel
positive terms: for the triangle T , the matrix S = A + A2 has every off-diagonal entry equal to
2 (by script), and modulo 2 these entries are 0, so the test would wrongly say “not connected”.
The exponent N − 1 is the largest one needed because a walk of any length contains a path
(Lemma 2.52) of at most N − 1 edges (Corollary 2.54), and that path is again a walk, counted
by one of the powers up to N − 1; adding higher powers cannot change which off-diagonal entries
are positive.


                                                 20
      In plain words. The same counts also tell us the pieces of a village. Two different
      houses are in the same piece exactly when some trip joins them. To find the distance,
      count the trips of one road, then of two roads, and so on. The first number of roads
      that has a trip is the distance.

Corollary 4.10 (Components and distances from the powers). For any graph with N ≥ 2
vertices, connected or not, and i ̸= j: (a) Sij > 0 if and only if ni and nj lie in the same
component. (b) If they do, d(ni , nj ) is the smallest k ≥ 1 with (Ak )ij > 0; if they do not, no
power has a positive (i, j) entry and d(ni , nj ) = +∞. [derived here]

Proof. (a) Proposition 4.5 never uses that G is connected. Its statement (i) says ni ∼ nj , which
is the definition of lying in one class, that is in one component (Definition 2.60). (b) Let k0 be
the smallest k ≥ 1 with (Ak )ij > 0. By Theorem 3.5 a walk of length k0 exists and no shorter
walk does. By Lemma 2.52 a path of length at most k0 exists; being a walk, it has length at
least k0 . So the shortest walk has length k0 , and the distance equals the length of the shortest
walk (Appendix A.5). If no power has a positive entry, there is no walk and the distance is
+∞.

   The distance statement is also made by Lehman, Leighton and Meyer, and by Paramadevan
and Sotheeswaran in their Theorem 3 [6, 7]. The entry Sij tells whether ni and nj are connected,
not which path joins them.
Remark 4.11 (The diagonal, and the cases N = 1 and N = 2). For N = 2 and one edge, S = A
has zeros on the diagonal although the graph is connected:
                                                  
                                               0 1
                                        A=           .
                                               1 0

So the diagonal of S cannot be required to be positive. For N ≥ 3 and G connected the diagonal
of S is positive anyway, because every vertex has a neighbour (an isolated vertex would have no
path to the other N − 1 vertices) and (A2 )ii = deg(ni ) (Corollary 3.9(d)); the test does not need
this. For N = 1 there are no pairs of different vertices and the graph is connected; the sum S
is empty, so the test is stated for N ≥ 2. [derived here]

4.3   The test as a procedure
      In plain words. Here is the check, in order. First write the table of the village.
      Then multiply the table by itself again and again. After each multiplication, add the
      new counts to a running total. Stop at the power that is one less than the number of
      houses. Look at every pair of different houses. If any total is zero, those two houses
      cannot reach each other. If no total is zero, everyone can reach everyone.

Test 4.12 (Matrix test for connectedness). Input: the adjacency matrix A of a graph with
N ≥ 2 vertices.

  1. Set P = A and S = A.

  2. For k = 2, 3, . . . , N − 1: replace P by P A (now P = Ak ) and add P to S.

  3. Look at the entries Sij with i ̸= j. If one of them is 0, report “not connected”. If none is
     0, report “connected”.

Remark 4.13. Correctness is Theorem 4.6. The procedure makes N − 2 matrix products, the
last one producing AN −1 . A zero at position (i, j) means by Corollary 4.10 that ni and nj are
in different components, so the procedure also lists the pieces. The test forbids stopping early:
it needs every power up to N − 1 (Proposition 4.17).

                                                21
Example 4.14. On B (N = 3) step 2 runs once (k = 2): P = A2 , S = A + A2 , no off-diagonal
zero, so “connected”. The matrices are in Section 6.

Non-example 4.15. Reporting after k = 1 only (the table A itself) is not the test: on B it
would report “not connected” because A13 = 0.

4.4   An equivalent form with one table
      In plain words. There is a second form of the check that uses one table only. Let
      a trip wait at a house for a step. Then count trips of one fixed length. Waiting lets
      short trips count too. The village is connected exactly when no pair of houses has a
      count of zero.

    The matrix that makes a walk wait is the identity matrix I, which has ones on the diagonal
and zeros elsewhere: “stay at the same vertex” is one allowed move, just as “follow one edge” is
the move given by A. Let m be a positive integer. When (I + A) is multiplied by itself m times,
each of the m factors offers a choice between waiting (I) and following one edge (A). A choice
with k edges followedand m − k waits gives the product Ak (because IX = X for every matrix
X), and there are m k such choices. So
                                                              
                           m     m        m         m 2              m m
                   (I + A) =         I+       A+        A + ··· +       A ,                 (3)
                                  0        1         2               m

where A0 = I stands for “no edge followed”. Because IA = AI = A, the matrices I and
A commute, which is what lets the expansion follow the ordinary binomial theorem. Every
coefficient is a positive integer.
    Why this decides
                  Pm connectedness.  For i ̸= j the identity matrix has the entry 0 at (i, j), so
          m                m
                              k
 (I + A) ij = k=1 k (A )ij , a sum of non-negative terms with positive coefficients. It is
positive exactly when some (Ak )ij with 1 ≤ k ≤ m is positive, that is, when a walk of length
at most m joins ni and nj . For m ≥ N − 1 this is the same as Sij > 0, by Lemma 2.52
and Corollary 2.54. On the diagonal the term I contributes 1, so no diagonal entry is zero.
Appendix A.4 gives the argument in detail.

      In plain words. So one table is enough. Take the table that allows waiting and
      raise it to a high enough power. A zero anywhere means that two houses cannot
      reach each other. Otherwise every house can reach every other house.

Proposition 4.16 (The form with I + A). Let G have N ≥ 2 vertices, let I be         the N × N
                                                                                 m
identity matrix, and let m ≥ N − 1 be an integer. Then (a) for i ̸= j, (I + A) ij > 0 if and
only if Sij > 0; (b) every diagonal entry of (I + A)m is at least 1. Hence G is connected if and
only if (I + A)N −1 has no zero entry. [derived here; proof in Appendix A.4]

    Bai states the case m = N − 1 as his Theorem 2, with a proof sketch that is incomplete
(Section 7.2) [1]. That statement is therefore [qualified] ; the proof in the appendix replaces the
sketch. For the board graph and for D the matrices (I + A)2 are in Section 6, and the zeros fall
in the same places as the zeros of S.

4.5   Why N − 1 and not less
      In plain words. Take four houses in a row. To go from the first house to the last
      you must pass every house in between. That takes three roads. If we counted only
      trips of up to two roads, we would miss this pair. We would say the village is cut in
      two, and we would be wrong. The same idea works for any row of houses.


                                                22
Proposition 4.17 (N − 1 cannot be lowered to N − 2). For every N ≥ 3 there is a connected
graph with N vertices for which the sum A + · · · + AN −2 has a zero entry off the diagonal.
[derived here]

Proof. Take the graph with edges 1–2, 2–3, . . . , (N − 1)–N , the row graph on N vertices; it is
connected. Each step of a walk changes the vertex number by exactly 1. To go from vertex 1
to vertex N the number must increase by N − 1, so at least N − 1 steps are needed. A walk of
length k < N − 1 from 1 to N does not exist, so by Theorem 3.5 (Ak )1N = 0 for 1 ≤ k ≤ N − 2.
Hence the (1, N ) entry of A + · · · + AN −2 is 0, although the graph is connected.

   For N = 3 the graph is the board graph and the sum A+· · ·+AN −2 is A itself, with A13 = 0.
For N = 4 (Figure 5) every matrix is written out below; the sum of the first N − 2 = 2 powers
has zeros at (1, 4) and (4, 1), and the sum of the first N − 1 = 3 powers has none.

                               1              2            3              4
                               u               u            u                u



                Figure 5: The row graph on four vertices, used in Example 4.18.

Example 4.18 (The bound N − 1 is needed; the row graph on four vertices). With N = 4, the
matrices from the script are
                                                                                           
                              0      1    0   0                             1       0   1   0
                             1      0    1   0                            0       2   0   1
                                                                      A2 = 
                                                                           
                         A= 0
                                                ,                                            ,
                                     1    0   1                           1       0   2   0
                              0      0    1   0                             0       1   0   1
                                                                                           
                              0      2    0   1                             1       1   1   0
                              2      0    3   0                            1       2   1   1
                        A3 =                                     A + A2 = 
                                                                          
                                                ,                                            ,
                             0      3    0   2                           1       1   2   1
                              1      0    2   0                             0       1   1   1
                                               
                              1      3    1   1
                              3      2    4   1
               A + A2 + A3 = 
                             
                                                .
                             1      4    2   3
                              1      1    3   1

With N − 2 = 2 powers the (1, 4) entry is 0, so the test would wrongly say “not connected”.
With N − 1 = 3 powers every entry is positive.


Table 6: The row graph on N vertices, N = 3, . . . , 8 (by script). The first power with a non-zero
(1, N ) entry is always N − 1.
          N    smallest    k       with   (1, N ) entry of A + · · · +   (1, N ) entry of A + · · · +
               (Ak )1N > 0                AN −2                          AN −1
           3   2                          0                              1
           4   3                          0                              1
           5   4                          0                              1
           6   5                          0                              1
           7   6                          0                              1
           8   7                          0                              1

    Using only the single power AN −1 is also wrong: on the board graph A2 has the zero entry
(1, 2).


                                                     23
Remark 4.19 (Which graphs the N − 2 version gets wrong). The test with only N − 2 powers is
wrong on exactly the labelled row graphs, that is, the row graph on N vertices with the vertices
numbered in any order. There are N !/2 of them for N ≥ 2 (N ! orders along the row, each row
counted twice because it can be read from either end): 1, 3, 12, 60, 360 for N = 2, . . . , 6. These
are the numbers in the last column of Table 10, which the script counted by brute force. [derived
here] Reason: the N − 2 version can only err by saying “not connected” for a connected graph,
because a positive entry always comes from a real walk. In a connected graph every distance is
at most N − 1 (Corollary 2.54), and by Corollary 4.10(b) the N − 2 version misses a pair exactly
when its distance is N − 1. A shortest path between such a pair has N vertices, so it passes
through every vertex of the graph. It has no chord, that is, no edge between two of its vertices
that are not neighbours on it, because such an edge would give a shorter path between the same
two vertices. So every edge of the graph lies on that path, and the graph is the row graph.
Conversely, Proposition 4.17 shows that a row graph fails. For N = 2 the sum of N − 2 = 0
powers is empty, and an empty sum is the zero matrix, so the test says “not connected” on the
one connected graph.

4.6    Breadth-first search, the alternative
       In plain words. There is another way, and it needs no table of counts. Stand at
       one house and mark it. Then mark every house next to it. Then mark every house
       next to those. Keep going until no new house appears. If every house is marked, the
       village is connected.

    Breadth-first search (BFS) from a start vertex s is this procedure.
    1. Mark s and put it on a waiting list, called a queue: vertices leave it in the order in which
       they entered.

    2. Take the first vertex off the list. Mark every neighbour of it that is not yet marked (these
       vertices are now discovered ) and put them at the end of the list.

    3. Repeat step 2 until the list is empty.

    4. Report “connected” if every vertex is marked, and “not connected” otherwise.
The correctness statement in the source is that for every vertex v there is a walk from s to v if
and only if v is discovered when the search ends, so G is connected if and only if every vertex
is discovered when BFS starts from any single vertex s [10]. (If every vertex is discovered, two
vertices u, v are joined by the reversal of a walk from s to u followed by a walk from s to v, as in
the justification of symmetry and transitivity in Definition 2.60; if some vertex is not discovered,
no walk from s reaches it, and G is not connected.) When the graph is stored as adjacency lists
(for each vertex, the list of its neighbours), the source gives a running time at most a fixed
multiple of N + |E| [10]. BFS and the matrix test agree on all labelled graphs with 2, 3, 4, 5, 6
vertices (2, 8, 64, 1024, 32768 graphs; a check, not a proof, Appendix A.6), and BFS also lists
the components directly. The two methods are compared for cost in Section 7.


5     Answer 3: the definition of a path between ni and nj
Question 3 asks for the definition of a path between two vertices ni and nj . The answer is
Definition 2.35, restated for a pair of vertices in Definition 5.1 below: in the course, a path is
a walk with no repeated vertex, which is the textbook’s Definition 1.2.13 [9, Definition 1.2.13,
p. 22]. This section adds only the form for a pair of vertices and the comparison of the three
naming conventions. The board uses the word in its definition of “connected” and does not say
which meaning it has [4, 5]. The assignment text is not reproduced in this paper. As reported

                                                24
by the user, it states that in the course “path” means a walk with no repeated vertices; the
answer to Question 3 rests on this statement, so it is [interpretation, qualified] : it is the user’s
report, and the board does not confirm it.

      In plain words. A path between two houses is a route from one to the other. It
      never passes a house twice, so it has no detour. If the two houses are the same, the
      route has no roads at all. It is just the one house.

Definition 5.1 (Path between ni and nj , course convention). Let ni and nj be vertices of G. A
path between ni and nj is a path in the sense of Definition 2.35 whose first vertex is ni and whose
last vertex is nj : a walk w0 , w1 , . . . , wk with w0 = ni , wk = nj and pairwise distinct vertices.
Its length is k.

   This definition is taken from the assignment text, as reported by the user, together with the
textbook’s Definition 1.2.13; it is not derived.
   This is a simple path in the textbook’s sense and a path in English usage [9, 3]; Grinberg
phrases the pair form as “a path from p to q is a path that starts at p and ends at q” [3,
Definition 2.9.1(d), p. 36].
Remark 5.2. The definition forbids repeated vertices, and so repeated edges (Proposition 2.39).
For i = j the only such path is the single vertex ni , of length 0 (this uses the reading of length-0
walks in Section 1.3, item 7). For i ̸= j the length is at least 1 and, by Corollary 2.54, at most
N −1. In the board’s sentence “there exists a path between nodes”, the words mean that at least
one such object exists. By Proposition 2.59 that statement has the same truth value whether
“path” means walk, trail or path in the sense above. What changes with the convention is how
many such objects there are (Remark 5.5).

Example 5.3. Example 2.37 gives the path 1, 2, 3 between n1 and n3 in B. It is the only one:
every path has at most N − 1 = 2 edges (Corollary 2.54), and the enumeration of walks up to
length 4 finds no other (by script). Between n1 and n1 the only path is the single vertex 1.

Non-example 5.4. The walk 1, 2, 1, 2, 3 of Example 2.25 joins n1 and n3 but is not a path
between them (Non-example 2.38, Non-example 2.34). In the graph D there is no path between
n1 and n3 at all.

5.1   The three conventions in one table
      In plain words. The same two rules get different names in different books. One
      rule says never drive a road twice. The other says never pass a house twice. Our
      textbook, English books and our course do not always use the same word for the
      same rule. So here is one table that puts the words side by side.

    The textbook’s rows are its Definitions 1.2.10 to 1.2.15 [9]. The English words for walk, trail,
path and cycle are Grinberg’s Definitions 2.9.1(c), 3.4.5 and 2.10.1(b) [3]; “closed trail” is this
paper’s own name for the English counterpart of the textbook’s cycle, since the sources checked
give no single standard word for it. Wikipedia says that a path has distinct vertices “by most
definitions” [8], and also records that some authors use “path” for walks with repeated vertices
and “simple path” for those with distinct vertices [8]. That is the textbook’s pattern, so the
course convention is one of at least two in use.

      In plain words. The word changes how many routes we count. It does not change
      whether a route exists. In the board village there is one route from the first house to
      the last. But there are three trips of at most four roads, and two of them turn back.



                                                 25
Table 7: The three naming conventions. “Course (stated)” is what the assignment text states,
as reported by the user: only the word path. For every other row the course convention is not
stated, so this paper follows the textbook and writes “simple cycle” for the English “cycle”.
Sources: textbook [9], Grinberg [3], Wikipedia [8].
    Property of the walk         Textbook        word   English word   Course          This paper
                                 (number)                              (stated)
    any list of steps along      walk (1.2.10)          walk           not stated      walk
    edges
    walk with first vertex       closed       walk      closed walk    not stated      closed walk
    equal to last                (1.2.11)
    no repeated edge; ver-       “path” (1.2.12)        trail          not stated      trail
    tices may repeat
    no repeated vertex (so       “simple     path”      path           path            path
    no repeated edge)            (1.2.13)
    closed, no repeated          “cycle” or “closed     closed trail   not stated      cycle (textbook
    edge;    vertices may        path” (1.2.14)                                        meaning)
    repeat
    closed, no repeated ver-     “simple     cycle”     cycle          not stated      simple cycle
    tex except first and last,   (1.2.15)
    length at least 3


Remark 5.5 (The number of objects depends on the convention). Under the course convention,
the number of paths from n1 to n3 in B is 1. The walks of length at most 4 from n1 to n3
are 1, 2, 3 (length 2), 1, 2, 1, 2, 3 and 1, 2, 3, 2, 3 (length 4); only the first is a path or a trail (by
script). So the number of walks, the number of trails and the number of paths are different
numbers in general, and the entries of Ak give only the first (Proposition 3.10). The existence
statement used by Definition 2.55 is the same under every convention (Proposition 2.59).


6      Worked example: the board graph and a graph with one edge
This section writes out every matrix for two graphs and applies Theorem 3.5 and Theorem 4.6
to them. The two graphs are the board graph B (the matrix on the board, Figure 1, left) and
the graph D with one edge (Figure 4). Every matrix and count below was computed by script,
and the script outputs were checked against independent code before the numbers were written
(Appendix A.7).

6.1      Powers of the board matrix
        In plain words. We take the village from the board. It has three houses in a row.
        The first and last houses each have one road. The middle house has two roads. We
        count trips of two roads, then of three roads. We list every trip, so the reader can
        see that each count is right.

Example 6.1 (The board matrix and its powers). The graph B has vertices n1 , n2 , n3 and edges
n1 n2 and n2 n3 . Its adjacency matrix and powers, copied from the script output, are
                                                                              
                    0 1 0                       1 0 1                      0 2 0
           A = 1 0 1  ,               A 2 = 0 2 0  ,           A 3 = 2 0 2  ,
                    0 1 0                       1 0 1                      0 2 0
                                                   
                    2 0 2                       0 4 0
           4                              5
          A = 0 4 0 ,
                                      A = 4 0 4 .
                                              
                    2 0 2                       0 4 0


                                                         26
The matrix A is symmetric with zero diagonal, as Proposition 2.13 requires; its row sums 1, 2, 1
are the degrees, and the sum of all its entries is 4 = 2|E|. Further, A3 = 2A and Ak+2 = 2Ak
for k = 1, . . . , 5 (by script), and the diagonal of A2 is (1, 2, 1), the degrees, with sum 4 = 2|E|
(Corollary 3.9(d)). Each power is symmetric (Corollary 3.9(c)).

   The board matrix is the matrix of a graph with two edges. The board drawing also shows
an edge 1–3 and an arrowhead; they are not in the matrix (Table 3), and this section follows
the matrix.

Every walk listed. For every entry of A, A2 and A3 the script lists the walks and checks that
their number equals the entry (labels 1, 2, 3 stand for n1 , n2 , n3 ).

    Length 1: 1-2 and 2-3, and their reverses.

    Length 2: from 1 to 1: 1-2-1 (one walk). From 1 to 3: 1-2-3 (one). From 2 to 2: 2-1-2 and
     2-3-2 (two). From 3 to 3: 3-2-3 (one). All other entries of A2 are 0.

    Length 3: from 1 to 2: 1-2-1-2 and 1-2-3-2 (two). From 2 to 3: 2-1-2-3 and 2-3-2-3 (two).
     The entries (2, 1) and (3, 2) follow by reversing the walks.

The induction step of Theorem 3.5 can be checked on three entries, by the sum over the second-
last vertex nr (script output):
                                   X
                         (A2 )22 =   A2r Ar2 = 1 · 1 + 0 · 0 + 1 · 1 = 2,
                                      r
                                     X
                           2
                         (A )11 =         A1r Ar1 = 0 · 0 + 1 · 1 + 0 · 0 = 1,
                                      r
                                     X
                         (A3 )12 =    (A2 )1r Ar2 = 1 · 1 + 0 · 0 + 1 · 1 = 2.
                                      r

In the last line the term r = 1 is the walk 1-2-1 of length 2 extended by the step to n2 , giving
1-2-1-2, and the term r = 3 is the walk 1-2-3 extended by the step to n2 , giving 1-2-3-2. The
walk 1-2-1, counted by (A2 )11 , is neither a path nor a trail: this is the counterexample of
Proposition 3.10.

Walks, trails and paths by length. Table 8 counts all walks, trails, paths and closed walks
of each length in B, over all pairs of start and end vertices, by enumeration. The totals in
the walk column equal the sums of all entries of Ak : 4, 6, 8, 12 for k = 1, 2, 3, 4 (script). From
k = 3 on there is no trail (it would need three distinct edges, and B has two) and no path (it
would need four distinct vertices, and B has three). The walk numbers keep growing; this is the
warning of Proposition 3.10 in numbers.

Table 8: All walks, trails, paths and closed walks of length k in the board graph B, counted
over all start and end vertices (by script). Length 0 counts the three single vertices.
                               k   walks     trails   paths    closed walks
                               0      3        3           3        3
                               1      4        4           4        0
                               2      6        2           2        4
                               3      8        0           0        0
                               4     12        0           0        8




                                                      27
6.2   The test on the board graph (connected)
      In plain words. Take three houses in a row. A road joins the first and the second
      house. Another road joins the second and the third. The first and the third share
      no road. Can you still go from one to the other? Yes, through the middle house. We
      expect the check to say connected.
Example 6.2 (Matrix test on B, N = 3, N − 1 = 2). Every product was computed by script.
With N − 1 = 2 the sum is S = A + A2 , and the second form is (I + A)2 :
                                                                      
                      0 1 0                                     1 0 1
                A = 1 0 1 ,                            A2 = 0 2 0 ,
                      0 1 0                                     1 0 1
                                                                      
                      1 1 1                                     2 2 1
                S = 1 2 1 ,                      (I + A)2 = 2 3 2 .
                      1 1 1                                     1 2 2
S has no zero entry off the diagonal (in fact none anywhere), so by Theorem 4.6 the graph is
connected. (I + A)2 has no zero entry, so by Proposition 4.16 the graph is connected. The two
answers agree, and breadth-first search from vertex 1 reaches {1, 2, 3} and agrees too. The entry
A13 is 0, so no edge joins n1 and n3 , yet (A2 )13 = 0 · 0 + 1 · 1 + 0 · 0 = 1: exactly
                                                                                    2 one walk of
                                                             2                    2
length 2 joins them, namely 1, 2, 3. The entry of (I + A) at (1, 3) is 1 = 2 (A )13 , since in
formula (3) both I and A have the entry 0 at (1, 3). As a check, (I + A)2 = I + 2A + A2 holds
entry by entry (script). [derived here]
   By Corollary 4.10(b), the smallest k with (Ak )ij > 0 is the distance: d(1, 2) = d(2, 3) = 1
from A, and d(1, 3) = 2 from A2 , in agreement with Example 2.50.

6.3   The test on the graph with one edge (disconnected)
      In plain words. Now take three houses again. Only one road exists, between the
      first and second house. The third house stands alone. Nobody can walk to it. We
      expect the check to say not connected. The check should also show that the third
      house is a piece by itself.
Example 6.3 (Matrix test on D, N = 3, N − 1 = 2). The graph D has the single edge n1 n2 .
From the script,
                                                               
                      0 1 0                                1 0 0
                 A = 1 0 0 ,                       A2 = 0 1 0 ,
                      0 0 0                                0 0 0
                                                               
                      1 1 0                                2 2 0
                 S = 1 1 0 ,                 (I + A)2 = 2 2 0 .
                      0 0 0                                0 0 1
The off-diagonal zeros of S are at (1, 3), (2, 3), (3, 1) and (3, 2), and the zeros of (I + A)2 are at
the same four places. So by Theorem 4.6 and Proposition 4.16 the graph is not connected. By
Corollary 4.10(a), vertices 1 and 2 lie in one component and vertex 3 in another: the components
are {1, 2} and {3}, which agrees with breadth-first search. Higher powers do not help: the entries
(1, 3) and (2, 3) of Ak are 0 for k = 1, . . . , 6 (script); for instance
                                                          
                                                   0 1 0
                                       A3 = 1 0 0 = A.
                                                   0 0 0
In fact no walk from vertex 1 or vertex 2 reaches vertex 3. [derived here]


                                                 28
Table 9: Outcome of the tests on the two graphs. Both forms of the matrix test and breadth-first
search give the same answer.
    Graph              Matrix test (Theorem 4.6)     Form with I + A (Proposition 4.16)    Components
    B, edges 12, 23              connected                         connected                 {1, 2, 3}
    D, edge 12                 not connected                     not connected              {1, 2}, {3}


The test on all small graphs. As a check of the statements, not as a proof, the script
compared the sum test, the form with I + A and the component statement of Corollary 4.10(a)
with breadth-first search on every labelled simple graph with N = 2, . . . , 6 vertices (Table 10).
All agree.

Table 10: Exhaustive check over all labelled simple graphs with N vertices (by script). “Sum test
agrees” counts the graphs on which the test of Theorem 4.6 gave the same answer as breadth-
first search. The last column counts the graphs on which the same test with only N − 2 powers
gives a wrong answer (Proposition 4.17).
              N       graphs    connected      sum test agrees   wrong with N − 2 powers
               2           2             1                  2                               1
               3           8             4                  8                               3
               4          64            38                 64                              12
               5       1,024           728              1,024                              60
               6      32,768        26,704             32,768                             360



7     Discussion: limitations and failure cases
7.1     What the sources and photographs leave open
     The mark above A. The photographs do not show clearly whether the mark above A
      in Question 1 is a k, an n, or quotation marks (Section 1.3, item 2). The paper reads it
      as k because the assignment text does. The answer does not change with the letter, since
      Theorem 3.5 holds for every positive integer exponent [interpretation, qualified]. What
      stays open is only what the lecturer wrote.

     The drawing and the matrix. The paper follows the matrix and reports the extra edge
      1–3 and the arrowhead (Table 3). If the lecturer meant the triangle T , the example would
      change but no theorem would: the statements hold for every simple undirected graph. The
      paper does not claim which graph was meant.

     The meaning of “path”. That the course means the textbook’s simple path is stated
      by the assignment text and is not on the board. If the course meant the textbook’s
      Definition 1.2.12, then “path” is a trail, and the answer to Question 3 changes in words.
      The answer to Question 2 does not change, by Proposition 2.59. Counts of paths would
      change; counts of walks would not. [qualified]

     What the lecturer expected for Question 2. The board shows only the question, not
      the answer. The paper gives the sum test, the form with I + A, and breadth-first search,
      and does not say which one the lecturer intended.

     The textbook beyond the pages checked. The statement that the textbook contains
      neither the counting theorem nor a matrix test is [qualified] : it rests on the pages checked


                                                      29
      and on a full-text search (Section 1.6), not on a page-by-page reading of the whole book.
      It does not affect the proofs, which do not depend on it.

7.2   Limits of the results
    Simple graphs. Both proofs are for finite simple undirected graphs. Directed graphs
     and graphs with loops or repeated edges are outside the paper, and the connectivity test
     should not be applied to them.

    Only as good as two results. The test rests on Theorem 3.5 and Lemma 2.52. The first
     is stated by several sources and proved here. The second is the textbook’s Lemma 1.2.1
     for u ̸= v, which has no length bound; the bound comes from Grinberg’s Corollary 2.9.7,
     and the paper proves the lemma with the bound itself (Section 2.3).

    The test answers yes or no. The sum S does not list a path between two vertices.
     Corollary 4.10 gives the components and the distances, and nothing more.

    Finite checks are not proofs. The brute-force comparisons (Appendix A.6) cover N ≤ 5
     for walk counting and N ≤ 6 for the test. They support the proofs and do not replace
     them.

Where other sources are weaker. Two sources that state the connectivity test prove it
incompletely, and one states the counting theorem with “paths” in place of walks; that is why
the paper proves both itself. Paramadevan and Sotheeswaran’s Theorem 1 reads: “the number
of different paths of length l between the i-th and j-th vertices of G is equal to the (i, j)-th entry
of AlG ”. This is false for paths in either sense (Proposition 3.10), although their own property 7
says walks. Their proof of Theorem 2 repeats the word: “bij = number of different paths of
length less than n from the vertex i to j”, and it ends “Conversely, if bij ̸= 0, then there exist at
least one path from vi to vj , thus G is connected”, which passes from a non-zero entry to a path
without the walk-to-path lemma [7]. Bai’s proof sketch of the (I + A)n−1 form says “(I + A)n−1
aggregates all paths of length ≤ n − 1” [1]. Both statements of the test are correct and the
proofs are incomplete [interpretation].

7.3   Failure cases of the test
Each of the following gives a wrong answer on a small graph.

    Stopping at AN −2 . On the row of four houses the (1, 4) entry is 0 (Example 4.18). The
     graphs on which this fails are exactly the labelled rows of houses (Remark 4.19).

    Using the single power AN −1 , or A2 alone for N = 3 (Non-example 4.4).

    Requiring positive diagonal entries of S. For N = 2 and one edge the diagonal is zero
     although the graph is connected (Remark 4.11).

    Using subtraction, or arithmetic modulo a number, in place of ordinary integer arith-
     metic. The step “a sum is positive exactly when a term is” needs non-negative integers
     (Theorem 4.6, why the argument is valid ).

    Reading (Ak )ij as the number of paths (Proposition 3.10).




                                                 30
7.4    Cost, in brief
[estimate] Reaching AN −1 from A takes N − 2 matrix products, and the school method of
multiplication uses about N 3 scalar multiplications for each product of two N × N matrices;
faster methods were not examined. That is about N 4 multiplications in all, against about
N + |E| operations for breadth-first search with the graph stored as adjacency lists [10], a single
pass over the graph. The matrix test is therefore useful for its clean statement about the powers
of A, not for speed [interpretation].


8      Conclusion: the three answers
Question 1: what does (Ak )ij represent? For the adjacency matrix A of a finite simple
undirected graph and an integer k ≥ 1, the entry (Ak )ij is the number of walks of length k from
ni to nj (Theorem 3.5). The proof is by induction on k, splitting the walks by their second-
last vertex. The number counts walks, not paths: a walk may repeat vertices and edges, so
(A2 )ii = deg(ni ) > 0 although no path of length 2 returns to ni (Proposition 3.10). On the
board graph, (A3 )12 = 2 while the only path from n1 to n2 has length 1. The reading of the
mark above A as k is an interpretation (Section 1.3); the theorem holds for any positive integer
exponent.

Question 2: how can one tell from A whether the graph is connected? For N ≥ 2,
the graph is connected if and only if every entry off the diagonal of S = A + A2 + · · · + AN −1
is positive (Theorem 4.6). Equivalently, (I + A)N −1 has no zero entry (Proposition 4.16). The
proof uses walk counting, the lemma that every walk contains a path, and the bound that a path
has at most N − 1 edges. The exponent N − 1 cannot be lowered to N − 2 (Proposition 4.17).
On the board graph the test says connected, and on the graph with the single edge 12 it says
not connected, with the components {1, 2} and {3} (Section 6). Breadth-first search gives the
same answers (Section 4.6).

Question 3: what is a path between ni and nj ? In the course convention, a path be-
tween ni and nj is a walk w0 , . . . , wk with w0 = ni , wk = nj and pairwise distinct vertices
(Definition 5.1). It is the textbook’s simple path, Definition 1.2.13, and the English path. The
textbook’s own word “path”, Definition 1.2.12, means a walk with no repeated edge; this paper
calls it a trail (Table 7). That the course uses this meaning comes from the assignment text
and is [qualified]. Whether a path exists between two vertices does not depend on the choice
(Proposition 2.59).

What the paper did not settle. The board’s mark above A, the extra edge and arrowhead in
the board drawing, and the lecturer’s intended answer to Question 2 remain open (Section 7.1).
The statement that the textbook contains no walk-counting theorem and no matrix test is
[qualified] : it rests on the pages checked and a full-text search (Section 1.6).


References
 [1]   Shuliang Bai. Important Properties and Applications of the Adjacency Matrix (20250310).
       Date 2025-03-10 as printed in the title. BIMSA lecture notes. 2025. url: https://bimsa
       .net/doc/notes/48535.pdf?id=0.3935315718408674 (visited on Oct. 27, 2026).




                                                31
 [2] Chapter 1 Matrices and Graphs, 1.1 The Adjacency Matrix (linear algebra course notes,
     University of Galway). Author and date do not appear in the file; the URL path suggests R.
     Quinlan, which the file does not confirm. School of Mathematical and Statistical Sciences,
     University of Galway. n.d. url: https://maths.nuigalway.ie/~rquinlan/linearalge
     bra/section1-1.pdf (visited on Oct. 27, 2026).
 [3]   Darij Grinberg. An introduction to graph theory (text for Math 530 in Spring 2022 at
       Drexel University). Lecture-note text, 454 pages; page locators are the document’s own
       page numbers. arXiv:2308.04512v3 [math.HO], Spring 2025 edition, 7 June 2025. 2025.
       url: https://arxiv.org/abs/2308.04512 (visited on Oct. 27, 2026).
 [4] Lecture whiteboard photo 1. Local file sources/whiteboard-1.jpg. Photograph of the
     lecture board, supplied by the user. n.d.
 [5] Lecture whiteboard photo 2. Local file sources/whiteboard-2.jpg. Second photograph of
     the same board at a slightly different angle, supplied by the user. n.d.
 [6]   Eric Lehman, F. Thomson Leighton, and Albert R. Meyer. 9.3: Adjacency Matrices, in
       Mathematics for Computer Science. Page last modified 2021-07-02; the year of the under-
       lying book is not on the page. Engineering LibreTexts, MIT OpenCourseWare material.
       n.d. url: https://eng.libretexts.org/Bookshelves/Computer_Science/Programmin
       g_and_Computation_Fundamentals/Mathematics_for_Computer_Science_(Lehman_Le
       ighton_and_Meyer)/02%3A_Structures/09%3A_Directed_graphs_and_Partial_Order
       s/9.03%3A_Adjacency_Matrices (visited on Oct. 27, 2026).
 [7]   P. Paramadevan and S. Sotheeswaran. “Properties of Adjacency Matrix of a Graph and
       It’s Construction”. In: JSc EUSL (Journal of Science, Eastern University, Sri Lanka) 12.1
       (2021), pp. 13–21. doi: 10.4038/jsc.v12i1.29. url: https://www.fsc.esn.ac.lk/jsc
       /archive/12.1.2.pdf (visited on Oct. 27, 2026).
 [8] Path (graph theory). Revision of 5 June 2026 (oldid 1357845833) as fetched; open to later
     edits. Wikipedia, English edition. n.d. url: https://en.wikipedia.org/wiki/Path_(g
     raph_theory) (visited on Oct. 27, 2026).
 [9]   P. A. Petrosyan, V. V. Mkrtchyan, and R. R. Kamalyan. Grafneri tesutyun (Graph Theory:
       a study guide), course textbook in Armenian. Local file Grafneri tesutyun.pdf at the
       repository root. Supplied by the user. Page numbers in this paper are the printed page
       numbers; the PDF page is the printed page plus one. Yerevan, 2015.
[10] Éric Schost. CS 341: Algorithms, Lecture 10: Graphs, breadth first search. David R. Cheri-
     ton School of Computer Science, University of Waterloo, Winter 2026, lecture slides. 2026.
     url: https : / / www . student . cs . uwaterloo . ca / ~cs341 / lectures / lecture10 . pdf
     (visited on Oct. 27, 2026).
[11]   Eric W. Weisstein. Connected Graph. Wolfram MathWorld. n.d. url: https://mathworl
       d.wolfram.com/ConnectedGraph.html (visited on Oct. 27, 2026).


A      Derivations, cross-checks and scripts
This appendix holds the longer derivations and the scripts that produced every number. The
body of the paper gives the proofs of Theorems 3.5 and 4.6 and Lemma 2.52. The appendix
adds the parts that the body only states: the reduction of walks to vertex lists, the general
counterexample behind Proposition 3.10, the proof of Proposition 4.16, the distance results
used in Remark 2.49 and Corollary 4.10, the chain of premises behind Theorem 4.6, and the
finite checks.




                                               32
A.1    Walks as vertex lists, and the induction step
In the textbook’s sense a walk lists vertices and edges alternately, each edge joining the two
vertices beside it (Definition 2.23). Take a list (w0 , . . . , wk ) of vertices in which each consecutive
pair is adjacent. For each t there is an edge wt−1 wt , and it is the only edge with these two
ends, because E is a set of unordered pairs (Definition 2.1). So the list determines the walk, by
et = wt−1 wt . Conversely, a walk determines its list of vertices. The two assignments are inverse
to each other, so the walks of length k from ni to nj are in one to one correspondence with the
lists (w0 , . . . , wk ) with w0 = ni , wk = nj and consecutive vertices adjacent. This is the reduction
used in the proof of Theorem 3.5. [derived here]
     The approach of the proof, induction on k with the sum over the second-last vertex, is the
one in the University of Galway notes and in Grinberg’s proof of his Theorem 4.5.10 [2, 3].
Grinberg also treats k = 0, with A0 = I and one walk of length 0 from a vertex to itself [3]; the
board question needs only k ≥ 1.
     The induction step, in words and in symbols, is the identity
                                                  N
                                                  X
                                    Wk (i, j) =         Wk−1 (i, r) Arj ,                             (4)
                                                  r=1

where Wk (i, j) is the number of walks of length k from ni to nj . The term for r counts the walks
of length k − 1 from ni to nr that can be extended by the step to nj ; the factor Arj is 1 when
that step exists and 0 otherwise. The three hand checks on the board graph are written out in
Section 6.1.

A.2    The walk-versus-path counterexample in general
Proposition 3.10(a) says: if ni has a neighbour nr , then the walk ni , nr , ni is counted by (A2 )ii ,
and it is neither a path nor a trail. The argument has three parts, each used in the proof in
the body. First, the walk repeats ni , so its vertices are not pairwise distinct. Second, it uses
the edge ni nr twice, so its edges are not pairwise distinct. Third, a path from a vertex to itself
has pairwise distinct vertices, so it has length 0, not 2. Under each of the three conventions of
Table 7 there is therefore no path or trail of length 2 from ni to ni , while (A2 )ii = deg(ni ) ≥ 1.
   On the board graph B the script also counts the closed walks from n1 to n1 . For k = 1, 2, 3, 4
there are 0, 1, 0, 2 of them, and none of these is a path or a trail. The 2 for k = 4 are 1-2-1-2-1
and 1-2-3-2-1, in agreement with (A4 )11 = 2 in Example 6.1. The walks from n1 to n2 are in
Table 5. The identity Ak+2 = 2Ak follows from A3 = 2A (checked by script for k = 1, . . . , 5) by
multiplying with Ak−1 .

A.3    The chain of premises behind the connectivity test
The proof of Theorem 4.6 is written in the body. Table 11 lists each step with the result it uses,
so that the proof can be audited without reading it twice.

A.4    The form with I + A and the exponent m
We prove Proposition 4.16. Let m ≥ N − 1 ≥ 1.
    Expansion. Write (I + A)m = (I + A)(I + A) · · · (I + A) with m factors. Expanding the
product gives one term for each choice of I or A from each factor, with the chosen matrices
multiplied in order. Because IX = XI = X for every matrix X, a term with k letters A and
m − k letters I equals Ak , wherever the letters stand. The number of choices with exactly k
                                      m
letters A is the binomial coefficient k . Therefore formula (3) holds:
                                                              
                           m       m       m         m 2             m m
                    (I + A) =         I+       A+       A + ··· +      A ,
                                   0       1         2               m

                                                    33
                         Table 11: The proof of Theorem 4.6, step by step.
      Step   Statement                                             Relies on
        1    G is connected iff every pair of vertices is joined   Definition 2.55, Proposition 2.59
             by a path
        2    A path between different vertices has length be-      Corollary 2.54
             tween 1 and N − 1
        3    A walk of length k from ni to nj exists iff           Theorem 3.5, Corollary 3.9(b)
             (Ak )ij > 0
        4    A sum of non-negative integers is positive iff a      Corollary 3.9(a)
             term is positive
        5    A walk from ni to nj contains a path from ni to       Lemma 2.52
             nj


with A0 = I. (This is the binomial theorem for the commuting matrices I and A.) For m = 2
it reads (I + A)2 = I + 2A + A2 , which the script confirmed entry by entry on the board graph
and on D.
    Off-diagonal entries. Let i ̸= j. The identity matrix has 0 at (i, j), so by (3)
                                                  m  
                                                  X  m
                                    (I + A)m ij =       (Ak )ij .
                                            
                                                     k
                                                     k=1

                   m
Every coefficient k with 1 ≤ k ≤ m is a positive integer, and every (Ak )ij is a non-negative
                    

integer (Corollary 3.9(a)). So the sum is positive if and only if at least one (Ak )ij with 1 ≤ k ≤ m
is positive, that is, if and only if there is a walk of length k from ni to nj for some k with
1 ≤ k ≤ m (Corollary 3.9(b)).
    If Sij > 0, such a k ≤ N − 1 ≤ m exists by Proposition 4.5. Conversely, if a walk from
ni to nj exists, Lemma 2.52 gives a path from ni to nj , of length k ′ with 1 ≤ k ′ ≤ N − 1 by
                                                          ′
Corollary 2.54; this path is a walk of length k ′ , so (Ak )ij > 0 and Sij > 0. So the off-diagonal
entry is positive exactly when Sij >  0, which is item (a).
    Diagonal entries. The term m   0 I contributes 1 to every diagonal entry and the other terms
are non-negative, so every diagonal entry is at least 1, whatever the graph is. This is item (b).
    Conclusion. By Theorem 4.6, G is connected if and only if Sij > 0 for all i ̸= j. By (a)
and (b) this holds if and only if (I + A)m has no zero entry. [derived here] Bai gives the idea in
item 3 of his proof sketch [1].
    In the proof any exponent m ≥ N − 1 works, not only m = N − 1; the script confirmed this
on all labelled graphs with N ≤ 6 (Appendix A.6).

A.5    Distance: shortest walk, shortest trail, shortest path
      In plain words. Look at the shortest trip between two houses. It never passes
      a house twice. If it did, we could cut out the detour and get a shorter trip. That
      cannot be. So the shortest trip is also a route. It also never drives a road twice.

Proposition A.1. For vertices u, v of a simple graph, the length of a shortest (u, v)-walk, of a
shortest (u, v)-trail and of a shortest (u, v)-path are equal. Each is +∞ when the corresponding
set is empty, and the three sets are empty together. So the distance of Definition 2.48 is the
same whether “path” is read as trail or as path, and it equals the length of a shortest walk.

Proof. Every path is a trail (Proposition 2.39) and every trail is a walk. So the set of lengths
of paths is contained in the set of lengths of trails, which is contained in the set of lengths of
walks. Hence the minimum over walks is at most the minimum over trails, which is at most
the minimum over paths. By Lemma 2.52, a shortest walk contains a path of at most the

                                                    34
same length, so the minimum over paths is at most the minimum over walks. Therefore the
three minima are equal. If there is no walk, there is no trail and no path. If there is a walk,
Lemma 2.52 gives a path, and so the three sets are non-empty together. Grinberg makes the
same remark [3, Section 2.9.4, p. 40].

      In plain words. The distance has three easy features. It is never negative, and it
      is zero only from a house to itself. It is the same in both directions. And going by
      way of a third house is never shorter than the shortest trip.

Proposition A.2. The three properties of Remark 2.49 follow from Definition 2.48.

Proof. By Proposition A.1 we may compute d by shortest walks. (1) Lengths are 0, 1, 2, . . . or
+∞, so d ≥ 0. The walk consisting of u alone has length 0, so d(u, u) = 0. If d(u, v) = 0
there is a walk of length 0 from u to v; it is the single vertex, so v = u. (2) If u0 , . . . , uk is a
(u, v)-walk, then uk , . . . , u0 is a (v, u)-walk of the same length, since each step is an edge and
edges are unordered. So the sets of walk lengths from u to v and from v to u are equal, and so
are their minima. (3) If d(u, w) or d(w, v) is +∞, the right side is +∞ and the inequality holds.
Otherwise join a shortest (u, w)-walk and a shortest (w, v)-walk at w. The result is a (u, v)-walk
of length d(u, w) + d(w, v), and the shortest (u, v)-walk is no longer than this.

A.6    Cross-checks by script
These are tests of the statements by computer. They support the proofs and do not replace
them. All were run by the scripts of Appendix A.7.

    Walk counting. A case is one choice of a graph, an exponent k and a pair i, j; the
     number of cases is the number of graphs times the number of exponents times the number
     of pairs. For every labelled simple graph on N = 2, 3, 4, 5 vertices (2, 8, 64, 1024 graphs),
     the script enumerated all walks by depth-first search and compared their number with the
     entry (Ak )ij , with k up to 5 for N ≤ 4 and up to 3 for N = 5. The numbers of cases are
     2 · 5 · 4 = 40, 8 · 5 · 9 = 360, 64 · 5 · 16 = 5120 and 1024 · 3 · 25 = 76800, and in all of them
     the count equals the entry.

    Walk-to-path lemma and its consequences. The construction of Lemma 2.52 pro-
     duced a path with the same ends, no longer than the walk, with vertices taken from the
     walk, for all 73 walks of length 0 to 6 in B, all 381 in T and all 4695 in Gtb : no failure.
     On 300 random graphs with N from 2 to 7 (seed 20261027) and 192696 walks of length 0
     to 5 there was no failure of the lemma, no path with a repeated edge (Proposition 2.39),
     no path longer than N − 1 (Corollary 2.54), and no disagreement between breadth-first
     distance and the shortest walk, trail and path (Proposition A.1).

    The connectivity test. On all labelled simple graphs with N = 2, . . . , 6 vertices (Ta-
     ble 10), the sum test, the form with I + A, and the component statement of Corol-
     lary 4.10(a) all agreed with breadth-first search. The same table counts the graphs on
     which the test with N − 2 powers fails: 1, 3, 12, 60, 360 for N = 2, . . . , 6 (for N = 2 the
     sum with 0 powers is empty).

A.7    Scripts and how to reproduce
Every number in the paper came from one of the scripts in the folder appendices/scripts/ of
the paper. They use pure Python integers, so there is no rounding, and no library. A reader
who wants to check the numbers must run them; the PDF alone cannot confirm them. Run
each one from the paper folder with python3 -I, which keeps the interpreter from loading files


                                                  35
Table 12: The scripts and what each one computes. The saved output of each of the first three
has the same name with output.txt or .out.txt in place of .py.
  Script                                Computes
  m1 walks.py                           matrix powers of the board matrix, explicit walk lists, the sums
                                        of the induction step, walks against paths and trails, the brute-
                                        force check of walk counting
  m2 walks.py                           classification of the example sequences, counts of walks, trails,
                                        paths and closed walks, the trace of the walk-to-path lemma,
                                        exhaustive and random tests, distances
  m3 connectivity.py                    the sum test and the (I + A)N −1 test on the board graph, on
                                        D and on the row graph on four vertices, the exhaustive check
                                        against breadth-first search, and operation counts (about 35 sec-
                                        onds)
  generate paper numbers.py             reads the three saved outputs, recomputes every matrix and
                                        table with independent code, asserts equality, and writes
                                        appendices/generated numbers.tex, which defines the matri-
                                        ces and table bodies used in the text


from the current directory. Each script prints its results, and the saved output next to it can be
compared with that print.
   For example, from the paper folder:
python3 -I appendices/scripts/m1_walks.py
python3 -I appendices/scripts/m2_walks.py
python3 -I appendices/scripts/m3_connectivity.py
python3 -I appendices/scripts/generate_paper_numbers.py
Three small cases can be checked by hand against the scripts’ output. (1) For the board matrix,
(A2 )13 = P  A11 A13 + A12 A23 + A13 A33 = 0 · 0 + 1 · 1 + 0 · 0 = 1. (2) For the board matrix,
(A )12 = r (A2 )1r Ar2 = 1 · 1 + 0 · 0 + 1 · 1 = 2, the two walks 1, 2, 1, 2 and 1, 2, 3, 2. (3) For
   3

the graph D with the single edge 12, row 1 of A + A2 is (0, 1, 0) + (1, 0, 0) = (1, 1, 0), and row
3 is (0, 0, 0), so the entries (1, 3) and (3, 1) of S are 0 and D is not connected. The matrices in
Section 6, Example 4.18 and the tables of Tables 5, 6, 8 and 10 are macros from that file, so
none was typed by hand.


B     Course terms and textbook numbers
This appendix lists every term of the course that the paper uses, with the number and printed
page in the course textbook [9] and the English word. Page numbers are the printed page
numbers of the textbook; the PDF page is one higher. The textbook’s own word is given in
Latin letters as “path”, “simple path” and so on; its Armenian words are not reproduced. Terms
that the pages checked give no number for are marked “none”.

Figures of the textbook used. Fig. 1.2.5 (printed p. 22) is the source of the examples
for walks, trails, paths and cycles; Figure 3 draws the seven edges that those examples force.
Fig. 2.1.1 (p. 48) shows three connected graphs and Fig. 2.1.2 (p. 49) a graph with four compo-
nents [9].

A note on print order. In the printed text, the textbook’s example sentence for Defini-
tion 1.2.13 (the sequence v1 , v3 , v2 , v4 , v3 , v5 is not a simple path, while v1 , v3 , v4 , v5 is) stands af-
ter Definition 1.2.14 and not directly after Definition 1.2.13; its content is about Definition 1.2.13,
and this paper cites it by page (p. 22), not by position.

                                                       36
Table 13: Course terms, textbook numbers and pages, English words, and where they are defined
in this paper.
    Term in this paper     Textbook number      Printed   Textbook word if       Defined in
                                                page      different
    simple    undirected   Definition 1.1.1     9         graph                  Definition 2.1
    graph
    adjacent               Definition 1.1.4     11        —                      Definition 2.5
    adjacency matrix       none (after Def.     11        A(G)                   Definition 2.9
                           1.1.6)
    degree                 Definition 1.2.1     16        dG (v), d(v)           Definition 2.16
    sum of degrees         Theorem 1.2.1 (Eu-   16        —                      Proposition 2.20
                           ler)
    walk                   Definition 1.2.10    21        walk                   Definition 2.23
    closed walk            Definition 1.2.11    22        closed walk            Definition 2.27
    trail                  Definition 1.2.12    22        “path”                 Definition 2.31
    path                   Definition 1.2.13    22        “simple path”          Definition 2.35
    cycle                  Definition 1.2.14    22        “cycle” or “closed     Definition 2.40
                                                          path”
    simple cycle           Definition 1.2.15    22        “simple cycle”         Definition 2.44
    distance               Definition 1.2.16    22–23     distance               Definition 2.48
    walk contains a path   Lemma 1.2.1 (for     23        —                      Lemma 2.52
                           u ̸= v)
    connected              Definition 2.1.1     48        connected              Definition 2.55
    connected   compo-     none (prose)         49        connectivity    com-   Definition 2.60
    nent                                                  ponent
    connected iff one      Remark 2.1.1         49        —                      Remark 2.61
    component
    path between ni and    Definition 1.2.13    22        “simple path”          Definition 5.1
    nj


Results that the textbook does not contain. The walk-counting theorem (Theorem 3.5)
and the matrix test for connectivity (Theorem 4.6) are not in the pages checked and were
not found by a full-text search of the book (Section 1.6), so their absence from the book is
[qualified]. For the walk-counting theorem the paper cites the University of Galway notes, and
for the statement of the test Paramadevan and Sotheeswaran and Weisstein; the proofs are the
paper’s own.

The board’s letters. The board writes (G, V ) with V the edge set, eij ∈ V , |G| = N and
ni [4, 5]; the textbook writes G = (V, E), e ∈ E, n and vi . The paper uses G = (V, E), N and
ni (Table 4).


C      The board photographs
The two photographs of the whiteboard are in the folder sources of the paper as whiteboard-
1.jpg and whiteboard-2.jpg [4, 5]. They are not embedded in this paper. They show the
same board, the second at a slightly different angle, with the reflection of a person on the right
of the board. Read from top to bottom, the board holds the following, which is the content of
Table 1.

    1. The definition of Aij as 1 or 0 according to whether eij is in the set the board calls V ,
       which is the edge set.

    2. A drawing of three circled vertices 1, 2, 3: a line from 1 to 2 with an arrowhead at 2, a


                                                    37
     line from 1 to 3, and a line from 2 to 3 (Figure 1, right). Next to it, a 3 × 3 grid labelled
     “adj.” with the rows 0 1 0, 1 0 1, 0 1 0.

  3. The problem statement: “Given graph (G, V ) with N nodes i.e. |G| = N and the graph is
     represented through it’s adj. matrix. So you have “A” matrix.”

  4. Question 1, “What does Aij represent”, with a small mark above A that looks like quota-
     tion marks or a small n.

  5. Question 2, “How to know if graph is connected or not”.

  6. The definition: “Graph is called connected if for any ni , nj there exists a path between
     nodes”.

The prose, the matrix entries and the vertex labels are legible. The mark above A, the extra
line 1–3 and the arrowhead are the points discussed in Section 1.3.




                                               38
```

# The Adjacency Matrix, Its Powers, and the Connectivity of a Graph

## 1. Introduction

A graph is a picture made of dots and lines. The dots are called vertices, or nodes. The lines are called edges. Graphs describe things that are joined to each other, such as cities joined by roads or people joined by friendships.

A computer cannot look at a picture of dots and lines. It needs numbers. The adjacency matrix is a table of numbers that stores the same information as the picture. This paper explains the adjacency matrix and uses it to answer three questions. The first two are written on the lecture board. The third was added by the assignment text that came with the photos of the board. Two photos of the same board are kept with this paper.

**The story used in this paper.** Think of every dot as a house and every line as a road between two houses. A road has no one-way sign, so you can walk it both ways. No road goes from a house back to the same house, and no two houses have two roads between them. Walking along one road is one hop. When the story needs "some number of hops", it calls that number $k$. House number $i$ and house number $j$ are any two houses. Every idea in this paper is first told as a story about houses and roads, in words a small child can follow when read aloud. Then the same idea is written in mathematics. The story and the mathematics always say the same thing.

In the story, the three questions are:

1. If I write down how many different trips of exactly $k$ hops go from one house to another, where do I find that number?
2. Can every house be reached from every other house?
3. What exactly is a trip that never visits the same house twice?

1. What does the entry $(A^k)_{ij}$ of the $k$-th power of the adjacency matrix represent?
2. How can we tell whether a graph is connected?
3. What is a path between two vertices $n_i$ and $n_j$?

The definitions follow the course textbook, "Graph Theory" (Grafneri tesutyun), Chapter 1 and Chapter 2. Where the lecture board or the textbook uses a different letter or name, this paper says so. The textbook does not contain a statement about powers of the adjacency matrix, so Section 3 is written from the definitions and proved in the paper.

### Conventions and assumptions

Every symbol used in this paper is defined here or where it first appears.

- A graph is written $G = (V, E)$, as in the textbook. The set $V$ holds the vertices and the set $E$ holds the edges. The lecture board writes the pair as $(G, V)$ and writes $|G| = N$ for the number of vertices. The meaning is the same.
- The graph has $N$ vertices, named $n_1, n_2, \ldots, n_N$, as on the board. The textbook writes $n$ for the number of vertices and names them $v_1, \ldots, v_n$. In symbols, $|V| = N$.
- The graph is undirected. An edge is a plain line with no arrow, and it can be travelled in both directions.
- The graph is simple. There is at most one edge between two vertices, and no edge joins a vertex to itself.
- The edge between $n_i$ and $n_j$ is written $e_{ij}$, as on the board. The textbook writes the same edge as $n_i n_j$. Because the graph is undirected, $e_{ij}$ and $e_{ji}$ are the same edge.
- Two vertices joined by an edge are called adjacent (textbook, Definition 1.1.4).
- The board writes the condition for an edge as $e_{ij} \in V$, using the letter $V$ for the set of edges. This paper writes $e_{ij} \in E$, as in the textbook.
- In the board's first question there is a small mark above the letter $A$. It could be read as a power or as quotation marks. The assignment text asks about $A^k$, so this paper takes that reading.
- The drawing on the board has a short arrowhead on the line from vertex 1 to vertex 2. The matrix on the board is symmetric, so the arrowhead is treated as a stray mark and the graph as undirected.

## 2. Definition of the adjacency matrix

**In plain words.** Give every house a number. Draw a big square table. Write the house numbers across the top and down the side. Each little box belongs to one house on the side and one house on the top. Write 1 in the box if those two houses have a road between them. Write 0 if they do not. This table is the adjacency matrix. Looking at the table tells you everything the picture tells you.

A matrix is a table of numbers arranged in rows and columns. The adjacency matrix has one row and one column for every vertex. The number in row $i$ and column $j$ is written $A_{ij}$. The textbook writes it in lowercase, $a_{ij}$, and writes the whole matrix as $A(G)$.

**Definition 1 (adjacency matrix; textbook Section 1.1).** The adjacency matrix of a graph $G = (V, E)$ with $N$ vertices is the matrix $A$ with $N$ rows and $N$ columns (an $N \times N$ matrix) whose entries are

$$
A_{ij} =
\begin{cases}
1, & \text{if } n_i \text{ and } n_j \text{ are adjacent, that is, } e_{ij} \in E, \\
0, & \text{otherwise.}
\end{cases}
$$

In words, $A_{ij} = 1$ means "vertex $i$ and vertex $j$ are joined by one edge". So the matrix answers the question "are these two vertices adjacent?" for every pair of vertices at once.

The textbook notes two facts right after the definition, and a third follows easily.

- The diagonal is zero. The diagonal is the line of boxes $A_{ii}$ whose row number and column number are the same. Here $A_{ii} = 0$ for every $i$, because no vertex is joined to itself.
- The matrix is symmetric: $A_{ij} = A_{ji}$ for all $i$ and $j$. The edge between $n_i$ and $n_j$ is the same edge as the edge between $n_j$ and $n_i$.
- Row $i$ lists the neighbours of $n_i$. The sum of row $i$ is the number of edges touching $n_i$. This number is called the degree of $n_i$.

The textbook also remarks that the reverse is true: every $N \times N$ table of zeros and ones with a zero diagonal and $A_{ij} = A_{ji}$ is the adjacency matrix of some graph with $N$ numbered vertices. So the matrix and the picture carry exactly the same information.

Row $i$ of the matrix answers "who is $n_i$ joined to?". Column $j$ answers "who is joined to $n_j$?". In an undirected graph these two questions have the same answer, which is another way of seeing that the matrix is symmetric.

Example and non-example. The matrix $A$ written out in Section 6 is the adjacency matrix of the three-vertex graph drawn there. The table with rows $0, 1$ and $0, 0$ is not the adjacency matrix of any undirected graph, because it is not symmetric: it says $n_1$ is joined to $n_2$ but $n_2$ is not joined to $n_1$.

## 3. Answer 1: the meaning of $(A^k)_{ij}$

### 3.1 Walks

First we need a word for a trip through the graph. The textbook's word is walk.

**In plain words.** A walk is a trip. You start at a house. Each hop takes you along one road to a house next door. You may go back to a house you already saw. You may use the same road again. The length of the walk is the number of hops.

**Definition 2 (walk; textbook Definition 1.2.10).** A walk of length $k$ from $n_i$ to $n_j$, also called an $(n_i, n_j)$-walk, where $k \geq 0$ is a whole number, is a list of $k + 1$ vertices

$$
n_i = u_0,\; u_1,\; u_2,\; \ldots,\; u_k = n_j
$$

in which every two neighbouring vertices in the list are adjacent. That is, $u_{s-1} u_s \in E$ for every $s = 1, 2, \ldots, k$. A walk of length 0 is a single vertex with no hops.

The textbook writes a walk in full as $u_0, e_1, u_1, e_2, \ldots, e_k, u_k$, listing the edge $e_s = u_{s-1} u_s$ between each pair of vertices, and then agrees to shorten it to the list of vertices alone. The textbook stresses that in a walk both vertices and edges may repeat, and that the length counts every edge as many times as the walk uses it. A walk is called closed if it starts and ends at the same vertex, $u_0 = u_k$ (Definition 1.2.11).

Example and non-example, in the graph of Section 6 with edges $e_{12}$ and $e_{23}$. The list $n_1, n_2, n_1, n_2, n_3$ is a walk of length 4 from $n_1$ to $n_3$: each neighbouring pair is adjacent, and it is allowed to repeat $n_1$, $n_2$, and the edge $e_{12}$. The list $n_1, n_3, n_2$ is not a walk, because $n_1$ and $n_3$ are not adjacent.

### 3.2 The statement

**In plain words.** Write the table down $k$ times and multiply all the copies together. You get a new table. Look at the box for house $i$ and house $j$. The number there is how many different trips of exactly $k$ hops go from house $i$ to house $j$. For $k = 1$ the new table is the old one. There is one trip of one hop exactly when there is a road.

The $k$-th power of $A$ is the matrix $A^k = A \cdot A \cdots A$, with $k$ copies of $A$ multiplied together. Its entry in row $i$ and column $j$ is written $(A^k)_{ij}$.

**Theorem 1.** For every $k \geq 1$, the entry $(A^k)_{ij}$ equals the number of different walks of length $k$ from $n_i$ to $n_j$.

For $k = 1$ this is just Definition 1. A walk of length 1 from $n_i$ to $n_j$ is a single edge, and $A_{ij}$ is 1 when that edge exists and 0 when it does not.

### 3.3 Why the theorem is true

**In plain words.** A trip of two hops from house $i$ to house $j$ stops at one house in the middle. To count such trips, try every house as the middle one. A house works as the middle if two roads exist. One road goes from house $i$ to it. The other goes from it to house $j$. Count how many houses work. That count is the answer. Multiplying the table by itself does this count for you.

The proof is by induction on $k$, a method explained at the end of this section. Look at $k = 2$ first. A walk of length 2 from $n_i$ to $n_j$ has one middle stop, call it $n_m$. The walk exists exactly when $n_i$ is adjacent to $n_m$ and $n_m$ is adjacent to $n_j$. To count all such walks, go through every possible middle stop $m = 1, 2, \ldots, N$ and count the ones where both edges exist.

The rule for multiplying a matrix by itself does exactly this count:

$$
(A^2)_{ij} = \sum_{m=1}^{N} A_{im} \, A_{mj} .
$$

The sign $\sum_{m=1}^{N}$ means: write the term for $m = 1$, then for $m = 2$, and so on up to $m = N$, and add them all. Each term $A_{im} A_{mj}$ is 1 when both edges exist and 0 otherwise. Adding the terms counts the walks of length 2.

The same reasoning works for any $k$. A walk of length $k$ from $n_i$ to $n_j$ is a walk of length $k - 1$ from $n_i$ to some vertex $n_m$, followed by one edge from $n_m$ to $n_j$. Therefore

$$
(A^k)_{ij} = \sum_{m=1}^{N} (A^{k-1})_{im} \, A_{mj} ,
$$

which is the rule for computing $A^k = A^{k-1} \cdot A$. If $(A^{k-1})_{im}$ already counts walks of length $k - 1$, then the sum counts walks of length $k$. Starting from $k = 1$ and repeating this step proves the theorem for every $k$. This kind of proof, where each case is built from the one before it, is called proof by induction. The textbook uses the same method for its Lemma 1.2.1.

### 3.4 An important warning

**In plain words.** The table counts trips where going back and forth is allowed. Walk to the neighbour's house and straight back home. That is a trip of two hops, and the table counts it. So the numbers in the table count all trips. They do not count only the trips that never turn back.

Theorem 1 counts walks, not paths. A walk may go back and forth over the same edge or return to a vertex it has already visited. For example, in any graph with an edge between $n_1$ and $n_2$, the list $n_1, n_2, n_1$ is a closed walk of length 2 from $n_1$ back to $n_1$, so $(A^2)_{11} \geq 1$. It uses the same edge twice and visits $n_1$ twice, so it is not a path in either sense defined in Section 5. In general, $(A^k)_{ii}$ counts the closed walks of length $k$ that start and end at $n_i$.

## 4. Answer 2: determining whether the graph is connected

The word "connected" is used for three different questions. They must be kept apart.

**In plain words.** There are three different questions. Is there a road straight from my house to yours? Can I get from my house to yours at all, maybe through other houses? Can everybody get to everybody? The lecture asks the last one.

### 4.1 Are two vertices joined by a direct edge?

**In plain words.** Look at the box for the two houses. A 1 means there is a road straight between them. A 0 means there is not.

Look at the single entry $A_{ij}$. If $A_{ij} = 1$, the vertices are adjacent. If $A_{ij} = 0$, they are not. This is the smallest question.

### 4.2 Are two vertices joined by a path?

**In plain words.** Maybe there is no road straight from house $i$ to house $j$. You may still get there by passing other houses. To find out, count trips of one hop, then two hops, then three, and so on. If any of those counts is bigger than zero, you can get there. You never need more hops than the number of houses minus one. A trip that never repeats a house cannot be longer than that.

Two vertices can be joined by a path even when $A_{ij} = 0$, because the path may pass through other vertices. Theorem 1 gives a test. The word path is defined precisely in Section 5; for now, a path is a walk that never visits the same vertex twice.

**Theorem 2.** Let $i \neq j$. There is a path from $n_i$ to $n_j$ if and only if $(A^k)_{ij} > 0$ for at least one $k$ with $1 \leq k \leq N - 1$.

Why this is true, in two halves.

- If some $(A^k)_{ij} > 0$, then by Theorem 1 there is a walk from $n_i$ to $n_j$. The textbook's Lemma 1.2.1 says that from any walk between two different vertices one can extract a path with no repeated vertices. The idea of its proof: if the walk visits some vertex twice, cut out the part of the walk between the two visits. The result is still a walk from $n_i$ to $n_j$, but shorter. Repeat until no vertex is visited twice. What remains is a path.
- If a path from $n_i$ to $n_j$ exists, it is also a walk of some length $m$, so $(A^m)_{ij} \geq 1$. A path never repeats a vertex, so it visits at most $N$ vertices and uses at most $N - 1$ edges. Hence $m \leq N - 1$, and powers beyond $N - 1$ are never needed.

### 4.3 Is the whole graph connected?

This is the question asked in the lecture.

**In plain words.** A graph is connected when you can walk from any house to any other house along the roads. If even one house cannot be reached from some other house, the graph is not connected.

**Definition 3 (connected graph; textbook Definition 2.1.1).** A graph $G$ is connected if for every two vertices $n_i$ and $n_j$ there exists an $(n_i, n_j)$-path in $G$.

This is the definition written at the bottom of the lecture board. The textbook states it with its own word path, which allows repeated vertices but not repeated edges (see Section 5). Lemma 1.2.1 shows that this makes no difference: if there is a path of either kind between two vertices, there is also one with no repeated vertices. So Definition 3 can be read with the course's convention that a path repeats no vertex. For the pair $n_i, n_i$ the condition holds by itself, because the single vertex $n_i$ is a path of length 0.

Example and non-example. The three-vertex graph of Section 6 is connected: every pair of its vertices is joined by a path. The same graph with the edge $e_{23}$ removed, also shown in Section 6, is not connected, because no path reaches $n_3$.

Applying Theorem 2 to every pair at once gives a test that uses only the adjacency matrix.

**In plain words.** Make the one-hop table and the two-hop table. Keep going up to the table for "number of houses minus one" hops. Add all these tables together, box by box. Skip the boxes where a house meets itself. Look at all the other boxes. If every one of them has a number bigger than zero, everybody can reach everybody. Then the graph is connected. If any of them has a zero, two houses cannot reach each other.

**Theorem 3.** Form the matrix

$$
S = A + A^2 + A^3 + \cdots + A^{N-1} .
$$

The graph is connected if and only if every entry $S_{ij}$ with $i \neq j$ is greater than zero.

The entry $S_{ij}$ is the total number of walks from $n_i$ to $n_j$ of length between 1 and $N - 1$. It is positive exactly when at least one such walk exists, which by Theorem 2 is exactly when a path exists. If this holds for every pair, the graph is connected by Definition 3. If some $S_{ij}$ is zero, no path joins $n_i$ to $n_j$, and the graph is not connected.

**In plain words.** There is a shortcut. Put a 1 in every box where a house meets itself. Write this new table down "houses minus one" times and multiply the copies together. If no box is zero, the graph is connected.

An equivalent form that is sometimes quicker to compute is to check that the matrix $(I + A)^{N-1}$ has no zero entries. Here $I$ is the identity matrix: the $N \times N$ matrix with $I_{ii} = 1$ on the diagonal and 0 everywhere else. Adding $I$ lets a walk "pause" at a vertex, so this single power collects all walks of length at most $N - 1$.

**In plain words.** Another way needs no tables at all. Start at one house. Visit every house next door, then every house next door to those, and keep going. Stop when there is nothing new to visit. If you visited every house, the graph is connected.

The textbook's own treatment of connectivity (Section 2.1) groups the vertices by the rule "there is a path between $n_i$ and $n_j$", and calls each group a connectivity component. Remark 2.1.1 there says a graph is connected exactly when it has one component. In practice, for large graphs, connectivity is tested by exploring the graph from one vertex, visiting neighbours of neighbours until no new vertex is found, and checking whether every vertex was visited. The matrix power method is the one that connects directly to Theorem 1.

## 5. Answer 3: definition of a path

**In plain words.** A path is a special trip: a trip that never visits the same house twice. You start at one house, hop along roads, and every house you reach is new. Because you never come back to a house, you also never use the same road twice.

The textbook defines a path in two steps. Both are given here, because the course uses the stricter one.

**Definition 4a (path; textbook Definition 1.2.12).** An $(n_i, n_j)$-walk $u_0, u_1, \ldots, u_m$ is called a path from $n_i$ to $n_j$, or an $(n_i, n_j)$-path, if its edges $u_0 u_1, u_1 u_2, \ldots, u_{m-1} u_m$ are pairwise different. In this definition a vertex may be visited more than once, but no edge is used twice.

**Definition 4b (simple path; textbook Definition 1.2.13).** An $(n_i, n_j)$-path is called a simple $(n_i, n_j)$-path if all of its vertices $u_0, u_1, \ldots, u_m$ are pairwise different.

In this course the word path is used in the sense of Definition 4b: a path repeats no vertex. Written out in full, that is:

**Definition 4 (path, course convention).** A path of length $m$ from $n_i$ to $n_j$, where $m \geq 0$ is a whole number, is a list of $m + 1$ vertices

$$
n_i = u_0,\; u_1,\; \ldots,\; u_m = n_j
$$

such that

1. every two neighbouring vertices in the list are adjacent, that is, $u_{s-1} u_s \in E$ for every $s = 1, 2, \ldots, m$, and
2. all the vertices in the list are different.

In simple words, a path is a route from $n_i$ to $n_j$ that follows the lines of the graph and never visits the same dot twice. Its length is the number of edges it uses, written $|P|$ in the textbook. If no vertex repeats, then no edge can repeat either, so every path in the course's sense is also a path in the textbook's sense.

Example and non-example, in the graph of Section 6. The list $n_1, n_2, n_3$ is a path of length 2 from $n_1$ to $n_3$: both pairs are adjacent and no vertex repeats. The walk $n_1, n_2, n_1, n_2, n_3$ from Section 3.1 is not a path, because $n_1$ and $n_2$ each appear twice. It is not a path in the textbook's sense either, because the edge $e_{12}$ is used three times. In the triangle drawn on the board, with all three edges $e_{12}$, $e_{13}$, $e_{23}$, the list $n_1, n_2, n_3, n_1$ is a path in the textbook's sense, because its three edges are all different, but not in the course's sense, because $n_1$ appears twice.

The textbook adds two related words. A path in the textbook's sense (Definition 4a) that starts and ends at the same vertex is called a cycle (Definition 1.2.14); a path in the course's sense cannot do this, because its first and last vertex would be the same. The distance between two vertices is the length of the shortest path between them (Definition 1.2.16). When no path exists, the textbook writes the distance as $+\infty$, read "infinity", meaning that no number of hops is enough.

Four ideas that are easy to confuse.

- An edge is a path of length 1. It joins two vertices directly.
- A walk (Definition 2) may revisit vertices and reuse edges. Every path is a walk. Not every walk is a path.
- A path in the textbook's sense (Definition 4a) may revisit a vertex but not an edge. A simple path, the course's path (Definition 4), does neither.
- Connectivity of the graph (Definition 3) is a statement about all pairs of vertices at once. A path is a statement about one pair.

## 6. Worked example

**In plain words.** Now the whole paper is tried out on the three houses from the lecture. First the table is built. Then the two-hop table and the three-hop table are computed. Then the connected test is run. Last, one road is taken away to watch the test fail.

Use the graph from the lecture. The matrix on the board has ones in the boxes for the pairs 1,2 and 2,3, so the graph has three vertices $n_1, n_2, n_3$ and two edges, $e_{12}$ and $e_{23}$. The drawing on the board does not match the matrix exactly: it is a triangle, with a third line from vertex 1 to vertex 3 that the matrix does not have. The matrix is the precise record, so this paper follows the matrix. Drawn as dots in a row:

```
n1 ---- n2 ---- n3
```

In the story: three houses in a row, a road from house 1 to house 2, and a road from house 2 to house 3. There is no road straight from house 1 to house 3.

Its adjacency matrix is

$$
A =
\begin{pmatrix}
0 & 1 & 0 \\
1 & 0 & 1 \\
0 & 1 & 0
\end{pmatrix}.
$$

Check row 2: it reads $1, 0, 1$, so $n_2$ is adjacent to $n_1$ and to $n_3$. The matrix is symmetric and the diagonal is zero, as expected.

**Direct edges.** $A_{12} = 1$, so $n_1$ and $n_2$ are adjacent. $A_{13} = 0$, so $n_1$ and $n_3$ are not adjacent.

**Second power.** Multiplying $A$ by itself gives

$$
A^2 =
\begin{pmatrix}
1 & 0 & 1 \\
0 & 2 & 0 \\
1 & 0 & 1
\end{pmatrix}.
$$

Reading the entries with Theorem 1:

- $(A^2)_{13} = 1$. There is one walk of length 2 from $n_1$ to $n_3$, namely $n_1, n_2, n_3$. This walk is also a path.
- $(A^2)_{11} = 1$. The one walk of length 2 from $n_1$ to itself is $n_1, n_2, n_1$. It is a closed walk but not a path, because it uses the edge $e_{12}$ twice and visits $n_1$ twice.
- $(A^2)_{22} = 2$. The two closed walks are $n_2, n_1, n_2$ and $n_2, n_3, n_2$.

**Third power.** For illustration,

$$
A^3 =
\begin{pmatrix}
0 & 2 & 0 \\
2 & 0 & 2 \\
0 & 2 & 0
\end{pmatrix}.
$$

$(A^3)_{12} = 2$: the walks are $n_1, n_2, n_1, n_2$ and $n_1, n_2, n_3, n_2$. Neither is a path.

**Connectivity test.** Here $N = 3$, so Theorem 3 needs only $A$ and $A^2$:

$$
S = A + A^2 =
\begin{pmatrix}
1 & 1 & 1 \\
1 & 2 & 1 \\
1 & 1 & 1
\end{pmatrix}.
$$

Every entry off the diagonal is positive, so the graph is connected. This agrees with the picture: $n_1$ reaches $n_2$ by an edge, $n_2$ reaches $n_3$ by an edge, and $n_1$ reaches $n_3$ by the path $n_1, n_2, n_3$. In the textbook's language, the graph has one connectivity component.

**In plain words.** Take away the road from house 2 to house 3. House 3 is now on its own. Nobody can walk to it. The test must say the graph is not connected. Let us check that it does.

**A graph that is not connected.** Remove the edge $e_{23}$. Call the new adjacency matrix $A'$. It, its square, and their sum are

$$
A' =
\begin{pmatrix}
0 & 1 & 0 \\
1 & 0 & 0 \\
0 & 0 & 0
\end{pmatrix},
\qquad
A'^2 =
\begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 0
\end{pmatrix},
\qquad
S' = A' + A'^2 =
\begin{pmatrix}
1 & 1 & 0 \\
1 & 1 & 0 \\
0 & 0 & 0
\end{pmatrix}.
$$

The entries $S'_{13}$ and $S'_{23}$ are zero. No path reaches $n_3$, so this graph is not connected. It has two connectivity components: one containing $n_1$ and $n_2$, and one containing only $n_3$. The zeros in the table show exactly what the story said: nobody can walk to house 3.

## 7. Conclusion

**In plain words.** A graph is houses and roads. The adjacency matrix is a table with a 1 where there is a road. Write the table down $k$ times and multiply the copies together. Then each box counts the trips of exactly $k$ hops between two houses, turning back allowed. A path is a trip that never visits the same house twice. Add up the trip tables for one hop up to "houses minus one" hops. Skip the boxes where a house meets itself. If none of the other boxes is zero, everybody can reach everybody, and the graph is connected.

The adjacency matrix $A$ stores a graph as a table of zeros and ones, where $A_{ij} = 1$ exactly when vertices $n_i$ and $n_j$ are adjacent. The entry $(A^k)_{ij}$ of the $k$-th power counts the walks of length $k$ from $n_i$ to $n_j$, where a walk may revisit vertices and reuse edges. A path, in the course's sense, is a walk that never revisits a vertex; the textbook calls this a simple path. Two different vertices are joined by a path exactly when some power $A^k$ with $1 \leq k \leq N - 1$ has a positive entry in their cell. The whole graph is connected exactly when every off-diagonal entry of $A + A^2 + \cdots + A^{N-1}$ is positive. The key to this topic is to keep four ideas apart: a direct edge, a walk, a path between two vertices, and connectivity of the whole graph.

## Appendix: terms used in the course textbook

| Textbook term (Armenian) | English term used here | Where defined |
| --- | --- | --- |
| գագաթ | vertex, node | Section 1.1 |
| կող | edge | Section 1.1 |
| հարևան գագաթներ | adjacent vertices | Definition 1.1.4 |
| կից | incident (a vertex and an edge that touch) | Definition 1.1.5 |
| հարևանության մատրից | adjacency matrix | Section 1.1 |
| կցության մատրից | incidence matrix (not used in this paper) | Section 1.1 |
| շրջանցում | walk | Definition 1.2.10 |
| փակ շրջանցում | closed walk | Definition 1.2.11 |
| ճանապարհ | path (no repeated edge) | Definition 1.2.12 |
| պարզ ճանապարհ | simple path (no repeated vertex); the course's "path" | Definition 1.2.13 |
| ցիկլ | cycle | Definition 1.2.14 |
| հեռավորություն | distance | Definition 1.2.16 |
| կապակցված գրաֆ | connected graph | Definition 2.1.1 |
| կապակցվածության բաղադրիչ | connectivity component | Section 2.1 |

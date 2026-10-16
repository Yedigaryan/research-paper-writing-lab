# The Adjacency Matrix, Its Powers, and the Connectivity of a Graph

## 1. Introduction

A graph is a picture made of dots and lines. The dots are called vertices, or nodes. The lines are called edges. Graphs describe things that are joined to each other, such as cities joined by roads or people joined by friendships.

A computer cannot look at a picture of dots and lines. It needs numbers. The adjacency matrix is a table of numbers that stores the same information as the picture. This paper explains the adjacency matrix and uses it to answer three questions from the lecture.

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

## 2. Definition of the adjacency matrix

A matrix is a table of numbers arranged in rows and columns. The adjacency matrix has one row and one column for every vertex. The number in row $i$ and column $j$ is written $A_{ij}$. The textbook writes it in lowercase, $a_{ij}$, and writes the whole matrix as $A(G)$.

**Definition 1 (adjacency matrix; textbook Section 1.1).** The adjacency matrix of a graph $G = (V, E)$ with $N$ vertices is the $N \times N$ matrix $A$ whose entries are

$$
A_{ij} =
\begin{cases}
1, & \text{if } n_i \text{ and } n_j \text{ are adjacent, that is, } e_{ij} \in E, \\
0, & \text{otherwise.}
\end{cases}
$$

In words, $A_{ij} = 1$ means "vertex $i$ and vertex $j$ are joined by one edge". So the matrix answers the question "are these two vertices adjacent?" for every pair of vertices at once.

The textbook notes two facts right after the definition, and a third follows easily.

- The diagonal is zero: $A_{ii} = 0$ for every $i$. No vertex is joined to itself.
- The matrix is symmetric: $A_{ij} = A_{ji}$ for all $i$ and $j$. The edge between $n_i$ and $n_j$ is the same edge as the edge between $n_j$ and $n_i$.
- Row $i$ lists the neighbours of $n_i$. The sum of row $i$ is the number of edges touching $n_i$. This number is called the degree of $n_i$.

The textbook also remarks that the reverse is true: every $N \times N$ table of zeros and ones with a zero diagonal and $A_{ij} = A_{ji}$ is the adjacency matrix of some graph with $N$ numbered vertices. So the matrix and the picture carry exactly the same information.

Row $i$ of the matrix answers "who is $n_i$ joined to?". Column $j$ answers "who is joined to $n_j$?". In an undirected graph these two questions have the same answer, which is another way of seeing that the matrix is symmetric.

## 3. Answer 1: the meaning of $(A^k)_{ij}$

### 3.1 Walks

First we need a word for a trip through the graph. The textbook's word is walk.

**Definition 2 (walk; textbook Definition 1.2.10).** A walk of length $k$ from $n_i$ to $n_j$, also called an $(n_i, n_j)$-walk, is a list of $k + 1$ vertices

$$
n_i = u_0,\; u_1,\; u_2,\; \ldots,\; u_k = n_j
$$

in which every two neighbouring vertices in the list are adjacent. That is, $u_{s-1} u_s \in E$ for every $s = 1, 2, \ldots, k$.

The textbook writes a walk in full as $u_0, e_1, u_1, e_2, \ldots, e_k, u_k$, listing the edge $e_s = u_{s-1} u_s$ between each pair of vertices, and then agrees to shorten it to the list of vertices alone. The textbook stresses that in a walk both vertices and edges may repeat, and that the length counts every edge as many times as the walk uses it. A walk is called closed if it starts and ends at the same vertex, $u_0 = u_k$ (Definition 1.2.11).

### 3.2 The statement

The $k$-th power of $A$ is the matrix $A^k = A \cdot A \cdots A$, with $k$ copies of $A$ multiplied together. Its entry in row $i$ and column $j$ is written $(A^k)_{ij}$.

**Theorem 1.** For every $k \geq 1$, the entry $(A^k)_{ij}$ equals the number of different walks of length $k$ from $n_i$ to $n_j$.

For $k = 1$ this is just Definition 1. A walk of length 1 from $n_i$ to $n_j$ is a single edge, and $A_{ij}$ is 1 when that edge exists and 0 when it does not.

### 3.3 Why the theorem is true

Look at $k = 2$ first. A walk of length 2 from $n_i$ to $n_j$ has one middle stop, call it $n_m$. The walk exists exactly when $n_i$ is adjacent to $n_m$ and $n_m$ is adjacent to $n_j$. To count all such walks, go through every possible middle stop $m = 1, 2, \ldots, N$ and count the ones where both edges exist.

The rule for multiplying a matrix by itself does exactly this count:

$$
(A^2)_{ij} = \sum_{m=1}^{N} A_{im} \, A_{mj} .
$$

Each term $A_{im} A_{mj}$ is 1 when both edges exist and 0 otherwise. Adding the terms counts the walks of length 2.

The same reasoning works for any $k$. A walk of length $k$ from $n_i$ to $n_j$ is a walk of length $k - 1$ from $n_i$ to some vertex $n_m$, followed by one edge from $n_m$ to $n_j$. Therefore

$$
(A^k)_{ij} = \sum_{m=1}^{N} (A^{k-1})_{im} \, A_{mj} ,
$$

which is the rule for computing $A^k = A^{k-1} \cdot A$. If $(A^{k-1})_{im}$ already counts walks of length $k - 1$, then the sum counts walks of length $k$. Starting from $k = 1$ and repeating this step proves the theorem for every $k$. This kind of proof, where each case is built from the one before it, is called proof by induction. The textbook uses the same method for its Lemma 1.2.1.

### 3.4 An important warning

Theorem 1 counts walks, not paths. A walk may go back and forth over the same edge or return to a vertex it has already visited. For example, in any graph with an edge between $n_1$ and $n_2$, the list $n_1, n_2, n_1$ is a closed walk of length 2 from $n_1$ back to $n_1$, so $(A^2)_{11} \geq 1$. It uses the same edge twice and visits $n_1$ twice, so it is not a path in either sense defined in Section 5. In general, $(A^k)_{ii}$ counts the closed walks of length $k$ that start and end at $n_i$.

## 4. Answer 2: determining whether the graph is connected

The word "connected" is used for three different questions. They must be kept apart.

### 4.1 Are two vertices joined by a direct edge?

Look at the single entry $A_{ij}$. If $A_{ij} = 1$, the vertices are adjacent. If $A_{ij} = 0$, they are not. This is the smallest question.

### 4.2 Are two vertices joined by a path?

Two vertices can be joined by a path even when $A_{ij} = 0$, because the path may pass through other vertices. Theorem 1 gives a test. The word path is defined precisely in Section 5; for now, a path is a walk that never visits the same vertex twice.

**Theorem 2.** Let $i \neq j$. There is a path from $n_i$ to $n_j$ if and only if $(A^k)_{ij} > 0$ for at least one $k$ with $1 \leq k \leq N - 1$.

Why this is true, in two halves.

- If some $(A^k)_{ij} > 0$, then by Theorem 1 there is a walk from $n_i$ to $n_j$. The textbook's Lemma 1.2.1 says that from any walk between two different vertices one can extract a path with no repeated vertices. The idea of its proof: if the walk visits some vertex twice, cut out the part of the walk between the two visits. The result is still a walk from $n_i$ to $n_j$, but shorter. Repeat until no vertex is visited twice. What remains is a path.
- If a path from $n_i$ to $n_j$ exists, it is also a walk of some length $m$, so $(A^m)_{ij} \geq 1$. A path never repeats a vertex, so it visits at most $N$ vertices and uses at most $N - 1$ edges. Hence $m \leq N - 1$, and powers beyond $N - 1$ are never needed.

### 4.3 Is the whole graph connected?

This is the question asked in the lecture.

**Definition 3 (connected graph; textbook Definition 2.1.1).** A graph $G$ is connected if for every two vertices $n_i$ and $n_j$ there exists an $(n_i, n_j)$-path in $G$.

This is the definition written at the bottom of the lecture board. The textbook states it with its own word path, which allows repeated vertices but not repeated edges (see Section 5). Lemma 1.2.1 shows that this makes no difference: if there is a path of either kind between two vertices, there is also one with no repeated vertices. So Definition 3 can be read with the course's convention that a path repeats no vertex.

Applying Theorem 2 to every pair at once gives a test that uses only the adjacency matrix.

**Theorem 3.** Form the matrix

$$
S = A + A^2 + A^3 + \cdots + A^{N-1} .
$$

The graph is connected if and only if every entry $S_{ij}$ with $i \neq j$ is greater than zero.

The entry $S_{ij}$ is the total number of walks from $n_i$ to $n_j$ of length at most $N - 1$. It is positive exactly when at least one such walk exists, which by Theorem 2 is exactly when a path exists. If this holds for every pair, the graph is connected by Definition 3. If some $S_{ij}$ is zero, no path joins $n_i$ to $n_j$, and the graph is not connected.

An equivalent form that is sometimes quicker to compute is to check that the matrix $(I + A)^{N-1}$ has no zero entries, where $I$ is the identity matrix. Adding $I$ lets a walk "pause" at a vertex, so this single power collects all walks of length at most $N - 1$.

The textbook's own treatment of connectivity (Section 2.1) uses the relation "there is a path between $u$ and $v$" to split the vertex set into pieces called connectivity components. Remark 2.1.1 there says a graph is connected exactly when it has one component. In practice, for large graphs, this is tested by exploring the graph from one vertex, visiting neighbours of neighbours until no new vertex is found, and checking whether every vertex was visited. The matrix power method is the one that connects directly to Theorem 1.

## 5. Answer 3: definition of a path

The textbook defines a path in two steps. Both are given here, because the course uses the stricter one.

**Definition 4a (path; textbook Definition 1.2.12).** An $(n_i, n_j)$-walk $u_0, u_1, \ldots, u_m$ is called a path from $n_i$ to $n_j$, or an $(n_i, n_j)$-path, if its edges $u_0 u_1, u_1 u_2, \ldots, u_{m-1} u_m$ are pairwise different. In this definition a vertex may be visited more than once, but no edge is used twice.

**Definition 4b (simple path; textbook Definition 1.2.13).** An $(n_i, n_j)$-path is called a simple $(n_i, n_j)$-path if all of its vertices $u_0, u_1, \ldots, u_m$ are pairwise different.

In this course the word path is used in the sense of Definition 4b: a path repeats no vertex. Written out in full, that is:

**Definition 4 (path, course convention).** A path of length $m$ from $n_i$ to $n_j$ is a list of $m + 1$ vertices

$$
n_i = u_0,\; u_1,\; \ldots,\; u_m = n_j
$$

such that

1. every two neighbouring vertices in the list are adjacent, that is, $u_{s-1} u_s \in E$ for every $s = 1, 2, \ldots, m$, and
2. all the vertices in the list are different.

In simple words, a path is a route from $n_i$ to $n_j$ that follows the lines of the graph and never visits the same dot twice. Its length is the number of edges it uses, written $|P|$ in the textbook. If no vertex repeats, then no edge can repeat either, so every path in the course's sense is also a path in the textbook's sense.

The textbook adds two related words. A path that starts and ends at the same vertex is a cycle (Definition 1.2.14). The simple path on $n$ vertices is written $P_n$. The distance between two vertices is the length of the shortest path between them, or $+\infty$ when no path exists (Definition 1.2.16).

Four ideas that are easy to confuse.

- An edge is a path of length 1. It joins two vertices directly.
- A walk (Definition 2) may revisit vertices and reuse edges. Every path is a walk. Not every walk is a path.
- A path in the textbook's sense (Definition 4a) may revisit a vertex but not an edge. A simple path, the course's path (Definition 4), does neither.
- Connectivity of the graph (Definition 3) is a statement about all pairs of vertices at once. A path is a statement about one pair.

## 6. Worked example

Use the graph from the lecture. It has three vertices $n_1, n_2, n_3$ and two edges, $e_{12}$ and $e_{23}$. Drawn as dots in a row:

```
n1 ---- n2 ---- n3
```

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

**A graph that is not connected.** Remove the edge $e_{23}$. The new matrix and its square are

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

The entries $S'_{13}$ and $S'_{23}$ are zero. No path reaches $n_3$, so this graph is not connected. It has two connectivity components: one containing $n_1$ and $n_2$, and one containing only $n_3$.

## 7. Conclusion

The adjacency matrix $A$ stores a graph as a table of zeros and ones, where $A_{ij} = 1$ exactly when vertices $n_i$ and $n_j$ are adjacent. The entry $(A^k)_{ij}$ of the $k$-th power counts the walks of length $k$ from $n_i$ to $n_j$, where a walk may revisit vertices and reuse edges. A path, in the course's sense, is a walk that never revisits a vertex; the textbook calls this a simple path. Two vertices are joined by a path exactly when some power $A^k$ with $k \leq N - 1$ has a positive entry in their cell. The whole graph is connected exactly when every off-diagonal entry of $A + A^2 + \cdots + A^{N-1}$ is positive. Keeping the ideas apart, a direct edge, a walk, a path between two vertices, and connectivity of the whole graph, is the key to this topic.

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

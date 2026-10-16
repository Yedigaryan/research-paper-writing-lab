# The Adjacency Matrix, Its Powers, and the Connectivity of a Graph

## 1. Introduction

A graph is a picture made of dots and lines. The dots are called nodes. The lines are called edges. Graphs are used to describe things that are joined to each other, such as cities joined by roads or people joined by friendships.

A computer cannot look at a picture of dots and lines. It needs numbers. The adjacency matrix is a table of numbers that stores the same information as the picture. This paper explains the adjacency matrix and uses it to answer three questions.

1. What does the entry $(A^k)_{ij}$ of the $k$-th power of the adjacency matrix represent?
2. How can we tell whether a graph is connected?
3. What is a path between two nodes $n_i$ and $n_j$?

### Conventions and assumptions

Every symbol used in this paper is defined here or where it first appears.

- A graph is written $G = (V, E)$. The set $V$ holds the nodes and the set $E$ holds the edges. The lecture notes write the pair as $(G, V)$ and write $|G| = N$ for the number of nodes. The meaning is the same. This paper uses the letters $V$ and $E$ because they are the most common in textbooks.
- The graph has $N$ nodes, named $n_1, n_2, \ldots, n_N$. In symbols, $|V| = N$.
- The graph is undirected. An edge is a plain line with no arrow, and it can be travelled in both directions.
- The graph is simple. There is at most one edge between two nodes, and no edge joins a node to itself.
- The edge between $n_i$ and $n_j$ is written $e_{ij}$. Because the graph is undirected, $e_{ij}$ and $e_{ji}$ are the same edge.
- A path never visits the same node twice. This is the convention used in the course.

## 2. Definition of the adjacency matrix

A matrix is a table of numbers arranged in rows and columns. The adjacency matrix has one row and one column for every node. The number in row $i$ and column $j$ is written $A_{ij}$.

**Definition 1 (adjacency matrix).** The adjacency matrix of a graph $G = (V, E)$ with $N$ nodes is the $N \times N$ matrix $A$ whose entries are

$$
A_{ij} =
\begin{cases}
1, & \text{if } e_{ij} \in E \text{ (there is an edge between } n_i \text{ and } n_j), \\
0, & \text{if } e_{ij} \notin E \text{ (there is no such edge).}
\end{cases}
$$

In words, $A_{ij} = 1$ means "node $i$ and node $j$ are joined by one edge". Two nodes joined by one edge are called adjacent. So the matrix answers the question "are these two nodes adjacent?" for every pair of nodes at once.

Three facts follow from the definition for an undirected simple graph.

- The matrix is symmetric: $A_{ij} = A_{ji}$. The edge between $n_i$ and $n_j$ is the same edge as the edge between $n_j$ and $n_i$.
- The diagonal is zero: $A_{ii} = 0$. No node is joined to itself.
- Row $i$ lists the neighbours of $n_i$. The sum of row $i$ is the number of edges touching $n_i$. This number is called the degree of $n_i$.

Row $i$ of the matrix answers "who is $n_i$ joined to?". Column $j$ answers "who is joined to $n_j$?". In an undirected graph, these two questions have the same answer, which is another way of seeing that the matrix is symmetric.

## 3. Answer 1: the meaning of $(A^k)_{ij}$

### 3.1 Walks

First we need a word for a trip through the graph.

**Definition 2 (walk).** A walk of length $k$ from $n_i$ to $n_j$ is a list of $k + 1$ nodes

$$
n_i = n_{t_0},\; n_{t_1},\; n_{t_2},\; \ldots,\; n_{t_k} = n_j
$$

such that every two neighbouring nodes in the list are joined by an edge. That is, $e_{t_s t_{s+1}} \in E$ for every $s = 0, 1, \ldots, k - 1$.

A walk may visit the same node more than once. The length of a walk is the number of edges it travels along, counting repeats.

### 3.2 The statement

The $k$-th power of $A$ is the matrix $A^k = A \cdot A \cdots A$, with $k$ copies of $A$ multiplied together. Its entry in row $i$ and column $j$ is written $(A^k)_{ij}$.

**Theorem 1.** For every $k \geq 1$, the entry $(A^k)_{ij}$ equals the number of different walks of length $k$ from $n_i$ to $n_j$.

For $k = 1$ this is just Definition 1. A walk of length 1 from $n_i$ to $n_j$ is a single edge, and $A_{ij}$ is 1 when that edge exists and 0 when it does not.

### 3.3 Why the theorem is true

Look at $k = 2$ first. A walk of length 2 from $n_i$ to $n_j$ has one middle stop, call it $n_m$. The walk exists exactly when $n_i$ is joined to $n_m$ and $n_m$ is joined to $n_j$. To count all such walks, go through every possible middle stop $m = 1, 2, \ldots, N$ and count the ones where both edges exist.

The rule for multiplying a matrix by itself does exactly this count:

$$
(A^2)_{ij} = \sum_{m=1}^{N} A_{im} \, A_{mj} .
$$

Each term $A_{im} A_{mj}$ is 1 when both edges exist and 0 otherwise. Adding the terms counts the walks of length 2.

The same reasoning works for any $k$. A walk of length $k$ from $n_i$ to $n_j$ is a walk of length $k - 1$ from $n_i$ to some node $n_m$, followed by one edge from $n_m$ to $n_j$. Therefore

$$
(A^k)_{ij} = \sum_{m=1}^{N} (A^{k-1})_{im} \, A_{mj} ,
$$

which is the rule for computing $A^k = A^{k-1} \cdot A$. If $(A^{k-1})_{im}$ already counts walks of length $k - 1$, then the sum counts walks of length $k$. Starting from $k = 1$ and repeating this step proves the theorem for every $k$.

### 3.4 An important warning

Theorem 1 counts walks, not paths. A walk may go back and forth over the same edge or return to a node it has already visited. For example, in any graph with an edge between $n_1$ and $n_2$, the list $n_1, n_2, n_1$ is a walk of length 2 from $n_1$ back to $n_1$, so $(A^2)_{11} \geq 1$. It is not a path, because $n_1$ appears twice.

## 4. Answer 2: determining whether the graph is connected

The word "connected" is used for three different questions. They must be kept apart.

### 4.1 Are two nodes joined by a direct edge?

Look at the single entry $A_{ij}$. If $A_{ij} = 1$, the nodes are adjacent. If $A_{ij} = 0$, they are not. This is the smallest question.

### 4.2 Are two nodes joined by a path?

Two nodes can be joined by a path even when $A_{ij} = 0$, because the path may pass through other nodes. Theorem 1 gives a test.

**Theorem 2.** Let $i \neq j$. There is a path from $n_i$ to $n_j$ if and only if $(A^k)_{ij} > 0$ for at least one $k$ with $1 \leq k \leq N - 1$.

Why this is true, in two halves.

- If some $(A^k)_{ij} > 0$, then by Theorem 1 there is a walk from $n_i$ to $n_j$. If the walk visits some node twice, cut out the part of the walk between the two visits. The result is still a walk from $n_i$ to $n_j$, but shorter. Repeat until no node is visited twice. What remains is a path.
- If a path from $n_i$ to $n_j$ exists, it is also a walk of some length $m$, so $(A^m)_{ij} \geq 1$. A path never repeats a node, so it visits at most $N$ nodes and uses at most $N - 1$ edges. Hence $m \leq N - 1$, and powers beyond $N - 1$ are never needed.

### 4.3 Is the whole graph connected?

This is the question asked in the lecture.

**Definition 3 (connected graph).** A graph is connected if for every pair of nodes $n_i$ and $n_j$ there exists a path from $n_i$ to $n_j$.

Applying Theorem 2 to every pair at once gives a test that uses only the adjacency matrix.

**Theorem 3.** Form the matrix

$$
S = A + A^2 + A^3 + \cdots + A^{N-1} .
$$

The graph is connected if and only if every entry $S_{ij}$ with $i \neq j$ is greater than zero.

The entry $S_{ij}$ is the total number of walks from $n_i$ to $n_j$ of length at most $N - 1$. It is positive exactly when at least one such walk exists, which by Theorem 2 is exactly when a path exists. If this holds for every pair, the graph is connected by Definition 3. If some $S_{ij}$ is zero, no path joins $n_i$ to $n_j$, and the graph is not connected.

An equivalent form that is sometimes quicker to compute is to check that the matrix $(I + A)^{N-1}$ has no zero entries, where $I$ is the identity matrix. Adding $I$ lets a walk "pause" at a node, so this single power collects all walks of length at most $N - 1$.

In practice, for large graphs, connectivity is usually tested by exploring the graph from one node, visiting neighbours of neighbours until no new node is found, and checking whether every node was visited. This method is called breadth-first search or depth-first search. The matrix power method is the one that connects directly to Theorem 1.

## 5. Answer 3: definition of a path

**Definition 4 (path).** A path of length $m$ from $n_i$ to $n_j$ is a list of $m + 1$ nodes

$$
n_i = n_{t_0},\; n_{t_1},\; \ldots,\; n_{t_m} = n_j
$$

such that

1. every two neighbouring nodes in the list are joined by an edge, that is, $e_{t_s t_{s+1}} \in E$ for every $s = 0, 1, \ldots, m - 1$, and
2. all the nodes in the list are different.

In simple words, a path is a route from $n_i$ to $n_j$ that follows the lines of the graph and never visits the same dot twice. Its length is the number of edges it uses.

Three ideas that are easy to confuse.

- An edge is a path of length 1. It joins two nodes directly.
- A walk (Definition 2) is like a path but may revisit nodes. Every path is a walk. Not every walk is a path.
- Connectivity of the graph (Definition 3) is a statement about all pairs of nodes at once. A path is a statement about one pair.

## 6. Worked example

Use the graph from the lecture. It has three nodes $n_1, n_2, n_3$ and two edges, $e_{12}$ and $e_{23}$. Drawn as dots in a row:

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

Check row 2: it reads $1, 0, 1$, so $n_2$ is joined to $n_1$ and to $n_3$. The matrix is symmetric and the diagonal is zero, as expected.

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
- $(A^2)_{11} = 1$. The one walk of length 2 from $n_1$ to itself is $n_1, n_2, n_1$. It is a walk but not a path, because $n_1$ repeats.
- $(A^2)_{22} = 2$. The two walks are $n_2, n_1, n_2$ and $n_2, n_3, n_2$.

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

Every entry off the diagonal is positive, so the graph is connected. This agrees with the picture: $n_1$ reaches $n_2$ by an edge, $n_2$ reaches $n_3$ by an edge, and $n_1$ reaches $n_3$ by the path $n_1, n_2, n_3$.

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

The entries $S'_{13}$ and $S'_{23}$ are zero. No path reaches $n_3$, so this graph is not connected.

## 7. Conclusion

The adjacency matrix $A$ stores a graph as a table of zeros and ones, where $A_{ij} = 1$ exactly when nodes $n_i$ and $n_j$ are joined by an edge. The entry $(A^k)_{ij}$ of the $k$-th power counts the walks of length $k$ from $n_i$ to $n_j$, where a walk may revisit nodes. A path is a walk that never revisits a node. Two nodes are joined by a path exactly when some power $A^k$ with $k \leq N - 1$ has a positive entry in their cell. The whole graph is connected exactly when every off-diagonal entry of $A + A^2 + \cdots + A^{N-1}$ is positive. Keeping the three ideas apart, a direct edge, a path between two nodes, and connectivity of the whole graph, is the key to this topic.

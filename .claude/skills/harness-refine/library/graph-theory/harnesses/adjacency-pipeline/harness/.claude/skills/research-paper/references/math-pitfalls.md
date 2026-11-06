# Mathematical pitfalls to check before writing

Questions that change the mathematics and must be settled in Phase 2, with
the assumption to state if the user does not know.

## Graph theory

| Question | Why it matters | Default if unknown |
| --- | --- | --- |
| Directed or undirected? | Undirected gives a symmetric adjacency matrix and one notion of connected. Directed splits into strongly and weakly connected. A symmetric matrix on the board points to undirected. | Undirected, say so, add a note on directed graphs. |
| Simple graph or multigraph? | Loops and multiple edges change the entries of A and the degree rule. | Simple. |
| Does a path allow repeated vertices? | The course textbook's "path" (ճանապարհ) forbids repeated edges only; its "simple path" (պարզ ճանապարհ) forbids repeated vertices. English books call these trail and path. The count given by powers of A is always the walk count. | Path means no repeated vertices, and the paper says this is the book's simple path. |
| Which letters name the sets? | Boards sometimes write (G, V) with G for nodes and V for edges. Textbooks write G = (V, E). | Use V for nodes and E for edges and note the board's labels. |
| Is the question about A or about A^k? | A small mark above A can be a superscript k, a prime, or quotation marks. A_ij is 1 or 0. (A^k)_ij counts walks of length k. | If the user's text names one reading, take it and record the board's mark as an assumption. Otherwise ask. |
| Does "connected" mean two nodes or the whole graph? | Adjacent (direct edge), joined by a path, and the whole graph being connected are three different claims. | Answer all three and label them. |
| Is a walk of length 0 (a single vertex) allowed? | It decides whether A^0 = I counts walks, whether walk-to-path holds for u = v, and every path count on the diagonal. A textbook's definitions may not say it in words while its later usage assumes it; parallel modules left without a ruling settle it two ways. | Allowed, recorded in the brief as the paper's convention with the source passages that agree with it. |

## Facts that are easy to state wrongly

- (A^k)_ij is the number of walks of length exactly k from node i to node
  j. It is not the number of paths and not "1 if reachable".
- A path with no repeated nodes in a graph with N nodes has at most N - 1
  edges. So the connectivity test only needs powers A^1 to A^(N-1).
- Two distinct nodes are joined by a path if and only if some (A^k)_ij > 0
  with 1 <= k <= N - 1. Proof needs both directions: a walk can be cut down
  to a path, and a path is a walk.
- The whole graph is connected if and only if every off-diagonal entry of
  A + A^2 + ... + A^(N-1) is positive. Equivalent: (I + A)^(N-1) has no
  zero entry.
- In an undirected simple graph A is symmetric, its diagonal is zero, and
  row sums are degrees. (A^2)_ii equals the degree of node i.
- Diagrams drawn by hand often have stray arrowheads or a line that ends
  near the wrong node. Trust the matrix when the two disagree, and say so.
- A positive (A^k)_ij means a walk of length k exists, so a path of length
  at most k exists. It never occurs "when no path exists"; what can be
  missing is a path of exactly length k. This holds in plain-words
  paragraphs too.
- The sum test reads off-diagonal entries only: in a connected graph the
  diagonal of A + ... + A^(N-1) can be zero (N = 2, one edge), and
  (A^2)_ii, the degree, is zero for an isolated vertex. A plain-words
  sentence about "every cell" or "never zero" breaks one of these.
- If length 0 is allowed, each vertex has exactly one path to itself, the
  single vertex. Every comparison of a diagonal entry with a path count
  includes it; check each counterexample against the paper's own
  convention, not against the source's wording.
- A closed trail that is not a simple cycle splits at a repeated vertex
  into two closed trails of positive length with no common edge. In a
  simple graph each has at least 3 edges, so the whole has at least 6.
  Two triangles sharing a vertex is one instance, not the condition.
- The reason for (I + A)^(N-1): I and A commute, so it equals the sum of
  C(N-1, k) A^k for k = 0 to N-1, every coefficient at least 1. Off the
  diagonal it is positive exactly where A + ... + A^(N-1) is; the k = 0
  term only fills the diagonal. It is one matrix power instead of a sum,
  which still takes N - 2 products (about log2(N-1) by repeated squaring),
  not one.
- A single power is not a test. In the path n1, n2, n3 the power
  A^(N-1) = A^2 has (A^2)_12 = 0 although n1n2 is an edge: every edge joins
  {n1, n3} to {n2}, so walks from n1 to n2 have odd length. Give the zero
  entry first, then this reason in words.
- The walk-counting induction step starts from (A^(k+1))_ij = sum over r of
  (A^k)_ir A_rj and matches the r-th term with the walks whose last-but-one
  vertex is n_r. Say in words how a matrix product is formed before the
  first use of a power.

## Verification habits

- Compute every matrix power by hand or with a short script before
  writing it into the paper.
- For each matrix entry you interpret, list the walks it counts and check
  that the count matches.
- Include one failing example when presenting a test, so the reader sees
  what "not connected" looks like.

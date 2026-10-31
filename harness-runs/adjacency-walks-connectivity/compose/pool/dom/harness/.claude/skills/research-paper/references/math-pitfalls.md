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

## Verification habits

- Compute every matrix power by hand or with a short script before
  writing it into the paper.
- For each matrix entry you interpret, list the walks it counts and check
  that the count matches.
- Include one failing example when presenting a test, so the reader sees
  what "not connected" looks like.

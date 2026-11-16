# Reader findings

The technician reader's findings, as returned, ungraded. They are advisory; severity belongs to the evaluator alone.

## Round 1, 2026-11-16

Reader level 1. It read the PDF pages. Its summary matches the paper's three answers.

FINDINGS
F1 | comprehension | Abstract, p. 1: "the entry (A^k)_ij is the number of walks of length k from v_i to v_j (walks, not paths)" | "walk" is used before Definition 2.2 defines it, and "adjacency matrix A" is used before Definition 2.1. A reader has to infer both from context. | Add a short gloss at first use, e.g. "walk (a sequence of vertices with each consecutive pair adjacent; Definition 2.2)".

F2 | comprehension | Section 1, p. 1: "using only matrix multiplication and induction" | The proofs also use a counting/bijection argument (Theorem 3.1 proof, "these walks fall into N classes ... in one-to-one correspondence") and a path-shortening argument (Lemma 4.1). The stated method does not match what is done. | Replace with "using matrix multiplication, induction, and counting arguments".

F3 | comprehension | Definition 2.3, p. 2: "Bai's definition agrees, except that it also admits cycles [1, p. 1]" | "cycles" is never defined, so the reader cannot tell what the difference from Bai's definition is. | Add one clause defining a cycle (closed walk with no repeated vertex other than its endpoints) or drop the comparison.

F4 | comprehension | Definition 2.4, p. 2: "This is equivalent to Grinberg's definition by components [3, Proposition 2.9.10 and Definition 2.9.12, p. 42]." | The "definition by components" is never stated, so the claimed equivalence must be taken on faith. | State Grinberg's definition in one sentence, or say why the two agree (each component is pairwise joined by paths).

F5 | comprehension | Section 3, proof of Theorem 3.1, p. 2: "Write a walk of length k + 1 from v_i to v_j as w_0 w_1 ··· w_k w_{k+1}" and "W_r is the set of walks ..." | Vertex names switch among u/w (Def. 2.2), v_i (theorem), and w_t (proof). The set name W_r is later reused for a single walk "W = u_0 ··· u_k" in Lemma 4.1 (p. 3). | Rename the classes (e.g. C_r) and use one vertex-naming scheme throughout.

F6 | comprehension | Section 3, p. 3: "Nor is the entry '1 if v_j can be reached from v_i': (A^3)_12 = 2 counts the walks ..." | The sentence is a double negative that refers to a claim no one has made. It must be read more than once to parse. | Rewrite as: "A reachability reading (entry is 1 when v_j is reachable from v_i) is also wrong: (A^3)_12 = 2 counts the walks ...".

F7 | comprehension | Lemma 4.1 proof, p. 3: "Remove the vertices at positions s+1,...,t, that is, the two equal positions together with the second copy" | The phrase says the two equal positions are removed, but position s is kept. The sentence is muddled and was read more than once. | Replace with: "Delete the vertices at positions s+1, ..., t; this removes the second copy u_t of the repeated vertex and everything between the two copies."

F8 | comprehension | Lemma 4.1 proof, p. 3: "By strong induction on k: for a walk of length k we assume the statement for all walks of smaller length." | Why strong (rather than ordinary) induction is needed is not said. The reason is that W' can have length k-(t-s), which may be less than k-1. | Add: "(strong induction, because W' may be shorter than k-1)".

F9 | comprehension | Lemma 4.2 proof (⇒), p. 3: "As i ≠ j, k ≥ 1." | The reason a path between different vertices has length at least 1 is not given in the sentence. It depends on Definition 2.3. | Add "(a length-0 path has a single vertex, so it cannot join different vertices)".

F10 | comprehension | Section 4, paragraph before Lemma 4.1, p. 3: "the second combines the walk-counting theorem with the bound on the length of a path, which Grinberg states in Section 2.9.4 [3, p. 40]." | The "bound" is never stated in the paper. The reader only meets it later, as the k ≤ N-1 step inside the Lemma 4.2 proof. | State the bound in this paragraph: "a path has at most N-1 edges, since it has at most N distinct vertices."

F11 | comprehension | Theorem 4.3 remark, p. 3: "For N = 1 there is no pair of different vertices and the graph is connected. The theorem is Theorem 2 of Paramadevan and Sotheeswaran [5, p. 17], whose proof does not pass through lemma 4.1." | It is unclear whether "the theorem" means Theorem 4.3 or only the N = 1 case. The reader cannot see why the proof route matters. This also sits oddly with the abstract's "each statement is proved in full". | Say directly: "Theorem 4.3 is stated for N >= 2. The N = 1 case is trivial; the sum test in [5, Theorem 2] is cited, not proved here."

F12 | comprehension | Section 4, p. 4, first line: "The test can also be written as '(I + A)^{N-1} has no zero entry' [2, Proposition 3, p. 2][1, Theorem 2, p. 1]." | The equivalence is asserted with citations only. It requires the binomial expansion of (I+A)^{N-1}, that I and A commute, and that the diagonal is positive because of the I term. None of this is shown. | Add one line: "(I+A)^{N-1} = sum_k C(N-1,k) A^k; its diagonal is positive from the I term, so no zero entry is equivalent to the off-diagonal sums being positive."

F13 | comprehension | Section 5, p. 4, heading "The sum must reach A^{N-1}" and sentence "A sum stopped at A^2 would have (1,4) entry 0 and call this connected graph disconnected." | "call this ... disconnected" is ambiguous, since it could read as the paper's own claim. The heading states a rule whose reason (the N-1 cutoff from Lemma 4.2) is given only in an earlier paragraph, which is not cross-referenced here. | Rewrite: "A sum stopped at A^2 would have (1,4) entry 0 and so wrongly report G_3 as disconnected; the path v1v2v3v4 has length 3 (see Lemma 4.2)."

F14 | comprehension | Section 5, Limits, p. 4: "a positive entry of A^k means a walk of length exactly k exists, hence a path of length at most k, not a path of length exactly k" | The "hence" step relies on Lemma 4.1, which is not named. The sentence has several embedded clauses and had to be read more than once. | Add "(Lemma 4.1)" after "hence" and split into two sentences.

F15 | comprehension | Section 5, Limits, p. 4: "The test uses A alone" | A reader could take this to mean that only the entries of A are used. The test actually uses A^2 through A^{N-1}, which are computed from A. | Replace with "The test takes only A as input".

F16 | comprehension | Introduction, p. 1: "every entry off the main diagonal of A + A^2 + ··· + A^{N-1} is positive" and the abstract's "off-diagonal entry" | "main diagonal" and "off-diagonal" are used before any definition of diagonal entries. Definition 2.1 defines only A_ij. | Add to Definition 2.1: "The diagonal entries are A_ii; the others are off-diagonal."

READER SUMMARY
The paper asks how to decide from a graph's adjacency matrix A whether the graph is connected, and how the entries of powers of A relate to walks and paths. It answers three questions. First, the (i,j) entry of A^k counts walks of length k from v_i to v_j, with repeated vertices allowed, so it does not count paths. Second, a path is a walk with no repeated vertex. Third, for graphs with N >= 2 vertices, the graph is connected exactly when every off-diagonal entry of A + A^2 + ... + A^{N-1} is positive. The proof uses the walk-counting result, a lemma that every walk contains a path of length at most its own length, and the bound that a path has at most N-1 edges. Section 5 checks the test by hand on three small graphs (a connected 3-vertex path, a 3-vertex graph with an isolated vertex, and a 4-vertex path), and lists the limits: only zero versus nonzero matters, walk counts are not path counts, and the diagonal is excluded on purpose.

### Author's response to the round 1 reader findings

As reported by the author after the revision; the detail is in the per-finding log of `self-evaluation.md`.

**Reader findings**
- **Changed:** F1 (abstract gloss), F2, F3 (moot after the Bai cut), F5, F6, F7, F8, F9, F10, F11, F12 (one line with the binomial expansion), F13, F14, F15, F16.
- **Partly met:**
  - F4: the paper now says the two definitions agree by Proposition 2.9.10, but does not restate Grinberg's definition, which needs components.
  - F5: the walk class is renamed C_r, but the u/w/v/w_t vertex naming stays, since the proof introduces w_t.
- **Left as is:** F1's "adjacency matrix" is not glossed in the abstract.

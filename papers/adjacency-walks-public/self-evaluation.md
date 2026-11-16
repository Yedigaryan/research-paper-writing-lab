# Self-evaluation: adjacency-walks-public

Build: `build.sh` exit 0, 5 pages against a budget of 5. `check_citations.py`, `check_claims.py`, `inspect_pdf.py`: 0 errors, 0 warnings. Grep of the .tex files for board, lecture, course, assignment, textbook, user, script, Petrosyan, own convention, n_1: no hits. Analogies: no, so no plain-words paragraphs.

Decisions: the scaffold's five sections and appendix were replaced by five sections (introduction, definitions, counting, connectivity, example) and no appendix. The reader-facing fixes from the brief were applied: the walk classes W_r are named before the correspondence; the last vertex is w_{k+1} and the vertex before it w_k; the powers of the three-vertex graph are printed before the warning, and (A^4)_22 was dropped; each lemma says which source states it; the cut in Lemma 4.1 says which vertices are removed and that the hypothesis is applied to the shorter walk; "counts the walk, which is also a path" in the example; the diagonal is stated as left out on purpose; the four-vertex example prints A, A^2, A^3 and the walk; N >= 2 is in the abstract and the theorem; there is one definition of path, with "path between two vertices" in the same definition, and Q2's answer points to it. Optional objective 1 (the (I+A)^{N-1} form) is one sentence after the sum test. Optional objective 2 (sources wording entries as paths) was left out: only Paramadevan does so and the paper already says why.

## 1 Introduction
Purpose: state Q1 to Q3 with answers, say why it matters, who states the results, what the support is. Claims: walk counting appears in Galway, Gotti, Bai (C31, C34, C38); walk-to-path lemma in Grinberg (C48); sum test in Paramadevan (C42); sources sketch or omit steps (C41, C43). Answer to Q3 follows from Theorem 4.3. Nothing unjustified.

## 2 Definitions
Purpose: setting, adjacency matrix, walk, path (and path between two vertices), connected. Claims: adjacency matrix 0/1, symmetric, zero diagonal (C33); walk with k >= 0 and path as distinct-vertex walk (C47); Bai's path agrees except for cycles (C39); Paramadevan leaves path undefined (C43); connectivity by paths equals Grinberg's one-component definition (C50, p5); simple-graph setting of Grinberg Section 2.9 (C47, C50). Entries of A^k non-negative integers: elementary, from the definition of products.

## 3 Q1: walk counting
Purpose: Theorem 3.1 with full induction proof, and the example that entries do not count paths. Claims: statement in Galway, Gotti, Bai (C31, C34, C38, m1-12); the proof is derived (m1-12); the example matrices and walk lists (p1), checked by script in `scripts/public_examples.py`. Conclusion: (A^2)_11 = 1 is not a path count, from p1 and Definition 2.3 (only path from v_1 to itself has length 0). Nothing unjustified.

## 4 Q3: the connectivity test
Purpose: Lemma 4.1, Lemma 4.2, Theorem 4.3 (all proved), the (I+A)^{N-1} sentence. Claims: Lemma 4.1 is Grinberg Corollary 2.9.7 (C48); path length at most N-1 (C49, m2-3); Lemma 4.2 derived (p4); sum test is Paramadevan Theorem 2 (C42), proof via Lemmas (m3-6); the (I+A)^{N-1} form is Gotti Proposition 3 and Bai Theorem 2 (C36, C40); the equivalence of the two forms is not proved in the paper (m3-7 holds the derivation in the evidence file only), so the sentence says only that the test "can also be written" that way, with the sources. Conclusion: Theorem 4.3 follows from Lemma 4.2 and Definition 2.4.

## 5 Examples and limits
Purpose: connected example G_1, disconnected G_2, the A^{N-1} example G_3, limits. Claims: matrices and walks are p1, p2, p3 (script). Conclusions: G_1 connected, G_2 not, G_3 needs A^3, each from Theorem 4.3 and printed matrices (B for G_3 is printed only partly in rows; all rows listed in the text). Limits: only zero/non-zero is read (Lemma 4.2); diagonal left out by design (N = 2 example, derivation by inspection); scope of the proof.

## Unverified claims
None. Evidence file: 5 sources, 35 claims (30 base, 5 new in `evidence/modules/author.json`: p1 to p5). Claim texts of the base file still write vertices as n_i; this is an internal label difference and the paper uses v_i throughout.

## Could not justify
Nothing. Note for the orchestrator: the page count is exactly the budget of 5; the last page is a part page.

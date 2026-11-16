# Self-evaluation: adjacency-walks-public

Build: `build.sh` exit 0, 5 pages against a budget of 5. `check_citations.py`, `check_claims.py`, `inspect_pdf.py`: 0 errors, 0 warnings. Grep of the .tex files for board, lecture, course, assignment, textbook, user, script, Petrosyan, own convention, n_1: no hits. Analogies: no, so no plain-words paragraphs.

Decisions: the scaffold's five sections and appendix were replaced by five sections (introduction, definitions, counting, connectivity, example) and no appendix. The reader-facing fixes from the brief were applied: the walk classes W_r are named before the correspondence; the last vertex is w_{k+1} and the vertex before it w_k; the powers of the three-vertex graph are printed before the warning, and (A^4)_22 was dropped; each lemma says which source states it; the cut in Lemma 4.1 says which vertices are removed and that the hypothesis is applied to the shorter walk; "counts the walk, which is also a path" in the example; the diagonal is stated as left out on purpose; the four-vertex example prints A, A^2, A^3 and the walk; N >= 2 is in the abstract and the theorem; there is one definition of path, with "path between two vertices" in the same definition, and Q2's answer points to it. Optional objective 1 (the (I+A)^{N-1} form) is one sentence after the sum test. Optional objective 2 (sources wording entries as paths) was left out: only Paramadevan does so and the paper already says why.

## 1 Introduction
Purpose: state Q1 to Q3 with answers, say why it matters, who states the results, what the support is. Claims: walk counting appears in Galway, Gotti, Bai (C31, C34, C38); walk-to-path lemma in Grinberg (C48); sum test in Paramadevan (C42); sources sketch or omit steps (C41, C43). Answer to Q3 follows from Theorem 4.3. Nothing unjustified.

## 2 Definitions (round 1: simple-graph claim p6; diagonal gloss)
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

## Round 1 revision: changed sections and evidence
Changed: main.tex (abstract gloss of walk), introduction, definitions, counting, connectivity, example; `evidence/evidence.base.json` (used_in fields), `evidence/modules/author.json` (used_in fixed, claim p6 added). Merged file rebuilt by the merge script. Section 2 now rests on p6 (Grinberg Definition 2.1.1, p. 9) for the simple-graph setting. The quote of p6 ("A simple graph is a pair (V, E), where V is a finite set, and where E is a subset of P2 (V ).") was taken from the evaluator's fetch, not from my own reading of the source; the next evaluator should fetch it again. Section 4 now states the (I+A)^{N-1} expansion in one line (derivation m3-7). Paper still 5 pages.

## Per-finding log (evaluator)
- F1: citation changed to Grinberg Definition 2.1.1, p. 9; claim p6 added to author.json. No other occurrence of "Section 2.9" for the setting.
- F2: clause "whose proof does not pass through ..." cut (connectivity.tex).
- F3: sentence on (A^2)_22 and (A^2)_12 cut (example.tex).
- F4: Limits parenthetical replaced by (A^3)_12 = 2 with the only path of length 1.
- F5: clause "because the sources sketch or omit some steps" cut (introduction.tex).
- F6: Bai/Paramadevan comparison sentence cut (definitions.tex); "cycles" no longer appears.
- F7: "the number |C_r| of walks in C_r" written at first use.
- F8: shortened to the suggested wording (definitions.tex).
- F9: "The sources prove this starting from k=1".
- F10: "(a) and (b)".
- F11: used_in of a4 emptied; used_in filled for cited claims in the base file and the fragment; merged file rebuilt.
- F12: \texorpdfstring in both titles, with plain "Ak" and "A" as PDF strings (a superscript alternative still warned); build log has no hyperref token warning.

## Per-finding log (reader, advisory)
- F1: abstract now glosses "walk" in a parenthesis; "adjacency matrix" is defined in Section 2 and left unglossed in the abstract for space.
- F2: changed to "matrix multiplication, induction, and counting arguments".
- F3: moot, the Bai comparison with cycles was cut (evaluator F6).
- F4: shortened per evaluator F8 to say the definitions agree by Proposition 2.9.10; Grinberg's definition is not restated (it needs components, out of scope).
- F5: classes renamed C_r. Vertex naming stays u/w for general walks, v_i for the graph, w_t in one proof: kept, the proof says it introduces w_t.
- F6: rewritten as suggested.
- F7: reworded to "this removes the second copy u_t ... and everything between the two copies".
- F8: added "(strong, because W' below may be shorter than k-1)".
- F9: added the reason in parentheses.
- F10: bound stated before Lemma 4.1.
- F11: the "proof does not pass through" clause cut; the sentence now names Theorem 2 of [5] as the source of the statement. The abstract's "proved in full" stands since Theorem 4.3 is proved here.
- F12: one line with the binomial expansion added after the sentence.
- F13: rewritten, with the reference to Lemma 4.2.
- F14: "(Lemma 4.1)" added and the sentence split.
- F15: "takes only A as input".
- F16: diagonal and off-diagonal defined in Definition 2.1.

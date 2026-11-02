# Self-evaluation (round 1 draft)

Build status: `build.sh` compiles cleanly (29 pages); two overfull boxes of 2 and 8 points remain (a textbook example line and one bibliography line). No claim is `unverified`. Claims marked `qualified` in the evidence file and disclosed in the text: C24, C29, C36, m1-9, m2-8, m2-15, m3-11. Evidence changes made by the author: one new claim `author-1` (textbook Definition 1.2.1 and Theorem 1.2.1, printed p. 16, read from the page image) in `evidence/modules/author.json`; the `derivation` pointers of C7, C10, C35, C37, m1-1 to m1-7, m2-9 to m2-14, m2-16, m3-3 to m3-10 were rewritten in their owning files to the labels and numbers of this draft (they pointed at an earlier layout); merged file rebuilt, `check_evidence_rebuild.py` reports 0 differences.

Notation in this file: "claim X" is an evidence-file id; the paper itself never prints ids.

## sections/introduction.tex: Introduction

Purpose: state the three questions and where each came from (board: Q1, Q2 and the definition of connected; assignment text: Q3, the reading of the mark as k, the setting, the meaning of "path"), report the board mismatch, fix the village story and the notation, summarize the answers, give the organization.

Claims and support:
- Board text: questions, problem, definition of connected, matrix, drawing with three lines and arrowhead: claims C25, C27, C28 (photos).
- The mark above A is read as k: claim C29 (qualified), m1-9 (qualified); disclosed as an interpretation.
- Board notation (G,V), e_ij in V, n_i, N against textbook G=(V,E), v_i, n: claims C25, C26, C1.
- Course meaning of "path" comes from the assignment text, the board does not say: claim C24 (qualified).
- Matrix, not drawing, defines the example: brief assumption, claim C28; arrowhead treated as stray because the matrix is symmetric.
- Textbook has no walk-counting theorem and no matrix test (full-text search of the whole book for the adjacency matrix; not all pages read): claim m3-11 (qualified); the paper states that qualification.
- Answer statements summarized: Q1 claim C6 (four sources) with the paper's own proof m1-3; walks not paths claims C8, C10, m1-6; one published statement says paths, wrong as written: claim C11; Q2 statements C34, C36 (sources) with own proof C35, C37; Q3 claims C16, m2-8, C24.

Conclusions and premises: none beyond the summaries; each is proved in the sections cited.

Not justified: nothing. Note that "assignment text" stands for the user's text recorded in the brief (not a file).

## sections/background.tex: Background

Purpose: the vocabulary in the textbook's order with textbook numbers, each definition followed by a remark, an example, and a non-example, each preceded by a plain-words paragraph.

Claims and support:
- Graph (Def 1.1.1): C1. Adjacent (1.1.4), adjacency matrix (after 1.1.6, p. 11): C2. Degree (1.2.1) and Euler's theorem (1.2.1): author-1.
- Proposition on properties of A: items 1 to 3 claim C3, item 6 claim C4, item 4 derived (m1-1; Paramadevan version C5), item 5 from Euler (author-1) and m1-1. Proof written in the text.
- Walk (1.2.10), length, repeats allowed: C12, C13. Walk equals vertex sequence in a simple graph: m1-2 (derived). Length 0 allowed: m2-15 (qualified, interpretation). Examples and non-examples from the textbook: m2-1.
- Closed walk (1.2.11): C14. Trail (1.2.12, textbook "path"): C15; English trail: C21; examples m2-1.
- Path (1.2.13, "simple path"): C16; English path: C21, C23; course convention: C24 (qualified); examples m2-2. Path implies trail: m2-10 (derived; Grinberg leaves it as an exercise: m2-5).
- Cycle, simple cycle (1.2.14, 1.2.15): C17, m2-2; English cycle: C22; B has no cycle and the triangle has a simple cycle: m2-14 (script); length-0 closed trail not a cycle: m2-15 (qualified).
- Distance (1.2.16) and its three properties: C18, m2-4; the properties are proved in Appendix A.1 (m2-16); equality of shortest walk, trail, path: m2-12; B distances: m2-13.
- Lemma (1.2.1 with length bound): C19 (textbook, u different from v), C20 (Grinberg, any u, v, bound), m2-9 (derived, proof in the text), textbook proof method: m2-3. Corollary on path length at most N-1: C33, m2-11, m2-6.
- Connected (2.1.1): C30, board C25; remark that the reading of "path" does not matter and that u = v is trivially satisfied: C32, C19, C20, derived; the u = v reading is marked an interpretation. Components and one-component remark (2.1.1): m3-1, C31; textbook examples and non-example: m3-2.
- Matrix product and powers (Definition 2.13, with an example and a non-example): standard definition, no claim; the example is the entry (A^2)_11 = 1 of the board matrix (script).

Conclusions and premises: Proposition on path implies trail (premise: edges of a simple graph are fixed by their ends); Lemma (premise: strong induction, the cut W' is a walk); Corollary (premise: path lists k+1 distinct vertices out of N).

Not justified: the textbook's number for the definition of A(G) does not exist (stated). Graph H uses seven edges that the textbook's examples use; the paper does not claim these are all the edges of the textbook's figure. Textbook examples are cited by page only.

## sections/answer1_walks.tex: Question 1

Purpose: answer Q1 with the walk-counting theorem, full induction proof, corollary, the diagonal of A^2, and the warning that walks are not paths.

Claims and support:
- Theorem (A^k)_ij counts walks of length k: C6 (Quinlan Theorem 1.1.3, Grinberg Theorem 4.5.10, Lehman et al. Corollary 9.3.3, Bai Theorem 1); proof route C7; the proof as written m1-3 (derived); finite cross-check m1-4.
- Textbook has no such theorem: m3-11 (qualified).
- Where hypotheses are used: m1-8 (interpretation, labelled so in the text).
- Corollary (entries are non-negative integers, positive iff a walk of exactly that length exists, A^k symmetric): m1-7 (derived).
- (A^2)_ii = degree: C9 (Quinlan remark), derived in the text; trace of A^2 = 2|E|.
- Walks are not paths: C8, C10, m1-6 (counterexamples (A^2)_11 = 1 and (A^3)_12 = 2, Table 2 from script); A^(k+2) = 2A^k for k = 1 to 5 from the saved script output.
- Paramadevan and Sotheeswaran Theorem 1 says paths and is wrong as written; their property 7 says walks: C11.

Conclusions and premises: Theorem follows from the definition of the product and the bijection between walks of length k ending at n_j via n_r and walks of length k-1 ending at n_r when n_r, n_j are adjacent. Proposition 3.6 follows from the explicit walks in B.

Not justified: nothing. The statement that A^(k+2) = 2A^k for k up to 5 rests on the saved output of the m1 script, not re-run by `generate_paper_numbers.py`, which asserts only A^3 = 2A.

## sections/answer2_connectivity.tex: Question 2

Purpose: answer Q2 with the sum test and the I + A form, the proofs, the components corollary, the sharpness of N - 1, and breadth-first search.

Claims and support:
- Statement of the test: C34 (Paramadevan and Sotheeswaran Theorem 2, MathWorld), C36 (Bai Theorem 2, qualified); proof is the paper's own: C35 (derived), C37 (derived); both web proofs say paths and omit the walk-to-path step: m3-12.
- Proposition 4.5 (one pair at a time) premises: Theorem 3.1 (C6), Lemma 2.47 (C19, C20, m2-9), Corollary 2.48 (C33), Proposition 2.38 (m2-10), Corollary 3.5 (m1-7).
- Proposition 4.6 (I + A, any m >= N - 1, diagonal at least 1): C37, m3-9 (derived, script check on all graphs with N up to 6: m3-8).
- Corollary 4.13 (components from S): m3-5 (derived).
- Distance as the smallest k: C38 (two sources), derived from Corollary 3.5 and Proposition A.1 (m2-12).
- Edge cases N = 1, 2 and the diagonal: m3-3 (derived).
- N - 1 cannot be lowered, path example, Table 3: m3-4 (derived, script).
- Breadth-first search statement: C39, m3-13 (Schost slides); agreement with the matrix test: m3-8 (check, not proof).

Conclusions and premises: Theorem 4.7 follows from Propositions 4.5 and 4.6 and the fact that pairs with u = v are always satisfied (Remark 2.50).

Not justified: nothing. The procedure (Definition 4.9) is the paper's own restatement of the test and carries no new claim.

## sections/answer3_path.tex: Question 3

Purpose: answer Q3 by pointing to the numbered definition of path, then add only the comparison of conventions and the proof that the readings agree.

Claims and support:
- Definition of a path between n_i and n_j: m2-8 (interpretation, qualified), C16, C24 (qualified); textbook Definition 1.2.13 and English usage: C16, C21.
- Table 4 (naming conventions): m2-7, C12 to C17, C21, C22; Wikipedia remark about the textbook's pattern: C23.
- Proposition 5.1 (walk, trail, path existence are equivalent): derived from Lemma 2.47 (m2-9) and Proposition 2.38 (m2-10); Grinberg Proposition 2.9.10 covers walks and paths only: C32.
- Example 5.2: B has one path between n_1 and n_3; every trail of length up to 4 in B is a path: m2-13, m2-14 (script); trail that is not a path in the textbook graph: m2-2.

Conclusions and premises: the choice of reading does not change connectivity, from Proposition 5.1.

Not justified: nothing. Whether the course uses "cycle" in the textbook's or the English sense is not stated by any input; the paper says so.

## sections/example.tex: Worked examples

Purpose: the three-vertex worked examples with every matrix written out, the table of walks, trails, paths, closed walks, and the exhaustive comparison with breadth-first search.

Claims and support:
- Powers of the board matrix, explicit walk lists, hand sums, A^3 = 2A, diagonal of A^2: m1-5, m1-6, C9 (all by script; matrices read from `figures/matrices.tex` generated by `generate_paper_numbers.py`).
- Table 5 (walks, trails, paths, closed walks by length): m2-13, m2-14; the paper adds that the counts of walks equal the entry sums of A^k (4, 6, 8, 12) and the closed counts equal traces (checked against the matrices).
- Connected example: m3-6. Disconnected example: m3-7. Both examples include the (I + A)^2 matrices and the BFS reading.
- Exhaustive comparison, Table 6: m3-8 (counts from the saved m3 output); N - 2 powers fail on N!/2 graphs: m3-4 (derived; the column values 1, 3, 12, 60, 360 equal N!/2).

Conclusions and premises: the test gives "connected" for B and "not connected" for D, with components {1,2} and {3}, from Theorem 4.7 and Corollary 4.13 and the matrices shown.

Not justified: nothing. The board drawing as a graph (triangle) is not run through the test.

## sections/discussion.tex: Discussion

Purpose: limits of the results, the conventions chosen, competing explanations, cost, and the status of the computer checks.

Claims and support:
- Scope: finite simple undirected (C1); loops and multigraphs are an interpretation of how the proof extends (m1-8, with the digraph and multidigraph versions in C6); directed graphs for the test not examined.
- Conventions: mark above A (C29, m1-9, qualified); drawing against matrix (C28); path word (C24, qualified); length 0 (m2-15, qualified).
- No claim about the lecturer's intended answer to Q2.
- Competing explanations: "paths" in two web sources: C11, m3-12; BFS: C39.
- Cost remark: m3-10 (estimate): (N - 2)N^3 = 98,000,000 and 7 squarings costing 7,000,000 for N = 100, N^2 = 10,000 entries read by BFS from the matrix, largest entry 38,742,049 of A^9 for K_10, all from the m3 script output (also reproduced by `generate_paper_numbers.py`); the paper writes N - 2 products, not the N - 1 of claim C39, because reaching A^(N-1) from A takes N - 2 products. BFS bound O(n + m) for adjacency lists: C39, m3-13.
- Checks that are not proofs: m1-4, m3-8.

Conclusions and premises: the matrix test is not faster than BFS by the operation counts, an estimate under the school-method assumption.

Not justified: the sentence that only the positions of the positive entries matter, so a version keeping only positivity gives the same answer, is a short argument written inline (entries are non-negative) and is not in the evidence file or checked by script. Claim C39's wording "N - 1 matrix products" disagrees with the count used here; the paper follows m3-10.

## sections/conclusion.tex: Conclusion

Purpose: the direct answers to Q1, Q2, Q3 and what stays open.

Claims and support: C6, m1-3, C8, m1-6 (Q1); C34, C35, C36, C37, m3-4, m3-6, m3-7, C39, m3-10 (Q2); C16, C15, C24, m2-8, m2-10, m2-12 (Q3); open items: C29, C28, m3-11.

Conclusions and premises: each follows from the theorem or proposition it cites.

Not justified: nothing. The statement that breadth-first search "needs far fewer operations" is the estimate of m3-10 and is worded as such.

## appendices/derivations.tex: Secondary derivations

Purpose: proofs of the distance statements used in the body (shortest walk, trail, path have equal length; the three distance properties) and the list of finite computer checks.

Claims and support: m2-12 (Proposition A.1, premises Lemma 2.47 and Proposition 2.38; Grinberg remark: m2-6), m2-16 (Proposition A.2, premise Proposition A.1), C18 and m2-4 (textbook statements); checks: m1-4, m3-8, m2-13, m2-14.

Conclusions and premises: Definition 1.2.16 does not depend on reading "path" as trail or path.

Not justified: the third check bullet (the walk, trail, path script) is described qualitatively ("saved output records no failure") without the counts, because the counts are not in the evidence file; the output file `appendices/scripts/m2_walks_output.txt` carries them.

## appendices/course-terms.tex: Textbook locators and the board's notation

Purpose: table of textbook numbers and printed pages, and the notation table (board, textbook, this paper).

Claims and support: C1, C2, C12 to C19, C30, C31, m3-1, author-1 (numbers and pages); C25, C26 (board notation).

Not justified: the page range 21 to 22 for the walk definition and length (definition on p. 21, length remark on p. 22) follows the evidence locators; the page of Remark 2.1.1 (p. 49) follows C31.

## appendices/photographs.tex: The board photographs

Purpose: transcription of the board, clear versus unclear marks, drawing against matrix edge by edge.

Claims and support: C25, C26, C27, C28, C29 (qualified). The Armenian "if" and the unreadable scratched mark under vertex 1 are reported as observed in the photographs and recorded in the repository's source notes (`graph-sources.md`), which the author checked against both photographs: the first photograph was viewed by the author; the second was not re-viewed in this round.

Not justified: the transcription of the mark on each side of the second A (quotation-mark look) rests on viewing photograph 1 only.

## appendices/reproducibility.tex: Sources read and how to rerun the computations

Purpose: what was read of each source, the list of scripts with run instructions.

Claims and support: source access notes in the evidence file (textbook partial: printed pp. 9-12, 16, 21-23, 48-49; Quinlan full; Grinberg, Bai, Schost, Lehman et al. partial or as recorded); m3-11 for the full-text search statement; scripts `m1_walks.py`, `m2_walks.py`, `m3_connectivity.py`, `generate_paper_numbers.py` in `appendices/scripts/` with saved outputs.

Not justified: the statement that Lehman et al., Paramadevan and Sotheeswaran, MathWorld, and Wikipedia were read "in the parts that carry the statements cited" follows the research record (full access status in the evidence file for these) and was not re-read by the author.

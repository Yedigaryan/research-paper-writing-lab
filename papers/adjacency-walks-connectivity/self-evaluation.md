# Self evaluation: Walks, Paths and Connectivity from the Adjacency Matrix

Author notes. All 77 evidence claims were left unchanged in content (only derivation locators in the base and module fragments were updated to the real section, table and label numbers, and the merged file was rebuilt with `merge_evidence.py`). No claim was added, so `evidence/modules/author.json` does not exist. Unverified claims in the text: none (0 in the evidence file). Qualified claims used and disclosed in the text: C24, C29, m1-9, m2-8, m2-15, C36, m3-11. Every number in the paper is produced by a script in `appendices/scripts/`.

## sections/introduction.tex: Introduction

Purpose: state the three questions and where each came from, fix the village story, preview the answers, fix assumptions, notation and the kinds of statement, and give the organization.

Claims and support:
- The board states the problem, question 1 and question 2 and a definition of connected: C25, C27 (whiteboard1, whiteboard2).
- The mark above A is not clearly k; reading it as k is an interpretation: C29, m1-9 (qualified).
- Q3 comes from the assignment text, not from the board: brief section 1; no evidence claim, so stated as the assignment's, not cited.
- Board notation (G,V), e_ij in V, |G| = N, n_i against the textbook's G = (V,E), v_i: C25, C26.
- Drawing shows 1-2 with arrowhead, 1-3, 2-3; matrix encodes only 1-2 and 2-3; the matrix is the example: C28.
- Textbook graphs are finite, simple, undirected: C1.
- Textbook "path" (1.2.12) allows repeated vertices, "simple path" (1.2.13) does not; English texts differ: C15, C16, C21, C23; course reading from assignment text: C24 (qualified).
- Walk-counting statement in standard notes: C6; the web note that says "paths": C11; test statements in a note and lecture notes with loose proofs: C34, C36, m3-12.
- Textbook has no walk-counting theorem and no matrix test in the pages read; full-book search found none; qualified: m3-11.

Conclusions and premises: "both results are proved here" follows from m3-11 (absence in the textbook, qualified) and C34/C36/m3-12 (sources prove loosely).

Not justified: the statement that the course meaning of "path" is "no repeated vertex" rests on the assignment text only (C24, qualified), as the paper says.

## sections/background.tex: Background: graphs, walks, and paths

Purpose: textbook-order prerequisites (graph, adjacent, degree, adjacency matrix, walk, closed walk, trail, path, cycle, simple cycle, naming table, distance, walk-contains-path lemma, length bound), each with plain words, remark, example, non-example.

Claims and support:
- Definition of graph, adjacent, adjacency matrix and its properties 1-3, 6: C1, C2, C3, C4. Row sums equal degrees and sum of entries 2|E|: m1-1 (derived; source with loops C5). Board writes the matrix rule with e_ij in V: C26.
- Walk, length, repeats allowed: C12, C13. Walk is its vertex list: m1-2 (derived). Length 0 allowed: m2-15 (qualified; textbook property d(u,u) = 0 from m2-4, Grinberg example in m2-5).
- Textbook examples for walk, trail, path, simple cycle: m2-1, m2-2. Closed walk: C14. Trail: C15, C21. Path: C16, C21. Distinct vertices give distinct edges: m2-10 (derived; Grinberg exercise in m2-5). Cycle and simple cycle: C17, C22. Board graph has no cycle, trails equal paths in it, triangle has a simple cycle: m2-14 (script). Naming table: m2-7, C23. Distance and its three properties: C18, m2-4; shortest walk = shortest trail = shortest path: m2-12; properties from definition: m2-16.
- Lemma (walk contains path, any u, v, length bound): C19, C20, m2-3, m2-9 (derived). Path has at most N - 1 edges: C33, m2-6, m2-11 (derived). Board distances and counts: m2-13.

Conclusions and premises: Lemma follows by strong induction on the length (premise: the cut construction is a walk, checked in the proof); the length bound follows from k + 1 distinct vertices among N.

Not justified or qualified: degree (Definition on degree) has no textbook number because the textbook's own definition of degree was not read; it is cited to the lecture-note remark (C9 quote). The seven textbook-graph edges are the ones the textbook's own examples force (m2-1, m2-2); this reading is the module's, not a separate claim. "A figure eight is a cycle" is marked derived from Definition 1.2.14 and has no evidence claim of its own. The statements about renumbering vertices permuting rows and columns, and that a closed walk of length 2 must reuse an edge, are elementary and marked derived or unmarked remarks without separate claims.

## sections/answer1_walks.tex: Q1: what the entry of a power of A counts

Purpose: define matrix product and power, state and prove the walk-counting theorem by induction, give consequences, and show that the entry counts walks and not paths.

Claims and support:
- Theorem: C6 (Quinlan Thm 1.1.3, Grinberg Thm 4.5.10, Lehman Cor 9.3.3, Bai Thm 1); proof route C7; the proof as written: m1-3 (derived); finite check m1-4.
- Where hypotheses are used (simplicity twice, undirectedness only for symmetry, multigraph version): m1-8 (interpretation).
- Corollary (non-negative integers, positivity means a walk, symmetry): m1-7 (derived).
- (A^2)_ii = degree and trace 2|E|: C9, derived here.
- Walks are not paths, under both textbook readings: C8, C10, m1-6 (derived); board numbers 1,0,2,0,4 walks and 1,0,0,0,0 paths: m1-6 and `author_numbers.py`.
- A^0 = I convention: C7 (Grinberg).

Conclusions and premises: Q1 answer follows from Theorem (induction: base k = 1 from Definition of A; step from the partition by second-last vertex and the bijection when A_rj = 1). Warning follows from the diagonal proposition and from "a path from n_i to n_i is the single vertex".

Not justified: nothing beyond the textbook gap (m3-11, qualified).

## sections/answer2_connectivity.tex: Q2: deciding connectivity from the matrix

Purpose: define connected, components, S, prove the test and its second form, state it as a procedure, show N - 1 is sharp, and give BFS.

Claims and support:
- Definition of connected, board's version: C30, C25. Walk or path give the same connectivity: C32 and derived Remark.
- Components, Remark 2.1.1: C31, m3-1. Textbook examples: m3-2.
- Test statement: C34 (Paramadevan Thm 2, MathWorld); second form: C36 (qualified, Bai); proofs of both: C35, C37 (derived), m3-3, m3-5, m3-9; loose proofs in sources: m3-12.
- Path has at most N - 1 edges: C33. N - 1 cannot be lowered: m3-4 (derived, script). Edge cases N = 1, 2 and diagonal of S: m3-3. Components from S: m3-5. Distance as smallest k: C38 (derived with m2-12).
- BFS decides connectivity, correctness statement: C39, m3-13; agreement with matrix test on all graphs up to 6 vertices: m3-8 (check, not proof).

Conclusions and premises: Theorem follows from Proposition (one pair at a time) and Proposition (I + A form). Proposition one pair: premises Walk counting (C6), Lemma (m2-9), Corollary (m2-11), path implies trail (m2-10), non-negative counts (m1-7). I + A form: binomial expansion with positive coefficients (C37, m3-9).

Not justified: the textbook does not state the test (m3-11, qualified). The proof of the I + A form is in the appendix.

## sections/answer3_path.tex: Q3: the definition of a path between n_i and n_j

Purpose: give the definition of a path between n_i and n_j under the course convention and show that the existence statement is the same under the textbook's other reading.

Claims and support: Definition and its identity with textbook Definition 1.2.13: C16, C24, m2-8 (qualified; the course reading comes from the assignment text and the board does not say). One path between n_1 and n_3 in the board graph: m2-13. Same truth value under both readings: m2-9, m2-10, C32 (derived). Counts differ by reading: C10, m1-6.

Conclusion and premises: Q3 answer is the definition itself. Qualification: the course reading of "path" is not in any file.

Not justified: nothing beyond the qualification above.

## sections/example.tex: Worked examples

Purpose: write out every matrix for the board graph, the connected and disconnected examples, the four-vertex path, and the exhaustive check.

Claims and support: board matrix, A^2 to A^5, A^3 = 2A, row sums, walk lists, hand sums: m1-5, m1-1. Walk, trail, path counts by length: m2-13 (script `m2_walks.py`). Connected example numbers: m3-6. Disconnected example numbers: m3-7. Four-vertex path matrices and N - 2 failure: m3-4. Exhaustive check table, failures with N - 2 powers (3 of 8, 12 of 64, 60, 360, 1 for N = 2): m3-8, m3-4. Drawing against matrix: C28. The matrices printed in the paper are generated by `appendices/scripts/author_numbers.py` and input from `figures/generated_numbers.tex`; assertions there compare each power with a direct walk enumeration.

Conclusions and premises: each reading follows from Theorem (test) and the printed matrices.

Not justified: the exhaustive table's "wrong with N - 2 powers" column is from the module script (checked: copy output is identical), not recomputed by `author_numbers.py`.

## sections/discussion.tex: Discussion: limits, disagreements, and cost

Purpose: separate proof from computer check, list convention choices, record where sources disagree, give the cost estimate, and list limits and open questions.

Claims and support: sources for walk counting: C6; lemma combination: C19, C20; conventions: C15, C16, C17, C22, C24, m2-15; mark above A: C29, m1-9; drawing: C28; Paramadevan Theorem 1 wrong as written: C11, C10; loose proofs: m3-12; cost counts (98,000,000 and 7,000,000 for N = 100; N^2 = 10,000; 38,742,049): m3-10 (estimate; script); BFS O(n + m) with adjacency lists: C39, m3-13; textbook absence: m3-11; multigraph interpretation: m1-8.

Conclusions and premises: "the matrix test is useful for its clean statement, not speed" is an interpretation resting on m3-10's counts. Repeated squaring is justified by m3-9.

Not justified: none unsupported. Faster matrix multiplication was not examined, and the text says so. C39's wording "N - 1 matrix products" disagrees with the count N - 2 in m3-10; the paper uses N - 2 and says the slides do not make the comparison.

## sections/conclusion.tex: Conclusion

Purpose: direct answers to Q1, Q2, Q3 and what stays open.

Claims and support: Q1: C6, m1-3, C8, m1-6. Q2: C34, C35, C37, m3-4, C39. Q3: C16, C24, m2-8. Open items: C28, C29, m3-11.

Conclusions and premises: each answer repeats the theorem or definition proved above.

Not justified: nothing new.

## appendices/derivations.tex: Derivations and checks

Purpose: proofs of the distance properties (A.1), the counterexample table (A.2), the premise chain of the test (A.3), the I + A proof (A.4), and the finite cross-checks (A.5).

Claims and support: m2-12, m2-16 (A.1); C10, m1-6 (A.2); C35 and premises C6, C20, C33, C30 (A.3); C37, m3-9 (A.4); m1-4, m3-8, m3-4, and the m2 script checks m2-9 to m2-12 (A.5; numbers 73, 381, 4695 walks, 300 random graphs, 192696 walks are from `m2_walks_output.txt`).

Conclusions and premises: A.4 follows from the binomial expansion and positivity of coefficients; for m greater than N - 1 it uses the length bound.

Not justified: the random-test numbers in A.5 are quoted from the module script output, not independently recomputed.

## appendices/course-terms.tex: The textbook's terms and numbers

Purpose: table of textbook definition numbers and printed pages used.

Claims and support: C1, C2, C3, C4, C12 to C19, C30, C31, m3-1. The textbook's number for the adjacency matrix definition is not recorded; the table says so.

Conclusions and premises: none beyond the table.

Not justified: pages are the printed pages as recorded in the evidence file; this author did not re-read the book, because the evidence file is declared final.

## appendices/photographs.tex: The whiteboard photographs

Purpose: transcription of the board and the edge by edge comparison of drawing and matrix.

Claims and support: C25, C26, C27, C28, C29. The photographs are included as images; the transcription is taken from the evidence quotes (C27 words "it's" and "adj." as on the board).

Conclusions and premises: the arrowhead as a stray mark is an interpretation (brief assumption), labelled as such.

Not justified: reading of the mark above A (qualified, C29).

## appendices/reproducibility.tex: Reproducibility

Purpose: list the scripts that produced every number and how to run them.

Claims and support: scripts `author_numbers.py` (new), `m1_walks.py`, `m2_walks.py`, `m3_connectivity.py`. Outputs of the three module scripts were re-run in this session and are identical to the saved outputs.

Conclusions and premises: none.

Not justified: nothing.

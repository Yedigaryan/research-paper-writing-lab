# Self-evaluation

Build: `build.sh` ok (LaTeX installed), 6 pages against a budget of 6, no overfull boxes.
check_citations: 0 errors, 0 warnings. check_claims: 0 errors, 0 warnings (47 supported, 3 qualified, 0 unverified). inspect_pdf: 6 pages, 0 errors, 0 warnings.
Analogies: no, so no plain-words layer and no check_plain_words run. No claim was added to the evidence file. Cross-references print capitalised ("Theorem 3.1", "Section 2") in the compiled text.
Optional objectives: O1 (Remark 4.4) and O3 (last paragraph of Section 6) are written; O2 is left out (no room).
Files: `main.tex`, `references.bib`, `sections/{introduction,definitions,walks,connectivity,examples,limits,notes}.tex`. The template's `analysis`, `background`, `discussion`, `conclusion` sections and `appendices/derivations.tex` were removed (no appendix needed; the proofs are in the body).

## Section 1 Introduction
Purpose: states the three questions, the three answers, the organization. Claims: the answers point to Theorem 3.1 (m1-3, C19), Theorem 4.3 (M2-3), Definition 2.4 (C10); the textbook printed-page convention. The sentence on the textbook's word "path" points to Remark 2.5 (C11). Nothing unjustified.

## Section 2 Setting and definitions (N1 to N4)
Purpose: fix notation and the five definitions in the textbook's order.
- Def 2.1 graph, simple, adjacent: C1, C2, C3, m1-1. Notation n_i (board) vs v_i (textbook): C6, stated in one clause.
- Def 2.2 adjacency matrix, symmetric, zero diagonal: C4.
- Matrix product and powers: standard definition, no claim.
- Def 2.3 walk: C7, C8; edges determined by vertices in a simple graph: m1-2 (derived, marked). Repeats allowed: C7. Length 0 is the paper's convention; agreement with textbook p. 23 and Grinberg: C15 (stated with the qualification that the textbook does not say it in words).
- Def 2.4 path: C10, C12, C13. The course meaning (C14, qualified) is carried by the clause "This is the meaning of path throughout the paper" in the body and by the Notes on sources.
- Remark 2.5: textbook path is a trail: C11. One path of length 0 per vertex and symmetry: derived from Def 2.4.
- Def 2.6 connected: C16 (restated with the paper's path). Pointer to Prop 4.2.
Conclusions: none beyond definitions.

## Section 3 Walk counting (N5)
Purpose: answer to question 1. Theorem 3.1 for all k >= 0 (as m1 states it), proof by induction with base case, hypothesis, and step in full; statement attributed to Galway Thm 1.1.3, Gotti Prop 2, Bai Thm 1 (C19, C20, C21); the proof is the paper's own (m1-3). Example 3.2: A^2 of the board graph and the entries (A^2)_11, (A^2)_22, (A^2)_13 (C22, m1-5; script m1_walks.py). Conclusion "entries count walks not paths" follows from the example plus the theorem. Nothing unjustified. I used the board graph's A^2 only; no A^3 or A^4.

## Section 4 Connectivity test (N6, N7, O1)
Purpose: answer to question 2.
- Lemma 4.1 (a) walk contains path, i = j allowed, (b) path length <= N - 1: M2-1, M2-2; Grinberg Cor 2.9.7 and p. 40 (C24, C25); textbook Lemma 1.2.1 has u != v and no bound (C26). Proofs as m2, complete.
- Proposition 4.2 (path iff trail): M2-4 and m1-4, written once (m1's Prop 1 and m2's Remark 2.3 are the same argument). Uses Lemma 4.1(a) in the trail-implies-path half, and is placed after the lemma. Derived, marked "Derived here".
- Theorem 4.3 sum test, N >= 2: M2-3, C27, C28. Premises: Theorem 3.1, Lemma 4.1, Def 2.6. N = 1 treated in the closing paragraph; diagonal can be zero (N = 2).
- Remark 4.4 (O1): C29, M2-10; the matrices R for G_1 and G_2 are from the script output (lines "(I + A)^2" of m2_connectivity_test.out).
Nothing unjustified.

## Section 5 Worked examples (N8)
Purpose: the test on the board graph and the test failing on a disconnected graph, all matrices printed. M2-5, M2-6; script m2_connectivity_test.py (output verified identical on rerun). The third graph of m2 (path on four vertices) is not used: S_22 = 2 on the board graph already shows that entries count walks.

## Section 6 What the test does not give (N9, O3)
Purpose: limits. Entries count walks: M2-7 restricted to the board graph (S_22 = 2, one path (n_2)). Not the cheapest: M2-9 (qualified), written with its qualification in the text: stated for depth-first search only, nothing on breadth-first search or on this test, an interpretation, no complexity analysis. O3: C32, C33 with quotes and pages; the counterexample (A^2)_11 = 1 checked against the length-0 convention.

## Notes on sources
Holds the board reading, the exponent k, the drawing/matrix mismatch, the (G,V) notation, C14 (qualified), C34 (qualified: text search plus four pages, p. 7 not viewed), authors by surname only, no BFS source, script locations. Under half a page.

## Qualified claims and where the text qualifies them
- C14: Notes on sources ("rests on a summary ... (qualified)"); body Def 2.4 says only "the meaning of path throughout the paper".
- C34: Notes on sources, second paragraph; the body does not state the absence.
- M2-9: Section 6, in the sentence beginning "That the test is therefore".

## Not justified or not done
- O2 (distance) omitted for room. The evidence claims C31, m1-6, M2-8 and the path-graph example of M2-7 are not used; no `check_citations` warning results.
- The bibliography entry for the textbook has no publisher or year (not read). The Galway and Gotti entries have no year; Galway has no author.
- Bibliography entries [4], [5], [10] cite local files; the body cites them only in the Notes on sources.

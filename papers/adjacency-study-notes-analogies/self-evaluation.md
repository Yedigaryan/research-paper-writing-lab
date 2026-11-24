# Self-evaluation

Build: `build.sh` ok (LaTeX installed), 6 pages against a budget of 6, no overfull boxes.
check_citations: 0 errors, 0 warnings. check_claims: 0 errors, 0 warnings (47 supported, 3 qualified, 0 unverified). inspect_pdf: 6 pages, 0 errors, 0 warnings.
Analogies: no, so no plain-words layer and no check_plain_words run. No claim was added to the evidence file. (Revised in round 1; see the logs at the end.) Cross-references print capitalised ("Theorem 3.1", "Section 2") in the compiled text.
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

## Round 1 revision: per-finding log

Checks after revision: build ok, 6 pages; check_citations 0/0; check_claims 0 errors, 0 warnings (47 supported, 3 qualified); inspect_pdf 0 errors, 0 warnings.
Sections changed: 1 (introduction), 2 (definitions), 3 (walks), 4 (connectivity), 5 (examples), 6 (limits), Notes. Claim support is as listed above, except where noted below; the Section 6 text now rests on M2-9 (qualified; the text says it is an interpretation and that the source does not discuss the matrix test), C32, C33, C21.

Evaluator findings
- F1, F2, F12 (evidence and bib): C20, C12, C5 quotes checked; no sentence of the paper quotes them. references.bib: Wayne entry now lists Sedgewick and Wayne; Galway left without author.
- F3: connectivity.tex, sentence after Theorem 4.3 shortened to the attribution and "the proof below is this paper's own".
- F4: limits.tex, first sentence now "The entries of S count walks, not paths (Example 3.2), so only their positivity is used."
- F5: definitions.tex: Grinberg clause and "(a derived remark)" removed. Not done as asked: the textbook's own vertex-sequence note on p. 21 is not held by any evidence claim (C7 and m1-2 quote Definition 1.2.10 with its edges only), so I did not cite it; the sentence says the edges are determined by the vertices in a simple graph, still cited to Definition 1.2.10 p. 21 just before it.
- F6: limits.tex one sentence on graph search, no O(E), no breadth-first sentence; the breadth-first sentence is cut from notes.tex.
- F7: limits.tex uses (A^k)_{ij}, k, N, quote marks on quoted words only; a closing sentence says Bai's n is N.
- F8: Bai's comment after Theorem 1 now named as a comment. Not done: crediting Paramadevan and Sotheeswaran's Section 2.2 item 7; no evidence claim holds that statement (C31 holds only Theorem 3, on distance), and adding one is not allowed in this round.
- F9: definitions.tex Definition 2.4 rewritten as asked.
- F10: Example 5.2 retitled "The test on a disconnected graph".
- F11: "(Derived here.)", "The following is derived here.", "(qualified)" removed; notes say "the assignment text"; Example 3.2 "computed by script" replaced by "checked against a brute-force count of walks" with the existing citation. Not done as asked: examples.tex no longer names the script file, but I did not add a bib entry for the m2 script, because the evidence file has no source for it and a new source is not allowed; the Notes on sources name it and say how to rerun.
- F13: used_in set in evidence.base.json, modules/m1.json, modules/m2.json; merged file rebuilt; only used_in changed.
- F14: walks.tex: "prove it from k = 1; the case k = 0 is added here".

Reader findings (advisory)
- R1: Example 3.2 retitled "The example graph G_1" and the introduction points to the Notes on sources for where the example comes from; "board graph" removed from the body.
- R2: "The University of Galway notes" in Section 3.
- R3: d(u,v) called the textbook's distance.
- R4: "Group the walks by their last-but-one vertex".
- R5: written out in Lemma 4.1(a).
- R6: Proposition 4.2 retitled.
- R7: case split written out.
- R8: closed with F6 (one sentence, interpretation).
- R9: "without defining 'path'".
- R10: N used; sentence says Bai's n is N.
- R11: mapping sentence added to Remark 2.5.
- R12: Definition 2.4 points to the Notes on sources.
- R13: closed with F11.
- R14, R15: one pointer sentence in the introduction; the retelling stays in the Notes (brief).
- R16: stays; the rows of R are printed in Remark 4.4 and a display would exceed the budget.
- R17: "has no edge at all".
- R18: stays; the style rules require a local-file entry to say it was supplied by the user; the user-statements entry now says it is a summary of the assignment's conventions.
- R19: the introduction says the textbook is in Armenian; missing publisher and year are in the Notes on sources.
- R20: Section 5 intro says what the script computes and checks; the file name is in the Notes.

## Round 1 revision, second pass (F5, F8, F11)
- F5: definitions.tex now cites the textbook's sentence after Definition 1.2.10 (p. 21) for writing a walk by its vertex sequence (m1-7).
- F8: limits.tex adds the clause that Paramadevan and Sotheeswaran's own list of properties states the fact with walks (Section 2.2, item 7, p. 16; M2-11).
- F11: references.bib has the entry m2_connectivity_script (evidence source record), cited in the first sentence of Section 5.
Checks: see the final report of this pass; page count stays 6.

## Final edits (round 2 minor findings and reader passages)
Sections touched: abstract (main.tex), 1, 2, 3, 4, 5, 6, Notes; references.bib. Checks: build ok, 6 pages; citations 0/0; claims 0/0; inspect_pdf 0/0. No claim, no new cite key, no statement or proof step changed.

Evaluator findings
- F16: stray semicolon removed (connectivity.tex).
- F17: "Grinberg's example of a length-0 walk" (definitions.tex), citation unchanged.
- F18: "Grinberg proves (a) without its last clause and states (b)" (connectivity.tex); Lemma 4.1 unchanged.
- F19: "stated only for two different vertices and has no length bound".
- F20: pages added: Galway Definition 1.1.1, p. 2; Grinberg Definition 2.9.1(c),(d), p. 36; Bai "definition of path after Theorem 1, p. 1".
- F21: the rule requires the "supplied by" note, so it stays but no longer says "the user": "supplied by the student who requested these notes", photograph "not public"; script notes say "written for these notes; see Notes on sources". File paths stay in howpublished. Keys unchanged.
- F22: Example 5.1 diagonal sentence cut; Example 5.2 last sentence shortened as asked.

Reader passages (changed unless marked stays)
- F1 changed (abstract names Theorems 3.1 and 4.3). F2 changed (gloss of walk in the introduction). F3 stays: the course is not named in any input. F4 changed. F5 changed. F6 stays: would add a sentence and the distance clause carries its citation. F7 changed.
- F8, F9, F11, F12, F13, F14 stay: they rewrite proof steps or the wording of a proof; F9 "penultimate" would also change the proof's terms.
- F10 changed (roles named; "their proofs start at k = 1"). F15 stays: proof step of the remark. F16 stays: would add a citation. F17 stays: no room and it alters the example's working. F18 changed (clause added). F19 stays: no cost source beyond M2-9. F20 stays: the marks cannot be shown without a figure. F21 changed (matrix is the object both questions are about; arrowhead and third line ignored). F22 stays: the convention is already pointed to the Notes. F23 stays: C34 limits the viewed pages to what the notes list; listing the others adds length. F24 changed ("unnumbered"). F25 changed ("isolated mode"). F26 changed ("where I is the identity matrix"). F27 changed (textbook's order; pages sentence kept).

## Plain words layer (added in this folder; Analogies: yes)
Formal text: unchanged. The diff against the released folder shows only added lines (twelve plain-words paragraphs with `\medskip`, and one added block at the end of the introduction: the story, the dictionary, and the sentence saying what the paragraphs are). No formal sentence was changed; `main.tex` and `references.bib` are identical to the released ones. Pages 7 of 8. Checks: build ok; citations 0/0; claims 0/0; inspect_pdf 0/0; check_plain_words: 12 paragraphs, 9 statements checked, 0 errors, 0 warnings.

Story dictionary (technical term, story word): vertex, house; edge, lane; adjacent, neighbours; adjacency matrix, neighbour chart; entry, box; walk, stroll; length, steps; path, no-return stroll; connected, joined-up; matrix power A^k, the chart used that many times over; sum of powers, the charts added up; the sum test, "the rule".

The twelve paragraphs (statement; why it is true of it)
- Def 2.1 graph and adjacency: a village of houses and lanes, lanes two-way between different houses, at most one per pair; this is the simple undirected setting.
- Def 2.2 adjacency matrix: a yes/no box per pair of houses; symmetric and no house its own neighbour, which are the symmetry and zero diagonal.
- Def 2.3 walk: moves along lanes, repeats of houses or lanes allowed, steps counted with repeats, standing still is length 0.
- Def 2.4 path: never visits a house twice; standing still counts; "between" start and end.
- Def 2.6 connected: any two houses linked by a no-return stroll; own house covered by standing still.
- Thm 3.1: the chart "used as many times over as you want steps" is A^k (k = 0 included: not at all); each box counts strolls of that many steps, repeats allowed, "not only no-return strolls".
- Ex 3.2: three houses in a row; the out-and-back stroll is the one two-step stroll from an end house to itself ((A^2)_11 = 1) and it is not a no-return stroll.
- Lemma 4.1: shortening by cutting out the part between two visits of a house; a no-return stroll has fewer steps than houses (at most N - 1).
- Prop 4.2: the textbook's weaker stroll (no lane reused); no-return implies no lane reused, and any such stroll cuts down to a no-return one (Lemma 4.1).
- Thm 4.3: chart used once up to N - 1 times, added; joined-up exactly when every box for two different houses is above zero; boxes of a house with itself not looked at.
- Ex 5.1: row of three houses, every off-diagonal box above zero, rule says joined-up.
- Ex 5.2: one lane between two houses, third house without a lane; boxes to it are zero; rule says not joined-up, which is correct.

What the story cannot express exactly: the exact count in Theorem 3.1 and in Example 3.2 (the numbers appear only in the formal text); "the chart used that many times over" stands for a matrix power, which is a product and not a repetition of a lookup; the sum in Theorem 4.3 is "added up" without saying entry by entry; the requirement N >= 2 is not mentioned; the finite size of the village is not stated. Mirror caveat: a village with a house and no lane is allowed, as the story's "some pairs" says.

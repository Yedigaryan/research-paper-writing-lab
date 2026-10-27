# Self-evaluation: adjacency-walks-connectivity

Author agent, first draft. Register: study-note. Numbers below ("Definition 2.20", "Theorem 3.5") are the paper's own numbers as compiled; labels are in brackets. Claim ids are from `evidence/evidence.json` (77 claims: 70 supported, 6 qualified, 1 unverified). "Derived here" means the paper proves or computes it; "script" means a number from `appendices/scripts/`.

## 0. Status and mechanical checks

| Check | Result |
|---|---|
| `build.sh` | exit 0, `main.pdf` 35 pages. TeX Live and biber are installed, so the no-LaTeX exit code 2 did not occur. |
| `check_citations.py` | 11 keys cited, 11 bib entries, 11 evidence sources, 0 errors, 0 warnings |
| `check_claims.py` | 77 claims, 0 errors, 0 warnings |
| `inspect_pdf.py` | 0 errors, 1 warning: 2 overfull boxes of 1.4 pt and 1.8 pt (a URL in the bibliography and one line of Appendix A.1) |
| biber | 6 warnings: the `year` field of six web or photo entries is `n.d.` because the evidence file has `year: null`; biber says it will not sort properly. The bibliography is in order of citation anyway. |
| Plain-words layer | 39 "In plain words" paragraphs. Every definition, theorem, lemma, proposition, corollary and test environment is preceded by one (checked by script). 206 sentences, mean 9.3 words, longest 18, 8 longer than 15. No `$` or backslash inside any of them. |
| Numbers | Every matrix and table body is a macro in `appendices/generated_numbers.tex`, written by `appendices/scripts/generate_paper_numbers.py`, which parses the saved module outputs, recomputes with independent code, and asserts equality (it passed). The three module scripts were re-run and reproduce their saved outputs exactly. |

Things I did not do, stated plainly:

- I did not open the textbook PDF. Every textbook definition number, page, quote-derived example and non-example comes from the evidence file (claims C1 to C4, C12 to C19, C30, C31, m2-1 to m2-4, m3-1, m3-2). If one of those is wrong, the paper repeats the error.
- I viewed both whiteboard photos. I could not read the handwritten word before the conditions in the first line (`A_ij = 1 ... e_ij in V`) with confidence; the paper prints "if" as in the brief and claim C26.
- I did not edit `evidence/modules/*.json`; only the merged `evidence/evidence.json` (see Section 11).

## 1. Abstract

Purpose: summarise the three answers. Claims: A1 walk counting (C6, m1-3), A2 test and equivalent form (C34, C35, C36, C37), A3 definition (C16, C24). Conclusions follow Sections 3 to 5. Nothing new is asserted. Weak point: the abstract states "the statement is in Quinlan's notes" with a cite; the proofs are the paper's.

## 2. Section 1, Introduction

| Part | Purpose | Claims and support | Not justified or qualified |
|---|---|---|---|
| 1.1 questions, Table 1 | Say where each question came from; list every board line | C25, C26, C27, C28, C29 (board text, both photos). Q3 came from the assignment text: this is a premise from `brief.md`, not an evidence claim. | The textbook lacks the theorem and the test: m3-11 (unverified), tagged in the text. |
| 1.1 answers in brief | Map of results | C6 (A1), C34/C35/C36/C37/m3-4 (A2), C16/C24/m2-8 (A3) | none |
| 1.2 story, Table 2 | Fix the houses-and-roads story and the dictionary to textbook words and numbers | Textbook numbers: C1, C2, C12 to C18, C30, C31. Story is the paper's own choice, not a claim. | Degree and adjacency matrix have no textbook number in the pages read (n.n.). |
| 1.3 conventions, Table 3 | State every reading made | Item 1 C1; item 2 C29, m1-9 (qualified); item 3 C27; item 4 C28 (edge by edge); item 5 C25, C26; item 6 C15, C16, C21, C24 (qualified); item 7 C7, m2-15 (qualified); item 8 m3-11 (unverified) | The reading of the mark above A and of "path" are interpretations that only the user can settle. The paper says so. |
| 1.4 notation, Table 4 | Fix letters before the first definition | C25, C26 for the board letters; textbook letters C1, C2 | none |
| 1.5 organisation | Say how statements are labelled | none | none |

Conclusion drawn in 1.3 item 4: the matrix is the example graph. Premises: the board says the graph is given through its adjacency matrix (C27), the matrix is symmetric (C28), the brief's assumption. The paper reports the mismatch and does not guess the lecturer's intent.

## 3. Section 2, Background

Purpose: the definitions in the textbook's order with number, page, plain words, remark, example, non-example. Examples use the board graph B, the board drawing T, and the textbook graph G_tb (seven forced edges, Fig. 2).

| Item | Claims | Notes |
|---|---|---|
| Def 2.1 graph [def:graph], 2.5 adjacent, 2.13 adjacency matrix | C1, C2, C26 | Definition 2.9 degree is the usual meaning, cited to nothing, no textbook number. Remarks 2.2, 2.6, 2.10, 2.14 are derived here (trivial). |
| Prop 2.17 properties of A [prop:Aproperties] | C3, C4, C5, m1-1 | Items 4 and 5 derived here; C5's source states item 4 with loops. Proof is complete for items 1 to 6. |
| Def 2.20 walk, Remark 2.21 | C12, C13, m1-2, m2-15 | Remark 2.21: a walk is its vertex list (derived, m1-2). Length-0 walks: interpretation, qualified (m2-15). |
| Def 2.24 closed walk | C14 | Remark 2.25 (no closed walk of length 1; length 2 repeats an edge) derived here. |
| Def 2.28 trail (textbook "path" 1.2.12) | C15, m2-1, m2-14 | Remark 2.29: trails equal paths in B up to length 4, by script. Textbook example and non-example are G_tb sequences. |
| Def 2.32 path (textbook "simple path" 1.2.13) | C16, m2-2, C24 (qualified) | Non-example 2.35 cites the page, not the position, as the orchestrator asked. Textbook defines it as a trail with distinct vertices; Prop 2.36 shows the two readings agree. |
| Prop 2.36 path implies trail | m2-10 | Proved here; Grinberg leaves it as an exercise (m2-5). |
| Def 2.37 cycle, 2.41 simple cycle | C17, C22, m2-2, m2-14, m2-15 | B has no cycle (script, closed walks up to length 6). Length-0 closed trail not counted as a cycle: interpretation, qualified. |
| Def 2.45 distance, Remark 2.46 | C18, m2-4, m2-12 | Written with "trail" for the textbook's "path". Independence of the reading: appendix A.5, derived. |
| Lemma 2.49 walk contains a path, Cor 2.51 length bound | C19, C20, m2-3, m2-9, m2-11, C33, m2-6 | Textbook states it for u different from v without a bound; the bound and u = v come from Grinberg Cor 2.9.7. The paper proves the general form (strong induction on k). The proof was also tested by script on 73 + 381 + 4695 walks and 192696 random walks (appendix A.6). |
| Def 2.52 connected, Prop 2.56 three readings agree | C30, C32, C19, C20, m3-3 | Prop 2.56 derived here (path => trail => walk => path). Reading u = v: interpretation (m3-3). |
| Def 2.57 component | C31, m3-1 | Textbook gives it in prose on p. 49; no number. Remark 2.58 is the textbook's Remark 2.1.1. |

Conclusions: "connectedness does not depend on the meaning of path" follows from Prop 2.36 and Lemma 2.49. Not justified: the textbook definition numbers themselves are taken from the evidence file.

## 4. Section 3, Answer 1

Purpose: answer Question 1 with a full proof and the warning.

| Item | Claims | Premises and conclusion |
|---|---|---|
| Def 3.1 product and power | none (standard definition) | Used by Thm 3.5. |
| Thm 3.5 walk counting [thm:walkcount] | C6 (four sources), C7 (route), m1-3 (proof), m1-8 | Conclusion: (A^k)_ij is the number of walks of length k. Premises: walks are vertex lists (Remark 2.21), the definition of the product, induction on k with the base case k = 1 and the second-last vertex split. The textbook does not state it in the pages read (m3-11, unverified). |
| "Why valid" paragraph | m1-8 (interpretation), m1-4 (finite check) | Says where simplicity is used. Finite test: 40, 360, 5120, 76800 cases. |
| Cor 3.9 (a) to (d) | m1-7, C9 | (d) (A^2)_ii = degree, trace(A^2) = 2|E|. |
| Prop 3.10 walks are not paths | C8, C10, m1-6, m1-5, C11 | Conclusion: the entry is not a path count. Premises: (A^2)_ii = degree > 0; the walk n_i, n_r, n_i repeats a vertex and an edge. Table 5 from script: 1,0,2,0,4 walks against 1,0,0,0,0 paths. The disagreement with Paramadevan and Sotheeswaran Theorem 1 (C11) is stated and resolved in favour of walks. |

Cannot justify beyond sources: "the same proof counts walks with multiplicity for a multigraph" is an interpretation (m1-8), tagged.

## 5. Section 4, Answer 2

Purpose: answer Question 2: test, proof, equivalent form, sharpness, BFS.

| Item | Claims | Premises and conclusion |
|---|---|---|
| Def 4.1 S | new notation | Stated as new. |
| Prop 4.5 one pair | C6, C19, C20, C33, m1-7, m2-9, m2-11 | (i) path, (ii) some k in 1..N-1, (iii) S_ij > 0 are equivalent. Uses Thm 3.5, Lemma 2.49, Cor 2.51, non-negativity of counts. |
| Thm 4.6 the test | C34 (statement), C35 (proof), m3-11, m3-12 | Conclusion: connected iff every off-diagonal entry of S is positive. Premises: Prop 4.5, Def 2.52, Prop 2.56. The two web proofs are loose (m3-12), so the paper proves it. |
| Cor 4.10 components, distance | m3-5, C38, m2-12 | Derived; distance part uses appendix A.5. |
| Remark 4.11 diagonal, N = 1, 2 | m3-3, C9 | Script for N = 2. |
| Test 4.12 | none | The loop makes N - 2 products. |
| Prop 4.16 (I + A)^m | C36 (qualified), C37, m3-9 | Proof is in appendix A.4 (binomial expansion). Bai's statement is cited only for the statement. |
| Prop 4.17 N - 1 sharp, Example 4.18, Table 6 | m3-4 | Row of N houses; script table for N = 3..8; four-house matrices written out. |
| 4.6 BFS paragraph | C39, m3-13, m3-10 | Cites the slides only for BFS correctness, the adjacency-list time O(n + m), and for what they say. |

Not justified: nothing in the proofs. The statement that the test is "also" in MathWorld rests on C34 (formula is an image; alt text read).

## 6. Section 5, Answer 3

Purpose: the definition of a path between n_i and n_j and the three-convention table.

Claims: Def 5.1 is C24/m2-8 (qualified; the textbook supplies the definition, the course use comes from the assignment text). Table 7: C12 to C17, C21, C22, C23, m2-7. Rem 5.5 numbers from script (m2-13). Conclusion: "a path between n_i and n_j" is a walk with pairwise distinct vertices; existence is convention independent (Prop 2.56). Not justified: that the course uses this convention (user's statement only); that the circuit row is accurate beyond Grinberg's remark that use is not uniform.

## 7. Section 6, Worked example

Purpose: every matrix for B and for D. Claims: m1-5 (A^2 to A^5), m3-6 (B), m3-7 (D), m2-13 (counts), m3-8 (exhaustive table), C28 (mismatch). All matrices are macros from the generator. Hand sums in Example 6.1 are from `m1_walks.py`. Conclusions: B connected, D not connected with components {1,2} and {3}; agreement with BFS (script). Nothing here is unjustified; the exhaustive agreement is a check, not a proof, and is said to be.

## 8. Section 7, Discussion

Purpose: limits. Claims: C29, m1-9 (mark), C28 (drawing), C24 (path), m3-11 (textbook coverage), m1-8 and C6 (digraphs), C11/C36/m3-12 (weak sources), m3-4 (failure cases), m3-9/m3-10 (cost).

Items I label interpretation or estimate because the evidence file does not carry them as claims: (i) that a Boolean version of the product avoids the growth of entries (from the m3 report only; tagged); (ii) that the matrix test is useful for its clean statement and not for speed (tagged interpretation); (iii) the cost counts are school-method estimates (m3-10). Claim C39's text says the matrix test needs N - 1 products; the paper writes N - 2 (m3-10) and says why; the slides support only the BFS time and correctness. I did not change C39's text.

## 9. Section 8, Conclusion

Direct answers to Q1, Q2, Q3, each pointing to the theorem (3.5, 4.6, 5.1) and its premises. Open items repeated: mark above A, drawing mismatch, lecturer's intended answer to Q2, textbook coverage.

## 10. Appendices

| Section | Purpose | Claims |
|---|---|---|
| A.1 walks as vertex lists | detail behind Thm 3.5 | C7, m1-2, m1-3 |
| A.2 walk versus path counterexample | general counterexample | C10, m1-5, m1-6; closed-walk counts 0,1,0,2 by script |
| A.3 chain of premises (Table 12) | audit trail for the test | C35 and the claims in the table |
| A.4 (I + A)^m | proof of Prop 4.16 and any m >= N - 1 | C37, m3-9 |
| A.5 distance | Props A.1, A.2: shortest walk = shortest trail = shortest path; the three distance properties | m2-12, m2-16, m2-6 |
| A.6 cross-checks | counts from the scripts | m1-4, m2-9 to m2-12, m3-8, m3-9, m3-4 |
| A.7 scripts (Table 13) | how to reproduce | scripts copied to `appendices/scripts/` |
| B course terms (Table 14) | terms, textbook numbers, pages | C1, C2, C12 to C19, C30, C31, m3-1, m3-2 |

## 11. Changes to the evidence file

Only `evidence/evidence.json`; the module fragments in `evidence/modules/` still carry the old pointers (merging again would duplicate claims, so I did not re-merge).

- `derivation` rewritten to the final labels for C7, C10, C35, C37, m1-1 to m1-7, m2-9 to m2-14, m2-16, m3-3 to m3-10. Pointers now name the paper's own numbers, the labels, and the copies of the scripts in `appendices/scripts/`.
- `used_in` rewritten for all 77 claims from the files where the id appears (the old values named `sections/analysis.tex`, which no longer exists).
- No claim added, none removed, no text or status changed.

## 12. Unverified, qualified, and unjustified items in the text

| Item | Where | Status |
|---|---|---|
| Textbook has no counting theorem or matrix test | 1.1, 1.3 item 8, Sec 3, Sec 4, Sec 7, App B | m3-11, unverified; tagged each time |
| Mark above A is k | 1.3 item 2, Sec 7 | C29 / m1-9, qualified |
| Course "path" = distinct vertices | 1.3 item 6, Def 2.32, Def 5.1, Sec 7 | C24 / m2-8, qualified |
| Length-0 walks allowed; length-0 closed trail not a cycle | Remark 2.21, 2.38, 1.3 item 7 | m2-15, qualified |
| Bai's (I + A)^(N-1) statement | Prop 4.16 | C36, qualified; proved in the paper |
| Boolean product avoids growth; matrix test not for speed | Sec 7.5 | interpretation, not an evidence claim |
| Textbook definition numbers for degree and adjacency matrix | Defs 2.9, 2.13, Table 2, App B | not recorded in the evidence file; the paper says "none" |
| The word before the conditions in the first board line | Table 1 row 1 | printed as "if" per brief and C26; I could not read it myself |
| Textbook title and author names | `references.bib` | the evidence title is in Armenian script, which pdfLaTeX cannot print; the bib entry uses the Latin form of the file name ("Grafneri tesutyun") and the English gloss in the evidence record |
| Missing years | `references.bib` | six entries have `year = {n.d.}`; biber warns |

## 13. Anything I could not justify

Nothing in the mathematics. Every theorem, lemma and proposition has a proof in the paper, and the proofs were checked by script on small cases (not as a substitute). What I cannot justify beyond the sources is the list in Section 12.

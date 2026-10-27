# Self-evaluation: adjacency-walks-connectivity (revision 1, after round 1)

Author agent. Register: study-note. Numbers such as "Definition 2.16" or "Theorem 3.5" are the paper's compiled numbers. Claim ids are those of `evidence/evidence.json`: 80 claims, 73 supported, 7 qualified, 0 unverified. "Derived here" means proved or computed in the paper; "script" means a number from `appendices/scripts/`. Nothing below is marked resolved; round 2 does that.

## 0. Mechanical checks (after the revision)

| Check | Result |
|---|---|
| `build.sh` | exit 0, `main.pdf` 35 pages, 0 overfull boxes |
| `check_citations.py` | 11 keys cited, 11 bib entries, 11 sources, 0 errors, 0 warnings |
| `check_claims.py` | 80 claims, 0 errors, 0 warnings |
| `inspect_pdf.py` | 0 errors, 0 warnings |
| biber | 6 warnings: `year = {n.d.}` on six entries whose year is unknown; unchanged |
| Plain words | 41 paragraphs, 215 sentences, mean 9.3 words, longest 18, 8 longer than 15; none contains `$` or a backslash. A script confirmed that every definition, theorem, lemma, proposition, corollary and test environment is directly preceded by one. |
| Numbers | `generate_paper_numbers.py` re-run, all assertions pass. The cost-table macro is still generated but no longer used in the text. |

Not done, as before: I did not re-read the textbook for the earlier pages. In this round I viewed printed p. 16 (PDF p. 17) as an image to confirm Definition 1.2.1 and Theorem 1.2.1 before adding them. I did not edit `evidence/modules/*.json`.

## 1. Changes to the evidence file

- **C39** text corrected: the BFS time bound holds for adjacency lists, and the matrix test needs N-2 products (the paper's own count, m3-10); the source does not compare the two. The discussion of the old wording is gone from Section 7.
- **m3-11** now `qualified` (was `unverified`), confidence medium, with the exact pages checked (9-12, 16, 21-23, 48-49), the evaluator's full-text search of the book (adjacency matrix only on pp. 11-12, 34, 60; no counting theorem or matrix test), and the unread ranges (13-15, 17-20, 24-47, 50-62, Chapters 3-8). The search is cited as the method, as the coordinator allowed. It has no `support` entry because the search is not a source.
- **au-1** (new, fact, supported): textbook Definition 1.2.1, p. 16, degree, with the Armenian sentence transcribed from the page image.
- **au-2** (new, fact, supported): textbook Theorem 1.2.1 (Euler), p. 16, sum of degrees is 2|E|.
- **au-3** (new, derived, supported): the N-2 test fails exactly on the labelled path graphs, N!/2 of them (new Remark 4.19, finding R15).
- `derivation` pointers and `used_in` regenerated for the final labels (including Remark 4.19, Proposition 2.20, Section 7.4).
- No other text or status changed.

## 2. Findings, one line each

| Id | Action | Where |
|---|---|---|
| E1 | Fixed. Degree is Definition 2.16, cited to textbook Definition 1.2.1, p. 16, with d_G(v), d(v) shown and the clash with distance explained; it now follows the adjacency matrix (Definition 2.9) and Proposition 2.13 (properties of A), as in the book. Row sums and the total are Proposition 2.20, citing Theorem 1.2.1 for the sum of degrees. The order list in Section 2, Tables 2, 4 and 14 are updated. | Sec. 2.1, 1.2, 1.4, App. B |
| E2 | Fixed. The exact pages checked and unread are in Section 1.6; Section 7.1, Appendix B and the conclusion say "pages checked" and point there. m3-11 is qualified, tagged `qualified`, and the method (the evaluator's full-text search) is stated. | 1.6, 7.1, 8, App. B |
| E3 | Fixed. "University of Galway notes" in the abstract, Section 3, Appendix A.1, Appendix B; Section 1.6 and the bib note say the URL suggests the name Quinlan and the file does not confirm it. | abstract, 3.2, A.1, B, bib |
| E4 | Fixed. The "circuit" parenthetical is gone from Table 7 and the sentence below it. Reason: the evidence file carries no quote of Grinberg's remark, so the paper no longer states it. "Closed trail" is labelled as this paper's own name. | 5.1 |
| E5 | Fixed. "Loop" means a self-edge only (stated in Remark 2.2); the closed sub-trip is now a "detour that comes back to the same house" in Remark 2.32, the plain-words paragraphs for path and for the lemma, and Appendix A. | 2.1, 2.2, 2.3 |
| E6, R19 | Fixed. Section 1.2 fixes the three story words (trip = walk, trail = trail, route = path) in the story paragraph and in Table 2; "clean route" is gone everywhere; "a house with at least one neighbour" in Section 3.4. | 1.2, 2, 3.4, A.5 |
| E7 | Fixed. Plain words before Corollary 4.10 now read: count the trips of one road, then of two roads, and so on; the first number of roads that has a trip is the distance. | 4.2 |
| E8 | Fixed. Glosses added for metric space (Remark 2.49), reflexive, symmetric, transitive and classes (Definition 2.60, with the reason for each by walks and Proposition 2.59), transpose (Corollary 3.9), queue and discovered (Section 4.6). Big-O removed: "at most a fixed multiple of N + |E|". | 2.4, 3.3, 4.6 |
| E9, R2, R3 | Fixed. No claim id and no mention of the evidence file remains in the reader's text (only LaTeX comments, which are the claim index). The legend of the kind tags moved to Section 1.1 at first use. Section 7.4 states N-2 products and C39 is corrected in `evidence.json` (Section 1 above). The appendix table of premises lost its claim column. | whole paper |
| E10, R16, R17 | Fixed. Section 7.4 is three sentences; Table 11, the Boolean-product paragraph, the 38,742,049 figure and the repeated-squaring text are removed. One multigraph and digraph sentence stays in Section 7.2; the other three (Section 3.2 "why valid", Appendix A.1, the sources sentence in Section 3.2) are removed. | 7.2, 7.4, 3.2, A.1 |
| E11 | Fixed. Bibliography URLs may break (biblatex URL penalties); the Appendix A.1 sentence is rephrased; A^3 = A for D is a displayed equation. The two story/terms tables were widened. 0 overfull boxes. | main.tex, A.1, 6.3 |
| R1 | Fixed. The abstract says "A university lecture whiteboard", names the textbook and gives an example number. | abstract |
| R4 | Fixed. Section 1.1: the answer to Question 2 "could appear to depend" on the meaning of path; it does not (Proposition 2.59). | 1.1 |
| R5 | Partly fixed. Section 1.1 (item Q3) and Section 5 state the assignment text's convention once, as content: in the course, "path" means a walk with no repeated vertices. I do not have the verbatim sentence (the brief records only its content), so it is not in quotation marks. If the coordinator can supply the sentence, it goes into Q3 in Section 1.1. | 1.1, 5 |
| R6 | Fixed. Section 5 opens by saying the answer is Definition 2.35 (path) and that the section adds only the pair form and the comparison table. Definition 5.1 is one line; the example and non-example refer to Example 2.37 (path), Example 2.25 (walk), Non-example 2.38 (path) and Non-example 2.34 (trail) instead of restating. | 5 |
| R7 | Fixed. Proposition 3.10(b): "More generally, on B (and not for every graph) A^{k+2} = 2A^k". | 3.4 |
| R8 | Fixed. Non-example 2.43: a cycle is a closed trail; a closed trail of positive length needs at least three distinct edges (Remark 2.28); B has two. No script check cited. | 2.2 |
| R9 | Fixed together with E8. Transitivity is justified by joining walks, after Proposition 2.59 (the definition already followed it). | 2.4 |
| R10 | Fixed. The seven edges of the textbook's example graph are listed in the text of Section 2. | 2 |
| R11 | Fixed. Remark 2.53: "positions 1 and 4 both hold vertex 3"; the removed entries 2, 4, 3 are shown at each cut. | 2.3 |
| R12 | Fixed. "Case" is defined; the counts are shown as 2*5*4 = 40, 8*5*9 = 360, 64*5*16 = 5120, 1024*3*25 = 76800, with the k range. | 3.2 |
| R13 | Fixed. Section 4.4 explains that I is "wait", gives the one-sentence expansion as formula (3) in the body (labelled eq:binomial), and Example 6.2 now uses it after it is explained. A second plain-words paragraph precedes Proposition 4.16. | 4.4, 6.2 |
| R14 | Fixed. BFS is a four-step procedure; N and |E| replace n and m; no big-O. | 4.6 |
| R15 | Fixed. New Remark 4.19: the N-2 version fails exactly on the labelled rows of houses, N!/2 of them (1, 3, 12, 60, 360), matching the script; the empty sum for N = 2 is explained. This is a new derived claim (au-3). | 4.5 |
| R18 | Fixed. Table 1 row 4 now reads "What does A_ij represent" with the mark described and a pointer to Section 1.3, item 2; the notation table no longer prints A with a dot. | 1.1, 1.4 |
| R20 | Fixed. New Section 1.6 holds sources, pages checked, source weaknesses and the script overview. Sections 2 to 6 keep only "by script" and a pointer to Appendix A.7; script file names are in A.7 only. The old Section 7.3 "where other sources are weaker" is removed; one sentence in Section 7.2 points to Section 1.6. | 1.6, 7, A.7 |
| R21 | Fixed. The offending sentences are quoted: Paramadevan and Sotheeswaran Theorem 1 (also in Section 3.4), the b_ij lines of their proof of Theorem 2, and Bai's "aggregates all paths". | 1.6, 3.4 |
| R22 | Fixed. Remark 4.11 says an isolated vertex would have no path to the other N-1 vertices. | 4.2 |

No finding was left unfixed. R5 is the only one fixed in part, for the reason given.

## 3. Section by section (what the section claims, and on what)

- **Abstract.** Summarises A1 (C6, m1-3), A2 (C34, C35, C36, C37), A3 (C16, C24). Nothing new.
- **1 Introduction.** 1.1 board lines and questions (C25-C29; Q3 from the assignment text, a premise of the brief, R5 above); 1.2 story and dictionary (textbook numbers C1, C2, C12-C18, C30, C31, au-1); 1.3 conventions (C1, C24, C29, m1-9, m2-15; items 1-7); 1.4 notation; 1.5 organisation; 1.6 provenance (C11, C36, m3-11, m3-12). Conclusion: the matrix is the example graph (premises C27, C28, brief).
- **2 Background.** Definitions in the textbook order with number and page: C1, C2, C3, C4, C12-C18, C30, C31, au-1, au-2, m2-1 to m2-4, m3-1, m3-2. Derived here: Proposition 2.20(a) (m1-1), Remark 2.24 (m1-2), Proposition 2.39 (path implies trail, m2-10), Lemma 2.52 and Corollary 2.54 (m2-9, m2-11, C19, C20, C33, m2-6), Proposition 2.59 (C32, C19, C20), the equivalence relation justification. Qualified: C24, m2-15.
- **3 Answer 1.** Theorem 3.5 (C6, C7, m1-3) with proof by induction; Corollary 3.9 (m1-7, C9); Proposition 3.10 (C8, C10, m1-5, m1-6; C11 contradiction stated and quoted). Interpretation: where simplicity is used (m1-8).
- **4 Answer 2.** Proposition 4.5, Theorem 4.6 (C34 statement, C35 proof, m3-11, m3-12), Corollary 4.10 (m3-5, C38), Remark 4.11 (m3-3), Test 4.12, Proposition 4.16 (C36 qualified, C37, m3-9), Proposition 4.17 and Remark 4.19 (m3-4, au-3), BFS (C39, m3-13).
- **5 Answer 3.** Definition 5.1 and Table 7 (C24, m2-8, m2-7, C15-C17, C21-C23, m2-5, m2-13).
- **6 Worked example.** Examples 6.1 to 6.3 (m1-5, m3-6, m3-7, m2-13, m3-8, C28). All matrices are macros from the generator.
- **7 Discussion.** 7.1 open readings (C29, C28, C24, m3-11); 7.2 limits; 7.3 failure cases (m3-4, au-3); 7.4 cost, three sentences (C39, m3-10; estimate).
- **8 Conclusion.** Direct answers; open items repeated.
- **Appendix A.** A.1 walks as vertex lists (m1-2, m1-3, C7); A.2 counterexample in general (C10, m1-6); A.3 chain of premises (C35); A.4 (I+A)^m proof (C37, m3-9); A.5 distance (m2-12, m2-16, m2-6); A.6 cross-checks (m1-4, m2-9 to m2-12, m3-8, m3-4); A.7 scripts.
- **Appendix B.** Course terms with textbook number and page (C1, C2, C12-C19, C30, C31, au-1, au-2, m3-1, m3-2).

## 4. What I still cannot justify beyond the sources

- Textbook numbers other than those for degree come from the evidence file; I viewed only p. 16 myself.
- The reading of the first board line's condition word as "if" (brief and C26); I cannot read it myself.
- The textbook title is printed in Latin letters ("Grafneri tesutyun") because pdfLaTeX cannot print the Armenian title; six bib entries have `year = {n.d.}`.
- R5: the verbatim assignment sentence.
- The statement that the textbook contains no counting theorem or matrix test stays `qualified`: it rests on the checked pages and the evaluator's search, not a page-by-page reading.
- Interpretation tags kept in the text: "the matrix test is useful for its clean statement, not for speed" (Section 7.4), the reading of the mark above A, the course meaning of path, length-0 walks.

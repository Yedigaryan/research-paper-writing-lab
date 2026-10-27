# Self-evaluation: adjacency-walks-connectivity (revision 2, after round 2)

Author agent. Register: study-note. Numbers such as "Definition 2.16" are the paper's compiled numbers. Claim ids are those of `evidence/evidence.json`: 80 claims, 73 supported, 7 qualified, 0 unverified. Nothing below is marked resolved; round 3 does that.

## 0. Mechanical checks (after this revision)

| Check | Result |
|---|---|
| `build.sh` | exit 0, `main.pdf` 38 pages, 0 overfull boxes |
| `check_citations.py` | 11 keys, 11 entries, 11 sources, 0 errors, 0 warnings |
| `check_claims.py` | 80 claims, 0 errors, 0 warnings |
| `inspect_pdf.py` | 0 errors, 0 warnings |
| Plain words | 41 paragraphs, 215 sentences, mean 9.4 words, longest 18, 8 longer than 15, no `$` or backslash. A script confirmed that every definition, theorem, lemma, proposition, corollary and test is directly preceded by one, and that the worked examples, the conventions table and the BFS paragraph have theirs. |
| Numbers | `generate_paper_numbers.py` re-run; all assertions pass, including new ones for graph H, the triangle T (S = 2J) and the hand-check cases of Appendix A.7. |
| biber | 6 warnings, `year = {n.d.}` on six entries (unchanged). |

## 1. Evidence file (E18, E12)

`evidence/evidence.json` is now reproducible from fragments.

- `evidence/evidence.base.json`: the research agent's part (11 sources, claims C1 to C39, 6 contradictions), with C39 corrected to N-2 products and with the pointer and `used_in` updates for the C claims.
- `evidence/modules/m1.json`, `m2.json`, `m3.json`: now carry the updated `derivation` and `used_in` of their own claims, and `m3.json` carries the revised m3-11.
- `evidence/modules/author.json` (new): au-1, au-2 (textbook Definition 1.2.1 and Theorem 1.2.1, p. 16), au-3 (the N-2 test fails exactly on the N!/2 labelled row graphs).
- Reproduce with: `cp evidence/evidence.base.json evidence/evidence.json`, then `python3 .claude/skills/research-paper/scripts/merge_evidence.py papers/adjacency-walks-connectivity`. I ran this; the result equals the merged file claim by claim (80 claims, same sources and contradictions). Claim order differs (author fragment first), content does not.
- m3-11: qualified, text corrected to printed pp. 7, 11, 12, 34, 61, and a `support` entry added with the search as locator. The quote in that entry is the textbook's definition of the adjacency matrix on p. 11 (the only quote available for the search; it does not quote the absence, which a quote cannot).

## 2. Findings, one line each

### Carried over from round 1

| Id | Action | Where |
|---|---|---|
| E5 | Fixed. "Loop" now means only a self-edge (Remark 2.2). Detours: Appendix A.5 plain words say "cut out the detour". Remark 4.13 says "The procedure makes N-2 matrix products"; Example 4.14 says "step 2 runs once". | A.5, 4.3 |
| R5 | Fixed as the evaluator asked. Sections 1.1 (Q3), 1.3 item 6, 2.2 (Remark 2.36) and 5 say: the assignment text is not reproduced; as reported by the user it states that in the course "path" means a walk with no repeated vertices; the answer to Question 3 rests on this statement. No quotation marks. | 1.1, 1.3, 2.2, 5 |
| R20 (E19) | Fixed. The print-order aside of Non-example 2.38 is in Appendix B ("A note on print order"); the pages-checked asides in 3.2 and 4.2 are "(Section 1.6)". | 2.2, 3.2, 4.2, App. B |

### Evaluator, new

| Id | Action | Where |
|---|---|---|
| E12 | Fixed. Printed pp. 7, 11, 12, 34, 61 in Section 1.6; m3-11 text and support entry corrected (Section 1 above). | 1.6, evidence |
| E13 | Fixed. 1.3 item 5 now says the paper keeps n_i and N, except that the textbook example graph keeps v_1 to v_5. | 1.3 |
| E14 | Fixed. Figure 3 caption says Fig. 1.2.5 also has the edge v1v5, which no example uses and the paper does not use; the sentence in Section 2 says "the ones that the textbook's own examples use". The v_1 label moved off its dot. | 2, Fig. 3 |
| E15 | Fixed. Section 3.2: Bai states the theorem for simple graphs; Grinberg (multidigraphs) and Lehman et al. (digraphs) are the more general ones. | 3.2 |
| E16 | Fixed. The 2 by 2 matrix in Remark 4.11 is displayed. | 4.2 |
| E17 | Fixed. Example 6.3: "no walk from vertex 1 or vertex 2 reaches vertex 3". | 6.3 |
| E18 | Fixed. See Section 1 above. | evidence |
| E19 | Fixed. "Step" now means only a move of a walk or a numbered step of a procedure: 4.1 says "the power one less than", 4.3 says "after each multiplication". A.5: "going by way of a third house". The aside items are under R20 above. | 4.1, 4.3, A.5 |

### Fresh reader

| Id | Action | Where |
|---|---|---|
| R23 | Fixed. The abstract names the photographs, "the board", and the assignment text before using them. | abstract |
| R24 | Fixed. New Appendix C describes the two photographs (content as in Table 1, the reflection, the legible parts) and says they are in `sources/`; they are not embedded. | App. C |
| R25 | Fixed. The forward reference now reads "(proved in Section 2.4: whether a path exists does not depend on the meaning of the word)". Each tag has a one-line operational meaning in Section 1.1 and the compound tag is explained. | 1.1 |
| R26 | Partly fixed. Table 2 is the single dictionary. Story words (trip, route, house, road) are removed from all non-box text outside Section 1.2, where the story is introduced; the plain-words boxes keep them. Examples that said "three houses in a row" now say "three vertices in a row"; the row graph is a named graph. | whole paper |
| R27 | Fixed. 1.3 item 4: the sources disagree on the edge 1-3, both B and T are used, no result depends on the choice. | 1.3 |
| R28 | Fixed. Section 2 names the definitions the three answers need and marks cycle, simple cycle and distance as context. | 2 |
| R29 | Fixed as the orchestrator directed. G_tb stays (the study-note standard needs the textbook's examples) and the seven edges are listed in the text; a graph of the paper's own, H (triangle with a pendant vertex, Figure 2), supplies a trail, a path, a non-trail, a non-cycle and a simple cycle. All H sequences are checked by script. | 2.2, Fig. 2 |
| R30 | Fixed. Half-sentence reasons added at Remark 2.2 (two different edges would need different pairs of ends), Remark 2.49 (a shortest walk contains a path no longer than itself, Lemma 2.52) and Remark 2.32 (a repeated vertex needs a closed trail, which needs three edges). | 2.1, 2.2 |
| R31 | Fixed. Proposition 2.59 is tagged "derived here from Lemma 2.52"; the source numbers moved into the proof's citation sentence. | 2.4 |
| R32 | Fixed. Remark 2.53 shows each cut as a displayed line with the removed detour in square brackets. | 2.3 |
| R33 | Fixed. The induction statement is P(k); a one-line example precedes the proof. | 2.3 |
| R34 | Fixed. Section 3.2 keeps one sentence; Appendix A.6 defines a case and gives graphs times exponents times pairs for 40, 360, 5120, 76800. | 3.2, A.6 |
| R35 | Fixed. Proposition 3.10(b) points to the matrix A^3 = 2A in Example 6.1 and states that (A^k)_12 doubles each time k grows by 2 while the path count is 1 then 0. | 3.4 |
| R36 | Fixed. The four sources are named in Section 3.4. | 3.4 |
| R37 | Fixed. The reason for stopping at N-1 is given with Lemma 2.52 and Corollary 2.54; the remark on mod-2 arithmetic has an example (for the triangle T, S has every off-diagonal entry 2, which is 0 modulo 2; checked by script). | 4.2 |
| R38 | Fixed. m is defined before the formula, A^0 = I is explained where formula (3) first appears, I and A commute because IA = AI = A, and Table 4 lists A^0. | 4.4, 1.4 |
| R39 | Fixed. Section 4.4 has the positivity argument in the body (positive coefficients, non-negative terms, walks of length at most m, Lemma 2.52 and Corollary 2.54, diagonal at least 1). | 4.4 |
| R40 | Fixed. Remark 4.19 states that in a connected graph every distance is at most N-1, and that a shortest path through all N vertices has no chord, so the graph is that path. | 4.5 |
| R41 | Fixed. Section 4.6 adds the reversal-and-joining sentence for BFS reachability. | 4.6 |
| R42 | Fixed. Definition 5.1 has no tag; the sentence under it says it is taken from the assignment text as reported by the user, with the textbook's Definition 1.2.13, and is not derived. | 5 |
| R43 | Fixed. Table 7 has the columns "Course (stated)" and "This paper"; "not stated" for every row except path. | 5 |
| R44 | Fixed. Section 7.4: about N^4 multiplications against about N + |E| operations. | 7.4 |
| R45 | Fixed. The eigenvalue sentence is deleted. | 7.2 |
| R46 | Fixed. "Module scripts" and "the paper's own script" are gone from Section 1.6 and Appendix A.7. Both say the reader must run the scripts, give the four commands, and give three small cases that can be checked by hand ((A^2)_13 = 1, (A^3)_12 = 2, row 3 of S for D). | 1.6, A.7 |
| R47 | Partly fixed. The full critique (quotes of Paramadevan and Sotheeswaran Theorem 1, the b_ij lines, Bai's sketch) is one paragraph in Section 7.2; Sections 1.6, 4.2 and 4.4 point to it. Section 3.4 keeps the single Theorem 1 sentence, because the warning is about that sentence and round 1 (R21) asked for it there. | 7.2, 3.4 |
| R48 | Fixed. A proof map opens Section 4. The reader's request to cut the plain-words boxes is not followed: the study-note register requires them (documented by the orchestrator). | 4 |
| R49 | Fixed. P_n and C_n carry a local note that n counts the vertices of the path or cycle; Table 4 now lists the relation symbol, the binomial coefficient and A^0. | 2.2, 1.4 |

## 3. Not fixed, with the reason

- Reader request to cut the plain-words paragraphs: not done; the study-note register requires them, as stated in the orchestrator's note to R48.
- R26 (story words only in boxes): kept in Section 1.2, where the story is told and Table 2 is introduced.
- R47: Section 3.4 keeps one quoted sentence (above).
- Nothing else is open that I know of.

## 4. What I still cannot justify beyond the sources

- Textbook numbers other than p. 16 come from the evidence file; I have viewed only p. 16 myself.
- The reading of the first board line's condition word as "if" (brief and C26).
- The textbook title in Latin letters (pdfLaTeX cannot print the Armenian), and six `n.d.` years.
- The verbatim assignment sentence (R5): the paper reports its content only, as the evaluator accepted.
- The statement that the textbook has no counting theorem or matrix test stays qualified: it rests on the pages checked and the full-text search.
- The support entry of m3-11 quotes a textbook sentence that is not itself the absence; the locator carries the search.

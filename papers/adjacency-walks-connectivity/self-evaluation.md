# Self-evaluation

Register: study-note. LaTeX is installed; `build.sh` exits 0 and produces an
18-page `main.pdf`. Claim ids (C, M1-, M2-, M3-, A-) are in `evidence/evidence.json`;
they appear only in this file, never in the paper text. One claim, A-1, was added in round 1 (`evidence/modules/author.json`, merged). Numbers in the paper are
recomputed by `appendices/computations.py` (output in
`appendices/computations.out.txt`).

Overlaps resolved as the orchestrator asked: the walk-to-path lemma with a length
bound is stated once (Lemma 3.2, `sections/paths.tex`) and Theorem 5.4 cites it;
the walk/trail/path agreement is stated once (Corollary 3.3); the proof of the
(I+A)^(N-1) form is in `appendices/derivations.tex`, which is where C24's
`derivation` field points (the field's wording "to be written" is stale but the
location is correct; I did not edit the base file).

## Section 1 Introduction (`sections/introduction.tex`)
Purpose: state the questions and their origin (board Q1, Q2; assignment text Q3),
fix the story and dictionary, list conventions, say what the sources contain.
- Board content and the three-versus-two edge mismatch: C1, C26, C28.
- Mark above A is k or n, reading k is an assumption: C27 (qualified, said so in text).
- Board V is textbook E; textbook G=(V,E): C1; printed pages = PDF minus one: source notes.
- Walk of length 0 is our choice, textbook silent: M2-2, M1-7 (qualified, said so).
- Five-town edge list read from page image: M2-5.
- Textbook search result (pages 7, 11, 12, 34, 61; no theorem, no test): C9 (qualified, stated as search result).
- Grinberg states multidigraph version; Paramadevan states the test: C4, C5, C22.
Conclusions: none beyond the roadmap. Not justified: Q3 "as reported" has no file; given as reported content, not quoted.

## Section 2 Background (`sections/background.tex`)
Purpose: definitions in the textbook's order, each with plain words, remark, example, non-example.
- Adjacent (1.1.4), adjacency matrix, zero diagonal, symmetric: C2, M1-1.
- Degree (1.2.1): C3; neighbours correspond to edges: M1-2.
- Walk 1.2.10, repeats allowed, vertex-sequence form: C10, M2-1.
- Closed walk 1.2.11: C11. Trail 1.2.12: C12, M2-3. Path = simple path 1.2.13: C13, M2-3, M2-11 (qualified).
- Cycle, simple cycle 1.2.14, 1.2.15; length at least 3: C14, M2-9. Distance 1.2.16: C15.
- Examples and non-examples on the five-town map: M2-5; all statuses recomputed in the computations output. d(n1,n3)=2 on the board map: M2 board example, M3-6.
Unjustified/limits: the textbook's Definition 1.2.13 is stated as trail with distinct vertices; the paper defines path as a walk with distinct vertices and relies on Proposition 3.1 for equivalence (stated in text). Textbook Definition 1.1.1 has no claim of its own, so "graph" is a paper definition with only the notation attributed (C1).

## Section 3 Question 3 (`sections/paths.tex`)
Purpose: the convention table; path/trail/walk facts used later.
- Table 2 conventions: C12, C13, M2-3 (Wikipedia and Grinberg only for English names).
- Prop 3.1 path implies trail implies walk, strictness: M2-4 (own proof; Grinberg leaves it as exercise).
- Lemma 3.2 walk contains path with bound: M2-6, C16, C17 (own proof by strong induction).
- Cor 3.3 three readings agree: M2-7, M3-1, C21 (trail step is ours); settles C19's qualifier.
- Prop 3.4 distance and N-1 bound: M2-8, C18.
- Example 3.5 board paths and distances: M2 board example (script part 8), M3-6.
Conclusion Q3 follows from Definition 2.8 plus Cor 3.3.

## Section 4 Question 1 (`sections/counting.tex`)
Purpose: matrix powers, properties, walk-counting theorem, walks versus paths.
- Prop 4.2 (a): C2; (b) M1-4; (c), (d): M1-2, C7 (Paramadevan p. 17 states (d)). Items are lettered so they do not clash with equation (1).
- Theorem 4.4 walk counting: M1-3, C4, C5 (own induction proof; textbook lacks it: C9).
- Example 4.5 and triangle matrices: M1-6, C28.
- Prop 4.6 walks not paths, counterexamples: M1-5, C8, C18.
- Table 3 five-town counts: M2-10 (script), M2-5.
- Paramadevan Theorem 1 "different paths": C6 (qualified). Text says it is incorrect as written under the course/English sense and agrees if read as "walk".
Conclusion Q1 follows from Theorem 4.4 (induction on k, premises: base case, step by splitting off the last vertex, A is 0/1).

## Section 5 Question 2 (`sections/connectivity.tex`)
Purpose: define connected and components, prove the test, give worked examples.
- Definition connected 2.1.1 and the board's wording: C19 (qualified then settled by Cor 3.3, M3-1).
- Components, Remark 2.1.1: C20, C21.
- Theorem 5.4 test: M3-3, C22 (qualified), C24 for the form; proof from Theorem 4.4, Lemma 3.2, Prop 3.4(c). N=1 excluded.
- Paramadevan's proof incomplete: C23 (qualified; marked as interpretation in text).
- Cor 5.5 (I+A)^(N-1): C24, M3-4; full proof in appendix; no source states it (said in text).
- Examples (matrices): M3-8; board matrix: C28. Cor 5.7 components: M3-5. Remark distance: M3-6. Sharpness: Proposition 5.12 with a proof, A-1 (derived; M3-7 is now only the computer illustration). Exhaustive check N<=6: M3-9 (experimental, said so).
- BFS paragraph (now before the computer check): M3-10, C25 (qualified). The "N-2 products" count is justified in one sentence and marked as our own; no timing claim is made.
Conclusion Q2 follows from Theorem 5.4 and Corollary 5.5.

## Section 6 Discussion, Section 7 Conclusion
Discussion (condensed in round 1) holds: what the results do not say, scope (loops, multigraphs, directed graphs in one sentence), the two statements of the published paper with quotations (C6, C22, C23, qualified), and the strength of the computer checks; the directed-graph remark is one sentence (cites C4). Claims about loops and multiple edges are explicitly not made. Conclusion answers Q1 to Q3 with pointers; no new claims.

## Appendices
A (`derivations.tex`): proof of Cor 5.5 (C24, M3-4). B (`provenance.tex`): sources read and pages viewed (from source notes), what is ours, how to rerun.

## Mechanical checks
- build.sh: ok. Two harmless overfull boxes (bibliography entry line, one appendix line of 0.8 pt).
- check_citations.py: 0 errors, 0 warnings. check_claims.py: 0 errors, 1 warning (C9 has no quote; it is an absence result and belongs to the base file).
- inspect_pdf.py: 0 errors, 1 warning (overfull boxes). No page is short except the last (19 lines, end of Appendix B); I rendered pages 1 to 18 at low resolution and saw no blank band; floats sit on or next to their text.
- check_plain_words.py with terms graph, vertex, edge, adjacent, adjacency, matrix, walk, trail, path, cycle, connected, component, distance, degree, length, power (and plurals): 30 plain-words paragraphs, 24 statements checked, 0 errors, 0 warnings. Plain-words paragraphs before worked examples were checked by reading.

## Unverified or qualified claims in the text
No unverified claims. Qualified claims, each disclosed in the text: C6, C9, C19, C22, C23, C25, C27, M1-7, M2-2, M2-11, M3-10.

## Could not justify or left open
- Whether the textbook admits walks of length 0 (not checked on the page).
- Whether the board mark is k or n; the lecturer's intent is not claimed.
- The textbook's edge list for Fig. 1.2.5 is my reading of a drawing.
- The (I+A)^(N-1) form has no source; only our derivation.
- The BFS cost comparison is unsourced and qualitative.
- Textbook title is transliterated in the bibliography because pdflatex has no Armenian font.

## Revision log, round 1 (technician pre-read)
All edits grepped across `sections/`, `appendices/`, `main.tex`. "The user" and "text layer" no longer occur in the reader's text.
- F1 (intro 1.1): added a sentence saying the note replies to lecture photos and an assignment and that the board content is reproduced; "user"/"us" removed; also in convention 1, 5 and Appendix B.
- F2: Q1 now reads "entry (i,j) of the k-th power"; the mark's uncertainty is only in convention 2.
- F3: pairs written (1,2),(2,3); drawing described in words with pointer to Fig. 1(b); extra 1-3 line named.
- F4: board's (G,V), A_ij = 1 if e_ij in V stated in full; V versus E explained.
- F5: edge list pointer to the Fig. 2 caption; says the examples need only the list; names the checks (the textbook's walk, trail, path, cycle examples).
- F6: Section 1.4 now says "searched the textbook's text for 'matrix'"; page list and source detail moved to Appendix B.
- F7: duplicate "round trip" sentence removed (cycle plain-words paragraph); Section 1.2 says story words are only an aid and never appear in statements or proofs.
- F8: worked line n1,n2,n3 (length 2) before Definition of walk.
- F9: Definition of path made self-contained; textbook comparison moved to Section 3.1, with a sentence there that the textbook's "trail with distinct vertices" and our definition agree by Prop. 3.1.
- F10: degree is now deg(n_i) everywhere; notation list says d(u,v) is distance.
- F11: both cases written in the proof of Prop. 3.1.
- F12: count of deleted vertices (b-a) and the example 1,2,3,2,4 -> 1,2,4 added to Lemma 3.2.
- F13: transpose defined; Prop. 4.2 items lettered (a)-(d); proof split into four lines; "(1) and (1)" removed.
- F14: step of Thm 4.4 cites Eq. (1) of Def. 4.1 and A^(k+1)=A^k A; items lettered so no clash.
- F15: proof of Prop. 4.7 split; both walks named with the edge each repeats.
- F16: caption of Table 3 explains how counts were obtained and the zeros (path bound 4; trail would need all 8 roads, none found by listing).
- F17: Section 4.5 now only points to Section 6; Section 6 quotes the source's Theorem 1 sentence and states the point is the word "path". Quote copied from the evidence quote of C6.
- F18: path list fixed.
- F19: equivalence class explained; reflexive, symmetric, transitive each justified (transitivity by joining walks and Cor. 3.3).
- F20: Remark 5.6 keeps only the technical point; the critique, with the quoted last line of the proof of Theorem 2 (C23), moved to Section 6, marked as interpretation.
- F21: sentence added in Section 5.2 and in Appendix A: binomial theorem needs commuting matrices, I commutes with all; N-1 is the same bound as in S.
- F22: remark replaced by Proposition 5.12 with a proof (index changes by 1 per step); new claim A-1; computer run kept as illustration.
- F23: BFS subsection moved before the computer check; BFS defined in a half-sentence there; the check says in words what the program compares.
- F24: BFS index renamed m (A_{mj}); N-2 products justified; stated that the section is a comparison and cross-check and no running-time claim is made.
- F25: Section 6 condensed; conventions and text-search repeats removed.
- F26: abstract: format sentence deleted; now says results are checked by computation on all graphs with up to 6 vertices.
- Overfull boxes: both gone (appendix wording changed; `\raggedright` in the bibliography and short bib note).
Checks after round 1: build ok; check_citations 0 errors, 0 warnings; check_claims 0 errors, 1 warning (C9 no quote, base file); inspect_pdf 0 errors, 0 warnings; check_plain_words 31 paragraphs, 25 statements, 0 errors, 0 warnings.

## Revision log, round 2 (evaluator E1-F1..F8 and reader R1-F1..F28)
The previous author's partial edits were checked finding by finding against the current files; only the gaps were edited.
Evaluator findings
- E1-F1 (major): done in the partial edits and verified: Remark 5.12 (`rem:distance`, connectivity.tex) cites Paramadevan Theorem 3 (p. 17, M3-11, qualified) and Section 2.2 item 7 (p. 16, M3-12), and says the proof via Lemma 3.2 is ours; it is not in "What is ours" in provenance.tex; discussion.tex says their item 7 counts walks, so "paths" in their Theorem 1 conflicts with their preliminaries. No other occurrence needed change.
- E1-F2: done earlier (convention 6 cites textbook p. 23 and p. 49). E1-F3: done (Definition 2.17 requires length at least 1; Remark 2.20 states why). E1-F4: done (Remark 5.6 says "In our reading ..."). E1-F5: done (Remark 4.2 in connectivity.tex and derivations.tex). E1-F6: done (introduction short answer says "length exactly k"). E1-F7: done ("XY = YX"; labelled graphs and 2^{N(N-1)/2}). E1-F8: done (@book with publisher; abstract reworded); the Figure 1 band was checked on rendered pages 1 to 3 and is not a blank band now. The DOI was not added, because it is not in evidence.json.
Reader findings
- R1-F1: short answers now explain walk and path in words and use no story word. F2, F3, F4, F5, F6: done in convention 2 to 6 (V means edge set; the ambiguity is harmless; Fig. 1(b) is a side example; uses of length 0 listed; nothing depends on matching the textbook). F7: added one sentence in Remark 2.20 that a cycle here is only a closed trail (background.tex). F8: done in Definition 2.15. F9, F10: done in Section 3. F11: textbook paragraph removed from 3.2. F12, F13, F14: done (sentences in Remark 4.2 and after Proposition 4.3, hand-checked entry). F15: caption of Table 3 now names the program computations.py (counting.tex) and the Euler-trail reason is in the text. F16: forward paragraph removed. F17, F18: done (Lemma split; "up to one road less than there are towns"). F19: the commuting binomial theorem is now proved in Appendix A, so no outside reference is needed; Example 5.8 check is cited. F20, F21, F22, F23: done. F24: Appendix B says which program does what. F25: Section 1.4 says the textbook numbers only match names. F26: "stay-at-home" and "endless" are in Table 1. F27: edge index is s; t is the middle index. F28: forward references say "proved in Section 3" and "stated below".
- Small extra edits: sentence in introduction.tex 1.4 reworded; bib notes say "supplied with the assignment" instead of "the user".
Checks after round 2: build ok (20 pages; last page has 5 lines of Appendix B); check_citations 0 errors, 0 warnings; check_claims 0 errors, 1 warning (C9, no quote); inspect_pdf 0 errors, 0 warnings; check_plain_words 0 errors, 1 warning (connectivity.tex:31, 21-word sentence in a story paragraph; kept, since it is the transitivity rule and splitting it loses the chain).

## Revision log, round 3 (E2-F1..F7, R2-F1..F29)
Changed sections: introduction, paths, counting, connectivity, Appendices A and B, abstract (main.tex). No new claims; no evidence change.
Evaluator findings
- E2-F1: Q1 short answer now defines a walk as a sequence of vertices joined by edges (no story word). E2-F2: convention 1 uses edge and vertex; paths.tex proof of Prop. 3.1 and counting.tex proof of Prop. 4.6 and the Euler argument use graph, edge, vertex; the rule sentence now says story words are not used in definitions or theorem statements. E2-F3: Appendix B says Section 2.2 (item 7) and Section 3.1. E2-F4: C(N-1,k) explained at first use (Cor. 5.8 sketch). E2-F5: "triangle" defined, and the reason for (A^2)_12 = 0 stated. E2-F6: Table 1 position claim removed; both floats now [htbp]; the Figure 1 band under the labels is small, and page 1 still ends with white space because the table moves to page 2 (accepted). E2-F7: the (A^3)_12 hand check moved to the board-matrix paragraph.
Reader findings, done
- R2-F1: abstract says what a walk is, defines n_i as the i-th vertex, and says the course "path" is the usual English meaning. R2-F3: "defined in Section 2 or, for connected, in Section 5"; "no zero outside the main diagonal" explained. R2-F13: "a repeated edge forces a repeated vertex" added to the proof of Prop. 3.1. R2-F14: Lemma 3.2 example written with n_i and the u-indices. R2-F15: Section 3 intro lists four facts including Cor. 3.3. R2-F16: sentence corrected ((c) is used to prove (d); only (b) is not used). R2-F17: transpose rule named standard; induction on k. R2-F18: disjointness of the groups of walks stated. R2-F19: Prop. 4.6 says the entry can be positive when no path or trail of that length exists. R2-F20: Euler trail named; the non-monotone trail counts said to come from the program. R2-F21: coefficient defined at first use. R2-F22: Appendix A says "by induction on m". R2-F23: sentence on why powers are summed. R2-F25: path graph explained as a chain, not a single path. R2-F27: Table of connected-graph counts (tab:exhaustive) added; text says what the program prints. R2-F29: Appendix B says which program backs which section. R2-F18 and others were grepped; no other occurrence.
- Plain-words warning at connectivity.tex:31 removed by splitting the sentence; check_plain_words now 0 warnings.
Reader findings, declined (required by the brief or a reader-position preference)
- R2-F2 (board transcription is required, kept); F4 (the three-convention table is required; only its position claim was fixed; story layer is required); F5, F6 (board mismatch report required; wording kept as it is clear after round 2); F7 (board notation mismatch is required); F8 (the textbook support for length-0 walks answers E1-F2); F9, F10 (textbook provenance and the search result are required and qualified); F11 (cycles are in the brief's required definitions); F12 (textbook numbering and the table are required); F24 (the Paramadevan remark is the E1-F1 fix and stays); F26 (BFS section is required by the brief); F28 (the published-paper discussion is required).
Checks after round 3: build ok, 20 pages; check_citations 0 errors, 0 warnings; check_claims 0 errors, 1 warning (C9 no quote); inspect_pdf 0 errors, 0 warnings; check_plain_words 0 errors, 0 warnings.

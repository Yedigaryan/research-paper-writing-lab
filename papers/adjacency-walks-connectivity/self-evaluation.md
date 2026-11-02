# Self-evaluation of the paper author

Paper: `papers/adjacency-walks-connectivity/`. Register: study-note. Claim ids are those in `evidence/evidence.json` (module fragments `m1`, `m2`, `m3`, `author`; merged from `evidence.base.json` plus fragments by `merge_evidence.py`, reproduced identically). Nothing in the reader's text carries these ids; they appear only here.

Build status: `build.sh` ok (22 pages after round 1, TeX Live, biber, latexmk present, so exit 0, not 2). `check_citations.py`: 0 errors, 2 warnings (evidence sources `lehman2017mcs` and `ntnugraphsearch` are not cited; no claim in the paper needs them). `check_claims.py`: 0 errors, 0 warnings (64 supported, 24 qualified, 0 unverified after round 1). `inspect_pdf.py`: 0 errors, 0 warnings. Biber prints 9 informational warnings that `year = {n.d.}` is not an integer for sources whose year is null in the evidence file; the bibliography uses `sorting=none`, so nothing is mis-sorted. All year fields that are known are copied; unknown ones are written `n.d.` because `check_citations.py` requires a year or date field.

Numbers: every matrix in the text is a macro in `appendices/generated-matrices.tex`, written by `appendices/scripts/paper_computations.py` (output saved in `paper_computations_output.txt`). Matrices were not typed by hand. The matrices also agree with the module scripts' outputs (checked: board A^1..A^4, triangle A^1..A^4, connected and disconnected B and R).

## Evidence added

`evidence/modules/author.json` adds source `paperscript` and claims A-4 (round 1: the textbook writes G = (V, E) on p. 9 and defines a_ij through adjacency on p. 11, with the page-11 quote copied from the page image; supported) and A-5 (round 1: Paramadevan's and Bai's two statements about paths, with verbatim quotes; qualified), plus A-1 (experimental: graph H, its matrix and the classification of the example sequences; supported), A-2 (derived, qualified: N = 1 case of the test), A-3 (derived, supported: adding powers beyond N - 1 is harmless). None is `unverified`.

## Section by section

### 1 Introduction (`sections/introduction.tex`)

Purpose: say where Q1, Q2, Q3 come from, fix the story and its dictionary, give the short answers, say what the textbook does and does not contain, and give the organisation.

Claims and support:
- The board shows N nodes, the adjacency matrix, two questions and the definition of connected without a definition of path: C2, C6 (whiteboard1). Supported.
- The mark above A is ambiguous: C3 (qualified), handled as Convention 2.2.
- The third question and the meaning of path come from the assignment text: reported content, not a source; recorded in Conventions 2.1 and 2.5 (C36 qualified, C-m2-10).
- The textbook's adjacency-matrix hits (table of contents, printed pp. 7, 11, 12, 34, 61) and "the pages viewed contain neither the theorem nor the test": C15 (qualified) and M1-10 (qualified, p. 7). Phrased as a search result, partial read stated.
- Lecture notes state the theorem and the test: C16, C43, C44.

Conclusions: the short answers to Q1, Q2, Q3 restate Theorem 5.1, Theorem 6.10 and Definition 3.35; premises are in those sections.

Could not justify: nothing here beyond the qualified claims above. The page list for p. 7 is from M1-10, whose only viewed page was p. 7 itself; I did not view the others.

### 2 Notation and conventions (`sections/conventions.tex`)

Purpose: one notation list, and seven numbered conventions where the board, the assignment text and the textbook leave a choice.

Claims and support:
- Board letters n_1..n_N, N, textbook v_1..v_n: whiteboard1, C10 (p. 11 quote uses v_1..v_n).
- Convention 2.1 (finite simple undirected): assignment text; consistent with C4 (symmetric, zero diagonal). The remark that directed graphs break symmetry is a derived one-sentence remark (no separate claim; M1-9 is not cited).
- Convention 2.2 (mark is exponent k): C3, qualified; premise is the assignment text.
- Convention 2.3 (board's V is E): C1, C7 (qualified), C8.
- Convention 2.4 (matrix is the example graph): C5 and the brief's decision; board problem statement C2.
- Convention 2.5 (path means no repeated vertex; trail for 1.2.12): C26, C27, C36 (qualified).
- Convention 2.6 (length 0): C-m2-06 (qualified), Grinberg Definition 2.9.1(a) (C32).
- Convention 2.7 (printed pages): graph-sources.md and the source notes.

Could not justify: that the assignment text says what I report it says, beyond the orchestrator's brief (sections 1, 7). It is given as reported content, with no quotation marks.

### 3 Background (`sections/background.tex`)

Purpose: the definitions in the textbook's order, each preceded by a plain-words paragraph and followed by a remark, an example and a non-example.

Claims and support:
- Definition 3.1 graph (1.1.1, p. 9), remark on antireflexive symmetric relation: C8, C-m2-05.
- Adjacent (1.1.4): C9. Adjacency matrix: C10, C11, C1. Degree (1.2.1): C12. Euler (Theorem 1.2.1): C13, cited, not reproved.
- Proposition 3.18 on A (symmetric, zero diagonal: C11; row sum = degree: proved here, M1-1, which replaced C14; sum of entries = 2|E|: proved from C13, part of M1-3 spirit).
- Walk (1.2.10): C23, C24; vertex-sequence remark: C-m2-05, M1-6; the textbook's own length-eight example: C-m2-08.
- Closed walk: C25. Trail (1.2.12): C26. Path (1.2.13): C27, and "a path with k edges has k+1 vertices" is immediate. Path between n_i and n_j: C36, C-m2-10 (qualified). Cycle and simple cycle (1.2.14, 1.2.15): C28, C29; "closed trail has length 0 or at least 3" and "the board graph has no cycle": C-m2-06 (qualified, derived in the text). Distance (1.2.16): C30.
- Every example and non-example about graph H, and the board-graph examples, were classified by script: A-1 (experimental), plus the m2 script's Part 1 for the textbook's own examples (not reused).

Conclusions: none beyond the definitions.

Round 1: the false general statement in the simple-cycle non-example was replaced by the evaluator's correction (a non-simple cycle needs two cycles with no common edge sharing a vertex; H has one cycle, checked by the script). The definition of graph says "unordered pair of different vertices"; "different" is taken from the textbook's antireflexive-relation remark (C-m2-05), not a verbatim quote, and the paper no longer mentions that remark.

### 4 Question Q3 (`sections/paths.tex`)

Purpose: answer Q3 by pointing to Definition 3.35, add the convention comparison, and prove Lemma 4.2 (walk contains path, length bound), Lemma 4.4 (path is trail), Proposition 4.5 (three readings), Proposition 4.8 (length bound), Proposition 4.9 (distance). m2 owns these; this section is the single place where they are proved, and Sections 5 and 6 cite them. (Numbers below are the compiled ones; one counter per section is shared by all environments.)

Claims and support:
- Table of three conventions: C26-C29, C38, C-m2-07 (qualified: the word trail rests on Wikipedia, partial access, tertiary); Grinberg Definition 2.9.1(a) and (c) (C32, C38). Bai's fourth reading: C38 (Bai p. 1).
- Lemma 4.2: derived, C-m2-01; statement also in textbook Lemma 1.2.1 (C31, u different from v, no bound) and Grinberg Corollary 2.9.7 (C33). Proof by strong induction, in the text. Script check on all labelled graphs with at most 5 vertices: `appendices/scripts/m2_paths.py` (output saved; 0 violations); it is mentioned only in the appendix.
- Lemma 4.4, Proposition 4.5: derived, C-m2-02, C-m2-03, C37 (qualified in the base file; its proof is C-m2-03). Grinberg Proposition 2.9.10 covers only walks and paths (C34).
- Proposition 4.8: derived, C-m2-04, C35 (Grinberg p. 40, Gotti p. 2).
- Proposition 4.9 and Remark on the textbook's three properties: derived, C-m2-04; the properties are listed in C30.

Conclusions: the textbook's definition of connected (which uses the trail) and the course reading (no repeated vertex) define the same connected graphs: premises Lemma 4.2, Lemma 4.4, Proposition 4.5; this resolves the base-file contradiction between C39 and C36.

Could not justify: the closed-trail and cycle rows of the table have "not compared" in the English column because no read source names them.

### 5 Question Q1 (`sections/walkcount.tex`)

Purpose: answer Q1: Theorem 5.1 with a full induction, properties of A^k, the board example, the drawing-versus-matrix report, and the warning that walks are not paths.

Claims and support:
- Theorem 5.1: derived (M1-2); statement in Galway Theorem 1.1.3, Bai Theorem 1, Gotti Proposition 2 (C16, C17). The textbook has no such theorem (C15, qualified).
- Remark on k = 0: M1-11, C-m2-06 (qualified).
- Proposition 5.3 (nonnegative integers, symmetric, (A^2)_ii = degree, trace = 2|E|): derived, M1-3; (A^2)_ii also in Galway p. 4 (C20).
- Board matrix powers A^2, A^3, A^4 and the walk table: M1-4, M1-5, A-1-style script output in `paper_computations_output.txt`; each entry agrees with brute-force enumeration for k = 1..4.
- Drawing against matrix, edge by edge: C4, C5 (reading of the drawing has medium confidence, said in the text). Triangle matrices and the comparison: M1-8 (qualified).
- Walks, not paths, with the three counterexamples: C19 (Bai), C20, C21, M1-5. Count equals path count for k = 2, i different from j: M1-7 (proved in the text).
- Paramadevan Theorem 1 is incorrect as worded: C22.

Conclusions: (A^k)_ij counts walks (Theorem 5.1, by induction); it does not count paths (counterexamples computed by script: (A^2)_11 = 1, (A^3)_12 = 2, A^4 not zero with N - 1 = 2).

Could not justify: what the lecturer meant by the arrowhead and the extra line. The paper says it cannot be settled from the photos.

### 6 Question Q2 (`sections/connectivity.tex`)

Purpose: textbook Definition 2.1.1 and components; Lemma 6.9 (pair criterion); Theorem 6.10 (four equivalent forms) with full proof; corollaries (components via R, distance via least k); two worked examples; breadth-first search paragraph; a finite check.

Claims and support:
- Definition 2.1.1, component, Remark 2.1.1, Figures 2.1.1 and 2.1.2: C39, C40, C41, m3-C8, m3-C9 (qualified). Board definition: C6.
- Pair criterion and the test: derived, m3-C4, C46 (qualified in the base file; proved here), C45 (sum form and (I+A)^(N-1) form equivalent; proved here). The statement is in Gotti Proposition 3 and Bai Theorem 2 (C43) and Paramadevan Theorem 2 (C44, qualified: statement only). The remark that Bai's proof sketch and Paramadevan's proof are not complete: C47, C44 notes.
- N = 1 case: A-2 (qualified).
- Limits (a single power is not enough; exponent N - 1 cannot be lowered; larger powers allowed): m3-C12 (experimental, script), A-3 (derived). The odd-length explanation for (A^2)_12 = 0 is derived in the text from the bipartition {n_1, n_3}, {n_2}.
- Corollaries 6.13 and 6.14: m3-C6, m3-C7 (derived).
- Examples: m3-C12 and `paper_computations_output.txt`; both agree with `m3_examples_output.txt`.
- BFS: m3-C1, m3-C2 (Waterloo slides 8 to 10), m3-C3 (proof in the text), cost remark m3-C10 (estimate, qualified, marked as the paper's own estimate).
- Finite check on all labelled graphs N = 2..6: m3-C11 (experimental, supported).

Conclusions: G is connected iff (b), (c), (d) hold. Premises: Theorem 5.1 (entries count walks), Lemma 4.2 (walk contains path), Proposition 4.8 (path length at most N - 1), Proposition 4.5 (readings agree), the binomial theorem for I and A, nonnegativity of entries (Proposition 5.3).

Could not justify: BFS correctness rests on one lecture deck (secondary) plus my own proof of the connectivity step; no algorithms textbook was accessed. The cost estimate is mine.

### 7 Discussion, 8 Conclusion (`sections/discussion.tex`, `sections/conclusion.tex`)

Purpose: scope limits, open readings, source quality; direct answers to Q1 to Q3.

Claims: restate earlier results; the multigraph/loop statements in the scope bullet (entries become multiplicities; a vertex sequence no longer determines a walk) are from m2's limitations section and are not in the evidence file; they are phrased as "we did not work these cases out" and carry no citation. This is the one set of unsupported general remarks in the paper (see below).

### Appendix A provenance (`appendices/provenance.tex`)

Purpose: sources, what was read, how to rerun. Statements about the pages viewed follow the source notes in the evidence file (petrosyan2015graph, wikipedia2026path). Scripts are in `appendices/scripts/`; copies of the module scripts are byte-identical to `modules/scripts/` (m2_paths, m3_examples, m3_exhaustive_check); outputs were regenerated by me for m3 scripts.

## Anything I could not justify

1. (Round 1: resolved.) The multigraph and loop scope remark is now one sentence, in Convention 2.1 only.
2. (Round 1: resolved.) The simple-cycle non-example is corrected.
3. The reading of the board drawing is medium confidence (C5). The reading of the mark above A is qualified (C3). Both are said in the text.
4. The English-column entries for closed trail and cycle are "not compared".
5. The word trail rests on one tertiary source (partial access).
6. The textbook was read in part; the "no theorem, no test" statement is the result of a search and of viewed pages, not of a full read.
7. The paper cites no source for the assignment text; it is described as reported content.
8. Evidence sources `lehman2017mcs` and `ntnugraphsearch` are unused.
9. `year = {n.d.}` in the bibliography for sources with unknown year (biber informational warnings).

## Per-finding log, round 1

Evaluator findings are E1-n (F1 to F15 of `paper-evaluator-round1.md`), reader findings are R1-n (F1 to F42 of `reader-findings.md`, Round 1). New numbers are the compiled ones. None is marked resolved by me.

Section 1 (introduction): E1-5 changed (Table 1 and every plain-words paragraph say "number of drives"; "size" removed in all sections). E1-9 changed (identity matrix and off-diagonal glossed at first use in the Q2 bullet). R1-1, R1-2 changed (Q1 stated with row, column and k-th power; the road table and the board matrix given in plain words in Section 1.2). R1-3 changed with E1-9. R1-4 changed (the search account moved to Appendix A; one sentence left in the introduction, qualified "as far as a search shows"). R1-5 changed (rule replaced by a two-sentence plain rule). Clause on the convention for path added.

Section 2 (conventions): E1-1 MAJOR changed. Convention 2.3 now says the textbook writes G = (V, E) (p. 9) and defines a_ij through adjacency (p. 11), citing the new claim A-4, whose Armenian quote was copied from the page image I viewed (printed p. 11); the e_ij form is stated as the board's. E1-13 changed (loops, repeated edges and directed graphs: one sentence, in Convention 2.1; the Discussion bullet and the "symmetry does not carry over" sentence were removed). R1-6 changed (textbook v_i remark and forward reference removed). R1-7 MAJOR changed (Figure 1, a labelled redraw of the board with the rule, the drawing with its arrowhead, the matrix and the Q1 mark; a redraw, not the photo, and it says so). R1-8 changed (Convention 2.6 in plain terms).

Section 3 (background): E1-3 MAJOR changed (Non-example 3.42 uses the evaluator's correction; H's single cycle checked by the script). E1-4 MAJOR changed for this file (Table 1 and the ring-trip plain paragraph and Figure 1 caption use "ring trip"; "loop" now means only a self-edge). E1-5 changed. E1-6 changed (plain-words paragraphs before Theorem 3.17 and Proposition 3.18). E1-7 changed (the plain paragraphs before trail and path no longer use the word path; the naming sentence sits in the formal definition). E1-11 changed (Remark after the path definition now says the trail condition is automatic by Lemma 4.4, so Definition 3.35 may drop it). R1-9 changed (pointer to Appendix A and what the script does). R1-10 changed (antireflexive sentence deleted). R1-11 changed (side-fact note after Euler's theorem). R1-12 not changed: the repository rule puts a definition before its remark and example, and the textbook does the same; Example after Definition 3.19 gives a concrete walk at once. R1-13 changed in part (roadmap says cycles are included for completeness; Non-example fixed); cycles are kept because the brief asks for the cycle definition. R1-14 MAJOR changed (distance is stated as the least length of a walk, the fewest drives; the textbook's trail wording is cited and Proposition 4.9 is cited for the agreement). R1-41 changed (roadmap at the start of Section 3).

Section 4 (paths): E1-4 MAJOR changed (subsection title "Cutting closed walks out of a walk"; plain words say "round trip"; Example 4.7 says "closed walk"). E1-6 changed (plain words moved above Lemma 4.4). E1-7 changed (plain words before the naming table have no word path). R1-15 changed (the "not compared" cells are dashes, the fourth-reading sentence deleted; the sources note for trail kept). R1-16 changed (Remark 4.1 restates the textbook definition in one line). R1-17 changed (worked cut inserted). R1-18 changed (reason added). R1-19 changed (slip fixed: the three sets are nonempty together, or all empty). R1-20 changed ("implies"). Bai's definition of path was removed from the text; claim C38 stays in the evidence file unused there.

Section 5 (walk count): E1-8 changed (sentence split). E1-9 changed (transpose glossed). E1-6 changed (plain words before Proposition 5.3). R1-21 MAJOR changed (formula for (A^{k+1})_{ij} stated at the start of the induction step). R1-22 changed (list). R1-23 changed (transpose defined; (2) and (4) kept, flagged as side facts). R1-24 changed (Table 3 says values are read off the printed matrices). R1-25 MAJOR changed (Section 5.3 refers to Figure 1 and says plainly that the drawing has three roads and the matrix two; the old right half of the board-graph figure was deleted, which also removes the blank band of E1-14). R1-26 changed. R1-27 changed (reason added to counterexample 3). R1-28 changed (the Paramadevan remark moved to Section 7 and attributed with exact quotes).

Section 6 (connectivity): E1-9 changed (binomial coefficient, commuting, induced subgraph and union-find glossed). E1-10 changed (Definition 6.5 says trail, "notes", and cites Proposition 4.5 for the course reading). E1-12 changed (Figure for G'; examples point to Figure 3 and Figure 4 by label). E1-13 changed (BFS is now one paragraph plus the plain-words paragraph; the proposition, the separate proof and the cost remark were removed, so claims m3-C3 and m3-C10 are no longer used as separate statements; the connectivity step is given in three sentences in the paragraph). R1-29 MAJOR changed (why R is introduced; "of B" replaced by "of the powers of A"). R1-30 MAJOR changed (source critique removed from the theorem area; one sentence points to Section 7). R1-31 changed (the garbled "Takea position" text was a PDF-extraction artefact of "Take a position"; reworded "Fix a pair"; commuting glossed; (b) cited only). R1-32 changed (N = 3 stated). R1-33 changed (one-line argument). R1-34 changed. R1-35 changed (R = I + 2A + A^2). R1-36 changed (diagonal remark deleted). R1-37 changed in part (to-do list defined; section marked optional; the cost arithmetic was removed with the cost remark for the scope reason in E1-13). R1-38 changed.

Section 7 (discussion) and 8 (conclusion): E1-2 MAJOR changed (the invented quotation removed; Paramadevan's "number of different paths of length less than n from the vertex i to j" [p. 17, proof of Theorem 2] and Bai's "(I + A)^{n-1} aggregates all paths of length <= n-1" [p. 2] are quoted separately, verbatim, with claim A-5; the Paramadevan sentence was checked against the downloaded article text). E1-13 changed. R1-39 changed (merged with the source critique, now in one place). R1-40 changed ("eigenvalue methods" deleted). R1-42 changed (the triangle is mentioned in the Q2 bullet).

References and layout: E1-14 changed in part. The textbook's year is now in its normal position (publisher, location, year fields). The Figure 2 blank band is gone and the Table 3 header is "Paths". The undated sources still carry `year = {n.d.}`: `check_citations.py` requires a year or date field, and writing a made-up date would be wrong, so I kept "n.d."; biber still prints its informational warnings. E1-15: not changed. `lehman2017mcs` is metadata-only and `ntnugraphsearch` is tertiary and superseded by the Waterloo slides; neither supports a claim in the paper, so I left them uncited and in the evidence file.

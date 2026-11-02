# Self-evaluation of the paper author

Paper: `papers/adjacency-walks-connectivity/`. Register: study-note. Claim ids are those in `evidence/evidence.json` (module fragments `m1`, `m2`, `m3`, `author`; merged from `evidence.base.json` plus fragments by `merge_evidence.py`, reproduced identically). Nothing in the reader's text carries these ids; they appear only here.

Build status: `build.sh` ok (21 pages, TeX Live, biber, latexmk present, so exit 0, not 2). `check_citations.py`: 0 errors, 2 warnings (evidence sources `lehman2017mcs` and `ntnugraphsearch` are not cited; no claim in the paper needs them). `check_claims.py`: 0 errors, 0 warnings (63 supported, 23 qualified, 0 unverified). `inspect_pdf.py`: 0 errors, 0 warnings. Biber prints 9 informational warnings that `year = {n.d.}` is not an integer for sources whose year is null in the evidence file; the bibliography uses `sorting=none`, so nothing is mis-sorted. All year fields that are known are copied; unknown ones are written `n.d.` because `check_citations.py` requires a year or date field.

Numbers: every matrix in the text is a macro in `appendices/generated-matrices.tex`, written by `appendices/scripts/paper_computations.py` (output saved in `paper_computations_output.txt`). Matrices were not typed by hand. The matrices also agree with the module scripts' outputs (checked: board A^1..A^4, triangle A^1..A^4, connected and disconnected B and R).

## Evidence added

`evidence/modules/author.json` adds source `paperscript` and claims A-1 (experimental: graph H, its matrix and the classification of the example sequences; supported), A-2 (derived, qualified: N = 1 case of the test), A-3 (derived, supported: adding powers beyond N - 1 is harmless). None is `unverified`.

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

Could not justify: the non-example for simple cycle says "a cycle that is not simple needs two triangles that share a vertex": true by inspection for graphs this small but not proved in the text and not scripted (stated for H only: "H has only one triangle"). The script confirms the only closed trails of length 3 in H are the triangle's. Also, definition of graph says "unordered pair of different vertices": the textbook states it as unordered pairs plus an antireflexive relation remark; "different" is therefore taken from C-m2-05, not a verbatim quote.

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

1. Multigraph and loop remarks in Section 7 (not in the evidence file; qualified in the text, uncited).
2. "A cycle that is not simple needs two triangles sharing a vertex" (Section 3, non-example): true by inspection in the setting of H, not proved in general.
3. The reading of the board drawing is medium confidence (C5). The reading of the mark above A is qualified (C3). Both are said in the text.
4. The English-column entries for closed trail and cycle are "not compared".
5. The word trail rests on one tertiary source (partial access).
6. The textbook was read in part; the "no theorem, no test" statement is the result of a search and of viewed pages, not of a full read.
7. The paper cites no source for the assignment text; it is described as reported content.
8. Evidence sources `lehman2017mcs` and `ntnugraphsearch` are unused.
9. `year = {n.d.}` in the bibliography for sources with unknown year (biber informational warnings).

## Per-finding log

No revision round yet.

# Self-evaluation

Register: study-note. LaTeX is installed; `build.sh` exits 0 and produces an
18-page `main.pdf`. Claim ids (C, M1-, M2-, M3-) are in `evidence/evidence.json`;
they appear only in this file, never in the paper text. No claim was added to
the evidence file (no `author.json` fragment was needed). Numbers in the paper are
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
- Prop 4.2 (1): C2; (2) M1-4; (3), (4): M1-2, C7 (Paramadevan p. 17 states (4)).
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
- Examples (matrices): M3-8; board matrix: C28. Cor 5.7 components: M3-5. Remark distance: M3-6. Sharpness: M3-7 (experimental, said so). Exhaustive check N<=6: M3-9 (experimental, said so).
- BFS paragraph: M3-10, C25 (qualified). Cost remark "N-2 products" is marked as our own count, unsourced.
Conclusion Q2 follows from Theorem 5.4 and Corollary 5.5.

## Section 6 Discussion, Section 7 Conclusion
Discussion restates limits; the directed-graph remark is one sentence (cites C4). Claims about loops and multiple edges are explicitly not made. Conclusion answers Q1 to Q3 with pointers; no new claims.

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

# Self-evaluation (author), round 0

Build status (round 0, superseded by round 1 below): `build.sh` exited 2 because no
LaTeX toolchain was installed. In round 1 the paper compiles (21 pages). I checked by script that every `\begin` has its `\end`, that braces
and dollar signs balance, and that every `\ref` and `\cref` has a label. That
is not a compile; TikZ, `cleveref`, and `biblatex` behaviour is untested.
`main.pdf` does not exist, so `inspect_pdf.py` could not run (exit 1, "main.pdf
not found"). The orchestrator decides how to proceed.

Other checks, run from the repository root:

- `check_citations.py`: 11 cited keys, 11 bib entries, 11 evidence sources,
  0 errors, 0 warnings.
- `check_claims.py`: 0 errors, 10 warnings, all inherited from the evidence
  files (supports without a quote for photos and the summary file; m2-14 is
  unverified and is qualified in the text, see below).
- `check_plain_words.py --terms walk,path,trail,cycle,vertex,vertices,edge,adjacent,matrix,entry,graph,connected,component,length,degree,power,diagonal,distance`:
  34 plain-words paragraphs, 28 statement environments, 0 errors, 0 warnings.

Evidence changes I made: `evidence/modules/author.json` adds claims a1 to a4
(computed examples; distance from powers). `evidence/evidence.base.json` marks
C53 `removed` (superseded by m3-1 to m3-4); `evidence.json` was rebuilt with
`merge_evidence.py`. New scripts in `scripts/`: `walks_check.py` (mine),
`walk_path_lemmas.py` (a copy of `modules/m2-check.py`), plus recorded outputs
`scripts/output-*.txt`. Every matrix printed in the paper comes from
`walks_check.py` or `m3_connectivity.py`.

Orchestrator decisions followed: "path" is vertex-distinct throughout;
length 0 is the paper's own convention (Convention 6); m2 Proposition 2.4 and
m3 Lemma M3.6 are stated once, as Proposition `prop:together`
(Section 3), and the connectivity section cites it; BFS cites m3-1 to m3-4,
not C53.

Claim ids are used only in this file, never in the paper text.

## Section 1 Introduction (`sections/introduction.tex`)

Purpose: say where Q1 to Q3 came from, fix conventions where the board, the
assignment summary, and the textbook disagree, fix the story and dictionary,
and give the answers in brief.

Claims and support:

- Board content: rule for A_ij (C1, m1-1), 3 by 3 matrix (C3, m1-2), problem
  statement (C4), Q2 (C6), definition of connected (C7). Photos viewed as
  images.
- Q3 and the setting, as reported (C8, C9, m2-12; qualified, the summary is
  not the user's words). Stated as reported content, no quotation marks.
- Convention 2 names: board V is the edge set; textbook writes uv and never
  e_ij (C11, m1-22).
- Convention 3 mark above A: could not be resolved; read as k (C5, m1-4;
  qualified interpretation).
- Convention 4 drawing against matrix (C2 qualified, m1-3 qualified).
- Convention 5 path words: C20, C21, C8.
- Convention 6 length 0 (C26, m1-17, m2-11, C47): marked as the paper's own
  convention.
- Convention 7 textbook absence: C30, m1-9 (search result, qualified; pp. 7
  and 11 read, hits on 12, 34, 61 not read for this paper).
- Answers in brief: restate Theorems `thm:counting`, `thm:sum`, `thm:power`
  and Definition `def:pathbetween`; premises are in those sections.

Conclusions: none new. Not justified: the first paragraph's informal
description of a graph and the "why it matters" paragraph carry no citation;
they are motivation, not claims about sources.

## Section 2 Graphs and the adjacency matrix (`sections/background.tex`)

Purpose: notation first (as the textbook does), then Definitions 2.1 to 2.4
in build order with a plain-words paragraph, remark, example, non-example
each; Proposition 2.5; the matrix product and powers.

Claims and support:

- Graph (C10), adjacent (C12, m1-6), adjacency matrix (C13, m1-5; board form
  C1), degree (C15, m1-7; book defines it after A), Euler Theorem 1.2.1 (C16,
  m1-8).
- Proposition 2.5 (symmetric, zero diagonal, row sums are degrees, total
  2|E|): derived (m1-10, m1-11), own proof; premises: Definition 2.3, 2.4,
  Euler's theorem. Statement of items 1 and 2 also in Galway (C33).
- Matrix product and powers: standard linear algebra definition, marked as
  such; the remark that entries of A^k are non-negative integers is an
  induction-free observation (sums and products of non-negative integers),
  used in the sum test.

Not justified: nothing. Note that the textbook's Definition 1.1.1 is quoted
only as "ordered pair (V, E)"; the "simple, finite, undirected" restriction is
Convention 1, not the textbook's.

## Section 3 Walks, trails, paths, and cycles (`sections/walks.tex`)

Purpose: answer Q3 by the numbered Definition 3.5, in the textbook's build
order (Definitions 1.2.10 to 1.2.16); table of the three naming conventions;
the lemmas that later sections use.

Claims and support:

- Definitions 3.1 to 3.4, 3.6, 3.7 with textbook numbers: C17, C18, C19, C20,
  C21, C22, C23, C24. Cycle length at least 3 and the C_n remark: m2-8. Two
  triangles sharing a vertex: m2-13, a script check (`walks_check.py`).
- Definition 3.5 (path between n_i and n_j): the textbook's 1.2.13 with ends
  fixed (C21, m2-12 qualified for the claim that the course uses it).
- Examples and non-examples on graph H: a1, computed by script.
- Trail word in English: m2-6 (Grinberg Definition 3.4.5). Table 2 English
  column: C39, C47, m2-6, m2-7; the column rests on two sources (m2-14,
  unverified; the caption and Section 6 say so). "Trail" as the textbook's
  "path" is my choice (stated).
- Lemma 3.8 (distinct vertices, distinct edges): m2-1, own proof.
- Lemma 3.9 (every walk contains a path): m2-2, own proof; textbook Lemma
  1.2.1 (C25, u different from v, no bound) and Grinberg Corollary 2.9.7 (C48)
  named in the first sentence after the statement.
- Corollary 3.10 (length at most N - 1): m2-3, C49.
- Proposition 3.11 (walk, trail, path exist together): m2-4, own proof;
  Grinberg Proposition 2.9.10 states walks and paths only (C50).
- Proposition 3.12 (distance equals least walk, trail, path length): m2-5,
  m2-10; own proof. The three distance properties in the remark are proved
  from walks; the textbook lists them without proof (m2-10).

Conclusions and premises: "connected" is the same under the textbook's trail
reading and the course's path reading follows from Proposition 3.11, which
follows from Lemmas 3.8 and 3.9.

Not justified: "English" column entry for distance is not backed by a quote
(the sources define distance in the usual way but I did not check their
wording); it is covered by the caption's qualification and m2-14. The word
"cycle" in Bai's sense was not read.

## Section 4 Question 1 (`sections/counting.tex`)

Purpose: answer Q1 with the walk-counting theorem, a full induction proof,
the worked board graph, and the warning that walks are not paths.

Claims and support:

- Theorem 4.1 (walk counting, k >= 0): m1-12, own proof; sources C31 (Galway,
  Theorem 1.1.3, p. 4), C38 (Bai, Theorem 1, p. 1), C34 (Gotti, Proposition 2,
  p. 1). I say only that Galway and Gotti prove it by induction (Bai's proof was
  not recorded). The case k = 0 is the paper's convention. Textbook absence:
  C30, m1-9.
- Directed graphs and multigraphs: one sentence, m1-20 (Gotti).
- Example 4.2 (powers A^2, A^3, A^4 and the walk lists): m1-19 / a3, computed
  by `walks_check.py`. The parity remark is a derived fact about this graph
  (m1-21).
- Brute-force check of the theorem: a3 (computation, not proof).
- Proposition 4.3 (A^k symmetric; (A^2)_ii = degree): m1-21, m1-13; Galway's
  sentence quoted (C32); own proof.
- Example 4.4 (walks not paths, (A^2)_11 = 1, (A^3)_12 = 2): m1-14, computed.
- Remark 4.5 (positive entry gives a path of length at most k): follows from
  Theorem 4.1 and Lemma 3.9.
- Corollary 4.6 (distance is the least k with positive entry): a4, derived from
  Theorem 4.1 and Proposition 3.12; the statement for connected graphs is
  Paramadevan Theorem 3 (C46), credited for the statement only.

Conclusions: (A^k)_ij counts walks (Theorem 4.1, by induction on k with the
last-but-one vertex); it does not count paths (Example 4.4).

Not justified: nothing.

## Section 5 Question 2 (`sections/connectivity.tex`)

Purpose: answer Q2: definition, components, reachability lemma, sum test,
power test, what the test does not say, worked examples, BFS for comparison.

Claims and support:

- Definition 5.1 (textbook 2.1.1 and the board): C27, C7. Reading of "path":
  Proposition 3.11 (m2-4, m3-9).
- Lemma 5.2 (equivalence relation): m3-8, own proof; the textbook only notes
  it (C28, "notes").
- Definition 5.3 components (C28), Corollary 5.4 (Remark 2.1.1: C29, m3-8).
- Textbook examples Fig. 2.1.1, 2.1.2: m3-14.
- Lemma 5.5 (reachability): m3-5, own proof from Theorem 4.1, Lemma 3.9,
  Corollary 3.10.
- Theorem 5.6 (sum test): m3-6; statement is Paramadevan Theorem 2 (C42); proof
  is the paper's own.
- Theorem 5.7 (power test): m3-7; statement Gotti Proposition 3 (C36) and Bai
  Theorem 2 (C40); proof by the binomial identity (C37). Equivalence of the two
  forms is shown here (C52, qualified interpretation: no source states both).
- Limits: N = 2 zero diagonal and single power (m3-11); early stopping
  (a2, computed on the four-vertex path).
- Worked examples, board graph and disconnected graph: m3-10, computed by
  `m3_connectivity.py`; the block shape is observed in the output and said to
  follow from Lemma 5.5.
- BFS paragraph: m3-1, m3-2, m3-3 (cited statements), m3-4 (interpretation,
  qualified, marked as such), m3-13 (cost, estimate, marked as such, one
  sentence).

Conclusions and premises: Theorem 5.6 follows from Lemma 5.5, non-negativity
of A^k entries, and Definition 5.1. Theorem 5.7 follows from the binomial
identity, positivity of coefficients, and Theorem 5.6. Lemma 5.5 follows from
Theorem 4.1, Lemma 3.9, and Corollary 3.10.

Not justified: m3-4 (BFS from n_1 as a connectivity test) is the paper's
interpretation; no source states it in exactly that form, and the BFS lemma
is cited, not proved. Lau's proof slides were not read.

## Section 6 Discussion (`sections/discussion.tex`)

Purpose: what the computations check; the board drawing read literally; word
traps; one item on two sources' wrong sentences, kept out of the theorem
statements; limits.

Claims and support:

- Exhaustive check on N = 1 to 6 (1, 2, 8, 64, 1024, 32768 graphs; 1, 1, 4,
  38, 728, 26704 connected): m3-12. Lemma checks (2052, 72664, 743680 walks):
  m2-2, m2-3, m2-5 derivation notes, recomputed by `walk_path_lemmas.py`.
- Triangle matrices: m3-10 (script output).
- Word traps: C20, C21, C22, C25, C24, m2-13, m2-5.
- Source critique: Paramadevan Theorem 1 (C45, m1-16) and proof of Theorem 2
  (C43), counterexamples from the board graph (m1-14, m3-10); Bai's sketch
  (C41), Bai's path definition (C39), Bai's Theorem 1 (C38). Each statement is
  quoted verbatim and restated in the paper's notation; where Paramadevan
  does not define "path" both readings are given and only the failing one is
  refuted. Bai's convention for "cycle" was not read, so the refutation of
  Bai's sentence is stated for the restatement and says so.
- Limits: C30, m1-9, m2-14 (unverified, qualified), m3-4, m3-13.

Not justified: the exact meaning of "cycle" in Bai's note (not read).

## Section 7 Conclusion (`sections/conclusion.tex`)

Direct answers to Q1, Q2, Q3, each pointing to its theorem or definition;
no new claims.

## Appendix A Sources, pages checked, reproduction (`appendices/derivations.tex`)

What was read from each source and how to rerun the three scripts. Pages
viewed in the textbook are listed from the evidence file's source note
(printed 7, 9, 11, 16, 21, 22, 23, 48, 49); I did not view textbook pages
myself in this run, and rely on the evidence file and `graph-sources.md` for
locators. I viewed the whiteboard photo 1 myself (crop at larger scale) to
check the drawing: three lines, an arrowhead at vertex 2 on the 1-2 line.

## Unverified or qualified claims used in the text

- m2-14 (English column of the naming table rests on two sources): unverified,
  qualified in the caption of Table 2 and in Section 6.
- Qualified: C2, C5, C8, C9, C28 (alpha "notes" only), C30, C52, m1-3, m1-4,
  m1-9, m2-12, m3-4, m3-13. Each is marked as a reading, a summary, a search
  result, an interpretation, or an estimate where it appears.
- C53 removed, not used.

## Things I could not justify

- The paper was not compiled (no LaTeX). The TikZ figure, `cleveref` labels,
  and the Armenian-free bibliography entry for the textbook are untested.
- The mark above A on the board is still a reading.
- The course's own word for the textbook's "path" (trail) was not reported;
  "trail" is my choice and is said to be.
- A plain-words paragraph precedes every definition, theorem, lemma,
  proposition, corollary, and worked example; the BFS paragraph also has one.
  The five-year-old read-aloud test was applied by me only, by reading the
  sentences, with the mechanical check of at most 20 words per sentence and no
  notation. An independent reader should test it.
- Remarks, examples, and non-examples after the definitions are one or two
  sentences each; I judged longer ones unnecessary. The four statements that
  are not definitions (the lemmas, theorems, and so on) have no separate
  remark, example, and non-example set, as the standard asks for definitions
  only; the example after the cut lemma and the worked examples after the tests
  serve as their worked instances.


## Round 1 update

Mechanical checks after the round 1 revision: `build.sh` exit 0 (21 pages);
`check_citations.py` 11 keys, 0 errors, 0 warnings; `check_claims.py` 0
errors, 10 inherited warnings; `inspect_pdf.py` 0 errors, 0 warnings;
`check_plain_words.py` 34 paragraphs, 28 statements, 0 errors, 0 warnings.
`pdffonts` shows Type 1 fonts throughout except one Type 3 font that I did
not trace (probably from the TikZ figure or a symbol); the "ff" ligature now
extracts correctly ("off the diagonal").

Evidence: new claim a5 in `evidence/modules/author.json` (walk count equals
path count when k is the distance; larger k can differ or agree; the triangle
entry (A^2)_12 = 1 is from `m3_connectivity.py` output). `evidence.json`
rebuilt. No other claim was added; sentences I reworded carry the same
citations as before.

Changed sections and what to re-read:

- Abstract (`main.tex`): defines walk and connected, no presentation remarks,
  says what is proved and what is cited. Fonts: `mathptmx` (Type 1 Times with
  math); `lmodern` is not installed here.
- Section 1 (`introduction.tex`): Q1 to Q3 stated up front; provenance
  shortened; conventions rewritten as 7 short items (drawing details and
  search details moved to Section 6.2 and Appendix A); reading guide added.
  Premises of the claims are unchanged (C1 to C9, C11, C26, C30, C47).
- Section 2 (`background.tex`): handshake reason stated; degree renamed
  deg; transpose and the product rule defined (standard linear algebra,
  marked as such); product explained with row and column vectors.
- Section 3 (`walks.tex`): walk defined as a vertex sequence first, with the
  length-0 part attributed to this note; purpose of trails, cycles, distance
  stated; Lemma 3.8 proof shortened to one vertex argument; Lemma 3.9 uses
  positions s < t and explains strong induction.
- Section 4 (`counting.tex`): the false sentence is replaced (a5); k-range
  attributions corrected to what the sources say; proof and example details
  expanded; labelled-graph count explained.
- Section 5 (`connectivity.tex`): relation, equivalence class, induced
  subgraph, commute, binomial theorem and coefficient defined; diagonal
  reason; block shape explained; cost estimate derived in the text.
- Section 6 (`discussion.tex`) and 7: title shortened; counts moved to the
  appendix; drawing-versus-matrix report is now Section 6.2 (label
  `sec:drawing`); Section 6.4 states its purpose and the B_22 and T_11
  arguments use "at most one path of any length joins the vertex to itself",
  which holds with or without length 0; the conclusion says why N - 1.
- Appendix A: search details, counts, `\path` for file names.

## Per-finding log, round 1

Evaluator findings.

- E1 (major): replaced "Otherwise the counts differ" by the correct statement
  (equality of walk and path counts when k is the distance; for larger k the
  entry is at least the path count, can be larger as in Example 4.5, or equal
  as in the triangle with (A^2)_12 = 1). Grepped sections, appendix and
  evidence for "counts differ" and similar: no other occurrence. The earlier
  sentences "A walk whose length equals the distance is a path" and Example
  4.5 are correct and kept. Claim a5 added. Note: the module report
  `modules/m1.md` section 3.4 still contains the false sentence ("In
  general the counts differ" is a weaker form there); I do not own that file.
- E2: abstract now says the two tests and the walk-counting theorem are proved
  and the textbook definitions, BFS comparison and standard linear algebra are
  cited.
- E3: relation, reflexive, symmetric, transitive, equivalence class and
  induced subgraph are defined before Lemma 5.2 and in Definition 5.3.
- E4: commute, the binomial theorem for commuting matrices, the binomial
  coefficient, and why I commutes are stated in the proof of the power test.
- E5: Definition 3.1 leads with the vertex sequence, cites the textbook only
  for the formal sequence, and says that k = 0 is this note's convention.
- E6: Section 4 now says Galway states positive integer k, Bai and Gotti state
  length k, and neither says in the passages read whether k = 0 is included
  (C31 "k a positive integer", C34, C38).
- E7: transpose defined in Section 2 (Definition of powers).
- E8: strong induction explained at the start of the proof of Lemma 3.9.
- E9: block structure described in words with the reason; the back reference is
  now `\cref{rem:nonneg}`.
- E10: fonts changed to `mathptmx` (Type 1). I could not use `lmodern`, which
  is not installed; the "ff" ligature now survives in the text layer. One
  Type 3 font remains (untraced).
- E11: section titles use `\texorpdfstring`; Discussion title shortened; file
  names use `\path`; `\emergencystretch` and url penalties remove the two
  overfull boxes (both were in the bibliography, not the appendix; the
  appendix fix still applies).

Reader findings.

- R1: abstract defines walk and connected; presentation remarks removed.
- R2: same as E10.
- R3: Q1 to Q3 stated at the start of Section 1; the board mark is in
  Convention 3.
- R4: provenance sentence is now "as it was relayed to the author of this
  note; the relay is a summary and not the assignment's own words", with the
  citation kept.
- R5: Convention 2 says once "we write G = (V, E) ...", board and textbook
  differences in one sentence.
- R6: sentence about prime or quotation marks deleted.
- R7: drawing discrepancy moved to Section 6.2; Convention 4 says only that the
  matrix defines the example.
- R8: walk explained in a clause where "path" first appears in Convention 5;
  textbook comparison pointed to Table 2.
- R9: Convention 6 explains why length 0 is wanted (A^0 = I).
- R10: Convention 7 is one sentence; search details moved to Appendix A.
- R11: the claim about order is fixed to match the layout (plain-words
  paragraph first, then the definition). I did not reduce the story words:
  each plain-words paragraph and the dictionary use them consistently, and
  replacing them would touch all 34 paragraphs; flagged for the evaluator.
- R12: Q1 answer reworded and cites the non-example `ex:notreach`.
- R13: handshake reason stated in the proof of Proposition 2.5.
- R14: degree renamed deg; textbook's d_G(v) mentioned.
- R15 and R16: matrix product explained in words in Definition 2.6; Example 2.7
  writes out row and column vectors. I did not add a separate 2 by 2 example.
- R17: caption of Figure 1 lists the edges of H; the figure itself renders in
  the PDF. I did not inspect the PDF image beyond the build.
- R18: Definition 3.1 leads with the vertex sequence.
- R19: purpose of trails stated at the start of Section 3.
- R20 and R21: purpose of cycles and distance stated at the start of Section 3
  (distance is used in Corollary 4.7).
- R22: positions s < t used instead of i < j.
- R23: Lemma 3.8 proof rewritten so that one end vertex settles all cases.
- R24: `(A^k)_ir = (A^k)_ir * 1 = ...` written out, and the zero case likewise.
- R25: the why-walks remark points to Example 4.5.
- R26: the three terms are written as (A^2)_11 A_12 + (A^2)_12 A_22 +
  (A^2)_13 A_32.
- R27: parity reason added (each hop alternates between the middle vertex and
  an end vertex).
- R28: 64 = 2^6 explained.
- R29: transpose defined in Section 2.
- R30: the "Otherwise" sentence replaced (see E1); Example 4.5 is the example
  where the counts differ.
- R31: Definition 5.1 now says walk, trail or path give the same graphs and
  points to Proposition 3.11.
- R32: see E3.
- R33: a paragraph before the test says components are a reformulation, used
  only to describe the block shape in Example 5.9.
- R34: "no term can cancel another" added.
- R35: see E4.
- R36: plain-words paragraph for the power test now says "start with the
  island table and add a one to every cell where row and column island are the
  same".
- R37: reason for ignoring the diagonal added (closed walks say nothing about
  reaching other vertices) in the theorem's plain-words paragraph and in the
  limits list.
- R38: see E9.
- R39: the remark on (A^2)_33 removed.
- R40: abstract qualified (E2); operation counts derived in two sentences in
  the BFS paragraph.
- R41: counts moved to Appendix A; Section 6.1 says only what the check shows.
- R42: Section 6.4 opens with its purpose and optional status; B_22 and T_11
  arguments simplified.
- R43: the conclusion says a path visits each vertex at most once, so it has at
  most N - 1 edges.
- R44: reading guide added at the end of Section 1.

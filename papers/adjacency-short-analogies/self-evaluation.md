# Self evaluation (short, plain version)

Register: technician, no analogies, no story, no plain-words paragraphs (brief section 4 overrides the standard references). Length: 4 pages including references (A4, 11pt, 2.5 cm margins, unchanged). No appendix. Evidence files were not edited. Condensed from the long version (21 pages, passed after three rounds); its statements, locators, and proofs were followed.

Decisions taken without asking: (1) only the sum test is given (the power test (I+A)^(N-1) is omitted; brief asks for one test); (2) the sum test is stated for N >= 2, with N = 1 noted as trivially connected; (3) the textbook's trail, cycle, distance, components, the naming table, BFS and the cost estimate are omitted (brief section 3); (4) the board drawing mismatch gets one sentence; (5) no figure; (6) scripts stay in `scripts/` and are named in the text, not moved to an appendix; (7) bib trimmed to the 7 cited entries (lau, mccauley, gotti, bai dropped; their notes/title addons shortened where this cost lines, no fields invented); (8) no module-defined "conventions" list; the length-0 convention is stated inside Definition 2.2.

## 1 Introduction
Purpose: state Q1 to Q3 and the answers in one sentence each.
- Board questions, board source of Q1, Q2: C4, C5, C6, C9 (Q3 and the exponent reading come from the user statements, qualified claims C5, C9, m1-4).
- Textbook has no walk-counting theorem or matrix test, by full-text search: C30, m1-9 (qualified; stated as a search result).
- Answers to Q1, Q2, Q3: m1-12, m3-6, m2-11/C21.
Conclusion follows from Sections 3 to 5. Printed pages one lower than PDF: stated in graph-sources.md and the bib.

## 2 Setting and definitions
Purpose: fix the setting, matrix, walk, path, connected, board graph.
- Graph, adjacent: C10, C12. Matrix rule: C13 (textbook), C1 (board). Walk: C17, C18; length 0 as own convention agreeing with textbook usage: C26, m1-17. Path = simple path, textbook's own "path" is a trail: C20, C21, C8/m2-12 (qualified, user's course convention). Connected: C7 (board), C27 (textbook). Board matrix: C3, m1-2; drawing mismatch: C2, m1-3 (qualified, one sentence).
- Non-negative entries of A^k: elementary, no source needed.
Not justified by a source: none.

## 3 Answer 1
Purpose: walk-counting theorem, full induction proof, one warning.
- Theorem: m1-12, C31 (Galway Theorem 1.1.3, p. 4). Proof is derived (m1-12).
- Warning: (A^2)_11 = 1 counts n1n2n1, only path n1 to n1 has length 0, (A^4)_22 = 4: m1-14, scripts/output-walks_check.txt.

## 4 Answer 3
Purpose: definition of path between n_i and n_j.
- C21, m2-11 (i = j gives the one-vertex path). Example on the board graph from m2-11 / script.

## 5 Answer 2
Purpose: the sum test with complete proof.
- Walk contains a path, strong induction, k = 0 allowed: m2-2 (textbook Lemma 1.2.1 is C25, u != v only; Grinberg Corollary 2.9.7 is C48). Proof written out in full.
- Path length at most N-1, proved inline in the reachability proof: m2-3, C49.
- Reachability lemma: m3-5. Sum test: m3-6, C42 (Paramadevan Theorem 2; their proof is not followed, ours uses the cut lemma). The test follows from reachability plus non-negative entries plus the definition of connected.
Not stated: "walk-to-path step that some sources pass over" (C43) is not discussed, to keep scope.

## 6 Worked example and limits
Purpose: the board graph (connected), edge plus isolated vertex (disconnected), and limits.
- A^2, B, disconnected matrices, test results: m3-10, scripts/output-m3_connectivity.txt. Walk lists, (A^3)_12 = 2, (A^4)_22 = 4: m1-14, scripts/output-walks_check.txt.
- Limits: zero diagonal for N = 2 (m3-11); sum must reach A^(N-1), path graph on four vertices (a2, scripts/output-walks_check.txt); positive entry gives a path of length at most k (m3-5, m2-2). "Single power is no test" (m3-11) was cut for length. Test proved only for finite simple undirected graphs (scope).

## Mechanical checks
- build.sh: ok, 4 pages, no overfull boxes, no undefined references.
- check_citations.py: errors 0, warnings 4: sources bai2025adjacency, gotti18211, lau2021bfs, mccauley2025bfs never cited but claims rest on them (accepted by the task; those claims are not used).
- check_claims.py: errors 0, warnings 10, all existing (missing quotes on C3, C8, C9, m1-3, m1-4, m2-12; unverified m2-14, which is not used in the text). Accepted by the task.
- inspect_pdf.py: pages 4, errors 0, warnings 0.
- check_plain_words.py: not run (technician register, no story dictionary).

## Unverified claims in the text
None. m2-14 (unverified) is not used.

## Could not justify
Nothing in the text lacks a claim, a derivation, or an elementary argument. The Q3 and exponent readings rest on the user's text (qualified claims), and are labelled as such in the introduction.

## Version with analogies: plain-words layer (added)

This folder is the plain version plus analogies. Formal text, proofs, numbers, and citations are unchanged; the only edits are added lines (checked with `diff -r` on `sections/`, differences are all additions), a `\plainwords` macro and a subtitle in `main.tex`. Pages: 5.

Story (introduction, last paragraph, with one sentence saying plain-words paragraphs precede the formal statements): a pond with islands (vertices), bridges (edges), next door (adjacent), a frog making trips of hops (walks, which may land twice on an island), fresh-island trips (paths), in one piece (connected), the island table (adjacency matrix). Every analogy about walks speaks of trips that may revisit islands; entries are trips with exactly that number of hops; the test asks only whether a cell is zero.

Plain-words paragraphs and the statement each precedes:
1. Definition 2.1 (adjacency matrix): islands, bridges, table of ones and zeros.
2. Definition 2.2 (walk): trips and hops, repeats allowed, trip with no hops.
3. Definition 2.3 (path): fresh-island trip, never repeats a bridge either (true by the textbook-independent argument that distinct vertices force distinct edges, the long version's Lemma on this), contrast with a trip.
4. Definition 2.4 (connected): pond in one piece, fresh-island trips suffice.
5. Theorem 3.1 (walk counting): cells count trips of exactly that many hops; they may land twice, so not all fresh-island trips.
6. Definition 4.1 (path between n_i and n_j): fresh-island trip between two islands, zero-hop trip allowed.
7. Lemma 5.1 (every walk contains a path): cut out the hops between two visits.
8. Lemma 5.3 (reachability): cell for two different islands, up to one fewer hops than islands.
9. Theorem 5.4 (sum test): sum of tables, only zero or not matters.
10. Worked example (start of Section 6): two ponds with three islands.

check_plain_words.py (terms: vertex, edge, walk, path, connected, adjacent, adjacency, matrix, entry, length, degree, theorem, definition, lemma and plurals): 10 paragraphs, 9 statements, 0 errors, 0 warnings after splitting three long sentences. Other checks: build ok (5 pages), citations 0 errors (same 4 accepted warnings), claims 0 errors (same 10), inspect_pdf 0 errors.
Plain paragraph 3's claim that a fresh-island trip never crosses a bridge twice rests on the paper's own argument that distinct vertices force distinct edges; it is not proved in this short text (an elementary one-line fact, flagged here).

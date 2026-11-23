# Evaluation report

## Round 1, 2026-11-23

Question: For a simple undirected graph with N vertices given by its adjacency matrix A: what does the entry (A^k)_{ij} represent, how can one determine from A whether the graph is connected, and what is the definition of a path between vertices n_i and n_j?

Scope: study notes for the course reader. Five definitions with the textbook's numbers, the walk-counting theorem, the walk-contains-path lemma, the sum test, the board's graph and one disconnected graph worked in full, the limits of the test, and notes on sources. Register `study-note`, no analogies.

Research summary: one research agent (9 sources opened, 34 claims) and two module owners, m1 definitions and walk counting, m2 the connectivity test (2 sources and 16 claims added). Merged evidence: 11 sources, 50 claims.

Model levels: research 2, modules 2, author 2, reader 1, evaluator 3, orchestrator the session model, not pinned. Hierarchy requirement: met.

Mechanical checks: build pass, citations pass, claims pass, pdf pass. Pages 6 of a budget of 6.

### Scores

| Dimension | Score | Observation |
|---|---|---|
| 1 Correctness | 4 | I traced every proof step: Theorem 3.1 (sections/walks.tex), Lemma 4.1, Proposition 4.2 and Theorem 4.3 (sections/connectivity.tex). Every matrix in Examples 3.2, 5.1, 5.2 and Remark 4.4 is right; I recomputed (I+A)^2 for G1 and G2 by hand, and both scripts reproduce their saved outputs byte for byte. The only inaccuracy is the claim in sections/limits.tex:3 that a search from a graph given by A runs in O(E) (F6). |
| 2 Evidence coverage | 3 | Every substantive claim has a `\cite` and an evidence entry. check_claims: 47 supported, 3 qualified, 0 unverified. But the quote behind the Gotti attribution in sections/walks.tex:7 (claim C20) does not state the proposition the paper attributes (F1). |
| 3 Citation integrity | 3 | All seven external spot checks support the attributed statements, with the correct numbers and pages. The Grinberg quote of C12 is not verbatim: it joins two sentences without marking the cut (F2). Two smaller attribution and metadata slips are F8 and F12. |
| 4 Logical validity | 5 | Lemma 4.1(a) handles the case b = k. Theorem 4.3 separates the two directions and says the bound N-1 is used only in the first; the N = 1 and N = 2 cases are dealt with (connectivity.tex after the proof). Proposition 4.2 justifies citing textbook Definition 2.1.1 for the paper's own connected. |
| 5 Understandability | 4 | Most terms are defined before use. Failures: O(E), and E as a number, are never explained (limits.tex:3, F6); "written from n_i to n_j" in Definition 2.4 (definitions.tex:20, F9); the title "The test failing on a disconnected graph" reads as if the test gives a wrong answer (examples.tex:15, F10). |
| 6 Completeness | 5 | N1 to N9 are all present: Definitions 2.1 to 2.6, Theorem 3.1 with Example 3.2, Lemma 4.1, Theorem 4.3, Examples 5.1 and 5.2 with every matrix printed, and Section 6. The optional O1 (Remark 4.4) and O3 (Section 6, second paragraph) are written within the budget. |
| 7 Methodological rigor | 4 | Every matrix is produced by scripts/m1_walks.py and scripts/m2_connectivity_test.py, with brute-force walk and path checks. Re-running both with `python3 -I` reproduces the saved outputs exactly. The proofs name their method, base case and step. |
| 8 Critical analysis | 4 | Section 6 states the limits (walks not paths; not the cheapest test) and qualifies the cost comparison as an interpretation. The diagonal and N = 1 caveats follow Theorem 4.3. The graph-search part goes beyond the brief's one-sentence limit (F6). |
| 9 Internal consistency | 4 | Terms are used consistently: walk, path and trail are each fixed once. Letter clashes: E is the edge set in Definition 2.1 but a number of edges in limits.tex:3. Section 6 (limits.tex:5) also uses n and l where the paper uses N and k (F7). |
| 10 Reproducibility | 4 | The scripts rerun identically, and the notes on sources say how to run them. In evidence.json, many `used_in` fields point to files that do not exist (sections/analysis.tex, background.tex, discussion.tex) (F13). |
| 11 LaTeX and PDF quality | 4 | build.sh succeeds; inspect_pdf reports 6 pages against a budget of 6, with 0 errors and 0 warnings. All references resolve. The matrices render. The only log noise is hyperref "Token not allowed in a PDF string" from math in section titles. |
| 12 Answer relevance | 4 | The introduction answers all three questions directly, each with a numbered pointer. There is surplus: the S_22 example is restated in Section 6, there is a critique of the Paramadevan proof beside Theorem 4.3, graph search takes more than one sentence, and the Grinberg citation after Definition 2.3 is redundant (F3, F4, F5, F6). |

### Findings

| Id | Severity | Location | Defect | Correction | Status |
|---|---|---|---|---|---|
| F1 | major | evidence/evidence.json claim C20; cited at sections/walks.tex:7 [3, Proposition 2, p. 1] | The evidence quote for "Gotti states this result" is the sentence before the proposition ("As we proceed to show, adjacency matrices can be used to compute number of walks in a graph."). It does not state the walk-counting result the paper attributes to Proposition 2, although the source does: I fetched it. | Replace the quote with the statement of Proposition 2, p. 1: "For any j, k ∈ [n] and ℓ ∈ N, there are A^ℓ_jk walks of length ℓ from j to k." Set the locator to "Proposition 2, p. 1". | resolved, confirmed by the round 2 evaluator |
| F2 | major | evidence/evidence.json claim C12; cited at sections/definitions.tex:20 [4, Definition 2.9.1(c),(d)] | The quote "A path (in G) means a walk (in G) whose vertices are distinct. A path from p to q means a path that starts at p and ends at q." is not verbatim. In the source, two sentences and the label "(d) Let p and q be two vertices of G. A walk from p to q means ..." stand between the two sentences, and the cut is not marked. Claim C5 (Galway Notes 1 and 2) silently drops the list markers "1." and "2." in the same way. | Split C12 into two support entries, one for (c) and one for (d), each with its own locator (Definition 2.9.1(c), p. 36 and Definition 2.9.1(d), p. 36), or mark the omission with "[...]". Do the same for C5. | resolved, confirmed by the round 2 evaluator |
| F3 | minor | sections/connectivity.tex:31 | Surplus, and against the checklist rule that a statement that a source is wrong sits in one discussion item and not beside a theorem: "their proof moves from a non-zero entry to a path without the step of Lemma 4.1(a)" criticises a source beyond O3 (the brief puts "a critique of the sources beyond O3" out of scope). | Shorten to "Paramadevan and Sotheeswaran state this test [8, Theorem 2, p. 17]; the proof below is this paper's own." | resolved, confirmed by the round 2 evaluator |
| F4 | minor | sections/limits.tex:3, first sentence | Surplus: this sentence restates Example 3.2 ("S_22 = 2 counts the walks n_2, n_1, n_2 and n_2, n_3, n_2, but only one path ..."), a repeated example that shows nothing new. | Shorten to "The entries of S count walks, not paths (Example 3.2), so only their positivity is used." | resolved, confirmed by the round 2 evaluator |
| F5 | minor | sections/definitions.tex:17 | Surplus and an inaccurate label. "(a derived remark); Grinberg also writes walks as vertex sequences [4, Definition 2.9.1(a), p. 36]": the textbook itself, on printed p. 21 right after Definition 1.2.10, says a walk is written as its vertex sequence u_0, ..., u_k with each vertex adjacent to the one before. So the remark is not derived, and the Grinberg citation adds nothing. | Replace with "the textbook itself writes a walk by its vertex sequence [9, p. 21]". Cut the Grinberg clause and "(a derived remark)". | resolved, confirmed by the round 2 evaluator |
| F6 | minor | sections/limits.tex:3, sentences 3 and 4 | Two problems in this passage. (a) Surplus beyond the brief's scope limit ("graph search ... beyond one sentence in N9"; "complexity analysis" out of scope): there are two sentences on DFS run time plus a meta-sentence about breadth-first search, which the body never mentions. (b) O(E) is never explained, and for a graph given by its adjacency matrix the slide's O(E) bound (which is for adjacency lists) does not apply as stated. | Shorten to one sentence that serves N9: "It is also not the cheapest way to decide connectivity: a graph search such as depth-first search from one vertex does the same job with less work [11]; this comparison is an interpretation, since the source does not discuss the matrix test." Also cut "No source on breadth-first search was opened." in sections/notes.tex:5. | resolved, confirmed by the round 2 evaluator |
| F7 | minor | sections/limits.tex:5; sections/limits.tex:3 | One letter, one meaning: Section 6 writes A^l, length l, and (I+A)^{n-1} where the paper uses k and N, and limits.tex:3 uses E for a number of edges when E is the edge set (Definition 2.1). The checklist asks for rejected statements to be restated in the paper's notation. | Write (A^k)_{ij} and length k for Paramadevan's Theorem 1 and (I+A)^{N-1} for Bai, keeping the verbatim quote marks only on the quoted words. Drop E as a count (this is resolved by F6). | resolved, confirmed by the round 2 evaluator |
| F8 | minor | sections/limits.tex:5 "his Theorem 1 says that powers of A count walks, not paths [1, p. 1]" | Bai's Theorem 1 says the entries count walks. The words "counts walks — not paths" are in the commentary after the definitions, not in the theorem. Separately, the paper does not credit that Paramadevan and Sotheeswaran's own Section 2.2 item 7 (p. 16) states the walk version correctly; the checklist requires crediting a correct statement by the same source. | Write "while his comment after Theorem 1 says that (A^k)_{ij} counts walks, not paths [1, p. 1]". For Paramadevan, add one clause: "their own list of properties states it with walks [8, Section 2.2, item 7, p. 16]". This serves O3; room comes from F4 and F6. | resolved, confirmed by the round 2 evaluator |
| F9 | minor | sections/definitions.tex:20 | Comprehension: "A path between n_i and n_j, written from n_i to n_j, is a path ..." leaves unclear what "written" refers to. | Rewrite: "A path between n_i and n_j (also called a path from n_i to n_j) is a path (v_0, ..., v_k) with v_0 = n_i and v_k = n_j." | resolved, confirmed by the round 2 evaluator |
| F10 | minor | sections/examples.tex:15, Example 5.2 title | "The test failing on a disconnected graph" can be read as the test giving a wrong answer. In fact the condition fails and the verdict, not connected, is correct. | Retitle "The test on a disconnected graph G_2". | resolved, confirmed by the round 2 evaluator |
| F11 | minor | sections/examples.tex:3; sections/walks.tex (Example 3.2, "computed by script"); sections/connectivity.tex:24, :44; sections/notes.tex:3, :5 | Pipeline material and status labels in the reader's text. The body names the script file `scripts/m2_connectivity_test.py`, although the brief says "the body only cites". The labels "(Derived here.)", "The following is derived here." and "(qualified)" are a bracketed status system, which book-style-standard.md rules out. "the user's own words" uses "the user" without introducing it. | Replace examples.tex:3 with a citation of the script entry (add a bib entry for m2 like [2]); the run instructions are already in the notes. Delete "(Derived here.)" and "The following is derived here."; a proof printed in the paper already marks the result as the paper's own. In the notes, replace "(qualified)" with plain wording and say "the student's own words" or "the assignment text". | resolved, confirmed by the round 2 evaluator |
| F12 | minor | references.bib entries wayne_cos226_undirected, galway_adjacency_notes | Metadata: the slide footer reads "Robert Sedgewick and Kevin Wayne • Copyright © 2006", but the entry lists Wayne only. The Galway entry has no author although the URL is a personal page (~rquinlan). | Add Sedgewick as an author and call it "Sedgewick and Wayne" if the text names it. Add the Galway author only if it can be read from the source; otherwise leave it as it is. | resolved, confirmed by the round 2 evaluator |
| F13 | minor | evidence/evidence.json, `used_in` of C22, C28, M2-1 to M2-10 | `used_in` names sections/analysis.tex, sections/background.tex and sections/discussion.tex, which do not exist. Most other claims have an empty `used_in`. This weakens tracing from claim to text. | Set `used_in` to the actual files (definitions.tex, walks.tex, connectivity.tex, examples.tex, limits.tex, notes.tex) for every claim the paper cites. | resolved, confirmed by the round 2 evaluator |
| F14 | minor | sections/walks.tex:7 "Galway's version is for k ≥ 1" | This implies the other two sources cover k = 0. Gotti's and Bai's proofs also start at k = 1. | Write "the three sources prove it from k = 1; the case k = 0 is added here." | resolved, confirmed by the round 2 evaluator |

### Citation and claim coverage

Sources 11. Claims: 47 supported, 3 qualified, 0 unverified. Spot checks this round: 11 lines covering every source the paper cites, 9 fetched and 2 viewed; carried: 0. Every check supports its statement; two evidence quotes are not usable as recorded (F1, F2).

### Unverified claims and access limits

No unverified claim. Three qualified claims are used: C14 (the course's meaning of "path", known only through a summary), C34 (the textbook has no walk-counting theorem and no matrix test; text search plus four viewed pages, printed p. 7 not viewed), and M2-9 (a graph search is cheaper than the test; an interpretation). The textbook's publisher and year were not read.

### Known limitations

The test is proved for finite simple undirected graphs with at least two vertices.

### Release conditions and decision

Conditions 1 to 9 hold as the evaluator reported them. Condition 10 is not met: two major findings are open (F1, F2). Under the severity rule a quotation that is not verbatim in its source, or does not state what is attributed to it, is at least major, even though the evaluator fetched both sources and found that they support the statements.

Decision: REVISE.

## Round 2, 2026-11-23

Question, scope: as in round 1.

Changes since round 1: the research agent re-opened four sources and corrected the quotes of C20, C12, C5, and C15; the module owners added claims m1-7 and M2-11 and one source (the m2 script) and corrected the authors of the slide source; the author revised every section for the round 1 findings and the reader's passages. Merged evidence: 12 sources, 52 claims.

Model levels: research 2, modules 2, author 2, reader 1, evaluator 3 (a fresh evaluator), orchestrator the session model, not pinned. Hierarchy requirement: met.

Mechanical checks: build pass, citations pass, claims pass, pdf pass. Pages 6 of a budget of 6. The evaluator ran all four itself on a copy and re-ran both scripts with identical output.

### Round 1 findings

The round 2 evaluator checked each of F1 to F14 against the revised paper and the sources and reports all fourteen resolved, the two major ones (F1, F2) by comparing the corrected quotes with the fetched sources character by character. The statuses in the round 1 table are updated accordingly. One trace of F2 remains in a claim the paper does not cite (new F15), and one of F11 in the bibliography (new F21).

### Scores

| Dimension | Score | Observation |
|---|---|---|
| 1 Correctness | 5 | I traced every step of Theorem 3.1 (sections/walks.tex:9-21), Lemma 4.1, Proposition 4.2 and Theorem 4.3 (sections/connectivity.tex:13-39). The N=1 and N=2 remarks at connectivity.tex:41 are right. Every matrix in Examples 3.2, 5.1 and 5.2 and the R rows in Remark 4.4 match scripts/m2_connectivity_test.out, which re-runs identically. |
| 2 Evidence coverage | 4 | Every substantive claim has a \cite and an evidence entry (check_claims: 49 supported, 3 qualified, 0 unverified). The C20 and C12 quotes now state what the paper attributes. One leftover defect in the record: the Galway quote under M2-6 joins two list items without their markers (F15). |
| 3 Citation integrity | 4 | Every fetch or view this round supports the attributed statement, with the correct number and page (block below). Smaller attribution slips remain: "Grinberg's definition" points to Example 2.9.2 (definitions.tex:17, F17); Lemma 4.1(a)'s clause on vertices is attributed to Grinberg Corollary 2.9.7, which does not state it (connectivity.tex:11, F18); some locators have no page (definitions.tex:4, :20, F20). |
| 4 Logical validity | 5 | Theorem 4.3 separates the two directions and says the bound N-1 is used only in the first (connectivity.tex:41). Proposition 4.2 now writes out both cases (connectivity.tex:24). Lemma 4.1(a) covers b = k (connectivity.tex:14). |
| 5 Understandability | 4 | Terms are defined before use. d(u,v) is named as distance (definitions.tex:17), and Remark 2.5 gives the path/simple path/trail mapping (definitions.tex:24). One gap: "the textbook's Lemma 1.2.1 is stated for u ≠ v" uses letters this paper never defines (connectivity.tex:11, F19). |
| 6 Completeness | 5 | N1 to N9 are present: Definitions 2.1 to 2.6; Theorem 3.1 with Example 3.2, which counts a walk that is not a path (walks.tex:32); Lemma 4.1; Theorem 4.3; Examples 5.1 and 5.2 with A, A^2 and S printed; and Section 6. The optional O1 (Remark 4.4) and O3 (limits.tex:5) fit within the 6 pages. |
| 7 Methodological rigor | 5 | Every matrix comes from scripts/m1_walks.py or scripts/m2_connectivity_test.py, which check against brute force. Re-run with python3 -I, both reproduce their saved outputs exactly. Every proof names its method, base case and step. |
| 8 Critical analysis | 4 | Section 6 (limits.tex:3) states both limits in brief and marks the cost comparison as an interpretation. Caveats on the diagonal and N=1 follow Theorem 4.3. O3 gives both readings of Paramadevan's undefined "paths", with the counterexample (A^2)_11 = 1 (limits.tex:5). |
| 9 Internal consistency | 4 | E is now only the edge set, and Bai's n is mapped to N (limits.tex:5). Walk, path and trail are fixed once each. Remaining: textbook letters u, v appear without mapping in connectivity.tex:11 (F19). |
| 10 Reproducibility | 5 | Both scripts re-run byte-identically. The notes on sources (notes.tex:5) say how to run them. Every used_in path in evidence.json now exists. |
| 11 LaTeX and PDF quality | 4 | build.sh exits 0. inspect_pdf: 6 pages, 0 errors, 0 warnings. References and cross-references resolve, and the matrices render. Blemishes: hyperref token warnings from math in a title, and the stray "; [9, Theorem 2, p. 17];" at connectivity.tex:31 (F16). |
| 12 Answer relevance | 4 | The introduction (introduction.tex:5) answers all three questions with numbered pointers, and Section 6 keeps graph search to one sentence. Small surplus: Examples 5.1 and 5.2 repeat the point about the diagonal already made at connectivity.tex:41 (F22), and Lemma 4.1(a) carries a clause no later proof uses (F18). |

### Findings

| Id | Severity | Location | Defect | Correction | Status |
|---|---|---|---|---|---|
| F15 | minor | evidence/evidence.json claim M2-6 (Galway support) | The quote "The adjacency matrix is symmetric (i.e. equal to its transpose) if the graph is undirected. The adjacency matrix has zeros on its main diagonal (unless the graph has loops)." joins Notes 1 and 2 of printed p. 3 and drops the markers "1." and "2.". This is the defect F2 fixed in C5. It is minor here because the paper's text does not cite Galway for M2-6; Example 5.2 cites the script. | Record it as in C5: two support entries that keep "1." and "2.", or drop this support. Add the script output (scripts/m2_connectivity_test.out, DISCONNECTED GRAPH section) as a support entry, since the claim is derived from it. | open |
| F16 | minor | sections/connectivity.tex:31 | The citation has a stray semicolon: "Paramadevan and Sotheeswaran state this test; [9, Theorem 2, p. 17]; the proof below is this paper's own." | Write "Paramadevan and Sotheeswaran state this test \cite[Theorem 2, p.~17]{paramadevan2021adjacency}; the proof below is this paper's own." | open |
| F17 | minor | sections/definitions.tex:17 "and with Grinberg's definition [4, Example 2.9.2, p. 37]" | The text says "definition" but the locator is an example. Grinberg's definition, which allows k ≥ 0, is Definition 2.9.1(a) on p. 36. Example 2.9.2 on p. 37 (verbatim: "The sequence (5) is a walk from 5 to 5. It has length 0. It is a path.") does support the agreement, so the fact is not in doubt. | Change the wording, not the citation: "and with Grinberg's example of a length-0 walk [4, Example 2.9.2, p. 37]". | open |
| F18 | minor | sections/connectivity.tex:7 (Lemma 4.1(a), "whose vertices all occur in the walk") and :11 ("Grinberg proves (a)") | Grinberg's Corollary 2.9.7 (p. 39) gives "a path from u to v of length ≤ k" and says nothing about which vertices the path uses, so the attribution covers more than the source says. The clause is also not used in Proposition 4.2 or Theorem 4.3. | Because a final edit may not change a numbered statement, change the attribution at :11: "Grinberg proves (a) without its last clause and states (b)". If another round runs, cut the clause from the lemma and from the last sentence of its proof. | open |
| F19 | minor | sections/connectivity.tex:11 "the textbook's Lemma 1.2.1 is stated for u ≠ v" | u and v are the textbook's letters and are never introduced in this paper's notation (one letter, one meaning). | Write "the textbook's Lemma 1.2.1 is stated only for two different vertices and has no length bound [10, p. 23]". | open |
| F20 | minor | sections/definitions.tex:4 "[7, Definition 1.1.1]"; sections/definitions.tex:20 "[4, Definition 2.9.1(c),(d)] [1]" | These locators have no page, and the Bai citation has no locator at all. The checklist asks for each source's own number and page. The pages are recorded in C2, C12 and C13. | Write [7, Definition 1.1.1, p. 2], [4, Definition 2.9.1(c),(d), p. 36] and [1, definition of path after Theorem 1, p. 1]. | open |
| F21 | minor | references.bib entries whiteboard1, whiteboard2, user_statements, m1_walks_script, m2_connectivity_script (PDF references [2], [5], [6], [8], [12]) | Comprehension (reader R18): the bibliography says "Supplied by the user", and "the user" is never introduced (checklist, Writing). It also gives internal file paths and script file names as titles. | Change the notes to "photograph of the lecture board, not public", "summary of the student's assignment and course conventions, not the assignment text", and "script written for these notes; see Notes on sources". Keep the file paths only in howpublished, or drop them. | open |
| F22 | minor | sections/examples.tex:12 last sentence; sections/examples.tex:22 last sentence | Surplus: "The diagonal is not read: S_11 = 1 and S_22 = 2 play no role." and "The positive entry S_11 = 1 ... which is why the test reads the off-diagonal entries." repeat the reason given after Theorem 4.3 (connectivity.tex:41). | Cut the examples.tex:12 sentence. Shorten examples.tex:22 to "The positive entry S_11 = 1 does not help reach n_3." | open |

### Citation and claim coverage

Sources 12. Claims: 49 supported, 3 qualified, 0 unverified. Spot checks this round: 17 lines; 6 fetched (C20, C12, C15, C5, M2-11, and C21 with C33 as the control), 3 viewed (C15 and m1-7 on the textbook pages, M2-5 by re-running the script), 8 carried from round 1. Every check supports its statement, and the control agrees with the round 1 record.

### Unverified claims and access limits

No unverified claim. The three qualified claims of round 1 are unchanged and each is qualified where it is used: C14 (`sections/notes.tex`), C34 (`sections/notes.tex`), M2-9 (`sections/limits.tex`). The textbook's publisher and year were not read.

### Known limitations

As in round 1. The technician reader's 27 passages for this round are in `reader-findings.md`; no evaluator graded them.

### Release conditions

Conditions 1 to 9 hold as the evaluator reported them: every score is at least 4, no critical finding, no unverified claim, complete proofs, hierarchy met, mechanical checks pass, `self-evaluation.md` present. No critical or major finding is open. Eight minor findings (F15 to F22) remain and go to final edits; no further evaluation round is run for them.

### Final edits

Findings closed after the evaluation: F15 by the m2 module owner (the Galway support of claim M2-6 is now two verbatim entries with their markers, as in C5, plus the script output line; the orchestrator compared the new quotes with C5 and with line 55 of `scripts/m2_connectivity_test.out`), and F16, F17, F18, F19, F20, F22 by the author with the evaluator's corrections. F18 was closed by the attribution wording; Lemma 4.1 and its proof are unchanged, so the clause "whose vertices all occur in the walk" stays in the lemma although no later proof uses it.

F21 is closed in part and documented: the bibliography no longer says "the user" (it says "the student who requested these notes"), and the script entries point to the notes on sources. The words "supplied by" stay because `references/latex-structure.md` requires them in a local-file entry, and the titles of the two script entries still name the script files.

Reader passages of round 2: the author changed twelve (reader F1, F2, F4, F5, F7, F10, F18, F21, F24, F25, F26, F27) and left fifteen, each with its reason in `reader-findings.md`.

Diff confined to the named passages: yes. The orchestrator read the word-level diff of `main.tex`, `sections/`, and `references.bib`. No statement of a definition, theorem, lemma, or proposition changed, no line inside a proof changed, and no citation key was added; the locators added for F20 agree with evidence claims C2, C12, and C13. One edit adds a reason and not only wording: the notes on sources now say the paper uses the board's matrix because it is the object both questions are about and ignores the arrowhead and the third line. This is the assumption recorded in the brief, section 7, and the orchestrator judged it a statement of the paper's own choice, not a new claim about a source.

Mechanical checks re-run: build pass, citations pass (12 keys, 12 entries, 12 sources), claims pass (49 supported, 3 qualified, 0 unverified), pdf pass, 6 pages of a budget of 6. `claims_changed.py` against the round 2 snapshot lists one changed claim, M2-6 (its support entries), and nothing new or removed.

Not re-read by an evaluator.

Decision: PASS -- conditions 1 to 9 held in round 2 with no critical or major finding open, the minor findings were closed or documented by final edits, and the mechanical checks pass on the final files.

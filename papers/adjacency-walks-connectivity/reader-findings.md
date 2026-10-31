# Technician reader findings

Diagnostic comprehension findings from the `technician-reader` agent, one
block per round. Advisory; the evaluator's findings govern release.

## Round 1, 2026-10-31

Reader configured at level 2. Twenty comprehension findings. The reader's
summary of the conclusions matches the paper's actual conclusions (all three
answers stated correctly), so no mismatch finding is raised. The reader's
closing remark: it could state the answers but could not say why the
village story, the board-reading discussion, and the source critique take up
so much of the note.

| Id | Location | Defect | Correction |
|---|---|---|---|
| R1 | Abstract, Section 1.1 | The abstract never says this is a study note answering a lecture's three questions; "as reported to us" is undefined. | One sentence in the Introduction on who set Q1 to Q3 and that the board and assignment are the only sources; define or drop "as reported to us". |
| R2 | Abstract | Q3 is a definition, yet the abstract lists it as answered and says "Both statements are proved in full"; the reader cannot tell what Q3 establishes. | Say Q3 is settled by fixing a definition and that the textbook uses "path" differently. |
| R3 | Section 1.3 item 5, Definition 2.9 | The board's V is the edge set but the paper's V is the vertex set; both appear in one paragraph. | Move the board-notation discussion to Appendix A; keep G = (V, E) in the main text with one footnote on the mismatch. |
| R4 | Section 1.3 item 4, Table 1 | Path, simple path, and trail appear in a story dictionary before any is defined; the textbook's "path" is the paper's "trail". | A three-line mini-table (textbook word, this note's word, meaning) at that point, or a pointer to Table 4. |
| R5 | Section 1.2 and plain-words paragraphs | The village layer adds a second vocabulary; several paragraphs bring in ideas the formal text has not reached ("shortest trip", "infinite"). | State at the top of Section 2 that the plain-words paragraphs may be skipped; keep the story only where it adds meaning. |
| R6 | Definition 2.40 | Distance is defined via the textbook's "path" (a trail) and relies on Proposition 2.47 seven pages later; "metric space" unexplained. | Define distance as the length of a shortest walk; drop or gloss "metric space". |
| R7 | Proposition 2.35 proof | The step from "u_b differs from u_a and u_{a-1}" to "the edges differ" is compressed. | Add "since b > a, b >= a+1, and all vertices have distinct indices" and state the conclusion explicitly. |
| R8 | Remark 2.20, Definition 2.19 | A walk is defined with edges then silently replaced by vertex sequences; Theorem 3.5 depends on the swap. | Move the vertex-sequence characterization into Definition 2.19. |
| R9 | Proof of Proposition 4.5 (i) to (ii) | The symbol l is introduced and never used; why the corollary is needed is unclear. | "A path has at most N-1 edges (Corollary 2.46), so it is a walk of length k with 1 <= k <= N-1." |
| R10 | Proof of Theorem 4.6, condition (c) | Proved by forward reference to Proposition 4.17 whose proof is in Appendix C.4; the idea appears only in plain words. | Add the one-sentence binomial-expansion argument inline, or move that half of the proof up. |
| R11 | Remark 4.9 | Mixes the diagonal, N = 1, and N = 2 cases; unclear whether needed for Theorem 4.6. | Say "not needed for Theorem 4.6" and split off N = 1. |
| R12 | Remark 4.16 | "Labelled paths" undefined; the step to N!/2 and the link to Table 6 are only asserted. | Add "(N! orderings of the vertices along the path, each counted twice because it can be read in reverse)". |
| R13 | Remark 4.18, Table 6 caption | Breadth-first search in one dense sentence; "queue", "adjacency lists", "independent" unexplained. | A three-line procedure or a tie to the plain-words "mark neighbours repeatedly"; say what "independent" means. |
| R14 | Example 6.1 | A^{k+2} = 2A^k for k = 1 uses A^0, which Remark 3.2 says is used only in Section 4; the purpose of the pattern is unstated. | State the purpose or delete; fix the A^0 inconsistency. |
| R15 | Example 6.2 | The (I + A)^2 check uses the expansion before it is introduced and does not say what it shows. | State the expansion first, then the entry computation on separate lines. |
| R16 | Table 6 and caption | The "1" for N = 2 is unexplained; the all-graphs check rests on a script the reader cannot see. | Explain the empty-sum case in one clause; add "see Appendix D" in the caption. |
| R17 | Section 7.4 | Critique of unnamed sources; the web sources are not separated from [7]; the section's purpose is unclear. | Name the sources inline and quote the criticised sentence, or shorten to one sentence and move the detail to an appendix. |
| R18 | Section 7.5 | 98,000,000, 7, and 38,742,049 are not derived; the cost section is not tied to the three questions. | Show the arithmetic in one line each, or cut the section. |
| R19 | Section 1.4 | The reader must take on faith that the Armenian textbook lacks the results; the purpose of the paragraph is clear only on a second read. | Shorten to "The textbook, as far as we searched, has neither result, so both are proved here." |
| R20 | Section 5.2, Section 6.1 | Points to a textbook figure the reader never sees; "a trail that repeated a vertex would contain a closed trail" has no argument. | Give a four-vertex example (triangle plus pendant edge) with trail and path counts, or drop the claim; add one line on why the closed trail exists. |

Reader's summary of the conclusions, verbatim:

The note asks three things about a graph (points joined by lines) written as an adjacency matrix A, a table of zeros and ones. First, what do the entries of the k-th power of A mean? The answer is that entry (i,j) of A^k is the number of walks of length k from vertex i to vertex j. A walk may repeat vertices and edges, so the entry does not count paths. Second, how can one tell from A whether the graph is connected? The answer is that the graph is connected exactly when every off-diagonal entry of A + A^2 + ... + A^(N-1) is positive, or equivalently when (I + A)^(N-1) has no zero entry. The proof uses the fact that any walk between two vertices contains a path of no more than N-1 steps. The note shows that N-1 cannot be reduced to N-2, because a straight-line graph needs all N-1 steps. It also offers breadth-first search as an alternative. Third, what is a path? The answer is a walk with no repeated vertex, which differs from the textbook's own "path" (a walk with no repeated edge). Two three-vertex examples, one connected and one not, and a computer check over all graphs with up to six vertices support the results. I can state the answer, but I could not say why the village story, the board-reading discussion and the source critique take up so much of the note.

The full verbatim message is in `reports/technician-reader-round1.md`.

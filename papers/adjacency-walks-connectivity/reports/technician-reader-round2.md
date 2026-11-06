FINDINGS

F1 | comprehension | Abstract: "two taken from a lecture whiteboard and one from an assignment ... the textbook's definitions, the breadth-first-search comparison, and standard linear algebra are cited, not proved" | The abstract refers to a whiteboard, an assignment and "the textbook" as if I knew them. It uses I, N and "breadth-first-search" without defining them. The third "answer" is a definition, not a finding. | Name the course and textbook once. State Q3 as "what 'path' means in this course". Say "I is the identity matrix" and "BFS is an alternative method".

F2 | comprehension | 1.1: "a 3 × 3 matrix with rows 0 1 0, 1 0 1, 0 1 0 ... a drawing of three vertices" | The board is never shown. Everything that follows about it (the drawing differing from the matrix, the arrowhead, the unreadable exponent) rests on photos I cannot see. | Add a redrawn figure of the board, or move the board discussion to an appendix and keep the main text self-contained.

F3 | comprehension | 1.2 item 2: "The board uses other letters (its V is the set of edges, and it writes ei j for an edge)" | This is notation trivia about a source I have not seen. It is stated before I know what the symbols are for. | Move it to a footnote or to 2.1, next to Definition 2.9 where it is used again.

F4 | comprehension | 1.2 item 4: "The board drawing and the board matrix do not show the same graph (section 6.2). Because the problem statement says ... the matrix is the example." | I am told the two disagree but not how. The decision is made 15 pages before the evidence. | Add one clause: "the drawing has an extra edge n1 n3", or just call the example "the 3-vertex path graph".

F5 | comprehension | 1.2 item 5: "'path' means a walk with no repeated vertex ... The textbook's own word 'path' means something else, which this note calls a trail" | A key convention uses walk and trail before they are defined. The paper uses one word with two meanings. A first-time reader cannot hold this. | Put a one-line definition of walk, trail and path with a tiny example here, before the convention.

F6 | comprehension | 1.2 item 7: "As far as a search of its text showed, the textbook contains neither the walk-counting theorem nor a matrix test" | This is a claim about a source I cannot check. It is also not clear why it matters to the reader. | Say why the claim matters ("so we prove both ourselves") and drop the search detail from the introduction.

F7 | comprehension | 1.3 and Table 1: "group of islands | connected component"; later Definition 5.6: "connectivity components" | The terms differ between table and text. The table also lists "ring trip", "distance" and "degree" before they are defined. | Use one term throughout and mark in the table which rows are needed for Q1 to Q3.

F8 | comprehension | 1.5: "section 2 up to definition 2.18, then definitions 3.1, 3.13 and 3.17, lemma 3.30, and corollary 3.32 ..." | The reading guide is a string of forward numbers that mean nothing to me yet. I cannot tell which are essential. | Replace it with one sentence per section on what it contributes, or drop the numbers.

F9 | comprehension | Definition 2.9 text: "the board writes ... Ai j = 1 if ei j ∈ V and 0 if ei j ∉ V" | The board's own notation is stated, with V as a set of edges. It contradicts V as vertices in the same paragraph's neighbours. It is a distraction at the point where the key definition is given. | Delete or footnote it.

F10 | comprehension | Proposition 2.17(4) proof: "which is the textbook's Theorem 1.2.1 (Euler)" and "Since A is symmetric, column sums are the degrees too." | The counting argument (each edge counted at both ends) is compressed. The column sum claim is dropped in without reasoning. | Add "because A_ij = A_ji, the column sum equals the row sum".

F11 | comprehension | Definition 2.18: "The transpose X^T ... the standard rule (XY)^T = Y^T X^T is used in section 4." | The transpose appears as a side remark with no stated purpose until section 4. | Introduce the transpose in section 4.3 where it is used.

F12 | comprehension | Section 3 intro: "the classification of every sequence below was checked by script (appendix A)" | I must take the scripted check on faith. The appendix gives only file names. | Say the examples are small enough to verify by hand, or show the checking rule.

F13 | comprehension | Definition 3.21: "A cycle is a closed trail of positive length whose only repeated vertices are its first and last" | I read this three times. "Closed trail" and "repeated vertices" stack up. | Add: "a cycle is a loop around the graph that never passes through the same vertex twice, except that it ends where it began".

F14 | comprehension | Definition 3.25 / Remark 3.26: "The distance d(u, v) is the length of a shortest (u, v)-trail ... (The textbook words this with its own 'path', that is, trail.)" | Distance is defined with a notion (trail) that the next remark replaces with walk or path. The reader sees three definitions at once. | Define distance by walks directly and note that the textbook uses trails.

F15 | comprehension | Lemma 3.29 proof: "Both are impossible, because s < t." | The two cases s−1 = t−1 and s−1 = t are dismissed in one clause. The case split rests on an unexplained reading of "edge equals edge". | Write each case on its own line: "s−1 = t−1 means s = t; s−1 = t means s > t".

F16 | comprehension | Lemma 3.30 statement: "there is a path from u to v of length at most k whose edges are edges of W" and proof: "(Ordinary induction would assume it only for length k − 1 ...)" | "Contains" and "edges of W" are undefined. The induction argument is dense. | Define "a path contained in W". Shorten the proof around the picture in Example 3.31, which is placed after it.

F17 | comprehension | Corollary 3.32: "The bound is attained: the path graph on N vertices has a path of length N − 1." | "Path graph" is never defined. It is easily confused with "path". | Write "a graph whose vertices lie in a row n1 n2 ... nN".

F18 | comprehension | Proposition 3.34 proof: "Every path is a trail and every trail is a walk (lemma 3.29), so Lw ≤ Lt ≤ Lp." | The step from "every path is a trail" to "least trail length ≤ least path length" is not explained. Lemma 3.29 proves only the first inclusion. | Add: "the minimum over a larger set cannot be larger".

F19 | comprehension | 4.1 closing paragraph: "The same induction works for directed graphs and multigraphs [2, Proposition 2, p. 1], which are outside this note's scope." | Directed graphs and multigraphs are used without definition. The claim is taken on faith. | Delete it or define the terms in one phrase.

F20 | comprehension | Example 4.2: "the script also compared the matrix power with a direct enumeration ... on all 64 labelled simple graphs on four vertices" | "Labelled" is defined only in section 6.1. The sentence interrupts a worked example, and the reader must trust the script. | Move it to 6.1 and refer to it from here.

F21 | comprehension | Example 4.2 closing: "every edge joins n2 to n1 or n3, so each hop alternates between the middle vertex n2 and an end vertex" | The parity argument is stated but not connected to the zero entries. A reader may not see why (A^2)_12 = 0 must follow. | State: "so walks between n1 and n2 have odd length, so even powers give 0".

F22 | comprehension | 4.4: "it can also agree, as in the triangle, where (A^2)_12 = 1 counts the single walk n1 n3 n2" | The triangle graph and its matrix are not introduced until section 6.2. The reader cannot check this. | Define the triangle here (three vertices, all pairs joined), or cite 6.2.

F23 | comprehension | 4.4: "by the remark after definition 3.17" and Corollary 4.7: "(see section 6 for what their proof reads into a non-zero entry)" | These are cross-references by description or to an unspecified place. "Their" has no antecedent that makes sense without section 6.4. | Cite remark 3.18 by number. Say "see 6.4".

F24 | comprehension | Definition 5.6: "each taken together with the edges of G that join two of its vertices (the subgraph induced on the class)" | "Subgraph" and "induced" are used with no definition. They are not used again in the answer to Q2. | Drop the induced-subgraph clause or define "subgraph" in one line. Say that components are just groups of vertices.

F25 | comprehension | Between Definition 5.1 and Lemma 5.5: "A relation ∼ on the vertices ... equivalence relation; it splits the set into equivalence classes" | This is a block of abstract vocabulary inserted in the middle of the friends story. The paper itself says components are not used in the proofs of the tests. | Mark the whole subsection "not needed for the tests", or move it after 5.4.

F26 | comprehension | Theorem 5.13 proof: "The binomial theorem (X+Y)^n = ∑ (n choose k) X^k Y^(n−k) holds for matrices that commute" | The binomial coefficient notation and the commuting condition are taken on faith. Why (I+A) is introduced at all (what the test buys) is never said. | Add one line on motivation: "I+A lets walks 'stay put', so one product holds all lengths up to N−1".

F27 | comprehension | Example 5.15: "they form two blocks along the diagonal, a 2 × 2 block and a 1 × 1 block" | "Block" structure is asserted and "every entry that links two components is zero" is stated without the reasoning. | Add a sentence on why: "no walk exists between components, so every such entry counts zero walks".

F28 | comprehension | Example 5.16: "the only power tried by a test that used A^(N−1) alone would be A^2, and (A^2)_12 = 0 although n1 n2 is an edge" | I read this three times. It is a hypothetical about a test no one proposed. Its "plain words" paragraph sits before it and talks about a different example. | Rephrase: "Suppose we looked only at A^2 for N = 3. Its entry for n1, n2 is 0, yet they are adjacent."

F29 | comprehension | 5.5: "reaching A^(N−1) from A takes N − 2 products ... about N^3 multiplications" | The cost comparison is given in unexplained "operations" with no stated conclusion about N^4 versus N^2. The words "the cheap way" are left vague. | State the totals: roughly N^2 for BFS and roughly N^4 for the matrix test.

F30 | comprehension | 5.5: "This is the note's interpretation of the two sources for its own definition of connected, which neither source states in exactly this form; the BFS lemma is cited and not proved here." | The section's purpose is unclear: is BFS an answer, a check, or a foil? The hedging obscures what I should conclude. | Open the section with one sentence stating its role ("a different method, for context only").

F31 | comprehension | 6.4: "Paramadevan and Sotheeswaran, Theorem 1 ... Read as paths in the sense of definition 3.13 it is false" and the Bai paragraph: "Bai's own convention for a cycle was not read, so this refutation is made for the restatement in this note's notation." | A reader has no reason to care about errors in other papers. The last sentence is hard to follow, and the whole paragraph claims a refutation that depends on an unread definition. | State the purpose in one sentence at the top ("the word 'path' is used loosely in some sources"). Cut the Bai caveat down to one clause.

F32 | comprehension | 6.2: "Read literally, the drawing is the triangle on n1, n2, n3" and "reads the arrowhead as a stray mark" | The central example rests on guessing handwriting I cannot see (see F2). | Show the figure, or state that the paper's results do not depend on the guess.

F33 | comprehension | Appendix A: "scripts/m3_connectivity.py", "scripts/walk_path_lemmas.py" | "m3" is an unexplained internal name, and the scripts are not in the document. The counts 1, 1, 4, 38, 728, 26704 are taken on faith. | Give the scripts plain names, and say the counts are checked output, not needed by the proofs.

F34 | comprehension | Whole paper (sections 1.2, 6.5, appendix A) | Roughly a third of the text is about sources, page numbers, and what was or was not read. A technician reader cannot tell which of this affects the answers. | Group all provenance in one short "Sources and limits" section after the conclusion, and leave the mathematical sections to the mathematics.

READER SUMMARY
The paper asks three things about the adjacency matrix A of a finite graph, which is a table of 0s and 1s showing which vertices share an edge. (1) What do the entries of the powers A^k mean? It answers that entry (i, j) of A^k counts the walks of length k from vertex i to vertex j, where a walk may revisit vertices and edges. These are not paths, which may not revisit vertices. (2) How can A show that the graph is connected, meaning every vertex reaches every other? It answers that the graph is connected exactly when every off-diagonal entry of A + A^2 + ... + A^(N−1) is positive, and equally when every entry of (I + A)^(N−1) is positive, with N the number of vertices. The cutoff N−1 is the longest a path can be. A single power such as A^2 is not enough. (3) What is a "path" in this course? It answers that a path is a sequence of pairwise distinct vertices with consecutive ones joined by an edge. The textbook's word "path" means something looser, which the paper calls a "trail". The two definitions give the same connected graphs. The proofs go by induction on k for the walk count, and by showing that any walk can be shortened to a path of length at most N−1.

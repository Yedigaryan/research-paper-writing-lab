# Technician reader findings

## Round 0

Pre-read of the first draft, before evaluation round 1. Source: reports/technician-reader-round0.md.

F1 | comprehension | Section 1.1, "A lecture board shows a small drawing ... [2, 3]. The board says ... A third question comes from the assignment text, which the user reported to us." | The reader cannot see the board photos or the assignment text. The note never says who "the user" or "us" is, and it never says what the "board" is for a stand-alone reader. | Add one sentence before Q1 saying this note is a reply to a student's lecture photos and assignment. Say that the board content is reproduced in full here, so the reader needs no photo. Replace "the user" with "the course".

F2 | comprehension | Section 1.1, Q1: "The board writes a small mark above the letter A; we read it as a power k (convention 2)." | The reader does not know what mark is meant, or why it is uncertain. The question as posed is not self-contained. | Rewrite Q1 directly: "What does entry (i,j) of A^k represent?" Move the uncertainty about the board mark to convention 2 only.

F3 | comprehension | Section 1.3, convention 3: "The matrix has a 1 only for the pairs 1, 2 and 2, 3. The two disagree on the pair 1, 3 ... the arrowhead is read as a stray mark" | The pair notation "1, 2 and 2, 3" is ambiguous; it can be read as three numbers. The reader cannot see the drawing's third line or the arrowhead, so the argument cannot be followed. | Write the pairs as (1,2) and (2,3). Describe the drawing in words ("the drawing has an extra line 1-3"). Point to Fig. 1(b) at this spot.

F4 | comprehension | Section 1.3, convention 4: "the board's V in that sentence is the textbook's E" | The sentence is hard to parse without seeing the board. It is not clear why the board's "(G, V)" and "eij ∈ V" imply this. | State the board's sentence in full, e.g. "(G,V) with e_ij ∈ V", and say that the board uses V for the edge set where the textbook uses E.

F5 | comprehension | Section 1.3, convention 7, and Fig. 2: "drawn after the textbook's Fig. 1.2.5 ... we read the edge list from the page image. All the textbook's statements about that figure that we checked hold on this reading." | The reader must trust a graph they cannot verify. It is not stated which statements were checked, or why the five-town map is needed at all. | Say that the edge list is given in the Fig. 2 caption and that nothing depends on the textbook figure. Drop the "checked" sentence or name the checks.

F6 | comprehension | Section 1.4, "A search of the text layer of the whole book for the word 'matrix' finds the adjacency matrix only on printed pages 7, 11, 12, 34 and 61 ... The text layer drops most symbols" | "Text layer" is jargon. The inference "the textbook has no such theorem, so we prove it" rests on a weak search. The paragraph also lists sources before the reader needs them. | Replace with "we searched the textbook's text for 'matrix' and did not find the theorem". Move the source-by-source detail to Appendix B.

F7 | comprehension | Section 1.2 and Table 1 (story dictionary, "trail = trip that uses no road twice", "cycle = round trip that uses no road twice") | Every definition is told twice, in story words and in technical words. Some plain-words paragraphs are nearly identical, for example the two "A round trip ends in the town where it began." paragraphs before Def. 2.11 and Def. 2.17. This adds length and some confusion about which vocabulary is the real one. | Remove the duplicate sentence. Say in Section 1.2 that the story words are only an aid and never appear in statements or proofs.

F8 | comprehension | Section 2.2, Def. 2.9: "A walk of length k from u0 to uk is a sequence u0, e1, u1, ..., uk−1, ek, uk of vertices and edges with et = ut−1 ut for 1 ≤ t ≤ k" | The subscripts are dense, and the later switch to vertex-only lists (Remark 2.10) is easy to miss. | Add a short worked line: "n1, n2, n3 means edges n1n2 and n2n3, so length 2". Put it before the formal version.

F9 | comprehension | Def. 2.15 and the passage after it: "For ni ≠ nj it is the textbook's simple (ni, nj)-path ... which the textbook states as a trail whose vertices are pairwise distinct; Proposition 3.1 shows that the condition on the edges is then automatic." | The paragraph depends on a forward reference. It also leans on the textbook's "path" and "simple path" terms, which are only sorted out in Table 2, two pages later. | Place Table 2 directly after Def. 2.15, or move the textbook comparison out of the definition into Section 3.1 and keep Def. 2.15 self-contained.

F10 | comprehension | Section 2.1, Def. 2.7 versus Def. 2.21 | The symbol d is used for degree, d(ni), and for distance, d(u,v). The note does not warn the reader. In Remark 5.12 and Prop. 4.3(4) the two meanings sit close together. | Use deg(ni) for degree, or state in the notation list that d with one argument is degree and d with two arguments is distance.

F11 | comprehension | Section 3.2, proof of Prop. 3.1: "so ua−1 is equal to ub−1 or to ub. Both of these have an index larger than a − 1, because b − 1 ≥ a. That contradicts the distinctness of the vertices." | A step is missing. The equation {ua−1, ua} = {ub−1, ub} gives two cases. The reader has to supply why each case produces a repeated vertex, and the second case is not worked out. | Write both cases: "if ua−1 = ub−1 then indices a−1 ≠ b−1 give a repeat; if ua−1 = ub then a−1 ≠ b gives a repeat".

F12 | comprehension | Section 3.3, Lemma 3.2 proof: "Delete ua+1, ..., ub. The result is u0, ..., ua, ub+1, ..., uk (if b = k it ends at ua = uk = v)." | The reader must re-read this to see that the cut keeps one copy of the repeated vertex. The new length k − (b − a) is not derived. | Add a small example: "walk 1,2,3,2,4 with a=1, b=3 becomes 1,2,4 (length 4 becomes 2)". Count the deleted vertices explicitly (b − a of them).

F13 | comprehension | Section 4.2, proof of Prop. 4.3: "Using (XY)^T = Y^T X^T repeatedly and A^T = A" and "By (1) and (1), (A²)ii = ..." | The transpose is used with no definition. "(1) and (1)" is garbled: it should be (1) of the proposition and Eq. (1) of Def. 4.1. The row-sum/degree argument is compressed into one sentence. | Define transpose in one line. Rewrite as "by Prop. 4.3(1) and Eq. (1)". Split the proof into four labelled lines.

F14 | comprehension | Section 4.3, proof of Thm 4.4, step: "because Atj = 1 allows exactly one last step from nt to nj and Atj = 0 allows none. By the induction hypothesis the right side is Σ(A^k)it Atj = (A^(k+1))ij by (1)." | The link between the counting identity and the matrix product is stated tersely. The final "by (1)" is ambiguous because three equations are numbered (1). | Say "by the definition of the product, Eq. (1) in Def. 4.1, and A^(k+1) = A^k A". Number equations and propositions with different schemes.

F15 | comprehension | Example 4.6 and Prop. 4.7 proof: "(A³)12 = 2 ... but a graph with 3 vertices has no path of length 3 by Proposition 3.4(c); and neither of the two walks counted uses its edges only once." | The claim "no path of length 3" and the claim about trails are both needed, but the sentence runs them together. The reader must check the walks against the edge list by hand. | Split into two sentences. Name the walks again (n1,n2,n1,n2 and n1,n2,n3,n2) and state which edge each one repeats.

F16 | comprehension | Table 3 (counts of walks, trails and paths from n1 to n5) | The trail and path columns are claimed with no way to check them in the text. For example, why does the trail count drop to 0 at k = 8 and paths to 0 from k = 5? The only pointer is the Appendix B script. | Add one sentence on how the columns were obtained (exhaustive enumeration on the 5-town map). Explain the 0 entries with the trail bound of 8 edges and the path bound of 4.

F17 | comprehension | Section 4.5: "Paramadevan and Sotheeswaran state in their Theorem 1 that the entry counts 'different paths' ... this is not correct as written" | This is a claim that a published result is wrong. The reader has to take the reading of the source on faith. The wording is also awkward ("if their word is read as 'walk' it agrees"). | Quote the source's sentence in full. Say that the only point is the word "path" and that the content matches Thm 4.4 when "path" means "walk".

F18 | comprehension | Section 5.1, Example after Remark 5.2: "the paths n1, n2, n2, n3 and n1, n2, n3 join the pairs of vertices" | "n1, n2, n2, n3" is not a valid walk, because n2 is repeated and there is no loop. It reads as a typo for two separate paths (n1,n2 and n2,n3). | Write "the paths n1,n2 and n2,n3 and n1,n2,n3 join all pairs of distinct vertices".

F19 | comprehension | Def. 5.3: "The relation 'there is a path between u and v' is an equivalence relation on V ... Its classes induce subgraphs of G" | "Equivalence relation" and "classes" are used without explanation. The reader has no reason to believe transitivity and no pointer to it. | Add "equivalence class = a group of mutually reachable vertices". Add "transitivity: join two walks (Cor. 3.3)".

F20 | comprehension | Remark 5.6: "In our reading, the proof of Theorem 2 of Paramadevan and Sotheeswaran [5, p. 17] treats the entries as counts of paths and passes from a nonzero entry to a path without this step" | Another critique of a source that the reader cannot check. The remark mixes two jobs: the technical point (why Lemma 3.2 is needed) and the source critique. | Keep the technical point in the remark. Move the source critique to Section 6 with a quotation.

F21 | comprehension | Corollary 5.7 and Appendix A, "the binomial theorem applies ... where (N−1 choose k) is the number of ways to choose k items from N−1 items" | The reader must know that I and A commute and why the binomial theorem needs this. The expansion is stated in the main text without the exponent N−1 being motivated. | Add one sentence: "the binomial theorem holds for matrices that commute, and I commutes with everything". Say why N−1 is the right exponent (the same bound as in S).

F22 | comprehension | Remark 5.13: "This is an experimental finding, a computation on four graphs, and it illustrates Proposition 3.4(c) without proving it ... A limit below N − 1 would miss such a pair." | The remark claims sharpness, but four graphs and an unproved sentence do not show it. The reader does not see why the path graph is the extreme case. | State the argument: in a path graph the only route from n1 to nN has N−1 edges, so no smaller power can be positive. This is a proof, not an experiment.

F23 | comprehension | Section 5.5: "both matrix tests of this section gave the same answer as a breadth-first search from n1 [4]" | "Breadth-first search" is used here before it is explained in Section 5.6. The reference [4] is a local script the reader cannot open. | Move the BFS paragraph before 5.5, or add a half-sentence definition here. Say what the script checks, in words.

F24 | comprehension | Section 5.6: "repeatedly adds every nj with Akj = 1 for some nk already in the set" and "By our own count, forming S takes N − 2 matrix products" | k is used here as a vertex index, but everywhere else k is an exponent. The "N − 2 products" count is unexplained (computing A² to A^(N−1) iteratively), and the comparison with BFS cost is not stated in comparable units. The section's purpose in the note is unclear. | Rename the index to m. Justify the count in one sentence. Say whether the section exists only as a cross-check.

F25 | comprehension | Section 6, "Where sources disagree ... We resolved both by proving the statements here." and "Strength of the evidence" | The Discussion repeats material from Sections 4.5, 5 and 1.4. The reader is told twice about the source critiques and the limits of the text-layer search. Only some of it is new. | Condense Section 6 to the limits that have not appeared before: directed graphs, multigraphs, finite computer checks.

F26 | comprehension | Abstract, "compared with the textbook's definitions and numbering ... each definition and theorem is introduced by a short paragraph in plain words." | The abstract spends space on the note's format and on a textbook the reader has never heard of. This hides the results. | Delete the format sentence. Replace with "Proofs are given and checked by computation up to 6 vertices".


## Round 1

Evaluation round 1. Source: reports/technician-reader-round1.md.

F1 | comprehension | 1.1, "the entry counts the walks of exactly k roads from ni to nj (Theorem 4.4); it counts walks, not paths (Proposition 4.7)" and "with every word defined in Section 2" | The short answers use "walk", "path" and "road" before any definition. Table 1, which explains "road", comes a page later. Section 2 does not define "road" either, only edge. A first-time reader meets three undefined words in the answer to Q1. | Move Table 1 before the short answers, or add one clause to each short answer, e.g. "a walk (a trip that may revisit towns and reuse roads)".

F2 | comprehension | 1.3 item 4, "defines Aij = 1 if eij ∈ V and Aij = 0 if eij ∉ V ... So the board uses V for the set of edges where the textbook uses E" | The sentence is hard to parse. It is unclear whether the board's V is the edge set, and why this matters later. | Say in one line that the board's V means "set of edges", and that this note always uses E. State that the board's notation never appears again.

F3 | comprehension | 1.3 item 2, "a small letter between quotation-like strokes that could be read as k or n" | The reader cannot see the board. The claim that the mark is ambiguous must be taken on faith. The reason "the assignment asks about powers Ak" is not shown. | Quote the assignment sentence. Add a one-line note that the result holds for any exponent name, so the ambiguity is harmless.

F4 | comprehension | 1.3 item 3, "the arrowhead is read as a stray mark because the matrix is symmetric" | The drawing disagrees with the matrix (an extra 1-3 line). The text decides that the matrix wins, but only the problem statement is offered as the reason. The reader cannot check the drawing. | Say explicitly that Fig 1(b) is a hypothetical extra example, not a claim about the lecturer's intent. Add a cross-reference to Example 5.10.

F5 | comprehension | 1.3 item 6, "so that A0, the identity matrix, also counts walks" | The reason is stated in one clause only. The reader does not see why a length-0 walk matters later: Lemma 3.2 base case, path of length 0, and the diagonal of (I+A)^(N-1). | Add "this is used in Lemma 3.2, Remark 2.16 and Appendix A".

F6 | comprehension | 1.3 item 7 and Fig. 2 caption, "we read one from the page image ... The textbook's own examples ... come out as the book says on this list" | The edge list rests on an inaccessible Armenian textbook. Table 3 and many examples depend on the list. The reader must take on faith that it is the textbook's graph. | State that nothing depends on matching the textbook. The five-town map is simply defined by its edge list, and the textbook is only the inspiration.

F7 | comprehension | 2.2, Definition 2.13 and Definition 2.17, "The textbook calls this a 'path'" and "A cycle is a closed trail" | The note uses "cycle" for a closed trail and says "simple cycle" for the usual meaning. This is the reverse of the common English usage. The reader must remember two non-standard meanings while reading the examples. | Add a short warning line "(in most English texts this is called a closed trail; cycle usually means our simple cycle)". Or drop cycles, since they are not used later.

F8 | comprehension | 2.2, Definition 2.15, "A path between ni and nj is a walk w0, ..., wk with ... pairwise distinct" combined with Remark 2.16 | Pairwise distinct vertices with w0 = wk = ni appears to be impossible for k > 0. Only the remark says the case i = j gives length 0. The reader must infer it. | Put "if ni = nj the only path is the one-vertex walk" in the definition itself.

F9 | comprehension | 3.2, Proof of Proposition 3.1, "so there are two cases. If ua−1 = ub−1 ... If ua−1 = ub ..." | The reader is not told why there are only two cases. The case ua = ub−1 / ua = ub is not obviously covered. The set equality {ua−1, ua} = {ub−1, ub} gives two matchings, which should be said. | Write "since two equal 2-element sets match their elements in one of two ways".

F10 | comprehension | 3.3, Lemma 3.2 proof, "Delete the b − a vertices ua+1, ..., ub; one copy of the repeated vertex, ua, stays" | The proof is stated abstractly. The indices a < b and the "new pair of neighbours" argument need two readings. The example is placed in the middle of the proof. | Put the example (1,2,3,2,4 → 1,2,4) before the general step. Label the three claims: still a walk, same ends, shorter.

F11 | comprehension | 3.2, the paragraph "The textbook states Definition 1.2.13 as a trail whose vertices are pairwise distinct. By Proposition 3.1 a walk with pairwise distinct vertices is already a trail" | This paragraph relies on a source the reader cannot see. It is not needed for the later argument. The reader cannot tell why it is there. | Delete it or move it to Appendix B.

F12 | comprehension | 4.1, Definition 4.1 and Remark 4.2 | The sum over a middle index t is explained, but the equation's link to walks is only hinted at ("pick a middle town"). The purpose of the definition is left implicit until Theorem 4.4. | Add one sentence: "This is the formula whose terms will be matched to walks in Theorem 4.4".

F13 | comprehension | 4.2, Proposition 4.3(b)-(d) | The proposition is not needed for Q1 or Q2 except (d) in Proposition 4.7. The section's purpose is unclear until later. The transpose paragraph appears between the statement and the proof. | Say at the start "(d) is used in Proposition 4.7; (b) and (c) are for completeness", or remove (b) and (c).

F14 | comprehension | 4.4, Example 4.6, "All these matrices were computed by exact integer arithmetic and the walks were listed by direct enumeration (Appendix B)" | The reader is not shown the multiplication for A2 and A3. A reader checking by hand has no worked intermediate step apart from the (A2)22 example. | Show A3 = A2·A for one entry, or state that the matrices are 3x3 and easy to verify by hand.

F15 | comprehension | 4.5, Table 3 and caption, "The counts were obtained by listing all walks of each length on the map" | The trail and path columns are claims the reader cannot check by hand. The k = 7 value of 16 trails and the k = 8 value of 0 are taken on faith. The caption says a trail of length 8 "would have to use every road once, and the listing finds none" without saying why none exists. The cause is that vertices 2 and 3 have odd degree. Eight edges also need an Euler trail, and the graph has four odd-degree vertices, so none exists. | Give the Euler-trail reason in one line, or say "from computation, see Appendix B". Point to which script produces the table.

F16 | comprehension | 4.5, "Paramadevan and Sotheeswaran state a related theorem in terms of 'paths'; the only point is their use of that word, and we discuss it in Section 6. We use their paper for the statement of the test in Section 5." | This paragraph points forward and gives no content. Why the reader should care about the cited paper is unclear here. | Delete it from 4.5 and keep only the Section 6 discussion, or add one sentence on what the paper claims.

F17 | comprehension | 5.1, Definition 5.3 | A single definition contains three jobs: the equivalence relation, the proof that it is one, and the definition of an induced subgraph. It had to be read three times. | Split into Definition (relation and component), Lemma (it is an equivalence relation, with the proof), and a separate sentence for the induced subgraph.

F18 | comprehension | 5.2, Theorem 5.5 plain-words paragraph, "We only need to try a few numbers of roads." | "A few" is vague. The reader is not told that the bound is N−1 until the end of the paragraph. | Write "only up to N−1 roads, because a path has at most N−1 roads".

F19 | comprehension | 5.2, after Corollary 5.7, "The idea is this. The binomial theorem holds for matrices that commute ..." | The main equivalence is justified only in Appendix A, so the body asks for faith. The note itself says "No source ... states the test in this form", so the claim rests wholly on the appendix. The binomial-for-commuting-matrices fact is assumed without a reference. | Cite a linear algebra reference for the commuting binomial theorem. Mention that Example 5.8 checks (I+A)^2 = I + 2A + A^2.

F20 | comprehension | 5.3, Example 5.10, "every entry of S is 2 and every entry of (I + A)2 is 3" | S for the triangle has diagonal entries of 2 (the earlier text said off-diagonal). The matrices are not displayed, so the reader cannot verify them. The diagonal of (I+A)^2 for the triangle needs its own check. | Show the matrices S and (I+A)^2 for the triangle, or say "diagonal 3, off-diagonal 3".

F21 | comprehension | 5.4, Proposition 5.13 proof, "a walk of length N−1 must use +1 at every step" | The reasoning is stated as obvious, but it needs the observation that N−1 steps with total change N−1 leave no room for a −1. The proof reads quickly past this. | Add "since N−1 steps of ±1 with sum N−1 must all be +1".

F22 | comprehension | 5.5, "By our own count, forming S takes N − 2 matrix products ... These are different units, so we make no claim about running time." | The sentence is cryptic. Which units differ? Why compare and then disclaim? The section's purpose, a "cross-check", is unclear. | Replace with "matrix products and row reads cannot be compared directly, so we do not compare cost", or drop the cost remark.

F23 | comprehension | 5.6, "A program listed every labelled simple graph with N = 1, ..., 6 vertices (1, 2, 8, 64, 1024 and 32768 graphs, of which 1, 1, 4, 38, 728 and 26704 are connected)" | The counts of connected graphs are asserted. The reader cannot check them, and no known sequence or formula is given. Reference [4] is a local file the reader cannot open. The 2^(C(N,2)) count of labelled graphs is not stated. | Add "2^(N(N−1)/2) labelled graphs". State the program inputs or give the OEIS-style sequence, noting that this has not been verified against an outside source.

F24 | comprehension | Appendix B and ref. [4], "m3 connectivity.py" vs "appendices/computations.py" | Two different program names appear: one for the exhaustive check, one for every number in the text. It is unclear which program produces which result. | Use one name, or say what each program does.

F25 | comprehension | References [2], [3], [7] | The board photos and the Armenian textbook are local files. About a dozen statements, such as "textbook Definition 1.2.13, p. 22", cannot be checked by any reader. | Add a short note in 1.4 that textbook citations serve only for matching names, and that the proofs are self-contained.

F26 | comprehension | 1.2, "Before every definition, theorem and worked example there is a short story paragraph ... The story words are only an aid. They never appear in statements or proofs." | The "In plain words" paragraphs break this rule at times. Example: "Note each town once" and "stay-at-home option" use new words not in Table 1. A reader may take them as technical terms. | Add "stay-at-home" and "endless" to Table 1, or avoid them.

F27 | comprehension | 1.3, notation list, "t (indices)" and "S" | The symbol t is used for the edge index in Definition 2.9 (et = ut−1 ut), for the summation index in Eq. (1), and for the middle vertex nt. Meanings overlap despite the claim that t "keeps one meaning". | Use a different letter for the edge index (s), or drop the claim.

F28 | comprehension | 2.1, Remark 2.22 and Example 5.9 | Forward references to Proposition 3.4 and Corollary 5.11 are used before their statements. The reader must accept them in advance. | Say "(proved in Section 3)" and "(Corollary 5.11 below, stated for later)".


## Round 2

Evaluation round 2. Source: reports/technician-reader-round2.md.

F1 | comprehension | Abstract: "the entry in row i and column j of the k-th power of A counts the walks of length k from vertex ni to vertex nj" and "under the course convention a path…" | The abstract uses ni, nj, "walk" and "course convention" with no definitions. A reader without the course doesn't know which convention is meant or that it differs from the textbook's. | Add one clause to the abstract: "a walk may repeat vertices and edges; the course's 'path' may not repeat a vertex". Define ni as "the i-th vertex".

F2 | comprehension | 1.1: "a small drawing with three points … and next to it a table … [2, 3]" and "Everything on the board that matters is reproduced here" | The first paragraph is about photographs I can't see. Citations [2, 3] are local image files. I have to take the transcription of the board on faith. | Put the board matrix and a one-line description of the drawing in a displayed box. State that the photos aren't needed. Move the provenance to the appendix.

F3 | comprehension | 1.1: "Short answers; every word is defined in Section 2. Q1: … (Theorem 4.4) … (Proposition 4.7) … (Definition 2.15)" | The short answers cite theorem numbers I can't open yet. "Every word is defined in Section 2" is false for "connected" and "component" (Section 5) and for "off-diagonal". | Say "defined in Sections 2 and 5". Say what "no zero off the diagonal" means in a few words.

F4 | comprehension | 1.2 and Table 1: "table 1, which comes right after this paragraph" and the story dictionary | The table is not where the text says it is. Some story words aren't intuitive ("stay-at-home table", "endless"). I couldn't tell whether the story is part of the argument or decoration. The paragraph says story words "never appear in statements or proofs", yet the short answers use them. | Place the table where it is announced. Drop the unneeded rows (identity, infinite distance, cycle). Say once, up front, that the story paragraphs can be skipped.

F5 | comprehension | 1.3 convention 2: "a small letter between quotation-like strokes that could be read as k or n … The assignment, as it was reported" | "As it was reported" doesn't say by whom. This is board-reading detail that doesn't affect the mathematics. | Cut to: "We write the exponent as k." Move the reading doubt to the appendix.

F6 | comprehension | 1.3 convention 3: "the arrowhead is read as a stray mark because the matrix is symmetric" and "The drawing's three-road map (fig. 1(b)) is also computed, as a side example" | I had to reread this three times. It is not clear which graph is the main example. The reasoning "stray mark because symmetric" is a guess, though it is stated as settled. | Open with "Main example: fig. 1(a). The board drawing disagrees with the board matrix; we use the matrix." Then give the side example in one sentence.

F7 | comprehension | 1.3 convention 4: "the board writes (G, V) … Aij = 1 if eij ∈ V … So the board's V means the set of edges" | The notation is garbled in the text. It isn't clear whether the board has a typo or a different meaning. The textbook page-offset remark is irrelevant to the reader. | Say: "The board writes V where it means the edge set; this note writes E." Delete the page-number remark.

F8 | comprehension | 1.3 convention 6: "The textbook's definition of a walk does not say so in words, but it assumes it implicitly: its distance properties give d(u, v) = 0 exactly when u = v" | The justification is about the textbook, and I can't check it. The point that matters is that A0 = I must count walks. | Replace with "We allow a walk of length 0 (one vertex), so that A0 = I fits Theorem 4.4."

F9 | comprehension | 1.3 convention 7 and Fig. 2: "we read one from the page image … Nothing depends on matching the textbook" | Reader-irrelevant provenance. Convention 7 is a list of edges in a figure caption, not a convention. | Delete the textbook references from the convention. Just say Fig. 2 is the five-town graph.

F10 | comprehension | 1.4: "We searched the textbook's text for the word 'matrix' and did not find a theorem … This shows only that we did not find them" | This is process commentary. A reader without the textbook gains nothing from it, and it raises doubt about whether the results are new. | Move 1.4 to the appendix. Keep one sentence: "Both results are proved here."

F11 | comprehension | 2.2, Definition 2.17 and Remarks 2.18, 2.20 (cycle, simple cycle) | Cycles and simple cycles are defined and exemplified but never used. The text says "Cycles are not used again after this section". I could not say why they are there. | Delete Definitions 2.17 and 2.19 along with their remarks. Or add a one-line reason.

F12 | comprehension | Definition 2.13 and Table 2: textbook word "path" for a trail, plus the "textbook number" column | Three vocabularies (textbook, English, this note) are presented before I know why they matter. Table 2 has a column of textbook numbers that mean nothing to me. | Open Section 3.1 with a single sentence, "The textbook's 'path' is our 'trail'". Drop the number column.

F13 | comprehension | Proof of Proposition 3.1: "since two equal sets of two elements match their elements in one of two ways, there are two cases. If ua−1 = ub−1 …" | I had to read it three times, and the wording hides a simple fact: a repeated edge forces a repeated vertex. | Rewrite as "If ea = eb with a < b, they share an endpoint at different positions, so a vertex repeats."

F14 | comprehension | Proof of Lemma 3.2: "deleting the 2 vertices u2, u3 leaves 1, 2, 4" | The example uses bare numbers 1, 2, 3, 2, 4 for vertices. The notation is inconsistent with ni and not tied to u0…uk. | Write the example as n1, n2, n3, n2, n4, with the u-indices shown beneath.

F15 | comprehension | Section 3 intro: "three facts that the later sections use … every path is a trail …, Lemma 3.2, … Proposition 3.4" | Proposition 3.1 and Corollary 3.3 are also used. Proposition 3.4 has three parts, (a) to (c), and only (c) is called out, which makes "three facts" misleading. | Say "four facts", or reword the list to match the numbering.

F16 | comprehension | 4.2: "parts (b) and (c) are given for completeness and are not used later" | This contradicts the proof of (d), which uses (c): "so (A2)ii = Σt Ait = deg(ni) by (c)". Part (d) is used later. | Change to "(b) is not used later; (c) is used to prove (d)."

F17 | comprehension | Proof of Proposition 4.3(b): "By (a), AT = A. Using (XY)T = YT XT repeatedly, (Ak)T = (AT)k = Ak" | The rule (XY)T = YT XT is stated without a reason. The step to powers is a one-line jump. | Cite it as the standard rule. Add "by induction on k".

F18 | comprehension | Theorem 4.4 proof: "Different t give different walks, because t can be read off the walk." | The step is sound but sketched. It is the whole reason the sum has no overlaps. | Add: "t is the second-to-last vertex of the walk, so the groups for different t are disjoint."

F19 | comprehension | Proposition 4.7: "in general neither paths nor trails" | The claim "in general" is shown by a single example, and nothing says what "counts paths" would have meant. Paths of length 3 can't occur in a 3-vertex graph, which is true but indirect. | State plainly: "The entry can be positive when no path or trail of that length exists." Then cite (A2)ii.

F20 | comprehension | Table 3 and the paragraph after it: trails column 3, 7, 6, 6, 16, 0; "In a trail that uses every road, each vertex other than the two ends is entered and left equally often" | The trail counts are not monotone (7, then 6, 6, then 16, then 0). The reader doesn't know why, and none of them can be checked without the program. The parity argument is Euler's trail theorem, but it is unnamed and the "ends" case (closed vs open trail) is not handled. | Name it ("a trail using every road is an Euler trail"). Say which columns are expected to behave oddly and why. State that the counts come from enumeration.

F21 | comprehension | Corollary 5.8 prose: "The binomial theorem holds for matrices X, Y that commute … expands into Σ C(N−1, k) Ak, a sum with positive coefficients" | The binomial coefficient notation, "commute" and "positive coefficients" are used before they're explained. The main text asserts the equivalence and defers the real argument to Appendix A. | Give one line: "(I+A)N−1 = Σ C(N−1, k) Ak, with every coefficient at least 1, so it is positive exactly where S is positive (off the diagonal)". Define C(n, k) where it first appears.

F22 | comprehension | Appendix A: "using IAk = Ak and Pascal's rule C(m,k) + C(m,k−1) = C(m+1,k) (with C(m,−1) = C(m,m+1) = 0)" | The displayed induction is hard to follow, and the statement that the binomial theorem is "proved in two lines" is not true of what follows. | Either cite the binomial theorem for commuting matrices as standard, or lay the induction out one line per step.

F23 | comprehension | Example 5.9: "The entry (A2)12 = 0 although n1 and n2 are adjacent; the entry A12 = 1 makes up for it in S." | I didn't see why this matters until the sentence after: "This is why the powers are summed". The link is implicit. | Add "Walks of exactly length 2 can't use the single edge n1 n2, which is why the test sums several powers."

F24 | comprehension | Remark 5.13 (distance): "d(ni, nj) is the least k ≥ 1 with (Ak)ij > 0 … Their proof of Theorem 3 reads a nonzero entry as a path; the proof here … is ours" | The remark mixes a new result with commentary on a published paper's proof. The reasoning ("Indeed, a walk of length k exists exactly when …") is compressed. | Split into the statement, a two-line proof, and a note about the other paper moved to Section 6.

F25 | comprehension | Proposition 5.14: "let G be the path graph with vertices n1,…,nN" | "Path graph" collides with the course's strict "path". A first-time reader may think it is a graph of one path. | Say "a chain of N towns (the path graph)". Say what the proposition is for: the bound N−1 can't be improved.

F26 | comprehension | 5.5 Breadth-first search: "we do not compare their cost" | The section is called a comparison and states that it compares nothing. Breadth-first search is introduced as a cross-check, but the reader isn't told what the cross-check gives. Its purpose is unclear. | Delete the cost sentences, or state the cost claim. Say that the section exists to give an independent algorithm for 5.6.

F27 | comprehension | 5.6: "the three answers always agreed [4]" and "of which 1, 1, 4, 38, 728 and 26704 are connected" | Nothing is shown besides the counts. The program [4] is a local file and the appendix names a different program, so I can't tell which one backs which claim. I have to take the agreement on faith. | Cite one script. Put the counts of connected graphs in a small table and say what the script prints.

F28 | comprehension | Section 6, "Two statements in a published paper" | About half a page of critique of another paper's wording that is not needed to follow the note, and is hedged ("this is an interpretation of their text"). A reader may wonder whether the note's claim is correct or only that paper's phrasing. | Cut to two sentences: "[5]'s Theorem 1 says 'paths' where it means 'walks'."

F29 | comprehension | Appendix B: "the program appendices/computations.py described below repeats those computations" alongside [4] "m3 connectivity.py" | There are two programs with overlapping roles. "Every number in the text can be rerun from that one program" conflicts with the text citing [4] for the 5.6 check. | Use one script name throughout, or say which sections each covers.


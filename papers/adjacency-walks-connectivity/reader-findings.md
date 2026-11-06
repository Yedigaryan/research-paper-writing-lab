# Reader findings

## Round 1

FINDINGS

F1 | comprehension | Abstract: "Each definition, theorem, and test is preceded by a plain-words paragraph told as a story about a frog on islands." and "the course textbook's numbering is used for its definitions" | The abstract spends space on the note's presentation and sources (whiteboard, assignment, textbook numbering, script). It never says in one plain sentence what a walk is or what "connected" means. A reader meets "walks, not paths", "A + A² + … + A^(N−1)" and "(I + A)^(N−1)" cold. | Define walk and connected in one clause each in the abstract. Move the "story" and "textbook numbering" remarks to Section 1.3.

F2 | comprehension | Abstract and 1.4 (Q2): "every entry o the diagonal of A + A² + · · · + A^(N−1) is positive" | "Off the diagonal" is hard to parse because the ligature "ff" is dropped in the PDF text. This is probably an extraction artifact, but check it. Elsewhere "o the diagonal" and "nite" also appear without their letters. | Check that the ligature glyphs render in the PDF. If they do, ignore. If not, fix the font or use microtype or no ligatures.

F3 | comprehension | 1.1: "a 3×3 matrix with rows 0 1 0, 1 0 1, 0 1 0, and a problem statement" and "(The board writes a small mark above A; see Convention 3.)" | Q1 is posed about an unreadable mark on a whiteboard photo, so the reader cannot tell what is being asked. The sentence "What does the entry Aij of a power of A represent?" only makes sense after Convention 3, which comes a page later. | State Q1 directly as "What does the entry (A^k)_ij represent?" and move the whiteboard-reading story into the conventions.

F4 | comprehension | 1.1: "The assignment text adds a third question, as it was reported to this note (the report is a summary, not the assignment's own words, and is used here as reported content) [11]." | The "report" and "summary of user statements" are not explained. The reader cannot tell who reported what, or why this affects the mathematics. | Replace with "The assignment, as relayed to the author, also asks Q3." Drop the provenance detail from the body.

F5 | comprehension | 1.2 Convention 2: "The board writes the graph as (G, V) and says 'eij ∈ V' for 'ni and nj are joined by an edge', so its V is the set of edges." | This is confusing. The board uses V for edges, the textbook uses E, and the note uses ni nj for eij. A newcomer cannot see why this matters. | Say once, "we write G = (V, E) with V the vertices and E the edges". Put the board's deviations in a footnote.

F6 | comprehension | 1.2 Convention 3: "it would change if the mark were a prime or quotation marks." | A prime would be a different object (a derivative or a transpose), and the reader has not been told what then follows. | Delete the sentence, or say what the alternative readings would mean.

F7 | comprehension | 1.2 Convention 4: "The arrowhead is read as a stray mark... The drawing read literally is a triangle; it is treated in section 6." | The reader must keep two candidate graphs in mind (a 2-edge path and a triangle) before they know what a graph example is for. | Move the drawing-versus-matrix discrepancy to 6.2. In 1.2 say only "the matrix defines the example graph."

F8 | comprehension | 1.2 Convention 5: "path means a walk with no repeated vertex... The textbook's own word path (Definition 1.2.12) means a walk with no repeated edge; this note calls that a trail" | "Walk" is used here before it is defined (Section 3.1). The nested terminology (path, trail, simple path, textbook numbers) comes before the reader has any picture of it. | Define walk in a sentence when the term first appears, or point forward ("walk, defined in 3.1"). Defer the textbook comparison to Table 2.

F9 | comprehension | 1.2 Convention 6: "It makes A⁰ = I count something, and it gives every vertex exactly one path to itself." | "A⁰ = I" and "count something" arrive before matrix powers (Section 2.2). The reason a length-0 walk is wanted is not explained. | Say "A⁰ is the identity matrix, so the walk count at k=0 must be 1 on the diagonal and 0 elsewhere. A length-0 walk gives exactly that." Or drop it until Section 2.2.

F10 | comprehension | 1.2 Convention 7: "hits only on printed pp. 7, 11, 12, 34, and 61; the two pages 7 and 11 were read..." | This process detail is not needed to follow the mathematics. A reader cannot say what "Who proves what" is for. | Replace with one sentence: "The textbook does not contain these results; we prove them here." Move the search details to the appendix.

F11 | comprehension | 1.3 and Table 1: "fresh-bridge trip | trail", "fresh-island trip | path", "ring trip | cycle", "in one piece | connected" | The story vocabulary adds a second layer of names, so the reader must keep a third set of synonyms. "Island, bridge, and hop" are easy, but "fresh-bridge" and "fresh-island" are cumbersome. The sentence "The formal text introduces the technical term before the story uses its word" contradicts the layout, because the plain-words paragraphs come before each definition. | Fix the claim to match the layout (the story paragraph precedes the definition). Consider fewer story words, or dropping the plain-words paragraphs for terms the story only restates.

F12 | comprehension | 1.4 (Q1): "It counts walks, not paths, and it is not 1 if reachable (example 4.5)." | "Not 1 if reachable" is cryptic, and the example cited (4.5) is the walks-versus-paths one. The matching non-example is 4.3. | Write "it is not simply 1 when nj can be reached from ni". Cite example 4.3.

F13 | comprehension | 1.5 / 2: "Section 2 fixes the graph, the adjacency matrix, and matrix powers." and Prop. 2.17 | The reader is told the sum of A_ij is "2|E|" via "the textbook's Theorem 1.2.1 (Euler)". The handshake result is taken on faith with no statement of what it says. | State it: "each edge is counted at both its ends, so the degrees sum to 2|E|."

F14 | comprehension | 2, Notation: "d(ni) the degree of ni" followed later by "d(u, v)" for distance (Def. 3.25) | The same letter d is used for degree (one argument) and distance (two arguments). Prop. 4.4 writes "(A²)ii = d(ni)" next to d(n1, n3) = 2 in examples. | Rename one, for example deg(ni) for degree.

F15 | comprehension | Def. 2.18: "The powers of A are A⁰ = I ... and A^(k+1) = A^k A. This is the standard definition from linear algebra." | The reader is assumed to know matrix multiplication. The formula (2) is stated, but "the sum over r" is not tied to the island picture here. The plain-words paragraph is better than the definition. | Add a tiny 2×2 numeric product, or point to Example 2.20 explicitly.

F16 | comprehension | Example 2.20: "(A²)11 = 0·0+1·1+0·0 = 1 and (A²)22 = 1·1+0·0+1·1 = 2." | The reader cannot see which row and column are multiplied. | Write the row and column vectors, for example "row 1 of A is (0,1,0), column 1 is (0,1,0)".

F17 | comprehension | Section 3 intro: "the classification of every sequence below was checked by script (appendix A)." and Fig. 1 | In the figure text the middle graph H is hard to read. Labels n2, n3 appear at the top and bottom of the extracted figure, so the layout may be confusing, and the edge list is only in prose. | Check the figure renders clearly. Repeat H's edge list in the caption.

F18 | comprehension | Def. 3.1: "a sequence u0, e1, u1, ..., ek, uk of vertices and edges in which et = u_{t−1}ut" | The notation is dense. "A walk ... is written by its vertices u0u1···uk" is only introduced in the last sentence. | Lead with the vertex-sequence form, then mention that the edges are determined.

F19 | comprehension | Def. 3.9 and Remark 3.10: "A walk is a trail if its edges u0u1, ..., u_{k−1}uk are pairwise distinct." and "it is this note's choice for the textbook's concept, because the course's word for it was not reported." | Trails are introduced only to explain a textbook naming difference, and they are never used in the main results except in Prop. 3.33. A reader asks why trails exist at all. | Say up front: "Trails matter only because the textbook uses 'path' for them."

F20 | comprehension | Def. 3.21: "A closed trail is a closed walk that is a trail. The textbook calls it a closed path or cycle... A cycle is a closed trail of positive length whose only repeated vertices are its first and last" | Cycles are not used in Q1 to Q3. Remark 3.22 introduces "two triangles sharing n1" with a long sequence. The purpose of the cycle material is not stated. | Say why cycles are included (for completeness of the textbook's order), or cut them and the "Closed trail" row of Table 2.

F21 | comprehension | Def. 3.25: "The distance d(u, v) is the length of a shortest (u, v)-trail if there is one, and ∞ otherwise" | The note says the textbook defines distance via trails, but then uses shortest paths. The reader cannot see why distance is in the paper before Cor. 4.7. | Add "Distance is used in Corollary 4.7, to read hop counts from the powers."

F22 | comprehension | Lemma 3.30 proof: "Form W′ = u0···ui uj+1···uk (if j = k, then W′ = u0···ui). It is a walk, because the only new consecutive pair is ui, uj+1 and ui = uj is adjacent to uj+1." | The subscripts i and j reuse the row and column index letters of the matrix (i, j), and "i<j" here is a position in the walk. The cut step is hard to follow in symbols. | Use different letters (s<t) for positions. Add one worked example next to the proof (Example 3.31 is after it).

F23 | comprehension | Lemma 3.29 proof: "Two equal two-element sets give u_{s−1} = u_{t−1} or u_{s−1} = u_t. The vertices are distinct, so the first forces s−1 = t−1..." | The case analysis is incomplete as printed. Equality of the sets also allows u_s = u_{t−1} or u_s = u_t. The reader must check why only two cases are listed. | Spell out all four cases or say "by symmetry".

F24 | comprehension | Theorem 4.1 proof: "there are (A^k)_ir = (A^k)_ir Arj of them." | The equation is correct only because Arj = 1, but it is printed with no word of explanation. It reads as a typo or tautology on first view. | Write "(A^k)_ir · 1 = (A^k)_ir Arj".

F25 | comprehension | Theorem 4.1 remark: "For paths the deletion of the final vertex would still give a path, but appending nj may repeat a vertex, and the one to one correspondence breaks." | Condensed. The reader sees why walks work but not concretely why paths do not. | Point to Example 4.5 (A²)11 here.

F26 | comprehension | Example 4.2: "The inductive case for (A³)12 reads, with r = 1, 2, 3, Σr (A²)1r Ar2 = 1 · 1 + 0 · 0 + 1 · 1 = 2" | The three terms are not matched to (A²)11, (A²)12, (A²)13 in the text, and the reader has to look back at the printed matrix A² to find 1, 0, 1. | Write the terms as (A²)11·A12 + (A²)12·A22 + (A²)13·A32.

F27 | comprehension | Example 4.2: "every edge joins n2 to n1 or n3, so a walk from n1 to n1 has even length, and a walk from n1 to n2 has odd length." | Parity is asserted. The reader is not told that the graph is bipartite (which would be the technical reason), and no proof is given. | Add "each hop alternates between the middle island and an end island, so" before the claim.

F28 | comprehension | Example 4.2: "the script also compared the matrix power with a direct enumeration of walks for k = 0, ..., 6 on six small graphs and for k = 0, ..., 5 on all 64 labelled simple graphs on four vertices" | "Labelled simple graphs" is not defined, and the number 64 is unexplained (2^6 edge subsets). | Add "(64 = 2^6 choices of which of the 6 possible edges are present)".

F29 | comprehension | Prop. 4.4 proof: "Since A^T = A and (XY)^T = Y^T X^T, we get (A^k)^T = (A^T)^k = A^k." | The transpose is not defined anywhere. The "In words" gloss is given after the formula and covers the claim only informally. | Define the transpose in Section 2 (flip over the diagonal) and note that (A^k)^T = (A^T)^k follows from the product rule.

F30 | comprehension | Remark 4.6 and 5.3: "a path of exactly that length can be missing." and Example 4.5: "a walk whose length equals the distance between its ends is a path" | The claim "walk of length equal to distance is a path" is stated with a one-line reason, but it is then used with "Otherwise the counts differ" and no example of a case where counts differ in value but both are positive. | Give one example, or drop the "otherwise" sentence.

F31 | comprehension | Def. 5.1: "G is connected if for any two vertices u and v there is a path from u to v." Remark 5.2: "Two readings of path are in play." | The reader has met three meanings of path, and here is told the choice does not matter. The proof for this is Prop. 3.33, 5 pages earlier, with no pointer in the definition text beyond a parenthetical. | Say in the definition, "(any of walk, trail, or path gives the same graphs; see Prop. 3.33)".

F32 | comprehension | Lemma 5.5 and Def. 5.6: "Let u ∼ v mean that there is a path from u to v. Then ∼ is reflexive, symmetric, and transitive." and "The equivalence classes of ∼, together with the subgraphs they induce" | "Equivalence relation", "equivalence class" and "induced subgraph" are used with no definition. A technician reader likely has not met them. The proof that "reversing a path gives a path" is only a phrase. | Define each in a sentence, or use the friends picture first and name the terms afterwards.

F33 | comprehension | Sec. 5, lemma 5.11 and the connectivity subsection: components are introduced (Def. 5.6, Cor. 5.10) and then never used in the proof of Theorems 5.12 and 5.13. They return only in Example 5.15. | The purpose of Section 5.1's component material is unclear. | Say that components are a reformulation, used only to describe the block shape of B in Example 5.15, or cut them.

F34 | comprehension | Theorem 5.12 proof: "Each A^k has non-negative entries (Remark after definition 2.18), so Bij = Σ ... is positive exactly when at least one term is positive." | A reader sees the key step (no cancellation, because everything is non-negative) only through a back-reference. The reason that positivity is the whole test is not said. | Add "so no term can cancel another".

F35 | comprehension | Theorem 5.13 proof: eq. (4) "(I + A)^(N−1) = Σ C(N−1,k) A^k" | "The matrices I and A commute, so the binomial theorem gives" assumes the binomial theorem for matrices is known and does not say why commuting matters. The binomial coefficient notation is not explained. | Add "the binomial theorem holds for matrices that commute, and I commutes with everything. C(n,k) counts the ways to choose k items from n."

F36 | comprehension | Theorem 5.13 lead-in: "That this test is equivalent to the sum test is shown here, and no source read states both together." and the plain-words "Put a one in every cell where the row island and the column island are the same." | The plain-words paragraph describes I + A in an odd way ("put a one in every cell where the row and column island are the same" then "multiply this new table by itself"). It does not say that the new table is A with ones added on the diagonal. | Say "the table A with ones added on the diagonal."

F37 | comprehension | Sec. 5.3, first bullet: "The diagonal of B is ignored. A connected graph can have zeros on the diagonal of B: for N = 2 and one edge, B = A = ..." | Why the diagonal of B is ignored is never said. The Section 5.2 plain-words text says "look only at cells where the row island and the column island are different" with no reason. | Explain that B_ii counts closed walks, which exist only if i has a neighbor. An isolated vertex in a one-vertex graph or a one-edge graph can give 0 without breaking connectivity.

F38 | comprehension | Example 5.15: "The matrices B and T are block diagonal along the two components {n1, n2} and {n3} ... in general it follows from lemma 5.11." | "Block diagonal" is not defined, and "follows from lemma 5.11" is unexplained. | Say "all non-zero entries lie in the n1,n2 block and the n3 block" and give the one-line reason (no walk crosses components).

F39 | comprehension | Example 5.15: "Note (A²)33 = 0: the isolated vertex has degree 0 (proposition 4.4)." | The remark has no stated purpose in the argument. | Remove or say why it is shown.

F40 | comprehension | 5.5: "As an estimate by counting, not a measurement, it takes about N² operations on an adjacency matrix, against N − 2 matrix products of about N³ multiplications each" | "BFS" operations count and the claim "N−2 matrix products" are asserted with no derivation. The 5.5 text says the BFS lemma is "cited and not proved here". Note also that the abstract and Section 1.4 promised that "all statements are proved in full". | Qualify the abstract ("except the BFS comparison, which is cited") and give a one-line derivation of the counts.

F41 | comprehension | 6.1: "of which 1, 1, 4, 38, 728, and 26704 are connected; the three tests agreed on all of them." | The sequence of counts is unexplained and gives no insight for a first-time reader. It is a data dump. | Say what the check shows in one sentence and move the counts to the appendix.

F42 | comprehension | 6.4: "Two sources also contain sentences that are wrong when path is read as a walk with no repeated vertex." (three bullets listed, with "(B11 = 1 would not refute it when length 0 is allowed.)") | Section 6.4 is a critique of cited papers, but the purpose is not stated up front. The length-0 argument for B22 is hard to follow ("at most one path of length less than 3 joins n2 to itself, the path (n2) of length 0 if length 0 is allowed and none if it is not"). The sentence "nothing else in the note depends on them" sits in the intro of the section. | Open with "This section is optional. It explains why some statements in published sources can mislead." Simplify the B22 argument to "B22 = 2, but there is at most one path from n2 to itself."

F43 | comprehension | 6.5 and Conclusion (Q2) | The conclusion says "The proof uses walk counting, the fact that a walk contains a path no longer than itself (lemma 3.30), and the fact that a path has length at most N − 1", yet the headline of Q2 is that G is connected if every off-diagonal entry is positive. The reader is not told why N−1 is the right cutoff in a single sentence. | Add "A path visits each vertex at most once, so it has at most N−1 hops."

F44 | comprehension | Whole paper, structure | The paper is long (21 pages). It mixes the answers with reporting on sources, pages read, and handling of ambiguous whiteboard photos. Sections 1.2, 3 (trails, cycles), 6.3, 6.4, and the appendix bear on provenance, not on the three questions. A reader cannot easily tell which parts are needed for Q1 to Q3. | Add a one-paragraph reading guide in 1.5 listing the minimum path through the paper (2.1, 2.2, 3.1 walk and path, 4.1, 5.1, 5.2).

READER SUMMARY
The paper starts from a lecture whiteboard and an assignment. It asks three things about a graph given by its adjacency matrix A. A graph is dots joined by lines, and A is a table of 0s and 1s that says which dots are joined. The three questions are what an entry of a power of A means, how to tell from A whether the graph is connected, and what a path is. For the first, the paper proves that the entry in row i and column j of A^k is the number of walks of exactly k steps from vertex i to vertex j. A walk may revisit vertices and reuse edges, so the entry counts walks and not paths, and it is not just 1 or 0 for reachability. For the second, it proves that the graph is connected if and only if every off-diagonal entry of A + A² + … + A^(N−1) is positive, where N is the number of vertices. Equivalently, no entry of (I + A)^(N−1) is zero. The cutoff N−1 works because any walk can be shortened to a path with no repeated vertices, and such a path has at most N−1 steps. A single power of A is not enough, and a sum stopped too early can wrongly report a connected graph as disconnected. For the third, a path between two vertices is a sequence of pairwise distinct vertices in which consecutive ones are adjacent. This is the course textbook's "simple path", and the textbook's plain "path" is what the note calls a trail. I could write this summary, but I had to dig it out from a lot of material about sources, conventions, and naming that does not bear on the answers.

## Round 2

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

## Round 3

FINDINGS
F1 | comprehension | Abstract: "Here I is the identity matrix." and "(I + A)N−1 has no zero entry" | The abstract uses "identity matrix" and "matrix power" with no gloss. It also uses the symbol N−1 as an exponent before N is tied to the vertex count in the sentence that uses it. "Positive" and "off the diagonal" are never glossed. | Add a clause on first use: "I, the table with ones on the diagonal and zeros elsewhere". Say "N is the number of vertices" next to the formula. Say "off the diagonal means in cells whose row and column are different".

F2 | comprehension | Abstract: "Third, the course's meaning of 'path' is this: a path between ni and nj is a sequence of pairwise distinct vertices…" | The abstract calls this a question answered, but it is a definition. The reader does not know why a "course meaning" differs from an ordinary one. Convention 5 and the "trail" renaming appear only much later. | Add one sentence to the abstract: "The textbook's word 'path' means something weaker, which this note calls a trail."

F3 | comprehension | 1.1: "The board holds a rule for the entries Aij … a drawing of three vertices, a 3 × 3 matrix…" | The "whiteboard" is cited as sources [5, 6] but the reader cannot see it. Its content is described in a dense run-on sentence, and the paper never says which parts matter. | Split the sentence into a short list. Say that only the matrix and the two questions are used later.

F4 | comprehension | 1.2 Convention 3: "a small mark above A that could not be resolved in the photos as a letter k or n" | The reader has no picture and cannot tell why this matters. The sentence "If the mark were a pair of quotation marks around A…" is hard to parse. | Rewrite: "The board's Q1 has an unreadable symbol above A. We assume it is an exponent k." Drop the quotation-mark speculation or move it to section 6.5.

F5 | comprehension | 1.2 Convention 5: "the textbook's own word 'path' means something else, which this note calls a trail" | The reader meets "walk", "trail" and "path" together here, before definitions. The text says "n1 n2 n1 is a walk but not a path" without saying what n1 n2 n1 denotes. | Add a forward pointer to Table 2 with a two-line gloss. Say that n1 n2 n1 means hop from n1 to n2 and back.

F6 | comprehension | 1.2 Convention 6 and 7: "Grinberg's definition…", "[3, Definition 2.9.1(a), p. 36]", "(details in appendix A)" | Citation-heavy provenance claims come before the reader has any mathematics. "Who proves what" is meta-text that blocks the start of the paper. Convention 7 asks the reader to take "as far as a search of its text showed" on faith. | Move conventions 6 and 7 to section 6 or the appendix. Keep a one-line pointer in 1.2.

F7 | comprehension | 1.3 and Table 1: "round trip", "ring trip", "friends", "connectivity component", "fresh-bridge trip" | The frog and pond story adds a second vocabulary. Table 1 lists terms such as degree, distance, and cycle that are not defined until sections 2 and 3. The paper says only some terms are needed, but it does not mark which in the table. | Mark the needed rows in the table, or delete the rows for terms the answers do not use.

F8 | comprehension | 1.5: "the lemma that every walk contains a path (lemma 3.30) with the bound on the length of a path (corollary 3.32)" | The reading guide lists numbered results the reader cannot yet interpret. It never says what the lemma is for. | Add one clause per item, e.g. "this is what lets a walk count stand in for a path".

F9 | comprehension | 2.1 Definition 2.1: "A graph G is an ordered pair (V, E)… each edge is a set uv = {u, v}" | "Ordered pair" and set notation are used without gloss. The notation uv switches between "edge" and a product-like juxtaposition. | Gloss in half a sentence: "a pair (V, E) means the list of vertices and the list of edges". Write "uv denotes the edge {u, v}".

F10 | comprehension | Proposition 2.17 item 4: "∑i,j Aij = 2|E|" and proof "which is the textbook's Theorem 1.2.1 (Euler)" | "|E|" is defined only in the Notation paragraph. The proof's step "every edge has two ends, so it is counted once at each end" is compressed. | Add "|E| is the number of edges" at the statement. Spell out the double counting in one line.

F11 | comprehension | 2.2 Definition 2.18: "(XY)ij = ∑r Xir Yrj … The transpose X^T … the standard rule (XY)^T = Y^T X^T is needed only for proposition 4.4" | The text reaches transpose and a rule the reader must take on faith. The reader has no motivation for the transpose here. | Move the transpose and its rule into the proof of Proposition 4.4. Cite a linear algebra source for the rule.

F12 | comprehension | 2.2 Remark 2.19: "A power is not the entrywise power." | The sentence is cryptic, because no one has proposed an entrywise power. It only becomes clear in Non-example 2.21. | Reword: "Ak means A multiplied by itself k times, not each entry raised to the k." Put it after the non-example.

F13 | comprehension | 3, intro: "the classification of every sequence below was checked by script (appendix A)" | The reader is told scripts were run before seeing any content. For a technician reader this adds noise. The shape of H is described only as a list of edges, so the reader must draw it. | Delete the script remark here, since 6.1 covers it. Add "see the middle drawing of fig. 1".

F14 | comprehension | 3.1 Definition 3.1: "Formally, the textbook defines it as a sequence u0, e1, u1, …, ek, uk … with et = ut−1 ut for 1 ≤ t ≤ k" | The subscripts t, k and the edge-labelling e_t are dense. The reader must decode "in a simple graph the edges are fixed by the vertices" without help. | Drop the formal textbook version from the main text, or add an example with explicit e_t values.

F15 | comprehension | 3.1 Definition 3.21 and Remark 3.22: "A cycle is a closed trail of positive length whose only repeated vertices are its first and last" | The paper itself says cycles are not needed for Q1 to Q3. The definition and the two-triangle example add length and are hard to follow in prose. | Move cycles to an appendix or optional box, or cut the definition.

F16 | comprehension | Definition 3.25: "The distance d(u, v) is the length of a shortest (u, v)-trail … and ∞ otherwise" | The symbol ∞ and the form "(u, v)-trail" are used without explanation. The note then says it will say "shortest path" instead, which is confusing given the textbook's "path" is a trail. | Add "(∞ means no such trail exists)". Pick one word, and avoid "shortest path" until Prop 3.34.

F17 | comprehension | Lemma 3.29 proof: "so s − 1 = t − 1 or s − 1 = t. The first gives s = t and the second gives s = t + 1" | This is a position-index argument that a reader must reconstruct. It is easy to lose track of which vertex equals which. | Add a short sentence that two edges that share an end vertex would force a repeated vertex. Or give a small example, say n1 n2 n1.

F18 | comprehension | Lemma 3.30 proof: "Form W′ = u0 ⋯ us ut+1 ⋯ uk … (if t = k, then W′ = u0 ⋯ us)" and "(Ordinary induction would assume it only for length k − 1…)" | Strong induction is named and explained only in a parenthesis. The deletion step and the claim "its edges are edges of W" are asserted without a worked case until Example 3.31, which comes after the proof. | Put Example 3.31 before the proof. Define "induction" in one line for a reader who has not met it.

F19 | comprehension | Corollary 3.32: "k + 1 ≤ N [3, Section 2.9.4, p. 40]" | The pigeonhole fact is given as a citation without a sentence of reasoning. | Add: "k+1 distinct vertices cannot exceed the N vertices available."

F20 | comprehension | Proposition 3.34 proof: "so Lw ≤ Lt ≤ Lp (the least value over a larger set cannot be larger…)" and "The textbook's d(u, v) is Lt by definition 3.25." | The inequality chain and the sentence that closes the circle are packed together. The proof of L_p ≤ L_w says "the cut … would give a shorter walk" but never states that the cut result is a path. | Write the two inequalities in two labelled steps: Lw ≤ Lt ≤ Lp, then Lp ≤ Lw. Name what is cut.

F21 | comprehension | Table 2 caption and body | Three naming columns plus a number column give 5 columns, and the heading "This note (course)" conflates two things. The reader cannot tell from the table which word to use. | Reduce to "term used here" and "textbook's word". Move the English-source column to a footnote.

F22 | comprehension | Theorem 4.1 text after statement: "All three start their induction at k = 1. The case k = 0 is this note's convention" | The reader is told the literature differs but not why that matters. Source-attribution detail interrupts the statement of the main result. | Move the attribution paragraph after the proof.

F23 | comprehension | Proof of Theorem 4.1: "the walks of length k + 1 … correspond one to one to the walks of length k from ni to nr: delete the final vertex nj to go one way, and append nj to go back" | The bijection is the core step, but it is described in one sentence. The reader may not see why "one to one" gives equal counts. | Add one line: "two sets with a one-to-one pairing have the same size". Show it on A^3_12 in Example 4.2 before the full proof.

F24 | comprehension | Theorem 4.1 post-proof: "For paths the deletion of the final vertex would still give a path, but appending nj may repeat a vertex, and the one to one correspondence breaks" | Dense. Directed graphs and multigraphs are mentioned and named in the same paragraph, with no gloss beyond parentheses. | Split into two sentences. Move the directed/multigraph remark to 6.5.

F25 | comprehension | Example 4.2: "the script also compared the matrix power with a direct enumeration … on all 64 labelled simple graphs on four vertices (labelled: … 64 = 2^6 choices …)" | Computational checking is mixed into a worked example. The "64 = 2^6" explanation is easy to misread because the exponent renders poorly. | Move the whole check to section 6.1.

F26 | comprehension | Example 4.2 explanation of zeros: "each hop alternates between the middle vertex n2 and an end vertex" | The parity argument is stated but not connected to why it is a "fact about this graph only". The reader does not see why this does not generalise. | Say: "this works because the graph is a path with three vertices. A triangle has odd closed walks."

F27 | comprehension | Proposition 4.4: "(Ak)^T = (A^T)^k = A^k" | The step from AT = A and the product rule to the power rule is not shown. The result also relies on the transpose rule introduced much earlier. | Add: "by repeating the rule k times". Or use the walk-reversal argument alone, since it is already given.

F28 | comprehension | 4.4: "if k equals the distance between ni and nj, every walk of length k from ni to nj is a path" | The distance is defined in 3, but a reader skipping to Q1 will not have seen it. The triangle aside in the same paragraph refers to "the board drawing read literally; section 6.2", a forward reference to material the reader cannot yet use. | Split the paragraph into three. Remove the forward reference or give the triangle's edges.

F29 | comprehension | Corollary 4.7 proof and section 4.5 | The corollary is "not needed for Q1 to Q3" per 1.5, but sits in the main flow. Its purpose is unclear until read twice. | Mark it optional in its heading.

F30 | comprehension | 5.1: "A relation ∼ on the vertices says, for each ordered pair u, v, whether u ∼ v holds or not. It is reflexive if…" | Equivalence relations are introduced, then (per the text) "not needed for the tests". The reader cannot say why the subsection exists. | Move 5.1's relation, component and corollary 5.10 material after 5.5, or label it optional at the heading.

F31 | comprehension | Lemma 5.5 proof: "Transitive. If W1 is a walk from u to v and W2 is a walk from v to w, writing W1 and then W2 (with the repeated v written once)…" | The lemma says path, but the proof builds a walk and invokes Lemma 3.30. The lemma statement never says this is what links the two. | Add a lead-in: "joined by a path" and "joined by a walk" are equivalent (Prop 3.33), so work with walks.

F32 | comprehension | Lemma 5.11 / Theorem 5.12 text: "the step from a positive entry to a path is the one that some sources pass over (section 6)" | A claim about other authors' gaps appears mid-argument before the reader knows the argument. It also forward-references section 6. | Delete this clause from the lemma and leave it in 6.4.

F33 | comprehension | Theorem 5.12 proof: "no term can cancel another, and the sum is positive exactly when at least one term is positive" | The key reason is Remark 2.19, which is far back. The reader may not see why cancellation is even a concern. | Add: "all entries are zero or larger, so no minus signs can hide a positive term."

F34 | comprehension | Theorem 5.13 proof: "The binomial theorem (X + Y)^n = ∑ C(n,k) X^k Y^(n−k) holds for matrices that commute" | The binomial theorem for commuting matrices is taken on faith. The reader gets no reason for taking I+A in the first place until the final sentence ("The role of I is…"), which comes after the proof. | Move the "role of I" sentence before the proof. Cite a linear algebra source for the binomial theorem.

F35 | comprehension | 5.3: "The diagonal of B is ignored. A connected graph can have zeros on the diagonal of B" | The bullet text for the first item is spread over several lines and mixes the claim, the N = 2 example and the disconnected example's B33 = 0. The reader has to read it three times. | Split into three short sentences, one per point.

F36 | comprehension | Example 5.14: "T has no zero entry; each entry equals the entry of A0 + 2A + A2, for example T12 = 0 + 2 + 0 = 2 and T22 = 1 + 0 + 2 = 3" | The reader must recompute A0 + 2A + A2 to check. The matrices are not shown for the intermediate step. | Show the three-term sum as one matrix, or give one full entry.

F37 | comprehension | Example 5.15: "the non-zero entries of B and T all lie in the rows and columns of one of them: they form two blocks along the diagonal" | The "block" claim is stated without a picture or visible partition lines. Components are invoked, though the text says earlier the tests do not use them. | Draw the matrix with a visible 2×2 block and 1×1 block, or delete this remark.

F38 | comprehension | Example 5.16: "Suppose a test looked only at AN−1" and Example 5.17 | The 'In plain words' paragraphs and examples are in the wrong order (the plain words before 5.17 describe four islands, but the text says "the script gives" with no matrix shown). | Print A, A2, A3 for the 4-vertex path in 5.17 so the zero and the 1 can be seen.

F39 | comprehension | 5.5: "As an estimate by counting, not a measurement: … about N^4 multiplications in all, against about N^2 for BFS" | The cost argument is brisk. "Operations" and "multiplications" are used interchangeably. The N^4 figure follows from (N−2) products at N^3 each, but "N−2 products" is not justified. The reader is told BFS is "not part of the answer" yet draws a conclusion on cost. | Say that N−2 products give A^2 up to A^(N−1). Either drop the cost conclusion or label it explicitly as outside the scope.

F40 | comprehension | 5.5 BFS paragraph: "Together this suggests the test… This is the note's interpretation of the two sources… the BFS lemma is cited and not proved here." | The reader has to take BFS correctness on faith. The text hedges through three layers (suggests, interpretation, cited not proved). | State plainly: "BFS correctness is assumed, not proved here".

F41 | comprehension | 6.1: "A script compared the sum test, the power test, and a breadth-first search written independently of the matrices on every labelled simple graph with up to six vertices" | The reader must trust the script. No result table is shown in the body, and "labelled" is defined mid-sentence. The 6.1 text also repeats the appendix. | Give the headline counts in one sentence in 6.1, or merge 6.1 into the appendix.

F42 | comprehension | 6.2: "between 1 and 2 (with an arrowhead at 2), between 1 and 3, and between 2 and 3 … reads the arrowhead as a stray mark" | The reader cannot see the board. A major premise (the board graph) rests on the author's reading of a handwritten drawing. The claim that the matrix wins is justified by "the problem statement says that the graph is given through its adjacency matrix", which is from a summary [11]. | Include the figure of the board or a redrawn version. State the assumption as an assumption, with what changes if it is wrong.

F43 | comprehension | 6.4: "Read as paths in the sense of definition 3.13 it is false… at most one path of any length joins n2 to itself" | The section tells the reader that three published sources contain false or misleading sentences. It is flagged optional. "Bai's convention for a cycle was not read, so this holds for the restatement" is hard to parse. | Shorten to one example per source. Rewrite the Bai sentence as "I did not check how Bai defines cycle, so this critique applies only to the quoted sentence."

F44 | comprehension | 6.5 and Appendix A: "The textbook was searched, not read in full" | The central claim in Convention 7, that the textbook has no such theorem, rests on partial reading of an Armenian-language text. The reader must take on faith that the claim is limited. | Put one sentence of this limit next to Convention 7 and in the abstract.

F45 | comprehension | 7 (Q2): "The cutoff N − 1 is the largest length a path can have: a path visits each vertex at most once, so it has at most N −1 edges." | The conclusion is clear but stands apart from the abstract's claim that the tests are "proved in full". The role of Lemma 3.30 versus Cor 3.32 is summarised in one dense sentence. | Add a two-line chain: walk exists, then path exists, then length at most N−1, then a power at most N−1 is positive.

F46 | comprehension | References [5], [6], [11] | Three sources are local files or a summary that the reader cannot access. Claims such as "the course uses 'path' in this sense" rest only on [11]. | Add a clear statement in the introduction that these are not independently checkable, with the quoted wording.

F47 | comprehension | Whole paper, structure | Sections 1 and 2 contain nine conventions, a story dictionary, and notation before the first answer. The first answer appears on page 3, and the main proofs begin on page 10. The reader cannot say early what the paper contributes beyond a restatement of standard results. | Put a two-paragraph worked example (board matrix, A^2, B) right after the questions. Move the conventions to a later section.

READER SUMMARY
The paper starts from a table of zeros and ones (the adjacency matrix A) that records which pairs of points in a graph are joined by a line. It asks three things. The first is what the entries of the powers of A (A multiplied by itself k times) mean. The answer is that entry (i, j) of A^k is the number of walks of length k from point i to point j, where a walk may revisit points and lines. It is not a count of paths, which may not repeat a point. The second is how to tell from A whether the graph is connected, meaning every point can be reached from every other. The answer is to add A, A^2, up to A^(N−1), where N is the number of points. The graph is connected exactly when every cell outside the diagonal is positive. An equivalent test is to raise I + A to the power N−1 and check that no cell is zero. The cutoff N−1 comes from the fact that a path can have at most N−1 lines. The third is what "path" means in the course. The answer is a sequence of distinct points with consecutive ones joined by a line. The textbook's own word "path" means something weaker, which the paper calls a trail. I did not follow why the extra vocabulary was needed (cycles, distance, components, equivalence relations, breadth-first search), or how the whiteboard evidence was weighed.

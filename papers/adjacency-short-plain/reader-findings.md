# Reader findings

The technician reader's findings, as returned, ungraded. They are advisory; severity belongs to the evaluator alone.

## Round 1, 2026-11-12

Reader level 1. No evaluator has read this paper yet.

FINDINGS
F1 | Abstract | "A graph on N vertices is connected if and only if every off-diagonal entry of A + A2 + ... + AN-1 is positive." | "off-diagonal" is never defined in the paper, and "walk"/"path" appear here before Section 2 defines them | Add "(entries (i, j) with i != j)" after "off-diagonal" in the abstract.

F2 | Section 1, para 1 | "The lecture board asks two questions about it, and the assignment adds a third [2, 3, 7]." | The reader does not know what the board, the assignment, or sources [2], [3], [7] are, and the paper does not say which question came from which source | State in one sentence what the board showed and where the third question came from, or say those sources are the author's own notes and are not available to the reader.

F3 | Section 1, Q1 | "The mark above A on the board is read as an exponent k [7]." | The meaning of the board notation rests only on a citation to "Summary of user statements", which the reader cannot see | State the reading in the text ("the superscript k denotes the k-th matrix power") so the claim does not depend on [7].

F4 | Section 1, para 3, and reference [6] | "A full-text search of the course textbook [6] finds neither the walk-counting theorem nor a matrix test for connectivity" | The reader cannot read [6] (noted only in the references as "in Armenian") and cannot check the search, yet many citations depend on it | Say in the text that [6] is in Armenian and that the search result is the author's, or add an English source for the same definitions.

F5 | Section 2, "Matrix powers" | "A = I (the identity matrix) and A k+1 = A k A" | The superscript 0 does not show in the extracted text, so the reader sees "A = I" and must guess A^0 | Write "A^0 = I" explicitly in the sentence. (Could be a pdftotext rendering artifact; the sum limits near "N 0 P" look similarly garbled.)

F6 | Section 2, "Matrix powers" | "Every entry of A is a non-negative integer, since sums and products of non-negative integers are non-negative integers (used in theorem 5.3)." | The sentence says only A, but Theorem 5.3 needs every power A^k | Change to "Every entry of every power A^k is a non-negative integer".

F7 | Section 2, Definition 2.2 | "This paper also allows k = 0 ... the textbook's usage assumes it [6, pp. 23, 49]." | The reader is not told why k = 0 is needed or what it is used for, so the claim must be taken on faith | Add one sentence: k = 0 gives A^0 = I, which is the base case of Theorem 3.1 and the length-0 path in Definition 2.4.

F8 | Section 2, Definition 2.3 | "the textbook's own word "path" means a walk with no repeated edge, and this paper never uses the word in that sense." | Three senses of "path" (course convention, textbook "simple path", textbook "path") are introduced in one place, and the reader cannot keep them apart | Move the textbook-sense remark to a footnote and state only the paper's own meaning of "path".

F9 | Section 2, Definition 2.4 | "the textbook's Definition 2.1.1 [6, p. 48] is the same with the textbook's own "path"" | Given F8, the reader cannot tell whether "the same" means the same notion of connectedness, since the textbook's path is a different object | Either explain why the textbook's connectedness coincides with this paper's, or drop the claim.

F10 | Section 2, "Board graph" | "The board's drawing shows a third line that the matrix does not encode; the matrix defines the example." | The reader does not know what the third line is or why it is mentioned | Either name its endpoints and say it is excluded, or delete the sentence and state only that the matrix defines the example.

F11 | Section 2, Definition 2.1 | "the board states the same rule in other letters [2, 3]" | "other letters" is unclear (symbols? a different notation?) | Replace with "the board states the same rule with different symbols".

F12 | Section 3, "Warning" paragraph | "Also (A4)22 = 4 by script, so the entry is not "1 if nj can be reached from ni"." | "by script" refers to a scripts/ folder not introduced until Section 6, and the value is given with no walks; the "1 if reachable" alternative is never stated as a claim anyone made | Write "(A^4)_22 = 4 (computed; see Section 6)" and, if useful, list the walks.

F13 | Section 3, proof of Theorem 3.1 | "Every walk is counted for exactly one r" (extracted with a spacing gap) and "deleting the final vertex nj gives such a walk, and appending nj to such a walk gives a walk of the kind" | The reader must reconstruct that these two operations are inverse to each other, which is what makes the correspondence one-to-one | Add "these two operations are inverse to each other" after the sentence about deleting and appending.

F14 | Section 4, Definition 4.1 | "This is definition 2.3 with the ends fixed, the textbook's Definition 1.2.13 with ends ni and nj" | The reader asks why path is defined twice and why Q3 is a separate question, since Definition 2.3 already gives a path | Fold the ends-fixed form into Definition 2.3, or add one sentence saying why Q3 needs the form with fixed endpoints.

F15 | Section 4, last sentence | "In the board graph n1 n2 n3 is the only path from n1 to n3." | Stated with no reason | Add a short justification, e.g. "the only other route would revisit a vertex", or say it was checked by enumeration.

F16 | Section 5, opening paragraph | "Both are stated in Grinberg [1, ...] and the first is the textbook's Lemma 1.2.1 for u != v without a length bound [6, p. 23]" | "Both" and "the first" have no referent; the two facts are not named until Lemmas 5.1 and 5.2, and reference [1] is first cited here | Name the two facts in the sentence (Lemma 5.1, every walk contains a path; Lemma 5.2, reachability from powers) before citing sources for them.

F17 | Section 5, proof of Lemma 5.1 | "By the hypothesis W', and so W, yields a path from u to v of length at most k - (t - s) <= k." | The sentence is hard to parse on first reading, and the step that the induction hypothesis applied to W' gives the path is unstated | Rewrite as "By the induction hypothesis applied to W' (length less than k), there is a path from u to v of length at most k - (t - s), which is at most k."

F18 | Section 5, proof of Lemma 5.1 | "It is a walk, because the only new consecutive pair is us , ut+1 and us = ut is adjacent to ut+1." | The reader must work out that ut is adjacent to ut+1 (from W) and that us = ut, so the new pair is an edge | Add "since ut is adjacent to ut+1 in W and us = ut".

F19 | Theorem 5.3 | "Let N >= 2 (for N = 1 the graph is connected)" | No reason is given for the N = 1 case | Add "(Definition 2.4 asks about pairs of distinct vertices, and there are none)".

F20 | Section 6, opening | "All matrices and walk lists below were computed by the scripts in the scripts/ folder, which also holds their outputs." | The scripts folder is not part of the PDF, so the reader cannot check any figure or the path-graph example | State the script file name and that it is outside this document, or note that the small matrices can be checked by hand.

F21 | Section 6, "Limits" | "on the path graph with edges n1 n2 , n2 n3 , n3 n4 (N = 4) the script gives (A1)14 = (A2)14 = 0 and (A3)14 = 1" | This graph is introduced only here, and the values rest on a script with no walk shown | Give the walk n1 n2 n3 n4 for the length-3 entry and note that no walk of length 1 or 2 joins n1 and n4.

F22 | Section 1, "The answers come in the order Q1, Q3, Q2" | The reader is told the order is chosen for dependency but is not told which definitions are needed for which answer until Section 5 | Low priority: add a short pointer, e.g. "Q2 uses the path of Q3 (Section 4)".

READER SUMMARY
The paper asks three questions about a finite simple undirected graph and its adjacency matrix A. It answers that (Q1) the entry (A^k)_ij counts walks of length k from n_i to n_j, with repeated vertices allowed, so it is not a path count; (Q3) a path between two vertices is a walk with no repeated vertex; and (Q2) the graph is connected exactly when every off-diagonal entry of A + A^2 + ... + A^(N-1) is positive. Each claim is given a proof (walk counting by induction on k, every walk contains a path, and reachability from the powers), and the connectivity test is run on a 3-vertex board graph (connected) and a 3-vertex graph with an isolated vertex (disconnected), plus a remark that the sum must run to A^(N-1) and a note that the test reads only whether entries are zero. I could write this paragraph, but only after resolving three points that the paper leaves open: what the "board", "assignment", and sources [2], [3], [7] contained; what the "third line" in the board drawing was; and which of several senses of "path" the connectivity statement relies on. Several numerical claims (A^4_22 = 4, the path-graph entries) rest on a script whose output the reader cannot see.

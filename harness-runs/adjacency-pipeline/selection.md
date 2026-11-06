# Selection: adjacency-pipeline

Selector: paper-evaluator (level 3), fresh, given only select/ (task.md,
source/ with the two whiteboard photos and the course textbook, and
candidates/cand-a to cand-d, the four final papers after their revision
rounds). Mission: the Selector section of references/missions.md.

Unblinded with pool-map.json: cand-a = composed, cand-b = base,
cand-c = inv, cand-d = dom.

Choice: cand-a (composed). Runner-up: cand-d (dom).

## Selector reply, verbatim

I read all four candidates in full. I checked the textbook pages as rendered images: printed pp. 9, 11, 16, 21 (including a zoomed crop of Fig. 1.2.5), 22, 23, 48 and 49, which are PDF pp. 10, 12, 17, 22, 23, 24, 49 and 50. I also viewed whiteboard-1.jpg. I recomputed the following by script:
- the matrices and powers for the board graph, the triangle and the disconnected graph;
- cand-c's Table 3 (walk, trail and path counts on the five-vertex graph): 1/1/1, 1/1/1, 8/3/3, 16/7/3, 72/6/0, 192/6/0, 704/16/0, 2112/0/0, all correct;
- cand-a's appendix walk totals 2052, 72664 and 743680, all correct;
- the counts of connected labelled graphs (1, 1, 4, 38, 728, 26704) and cand-d's 5525 = 5·1105, both correct.

**What the textbook says, as checked on the page images**
- **p. 9:** V is a finite nonempty set, E ⊆ V^(2), and Def 1.1.1 calls (V,E) a graph.
- **p. 11:** Def 1.1.4 (adjacent). A(G) is defined after Def 1.1.6, with a_ii = 0 and a_ij = a_ji.
- **p. 16:** Def 1.2.1 (degree, d_G(v)) and Theorem 1.2.1 (Euler).
- **p. 21:** Fig. 1.2.5. Its edges are v1v2, v1v3, v1v5, v2v3, v2v4, v3v4, v3v5, v4v5, exactly as cand-c lists them.
- **p. 22:** Def 1.2.11 to 1.2.16. Def 1.2.14 is the "closed path or cycle", meaning a closed trail. Def 1.2.15 is the simple cycle. Cn has n ≥ 3. Def 1.2.16 defines distance by the shortest textbook "path", which is a trail. The example sequences all four candidates quote are on this page.
- **p. 23:** The three properties of distance, and Lemma 1.2.1 (for u ≠ v, by induction).
- **p. 48:** Def 2.1.1, and Fig. 2.1.1 (a cycle, a grid, a tree).
- **p. 49:** The equivalence relation, the components, Remark 2.1.1, and Fig. 2.1.2 with four components.

**1. DELIVERY**
- **cand-a:** Answers Q1 (Thm 4.1, all k ≥ 0), Q2 (Thm 5.12 and 5.13) and Q3 (Def 3.17), with conclusion lines 985–1002. It has the connected and disconnected examples (Ex 5.14, 5.15), BFS (§5.5), the mismatch (§6.2), and a full naming table (Table 2, lines 404–423) whose English column is complete. Every definition has a remark, an example and a non-example, and the plain-words layer is complete.
- **cand-b:** Q1 to Q3 are answered (Thm 5.1 for k ≥ 1, Thm 6.10, Def 3.35). However, Table 2 (lines 528–546) leaves the English column as "–" for closed walk, cycle and simple cycle ("we did not check"). That is a gap in the deliverable "three naming conventions in one table". Lemma 6.9 and Thm 6.10 share one plain-words paragraph.
- **cand-c:** Everything is present. Def 2.1 (line 192) carries no textbook number (1.1.1), although the brief asks for the numbers to be cited. Table 2 (line 355) covers only walk, trail and path, with no cycle row.
- **cand-d:** Everything is present, and Table 2 is complete (line 408).

**2. CONFORMANCE**
- **cand-a:** Stays in scope. Directed graphs and multigraphs get one sentence (line 549). The BFS cost remark is a few sentences (lines 881–886). Textbook v_i is mentioned once (line 163), as the brief requires.
- **cand-b:** In scope. It adds component and distance corollaries (6.13 and 6.14), which are allowed.
- **cand-c:** Adds a digression on Euler trails (lines 629–633) and a two-sentence remark on directed graphs (lines 881–883).
- **cand-d:** Uses the textbook's v-labelled sequences about ten times (Non-ex 2.25, Ex 2.32, 2.33, 2.36, 2.37, 2.40, Lemma 3.3). This goes against the brief's "v_i is mentioned once" and gives a first-time reader two vertex notations at once.

**3. FIDELITY**
All four are accurate against the textbook pages listed above.
- **cand-a:** Faithful on Def 1.2.14 and 1.2.15, on distance by trails (Def 3.25), on Lemma 1.2.1, and on Remark 2.1.1 and both figures.
- **cand-b:** Def 3.1 matches p. 9 ("finite nonempty"). Def 3.43 changes distance to "least walk length" while labelling it textbook Def 1.2.16; it does disclose this. The word "trail" rests on Wikipedia "read through a summarising tool" (lines 544–546, 1245).
- **cand-c:** Accurate about Fig. 1.2.5 and its examples. Def 2.21 defines distance by course paths under the 1.2.16 label, with a disclosure. It says no source states the (I+A)^{N-1} form with a proof, which is hedged as "that we read".
- **cand-d:** Accurate, and gives distance by trails as the textbook does.

The source does not settle which meaning of "cycle" the course uses. cand-a and cand-d use the simple cycle; cand-b and cand-c use the textbook's closed trail. All four flag their choice, so this is neutral.

**4. INTERNAL CONSISTENCY**
- **cand-a:** One slip. §1.5 (line 155) says "the power test … not needed for (Q1) to (Q3)", while the Q2 answer includes that test.
- **cand-b:** Convention 2.5 (line 208) says "Plain 'path' always means no repeated vertex". But Def 6.1 (line 889) then uses plain "path" to mean a trail. Remark 4.1 cites "Definition 6.1" as the textbook's definition, which mixes the note's own numbering with the book's.
- **cand-c:** Ex 5.9 (line 757) says "Walks of exactly length 2 cannot use the single edge n1n2". As written this contradicts its own example of the walk n1,n2,n1. The list of uses for Convention 6 (line 139) is incomplete.
- **cand-d:** The answer labels "(A1)", "(A2)" and "(A3)" (lines 56–61) clash with the matrix powers A^1 and A^2, which appear as "(A1)14" in Remark 5.5.

**5. OPERATIONAL FITNESS**
All four are followable, and every proof is written out step by step.
- **cand-a:** The frog and island story is consistent, and there is a reading guide (§1.5).
- **cand-b:** At 23 pages it is the longest.
- **cand-d:** The mixed n/v notation and the A1/A2 labels add friction for a first-time reader. It also hedges Q3 oddly as "best taken as the third question this note has chosen to answer" (line 45), although the brief says the user's assignment asked it.

**6. FINISH**
None has placeholders or broken references. All leak a little of how they were produced:
- cand-a: "prefix m3 … only a label".
- cand-b: "a later independent review of those page images" (line 1235), plus module-named scripts.
- cand-c: m3 script names.
- cand-d: "modules/m3_check.py".

<why>
The pick came down to conformance and internal consistency among papers that all deliver and are all faithful to the textbook. cand-a meets every objective, has a complete three-column naming table, mentions v_i once as the brief requires, and its numbers are verified. Its only flaw is a one-line slip in the reading guide. The runner-up is cand-d. It is equally correct, but it reuses the textbook's v-labelled vertices throughout, against the brief, and its answer labels A1/A2 clash with the matrix powers. cand-b lost on its "path" meaning a trail in Def 6.1 and the unchecked cells in Table 2. cand-c lost on its partial naming table and the missing number on Def 1.1.1.
</why>

```choice
cand-a
```

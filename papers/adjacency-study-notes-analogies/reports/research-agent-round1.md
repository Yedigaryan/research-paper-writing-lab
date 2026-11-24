I corrected C20, C12, C5 and one more quote, C15, in `papers/adjacency-study-notes/evidence/evidence.base.json`. I changed nothing else (no claim text, status or id), and the check passes with errors 0 and warnings 0. The merged file has 11 sources and 50 claims, because `merge_evidence.py` added 2 sources and 16 claims from module fragments.

**Changed claims**
- **C20** (Gotti):
  - Old: locator "Proposition 2 and the sentence before it, p. 1"; quote "As we proceed to show, adjacency matrices can be used to compute number of walks in a graph."
  - New: locator "Proposition 2, p. 1"; quote "Let G be a graph (directed or undirected) on [n] with adjacency matrix A. For any j, k ∈ [n] and ℓ ∈ N, there are Aℓjk walks of length ℓ from j to k."
  - Text extraction prints ℓ as a backtick and flattens the superscript, so "Aℓjk" is my plain-text rendering of A^ℓ_jk. I wrote ℓ in place of the backtick. The Gotti source note already says the math is flattened; claims have no note field, so I added nothing there.
- **C12** (Grinberg): the one joined support entry is now two entries.
  - Definition 2.9.1(c), p. 36: "A path (in G) means a walk (in G) whose vertices are distinct."
  - Definition 2.9.1(d), p. 36: "A path from p to q means a path that starts at p and ends at q."
  - Old, for reference: a single entry at "Definition 2.9.1(c),(d), p. 36" that joined the (c) sentence "A path (in G) means a walk (in G) whose vertices are distinct." to the (d) sentence "A path from p to q means a path that starts at p and ends at q." with the text between them dropped and no mark.
- **C5** (Galway): the one joined support entry is now two entries, each with its list marker as printed.
  - Note 1, printed p. 3: "1. The adjacency matrix is symmetric (i.e. equal to its transpose) if the graph is undirected."
  - Note 2, printed p. 3: "2. The adjacency matrix has zeros on its main diagonal (unless the graph has loops)."
  - Old: one entry at "Notes 1 and 2 on the adjacency matrix, printed p. 3" with the two sentences run together and the "1." and "2." markers dropped without a mark.
- **C15** (textbook distance property): the second support entry dropped the list marker "1." at its start. The quote now begins with "1. " before the Armenian text; the locator "distance property 1, printed p. 23" is unchanged. I made this correction on my own initiative after re-checking the sources for the same faults, and it is not on your list.

I re-read every other quote against the source files (textbook page images, Galway, Gotti, Grinberg, Bai, Paramadevan) and found no other lead-in sentence standing in for a statement, and no sentences joined without a mark.

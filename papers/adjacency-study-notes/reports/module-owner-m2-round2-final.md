I corrected claim M2-6 in `papers/adjacency-study-notes/evidence/modules/m2.json`. The two Galway entries match base claim C5 exactly, and I added the script-output entry. The claim's statement, id, status and every other claim are unchanged. I did not run the merge or the check, and I did not edit `evidence.base.json`, `evidence.json` or `modules/m2.md`. The report `modules/m2.md` does not repeat the joined Galway quote; `grep "equal to its transpose"` finds nothing there.

The support of M2-6 is now these three entries:

1. source `galway_adjacency_notes`, locator "Note 1 on the adjacency matrix, printed p. 3", quote "1. The adjacency matrix is symmetric (i.e. equal to its transpose) if the graph is undirected."
2. source `galway_adjacency_notes`, locator "Note 2 on the adjacency matrix, printed p. 3", quote "2. The adjacency matrix has zeros on its main diagonal (unless the graph has loops)."
3. source `m2_connectivity_script`, locator "scripts/m2_connectivity_test.out, DISCONNECTED GRAPH section, line 55", quote "off-diagonal entries (i, j, S_ij): [(1, 2, 1), (1, 3, 0), (2, 1, 1), (2, 3, 0), (3, 1, 0), (3, 2, 0)]". I confirmed this line verbatim in the saved output.

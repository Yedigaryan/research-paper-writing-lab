The evaluator was right: the source's slide footer names two authors, so I corrected the record in `papers/adjacency-study-notes/evidence/modules/m2.json`.

**Footer.** The title-slide footer, in the text I extracted and again on the rendered slide, reads "Robert Sedgewick and Kevin Wayne • Copyright © 2006 • http://www.Princeton.EDU/~cos226". The footer is on slide 2, not on slide 24 where the running-time quote comes from. The PDF metadata names only Kevin Wayne, and that is where I took the author from before.

**Source `wayne_cos226_undirected`** (id unchanged, no claim changed)

| Field | Old | New |
|---|---|---|
| `authors` | ["Kevin Wayne"] | ["Robert Sedgewick", "Kevin Wayne"] |
| `year` | 2006 | 2006 (unchanged; the footer confirms it) |

I also rewrote the `notes` field to cite the footer instead of the PDF metadata.

**Rebuild and check** (copy, merge, then check, run from the repository root as instructed):
- Merge: "+2 sources, +16 claims; total 11 sources, 50 claims".
- Check: "sources 11; claims unverified 0, supported 47, qualified 3, removed 0; errors 0; warnings 0".

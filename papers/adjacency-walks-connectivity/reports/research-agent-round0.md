I wrote `evidence/evidence.base.json` and copied it to `evidence/evidence.json`. `check_claims.py` reports 0 errors and 6 warnings.

**Counts.** There are 10 sources and 34 claims. Of the claims, 27 are supported, 5 qualified and 2 unverified.

**Sources.**
- **Course textbook** (Petrosyan, Mkrtchyan, Kamalyan, 2015): I viewed printed pp. 11, 16, 21–23, 48 and 49 as images. Armenian quotes are transcribed from those images.
- **Whiteboard photos:** both viewed.
- **Galway notes, Gotti (MIT 18.211), Bai (BIMSA), Paramadevan:** read in full.
- **Grinberg (arXiv v3):** only Section 2.9, pp. 36–42.
- **Waterloo CS 341 slides:** the Module 3 deck (BFS), not the "Lecture 10" file named in `graph-sources.md`. Slide 11 is the BFS correctness summary.
- **Lehman–Leighton–Meyer (LibreTexts copy):** metadata only, never opened, supports nothing.

**Warnings.**
- **C4, C7:** unverified. Both are derived claims (row sums equal degrees; the (A^2)_ii counterexample) whose proofs are not yet in `appendices/derivations.tex`.
- **C8, C19, C29:** each has a support entry with no quote. Two are the textbook-absence and length-0 claims; the third is the board claim, whose handwritten drawing has no quotable text. All three are marked qualified.

**Contradictions recorded (7).**
- **Paramadevan Theorem 1:** it says the entry of A^l counts paths, but Galway, Gotti and Bai say walks. The same paper's property 7 (p. 16) also says walks.
- **Paramadevan Theorem 2 proof:** it sums path counts without the walk-to-path step.
- **Bai's proof-sketch sentence:** it says "paths", but Gotti's proof of the same test works through walks.
- **Textbook "path":** this is the English trail; "simple path" is the course path.
- **Textbook Lemma 1.2.1:** it excludes u = v and gives no length bound; Grinberg's Corollary 2.9.7 covers both.
- **Board drawing:** it shows three edges but the matrix encodes two; the matrix is taken as the example.

**Discrepancies and limits.**
- `graph-sources.md` says Grinberg is multidigraph-general. In v3, Definition 2.9.1 is for simple graphs, so I cited it that way.
- The Galway notes have no author or date; I recorded them that way.
- No sum-form test (A + … + A^(N−1)) comes from a source other than Paramadevan's statement; the paper must prove it. That claim is qualified.
- The textbook-absence claim rests on my text-layer search, which returned the same pages as `graph-sources.md`. I viewed only p. 11 of those.

**Thin modules.** m1 is adequately covered by 3 independent sources for walk counting, but its row-sum and counterexample claims are unverified. m3 has no independent proof of the sum form and only slide-level support for BFS. m2 rests on the textbook plus Grinberg alone.

File: `/home/user/research-paper-writing-lab/papers/adjacency-walks-connectivity/evidence/evidence.base.json`

Both passages are confirmed and recorded. One page number differs from the evaluator's report.

I re-fetched the PDF (HTTP 200) and read the text layer. I did not view page images, so the page assignments rest on the page numbers printed at the foot of each page.

- **M3-11 (new, qualified):** Theorem 3 on p. 17 says the distance between two vertices is the smallest l with a nonzero entry of (A^l)_{ij}, for a connected graph. The claim carries the theorem's exact quote and a quote from its proof. The result is correct, but the proof reads a nonzero entry as a path and never applies the walk-to-path lemma. It is qualified for that reason.
- **M3-12 (new, qualified):** Section 2.2 ("Properties of Adjacency matrix"), item 7, says the entry of A^m counts walks of length m, and that the least nonzero m is the distance. This item is on p. 16, not p. 15. It is stated without proof and is correct as a walk count, unlike their Theorem 1.
- **M3-6 (extended):** I added the Theorem 3 quote as a second support entry and noted that the module's proof via Lemma 3.2 does not depend on theirs.

In `modules/m3.md`, Remark 3.7 now says the distance result is not new to this paper. It cites Theorem 3 (p. 17) and item 7 (p. 16) and keeps the Lemma 3.2 proof as the module's own. The Section 4 evidence table row was updated to match.

For the author, the paper's Remark 5.12 should cite "Paramadevan and Sotheeswaran, Theorem 3, p. 17, and Section 2.2 item 7, p. 16" for the statement. It should keep the proof via Lemma 3.2 as the paper's own, because theirs is incomplete. I did not touch `evidence.base.json` or `evidence.json`.

Files are in `/home/user/research-paper-writing-lab/papers/adjacency-walks-connectivity/`:
- `evidence/modules/m3.json`
- `modules/m3.md`

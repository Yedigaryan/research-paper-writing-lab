Module m1 is written. A trial merge of the fragment into a scratch copy of `evidence.json` gave 0 errors and 6 warnings, none from my claims.

**What it establishes**
- **Properties of A:** A is symmetric with zero diagonal, row sums are degrees, and the entries sum to 2|E|.
- **Walk counting:** (A^k)_ij counts walks of length k, with a full induction proof (base case k = 1, step grouped by last-but-one vertex). Walk length 0 is allowed as the paper's own convention, so A^0 = I.
- **Walks, not paths:** (A^2)_ii equals the degree of n_i. On the board graph the diagonal of A^2 is 1, 2, 1, and no path of length 2 returns to its start. Off the diagonal, (A^3)_12 = 2, but both walks are neither paths nor trails.
- **Script checks:** every product is computed by `modules/m1-calc/m1_check.py`, with output in `modules/m1-calc/m1_check.out`. A brute-force comparison of 24255 entries against enumerated walks found no failures.

**Claims and files**
- **New claims:** M1-1 to M1-6 are in `/home/user/research-paper-writing-lab/papers/adjacency-walks-connectivity/evidence/modules/m1.json`, with no new sources. The report is `/home/user/research-paper-writing-lab/papers/adjacency-walks-connectivity/modules/m1.md`.
- **C4 and C7:** M1-1 and M1-2 are their derived, supported replacements, with full derivations and script checks. The base file still marks C4 and C7 unverified, so you need to mark them superseded in `evidence.base.json`, or have the paper cite M1-1 and M1-2.
- **Qualified:** M1-5 (walk of length 0 allowed) is qualified because it is the paper's own convention, and the textbook is silent on it. The existing C8 stays qualified because it rests on a text search, not a proof of absence.

**For you to reconcile**
- **m2:** it must use the same length-0 convention (allowed) and the same meaning of "path" (no repeated vertex). I could not see m2 or m3.
- **m3:** it can cite M1-3 and M1-6, and the (A^2)_12 = 0 example showing that one power is not a test.

All five post-release fixes are in, and the build and the four checks pass. I did not commit or push.

- **E2-F6:** the blank band under the Figure 1 subfigures is gone. I made the three label nodes rectangles with no padding, so they no longer widen the figure. I checked page 2 as a rendered image and saw no gap between the labels and the caption.
- **E3-F1:** Remark 2.4 now says "If n_i and n_j are adjacent, n_j is called a neighbour of n_i." I checked every later use against it, and none needed changing:
  - `background.tex`, the degree remark;
  - `counting.tex`, the closed walks, the Proposition 4.6 statement and its proof;
  - `paths.tex`, Lemma 3.2;
  - `connectivity.tex`, "n_3 has no neighbour".
- **E3-F2:** "loop" is replaced by "the part of the trip between the two visits".
- **E3-F3:** the text now reads "so the proofs of (b) to (d) are ours". The sentence just before it already says Paramadevan and Sotheeswaran state (d), so I did not repeat it.
- **E3-F4:** Definition 2.1 now cites page 9 of the textbook. I checked it on the page image: PDF page 10 carries the printed number 9 at the foot, and Definition 1.1.1 introduces G = (V, E) there.

The checks:
- `build.sh` is ok at 20 pages.
- `check_citations.py` reports 0 errors and 0 warnings.
- `check_claims.py` reports 0 errors and the single C9 warning, which has no quote, as before.
- `inspect_pdf.py` reports 0 errors and 0 warnings.
- `check_plain_words.py` reports 0 errors and 0 warnings.

`self-evaluation.md` has the "Revision log, post-release fixes" appended. The files I changed are `sections/introduction.tex`, `sections/background.tex`, `sections/paths.tex` and `sections/counting.tex` in `/home/user/research-paper-writing-lab/papers/adjacency-walks-connectivity/`.

Round 1 revision of `papers/adjacency-walks-public/` is done. The paper is 5 pages against a budget of 5, and all four checks pass.

**Checks**
- `build.sh`: exit 0.
- `check_citations.py`: 0 errors, 0 warnings.
- `check_claims.py`: 0 errors, 0 warnings.
- `inspect_pdf.py`: 5 pages, 0 errors, 0 warnings.
- The hyperref "Token not allowed in a PDF string" warning is gone from the build log.
- The forbidden-word grep (board, lecture, course, assignment, textbook, user, script, Petrosyan, own convention, n_1) over the `.tex` files finds nothing.

**Files changed**
- `main.tex`: the abstract now says what a walk is.
- `sections/introduction.tex`, `definitions.tex`, `counting.tex`, `connectivity.tex`, `example.tex`.
- `evidence/evidence.base.json`: `used_in` fields only.
- `evidence/modules/author.json`: `used_in` fixed on p1 to p5, and new claim p6.
- `evidence/evidence.json`: rebuilt by the merge script, not edited by hand.
- `self-evaluation.md`: the per-finding log is appended below the section-by-section body.

**Evaluator findings**
- **F1:** the simple-graph definition now cites Grinberg Definition 2.1.1, p. 9. Claim p6 carries the evaluator's quote exactly as reported. `self-evaluation.md` says the quote comes from the evaluator's fetch, not from my own reading of Grinberg, so the next evaluator should fetch it again.
- **F2:** I cut the clause about another paper's proof.
- **F3:** I cut the sentence on (A^2)_22 and (A^2)_12.
- **F4:** the parenthetical in the Limits paragraph now reads "(A^3)_12 = 2, yet the only path from v_1 to v_2 has length 1".
- **F5:** I cut the clause about sources sketching or omitting steps.
- **F6:** I cut the Bai and Paramadevan comparison sentence. "Cycles" no longer appears.
- **F7:** the first use now reads "the number |C_r| of walks in C_r".
- **F8:** shortened to the wording you suggested.
- **F9:** now "The sources prove this starting from k=1".
- **F10:** now "(a) and (b)".
- **F11:** a4's `used_in` is emptied and the cited claims now carry `used_in` values. Both are fixed in the base file and the author fragment.
- **F12:** both section titles use `\texorpdfstring`. I used plain "Ak" as the PDF string, because a superscript there still warned.

**Reader findings**
- **Changed:** F1 (abstract gloss), F2, F3 (moot after the Bai cut), F5, F6, F7, F8, F9, F10, F11, F12 (one line with the binomial expansion), F13, F14, F15, F16.
- **Partly met:**
  - F4: the paper now says the two definitions agree by Proposition 2.9.10, but does not restate Grinberg's definition, which needs components.
  - F5: the walk class is renamed C_r, but the u/w/v/w_t vertex naming stays, since the proof introduces w_t.
- **Left as is:** F1's "adjacency matrix" is not glossed in the abstract.

**Could not justify:** nothing. The sentence on the (I+A)^{N-1} expansion in Section 4 rests on the derived claim m3-7, not on a new citation.

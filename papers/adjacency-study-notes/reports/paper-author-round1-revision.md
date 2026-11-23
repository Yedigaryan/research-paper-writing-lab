Round 1 revision is done: 6 pages against the budget of 6. Two evaluator corrections (F5, F8, F11 in part) could not be done as written without a new claim or source, so I stopped short on those parts; details below. All checks pass.

**Checks**
- `build.sh` succeeded.
- `check_citations.py`: 0 errors, 0 warnings.
- `check_claims.py`: 47 supported, 3 qualified, 0 unverified; 0 errors, 0 warnings.
- `inspect_pdf.py`: 6 pages, 0 errors, 0 warnings.

**Evaluator findings F3 to F14**
- **F3** (`connectivity.tex`): the remark after Theorem 4.3 now reads "Paramadevan and Sotheeswaran state this test [8, Theorem 2, p. 17]; the proof below is this paper's own."
- **F4** (`limits.tex`): the first sentence is shortened to "The entries of S count walks, not paths (Example 3.2), so only their positivity is used."
- **F5** (`definitions.tex`): the Grinberg clause and "(a derived remark)" are cut.
  - **Not done as asked:** no evidence claim holds the textbook's p. 21 sentence that writes a walk by its vertex sequence. C7 and m1-2 quote Definition 1.2.10 with its edges only, so I did not cite that locator.
  - The sentence now says the edges are determined by the vertices in a simple graph, still cited to Definition 1.2.10, p. 21.
- **F6** (`limits.tex`, `notes.tex`): `limits.tex` has one sentence on graph search, with no O(E), no E, and no breadth-first sentence. The comparison is marked as an interpretation because the source does not discuss the matrix test. The breadth-first sentence is cut from `notes.tex`.
- **F7** (`limits.tex`): the restated statements use (A^k)_{ij}, k, N and (I+A)^{N-1}, with quote marks only on quoted words. A closing sentence says Bai's n is this paper's N.
- **F8** (`limits.tex`): Bai's "comment after Theorem 1" is now named as a comment, not the theorem.
  - **Not done:** crediting Paramadevan and Sotheeswaran's Section 2.2 item 7. No evidence claim holds that statement; C31 holds only Theorem 3, on distance. Adding one is not allowed this round.
- **F9** (`definitions.tex`): Definition 2.4 now reads "(also called a path from n_i to n_j)".
- **F10** (`examples.tex`): Example 5.2 is retitled "The test on a disconnected graph G_2".
- **F11:**
  - "(Derived here.)" and "The following is derived here." are deleted.
  - "(qualified)" is replaced with plain wording, and the notes now say "the assignment text".
  - Example 3.2 now says "checked against a brute-force count of walks", with the existing citation.
  - `examples.tex` no longer names the script file.
  - **Not done:** the bib entry for the m2 script. The evidence file has no source for it, so I added none. The Notes on sources name the script and say how to rerun it.
- **F12** (`references.bib`): the Wayne entry now lists Sedgewick and Wayne. The Galway entry stays without an author.
- **F13** (`evidence.base.json`, `evidence/modules/m1.json`, `m2.json`): `used_in` is set to the section files that actually use each claim, and the merged `evidence.json` is rebuilt. I rewrote the JSON files, so check the diff for formatting noise.
- **F14** (`walks.tex`): now reads "prove it from k = 1; the case k = 0 is added here".
- **F1, F2:** no sentence of the paper quotes C20, C12 or C5, so nothing needed changing there.

**Reader passages**
- **Changed:**
  - R1: Example 3.2 is retitled "The example graph G_1", and no "board graph" wording remains in the body.
  - R2: "The University of Galway notes" in Section 3.
  - R3: d(u,v) is called the textbook's distance.
  - R4: "Group the walks by their last-but-one vertex".
  - R5: the Lemma 4.1(a) step is written out.
  - R6: Proposition 4.2 is retitled.
  - R7: the case split is written out in the proof of Proposition 4.2.
  - R8: closed with F6.
  - R9: "without defining 'path'".
  - R10: closed with F7.
  - R11: a mapping sentence is added to Remark 2.5.
  - R12: Definition 2.4 points to the Notes on sources.
  - R13: closed with F11.
  - R14, R15: one pointer sentence in the introduction; the retelling stays in the Notes on sources.
  - R17: "has no edge at all".
  - R19: the introduction says the textbook is in Armenian.
  - R20: Section 5 now says what the script computes and checks.
- **Stays, reason in `self-evaluation.md`:**
  - R16 stays because the rows of R are already printed in Remark 4.4, and a matrix display would exceed the page budget.
  - R18 stays because the style rules require a local-file entry to say it was supplied by the user. I did reword the user-statements entry to "a summary of the assignment's conventions, not the assignment text".

`self-evaluation.md` has the per-finding log appended below the per-section part.

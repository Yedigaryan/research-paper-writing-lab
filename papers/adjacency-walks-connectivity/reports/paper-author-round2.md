All round 1 findings are handled except two that I deliberately did not fully act on, and `main.pdf` rebuilds cleanly at 20 pages. `build.sh` reports no overfull boxes and no hyperref warnings. `check_citations.py` reports 0 errors and 0 warnings. `check_claims.py` reports 0 errors, 0 unverified claims and 6 warnings (support entries without a quote in claims owned by the base file or other modules). `inspect_pdf.py` reports 0 errors and 0 warnings. Biber still prints six warnings that `year = {n.d.}` is not an integer, for sources with no date.

I rebuilt `evidence.json` from the updated base, which drops the Lehman source. I added claim A-3 to `evidence/modules/author.json` after fetching the Paramadevan paper myself.

**Not fully done**
- **R1-F5:** I added a one-line preview of the naming to Convention 5 but did not move Table 2 up.
- **R1-F4:** the transliteration "harevanutyan matrits" is given and the note says a reader without Armenian cannot check the textbook citations directly, but the Armenian script is not typeset because pdflatex cannot render it.

**Evaluator findings**
- **E1-F1 (major):** the discussion item is now conditional. The paper never defines "path", and its proof for l = 2 uses "path" for walk. Under that reading, sentence 1 is Theorem 4.1 and its own property 7. Under the standard no-repeated-vertex meaning, it is false. The counterexamples are (A²)₁₁ = 1 and the off-diagonal (A³)₁₂ = 2, which does not depend on length 0. Sentence 2 is qualified the same way. "False as written" and "disagrees with itself" are removed. Sentence 3 stays, since Bai's Theorem 1 already separates walks from paths.
- **E1-F2:** the paper no longer says the textbook is silent on length 0 overall. It now says Definitions 1.2.10 to 1.2.16 do not say, and that p. 23 (d(u,v) = 0 iff u = v) and p. 49 (reflexivity) assume it. This is in Convention 6, Remark 4.2 and the discussion.
- **E1-F3:** a new remark covers reading "any two vertices" as two different vertices when length 0 is not allowed. It includes N = 1, and the discussion points to it.
- **E1-F4:** the connected definition now explains reflexive, symmetric, transitive, equivalence relation, equivalence class and induced subgraph.
- **E1-F5:** the non-example cites Fig. 1.2.5, p. 21, "as the figure shows".
- **E1-F6:** strong induction and the binomial theorem for commuting matrices are explained in a clause, including the binomial coefficient.
- **E1-F7:** the Galway sentence now says the number of such walks equals the degree.
- **E1-F8:** the abstract now says each result is proved here, using the textbook's definitions. "Proposition" is removed from Convention 8.
- **E1-F9:** file paths use `\path{}` with `xurl` added. The walkcount section title uses `\texorpdfstring`. The distance remark and the bibliography titles are shortened.
- **E1-F10:** evidence rebuilt from the base. The Lehman mention is removed from the appendix; it was never in the bib.

**Reader findings**
- **R1-F1:** the abstract now names the course, the whiteboard and what the matrix is. The board mismatch is one clause.
- **R1-F2 and F3:** the board's wording of questions 1 and 2 is quoted, and the reading of the mark as k is marked as an interpretation. Q3 is said to come from the assignment as reported and is treated as the note's chosen question.
- **R1-F6:** cycle is defined once, with the textbook's names in a separate sentence.
- **R1-F7:** Section 2 opens by saying which definitions the later proofs use.
- **R1-F8:** the reflexivity inconsistency is resolved by tying reflexivity to Convention 6, with the F4 explanations.
- **R1-F9:** degree is now written deg and d is kept for distance, with a sentence saying so.
- **R1-F10:** the handshake sum is said to be the textbook's Theorem 1.2.1, taken without proof. Definition 1.2.1 is named as degree.
- **R1-F11:** the Lemma 3.1 step is split into cases q &lt; k and q = k, each with a board-graph example.
- **R1-F12:** the reasons s−1 &lt; t−1 and s−1 &lt; t, and the set equality, are spelled out.
- **R1-F13:** the Theorem 4.1 proof states the one-to-one correspondence explicitly.
- **R1-F14:** 5525 = 5 × 1105 is derived, the N = 4 path powers are in the text with the walk, and the key script output is reproduced in the appendix.
- **R1-F15:** the BFS paragraph gives both directions and the N² bound, and states the purpose.
- **R1-F16:** I added a TikZ figure of the board drawing as read. It sits in Section 6.3 rather than next to Figure 1, because that is where the mismatch is discussed. Convention 4 points to it.
- **R1-F17:** quotations are the sources' own words with symbols typeset, and the heading is softened to "do not hold under the standard meaning of path".
- **R1-F18:** "module owner" and "supplied by the user" are removed from the bibliography. The scripts are described as supplementary verification scripts.
- **R1-F19:** I trimmed the plain-words paragraphs for adjacent and degree only. The study-note standard requires one before every definition.
- **R1-F20:** Theorem 5.3's proof now says what the binomial expansion is for.

`self-evaluation.md` has an updated header and a round 1 per-finding log appended below the per-section body. The body gained notes on A-3 and the new remark. Changes are in `main.tex`, `references.bib`, `appendices/provenance.tex`, `evidence/modules/author.json` and the `sections/` files, all under `/home/user/research-paper-writing-lab/papers/adjacency-walks-connectivity/`.

The final edits after round 3 are done. The paper is 7 pages against the budget of 8, and all five checks come out clean. I added no claim, no citation, and changed no numbered statement or proof step. The PDF text shows each of the twelve plain-words paragraphs on the same page as the start of its statement.

**Check lines**
- `build.sh`: ok.
- `check_citations.py`: `cited keys 12; bib entries 12; evidence sources 12; errors 0; warnings 0`
- `check_claims.py`: `sources 12; claims supported 49, unverified 0, removed 0, qualified 3; errors 0; warnings 0`
- `inspect_pdf.py`: `pages 7; errors 0; warnings 0`
- `check_plain_words.py`: `plain-words paragraphs 12; statements checked 9; errors 0; warnings 0`

**Terms list used** (I added `diagonal` and `positive` to the earlier list): `vertex,vertices,edge,edges,adjacent,adjacency,walk,walks,length,path,paths,connected,matrix,matrices,entry,entries,graph,trail,trails,power,powers,sum,test,lemma,theorem,diagonal,positive`

**Updated story dictionary:** the new rows are graph = village, matrix power = chaining the chart with itself once for each step, sum of powers = adding such charts box by box, and sum test = "the adding rule". The old rows are unchanged. A box now holds one for neighbours and zero otherwise.

**Evaluator findings: old to new text**
- **F23** (Theorem 3.1 paragraph in `walks.tex`):
  - Old: "Use the neighbour chart as many times over as you want steps. Then each box counts the strolls with that many steps from one house to another."
  - New: "Chain the neighbour chart with itself, once for each step. Then each box, even a house's box with itself, counts the strolls of that many steps."
  - The one-or-zero convention is now in the introduction story, in the Definition 2.2 paragraph, and as "holds more than zero" and "holds zero" in the Theorem 4.3 and Example 5.1 and 5.2 paragraphs.
- **F24** (Example 3.2 paragraph in `walks.tex`):
  - Old: "Three houses stand in a row, and the middle house has a lane to each end house. Walking from an end house ..."
  - New: "Three houses stand in a row; only the middle house has lanes, one to each end house. Going from an end house to the middle and back takes two steps ..."
- **F25:**
  - The dictionary sentence in the introduction now adds village, chaining, adding box by box, and the adding rule.
  - The Example 5.1 and 5.2 paragraphs say "the adding rule" instead of "the rule".
- **F26** (Definition 2.2 paragraph in `definitions.tex`):
  - Old: "The neighbour chart has one box for every pair of houses. A box says yes ... The chart reads the same from either side, and no house is its own neighbour."
  - New: "The neighbour chart has a row and a column for each house. The box in one house's row and another's column holds one if they are neighbours, and zero otherwise. Swapping the two houses gives the same box, and a house's box with itself holds zero."
- **F27:**
  - `main.tex` loads the `needspace` package and defines `\plainstart` and `\plainend`.
  - `\plainstart` reserves 9 lines and puts a `\bigskip` above the paragraph. `\plainend` blocks a page break and tightens the space below by 4pt, so the space above exceeds the space below.
  - All twelve paragraphs use them. Font, margins and line spacing are untouched.

**Other text changes**
- **Abstract** (`main.tex`): "The first two results are proved in full" is now "The answers to the first two questions are proved in full".
- **Definition 2.4 paragraph:** "Standing still at one house counts as one." is now "Standing still at one house is also a no-return stroll, with no steps."
- **Theorem 4.3 paragraph:**
  - Old: "Add up the neighbour chart used once, twice, and so on, up to one less than the number of houses. ... every box for two different houses is above zero. The boxes for a house with itself are not looked at."
  - New: "Chain the neighbour chart for one step, two steps, and so on. Stop at one less than the number of houses, and add the charts box by box. The village is joined-up exactly when each box for two different houses holds more than zero."
- **Proposition 4.2 paragraph:** the last sentence now ends "..., as shown below."
- **Remark 2.5:** "something weaker" is now "a less restricted notion".
- **Lemma 4.1 attribution:** "Grinberg proves (a) without its last clause" is now "without the clause that the path's vertices occur in the walk".
- **Remark 4.4:** the graphs are now named "G_1 of Example 3.2" and "G_2 of Example 5.2".
- **Introduction, order sentence:** it now ends "so that its definition numbers can be checked".
- **Introduction, story block:** it now has the bold heading "Story and dictionary".
- **Section 6 (Bai):** "Bai's proof sketch (his n is written N here) says that ..." replaces the closing sentence "The notation here is this paper's: Bai's n is N."
- **Notes on sources (Bai):** "Grinberg and Bai define 'path' as this paper does [..] (Bai's proof sketch still uses 'paths' for walks; see Section 6)". This is the F14 fix: the two places no longer read as disagreeing.
- **Notes on sources (textbook search):** the textbook sentence is split into two.
  - Sentence one: "A text search of the whole book for the adjacency-matrix phrase, and a reading of printed pp. 11, 12, 34, 61, found no walk-counting theorem and no matrix test for connectivity in the textbook."
  - Sentence two: "Page 7, a notation list, was not read, so this absence is not certain."

**Reader passages (one line each)**
- F1 changed: added the "Story and dictionary" heading, and the dictionary stays one sentence.
- F2 changed: abstract reworded.
- F3 changed: "is also a no-return stroll, with no steps".
- F4 changed: "a less restricted notion".
- F5 stays: that sentence carries the textbook definition and its citation, kept at the round 1 finding.
- F6 changed: handled with F23.
- F7 changed: the missing clause is named.
- F8 stays: it is a proof step.
- F9 changed in part: box by box, and stop at one less than the number of houses. Notation and names are not allowed in the paragraph, so I did not apply it literally.
- F10 changed: Remark 4.4 names the two graphs.
- F11 stays: names such as G1 and S are not allowed in a plain-words paragraph, and the example itself names them right below.
- F12 stays: it needs a citation at a new place.
- F13 stays: the clause sits inside Definition 2.4, a numbered statement.
- F14 changed: reworded in Section 6 and in the Notes on sources, as above.
- F15 stays: the introduction already points to the Notes on sources for the example graph.
- F16 changed: split into two sentences.
- F17 stays: the local-file rule requires those bibliography entries, and the notes say the sources are not public.
- F18 stays: it is a proof label.
- F19 changed: "as shown below".
- F20 changed: the order sentence now gives its reason.

`self-evaluation.md` in the new folder has a "Final edits after round 3" section with the same content.

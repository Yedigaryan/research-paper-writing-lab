The three plain-words sentences are corrected in `papers/adjacency-study-notes-analogies/`, and nothing else in the paper changed. The paper is still 7 pages, and all checks are clean.

**Old and new text**
1. `sections/walks.tex`, paragraph before Example 3.2:
   - Old: "Three houses stand in a row; only the middle house has lanes, one to each end house."
   - New: "Three houses in a row have two lanes only: the middle house to each end house."
   - My first rewrite ("Three houses stand in a row, with a lane from the middle house to each end house and no other lane.") ran to 21 words, and `check_plain_words.py` warned. The new sentence is shorter, still says the end houses share no lane, and the paragraph keeps three sentences.
2. `sections/definitions.tex`, paragraph before Definition 2.2:
   - Old: "Swapping the two houses gives the same box,"
   - New: "Swapping the two houses gives the same number,"
3. `sections/introduction.tex`, the story:
   - Old: "a neighbour chart has a box for each pair of houses, holding one for neighbours and zero otherwise."
   - New: "a neighbour chart has a row and a column for each house, and the box in one house's row and another's column holds one for neighbours and zero otherwise."
   - This agrees with the Definition 2.2 paragraph, and the story is still four sentences.

**Check lines**
- `build.sh`: ok.
- `check_citations.py`: `cited keys 12; bib entries 12; evidence sources 12; errors 0; warnings 0`
- `check_claims.py`: `sources 12; claims unverified 0, qualified 3, removed 0, supported 49; errors 0; warnings 0`
- `inspect_pdf.py`: `pages 7; errors 0; warnings 0`
- `check_plain_words.py`, run with the same terms list as before: `plain-words paragraphs 12; statements checked 9; errors 0; warnings 0`

`self-evaluation.md` has a short block at the end of the "Final edits after round 3" section recording the three changes.

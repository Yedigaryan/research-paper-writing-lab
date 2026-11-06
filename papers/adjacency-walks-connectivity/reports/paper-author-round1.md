I wrote the full paper, but it has never been compiled. This environment has no `latexmk` or `biber`, so `build.sh` exits 2 and `main.pdf` does not exist. `inspect_pdf.py` therefore could not run either. A script of mine confirms that environments and braces balance and that every reference has a label. The TikZ figure, `cleveref` and the biblatex output are untested.

## What was written
All paths are under `/home/user/research-paper-writing-lab/papers/adjacency-walks-connectivity/`.
- **Paper files:** `main.tex`, `references.bib` and `self-evaluation.md`.
- **Sections:**
  - `sections/introduction.tex`: where the questions came from, seven numbered conventions, the frog-and-islands story with its dictionary, and the answers in brief.
  - `sections/background.tex`: graph, adjacent, adjacency matrix, degree, matrix powers, and their basic properties.
  - `sections/walks.tex`: walk to distance in the textbook's order. Definition 3.5 is the path between n_i and n_j, answering Q3. It also holds the three-convention table and the walk-to-path lemma. The walk/trail/path equivalence is stated once here, and the connectivity section cites it.
  - `sections/counting.tex`: Q1, the walk-counting theorem with its induction proof, the board-graph powers, and the walks-not-paths example.
  - `sections/connectivity.tex`: Q2, components, the sum test and the power test, a connected and a disconnected worked example, failure cases, and breadth-first search (BFS). The BFS paragraph cites m3-1 to m3-4, not C53.
  - `sections/discussion.tex`, `sections/conclusion.tex`.
- **Appendix:** `appendices/derivations.tex` lists the sources read, the pages checked, and how to rerun the scripts.
- **Removed:** the stale `sections/analysis.tex`.
- **Scripts:** I added `scripts/walks_check.py` and `scripts/walk_path_lemmas.py`, a copy of `modules/m2-check.py`, with recorded outputs in `scripts/output-*.txt`. Every matrix in the paper comes from `walks_check.py` or `m3_connectivity.py`.

## Evidence changes
- Added `evidence/modules/author.json` with computed claims a1 to a4.
- Marked C53 as removed in `evidence/evidence.base.json`, because m3-1 to m3-4 supersede it.
- Rebuilt `evidence.json` with `merge_evidence.py`.

## Check results
- **`build.sh`:** exit 2, as above.
- **`check_citations.py`:** 11 keys cited, 11 bib entries, 0 errors, 0 warnings.
- **`check_claims.py`:** 0 errors, 10 warnings, all inherited from the evidence files (supports without a quote for the photos and the user summary, and the unverified m2-14).
- **`check_plain_words.py`:** 34 plain-words paragraphs and 28 statement environments, 0 errors, 0 warnings. I passed it the technical-term list in `self-evaluation.md`.

## Unverified and qualified claims in the text
- **Unverified:** m2-14, the English column of the naming table, which rests on two sources. It is qualified in the table caption and in the discussion.
- **Qualified:** C2, C5, C8, C9, C28, C30, C52, m1-3, m1-4, m1-9, m2-12, m3-4 and m3-13. Each is marked in the text as a reading, a summary, a search result, an interpretation or an estimate.

## Open issues
- **No compile:** build and PDF inspection are pending until TeX Live with `latexmk` and `biber` is available.
- **Board mark:** the mark above A in question 1 stays a reading of k.
- **Course word:** "trail" for the textbook's "path" is my choice, and the paper says so.
- **Bai's "cycle":** I did not read Bai's convention for a cycle. The refutation of his sentence is therefore stated for the restatement in this paper's notation, and says so.
- **BFS test:** "BFS from n_1 visits all vertices iff connected" is my interpretation of two sources. No algorithms textbook was opened.
- **Textbook pages:** I did not view textbook pages myself. The page locators rest on the evidence file and `graph-sources.md`. I did view the whiteboard photo and checked the drawing.
- **Plain words:** the paragraphs pass the mechanical limits (20 words per sentence, no notation, no technical terms), but the read-aloud test has only been applied by me. An independent reader should check it.

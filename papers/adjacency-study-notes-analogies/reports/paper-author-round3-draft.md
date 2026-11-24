The plain-words layer is added in `papers/adjacency-study-notes-analogies/`, and the paper is 7 pages against the budget of 8. The released folder was not touched. The formal text is unchanged: a diff of `sections/` against the released folder shows only added lines, and `main.tex` and `references.bib` are identical to the released ones.

**Story dictionary** (technical term, story word). The story is fixed at the end of the introduction in four sentences, with the dictionary given once in the sentence after it:

| Technical term | Story word |
|---|---|
| vertex | house |
| edge | lane |
| adjacent | neighbours |
| adjacency matrix | neighbour chart |
| entry | box |
| walk | stroll |
| length | steps |
| path | no-return stroll |
| connected | joined-up |

The matrix power A^k is "the chart used that many times over", the sum of powers is "the charts added up", and the sum test is "the rule". The plain-words paragraphs use none of the technical terms, and no notation.

**Layer added:**
- **Twelve paragraphs:** one before each of Definitions 2.1, 2.2, 2.3, 2.4, 2.6, Theorem 3.1, Example 3.2, Lemma 4.1, Proposition 4.2, Theorem 4.3 and Examples 5.1, 5.2. Each has at most three sentences, a `\medskip` before it, and none between it and its statement.
- **Introduction:** one block at the end holds the story, the dictionary, and a sentence saying the paragraphs retell the statements and the formal text stands without them.

**Checks** (run from the repository root on the new folder)
- `build.sh`: `ok: papers/adjacency-study-notes-analogies/main.pdf`
- `check_citations.py`: `cited keys 12; bib entries 12; evidence sources 12; errors 0; warnings 0`
- `check_claims.py`: `sources 12; claims qualified 3, supported 49, unverified 0, removed 0; errors 0; warnings 0`
- `inspect_pdf.py`: `pages 7; errors 0; warnings 0`
- `check_plain_words.py`: `plain-words paragraphs 12; statements checked 9; errors 0; warnings 0`

**Exact `--terms` list used:** `vertex,vertices,edge,edges,adjacent,adjacency,walk,walks,length,path,paths,connected,matrix,matrices,entry,entries,graph,trail,trails,power,powers,sum,test,lemma,theorem`

**Formal-text sentences changed:** none. The abstract and the introduction's outline are untouched; only the new story block was appended to the introduction.

**What the story cannot say exactly:** these are listed in the new section of `self-evaluation.md`, along with the story dictionary and the twelve paragraphs and why each is true of its statement.
- The story gives no numbers, so the exact counts in Theorem 3.1 and Example 3.2 appear only in the formal text.
- "The chart used that many times over" stands for a matrix power, which is a product, not a repetition of a lookup.
- The sum in Theorem 4.3 is only "added up", not entry by entry.
- It does not mention N >= 2 or that the village is finite.

I could not leave anything undone.

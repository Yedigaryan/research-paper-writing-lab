# Planted defects in the fixture paper

The evaluator must raise each of these. A run that misses a critical or
major item is a failed test of the evaluator or the rubric.

## Caught by the scripts

| Script | Expected error |
|---|---|
| `check_citations.py` | cited key `page1999pagerank` not in `references.bib` and not in the evidence file |
| `check_citations.py` | bib entry `unusedentry` is not an evidence source and has no year |
| `check_claims.py` | claim C2 marked supported but its only source is `unavailable` |
| `check_claims.py` | claim C3 is `derived` and supported but has no derivation |
| `build.sh` | undefined citation `page1999pagerank` |

## Must be found by the evaluator

| Id | Severity | Location | Defect |
|---|---|---|---|
| E1 | critical | Theorem in Section 2 | States "paths" where the cited source and the evidence claim C1 say "walks". A path repeats no vertex; the count is of walks. The conclusion rests on this. |
| E2 | major | Section 1, PageRank sentence | Claim has no evidence entry and the cited key does not exist. Uncited and unverifiable universal claim ("every implementation"). Critical if the evaluator judges the citation fabricated rather than missing. |
| E3 | critical | Section 1, factor 3.7 | Numerical claim rests on a source that could not be accessed; presented as established fact without qualification. |
| E4 | major | Proof of the theorem | "Obvious by induction" is not a proof. The induction step is the whole content. |
| E5 | major | Section 2, connectivity test | Text sums powers to $A^N$ while evidence claim C3 says $A^{N-1}$; and the claim has no derivation or source. Internal inconsistency plus unsupported claim. |
| E6 | major | Section 2, "CSR layout" | Acronym never expanded or explained; concept introduced after use with no definition. |
| E7 | major | Conclusion | "Spectral methods are always preferable" appears nowhere in the body or the evidence. New unsupported claim in the conclusion. |
| E8 | minor | Section 1 | "Simple undirected graph" is assumed in the theorem but the introduction says "any graph". |
| E9 | minor | Whole paper | No definition of walk, path, adjacency matrix, or connected before use; audience requirement unmet. Major is acceptable. |
| E10 | major | Evidence claim C1 | The quote attributed to Diestel Section 1.9 is a paraphrase, not verbatim, and the result is an end-of-chapter exercise there, not a statement in the section. Found by fetching the source. |
| E11 | major | Paper folder | No `self-evaluation.md`, so release condition 9 fails. |

## Expected recommendation

FAIL. Dimensions 1, 2, 3, 4 and 5 must each score at most 2.

## Run log

| Date | Evaluator level | Caught | Missed | Recommendation | Notes |
|---|---|---|---|---|---|
| 2026-10-27 | 3 (opus) | E1 to E9, plus E10 and E11 which were added from this run | none | FAIL, scores 1,1,0,1,1,1,1,0,2,1,0,1 | Also found that the fixture preamble lacked `\newtheorem`, fixed the same day so the build fails only on the planted undefined citation. Judged `smith2021walks` fabricated by checking the DOI prefix with doi.org and Crossref. |

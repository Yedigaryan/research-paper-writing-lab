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
| 2026-11-02 | reader only, level 1 (haiku) | comprehension side of E1, E2, E3, E4, E6, E7, E8, E9, and E5's unsupported sum | E5's N versus N-1 mismatch; E10 and E11 are evaluator checks | not applicable | Check after moving technician-reader to Haiku. Ten findings, each with a quoted passage and a correction; about 12.5k tokens. |
| 2026-11-08 | 3 (opus) evaluator plus reader level 1 (haiku), run in parallel | E1 to E9 at the expected severity or higher (E9 as major); E11 named in the recommendation (condition 9 fails) and in the reading notes, but not as a finding line | E10: Diestel full text paywalled, quote not checked against the source; E11 as a finding line | FAIL, scores 1,1,0,1,1,1,1,1,2,1,2,1 | Check after the change that reader findings are ungraded. Reader returned 12 findings, all tagged comprehension with no severity, plus a summary. Evaluator verified the walk count and both connectivity sums by brute force on all 1,099 simple graphs up to 5 vertices. It also found that inspect_pdf.py misses a raw bracketed key such as [page1999pagerank]. |
| 2026-11-14 | 3 (opus) evaluator plus reader level 1 (haiku), run in parallel | E1, E3 critical; E2 critical (expected major); E4, E5, E7 major; E9 major (expected minor); E8 inside a critical finding; E6 and E10 raised, but as minor | E11: the missing self-evaluation.md is not mentioned at all; E6 and E10 below the expected severity (E6 as a minor surplus finding with the correction cut, E10 as a minor locator and quote correction) | FAIL, scores 0,0,0,0,1,1,0,0,1,1,1,1 | Check after the change that adds the page budget, surplus findings, final edits, carried source checks, and the reader reading pages. The evaluator raised two surplus findings (PageRank and the 3.7 comparison as major, the CSR sentence as minor) and reported its spot checks with claim id and locator. It fetched the Diestel preview and found that the quoted statement is an exercise, not text of Section 1.9. It checked the connectivity statement on every graph with 2 to 6 vertices. The reader read the page as an image through the Read tool and returned 12 findings, all tagged comprehension, plus a summary. |

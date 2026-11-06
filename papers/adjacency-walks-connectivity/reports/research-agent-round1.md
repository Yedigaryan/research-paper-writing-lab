Both E1-F10 items are fixed in `evidence.base.json`. I copied it to `evidence.json`, ran `merge_evidence.py` and `check_claims.py`, and the check reports 0 errors and 0 unverified claims.

1. **C4 and C7 are now `supported`.** Each has its `derivation` pointing to `modules/m1.md` (section 5.1 for C4, 5.2 for C7), to the module claims M1-1 and M1-2 in `evidence/modules/m1.json`, and to `modules/m1-calc/m1_check.py`. Their text now says module m1 proved them as M1-1 and M1-2.
2. **`lehman_llm_adjacency_libretexts` is removed.** It was metadata-only, no claim cited it, and nothing else referenced it, so removal left no dangling reference. The schema has no "located, not used" status for sources. As a result, the merged file has 11 sources.

The merged file has 67 claims: 56 supported, 11 qualified, 0 unverified. The 6 remaining warnings are support entries without a quote (C8, C19, C29, M2-4, M2-14). C29 and M2-14 cite the handwritten board, which has no quotable text; the other three are the textbook-absence and length-0 claims. All are qualified claims.

I did not touch `.claude/` or `tests/`.

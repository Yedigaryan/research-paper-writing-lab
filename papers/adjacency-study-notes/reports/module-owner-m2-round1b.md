Both records are added to `papers/adjacency-study-notes/evidence/modules/m2.json`, and the check passes. I changed nothing else in that file, and I did not touch `m1.json`.

**1. Source `m2_connectivity_script`**
- Modelled on `m1_walks_script`: type `code`, `identifier.path` = `scripts/m2_connectivity_test.py`, `access_status` full, `credibility` primary, `found_by` `module:m2`, `accessed` 2026-11-23.
- The notes say it is run with `python3 -I`, give the saved output as `scripts/m2_connectivity_test.out`, list the graphs and checks, and call it a check of examples, not a proof.
- I added it as a second support entry on M2-5:
  - Locator: `scripts/m2_connectivity_test.out`, board graph section.
  - Quote: "off-diagonal entries (i, j, S_ij): [(1, 2, 1), (1, 3, 1), (2, 1, 1), (2, 3, 1), (3, 1, 1), (3, 2, 1)]".
  - M2-5's other support, the whiteboard entry, is unchanged.

**2. Claim M2-11 (O3), added**
- I re-downloaded the Paramadevan and Sotheeswaran PDF and read Section 2.2. The list starts on p. 15 and item 7 is on p. 16, so the page is as you reported. The item reads "The (i, j)th entry of A^m is equal to the number of walks of length m from vi to vj, and the least non-zero m ... is equal to the distance".
- The claim says their property list uses "walks" while their Theorem 1 uses the undefined word "paths".
- Locator: "Section 2.2, item 7, p. 16 (the list begins on p. 15; item 7 is on p. 16)".
- Quote: "is equal to the number of walks of length m from vi to vj". It is the flattened text, with no subscripts, as in the other records for this source, and it covers only part of the item's sentence.
- `kind` fact, `status` supported, `confidence` medium, `used_in` `["sections/limits.tex"]`.

**Check**, run twice from the repository root as instructed (the three commands):
- Merge: "+3 sources, +18 claims; total 12 sources, 52 claims" both times.
- Check: "sources 12; claims supported 49, qualified 3, unverified 0, removed 0; errors 0; warnings 0" both times.

Both E2 fixes are in `evidence.base.json`. I did not copy or merge, and did not touch `.claude/` or `tests/`.

1. **C31, the Paramadevan Theorem 1 claim.** It now follows the two-reading treatment. The source never defines "path". Under the walk reading, which its own proof and its property 7 use, the sentence agrees with walk counting. Under the standard no-repeated-vertex meaning it is false: on the board graph (A^2)_11 = 1, and (A^3)_12 = 2 while only one path joins n1 to n2. I changed its kind from `fact` to `interpretation` and its confidence to `medium`, since the claim is now a reading of the source.
2. **Galway notes locators.** C2 (Definition 1.1.1) is now "printed p. 2 (PDF p. 1)". C5 and C7 now read "printed p. 4 (PDF p. 3)". The source's notes field now records that printed pages are PDF pages plus one, because the first page carries no number.

I checked the page offset against the extracted footers. Theorem 1.1.3 sits between the footers "3" and "4", so printed p. 4 is correct and matches the earlier locator.

One loose end for the orchestrator. The first entry in `contradictions` still says "Paramadevan Theorem 1 says the entry of A^l counts paths". That is accurate as a description of the source's wording, so I left it. Reword it in the next pass if you want it to match the two-reading framing.

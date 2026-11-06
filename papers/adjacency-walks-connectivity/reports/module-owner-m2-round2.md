E2-F5 is fixed in `evidence/modules/m2.json`. I did not run the merge or `check_claims.py`. The JSON loads, and I changed nothing outside this file.

M2-14 now cites `author_compute_script` with exact lines from `appendices/compute.out`. The cited lines are 24, 25, 27 and 28, and 29 and 30 together. They cover the four counts in the claim:
- **n1 to n1, length 2:** one walk, no paths (line 24).
- **n2 to n2, length 2:** two walks (line 25).
- **n1 to n3, length 2:** one walk and one path (line 29). **Length 4:** two walks, no trails, no paths (line 30).
- **n1 to n2, length 3:** two walks. **Length 2:** none (lines 27 and 28).

The derivation field now points to `appendices/compute.py` and `compute.out`. It also mentions my `modules/m2-calc.py` PART 2, which prints the same counts independently.

I dropped the whiteboard entry. It had no quote, and it supports only the identity of the board graph, which is not one of the claim's numbers.

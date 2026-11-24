# Source checks

The evaluators' CITATION SPOT CHECKS blocks, as returned, round by round. A later round carries a check recorded as `supports` when `claims_changed.py` does not list its claim.

## Round 1, 2026-11-23

```
CITATION SPOT CHECKS
gotti_18211_lecture27 | C20 | Proposition 2, p. 1 | fetched | supports | The proposition says "there are A^ℓ_jk walks of length ℓ from j to k", for directed or undirected graphs, by induction from ℓ = 1. The evidence quote is only the lead-in sentence (F1).
gotti_18211_lecture27 | C29 | Proposition 3, p. 2 | fetched | supports | The quote is verbatim: "Then G is connected if and only if all the entries of (In + A)n−1 are positive." The proof uses the binomial identity.
paramadevan2021adjacency | C27 | Theorem 2 and proof, p. 17 | fetched | supports | Statement and proof quotes are verbatim. The converse step "if bij ≠ 0, then there exist at least one path" confirms the gap the paper describes. Metadata matches: JSc EUSL 12(1) 2021, pp. 13-21, DOI 10.4038/jsc.v12i1.29.
paramadevan2021adjacency | C32 | Theorem 1, p. 16 | fetched | supports | "different paths of length l ... equal to the (i, j)th entry of A^l_G", verbatim. "path" is undefined in the paper. Section 2.2 item 7 (p. 16) says walks (F8).
grinberg_graph_theory | C24, C25 | Corollary 2.9.7, p. 39; Section 2.9.4, p. 40 | fetched | supports | arXiv:2308.04512v3, "Spring 2025 edition, June 7, 2025"; the page headers match. Both quotes are verbatim and contiguous.
grinberg_graph_theory | C8, C12, C15 | Definition 2.9.1(a)-(d), p. 36; Example 2.9.2, p. 37 | fetched | supports | C8 and C15 are verbatim. C12 joins sentences from (c) and (d) without an ellipsis (F2).
bai_bimsa_adjacency | C13, C21, C29, C33 | pp. 1-2 | fetched | supports | Theorem 1, the path definition, Theorem 2 and "aggregates all paths of length ≤ n − 1" are verbatim. "counts walks — not paths" is commentary, not Theorem 1 (F8).
galway_adjacency_notes | C2, C19 | Definition 1.1.1, p. 2; Theorem 1.1.3, p. 4 | fetched | supports | Both quotes are verbatim. Theorem 1.1.3 is for positive k.
wayne_cos226_undirected | M2-9 | slide "Depth First Search" (PDF p. 6) | fetched | supports | "Running time. O(E) since each edge examined at most twice." The authors in the footer are Sedgewick and Wayne (F12).
petrosyan_graph_theory | C1, C3, C4, C7, C10, C11, C15, C16, C26 | printed pp. 9, 11, 21, 22, 23, 48 (PDF pp. 10, 12, 22, 23, 24, 49) | viewed | supports | I viewed these pages as images. Definition 1.1.1 is on p. 9; Definition 1.1.4 and the adjacency matrix with a_ii = 0 and a_ij = a_ji are on p. 11; Definition 1.2.10 is on p. 21; the repetition note and Definitions 1.2.12 and 1.2.13 are on p. 22; distance property 1 and Lemma 1.2.1 (u ≠ v, no bound) are on p. 23; Definition 2.1.1 is on p. 48. Page 21 also says a walk is written by its vertex sequence (F5).
whiteboard1, whiteboard2 | C6, C17, C22 | whole board | viewed | supports | The matrix rows are 0 1 0 / 1 0 1 / 0 1 0. The drawing has three lines with an arrowhead at 2. The "Def." line reads "for any n_i, n_j ∃ path between nodes". All of this matches the notes on sources.
```

## Round 2, 2026-11-23

```
CITATION SPOT CHECKS
gotti_18211_lecture27 | C20 | Proposition 2, p. 1 | fetched | supports | Matches the source character by character except that the superscript ℓ and subscript jk of A^ℓ_jk are flattened ("Aℓjk"); "adjacency ma-trix" is a line-break hyphen in the PDF. On PDF p. 1. F1 resolved.
grinberg_graph_theory | C12 | Definition 2.9.1(c), p. 36; Definition 2.9.1(d), p. 36 | fetched | supports | arXiv 2308.04512v3 (June 7, 2025), 454 pp. Both sentences are verbatim, one entry each; the page header puts Definition 2.9.1 on p. 36. F2 resolved for C12.
grinberg_graph_theory | C15 | Example 2.9.2, p. 37 | fetched | supports | "The sequence (5) is a walk from 5 to 5. It has length 0. It is a path." is verbatim and lies between the p. 37 and p. 38 headers. The paper's label "definition" is F17.
petrosyan_graph_theory | C15 | distance property 1, printed p. 23 (PDF p. 24) | viewed | supports | Viewed as an image. Item 1: d_G(u,v) ≥ 0 and d_G(u,v) = 0 exactly when u = v. Matches the recorded Armenian quote.
galway_adjacency_notes | C5 | Notes 1 and 2 after the adjacency matrix, printed p. 3 (PDF p. 2) | fetched | supports | Both entries are verbatim with their markers "1." and "2.". C5 is not cited in the text. M2-6 still carries the joined version (F15).
paramadevan2021adjacency | M2-11 | Section 2.2, item 7, p. 16 | fetched | supports | "The (i, j)th entry of A^m_G is equal to the number of walks of length m from vi to vj": the recorded fragment is verbatim. The list starts on p. 15 and item 7 is on p. 16, as the locator says. Theorem 1 is also on p. 16.
petrosyan_graph_theory | m1-7 | printed p. 21, sentence after Definition 1.2.10 (PDF p. 22) | viewed | supports | Viewed as an image. The sentence on abbreviating a (u0, uk)-walk as its vertex sequence u0, ..., uk, each vertex adjacent to the one before, matches the recorded quote word for word; the text layer confirms the words.
m2_connectivity_script | M2-5 | scripts/m2_connectivity_test.out, BOARD GRAPH section | viewed | supports | Re-ran with python3 -I: identical output. The quoted line "off-diagonal entries (i, j, S_ij): [...]" is verbatim.
bai_bimsa_adjacency | C21, C33 (control) | Theorem 1 and following text, p. 1; Theorem 2 proof sketch point 4, p. 2 | fetched | supports | Control. "counts walks — not paths." follows Theorem 1 and the definitions. "(I + A)n−1 aggregates all paths of length ≤ n − 1." is on p. 2. Agrees with the round 1 record.
gotti_18211_lecture27 | C29 | Proposition 3, p. 2 | carried | supports | Round 1 record; I saw Proposition 3 on PDF p. 2 this round.
paramadevan2021adjacency | C27, C32 | Theorem 2, p. 17; Theorem 1, p. 16 | carried | supports | Round 1 record; the pages agree with this round's fetch.
grinberg_graph_theory | C8, C24, C25 | Definition 2.9.1(a),(b), p. 36; Corollary 2.9.7, p. 39; Section 2.9.4, p. 40 | carried | supports | Round 1 record; the page headers agree with this round's fetch.
bai_bimsa_adjacency | C13, C29 | p. 1 | carried | supports | Round 1 record.
galway_adjacency_notes | C2, C19 | Definition 1.1.1, p. 2; Theorem 1.1.3, p. 4 | carried | supports | Round 1 record.
wayne_cos226_undirected | M2-9 | slide "Depth First Search" (PDF p. 6) | carried | supports | Round 1 record.
petrosyan_graph_theory | C1, C3, C4, C7, C10, C11, C16, C26 | printed pp. 9, 11, 21, 22, 23, 48 | carried | supports | Round 1 record; I also viewed pp. 21 and 23 this round.
whiteboard1, whiteboard2 | C6, C17, C22 | whole board | carried | supports | Round 1 record.
```

## Round 3, 2026-11-24

```
CITATION SPOT CHECKS
galway_adjacency_notes | M2-6 | Notes 1 and 2 after Definition 1.1.2, printed p. 3 | fetched | supports | Changed claim. "1. The adjacency matrix is symmetric (i.e. equal to its transpose) if the graph is undirected." and "2. The adjacency matrix has zeros on its main diagonal (unless the graph has loops)." are verbatim, with markers, above the "3" footer. They support only the structural part of M2-6; the paper does not cite Galway for it. Round 2 F15 resolved.
m2_connectivity_script | M2-6 | scripts/m2_connectivity_test.out, DISCONNECTED GRAPH section, line 55 | viewed | supports | Re-ran with python3 -I: byte-identical. Line 55 is the quoted off-diagonal list, verbatim; the verdict is connected = False and the brute force agrees.
paramadevan2021adjacency | C27 (control) | Theorem 2, p. 17 | fetched | supports | Control. Theorem 2 (B = A_G + ... + A_G^{n-1}; connected iff b_ij != 0 for i != j) is on PDF p. 5 above the printed "17" footer. Metadata JSc EUSL 12(1), pp. 13-21. Agrees with the round 1 and 2 record.
gotti_18211_lecture27 | C20, C29 | Proposition 2, p. 1; Proposition 3, p. 2 | carried | supports | Round 2 record.
grinberg_graph_theory | C8, C12, C15, C24, C25 | Definition 2.9.1(a)-(d), p. 36; Example 2.9.2, p. 37; Corollary 2.9.7, p. 39; Section 2.9.4, p. 40 | carried | supports | Rounds 1 and 2 record.
bai_bimsa_adjacency | C13, C21, C29, C33 | pp. 1-2 | carried | supports | Rounds 1 and 2 record.
galway_adjacency_notes | C2, C5, C19 | Definition 1.1.1, p. 2; Notes 1 and 2, p. 3; Theorem 1.1.3, p. 4 | carried | supports | Rounds 1 and 2 record; I saw Definition 1.1.1 on p. 2 in this round's fetch.
paramadevan2021adjacency | C32, M2-11 | Theorem 1, p. 16; Section 2.2, item 7, p. 16 | carried | supports | Rounds 1 and 2 record.
wayne_cos226_undirected | M2-9 | slide "Depth First Search" (PDF p. 6) | carried | supports | Round 1 record.
petrosyan_graph_theory | C1, C3, C4, C7, C10, C11, C15, C16, C26, m1-7 | printed pp. 9, 11, 21, 22, 23, 48 | carried | supports | Rounds 1 and 2 record.
whiteboard1, whiteboard2 | C6, C17, C22 | whole board | carried | supports | Round 1 record.
m2_connectivity_script | M2-5 | scripts/m2_connectivity_test.out, BOARD GRAPH section | carried | supports | Round 2 record; this round's re-run is identical.
```

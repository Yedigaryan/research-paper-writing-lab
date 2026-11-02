# Baseline: adjacency paper under the current harness

The end product of one full research-paper run under the harness that is
live today (base commit 3aa1ca7, after the DOM adoption and the
Proposition 2.9.10 correction), produced on 2026-11-02 as the base
rollout of the whole-pipeline refinement step. Every candidate harness in
that step is measured against this run. Each candidate runs the same
brief, the same sources, and the same models.

Files in this folder:

- adjacency-baseline.pdf: the final paper, 23 pages.
- evaluation-report.md: all three evaluation rounds.
- reader-findings.md: the technician reader's findings for each round.

The full run, with the brief, the evidence, the module reports and every
agent report, is on branch claude/harness/adjacency-pipeline/base at
commit ef7f181.

## Run

| Item | Value |
|---|---|
| Steps | research, 3 module owners, author, gate, 3 evaluation rounds with 2 revisions |
| Wall clock | 19:31 to 20:27 UTC, about 56 minutes |
| API-equivalent cost | 21.37 USD (Opus 5.5 orchestrator, Sonnet workers and reader, Opus evaluator) |
| Evidence | 16 sources, 88 claims: 64 supported, 24 qualified |
| Decision | INCOMPLETE: three-round limit reached, conditions 4, 5 and 10 fail |

## Scores by round

| Dimension | Round 1 | Round 2 | Round 3 |
|---|---|---|---|
| 1 Correctness | 4 | 4 | 4 |
| 2 Evidence coverage | 3 | 4 | 4 |
| 3 Citation integrity | 3 | 5 | 5 |
| 4 Logical validity | 4 | 4 | 3 |
| 5 Understandability | 3 | 4 | 4 |
| 6 Completeness | 4 | 5 | 5 |
| 7 Methodological rigor | 5 | 5 | 5 |
| 8 Critical analysis | 5 | 5 | 4 |
| 9 Internal consistency | 3 | 4 | 4 |
| 10 Reproducibility | 5 | 5 | 5 |
| 11 LaTeX and PDF quality | 4 | 4 | 4 |
| 12 Answer relevance | 4 | 5 | 5 |

## Findings by round

| Round | Evaluator findings | of which major | Reader findings | of which major | Pages |
|---|---|---|---|---|---|
| 1 | 15 | 4 | 42 | 6 | 21 |
| 2 | 11 | 1 | 22 | 5 | 22 |
| 3 | 8 | 1 | 22 | 2 | 23 |

No critical finding in any round.

## What was still open at the end

- E3-1, major: the Section 7 critique of the literature claims one
  counterexample refutes three published statements, and it does not
  refute the restated sum claim.
- R3-1, major: the course meaning of "path" rests on an assignment text
  that is not quoted, because no file holds it.
- R3-15, major: the parity argument for why a single matrix power is not
  enough is hard to follow.
- Minor: "one multiplication" is false for N > 3; "grow quickly" is
  unsupported; plain-words sentences of 23 to 32 words; undated sources
  print "n.d."; a blank band on pages 19 and 20; two uncited evidence
  sources; awkward provenance wording.

## How to compare after the fixes

Compare a candidate's final paper with this one on:

1. The decision. PASS beats INCOMPLETE.
2. Major findings open at the end: 3 here.
3. Findings in round 1, before any revision: 4 evaluator majors and 42
   reader findings here. This measures the first draft.
4. Rounds used: 3 here, the maximum.
5. The final scores, read with their observations, not as a total.
6. Cost and wall clock, from the probe session.

The refinement step's own decision is made by a blind selector reading
the papers, not by these numbers. This sheet is for your own comparison.

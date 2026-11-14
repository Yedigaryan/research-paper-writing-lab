# Model capability levels

The pipeline requires the independent evaluator to run on a model at least
one level above the author and every module owner. Levels are a documented
capability ladder, not names, prices, or parameter counts.

## Ladder

| Level | Model alias | Agent frontmatter value |
|---|---|---|
| 1 | Haiku | `model: haiku` |
| 2 | Sonnet | `model: sonnet` |
| 3 | Opus | `model: opus` |
| 4 | Fable | `model: fable` |

## Configured assignment

| Agent | Level | Reason |
|---|---|---|
| `research-agent` | 2 | Long web-search context; breadth over depth. |
| `module-owner` | 2 | One per subtopic, run in parallel. |
| `paper-author` | 2 | Writes from module reports and evidence, not from memory. |
| `technician-reader` | 1 | Diagnostic reader; its findings are advisory. Haiku since 2026-11-02 to save usage; it reads the compiled pages only. |
| `paper-evaluator` | 3 | Must exceed level 2. |
| Orchestrator | session model | Not pinned. Recorded in the report. |

Rule: evaluator level must be strictly greater than the maximum level of
`paper-author` and `module-owner`. If either is raised to 3, the evaluator
must be raised to 4. If the evaluator cannot be raised because no higher
level exists, the evaluation report marks the hierarchy requirement as not
met; the pipeline does not silently continue with an equal level.

## What the orchestrator records

In every round of `evaluation-report.md`:

- The level configured for each agent that ran, taken from this table.
- Whether the hierarchy rule holds for the configured levels.
- The note that a runtime fallback to another model is not observable from
  inside the session. The report states configured levels, not served
  models. If the harness reports a fallback for the evaluator, the round is
  marked as not meeting the hierarchy requirement and is re-run.

## Changing a level

Edit the `model:` line in the agent file under `.claude/agents/` and the
table above in the same commit. Then run the pipeline on
`tests/fixtures/defective-paper/` and confirm the evaluator still raises the
findings in `expected-findings.md`.

## Decisions log

- 2026-10-27: Evaluator is a fresh agent each round, given the previous
  round's report for verifying resolution. Alternative: message the same
  evaluator across rounds. Switch if rounds regularly exceed three or the
  fresh evaluator re-raises findings marked resolved. Not yet measured.
- 2026-11-02: `technician-reader` moved from level 2 (Sonnet) to level 1
  (Haiku) to reduce usage. The hierarchy rule is unaffected: it constrains
  the evaluator against the author and module owners, and the reader's
  findings are advisory. Orchestrator sessions for refinement probes run
  on Opus 5.5, not Fable 5.1. Watch the reader's findings in the next runs;
  if they become shallow or wrong, move it back to Sonnet.
- 2026-11-08: The orchestrator never grades reader findings. The reader
  returns ungraded comprehension findings; they are recorded as returned in
  `reader-findings.md` and sent to the author as advisory. Severity belongs
  to the evaluator alone, which reads `reader-findings.md` on later rounds
  and raises a reader passage as its own finding when it shows a real
  defect. Reason: in the adjacency-pipeline step the base orchestrator
  graded reader findings itself, which made rounds differ for reasons
  outside the harness under test.
- 2026-11-14: Three changes to how rounds are spent, after the
  adjacency-pipeline step cost about 19 to 21 USD a run with three rounds
  each. (1) Minor findings no longer cost a round: a round with every
  dimension at 3 or more and no critical or major finding open is
  released after final edits that the orchestrator checks by diff and no
  evaluator re-reads. In that step the composed run spent its third
  evaluation on minor findings alone. (2) Later rounds carry the recorded
  source checks of unchanged claims and fetch only for what
  `claims_changed.py` lists, plus one control; the evaluators had fetched
  5, 6, then 8 sources in successive rounds. (3) The reader reads the
  PDF pages, not extracted text, because `pdftotext` drops superscripts
  and both readers of the short adjacency papers reported "A = I" for
  A^0 = I. Watch for a defect that final edits let through, and for a
  control fetch that disagrees with the record; either is a reason to
  revisit the change.

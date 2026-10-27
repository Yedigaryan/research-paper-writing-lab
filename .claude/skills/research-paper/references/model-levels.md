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
| `technician-reader` | 2 | Diagnostic reader; its findings are advisory. |
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

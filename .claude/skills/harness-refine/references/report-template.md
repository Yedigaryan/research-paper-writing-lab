# Refinement report template

Written by the orchestrator to `harness-runs/<task>/refinement-report.md`.
One file per refinement step; sequential rounds append a section each.

```
# Refinement report: <task>

Task: <paper slug>, stage <author | pipeline>, k = <k>, mode <agg | seq>
Base commit: <hash>
Date: <YYYY-MM-DD>
Domain: <library domain>

## Budget

| Item | Allowed | Used |
|---|---|---|
| Rollouts | 4k = <n> | <n> |
| Improver sessions | 3k = <n> | <n> |
| Selection sessions | 1 | <n> |
| Reflection sessions | 1 | <n> |

## Candidates

| Label | Dimension | Validation | Tree diff vs base | Probe branch | Deliverable |
|---|---|---|---|---|---|
| base | none | valid | none | <branch> | <pages> pages, <rounds> rounds |
| inv | INV | valid | <n added, n modified> | <branch> | ... |
| dom | DOM | valid or fell back to base (reason) | ... | ... | ... |
| composed | compose | valid or KEEP_BASE | ... | ... | ... |

## Proposer notes

### inv
<the notes block verbatim>

### dom
<the notes block verbatim>

## Composer notes
<the notes block verbatim>

## Selection

Pool: <labels>, anonymised as <ids> (map in pool-map.json).
Selector: paper-evaluator, level 3, given task.md, source/, candidates/
only.

<the why block verbatim>

Choice: <id> = <label>

## Reflection

<the edits block verbatim>

<the experience block verbatim, or NO_ENTRY>

## Decision

Adopted: <label, or KEEP_BASE>
Installed into .claude/: <yes, commit hash | no>
Library entry: <path | none (NO_ENTRY | confounded)>
tests/run-checks.sh after install: <pass | fail>

## Evaluator scores, for the record only

Reported after the decision, never used to steer it. One row per
candidate: the final-round dimension scores from each rollout's
evaluation report.

| Label | Correctness | Evidence | Citations | Logic | Understandability | ... |
|---|---|---|---|---|---|---|
```

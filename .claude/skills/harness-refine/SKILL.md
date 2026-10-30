---
name: harness-refine
description: Refine the research-paper harness itself, with model weights fixed and without an answer key, by the Harness2 loop: propose candidate harness trees on two dimensions from the evidence of earlier rollouts, probe each candidate in a fresh session, compose one, select the best paper blind, reflect the lessons into a per-domain library, and adopt the winner. Use when the user asks to improve, tune, refine, or learn from the pipeline, or to run a refinement step on a finished paper.
---

# Harness refine

Runs one refinement step of the research-paper harness on one task. The
session running this skill is the orchestrator: it builds evidence, spawns
the improver agents, validates and probes candidate trees, runs the blind
selection, records the reflection, and adopts or keeps the base. It never
edits a candidate tree itself and never judges a paper itself.

The method is Harness2's (see `third_party/harness2/NOTICE.md`), applied to
this repository: the model is fixed, the editable surface is declared, the
evaluator and rubric are frozen, and every edit must trace to a moment in
a trajectory.

## Roles

| Role | Where it runs | Level | Reads | Writes |
|---|---|---|---|---|
| Orchestrator | this session | session model | everything | `harness-runs/<task>/`, `.claude/` on adoption, the library |
| `harness-proposer` | agent, two in parallel (INV, DOM) | 3 | one context copy | its `context/harness/` in place |
| `harness-composer` | agent | 3 | context with pool | its `context/harness/` in place |
| `paper-evaluator` as selector | agent, fresh | 3 | task, sources, anonymised candidates | nothing; returns a choice |
| `harness-reflector` | agent, fresh | 3 | context with pool and the choice | nothing; returns edit rows and a lesson |
| probe | fresh Claude Code session on a branch | the pipeline's own levels | the candidate tree as the live `.claude/` | the paper folder on its branch |

Levels follow `.claude/skills/research-paper/references/model-levels.md`.
Improver agents sit at level 3, equal to the evaluator and above the
author and module owners whose files they edit.

## Files

```
.claude/skills/harness-refine/harness.yaml     the editable surface and the reserved yardstick
.claude/skills/harness-refine/scripts/
    harness_tree.py     export, validate, diff, install a tree
    build_evidence.py   build the context directory from a paper folder
    anonymize_pool.py   blind the deliverables for selection
    library_add.py      store an adopted harness and rebuild INDEX.md
.claude/skills/harness-refine/references/
    missions.md         the agents' missions
    surface.md          what a tree may contain
    probe-prompt.md     prompts for probe sessions and how to collect one
    report-template.md  refinement-report.md
    library-layout.md   the domain library
.claude/skills/harness-refine/library/<domain>/   adopted harnesses
harness-runs/<task>/                              one directory per step
```

Under `harness-runs/<task>/`, `context/`, `propose/`, and `probe/` are
ignored by git; `refinement-report.md`, `pool-map.json`, `selection.md`,
and `reflection.md` are committed.

## Budget identity

For k = 1 (the default and the only mode to start with):

| Item | Count |
|---|---|
| Rollouts | 4: base, INV probe, DOM probe, composed probe |
| Improver sessions | 3: INV proposer, DOM proposer, composer |
| Selection | 1 |
| Reflection | 1 |

A proposer that answers KEEP_BASE, or a composer that answers KEEP_BASE,
saves its probe: the base rollout stands in for it. A validation retry is
not a new session. The step never exceeds these counts; if it would, stop
and report.

## Stages

The author stage is the cheapest useful rollout and the place to start:
the brief, evidence file, and module reports are fixed inputs, and a
rollout is one author run, the mechanical gate, one evaluator round, and
one reader pass. The whole-pipeline stage reruns every step up to the
three-round limit. The user names the stage; default `author`.

## Preconditions

- A finished base rollout: a paper folder under `papers/<slug>/` with
  `brief.md`, `evidence/evidence.json`, `modules/`, a compiled paper, and
  `evaluation-report.md`, all committed. The current head is the base
  commit.
- `bash tests/run-checks.sh` passes and the working tree is clean.
- The session is on a `claude/*` branch. Probe branches are named
  `claude/harness/<task>/<label>`, inside the pushable namespace that the
  repository's `CLAUDE.md` allows.
- A domain name for the library, from the user or the brief (for example
  `graph-theory`). If none is clear, ask once.

## Step 1: Build the base evidence

```
T=harness-runs/<task>
BASE=$(git rev-parse HEAD)
python3 .claude/skills/harness-refine/scripts/build_evidence.py rollout \
    papers/<slug> --label base --out $T/context \
    --library .claude/skills/harness-refine/library/<domain>
python3 .claude/skills/harness-refine/scripts/harness_tree.py validate repo
```

`context/harness/` is the exported live tree. If the paper has no
`reports/` folder, the trajectory says so; the step still runs on the
commits, the evaluation report, the self-evaluation, and the module
reports.

Then make one copy of the context per proposer:

```
cp -r $T/context $T/propose/inv
cp -r $T/context $T/propose/dom
```

## Step 2: Propose (two proposers in parallel)

Spawn two `harness-proposer` agents in one message. Each gets: the
absolute path of its context copy, its dimension (`INV` or `DOM`), and the
instruction to read `references/missions.md` as its agent file says. Do
not paste trajectories or your own diagnosis into the prompt; the agent
reads the evidence itself. Do not tell it what the evaluator scored.

When each returns, save its notes to `$T/propose/<label>/NOTES.md` and
validate its tree:

```
python3 .claude/skills/harness-refine/scripts/harness_tree.py \
    validate $T/propose/<label>/harness --base repo
python3 .claude/skills/harness-refine/scripts/harness_tree.py \
    diff repo $T/propose/<label>/harness
```

Invalid: send the error list back to the same agent once. Still invalid:
the candidate becomes the base tree, recorded in the report with the
reason, and its probe is skipped. `KEEP_BASE` with no diff: same, without
the error.

## Step 3: Probe each candidate

A probe runs in a fresh session because this session loaded its agents at
start. For each candidate that differs from the base:

```
git checkout -b claude/harness/<task>/<label> $BASE
python3 .claude/skills/harness-refine/scripts/harness_tree.py \
    install $T/propose/<label>/harness
bash tests/run-checks.sh
```

If the checks fail, the candidate's scripts broke the pipeline: record it,
delete the branch, treat the candidate as base. Otherwise, for the author
stage, remove the author's outputs so the probe starts from the inputs:
`main.tex`, `sections/`, `appendices/`, `figures/`, `references.bib`,
`main.pdf`, `self-evaluation.md`, `evaluation-report.md`,
`reader-findings.md`, `reports/`, and `evidence/modules/author.json`; then
rebuild `evidence/evidence.json` from the base file and the remaining
fragments as the research-paper skill's Step 3 says. For the whole
pipeline stage, keep only `brief.md` and `sources/`. Commit on the probe
branch with the message "Probe <label>: candidate harness and reset
inputs" and push it. Return to the working branch.

Start the probe with the prompt from `references/probe-prompt.md`. Use
`create_session` from the claude-code-remote server when it is available,
with `source_revision` set to the probe branch. If it is not available,
give the user the branch name and the prompt, say that the step waits on
the probe, and end the turn. Never run a probe inside this session.

Run the INV and DOM probes in parallel. When a probe reports back, collect
it as `references/probe-prompt.md` says: fetch the branch, add a worktree
under `$T/probe/<label>`, build its rollout into `$T/context` with
`--since $BASE --no-harness`, and add its tree to the pool. A probe that
produced no paper is collected the same way and counts as a rollout.

## Step 4: Compose

```
rm -rf $T/compose && cp -r $T/context $T/compose
```

The copy carries `harness/` (the base tree), `pool/inv`, `pool/dom`, and
every rollout. Spawn `harness-composer` with that path. Validate and diff
its tree as in Step 2, with the same single retry and the same fallback.
Save its notes to `$T/compose/NOTES.md`.

If the composed tree differs from the base, probe it as in Step 3 with
label `composed`. If it equals the base or an existing candidate, its
rollout is that candidate's rollout; record that and skip the probe.

## Step 5: Select blind

Build the pool from every distinct rollout, then anonymise:

```
python3 .claude/skills/harness-refine/scripts/anonymize_pool.py \
    $T/select --map $T/pool-map.json \
    base=$T/context/deliverables/base.md inv=... dom=... composed=...
cp $T/context/task.md $T/select/ && cp -r $T/context/source $T/select/
cp $T/context/LAYOUT.md $T/select/
```

`$T/select` holds `task.md`, `source/`, `candidates/`, and nothing else.
Spawn a fresh `paper-evaluator` with that path and the "Selector" section
of `references/missions.md` as its mission, stated in the prompt: it is
not evaluating against the rubric this time, it is choosing one of the
candidates by the mission's order of criteria, and it must not look
outside `$T/select`. Do not give it rollouts, the pool, the map, or any
label. Save its full reply to `$T/selection.md` and unblind the choice
with `pool-map.json`.

## Step 6: Reflect

Tell the reflector the selected label. Spawn `harness-reflector` with
`$T/compose` (which has the base tree, the pool including `composed`, and
every rollout) and the label. Save its reply to `$T/reflection.md`.

## Step 7: Record and decide

Write `$T/refinement-report.md` from `references/report-template.md`:
budget used, candidates with validation and diff results, proposer and
composer notes verbatim, the selection reasoning and choice, the
reflection, and the decision. Evaluator scores from the rollouts go in the
last section, for the record only; they never decide anything in this
skill.

Decision rule: adopt the tree that produced the selected paper.

- Selected `base`: KEEP_BASE. Nothing is installed. The report records
  it as a result, not a failure.
- Selected a candidate: install its tree into `.claude/` on the working
  branch and run the checks:

```
python3 .claude/skills/harness-refine/scripts/harness_tree.py \
    install $T/<propose|compose>/<label>/harness
bash tests/run-checks.sh
```

The adopted tree never touches the evaluator, reader, or rubric, so the
fixture evaluator check in `tests/README.md` is not required by adoption
alone; run it anyway if a script or the evidence schema changed.

Library: if the reflection has an experience block,

```
python3 .claude/skills/harness-refine/scripts/library_add.py <domain> <task> \
    --tree <adopted tree dir> --label <label> --why $T/selection.md \
    --reflection $T/reflection.md --run $T
```

The script refuses `NO_ENTRY` and a lesson without cue, lesson, and
evidence; then the library stays as it is and the report says so. A
KEEP_BASE step with a real lesson still writes an entry whose tree is the
base.

Commit `harness-runs/<task>/` (the committed files only), the adopted
tree if any, and the library entry if any, in one commit with a message
naming the task, the decision, and the selected label. Push according to
the repository's `CLAUDE.md`. Delete the probe worktrees; keep the probe
branches until the user says otherwise.

Report to the user: the decision, the one-line reason from the selector,
the edit rows' verdicts, whether a lesson was stored, the budget used, and
the paths of the report and the probe branches.

## Sequential mode (k = 2, later)

Run Steps 2 to 4 again with the composed tree as the new base: the
proposers edit the checkpoint, the evidence carries every earlier
rollout, and `KEEP_BASE` means keep the checkpoint. Selection and
reflection run once at the end over every distinct rollout. Budget: eight
rollouts and six improver sessions. Do not run this before one k = 1 step
has completed on the task and the user has read its report.

## Hold-out check (later)

After a library entry exists, take one question not in the library, run
the research-paper skill once under the original harness and once under
the adopted one, and report both evaluation results side by side. Scores
are reported here as the normal evaluator produced them, after adoption;
they never steer a refinement step.

## Rules the orchestrator never breaks

- The evaluator, the reader, the rubric, the model ladder, the hooks, this
  skill, and the library are the yardstick. A candidate that touches them
  is rejected by the validator; never install around it.
- Proposers, the composer, and the reflector never receive the fixture's
  `expected-findings.md`, a rubric score as a target, or the
  orchestrator's own opinion of what should change. The evidence builder's
  leak check runs on every context before an agent sees it.
- The selector never sees a rollout, a harness tree, a label, or the map.
- No script from a candidate tree is executed by an improver agent; the
  orchestrator runs candidate scripts only through `tests/run-checks.sh`
  on the probe branch.
- Every probe is a fresh session on its own branch. This session never
  swaps its own `.claude/` to probe.
- Budget counts are recorded in the report and never exceeded.
- KEEP_BASE is a result. A score is never consulted to decide adoption.
- Clean text in every file this skill writes: no emojis, no decorative
  symbols. `SKILL.md` stays under 500 lines; references stay one level
  deep.
- Commit and push only as the repository's `CLAUDE.md` allows.

# Probe prompts

A probe is one rollout of a candidate harness. The candidate's files must
be the live `.claude/` tree, and a Claude Code session loads agents when
it starts, so a probe always runs in a fresh session on the candidate's
branch. The orchestrator fills the placeholders and sends the prompt
either through the `create_session` tool of the claude-code-remote server
(preferred: `source_revision` set to the branch, `permission_mode`
inherited, no plan mode) or, when that tool is unavailable, by giving the
user the prompt and the branch to start a session on.

The probe session never edits `.claude/`, never touches another branch,
and commits and pushes everything it produced. Everything it must leave
behind for the trajectory is listed in the prompt; the evidence builder
reads only the branch.

## Author-stage probe

```
You are on branch <branch>. Do not change anything under .claude/ or
tests/. Do not switch branches.

Run the research-paper skill on papers/<slug>, author stage only:

1. The brief, evidence/evidence.json, and modules/ are final inputs. Do
   not run research or module owners.
2. Step 4: spawn paper-author to write the paper from scratch, then run
   the mechanical gate. Send failures back to the author until it passes.
3. Step 5 once: spawn a fresh paper-evaluator and technician-reader.
4. Step 6: write Round 1 into evaluation-report.md and write the reader's
   findings to reader-findings.md. Do not revise the paper afterwards;
   this probe is one round.
5. Save each agent's final message verbatim under
   papers/<slug>/reports/<agent-name>-round1.md.
6. Commit everything in papers/<slug>/ with the message
   "Probe <label>: author-stage rollout of <slug>" and push with
   git push -u origin <branch>.

Report back: the commit hash, the evaluator's recommendation, and any
step that could not be completed.
```

Before sending, the orchestrator has already reset the author's outputs
on the branch (see the skill, Step 4), so the author starts from the
brief, evidence, and modules alone.

## Whole-pipeline probe

```
You are on branch <branch>. Do not change anything under .claude/ or
tests/. Do not switch branches.

Run the research-paper skill end to end on the question in
papers/<slug>/brief.md. The brief is final; do not ask the user. Follow
every step through the three-round limit and the release conditions.
Save each agent's final message verbatim under
papers/<slug>/reports/<agent-name>-round<n>.md and the reader's findings
of each round to reader-findings.md. Commit after each step as the skill
says, with messages prefixed "Probe <label>:", and push with
git push -u origin <branch>.

Report back: the final decision, the last commit hash, and any step that
could not be completed.
```

## Collecting a probe

```
git fetch origin <branch>
git worktree add harness-runs/<task>/probe/<label> <branch>
python3 .claude/skills/harness-refine/scripts/build_evidence.py rollout \
    harness-runs/<task>/probe/<label>/papers/<slug> \
    --repo harness-runs/<task>/probe/<label> \
    --label <label> --out harness-runs/<task>/context \
    --since <base commit> --no-harness
python3 .claude/skills/harness-refine/scripts/build_evidence.py pool \
    harness-runs/<task>/context --label <label> \
    --tree harness-runs/<task>/propose/<label>/harness
```

A probe that produced no paper is still a rollout: its trajectory is
built and its deliverable file says so. It counts against the budget.

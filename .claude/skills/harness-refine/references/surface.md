# The editable surface

What a candidate harness tree may contain, and the rules the validator
enforces before any candidate runs. The authoritative list is
`harness.yaml` next to the skill; this file explains it to the agents
that edit a tree.

## Files in the tree

Paths are relative to the repository root, exactly as they appear in
`context/harness/`.

| Component | Path | Role |
|---|---|---|
| Skill | `.claude/skills/research-paper/SKILL.md` | Always-on text for the orchestrator: the steps, roles, and rules. |
| References | `.claude/skills/research-paper/references/<name>.md` | On-demand knowledge, read when a step names the file. |
| Scripts | `.claude/skills/research-paper/scripts/<name>.py` or `.sh` | Deterministic checks and transforms, run from the repository root. |
| Agents | `.claude/agents/research-agent.md`, `module-owner.md`, `paper-author.md` | Always-on text for one agent each: frontmatter plus the instructions. |

Not in the tree and never editable: `paper-evaluator.md`,
`technician-reader.md`, `references/rubric.md`,
`references/model-levels.md`, anything under
`.claude/skills/harness-refine/`, `CLAUDE.md`, `tests/`, and
`.claude/settings.json`. A tree that contains one of these is rejected.

## Rules the validator enforces

1. Every file matches the editable list. A new reference file or script
   is allowed; a new agent, a nested reference directory, or a file
   elsewhere is not.
2. The skill and the three agent files must be present.
3. `SKILL.md` keeps `name: research-paper` and a `description:` in its
   frontmatter, and its body stays under 500 lines.
4. Each agent file keeps `name:` equal to its filename and a
   `description:`. Its `tools:` and `model:` lines are frozen: they must
   equal the base tree's.
5. A reference the skill names as `references/<name>.md` must be in the
   tree (the rubric and model levels may be named without being shipped).
   A script any file invokes as `scripts/<name>.py` or `.sh` must be in
   the tree.
6. Every `.py` compiles; every `.sh` passes `bash -n`.
7. No forbidden phrase from `harness.yaml` appears anywhere (phrases that
   aim at the evaluator instead of the work).
8. No emoji or decorative symbol anywhere.

An invalid candidate gets one retry with the error list, then falls back
to the base tree and is recorded as such.

## How components are reached at run time

- The orchestrator reads `SKILL.md` when the user invokes the skill. A
  reference file is read only when a step names it, so a new reference
  must be named from the step where it applies or it is dead weight.
- An agent reads its own file at spawn time and nothing else of the tree
  unless its instructions name a path.
- Scripts run as `python3 .claude/skills/research-paper/scripts/<name>.py
  <args>` from the repository root. They receive paths, never pasted
  content, and exit non-zero with a message on failure.
- Reference files are one level deep: `SKILL.md` names a reference, a
  reference does not name another reference.

## What a good edit looks like

- A sentence in the step where the divergence happened, not a new section
  at the end.
- A check the agent can run and whose failure it can act on.
- A reference file with a trigger line in the skill, carrying knowledge
  that applies whenever that trigger fires.
- A script that replaces a repeated manual check, with its invocation
  named in the step that needs it.

What a bad edit looks like: restating the rubric, hedging language, a rule
for one paper's facts written as if universal, or a paragraph that tells
the agent to be careful.

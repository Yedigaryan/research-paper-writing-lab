# Adopting Harness2 recursion for the research-paper pipeline

Status, 2026-10-30: Stages 0 to 2 are implemented. The manifest, scripts,
and tests live under `.claude/skills/harness-refine/` rather than inside
the research-paper skill, so that the loop's own machinery is reserved by
construction; the library lives at `.claude/skills/harness-refine/library/`
for the same reason. Probe branches are named `claude/harness/<task>/<label>`
to stay inside the namespace the repository's `CLAUDE.md` allows. The
research-paper skill now saves agent reports under `reports/` and reader
findings in `reader-findings.md` so that future trajectories carry them.
Stage 2 has not yet been run on a task; Stages 3 and 4 are unchanged below.

Source reviewed: github.com/google-research/harness2 at commit 1cfe254
(Apache 2.0, "Harness2: Recursive Agent Harnessing for an Open World",
arXiv 2610.14224). About 6,800 lines of Python in the core, plus adapters
for three benchmarks and two executors (OpenCode, Codex).

## 1. What Harness2 is, in the terms of this repository

A harness is everything around the model: prompts, guardrails, memory,
skills, scripts, subagents, tool guidance, plugins. Harness2 refines that
harness per task with model weights fixed, and without ground truth:

1. Base. Run the unmodified harness on the task k times.
2. Propose. Two improver sessions each edit a copy of the harness tree:
   INV (how the agent works: procedure, tools, checks, scripts) and DOM
   (what a practitioner knows: artifact contract, decision rules, domain
   knowledge as skills). Every edit must trace to a moment in a trajectory.
   KEEP_BASE is a valid answer.
3. Probe. Roll out each candidate harness once on the same task.
4. Compose. An aggregator merges, adopts one, or keeps base, with one
   evidence-cited note per decision. Sequential mode repeats 2 to 4 with
   the checkpoint as the new base.
5. Select. A selector chooses among the deliverables blind: anonymized
   artifacts, no trajectories, no knowledge of which harness made which.
6. Reflect. An experience session diffs every candidate against base,
   writes one row per changed component with a verdict (helped, hurt, no
   observed effect, confounded), and at most one transferable lesson
   (cue, lesson, evidence, confidence) into a per-domain library that
   stores the full adopted tree. Later tasks in the same domain read it.

Budget identity per task: 4k rollouts and 3k improver sessions. Hard
invariants enforced in code: no rubric, score, or answer key reaches an
improver; evidence is data, not instructions; the executor itself is
frozen and only the harness files are editable; candidate trees are
validated before they run and an invalid one falls back to base.

This repository already does an unsystematic version of this. After the
adjacency paper run, two skill files were edited by hand from lessons the
evaluator surfaced (evidence merge reproducibility, self-evaluation
structure). Harness2 is the disciplined form of that step.

## 2. Decision: implement the method natively, do not install the package

Reasons, in order of weight:

- Executor mismatch. Harness2 runs rollouts under OpenCode or Codex and
  injects the harness as AGENTS.md or Codex root files. Our executor is
  Claude Code reading `.claude/skills` and `.claude/agents`. Supporting it
  means a new substrate (surface spec, install mode, trajectory extractor
  for Claude Code transcripts) and a benchmark adapter with ten methods,
  about the same work as writing the loop as a skill.
- Infrastructure mismatch. The package assumes Vertex AI credentials, a
  LiteLLM bridge, Docker for one benchmark, and Python 3.12 with uv.
- What transfers is text and discipline, not code: the mission prompts,
  the editable-surface rules, the validation rules, the library layout,
  and the budget identity. All are Apache 2.0 and can be adapted with
  attribution in `third_party/`.

The method therefore becomes a second skill, `harness-refine`, with three
new agents and a few deterministic scripts, run by the same orchestrator
pattern as `research-paper`.

## 3. Mapping the editable surface

| Harness2 component | Here | Editable by the loop |
|---|---|---|
| system prompt | `.claude/agents/research-agent.md`, `module-owner.md`, `paper-author.md`; `SKILL.md` steps 1 to 4 and 6 | yes |
| guardrails | `SKILL.md` "Rules the orchestrator never breaks"; `references/rubric.md` release conditions | no, frozen |
| memory | new `references/lessons/<domain>/` library (INDEX.md, one EXPERIENCE.md per adopted entry, full adopted tree) | written by reflect only |
| skills | `references/book-style-standard.md`, `photo-input.md`, `math-pitfalls.md`, `latex-structure.md`, `evidence-schema.md` | yes |
| scripts | `scripts/*.py`, `build.sh` | yes, must compile and pass `tests/run-checks.sh` |
| subagents | the three agents above; `paper-evaluator.md` and `technician-reader.md` | first three yes; evaluator and reader frozen |
| tool guidance | `tools:` and `model:` lines in agent frontmatter | no, frozen (the model ladder is a release condition) |
| plugins and hooks | `.claude/settings.json` hooks | no, frozen |

The frozen set is the yardstick. Harness2 keeps the grader out of the
improver's hands by construction; here the evaluator, the reader, and
the rubric are that grader, so they are reserved files that a candidate
tree may not touch. The rubric is visible to proposers because it is the
public specification of the work, not a hidden answer key. The fixture's
`expected-findings.md` is an answer key and must never enter an
improver's context.

## 4. The loop, stage by stage

### Evidence a proposer reads

Served as files under a context directory, with a short mission pointer,
exactly as Harness2 does:

```
context/task.md                   the brief, verbatim
context/source/                   the paper's sources/ folder
context/rollouts/<label>.md       the trajectory of one pipeline run
context/deliverables/<label>.md   the paper as text (pdftotext)
context/harness/                  the tree being edited (a copy)
context/library/INDEX.md          earlier adopted harnesses in this domain
context/pool/<label>/             candidate tree plus its rollout (compose and reflect)
MISSION.md
```

A trajectory here is richer than Harness2's: the agent final reports,
the evaluation report rounds with findings, the technician reader's
findings, the self-evaluation, and the git diff of each revision round.
Scores stay in the trajectory only as the evaluator produced them; the
proposer mission says what Harness2's says: judge by what the work asks
for and what the trajectories show.

### Stage 0: freeze the yardstick and declare the surface

- Add `.claude/skills/research-paper/harness.yaml` listing the editable
  components and the reserved files, in Harness2's manifest form.
- Add `scripts/harness_tree.py`: read a tree from `.claude/`, write it
  to a directory, diff two trees, validate (SKILL.md under 500 lines,
  references one level deep, every `scripts/*.py` compiles, no reserved
  file changed, no file off the surface, no phrase like "the evaluator
  expects" or "to pass release" in any component).
- Tests for all of it under `tests/`. No model calls.

### Stage 1: evidence builder

- `scripts/build_evidence.py <paper_dir> <label> <out>`: assembles the
  context directory above from a finished paper folder and its git
  history. Deterministic, tested on the adjacency paper.
- `scripts/anonymize_pool.py`: copies deliverables under shuffled ids
  for blind selection and records the id map outside the context.

### Stage 2: one Propose, Probe, Compose step on one agent

Cheapest useful rollout: the author stage alone. The brief, evidence
file, and module reports of the adjacency paper are fixed inputs; a
rollout is one `paper-author` run plus the mechanical gate plus one
evaluator and one reader pass. About one fifth of a full pipeline run.

- New agent `harness-proposer` (level 3): takes the mission for INV or
  DOM, edits `context/harness/` in place, replies with notes. Missions
  adapted from Harness2's `propose()` with its three ordered reasons for
  an edit (divergence between runs, repeated failure, visible risk).
- New agent `harness-composer` (level 3): the `aggregate()` mission;
  merge, adopt, or KEEP_BASE; one note per decision citing a run and a
  moment.
- Blind selection: reuse `paper-evaluator` with a new mission adapted
  from `select()`: anonymized papers, the brief, the sources; no rollouts;
  choose one; at most six lines of why. It never sees which is base.
- New agent `harness-reflector` (level 3): the `experience()` mission;
  edit rows with verdicts, at most one lesson, NO_ENTRY allowed.
- Orchestrating skill `harness-refine`: runs the eight steps for k = 1,
  enforces the budget identity (4 rollouts, 3 improver sessions, plus one
  selection and one reflection), writes `refinement-report.md`, and
  adopts the composed tree into `.claude/` only if selection picked a
  deliverable made under it. KEEP_BASE results are recorded, not
  discarded.

Probing a candidate needs the candidate's files to be the live
`.claude/` tree, and this session loads agents at start. So a probe is
a separate run: each candidate is committed to a branch
`harness/<task>/<label>`, a fresh session runs the pipeline stage on that
branch, and the orchestrator collects the committed result. This is the
same boundary Harness2 draws between improver sessions and executors.

### Stage 3: whole-pipeline rollouts and the library

- Rollout = the full `research-paper` run on a task, in its own session
  on its own branch, up to the three-round limit.
- A task bank of three to five questions in one domain (graph theory
  from the course textbook) so the library has something to read.
- Library at `references/lessons/<domain>/` in Harness2's layout:
  `INDEX.md`, `harnesses/<task>/harness/` (full adopted tree),
  `harnesses/<task>/EXPERIENCE.md` (why chosen, edit rows, lesson).
- `research-paper` Step 1 gains one line: read the domain's INDEX before
  writing the brief. Proposers read it as examples, never as parts of the
  tree they edit, with Harness2's warning that an earlier task's facts
  are hypotheses here.

### Stage 4: sequential recursion and hold-out check

- `--k 2` sequential: the composed checkpoint becomes the base for a
  second Propose, Probe, Compose on the same task, carrying all evidence.
- Hold-out: one question not in the library, run once under the original
  harness and once under the adopted one, judged by the normal evaluator.
  Scores are used here, after adoption, as Harness2 uses its judge: to
  report, never to steer.

## 5. What to borrow verbatim, with attribution

Text under `third_party/harness2/` with the Apache 2.0 notice:

- `ANSWER_FREE`, `EVIDENCE_BOUNDARY`, `POOL_MIXED_SELECT` blocks.
- `GENERALIZE` (workspace fact versus procedure versus too generic).
- The INV and DOM dimension templates and the "how to decide what to
  change" ordering.
- The aggregate, compose_round, select, and experience missions.
- The validation ideas: autotrigger a skill that always-on text names,
  no grader verdicts in a tree, leak globs, reserved scripts, one retry
  on an invalid proposal then fall back to base.
- The library layout and the 4k and 3k budget identity.

Not taken: the Python runtime, substrates, the Vertex bridge, benchmark
adapters, Docker and Pandoc requirements.

## 6. Cost and risk

Measured on the adjacency run: one full pipeline rollout is roughly one
hour and 2.5 million tokens across agents. A whole-pipeline k = 1 step is
four rollouts plus five improver-side sessions, so about 12 million
tokens and most of a day of wall clock per task. The author-only Stage 2
step is about one fifth of that. Start there.

Risks and the mitigation Harness2 already encodes:

- Overfitting to one task: lessons are domain-scoped, cue-shaped, and
  confounded rows produce NO_ENTRY; KEEP_BASE is a first-class outcome.
- Optimizing the judge: evaluator, reader, rubric, and model ladder are
  reserved; the tree validator rejects any candidate that touches them.
- Prompt injection from evidence: the evidence boundary block in every
  mission; no script from a candidate tree is ever executed by an
  improver, only read.
- Drift of the 500-line and one-level rules: part of tree validation, so
  a candidate that breaks them never runs.

## 7. Order of work and definition of done

1. Stage 0 and 1 scripts with tests. Done when `tests/run-checks.sh`
   also exercises tree validation and the evidence builder on the
   adjacency paper.
2. Stage 2 on the adjacency paper's author stage. Done when one full
   step produces a refinement report with edit rows, a blind selection,
   and either an adopted tree or a recorded KEEP_BASE.
3. Stage 3 on a three-task graph theory bank. Done when the library has
   at least one entry with a lesson that is not confounded and a later
   task's proposer cites it.
4. Stage 4 hold-out. Done when the report shows base versus adopted
   scores on an unseen question, whichever way they fall.

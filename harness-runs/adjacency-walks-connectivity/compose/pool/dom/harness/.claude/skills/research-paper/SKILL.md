---
name: research-paper
description: Turn a research question, topic, document, dataset, source file, or set of photos (lecture whiteboards, handwritten notes, textbook pages) into an evidence-based research paper in LaTeX with a compiled PDF, a BibTeX bibliography, and an independent evaluation report. Use when the user asks to research a topic, answer a technical question with sources, write up lecture material as a paper or study note, or check an existing paper in this repository against its sources and evidence.
---

# Research Paper

Orchestrates a pipeline of specialized agents that research a question,
establish evidence for every claim, write the paper in LaTeX, evaluate it
independently, and release it only when the mandatory conditions pass.

The session running this skill is the orchestrator. It talks to the user,
writes the research brief, spawns the agents, merges their outputs, applies
the release conditions, and writes the evaluation report. It never writes
paper prose itself; the author agent owns the paper.

Standard for the finished paper: every meaningful claim is understandable,
every factual claim has appropriate supporting evidence, and every
conclusion is justified. The reader is technically literate at technician
level with no prior knowledge of the topic.

## Roles

| Role | Where it runs | Model level | Reads | Writes |
|---|---|---|---|---|
| Orchestrator | this session | session model | everything | `brief.md`, `evaluation-report.md` |
| `research-agent` | agent | 2 | brief, inputs, web | `evidence/evidence.json` |
| `module-owner` | agent, one per module, parallel | 2 | brief, evidence, web | `modules/<id>.md`, `evidence/modules/<id>.json` |
| `paper-author` | agent, kept alive across revisions | 2 | brief, evidence, modules | `main.tex`, `sections/`, `references.bib`, `self-evaluation.md` |
| `paper-evaluator` | agent, fresh each round | 3 | paper, brief, evidence, rubric | nothing; returns findings |
| `technician-reader` | agent | 2 | compiled paper text | nothing; returns unclear passages |

Model levels are defined in `references/model-levels.md`. The evaluator
must sit at least one level above the author and every module owner. The
orchestrator records the configured levels in the evaluation report and
marks the hierarchy requirement unmet if the evaluator could not run at the
configured level.

Agent definitions live in `.claude/agents/`. Each agent is given file paths,
not pasted content, and reads what it needs itself. Agents return a short
report; everything that must survive goes to disk in the paper folder.
Save every agent's final message verbatim to
`papers/<slug>/reports/<agent-name>-round<n>.md` (round 0 for research and
modules) so that a later refinement step can read the run as it happened.

## Paper folder

Every paper lives in `papers/<slug>/`. Create it with:

```
python3 .claude/skills/research-paper/scripts/new_paper.py <slug> --question "<question>"
```

Layout, file formats, and the LaTeX conventions are in
`references/latex-structure.md`. The evidence file format is in
`references/evidence-schema.md`. There is exactly one evidence file per
paper, `evidence/evidence.json`; module fragments under `evidence/modules/`
are staging only and are merged into it by script.

## Step 1: Analyze the input (orchestrator)

Inspect everything the user supplied: text, images, PDFs, documents, code,
datasets, tables, papers. Read images and PDFs directly. Copy supplied files
into `papers/<slug>/sources/` with descriptive names.

For photos of whiteboards, handwritten notes, or book pages, follow
`references/photo-input.md` before anything else: transcribe, separate the
clearly visible from the inferred from the unreadable, and report mismatches
between diagrams and formulas instead of picking a side.

If `.claude/skills/harness-refine/library/<domain>/INDEX.md` exists for
the paper's domain, read it and the `EXPERIENCE.md` of any entry whose cue
matches this task before writing the brief. A stored lesson may shape the
module plan or an assumption; it is never evidence for a claim.

Then write `brief.md` with these sections:

1. Research question, in one sentence, and where it came from.
2. Objectives: what the paper must answer or show.
3. Scope and exclusions.
4. Audience register: `technician` (default) or `study-note` (adds the plain
   words layer and the textbook standard; see `references/photo-input.md`).
5. Input inventory: each supplied file, what it contains, how reliable it is.
6. Allowed research sources. Web search is the default. If the user supplied
   documents, say whether they are the only allowed sources, the primary
   sources, or context. If this is unclear, ask before research starts.
7. Assumptions, each with the reason it was made.
8. Open questions for the user.
9. Proposed modules: two to five named subtopics with one line each on what
   the module must establish, and the dependencies between them.
10. Deliverables and any user constraints (length, citation style, deadline).

Ask the user when essential information is missing or the question has two
readings that lead to different papers. Ask one focused question at a time
and offer the assumption you will use if they do not know. When the gap is
minor, record the assumption in the brief and proceed. End the turn after
asking; do not start research with an open question that changes scope.

## Step 2: Research (research-agent)

Spawn `research-agent` with the path to `brief.md`. It produces
`evidence/evidence.base.json` holding every source found, its credibility
and access status, the claims each source supports with exact locators,
and contradictions between sources. It does not write prose.

When it returns, build the merged file and check it:

```
cp papers/<slug>/evidence/evidence.base.json papers/<slug>/evidence/evidence.json
python3 .claude/skills/research-paper/scripts/check_claims.py papers/<slug>
```

Fix schema errors by sending the agent back with the error output. Read the
contradictions list and decide whether any of them changes the module plan.

## Step 3: Modules (module-owner, parallel)

Spawn one `module-owner` per module in the brief, all in one message so
they run in parallel. Each gets the brief path, its module id, and the
evidence path. Each writes `modules/<id>.md` (explanation from first
principles, derivations, worked examples, assumptions, limitations,
dependencies on other modules) and `evidence/modules/<id>.json` (new
sources and the claims the module makes, each tied to support).

When all return, rebuild the merged file from the base file and the
fragments, then check it. Always rebuild from the base file so that a
second merge never duplicates claims:

```
cp papers/<slug>/evidence/evidence.base.json papers/<slug>/evidence/evidence.json
python3 .claude/skills/research-paper/scripts/merge_evidence.py papers/<slug>
python3 .claude/skills/research-paper/scripts/check_claims.py papers/<slug>
```

Read every module report once. Look for gaps between modules, terms used
with two meanings, and assumptions that conflict. Resolve each by sending
the owning agent a message with the specific conflict. Do not resolve it by
editing the report yourself.

## Step 4: Draft (paper-author)

Spawn `paper-author` with the brief, the evidence file, and the module
reports. It writes the LaTeX paper, compiles it with the build script,
runs the citation and claim checks, and writes `self-evaluation.md`:
section by section, what the section claims, which evidence supports each
claim, and which conclusions follow from what. Keep this agent alive for
revisions; it is the author and must be able to explain every line.

The author may not introduce a claim that is not in the evidence file. A
claim it finds necessary and cannot source goes into the evidence file as
`unverified`, is qualified in the text, and is listed in the self
evaluation.

After it returns, run the mechanical gate yourself:

```
bash   .claude/skills/research-paper/scripts/build.sh papers/<slug>
python3 .claude/skills/research-paper/scripts/check_citations.py papers/<slug>
python3 .claude/skills/research-paper/scripts/check_claims.py papers/<slug>
python3 .claude/skills/research-paper/scripts/inspect_pdf.py papers/<slug>
```

Any failure goes back to the author before evaluation. The evaluator's time
is the most expensive in the pipeline; never spend it on a paper that does
not compile.

## Step 5: Independent evaluation (paper-evaluator, technician-reader)

Spawn a fresh `paper-evaluator` with the paths to the paper folder, the
brief, the evidence file, and `references/rubric.md`. Do not give it
`self-evaluation.md`, the module reports, or your own opinion. On a second
or later round, also give it the previous `evaluation-report.md` so it can
verify that earlier findings were resolved; that report is the
orchestrator's record, not the author's self assessment.

In the same message spawn `technician-reader` with the paper folder path.
It reads the compiled text as a reader who knows nothing about the topic
and returns the exact passages it could not follow.

Both agents return findings in the format fixed in `references/rubric.md`:
one score per dimension with the observation behind it, and a list of
findings each with severity, location, the defect, and the correction.

Why a fresh evaluator each round: it matches the independence requirement
literally and cannot be anchored by its own earlier scores. The cost is a
full re-read per round. If evaluation rounds regularly exceed three, or the
fresh evaluator keeps re-raising findings the previous report marks as
resolved, switch to messaging the same evaluator and record the change in
`references/model-levels.md`. Start with the fresh evaluator.

## Step 6: Record, decide, revise (orchestrator)

Write or append to `evaluation-report.md` using the template in
`references/rubric.md`: round number, configured model levels, scores,
findings with severity and status, mechanical check results, and the
decision for this round. Never overwrite a previous round. Append the
technician reader's findings for the round to `reader-findings.md`.

Apply the release conditions from `references/rubric.md`. If any fails:

1. Group the findings by section and send them to the living `paper-author`
   agent. A finding that needs new research goes to the owning
   `module-owner` first, then to the author.
2. Require the author to update `self-evaluation.md` for every changed
   section.
3. Re-run the mechanical gate from Step 4.
4. Return to Step 5.

Critical and major findings must be resolved. Minor findings are resolved
or documented in the report with the reason. A finding is resolved when the
next evaluator confirms it, not when the author says so.

If three rounds pass without reaching release, stop. Report to the user
which conditions still fail and why, with the decision `INCOMPLETE`. Never
force a pass.

## Step 7: Release

When every release condition passes, write the final round in
`evaluation-report.md` with decision `PASS`, make sure `README.md` in the
paper folder states how to compile, and commit the folder with a clear
message. Push according to the repository's `CLAUDE.md` git rules.

Report to the user: the question as interpreted, the modules, the scores,
unverified claims and source access limits, known limitations, and the
model levels used.

## Checking an existing paper

When asked to check a paper already in the repository, skip Steps 2 to 4.
Write a brief from the paper's own stated question and assumptions, run the
mechanical gate if the paper is LaTeX, then run Step 5 and write the report.
For a Markdown paper written from photos, add the photo checks in
`references/photo-input.md`. Do not rewrite the paper unless asked.

## Testing the pipeline

`tests/README.md` describes the fixture paper with planted defects and the
findings the evaluator must raise. Run the mechanical checks against the
fixture with `tests/run-checks.sh`; they must fail. Run Step 5 on the
fixture after any change to an agent definition or the rubric and compare
the findings with `tests/fixtures/defective-paper/expected-findings.md`.

## Rules the orchestrator never breaks

- No fabricated citations, quotations, measurements, metadata, or results,
  anywhere in the pipeline. A source that cannot be accessed is recorded
  with its access status, not implied verified.
- The evaluator never sees the author's self evaluation.
- Scores come from findings. A score is never raised to meet a threshold.
- A compile success is not a quality result. A high score in one dimension
  never offsets a critical defect in another.
- Clean text in all deliverables: no emojis, no decorative symbols.
- Commit with clear messages. Push only as the repository's `CLAUDE.md`
  git rules allow; never to a branch outside `claude/*` without the user.

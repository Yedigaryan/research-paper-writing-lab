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
level with no prior knowledge of the topic. The paper is as long as the
question needs and no longer: the brief sets a page budget, and material
that does not serve the question is a defect.

## Roles

| Role | Where it runs | Model level | Reads | Writes |
|---|---|---|---|---|
| Orchestrator | this session | session model | everything | `brief.md`, `evaluation-report.md` |
| `research-agent` | agent | 2 | brief, inputs, web | `evidence/evidence.json` |
| `module-owner` | agent, one per module, parallel | 2 | brief, evidence, web | `modules/<id>.md`, `evidence/modules/<id>.json` |
| `paper-author` | agent, kept alive across revisions | 2 | brief, evidence, modules | `main.tex`, `sections/`, `references.bib`, `self-evaluation.md` |
| `paper-evaluator` | agent, fresh each round | 3 | paper, brief, evidence, rubric | nothing; returns findings |
| `technician-reader` | agent | 1 | compiled paper pages | nothing; returns unclear passages |

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
into `papers/<slug>/sources/` with descriptive names. When the paper will
rest on something the user only said or typed (a convention, a question,
an assignment they did not attach), save their words verbatim with the
date in `sources/user-statements.md` and list it in the input inventory,
so agents can quote and cite it as a `local-file` source. If only a
summary of their words is available, the file says it is a summary and
nobody quotes it.

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
2. Objectives, in two lists. "Needed to answer": what the paper must
   contain for the question to be answered; nothing else goes here.
   "Optional": related material that is written only if the page budget
   allows; the list may be empty. A concept the answer does not use, a
   second method, a comparison of sources, and a history of the topic are
   optional unless the user asked for them.
3. Scope and exclusions.
4. Audience register: `technician` (default) or `study-note` (adds the
   textbook standard; see `references/photo-input.md`). Then one line,
   `Analogies: no` or `Analogies: yes`. The default is `no`. Write `yes`
   only when the user asks for analogies, a story, or plain-words
   explanations; it adds the plain words layer of `photo-input.md` in
   either register.
5. Input inventory: each supplied file, what it contains, how reliable it is.
6. Allowed research sources. Web search is the default. If the user supplied
   documents, say whether they are the only allowed sources, the primary
   sources, or context. If this is unclear, ask before research starts.
7. Assumptions, each with the reason it was made.
8. Open questions for the user.
9. Proposed modules: one to five named subtopics, as few as cover the
   needed objectives, with one line each on what the module must
   establish and the dependencies between them. Name the objectives each
   module serves; an optional objective is marked optional there too.
10. Deliverables and constraints. The first line is `Page budget: <n>`,
    the largest number of pages `main.pdf` may have, references and
    appendices included, in the template's format. Then any user
    constraints (citation style, deadline).

Setting the page budget: a length the user gave wins. Otherwise count what
the needed objectives require: about half a page for each definition or
result with its proof, one page for each worked example, and one page for
the introduction and the references together; round up. A question a
lecturer answers on one board comes to three to six pages. Write the count
next to the number. The budget is a ceiling, not a target, and
`inspect_pdf.py` fails a paper that exceeds it. If the author reports that
a needed objective cannot be written in full within it, raise the number
in the brief and say why; never let a proof be cut to fit.

Ask the user when essential information is missing or the question has two
readings that lead to different papers. Ask one focused question at a time
and offer the assumption you will use if they do not know. When the gap is
minor, record the assumption in the brief and proceed. End the turn after
asking; do not start research with an open question that changes scope.

## Step 2: Research (research-agent)

Spawn `research-agent` with the path to `brief.md`. It produces
`evidence/evidence.base.json` holding the sources the objectives need,
their credibility and access status, the claims each source supports with
exact locators, and contradictions between sources that bear on a needed
objective. It does not write prose.

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
evidence path. Each writes `modules/<id>.md` (what the needed objectives
of the module require: explanation from first principles, derivations, a
worked example, assumptions, limitations, dependencies on other modules)
and `evidence/modules/<id>.json` (new sources and the claims the module
makes, each tied to support).

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
reports. It writes the LaTeX paper within the page budget, compiles it
with the build script, runs the citation and claim checks, and writes
`self-evaluation.md`:
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

`inspect_pdf.py` reads the page budget from `brief.md` and fails a paper
that is over it. When the brief says `Analogies: yes` also run
`python3 .claude/skills/research-paper/scripts/check_plain_words.py papers/<slug>`;
its errors are failures, and its warnings go to the author with the next
batch of findings.

Any failure goes back to the author before evaluation. The evaluator's time
is the most expensive in the pipeline; never spend it on a paper that does
not compile.

## Step 5: Independent evaluation (paper-evaluator, technician-reader)

Spawn a fresh `paper-evaluator` with the paths to the paper folder, the
brief, the evidence file, and `references/rubric.md`. Do not give it
`self-evaluation.md`, the module reports, or your own opinion. On a second
or later round, also give it the previous `evaluation-report.md` so it can
verify that earlier findings were resolved, `reader-findings.md` so it
can judge the reader's passages, and `source-checks.md` with the output of

```
python3 .claude/skills/research-paper/scripts/claims_changed.py papers/<slug>
```

so that it fetches sources only for claims that changed and for checks
that did not hold; see "Source checks across rounds" in the rubric. All of
these are the orchestrator's record, not the author's self assessment.

In the same message spawn `technician-reader` with the paper folder path.
It reads the compiled pages as a reader who knows nothing about the topic
and returns the exact passages it could not follow.

The evaluator returns the format fixed in `references/rubric.md`: one score
per dimension with the observation behind it, and a list of findings each
with severity, location, the defect, and the correction. The reader returns
only comprehension findings and a summary paragraph, with no severity and
no score. The orchestrator never assigns a severity to a reader finding.
Severity is a judgment about the paper and belongs to the evaluator alone;
a reader passage becomes a graded finding only when an evaluator raises it
as its own.

Why a fresh evaluator each round: it matches the independence requirement
literally and cannot be anchored by its own earlier scores. The cost is a
full re-read per round. If evaluation rounds regularly exceed three, or the
fresh evaluator keeps re-raising findings the previous report marks as
resolved, switch to messaging the same evaluator and record the change in
`references/model-levels.md`. Start with the fresh evaluator.

## Step 6: Record, decide, revise (orchestrator)

Write or append to `evaluation-report.md` using the template in
`references/rubric.md`: round number, configured model levels, scores, the
evaluator's findings with severity and status, mechanical check results,
and the decision for this round. Never overwrite a previous round. Append
the technician reader's findings and summary for the round to
`reader-findings.md` exactly as returned, ungraded; they do not enter the
findings table of the evaluation report. If the summary paragraph does not
match the paper's actual conclusion, note that next to it in plain words,
without a severity.

Append the evaluator's CITATION SPOT CHECKS block for the round to
`source-checks.md` as returned, under the round number, and record which
claims that round saw:

```
python3 .claude/skills/research-paper/scripts/claims_changed.py papers/<slug> --record <n>
```

Apply the release conditions from `references/rubric.md`. They are decided
by the evaluator's findings and scores, never by reader findings.

If conditions 1 to 9 hold and no critical or major finding is open, the
round passes even when minor findings remain. Do not run another
evaluation for them. Follow "Final edits" in the rubric: send the minor
findings and the reader's findings to the author, read the diff when it
returns, confirm that it touches only the passages those findings name and
adds no claim, citation, changed statement, or changed proof step, re-run
the mechanical gate from Step 4, record the final edits in the report, and
go to Step 7. If the diff goes further than that, run another round.

If a condition fails or a critical or major finding is open:

1. Group the evaluator's findings by section and send them to the living
   `paper-author` agent, with the reader's findings attached as advisory:
   the author changes the passage or says in `self-evaluation.md` why it
   stays, and the next round records that response in `reader-findings.md`.
   A finding that needs new research goes to the owning `module-owner`
   first, then to the author.
2. Require the author to update `self-evaluation.md` for every changed
   section.
3. Re-run the mechanical gate from Step 4.
4. Return to Step 5.

Critical and major evaluator findings must be resolved. Minor findings are
resolved or documented in the report with the reason. A critical or major
finding is resolved when the next evaluator confirms it, not when the
author says so. A finding whose correction is `cut` or `shorten` is
handled like any other; the author never answers a finding by adding text
that pushes the paper over its page budget. The
orchestrator never holds a release on a reader finding that no evaluator
raised as its own.

If three rounds pass without reaching release, stop. Report to the user
which conditions still fail and why, with the decision `INCOMPLETE`. Never
force a pass.

## Step 7: Release

When every release condition passes, write the final round in
`evaluation-report.md` with decision `PASS`, make sure `README.md` in the
paper folder states how to compile, and commit the folder with a clear
message. Push according to the repository's `CLAUDE.md` git rules.

Report to the user: the question as interpreted, the modules, the page
count against the budget, the scores, unverified claims and source access
limits, any findings closed by final edits that no evaluator re-read,
known limitations, and the model levels used.

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

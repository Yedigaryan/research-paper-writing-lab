# Refinement report: adjacency-walks-connectivity

Task: adjacency-walks-connectivity, stage author, k = 1, mode agg
Base commit: aa7511e949c23d01e5b76ebdb28ee4b909899759
Dates: 2026-10-30 to 2026-11-02
Domain: graph-theory

## Budget

| Item | Allowed | Used |
|---|---|---|
| Rollouts | 4k = 4 | 4: base (existing run), inv, dom, composed probes |
| Improver sessions | 3k = 3 | 3: INV proposer, DOM proposer, composer |
| Selection sessions | 1 | 1 |
| Reflection sessions | 1 | 1 |

No validation retries were needed.

## Candidates

| Label | Dimension | Validation | Tree diff vs base | Probe branch | Deliverable |
|---|---|---|---|---|---|
| base | none | valid | none | none (existing run) | first draft 36 pages (commit 7adfc9d); final 39 pages after 3 rounds |
| inv | INV | valid | 3 scripts added; SKILL.md, paper-author.md, evidence-schema.md, latex-structure.md, inspect_pdf.py modified | claude/harness/adjacency-walks-connectivity/inv | 32 pages, 1 round |
| dom | DOM | valid | graph-sources.md added; module-owner.md, paper-author.md, book-style-standard.md, quality-checklist.md modified | claude/harness/adjacency-walks-connectivity/dom | 29 pages, 1 round |
| composed | compose | valid | 1 reference and 3 scripts added; 8 files modified | claude/harness/adjacency-walks-connectivity/composed | 30 pages, 1 round |

## Proposer notes

The verbatim notes are in the run's ignored working files
(`propose/inv/NOTES.md`, `propose/dom/NOTES.md`). Summary:

- inv: three new check scripts (`check_evidence_rebuild.py`,
  `check_self_evaluation.py`, `check_round_record.py`), a `--text-out`
  option for `inspect_pdf.py`, a compiled-text read before the
  self-evaluation, a four-step revision procedure for the author, and a
  per-file self-evaluation layout. Traced to base E18, E25, E26, the
  round 3 partial release condition 9, and the errors introduced during
  revision rounds (E12, E19 to E23).
- dom: a new reference `graph-sources.md` of verified textbook locators
  and source attributions; a pointer to it in paper-author and
  module-owner; a rule against invented bracketed status labels in
  book-style-standard; nine new checklist items on sources, notation, and
  writing. Traced to base E1 to E4, E12, E14, E15, E20, E21, and the tag
  findings R2, R25, R52.

## Composer notes

Verbatim in `compose/NOTES.md` (ignored). The composer kept all of INV's
procedure edits and DOM's `graph-sources.md`, revised three of its
entries (Proposition 2.9.10 scope, the Kirchhoff page, the Fig. 1.2.5
edge list) and added evaluator-verified attribution facts, kept two of
DOM's checklist items, dropped the other seven because DOM's own rollout
repeated the failures they name, and removed "supplied by the user" from
the bibliography rule in latex-structure.md. 9 kept, 5 revised, 6 dropped.

## Selection

Pool: base first draft, inv, dom, composed, anonymised as cand-a to
cand-d (map in `pool-map.json`). Selector: paper-evaluator, level 3,
given task.md, source/ (two whiteboard photos and the course textbook),
and candidates/ only.

The base entry is the base run's first draft, not its final paper,
because each probe is one author pass with no revision. The selector
was told that every candidate came from one author pass with no
revision.

Reasoning verbatim in `selection.md`. Decided on fidelity and finish:
only the dom and composed drafts give every textbook number and page
correctly, verified against page images; the base draft leaves about 80
internal tags in the reader's text; the inv draft says the textbook's
degree definition was not read. The composed draft lost to dom on
internal consistency (n and m clash with N and the exponent m; a
conclusion cites the wrong remark).

Choice: cand-a = dom. Runner-up: cand-b = composed.

## Reflection

Verbatim in `reflection.md`. Twelve edit rows: one helped, four
confounded, seven no observed effect.

- helped: `graph-sources.md`. The textbook degree definition was cited in
  both runs that had the file and missed in both that did not; the dom
  author names the file as the reason. A wrong entry in dom's version
  propagated into the dom paper (F9); composed's corrected entry did not.
- confounded: the compiled-text read in `inspect_pdf.py`, the
  quality-checklist items, the book-style rule on status labels, and the
  bibliography wording in latex-structure.md.
- no observed effect: the three new scripts, the SKILL.md gate and
  record changes, the author revision procedure, the module-owner
  pointer, and the evidence-schema pointer. No probe ran a revision round
  or a module owner, so most of these were never exercised.

Lesson (confidence low): when a paper must cite a fixed primary source by
its own numbers and pages, record evaluator-verified locators and scopes
in a triggered reference file named from the author and module-owner
files, copy each entry with its exact scope, and check every entry
against its finding before adopting the file.

## Decision

Adopted: dom.
Installed into .claude/: yes, in the commit that adds this report.
Library entry: `.claude/skills/harness-refine/library/graph-theory/harnesses/adjacency-walks-connectivity/`.
tests/run-checks.sh after install: pass.

### Known issue in the adopted tree

`references/graph-sources.md`, line 63, says Proposition 2.9.10 is "the
walk, trail, path equivalence". The dom evaluator found that it covers
only walks and paths (dom F9), and the composer's version corrects the
entry. The decision rule adopts the selected tree unchanged and the
orchestrator never edits a candidate tree, so the entry was installed as
it is. It needs a one-line fix before the next graph theory paper. The
corrected wording is in the composed tree on branch
`claude/harness/adjacency-walks-connectivity/composed`.

Fixed after adoption: the entry now carries the composed wording, in
the live tree and in the library copy, at the user's request.

### Confounds and process notes

- One rollout per candidate; selection compares four single drafts.
- The composed probe's orchestrator session ran on a different session
  model from the inv and dom probes. The author, evaluator, and reader
  agents are pinned in their files and were the same in every probe.
- The base first draft was produced before the evidence base-file fix,
  from the same 77 claims; the probes started from a rebuilt merged file.
- A container restart lost `compose/`. It was rebuilt from the composed
  probe branch (identical tree) and the composer notes were recovered
  from its transcript.
- The reflector was given `compose/`, whose `harness/` the composer had
  edited in place, and reconstructed the base itself. SKILL.md Step 6 now
  hands the reflector `context/` instead.
- Probe collection first included the reset commit in each trajectory;
  SKILL.md and probe-prompt.md now start the history after it.

## Evaluator scores, for the record only

Reported after the decision, never used to steer it. Round 1 scores of
each run's first draft; base is its own round 1.

| Label | 1 Corr | 2 Evid | 3 Cit | 4 Logic | 5 Und | 6 Compl | 7 Rigor | 8 Crit | 9 Cons | 10 Repro | 11 LaTeX | 12 Ans | Recommendation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| base | 4 | 4 | 4 | 5 | 3 | 4 | 5 | 4 | 4 | 5 | 4 | 4 | revise |
| inv | 5 | 4 | 4 | 5 | 4 | 4 | 5 | 5 | 4 | 5 | 4 | 5 | PASS |
| dom | 4 | 4 | 4 | 5 | 4 | 5 | 5 | 5 | 3 | 5 | 5 | 5 | REVISE (one major) |
| composed | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | PASS |

The selector and the round 1 evaluators weighed different things: the
selector checked every textbook locator against page images, while the
inv round 1 evaluator recorded the missing degree definition (inv F1) as
minor. This is why the blind choice and the highest round 1 recommendation
differ.

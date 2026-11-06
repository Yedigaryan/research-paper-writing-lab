# Refinement report: adjacency-pipeline

Task: adjacency-walks-connectivity, stage pipeline, k = 1, mode agg
Base commit: 3aa1ca7c30486d367c7a4616951700d9aa7536f8
Dates: 2026-11-02 to 2026-11-06
Domain: graph-theory

## Budget

| Item | Allowed | Used |
|---|---|---|
| Rollouts | 4k = 4 | 4: base, inv, dom, composed |
| Improver sessions | 3k = 3 | 3: INV proposer, DOM proposer, composer |
| Selection sessions | 1 | 1 |
| Reflection sessions | 1 | 1 |

Validation retries: one. The first INV tree broke the frozen fixture
expectation "error: bib entry unusedentry has no year". INV was sent the
error once and fixed it.

Probes ran one at a time, from Thursday 2026-11-05, at the user's
request. All four run orchestrators were pinned to the same session
model. Agent models came from each tree's frontmatter, which is the same
in every candidate.

| Label | Session | Wall clock | Rounds | Decision | Last commit | Cost (USD, API equivalent) |
|---|---|---|---|---|---|---|
| base | probe session, 2026-11-02 | 56 min | 3 | INCOMPLETE | ef7f181 | 21.37 |
| inv | session_01V3X5px4ShXGvaa9cTb4xGT | about 12 h, including a stall | 3 | PASS | b4a5dd7 | 20.26 |
| dom | session_01V3X5pzCTTYKai69Mbmmzz1 | 49 min | 3 | PASS | ab876b9 | 18.76 |
| composed | session_01V3X5pv2N8SZAvo5Wd9Aoba | 49 min | 3 | PASS | 96a36c8 | 18.92 |

Rollouts total 79.31 USD. That excludes the orchestrator, the two
proposers, the composer, the selector, and the reflector, which ran in
this session.

## Candidates

| Label | Dimension | Validation | Tree diff vs base | Probe branch | Deliverable |
|---|---|---|---|---|---|
| base | none | valid | none | claude/harness/adjacency-pipeline/base | 23 pages, 3 rounds, INCOMPLETE |
| inv | INV | valid after one retry | 1 added, 5 modified | claude/harness/adjacency-pipeline/inv | 20 pages, 3 rounds, PASS |
| dom | DOM | valid | 5 modified | claude/harness/adjacency-pipeline/dom | 20 pages, 3 rounds, PASS |
| composed | compose | valid | 1 added, 8 modified | claude/harness/adjacency-pipeline/composed | 21 pages, 3 rounds, PASS |

## Proposer notes

### inv

```
.claude/skills/research-paper/scripts/check_plain_words.py -> new script for study-note papers. It finds every plain-words paragraph, whether marked by the literal phrase or by a macro whose definition contains it. It exits 1 when a definition, theorem, lemma, proposition or corollary has no plain-words paragraph before it, or when the paper has none at all. It warns on sentences over 20 words, on math inside the layer, and on any `--terms` word. -> Every round had plain-words findings that the author checked by hand and missed: E1-5 to E1-8 in round 1, E2-2 and E2-3 in round 2, E3-5 in round 3 (sentences of 23 to 32 words). The round-3 evaluator confirmed E1-7 "checked by script", which shows the check is mechanical.
.claude/skills/research-paper/SKILL.md (Step 4 gate) -> adds `check_plain_words.py` for the study-note register. Its errors go back to the author; its warnings go with the next batch of findings. -> Same moments. E1-6 (no paragraph before Thm 3.17, Prop 3.18 and Prop 5.3; Lemma 4.4's came after the statement) reached a level-3 evaluator even though all four mechanical checks passed with 0 errors.
.claude/agents/paper-author.md (after the check commands) -> run `check_plain_words.py --terms <story-dictionary terms>`. Fix every error, and for each warning either fix it or say why in self-evaluation.md. -> Same moments. The term warnings target E1-7 and E2-3 ("graph", "diagonal", "length", "size" inside story paragraphs).
.claude/skills/research-paper/scripts/check_citations.py (year) [REVISED IN RETRY] -> a bib entry with no year or date is still the error "bib entry <key> has no year", unless the key is an evidence source whose own year is null. A year or date that is not a year, such as `n.d.`, is an error. The retry restores the exact error text and makes it fire for entries that are not evidence sources, which the frozen fixture test in tests/run-checks.sh requires. -> The script itself caused the `n.d.` defect. paper-author-round2 kept `year = {n.d.}` because "check_citations.py requires a year or date field", and round 3 said "removing it would produce errors". It was raised as E1-14, E2-8 and E3-6 and listed as a known limitation in the round-3 INCOMPLETE report.
.claude/skills/research-paper/references/latex-structure.md (Bibliography, Build) -> an undated source gets no year or date field, never `n.d.`. The bib needs one entry per evidence source the paper cites, which removes the clash with "No entry without a \cite". Also documents the new inspect_pdf warning and check_plain_words.py. -> Same as the line above. The uncited-source part is E1-15, E2-9 and E3-7.
.claude/skills/research-paper/scripts/check_citations.py (uncited sources) -> an uncited source warns only while a claim that is not `removed` rests on it. The warning names those claims and the three ways to clear it (cite, drop the support entry, mark the claim removed). A source with no live claim prints as a note. -> The same uncited sources (lehman2017mcs, ntnugraphsearch) were re-raised in all three rounds (E1-15, E2-9, E3-7). The author "did not edit evidence.base.json", although m3 had said NTNU claim C48 was superseded by m3-C1 and m3-C2. Lehman's record says "Supports no claim".
.claude/agents/paper-author.md (Evidence changes) -> when check_citations warns about an uncited source that still carries claims, cite it, or set those claims to `removed` with the reason in the owning file, including evidence.base.json, and rebuild. -> Same moments (paper-author-round2 E1-15 and round3 E2-9 replies).
.claude/skills/research-paper/scripts/inspect_pdf.py -> new warning for any page before the last whose text-line count is under 65 percent of the median, telling the reader to view it as an image. -> A blank band was found in every round while inspect_pdf reported "0 errors, 0 warnings" each time: p. 13 (E1-14), p. 3 (E2-8), pp. 19 to 20 (E3-6).
.claude/agents/paper-author.md (layout) -> render each page that inspect_pdf flags once with pdftoppm and look at it. Fix it by float placement or source order, or say why the page is right. If pdftoppm is missing, say so and go on. -> Same moments. The author only learned of each band from the evaluator.
.claude/agents/paper-author.md (Revision rounds) -> before closing a finding, grep sections/, appendices/ and main.tex for the defective word, sentence or claim and fix every occurrence, logging the other locations. -> Only the flagged location got fixed. E2-6 "grow quickly" was fixed at connectivity.tex:185 but survived at discussion.tex:44 (E3-4). E1-4 "loop" survived at connectivity.tex:81 (E2-2). E1-5 "size" carried into E2-3. The E2-1 major was a sentence copied from the m1 report.
.claude/skills/research-paper/SKILL.md (Step 4) -> once the gate passes and before evaluation round 1, run technician-reader once (round 0). Save its report and findings, send them to the author grouped by section, and re-run the gate. This does not count as one of the three rounds. -> Reader majors were open at every decision: 6 in round 1, 5 in round 2, and R3-1 and R3-15 in round 3, which with E3-1 left the run INCOMPLETE. Reader findings ran 42, 22, 22, so one extra reader-only pass would have reached the evaluator with fewer of them.
.claude/skills/research-paper/SKILL.md (Step 1) -> when the paper rests on something the user only said or typed, save their words verbatim with the date in sources/user-statements.md as a local-file source. If only a summary exists, the file says so and nobody quotes it. -> R3-1 (major, open at INCOMPLETE) asked for the assignment sentence to be quoted, but it existed in no file. The m2 report says C-m2-10 "comes from the user, not from a file", and paper-author-round1 lists "Assignment text: reported without quotation marks and has no source".
```

### dom

```
.claude/skills/research-paper/references/graph-sources.md -> added textbook facts the evaluators verified on the page images: the book never writes e_ij (p. 9 has G = (V, E) and e = uv; the a_ij rule on p. 11 is stated through adjacency); p. 7 is the notation list, so hits for կցության are incidence-matrix pages; pp. 12, 34 and 61 contain neither result -> evaluator round 1 F1/E1-1 (Convention 2.3 put the e_ij rule on p. 9); m1 round-0 report and follow-up (the p. 7 page conflict with the evidence file); round 2 and round 3 spot checks of pp. 12, 34 and 61
.claude/skills/research-paper/references/graph-sources.md -> added that the textbook says nothing about length-0 walks and that the reflexivity of alpha is not evidence for them; Def 1.2.14 is the closed trail "closed path or cycle" and 1.2.15 is the English cycle; Def 1.2.16 measures distance by a shortest trail; on p. 49 the book "notes" alpha's properties and does not prove them -> m3 round-0 claim "reflexivity shows the book counts length 0", withdrawn after orchestrator reconciliation; reader round 1 F14/R1-14 (distance defined with two meanings of path); evaluator round 1 F10/E1-10 ("shows" should be "notes"); round 3 spot check of 1.2.14
.claude/skills/research-paper/references/graph-sources.md -> exact locators and scopes for Galway Thm 1.1.3, Gotti Props 2 and 3, Grinberg Def 2.9.1(a) with k >= 0 and the p. 40 bound, Bai (pp. 1-2, no sum form), Paramadevan (pp. 16-17; the sum covers lengths 1 to n-1), and Waterloo/Schost (slides 8-9 prove the walk/discovery equivalence; slide 10 states connectivity without proof); Lehman marked metadata-only -> evaluator round 1 F2/E1-2 (a quote and a sum test attributed to Bai, who has neither); round 2 and round 3 citation spot checks; research-agent report (access limits)
.claude/skills/research-paper/references/graph-sources.md -> new section "When the paper says one of these sources is wrong": the critique goes in one discussion item; each of the three statements is quoted, restated in the paper's notation and refuted by its own counterexample; the board-graph counterexamples (A^2)_11 = 1, B_22 = 2 and R_11 = 2 are given -> the literature critique produced a major finding in every round: E1-2 (invented quote), R1-30 (critique inside the theorem), R2-18 (symbols not translated), E3-1 (one example claimed to refute three statements, and it fails on B under the length-0 path); E3-1 was one of the findings left open at INCOMPLETE
.claude/skills/research-paper/references/quality-checklist.md -> a Sources item stating the same rule for any paper that says a source is wrong: one discussion item, verbatim quote with locator, restatement in the paper's conventions, one counterexample per statement, no merged or paraphrased quotation -> same chain: E1-2, R1-30, R2-18, E3-1
.claude/skills/research-paper/references/math-pitfalls.md -> a question-table row for length-0 walks (default: allowed, recorded in the brief as the convention) -> the brief left it open; m1 and m3 settled it differently in round 0 and needed orchestrator reconciliation (m1 follow-up item 2, m3 follow-up item 2)
.claude/skills/research-paper/references/math-pitfalls.md -> six more "easy to state wrongly" facts: a positive entry always implies some path exists; the length-0 path counts on the diagonal; a non-simple closed trail has at least 6 edges (not "two triangles"); the reason for (I + A)^(N-1), and that it needs N - 2 products, not one; why a single power fails (the parity zero entry); the induction step starts from the product formula -> E2-1 (false plain-words sentence), E3-1, E1-3 and R2-7 (non-example 3.42), R1-29, R2-12, R3-F14 and E3-2 (the reason for I and "one multiplication"), R3-15 (parity argument, open at INCOMPLETE), R1-21 and R3-F3 (product formula)
.claude/agents/paper-author.md -> item 6 now also points the author to "Facts that are easy to state wrongly" in math-pitfalls.md for graph-theory papers, plain-words paragraphs included; to pay for it, removed the clean-text bullet, which latex-structure.md (read first) states word for word -> the author and module owners never read math-pitfalls.md (only the orchestrator reaches it, through photo-input.md), and the errors above were written by the author in rounds 1 to 3
.claude/agents/module-owner.md -> the graph-sources pointer now also names the math-pitfalls facts section -> the length-0 divergence and the false reflexivity reading started in the module reports (m3 round 0)
```

## Composer notes

Verbatim in `composer-notes.md`, which is committed next to this
report. Decision: merge. 6 kept, 4 revised, 2 dropped. Kept: the
user-statements step, check_plain_words.py, the citation checker's
year handling and uncited-source rule, the math-pitfalls pointer, and
the clean-text bullet removal. Revised: the author's grep before closing
a finding (now also over evidence), math-pitfalls.md, graph-sources.md,
and the quality-checklist critique item. Dropped: INV's reader pre-read
before round 1, and INV's inspect_pdf blank-band check.

The reflector corrected three points in these notes. The composed
graph-sources.md drops DOM's Waterloo CS 341 entry without recording
it. INV's "0 citation warnings" did not come from the uncited-source
edit, whose path never fired. "No major mathematics finding" holds for
DOM only, since composed had one (E1).

## Selection

Pool: base, inv, dom, composed. Each entry is a final paper after its
revision rounds. They were anonymised as cand-a to cand-d (map in
`pool-map.json`). Selector: paper-evaluator, level 3, fresh. It was given
`task.md`, `source/` (the two whiteboard photos and the course textbook),
and `candidates/` only. Its full reply is in `selection.md`. It checked
eight textbook pages as images and recomputed every count in the papers
by script. It found all four papers faithful to the textbook.

```
<why>
The pick came down to conformance and internal consistency among papers that all deliver and are all faithful to the textbook. cand-a meets every objective, has a complete three-column naming table, mentions v_i once as the brief requires, and its numbers are verified. Its only flaw is a one-line slip in the reading guide. The runner-up is cand-d. It is equally correct, but it reuses the textbook's v-labelled vertices throughout, against the brief, and its answer labels A1/A2 clash with the matrix powers. cand-b lost on its "path" meaning a trail in Def 6.1 and the unchecked cells in Table 2. cand-c lost on its partial naming table and the missing number on Def 1.1.1.
</why>
```

Choice: cand-a = composed. Runner-up: cand-d = dom. The base paper was
cand-b and the inv paper was cand-c.

## Reflection

Verbatim in `reflection.md`. The reflector rated twelve edit rows: 1
helped, 6 confounded, 5 no observed effect.

| Component | Candidates | Verdict |
|---|---|---|
| SKILL.md Step 1 user-statements file | inv, composed | confounded |
| check_plain_words.py and its gate lines | inv, composed | no observed effect |
| SKILL.md Step 4 reader pre-read (dropped) | inv | no observed effect |
| check_citations.py year handling, author and latex-structure lines | inv, composed | helped |
| check_citations.py uncited-source rule | inv, composed | no observed effect |
| paper-author.md grep before closing a finding | inv, composed | confounded |
| inspect_pdf.py blank-band check and render step (dropped) | inv | no observed effect |
| math-pitfalls pointer in paper-author.md and module-owner.md | dom, composed | confounded |
| math-pitfalls.md facts | dom, composed | confounded |
| graph-sources.md entries and critique section | dom, composed | confounded |
| quality-checklist.md critique item | dom, composed | confounded |
| paper-author.md clean-text bullet removal | dom, composed | no observed effect |

The selector's reasons were a complete naming table, v_i mentioned only
once, and the dom paper's A1/A2 label clash. The reflector traced none
of them to an edit.

```
<experience>
cue: A mechanical gate script requires a metadata field (year, date, author, page) that some legitimate sources do not have, such as undated lecture notes or anonymous course files, and agents must pass the gate before evaluation.
lesson: In the gate script (here scripts/check_citations.py), accept a missing field when the source's own evidence record has that field null, and reject placeholder values such as "n.d.", "unknown" or "?" as errors. Add one sentence to paper-author.md saying such a field is omitted, never filled. Check: grep references.bib for the placeholder strings and expect zero hits, with the gate passing.
evidence: The check_citations.py year-handling row is the only one rated helped. Without the edit, base and dom wrote year = {n.d.}, and in both runs the author named the checker as the reason (base.md 7081; dom.md 4753). In base this drew an evaluator finding in every round (E1-14, E2-8, E3-6). With the edit, inv and composed contain no "n.d." at all, and composed's undated Galway and Gotti entries pass with the year left out (composed.md 3493-3508).
confidence: medium. The contrast is 2 runs against 2, and the agents state the mechanism in both runs without the edit. Each candidate still has only one rollout, the base run comes from an earlier session, and the defect it removes is minor, so how much it matters is low even if the effect is real.
</experience>
```

## Decision

Adopted: composed.
Installed into .claude/: yes, in the commit that adds this report.
Kept from after the base: technician-reader stays on Haiku. Its file is
reserved and was not touched. The research-paper SKILL.md roles table
keeps the reader at level 1, as in commit 036c58b. The composed tree
came from 3aa1ca7, where the row said 2, so the row was restored after
install. That one table row is the only difference between the live tree
and the composed tree.
Library entry: `.claude/skills/harness-refine/library/graph-theory/harnesses/adjacency-pipeline/`.
tests/run-checks.sh after install: pass.

### Correction to the reflection: why base was INCOMPLETE

The reflector wrote that the candidate runs' reader "no longer grades
severity". The reader definition is identical in all four runs (same
file hash). It never asks for a severity: its output format is
`F1 | comprehension | passage | what was missing | fix`. The difference
lies with the run orchestrators. The base orchestrator assigned
severities to the reader's findings and counted R3-1 and R3-15 as open
majors. The three probe orchestrators did not. The research-paper
SKILL.md Step 5 contributes to this: it says both the evaluator and the
reader return findings "in the format fixed in rubric.md", with
severity, while the reader file forbids it.

So base's INCOMPLETE, against PASS in every candidate run, is not
evidence that any candidate harness is better. Two of base's three open
majors at the end were reader findings graded by its orchestrator, and
the third (E3-1, the literature critique) is a fair comparison point.
The selection was not affected: the selector saw only the final papers.

### Confounds and process notes

- One rollout per candidate; selection compares four single papers.
- inv stalled from about 11:21 to 11:50 UTC on 2026-11-05 at a
  permission prompt on an unguarded `rm`. It was interrupted and then
  continued. Its living author was lost to container restarts in
  round 2.
- dom and composed got one extra prompt paragraph, saying nobody is
  watching and to guard `rm` paths. inv did not.
- The base run is from 2026-11-02. The probes ran on 2026-11-05 and
  2026-11-06.
- build_evidence.py overcounted deliverable pages by one. The base, inv,
  and dom headers were regenerated before selection, and only the header
  line changed. The script and its test were fixed in 0644cde.
- Process record: `process-notes.md`. Probe branches kept: base, inv,
  dom, composed under `claude/harness/adjacency-pipeline/`.

## Evaluator scores, for the record only

Reported after the decision, never used to steer it. These are the
final-round (round 3) scores from each rollout's own evaluation report,
with each run's round-1 evaluator majors. For base, the round-1 count is
evaluator findings only, from `baseline/BASELINE.md`.

| Label | 1 Corr | 2 Evid | 3 Cit | 4 Logic | 5 Und | 6 Compl | 7 Rigor | 8 Crit | 9 Cons | 10 Repro | 11 LaTeX | 12 Ans | Round-1 evaluator majors | Open majors at end | Decision |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| base | 4 | 4 | 5 | 3 | 4 | 5 | 5 | 4 | 4 | 5 | 4 | 5 | 4 | 3 (1 evaluator, 2 reader) | INCOMPLETE |
| inv | 5 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 1 | 0 | PASS |
| dom | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 1 | 0 | PASS |
| composed | 5 | 4 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 1 | 0 | PASS |

Each run had a fresh evaluator, so scores from different runs are not on
one scale. The blind selector preferred composed over dom, although dom
has the higher final-round scores. The selector checked conformance to
the brief, while each round's evaluator scored against the rubric.

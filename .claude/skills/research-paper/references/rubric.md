# Evaluation rubric, release conditions, and report format

Used by `paper-evaluator`, `technician-reader`, and the orchestrator.

## Scale

| Score | Meaning |
|---|---|
| 0 | Missing or invalid. No acceptable evidence of compliance. |
| 1 | Poor. Major deficiencies. |
| 2 | Insufficient. Partial compliance with significant gaps. |
| 3 | Acceptable. Meets the minimum standard. |
| 4 | Strong. Clear, rigorous, well supported. |
| 5 | Excellent. Thoroughly verified, precise, exceptionally clear. |

Every score is justified by at least one concrete observation with a
location in the paper. A score with no observation is invalid.

## Dimensions

1. Correctness: claims, explanations, calculations, conclusions are accurate.
2. Evidence coverage: every substantive factual claim has appropriate support.
3. Citation integrity: references are real, traceable, relevant, and
   accurately represented. On the first round spot-check at least three by
   fetching the source. On a later round follow "Source checks across
   rounds" below.
4. Logical validity: conclusions follow from premises and evidence.
5. Understandability: no unexplained term, symbol, acronym, or missing step
   for a technician-level reader.
6. Completeness: everything the brief lists as needed to answer the
   question is present. An optional objective, or a topic outside the
   brief's scope, is not required, and its absence is never a finding.
7. Methodological rigor: methods, assumptions, experiments, calculations are
   appropriate and transparent.
8. Critical analysis: limitations, competing explanations, counterarguments,
   uncertainty are addressed in proportion to the question. A short answer
   needs a short statement of its limits, not a survey.
9. Internal consistency: terminology, notation, assumptions, conclusions
   agree throughout.
10. Reproducibility: important calculations and results can be checked.
11. LaTeX and PDF quality: compiles, readable, references resolve, tables
    and figures render.
12. Answer relevance: the paper directly and adequately answers the
    question in `brief.md`, in proportion. Material that does not serve the
    question, or that goes beyond the brief's scope, lowers this score.

## Severity

- Critical: invalidates a material conclusion, fabricated or misrepresented
  evidence, or a major correctness, integrity, or safety problem.
- Major: a significant claim unsupported, a key concept unexplained, or an
  important part of the question unanswered.
- Minor: clarity, consistency, presentation, or a nonessential omission.

## Surplus

Material that does not serve the brief's question is a defect, like a
missing step. The evaluator raises it as a finding whose defect starts with
the word `Surplus:`, names the passage, and gives `cut` or `shorten to
<what remains>` as the correction. It is minor when it only costs the
reader time. It is major when the reader has to get through it before
reaching an answer, or when the paper is over the page budget in
`brief.md`.

Surplus includes: a concept defined and never used in an answer; a second
example that shows nothing the first did not; a remark, example, or
non-example after a definition that no reader would get wrong; text about
where the inputs came from in the body instead of the notes on sources;
analogies when the brief says `Analogies: no`.

A correction that adds text names the needed objective it serves. An
addition that serves no needed objective is not asked for. When the paper
is at its page budget, a correction that adds text also names what can be
cut to make room.

## Comprehension review

For every section the evaluator and the technician reader ask:

- What is the purpose of this section?
- Is every essential concept introduced before it is used?
- Are technical terms, acronyms, variables, and equations explained?
- Can each important conclusion be traced to evidence or valid reasoning?
- Is there a step the reader must supply by an unstated assumption?
- Could a technician-level reader explain the main point after reading it?

A failure names the exact passage and gives the correction.

## Release conditions

All must hold:

1. Every dimension scores at least 3.
2. No unresolved critical factual, logical, citation, or safety defect.
3. Every substantive factual claim has support or explicit qualification.
4. All material conclusions have adequate justification.
5. No essential concept or reasoning step is unexplained.
6. The evaluator's configured level exceeds the author's and every module
   owner's level (`model-levels.md`).
7. `build.sh` succeeds and `inspect_pdf.py` reports no errors, which
   includes the page budget in `brief.md`.
8. `check_citations.py` and `check_claims.py` report no errors.
9. `self-evaluation.md` covers every section of the current draft.
10. An independent evaluation passed on the current draft, or on the
    draft as it stood before the final edits described below.

Critical and major findings must be resolved, and the next evaluator
confirms each. Minor findings are resolved or documented with a reason.
Scores are never adjusted to satisfy a condition.

## Final edits

Minor findings never cost an evaluation round on their own. When a round
ends with conditions 1 to 9 holding and no critical or major finding open,
the paper is released in that round, after the final edits:

- The author resolves each minor finding or says why it stays, and may
  change a passage the reader named. It changes nothing else.
- A final edit adds no claim and no citation, and changes no numbered
  statement and no step of a proof. A finding that needs any of these is
  documented as open, or the orchestrator runs another round.
- The orchestrator reads the diff, confirms that it touches only passages
  those findings name, and re-runs the mechanical checks.
- The report says which findings were closed by final edits and that no
  evaluator re-read them.

## Source checks across rounds

Fetching a source to check a quote is the slowest thing an evaluator does,
and a source that was checked does not change between rounds. The
orchestrator keeps `source-checks.md`, the evaluators' CITATION SPOT CHECKS
blocks round by round, and before a later round runs `claims_changed.py`,
which lists the evidence claims that are new or changed since the last
evaluated round. On a later round the evaluator:

- does not fetch again for a check recorded as `supports` whose claim is
  not on the changed list, and reports it as `carried`;
- fetches for every weight-bearing claim on the changed list that the
  paper cites, for every earlier check whose result was not `supports`, and
  for every source that was `unavailable`;
- fetches one carried check of its own choice again as a control, and
  reports a disagreement with the record as a finding.

## Findings format returned by agents

```
SCORES
1 Correctness: <0-5> -- <observation with location>
...
12 Answer relevance: <0-5> -- <observation with location>

FINDINGS
F1 | critical|major|minor | <file:line or section> | <defect in one sentence> | <correction>
F2 | ...

CITATION SPOT CHECKS
<source key> | <claim id> | <locator> | fetched|viewed|unavailable|carried | supports|does not support|partially supports | <note>

UNVERIFIED CLAIMS IN TEXT
<claim id> | <location> | qualified|not qualified

RECOMMENDATION
PASS | REVISE | FAIL -- <one sentence>
```

The technician reader returns only the FINDINGS block, every line tagged
`comprehension` in place of a severity, plus a one-paragraph summary of
what it believed the paper concluded. Reader findings carry no severity and
no score, and the orchestrator never assigns one. They are recorded
ungraded in `reader-findings.md` and go to the author as advisory. Only the
evaluator grades: on a later round it reads `reader-findings.md`, and when
a reader passage, or a mismatch between the reader's summary and the
paper's actual conclusion, shows a real defect, it raises that as its own
finding with a severity from this rubric.

## Evaluation report template

`papers/<slug>/evaluation-report.md`, one block per round, appended.

```
# Evaluation report

## Round <n>, <date>

Question: <from brief.md>
Scope: <one paragraph>
Research summary: <sources found, modules, rounds of research>

Model levels: research 2, modules 2, author 2, reader 1, evaluator 3,
orchestrator <session model>. Hierarchy requirement: met | not met.

Mechanical checks: build <pass|fail>, citations <pass|fail>,
claims <pass|fail>, pdf <pass|fail>. Pages <n> of a budget of <n>.

### Scores
<table: dimension, score, observation>

### Findings
<evaluator findings only: id, severity, location, defect, status (open|resolved|documented)>

### Citation and claim coverage
<counts: sources, claims by status, spot checks fetched this round, spot checks carried>

### Unverified claims and access limits
<list>

### Known limitations
<list>

### Final edits
<none, or: finding ids closed after the evaluation, diff confined to the
named passages yes|no, mechanical checks re-run pass|fail; not re-read by an
evaluator>

Decision: PASS | FAIL | INCOMPLETE -- <reason>
```

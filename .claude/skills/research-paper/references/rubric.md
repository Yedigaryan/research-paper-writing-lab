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
   accurately represented. Spot-check at least three by fetching the source.
4. Logical validity: conclusions follow from premises and evidence.
5. Understandability: no unexplained term, symbol, acronym, or missing step
   for a technician-level reader.
6. Completeness: the information needed to understand and assess the topic
   is present.
7. Methodological rigor: methods, assumptions, experiments, calculations are
   appropriate and transparent.
8. Critical analysis: limitations, competing explanations, counterarguments,
   uncertainty are addressed.
9. Internal consistency: terminology, notation, assumptions, conclusions
   agree throughout.
10. Reproducibility: important calculations and results can be checked.
11. LaTeX and PDF quality: compiles, readable, references resolve, tables
    and figures render.
12. Answer relevance: the paper directly and adequately answers the
    question in `brief.md`.

## Severity

- Critical: invalidates a material conclusion, fabricated or misrepresented
  evidence, or a major correctness, integrity, or safety problem.
- Major: a significant claim unsupported, a key concept unexplained, or an
  important part of the question unanswered.
- Minor: clarity, consistency, presentation, or a nonessential omission.

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
7. `build.sh` succeeds and `inspect_pdf.py` reports no errors.
8. `check_citations.py` and `check_claims.py` report no errors.
9. `self-evaluation.md` covers every section of the current draft.
10. The independent evaluation of the current draft passed.

Critical and major findings must be resolved. Minor findings are resolved
or documented with a reason. Scores are never adjusted to satisfy a
condition.

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
<key> | fetched|unavailable | supports|does not support|partially supports | <note>

UNVERIFIED CLAIMS IN TEXT
<claim id> | <location> | qualified|not qualified

RECOMMENDATION
PASS | REVISE | FAIL -- <one sentence>
```

The technician reader returns only the FINDINGS block, all tagged
`comprehension`, plus a one-paragraph summary of what it believed the paper
concluded. A mismatch between that paragraph and the actual conclusion is
itself a major finding.

## Evaluation report template

`papers/<slug>/evaluation-report.md`, one block per round, appended.

```
# Evaluation report

## Round <n>, <date>

Question: <from brief.md>
Scope: <one paragraph>
Research summary: <sources found, modules, rounds of research>

Model levels: research 2, modules 2, author 2, reader 2, evaluator 3,
orchestrator <session model>. Hierarchy requirement: met | not met.

Mechanical checks: build <pass|fail>, citations <pass|fail>,
claims <pass|fail>, pdf <pass|fail>.

### Scores
<table: dimension, score, observation>

### Findings
<table: id, severity, location, defect, status (open|resolved|documented)>

### Citation and claim coverage
<counts: sources, claims by status, spot checks>

### Unverified claims and access limits
<list>

### Known limitations
<list>

Decision: PASS | FAIL | INCOMPLETE -- <reason>
```

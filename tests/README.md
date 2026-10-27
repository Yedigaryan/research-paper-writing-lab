# Pipeline tests

The research-paper skill must be able to reject a bad paper. This folder
holds the fixture that proves it.

## Fixture

`fixtures/defective-paper/` is a short LaTeX paper with planted defects:
a theorem that says "paths" where the source says "walks", a citation key
with no bibliography entry, a numeric claim resting on an unreachable
source, an unexpanded acronym, a proof that is not a proof, and a
conclusion that claims something the body never argued. The complete list
with severities is in `fixtures/defective-paper/expected-findings.md`.

## Mechanical checks

```
bash tests/run-checks.sh
```

Runs `check_citations.py` and `check_claims.py` against the fixture and
asserts that both fail with the errors listed under "Caught by the
scripts". Run it after any change to the scripts or the evidence schema.
`build.sh` is also run when a LaTeX toolchain is installed; without one it
exits 2 and the test reports the build step as skipped.

## Evaluator check

After any change to `.claude/agents/paper-evaluator.md`,
`.claude/agents/technician-reader.md`, or
`.claude/skills/research-paper/references/rubric.md`, run Step 5 of the
skill on `tests/fixtures/defective-paper/` and compare the findings with
`expected-findings.md`. Every critical and major item must be raised and
the recommendation must be FAIL. Record the result in the commit message.

## Adding a fixture

Copy the layout of `defective-paper`, plant defects that the current
checks or rubric would miss, and list them in a new `expected-findings.md`.
Keep each fixture short enough to evaluate in one agent run.

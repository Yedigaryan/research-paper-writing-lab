#!/usr/bin/env bash
# Run the mechanical checks against the defective fixture and assert they fail
# with the expected errors. Exit 0 when every expectation holds.
set -u
root="$(cd "$(dirname "$0")/.." && pwd)"
scripts="$root/.claude/skills/research-paper/scripts"
fixture="$root/tests/fixtures/defective-paper"
status=0

expect_fail() {
  local name="$1"; shift
  local out
  out="$("$@" 2>&1)"
  local code=$?
  if [ $code -eq 0 ]; then
    echo "FAIL: $name exited 0 but the fixture must fail"
    echo "$out"
    status=1
  else
    echo "ok: $name failed as expected (exit $code)"
  fi
  printf '%s\n' "$out"
}

expect_contains() {
  local haystack="$1" needle="$2"
  if printf '%s' "$haystack" | grep -qF -- "$needle"; then
    echo "ok: found '$needle'"
  else
    echo "FAIL: missing '$needle'"
    status=1
  fi
}

cit="$(expect_fail check_citations python3 "$scripts/check_citations.py" "$fixture")"
echo "$cit" | head -1
expect_contains "$cit" "cited key page1999pagerank not in references.bib"
expect_contains "$cit" "bib entry unusedentry is not an evidence source"
expect_contains "$cit" "bib entry unusedentry has no year"

clm="$(expect_fail check_claims python3 "$scripts/check_claims.py" "$fixture")"
echo "$clm" | head -1
expect_contains "$clm" "claim[1] C2: marked supported but source smith2021walks is unavailable"
expect_contains "$clm" "claim[2] C3: derived claim without derivation"

if command -v latexmk >/dev/null 2>&1; then
  bld="$(expect_fail build bash "$scripts/build.sh" "$fixture")"
  echo "$bld" | head -1
  expect_contains "$bld" "undefined citations"
else
  echo "skipped: build.sh (no latexmk installed)"
fi

if python3 "$root/tests/test_harness.py" 2>&1 | tail -3; then
  echo "ok: harness-refine script tests"
else
  echo "FAIL: harness-refine script tests"
  status=1
fi

if python3 "$root/.claude/skills/harness-refine/scripts/harness_tree.py" validate repo >/dev/null; then
  echo "ok: live harness tree is valid"
else
  echo "FAIL: live harness tree is invalid"
  status=1
fi

if [ $status -eq 0 ]; then
  echo "all expectations hold"
fi
exit $status

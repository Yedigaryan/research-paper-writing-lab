#!/usr/bin/env bash
# Compile papers/<slug>/main.tex with latexmk and biber.
# Usage: build.sh <paper_dir>
# Exit 0 on a clean build, 1 on LaTeX errors or unresolved references,
# 2 when no LaTeX toolchain is installed.
set -u

if [ $# -ne 1 ]; then
  echo "usage: build.sh <paper_dir>" >&2
  exit 1
fi
paper="$1"
if [ ! -f "$paper/main.tex" ]; then
  echo "error: $paper/main.tex not found" >&2
  exit 1
fi

if ! command -v latexmk >/dev/null 2>&1; then
  echo "error: latexmk not installed. Install TeX Live with latexmk and biber" >&2
  echo "(Debian/Ubuntu: apt-get install texlive-latex-extra texlive-bibtex-extra biber latexmk)." >&2
  exit 2
fi
if ! command -v biber >/dev/null 2>&1; then
  echo "error: biber not installed; the bibliography cannot be resolved." >&2
  exit 2
fi

mkdir -p "$paper/build"
(
  cd "$paper" || exit 1
  latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
    -outdir=build main.tex
)
status=$?
log="$paper/build/main.log"

fail=0
if [ $status -ne 0 ]; then
  echo "error: latexmk exited with $status" >&2
  fail=1
fi
if [ -f "$log" ]; then
  if grep -qE "^(.*:[0-9]+: |! )" "$log"; then
    echo "error: LaTeX errors in $log:" >&2
    grep -E "^(.*:[0-9]+: |! )" "$log" | head -20 >&2
    fail=1
  fi
  if grep -q "Reference .* undefined" "$log"; then
    echo "error: undefined references:" >&2
    grep "Reference .* undefined" "$log" | sort -u | head -20 >&2
    fail=1
  fi
  if grep -q "Citation .* undefined" "$log"; then
    echo "error: undefined citations:" >&2
    grep "Citation .* undefined" "$log" | sort -u | head -20 >&2
    fail=1
  fi
  if grep -q "File .* not found" "$log"; then
    echo "error: missing files:" >&2
    grep "File .* not found" "$log" | sort -u | head -20 >&2
    fail=1
  fi
  overfull=$(grep -c "Overfull" "$log" || true)
  if [ "$overfull" -gt 0 ]; then
    echo "warning: $overfull overfull boxes (see $log)"
  fi
else
  echo "error: no log at $log" >&2
  fail=1
fi

if [ $fail -eq 0 ] && [ -f "$paper/build/main.pdf" ]; then
  cp "$paper/build/main.pdf" "$paper/main.pdf"
  echo "ok: $paper/main.pdf"
  exit 0
fi
exit 1

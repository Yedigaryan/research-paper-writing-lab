# Paper folder and LaTeX conventions

## Layout

```
papers/<slug>/
  brief.md                 orchestrator: research brief
  sources/                 user-supplied files, descriptive names
  evidence/
    evidence.json          single source of truth (merged)
    modules/<id>.json      module fragments, merged by script
  modules/<id>.md          module reports
  main.tex                 document shell, inputs sections
  sections/*.tex           one file per section
  appendices/*.tex         derivations, data, supplementary material
  figures/                 images and TikZ sources
  references.bib           bibliography, keys equal evidence source ids
  self-evaluation.md       author: section by section claims and support
  evaluation-report.md     orchestrator: rounds, scores, findings, decision
  README.md                how to compile, dependencies
  main.pdf                 compiled output
  build/                   latexmk auxiliary files, ignored by git
```

`scripts/new_paper.py` creates this layout with a compilable empty shell.

## Document conventions

- Document class `article`, 11pt, A4, `geometry` with 2.5 cm margins.
- Packages: `amsmath`, `amsthm`, `amssymb`, `graphicx`, `booktabs`,
  `hyperref`, `cleveref`, `biblatex` with `backend=biber`, numeric style,
  `urldate` printed for web sources.
- Theorem environments: `definition`, `theorem`, `lemma`, `remark`,
  `example`, numbered within section.
- Every section file starts with `\section{...}\label{sec:...}`.
- Every equation that is referred to has a label. Every figure and table
  has a caption, a label, and is referred to in the text.
- Citations sit next to the claim they support, inside the sentence.
- Acronyms are expanded on first use. Variables are defined before use.
- Clean text: no emojis, no decorative symbols, no unexplained jargon.

## Required sections (adapt names to the topic)

1. Introduction: the question, where it came from, why it matters, what
   the paper will show, how it is organized.
2. Background: prerequisite concepts, definitions, notation, assumptions,
   in build order.
3. Prior work or state of knowledge, where applicable.
4. Method, derivation, or analysis: the body that answers the question.
5. Results and evidence: findings, calculations, comparisons.
6. Discussion: limitations, counterarguments, failure cases, implications.
7. Conclusion: the direct answer to the question.
8. Appendices: full derivations, data, reproducibility notes.

In the `study-note` register the Background section follows the textbook
standard in `book-style-standard.md` and every definition, theorem, test,
and worked example is preceded by a plain words paragraph; see
`photo-input.md`.

## Bibliography

- One entry per source in `evidence.json`, key identical to the source id.
- Fields as complete as the source allows: author, title, year, journal or
  publisher, volume, pages, doi, url, urldate. Never fill a field with a
  guess; leave it out.
- Web sources carry `urldate`. Local files are cited as `@misc` with
  `howpublished` naming the file and `note` saying it was supplied by the
  user.
- No entry without a `\cite`; `check_citations.py` reports unused entries.

## Build

`scripts/build.sh papers/<slug>` runs `latexmk -pdf` with biber in
`build/`, copies `main.pdf` to the paper folder, and fails on LaTeX errors,
undefined references, undefined citations, or missing files. It exits with
code 2 when no LaTeX toolchain is installed; the paper README says what to
install (TeX Live with latexmk and biber).

`scripts/inspect_pdf.py papers/<slug>` checks the PDF text for unresolved
references (`??`), unresolved citations, empty pages, and the log for
overfull boxes and missing figures.

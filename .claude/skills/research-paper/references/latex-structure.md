# Paper folder and LaTeX conventions

## Layout

```
papers/<slug>/
  brief.md                 orchestrator: research brief
  sources/                 user-supplied files, descriptive names
  evidence/
    evidence.json          single source of truth (merged)
    modules/<id>.json      module fragments, merged by script
    checked-claims.json    claims as the last evaluated round saw them
  modules/<id>.md          module reports
  main.tex                 document shell, inputs sections
  sections/*.tex           one file per section
  appendices/*.tex         derivations, data, supplementary material
  figures/                 images and TikZ sources
  references.bib           bibliography, keys equal evidence source ids
  self-evaluation.md       author: section by section claims and support
  evaluation-report.md     orchestrator: rounds, scores, findings, decision
  reader-findings.md       orchestrator: the reader's findings, ungraded
  source-checks.md         orchestrator: the evaluators' source checks by round
  reports/                 every agent's final message, verbatim
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

## Sections (adapt names to the topic)

A section exists because the question needs it, not because this list
names it. A paper of up to about six pages usually has an introduction,
the definitions, one section per question, a worked example with the
limits of the answer, and the notes on sources.

1. Introduction: the question, the answer in a sentence or two, how the
   paper is organized. Nothing about where the inputs came from.
2. Background: the concepts, definitions, notation, and assumptions the
   answers use, in build order, and no others.
3. Prior work or state of knowledge, when the question is about it.
4. Method, derivation, or analysis: the body that answers the question.
5. Results and evidence: findings, calculations, a worked example.
6. Limits: limitations and failure cases of the answer. A paragraph in a
   short paper, a section in a long one.
7. Conclusion: the direct answer. A paper whose introduction already
   states its answers closes with the limits and has no separate
   conclusion.
8. Notes on sources: see below.
9. Appendices: only what a needed objective requires and the body cannot
   hold. They count toward the page budget.

The page budget in `brief.md` counts every page of `main.pdf`. Meet it by
leaving out what the question does not need, never by changing the font
size, the margins, or the spacing, and never by dropping a proof step.

In the `study-note` register the Background section follows the textbook
standard in `book-style-standard.md`. When the brief says `Analogies: yes`,
each definition, theorem, test, and worked example is preceded by a plain
words paragraph; see `photo-input.md`.

## Notes on sources

One short section before the references, `\section*{Notes on sources}`,
holds everything about where the paper's inputs came from: which question
came from the board, the user's words, or the paper itself; how an
uncertain mark on a photo was read; where a drawing and a formula
disagreed; what was searched in a source that lacks a result; which
sources could not be opened; where the scripts are and how to rerun them.
Keep it under half a page.

In the body a statement carries its `\cite` and nothing else about its
origin. The body does not mention the board, the assignment, the user, or
a search of a source. A convention that fixes the mathematics, such as
what "path" means in this paper, is stated in one clause where the term is
defined; who uses the other convention goes in the notes.

## Bibliography

- One entry per evidence source the paper cites, key identical to the
  source id. A source whose claims are all `removed`, or that supports no
  claim, needs no entry.
- Fields as complete as the source allows: author, title, year, journal or
  publisher, volume, pages, doi, url, urldate. Never fill a field with a
  guess; leave it out. An undated source (evidence `year` null) has no
  `year` or `date` field at all, never `n.d.`; `check_citations.py`
  accepts the omission and rejects a year that is not a year.
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
overfull boxes and missing figures. It reads the line `Page budget: <n>`
from `brief.md` and fails a PDF with more pages than that.

`scripts/claims_changed.py papers/<slug>` lists the evidence claims that
are new or changed since the last evaluated round; with `--record <n>` it
stores the claims as round n saw them. The orchestrator runs it around
each evaluation so that later rounds fetch sources only for what changed.

`scripts/check_plain_words.py papers/<slug> --terms <words>` applies when
the brief says `Analogies: yes`: it finds every plain-words paragraph, fails
when a definition, theorem, lemma, proposition, or corollary has none
before it, and warns about sentences over 20 words, notation, and the
listed technical words inside those paragraphs.

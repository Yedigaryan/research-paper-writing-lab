# Photo and lecture-material input

Applies when the input includes photos of whiteboards, handwritten notes,
or textbook pages. This replaces the former `whiteboard-to-paper` skill.
The orchestrator does this work in Step 1 because it is the only role that
can ask the user a question.

## Read the photos

Read every photo: handwritten text, notation, matrices, diagrams. Report,
in this order:

1. A line-by-line transcription in reading order.
2. The main topic and the concepts involved, in your own words.
3. Observations in three labelled groups:
   - Clearly visible: text read with confidence.
   - Likely interpretation: inferred from context, not verifiable.
   - Unclear or missing: needs the user.

Rules:

- Never invent missing text. Never silently assign a meaning to an
  uncertain symbol. A small mark can be a superscript, a prime, or
  quotation marks, and each changes the question.
- Compare diagrams against matrices and formulas on the same board. Report
  mismatches edge by edge rather than picking a side. Mention stray marks.
- When two photos show the same board, say so and read them together.
- Compare the board's notation with the user's text and with textbook
  convention. Flag differences.
- If the user lists the questions in text, the text wins over the reading
  of the board, but the brief still records what the board says.

## Ask only what changes the paper

Ask about things that change the mathematics or the wording. One question
per turn, most important first. For each: what was understood so far, the
question in plain language, why it matters in one or two sentences, two or
three choices including "not sure" with the assumption that will then be
used. Subject-specific questions that usually matter are in
`math-pitfalls.md`; for a subject not covered there, write the same kind of
table before asking.

When the user mentions a file that did not arrive, say so and ask for it
again; continue with work that does not depend on it.

## Study-note register

When the user wants to learn the material, or the input is lecture
material and no other audience was named, set the register to `study-note`
in the brief. This adds to the technician standard:

- The course textbook is the quality bar. Its presentation pattern is in
  `book-style-standard.md`. For this repository the textbook is
  `Grafneri_tesutyun.pdf` at the root; its text layer drops symbols, so
  formulas are checked by viewing the page as an image.
- Definitions are numbered, in the book's build order, and cite the
  book's definition numbers. Only the concepts an answer uses are defined;
  the book's whole chain of concepts is not reproduced.
- A remark, an example, or a non-example follows a definition only where a
  reader would go wrong without it: the board, the user, and the book use
  the word differently, or beginners confuse the concept with its
  neighbour. One worked example carries the paper. A second is written
  only when it shows something the first cannot, such as a test failing.
- When the board, the user, or the book disagree on a convention, the
  paper uses one, says which in one clause where the term is defined, and
  gives the other reading in the notes on sources (`latex-structure.md`).
- Every matrix product, sum, and count is computed by script before it is
  written.
- Cite the textbook as a `local-file` source in the evidence file with the
  page or definition number as locator.

The `quality-checklist.md` items under "Sources", "Standard of
presentation", "Mathematics", and "Writing" apply in this register and are
passed to the author and the evaluator as additional criteria.

## Analogies: the plain words layer

Off unless the brief says `Analogies: yes`; then it applies in either
register, and the checklist items under "Analogies" apply with it.

- One concrete story is fixed in the introduction in at most four
  sentences, with one story word for each technical term.
- A paragraph marked "In plain words" stands before each definition,
  theorem, lemma, test, and worked example: at most three sentences, no
  notation, sentences of about fifteen words, one idea each, story words
  only. Read each aloud in your head; split any sentence that needs a
  symbol or a defined term.
- Each paragraph opens the statement it precedes. Put vertical space
  before it (`\medskip`) and none between it and its statement, so that it
  is not read as the end of the statement above.
- An analogy must be true of the mathematics. One that is easier because
  it is wrong fails; hold each to `math-pitfalls.md`.
- The formal text stands without the layer: with every plain-words
  paragraph removed, the paper is still complete.
- The layer counts toward the page budget. The brief's count allows about
  one page for every ten statements that get a paragraph.

## Checking an existing photo-based paper

Run the photo reading above on the files in the paper's `sources/` folder.
The paper's "Conventions and assumptions" list stands in for the user's
text, so no clarifying question is needed. Then:

1. Mark each `quality-checklist.md` item pass or fail with a quoted line.
2. Recompute every matrix, product, sum, and count with a short script.
3. Check every cited textbook definition number against the PDF.
4. If the paper has a plain words layer, list every definition, theorem,
   test, and worked example and whether a plain words paragraph precedes
   it; quote any sentence that fails the read-aloud test.

Report mismatches between paper and photos, any definition that is not
exactly correct, and any sentence a beginner could not follow. Do not
rewrite the paper unless asked.

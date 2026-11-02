# Final quality checklist

Run every item before presenting the paper. Fix failures, then re-run.

## Sources

- [ ] Every line of text on the photos was considered. Nothing on the board
      is missing from the paper without a stated reason.
- [ ] Every uncertain reading was either resolved with the user or is
      stated as an assumption in the paper.
- [ ] The paper's example matches the photo's example, or the paper says
      why it differs and describes the difference correctly, edge by edge
      (for example, the drawing and the matrix disagreed).
- [ ] The introduction says where each question came from: the board, the
      user's text, or the paper itself.
- [ ] The paper uses the course textbook's names for concepts and cites
      its definition numbers, and says where the textbook convention
      differs from the board.
- [ ] Every attribution matches the quote in the evidence file: the same
      object (a closed walk is not a closed trail), the same setting
      (simple graphs, digraphs, multigraphs), the source's own number and
      page, and an author named only if the source record lists one.
- [ ] Every sentence that says a source lacks something ("the textbook
      does not define ...") was checked by a search of that source, and
      the paper says what was searched.
- [ ] Text the user reported but did not supply (an assignment sheet) is
      given as reported content, never inside quotation marks.

## Standard of presentation (modelled on the textbook)

- [ ] Notation is fixed in one place before the first definition.
- [ ] Every definition, theorem, and remark is numbered and referred to
      by number afterwards.
- [ ] Every definition is followed by a remark on what it allows and
      forbids, an example, and a non-example.
- [ ] Concepts appear in the textbook's build order; nothing is used
      before it is defined.
- [ ] Every theorem is stated in one sentence before its argument, and
      the argument names its method and covers every case.
- [ ] A result the textbook does not contain is marked as proved in the
      paper, not attributed to the book.

## Mathematics

- [ ] Every required question is answered with a precise statement.
- [ ] Every symbol is defined before it is used.
- [ ] Every definition and theorem is correct under the stated
      conventions.
- [ ] Every matrix, product, sum, and count was computed and checked.
- [ ] Concepts that beginners confuse are separated explicitly and named.
- [ ] One meaning per word and per letter in the whole paper, plain-words
      paragraphs included. List every defined word (walk, trail, path,
      cycle, loop, step, component) and every letter (N, n, m, k, S) and
      grep each: a defined word is never used in an everyday sense, and a
      letter never names two things. Where a source uses a word in another
      sense (cycle as closed trail or as simple cycle), one sentence fixes
      the sense this paper uses.
- [ ] A matrix entry is a count, never the object it counts: write "counts
      the walks", not "is a walk".
- [ ] No claim is made about what the professor intended beyond what the
      photos and the user said.

## Writing (five-year-old standard)

- [ ] One concrete story is fixed in the introduction and matches the
      mathematics exactly.
- [ ] Every definition, theorem, test, and worked example is preceded by
      an "In plain words" paragraph told in that story, with no notation
      beyond the letters the introduction's story explained.
- [ ] Each plain-words paragraph passes the read-aloud test: a
      five-year-old could follow it sentence by sentence.
- [ ] Short sentences, one idea each; about fifteen words or fewer in
      plain-words paragraphs.
- [ ] Unfamiliar words explained where they first appear.
- [ ] Simple explanation first, formal definition second, example third.
- [ ] No emojis, no decorative symbols, clean copyable text.
- [ ] Mathematics renders: LaTeX compiles without errors, or for a legacy
      Markdown paper the math renders on GitHub (`$...$`, `$$...$$`, `pmatrix`).
- [ ] The story has a fixed dictionary, one story word per technical
      term, given once in a table. Plain-words paragraphs use only those
      story words; a technical word inside a story paragraph, or two story
      words for one term, fails.
- [ ] The reader's text contains nothing from the pipeline: no claim ids,
      no "evidence file", no module names or script-internal names, no
      unintroduced "the user". Sources, pages checked, and how to rerun
      the scripts sit together in one short provenance section or
      appendix; the mathematical sections only cite.
- [ ] Every scope limit in the brief is met literally: a "one-sentence
      remark" is one sentence in one place, a "short remark" is a
      paragraph, not a section.
- [ ] Structure: title, introduction with conventions, definitions, one
      section per question, worked example, conclusion. A question whose
      answer is a definition is answered by that numbered definition in
      its build-order place; its section points to it and adds only what
      is new there (the convention comparison), never a restated
      definition or restated examples.

## Repository

- [ ] Paper saved under `papers/<topic-slug>/` in the layout of
      `latex-structure.md` (legacy photo papers: `paper.md`).
- [ ] Source photos copied to `papers/<topic-slug>/sources/`.
- [ ] Changes committed with a clear message.
- [ ] Nothing pushed without the user's explicit confirmation.

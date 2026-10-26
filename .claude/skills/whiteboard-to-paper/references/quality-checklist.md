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
- [ ] Markdown math renders on GitHub (`$...$`, `$$...$$`, `pmatrix`).
- [ ] Structure: title, introduction with conventions, definitions, one
      section per question, worked example, conclusion.

## Repository

- [ ] Paper saved at `papers/<topic-slug>/paper.md`.
- [ ] Source photos copied to `papers/<topic-slug>/sources/`.
- [ ] Changes committed with a clear message.
- [ ] Nothing pushed without the user's explicit confirmation.

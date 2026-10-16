---
name: whiteboard-to-paper
description: Turn photos of lecture whiteboards, handwritten notes, or textbook pages into a beginner-friendly, mathematically correct study paper. Use when the user shares class photos or scanned book pages and asks to understand the material, answer the lecture's questions, or write it up as an assignment or study note. Also use when the user asks to check an existing paper in this repository against its source photos.
---

# Whiteboard to Paper

Interactive tutor and academic writing coach. The input is one or more photos
of lecture material, optionally with a textbook excerpt. The output is a
polished Markdown paper saved in this repository, written so that a complete
beginner can follow it, with every definition mathematically correct.

Work in six phases. Phases 1 and 2 always run first and end the turn with a
question. Never jump straight to the final paper.

## Phase 1: Analyze the photos

Read every photo carefully: handwritten text, notation, matrices, diagrams.
Then report, in this order:

1. A line-by-line transcription of what the board says, in reading order.
2. The main topic and the concepts involved, in your own words.
3. Observations in three labelled groups:
   - Clearly visible: text you can read with confidence.
   - Likely interpretation: inferred from context, not verifiable.
   - Unclear or missing: needs the user.

Rules:

- Never invent missing text. Never silently assign a meaning to an uncertain
  symbol. A small mark can be a superscript, a prime, or quotation marks, and
  each changes the question.
- Compare diagrams against matrices and formulas on the same board. Report
  any mismatch rather than picking a side.
- Compare the board's notation with the user's prompt and with textbook
  convention. Flag differences, for example a board that writes the edge
  set as V.
- If the user lists the questions in text, the text wins over your reading
  of the board, but still report what the board says.

## Phase 2: Ask clarifying questions

Ask only about things that change the mathematics or the wording of the
final paper. Ask one question per turn, most important first. For each
question:

- State what you understood so far, briefly.
- Ask the question in plain conversational language.
- Say in one or two sentences why it matters.
- Offer two or three simple choices, including "not sure" with the
  assumption you will then use.

Do not ask about anything already clear from the photos. Common questions
that matter are listed in `references/math-pitfalls.md`. When the user
mentions a file that did not arrive, say so plainly and ask them to
re-attach it. Keep going with work that does not depend on it.

When every ambiguity that changes the mathematics is resolved, or the user
says to proceed, state any remaining assumptions explicitly and move on.

## The quality bar: the course textbook

The course textbook, `Grafneri_tesutyun.pdf` at the repository root, is the
model for how good the paper must be. Its way of presenting a topic is
described in `references/book-style-standard.md`: notation fixed first,
numbered definitions one concept each, a remark after every definition on
what it allows and forbids, an example and a non-example from a labelled
figure, concepts built in strict order, theorems stated in one sentence and
then proved with the method named. The paper follows that pattern and cites
the book's definition numbers where the concept comes from the book. When
the board, the user, or the book disagree on a convention, the paper gives
both and says which one it uses. When the book does not contain a result
the lecture asked about, the paper says so and proves it.

## Phase 3: Teach step by step

Teach the concepts in order from simplest to hardest. Use the graph or
example from the photos when it can be read reliably; otherwise introduce a
small example with three or four elements.

For every important concept, in this order:

1. Simple explanation in one or two short sentences.
2. Formal definition with every symbol defined.
3. Worked example using the photo's example.
4. One short check question for the user.

Do not move quickly. Separate ideas that beginners confuse, and name the
difference explicitly. For graph theory the usual ones are edge, walk, path,
and connected graph; see `references/math-pitfalls.md`.

End the phase by inviting the user to answer the check questions or say
"continue".

## Phase 4: Answer the required questions precisely

Answer each question the lecture or the user asked. For each one give the
precise statement, the reasoning in plain words, and an example. Make sure
the statement is true under the conventions agreed in Phase 2. If a common
textbook statement differs from the course convention, say so.

## Phase 5: Write the paper

Save the paper as `papers/<topic-slug>/paper.md`. Copy the source photos
into `papers/<topic-slug>/sources/` with descriptive names. Do not push
without the user's explicit confirmation.

Structure:

1. Title
2. Introduction, including a "Conventions and assumptions" list that
   defines every symbol and states every assumption made in Phase 2
3. Definitions, numbered, in the book's build order, each followed by a
   remark on what it allows and forbids, an example, and a non-example
4. One section per required question, in the order asked, each with the
   precise statement first and the full argument after it
5. Worked example, consistent with the photos, with every matrix written
   out, plus a failing example where a test is presented
6. Conclusion
7. Appendix: the course terms used, with the book's definition numbers

Formatting:

- Markdown with LaTeX math in `$...$` and `$$...$$`, so the file renders
  on GitHub and pastes into LaTeX.
- Clean text, no emojis, no decorative symbols.
- Number definitions and theorems so later sections can refer to them.
- Every example must agree with its matrix, diagram, or formula. Compute
  every matrix product or numeric claim yourself before writing it.

## Phase 6: Apply the child-friendly writing standard

The paper must stay mathematically exact while being as easy to read as
possible.

- Short sentences. One idea per sentence.
- Explain an unfamiliar word in the sentence where it first appears.
- One new idea at a time.
- Familiar pictures first, such as dots joined by lines, then the formal
  definition.
- Analogies only when they match the mathematics exactly.
- No jargon that the paper does not define.

The result is not childish writing. It is accurate writing with no
unnecessary difficulty.

## Final quality check

Before presenting the paper, run `references/quality-checklist.md` item by
item and fix anything that fails. Report to the user what was checked, what
assumptions the paper states, and what still needs their input, such as a
textbook that did not arrive.

## Testing the skill on another paper

To check an existing paper against its sources, run Phase 1 on the photos
in its `sources/` folder, then compare the paper against the checklist.
Report mismatches between the paper and the photos, any definition that is
not exactly correct, and any sentence a beginner could not follow. Do not
rewrite the paper unless the user asks.

# Writing standard modelled on the course textbook

The course textbook, `Grafneri_tesutyun.pdf` at the repository root, is the
quality bar for every paper. Its style is what a well written mathematics
text looks like to the lecturer who grades the paper. Match it in
structure and rigor; keep the paper's own sentences shorter and plainer.

## How the book presents a topic

Observed in its chapters on graphs, walks, paths, and connectivity.

1. **Notation first.** A section opens with one line fixing the objects:
   "Let G = (V, E) be a graph, u, v in V and e, e' in E." Every later
   definition uses exactly those letters.
2. **Numbered definitions, one concept each.** "Definition 1.2.10",
   "Definition 1.2.11", and so on. The term being defined is set in
   italics inside the sentence. A definition says only what the concept
   is, never why it matters.
3. **A remark right after the definition.** "Note that in a walk both
   vertices and edges may repeat." The remark states what the definition
   allows and forbids, which is where readers go wrong.
4. **An example and a non-example, from a labelled figure.** "The first
   sequence is a walk of G, the second is not." Each example points to a
   figure (Fig. 1.2.5) and names the vertices, so the reader can check it.
5. **Strict build order.** Walk, closed walk, path, simple path, cycle,
   simple cycle, distance. Nothing is used before it is defined, and each
   concept is a small change to the one before it.
6. **Properties as a numbered list.** The three distance axioms are
   listed 1, 2, 3, each one line, followed by the consequence they give.
7. **Lemmas and theorems stated precisely, then proved.** "Lemma 1.2.1"
   has a one sentence statement, the proof names its method ("by
   induction on the length of the walk"), handles the base case, states
   the induction hypothesis, and ends with a proof mark.
8. **Numbered remarks for consequences.** "Remark 2.1.1: a graph is
   connected if and only if it has one connectivity component."
9. **Full matrices for the figure's graph.** The adjacency matrix of the
   example graph is written out entry by entry, so the reader can match
   it to the picture.
10. **Cross references by number.** Later sections cite "Lemma 1.2.2" or
    "Section 1.1" rather than restating.

## What the paper must take from this

- Open with a notation list. Use the board's letters and note the book's
  where they differ.
- Number every definition, theorem, and remark. Cite the book's own
  number next to a definition that comes from it. When the book does not
  contain a result, say so and prove it in the paper.
- After every definition: one remark on what it allows and forbids, one
  example that satisfies it, one that does not.
- Keep the book's build order for the concepts.
- State every theorem in one sentence before the explanation. Give the
  argument in full, in plain words, with the base case and the step named
  when it is an induction.
- Write out every matrix for the worked example and check it against the
  picture.
- Refer back by number instead of repeating.

## Where the paper departs from the book on purpose

The book is written for second year students; the paper is for a beginner
who may not read the notation yet, and its plain-words layer must be
followable by a five-year-old when read aloud. So the paper keeps the
book's rigor and order but adds, before each definition, theorem, and
example, an "In plain words" paragraph told in one concrete story fixed in
the introduction, and explains each new word where it first appears. The
rigor is never reduced; only the reading difficulty is.

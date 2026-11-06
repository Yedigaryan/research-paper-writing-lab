# adjacency-pipeline

- adopted: `composed` (run `harness-runs/adjacency-pipeline`)
- components: 7 references, 7 scripts, 3 agents; 25,635 always-on chars

## Why this was chosen
# Selection: adjacency-pipeline

Selector: paper-evaluator (level 3), fresh, given only select/ (task.md,
source/ with the two whiteboard photos and the course textbook, and
candidates/cand-a to cand-d, the four final papers after their revision
rounds). Mission: the Selector section of references/missions.md.

Unblinded with pool-map.json: cand-a = composed, cand-b = base,
cand-c = inv, cand-d = dom.

Choice: cand-a (composed). Runner-up: cand-d (dom).

## Selector reply, verbatim

I read all four candidates in full. I checked the textbook pages as rendered images: printed pp. 9, 11, 16, 21 (including a zoomed crop of Fig. 1.2.5), 22, 23, 48 and 49, which are PDF pp. 10, 12, 17, 22, 23, 24, 49 and 50. I also viewed whiteboard-1.jpg. I recomputed the following by script:
- the matrices and powers for the board graph, the triangle and the disconnected graph;
- cand-c's Table 3 (walk, trail and path counts on the five-vertex graph): 1/1/1, 1/1/1, 8/3/3, 16/7/3, 72/6/0, 192/6/0, 704/16/0, 2112/0/0, all correct;
- cand-a's appendix walk totals 2052, 72664 and 743680, all correct;
- the counts of connected labelled graphs (1, 1, 4, 38, 728, 26704) and cand-d's 5525 = 5·1105, both correct.

**What the textbook says, as checked on the page images**
- **p. 9:** V is a finite nonempty set, E ⊆ V^(2), and Def 1.1.1 calls (V,E) a graph.
- **p. 11:** Def 1.1.4 (adjacent). A(G) is defined after Def 1.1.6, with a_ii = 0 and a_ij = a_ji.
- **p. 16:** Def 1.2.1 (degree, d_G(v)) and Theorem 1.2.1 (Euler).
- **p. 21:** Fig. 1.2.5. Its edges are v1v2, v1v3, v1v5, v2v3, v2v4, v3v4, v3v5, v4v5, exactly as cand-c lists them.
- **p. 22:** Def 1.2.11 to 1.2.16. Def 1.2.14 is the "closed path or cycle", meaning a closed trail. Def 1.2.15 is the simple cycle. Cn has n ≥ 3. Def 1.2.16 defines distance by the shortest textbook "path", which is a trail. The example sequences all four candidates quote are on this page.
- **p. 23:** The three properties of distance, and Lemma 1.2.1 (for u ≠ v, by induction).
- **p. 48:** Def 2.1.1, and Fig. 2.1.1 (a cycle, a grid, a tree).
- **p. 49:** The equivalence relation, the components, Remark 2.1.1, and Fig. 2.1.2 with four components.

**1. DELIVERY**
- **cand-a:** Answers Q1 (Thm 4.1, all k ≥ 0), Q2 (Thm 5.12 and 5.13) and Q3 (Def 3.17), with conclusion lines 985–1002. It has the connected and disconnected examples (Ex 5.14, 5.15), BFS (§5.5), the mismatch (§6.2), and a full naming table (Table 2, lines 404–423) whose English column is complete. Every definition has a remark, an example and a non-example, and the plain-words layer is complete.
- **cand-b:** Q1 to Q3 are answered (Thm 5.1 for k ≥ 1, Thm 6.10, Def 3.35). However, Table 2 (lines 528–546) leaves the English column as "–" for closed walk, cycle and simple cycle ("we did not check"). That is a gap in the deliverable "three naming conventions in one table". Lemma 6.9 and Thm 6.10 share one plain-words paragraph.
- **cand-c:** Everything is present. Def 2.1 (line 192) carries no textbook number (1.1.1), although the brief asks for the numbers to be cited. Table 2 (line 355) covers only walk, trail and path, with no cycle row.
- **cand-d:** Everything is present, and Table 2 is complete (line 408).

**2. CONFORMANCE**
- **cand-a:** Stays in scope. Directed graphs and multigraphs get one sentence (line 549). The BFS cost remark is a few sentences (lines 881–886). Textbook v_i is mentioned once (line 163), as the brief requires.
- **cand-b:** In scope. It adds component and distance corollaries (6.13 and 6.14), which are allowed.
- **cand-c:** Adds a digression on Euler trails (lines 629–633) and a two-sentence remark on directed graphs (lines 881–883).
- **cand-d:** Uses the textbook's v-labelled sequences about ten times (Non-ex 2.25, Ex 2.32, 2.33, 2.36, 2.37, 2.40, Lemma 3.3). This goes against the brief's "v_i is mentioned once" and gives a first-time reader two vertex notations at once.

**3. FIDELITY**
All four are accurate against the textbook pages listed above.
- **cand-a:** Faithful on Def 1.2.14 and 1.2.15, on distance by trails (Def 3.25), on Lemma 1.2.1, and on Remark 2.1.1 and both figures.
- **cand-b:** Def 3.1 matches p. 9 ("finite nonempty"). Def 3.43 changes distance to "least walk length" while labelling it textbook Def 1.2.16; it does disclose this. The word "trail" rests on Wikipedia "read through a summarising tool" (lines 544–546, 1245).
- **cand-c:** Accurate about Fig. 1.2.5 and its examples. Def 2.21 defines distance by course paths under the 1.2.16 label, with a disclosure. It says no source states the (I+A)^{N-1} form with a proof, which is hedged as "that we read".
- **cand-d:** Accurate, and gives distance by trails as the textbook does.

The source does not settle which meaning of "cycle" the course uses. cand-a and cand-d use the simple cycle; cand-b and cand-c use the textbook's closed trail. All four flag their choice, so this is neutral.

**4. INTERNAL CONSISTENCY**
- **cand-a:** One slip. §1.5 (line 155) says "the power test … not needed for (Q1) to (Q3)", while the Q2 answer includes that test.
- **cand-b:** Convention 2.5 (line 208) says "Plain 'path' always means no repeated vertex". But Def 6.1 (line 889) then uses plain "path" to mean a trail. Remark 4.1 cites "Definition 6.1" as the textbook's definition, which mixes the note's own numbering with the book's.
- **cand-c:** Ex 5.9 (line 757) says "Walks of exactly length 2 cannot use the single edge n1n2". As written this contradicts its own example of the walk n1,n2,n1. The list of uses for Convention 6 (line 139) is incomplete.
- **cand-d:** The answer labels "(A1)", "(A2)" and "(A3)" (lines 56–61) clash with the matrix powers A^1 and A^2, which appear as "(A1)14" in Remark 5.5.

**5. OPERATIONAL FITNESS**
All four are followable, and every proof is written out step by step.
- **cand-a:** The frog and island story is consistent, and there is a reading guide (§1.5).
- **cand-b:** At 23 pages it is the longest.
- **cand-d:** The mixed n/v notation and the A1/A2 labels add friction for a first-time reader. It also hedges Q3 oddly as "best taken as the third question this note has chosen to answer" (line 45), although the brief says the user's assignment asked it.

**6. FINISH**
None has placeholders or broken references. All leak a little of how they were produced:
- cand-a: "prefix m3 … only a label".
- cand-b: "a later independent review of those page images" (line 1235), plus module-named scripts.
- cand-c: m3 script names.
- cand-d: "modules/m3_check.py".

<why>
The pick came down to conformance and internal consistency among papers that all deliver and are all faithful to the textbook. cand-a meets every objective, has a complete three-column naming table, mentions v_i once as the brief requires, and its numbers are verified. Its only flaw is a one-line slip in the reading guide. The runner-up is cand-d. It is equally correct, but it reuses the textbook's v-labelled vertices throughout, against the brief, and its answer labels A1/A2 clash with the matrix powers. cand-b lost on its "path" meaning a trail in Def 6.1 and the unchecked cells in Table 2. cand-c lost on its partial naming table and the missing number on Def 1.1.1.
</why>

```choice
cand-a
```

## What each edit did
component: .claude/skills/research-paper/SKILL.md (Step 1: save the user's words verbatim to sources/user-statements.md, or label the file a summary)
candidates: inv, composed
change: When the paper rests on something the user only said or typed, the orchestrator saves those words with a date in sources/user-statements.md and lists the file in the input inventory, so agents can cite it as a local-file source. If only a summary exists, the file says so and nobody quotes it.
observed: inv never ran the step. No file was created, and the course meaning of "path" still rested on "the user's statement recorded in the brief" (rollouts/inv.md 9545, 9681). Its reader again asked for the assignment to be quoted (inv R1-F3, inv.md 9767). composed did run it. It wrote a file that is explicitly a summary (composed.md 208-231) and cited it as [11] with the note "a summary, not the assignment's own words" (composed.md 3490). The paper's provenance wording then drew reader R1-F4 ("who reported what", composed.md 9556) and was reworded as "as relayed" (composed.md 6994-6995). The base complaint R3-1 (base.md 10696) cannot be compared: the candidates' readers no longer grade severity, and the verbatim text was never available to any run. The selector faulted dom for hedging where Q3 came from (selection.md line 62) and did not fault composed. That contrast is one rollout each and has no trace linking it to this step.
verdict: confounded

component: .claude/skills/research-paper/scripts/check_plain_words.py (new), plus the SKILL.md Step 4 gate line, the paper-author.md `--terms` paragraph and the latex-structure.md description
candidates: inv, composed
change: A study-note checker. It fails when a definition, theorem, lemma, proposition or corollary has no plain-words paragraph before it. It warns about sentences over 20 words, notation, and listed technical words inside plain-words paragraphs. The orchestrator and the author both run it.
observed: The checker ran at every gate in both runs. It reported 0 errors throughout (inv.md 9498, 9566, 9638; composed.md 9850, 9943, 10034). It raised exactly one warning, a 21-word sentence in inv. The author kept that sentence in round 2 (inv.md 8933) and split it in round 3 (inv.md 8370). No evaluator in inv or composed raised a missing-paragraph or sentence-length finding. dom ran without the script and also had none (dom.md 8062-8071, 8148-8158, 8236-8238). The base findings it targets (E1-6, E1-8, E2-3, E3-5; base.md 10527, 10529, 10609, 10687) came from an earlier session with a different reader. Without the script, dom had the same outcome.
verdict: no observed effect

component: .claude/skills/research-paper/SKILL.md (Step 4: technician-reader pre-read of the first draft before round 1)
candidates: inv (dropped by the composer)
change: After the gate passes, the technician reader reads the draft once (round 0), and the author revises before evaluation round 1.
observed: The step ran: 26 findings were all addressed (inv.md 8823-8861, 9702). inv round 1 still had one evaluator major and understandability 4 (inv.md 9508, 9523). dom and composed ran without the pre-read and got the same round-1 result: one major and understandability 4 (dom.md 8049, 8062; composed.md 9860, 9875). All three reached PASS in round 3. The reader's finding counts did not fall after the pre-read: 28, 29 and 39 in inv (inv.md 9532, 9612, 9671), against 20, 28 and 30 in dom and 44, 34 and 47 in composed. inv's round 1 also overlapped a permission stall, and its living author was lost to container restarts in round 2 (process-notes.md; inv.md 9562).
verdict: no observed effect

component: .claude/skills/research-paper/scripts/check_citations.py (year handling), plus the paper-author.md clause "an undated source gets no year field, never n.d." and the matching latex-structure.md line
candidates: inv, composed
change: The base script made a missing year or date an error. The edited script accepts the omission when the evidence source's own year is null, and it rejects a year or date that is not a year, such as "n.d.".
observed: Without the edit, authors filled the field with a placeholder and named the checker as the reason. The base author wrote: "Undated sources still carry year = {n.d.}, because check_citations.py requires a year or date field" (base.md 7081). The base evaluator raised it every round (E1-14, E2-8, E3-6; base.md 10535, 10614, 10688), and the base limitations blame the checker (base.md 10715). On the base script, dom wrote year = {n.d.} "(the checker requires a year or date)" (dom.md 3853, 4753), which produced 6 biber warnings (dom.md 5915) and a reader mention (dom R2-F27, dom.md 8398). With the edit, neither inv nor composed contains "n.d." anywhere. composed's undated Galway and Gotti entries omit the year and carry a "no date" note instead (composed.md 3493-3508). The contrast is 2 runs against 2, and agents state the mechanism in both runs without the edit. The defect itself is minor.
verdict: helped

component: .claude/skills/research-paper/scripts/check_citations.py (uncited-source warning only when live claims rest on the source), plus the paper-author.md paragraph and the latex-structure.md "one entry per cited source" bullet
candidates: inv, composed
change: An uncited evidence source now warns only while a non-removed claim rests on it, with a fix-it message. Otherwise it is a note. The author must cite the source or set its claims to removed in the owning file.
observed: The new path never fired. The strings "claims rest on it" and "supports no live claim" appear in no rollout. inv cited all 7 of its sources from round 1 (inv.md 9498: 7 cited, 7 bib). composed reported 11 keys and 0 errors (composed.md 9848). The composer's attribution of inv's "0 citation warnings" to this edit does not hold. dom ran on the base script and resolved the same kind of finding (E1-F10, uncited Lehman source; dom.md 5049) by round 2 (dom.md 8143). Base left its two uncited sources open in all three rounds (base.md 10536, 10615, 10689), but that was in a different session.
verdict: no observed effect

component: .claude/agents/paper-author.md (grep for a finding's phrase before closing it; composed extends the grep to <paper>/evidence and fixes the claim in its owning file)
candidates: inv (sections, appendices, main.tex), composed (adds evidence)
change: Before closing a finding, the author greps for its phrase and fixes every occurrence, and names the other locations in the per-finding log.
observed: The step ran in both runs. inv: "All edits grepped across sections/, appendices/, main.tex" (inv.md 6155), and "R2-F18 and others were grepped; no other occurrence" (inv.md 8369). composed: "Grepped sections, appendix and evidence for 'counts differ'... no other occurrence", which also found the false sentence still in modules/m1.md, a file the author does not own (composed.md 7336-7341). dom had no grep instruction. There, evidence claim C31 kept old wording after the text fix and became E2-F5 (dom.md 8152). Neither inv nor composed drew a stale-evidence finding. That rests on one rollout per variant, and other components changed at the same time.
verdict: confounded

component: .claude/skills/research-paper/scripts/inspect_pdf.py (median line-count warning), its latex-structure.md line, and the paper-author.md pdftoppm render paragraph
candidates: inv (dropped by the composer)
change: inspect_pdf warns when a page has under 65 percent of the median number of text lines. The author renders each such page with pdftoppm and fixes blank bands.
observed: The checks ran and missed the defect they target. inspect_pdf reported 0 warnings in every round (inv.md 9498, 9566, 9638). The author reported "I rendered the pages at low resolution and saw no blank bands" (inv.md 8882), and in round 2 "I rendered pages 1 to 3 and saw no blank band by Figure 1" (inv.md 8909). Meanwhile the evaluator's blank band under Figure 1 persisted from E1-F8 to E2-F6 and was documented at release (inv.md 9530, 9609, 9665). The render gave the author grounds not to fix the band in round 2. dom and composed had no layout-band finding without the check.
verdict: no observed effect

component: .claude/agents/paper-author.md and .claude/agents/module-owner.md (pointer to the "Facts that are easy to state wrongly" section of math-pitfalls.md)
candidates: dom, composed
change: Authors and module owners are told to read math-pitfalls.md's facts section and to hold every sentence about walks, paths, cycles and the test to it, plain-words paragraphs included.
observed: No rollout records the file being read; the string "math-pitfalls" appears in none. dom had no major mathematics finding, but it still produced two false plain-words sentences, one about the diagonal and one about an isolated vertex (E2-F7, E2-F8; dom.md 8154-8155). composed drew a round-1 major on a walk-versus-path count sentence ("Otherwise the counts differ", E1; composed.md 9875). That sentence came from modules/m1.md (composed.md 7340-7341), and the module owner had the pointer. The composer's note that "no evaluator raised a major mathematics finding" is true of dom only. Base E2-1 (base.md 10607) is the earlier comparison point, in a different session.
verdict: confounded

component: .claude/skills/research-paper/references/math-pitfalls.md (length-0 row plus seven facts from dom; composed rewords the row and adds a diagonal and isolated-vertex bullet)
candidates: dom, composed (revised)
change: Adds a length-0 walk question and facts on: positive entry versus missing path, the single-vertex path, closed trails that are not simple cycles, the reason for (I+A)^(N-1) and its product count, a single power not being a test (the parity reason), and the matrix-product induction step. composed changes the row to "definitions may be silent while later usage assumes it" and adds that the sum test reads off-diagonal entries only.
observed: Results were mixed and there is no read trace. dom's row as written ("The course textbook does not say") fits dom E1-F2 ("textbook silent on length 0", dom.md 8063). But inv, without any length-0 text, made the same claim (inv E1-F2, inv.md 9524), so the claim arises independently. composed carried the repeated-squaring bullet, yet its cost remark omitted repeated squaring (E23, composed.md 10073). composed drew no diagonal or isolated-vertex finding, but that rests on one rollout. The other facts target base findings (E1-3, E3-2, R3-15) from an earlier session whose reader graded severity, and the candidate readers do not.
verdict: confounded

component: .claude/skills/research-paper/references/graph-sources.md (dom: notation, length-0, Def 1.2.14/1.2.16/2.1.1 entries, Galway/Gotti/Bai/Paramadevan detail, Waterloo entry, a "When the paper says one of these sources is wrong" section; composed revises it with the two-reading rule, Paramadevan Theorem 3 credited, Galway as an equality, Bai's path definition, evaluator-viewed pages and a view-before-describing rule, and drops dom's Waterloo entry without recording it)
candidates: dom, composed (revised)
change: Extends the verified-locator file with entries that pass verdicts on sources (wrong, silent, related) and with ready-made counterexamples for critiquing sources.
observed: Authors copied the entries into the paper nearly word for word, in both directions. In dom, entries written loosely came back as findings: "false as stated" (kept from base) became "false as written" in E1-F1, a major (dom.md 5040, 8062); "relates walks of length 2 ... to its degree" became E1-F7 (dom.md 5046); the page list became E2-F6 and the PDF/printed page mix became E2-F4 (dom.md 8151, 8153). In composed, §6.4 reproduces the revised section's structure and counterexamples ((A^2)_11 = 1, B_22 = 2, T_11 = 2; deliverables/composed.md 930-956). It also credits Paramadevan Theorem 3 (deliverables/composed.md 645) and Bai's correct Theorem 2. The round-1 evaluator wrote "Sec. 6.4 correctly refutes" (composed.md 9863), and no critique or crediting finding arose, whereas inv E1-F1 and dom E1-F1 were both majors. composed still drew length-0 attribution slips (E5, E12; composed.md 9879, 9974). The Waterloo drop had no effect: composed found and used the source anyway (composed.md 9836). The positive outcome rests on composed's single rollout, and the quality-checklist item changed at the same time.
verdict: confounded

component: .claude/skills/research-paper/references/quality-checklist.md (source-critique item)
candidates: dom, composed (revised)
change: A sentence saying a source is wrong sits in one discussion item, quotes the statement verbatim with its locator, restates it in the paper's notation, and refutes it with its own counterexample. composed adds a rule: give both readings when the source does not define the word, and credit what the same source states correctly.
observed: dom had the item and still drew E1-F1, the major for calling Paramadevan "false as written" (dom.md 8062). composed's §6.4 follows the revised item: it puts the critique in one optional subsection, gives both readings, and credits Bai's Theorem 2 as correct (deliverables/composed.md 930-956). No critique finding followed. This cannot be separated from the graph-sources revision, which carries the same rule with worked counterexamples, and it is one rollout.
verdict: confounded

component: .claude/agents/paper-author.md (removal of the "Clean text" bullet)
candidates: dom, composed
change: Drops a sentence that latex-structure.md line 40 already carries word for word.
observed: No run raised an emoji, decorative-symbol or jargon-format finding, with or without the bullet.
verdict: no observed effect

## Transferable lesson
- **cue**: A mechanical gate script requires a metadata field (year, date, author, page) that some legitimate sources do not have, such as undated lecture notes or anonymous course files, and agents must pass the gate before evaluation.
- **lesson**: In the gate script (here scripts/check_citations.py), accept a missing field when the source's own evidence record has that field null, and reject placeholder values such as "n.d.", "unknown" or "?" as errors. Add one sentence to paper-author.md saying such a field is omitted, never filled. Check: grep references.bib for the placeholder strings and expect zero hits, with the gate passing.
- **evidence**: The check_citations.py year-handling row is the only one rated helped. Without the edit, base and dom wrote year = {n.d.}, and in both runs the author named the checker as the reason (base.md 7081; dom.md 4753). In base this drew an evaluator finding in every round (E1-14, E2-8, E3-6). With the edit, inv and composed contain no "n.d." at all, and composed's undated Galway and Gotti entries pass with the year left out (composed.md 3493-3508).
- **confidence**: medium. The contrast is 2 runs against 2, and the agents state the mechanism in both runs without the edit. Each candidate still has only one rollout, the base run comes from an earlier session, and the defect it removes is minor, so how much it matters is low even if the effect is real.

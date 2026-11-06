# Reflection: adjacency-pipeline

Reflector: harness-reflector, given context/ (base tree, pool/inv,
pool/dom, pool/composed, all four rollouts), composer-notes.md,
selection.md, and process-notes.md. Selected label: composed.

## Reflector reply, verbatim

<edits>
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
</edits>

<experience>
cue: A mechanical gate script requires a metadata field (year, date, author, page) that some legitimate sources do not have, such as undated lecture notes or anonymous course files, and agents must pass the gate before evaluation.
lesson: In the gate script (here scripts/check_citations.py), accept a missing field when the source's own evidence record has that field null, and reject placeholder values such as "n.d.", "unknown" or "?" as errors. Add one sentence to paper-author.md saying such a field is omitted, never filled. Check: grep references.bib for the placeholder strings and expect zero hits, with the gate passing.
evidence: The check_citations.py year-handling row is the only one rated helped. Without the edit, base and dom wrote year = {n.d.}, and in both runs the author named the checker as the reason (base.md 7081; dom.md 4753). In base this drew an evaluator finding in every round (E1-14, E2-8, E3-6). With the edit, inv and composed contain no "n.d." at all, and composed's undated Galway and Gotti entries pass with the year left out (composed.md 3493-3508).
confidence: medium. The contrast is 2 runs against 2, and the agents state the mechanism in both runs without the edit. Each candidate still has only one rollout, the base run comes from an earlier session, and the defect it removes is minor, so how much it matters is low even if the effect is real.
</experience>

Three corrections to the composer's notes (/home/user/research-paper-writing-lab/harness-runs/adjacency-pipeline/composer-notes.md):
- The composed graph-sources.md silently drops dom's Waterloo CS 341 entry. The drop is not recorded among the composer's kept, revised and dropped decisions.
- inv's "0 citation warnings" is credited to the uncited-source edit, but that warning path never fired in any run.
- "No major mathematics finding" holds for dom only; composed had one (E1).

Base's INCOMPLETE against PASS in every candidate run can't be attributed to the harness. Base was blocked partly by reader majors (R3-1, R3-15), and the candidate runs' reader, which sits outside the harness, no longer grades severity, so its findings cannot block release.

The selector picked composed and ranked dom second for reasons that trace to no edit. composed's naming table was complete and it mentions v_i only once. dom used v-labelled sequences and had the A1/A2 label clash.

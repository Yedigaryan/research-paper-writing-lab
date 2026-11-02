# Reflection

Reflector: harness-reflector (level 3), fresh agent, given compose/ and the selected label `dom`.

<edits>
component: .claude/skills/research-paper/SKILL.md
candidates: inv, composed
change: Step 2 now says to commit evidence.base.json. The Step 4 gate adds check_evidence_rebuild.py and check_self_evaluation.py. Step 6 now requires reports/ files and "## Round n" headings in reader-findings.md, confirmed by check_round_record.py. (The true base was reconstructed from dom's untouched copy, because context harness/ was edited in place by the composer and now holds the composed tree.)
observed: In both the inv and composed runs the orchestrator ran the extended gate, everything passed on the first submission, and nothing went back to the author (inv evaluation report, "Mechanical checks"; composed evaluation report, the same section). The dom run used the base SKILL and still saved reports/paper-author-round1.md and the evaluator and reader reports. It also wrote reader-findings.md under a round heading and got a clean rebuild ("base plus fragments reproduced the old merged file exactly", dom paper-author-round1). Research did not run in any probe, so the Step 2 sentence was never exercised.
verdict: no observed effect

component: .claude/skills/research-paper/scripts/check_evidence_rebuild.py
candidates: inv, composed
change: New script. It rebuilds the merged evidence file from evidence.base.json plus the fragments and diffs the result against evidence.json. It has an --init-base fallback that stops after two passes.
observed: It reported 0 differences in inv (paper-author-round1) and in composed ("base file plus 4 fragments with 0 differences"). Without the script, the dom author also left evidence.json alone and rebuilt it correctly. The hand-edit failure it targets, base E18, happened in a revision round of a base run that predates the base-file fix, and no probe ran a revision round.
verdict: no observed effect

component: .claude/skills/research-paper/scripts/check_self_evaluation.py
candidates: inv, composed
change: New script. It fails when a section file that main.tex inputs has no heading in self-evaluation.md.
observed: It reported 13 inputs and 0 errors in both inv and composed. Without the script, dom's self-evaluation also covered all eight sections and the appendices (dom release condition 9 "holds"). The failure it targets (base round 3, condition 9 only "partially met") came from a revision round, and no probe ran one.
verdict: no observed effect

component: .claude/skills/research-paper/scripts/check_round_record.py
candidates: inv, composed
change: New script. It lists the round-record files that are missing (reports, reader findings, round headings).
observed: The records were complete in inv and composed, and also in dom, which did not have the script. In the base run, "no reports/ folder" and "reader-findings.md not present" belong to an earlier run, not to these probes.
verdict: no observed effect

component: .claude/skills/research-paper/scripts/inspect_pdf.py
candidates: inv, composed
change: Adds a --text-out option, plus a paper-author paragraph telling the author to read build/main.txt once and fix defects that only show in the compiled text.
observed: Only the authors' own reports show an effect. The inv author reported "One real fix: the Theorem 4.15 paragraph had confused which source gave which proof". The composed author fixed lower-case cross-references and reworded two sentences. Dom had no such pass, and its evaluator raised one defect that shows in the printed text: F7, where "(5)" reads as an equation reference. No evaluator in inv or composed raised a defect of that kind. That rests on one rollout each and on self-reports, with many other components changed at the same time.
verdict: confounded

component: .claude/agents/paper-author.md (revision procedure, per-file self-evaluation headings, Revision log)
candidates: inv, composed
change: Revisions use the smallest edit, reopen changed lines with git diff against main.txt, and grep any reused word to check it keeps one meaning. The self-evaluation has one heading per file with a final "## Revision log".
observed: Every probe was a single author pass with no revision round, so the revision procedure never ran. The per-file headings showed up in inv and composed, and dom's base-worded file was also per-section.
verdict: no observed effect

component: .claude/skills/research-paper/references/graph-sources.md (new; read pointer added as item 6 in agents/paper-author.md)
candidates: dom, composed (composed revised it)
change: A triggered reference file of verified textbook locators, build order and source attributions. The composed version narrows the Proposition 2.9.10 scope, lists the seven edges of Fig. 1.2.5, hedges the Kirchhoff page, and adds facts about the Schost slides, Paramadevan and the board.
observed: The textbook's degree definition (Definition 1.2.1 and Theorem 1.2.1, p. 16) was cited in both runs that had the file and missing in both that did not. The dom author added A1 and A2 "since graph-sources.md says the textbook defines degree". The composed author added author-1. Base round 1 missed it (E1), and the inv author wrote "The textbook's own definition of degree ... were never recorded" (inv F1). The author also copies wrong entries: dom's entry "Proposition 2.9.10 ... is the walk, trail, path equivalence" reappeared in the dom paper and was caught as F9. With composed's corrected entry the error did not recur (composed evaluator: "Proposition 2.9.10 (walk iff path)" checks out). The file is not enough on its own: composed still called the Galway notes "Quinlan's" (F4) although the file says not to name an author. Composed listed the seven Fig. 1.2.5 edges before first use and drew no edge-list finding, while base (R10, R29), inv (reader F7) and dom (F17) all did, but that rests on composed's single rollout.
verdict: helped

component: .claude/agents/module-owner.md
candidates: dom, composed
change: Adds a pointer to graph-sources.md for modules that cite the textbook or a graph-theory source.
observed: All three probes used the same module reports as fixed inputs ("Research and modules were final inputs to this probe"), so module-owner never ran in any probe.
verdict: no observed effect

component: .claude/skills/research-paper/references/quality-checklist.md
candidates: dom (nine items), composed (kept two: keep pipeline material out of the reader's text; answer a definition question by pointing to its definition)
change: Dom added items on attribution matching, checking "source lacks X" sentences, reported text outside quotation marks, one meaning per word and letter, matrix entries as counts, a story dictionary, keeping pipeline material out, meeting scope limits literally, and answering definition questions by pointing.
observed: Dom repeated the failures its own items name. It had the lowest internal-consistency score of any run (3), with "loop", "length", S, n and t clashes (F2 to F5), even though the evaluator quoted the one-meaning rule. Scope overrun F12 repeated base E10, and attribution errors F1 (major), F9 and F10 still occurred. On the two items composed kept: pipeline-leak findings appeared in base round 1 (E9, R2, R3) and inv (reader F8, F34, F35) but not in dom or composed. Yet dom's reader still flagged "as reported to us" (R1), and composed's reader still struggled with the Q3 section (F20 and the closing summary).
verdict: confounded

component: .claude/skills/research-paper/references/book-style-standard.md
candidates: dom, composed
change: Says to show the kind of each statement through its environment and attribution, and forbids inventing bracketed status labels.
observed: Base round 1 (R2, "[interpretation, qualified]") and inv (22 parenthetical tags; reader F4) used tag systems. Dom and composed did not. In composed the hedging moved into prose instead ("as an interpretation of how the proof works", reader F13; stacked qualifications, F9 and F20). There is no agent trace linking the change to the rule, and the evidence is one rollout per candidate.
verdict: confounded

component: .claude/skills/research-paper/references/evidence-schema.md
candidates: inv, composed
change: Adds a pointer to check_evidence_rebuild.py.
observed: Same as the script row: the dom run rebuilt correctly without it.
verdict: no observed effect

component: .claude/skills/research-paper/references/latex-structure.md
candidates: inv (evidence.base.json layout line), composed (that line, plus a local-file bibliography `note` that no longer says "supplied by the user")
change: Documents the base evidence file. The composed version also drops the instruction that put "supplied by the user" into references.bib.
observed: The layout line had no observable effect. The bibliography wording follows the instruction text: base, inv and dom all printed "Supplied by the user" in the reference list (dom F14, even though dom also had the checklist item against an unintroduced "the user"), and composed did not. Only the composed rollout carries the change.
verdict: confounded
</edits>

<experience>
cue: The paper must cite a fixed primary source (a course textbook, a standard, a manual) by its own numbers and pages, and an earlier run's evaluator has already verified locators or source scopes that the authoring agents missed or overstated. Examples: a definition the paper said the source lacks, or a cited proposition credited with more than it covers.
lesson: Record those verified facts in a triggered reference file (references/<domain>-sources.md), and point paper-author.md and module-owner.md to it as something to read when the paper cites that source. Copy each entry from the verifier's finding with its exact scope, stating what it covers and what it does not, never as a paraphrase. Authors copy these entries into the paper, so before adopting the file, check every entry against the finding it came from.
evidence: graph-sources.md row. The degree definition was cited in dom and composed, which had the file (the dom author names the file as the reason), and missing in base round 1 (E1) and inv (F1), which did not. Dom's overstated entry "walk, trail, path equivalence" went into the paper verbatim and was caught as F9. Composed's corrected entry did not recur. Counter-case: composed still misattributed the Galway notes (F4) despite the file, so the file does not guarantee compliance.
confidence: low. There is one rollout per candidate, and the composed orchestrator ran on a different session model. The base comparison point is a first draft from an earlier harness. The degree contrast is only 2 runs against 2, though one trajectory states the mechanism directly, and propagation of a wrong entry is shown once.
</experience>

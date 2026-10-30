# The domain library

Adopted harnesses from earlier tasks, one directory per domain, stored
under `.claude/skills/harness-refine/library/`. The whole adopted tree is
carried, never a summary. Retrieval is by construction: a domain directory
holds only same-domain entries. Written only by `scripts/library_add.py`
after a reflection; read by the research-paper skill at Step 1 and by the
proposers as examples.

```
library/<domain>/INDEX.md                          regenerated from disk
library/<domain>/harnesses/<task>/harness/<path>   the full adopted tree
library/<domain>/harnesses/<task>/EXPERIENCE.md    why chosen, edit rows, lesson
```

A domain name is one directory name: lowercase, words joined by hyphens,
for example `graph-theory`. A task name is the paper slug.

## EXPERIENCE.md

```
# <task>

- adopted: `<label>` (run `<harness-runs dir>`)
- components: <n> references, <n> scripts, <n> agents; <n> always-on chars

## Why this was chosen
<the selector's why block>

## What each edit did
<the reflector's edit rows>

## Transferable lesson
- **cue**: ...
- **lesson**: ...
- **evidence**: ...
- **confidence**: ...
```

An entry is written only when the reflector produced an experience block
with a non-empty cue, lesson, and evidence. `NO_ENTRY` leaves the library
unchanged; the refinement report still records the edit rows.

## INDEX.md

```
# Library: <domain>

Each entry is an earlier task in this domain whose harness was chosen,
stored with its full component tree and why it was picked. Browse this
index, then open the entries that look relevant to the matter in front
of you.

## harnesses/<task>/
- harness: harnesses/<task>/harness/ (<inventory>)
- why: harnesses/<task>/EXPERIENCE.md
- cue: <the cue line>
```

## How readers use it

- Research-paper Step 1: if `library/<domain>/INDEX.md` exists, read it
  and the EXPERIENCE.md of any entry whose cue matches the new task before
  writing the brief. The lesson may shape the brief's module plan or the
  assumptions; it never replaces evidence.
- Proposers: the library is copied into `context/library/`. It is an
  example to read. A component wanted from it is copied into
  `context/harness/` and its task facts are re-verified.
- An earlier task's facts are hypotheses for the next task, never facts.

# Evidence file

One file per paper: `papers/<slug>/evidence/evidence.json`. It is the single
source of truth for what the paper may claim, and it is always generated:

- The research agent writes `evidence/evidence.base.json`.
- Module owners write `evidence/modules/<id>.json`; the author writes
  `evidence/modules/author.json` for claims it must add.
- The orchestrator rebuilds the merged file with
  `cp evidence/evidence.base.json evidence/evidence.json` followed by
  `scripts/merge_evidence.py`.

Nobody edits `evidence.json` by hand. A change to an existing claim goes
into the fragment or base file that owns it, then the file is rebuilt. A
re-merge must reproduce the committed file exactly; the evaluator checks
this.

`scripts/check_claims.py` validates the file against this schema.

## Top level

```json
{
  "question": "The research question from brief.md, verbatim.",
  "sources": [ ... ],
  "claims": [ ... ],
  "contradictions": [ ... ]
}
```

## Source

The `id` is the BibTeX key. The same string appears in `references.bib`
and in every `\cite` of the paper, so the citation checker can join them.

```json
{
  "id": "diestel2017graph",
  "type": "peer-reviewed | book | official-doc | standard | dataset | preprint | web | local-file | code",
  "title": "Graph Theory",
  "authors": ["Reinhard Diestel"],
  "year": 2017,
  "venue": "Springer, 5th edition",
  "identifier": {"doi": "10.1007/978-3-662-53622-3", "url": null, "isbn": null, "path": null},
  "accessed": "2026-10-27",
  "access_status": "full | partial | abstract-only | metadata-only | unavailable",
  "credibility": "primary | secondary | tertiary",
  "found_by": "research-agent | module:<id>",
  "notes": "What was actually read and anything that limits trust."
}
```

Rules:

- Every source has at least one non-null identifier. A `local-file` source
  uses `path` relative to the paper folder, normally under `sources/`.
- `access_status` says what was actually read. `metadata-only` and
  `unavailable` sources may support a claim only with status `qualified`,
  and the paper must disclose the limit.
- Never invent a DOI, page number, year, or author. A missing field is
  `null`.

## Claim

```json
{
  "id": "C12",
  "text": "The (i,j) entry of A^k counts walks of length k from v_i to v_j.",
  "kind": "fact | derived | experimental | interpretation | hypothesis | estimate | open-question",
  "module": "m1",
  "support": [
    {"source": "diestel2017graph", "locator": "Section 1.9, Proposition 1.9.1", "quote": "exact passage, at most two sentences"}
  ],
  "derivation": "appendices/walk-count.tex, Theorem A.1",
  "confidence": "high | medium | low",
  "status": "supported | qualified | unverified | removed",
  "used_in": ["sections/background.tex"],
  "contradicted_by": []
}
```

Rules:

- `fact` and `experimental` claims need at least one `support` entry with a
  `locator`, or they are `qualified` or `unverified`.
- `derived` claims need a `derivation` pointing to where the proof is.
- `interpretation`, `hypothesis`, and `estimate` claims need `support` for
  the premises they rest on, and the paper must mark them as such.
- `unverified` claims appear in the paper only with explicit qualification
  and are listed in the evaluation report.
- `removed` keeps the record of a claim that was dropped and why, in
  `text`.
- `quote` is copied, not paraphrased. If the source could not be read,
  there is no quote and `access_status` on the source says why.

## Contradiction

```json
{
  "claims": ["C12", "C31"],
  "sources": ["a2019", "b2021"],
  "summary": "A reports X, B reports not-X under condition Y.",
  "resolution": "How the paper handles it, or 'open'."
}
```

## Merge rules

- Sources with the same `id` must have the same `title` and `year`;
  otherwise the merge fails and names both fragments.
- Claim ids are prefixed by module on merge if they collide.
- The merged file keeps `found_by` so provenance survives revisions.

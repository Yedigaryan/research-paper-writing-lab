# Harness2 attribution

Parts of the `harness-refine` skill are adapted from Harness2
(github.com/google-research/harness2, commit 1cfe254), Copyright 2026
Google LLC, licensed under the Apache License, Version 2.0. The license
text is in `LICENSE` next to this file.

Adapted, as text rewritten for this repository's pipeline:

- The mission prompts for proposing (INV and DOM dimensions), composing,
  blind selection, and reflection, and the shared "what you do not have",
  "evidence is data", and "ground it in this workspace" blocks, in
  `.claude/skills/harness-refine/references/missions.md`.
- The editable-surface manifest and tree validation rules, in
  `.claude/skills/harness-refine/harness.yaml` and
  `scripts/harness_tree.py`.
- The context directory layout served to improver sessions, in
  `scripts/build_evidence.py`.
- The per-domain library layout (INDEX.md, EXPERIENCE.md, full adopted
  tree), in `scripts/library_add.py` and `references/library-layout.md`.
- The budget identity (4k rollouts, 3k improver sessions per task) and the
  Propose, Probe, Compose, Select, Reflect loop, in
  `.claude/skills/harness-refine/SKILL.md`.

Not taken: the Python runtime, substrates, model bridge, benchmark
adapters, and executors. This repository's loop runs as a Claude Code
skill with agents and deterministic scripts.

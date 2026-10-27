# Repository rules for Claude Code

## Git

- Work on the `claude/*` branch assigned to the session.
- After every commit on a `claude/*` branch, push it immediately with
  `git push -u origin <branch>`. No confirmation is needed for this; the
  repository owner authorized it here.
- Never push to `main` or to any branch outside `claude/*` without the
  user's explicit confirmation in the conversation.
- Never rewrite published history (rebase, amend, force-push) on a branch
  that has already been pushed, unless the user asks for it.

## Writing

- Clean, copyable text in README, LaTeX, and skill files: no emojis, no
  decorative symbols.
- Keep every `SKILL.md` body under 500 lines. Reference files stay one
  level deep from `SKILL.md`.

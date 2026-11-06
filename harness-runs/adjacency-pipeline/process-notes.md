# Process notes: adjacency-pipeline

Running record of the whole-pipeline refinement step. The refinement
report draws on it at the end.

Base commit: 3aa1ca7. Probes run one at a time, from Thursday 2026-11-05,
at the user's request. Every probe orchestrator is pinned to the same
session model; agent models come from each candidate's frontmatter.

## Rollouts

| Label | Session | Started (UTC) | Finished (UTC) | Rounds | Decision | Last commit | Cost (USD, API equivalent) |
|---|---|---|---|---|---|---|---|
| base | earlier run | | | 3 | INCOMPLETE | | 21.37 |
| inv | session_01V3X5px4ShXGvaa9cTb4xGT | 2026-11-05 10:46 | 2026-11-05 22:52 | 3 | PASS | b4a5dd7 | 20.26 |
| dom | session_01V3X5pzCTTYKai69Mbmmzz1 | 2026-11-06 14:57 | | | | | |

## Confounds

- inv: from 11:21 to about 11:50 UTC on 2026-11-05 the paper-author
  subagent was stopped at a permission prompt. A safety check blocks
  `rm -f $D/*.png` because the variable is unguarded, and nobody was
  present to approve it. The orchestrator interrupted the probe. The run
  then went on to a PASS in round 3. The interrupt may have cut off one
  author tool call in round 1.
- dom and later probes: the prompt gets one extra paragraph saying that
  nobody is watching and that `rm` must use a literal path or
  `"${VAR:?}"`. This is a process instruction, not harness content, but
  inv did not receive it.
- The scheduled start fired at 08:07 UTC. A worker restart delayed the
  inv session to 10:46. The dom probe began a day later, after the
  orchestrator session was idle.

#!/usr/bin/env python3
"""Copy deliverables into <context_dir>/candidates/ under shuffled ids for blind selection.

    anonymize_pool.py <context_dir> --map <path_outside_context> [--seed N] \\
                      <label>=<deliverable.md> [<label>=<deliverable.md> ...]

The id map (which id came from which label) is written to --map, which must
lie outside the context directory, so the selector never sees it. Ids carry
no information about order or origin. With --seed the shuffle is repeatable.

Adapted from the blind-selection step of google-research/harness2 (Apache 2.0).
"""

from __future__ import annotations

import argparse
import json
import random
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import harness_tree as ht  # noqa: E402


def anonymize(context: Path, items: dict[str, Path], map_path: Path, seed: int | None) -> dict:
    context = context.resolve()
    map_path = map_path.resolve()
    if map_path == context or context in map_path.parents:
        raise ValueError("the id map must be written outside the context directory")
    if len(items) < 2:
        raise ValueError("blind selection needs at least two candidates")
    for label, path in items.items():
        if not path.is_file():
            raise ValueError(f"{label}: deliverable {path} is not a file")

    rng = random.Random(seed) if seed is not None else random.SystemRandom()
    ids = [f"cand-{c}" for c in "abcdefghijklmnopqrstuvwxyz"[: len(items)]]
    rng.shuffle(ids)
    dest = context / "candidates"
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    mapping = {}
    for cid, (label, path) in zip(ids, sorted(items.items())):
        body = path.read_text(encoding="utf-8", errors="replace")
        body = _strip_label(body, label, cid)
        (dest / f"{cid}.md").write_text(body, encoding="utf-8")
        mapping[cid] = {"label": label, "source": str(path)}
    map_path.parent.mkdir(parents=True, exist_ok=True)
    map_path.write_text(json.dumps(mapping, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    manifest = ht.load_manifest()
    ht.assert_no_leak_paths(context, manifest["leak_globs"])
    return mapping


def _strip_label(body: str, label: str, cid: str) -> str:
    """The deliverable header names its run label; replace it with the blind id."""
    return body.replace(f"`{label}`", f"`{cid}`").replace(f"Deliverable {label}", f"Deliverable {cid}")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("context")
    ap.add_argument("--map", required=True)
    ap.add_argument("--seed", type=int, default=None)
    ap.add_argument("items", nargs="+", help="label=path pairs")
    args = ap.parse_args(argv)
    items: dict[str, Path] = {}
    for it in args.items:
        if "=" not in it:
            print(f"bad item {it!r}; expected label=path")
            return 2
        label, path = it.split("=", 1)
        items[label] = Path(path)
    try:
        mapping = anonymize(Path(args.context), items, Path(args.map), args.seed)
    except ValueError as exc:
        print(f"REFUSED: {exc}")
        return 1
    print(f"{len(mapping)} candidates written to {args.context}/candidates; map at {args.map}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

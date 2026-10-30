#!/usr/bin/env python3
"""Store one adopted harness in the domain library and rebuild its INDEX.md.

    library_add.py <domain> <task> --tree <tree_dir> --label <label> \\
                   --why <file> --reflection <file> [--run <dir>] [--library <dir>]
    library_add.py <domain> --rebuild-index [--library <dir>]

`--reflection` is the reflector's final message: an <edits> block and either
an <experience> block or the line NO_ENTRY. With NO_ENTRY, or an experience
block missing cue, lesson, or evidence, nothing is stored and the exit code
is 1; the refinement report keeps the edit rows.

The tree is validated against the live base before it is stored.
Adapted from the library layout of google-research/harness2 (Apache 2.0).
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import harness_tree as ht  # noqa: E402

LIBRARY = Path(__file__).resolve().parents[1] / "library"
FIELDS = ("cue", "lesson", "evidence", "confidence")


def domain_dir(domain: str) -> str:
    name = re.sub(r"[^a-z0-9]+", "-", domain.strip().lower()).strip("-")
    if not name:
        raise ValueError("domain name is empty after normalisation")
    return name


def parse_reflection(text: str) -> tuple[str, dict[str, str] | None]:
    """Return (edit rows, experience fields or None for NO_ENTRY)."""
    m = re.search(r"<edits>\s*(.*?)\s*</edits>", text, re.S)
    edits = m.group(1).strip() if m else ""
    m = re.search(r"<experience>\s*(.*?)\s*</experience>", text, re.S)
    if not m:
        return edits, None
    fields: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            k = k.strip().lower()
            if k in FIELDS:
                fields[k] = v.strip()
    if not all(fields.get(k) for k in ("cue", "lesson", "evidence")):
        return edits, None
    return edits, fields


def inventory(tree: ht.Tree) -> str:
    c = ht.census(tree)
    return (
        f"{c['references']} references, {c['scripts']} scripts, {c['agents']} agents; "
        f"{c['always_on_chars']:,} always-on chars"
    )


def add(domain: str, task: str, tree: ht.Tree, *, label: str, why: str, edits: str,
        experience: dict[str, str], run: str = "", library: Path = LIBRARY) -> Path:
    manifest = ht.load_manifest()
    ht.validate(tree, manifest, ht.live_tree(manifest))
    low = (why + edits + " ".join(experience.values())).lower()
    for phrase in manifest["forbidden_phrases"]:
        if str(phrase).lower() in low:
            raise ValueError(f"experience text contains forbidden phrase {phrase!r}")
    d = library / domain_dir(domain) / "harnesses" / task
    if (d / "harness").exists():
        shutil.rmtree(d / "harness")
    ht.write_tree(tree, d / "harness")
    lines = [
        f"# {task}",
        "",
        f"- adopted: `{label}`" + (f" (run `{run}`)" if run else ""),
        f"- components: {inventory(tree)}",
        "",
    ]
    if why.strip():
        lines += ["## Why this was chosen", why.strip(), ""]
    if edits.strip():
        lines += ["## What each edit did", edits.strip(), ""]
    lines += ["## Transferable lesson"]
    lines += [f"- **{f}**: {experience[f]}" for f in FIELDS if experience.get(f)]
    lines.append("")
    (d / "EXPERIENCE.md").write_text("\n".join(lines), encoding="utf-8")
    rebuild_index(domain, library)
    return d


def _field(path: Path, name: str) -> str:
    if not path.is_file():
        return ""
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith(f"- **{name}**:"):
            return line.split(":", 1)[1].strip()
    return ""


def rebuild_index(domain: str, library: Path = LIBRARY) -> Path:
    d = library / domain_dir(domain)
    rows = [
        f"# Library: {domain_dir(domain)}",
        "",
        "Each entry is an earlier task in this domain whose harness was chosen,",
        "stored with its full component tree and why it was picked. Browse this",
        "index, then open the entries that look relevant to the matter in front",
        "of you.",
        "",
    ]
    hd = d / "harnesses"
    names = sorted(p.name for p in hd.iterdir() if p.is_dir()) if hd.is_dir() else []
    if not names:
        rows.append("(empty: this is the first task in this domain)")
    for name in names:
        ed = hd / name
        tree, _ = ht.read_tree(ed / "harness")
        rows += [
            f"## harnesses/{name}/",
            f"- harness: harnesses/{name}/harness/ ({inventory(tree)})",
            f"- why: harnesses/{name}/EXPERIENCE.md",
        ]
        cue = _field(ed / "EXPERIENCE.md", "cue")
        if cue:
            rows.append(f"- cue: {cue}")
        rows.append("")
    d.mkdir(parents=True, exist_ok=True)
    (d / "INDEX.md").write_text("\n".join(rows), encoding="utf-8")
    return d / "INDEX.md"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("domain")
    ap.add_argument("task", nargs="?")
    ap.add_argument("--tree")
    ap.add_argument("--label", default="")
    ap.add_argument("--why", help="file holding the selector's why block")
    ap.add_argument("--reflection", help="file holding the reflector's final message")
    ap.add_argument("--run", default="", help="the harness-runs directory of this step")
    ap.add_argument("--library", default=str(LIBRARY))
    ap.add_argument("--rebuild-index", action="store_true")
    args = ap.parse_args(argv)
    library = Path(args.library)

    if args.rebuild_index:
        print(f"index written: {rebuild_index(args.domain, library)}")
        return 0
    if not (args.task and args.tree and args.reflection):
        ap.error("task, --tree and --reflection are required unless --rebuild-index")

    edits, experience = parse_reflection(Path(args.reflection).read_text(encoding="utf-8"))
    if experience is None:
        print("NO_ENTRY: the reflection carries no transferable lesson; library unchanged")
        return 1
    tree, _ = ht.read_tree(Path(args.tree))
    why = Path(args.why).read_text(encoding="utf-8") if args.why else ""
    try:
        d = add(args.domain, args.task, tree, label=args.label, why=why, edits=edits,
                experience=experience, run=args.run, library=library)
    except ValueError as exc:
        print(f"REFUSED: {exc}")
        return 1
    print(f"library entry written: {d}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

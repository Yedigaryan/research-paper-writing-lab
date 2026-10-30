#!/usr/bin/env python3
"""Export, validate, diff, and install the editable research-paper harness tree.

A tree is the set of files the refinement loop may edit, as declared in
harness.yaml next to this script. On disk a tree is a directory holding those
files at their repository-relative paths.

    harness_tree.py export  <dest_dir>            copy the live tree out of the repo
    harness_tree.py validate <tree_dir> [--base B] check a tree; exit 1 listing problems
    harness_tree.py diff    <a> <b> [--json]      compare two trees ("repo" = live tree)
    harness_tree.py install <tree_dir>            validate, then write the tree into the repo
    harness_tree.py census  <tree_dir>            one-line inventory

Validation rules (every one is a reason to reject a candidate before it runs):
  off-surface or reserved file; frozen frontmatter line changed; required file
  missing; SKILL.md body over the line cap; missing or mismatched frontmatter;
  a reference or script that is named but not shipped; a script that does not
  compile; a forbidden phrase; an emoji or decorative symbol.

Adapted from the tree validation ideas in google-research/harness2 (Apache 2.0).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MANIFEST = HERE.parent / "harness.yaml"
REPO = HERE.parents[3]

Tree = dict[str, str]


# --- manifest -----------------------------------------------------------------


def load_manifest(path: Path = MANIFEST) -> dict:
    """Read the YAML subset used by harness.yaml: scalars and lists of scalars."""
    data: dict = {}
    key: str | None = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].rstrip() if not raw.lstrip().startswith('"') else raw.rstrip()
        if not line.strip():
            continue
        if line.startswith("- ") or line.startswith("  - "):
            if key is None:
                raise ValueError(f"{path}: list item before any key: {raw!r}")
            data.setdefault(key, [])
            if not isinstance(data[key], list):
                raise ValueError(f"{path}: {key} mixes scalar and list")
            data[key].append(_scalar(line.split("- ", 1)[1]))
            continue
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if not m:
            raise ValueError(f"{path}: cannot parse line {raw!r}")
        key, value = m.group(1), m.group(2).strip()
        data[key] = _scalar(value) if value else []
    for field in ("editable", "reserved"):
        if not data.get(field):
            raise ValueError(f"{path}: `{field}` must list at least one path")
    data.setdefault("frozen_frontmatter", [])
    data.setdefault("forbidden_phrases", [])
    data.setdefault("leak_globs", [])
    data["skill_body_max_lines"] = int(data.get("skill_body_max_lines", 500))
    return data


def _scalar(text: str):
    text = text.strip()
    if len(text) >= 2 and text[0] == text[-1] and text[0] in "\"'":
        return text[1:-1]
    if re.fullmatch(r"-?\d+", text):
        return int(text)
    return text


def glob_re(pattern: str) -> re.Pattern:
    """`*` and `?` never cross a slash; `**` matches any number of path parts."""
    out = []
    i = 0
    while i < len(pattern):
        c = pattern[i]
        if pattern.startswith("**/", i):
            out.append("(?:.*/)?")
            i += 3
        elif pattern.startswith("**", i):
            out.append(".*")
            i += 2
        elif c == "*":
            out.append("[^/]*")
            i += 1
        elif c == "?":
            out.append("[^/]")
            i += 1
        else:
            out.append(re.escape(c))
            i += 1
    return re.compile("".join(out) + r"\Z")


def matches_any(rel: str, patterns: list[str]) -> bool:
    return any(glob_re(p).match(rel) for p in patterns)


def required_files(manifest: dict) -> list[str]:
    return [p for p in manifest["editable"] if not any(ch in p for ch in "*?")]


# --- trees --------------------------------------------------------------------


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def live_tree(manifest: dict, repo: Path = REPO) -> Tree:
    """Every file in the repository that the manifest marks editable."""
    tree: Tree = {}
    for p in sorted(repo.rglob("*")):
        if not p.is_file() or ".git" in p.parts:
            continue
        rel = p.relative_to(repo).as_posix()
        if matches_any(rel, manifest["editable"]) and not matches_any(rel, manifest["reserved"]):
            tree[rel] = _read(p)
    return tree


def read_tree(d: Path) -> tuple[Tree, list[str]]:
    """Read a tree directory. Returns (files, every relative path found)."""
    files: Tree = {}
    for p in sorted(d.rglob("*")):
        if p.is_file() and ".git" not in p.parts:
            files[p.relative_to(d).as_posix()] = _read(p)
    return files, sorted(files)


def write_tree(tree: Tree, dest: Path) -> int:
    for rel, body in tree.items():
        out = dest / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(body, encoding="utf-8")
    return len(tree)


def resolve_tree(spec: str, manifest: dict, repo: Path = REPO) -> Tree:
    if spec == "repo":
        return live_tree(manifest, repo)
    tree, _ = read_tree(Path(spec))
    return tree


# --- validation ---------------------------------------------------------------

_FM = re.compile(r"\A---\n(.*?)\n---\n?", re.S)
_EMOJI = re.compile(
    "[\U0001F000-\U0001FAFF\U0001FB00-\U0001FFFF☀-➿⭐⭕✅❌✔✖]"
)
_REF_MENTION = re.compile(r"references/([A-Za-z0-9_.\-]+\.md)")
_SCRIPT_MENTION = re.compile(r"scripts/([A-Za-z0-9_.\-]+\.(?:py|sh))")


def frontmatter(src: str) -> tuple[dict[str, str], str]:
    m = _FM.match(src)
    if not m:
        return {}, src
    fields: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fields[k.strip()] = v.strip()
    return fields, src[m.end():]


def validate(tree: Tree, manifest: dict, base: Tree | None = None) -> dict:
    """Raise ValueError listing every problem; return a census of a valid tree."""
    errs: list[str] = []
    editable, reserved = manifest["editable"], manifest["reserved"]

    for rel in tree:
        if matches_any(rel, reserved):
            errs.append(f"{rel}: reserved file; the loop may not touch the yardstick")
        elif not matches_any(rel, editable):
            errs.append(f"{rel}: off the editable surface declared in harness.yaml")

    for rel in required_files(manifest):
        if rel not in tree:
            errs.append(f"{rel}: required file missing from the tree")

    skill_dir = ""
    for rel, src in tree.items():
        if rel.endswith("/SKILL.md"):
            skill_dir = rel.rsplit("/", 1)[0]
            name = skill_dir.rsplit("/", 1)[-1]
            fm, body = frontmatter(src)
            if fm.get("name") != name:
                errs.append(f"{rel}: frontmatter `name:` must be `{name}`")
            if not fm.get("description"):
                errs.append(f"{rel}: frontmatter needs a `description:`")
            n = len(body.splitlines())
            cap = manifest["skill_body_max_lines"]
            if n > cap:
                errs.append(f"{rel}: body is {n} lines, over the {cap} line cap")
            for ref in set(_REF_MENTION.findall(src)):
                if f"{skill_dir}/references/{ref}" not in tree and not _reserved_ref(
                    f"{skill_dir}/references/{ref}", manifest
                ):
                    errs.append(f"{rel}: names references/{ref} but the tree does not ship it")
        elif rel.startswith(".claude/agents/") and rel.endswith(".md"):
            name = rel.rsplit("/", 1)[-1][:-3]
            fm, _ = frontmatter(src)
            if fm.get("name") != name:
                errs.append(f"{rel}: frontmatter `name:` must be `{name}`")
            if not fm.get("description"):
                errs.append(f"{rel}: frontmatter needs a `description:`")
            if base is not None and rel in base:
                bfm, _ = frontmatter(base[rel])
                for field in manifest["frozen_frontmatter"]:
                    if fm.get(field) != bfm.get(field):
                        errs.append(
                            f"{rel}: frontmatter `{field}:` is frozen "
                            f"({bfm.get(field)!r} in the base, {fm.get(field)!r} here)"
                        )

    if skill_dir:
        shipped = {rel for rel in tree if rel.startswith(f"{skill_dir}/scripts/")}
        for rel, src in tree.items():
            if not (rel.endswith(".md")):
                continue
            for script in set(_SCRIPT_MENTION.findall(src)):
                want = f"{skill_dir}/scripts/{script}"
                if want not in shipped:
                    errs.append(f"{rel}: invokes scripts/{script} but the tree does not ship it")

    for rel, src in tree.items():
        if rel.endswith(".py"):
            try:
                compile(src, rel, "exec")
            except (SyntaxError, ValueError) as exc:
                errs.append(f"{rel}: does not compile: {type(exc).__name__}: {exc}"[:200])
        elif rel.endswith(".sh"):
            r = subprocess.run(["bash", "-n"], input=src, text=True, capture_output=True)
            if r.returncode != 0:
                errs.append(f"{rel}: bash -n failed: {r.stderr.strip()[:160]}")

    phrases = [str(p).lower() for p in manifest["forbidden_phrases"]]
    for rel, src in tree.items():
        low = src.lower()
        for phrase in phrases:
            if phrase in low:
                errs.append(f"{rel}: contains forbidden phrase {phrase!r}")
        m = _EMOJI.search(src)
        if m:
            errs.append(f"{rel}: contains an emoji or decorative symbol U+{ord(m.group(0)):04X}")

    if errs:
        raise ValueError("\n".join(sorted(set(errs))))
    return census(tree)


def _reserved_ref(rel: str, manifest: dict) -> bool:
    """A reserved reference (rubric, model levels) may be named without being shipped."""
    return matches_any(rel, manifest["reserved"])


def census(tree: Tree) -> dict:
    skill = [rel for rel in tree if rel.endswith("/SKILL.md")]
    body_lines = 0
    if skill:
        _, body = frontmatter(tree[skill[0]])
        body_lines = len(body.splitlines())
    agents = [rel for rel in tree if rel.startswith(".claude/agents/")]
    return {
        "files": len(tree),
        "skill_body_lines": body_lines,
        "references": sum(1 for rel in tree if "/references/" in rel),
        "scripts": sum(1 for rel in tree if "/scripts/" in rel),
        "agents": len(agents),
        "always_on_chars": sum(len(tree[rel]) for rel in skill + agents),
    }


# --- diff and install -----------------------------------------------------------


def diff_trees(before: Tree, after: Tree) -> dict:
    out = {"added": [], "removed": [], "modified": []}
    for rel in sorted(set(after) - set(before)):
        out["added"].append({"path": rel, "lines": len(after[rel].splitlines())})
    for rel in sorted(set(before) - set(after)):
        out["removed"].append({"path": rel, "lines": len(before[rel].splitlines())})
    for rel in sorted(set(before) & set(after)):
        if before[rel] != after[rel]:
            a, b = before[rel].splitlines(), after[rel].splitlines()
            out["modified"].append({"path": rel, "lines_before": len(a), "lines_after": len(b)})
    out["unchanged"] = len(before) == len(after) and not any(
        out[k] for k in ("added", "removed", "modified")
    )
    return out


def install(tree: Tree, manifest: dict, repo: Path = REPO) -> dict:
    base = live_tree(manifest, repo)
    validate(tree, manifest, base)
    d = diff_trees(base, tree)
    for item in d["removed"]:
        (repo / item["path"]).unlink()
    for rel, body in tree.items():
        out = repo / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(body, encoding="utf-8")
    return d


def assert_no_leak_paths(root: Path, patterns: list[str]) -> None:
    """Refuse a context directory that holds an answer-key path."""
    hits = []
    for p in root.rglob("*"):
        if p.is_file():
            rel = p.relative_to(root).as_posix()
            if matches_any(rel, [str(x) for x in patterns]):
                hits.append(rel)
    if hits:
        raise ValueError("answer-key path(s) would enter model context: " + ", ".join(sorted(hits)[:8]))


# --- cli --------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", default=str(REPO), help="repository root (default: this checkout)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("export"); s.add_argument("dest")
    s = sub.add_parser("validate"); s.add_argument("tree"); s.add_argument("--base", default="repo")
    s = sub.add_parser("diff"); s.add_argument("a"); s.add_argument("b"); s.add_argument("--json", action="store_true")
    s = sub.add_parser("install"); s.add_argument("tree")
    s = sub.add_parser("census"); s.add_argument("tree")
    args = ap.parse_args(argv)
    manifest = load_manifest()
    repo = Path(args.repo).resolve()

    if args.cmd == "export":
        tree = live_tree(manifest, repo)
        n = write_tree(tree, Path(args.dest))
        print(f"exported {n} files to {args.dest}")
        return 0

    if args.cmd == "validate":
        tree = resolve_tree(args.tree, manifest, repo)
        base = resolve_tree(args.base, manifest, repo)
        try:
            c = validate(tree, manifest, base)
        except ValueError as exc:
            print("INVALID TREE")
            print(exc)
            return 1
        print("valid tree: " + ", ".join(f"{k} {v}" for k, v in c.items()))
        return 0

    if args.cmd == "diff":
        d = diff_trees(resolve_tree(args.a, manifest, repo), resolve_tree(args.b, manifest, repo))
        if args.json:
            print(json.dumps(d, indent=2))
        else:
            for item in d["added"]:
                print(f"added     {item['path']} (+{item['lines']} lines)")
            for item in d["removed"]:
                print(f"removed   {item['path']} (-{item['lines']} lines)")
            for item in d["modified"]:
                print(f"modified  {item['path']} ({item['lines_before']} -> {item['lines_after']} lines)")
            if d["unchanged"]:
                print("no differences")
        return 0

    if args.cmd == "install":
        tree, _ = read_tree(Path(args.tree))
        try:
            d = install(tree, manifest, repo)
        except ValueError as exc:
            print("REFUSED: tree is invalid against the live base")
            print(exc)
            return 1
        print(
            f"installed: {len(d['added'])} added, {len(d['removed'])} removed, "
            f"{len(d['modified'])} modified"
        )
        return 0

    if args.cmd == "census":
        print(json.dumps(census(resolve_tree(args.tree, manifest, repo)), indent=2))
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())

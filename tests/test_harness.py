#!/usr/bin/env python3
"""Tests for the harness-refine scripts. No model calls. Run: python3 tests/test_harness.py"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / ".claude" / "skills" / "harness-refine" / "scripts"
sys.path.insert(0, str(SCRIPTS))
import anonymize_pool  # noqa: E402
import harness_tree as ht  # noqa: E402
import library_add  # noqa: E402

PAPER = ROOT / "papers" / "adjacency-walks-connectivity"
AUTHOR = ".claude/agents/paper-author.md"
SKILL = ".claude/skills/research-paper/SKILL.md"


class TreeTests(unittest.TestCase):
    def setUp(self):
        self.manifest = ht.load_manifest()
        self.base = ht.live_tree(self.manifest)

    def test_live_tree_is_valid_and_complete(self):
        c = ht.validate(dict(self.base), self.manifest, self.base)
        self.assertIn(SKILL, self.base)
        self.assertIn(AUTHOR, self.base)
        self.assertNotIn(".claude/agents/paper-evaluator.md", self.base)
        self.assertNotIn(".claude/skills/research-paper/references/rubric.md", self.base)
        self.assertEqual(c["agents"], 3)
        self.assertLessEqual(c["skill_body_lines"], 500)

    def _rejects(self, tree, needle):
        with self.assertRaises(ValueError) as cm:
            ht.validate(tree, self.manifest, self.base)
        self.assertIn(needle, str(cm.exception))

    def test_reserved_file_rejected(self):
        t = dict(self.base)
        t[".claude/agents/paper-evaluator.md"] = self.base[AUTHOR]
        self._rejects(t, "reserved")

    def test_off_surface_file_rejected(self):
        t = dict(self.base)
        t[".claude/agents/new-agent.md"] = "---\nname: new-agent\ndescription: x\n---\n"
        self._rejects(t, "off the editable surface")

    def test_nested_reference_rejected(self):
        t = dict(self.base)
        t[".claude/skills/research-paper/references/deep/more.md"] = "x\n"
        self._rejects(t, "off the editable surface")

    def test_frozen_frontmatter_rejected(self):
        t = dict(self.base)
        t[AUTHOR] = self.base[AUTHOR].replace("model: sonnet", "model: opus", 1)
        self._rejects(t, "frozen")
        t[AUTHOR] = self.base[AUTHOR].replace("tools: Read,", "tools: WebSearch, Read,", 1)
        self._rejects(t, "frozen")

    def test_required_file_missing_rejected(self):
        t = dict(self.base)
        del t[SKILL]
        self._rejects(t, "required file missing")

    def test_skill_body_cap(self):
        t = dict(self.base)
        t[SKILL] = self.base[SKILL] + "\n" * 600
        self._rejects(t, "line cap")

    def test_forbidden_phrase(self):
        t = dict(self.base)
        t[AUTHOR] = self.base[AUTHOR] + "\nWrite what the evaluator expects.\n"
        self._rejects(t, "forbidden phrase")

    def test_emoji_rejected(self):
        t = dict(self.base)
        t[AUTHOR] = self.base[AUTHOR] + "\nDone ✅\n"
        self._rejects(t, "emoji")

    def test_broken_script_rejected(self):
        t = dict(self.base)
        t[".claude/skills/research-paper/scripts/check_claims.py"] = "def (:\n"
        self._rejects(t, "does not compile")
        t = dict(self.base)
        t[".claude/skills/research-paper/scripts/build.sh"] = "if [ ; then\n"
        self._rejects(t, "bash -n failed")

    def test_unshipped_script_or_reference_rejected(self):
        t = dict(self.base)
        t[SKILL] = self.base[SKILL] + "\nRun scripts/missing_tool.py first.\n"
        self._rejects(t, "scripts/missing_tool.py")
        t = dict(self.base)
        t[SKILL] = self.base[SKILL] + "\nSee references/nowhere.md.\n"
        self._rejects(t, "references/nowhere.md")

    def test_reserved_reference_may_be_named(self):
        t = dict(self.base)
        t[SKILL] = self.base[SKILL] + "\nSee references/rubric.md and references/model-levels.md.\n"
        ht.validate(t, self.manifest, self.base)

    def test_diff(self):
        t = dict(self.base)
        t[AUTHOR] = self.base[AUTHOR] + "\nOne more rule.\n"
        del t[".claude/skills/research-paper/references/math-pitfalls.md"]
        t[".claude/skills/research-paper/references/new.md"] = "# New\n"
        d = ht.diff_trees(self.base, t)
        self.assertEqual([x["path"] for x in d["modified"]], [AUTHOR])
        self.assertEqual([x["path"] for x in d["removed"]], [".claude/skills/research-paper/references/math-pitfalls.md"])
        self.assertEqual([x["path"] for x in d["added"]], [".claude/skills/research-paper/references/new.md"])
        self.assertTrue(ht.diff_trees(self.base, dict(self.base))["unchanged"])

    def test_export_validate_install_cli(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            repo = tmp / "repo"
            shutil.copytree(ROOT / ".claude", repo / ".claude")
            tree_dir = tmp / "tree"
            run = lambda *a: subprocess.run(
                [sys.executable, str(SCRIPTS / "harness_tree.py"), "--repo", str(repo), *a],
                text=True, capture_output=True,
            )
            r = run("export", str(tree_dir))
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            r = run("validate", str(tree_dir))
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            # edit the candidate, then install it
            author = tree_dir / AUTHOR
            author.write_text(author.read_text() + "\nAdded by the test.\n")
            (tree_dir / ".claude/skills/research-paper/references/math-pitfalls.md").unlink()
            r = run("diff", "repo", str(tree_dir))
            self.assertIn("modified  " + AUTHOR, r.stdout)
            r = run("install", str(tree_dir))
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            self.assertIn("Added by the test.", (repo / AUTHOR).read_text())
            self.assertFalse((repo / ".claude/skills/research-paper/references/math-pitfalls.md").exists())
            self.assertTrue((repo / ".claude/agents/paper-evaluator.md").exists())
            # an invalid candidate is refused and leaves the repo untouched
            (tree_dir / ".claude/agents/paper-evaluator.md").write_text("---\nname: paper-evaluator\ndescription: x\n---\n")
            before = (repo / ".claude/agents/paper-evaluator.md").read_text()
            r = run("install", str(tree_dir))
            self.assertEqual(r.returncode, 1)
            self.assertIn("REFUSED", r.stdout)
            self.assertEqual(before, (repo / ".claude/agents/paper-evaluator.md").read_text())


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        if not PAPER.is_dir():
            self.skipTest("adjacency paper not present")

    def _run(self, *a):
        return subprocess.run(
            [sys.executable, str(SCRIPTS / "build_evidence.py"), *a], text=True, capture_output=True
        )

    def test_rollout_pool_and_leak_check(self):
        with tempfile.TemporaryDirectory() as tmp:
            ctx = Path(tmp) / "context"
            r = self._run("rollout", str(PAPER), "--label", "base", "--out", str(ctx))
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            self.assertTrue((ctx / "task.md").read_text().strip())
            self.assertTrue(any((ctx / "source").iterdir()))
            traj = (ctx / "rollouts" / "base.md").read_text()
            self.assertIn("# Commits", traj)
            self.assertIn("## Round 1", traj)
            self.assertIn("self-evaluation.md", traj)
            deliv = (ctx / "deliverables" / "base.md").read_text()
            self.assertIn("pages", deliv.splitlines()[2])
            self.assertGreater(len(deliv), 10_000)
            self.assertTrue((ctx / "harness" / SKILL).is_file())
            self.assertFalse((ctx / "harness" / ".claude/agents/paper-evaluator.md").exists())
            self.assertTrue((ctx / "LAYOUT.md").is_file())
            # deterministic
            r2 = self._run("rollout", str(PAPER), "--label", "base", "--out", str(ctx))
            self.assertEqual(r2.returncode, 0)
            self.assertEqual(traj, (ctx / "rollouts" / "base.md").read_text())
            # pool
            r = self._run("pool", str(ctx), "--label", "inv", "--tree", str(ctx / "harness"))
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            self.assertTrue((ctx / "pool" / "inv" / "harness" / AUTHOR).is_file())
            # leak
            (ctx / "source" / "expected-findings.md").write_text("E1 ...\n")
            r = self._run("check", str(ctx))
            self.assertEqual(r.returncode, 1)
            self.assertIn("LEAK", r.stdout)

    def test_anonymize(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            ctx = tmp / "context"
            ctx.mkdir()
            items = {}
            for label in ("base", "inv", "dom"):
                p = tmp / f"{label}.md"
                p.write_text(f"# Deliverable `{label}`\n\nbody of {label}\n")
                items[label] = p
            mapping = anonymize_pool.anonymize(ctx, items, tmp / "map.json", seed=7)
            ids = sorted((ctx / "candidates").glob("*.md"))
            self.assertEqual(len(ids), 3)
            self.assertEqual(set(mapping), {p.stem for p in ids})
            self.assertEqual(sorted(v["label"] for v in mapping.values()), ["base", "dom", "inv"])
            for cid, v in mapping.items():
                body = (ctx / "candidates" / f"{cid}.md").read_text()
                self.assertIn(f"`{cid}`", body)
                self.assertNotIn(f"`{v['label']}`", body)
            self.assertTrue(json.loads((tmp / "map.json").read_text()))
            with self.assertRaises(ValueError):
                anonymize_pool.anonymize(ctx, items, ctx / "map.json", seed=7)
            with self.assertRaises(ValueError):
                anonymize_pool.anonymize(ctx, {"base": items["base"]}, tmp / "m2.json", seed=7)


REFLECTION = """\
<edits>
component: .claude/agents/paper-author.md
candidates: inv, composed
change: added a rule to state the term convention before the first theorem
observed: rollout inv had no terminology finding in round 1; base had R12
verdict: confounded
</edits>

<experience>
cue: two sources define the same word differently
lesson: make paper-author state the convention before the first theorem
evidence: edit row 1; base R12 versus inv round 1
confidence: low, one rollout
</experience>
"""


class LibraryTests(unittest.TestCase):
    def test_parse_reflection(self):
        edits, exp = library_add.parse_reflection(REFLECTION)
        self.assertIn("component: .claude/agents/paper-author.md", edits)
        self.assertEqual(exp["cue"], "two sources define the same word differently")
        edits, exp = library_add.parse_reflection(REFLECTION.split("<experience>")[0] + "NO_ENTRY\n")
        self.assertTrue(edits)
        self.assertIsNone(exp)
        _, exp = library_add.parse_reflection("<experience>\ncue: x\nlesson: y\n</experience>")
        self.assertIsNone(exp)

    def test_add_and_index(self):
        manifest = ht.load_manifest()
        base = ht.live_tree(manifest)
        with tempfile.TemporaryDirectory() as tmp:
            lib = Path(tmp) / "library"
            edits, exp = library_add.parse_reflection(REFLECTION)
            d = library_add.add("Graph Theory", "adjacency", base, label="inv", why="<why>\nclearer\n</why>",
                                edits=edits, experience=exp, run="harness-runs/adjacency", library=lib)
            self.assertTrue((d / "harness" / AUTHOR).is_file())
            text = (d / "EXPERIENCE.md").read_text()
            self.assertIn("- **cue**: two sources", text)
            index = (lib / "graph-theory" / "INDEX.md").read_text()
            self.assertIn("harnesses/adjacency/", index)
            self.assertIn("cue: two sources", index)
            with self.assertRaises(ValueError):
                library_add.add("graph-theory", "t2", base, label="x", why="what the evaluator expects",
                                edits="", experience=exp, library=lib)
            (Path(tmp) / "r.md").write_text("<edits>\n</edits>\nNO_ENTRY\n")
            r = subprocess.run(
                [sys.executable, str(SCRIPTS / "library_add.py"), "graph-theory", "t3", "--tree", str(d / "harness"),
                 "--reflection", str(Path(tmp) / "r.md"), "--library", str(lib)],
                text=True, capture_output=True,
            )
            self.assertEqual(r.returncode, 1)
            self.assertIn("NO_ENTRY", r.stdout)
            self.assertFalse((lib / "graph-theory" / "harnesses" / "t3").exists())


if __name__ == "__main__":
    unittest.main(verbosity=1)

import contextlib
import datetime
import io
import os
import subprocess
import tempfile
import unittest
from unittest import mock

import repo_check

HERE = os.path.dirname(os.path.abspath(__file__))
FIXTURES = os.path.join(HERE, "fixtures")
TODAY = datetime.date(2026, 10, 20)


def run(name):
    return repo_check.check(os.path.join(FIXTURES, name), today=TODAY)


def write_tree(root, files):
    for rel, content in files.items():
        path = os.path.join(root, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(content)


def check_files(files, **kwargs):
    kwargs.setdefault("today", TODAY)
    with tempfile.TemporaryDirectory() as root:
        write_tree(root, files)
        return repo_check.check(root, **kwargs)


class ReferenceTests(unittest.TestCase):
    def test_broken_ref_reports_line_and_closest_path(self):
        errors, _, _ = run("closest_path")
        self.assertEqual(
            errors,
            [
                '01-knowledge-base/doc.md:4: broken path "04-active-work/prds/alfa/prd.md".'
                " Fix: point it at 04-active-work/prds/alpha/prd.md or remove the reference.",
                '01-knowledge-base/doc.md:4: broken path "04-active-work/prds/alpha/prdd.md".'
                " Fix: point it at 04-active-work/prds/alpha/prd.md or remove the reference.",
            ],
        )

    def test_renamed_roadmap_items_folder_is_caught(self):
        errors, scanned, _ = run("roadmap_items_rename")
        doc = "01-knowledge-base/processes/ai-agent-operations.md"
        self.assertEqual(scanned, 5)
        self.assertEqual(len(errors), 5)
        for error, line in zip(errors, (3, 5, 8, 9, 10)):
            self.assertTrue(error.startswith("%s:%d: broken path" % (doc, line)), error)
            self.assertIn("04-active-work/roadmap-items/", error)
            self.assertTrue(error.endswith("Fix: update the path or remove the reference."), error)

    def test_placeholders_are_skipped(self):
        errors, scanned, checked = run("placeholders")
        self.assertEqual((errors, scanned, checked), ([], 1, 0))

    def test_external_anchor_absolute_and_unrelated_tokens_are_skipped(self):
        errors, _, checked = run("external_and_anchors")
        self.assertEqual((errors, checked), ([], 0))

    def test_paths_resolve_from_root_and_from_doc_directory(self):
        errors, _, _ = run("resolves")
        self.assertEqual(
            errors,
            [
                '.claude/skills/demo/SKILL.md:4: broken path "04-active-work/prds/gamma/prd.md".'
                " Fix: update the path or remove the reference."
            ],
        )

    def test_percent_20_and_angle_wrapped_spaces_resolve(self):
        errors, _, checked = run("encoded_spaces")
        self.assertEqual(checked, 4)
        self.assertEqual(len(errors), 1)
        self.assertIn('doc.md:6: broken path "04-active-work/Other File.md"', errors[0])
        self.assertIn("point it at 04-active-work/Some File.md", errors[0])

    def test_resolution_is_case_sensitive(self):
        errors, _, _ = run("case_mismatch")
        self.assertEqual(len(errors), 1)
        self.assertIn('broken path "04-active-work/Readme.md"', errors[0])
        self.assertIn("point it at 04-active-work/README.md", errors[0])


class ScopeTests(unittest.TestCase):
    def test_skipped_directories_are_not_scanned(self):
        errors, scanned, _ = run("skipped_dirs")
        self.assertEqual((errors, scanned), ([], 1))


class ExceptionTests(unittest.TestCase):
    def test_exception_with_reason_and_future_date_is_honoured(self):
        errors, _, _ = run("exception_honoured")
        self.assertEqual(len(errors), 1)
        self.assertIn('doc.md:8: broken path "04-active-work/planned/three.md"', errors[0])

    def test_expired_exception_is_an_error_and_does_not_suppress(self):
        errors, _, _ = run("exception_expired")
        self.assertEqual(len(errors), 2)
        self.assertTrue(errors[0].startswith("doc.md:3: exception expired on 2000-01-01."), errors[0])
        self.assertTrue(errors[1].startswith('doc.md:4: broken path "04-active-work/planned/one.md"'), errors[1])

    def test_exception_is_valid_through_its_until_date(self):
        root = os.path.join(FIXTURES, "exception_expired")
        self.assertEqual(repo_check.check(root, today=datetime.date(2000, 1, 1))[0], [])
        self.assertEqual(len(repo_check.check(root, today=datetime.date(2000, 1, 2))[0]), 2)

    def test_malformed_exceptions_are_errors(self):
        errors, _, _ = run("exception_invalid")
        messages = [e for e in errors if "broken path" not in e]
        self.assertEqual(len(messages), 4)
        self.assertIn("doc.md:3: exception has no reason.", messages[0])
        self.assertIn("doc.md:5: exception has no valid until date.", messages[1])
        self.assertIn("doc.md:7: exception has no valid until date.", messages[2])
        self.assertIn("doc.md:9: unknown repo-check directive.", messages[3])
        self.assertEqual(len(errors) - len(messages), 3)


class SuggestionTests(unittest.TestCase):
    def fix_for(self, target, files, doc="04-active-work/prds/reflex/overview.md"):
        tree = dict(files)
        tree[doc] = "`%s`\n" % target if "/" in target and not target.startswith(".") else "[x](%s)\n" % target
        errors = check_files(tree).errors
        self.assertEqual(len(errors), 1, errors)
        return errors[0].split("Fix: ")[1]

    def test_deleted_sibling_target_never_suggests_a_different_file_in_the_directory(self):
        fix = self.fix_for("./phased-plan.md", {"04-active-work/prds/reflex/prd.md": "# PRD\n"})
        self.assertEqual(fix, "update the path or remove the reference.")

    def test_bare_name_whose_target_moved_to_a_differently_named_file_gets_no_suggestion(self):
        files = {"04-active-work/prds/fin-email-auth-data-policy/prd.md": "# PRD\n"}
        fix = self.fix_for("fin-email-auth-data-policy-prd.md", files)
        self.assertEqual(fix, "update the path or remove the reference.")

    def test_unique_file_with_the_same_basename_elsewhere_is_suggested(self):
        fix = self.fix_for("04-active-work/old/phased-plan.md", {"04-active-work/prds/reflex/phased-plan.md": "# P\n"})
        self.assertEqual(fix, "point it at 04-active-work/prds/reflex/phased-plan.md or remove the reference.")

    def test_suggestion_for_a_relative_reference_is_relative_to_the_doc(self):
        fix = self.fix_for("../old/phased-plan.md", {"04-active-work/research/phased-plan.md": "# P\n"})
        self.assertEqual(fix, "point it at ../../research/phased-plan.md or remove the reference.")

    def test_basename_shared_by_several_files_is_ambiguous_and_not_suggested(self):
        files = {"04-active-work/a/prd.md": "# A\n", "04-active-work/b/prd.md": "# B\n"}
        self.assertEqual(self.fix_for("04-active-work/c/prd.md", files), "update the path or remove the reference.")

    def test_similar_basename_is_suggested_at_point_eight_and_not_below(self):
        near = {"04-active-work/prds/reflex/phased-plans.md": "# P\n"}
        far = {"04-active-work/prds/reflex/phased-roadmap.md": "# P\n"}
        self.assertEqual(
            self.fix_for("04-active-work/old/phased-plan.md", near),
            "point it at 04-active-work/prds/reflex/phased-plans.md or remove the reference.",
        )
        self.assertEqual(self.fix_for("04-active-work/old/phased-plan.md", far), "update the path or remove the reference.")


class ExceptionScopeTests(unittest.TestCase):
    def marker(self, until="2026-11-01", keyword="ignore"):
        return '<!-- repo-check: %s reason="planned" until=%s -->' % (keyword, until)

    def test_marker_on_its_own_line_covers_only_the_next_line(self):
        doc = "\n".join(
            [
                self.marker(),
                "`04-active-work/a.md` `04-active-work/b.md`",
                "`04-active-work/c.md`",
            ]
        )
        errors, _, _ = check_files({"doc.md": doc})
        self.assertEqual(len(errors), 1)
        self.assertIn('doc.md:3: broken path "04-active-work/c.md"', errors[0])

    def test_trailing_marker_covers_only_its_own_line(self):
        doc = "\n".join(
            [
                "`04-active-work/a.md` " + self.marker(),
                "`04-active-work/b.md`",
            ]
        )
        errors, _, _ = check_files({"doc.md": doc})
        self.assertEqual(len(errors), 1)
        self.assertIn('doc.md:2: broken path "04-active-work/b.md"', errors[0])

    def test_until_accepts_only_strict_iso_dates(self):
        for until in ("20261101", "2026-1-5", "2026-11-01T00:00", "2026-13-01", "２０２６-１１-０１"):
            errors, _, _ = check_files({"doc.md": self.marker(until) + "\n`04-active-work/a.md`\n"})
            self.assertEqual(len(errors), 2, until)
            self.assertIn("no valid until date", errors[0], until)

    def test_until_is_capped_at_180_days(self):
        latest = TODAY + datetime.timedelta(days=180)
        ok, _, _ = check_files({"doc.md": self.marker(latest.isoformat()) + "\n`04-active-work/a.md`\n"})
        self.assertEqual(ok, [])
        late = (latest + datetime.timedelta(days=1)).isoformat()
        errors, _, _ = check_files({"doc.md": self.marker(late) + "\n`04-active-work/a.md`\n"})
        self.assertEqual(len(errors), 2)
        self.assertIn("more than 180 days", errors[0])
        self.assertIn(latest.isoformat(), errors[0])

    def test_keyword_must_be_exactly_ignore(self):
        errors, _, _ = check_files({"doc.md": self.marker(keyword="ignoreall") + "\n`04-active-work/a.md`\n"})
        self.assertEqual(len(errors), 2)
        self.assertIn("unknown repo-check directive", errors[0])

    def test_marker_text_inside_a_code_span_is_not_a_marker(self):
        doc = "Write `%s` above a line.\n" % self.marker(keyword="allow")
        self.assertEqual(check_files({"doc.md": doc})[0], [])

    def test_backticked_path_inside_a_marker_is_not_checked(self):
        doc = '<!-- repo-check: ignore reason="see `04-active-work/x.md`" until=2026-11-01 -->\ntext\n'
        self.assertEqual(check_files({"doc.md": doc})[0], [])


class CommandLineTests(unittest.TestCase):
    def invoke(self, name):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = repo_check.main(["--root", os.path.join(FIXTURES, name)])
        return code, out.getvalue().splitlines()

    def test_exit_code_is_one_with_errors(self):
        code, lines = self.invoke("closest_path")
        self.assertEqual(code, 1)
        self.assertEqual(lines[-1], "repo-check: 2 error(s), 2 docs scanned, 2 references checked.")

    def test_exit_code_is_zero_when_clean(self):
        code, lines = self.invoke("placeholders")
        self.assertEqual(code, 0)
        self.assertEqual(lines, ["repo-check: ok, 1 docs scanned, 0 references checked."])


GIT_ENV = {
    key: value
    for key, value in os.environ.items()
    if key not in ("GIT_DIR", "GIT_INDEX_FILE", "GIT_WORK_TREE", "GIT_PREFIX")
}
GIT_ENV.update(
    GIT_AUTHOR_NAME="t",
    GIT_AUTHOR_EMAIL="t@example.com",
    GIT_COMMITTER_NAME="t",
    GIT_COMMITTER_EMAIL="t@example.com",
    GIT_CONFIG_NOSYSTEM="1",
)


def git(root, *args, **kwargs):
    return subprocess.run(
        ["git", "-c", "commit.gpgsign=false", "-c", "init.defaultBranch=main", "-C", root] + list(args),
        env=GIT_ENV,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        **kwargs
    )


class ScratchRepo(object):
    def __init__(self, files):
        self.dir = tempfile.TemporaryDirectory()
        self.root = self.dir.name
        git(self.root, "init", "-q").check_returncode()
        self.write(files)
        self.commit()

    def write(self, files):
        write_tree(self.root, files)

    def stage(self, *paths):
        git(self.root, "add", "--", *paths).check_returncode()

    def commit(self):
        git(self.root, "add", "-A").check_returncode()
        git(self.root, "commit", "-q", "-m", "base").check_returncode()

    def errors(self, **kwargs):
        return repo_check.check(self.root, today=TODAY, **kwargs).errors

    def cleanup(self):
        self.dir.cleanup()


BASE = {
    "04-active-work/target.md": "# Target\n",
    "01-knowledge-base/clean.md": "# Clean\n",
    "01-knowledge-base/other.md": "# Other\n",
}


class TrackedFilesTests(unittest.TestCase):
    def setUp(self):
        self.repo = ScratchRepo(BASE)
        self.addCleanup(self.repo.cleanup)

    def test_untracked_target_is_broken_so_local_and_ci_agree(self):
        self.repo.write(
            {"04-active-work/new.md": "# New\n", "01-knowledge-base/doc.md": "`04-active-work/new.md`\n"}
        )
        self.repo.stage("01-knowledge-base/doc.md")
        errors = self.repo.errors()
        self.assertEqual(len(errors), 1)
        self.assertIn('doc.md:1: broken path "04-active-work/new.md"', errors[0])

    def test_tracked_target_resolves(self):
        self.repo.write({"01-knowledge-base/clean.md": "`04-active-work/target.md`\n"})
        self.assertEqual(self.repo.errors(), [])

    def test_target_deleted_from_the_working_tree_is_broken(self):
        self.repo.write({"01-knowledge-base/clean.md": "`04-active-work/target.md`\n"})
        os.remove(os.path.join(self.repo.root, "04-active-work/target.md"))
        self.assertEqual(len(self.repo.errors()), 1)


class DirectoryReferenceTests(unittest.TestCase):
    TREE = {"04-active-work/prds/alpha/prd.md": "# Alpha\n", ".claude/skills/demo/SKILL.md": "# Demo\n"}

    def check_doc(self, text, **kwargs):
        files = dict(self.TREE)
        files["01-knowledge-base/doc.md"] = text
        return check_files(files, **kwargs).errors

    def test_directory_that_no_longer_exists_is_caught(self):
        errors = self.check_doc("Drafts live in `04-active-work/roadmap-items/` today.\n")
        self.assertEqual(
            errors,
            ['01-knowledge-base/doc.md:1: broken path "04-active-work/roadmap-items/". Fix: update the path or remove the reference.'],
        )

    def test_existing_directory_resolves_from_a_code_span_and_a_link(self):
        text = "`04-active-work/prds/` and [prds](04-active-work/prds/alpha/) and `.claude/skills/`\n"
        self.assertEqual(self.check_doc(text), [])

    def test_only_repo_directories_are_checked(self):
        text = "`somewhere/else/` `~/Downloads/` `https://example.com/a/` `/etc/` `src/`\n"
        self.assertEqual(self.check_doc(text), [])

    def test_numbered_top_level_name_is_checked_even_when_the_directory_is_gone(self):
        self.assertEqual(len(self.check_doc("`06-renamed/sub/`\n")), 1)

    def test_dot_claude_directory_is_checked(self):
        self.assertEqual(len(self.check_doc("`.claude/agents/`\n")), 1)

    def test_placeholder_directories_are_skipped(self):
        self.assertEqual(self.check_doc("`04-active-work/prds/<initiative>/` `04-active-work/*/`\n"), [])

    def test_ignored_directory_is_checked_on_disk_and_skipped_in_ci(self):
        repo = ScratchRepo(
            {".gitignore": "local-only/\n", "01-knowledge-base/doc.md": "`01-knowledge-base/local-only/`\n"}
        )
        self.addCleanup(repo.cleanup)
        with mock.patch.dict(os.environ):
            os.environ.pop("CI", None)
            absent = repo.errors()
            os.environ["CI"] = "true"
            skipped = repo.errors()
            os.environ.pop("CI")
            os.makedirs(os.path.join(repo.root, "01-knowledge-base/local-only"))
            present = repo.errors()
        self.assertEqual(len(absent), 1)
        self.assertIn("ignored by .gitignore, not found on disk", absent[0])
        self.assertEqual((skipped, present), ([], []))


    def test_directory_whose_files_are_ignored_one_by_one_counts_as_an_ignored_tree(self):
        repo = ScratchRepo(
            {
                ".gitignore": "01-knowledge-base/sops/INDEX.md\n01-knowledge-base/sops/a/one.md\n",
                "01-knowledge-base/doc.md": "`01-knowledge-base/sops/a/` `01-knowledge-base/sops/`\n",
            }
        )
        self.addCleanup(repo.cleanup)
        with mock.patch.dict(os.environ):
            os.environ.pop("CI", None)
            absent = repo.errors()
            os.environ["CI"] = "true"
            skipped = repo.errors()
            os.environ.pop("CI")
            os.makedirs(os.path.join(repo.root, "01-knowledge-base/sops/a"))
            present = repo.errors()
        self.assertEqual(len(absent), 2)
        self.assertEqual((skipped, present), ([], []))

    def test_date_pattern_directories_are_placeholders(self):
        self.assertEqual(self.check_doc("`04-active-work/meeting-notes/YYYY-MM/` `04-active-work/YYYY-MM-DD-slug.md`\n"), [])


class IgnoredTargetTests(unittest.TestCase):
    def setUp(self):
        self.repo = ScratchRepo(
            {
                ".gitignore": "local-only/\n",
                "01-knowledge-base/doc.md": "`local-only/data.md`\n`04-active-work/missing.md`\n",
            }
        )
        self.addCleanup(self.repo.cleanup)

    def run_check(self, ci, on_disk):
        if on_disk:
            self.repo.write({"local-only/data.md": "# Local\n"})
        with mock.patch.dict(os.environ):
            os.environ.pop("CI", None)
            if ci:
                os.environ["CI"] = "true"
            return self.repo.errors()

    def test_ignored_target_present_on_disk_passes_locally_and_in_ci(self):
        for ci in (False, True):
            errors = self.run_check(ci, on_disk=True)
            self.assertEqual(len(errors), 1, ci)
            self.assertIn('doc.md:2: broken path "04-active-work/missing.md"', errors[0])

    def test_ignored_target_absent_is_an_error_locally(self):
        errors = self.run_check(ci=False, on_disk=False)
        self.assertEqual(len(errors), 2)
        self.assertIn('doc.md:1: broken path "local-only/data.md" (ignored by .gitignore, not found on disk)', errors[0])

    def test_ignored_target_absent_is_skipped_when_ci_is_set(self):
        errors = self.run_check(ci=True, on_disk=False)
        self.assertEqual(len(errors), 1)
        self.assertIn("04-active-work/missing.md", errors[0])


class StagedModeTests(unittest.TestCase):
    def setUp(self):
        self.repo = ScratchRepo(BASE)
        self.addCleanup(self.repo.cleanup)

    def test_a_unstaged_broken_ref_in_another_doc_does_not_block(self):
        self.repo.write({"01-knowledge-base/clean.md": "`04-active-work/target.md`\n"})
        self.repo.stage("01-knowledge-base/clean.md")
        self.repo.write({"01-knowledge-base/other.md": "`04-active-work/missing.md`\n"})
        self.assertEqual(self.repo.errors(staged=True), [])
        self.assertEqual(len(self.repo.errors()), 1)

    def test_b_staged_broken_ref_blocks_even_if_the_working_tree_was_fixed(self):
        self.repo.write({"01-knowledge-base/clean.md": "`04-active-work/missing.md`\n"})
        self.repo.stage("01-knowledge-base/clean.md")
        self.repo.write({"01-knowledge-base/clean.md": "# Clean\n"})
        errors = self.repo.errors(staged=True)
        self.assertEqual(len(errors), 1)
        self.assertIn('clean.md:1: broken path "04-active-work/missing.md"', errors[0])
        self.assertEqual(self.repo.errors(), [])

    def test_c_doc_linking_a_new_untracked_file_blocks(self):
        self.repo.write(
            {"04-active-work/new.md": "# New\n", "01-knowledge-base/clean.md": "`04-active-work/new.md`\n"}
        )
        self.repo.stage("01-knowledge-base/clean.md")
        self.assertEqual(len(self.repo.errors(staged=True)), 1)

    def test_staging_the_new_target_with_the_doc_resolves_it(self):
        self.repo.write(
            {"04-active-work/new.md": "# New\n", "01-knowledge-base/clean.md": "`04-active-work/new.md`\n"}
        )
        self.repo.stage("01-knowledge-base/clean.md", "04-active-work/new.md")
        self.assertEqual(self.repo.errors(staged=True), [])

    def test_target_staged_for_deletion_is_broken(self):
        self.repo.write({"01-knowledge-base/clean.md": "`04-active-work/target.md`\n"})
        git(self.repo.root, "rm", "-q", "04-active-work/target.md").check_returncode()
        self.repo.stage("01-knowledge-base/clean.md")
        self.assertEqual(len(self.repo.errors(staged=True)), 1)

    def test_staged_mode_needs_a_git_repository(self):
        with tempfile.TemporaryDirectory() as root:
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                code = repo_check.main(["--root", root, "--staged"])
        self.assertEqual(code, 2)
        self.assertIn("--staged needs a git repository", err.getvalue())


REPO_ROOT = os.path.dirname(HERE)


class HookTests(unittest.TestCase):
    def setUp(self):
        files = dict(BASE)
        for rel in ("scripts/repo_check.py", ".githooks/pre-commit"):
            with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as handle:
                files[rel] = handle.read()
        self.repo = ScratchRepo(files)
        self.addCleanup(self.repo.cleanup)
        self.hook = os.path.join(self.repo.root, ".githooks/pre-commit")
        os.chmod(self.hook, 0o755)
        git(self.repo.root, "config", "core.hooksPath", ".githooks").check_returncode()

    def commit(self):
        return git(self.repo.root, "commit", "-q", "-m", "change")

    def test_a_hook_allows_a_clean_commit_beside_an_unstaged_broken_ref(self):
        self.repo.write({"01-knowledge-base/clean.md": "`04-active-work/target.md`\n"})
        self.repo.stage("01-knowledge-base/clean.md")
        self.repo.write({"01-knowledge-base/other.md": "`04-active-work/missing.md`\n"})
        self.assertEqual(self.commit().returncode, 0)

    def test_b_hook_blocks_a_staged_broken_ref_after_the_working_copy_was_fixed(self):
        self.repo.write({"01-knowledge-base/clean.md": "`04-active-work/missing.md`\n"})
        self.repo.stage("01-knowledge-base/clean.md")
        self.repo.write({"01-knowledge-base/clean.md": "# Clean\n"})
        result = self.commit()
        self.assertEqual(result.returncode, 1)
        self.assertIn('broken path "04-active-work/missing.md"', result.stderr.decode())

    def test_c_hook_blocks_a_doc_that_links_a_new_untracked_file(self):
        self.repo.write(
            {"04-active-work/new.md": "# New\n", "01-knowledge-base/clean.md": "`04-active-work/new.md`\n"}
        )
        self.repo.stage("01-knowledge-base/clean.md")
        self.assertEqual(self.commit().returncode, 1)

    def test_hook_exits_one_with_a_message_when_python3_is_missing(self):
        with tempfile.TemporaryDirectory() as empty:
            result = subprocess.run(
                ["/bin/sh", self.hook],
                cwd=self.repo.root,
                env={"PATH": empty},
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
        self.assertEqual(result.returncode, 1)
        message = result.stderr.decode()
        self.assertIn("python3", message)
        self.assertIn("git commit --no-verify", message)
        self.assertEqual(len(message.splitlines()), 1)


if __name__ == "__main__":
    unittest.main()

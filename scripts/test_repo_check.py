import contextlib
import datetime
import io
import os
import subprocess
import tempfile
import unittest

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
            self.assertIn("../../04-active-work/prds/", error.split("Fix:")[1])

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
                " Fix: point it at 04-active-work/prds/alpha/prd.md or remove the reference."
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


class GitAwareTests(unittest.TestCase):
    def test_gitignored_targets_are_not_checked_and_untracked_files_resolve(self):
        with tempfile.TemporaryDirectory() as root:
            subprocess.run(["git", "init", "-q", root], check=True)
            os.makedirs(os.path.join(root, "04-active-work"))
            files = {
                ".gitignore": "local-only/\n",
                "doc.md": "`local-only/data.md`\n`04-active-work/new.md`\n`04-active-work/missing.md`\n",
                "04-active-work/new.md": "# New\n",
            }
            for rel, content in files.items():
                with open(os.path.join(root, rel), "w", encoding="utf-8") as handle:
                    handle.write(content)
            errors, _, _ = repo_check.check(root, today=TODAY)
        self.assertEqual(len(errors), 1)
        self.assertIn('doc.md:3: broken path "04-active-work/missing.md"', errors[0])


if __name__ == "__main__":
    unittest.main()

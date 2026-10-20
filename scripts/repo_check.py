#!/usr/bin/env python3
"""Check authored docs for broken repo path references (rule R5).

A reference is a markdown link target or a backticked token. A file reference
ends in a known file extension, and a backticked one must also contain a slash.
A directory reference ends in a slash and starts with an existing top-level
directory, a two-digit prefix such as 04-, or .claude.

A reference resolves when a tracked file exists at that path (for a directory,
under that path) from the repo root or from the doc's own directory, so an
untracked file fails locally exactly as it fails in CI. A target that
.gitignore matches must exist on disk in a plain local run, which catches a
renamed file in a content tree that only the maintainer's machine holds. The
check skips that target when the CI environment variable is set, when
REPO_CHECK_SKIP_IGNORED=1 is set, and always under --staged, so a fresh clone,
an agent worktree and the pre-commit hook never fail on content they cannot
have. A plain local run that finds no file at all under the ignored tree adds
a hint that names the override. A directory with no tracked files counts as an
ignored tree when .gitignore lists a path beneath it. Placeholders (<x>, {x},
[x], *, YYYY), external URLs, anchors and absolute paths are not checked.
Symlinked docs are skipped.

Modes:
    python3 scripts/repo_check.py            reads the working tree (CI)
    python3 scripts/repo_check.py --staged   reads docs and resolves targets
                                             from the index (pre-commit),
                                             skipping ignored targets
    REPO_CHECK_SKIP_IGNORED=1 python3 scripts/repo_check.py
                                             plain run that skips ignored targets

Error format, one per line on stderr. The summary line goes to stdout:
    path:line: broken path "<target>". Fix: point it at <path> or remove the reference.
    path:line: broken path "<target>". Fix: update the path or remove the reference.
A path is suggested only when exactly one tracked file has the same basename,
or exactly one has a basename at least 0.8 similar.

An exception is an HTML comment. Alone on its own line it covers the next line
only. Trailing a line it covers that line only:
    <!-- repo-check: ignore reason="why" until=YYYY-MM-DD -->
The keyword must be exactly "ignore". A missing reason, a date that is not
strict YYYY-MM-DD, an expired date and a date more than 180 days away are errors.

Not covered: bare unformatted paths, wikilinks, reference-style link
definitions, HTML hrefs, backticked filenames without a slash, and file
extensions outside the EXTENSIONS list.

Exit code is 1 when any error is reported, 2 when git or the arguments fail,
and 0 otherwise.
"""

import argparse
import datetime
import difflib
import os
import posixpath
import re
import subprocess
import sys
from typing import List, NamedTuple, Set
from urllib.parse import unquote

SKIP_PREFIXES = (
    "01-knowledge-base/Support content/",
    "01-knowledge-base/processes/Care Agent SOPs/",
    "03-templates/Checkout.com Brand Identity/",
    "05-archive/",
    "04-active-work/meeting-notes/",
    "04-active-work/merchant-interview-transcripts-2025/",
)
AUTHORED_DIRS = ("01-knowledge-base/", "02-workflows/", "03-templates/", "04-active-work/")
EXTENSIONS = "md|csv|tsv|json|html|yaml|yml|pdf|png"

EXT_RE = re.compile(r"\.(?:%s)$" % EXTENSIONS, re.IGNORECASE)
NUMBERED_DIR_RE = re.compile(r"^[0-9]{2}-")
PLACEHOLDER_RE = re.compile(r"[<>\[\]{}*]|YYYY")
SCHEME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
CODE_SPAN_RE = re.compile(r"`([^`\n]+)`")
LINK_RE = re.compile(r"\[[^\]]*\]\((<[^>]+>|[^)\s]+)(?:\s+\"[^\"]*\")?\)")
MARKER_RE = re.compile(r"<!--\s*repo-check:(.*?)-->")
REASON_RE = re.compile(r"\breason=\"([^\"]*)\"")
UNTIL_RE = re.compile(r"\buntil=(\S+)")
ISO_DATE_RE = re.compile(r"([0-9]{4})-([0-9]{2})-([0-9]{2})", re.ASCII)
MAX_EXCEPTION_DAYS = 180
MIN_NAME_SIMILARITY = 0.8
SKIP_IGNORED_ENV = "REPO_CHECK_SKIP_IGNORED"
ABSENT_TREE_HINT = "(ignored tree not present here: set %s=1)" % SKIP_IGNORED_ENV


class Exceptions(NamedTuple):
    valid_lines: Set[int]
    errors: List[tuple]


class Ref(NamedTuple):
    target: str
    is_dir: bool


class RepoCheckError(Exception):
    pass


class Result(NamedTuple):
    errors: List[str]
    docs_scanned: int
    refs_checked: int


def git_lines(root, *args):
    out = subprocess.run(
        ["git", "-C", root] + list(args), stdout=subprocess.PIPE, check=True
    ).stdout.decode("utf-8", "replace")
    return [part for part in out.split("\0") if part]


def has_git(root):
    return os.path.exists(os.path.join(root, ".git"))


class Tree(NamedTuple):
    files: Set[str]
    symlinks: Set[str]


def list_tree(root, staged):
    if has_git(root):
        files, symlinks = set(), set()
        for entry in git_lines(root, "ls-files", "-s", "-z"):
            meta, _, path = entry.partition("\t")
            files.add(path)
            if meta.split()[0] == "120000":
                symlinks.add(path)
        if not staged:
            files -= set(git_lines(root, "ls-files", "-z", "--deleted"))
        return Tree(files, symlinks)
    if staged:
        raise RepoCheckError("repo-check: --staged needs a git repository.")
    files, symlinks = set(), set()
    for base, dirs, names in os.walk(root):
        rel = os.path.relpath(base, root).replace(os.sep, "/")
        dirs[:] = [d for d in dirs if d != ".git" and posixpath.join(rel, d) != ".claude/worktrees"]
        for name in names:
            path = posixpath.normpath(posixpath.join(rel, name))
            files.add(path)
            if os.path.islink(os.path.join(root, path)):
                symlinks.add(path)
    return Tree(files, symlinks)


def decode(raw):
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return None


def read_index(root, paths):
    request = "".join(":%s\n" % path for path in paths).encode("utf-8")
    data = subprocess.run(
        ["git", "-C", root, "cat-file", "--batch"], input=request, stdout=subprocess.PIPE, check=True
    ).stdout
    contents, pos = {}, 0
    for path in paths:
        end = data.index(b"\n", pos)
        header = data[pos:end].split()
        pos = end + 1
        if header[-1] == b"missing":
            contents[path] = None
            continue
        size = int(header[2])
        contents[path] = decode(data[pos:pos + size])
        pos += size + 1
    return contents


def read_working_tree(root, paths):
    contents = {}
    for path in paths:
        try:
            with open(os.path.join(root, path), "rb") as handle:
                contents[path] = decode(handle.read())
        except OSError:
            contents[path] = None
    return contents


def is_authored(rel):
    if any(rel.startswith(prefix) for prefix in SKIP_PREFIXES):
        return False
    parts = rel.split("/")
    if rel.endswith(".md") and (len(parts) == 1 or rel.startswith(AUTHORED_DIRS)):
        return True
    return len(parts) == 4 and parts[:2] == [".claude", "skills"] and parts[3] == "SKILL.md"


def clean_target(raw, top_dirs):
    target = unquote(raw.strip().strip("<>")).split("#", 1)[0].strip()
    if not target or PLACEHOLDER_RE.search(target):
        return None
    if SCHEME_RE.match(target) or target.startswith(("/", "~")):
        return None
    if EXT_RE.search(target):
        return Ref(target, False)
    first = target.split("/", 1)[0]
    if target.endswith("/") and (first in top_dirs or first == ".claude" or NUMBERED_DIR_RE.match(first)):
        return Ref(target, True)
    return None


def extract_refs(line, top_dirs):
    found = []
    for pattern, kind in ((LINK_RE, "link"), (CODE_SPAN_RE, "code")):
        for match in pattern.finditer(line):
            ref = clean_target(match.group(1), top_dirs)
            if ref and (kind == "link" or "/" in ref.target):
                found.append((match.start(), ref))
    return list(dict.fromkeys(ref for _, ref in sorted(found)))


def candidates(doc, target):
    options = []
    for base in ("", posixpath.dirname(doc)):
        path = posixpath.normpath(posixpath.join(base, target))
        if not path.startswith("..") and path not in options:
            options.append(path)
    return options


def mask_code_spans(line):
    return CODE_SPAN_RE.sub(lambda match: " " * len(match.group(0)), line)


def strip_markers(line):
    masked = mask_code_spans(line)
    kept, pos = [], 0
    for marker in MARKER_RE.finditer(masked):
        kept.append(line[pos:marker.start()])
        pos = marker.end()
    kept.append(line[pos:])
    return "".join(kept)


def parse_iso_date(text):
    match = ISO_DATE_RE.fullmatch(text)
    if not match:
        return None
    try:
        return datetime.date(*(int(part) for part in match.groups()))
    except ValueError:
        return None


def parse_exceptions(rel, lines, today):
    valid, errors = set(), []
    latest = today + datetime.timedelta(days=MAX_EXCEPTION_DAYS)
    for number, line in enumerate(lines, 1):
        masked = mask_code_spans(line)
        alone = not strip_markers(line).strip()
        for marker in MARKER_RE.finditer(masked):
            body = marker.group(1).strip()
            where = "%s:%d:" % (rel, number)
            reason = REASON_RE.search(body)
            until = UNTIL_RE.search(body)
            if body.split(None, 1)[:1] != ["ignore"]:
                errors.append((rel, number, '%s unknown repo-check directive. Fix: use <!-- repo-check: ignore reason="..." until=YYYY-MM-DD -->.' % where))
                continue
            if not reason or not reason.group(1).strip():
                errors.append((rel, number, '%s exception has no reason. Fix: add reason="why this reference is allowed".' % where))
                continue
            expiry = parse_iso_date(until.group(1)) if until else None
            if expiry is None:
                errors.append((rel, number, "%s exception has no valid until date. Fix: add until=YYYY-MM-DD." % where))
            elif expiry < today:
                errors.append((rel, number, "%s exception expired on %s. Fix: repair the reference or renew the date with a reason." % (where, expiry.isoformat())))
            elif expiry > latest:
                errors.append((rel, number, "%s exception until=%s is more than %d days away. Fix: use a date on or before %s." % (where, expiry.isoformat(), MAX_EXCEPTION_DAYS, latest.isoformat())))
            else:
                valid.add(number + 1 if alone else number)
    return Exceptions(valid, errors)


def index_by_basename(files):
    index = {}
    for path in sorted(files):
        index.setdefault(posixpath.basename(path).lower(), []).append(path)
    return index


def suggest(index, doc, target):
    name = posixpath.basename(target).lower()
    matches = index.get(name)
    if matches is None:
        names = [n for n in index if n.endswith(posixpath.splitext(name)[1])]
        close = difflib.get_close_matches(name, names, n=1, cutoff=MIN_NAME_SIMILARITY)
        matches = index[close[0]] if close else []
    if len(matches) != 1:
        return None
    best = matches[0]
    if target.startswith(".") or "/" not in target:
        best = posixpath.relpath(best, posixpath.dirname(doc) or ".")
    return best


def probe_path(candidate, ref):
    return candidate + "/" if ref.is_dir else candidate


def ignored_trees(root):
    try:
        with open(os.path.join(root, ".gitignore"), encoding="utf-8", errors="replace") as handle:
            patterns = {line.strip().lstrip("/") for line in handle if line.strip() and not line.startswith("#")}
    except OSError:
        return set()
    return parent_dirs(patterns)


def gitignored(root, paths):
    if not paths or not has_git(root):
        return set()
    proc = subprocess.run(
        ["git", "-C", root, "check-ignore", "--no-index", "-z", "--stdin"],
        input="\0".join(paths).encode("utf-8"),
        stdout=subprocess.PIPE,
    )
    return {part for part in proc.stdout.decode("utf-8", "replace").split("\0") if part}


def parent_dirs(files):
    found = set()
    for path in files:
        parent = posixpath.dirname(path)
        while parent and parent not in found:
            found.add(parent)
            parent = posixpath.dirname(parent)
    return found


def tree_top(candidate, ref, dirs):
    parts = candidate.split("/")
    for depth in range(1, len(parts) + (1 if ref.is_dir else 0)):
        top = "/".join(parts[:depth])
        if top not in dirs:
            return top
    return None


def holds_no_file(root, top):
    return not any(names for _, _, names in os.walk(os.path.join(root, top)))


def check(root, today=None, staged=False):
    today = today or datetime.date.today()
    tree = list_tree(root, staged)
    files = tree.files
    dirs = parent_dirs(files)
    top_dirs = {d for d in dirs if "/" not in d}
    index = index_by_basename(files)
    docs = sorted(f for f in files - tree.symlinks if is_authored(f) and "\n" not in f)
    texts = (read_index if staged else read_working_tree)(root, docs)

    errors, unresolved, checked = [], [], 0
    for doc in docs:
        if texts[doc] is None:
            errors.append((doc, 0, "%s: unreadable. Fix: make it readable UTF-8 text or remove the file." % doc))
            continue
        lines = texts[doc].split("\n")
        exceptions = parse_exceptions(doc, lines, today)
        allowed = exceptions.valid_lines
        errors.extend(exceptions.errors)
        for number, line in enumerate(lines, 1):
            if number in allowed:
                continue
            for ref in extract_refs(strip_markers(line), top_dirs):
                checked += 1
                known = dirs if ref.is_dir else files
                if not any(c in known for c in candidates(doc, ref.target)):
                    unresolved.append((doc, number, ref))

    skip_ignored = staged or bool(os.environ.get("CI")) or os.environ.get(SKIP_IGNORED_ENV) == "1"
    probes = {probe_path(c, ref) for doc, _, ref in unresolved for c in candidates(doc, ref.target)}
    matched = gitignored(root, sorted(probes))
    trees = ignored_trees(root)
    for doc, number, ref in unresolved:
        hits = [
            c for c in candidates(doc, ref.target)
            if probe_path(c, ref) in matched or (ref.is_dir and c in trees)
        ]
        if hits:
            if skip_ignored or any(os.path.exists(os.path.join(root, c)) for c in hits):
                continue
            message = '%s:%d: broken path "%s" (ignored by .gitignore, not found on disk). Fix: restore it locally, update the path or remove the reference.' % (doc, number, ref.target)
            tops = [tree_top(c, ref, dirs) for c in hits]
            if all(top and holds_no_file(root, top) for top in tops):
                message += " " + ABSENT_TREE_HINT
            errors.append((doc, number, message))
            continue
        best = None if ref.is_dir else suggest(index, doc, ref.target)
        fix = "point it at %s or remove the reference." % best if best else "update the path or remove the reference."
        errors.append((doc, number, '%s:%d: broken path "%s". Fix: %s' % (doc, number, ref.target, fix)))
    errors.sort(key=lambda e: (e[0], e[1]))
    return Result([e[2] for e in errors], len(docs), checked)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Check authored docs for broken repo path references.")
    parser.add_argument("--root", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    parser.add_argument(
        "--staged",
        action="store_true",
        help="read docs and resolve targets from the git index instead of the working tree",
    )
    args = parser.parse_args(argv)
    try:
        result = check(os.path.abspath(args.root), staged=args.staged)
    except RepoCheckError as error:
        print(error, file=sys.stderr)
        return 2
    except (OSError, subprocess.CalledProcessError) as error:
        print("repo-check: cannot list files with git (%s)." % error.__class__.__name__, file=sys.stderr)
        return 2
    for error in result.errors:
        print(error, file=sys.stderr)
    status = "%d error(s)" % len(result.errors) if result.errors else "ok"
    print("repo-check: %s, %d docs scanned, %d references checked." % (status, result.docs_scanned, result.refs_checked))
    return 1 if result.errors else 0


if __name__ == "__main__":
    sys.exit(main())

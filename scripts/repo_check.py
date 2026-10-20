#!/usr/bin/env python3
"""Check authored docs for broken repo path references (rule R5).

A reference is a markdown link target or a backticked token that ends in a
known file extension. Backticked tokens must also contain a slash. A reference
resolves when a tracked file exists at that path from the repo root or from the
doc's own directory, so an untracked file fails locally exactly as it fails in
CI. A target that .gitignore matches must exist on disk. It is skipped when the
CI environment variable is set, because ignored trees do not exist in a
checkout. Placeholders, external URLs, anchors and absolute paths are not
checked.

Error format, one per line:
    path:line: broken path "<target>". Fix: point it at <closest path> or remove the reference.

An exception is an HTML comment. Alone on its own line it covers the next line
only. Trailing a line it covers that line only:
    <!-- repo-check: ignore reason="why" until=YYYY-MM-DD -->
The keyword must be exactly "ignore". A missing reason, a date that is not
strict YYYY-MM-DD, an expired date and a date more than 180 days away are errors.

Exit code is 1 when any error is reported and 0 otherwise.
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


def list_files(root, staged):
    if has_git(root):
        listed = set(git_lines(root, "ls-files", "-z", "--cached"))
        return listed if staged else listed - set(git_lines(root, "ls-files", "-z", "--deleted"))
    if staged:
        raise RepoCheckError("repo-check: --staged needs a git repository.")
    found = set()
    for base, dirs, names in os.walk(root):
        rel = os.path.relpath(base, root).replace(os.sep, "/")
        dirs[:] = [d for d in dirs if d != ".git" and posixpath.join(rel, d) != ".claude/worktrees"]
        for name in names:
            found.add(posixpath.normpath(posixpath.join(rel, name)))
    return found


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
            continue
        size = int(header[2])
        contents[path] = data[pos:pos + size].decode("utf-8", "replace")
        pos += size + 1
    return contents


def read_working_tree(root, paths):
    contents = {}
    for path in paths:
        with open(os.path.join(root, path), encoding="utf-8", errors="replace") as handle:
            contents[path] = handle.read()
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


def suggest(files_by_ext, doc, target):
    pool = files_by_ext.get(posixpath.splitext(target)[1].lower(), [])
    intended = posixpath.normpath(posixpath.join(posixpath.dirname(doc), target)) if target.startswith(".") else target
    base = posixpath.basename(intended)
    same_name = [p for p in pool if posixpath.basename(p) == base]
    if same_name:
        best = max(same_name, key=lambda p: difflib.SequenceMatcher(None, intended, p).ratio())
    else:
        close = difflib.get_close_matches(intended, pool, n=1, cutoff=0.75)
        best = close[0] if close else None
    if best and (target.startswith(".") or "/" not in target):
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


def check(root, today=None, staged=False):
    today = today or datetime.date.today()
    files = list_files(root, staged)
    dirs = parent_dirs(files)
    top_dirs = {d for d in dirs if "/" not in d}
    files_by_ext = {}
    for path in sorted(files):
        files_by_ext.setdefault(posixpath.splitext(path)[1].lower(), []).append(path)
    docs = sorted(f for f in files if is_authored(f) and "\n" not in f)
    texts = (read_index if staged else read_working_tree)(root, docs)

    errors, unresolved, checked = [], [], 0
    for doc in docs:
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

    ci = bool(os.environ.get("CI"))
    probes = {probe_path(c, ref) for doc, _, ref in unresolved for c in candidates(doc, ref.target)}
    matched = gitignored(root, sorted(probes))
    trees = ignored_trees(root)
    for doc, number, ref in unresolved:
        hits = [
            c for c in candidates(doc, ref.target)
            if probe_path(c, ref) in matched or (ref.is_dir and c in trees)
        ]
        if hits:
            if ci or any(os.path.exists(os.path.join(root, c)) for c in hits):
                continue
            message = '%s:%d: broken path "%s" (ignored by .gitignore, not found on disk). Fix: restore it locally, update the path or remove the reference.' % (doc, number, ref.target)
            errors.append((doc, number, message))
            continue
        best = None if ref.is_dir else suggest(files_by_ext, doc, ref.target)
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
    for error in result.errors:
        print(error)
    status = "%d error(s)" % len(result.errors) if result.errors else "ok"
    print("repo-check: %s, %d docs scanned, %d references checked." % (status, result.docs_scanned, result.refs_checked))
    return 1 if result.errors else 0


if __name__ == "__main__":
    sys.exit(main())

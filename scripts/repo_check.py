#!/usr/bin/env python3
"""Check authored docs for broken repo path references (rule R5).

A reference is a markdown link target or a backticked token that ends in a
known file extension. Backticked tokens must also contain a slash. A reference
resolves when a tracked file exists at that path from the repo root or from the
doc's own directory, so an untracked file fails locally exactly as it fails in
CI. Placeholders, external URLs, anchors, absolute paths and targets
that .gitignore excludes are not checked.

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
PLACEHOLDER_RE = re.compile(r"[<>\[\]{}*]")
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


def list_files(root):
    if has_git(root):
        listed = set(git_lines(root, "ls-files", "-z", "--cached"))
        return listed - set(git_lines(root, "ls-files", "-z", "--deleted"))
    found = set()
    for base, dirs, names in os.walk(root):
        rel = os.path.relpath(base, root).replace(os.sep, "/")
        dirs[:] = [d for d in dirs if d != ".git" and posixpath.join(rel, d) != ".claude/worktrees"]
        for name in names:
            found.add(posixpath.normpath(posixpath.join(rel, name)))
    return found


def is_authored(rel):
    if any(rel.startswith(prefix) for prefix in SKIP_PREFIXES):
        return False
    parts = rel.split("/")
    if rel.endswith(".md") and (len(parts) == 1 or rel.startswith(AUTHORED_DIRS)):
        return True
    return len(parts) == 4 and parts[:2] == [".claude", "skills"] and parts[3] == "SKILL.md"


def clean_target(raw):
    target = unquote(raw.strip().strip("<>")).split("#", 1)[0].strip()
    if not target or not EXT_RE.search(target) or PLACEHOLDER_RE.search(target):
        return None
    if SCHEME_RE.match(target) or target.startswith(("/", "~")):
        return None
    return target


def extract_refs(line):
    found = []
    for pattern, kind in ((LINK_RE, "link"), (CODE_SPAN_RE, "code")):
        for match in pattern.finditer(line):
            target = clean_target(match.group(1))
            if target and (kind == "link" or "/" in target):
                found.append((match.start(), target))
    return list(dict.fromkeys(target for _, target in sorted(found)))


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


def gitignored(root, paths):
    if not paths or not has_git(root):
        return set()
    proc = subprocess.run(
        ["git", "-C", root, "check-ignore", "--no-index", "-z", "--stdin"],
        input="\0".join(paths).encode("utf-8"),
        stdout=subprocess.PIPE,
    )
    return {part for part in proc.stdout.decode("utf-8", "replace").split("\0") if part}


def check(root, today=None):
    today = today or datetime.date.today()
    files = list_files(root)
    files_by_ext = {}
    for path in sorted(files):
        files_by_ext.setdefault(posixpath.splitext(path)[1].lower(), []).append(path)
    docs = sorted(f for f in files if is_authored(f))

    errors, unresolved, checked = [], [], 0
    for doc in docs:
        with open(os.path.join(root, doc), encoding="utf-8", errors="replace") as handle:
            lines = handle.read().split("\n")
        exceptions = parse_exceptions(doc, lines, today)
        allowed = exceptions.valid_lines
        errors.extend(exceptions.errors)
        for number, line in enumerate(lines, 1):
            if number in allowed:
                continue
            for target in extract_refs(strip_markers(line)):
                checked += 1
                if not any(c in files for c in candidates(doc, target)):
                    unresolved.append((doc, number, target))

    ignored = gitignored(root, sorted({c for d, _, t in unresolved for c in candidates(d, t)}))
    for doc, number, target in unresolved:
        if any(c in ignored for c in candidates(doc, target)):
            continue
        best = suggest(files_by_ext, doc, target)
        fix = "point it at %s or remove the reference." % best if best else "remove the reference."
        errors.append((doc, number, '%s:%d: broken path "%s". Fix: %s' % (doc, number, target, fix)))
    errors.sort(key=lambda e: (e[0], e[1]))
    return Result([e[2] for e in errors], len(docs), checked)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Check authored docs for broken repo path references.")
    parser.add_argument("--root", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    args = parser.parse_args(argv)
    result = check(os.path.abspath(args.root))
    for error in result.errors:
        print(error)
    status = "%d error(s)" % len(result.errors) if result.errors else "ok"
    print("repo-check: %s, %d docs scanned, %d references checked." % (status, result.docs_scanned, result.refs_checked))
    return 1 if result.errors else 0


if __name__ == "__main__":
    sys.exit(main())

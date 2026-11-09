#!/usr/bin/env python3
"""Flag prose that reads like AI slop or app microcopy.

Usage:
  python3 scripts/check_style.py            # summary table, worst files first
  python3 scripts/check_style.py -v FILE…   # every hit with its line
  python3 scripts/check_style.py --strict   # exit 1 if any banned phrase appears

Scans Markdown prose (not code blocks, not "Sources and further reading", not
Bryan's-take callouts, which are his own words). Banned phrases are hard errors
under --strict; the density numbers are signals for a human to judge.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "build", "site", "node_modules"}
SKIP_FILES = {"AGENTS.md", "CLAUDE.md", "CONTRIBUTING.md"}

BANNED = [
    r"it'?s (important|worth) (to note|noting)", r"\bin today'?s\b", r"let'?s dive", r"\bdive (into|deep)\b",
    r"\bdelv(e|es|ing)\b", r"\bunlock(s|ing)?\b", r"\bleverag(e|es|ing)\b", r"\brobust\b", r"\bseamless(ly)?\b",
    r"\bgame[- ]chang", r"\brevolutioni[sz]", r"\bcutting[- ]edge\b", r"\bparadigm\b", r"\btransformative\b",
    r"\bsupercharg", r"\bholistic\b", r"\bempower", r"\btapestry\b", r"\brealm\b", r"\btestament to\b",
    r"\bunderscor(e|es|ing)\b", r"\bpivotal\b", r"\bmultifaceted\b", r"\bmyriad\b", r"\bever[- ]evolving\b",
    r"\bnavigat(e|ing) the\b", r"here'?s the thing", r"here'?s why:", r"the catch\?", r"the result\?",
    r"that'?s where .{1,40} comes in", r"\bin conclusion\b", r"\bat the end of the day\b", r"\bsimply put\b",
    r"\bin essence\b", r"\bthe bottom line\b", r"\bkey takeaway", r"\bwhen it comes to\b", r"\bplays a (key|crucial|vital) role\b",
    r"\bclick here\b", r"\blearn more\b", r"\bpro tip\b", r"\bheads up\b",
]
SIGNALS = {
    "em dashes": r"—",
    "casual fillers": r"\b(honestly|kind of|pretty much|a ton|super)\b",
    "label openers": r"^\s*(?:[-*]|\d+\.)?\s*\*\*(note|tip|key point|why|important|remember|warning)\*\*:?",
    "not just X but Y": r"\bnot (just|only) .{1,60}, but\b",
    "crucial/critical": r"\b(crucial(ly)?|critical(ly)?|vital)\b",
    "rhetorical Q→A": r"\?\s+(Because|Simple|It turns out|Short answer)\b",
}


def prose_lines(text):
    in_fence = in_sources = False
    for n, line in enumerate(text.splitlines(), 1):
        if re.match(r"^\s*(```|~~~)", line):
            in_fence = not in_fence
            continue
        if re.match(r"^## ", line):
            in_sources = line.strip() == "## Sources and further reading"
        if in_fence or in_sources or line.startswith("> **Bryan's take:**"):
            continue
        yield n, re.sub(r"`[^`]*`|\]\([^)]*\)", "", line)


def scan(path):
    banned, signals, words = [], {k: [] for k in SIGNALS}, 0
    for n, line in prose_lines(path.read_text()):
        words += len(line.split())
        for pat in BANNED:
            for m in re.finditer(pat, line, re.I):
                banned.append((n, m.group(0), line.strip()))
        for name, pat in SIGNALS.items():
            for m in re.finditer(pat, line, re.I | re.M):
                signals[name].append((n, m.group(0), line.strip()))
    return words, banned, signals


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    verbose = "-v" in sys.argv
    strict = "--strict" in sys.argv
    files = [pathlib.Path(a).resolve() for a in args] or sorted(
        p for p in ROOT.rglob("*.md")
        if not SKIP_DIRS & set(p.relative_to(ROOT).parts) and p.name not in SKIP_FILES)
    rows, total_banned = [], 0
    for f in files:
        words, banned, signals = scan(f)
        total_banned += len(banned)
        per_k = lambda hits: 1000 * len(hits) / max(words, 1)
        rows.append((len(banned), f, words, banned, signals, per_k))
    rows.sort(key=lambda r: (-r[0], -r[5](r[4]["em dashes"])))
    print(f"{'file':58} {'words':>6} {'banned':>6} {'—/1k':>6} {'casual/1k':>9} {'labels':>6}")
    for nb, f, words, banned, signals, per_k in rows:
        rel = str(f.relative_to(ROOT))
        print(f"{rel[:58]:58} {words:6} {nb:6} {per_k(signals['em dashes']):6.1f} "
              f"{per_k(signals['casual fillers']):9.1f} {len(signals['label openers']):6}")
        if verbose:
            for n, hit, line in banned:
                print(f"    BANNED {n}: {hit!r}: {line[:110]}")
            for name, hits in signals.items():
                for n, hit, line in hits:
                    print(f"    {name} {n}: {line[:110]}")
    print(f"\n{total_banned} banned phrase(s) across {len(rows)} file(s)")
    return 1 if strict and total_banned else 0


if __name__ == "__main__":
    sys.exit(main())

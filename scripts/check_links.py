#!/usr/bin/env python3
"""Check that relative Markdown links and heading anchors resolve.

Usage: python3 scripts/check_links.py   (run from anywhere; exits 1 on broken links)

External (http/https/mailto) links are not fetched. Anchors use GitHub's
heading-slug rules; headings inside fenced code blocks are ignored.
"""
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parent.parent
LINK = re.compile(r"(?<!\!)\[(?:[^\[\]]|\[[^\]]*\])*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)|<img[^>]+src=\"([^\"]+)\"")
FENCE = re.compile(r"^\s*(```|~~~)")


def strip_code(text):
    """Blank out fenced code blocks and inline code so links inside them are ignored."""
    out, in_fence = [], False
    for line in text.splitlines():
        if FENCE.match(line):
            in_fence = not in_fence
            out.append("")
            continue
        out.append("" if in_fence else re.sub(r"`[^`]*`", "", line))
    return "\n".join(out)


def slug(heading):
    h = heading.strip().lower()
    h = re.sub(r"<[^>]+>", "", h)            # inline html
    h = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", h)  # links -> text
    h = h.replace("`", "")
    kept = []
    for ch in h:
        cat = unicodedata.category(ch)
        if ch in " -_" or cat[0] in ("L", "N"):
            kept.append(ch)
    return "".join(kept).replace(" ", "-")


def anchors(path, cache={}):
    if path in cache:
        return cache[path]
    seen, result, in_fence = {}, set(), False
    for line in path.read_text().splitlines():
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", line)
        if not m:
            continue
        base = slug(m.group(2))
        n = seen.get(base, 0)
        result.add(base if n == 0 else f"{base}-{n}")
        seen[base] = n + 1
    cache[path] = result
    return result


def main():
    broken = 0
    files = sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)
    for md in files:
        text = strip_code(md.read_text())
        for lineno, line in enumerate(text.splitlines(), 1):
            for m in LINK.finditer(line):
                target = m.group(1) or m.group(2)
                if re.match(r"^(https?:|mailto:)", target):
                    continue
                path_part, _, frag = target.partition("#")
                dest = md if not path_part else (md.parent / path_part).resolve()
                problem = None
                if not dest.exists():
                    problem = "missing file"
                elif frag and dest.is_file() and dest.suffix == ".md" and frag.lower() not in anchors(dest):
                    problem = f"missing anchor #{frag}"
                if problem:
                    broken += 1
                    print(f"{md.relative_to(ROOT)}:{lineno}: {target} ({problem})")
    print(f"checked {len(files)} files: {broken} broken link(s)")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())

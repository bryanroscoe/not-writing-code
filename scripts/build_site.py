#!/usr/bin/env python3
"""Build the GitHub Pages site and slide decks.

Usage:
  python3 scripts/build_site.py               # site + HTML decks
  python3 scripts/build_site.py --pdf --pptx  # also PDF and PowerPoint decks (needs Chrome)
  python3 scripts/build_site.py --no-slides   # site only (no Node needed)

Needs: pip install -r requirements-site.txt, and Node.js (npx) for the decks.
Output: site/ (the deployable site). build/ holds the assembled sources.

The repo keeps Markdown where it reads well on GitHub. This script copies it into
build/docs/ in the shape MkDocs wants (README.md becomes the home page), renders
each Marp deck in slides/ into build/docs/slides/, writes a slides index page,
then runs `mkdocs build --strict`.
"""
import argparse
import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
BUILD = ROOT / "build"
DOCS = BUILD / "docs"
MARP = "@marp-team/marp-cli@4.5.1"
# Copied into the site. AGENTS.md and CLAUDE.md stay repo-only.
DIRS = ["modules", "paths", "course", "workplace", "reference", "assets"]
FILES = ["CONTRIBUTING.md", "LICENSE"]


def decks():
    return sorted(p for p in (ROOT / "slides").glob("[0-9][0-9]-*.md"))


def front_matter(path):
    text = path.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    meta = {}
    if m:
        for line in m.group(1).splitlines():
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta


def assemble():
    if BUILD.exists():
        shutil.rmtree(BUILD)
    DOCS.mkdir(parents=True)
    for d in DIRS:
        shutil.copytree(ROOT / d, DOCS / d)
    for f in FILES:
        shutil.copy2(ROOT / f, DOCS / f)
    # Home page: README.md, with the repo-relative icon path kept valid.
    shutil.copy2(ROOT / "README.md", DOCS / "index.md")
    for md in DOCS.rglob("*.md"):
        fix_links(md)


LINK = re.compile(r"\]\(([^)\s]+)\)")
GITHUB = "https://github.com/bryanroscoe/not-writing-code"


def fix_links(md):
    """Make repo-relative links work on the site.

    - slides/ and slides/README.md -> the generated slides index; slides/NN-x.md -> the rendered deck.
    - a link to a folder -> that folder's README.md (MkDocs serves it as the folder index).
    - a link to a repo file that isn't part of the site -> the file on GitHub.
    """
    rel_dir = md.parent.relative_to(DOCS)
    out, in_fence = [], False
    for line in md.read_text().splitlines(keepends=True):
        if re.match(r"^\s*(```|~~~)", line):
            in_fence = not in_fence
        if not in_fence:
            line = LINK.sub(lambda m: "](" + rewrite(m.group(1), rel_dir) + ")", line)
        out.append(line)
    md.write_text("".join(out))


def rewrite(target, rel_dir):
    if re.match(r"^(https?:|mailto:|#)", target):
        return target
    path, hash_, frag = target.partition("#")
    suffix = hash_ + frag
    repo_path = (ROOT / rel_dir / path).resolve()
    try:
        repo_rel = repo_path.relative_to(ROOT)
    except ValueError:
        return target
    parts = repo_rel.parts
    if parts and parts[0] == "slides":
        if len(parts) == 1 or parts[1] == "README.md":
            return relpath("slides/index.md", rel_dir) + suffix
        if re.match(r"^[0-9]{2}-[a-z0-9-]+\.md$", parts[1]):
            return relpath("slides/" + parts[1][:-3] + ".html", rel_dir) + suffix
    site_path = DOCS / repo_rel
    if repo_rel == pathlib.Path("README.md"):
        return relpath("index.md", rel_dir) + suffix
    if site_path.is_dir() and (site_path / "README.md").exists():
        return relpath(str(repo_rel / "README.md"), rel_dir) + suffix
    if site_path.exists():
        return target
    if repo_path.exists():
        kind = "tree" if repo_path.is_dir() else "blob"
        return f"{GITHUB}/{kind}/main/{repo_rel.as_posix()}{suffix}"
    return target


def relpath(site_rel, rel_dir):
    import os
    return os.path.relpath(site_rel, rel_dir if str(rel_dir) != "." else ".").replace(os.sep, "/")


def build_slides(formats):
    out = DOCS / "slides"
    out.mkdir(parents=True, exist_ok=True)
    found = decks()
    if not found:
        print("no decks in slides/")
    else:
        src = BUILD / "slides-src"
        src.mkdir(parents=True, exist_ok=True)
        for p in found:
            shutil.copy2(p, src / p.name)
        for fmt in formats:
            flag = {"html": [], "pdf": ["--pdf"], "pptx": ["--pptx"]}[fmt]
            if fmt != "html":
                # Headless Chrome can stall when several decks render at once (seen on
                # CI runners and laptops alike). Render one at a time with a long timeout.
                flag += ["--no-parallel", "--browser-timeout", "300"]
            cmd = ["npx", "--yes", MARP, "--theme-set", str(ROOT / "slides" / "theme"),
                   "--input-dir", str(src), "--output", str(out), "--html",
                   "--allow-local-files", *flag]
            for attempt in (1, 2):
                print("+", " ".join(cmd), f"(attempt {attempt})")
                if subprocess.run(cmd, cwd=ROOT).returncode == 0:
                    break
                if attempt == 2:
                    sys.exit(f"marp failed twice converting decks to {fmt}")
    write_slides_index(found, formats)


def write_slides_index(found, formats):
    lines = [
        "# Slides",
        "",
        "One deck per module, for a 30–50 minute talk or class session. Open a deck and press `F` for",
        "full screen; `P` opens presenter view with speaker notes. The module is the reading that goes with it.",
        "",
        "| # | Deck | Downloads | Reading |",
        "| --- | --- | --- | --- |",
    ]
    for p in found:
        meta = front_matter(p)
        num, slug = p.stem[:2], p.stem
        title = meta.get("title", slug)
        title = re.sub(r"^\d{2}:\s*", "", title)
        downloads = " · ".join(f"[{f.upper()}]({slug}.{f})" for f in formats if f != "html") or "—"
        module = ROOT / "modules" / f"{slug}.md"
        reading = f"[Module {num}](../modules/{slug}.md)" if module.exists() else "—"
        href = f"{slug}.html" if "html" in formats else f"{GITHUB}/blob/main/slides/{p.name}"
        lines.append(f"| {num} | [{title}]({href}) | {downloads} | {reading} |")
    lines += [
        "",
        "The decks are written in [Marp](https://marp.app/) Markdown in the repo's",
        "[`slides/`](https://github.com/bryanroscoe/not-writing-code/tree/main/slides) folder,",
        "which also explains the conventions for writing one.",
        "",
    ]
    (DOCS / "slides").mkdir(parents=True, exist_ok=True)
    (DOCS / "slides" / "index.md").write_text("\n".join(lines))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", action="store_true")
    ap.add_argument("--pptx", action="store_true")
    ap.add_argument("--no-slides", action="store_true")
    args = ap.parse_args()
    assemble()
    formats = ["html"] + (["pdf"] if args.pdf else []) + (["pptx"] if args.pptx else [])
    if args.no_slides:
        write_slides_index(decks(), [])
    else:
        build_slides(formats)
    subprocess.run([sys.executable, "-m", "mkdocs", "build", "--strict", "-f", str(ROOT / "mkdocs.yml")],
                   check=True, cwd=ROOT)
    print("site built in", ROOT / "site")


if __name__ == "__main__":
    main()

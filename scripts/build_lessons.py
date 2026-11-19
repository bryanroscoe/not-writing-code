#!/usr/bin/env python3
"""Inline lessons/NN.html into lessons/shell.html and write the lesson player.

Fails with a list of problems when a lesson breaks the format. Run it after every lesson edit:
    python3 scripts/build_lessons.py --only 02   # just lesson 02, written to build/lessons/02.html
    python3 scripts/build_lessons.py             # every lesson, written to site/lessons/index.html

scripts/build_site.py runs it after MkDocs, so the player is served at /lessons/ next to the modules.
"""
import argparse
import html
import re
import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LESSONS = ROOT / 'lessons'
MODULES = ROOT / 'modules'
# Go-deeper links point at the module pages MkDocs builds next to /lessons/.
MODULE_LINK = re.compile(r'^\.\./modules/([0-9]{2}-[a-z0-9-]+)/(?:#(.+))?$')
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr',
        'path', 'rect', 'circle', 'line', 'polyline', 'polygon', 'ellipse', 'use', 'stop'}
FIRST_LINE = re.compile(r'^<section class="lesson" data-lesson="(\d\d)" data-title="([^"]+)" data-minutes="(\d+)" hidden>\n')
TALK_MAX_CHARS = 1500
CHECK_SAY = ('for (const [re, to] of JSON.parse(process.argv[1])) {'
             ' if (typeof to !== "string") throw new Error("spoken form must be a string"); new RegExp(re, "g"); }')


class Balance(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.problems, self.ids = [], [], []

    def handle_starttag(self, tag, attrs):
        for k, v in attrs:
            if k == 'id':
                self.ids.append(v)
        if tag not in VOID:
            self.stack.append((tag, self.getpos()[0]))

    def handle_startendtag(self, tag, attrs):
        for k, v in attrs:
            if k == 'id':
                self.ids.append(v)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if self.stack and self.stack[-1][0] == tag:
            self.stack.pop()
        else:
            open_tag = self.stack[-1] if self.stack else None
            self.problems.append(f'line {self.getpos()[0]}: </{tag}> closes {open_tag}')


def github_slugs(md_text):
    slugs, seen, fenced = set(), {}, False
    for line in md_text.splitlines():
        if line.lstrip().startswith('```'):
            fenced = not fenced
            continue
        m = None if fenced else re.match(r'^#{1,6}\s+(.*?)\s*#*\s*$', line)
        if not m:
            continue
        text = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', m.group(1)).replace('`', '')
        slug = re.sub(r'[^\w\- ]', '', text.strip().lower()).replace(' ', '-')
        n = seen.get(slug, 0)
        seen[slug] = n + 1
        slugs.add(slug if n == 0 else f'{slug}-{n}')
    return slugs


def text_of(fragment):
    return html.unescape(re.sub(r'<[^>]+>', '', fragment)).strip()


def check_lesson(path, frag, slug_cache):
    problems = []
    m = FIRST_LINE.match(frag)
    if not m:
        return ['first line must be <section class="lesson" data-lesson="NN" data-title="..." data-minutes="N" hidden>']
    if m.group(1) != path.stem:
        problems.append(f'data-lesson="{m.group(1)}" does not match the file name')
    if not frag.rstrip().endswith('</section>'):
        problems.append('must end with </section>')
    if '—' in frag:
        problems.append(f'{frag.count(chr(0x2014))} em dash(es); rewrite those sentences')
    for bad in ('TrueMed', 'TRUEMED'):
        if bad in frag:
            problems.append(f'write "Truemed", not "{bad}"')

    articles = re.findall(r'<article class="screen[^"]*"([^>]*)>(.*?)</article>', frag, re.S)
    if len(articles) < 4:
        problems.append(f'only {len(articles)} screens')
    for k, (attrs, body) in enumerate(articles):
        where = f'screen {k}'
        title = re.search(r'data-title="([^"]*)"', attrs)
        if k == 0 and (not title or title.group(1) != 'Start'):
            problems.append('first screen needs data-title="Start"')
        if k == len(articles) - 1 and (not title or title.group(1) != 'Done'):
            problems.append('last screen needs data-title="Done"')
        if 0 < k < len(articles) - 1 and not re.search(r'<h2[ >]', body):
            problems.append(f'{where}: needs an <h2> headline')
        talk = re.search(r'<div class="talk" hidden>(.*?)</div>\s*$', body, re.S)
        if not talk:
            problems.append(f'{where}: needs <div class="talk" hidden> as its last child')
            continue
        paras = re.findall(r'<p( class="inclass")?>(.*?)</p>', talk.group(1), re.S)
        spoken = [text_of(p) for cls, p in paras if not cls]
        if not spoken:
            problems.append(f'{where}: talk track has no spoken paragraph')
        if any(not p for p in spoken):
            problems.append(f'{where}: empty talk paragraph')
        for p in spoken:
            if len(p) > TALK_MAX_CHARS:
                problems.append(f'{where}: a talk paragraph is {len(p)} chars (max {TALK_MAX_CHARS})')

    for raw in re.findall(r'<script type="application/json" class="say">(.*?)</script>', frag, re.S):
        r = subprocess.run(['node', '-e', CHECK_SAY, raw], capture_output=True, text=True)
        if r.returncode:
            problems.append(f'say list: {r.stderr.strip().splitlines()[-1]}')

    for href in re.findall(r'href="([^"]+)"', frag):
        if href.startswith('#lesson-') or href == '#map':
            continue
        link = MODULE_LINK.match(href)
        if link:
            name, anchor = link.group(1) + '.md', link.group(2)
            md = MODULES / name
            if not md.exists():
                problems.append(f'link to missing module file {name}')
                continue
            if anchor:
                slugs = slug_cache.setdefault(name, github_slugs(md.read_text()))
                if anchor not in slugs:
                    problems.append(f'link anchor #{anchor} not found in {name}')
        elif href.startswith('#'):
            problems.append(f'in-page link {href}: use #lesson-NN or #map')
        elif href.startswith('../') or 'github.com/bryanroscoe/not-writing-code/blob/' in href:
            problems.append(f'link {href}: link modules as ../modules/NN-name/#anchor')
    return problems


def check_scripts(page):
    problems = []
    scripts = re.findall(r'<script>(.*?)</script>', page, re.S)
    with tempfile.TemporaryDirectory() as tmp:
        for k, js in enumerate(scripts):
            f = Path(tmp) / f's{k}.js'
            f.write_text(js)
            r = subprocess.run(['node', '--check', str(f)], capture_output=True, text=True)
            if r.returncode:
                problems.append(f'script {k} does not parse: {r.stderr.strip().splitlines()[-1]}')
    return problems


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--only', help='build and check just this lesson, into build/lessons/NN.html')
    args = ap.parse_args()

    shell = (LESSONS / 'shell.html').read_text()
    lesson_paths = sorted(LESSONS.glob('[0-9][0-9].html'))
    problems, frags, slug_cache = [], [], {}
    if args.only:
        lesson_paths = [p for p in lesson_paths if p.stem == args.only]
        if not lesson_paths:
            sys.exit(f'no lessons/{args.only}.html')
    for path in lesson_paths:
        frag = path.read_text()
        frags.append(frag.rstrip() + '\n')
        for p in check_lesson(path, frag, slug_cache):
            problems.append(f'{path.name}: {p}')

    page = shell.replace('<!-- LESSONS -->', '\n'.join(frags))
    bal = Balance()
    bal.feed(page)
    problems += [f'page: {p}' for p in bal.problems]
    if bal.stack:
        problems.append(f'page: unclosed tags {bal.stack[:5]}')
    dupes = sorted({i for i in bal.ids if bal.ids.count(i) > 1})
    if dupes:
        problems.append(f'page: duplicate ids {dupes} (prefix lesson ids with lNN-)')
    problems += [f'page: {p}' for p in check_scripts(page)]

    out = ROOT / 'build' / 'lessons' / f'{args.only}.html' if args.only else ROOT / 'site' / 'lessons' / 'index.html'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page)
    for path, frag in zip(lesson_paths, frags):
        screens = len(re.findall(r'<article class="screen', frag))
        talk = ' '.join(text_of(t) for t in re.findall(r'<div class="talk" hidden>(.*?)</div>', frag, re.S))
        print(f'{path.stem}: {screens} screens, {len(talk.split())} spoken words')
    print(f'{out.relative_to(ROOT)}: {len(page) // 1024} KB')
    if problems:
        print('\nPROBLEMS')
        print('\n'.join(problems))
        sys.exit(1)


if __name__ == '__main__':
    main()

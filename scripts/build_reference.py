#!/usr/bin/env python3
"""Harvest glossary terms and papers from module files.

Usage: python3 scripts/build_reference.py
Rewrites everything after the BEGIN GENERATED marker in reference/glossary.md and
reference/papers.md. Text above the marker is hand-written and kept.
"""
import pathlib
import re

root = pathlib.Path(__file__).resolve().parent.parent
MARKER = "<!-- BEGIN GENERATED: edit the modules, then run python3 scripts/build_reference.py -->"


def write_generated(path, body):
    text = path.read_text()
    head = text[: text.index(MARKER) + len(MARKER)]
    path.write_text(head + "\n\n" + body.strip() + "\n")

mods = sorted((root / "modules").glob("[0-9][0-9]-*.md"))


def title_of(text):
    m = re.search(r"^# (.+)$", text, re.M)
    return m.group(1).strip() if m else ""


def section(text, name):
    m = re.search(rf"^## {re.escape(name)}\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1) if m else ""


# ---------- glossary ----------
terms = {}  # key -> dict(term, definition, modules[])
for p in mods:
    text = p.read_text()
    num = p.name[:2]
    for line in section(text, "Terms introduced").splitlines():
        m = re.match(r"^- \*\*(.+?)\*\*:?\s*:?\s*(.+)$", line.strip())
        if not m:
            continue
        term = m.group(1).rstrip(":").strip()
        definition = m.group(2).lstrip(": ").strip()
        key = re.sub(r"[^a-z0-9]+", " ", term.lower()).strip()
        entry = terms.setdefault(key, {"term": term, "def": definition, "mods": []})
        if num not in entry["mods"]:
            entry["mods"].append((num, p.name))

def sort_key(k):
    t = terms[k]["term"]
    t = re.sub(r"^[^A-Za-z0-9]+", "", t)
    return t.lower()

out = []
current = None
for key in sorted(terms, key=sort_key):
    e = terms[key]
    first = re.sub(r"^[^A-Za-z0-9]+", "", e["term"])[:1].upper()
    letter = first if first.isalpha() else "#"
    if letter != current:
        current = letter
        out.append(f"\n## {letter}\n")
    links = ", ".join(f"[{n}](../modules/{fn})" for n, fn in e["mods"])
    d = e["def"]
    d = d[0].upper() + d[1:] if d else d
    out.append(f"- **{e['term']}**: {d} ({links})")
write_generated(root / "reference" / "glossary.md", "\n".join(out))
print("terms:", len(terms))

# ---------- papers ----------
papers = {}  # arxiv id -> dict(line, mods)
order = []
arx = re.compile(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})")
for p in mods:
    text = p.read_text()
    num = p.name[:2]
    src = section(text, "Sources and further reading")
    for line in src.splitlines():
        s = line.strip()
        if not s.startswith(("-", "*")):
            continue
        ids = arx.findall(s)
        if not ids:
            continue
        pid = ids[0]
        if pid not in papers:
            papers[pid] = {"line": s.lstrip("-* ").strip(), "mods": [], "home": (num, p.name, title_of(text))}
            order.append(pid)
        if num not in [m[0] for m in papers[pid]["mods"]]:
            papers[pid]["mods"].append((num, p.name))

groups = {}
for pid in order:
    groups.setdefault(papers[pid]["home"], []).append(pid)

out = []
for (num, fn, title), pids in sorted(groups.items()):
    out.append(f"\n## {title}\n\n[Module {num}](../modules/{fn})\n")
    for pid in pids:
        e = papers[pid]
        also = [f"[{n}](../modules/{f})" for n, f in e["mods"] if n != num]
        suffix = f" · also cited in {', '.join(also)}" if also else ""
        out.append(f"- {e['line']}{suffix}")
write_generated(root / "reference" / "papers.md", "\n".join(out))
print("papers:", len(papers))

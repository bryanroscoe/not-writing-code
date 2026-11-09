# Slides

> **Last verified:** 2026-11-08

One slide deck per module, written in [Marp](https://marp.app/) Markdown. Each deck is a 30–50 minute talk or class session. The module it's built from is the reading that goes with it.

The decks are built to HTML, PDF, and PowerPoint on every push to `main` and published with the site. To present, open a deck's HTML version and press `F` for full screen; `P` opens presenter view with speaker notes.

| # | Deck | Module |
| --- | --- | --- |
| 00 | [Orientation](00-orientation.md) | [00](../modules/00-orientation.md) |
| 01 | [What is an LLM?](01-what-is-an-llm.md) | [01](../modules/01-what-is-an-llm.md) |
| 02 | [Training, tuning, and self-tuning](02-training-and-tuning.md) | [02](../modules/02-training-and-tuning.md) |
| 03 | [The model landscape](03-model-landscape.md) | [03](../modules/03-model-landscape.md) |
| 04 | [Open weight vs closed weight](04-open-vs-closed-weights.md) | [04](../modules/04-open-vs-closed-weights.md) |
| 05 | [How to tell if a model is good](05-judging-models.md) | [05](../modules/05-judging-models.md) |
| 06 | [Harnesses, tools, and MCP](06-harnesses-and-tools.md) | [06](../modules/06-harnesses-and-tools.md) |
| 07 | [Context engineering and the buzzwords](07-context-engineering.md) | [07](../modules/07-context-engineering.md) |
| 08 | [Agentic workflows](08-agentic-workflows.md) | [08](../modules/08-agentic-workflows.md) |
| 09 | [Multiple agents](09-multi-agent-systems.md) | [09](../modules/09-multi-agent-systems.md) |
| 10 | [AI code review](10-ai-code-review.md) | [10](../modules/10-ai-code-review.md) |
| 11 | [Security and prompt injection](11-security-and-prompt-injection.md) | [11](../modules/11-security-and-prompt-injection.md) |
| 12 | [Costs](12-costs-subscriptions-and-apis.md) | [12](../modules/12-costs-subscriptions-and-apis.md) |
| 13 | [Open-source ecosystem](13-open-source-ecosystem.md) | [13](../modules/13-open-source-ecosystem.md) |
| 14 | [Keeping up](14-keeping-up.md) | [14](../modules/14-keeping-up.md) |
| 15 | [Learning, careers, and responsibility](15-learning-careers-and-responsibility.md) | [15](../modules/15-learning-careers-and-responsibility.md) |

## Building locally

```bash
npx @marp-team/marp-cli@4 --theme-set slides/theme --input-dir slides --output site/slides --html
```

Add `--pdf` or `--pptx` for those formats (they need a local Chrome or Chromium).

## Writing a deck

Every deck follows the same conventions, so they look and feel like one course.

**Front matter** (copy and edit):

```markdown
---
marp: true
theme: not-writing-code
paginate: true
title: "08: Agentic workflows"
description: "How much autonomy actually works"
footer: "A Brief Introduction to Not Writing Code · 08 Agentic workflows"
---
```

**Structure**, in order:

1. Title slide, with `<!-- _class: lead -->`: module number and title, one-line subtitle.
2. "Why this matters": one slide, the stakes in plain language.
3. The core ideas: one idea per slide, usually 8–20 slides. Use `<!-- _class: divider -->` slides to split a deck into two or three parts.
4. Bryan's take slides, with `<!-- _class: take -->`. Quote the module's callouts word for word, as `> **Bryan's take:** …`. Never write new opinions.
5. "Try it": the module's exercise, condensed.
6. Discussion: two to four questions from the module.
7. "Read more": a link to the module on the site (`../modules/NN-slug/`) and two or three key sources.

**Slide rules:**

- One idea per slide. At most six bullets, at most about twelve words each.
- Prefer a table, a short code block, or a single sentence in large type over a wall of bullets.
- Put the detail in **speaker notes**: an HTML comment at the end of the slide (`<!-- … -->`) becomes presenter notes. Notes should let someone other than Bryan give the talk.
- Facts, numbers, and dates come from the module, which is the source of truth. Don't add facts the module doesn't have.
- Date anything volatile ("as of November 2026").
- No images that need separate files. Marp doesn't render Mermaid, so redraw diagrams as tables, arrows in text (`explore → plan → implement → verify → commit`), or short lists.

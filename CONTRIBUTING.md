# Contributing and style guide

This knowledge base teaches **AI-accelerated software engineering**: using large
language models and coding agents to build real software faster *without* giving
up engineering judgment. It is not about "vibe coding," which means never
reading the code. Mention vibe coding where it's relevant and define it, but
don't use it as the name for what this course teaches (see
[module 00](modules/00-orientation.md)).

The same material serves three audiences:

| Audience | Starting point | What they need |
| --- | --- | --- |
| **Students** (e.g., a university course) | Can program a little; have used ChatGPT | Mental models, fundamentals, safe habits, hands-on labs |
| **Working engineers** | Ship code daily; may be AI-skeptical or AI-casual | Concrete workflows, tool choices, where it breaks, how to go AI-first |
| **Leads and champions** | Want their team to adopt AI well | Adoption playbook, costs, policy, how to measure, how to answer objections |

Rather than writing three versions of everything, every module is layered by
depth, and the [learning paths](paths/) tell each audience what to read.

## File map

Modules are numbered in reading order. Link between them with relative links.

| File | Topic |
| --- | --- |
| `modules/00-orientation.md` | AI-accelerated coding vs vibe coding, how to use this, why it moves so fast |
| `modules/01-what-is-an-llm.md` | Tokens, transformers, pretraining, post-training, reasoning models, limits |
| `modules/02-training-and-tuning.md` | How models are made, fine-tuned (LoRA etc.), distilled, and how models now tune themselves |
| `modules/03-model-landscape.md` | The labs, the current lineups, who leads where, the best model for the job |
| `modules/04-open-vs-closed-weights.md` | Open weight vs closed, licenses, running locally, where open models sit in the chain |
| `modules/05-judging-models.md` | Benchmarks, how to read them, benchmark-maxing, vibes, building your own evals |
| `modules/06-harnesses-and-tools.md` | Chat, IDE, CLI and cloud agents; MCP; skills; hooks; closed products built on top |
| `modules/07-context-engineering.md` | Prompt → context → harness → loop → graph engineering; CLAUDE.md/AGENTS.md history |
| `modules/08-agentic-workflows.md` | Day-to-day workflows, Yegge's levels, parallel agents, how much autonomy works |
| `modules/09-multi-agent-systems.md` | Multiple agents building and reviewing; what the research says |
| `modules/10-ai-code-review.md` | Review tools, multi-model review, keeping humans accountable |
| `modules/11-security-and-prompt-injection.md` | Prompt injection, the lethal trifecta, sandboxing, supply chain |
| `modules/12-costs-subscriptions-and-apis.md` | Subscriptions vs API billing, real costs, rate limits, budgeting |
| `modules/13-open-source-ecosystem.md` | Open-source harnesses, inference engines, frameworks, MCP servers |
| `modules/14-keeping-up.md` | Velocity, regressions, model ups and downs, which sources to trust |
| `modules/15-learning-careers-and-responsibility.md` | Skill formation, academic integrity, careers, ethics, data policy |
| `reference/glossary.md` | Every term, one or two sentences each |
| `reference/papers.md` | Annotated reading list of research papers |
| `reference/timeline.md` | Dated history, 2017 to now |
| `paths/*.md` | Reading paths per audience |
| `slides/*.md` | One Marp slide deck per module (conventions in `slides/README.md`) |
| `course/` | A semester course built from the modules, with labs |
| `workplace/` | AI-first adoption playbook for engineering teams |

## Module template

Every module follows this shape so readers can skip to the depth they need:

```markdown
# NN: Title

*About a 25-minute read. Last checked November 8, 2026.*

**TL;DR**
- Three to six bullets a busy person can stop after.

## Foundations
Concepts with no assumed background. Analogies welcome. Define every term on first use.

## In practice
What working engineers actually do with this. Concrete commands, prompts,
checklists, failure modes, war stories.

## Going deeper
Research, internals, open debates, edge cases. Optional for beginners.

## Bryan's take
Opinions, clearly labelled (see below). Optional per module.

## Try it
Hands-on exercises: one for individuals, one for a class or team.

## Discussion questions
Three to six questions for a classroom or a lunch-and-learn.

## Sources and further reading
Papers first, then primary sources, then good commentary.
```

Use `###` subheadings freely inside each level.

## Voice

Write the way Bryan talks: an experienced engineer explaining this to a smart colleague or a student over lunch.

- Direct and plain. Short sentences, everyday words, contractions. Say the thing.
- Conversational, not cute. "Kind of," "pretty good," "goes off the rails" are fine where they fit naturally. Don't force it.
- Candid about limits. "Nobody really knows yet" beats a stack of hedges. Keep the one qualifier that's true.
- Practical. What to do, what breaks, why it matters on a real team.
- Talk to the reader as "you."
- Teach mental models that will survive the next model release, then give the current specifics as examples.
- No AI slop: no "it's important to note," "let's dive in," "unlock," "leverage," "robust," "seamless," "game-changer," reflexive "it's not X, it's Y," or every paragraph ending on a tidy moral.
- Running text can sound like Bryan, but don't put experiences or opinions in his mouth. Those go in callouts, in his words.
- Avoid microcopy: UI-style labels ("Note:", "Tip:", "Key point:"), badges, breadcrumb asides like "(see above)", "click here," decorative bold and arrows. Fold them into a sentence or cut them.

## Opinions vs facts

The author, Bryan Roscoe, has strong opinions from daily use. They are valuable
and they are opinions. Mark them:

```markdown
> **Bryan's take:** I don't trust fully autonomous agent pipelines yet. ...
```

- Never state an opinion as a fact in the main text.
- When credible people disagree, say so and give the strongest counterpoint.
- Opinions about specific labs or models are dated, like everything else.

## Freshness

This field changes monthly. To keep the material useful:

- Put "*About an N-minute read. Last checked Month D, YYYY.*" under each module title, and update the date when you re-check facts. No other labels in the header; the [learning paths](paths/) say who should read what.
- Mark volatile facts inline: "(as of November 2026)."
- Keep specific model versions, prices, and leaderboard numbers mostly in
  [module 03](modules/03-model-landscape.md), [module 12](modules/12-costs-subscriptions-and-apis.md),
  and the [timeline](reference/timeline.md). Elsewhere, refer to them by tier or link there.
- Prefer durable concepts (the agent loop, context limits, injection) over
  product trivia.

## Sources

- Prefer primary sources: papers (arXiv, conference proceedings), lab
  announcements, system cards, official docs, the author's own blog.
- Cite papers as `[Title](https://arxiv.org/abs/XXXX.XXXXX) (Authors, Year)`.
- Reputable journalism is fine for context and reception.
- Avoid SEO aggregator and auto-generated "AI news" sites. Many of them
  invent or garble model details.
- If a claim can't be verified, say "reported" and name the source, or leave it out.

## Formatting

- GitHub-flavored Markdown. Tables, footnotes, and
  [GitHub alerts](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#alerts)
  (`> [!WARNING]`) are fine. Mermaid diagrams render on GitHub; use them when a picture
  explains a mechanism better than prose.
- Code blocks get a language tag.
- One sentence per idea; keep paragraphs short.

## Tooling

CI runs all of these on every pull request.

- `python3 scripts/check_links.py` checks that every relative link and heading anchor resolves.
- `python3 scripts/build_reference.py` regenerates the generated halves of `reference/glossary.md` (from each module's "Terms introduced") and `reference/papers.md` (from each module's "Sources and further reading"). Text above the `BEGIN GENERATED` marker is hand-written and kept. Write terms as `- **Term**: definition`.
- `python3 scripts/build_site.py` builds the website (MkDocs Material) and the slide decks (Marp) into `site/`. It needs `pip install -r requirements-site.txt` and Node.js. Add `--pdf --pptx` for downloadable decks (needs Chrome), or `--no-slides` to skip Node. Merges to `main` deploy the site to GitHub Pages.

## Privacy

Keep any specific employer, client, or private project out of this repository.
The workplace material is written for "an engineering team" in general.

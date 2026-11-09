<img src="assets/icon.svg" width="64" height="64" alt="">

# A Brief Introduction to Not Writing Code

**A knowledge base and short course on AI-accelerated software engineering.** It goes from "what is a language model?" to running several coding agents in parallel and having them review each other's work, while you stay the one accountable for what ships.

The title is a joke with a point. You'll write a lot less code by hand, and do a lot more engineering. "Vibe coding" originally meant prompting an AI and never reading the code. This material uses the popular name and teaches the disciplined version: AI does most of the typing; humans decide, verify, and own the result. See [what we mean by vibe coding](modules/00-orientation.md#what-we-mean-by-vibe-coding).

> **Status:** first full draft, November 2026. Facts are dated in each module's header. The field moves monthly, so check the **Last verified** date before you rely on a specific model name or price.

## Start here

| You are | Read this | Then |
| --- | --- | --- |
| A **student** or new to AI coding tools | [Student path](paths/students.md) | The [semester course](course/syllabus.md) and its [labs](course/labs/) |
| A **working engineer** | [Engineer path](paths/engineers.md) | The two-week practice plan at the end of it |
| A **lead or AI champion** bringing a team along | [Leads path](paths/leads.md) | The [workplace playbook](workplace/ai-first-playbook.md) |

Everyone should read [00: Orientation](modules/00-orientation.md) first. It's 20 minutes.

## The modules

Every module has the same layers: **Foundations** (no background assumed), **In practice** (what working engineers do), **Going deeper** (research and open debates), plus hands-on exercises and discussion questions. Read the layers that fit you.

| # | Module | What you'll learn |
| --- | --- | --- |
| 00 | [Orientation](modules/00-orientation.md) | What this is, what "vibe coding" means here, six ideas that outlast the hype |
| 01 | [What is an LLM?](modules/01-what-is-an-llm.md) | Tokens, transformers ("Attention Is All You Need"), pretraining, reasoning models, hallucination |
| 02 | [Training, tuning, and self-tuning](modules/02-training-and-tuning.md) | How models are made, fine-tuning open weights with LoRA, distillation, models that update their own weights |
| 03 | [The model landscape](modules/03-model-landscape.md) | The labs, current lineups, where Meta's Muse fits, the best model for each job |
| 04 | [Open weight vs closed weight](modules/04-open-vs-closed-weights.md) | Licenses, running models locally, where open models sit in the chain |
| 05 | [How to tell if a model is good](modules/05-judging-models.md) | Benchmarks and their flaws, benchmark-maxing, productivity studies, building your own eval |
| 06 | [Harnesses, tools, and MCP](modules/06-harnesses-and-tools.md) | Chat vs IDE vs CLI vs cloud agents, MCP, skills, hooks, products like Claude Design |
| 07 | [Context engineering and the buzzwords](modules/07-context-engineering.md) | Prompt → context → harness → loop → graph engineering, and the rise and fall of giant `CLAUDE.md` files |
| 08 | [Agentic workflows](modules/08-agentic-workflows.md) | The workflow that works, Yegge's eight stages, how much autonomy is real today |
| 09 | [Multiple agents](modules/09-multi-agent-systems.md) | Agents building and reviewing together, and what the research says |
| 10 | [AI code review](modules/10-ai-code-review.md) | Review tools, cross-model review, how humans should review AI-written code |
| 11 | [Security and prompt injection](modules/11-security-and-prompt-injection.md) | Why injection is unsolved, the lethal trifecta, real incidents, sandboxing |
| 12 | [Costs](modules/12-costs-subscriptions-and-apis.md) | Subscriptions vs API billing, why agents eat tokens, a worked cost example |
| 13 | [Open-source ecosystem](modules/13-open-source-ecosystem.md) | Open harnesses, inference engines, frameworks, and the AI-slop problem for maintainers |
| 14 | [Keeping up](modules/14-keeping-up.md) | Model ups and downs, which sources to trust, a sustainable routine |
| 15 | [Learning, careers, and responsibility](modules/15-learning-careers-and-responsibility.md) | Learning with AI without losing the skill, careers, privacy, licensing, ethics |

## Also in this repo

- **[Course](course/)**: a 15-week course proposal with a [syllabus](course/syllabus.md), an [instructor guide](course/instructor-guide.md), and eight labs.
- **[Workplace](workplace/)**: an [AI-first rollout playbook](workplace/ai-first-playbook.md), [honest answers to common objections](workplace/objections.md), a ready-to-run [internal session series](workplace/session-series.md), and a [team policy template](workplace/policy-template.md).
- **[Reference](reference/)**: a [glossary](reference/glossary.md) of 300+ terms, an annotated [reading list](reference/papers.md) of 180+ research papers (start with the short list of eighteen), and a dated [timeline](reference/timeline.md) from 2017 to now.

## Conventions

- **Bryan's take** callouts are the author's opinions from daily use, clearly labelled. Everything else should be sourced. When credible people disagree, the module says so.
- **Last verified** dates appear at the top of each module. Specific model names, prices, and benchmark numbers are kept mostly in [module 03](modules/03-model-landscape.md), [module 12](modules/12-costs-subscriptions-and-apis.md), and the [timeline](reference/timeline.md) so they're easy to refresh.
- Papers are linked wherever a claim rests on research.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the module template, voice, and sourcing rules. Found something wrong or stale? That's a bug; please open an issue or a pull request with a source.

## License

The written material and slides are [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/): reuse and adapt them with credit. The scripts and build configuration are MIT. See [LICENSE](LICENSE).

## About

Written by Bryan Roscoe, a software engineer who works this way every day, with research and drafting help from coding agents. [Module 00 explains how it was made](modules/00-orientation.md#how-this-material-was-made).

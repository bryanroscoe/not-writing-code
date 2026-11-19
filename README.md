<img src="assets/icon.svg" width="64" height="64" alt="">

# A Brief Introduction to Not Writing Code

A knowledge base and short course on AI-accelerated software engineering, from "what is a language model?" to running several coding agents in parallel and having them review each other's work. You're accountable for what ships.

You'll write a lot less code by hand. You still have to do the engineering. This isn't a vibe coding course: vibe coding means prompting an AI and never reading the code. This is [AI-accelerated coding](modules/00-orientation.md#ai-accelerated-coding-not-vibe-coding), where AI does a lot of the typing and people decide, verify, and own the result.

This is the first full draft (November 2026). Facts are dated in each module's header. The field moves monthly, so check the Last checked date before you rely on a specific model name or price.

## Start here

| You are | Read this | Then |
| --- | --- | --- |
| A **student** or new to AI coding tools | [Student path](paths/students.md) | The [semester course](course/syllabus.md) and its [labs](course/labs/) |
| A **working engineer** | [Engineer path](paths/engineers.md) | The two-week practice plan at the end of it |
| A **lead or AI champion** bringing a team along | [Leads path](paths/leads.md) | The [workplace playbook](workplace/ai-first-playbook.md) |

Everyone should read [00: Orientation](modules/00-orientation.md) first. It's 20 minutes.

## The modules

Every module has the same layers: Foundations (no background assumed), In practice (what working engineers do), and Going deeper (research and open debates), plus hands-on exercises and discussion questions. Read the parts you need.

| # | Module | What you'll learn |
| --- | --- | --- |
| 00 | [Orientation](modules/00-orientation.md) | What this is, AI-accelerated coding vs vibe coding, six ideas that outlast the hype |

### Stage 1: How the machine works

| # | Module | What you'll learn |
| --- | --- | --- |
| 01 | [What is an LLM?](modules/01-what-is-an-llm.md) | Tokens, transformers ("Attention Is All You Need"), pretraining, reasoning models, hallucination |
| 02 | [How a model is made](modules/02-how-a-model-is-made.md) | Data, pretraining, distillation, and quantization: how a base model gets made |
| 03 | [Post-training and reinforcement learning](modules/03-post-training-and-rl.md) | Post-training and RL, fine-tuning open weights with LoRA, models that update their own weights |

### Stage 2: Choosing a model

| # | Module | What you'll learn |
| --- | --- | --- |
| 05 | [The model landscape](modules/05-model-landscape.md) | The labs, current lineups, where Meta's Muse fits, the best model for each job |
| 06 | [Open weight vs closed weight](modules/06-open-vs-closed-weights.md) | Licenses, running models locally, where open models sit in the chain |
| 07 | [How to tell if a model is good](modules/07-judging-models.md) | Benchmarks and their flaws, benchmark-maxing, productivity studies, building your own eval |

### Stage 3: Working with agents

| # | Module | What you'll learn |
| --- | --- | --- |
| 08 | [Harnesses, tools, and MCP](modules/08-harnesses-and-tools.md) | Chat vs IDE vs CLI vs cloud agents, MCP, skills, hooks, products like Claude Design |
| 09 | [Context engineering and the buzzwords](modules/09-context-engineering.md) | Prompt → context → harness → loop → graph engineering, and the rise and fall of giant `CLAUDE.md` files |
| 10 | [Agentic workflows](modules/10-agentic-workflows.md) | The workflow that works, Yegge's eight stages, how much autonomy is real today |

### Stage 4: Trusting the output

| # | Module | What you'll learn |
| --- | --- | --- |
| 12 | [Multiple agents](modules/12-multi-agent-systems.md) | Agents building and reviewing together, and what the research says |
| 13 | [AI code review](modules/13-ai-code-review.md) | Review tools, cross-model review, how humans should review AI-written code |
| 14 | [Security and prompt injection](modules/14-security-and-prompt-injection.md) | Why injection is unsolved, the lethal trifecta, real incidents, sandboxing |

### Stage 5: Practice for the long run

| # | Module | What you'll learn |
| --- | --- | --- |
| 15 | [Costs](modules/15-costs-subscriptions-and-apis.md) | Subscriptions vs API billing, why agents eat tokens, a worked cost example |
| 16 | [Open-source ecosystem](modules/16-open-source-ecosystem.md) | Open harnesses, inference engines, frameworks, and the AI-slop problem for maintainers |
| 17 | [Keeping up](modules/17-keeping-up.md) | Model ups and downs, which sources to trust, a sustainable routine |
| 18 | [Learning, careers, and responsibility](modules/18-learning-careers-and-responsibility.md) | Learning with AI without losing the skill, careers, privacy, licensing, ethics |

## Also in this repo

- A 15-week [course](course/) proposal with a [syllabus](course/syllabus.md), an [instructor guide](course/instructor-guide.md), and eight labs.
- [Workplace](workplace/) material with an [AI-first rollout playbook](workplace/ai-first-playbook.md), [honest answers to common objections](workplace/objections.md), a ready-to-run [internal session series](workplace/session-series.md), and a [team policy template](workplace/policy-template.md).
- [Reference](reference/) pages with a [glossary](reference/glossary.md) of 300+ terms, an annotated [reading list](reference/papers.md) of 180+ research papers (start with the short list of eighteen), and a dated [timeline](reference/timeline.md) from 2017 to now.

## Conventions

- Bryan's take callouts are the author's opinions from daily use, clearly labelled. Everything else should be sourced. When credible people disagree, the module says so.
- Each module has a Last checked date at the top. Specific model names, prices, and benchmark numbers are kept mostly in [module 05](modules/05-model-landscape.md), [module 15](modules/15-costs-subscriptions-and-apis.md), and the [timeline](reference/timeline.md) so they're easy to refresh.
- Papers are linked wherever a claim rests on research.

## Contributing

[CONTRIBUTING.md](CONTRIBUTING.md) has the module template, voice, and sourcing rules. Anything wrong or stale is a bug, so please open an issue or a pull request with a source.

## License

The written material and slides are [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/): reuse and adapt them with credit. The scripts and build configuration are MIT. See [LICENSE](LICENSE).

## About

Written by Bryan Roscoe, a software engineer who works this way every day, with research and drafting help from coding agents. [Module 00 explains how it was made](modules/00-orientation.md#how-this-material-was-made).

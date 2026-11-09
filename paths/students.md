# Student path

> **For:** university students, bootcamp learners, and anyone who can program a little and has used ChatGPT but not a coding agent.
> **Time:** one semester (see the [course syllabus](../course/syllabus.md)), or about 15 hours of reading plus labs if you're self-paced.

## What you'll be able to do at the end

- Explain what a language model is and isn't, well enough to predict where it will fail.
- Use a coding agent to explore, plan, build, test, and review a small project, while understanding every line you submit.
- Tell a good model claim from marketing, and test a model on your own tasks.
- Spot prompt injection and other security risks before they bite you.
- Use AI in a way that makes you a *better* programmer, not a dependent one.

## How to read each module

Every module has three depth levels. On this path:

- **Read** Foundations and In practice.
- **Skim** Going deeper. Read it when a topic grabs you, or when the syllabus says to.
- **Do** the "Try it" exercises. They're short and they're where the learning happens.
- **Skip** nothing in the TL;DR and Bryan's take. They're short.

## The path

Read in this order. It's not quite numeric: we get you using tools early, then come back for the theory once you have something to hang it on.

| Step | Module | Focus on | Lab |
| --- | --- | --- | --- |
| 1 | [00 Orientation](../modules/00-orientation.md) | "What we mean by vibe coding," the six durable ideas, ground rules | |
| 2 | [01 What is an LLM?](../modules/01-what-is-an-llm.md) | Next-token prediction, tokens, "What an LLM is not," hallucination | [Lab 1](../course/labs/lab-01-tokens-and-temperature.md) |
| 3 | [06 Harnesses, tools, and MCP](../modules/06-harnesses-and-tools.md) | What a harness is, the short history, "A sane baseline setup" | [Lab 2](../course/labs/lab-02-first-agent-session.md) |
| 4 | [07 Context engineering](../modules/07-context-engineering.md) | Prompting basics, what fills the context window, context limits | |
| 5 | [08 Agentic workflows](../modules/08-agentic-workflows.md) | The agent loop, explore → plan → implement → verify → commit, tests as the contract, failure modes | [Lab 3](../course/labs/lab-03-plan-test-build.md) |
| 6 | [15 Learning, careers, and responsibility](../modules/15-learning-careers-and-responsibility.md) | What the evidence says about learning, "How to learn with AI," academic integrity | |
| 7 | [10 AI code review](../modules/10-ai-code-review.md) | How AI reviewers work, how humans should review AI-written PRs | [Lab 4](../course/labs/lab-04-review-ai-code.md) |
| 8 | [11 Security and prompt injection](../modules/11-security-and-prompt-injection.md) | Instructions and data share one channel, the lethal trifecta, student checklist | [Lab 5](../course/labs/lab-05-prompt-injection.md) |
| 9 | [03 The model landscape](../modules/03-model-landscape.md) | How to read model names and tiers, "Best model for the job" | |
| 10 | [05 How to tell if a model is good](../modules/05-judging-models.md) | What a benchmark is, the benchmark-claim checklist, build your own eval | [Lab 6](../course/labs/lab-06-your-own-eval.md) |
| 11 | [09 Multiple agents](../modules/09-multi-agent-systems.md) | Why and why not, building vs reviewing, cross-model review | [Lab 7](../course/labs/lab-07-multi-agent-review.md) |
| 12 | [02 Training and tuning](../modules/02-training-and-tuning.md) | The pipeline at a glance, distillation, "Models that tune themselves" | |
| 13 | [04 Open vs closed weights](../modules/04-open-vs-closed-weights.md) | The openness spectrum, licenses, the hardware math | |
| 14 | [12 Costs](../modules/12-costs-subscriptions-and-apis.md) | Three ways to pay, why agentic coding eats tokens | |
| 15 | [13 Open-source ecosystem](../modules/13-open-source-ecosystem.md) | A map of the stack, etiquette, "How students can contribute" | [Lab 8](../course/labs/lab-08-open-source-contribution.md) |
| 16 | [14 Keeping up](../modules/14-keeping-up.md) | What stays stable, a curated information diet, a sustainable routine | |

## If you only have a weekend

Read the TL;DRs of every module, then read these four in full: [00](../modules/00-orientation.md), [01](../modules/01-what-is-an-llm.md), [08](../modules/08-agentic-workflows.md), and [15](../modules/15-learning-careers-and-responsibility.md). Do [Lab 3](../course/labs/lab-03-plan-test-build.md).

## Habits to build from day one

1. **Attempt first.** Spend ten minutes on a problem before you ask an AI. You'll ask a better question, and you'll learn more from the answer ([module 15](../modules/15-learning-careers-and-responsibility.md)).
2. **Ask for hints, not answers,** when the goal is learning. Ask for answers when the goal is shipping. Know which one you're doing.
3. **Read every line you submit.** If you can't explain it, you don't get to submit it.
4. **Make the agent prove it.** "Run the tests and show me the output" beats "does it work?" ([module 08](../modules/08-agentic-workflows.md)).
5. **Keep a "surprised me" log.** Every time a model does something you didn't expect, write one line. It becomes your personal eval set ([module 05](../modules/05-judging-models.md)) and your study guide.
6. **Disclose.** Follow your course's AI policy and say what you used. It's a professional habit, not a confession.

## Where to go next

- The [engineer path](engineers.md) once you have an internship or job.
- The [papers list](../reference/papers.md), starting with the short list of eighteen.
- Contribute to an open-source project with AI help, carefully ([module 13](../modules/13-open-source-ecosystem.md)).

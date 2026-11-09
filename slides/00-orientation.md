---
marp: true
theme: not-writing-code
paginate: true
title: "00: Orientation"
description: "What this course is, what we mean by vibe coding, and how to use it"
footer: "A Brief Introduction to Not Writing Code · 00 Orientation"
---

<!-- _class: lead -->

# 00: Orientation

What this course is, and how to use it

<!--
We start with what "vibe coding" means here, why the field moves so fast, six ideas that outlast the churn, and how to use the material.

Rough timing for a 40-minute session: Part 1 (the term and the stance) about 12 minutes, Part 2 (pace and the durable ideas) about 13 minutes, Part 3 (how to use the course) about 8 minutes, then the exercise and discussion.

Facts in this deck come from module 00, which was last verified in November 2026.
-->

---

## Why this matters

| January 2025 | Late 2026 |
| --- | --- |
| AI as fancy autocomplete | Engineers direct several coding agents at once |
| A chat window you paste code into | Agents read the repo, run commands, test, and open PRs |

Anthropic reports Claude wrote **more than 80%** of its merged code by May 2026.

<!--
Between early 2025 and late 2026, writing software arguably changed more than it had in the previous twenty years. I say "arguably" on purpose. That's a judgment, not a measurement.

The 80% figure is Anthropic's own report about its own codebase, and module 08 covers it. Not every team looks like this. But the tools people tried a couple of years ago are not the tools that exist now.
-->

---

## Who this is for

- Students whose courses ignore or ban the tools, then jobs expect fluency
- Engineers who tried a tool in 2024 and found it wrong half the time
- Leads who want their teams to adopt these tools well

It runs from "what is a language model?" to parallel agents that are reviewed, secure, and affordable.

<!--
Students learn to program in courses that mostly pretend these tools don't exist, or ban them, and then graduate into jobs that expect fluency.

Engineers who tried an AI tool in 2024, found it wrong half the time, and decided it wasn't worth it made a reasonable call. The tools changed.

Leads want adoption done well, which isn't the same as done quickly.

The course starts at "what is a language model?" and ends at running several agents in parallel, reviewing their work with other agents, and keeping it all secure and affordable.
-->

---

<!-- _class: divider -->

# Part 1

## What we mean by "vibe coding"

<!--
Part 1 is about the name, and the stance the whole course takes. About 12 minutes.
-->

---

## Where the phrase came from

> "a new kind of coding I call 'vibe coding', where you fully give in to the vibes, embrace exponentials, and forget that the code even exists"

Andrej Karpathy, February 2, 2025

Describe it → accept the output → paste errors back → never read the diff

<!--
Karpathy is a founding member of OpenAI and a former head of AI at Tesla. His post described a real way of working: you describe what you want, accept whatever the model writes, paste error messages back in, and never read the diff.

For throwaway projects, personal tools, and prototypes, this is useful. For software other people depend on, it's a bad way to build, and that line runs through the whole course.
-->

---

## The disciplined version got its own names

| When | Simon Willison's position |
| --- | --- |
| March 2025 | If you review, test, and can explain it, it isn't vibe coding |
| October 2025 | Proposes "vibe engineering" for the disciplined version |
| Early 2026 | Reports that "agentic engineering" is winning as the name |

<!--
Simon Willison drew the line a month after Karpathy's post. If you review, test, and can explain the code an LLM wrote, that's not vibe coding. That's software development with a powerful assistant.

In October 2025 he proposed "vibe engineering" for the disciplined version. By early 2026 he reported that "agentic engineering" was winning as the name.

You'll hear all three. The last two mean the practice this course teaches.
-->

---

## So why keep the phrase?

People search for "vibe coding course," not "agentic engineering course."

We use the popular phrase and mean the disciplined version.

*A Brief Introduction to Not Writing Code* means you type much less code, so the engineering around it matters more.

<!--
This is a practical choice. The popular phrase stuck, so the course uses it and means the disciplined version throughout.

The course title is the same joke from the other side. You'll type much less code by hand. Deciding what to build, checking it, and answering for it become more of the job.
-->

---

<!-- _class: take -->

## What "vibe coding" means in this course

> **Bryan's take:** When I say vibe coding, I mean AI-accelerated coding, not really vibe coding. The AI does most of the typing. A human still decides what to build, reads what matters, makes sure it's tested, and owns the result. That's the only version I'd teach.

<!--
These "Bryan's take" callouts are where my opinions go. Everything else should be sourced, so an unsourced or stale claim is a bug.

You can disagree with this. Discussion question 1 asks when not reading the code is the right choice.
-->

---

## The spectrum

| Mode | Who writes | Who reads | Good for |
| --- | --- | --- | --- |
| Hand-coding | You | You | Learning, tricky core logic |
| Autocomplete | You, with suggestions | You | Boilerplate, familiar code |
| Chat-assisted | Model writes, you paste | You | Explanations, one-off functions |
| **Supervised agent** | Agent edits the repo | You, every diff | Most professional work today |
| **Parallel supervised agents** | Several agents | You, plus agent cross-review | Experienced users, good tests |
| Background / cloud agents | Agent, unattended | You review the PR | Well-specified, well-tested tasks |
| Pure vibe coding | Model | Nobody | Prototypes, throwaways |
| Fully autonomous pipeline | Agents | Other agents | Contested |

<!--
Go top to bottom. Most of this course lives in the two bold rows: one supervised agent whose every diff you review, and several supervised agents on separate tasks that also cross-review each other's work.

Background or cloud agents work unattended and open a pull request. They suit well-specified, well-tested tasks.

Pure vibe coding is fine for prototypes, personal tools, and throwaways.

The fully autonomous pipeline, where agents review agents and no human reads the code, is contested. Module 08 has the evidence.

Ask the room which row they work in today.
-->

---

## Why the human stays in charge

| Reason | Why it holds |
| --- | --- |
| Accountability doesn't transfer | A model can't be fired, sued, or paged at 3 a.m. |
| The productivity evidence is mixed | Careful studies found experienced developers slower, while feeling faster |
| Learning requires effort | Letting AI do the work can reduce what you learn |

Use AI in a way where you still get better, and where someone can answer for the result.

<!--
This caution may age badly. For now, these three reasons hold.

First, accountability. Whoever merges the change owns it. That holds in a classroom (academic integrity), at work (on-call), and legally (licensing, security, privacy).

Second, productivity. Some of the most careful studies found experienced developers were slower with AI while believing they were faster. Newer studies, in modules 05 and 08, show modest gains with wide error bars. The gains are real for people with good habits, and they aren't automatic.

Third, learning. Studies of students and new developers find that letting AI do the work can reduce what you learn, even when the output is better. For a student, the point of an assignment is the skill, not the artifact. That's module 15.
-->

---

<!-- _class: divider -->

# Part 2

## How fast this moves, and what lasts

<!--
Part 2 is why the course is built the way it is. Things change monthly, so it teaches ideas that survive the churn. About 13 minutes.
-->

---

## Models ship monthly

In 2026 alone (as of November 2026):

| Lab | What shipped |
| --- | --- |
| Anthropic | Eleven generally available models across four tiers |
| OpenAI | GPT-5.3 through GPT-6.1 |
| Google | Cancelled one flagship, launched another, announced a third |

Google's third flagship is open only to vetted cyber defenders so far.

<!--
Anthropic's count is more than a dozen if you include the restricted Mythos versions.

Module 03 and the timeline in the reference section have the names, dates, and sources. Don't memorize them. Look at the pace. The lineup you learn this term will be out of date before the term ends.
-->

---

## Everything else churns too

| What | How fast |
| --- | --- |
| Task length | METR's "time horizon" doubling every few months |
| Vocabulary | Prompt → context → harness → loop → graph engineering, in ~18 months |
| Tools | Roo Code shut down (May 2026) |
| | Cursor acquired by SpaceX (August 2026) |
| | Gemini CLI moved to enterprise-only (June 2026) |

Learn ideas that survive the next release.

<!--
METR, an independent evaluator, measures how long a task (in human working time) an AI agent can complete half the time. That "time horizon" has been doubling every few months, much faster than the roughly seven months its original 2025 paper found. Module 05 covers it.

The vocabulary went from prompt engineering to graph engineering in about eighteen months. Module 07 explains each term.

Tools show up, become essential, and disappear. Roo Code was a popular open-source agent. Modules 06 and 13 cover these.

The course teaches ideas that still work when the names change, plus how to check what's current (module 14).
-->

---

## Six ideas that last (1–3)

1. A language model predicts the next token. It has no built-in notion of truth.
2. The model only knows what's in its context. You control that.
3. Verification is your job. You can delegate the checking, not the responsibility.

<!--
If people remember nothing else from the course, it should be these six. Every module expands on one or more of them.

One. Chat, reasoning, and coding agents are all built on next-token prediction plus a lot of training. With no notion of truth, a model can be confidently wrong. That's module 01.

Two. The model's working memory is the text in front of it right now, meaning your prompt, the files it read, and the tool output it saw. Module 07.

Three. An agent stops when it thinks it's done. Give it tests, builds, and linters it can run, ask for the evidence, then look. Modules 08 and 10.
-->

---

## Six ideas that last (4–6)

4. The harness matters as much as the model. Agent = model + harness.
5. Anything the model reads can give it orders. Prompt injection isn't solved.
6. Cost scales with context, not with the size of your question.

<!--
Four. The same model scores very differently in different tools. Modules 05 and 06.

Five. A README, a web page, an issue comment, or a tool result can contain instructions, and the model can't reliably tell data from commands. That's prompt injection, and it is not solved. Module 11.

Six. Agents re-send the whole conversation every turn. That's why heavy agentic work on pay-per-token pricing gets expensive, and why subscriptions changed the economics. Module 12.

Leave the room with discussion question 2 in mind: which of these six is most likely to be wrong in two years?
-->

---

## A two-minute history

| Year | Milestone |
| --- | --- |
| 2017 | Transformer paper, "Attention Is All You Need" |
| 2020 | GPT-3 shows few-shot learning at scale |
| 2021 | GitHub Copilot brings autocomplete to IDEs |
| 2022 | ChatGPT launches (November 30) |
| 2023 | GPT-4, Claude 2, open-weight Llama models |
| 2024 | Claude 3.5 Sonnet, Cursor takes off, o1 reasoning model, MCP announced |
| 2025 | "Vibe coding" coined, Claude Code and Codex CLI, DeepSeek-R1, AGENTS.md, Agent Skills |
| 2026 | Parallel agents mainstream, Opus 4.6 to 5.5, GPT-5.3 to 6.1, Gemini 4, Kimi K3 |

<!--
Look at how much closer together these releases get. It's about eight years from a machine-translation paper to agents that open pull requests, and most of the change came in the last two.

The module's 2026 entry also lists loop and graph engineering, covered in module 07. The full dated history, with sources, is in the timeline in the reference section.
-->

---

## How the modules fit together

| Modules | About |
| --- | --- |
| 01–05 | Models: what they are, who makes them, how to judge them |
| 06–10 | Working with them: tools, context, workflows, multiple agents, review |
| 11–15 | Doing it responsibly: security, cost, ecosystem, keeping up, careers |

Core path: 01 → 06 → 07 → 08 → 09 → 10

<!--
This redraws the module's dependency diagram. 01 (what an LLM is) leads to 02 (training), 03 (the model landscape), and 06 (harnesses). 03 leads to 04 (open vs closed weights) and 05 (judging models). 06 leads to 07 (context engineering), 11 (security), 12 (costs), and 13 (open source). 08 (agentic workflows) leads to 09 (multiple agents), 11, and 15 (learning and careers). 05 leads to 14 (keeping up).

The chain from 01 through 10 is the longest path, and it's the core of working with agents.
-->

---

<!-- _class: divider -->

# Part 3

## How to use this course

<!--
Part 3 is which path to take, the ground rules, and what you need. About 8 minutes.
-->

---

## Pick a path

| You are | Start with | Time |
| --- | --- | --- |
| A student, or new to AI tools | Student path | A semester, or ~15 hours self-paced |
| A working engineer | Engineer path | ~6–8 hours, plus a two-week practice plan |
| A lead, manager, or AI champion | Leads path | ~3 hours, plus the workplace playbook |

Every module has three levels: Foundations, In practice, Going deeper.

<!--
The three reading paths are in the paths folder. Each one says what to read in full, what to skim, and what to skip on a first pass.

Foundations assumes no background. In practice is what working engineers do. Going deeper covers research and open debates.

There's also a semester course outline with labs, a glossary, and an annotated reading list of papers.
-->

---

## Ground rules we assume throughout

1. You own what you ship. "The AI wrote it" is never an excuse.
2. Read every diff you merge, or have a check you trust read it.
3. No secrets or private data in tools not approved for that data.
4. Disclose AI use where your course, employer, or project asks.
5. A human approves anything irreversible.
6. When a tool surprises you, write it down.

<!--
Every exercise in the course expects these habits. They're also a decent starting policy for a team.

One holds in a class and in a postmortem.

Two: start by reading everything. You earn the right to read less by building tests and review.

Three is in module 15. Open-source projects increasingly ask for four too (modules 13 and 15).

Five: irreversible means deploying, deleting, sending, paying, or force-pushing. Module 11.

Six: a short log of "the model did X when I expected Y" is the start of your own evaluation set, which is module 05.
-->

---

## What you need to follow along

- A computer with a terminal, git, and a code editor
- One frontier coding agent; a $20/month plan covers every lab
- Optionally, a second agent from a different lab, for cross-review
- No GPU. Nothing requires downloading model weights.

<!--
The $20/month individual plan is from Anthropic or OpenAI, as of November 2026. Student and education discounts change often, so check current offers. Module 12 covers costs.

The second agent is for the cross-review exercises in module 10.

If you want to try running models locally, module 04 explains what it takes. It's optional.
-->

---

## Reading this material with an AI

Please do, with two cautions.

- Many 2026 facts here postdate the model's training cutoff. Trust the sources.
- Ask it to quiz you instead of summarizing.

<!--
Paste a module into your assistant of choice and ask it to quiz you, explain a section differently, or argue with one of my takes.

Ask a model about events after its training cutoff and it may invent plausible details. Many of the 2026 facts in this course postdate the models you'll use, so trust the cited sources over the model's memory.

Answering questions teaches you more than reading a summary. Module 15 has the research.
-->

---

## Try it

**On your own (30 minutes)**

- Ask an AI to explain a program you wrote, improve it, and test it
- Predict what the test will do before running it
- Note one thing it got right, and one it got wrong or glossed over

**In a group (45 minutes)**

- Each person finishes the sentence "Using AI to code is like…"
- Sort the analogies by which of the six ideas they capture or miss

<!--
For the individual exercise, pick a small program you wrote before, like a class assignment or a script. Ask the assistant to explain it back, suggest one improvement, and write a test for it. The prediction step matters most, because it makes you think before the tool does.

In a live session, run a 10-minute version of the group exercise. Collect five or six analogies and sort them on the board against the six ideas. Keep the list and come back to it at the end of the course.
-->

---

## Discussion

1. Karpathy's vibe coding meant *not* reading the code. When is that the right choice?
2. Which durable idea is most likely to be wrong in two years? Why?
3. If AI writes 80% of a team's code, what should the humans do?
4. What would convince you that a fully autonomous coding pipeline is trustworthy?

<!--
Pick two if time is short. Question 1 pairs with the spectrum slide. Question 4 previews module 08.

The module has one more question for a course setting: where should the line be between "AI helped me" and "AI did it for me" in a programming course?
-->

---

## Read more

- Module: [00 Orientation](../modules/00-orientation/)
- Andrej Karpathy, ["vibe coding" post](https://twitter.com/karpathy/status/1886192184808149383) (February 2, 2025)
- Simon Willison, ["Not all AI-assisted programming is vibe coding"](https://simonwillison.net/2025/Mar/19/vibe-coding/) (March 19, 2025)
- Simon Willison, ["Vibe engineering"](https://simonwillison.net/2025/Oct/7/vibe-engineering/) (October 7, 2025; updated February 2026)

<!--
The module page has the paths, the course outline, and links to every later module. Next session is 01, What is an LLM?
-->

# Course proposal: A Brief Introduction to Not Writing Code

*AI-accelerated software engineering, with a human in charge.*

This syllabus is for instructors, curriculum committees, and students. It's a proposal for an upper-level undergraduate computer science elective, and no institution has approved or adopted it. Anything in `[square brackets]` is a placeholder for the adopting department to fill in.

*Last checked November 8, 2026.*

**TL;DR**
- A course on building real software with coding agents. A human stays accountable, so you read, test, review, secure, and explain everything you ship.
- Six units: a one-hour orientation, then one unit for each of the knowledge base's five stages. Units are sized by their content, so the course fits a semester, a short intensive, or self-paced study.
- Eight labs, three short AI-free checks, and individual oral walkthroughs. An optional team capstone ships a small real app alongside Units 3–5, and when it runs, Labs 6 and 7 are done on it.
- About 32 hours in class, plus about 90 hours outside it with the capstone or about 65 without. Most of the outside time goes to labs and the capstone.
- Every assignment is labelled AI-free, AI-as-tutor, or AI-accelerated, and every AI-assisted submission includes a short AI log.
- Students need one frontier coding-agent plan (about $20/month as of November 2026) or an institutional license. No GPU, no model downloads, no API keys.
- The readings are this knowledge base's modules, and the [instructor guide](instructor-guide.md) has unit-by-unit teaching notes.

## Course description

Catalog description (draft). Coding agents now read codebases, run commands, and write and test changes. This course teaches students to use them to build software faster without giving up engineering judgment. Students study how language models work and fail, how they're trained, the hardware they run on, and how labs try to make them safe. They learn to choose and evaluate models, use agent harnesses, tools, and context, and follow a workflow of exploring, planning, writing tests first, implementing, verifying, and committing. They verify agent output, review AI-written code, and practice multi-agent and cross-model review. The course also covers prompt injection, agent security, cost, open-source contribution, and AI's effects on learning and careers. Some work is done without AI, to build and check fundamentals. Students ship real changes built with supervised agents and defend every line of them.

Vibe coding means accepting whatever a model writes without reading the code ([module 00](../modules/00-orientation.md#ai-accelerated-coding-not-vibe-coding)). This course is AI-accelerated coding: agents do much of the typing. Students decide what to build, write the checks, read what matters, and answer for the result.

> **Author's note:** Vibe coding means you're not really ever reading the code. We're talking about AI-accelerated coding here. Vibe coding is worth knowing about and calling out, but it's not what this course is about.

The course carries `[3]` credit hours (placeholder; the [workload estimates](#workload) assume 3) and meets `[meeting pattern, for example two 75-minute sessions per week]`. Each unit lists its readings, which are due before the unit's first session.

## Prerequisites

- `[Data structures course number]` or equivalent, with a grade of `[C]` or better.
- Comfortable in one programming language. The starter repositories use `[Python and/or TypeScript]`.
- Git basics: clone, branch, commit, diff, merge, pull request.
- Comfortable at a command line.
- Helpful, not required: some web development, a software engineering course, any prior use of chat assistants.

Students show up at very different levels. Some have shipped code at an internship, and some have never used a coding agent. The [instructor guide](instructor-guide.md#handling-different-starting-levels) covers how the labs scale for both.

## Learning outcomes

By the end of the course, students can:

| # | Outcome | Assessed by |
| --- | --- | --- |
| 1 | Explain how a language model produces text (tokens, next-token prediction, sampling, context window) and use that explanation to predict at least three kinds of failure, such as invented APIs, tokenization errors, and context degradation. | Lab 1, AI-free check 1 |
| 2 | Explain how a model is made and run: the stages of training, how code's unusual checkability is a big part of why coding agents improved so quickly in 2025–2026, and the compute and memory-bandwidth arithmetic behind the cost of training and of generating text. | AI-free check 1, reading responses |
| 3 | Tell safety, security, and alignment apart, and judge a reported model behavior by the setting it was observed in, from a contrived test to a deployed product. | AI-free check 1, reading responses |
| 4 | Evaluate claims about models, benchmarks, prices, and licenses against primary sources, with dates. | AI-free check 1, reading responses |
| 5 | Configure a coding agent with least-privilege permissions and a short instruction file, measure what fills its context, and explain what the harness adds to the model. | Lab 2 |
| 6 | Complete the explore → plan → implement → verify → commit loop with tests written before the implementation, and show evidence at each step (failing output, passing output, diff summary). | Lab 3, capstone |
| 7 | Give an agent a check it can loop against, protect that check from being gamed (read-only or hidden tests, a test diff, a mutation check), and say what passing it does and doesn't prove. | Lab 3, Lab 6, the Unit 4 verifier-loop activity |
| 8 | Build an evaluation of at least eight golden tasks, run it blind on two agent configurations, and report results with error bars and without overclaiming. | Lab 6, AI-free check 1 |
| 9 | Review AI-written code with a checklist, verify each finding by reproducing or refuting it, and report recall and false positives for human and AI reviewers. | Labs 4 and 7, AI-free check 3 |
| 10 | Run an independent, multi-reviewer, cross-model code review with adversarial verification, and judge whether it was worth its cost. | Lab 7 |
| 11 | Threat-model an agent workflow with the lethal trifecta and the Rule of Two, apply at least two architectural defenses, and say which risk each one removes. | Lab 5, capstone security review |
| 12 | Contribute a small, tested, disclosed change to a shared codebase that follows that project's contribution and AI policies. | Lab 8 |
| 13 | Read, debug, and test code without AI, and explain every line of their own submitted work in a live walkthrough. | AI-free checks, walkthroughs |

## Required tools and cost

| Item | Notes |
| --- | --- |
| A laptop | macOS, Linux, or Windows with WSL. Must run a terminal, git, a code editor, and a container or VM tool. **No GPU needed.** `[Or: department lab machines.]` |
| Git and a GitHub account | Free. Used for every lab and the capstone. |
| Python 3 and/or Node.js | Whatever the starter repositories use. `[Specify versions.]` |
| A container or VM tool | Docker or equivalent, for the sandbox in [Lab 5](labs/lab-05-prompt-injection.md). `[Or: a department-provided VM image.]` |
| **One frontier coding-agent plan** | For example Anthropic's Claude Pro (includes Claude Code) or OpenAI's ChatGPT Plus (includes Codex). Both were $20/month as of November 2026 ([module 15 price snapshot](../modules/15-costs-subscriptions-and-apis.md#price-snapshot-as-of-2026-11-08)). `[Or: institutional licenses provided by the department.]` |
| Optional: a second lab's tool | A free tier or a classmate-operated tool from a different lab, for the cross-model steps in Labs 4 and 7. Never required. |

Plans bill by the month, so the cost depends on how long the course runs. A 15-week semester covers about four billing months, roughly $80 before tax at November 2026 prices. Billing dates can push that to a fifth month, so budget $80–$100 before tax and check your renewal date. A three-week intensive needs one or two months. Students can cancel when the course ends.

- Check current education offers before you pay. Vendors change student and education pricing often. Anthropic and OpenAI both sell education or institutional plans ([module 15](../modules/15-costs-subscriptions-and-apis.md#price-snapshot-as-of-2026-11-08), [module 18](../modules/18-learning-careers-and-responsibility.md#data-privacy-what-not-to-paste)), and what they include varies. This proposal doesn't assume any particular discount exists.
- No lab needs a pay-per-token API key, so don't use one. Agent sessions re-send the whole conversation every turn, and heavy use on API billing gets expensive fast ([module 15](../modules/15-costs-subscriptions-and-apis.md#why-agentic-coding-eats-tokens)).
- Free tiers are fine for a second opinion, but their limits are too tight for a main tool. As of November 2026, OpenAI's free tier gave only limited Codex access on a small model ([module 15](../modules/15-costs-subscriptions-and-apis.md#price-snapshot-as-of-2026-11-08)).
- **Nobody's grade depends on ability to pay.** `[Department: describe how students who can't buy a plan get access, for example loaner seats on a team plan or lab accounts.]` Each term, the instructor checks that every lab fits within one $20 plan's limits ([refresh checklist](instructor-guide.md#refresh-checklist-for-each-term)).
- Consumer plans may let the vendor train on your chats and coding sessions, depending on a setting you control, and education and enterprise terms differ. Check that setting before the first lab ([module 18](../modules/18-learning-careers-and-responsibility.md#data-privacy-what-not-to-paste)).

> **Author's note:** API pricing is too expensive for heavy agentic use. Subscriptions are what make it affordable to work this way every day.

> **Author's note:** For coding, Claude and Codex are the best, in my opinion. Different models are better for different use cases.

Opinions about models go stale fast. The course works with any frontier coding agent that can read a repository, run commands, and edit files. [Module 05](../modules/05-model-landscape.md#best-model-for-the-job) covers the current options.

## Course outline

The course has six units. Unit 0 is a one-hour orientation, and Units 1–5 follow the [five stages](../modules/README.md) of the modules: how the machine works, choosing a model, working with agents, trusting the output, and practice for the long run. Each unit is sized by what it has to teach. The first two are mostly reading and discussion, and the last three are where students build things.

Sessions are about 75 minutes. Read the listed sections before the unit's first session. The default depth for every module is Foundations and In practice ([student path](../paths/students.md#how-to-read-each-module)), and the lists below name the sections to focus on. AI-free checks take about 30 minutes, in class.

### Workload

Plan on about 32 hours in class: the one-hour orientation and 25 sessions of 75 minutes. Outside class, plan on about 90 hours with the capstone and about 65 without it.

| Unit | Modules | Sessions | Labs | Reading | Lab work | Capstone | Hours outside class |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0: Orientation | 00 | 1 short | None | 0.5 | 1 (setup) | None | 1.5 |
| 1: How the machine works | 01–04 | 4 | 1 | 5 | 3 | None | 8 |
| 2: Choosing a model | 05–07 | 3 | None | 4 | None | None | 4 |
| 3: Working with agents | 08–10 | 6 | 2, 3, 6 | 4.5 | 13.5 | 8 | 26 |
| 4: Trusting the output | 11–14 | 7 | 4, 5, 7 | 5 | 10.5 | 10 | 25.5 |
| 5: Practice for the long run | 15–18 | 5 | 8 | 4 | 10 | 12 | 26 |
| Total | | 25 and the orientation | 8 | 23 | 38 | 30 | About 91 |

Without the capstone, drop its 30 hours and add about 3 for the final reflective report, which is then written about your lab work. Each term, the instructor should check these estimates against the time students actually spend. If you're regularly well past them, tell the instructor.

Each lab sits in the first unit where its prerequisites are met. Lab 6 builds the eval that module 07 describes, but it needs the agent skills from Labs 2 and 3, so it comes in Unit 3. Lab 8 belongs to Unit 5, and its first phase starts during Unit 4 because maintainers need time to reply. Each lab's header says which unit it goes with and when it's due.

### Unit 0: Orientation

Students know what the course is for, how the AI-use policy works, and what they need installed.

The one session runs about an hour: the course's stance and the AI-use policy with its tiers, then the AI-free diagnostic (30 minutes, ungraded). Setup happens outside class from the setup checklist: install one agent, sign in with the subscription instead of an API key, and check the data-training setting. A TA runs a drop-in clinic for anyone who gets stuck. The setup checklist also asks for your one-sentence "Using AI to code is like…" analogy ([00 Try it](../modules/00-orientation.md#try-it)), which comes back in the last session.

Read these first:

- [00: Orientation](../modules/00-orientation.md), all of it
- [18](../modules/18-learning-careers-and-responsibility.md): [producing vs learning](../modules/18-learning-careers-and-responsibility.md#producing-the-work-vs-learning-from-it), [how to learn with AI](../modules/18-learning-careers-and-responsibility.md#how-to-learn-with-ai-instead-of-outsourcing-learning), and [academic integrity](../modules/18-learning-careers-and-responsibility.md#academic-integrity). The policy rests on them, and the learning habits matter from the first lab.

About 1.5 hours outside class: half an hour of reading and an hour of setup.

### Unit 1: How the machine works

Students can explain how a model is built, trained, run, and made safe, well enough to predict where it will fail.

Read these first:

- [01](../modules/01-what-is-an-llm.md): [next token](../modules/01-what-is-an-llm.md#the-one-idea-predict-the-next-token), [what it is not](../modules/01-what-is-an-llm.md#what-an-llm-is-not), [tokens](../modules/01-what-is-an-llm.md#tokens-and-tokenization), [the transformer](../modules/01-what-is-an-llm.md#the-transformer-and-attention), [sampling](../modules/01-what-is-an-llm.md#sampling-temperature-and-determinism), [hallucination](../modules/01-what-is-an-llm.md#hallucination-and-why-it-happens), [sycophancy](../modules/01-what-is-an-llm.md#sycophancy), [mental model](../modules/01-what-is-an-llm.md#a-working-mental-model)
- [02](../modules/02-how-a-model-is-made.md): all of Foundations, including [the hardware](../modules/02-how-a-model-is-made.md#the-hardware-what-it-takes-to-train-and-run-a-model), and [quantization basics](../modules/02-how-a-model-is-made.md#quantization-basics)
- [03](../modules/03-post-training-and-rl.md): [RL in five minutes](../modules/03-post-training-and-rl.md#rl-in-five-minutes), [RLHF](../modules/03-post-training-and-rl.md#rlhf-end-to-end-the-coaching), [RLVR](../modules/03-post-training-and-rl.md#rlvr-and-reasoning-models-the-practice-exams), [RL for coding agents](../modules/03-post-training-and-rl.md#rl-for-coding-agents), [reward hacking](../modules/03-post-training-and-rl.md#reward-hacking), [should you fine-tune?](../modules/03-post-training-and-rl.md#should-you-fine-tune-at-all), and a skim of [demonstrated, deployed, or speculation?](../modules/03-post-training-and-rl.md#demonstrated-deployed-or-speculation)
- [04](../modules/04-model-safety-and-alignment.md): Foundations, then [always ask where](../modules/04-model-safety-and-alignment.md#observed-concerning-behaviors-always-ask-where), [the 2026 incidents](../modules/04-model-safety-and-alignment.md#two-2026-incidents-outside-contrived-setups), and [why your coding agent cheats](../modules/04-model-safety-and-alignment.md#why-your-coding-agent-sometimes-cheats)

The unit takes four sessions:

1. What an LLM is. The human language model game ([01 Try it](../modules/01-what-is-an-llm.md#try-it)) and a live demo of a hallucinated API.
2. How a model is made. Work a training run from 6·N·D to GPU-hours and days, then see why generating text waits on memory ([02 Try it](../modules/02-how-a-model-is-made.md#try-it)).
3. Post-training and RL. Design a reward for a small coding task and then break it, and decide between fine-tuning, retrieval, and prompting ([03 Try it](../modules/03-post-training-and-rl.md#try-it)).
4. Model safety and alignment. Sort reported behaviors by the setting they were observed in, then the open-weights safety debate ([04 Try it](../modules/04-model-safety-and-alignment.md#try-it)).

[Lab 1](labs/lab-01-tokens-and-temperature.md) runs alongside the unit and is due at the start of Unit 2.

About 8 hours outside class: 5 of reading and 3 for Lab 1.

### Unit 2: Choosing a model

Students can read model names, launch claims, benchmarks, and licenses, and know what it would take to test a model on their own work.

Read these first:

- [05](../modules/05-model-landscape.md): [names and tiers](../modules/05-model-landscape.md#how-to-read-model-names-and-tiers), [places in the chain](../modules/05-model-landscape.md#different-places-in-the-chain), [best model for the job](../modules/05-model-landscape.md#best-model-for-the-job), [picking next month](../modules/05-model-landscape.md#how-to-pick-a-model-next-month-when-all-of-this-is-stale)
- [06](../modules/06-open-vs-closed-weights.md): [weights](../modules/06-open-vs-closed-weights.md#what-weights-actually-are), [openness spectrum](../modules/06-open-vs-closed-weights.md#the-openness-spectrum), [licenses](../modules/06-open-vs-closed-weights.md#licenses-in-practice), [hardware math](../modules/06-open-vs-closed-weights.md#running-open-models-the-hardware-math)
- [07](../modules/07-judging-models.md): [what a benchmark is](../modules/07-judging-models.md#what-a-benchmark-actually-is), [claim checklist](../modules/07-judging-models.md#reading-a-benchmark-claim-a-checklist), [harness matters](../modules/07-judging-models.md#harness-matters), [benchmark-maxing](../modules/07-judging-models.md#benchmark-maxing), [productivity evidence](../modules/07-judging-models.md#real-world-productivity-evidence), [vibes](../modules/07-judging-models.md#vibes-are-data-too), [build your own eval](../modules/07-judging-models.md#build-your-own-eval), [small-eval statistics](../modules/07-judging-models.md#the-statistics-of-small-evals), [reward hacking](../modules/07-judging-models.md#cheating-reward-hacking-and-grader-trust)

The unit takes three sessions:

1. The model landscape. Read a real launch post against the claim checklist.
2. Open vs closed weights. Memory math for running a model yourself, and a license review ([06 Try it](../modules/06-open-vs-closed-weights.md#try-it)).
3. Building your own eval. A golden-task workshop and error bars by hand, then AI-free check 1.

This unit has no lab.

About 4 hours outside class, all reading.

### Unit 3: Working with agents

Students can set up a coding agent safely, give it the right context, and run the full explore → plan → implement → verify → commit loop on a real change.

Read these first:

- [08](../modules/08-harnesses-and-tools.md): [what a harness is](../modules/08-harnesses-and-tools.md#what-a-harness-is), [history](../modules/08-harnesses-and-tools.md#a-short-history-from-autocomplete-to-orchestrators), [tools](../modules/08-harnesses-and-tools.md#tools-how-a-model-does-things), [MCP](../modules/08-harnesses-and-tools.md#mcp-the-model-context-protocol), [baseline setup](../modules/08-harnesses-and-tools.md#a-sane-baseline-setup); and from later modules, [16: a loop in 30 lines](../modules/16-open-source-ecosystem.md#framework-or-just-a-loop) and [14: the student checklist](../modules/14-security-and-prompt-injection.md#student-checklist), which you need before you run an agent
- [09](../modules/09-context-engineering.md): [the ladder](../modules/09-context-engineering.md#the-buzzword-ladder-at-a-glance), [prompting basics](../modules/09-context-engineering.md#prompting-basics-that-still-matter), [what fills the window](../modules/09-context-engineering.md#what-actually-fills-an-agents-context-window), [context limits](../modules/09-context-engineering.md#context-limits-in-practice), [instruction files](../modules/09-context-engineering.md#the-rise-and-fall-of-giant-claudemd-and-agentsmd-files)
- [10](../modules/10-agentic-workflows.md): [the loop](../modules/10-agentic-workflows.md#the-agent-loop), [autonomy](../modules/10-agentic-workflows.md#the-autonomy-spectrum), [Yegge's stages](../modules/10-agentic-workflows.md#steve-yegges-eight-stages), [core loop](../modules/10-agentic-workflows.md#the-core-loop-explore--plan--implement--verify--commit), [failure modes](../modules/10-agentic-workflows.md#failure-modes-and-counter-moves); and two sections of module 11 that Lab 3 depends on, [it stops when it thinks it's done](../modules/11-verification.md#the-key-fact-the-loop-stops-when-the-model-thinks-it-is-done) and [tests as contract](../modules/11-verification.md#tests-as-the-agents-contract)

The unit takes six sessions:

1. Harnesses, tools, and MCP. The agent loop and the context breakdown, live, and a 30-line loop traced line by line.
2. Lab 2 working session.
3. Context engineering. Trim a bloated `AGENTS.md` and rewrite vague prompts.
4. Agentic workflows. A full explore-to-commit session, live, and how much autonomy works.
5. Lab 3 working session.
6. Lab 6 kickoff: choosing golden tasks and setting up hidden tests. Then AI-free check 2.

[Lab 2](labs/lab-02-first-agent-session.md) and [Lab 3](labs/lab-03-plan-test-build.md) run in order. [Lab 6](labs/lab-06-your-own-eval.md) opens at the end of the unit. With the capstone, it draws its tasks from the project, so it opens once the vertical slice is deployed and its runs finish early in Unit 4. Without the capstone, the instructor forms teams for it and supplies tasks from the eval starter.

About 26 hours outside class: 4.5 of reading, 13.5 for the three labs, and 8 for the capstone's pitch, design doc, and vertical slice.

### Unit 4: Trusting the output

Students can give an agent checks it can run, keep those checks honest, review agent work with people and other models, and contain an agent that reads untrusted text.

Read these first:

- [11](../modules/11-verification.md): Foundations, then [problems an agent can loop on](../modules/11-verification.md#problems-an-agent-can-loop-on), [loops in practice](../modules/11-verification.md#loops-in-practice), [Stop hooks and CI gates](../modules/11-verification.md#stop-hooks-and-ci-gates), [protecting the verifier](../modules/11-verification.md#protecting-the-verifier), [proof of done](../modules/11-verification.md#proof-of-done), [calibrating your own trust](../modules/11-verification.md#calibrating-your-own-trust)
- [12](../modules/12-multi-agent-systems.md): Foundations, [patterns](../modules/12-multi-agent-systems.md#patterns-and-when-each-helps), [review swarm](../modules/12-multi-agent-systems.md#recipe-1-a-review-swarm), [cross-model review](../modules/12-multi-agent-systems.md#recipe-2-cross-model-review), [parallel builders](../modules/12-multi-agent-systems.md#recipe-3-parallel-builders-when-you-must), [budgets](../modules/12-multi-agent-systems.md#budgets-and-stop-conditions), [anti-patterns](../modules/12-multi-agent-systems.md#anti-patterns)
- [13](../modules/13-ai-code-review.md): [good and bad at](../modules/13-ai-code-review.md#what-they-are-good-and-bad-at), [layered workflow](../modules/13-ai-code-review.md#a-layered-review-workflow), [verify findings](../modules/13-ai-code-review.md#verify-findings-before-acting), [severity](../modules/13-ai-code-review.md#severity-triage), [reviewing AI PRs](../modules/13-ai-code-review.md#how-humans-should-review-ai-written-prs), [accountability](../modules/13-ai-code-review.md#accountability-the-human-who-merges-owns-it)
- [14](../modules/14-security-and-prompt-injection.md): Foundations, [incidents](../modules/14-security-and-prompt-injection.md#real-incidents-20252026), [coding-agent risks](../modules/14-security-and-prompt-injection.md#risks-specific-to-coding-agents), [defenses](../modules/14-security-and-prompt-injection.md#practical-defenses), [student checklist](../modules/14-security-and-prompt-injection.md#student-checklist)
- Before the Lab 8 kickoff, [16: etiquette](../modules/16-open-source-ecosystem.md#etiquette-for-contributing-with-ai)

The unit takes seven sessions:

1. Verification. The ladder of checks, and a live `Stop` hook that blocks "done" until the tests pass, run against a task whose test contradicts the spec.
2. Build a loop with a verifier, from [module 11's class exercise](../modules/11-verification.md#try-it). Groups take a toy project with about ten broken tests, and each builds a different loop: a shell loop with a plan file, a goal with a test condition, or a `Stop` hook. Every loop gets the same budget. Then the class compares which finished, what each cost, and whether any passed by weakening a test. It counts toward participation, and [Lab 3's optional extension](labs/lab-03-plan-test-build.md#if-you-finish-early) runs the same idea on a feature with hidden tests.
3. Multiple agents. Debate vs vote ([12 Try it](../modules/12-multi-agent-systems.md#try-it)).
4. AI code review. A live demo of tautological tests, and a seeded PR reviewed together. Lab 4 pairs swap branches.
5. Security and prompt injection. A live demo of injection through a README, in a sandbox, and a workflow threat-modeled together ([14 Try it](../modules/14-security-and-prompt-injection.md#try-it)). Lab 5 sandbox plans are approved here.
6. Lab 5 working session. Lab 7 pull requests are assigned.
7. AI-free check 3, then the Lab 8 kickoff.

[Lab 4](labs/lab-04-review-ai-code.md) comes first, then [Lab 5](labs/lab-05-prompt-injection.md) and [Lab 7](labs/lab-07-multi-agent-review.md), which both build on it. With the capstone, Lab 7 reviews a teammate's pull request and the security review is due late in the unit. Without it, Lab 7 reviews a classmate's Lab 3 feature.

About 25.5 hours outside class: 5 of reading, 10.5 for the three labs, and 10 for the capstone.

### Unit 5: Practice for the long run

Students can budget for agent work, contribute to someone else's project with care, keep up without chasing every release, and decide how they'll keep learning.

Read these first:

- [15](../modules/15-costs-subscriptions-and-apis.md): [three ways to pay](../modules/15-costs-subscriptions-and-apis.md#three-ways-to-pay), [why agents eat tokens](../modules/15-costs-subscriptions-and-apis.md#why-agentic-coding-eats-tokens), [worked example](../modules/15-costs-subscriptions-and-apis.md#worked-example-one-hour-of-agentic-coding), [cost per task](../modules/15-costs-subscriptions-and-apis.md#cost-per-task-not-cost-per-token)
- [16](../modules/16-open-source-ecosystem.md): [map of the stack](../modules/16-open-source-ecosystem.md#a-map-of-the-stack), [AI slop](../modules/16-open-source-ecosystem.md#the-other-side-ai-slop-and-maintainer-burden), [students contributing](../modules/16-open-source-ecosystem.md#how-students-can-contribute-to-open-source-with-ai-responsibly)
- [17](../modules/17-keeping-up.md): [what stays stable](../modules/17-keeping-up.md#what-stays-stable), [ups and downs](../modules/17-keeping-up.md#ups-and-downs-are-normal), [model, task, or harness?](../modules/17-keeping-up.md#is-it-the-model-the-task-or-the-harness), [launch claims](../modules/17-keeping-up.md#weighing-launch-claims), [a routine](../modules/17-keeping-up.md#a-sustainable-routine), [evaluating a release](../modules/17-keeping-up.md#evaluating-a-brand-new-release-in-an-afternoon)
- [18](../modules/18-learning-careers-and-responsibility.md): [the evidence](../modules/18-learning-careers-and-responsibility.md#what-the-evidence-says), [careers](../modules/18-learning-careers-and-responsibility.md#careers), [deskilling](../modules/18-learning-careers-and-responsibility.md#deskilling-real-risk-or-old-panic), [the human side](../modules/18-learning-careers-and-responsibility.md#the-human-side)
- Before the last session, a re-read of [00: six ideas](../modules/00-orientation.md#six-ideas-that-outlast-the-hype)

The unit takes five sessions:

1. Costs and the open-source ecosystem. The maintainer's chair ([16 Try it](../modules/16-open-source-ecosystem.md#try-it)) and a quick team budget ([15 Try it](../modules/15-costs-subscriptions-and-apis.md#try-it)).
2. Keeping up. Incident presentations ([17 Try it](../modules/17-keeping-up.md#try-it)).
3. Learning, careers, and responsibility. The write-the-policy exercise ([18 Try it](../modules/18-learning-careers-and-responsibility.md#try-it)) and AI-free debugging practice.
4. Working session: the capstone's final sprint, or Lab 8 without the capstone.
5. Ship and reflect. Final demos (or Lab 8 show-and-tell without the capstone), the analogies from Unit 0, and a course retrospective.

[Lab 8](labs/lab-08-open-source-contribution.md) finishes in this unit. Individual 10-minute walkthroughs follow the last session.

About 26 hours outside class: 4 of reading, 10 for Lab 8, and 12 for the capstone's final sprint, demo, reflective report, and walkthrough prep.

## Running it on your calendar

The units don't assume any particular calendar. These sketches are starting points; the pilot of Units 3 and 4 should set the real pace.

- **15-week semester**, two 75-minute sessions a week: Units 0–2 take about four weeks and Units 3–5 about three and a half weeks each, leaving spare sessions for capstone work and walkthroughs in finals week. Outside work stays near 7 hours in the busiest weeks.
- **Three-week intensive**, about two sessions a day: skip the capstone and use Lab 8's class repository, since an outside maintainer's go-ahead can take longer than the course.
- **Self-paced:** take the units in order, skip the sessions, and do the readings and labs, about 60 hours in all. The [course README](README.md#where-to-start) covers labs that expect a partner or an instructor.

## Capstone project (optional)

The capstone is a team project that runs alongside Units 3–5. The instructor decides whether a given offering runs it: a semester has room for it, and a short intensive usually doesn't. When it runs, everyone is on a team, and two labs are done on the project instead of next to it. [Lab 6](labs/lab-06-your-own-eval.md) is the project's eval set and [Lab 7](labs/lab-07-multi-agent-review.md) is its cross-model review, so that work happens once and is graded once.

### What you build

Teams of three or four use supervised coding agents to build and ship a small, real application for a real user. "Real" means someone outside the team relies on it, such as a campus club, a nonprofit, a lab group, a local business, or other students using your tool. "Small" means one clear job done well. Assessment focuses on how you specify, constrain, verify, review, and secure the agents' work, and what you learn doing it.

### Constraints

- Name one person outside the team as your user and meet them at least twice. At least three people outside the team use the app before the final demos.
- The app costs nothing beyond your agent plans. Deploy on a free hosting tier, or ship an installable package, CLI, or browser extension.
- The app makes no paid model API calls, and it doesn't need to use AI at all. `[Unless the department provides API keys.]`
- Use synthetic data. Real personal data stays out of development and prompts. An app that will store other people's personal data needs instructor approval and must follow `[institution's data policy]` ([module 18](../modules/18-learning-careers-and-responsibility.md#data-privacy-what-not-to-paste)).
- Protect `main` with branch protection and one approving review from a teammate who didn't write the change. Turn on secret scanning and run tests in CI. `[Department: provide a private hosting plan that supports these controls, or an equivalent private service; do not require students to publish their coursework or buy hosting features.]` Every pull request uses the [PR template from module 13](../modules/13-ai-code-review.md#make-the-author-explain-the-change), including "What the agent did vs what I did."
- Agents are always supervised. Any autonomy level is allowed if your checks can catch what you've stopped watching ([module 10](../modules/10-agentic-workflows.md#the-autonomy-spectrum)). Unattended runs need a turn cap, a sandbox, and a pull request a human approves. Skip-permissions modes are allowed only in a disposable sandbox ([module 14](../modules/14-security-and-prompt-injection.md#risks-specific-to-coding-agents)).
- Keep your commit history, PR descriptions, AI logs, and exported transcripts of key decisions.

### Deliverables

| When | Deliverable | What it contains |
| --- | --- | --- |
| Start of Unit 3 | **Pitch** | One page: the user, the problem, the smallest useful version, the biggest risk |
| Middle of Unit 3 | **Design doc** | Problem and user; requirements and non-goals; architecture and data model; the interfaces you'll write *before* agents build in parallel ([module 12](../modules/12-multi-agent-systems.md#recipe-3-parallel-builders-when-you-must)); test strategy (what is your [oracle](../modules/11-verification.md#verifiers-and-oracles)?); which tasks go to agents and at what autonomy; quota plan; risks |
| End of Unit 3 | **Vertical slice** | One end-to-end feature deployed, with tests and CI |
| Early in Unit 4 | **Eval set** | This is [Lab 6](labs/lab-06-your-own-eval.md), done on your project: at least eight golden tasks from your project's history (three or more per member), with hidden tests, run blind on two agent configurations and summarized with error bars, plus the configuration your team chose for the final sprint and why. Nothing extra to submit. |
| Late in Unit 4 | **Security review** | Rule of Two analysis for your agent workflow and for the app ([module 14](../modules/14-security-and-prompt-injection.md#two-frameworks-that-make-this-tractable)); the [team checklist](../modules/14-security-and-prompt-injection.md#team-checklist) items that apply; every dependency verified as real and intended; scanner results; an independent fresh-session security review (a different lab’s model where available), with each finding verified; fixes |
| End of Unit 4 | **Cross-model code review** | This is [Lab 7](labs/lab-07-multi-agent-review.md), done on your project: each member runs a review swarm with adversarial verification on a different teammate's pull request from after the vertical slice, using a different lab's model where possible. Confirmed High and Medium findings are fixed through reviewed PRs. Nothing extra to submit. |
| End of Unit 5 | **Shipped app, repository, and demo** | Working app with real users; README covering trade-offs, rejected alternatives, and a short section on what your eval (Lab 6) and reviews (Lab 7) found and what you changed; tests and CI green; a 10-minute demo that includes one thing an agent got wrong |
| End of Unit 5 | **Reflective report** (individual) | "What I learned vs what the AI did" ([below](#reflective-report)) |
| After Unit 5 | **Walkthrough** (individual) | 10 minutes: explain code you merged, answer "what if" questions, show the test that guards it |

Each team deliverable gets one score, adjusted per member using individual evidence: commits, reviews given, AI logs, and `[peer evaluation process]`.

## Reflective report

Write 1,000 to 1,500 words without AI, and back each answer with evidence from your commits, PRs, and logs. Without the capstone, answer the same questions about your lab work.

1. What I built: your part of the system, in two paragraphs.
2. What the agents did: roughly how much of your merged code an agent drafted, and how you know.
3. What I did that the agents didn't or couldn't: decisions, specs, tests, reviews, debugging.
4. Three times I overrode an agent, and why.
5. One bug an agent introduced, and how it was caught (or missed).
6. What I can now do without AI. Rebuild one small component without AI before you write this section ([module 18](../modules/18-learning-careers-and-responsibility.md#how-to-learn-with-ai-instead-of-outsourcing-learning), habit 7). What came easily? What didn't?
7. Where I sit on Yegge's stages ([module 10](../modules/10-agentic-workflows.md#steve-yegges-eight-stages)), and whether that was the right place for this work.
8. What I'd do differently next time.

## Assessment

| Component | Weight |
| --- | --- |
| Labs 1–8 | 45%. Labs 1–5 and 8: 5% each. Labs 6 and 7: 7.5% each, because they're the capstone's eval set and cross-model review. |
| Capstone | 30%. Design doc 5%, security review 5%, shipped app 10%, reflective report 6%, walkthrough 4%. The pitch and vertical slice get feedback only, and the eval set and cross-model review are graded once, as Labs 6 and 7. |
| AI-free checks | 15%. Three in-class checks, 5% each, at the ends of Units 2, 3, and 4. |
| Participation | 10%. Reading responses, in-class exercises including the verifier-loop activity, peer review, and Lab 8 maintainer shifts if you use the class repository. |

An offering that drops the capstone moves its 30% to the labs and the reflective report: labs become 60% (7.5% each), and the report and walkthrough 15% (report 10%, walkthrough 5%), both on lab work.

Each lab has its own rubric. The AI-free checks cover reading code, predicting what code and tests do, finding bugs by hand, and explaining core concepts.

`[Grading scale.]` `[Late-work policy.]` `[Attendance policy.]`

The instructor or a TA may follow up any submission with a five-minute walkthrough. Expect at least one during the course besides the final 10-minute walkthrough after Unit 5, which everyone does, on capstone code or, without the capstone, on lab work. If a walkthrough shows you can't explain your submission, it doesn't count as yours yet, and you get one chance to redo the walkthrough or the work. The instructor guide describes [how walkthroughs are run](instructor-guide.md#oral-check-ins-and-walkthroughs).

## AI-use policy

This course requires both AI-assisted and AI-free work. The research summarized in [module 18](../modules/18-learning-careers-and-responsibility.md#what-the-evidence-says) finds that outsourcing the thinking weakens the skill you outsourced, while using AI to ask why, get hints, and check understanding mostly doesn't. Supervising agents also depends on skills you build by hand, like reading and debugging code. So the course mixes AI-free practice, AI-as-tutor learning, and full acceleration.

### The three tiers

The labels come from [module 18's suggested policy](../modules/18-learning-careers-and-responsibility.md#a-suggested-policy-for-an-ai-accelerated-course).

| Tier | What's allowed | What's graded |
| --- | --- | --- |
| **AI-free** | No AI tools of any kind, including IDE autocomplete and AI features in search or editors. | The fundamentals you need without help. |
| **AI-as-tutor** | AI may explain, give hints, ask you questions, and critique your work. It may not write code or prose you submit. | Your own work, and your use of AI to learn. |
| **AI-accelerated** | Use any AI tools. | The result, your design decisions, your verification evidence, and your ability to explain every line. |

- A model you're studying isn't "AI help." In Labs 1 and 5 the model is the subject of the experiment. The tier governs who writes what you submit.
- You write your own reflections, AI logs, PR descriptions, and replies to reviewers in every tier. In AI-accelerated work, AI may critique them but not write them.

### Tier for each assignment

| Assignment | Tier |
| --- | --- |
| Unit 0 diagnostic; AI-free checks 1–3 | AI-free |
| Reading responses | AI-as-tutor. You're encouraged to have AI quiz you on the reading ([module 00](../modules/00-orientation.md#reading-this-material-with-an-ai)). |
| [Lab 1: Tokens and temperature](labs/lab-01-tokens-and-temperature.md) | AI-as-tutor |
| [Lab 2: First agent session](labs/lab-02-first-agent-session.md) | AI-accelerated |
| [Lab 3: Plan, test, build](labs/lab-03-plan-test-build.md) | Part A (spec and acceptance tests): AI-as-tutor. Part B (implementation): AI-accelerated. |
| [Lab 4: Review AI code](labs/lab-04-review-ai-code.md) | Part A (hand review): AI-free. The rest: AI-accelerated. |
| [Lab 5: Prompt injection](labs/lab-05-prompt-injection.md) | AI-accelerated, under the lab's mandatory safety rules |
| [Lab 6: Your own eval](labs/lab-06-your-own-eval.md) | AI-accelerated for tooling. Task selection, hidden tests, and blind scoring are yours. |
| [Lab 7: Multi-agent review](labs/lab-07-multi-agent-review.md) | AI-accelerated |
| [Lab 8: Open-source contribution](labs/lab-08-open-source-contribution.md) | AI-as-tutor, or stricter if the project's own policy is stricter |
| Capstone pitch and design doc | AI-as-tutor. Agents may interview you and critique drafts; the decisions and the text are yours. |
| Capstone vertical slice, shipped app, and security review (the eval set and cross-model review are Labs 6 and 7) | AI-accelerated |
| Reflective report and walkthrough | AI-free |

### Rules that apply in every tier

1. Every AI-as-tutor or AI-accelerated submission discloses AI use in an AI log (template below).
2. You're responsible for everything you submit, including bugs, security flaws, and license problems an AI introduced ([module 18](../modules/18-learning-careers-and-responsibility.md#human-accountability)).
3. If you can't explain it in a walkthrough, it doesn't count as yours.
4. Don't paste anyone's personal data or credentials into AI tools. Share a partner’s or teammate’s code only for assigned collaboration, with their consent and using the course-approved tools and data settings ([module 18](../modules/18-learning-careers-and-responsibility.md#data-privacy-what-not-to-paste)).
5. The stricter rule wins. An open-source project's AI policy, a client's confidentiality request, or another course's policy overrides this one when it's stricter.
6. Keep your commit history and export the transcript of any agent session that made a key decision. Most harnesses save sessions locally.
7. When you're unsure whether a use is allowed, ask the instructor in writing before you submit.

### AI log template

Put this at the end of each AI-as-tutor or AI-accelerated submission.

```markdown
## AI log: <assignment name>

- Tier: <AI-as-tutor | AI-accelerated>
- Tools: <harness and version, model, plan>
- What I used AI for: <two to five bullets>
- What I did myself: <two to five bullets>
- One thing the AI got wrong that I caught, and how I caught it (or “none observed”):
- One thing I learned:
- Transcripts attached: <file names, for key decisions>
```

For commits, pull requests, and READMEs, a one-paragraph disclosure is enough. Use [module 18's template](../modules/18-learning-careers-and-responsibility.md#disclosure-template-for-students):

```text
AI assistance: I used [tool] to [explain X / suggest a fix for Y /
generate the initial version of Z]. I reviewed and modified the output,
[wrote the tests myself / rewrote the parser]. The AI incorrectly
[suggested a package that doesn't exist / missed an edge case], which
I caught by [running the tests / reading the docs].
```

If your tool adds a co-author trailer to commits, leave it on unless a project's rules say otherwise ([module 18](../modules/18-learning-careers-and-responsibility.md#attribution-and-disclosure-in-commits-and-prs)).

## Accessibility

`[Insert the institution's accessibility statement and the disability services office's contact information.]`

For this course:

- A written or recorded walkthrough can replace an oral one as an accommodation.
- AI tools can be assistive technology, for example voice-driven coding or plain-language explanations ([module 18](../modules/18-learning-careers-and-responsibility.md#bias-and-accessibility)). If you need one during an AI-free assessment, arrange it through `[disability services]` in advance. It won't count against you.
- Capstone interfaces must pass applicable accessibility checks and a keyboard-only test before the final demo. Use an automated checker for web interfaces, and document equivalent checks for CLI or installable tools. Generated interfaces often miss labels, contrast, and keyboard access.

## Academic integrity

`[Insert the institution's academic integrity policy and reporting process.]`

In this course, these are integrity violations:

- Submitting AI-written code or prose in AI-free or AI-as-tutor work.
- Leaving out AI use that the AI log should have disclosed.
- Fabricating evidence or altering logs, transcripts, test output, or commit history to misrepresent what happened. Clearly labelled privacy redactions and the history-squashing step required by Lab 4 are allowed; retain original evidence privately.
- Submitting another person's work as your own, whether or not an AI was involved.
- Breaking the safety rules in [Lab 5](labs/lab-05-prompt-injection.md), or testing injection against systems you don't own.
- Violating an open-source project's AI policy in Lab 8.

The course doesn't use AI-detection tools as evidence, because AI use is hard to detect reliably ([module 18](../modules/18-learning-careers-and-responsibility.md#what-instructors-can-reasonably-allow)). It relies on process evidence (commits, logs, transcripts) and walkthroughs instead. A walkthrough you can't complete isn't by itself a finding of misconduct. It means the work doesn't count yet.

## Keeping this course current

This field changes monthly, and parts of this syllabus will be wrong within a term ([module 17](../modules/17-keeping-up.md#how-fast-it-moves)). Verification, context control, security, review, and honest evaluation should outlast the current names, prices, commands, and policies. Before each offering, work through the instructor guide's [refresh checklist](instructor-guide.md#refresh-checklist-for-each-term): prices and education offers, data terms, every command and setting the labs name, quota per lab on one $20 plan, the live demos, module "Last checked" dates, and institutional policies.

## Sources

Everything in this syllabus draws on the modules of this knowledge base, which cite their primary sources. The most directly used:

- [Module 00](../modules/00-orientation.md): the course's stance and ground rules.
- [Module 10](../modules/10-agentic-workflows.md): the explore → plan → implement → verify → commit workflow.
- [Module 11](../modules/11-verification.md): checks, oracles, protecting the verifier, and the verifier-loop activity.
- [Module 13](../modules/13-ai-code-review.md): review checklist, PR template, accountability.
- [Module 14](../modules/14-security-and-prompt-injection.md): threat models and defenses.
- [Module 15](../modules/15-costs-subscriptions-and-apis.md): plans and prices.
- [Module 18](../modules/18-learning-careers-and-responsibility.md): learning evidence, the three-tier policy, disclosure, data privacy.

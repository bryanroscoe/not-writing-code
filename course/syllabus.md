# Course proposal: AI-Accelerated Software Engineering

> **Audience:** instructors, curriculum committees, and students · **Last verified:** 2026-11-08
> **Status:** A proposal for an upper-level undergraduate computer science elective. No institution has approved or adopted it. Anything in `[square brackets]` is a placeholder for the adopting department to fill in.

**TL;DR**
- A 15-week elective on building real software with coding agents while a human stays accountable: you read, test, review, secure, and explain everything you ship.
- Eight labs, a team term project that ships a small real app, three short AI-free checks, and individual oral walkthroughs. Labs 6 and 7 are done on the project, so the eval and review work happens once.
- About 9–10 hours a week in total, in and out of class, for a `[3]`-credit course.
- Every assignment is labelled **AI-free**, **AI-as-tutor**, or **AI-accelerated**, and every AI-assisted submission includes a short AI log.
- Students need one frontier coding-agent plan (about $20/month as of November 2026) or an institutional license. No GPU, no model downloads, no API keys.
- The readings are the modules of this knowledge base. The [instructor guide](instructor-guide.md) has week-by-week teaching notes.

## Course description

**Catalog description (draft).** Coding agents now read codebases, run commands, and write and test changes. This course teaches students to use them to build software faster without giving up engineering judgment. Topics include how language models work and fail; agent harnesses, tools, and context; a disciplined agent workflow (explore, plan, test first, implement, verify, commit); reviewing AI-written code; prompt injection and agent security; evaluating models on your own tasks; multi-agent and cross-model review; cost; open-source contribution; and the effects of AI on learning and careers. Some work is done without AI to build and check fundamentals. Teams ship a small real application built with supervised agents and defend every line of it.

**What "vibe coding" means here.** The phrase originally meant accepting whatever a model writes without reading the code ([module 00](../modules/00-orientation.md#what-we-mean-by-vibe-coding)). This course teaches the opposite habit. Agents do much of the typing. Students decide what to build, write the checks, read what matters, and answer for the result.

> **Bryan's take:** When I say vibe coding, I mean AI-accelerated coding, not really vibe coding: AI-accelerated engineering with a human in charge, not blind acceptance of whatever the model produces.

**Format.** `[3]` credit hours (placeholder; the [workload estimates](#workload) assume 3), `[meeting pattern, for example two 75-minute sessions per week: one discussion and demo, one hands-on lab]`. Readings are due before the first session of each week.

## Prerequisites

- `[Data structures course number]` or equivalent, with a grade of `[C]` or better.
- Comfortable in one programming language. The starter repositories use `[Python and/or TypeScript]`.
- Git basics: clone, branch, commit, diff, merge, pull request.
- Comfortable at a command line.
- Helpful, not required: some web development, a software engineering course, any prior use of chat assistants.

Students arrive at very different levels. Some have shipped code at an internship; some have never used a coding agent. The [instructor guide](instructor-guide.md#handling-different-starting-levels) describes how labs scale for both.

## Learning outcomes

By the end of the course, students can:

| # | Outcome | Assessed by |
| --- | --- | --- |
| 1 | Explain how a language model produces text (tokens, next-token prediction, sampling, context window) and use that explanation to predict at least three kinds of failure, such as invented APIs, tokenization errors, and context degradation. | Lab 1, AI-free check 1 |
| 2 | Configure a coding agent with least-privilege permissions and a short instruction file, measure what fills its context, and explain what the harness adds to the model. | Lab 2 |
| 3 | Complete the explore → plan → implement → verify → commit loop with tests written before the implementation, and show evidence at each step (failing output, passing output, diff summary). | Lab 3, term project |
| 4 | Review AI-written code with a checklist, verify each finding by reproducing or refuting it, and report recall and false positives for human and AI reviewers. | Labs 4 and 7, AI-free check 2 |
| 5 | Threat-model an agent workflow with the lethal trifecta and the Rule of Two, apply at least two architectural defenses, and say which risk each one removes. | Lab 5, project security review |
| 6 | Build an evaluation of at least eight golden tasks, run it blind on two agent configurations, and report results with error bars and without overclaiming. | Lab 6 (the project's eval set), AI-free check 3 |
| 7 | Run an independent, multi-reviewer, cross-model code review with adversarial verification, and judge whether it was worth its cost. | Lab 7 (the project's cross-model review) |
| 8 | Contribute a small, tested, disclosed change to a shared codebase that follows that project's contribution and AI policies. | Lab 8 |
| 9 | Evaluate claims about models, benchmarks, prices, and licenses against primary sources, with dates. | Reading responses, AI-free check 3 |
| 10 | Read, debug, and test code without AI, and explain every line of their own submitted work in a live walkthrough. | AI-free checks, walkthroughs |

## Required tools and cost

| Item | Notes |
| --- | --- |
| A laptop | macOS, Linux, or Windows with WSL. Must run a terminal, git, a code editor, and a container or VM tool. **No GPU needed.** `[Or: department lab machines.]` |
| Git and a GitHub account | Free. Used for every lab and the project. |
| Python 3 and/or Node.js | Whatever the starter repositories use. `[Specify versions.]` |
| A container or VM tool | Docker or equivalent, for the sandbox in [Lab 5](labs/lab-05-prompt-injection.md). `[Or: a department-provided VM image.]` |
| **One frontier coding-agent plan** | For example Anthropic's Claude Pro (includes Claude Code) or OpenAI's ChatGPT Plus (includes Codex). Both were $20/month as of November 2026 ([module 12 price snapshot](../modules/12-costs-subscriptions-and-apis.md#price-snapshot-as-of-2026-11-08)). `[Or: institutional licenses provided by the department.]` |
| Optional: a second lab's tool | A free tier or a classmate's tool from a different lab, for the cross-model steps in Labs 4 and 7. Never required. |

**What it costs.** A 15-week term spans about four billing months, so roughly $80 at November 2026 prices. Students can cancel after the term.

- **Check current education offers before you pay.** Vendors change student and education pricing often. Anthropic and OpenAI both sell education or institutional plans ([module 12](../modules/12-costs-subscriptions-and-apis.md#price-snapshot-as-of-2026-11-08), [module 15](../modules/15-learning-careers-and-responsibility.md#data-privacy-what-not-to-paste)), and what they include varies. This proposal doesn't assume any particular discount exists.
- **Don't use pay-per-token API keys for the labs.** No lab needs one. Agent sessions re-send the whole conversation every turn, so heavy use on API billing gets expensive quickly ([module 12](../modules/12-costs-subscriptions-and-apis.md#why-agentic-coding-eats-tokens)).
- **Free tiers are a second opinion, not a main tool.** Their limits are tight. OpenAI's free tier, for example, gave only limited Codex access on a small model as of November 2026 ([module 12](../modules/12-costs-subscriptions-and-apis.md#price-snapshot-as-of-2026-11-08)).
- **Nobody's grade depends on ability to pay.** `[Department: describe how students who can't buy a plan get access, for example loaner seats on a team plan or lab accounts.]` The instructor checks each term that every lab fits within one $20 plan's limits ([refresh checklist](instructor-guide.md#refresh-checklist-for-each-term)).
- **Set your data preferences first.** Consumer plans may let the vendor train on your chats and coding sessions, depending on a setting you control. Education and enterprise terms differ. Check your setting before the first lab ([module 15](../modules/15-learning-careers-and-responsibility.md#data-privacy-what-not-to-paste)).

> **Bryan's take:** API pricing is too expensive for heavy agentic use. Subscriptions are what make it affordable to work this way every day.

> **Bryan's take:** For coding, Claude and Codex are the best, in my opinion. Different models are better for different use cases.

Opinions about models date quickly. The course works with any frontier coding agent that can read a repository, run commands, and edit files; see [module 03](../modules/03-model-landscape.md#best-model-for-the-job) for the current landscape.

## Weekly schedule

### Workload

Plan on about 9–10 hours a week in total, which is typical for a `[3]`-credit course: about `[2.5]` hours in class and 6–7.5 hours outside it. The last column of the schedule estimates the outside hours for each week: reading, labs, and your share of the project. Weeks 1–4 are lighter while you set up. No week is planned above 7.5 outside hours; if you're regularly well past that, tell the instructor, because the estimates are meant to be checked against real students each term.

Two labs are done on the term project instead of alongside it. [Lab 6](labs/lab-06-your-own-eval.md) is the project's eval set and [Lab 7](labs/lab-07-multi-agent-review.md) is its cross-model review, so that work is done once and graded once.

### Schedule

Read the listed sections before the week's first session. "Students: Foundations + In practice" is the default depth for every module ([student path](../paths/students.md#how-to-read-each-module)). Each lab is released at least a week before it's due; its header gives both weeks. AI-free checks are short (about 30 minutes) and happen in class.

| Week | Topic | Read | In class | Due | Hours outside class |
| --- | --- | --- | --- | --- | --- |
| 1 | What this course means by vibe coding | [00](../modules/00-orientation.md) (all); [15](../modules/15-learning-careers-and-responsibility.md): [producing vs learning](../modules/15-learning-careers-and-responsibility.md#producing-the-work-vs-learning-from-it), [academic integrity](../modules/15-learning-careers-and-responsibility.md#academic-integrity) | The "using AI to code is like..." exercise ([00 Try it](../modules/00-orientation.md#try-it)); walk through the AI-use policy; tool setup clinic | Setup checklist; AI-free diagnostic (in class, ungraded) | 4 |
| 2 | What an LLM is | [01](../modules/01-what-is-an-llm.md): [next token](../modules/01-what-is-an-llm.md#the-one-idea-predict-the-next-token), [what it is not](../modules/01-what-is-an-llm.md#what-an-llm-is-not), [tokens](../modules/01-what-is-an-llm.md#tokens-and-tokenization), [sampling](../modules/01-what-is-an-llm.md#sampling-temperature-and-determinism), [hallucination](../modules/01-what-is-an-llm.md#hallucination-and-why-it-happens), [sycophancy](../modules/01-what-is-an-llm.md#sycophancy), [mental model](../modules/01-what-is-an-llm.md#a-working-mental-model) | The human language model game ([01 Try it](../modules/01-what-is-an-llm.md#try-it)); live demo: a hallucinated API | Reading response | 5 |
| 3 | Harnesses, tools, and MCP | [06](../modules/06-harnesses-and-tools.md): [what a harness is](../modules/06-harnesses-and-tools.md#what-a-harness-is), [history](../modules/06-harnesses-and-tools.md#a-short-history-from-autocomplete-to-orchestrators), [tools](../modules/06-harnesses-and-tools.md#tools-how-a-model-does-things), [MCP](../modules/06-harnesses-and-tools.md#mcp-the-model-context-protocol), [baseline setup](../modules/06-harnesses-and-tools.md#a-sane-baseline-setup); [13: a loop in 30 lines](../modules/13-open-source-ecosystem.md#framework-or-just-a-loop) | Live: the agent loop and the context breakdown; trace a 30-line loop | [Lab 1](labs/lab-01-tokens-and-temperature.md) | 5 |
| 4 | Context engineering | [07](../modules/07-context-engineering.md): [the ladder](../modules/07-context-engineering.md#the-buzzword-ladder-at-a-glance), [prompting basics](../modules/07-context-engineering.md#prompting-basics-that-still-matter), [what fills the window](../modules/07-context-engineering.md#what-actually-fills-an-agents-context-window), [context limits](../modules/07-context-engineering.md#context-limits-in-practice), [instruction files](../modules/07-context-engineering.md#the-rise-and-fall-of-giant-claudemd-and-agentsmd-files) | Trim a bloated `AGENTS.md`; rewrite vague prompts; **AI-free check 1** | [Lab 2](labs/lab-02-first-agent-session.md); teams formed | 5.5 |
| 5 | Agentic workflows | [08](../modules/08-agentic-workflows.md): [the loop](../modules/08-agentic-workflows.md#the-agent-loop), [it stops when it thinks it's done](../modules/08-agentic-workflows.md#the-key-fact-the-loop-stops-when-the-model-thinks-it-is-done), [autonomy](../modules/08-agentic-workflows.md#the-autonomy-spectrum), [Yegge's stages](../modules/08-agentic-workflows.md#steve-yegges-eight-stages), [core loop](../modules/08-agentic-workflows.md#the-core-loop-explore--plan--implement--verify--commit), [tests as contract](../modules/08-agentic-workflows.md#tests-as-the-agents-contract), [failure modes](../modules/08-agentic-workflows.md#failure-modes-and-counter-moves) | Live: a full explore-to-commit session; discuss how much autonomy works | Project pitch | 6 |
| 6 | Learning with AI, integrity, careers | [15](../modules/15-learning-careers-and-responsibility.md): [the evidence](../modules/15-learning-careers-and-responsibility.md#what-the-evidence-says), [how to learn with AI](../modules/15-learning-careers-and-responsibility.md#how-to-learn-with-ai-instead-of-outsourcing-learning), [careers](../modules/15-learning-careers-and-responsibility.md#careers), [deskilling](../modules/15-learning-careers-and-responsibility.md#deskilling-real-risk-or-old-panic) | Write-the-policy exercise ([15 Try it](../modules/15-learning-careers-and-responsibility.md#try-it)); AI-free debugging practice | [Lab 3](labs/lab-03-plan-test-build.md) | 6 |
| 7 | AI code review | [10](../modules/10-ai-code-review.md): [good and bad at](../modules/10-ai-code-review.md#what-they-are-good-and-bad-at), [layered workflow](../modules/10-ai-code-review.md#a-layered-review-workflow), [verify findings](../modules/10-ai-code-review.md#verify-findings-before-acting), [severity](../modules/10-ai-code-review.md#severity-triage), [reviewing AI PRs](../modules/10-ai-code-review.md#how-humans-should-review-ai-written-prs), [accountability](../modules/10-ai-code-review.md#accountability-the-human-who-merges-owns-it) | Live demo: tautological tests; review a seeded PR together | Project design doc | 6.5 |
| 8 | Security and prompt injection | [11](../modules/11-security-and-prompt-injection.md): Foundations (all), [incidents](../modules/11-security-and-prompt-injection.md#real-incidents-20252026), [coding-agent risks](../modules/11-security-and-prompt-injection.md#risks-specific-to-coding-agents), [defenses](../modules/11-security-and-prompt-injection.md#practical-defenses), [student checklist](../modules/11-security-and-prompt-injection.md#student-checklist) | Live demo: injection through a README, in a sandbox; threat-model a workflow ([11 Try it](../modules/11-security-and-prompt-injection.md#try-it)); **AI-free check 2** | [Lab 4](labs/lab-04-review-ai-code.md); Lab 5 sandbox plan approved | 7.5 |
| 9 | The model landscape and reading claims | [03](../modules/03-model-landscape.md): [names and tiers](../modules/03-model-landscape.md#how-to-read-model-names-and-tiers), [places in the chain](../modules/03-model-landscape.md#different-places-in-the-chain), [best model for the job](../modules/03-model-landscape.md#best-model-for-the-job), [picking next month](../modules/03-model-landscape.md#how-to-pick-a-model-next-month-when-all-of-this-is-stale); [05](../modules/05-judging-models.md): [what a benchmark is](../modules/05-judging-models.md#what-a-benchmark-actually-is), [claim checklist](../modules/05-judging-models.md#reading-a-benchmark-claim-a-checklist), [benchmark-maxing](../modules/05-judging-models.md#benchmark-maxing); for Lab 8: [13 etiquette](../modules/13-open-source-ecosystem.md#etiquette-for-contributing-with-ai) | Read a real launch post against the checklist; Lab 8 kickoff | [Lab 5](labs/lab-05-prompt-injection.md); [Lab 8](labs/lab-08-open-source-contribution.md) phase 1 (project proposal) | 7.5 |
| 10 | Building your own eval | [05](../modules/05-judging-models.md): [harness matters](../modules/05-judging-models.md#harness-matters), [productivity evidence](../modules/05-judging-models.md#real-world-productivity-evidence), [vibes](../modules/05-judging-models.md#vibes-are-data-too), [build your own eval](../modules/05-judging-models.md#build-your-own-eval), [small-eval statistics](../modules/05-judging-models.md#the-statistics-of-small-evals), [reward hacking](../modules/05-judging-models.md#cheating-reward-hacking-and-grader-trust) | Golden-task workshop; compute error bars by hand | Project: vertical slice deployed | 7 |
| 11 | Multiple agents | [09](../modules/09-multi-agent-systems.md): Foundations (all), [patterns](../modules/09-multi-agent-systems.md#patterns-and-when-each-helps), [review swarm](../modules/09-multi-agent-systems.md#recipe-1-a-review-swarm), [cross-model review](../modules/09-multi-agent-systems.md#recipe-2-cross-model-review), [parallel builders](../modules/09-multi-agent-systems.md#recipe-3-parallel-builders-when-you-must), [budgets](../modules/09-multi-agent-systems.md#budgets-and-stop-conditions), [anti-patterns](../modules/09-multi-agent-systems.md#anti-patterns) | Debate vs vote ([09 Try it](../modules/09-multi-agent-systems.md#try-it)); assign Lab 7 PRs within each team | Project security review; Lab 8 phase 2 (go-ahead received, or switch to the class repository) | 7 |
| 12 | How models are made; open vs closed weights | [02](../modules/02-training-and-tuning.md): [pipeline](../modules/02-training-and-tuning.md#the-pipeline-at-a-glance), [distillation](../modules/02-training-and-tuning.md#distillation-and-synthetic-data), [should you fine-tune?](../modules/02-training-and-tuning.md#should-you-fine-tune-at-all), [models that tune themselves](../modules/02-training-and-tuning.md#models-that-tune-themselves); [04](../modules/04-open-vs-closed-weights.md): [weights](../modules/04-open-vs-closed-weights.md#what-weights-actually-are), [openness spectrum](../modules/04-open-vs-closed-weights.md#the-openness-spectrum), [licenses](../modules/04-open-vs-closed-weights.md#licenses-in-practice), [hardware math](../modules/04-open-vs-closed-weights.md#running-open-models-the-hardware-math) | Fine-tune, retrieve, or prompt? ([02 Try it](../modules/02-training-and-tuning.md#try-it)); license review ([04 Try it](../modules/04-open-vs-closed-weights.md#try-it)); **AI-free check 3** | [Lab 6](labs/lab-06-your-own-eval.md), which is the project's eval set | 7 |
| 13 | Costs and the open-source ecosystem | [12](../modules/12-costs-subscriptions-and-apis.md): [three ways to pay](../modules/12-costs-subscriptions-and-apis.md#three-ways-to-pay), [why agents eat tokens](../modules/12-costs-subscriptions-and-apis.md#why-agentic-coding-eats-tokens), [worked example](../modules/12-costs-subscriptions-and-apis.md#worked-example-one-hour-of-agentic-coding), [cost per task](../modules/12-costs-subscriptions-and-apis.md#cost-per-task-not-cost-per-token); [13](../modules/13-open-source-ecosystem.md): [map of the stack](../modules/13-open-source-ecosystem.md#a-map-of-the-stack), [AI slop](../modules/13-open-source-ecosystem.md#the-other-side-ai-slop-and-maintainer-burden), [students contributing](../modules/13-open-source-ecosystem.md#how-students-can-contribute-to-open-source-with-ai-responsibly) | The maintainer's chair ([13 Try it](../modules/13-open-source-ecosystem.md#try-it)); a quick team budget ([12 Try it](../modules/12-costs-subscriptions-and-apis.md#try-it)) | [Lab 7](labs/lab-07-multi-agent-review.md), which is the project's cross-model review | 7 |
| 14 | Keeping up | [14](../modules/14-keeping-up.md): [what stays stable](../modules/14-keeping-up.md#what-stays-stable), [ups and downs](../modules/14-keeping-up.md#ups-and-downs-are-normal), [model, task, or harness?](../modules/14-keeping-up.md#is-it-the-model-the-task-or-the-harness), [launch claims](../modules/14-keeping-up.md#weighing-launch-claims), [a routine](../modules/14-keeping-up.md#a-sustainable-routine), [evaluating a release](../modules/14-keeping-up.md#evaluating-a-brand-new-release-in-an-afternoon) | Incident presentations ([14 Try it](../modules/14-keeping-up.md#try-it)); final-sprint working session | [Lab 8](labs/lab-08-open-source-contribution.md) | 7 |
| 15 | Ship and reflect | Re-read [00: six ideas](../modules/00-orientation.md#six-ideas-that-outlast-the-hype) and [15: the human side](../modules/15-learning-careers-and-responsibility.md#the-human-side) | Final demos; revisit the week 1 analogies; course retrospective | Shipped app and demo; individual reflective report | 7 |
| Finals | Walkthroughs |  | Individual 10-minute walkthroughs of project code |  | 1 |

## Term project

### What you build

Teams of three or four build and ship a small, real application for a real user, using supervised coding agents. "Real" means someone outside the team relies on it: a campus club, a nonprofit, a lab group, a local business, or a tool other students use. "Small" means one clear job done well. The point is the process: how you specify, constrain, verify, review, and secure work that agents do, and what you learn along the way.

### Constraints

- **A real user.** Name one person outside the team as your user and meet them at least twice. At least three people outside the team use the app before week 15.
- **No cost beyond your agent plans.** Deploy on a free hosting tier, or ship an installable package, CLI, or browser extension.
- **No paid model API calls inside the app.** The app doesn't need to use AI at all. `[Unless the department provides API keys.]`
- **No real personal data in development or in prompts.** Use synthetic data. An app that will store other people's personal data needs instructor approval and must follow `[institution's data policy]` ([module 15](../modules/15-learning-careers-and-responsibility.md#data-privacy-what-not-to-paste)).
- **Repository rules.** Branch protection on `main`, with one approving review from a teammate who didn't write the change. Secret scanning on. Tests in CI. Every pull request uses the [PR template from module 10](../modules/10-ai-code-review.md#make-the-author-explain-the-change), including "What the agent did vs what I did."
- **Supervised agents only.** Any autonomy level is allowed if your checks can catch what you no longer watch ([module 08](../modules/08-agentic-workflows.md#the-autonomy-spectrum)). Unattended runs need a turn cap, a sandbox, and a pull request a human approves. No skip-permissions modes outside a disposable sandbox ([module 11](../modules/11-security-and-prompt-injection.md#risks-specific-to-coding-agents)).
- **Keep the evidence.** Commit history, PR descriptions, AI logs, and exported transcripts for key decisions.

### Deliverables

| Due | Deliverable | What it contains | Tier | Weight |
| --- | --- | --- | --- | --- |
| Week 5 | **Pitch** | One page: the user, the problem, the smallest useful version, the biggest risk | AI-as-tutor | Gate (feedback only) |
| Week 7 | **Design doc** | Problem and user; requirements and non-goals; architecture and data model; the interfaces you'll write *before* agents build in parallel ([module 09](../modules/09-multi-agent-systems.md#recipe-3-parallel-builders-when-you-must)); test strategy (what is your oracle?); which tasks go to agents and at what autonomy; quota plan; risks | AI-as-tutor: agents may interview you and critique drafts; the decisions and the text are yours | 5% |
| Week 10 | **Vertical slice** | One end-to-end feature deployed, with tests and CI | AI-accelerated | Milestone (feedback only) |
| Week 11 | **Security review** | Rule of Two analysis for your agent workflow and for the app ([module 11](../modules/11-security-and-prompt-injection.md#two-frameworks-that-make-this-tractable)); the [team checklist](../modules/11-security-and-prompt-injection.md#team-checklist) items that apply; every dependency verified as real and intended; scanner results; a second-model security review with each finding verified; fixes | AI-accelerated | 5% |
| Week 12 | **Eval set** | This is [Lab 6](labs/lab-06-your-own-eval.md), done on your project: at least eight golden tasks from your project's history (three or more per member), with hidden tests, run blind on two agent configurations and summarized with error bars, plus the configuration your team chose for the final sprint and why. Nothing extra to submit. | AI-accelerated; task selection and scoring are yours | Graded as Lab 6 |
| Week 13 | **Cross-model code review** | This is [Lab 7](labs/lab-07-multi-agent-review.md), done on your project: each member runs a review swarm with adversarial verification on a different teammate's pull request from week 10 on, using a different lab's model where possible. Confirmed High and Medium findings are fixed through reviewed PRs. Nothing extra to submit. | AI-accelerated | Graded as Lab 7 |
| Week 15 | **Shipped app, repository, and demo** | Working app with real users; README covering trade-offs, rejected alternatives, and a short section on what your eval (Lab 6) and reviews (Lab 7) found and what you changed; tests and CI green; a 10-minute demo that includes one thing an agent got wrong | AI-accelerated | 10% |
| Week 15 | **Reflective report** (individual) | "What I learned vs what the AI did" (below) | AI-free | 6% |
| Finals | **Walkthrough** (individual) | 10 minutes: explain code you merged, answer "what if" questions, show the test that guards it | AI-free | 4% |

Team deliverables get one team score, adjusted for each member by individual evidence: commits, reviews given, AI logs, and `[peer evaluation process]`.

### The reflective report

1,000 to 1,500 words, written without AI. Answer each prompt with evidence from your commits, PRs, and logs.

1. **What I built.** Your part of the system, in two paragraphs.
2. **What the agents did.** Roughly how much of your merged code an agent drafted, and how you know.
3. **What I did that the agents didn't or couldn't.** Decisions, specs, tests, reviews, debugging.
4. **Three times I overrode an agent,** and why.
5. **One bug an agent introduced,** and how it was caught (or missed).
6. **What I can now do without AI.** Rebuild one small component without AI before you write this section ([module 15](../modules/15-learning-careers-and-responsibility.md#how-to-learn-with-ai-instead-of-outsourcing-learning), habit 7). What came easily? What didn't?
7. **Where I sit on Yegge's stages** ([module 08](../modules/08-agentic-workflows.md#steve-yegges-eight-stages)), and whether that was the right place for this project.
8. **What I'd do differently** next time.

## Assessment

| Component | Weight | Notes |
| --- | --- | --- |
| Labs 1–8 | 45% | Labs 1–5 and 8: 5% each. Labs 6 and 7: 7.5% each, because they're done on the term project and serve as its eval set and cross-model review. Each lab has its own rubric. |
| Term project | 30% | Design doc 5%, security review 5%, shipped app 10%, reflective report 6%, walkthrough 4%. |
| AI-free checks | 15% | Three in-class checks, 5% each (weeks 4, 8, 12): reading code, predicting what code and tests do, finding bugs by hand, explaining core concepts. |
| Participation | 10% | Reading responses, in-class exercises, peer review, Lab 8 maintainer shifts if you use the class repository. |

`[Grading scale.]` `[Late-work policy.]` `[Attendance policy.]`

**Walkthroughs.** Any submission may be followed by a five-minute walkthrough with the instructor or a TA. Expect at least one per student per term outside the final. A walkthrough that shows you can't explain your submission means it doesn't count as yours yet: you get one chance to redo the walkthrough or the work. The instructor guide describes [how walkthroughs are run](instructor-guide.md#oral-check-ins-and-walkthroughs).

## AI-use policy

This course requires AI tools, and it also requires work without them. Both are deliberate. The research summarized in [module 15](../modules/15-learning-careers-and-responsibility.md#what-the-evidence-says) finds that outsourcing the thinking weakens the skill you outsourced, while using AI to ask why, get hints, and check understanding mostly doesn't. Supervising agents also depends on skills you build by hand, such as reading and debugging code. So the course mixes AI-free practice, AI-as-tutor learning, and full acceleration.

### The three tiers

These labels come from [module 15's suggested policy](../modules/15-learning-careers-and-responsibility.md#a-suggested-policy-for-an-ai-accelerated-course).

| Tier | What's allowed | What's graded |
| --- | --- | --- |
| **AI-free** | No AI tools of any kind, including IDE autocomplete and AI features in search or editors. | The fundamentals you need without help. |
| **AI-as-tutor** | AI may explain, give hints, ask you questions, and critique your work. It may not write code or prose you submit. | Your own work, and your use of AI to learn. |
| **AI-accelerated** | Use any AI tools. | The result, your design decisions, your verification evidence, and your ability to explain every line. |

Two clarifications:

- **A model you're studying isn't "AI help."** In Labs 1 and 5 the model is the subject of the experiment. The tier governs who writes what you submit.
- **Some things are always yours.** Reflections, AI logs, PR descriptions, and replies to reviewers are written by you in every tier. In AI-accelerated work, AI may critique them, not write them.

### Tier for each assignment

| Assignment | Tier |
| --- | --- |
| Week 1 diagnostic; AI-free checks 1–3 | AI-free |
| Reading responses | AI-as-tutor. You're encouraged to have AI quiz you on the reading ([module 00](../modules/00-orientation.md#reading-this-material-with-an-ai)). |
| [Lab 1: Tokens and temperature](labs/lab-01-tokens-and-temperature.md) | AI-as-tutor |
| [Lab 2: First agent session](labs/lab-02-first-agent-session.md) | AI-accelerated |
| [Lab 3: Plan, test, build](labs/lab-03-plan-test-build.md) | Part A (spec and acceptance tests): AI-as-tutor. Part B (implementation): AI-accelerated. |
| [Lab 4: Review AI code](labs/lab-04-review-ai-code.md) | Part A (hand review): AI-free. The rest: AI-accelerated. |
| [Lab 5: Prompt injection](labs/lab-05-prompt-injection.md) | AI-accelerated, under the lab's mandatory safety rules |
| [Lab 6: Your own eval](labs/lab-06-your-own-eval.md) | AI-accelerated for tooling. Task selection, hidden tests, and blind scoring are yours. |
| [Lab 7: Multi-agent review](labs/lab-07-multi-agent-review.md) | AI-accelerated |
| [Lab 8: Open-source contribution](labs/lab-08-open-source-contribution.md) | AI-as-tutor, or stricter if the project's own policy is stricter |
| Project design doc | AI-as-tutor |
| Project code and security review (the eval set and cross-model review are Labs 6 and 7) | AI-accelerated |
| Project reflective report and walkthrough | AI-free |

### Rules that apply in every tier

1. **Disclose.** Every AI-as-tutor or AI-accelerated submission includes an AI log (template below).
2. **Own it.** You're responsible for everything you submit, including bugs, security flaws, and license problems an AI introduced ([module 15](../modules/15-learning-careers-and-responsibility.md#human-accountability)).
3. **Explain it.** If you can't explain it in a walkthrough, it doesn't count as yours.
4. **Protect data.** Don't paste other students' work, anyone's personal data, or credentials into AI tools ([module 15](../modules/15-learning-careers-and-responsibility.md#data-privacy-what-not-to-paste)).
5. **The stricter rule wins.** An open-source project's AI policy, a client's confidentiality request, or another course's policy overrides this one when it's stricter.
6. **Keep evidence.** Keep your commit history and export the transcript of any agent session that made a key decision. Most harnesses save sessions locally.
7. **Ask first.** When you're unsure whether a use is allowed, ask the instructor in writing before you submit.

### AI log template

Put this at the end of each AI-as-tutor or AI-accelerated submission.

```markdown
## AI log: <assignment name>

- Tier: <AI-as-tutor | AI-accelerated>
- Tools: <harness and version, model, plan>
- What I used AI for: <two to five bullets>
- What I did myself: <two to five bullets>
- One thing the AI got wrong that I caught, and how I caught it:
- One thing I learned:
- Transcripts attached: <file names, for key decisions>
```

For commits, pull requests, and READMEs, a one-paragraph disclosure is enough. This is [module 15's template](../modules/15-learning-careers-and-responsibility.md#disclosure-template-for-students):

```text
AI assistance: I used [tool] to [explain X / suggest a fix for Y /
generate the initial version of Z]. I reviewed and modified the output,
[wrote the tests myself / rewrote the parser]. The AI incorrectly
[suggested a package that doesn't exist / missed an edge case], which
I caught by [running the tests / reading the docs].
```

If your tool adds a co-author trailer to commits, leave it on unless a project's rules say otherwise ([module 15](../modules/15-learning-careers-and-responsibility.md#attribution-and-disclosure-in-commits-and-prs)).

## Accessibility

`[Insert the institution's accessibility statement and the disability services office's contact information.]`

Course-specific notes:

- Oral walkthroughs can be replaced by a written or recorded walkthrough as an accommodation.
- AI tools can be assistive technology, for example voice-driven coding or plain-language explanations ([module 15](../modules/15-learning-careers-and-responsibility.md#bias-and-accessibility)). If you need one during an AI-free assessment, arrange it through `[disability services]` in advance. It won't count against you.
- Project apps must pass an automated accessibility checker and a keyboard-only test before the final demo. Generated interfaces often miss labels, contrast, and keyboard access.

## Academic integrity

`[Insert the institution's academic integrity policy and reporting process.]`

In this course, these are integrity violations:

- Submitting AI-written code or prose in AI-free or AI-as-tutor work.
- Leaving out AI use that the AI log should have disclosed.
- Fabricating or editing logs, transcripts, test output, or commit history.
- Submitting another person's work as your own, whether or not an AI was involved.
- Breaking the safety rules in [Lab 5](labs/lab-05-prompt-injection.md), or testing injection against systems you don't own.
- Violating an open-source project's AI policy in Lab 8.

The course doesn't use AI-detection tools as evidence. AI use is hard to detect reliably ([module 15](../modules/15-learning-careers-and-responsibility.md#what-instructors-can-reasonably-allow)), so the course relies on process evidence (commits, logs, transcripts) and walkthroughs. A walkthrough you can't complete is not by itself a finding of misconduct. It means the work doesn't count yet.

## Keeping this course current

This field changes monthly, and parts of this syllabus will be wrong within a term ([module 14](../modules/14-keeping-up.md#how-fast-it-moves)). The durable parts are the habits: verification, context control, security, review, and honest evaluation. The perishable parts are names, prices, commands, and policies. Before each term, re-verify:

1. **Plans and prices** for the tools students will buy, and current education offers ([module 12](../modules/12-costs-subscriptions-and-apis.md#price-snapshot-as-of-2026-11-08)).
2. **Data and training terms** for consumer and education plans ([module 15](../modules/15-learning-careers-and-responsibility.md#data-privacy-what-not-to-paste)).
3. **Every command and setting named in a lab:** plan mode, the context view, checkpoints, review commands, permission and sandbox settings, hooks, non-interactive mode. For Lab 5, check how deny rules treat shell commands and whether each harness's own sandbox starts inside the recommended container.
4. **The free tools in Lab 1:** a tokenizer page and a playground with a temperature control.
5. **The AI policies of open-source projects** suggested for Lab 8 ([module 13](../modules/13-open-source-ecosystem.md#the-other-side-ai-slop-and-maintainer-burden)).
6. **That each lab still fits in one $20 plan.** Run it yourself and note the quota used.
7. **That the live demos still fail the way they're supposed to.** Models improve; some demos stop working.
8. **The "Last verified" date of each assigned module.** Anything older than about six months needs a check.
9. **The institution's AI and integrity policies,** which are changing too.

The full list, with how to check each item, is the instructor guide's [refresh checklist](instructor-guide.md#refresh-checklist-for-each-term).

## Sources

Everything in this syllabus draws on the modules of this knowledge base, which cite their primary sources. The most directly used:

- [Module 00](../modules/00-orientation.md): the course's stance and ground rules.
- [Module 08](../modules/08-agentic-workflows.md): the explore → plan → implement → verify → commit workflow.
- [Module 10](../modules/10-ai-code-review.md): review checklist, PR template, accountability.
- [Module 11](../modules/11-security-and-prompt-injection.md): threat models and defenses.
- [Module 12](../modules/12-costs-subscriptions-and-apis.md): plans and prices.
- [Module 15](../modules/15-learning-careers-and-responsibility.md): learning evidence, the three-tier policy, disclosure, data privacy.

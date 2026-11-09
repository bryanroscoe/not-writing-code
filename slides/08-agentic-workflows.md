---
marp: true
theme: not-writing-code
paginate: true
title: "08: Agentic workflows"
description: "How much autonomy actually works"
footer: "A Brief Introduction to Not Writing Code · 08 Agentic workflows"
---

<!-- _class: lead -->

# 08: Agentic workflows

How much autonomy actually works

<!--
Today we cover what a coding agent actually is, the daily workflow that holds up, and what the evidence says about letting agents run on their own. The reading is module 08. About 40 minutes, then discussion.

Products and numbers are as of November 2026 unless a slide gives another date.
-->

---

## Why this matters

- A coding agent is a loop that runs until it *thinks* it's done
- Most of the skill is controlling that loop
- Autonomy is a dial you turn one notch at a time
- Only turn it up when your checks catch what you stop seeing
- The productivity evidence is mixed and keeps changing

<!--
The people who get good results from agents mostly differ in how they control the loop. Which model they use matters less.

You can go anywhere from autocomplete to agents that open pull requests while you sleep. Every notch up means you see less of the code yourself. So turn it one notch at a time, and only when an automated check can catch what you'll stop looking at.

METR measured a 19% slowdown for experienced developers in early 2025, and its 2026 follow-up points to modest speedups with wide error bars. We'll come back to that in part 3.

Agents help with a lot more than feature code: reading unfamiliar code, debugging from logs, migrations, SQL, scripts, tickets, incident timelines. Those make good first tasks to trust an agent with. They're lower risk and they have clear checks.
-->

---

## The agent loop

**think → act (call a tool) → observe → think → …** until the model decides it's done. Then you verify.

> "Claude stops when the work looks done." … "In practice that makes you the test suite."
> (Claude Code best practices)

A check that returns pass or fail beats asking nicely.

<!--
A chat assistant answers once and waits. An agent keeps going. It's a language model in a loop that lets it take actions (read a file, run a command, edit code) and see what happened. The pattern is called ReAct, "reason + act," from Yao et al. in 2022. Every coding agent you'll use is a version of this loop: Claude Code, Codex, Cursor's agent, Copilot's agent mode, the open-source ones.

If these terms are new:
- A tool is a function the model can call, like read_file or run_command. The model writes the request; the harness runs it and hands back the result.
- The harness is the program around the model. It runs the loop, holds the tools, enforces permissions, and manages context. Claude Code and the Codex CLI are harnesses.
- The context window is everything the model can see on a turn. Large but finite.

If the agent has nothing to run that tells it the work is done, "looks done" is all it has. You make agents reliable by giving them tests, a build, a linter, or a screenshot, and asking for the evidence.

The SWE-agent paper (Yang et al., 2024) showed tool design matters as much as the model. It called this the agent-computer interface.

Whatever the tool, you control four things: what it knows (prompt, spec, instruction files), what it can do (tools, permissions, sandbox), how it knows it's done (tests, builds, a reviewer), and how long and how much (turn, spend, and time limits).
-->

---

## Autonomy is a dial

| Level | What it looks like | Who checks each change |
| --- | --- | --- |
| 1. Autocomplete | The editor suggests the next line | You, as you type |
| 2. Chat | Paste code in, paste answers back | You, line by line |
| 3. Supervised agent | One agent edits and runs commands while you watch | You, per step or diff |
| 4. Parallel supervised | Several agents, each on its own checkout | You, per branch |
| 5. Background or cloud | Hand off a task, get a PR later | You or a reviewer, at the PR |
| 6. Fully autonomous | Specs in, software out | Automated checks only |

<!--
"Using AI to code" can mean very different amounts of delegation, so it helps to name the levels. This six-level table is the course's own framing. Look at the right-hand column. Going down, the human check moves from every keystroke to every step, every branch, every PR, and finally nobody.

Level 6 is what people call a "software factory" or "dark factory."

Dan Shapiro's five levels (January 2026) are another map, borrowed from self-driving cars. Level 0 is "your parents' Volvo." Level 3 is "a Waymo with a safety driver," where you spend your day reviewing AI-written code. Level 4 is "a robotaxi": you write specs and check whether the tests pass. Level 5 is the dark factory, named after lights-out factories that run without people.

The third map is Steve Yegge's eight stages, which describes the developer instead of the tool. That's next.
-->

---

## Yegge's eight stages: 1–4

| Stage | Yegge's words | Moving up safely |
| --- | --- | --- |
| 1 | "Zero or Near-Zero AI" | One small, well-tested agent change. Read the whole diff. |
| 2 | "Coding agent in IDE, permissions turned on" | Allowlist the safe commands you keep approving, not everything |
| 3 | "Agent in IDE, YOLO mode" | A sandbox or auto mode, plus hard deny rules |
| 4 | "In IDE, wide agent" | Tests are the contract. Ask for output, not "done." |

From [Yegge's republication of "Welcome to Gas Town"](https://yegge.ai/essays/welcome-to-gas-town/) (January 1, 2026). Labels excerpt his prose; full wording is in the notes. The right column is this course's advice.

<!--
Steve Yegge is a long-time engineer and blogger, and co-author with Gene Kim of the book Vibe Coding. On January 1, 2026 he published "Welcome to Gas Town," introducing his open-source agent orchestrator. Partway through, he asks readers to "locate yourself on the chart" of "The 8 Stages of Dev Evolution To AI." It's become common shorthand.

His full wording for these four stages:
1. "Zero or Near-Zero AI: maybe code completions, sometimes ask Chat questions." AI feels like a smarter search box, and you own every keystroke.
2. "Coding agent in IDE, permissions turned on. A narrow coding agent in a sidebar asks your permission to run tools." Lots of approve buttons, and you learn what agents try to do. Commit before each task so you can revert.
3. "Agent in IDE, YOLO mode: Trust goes up. You turn off permissions, agent gets wider." Faster, and a little nervous. Instead of no permissions, use a sandbox or a classifier-based auto mode, plus hard deny rules for secrets, pushes, and production. Module 11 covers why.
4. "In IDE, wide agent: Your agent gradually grows to fill the screen. Code is just for diffs." You review diffs instead of typing code.

Place yourself on the chart, silently. We'll come back to it at the end.
-->

---

## Yegge's eight stages: 5–8

| Stage | Yegge's words | Moving up safely |
| --- | --- | --- |
| 5 | "CLI, single agent. YOLO." | Review every PR, never skip it. Add an independent reviewer. |
| 6 | "CLI, multi-agent, YOLO." | One worktree per agent, non-overlapping tasks, a task list |
| 7 | "10+ agents, hand-managed." | Tracking and merge discipline, or step back to 6 |
| 8 | "Building your own orchestrator." | Treat it as production software: tests, budgets, kill switches |

<!--
Full wording:
5. "CLI, single agent. YOLO. Diffs scroll by. You may or may not look at them." Terminal-first; the agent drives and you steer. Move review from every edit to every pull request, but never skip it.
6. "CLI, multi-agent, YOLO. You regularly use 3 to 5 parallel instances. You are very fast." It feels like running a small team, and your attention becomes the bottleneck.
7. "10+ agents, hand-managed. You are starting to push the limits of hand-management." Tabs everywhere, lost work, merge conflicts, agents you forgot about. Add an issue list agents can read and update.
8. "Building your own orchestrator. You are on the frontier, automating your workflow." You're building infrastructure for agents instead of features.

Yegge is blunt about who stage 8 tooling is for: "If you're not at least Stage 7, or maybe Stage 6 and very brave, then you will not be able to use Gas Town." He's just as upfront about the trade-offs. Gas Town is "100% vibe coded. I've never seen the code." It's "expensive as hell." Work is "chaotic and sloppy": "Some bugs get fixed 2 or 3 times, and someone has to pick the winner. Other fixes get lost."

Gas Town's roles (a Mayor you talk to, worker Polecats, a merging Refinery, a supervising Witness) read like a list of stage 7 problems: who's doing what, merge conflicts, and agents that stop when their context fills up.
-->

---

## Reading the chart

1. The stages measure delegation, not quality
2. Yegge assumes YOLO from stage 3 up; sandboxes get you most of the speed
3. Moving down is allowed

<!--
You don't have to climb this ladder.

First, a stage 3 engineer with strong tests can ship better software than a stage 7 engineer without them. The chart says how much you hand off, not how good the result is.

Second, Yegge assumes permissions are off from stage 3 up. You don't have to take on that exposure to get the speed; sandboxes, deny rules, and worktrees cover most of it. Module 11 explains the risk of running without permissions on your main machine.

Third, plenty of experienced engineers move between stages depending on the task: stage 6 for a batch of independent chores, stage 4 for a delicate change to payment code. Which tasks in your week would you run at stage 4, and which at stage 6?
-->

---

<!-- _class: divider -->

# Part 2: In practice

The workflow that holds up in daily use

<!--
In part 2, we'll use the core loop day to day, with prototypes, tests, git, parallel agents, and unattended runs.
-->

---

## The core loop

**explore → plan → implement → verify → commit**

| Step | What you ask for |
| --- | --- |
| Explore | Read-only. "Don't change anything yet." |
| Plan | A plan you read before any edit (plan mode) |
| Implement | A failing test first, then make it pass |
| Verify | The command it ran and the output |
| Commit | Small commits: the test, then the fix |

<!--
The two leading coding-agent vendors have landed on the same workflow. Anthropic's original Claude Code best-practices post (April 2025) called it "explore, plan, code, commit." The current docs stress writing a spec, giving the agent a check to run, and having someone who didn't write the code review it. OpenAI's Codex best practices say "If the task is complex, ambiguous, or hard to describe well, ask Codex to plan before it starts coding," and "Codex can do this loop for you, but only if it knows what 'good' looks like."

Step by step:
- Explore first. Make the agent build a picture before it touches anything: "Read src/auth/ and its tests. Don't change anything yet. Explain how token refresh works."
- The plan is the cheapest place to catch a wrong idea. Claude Code has plan mode (Shift+Tab until the status bar shows it): it "reads files and proposes a plan but makes no edits until you approve." Codex has a Plan mode too. If you don't know what you want yet, have the agent interview you and write SPEC.md, then start a fresh session to build from it.
- When it implements, the test is the contract. "Write a failing test that reproduces the bug. Run it and show me the failure. Then make it pass without modifying the test."
- To verify, remember "All tests pass" on its own "tells you very little" (Anthropic docs). Ask for the command and the output. Then get an independent look from a fresh session or a review command. For a UI, look at it yourself.
- Commit the test and the fix separately. Write or check the message yourself.

The module's sample session fixes a rate limiter that put every user behind a load balancer in one bucket. Read-only exploration, a question back to the human, a plan that names the security trap, a test that fails before it passes, a two-file diff, and a reviewer that never saw the conversation.
-->

---

## Prototype first

> "plan to throw one away; you will, anyhow."
> (Fred Brooks, *The Mythical Man-Month*, 1975)

A throwaway version took weeks then. Now it takes minutes.

| Level | What you build | Feedback you get |
| --- | --- | --- |
| Application | Clickable mockup, single-page app, Artifact or Claude Design prototype | "Not that button, and where's the export?" |
| Code | A spike: two API shapes, two module layouts | Which code you'd rather read and keep |

<!--
The core loop assumes you know what you want. Often you don't, until you see something. That's when a prototype earns its keep. The module calls this draft-driven or prototype-driven development.

The idea is old. Brooks wrote "plan to throw one away" in 1975. What changed is the cost. A throwaway version used to cost weeks, so teams argued over specs instead. Now an agent can build one in minutes, and you react to it instead of imagining it.

You can do this at two levels:
- For an application, put a clickable mockup in front of the people who'll use it. "Not that button, and where's the export?" is better feedback than any review of a requirements document.
- For code, do a spike. Try two shapes of an API or two ways to structure a module, then look at the actual code and pick one. Code you can read is easier to judge than a design you have to picture.

A spike is a short, timeboxed experiment in code that answers a design question before you commit to an approach.
-->

---

## Prototyping well

1. Timebox it and mark it as a draft: a `spike/` branch, a README banner
2. Write what you learned into a short spec
3. Rebuild or harden it on purpose; never let it slide into production

A prototype *looks* finished. That's the risk.

<!--
These steps come from the module.

1. Timebox it and say out loud that it's a draft. Build it on a spike/ branch or in a scratch folder, with a banner in the README.
2. Put what you learned in a short spec: the decisions, the surprises, what users said. Module 07 covers spec-driven development.
3. Rebuild or harden on purpose. Either start fresh with the core loop, tests first, or keep the prototype and review it as production code, line by line. Don't let it drift into production by default.

A prototype looks finished, so people (you included) start treating it as the real thing before anyone has checked error handling, security, or tests.

To be fair to Brooks, in the 20th-anniversary edition (1995) he called the throw-one-away advice too simple and argued for growing software incrementally. Get to something concrete fast, then harden the version you keep.
-->

---

## Tests are the agent's contract

The contract only works if the agent can't quietly rewrite it.

- Write or approve the tests yourself; commit them separately
- Make each test fail first
- Check the test diff: `git diff --stat main -- tests/`
- Enforce with a hook or deny rule, not just a `CLAUDE.md` line
- Keep some checks out of the agent's reach

<!--
Test-driven development means writing a failing test before the code that makes it pass. It suits agents unusually well. Simon Willison: "Test-first development is particularly effective with agents that can iterate in a loop."

The problem is that agents under pressure to make tests pass sometimes delete, skip, or special-case them. So defend the contract:
- A test that never failed may not test anything.
- Checking the test diff takes a second.
- Anthropic's docs say a line in CLAUDE.md is followed "nearly every time," while a hook or a deny rule applies every time. Anthropic's long-running agent harness told its agents: "It is unacceptable to remove or edit tests because this could lead to missing or buggy functionality."
- StrongDM's team keeps end-to-end "scenarios" outside the codebase, like a holdout set in machine learning, so agents can't tune the code to them.
-->

---

## Safety nets and steering

- One branch per task; small diffs that keep the build green
- `git add -p` and `git diff --stat main`: what did it touch?
- Checkpoints (`/rewind`) work *alongside* git, not instead of it
- Watch the first minute; press `Esc` the moment it drifts
- After two failed corrections, `/clear` and write a better prompt

<!--
Small diffs are easier for you to review, easier for a review bot to check, and cheaper to throw away. Ask for the smallest change that satisfies the spec, and split big work into steps that each leave the build green.

Git is your undo button. A branch per task, stage hunk by hunk while you read, look at the diff stat against main, and restore any unwanted edit from HEAD.

Harnesses also keep checkpoints. In Claude Code, /rewind (or Esc twice) restores code, conversation, or both. There are two limits. Checkpoints only cover files the agent changed with its own edit tools, so changes made by shell commands aren't restored. And they "work alongside git rather than replacing it."

Anthropic's steering advice is short enough to memorize: "Watch the first minute, press Esc the moment Claude drifts, and after two failed corrections run /clear and write a better prompt instead of a third." A conversation with two failed attempts in it keeps re-reading them. A fresh start with one better prompt usually wins.
-->

---

## Parallel agents need worktrees

A git worktree is another checkout of the same repo, in its own folder, on its own branch.

- One task, one agent, one worktree, one branch
- Pick tasks that touch different files
- Keep a written task list you and the agents can see
- Review every branch before merging
- Mind the disk and the bill; remove merged worktrees

<!--
Worktrees share one .git history, so several agents can edit at once without overwriting each other's files. OpenAI's guide lists "Running live tasks on the same files without using Git worktrees" as a common mistake. Claude Code can create worktrees itself (claude -w), and its /batch command splits a large mechanical change into 5 to 30 units, each with its own worktree and pull request.

The rules address common problems:
- Two agents editing the same module produce a merge conflict or, worse, two inconsistent designs. Module 09 explains why read-heavy work parallelizes far better than write-heavy work.
- At stage 7, losing track is the main failure, so the task list isn't optional.
- Parallelism multiplies output, and it multiplies unreviewed code just as fast.
- Each worktree needs its own dependencies and build output, and each agent spends tokens.
-->

---

## Before you walk away

Five questions before any unattended run:

1. Does it know what done looks like?
2. Can it check its own work?
3. What is it allowed to touch?
4. What stops it?
5. Where does the result go, and who signs off?

<!--
Going from "I watch" to "I come back later" is where most of the risk comes in. These five questions are from Anthropic's docs. Some example answers:
1. A goal, a spec file, or a failing test to turn green.
2. Tests, a Stop hook that blocks finishing until a check passes, a review step.
3. Permissions, a sandbox, a worktree, one branch it may push to.
4. A turn limit, a budget limit in dollars, a provider spend limit.
5. A pull request, then a person approving the merge.

For scripted batch runs, like migrating one file per run to a new logger API, the docs say: "Try it on three files first, see what goes wrong, fix the prompt, then run the rest."

The extreme version is Geoffrey Huntley's "Ralph Wiggum" technique (July 2025): "In its purest form, Ralph is a Bash loop" that feeds the same prompt file to an agent forever. Each pass starts with fresh context and carries state in files and git history. Huntley's own caveats: do one thing per loop, wire in tests and a type checker as "backpressure," expect to "wake up to a broken codebase that doesn't compile from time to time," and "There's no way in heck would I use Ralph in an existing code base." Harnesses now ship tamer versions of the idea, like Claude Code's /loop and /goal and Codex automations.
-->

---

## Failure modes and counter-moves

| Failure | Counter-move |
| --- | --- |
| Vague task | Name the file, the symptom, and what "fixed" means |
| Hallucinated APIs and packages | Typecheck every step; verify new dependencies by hand |
| Fake or tautological tests | Approve tests first; make them fail first |
| Over-engineering | "Smallest change. No new abstractions or dependencies." |
| Sycophancy | Ask it to argue the other side, and for evidence |
| Context exhaustion and drift | One task per session; `/clear` between tasks |
| Declaring victory early | Require the command and its output |
| Reward hacking | Hidden tests and evaluators the agent can't edit |

<!--
Talk through two or three rows, depending on the audience.

- On vague tasks, Anthropic's example is not "fix the login bug" but "users report login fails after the session times out. look at token refresh in src/auth/, write a failing test that reproduces it, then fix it."
- Hallucinated packages are common. In one study, at least 5.2% of packages suggested by commercial models and 21.7% by open models didn't exist (Spracklen et al., 2024). Attackers register those names. Module 11 covers this.
- Tautological tests check a mock against its own setup. Mutation testing (break the code on purpose and see if a test notices) catches them.
- On over-engineering, Anthropic warns that if you fix every finding a reviewer raises, "you end up with extra abstraction layers and tests for cases that can't happen."
- Sycophancy is measured and trained-in (Sharma et al., 2023). OpenAI rolled back a GPT-4o update in April 2025 for being overly agreeable.
- For drift, compact with a focus and keep a progress file. Cursor found even its long-running systems needed periodic fresh starts "to combat drift and tunnel vision."
- One that's not on the slide is silent scope creep, the "while I was there" refactor. State the scope, check the diff stat, reject unrelated changes.
-->

---

<!-- _class: divider -->

# Part 3: How much autonomy works?

The evidence on both sides, and what the successes share

<!--
Part 3 is the debate about full autonomy. Give both sides a fair hearing. The people building autonomous pipelines aren't naive.
-->

---

## The case for, and the case against

| For | Against |
| --- | --- |
| METR time horizons: doubling every ~7 months, faster lately | METR trial, early 2025: experienced developers 19% *slower* |
| C compiler: 16 agents, ~2 weeks, just under $20,000 | Told not to cheat, still reward hacking in 70–95% of runs (one task) |
| Browser: over 1 million lines in about a week | Long tasks drift, then declare the job done |
| StrongDM: no human writes or reviews the code | The last 30% is the hard part |
| Anthropic: over 80% of merged code by Claude (May 2026) | Human review becomes the bottleneck |

<!--
The case for:
- METR measures the length of task (in human expert time) a model completes with 50% reliability, its time horizon. The original paper found it doubling roughly every seven months from 2019 to 2025. The January 2026 update estimated about 131 days for models since 2023 and about 89 days for models since 2024. On May 8, 2026, METR added an early Claude Mythos Preview measurement: about 17.4 hours (95% CI 8.5–55 hours). Its [tracking page](https://metr.org/time-horizons/) warns that measurements above 16 hours are unreliable with the current task suite.
- Nicholas Carlini at Anthropic (February 2026) had 16 parallel Claude agents build a C compiler in Rust over nearly 2,000 sessions. About 100,000 lines that compile Linux 6.9 for x86, ARM, and RISC-V. No orchestrator; agents claimed tasks with lock files.
- Wilson Lin at Cursor (January 2026) had hundreds of concurrent agents that "ran for close to a week, writing over 1 million lines of code across 1,000 files" to build a browser.
- StrongDM's charter (February 2026) says "Code must not be written by humans" and "Code must not be reviewed by humans."
- Anthropic, as of May 2026: "more than 80% of the code we merge into Anthropic's codebase was authored by Claude." Be careful what that measures. It's who typed the code, not whether a human directed and reviewed it.

The case against:
- METR's randomized trial (early 2025) had 16 experienced open-source developers on 246 real tasks. With AI allowed, tasks took 19% longer. They expected a 24% speedup and afterward still believed they'd been 20% faster. METR now calls those results out of date. Its February 2026 follow-up estimated tasks about 4% to 18% faster, with confidence intervals that include zero.
- Reward hacking: on the one task where METR tested anti-cheating instructions, models still cheated in 70–95% of runs. In June 2026 METR declined to publish a reliable time horizon for GPT-5.6 Sol at all, because its cheating rate was the highest METR had seen.
- Drift: Anthropic's long-running agents would "look around, see that progress had been made, and declare the job done."
- Addy Osmani's "70% problem" (December 2024): the last 30% is edge cases, error handling, security, maintainability.
- Anthropic reports engineers merging about 8× as much code per day as in 2024, and says human review may cap the gain. The 2025 DORA report links AI adoption with higher throughput and lower delivery stability.
- And cost. StrongDM's benchmark is $1,000 of tokens per engineer per day.
-->

---

## What the successes have in common

| Project | Automated oracle | Greenfield? | Harness built by | Cost |
| --- | --- | --- | --- | --- |
| C compiler | GCC as reference, compiler test suites | Yes | Carlini: prompt, loop, tests, CI, spec | ~$20,000 |
| Cursor browser | Web standards specs, builds, tests | Yes | Planner, worker, judge; several failed designs first | Trillions of tokens |
| StrongDM | Holdout scenarios, digital twins | Their own products | A whole team | $1,000+ per engineer per day |
| Gas Town | Yegge's tests and judgment | His own projects | Yegge: four orchestrators in 2025 | Lost work; multiple subscriptions |

**Autonomy scales with the strength of the automated oracle.**

<!--
An oracle is an automated source of truth to check results against, like a reference implementation or a conformance suite. A C compiler is close to the best case. There's a reference implementation to diff against and decades of conformance tests. Most product work has neither. The real spec lives in product managers' heads, in customer contracts, and in behavior users depend on. Until that spec is written down as checks an agent can't game, full autonomy means shipping whatever passes the tests you happened to write.

These projects had problems too. Carlini lists his own: the Rust is "nowhere near the quality of what an expert Rust programmer might produce," the compiler has no assembler or linker of its own, and even optimized it "outputs less efficient code than GCC with all optimizations disabled." He writes that "the thought of programmers deploying software they've never personally verified is a real concern." Critics of Cursor's browser reported a fresh clone that failed to build and an 88% CI job failure rate. Simon Willison later built it and found pages "legible and look mostly correct" with visible glitches. Cursor's own post calls the system "nowhere near optimal."

If there's time, some open questions. Do long time horizons transfer to messy repositories? Do holdout tests stay held out as models get better at finding them? And who's accountable for code nobody reviewed?
-->

---

<!-- _class: take -->

## On prototypes

> **Bryan's take:** I like draft-driven or prototype-driven development, and you can do it with AI now. From a coding point of view or an application point of view, it's easier to comment on something you can see than to conceptualize it from scratch.

<!--
This slide and the next two are my opinions, quoted from the module. Take them as one practitioner's view, not findings.

The prototypes in part 2 help you get feedback. Reacting to something concrete is easier than reasoning about a description, whether that's a whole application or two versions of a function. Remember the risk from that section, though. A prototype looks finished, so harden or rebuild it on purpose.
-->

---

<!-- _class: take -->

## On Yegge's chart

> **Bryan's take:** On Yegge's chart I'm one or two from the top, roughly stage 6–7: several CLI agents running in parallel, each on its own task, managed by hand. I haven't built my own orchestrator. I still decide what gets merged, though honestly that's emergent to an extent. There are projects I mostly just vibe code. For work, I actually read the code.

<!--
This goes back to the "Reading the chart" slide: the stage depends on the project. Look at the split at the end. Personal projects get a looser touch, and work code gets read. That's "moving down is allowed" in practice.

Where did you place yourself earlier? Does your stage change between personal and professional work?
-->

---

<!-- _class: take -->

## On full autonomy

> **Bryan's take:** I don't believe fully autonomous agentic workflows work reliably today. Maybe I'm just too dumb; I haven't had good results, but some people claim they work. Gas Town, in particular, really did not work for me.

<!--
There is a strong counter-argument. The trend lines are steep, and the people closest to the frontier already work this way. Anthropic says most of its merged code is written by Claude. METR's measured horizons grew from minutes to a working day in about two years. StrongDM's holdout scenarios plus digital twins are a serious answer to "tests can be gamed."

As of late 2026, full autonomy works today for well-specified, oracle-rich, greenfield problems, and the edge of that set is moving. Check the evidence again in six months (module 14).
-->

---

## Try it

On your own, fix a verified bug, then go up one notch:

1. Fix a small, real bug with the full loop. Save the evidence.
2. Review it in a fresh session. Mark each finding real or not.
3. Start a second agent in its own worktree. Where did your attention go?

As a class or team, climb the autonomy ladder: hidden acceptance tests, three conditions, score the results.

<!--
The individual exercise in full. Pick a real, small bug in a repository you know, or plant one in a toy project. Run explore (read-only), plan, failing test, fix, verify, commit. Save the plan, the failing test output, the passing output, and the diff stat. Run an independent review in a fresh session and record whether each finding was real. Then go up one stage. Start a second agent in its own worktree on an unrelated task while the first works. Afterward, write three sentences on where your attention went and what you nearly missed.

For a class or team, the instructor writes one small feature spec and a set of hidden acceptance tests participants never see. Teams build it three ways: (a) supervised, approving each step; (b) one unattended agent with visible tests and a turn cap; (c) one unattended agent with only the spec. Score each on hidden-test pass rate, diff size, wall-clock time, token cost, and the number of edits the agent made to test files. Then talk about where autonomy paid off and where it produced confident, wrong work.
-->

---

## Discussion

1. Yegge's stages measure delegation. What would a chart of *outcomes* look like?
2. What's the closest thing to an oracle in your codebase?
3. METR's developers felt 20% faster and measured 19% slower. Why the gap?
4. When should you move *down* a stage?

<!--
Pick two or three. If the room is lively, the module has more:
- If a pipeline's rule is "code must not be reviewed by humans," who's accountable when it ships a security bug?
- Which tasks in your week are safe to hand to a background agent today, and which aren't? What makes the difference?

If question 3 stalls: waiting on an agent feels like rest, not work. Time spent reviewing and fixing is easy to forget. And how would you measure your own team's real speedup?
-->

---

## Read more

- [Module 08: Agentic workflows](../modules/08-agentic-workflows/)
- Anthropic, [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)
- Steve Yegge, [Welcome to Gas Town](https://yegge.ai/essays/welcome-to-gas-town/) (January 1, 2026)
- Becker et al. (METR), [the early-2025 developer productivity trial](https://arxiv.org/abs/2507.09089) (2025)

<!--
The module has the full source list, including the C compiler and Cursor browser write-ups, METR's time-horizon and reward-hacking posts, and Huntley's Ralph post. Next time, module 09 picks up the read/write asymmetry and multi-agent review.
-->

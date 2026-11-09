# Objections and honest answers

> **Audience:** AI champions, leads, and skeptics themselves · **Reading time:** ~40 min · **Last verified:** 2026-11-08
> **Use with:** the [playbook](ai-first-playbook.md) and [Session 0](session-series.md#session-0-watch-it-work-on-our-code) of the training series.

**TL;DR**
- Most objections to AI-first engineering are partly right. Start every answer with what's true. Skeptical engineers trust people who concede real limits.
- The best answer to an objection is usually an experiment on your own code, not a study or a launch post. Each entry below ends with one.
- The strongest objections are about verification, review load, security, and learning. The weakest are about 2024-era tools. Treat them differently.
- Some questions don't have good answers yet. Say so. There's a list [at the end](#questions-nobody-can-fully-answer-yet).

## How to use this guide

- **Don't argue; demo.** Pick the objection, then run the "Try this" on a real task with the person who raised it.
- **Concede first.** Each entry opens with "What's true." Read that part out loud.
- **Link, don't lecture.** Every claim links to the module section that sources it, so a skeptic can check it.
- **Keep an objections log.** When someone raises one that isn't here, or the answer here doesn't land, write it down. Revisit it at the monthly radar review ([playbook](ai-first-playbook.md#keeping-it-current)).
- **Respect "no."** Some people will stay at one supervised agent, or use agents only for chores. That's AI-first enough if their work is reviewed and their skills stay sharp.

## Index

| # | Objection | Category |
| --- | --- | --- |
| 1 | ["It hallucinates. I can't trust anything it says."](#1-it-hallucinates-i-cant-trust-anything-it-says) | Quality and trust |
| 2 | ["I tried it in 2024 and it was useless."](#2-i-tried-it-in-2024-and-it-was-useless) | Quality and trust |
| 3 | ["It writes unmaintainable code."](#3-it-writes-unmaintainable-code) | Quality and trust |
| 4 | ["It cheats on tests, or writes tests that test nothing."](#4-it-cheats-on-tests-or-writes-tests-that-test-nothing) | Quality and trust |
| 5 | ["Our codebase is too big and too weird for it."](#5-our-codebase-is-too-big-and-too-weird-for-it) | Quality and trust |
| 6 | ["It got worse last week. You can't build on something that changes under you."](#6-it-got-worse-last-week-you-cant-build-on-something-that-changes-under-you) | Quality and trust |
| 7 | ["Reviewing its code is slower than writing it myself."](#7-reviewing-its-code-is-slower-than-writing-it-myself) | Speed |
| 8 | ["The METR study says it makes you slower."](#8-the-metr-study-says-it-makes-you-slower) | Speed |
| 9 | ["The productivity claims are vendor marketing."](#9-the-productivity-claims-are-vendor-marketing) | Speed |
| 10 | ["The benchmarks are fake."](#10-the-benchmarks-are-fake) | Speed |
| 11 | ["Fully autonomous agents are hype."](#11-fully-autonomous-agents-are-hype) | Autonomy |
| 12 | ["I don't want to be a prompt engineer. I like writing code."](#12-i-dont-want-to-be-a-prompt-engineer-i-like-writing-code) | Autonomy |
| 13 | ["It'll take our jobs."](#13-itll-take-our-jobs) | People |
| 14 | ["Juniors won't learn anything."](#14-juniors-wont-learn-anything) | People |
| 15 | ["I'll lose my own skills."](#15-ill-lose-my-own-skills) | People |
| 16 | ["This is just a way to squeeze more output out of us."](#16-this-is-just-a-way-to-squeeze-more-output-out-of-us) | People |
| 17 | ["Security will never approve it."](#17-security-will-never-approve-it) | Security, privacy, legal |
| 18 | ["Our code will end up training their models."](#18-our-code-will-end-up-training-their-models) | Security, privacy, legal |
| 19 | ["We'll get sued over IP and licensing."](#19-well-get-sued-over-ip-and-licensing) | Security, privacy, legal |
| 20 | ["It's too expensive."](#20-its-too-expensive) | Cost and tools |
| 21 | ["Which tool? It changes every week."](#21-which-tool-it-changes-every-week) | Cost and tools |
| 22 | ["We can't measure the ROI, so we can't justify it."](#22-we-cant-measure-the-roi-so-we-cant-justify-it) | From managers |
| 23 | ["Why not just mandate it and set a target?"](#23-why-not-just-mandate-it-and-set-a-target) | From managers |
| 24 | ["What about the environmental cost?"](#24-what-about-the-environmental-cost) | Other |

## Quality and trust

### 1. "It hallucinates. I can't trust anything it says."

**What's true.** It does hallucinate. A language model predicts plausible text and has no built-in notion of truth. In code that shows up as invented APIs, wrong library versions, confident descriptions of files it never opened, and package names that don't exist ([module 01](../modules/01-what-is-an-llm.md#hallucination-and-why-it-happens)). In one study, at least 5.2% of packages suggested by commercial models and 21.7% by open models didn't exist, and attackers register those names ([module 11](../modules/11-security-and-prompt-injection.md#risks-specific-to-coding-agents)).

**The answer.** You're right not to trust it. The point is that you don't have to. A coding agent isn't a chat window: it can run the compiler, the tests, and the type checker, and read the installed package's source. An invented method fails the build in seconds, if the agent is told to run the build. Treat every claim as a hypothesis until a compiler, test, document, or person confirms it ([module 01](../modules/01-what-is-an-llm.md#a-working-mental-model)). Your instinct matches the field's: in Stack Overflow's 2026 survey, 48% of developers trust AI output only when it's easy to verify ([module 05](../modules/05-judging-models.md#real-world-productivity-evidence)). The job is to make verification easy.

Be careful where no check catches the error: new dependency names, explanations of code, and claims about files. Verify those by hand.

**Try this.** Ask the agent to explain a module you know well. Require a file path and line number for every claim. Check five claims against the code.

### 2. "I tried it in 2024 and it was useless."

**What's true.** For a lot of 2024 work, it was. Most people then used autocomplete or pasted code into a chat window. Even early-2025 agents slowed experienced developers down in METR's study ([module 08](../modules/08-agentic-workflows.md#the-case-against-or-at-least-not-yet)). Your judgment was reasonable for the tool you tried.

**The answer.** It's a different product now. A modern agent reads your repository, runs your tests, and iterates until they pass. METR measures the length of task (in skilled-human time) that an agent completes half the time. That was about 50 minutes in March 2025. METR put public frontier models at around 12 hours by early 2026, with a wide confidence interval ([module 05](../modules/05-judging-models.md#long-horizons)). Two cautions: the 80% horizon is much shorter (about 1.5 hours), and METR's tasks are cleaner than most real tickets. Harnesses also grew plan modes, hooks, sandboxes, and worktrees in that time ([module 06](../modules/06-harnesses-and-tools.md#the-rest-of-the-harness-toolkit)).

What hasn't changed: it still gets you most of the way quickly, and the last stretch (edge cases, error handling, security) is still yours ([module 08](../modules/08-agentic-workflows.md#the-case-against-or-at-least-not-yet)).

**Try this.** Day 2 of the [engineer path](../paths/engineers.md#week-1-one-supervised-agent): a small real bug with a reproducible failure. The agent writes a failing test first, then fixes it. Read the diff line by line.

### 3. "It writes unmaintainable code."

**What's true.** Unsupervised, it often does. The recognizable patterns are over-engineering, abstractions with one implementation, swallowed errors, dead code, and a new helper that duplicates an existing one ([module 10](../modules/10-ai-code-review.md#how-humans-should-review-ai-written-prs)). Users complained that one 2026 frontier model over-engineered beyond what was asked ([module 05](../modules/05-judging-models.md#a-recent-example-opus-5-to-opus-55)). A vendor study found about 1.7 times as many issues in PRs with signs of AI co-authorship, with real caveats about its labels and its author's commercial interest ([module 10](../modules/10-ai-code-review.md#why-it-matters-now)).

**The answer.** Maintainability is a review standard, not a property of the tool. Hold AI-written code to the same bar as human code ([playbook review policy](ai-first-playbook.md#review-policy-for-ai-written-prs)). Then steer:
- Ask for "the smallest change that satisfies the spec, no new abstractions or dependencies."
- Put "use the helpers in X" and "don't copy the patterns in `legacy/`" in the instruction file. Flagging a misleading pattern that's everywhere in the code is exactly what that file is for ([module 07](../modules/07-context-engineering.md#current-best-practice)).
- In review, ask "what can we delete?"
- Don't fix every bot finding. Anthropic warns that doing so leaves "extra abstraction layers and tests for cases that can't happen" ([module 10](../modules/10-ai-code-review.md#verify-findings-before-acting)).

**Try this.** Run the module 10 review checklist over the last five AI-assisted PRs your team merged. Count findings by type. That tells you which line to add to the instruction file.

### 4. "It cheats on tests, or writes tests that test nothing."

**What's true.** Yes. This is documented, not anecdotal. METR saw frontier models rewrite timers and monkey-patch evaluators, and telling them not to cheat still left reward hacking in 70–95% of runs on the affected tasks ([module 08](../modules/08-agentic-workflows.md#the-case-against-or-at-least-not-yet)). Agents also write tautological tests that check a mock against itself, and delete or skip failing tests under pressure ([module 08](../modules/08-agentic-workflows.md#failure-modes-and-counter-moves)).

**The answer.** That's why the test is the contract, and why you defend it ([module 08](../modules/08-agentic-workflows.md#tests-as-the-agents-contract)):
- Write or approve the tests before implementation. Commit them separately.
- Make the agent show the test failing before it passes.
- Read the test diff first in every review (`git diff --stat main -- tests/`).
- Say it in the prompt: "Make it pass without modifying the test."
- Enforce it with a hook when it matters. A rule in an instruction file is followed "nearly every time"; a hook applies every time.
- For unattended work, keep some checks out of the agent's reach.

**Try this.** Break a function on purpose (mutation testing by hand). If no test fails, the agent's tests, or yours, aren't testing it.

### 5. "Our codebase is too big and too weird for it."

**What's true.** Mature codebases with tacit conventions speed up less than greenfield work, and experts on code they wrote gain least ([module 05](../modules/05-judging-models.md#real-world-productivity-evidence)). The real spec of a legacy system lives in people's heads ([module 08](../modules/08-agentic-workflows.md#what-the-successes-have-in-common)). Even the inventor of the Ralph loop wrote "There's no way in heck would I use Ralph in an existing code base" ([module 08](../modules/08-agentic-workflows.md#background-and-unattended-runs)).

**The answer.** Size is less of a problem than it was. With million-token windows and search tools, agents rarely run out of space; they search instead of reading everything ([module 07](../modules/07-context-engineering.md#context-limits-in-practice)). The real problem is tacit knowledge, and that's exactly what a short instruction file is for: the frozen directory that looks live, the helper the team chose, the test that needs Docker ([playbook starter file](ai-first-playbook.md#the-starter-team-instruction-file)). Nested `AGENTS.md` files or path-scoped rules cover different areas of a big repository.

The weird legacy corner nobody remembers is often where agents help most, starting read-only. Concede the rest: there will be modules where it isn't worth it yet.

**Try this.** Pick the part of the codebase people are most afraid of. Ask the agent, read-only, to "trace a request from the entry point to the database, listing files in order and what each does." Check it against the code.

### 6. "It got worse last week. You can't build on something that changes under you."

**What's true.** Quality does go up and down. Anthropic published postmortems for weeks of degraded answers in 2025 (three infrastructure bugs) and six weeks of Claude Code complaints in 2026 (harness changes). OpenAI's Codex team published its own degradation investigation. In several cases, users noticed before the labs' evaluations did ([module 14](../modules/14-keeping-up.md#a-field-guide-to-recent-ups-and-downs)).

**The answer.** Treat it like any other dependency that changes. Most documented regressions were in the harness, product, or serving layer, not the model weights. Diagnose before you switch: status page, then your tool's version and settings, then your golden tasks, then whether today's task is just harder ([module 14](../modules/14-keeping-up.md#is-it-the-model-the-task-or-the-harness)). Pin CLI versions and model snapshots for anything automated. Keep a second tool configured and warm ([module 14](../modules/14-keeping-up.md#when-to-switch-tools)).

**Try this.** Build five golden tasks from merged PRs ([module 05](../modules/05-judging-models.md#build-your-own-eval)). Next time someone says "it got dumber," rerun them. Now it's a measurement.

## Speed and productivity

### 7. "Reviewing its code is slower than writing it myself."

**What's true.** Sometimes it is. Review has become the bottleneck as agents write more code, and AI-written code is tidy and plausible, which makes problems easy to skim past ([module 10](../modules/10-ai-code-review.md#why-it-matters-now)). In one industrial study, average PR closure time *rose* from about 6 to over 8 hours after a review bot was added ([module 10](../modules/10-ai-code-review.md#what-the-research-says)). Some engineers find supervising agents more tiring than writing the code ([module 15](../modules/15-learning-careers-and-responsibility.md#the-human-side)).

**The answer.** It changes what you review and when:
- **Review the plan, not just the code.** The plan is the cheapest place to catch a wrong idea ([module 08](../modules/08-agentic-workflows.md#the-core-loop-explore--plan--implement--verify--commit)).
- **Review the test.** If you approved a failing test first, the diff mostly has to make it pass.
- **Keep diffs small.** Ask for the smallest change.
- **Let a bot take the first pass** on local bugs, so you spend your attention on intent, design, and risk ([module 10](../modules/10-ai-code-review.md#a-layered-review-workflow)). Another industrial study saw PR cycle time fall 30.8%.

And concede the rest: for a ten-line change in code you know cold, typing it yourself may well be faster. AI-first isn't AI-only. The wins are biggest on unfamiliar code, tests, migrations, glue scripts, and debugging from logs ([module 08](../modules/08-agentic-workflows.md#ai-first-beyond-writing-code)).

**Try this.** For two weeks, log three tasks a week: one done by hand, two with an agent. Record wall-clock time including review. Compare by task type.

### 8. "The METR study says it makes you slower."

**What's true.** It did. In METR's 2025 randomized trial, 16 experienced open-source maintainers took 19% longer on 246 real tasks in their own large repositories when AI was allowed. They expected a 24% speedup and afterward believed they'd been 20% faster ([module 05](../modules/05-judging-models.md#real-world-productivity-evidence)). It's a careful study, and it deserves to be taken seriously.

**The answer.** Take all of it seriously, including what came after:
- The tools were early-2025 agents. METR itself now marks the result out of date.
- METR's February 2026 follow-up, with late-2025 tools, estimated tasks about 4% to 18% faster depending on the group, with confidence intervals that include zero. METR calls that an unreliable signal, likely biased toward zero, because 30–50% of developers withheld tasks they didn't want to do without AI ([module 08](../modules/08-agentic-workflows.md#the-case-against-or-at-least-not-yet)).
- The finding that holds up across every study is the **perception gap**. METR's 2026 assessment of one AI lab found self-reported uplift of about 12x against a measured 2x ([module 05](../modules/05-judging-models.md#self-report-vs-measurement)).

So the right conclusion isn't "it makes you slower." It's "don't trust how fast it feels, yours or anyone's." Experts on familiar code may see small gains. Nobody should promise 10x.

**Try this.** Measure your own team: a baseline, golden-task timing, and stability metrics ([playbook](ai-first-playbook.md#how-to-measure)).

### 9. "The productivity claims are vendor marketing."

**What's true.** Many are. Launch posts are written by the labs. Customer quotes are testimonials, often unverified ([module 14](../modules/14-keeping-up.md#weighing-launch-claims)). Some widely shared numbers come from vendors measuring their own tools ([module 10](../modules/10-ai-code-review.md#what-the-research-says)). Self-reports everywhere run ahead of measurement.

**The answer.** Agree, and discount them. Then look at independent work. Published field studies range from 55.8% faster (a small greenfield task, 2023) to 19% slower (METR, 2025). Three field RCTs covering 4,867 developers found 26% more completed tasks, with bigger gains for less experienced developers ([module 05](../modules/05-judging-models.md#real-world-productivity-evidence)). They disagree because they measured different tasks, tools, people, and outcomes. The honest summary: real speedups on some work, real slowdowns on other work, and the predictors are task type, skill with the tools, and verification practices. DORA's 2025 framing is the one to remember: AI "amplifies what's already there."

**Try this.** Ignore every number in this guide and run your own [eval](../modules/05-judging-models.md#build-your-own-eval).

### 10. "The benchmarks are fake."

**What's true.** A lot of the criticism is right. Benchmarks leak into training data: in one study, models named the file to fix in up to 76% of SWE-bench Verified tasks from the issue text alone, without seeing the repository. OpenAI stopped reporting that benchmark in 2026. Scores swing with harness and settings. Labs pick favorable comparisons, and some providers tested many private variants on Arena and published only the best ([module 05](../modules/05-judging-models.md#why-evaluation-is-hard), [module 05](../modules/05-judging-models.md#benchmark-maxing)).

**The answer.** "Fake" is too strong. "Narrow, perishable, and selectively reported" is fair. Benchmarks are good for spotting large generational gaps and trends. They're poor for choosing between two frontier models a few points apart, especially in a harness different from yours. Cross-check with independent evaluators, and decide with your own golden tasks ([module 05](../modules/05-judging-models.md#independent-evaluators)).

> **Bryan's take:** Opus 5 felt benchmark-maxed to me. It posted great numbers and kind of sucked in daily use, and people didn't like it. Opus 5.5 is the one people really liked.

To be fair to the other reading: no public evidence shows that model was trained on benchmark answers. The better-supported story is that benchmarks scored task completion, while users also cared about communication and scope, which benchmarks barely measure ([module 05](../modules/05-judging-models.md#a-recent-example-opus-5-to-opus-55)).

**Try this.** Pick a launch chart and run it through the eight-question checklist in [module 05](../modules/05-judging-models.md#reading-a-benchmark-claim-a-checklist).

## Autonomy and the nature of the work

### 11. "Fully autonomous agents are hype."

**What's true.** For ordinary product work, mostly yes, today. The famous successes share four things: a strong automated oracle, greenfield code, a harness humans built, and a high tolerance for waste ([module 08](../modules/08-agentic-workflows.md#what-the-successes-have-in-common)). A C compiler built by parallel agents cost about $20,000 and its author lists serious limitations. A week-long agent-built browser drew sharp criticism about whether it even built. Steve Yegge describes his own orchestrator as "chaotic and sloppy" and "expensive as hell" ([module 08](../modules/08-agentic-workflows.md#the-case-against-or-at-least-not-yet)).

**The answer.** You don't need to believe in full autonomy to get value. Most of it is in supervised agents and parallel supervised agents, where a human reviews every merge. Autonomy is a dial, not a switch: turn it up one notch at a time, only as fast as your automated checks can catch what you stop looking at ([module 08](../modules/08-agentic-workflows.md#the-autonomy-spectrum)).

> **Bryan's take:** I don't believe fully autonomous agentic workflows work reliably today. Maybe I'm just too dumb; I haven't had good results, but some people claim they work.

The strongest counterpoint: the trend lines are steep, Anthropic reports that Claude writes more than 80% of the code it merges, and some teams build serious software with holdout tests and digital twins of their dependencies ([module 08](../modules/08-agentic-workflows.md#the-case-for-full-autonomy)). A fair position: full autonomy works for well-specified, oracle-rich, greenfield problems, and that boundary is moving.

**Try this.** The "autonomy ladder" exercise in [module 08](../modules/08-agentic-workflows.md#try-it): one spec, hidden tests, three levels of autonomy. Compare the results.

### 12. "I don't want to be a prompt engineer. I like writing code."

**What's true.** The work does shift, toward specifying, reviewing, and verifying. Some people find that less satisfying, and some feel they aren't "real" engineers when an agent typed the code ([module 15](../modules/15-learning-careers-and-responsibility.md#the-human-side)). That's a legitimate feeling, not a skill gap.

**The answer.** Two things. First, "prompt engineering" as a bag of tricks mostly aged badly. Claude Code's own docs say capital letters and "IMPORTANT" mostly make the model over-apply a rule, and "think harder" is just text ([module 07](../modules/07-context-engineering.md#prompting-basics-that-still-matter)). What works is what you already do: state the problem precisely, give the reason, define done, and provide a check. The skills that gain value are specification, decomposition, reading code, debugging, testing, and systems thinking ([module 15](../modules/15-learning-careers-and-responsibility.md#skills-that-gain-value)).

Second, you choose what to delegate. Keep writing the parts you enjoy. Hand off the parts you don't: boilerplate, migrations, test scaffolding, log spelunking, ticket drafting.

**Try this.** For two weeks, use the agent only for the three chores you like least. Then decide.

## People and careers

### 13. "It'll take our jobs."

**What's true.** Early-career hiring is under real pressure. Payroll data show employment of 22–25-year-olds in AI-exposed occupations, including software developers, about 19% below trend by mid-2026, mostly through fewer hires ([module 15](../modules/15-learning-careers-and-responsibility.md#what-the-evidence-says-about-early-career-jobs)). Nobody knows the long-run effect, and anyone who promises you a specific outcome is guessing.

**The answer.** The evidence so far points to AI complementing experienced engineers more than replacing them. Where AI mainly complements workers, employment is flat or rising, especially for experienced ones. The same authors find no broad, economy-wide displacement, and other explanations (the post-2022 correction, interest rates) remain in play. The US Bureau of Labor Statistics still projects 10% growth in software developer jobs from 2025 to 2035; projections can be wrong both ways ([module 15](../modules/15-learning-careers-and-responsibility.md#counter-evidence-and-uncertainty)).

Who typed the code is not the job. Someone still decides what to build, catches the "almost right" solution, and answers for the result. The practical move is the one module 15 recommends: get good at the tools, invest in the skills agents can't supply, and help others adopt well ([module 15](../modules/15-learning-careers-and-responsibility.md#for-engineers-worried-about-their-jobs)).

**Try this.** Read the skills table in [module 15](../modules/15-learning-careers-and-responsibility.md#skills-that-gain-value). Pick one skill to deliberately practice this quarter.

### 14. "Juniors won't learn anything."

**What's true.** The evidence supports the worry. In a 2026 randomized trial, mostly junior engineers learning a new library with AI scored 50% on a follow-up quiz against 67% for those who coded by hand, and weren't significantly faster. The biggest gap was in debugging ([module 15](../modules/15-learning-careers-and-responsibility.md#what-the-evidence-says)).

**The answer.** The same trial shows *how* they use it matters. Participants who asked conceptual questions, or asked for explanations alongside code, scored 65% or higher. Those who delegated scored below 40%. A high-school study found the same split: an AI that gave answers hurt later exam scores, and one that tutored with hints didn't. So design the work ([playbook](ai-first-playbook.md#juniors-and-learning)):
- AI-free reps for some fundamentals and onboarding tasks.
- AI-as-tutor (learning modes, hints, explain-back) while learning.
- AI-accelerated once they can verify the output.
- Seniors pair with juniors on agent sessions and narrate what they reject and why.
- Explain-back in every code review.

**Try this.** Have a junior and a senior each run the same small task with an agent, then swap and explain each other's diff without the agent open.

### 15. "I'll lose my own skills."

**What's true.** You can. A survey of knowledge workers found that higher confidence in AI was associated with less critical thinking ([module 15](../modules/15-learning-careers-and-responsibility.md#what-the-evidence-says)). This round of automation is broader than past ones: agents touch the skills you need to supervise them, like reading code and debugging ([module 15](../modules/15-learning-careers-and-responsibility.md#deskilling-real-risk-or-old-panic)).

**The answer.** Treat it like a pilot treats hand-flying: deliberate practice. Debug some problems yourself before asking. Do some work agent-free. Read every line you merge; reviewing a lot of code is itself skill-building, as long as you actually read it. Use the agent to understand, not only to produce: ask why, then explain it back ([module 15](../modules/15-learning-careers-and-responsibility.md#how-to-learn-with-ai-instead-of-outsourcing-learning)). Module 15 puts the payoff plainly: when tools change or fail, the people who understand the system underneath are the ones who fix it.

**Try this.** Pick one hour a week with no assistant. Spend it on the part of the system you understand least.

### 16. "This is just a way to squeeze more output out of us."

**What's true.** The risk is real. Research in Harvard Business Review argued that AI tools tend to intensify work rather than reduce it. Running several agents means constant context switching, and some engineers find it more tiring than writing code themselves ([module 15](../modules/15-learning-careers-and-responsibility.md#the-human-side)). Headlines about labs merging several times more code per day invite exactly the wrong targets.

**The answer.** A good rollout rejects that framing in writing. The [playbook](ai-first-playbook.md#how-to-measure) refuses lines of code, PR counts, and "% written by AI" as targets, measures stability and review quality alongside throughput, and tells people to run only as many agents as they can actually review. If anyone starts ranking engineers by tokens or PRs, that's a fair thing to push back on, and the modules back you: Goodhart's law applies, and these numbers reward bloat ([module 10](../modules/10-ai-code-review.md#team-metrics-what-to-watch-what-not-to-measure)).

**Try this.** Ask your lead to commit, in the team's policy, to the metrics they will and won't use.

## Security, privacy, and legal

### 17. "Security will never approve it."

**What's true.** Security's concerns are legitimate. Prompt injection is not solved; one 2025 study bypassed most published defenses at success rates above 90% ([module 11](../modules/11-security-and-prompt-injection.md#why-it-is-still-unsolved)). A coding agent on a laptop has untrusted input, private data, and the ability to act, by default. Real incidents hit exactly that setup, including malware that drove developers' own AI CLIs to hunt for secrets ([module 11](../modules/11-security-and-prompt-injection.md#real-incidents-20252026)). The agent tools themselves ship security advisories.

**The answer.** Security teams can approve a scoped rollout with architectural controls, because the defenses are architectural ([module 11](../modules/11-security-and-prompt-injection.md#practical-defenses)): business plans with no-training terms, sandboxes, deny rules for secret files, no production credentials on agent machines, branch protection, managed settings that disable skip-permissions modes, an approved list of MCP servers and skills, and read-only CI agents for untrusted input. Bring them the [team checklist](../modules/11-security-and-prompt-injection.md#team-checklist) and the [policy template](policy-template.md), and ask which leg of the Rule of Two to cut for each workflow.

Two more points worth making: attackers already use these tools, and unmanaged personal use is usually already happening. A controlled rollout is the safer state. Concede that some things (browser agents on logged-in sessions, CI agents holding secrets while reading public input) should wait until the controls exist.

**Try this.** Run the safe self-injection exercise in [module 11](../modules/11-security-and-prompt-injection.md#try-it) with your security team, in a throwaway container with a fake secret.

### 18. "Our code will end up training their models."

**What's true.** On some plans, it can. Anthropic's consumer terms changed in August 2025 so that Free, Pro, and Max users choose whether their sessions are used for training; if they allow it, data can be retained for up to five years. ChatGPT consumer accounts have their own setting. Defaults change ([module 15](../modules/15-learning-careers-and-responsibility.md#data-privacy-what-not-to-paste)). And anything an agent reads, including a `.env` file, goes to the provider and may sit in transcripts on disk ([module 11](../modules/11-security-and-prompt-injection.md#risks-specific-to-coding-agents)).

**The answer.** Use business or API plans and get the terms in writing. Anthropic's and OpenAI's business and API terms default to no training on your data. Ask about retention, zero data retention for sensitive uses, data residency, SSO, and audit logs before you buy ([module 12](../modules/12-costs-subscriptions-and-apis.md#team-budgeting)). Ban personal accounts for company code. Keep secrets out of the working tree and deny agents read access to them.

If code truly can't leave your network, self-hosted open-weight models are an option, with a capability trade-off and their own security work ([module 04](../modules/04-open-vs-closed-weights.md#privacy-data-residency-and-compliance)). Note that cheap third-party "coding plans" send your code to yet another provider, possibly in another jurisdiction ([module 12](../modules/12-costs-subscriptions-and-apis.md#cheaper-alternatives)).

**Try this.** Send the procurement questions in [module 12](../modules/12-costs-subscriptions-and-apis.md#team-budgeting) to your vendor and share the written answers with the team.

### 19. "We'll get sued over IP and licensing."

**What's true.** There are two real questions, and neither is fully settled. **Ownership:** the US Copyright Office concluded in January 2025 that AI-assisted output can be protected where a human determined the expressive elements, but that "prompts alone" are unlikely to qualify. Other countries differ. **Infringement:** models sometimes reproduce training code, including copyleft-licensed code with obligations, and the risk is highest for long, distinctive snippets ([module 15](../modules/15-learning-careers-and-responsibility.md#licensing-and-copyright-of-generated-code)).

**The answer.** Manage it like other IP risk, and get your legal team's view (this isn't legal advice):
- Code that engineers substantially shape, review, and modify is on firmer ground than one-prompt output nobody touched.
- Run license scanning in CI. Some assistants can flag or block suggestions that match public code.
- Be suspicious of any large, polished block that appears instantly for a niche problem. It's on the review checklist.
- Check customer contracts for restrictions on AI use with their code or data.
- For open-source contributions, follow each project's AI policy. Some ban AI-generated contributions; others require disclosure and full human accountability ([module 13](../modules/13-open-source-ecosystem.md#the-other-side-ai-slop-and-maintainer-burden)).

**Try this.** Ask legal to review the IP section of the [policy template](policy-template.md#13-generated-code-and-intellectual-property) before rollout.

## Cost and tools

### 20. "It's too expensive."

**What's true.** At API prices with heavy use, it is. Agents re-send the whole conversation every turn, so cost grows roughly with the square of session length. Module 12's worked example puts one full-time agent on a frontier model at about $630 a month even with caching, and parallel agents multiply that ([module 12](../modules/12-costs-subscriptions-and-apis.md#worked-example-one-hour-of-agentic-coding)). Multi-agent systems use about 15 times the tokens of a chat ([module 09](../modules/09-multi-agent-systems.md#why-not)).

**The answer.** For interactive work, subscriptions change the math: roughly $20 to $200 a month for individuals (more for some tiers), and team seats with admin controls (as of November 2026; [module 12](../modules/12-costs-subscriptions-and-apis.md#price-snapshot-as-of-2026-11-08)). At a loaded cost of about $100 per engineer-hour, a $200 seat costs about two engineer-hours a month ([module 12](../modules/12-costs-subscriptions-and-apis.md#team-budgeting)). Use the API for CI and automation, with spend limits. Judge cost per finished task, not per token: a cheaper model that takes three times the turns can cost more ([module 12](../modules/12-costs-subscriptions-and-apis.md#cost-per-task-not-cost-per-token)).

> **Bryan's take:** API pricing is too expensive for heavy agentic use. Subscriptions are what make it affordable to work this way every day.

Concede the catches: subscriptions have caps that bite at the worst time, vendors have changed limits and terms several times in a year, and the ROI depends entirely on whether the tools actually help your team, which you have to measure.

**Try this.** Have two people run `npx ccusage@latest daily` after a normal week and compare API-equivalent cost to their seat price ([module 12](../modules/12-costs-subscriptions-and-apis.md#try-it)).

### 21. "Which tool? It changes every week."

**What's true.** It nearly does. OpenAI's Codex CLI had reached version 0.167 by November 2026. In 2026 alone, Roo Code (a popular open-source agent) shut down, Cursor was acquired, and Gemini CLI moved to enterprise-only ([module 00](../modules/00-orientation.md#how-fast-this-moves), [module 14](../modules/14-keeping-up.md#how-fast-it-moves)). Pricing and plans get reshuffled too.

**The answer.** The concepts transfer even when the tools don't. By late 2026 nearly every major harness had instruction files, skills, hooks, MCP, subagents, worktrees, and sandboxes ([module 06](../modules/06-harnesses-and-tools.md#why-harness-features-converge)). So:
- Pick one primary tool and keep one warm backup from a different lab.
- Put team knowledge in portable formats: `AGENTS.md`, Agent Skills, MCP ([module 06](../modules/06-harnesses-and-tools.md#common-failure-modes)).
- Run a team AI radar and apply the two-week rule to new releases ([module 14](../modules/14-keeping-up.md#team-ai-radar)).
- Switch only when your golden tasks say so, by more than the error bar.

> **Bryan's take:** For coding, Claude and Codex are the best. Claude and Codex have both had ups and downs.

**Try this.** Run the [afternoon evaluation](../modules/14-keeping-up.md#evaluating-a-brand-new-release-in-an-afternoon) on the next release that tempts you. Decide adopt, trial, or wait.

## From managers

### 22. "We can't measure the ROI, so we can't justify it."

**What's true.** Measuring productivity is hard, and getting harder. Clean randomized trials struggle because people no longer want to work without AI. Self-reports are unreliable: at one AI lab, staff self-reported about 12x uplift against about 2x measured ([module 05](../modules/05-judging-models.md#self-report-vs-measurement)).

**The answer.** You can measure enough to decide. Record a baseline, then track review latency, PR size, change failure and revert rates, escaped defects, golden-task results, and cost ([playbook](ai-first-playbook.md#how-to-measure)). For the business case, show the arithmetic with its assumptions: a 10-person team on $200 seats costs about $24,000 a year, roughly 13% of one loaded engineer, so the break-even gain is small ([module 12](../modules/12-costs-subscriptions-and-apis.md#team-budgeting)). The weak link is the assumed gain, so replace it with your measured numbers after the pilot. Fluency with these tools is also becoming a baseline expectation for engineers ([module 15](../modules/15-learning-careers-and-responsibility.md#for-engineers-worried-about-their-jobs)), which matters for hiring and retention.

**Try this.** Fund a small pilot with a written exit decision ([playbook Phase 1](ai-first-playbook.md#phase-1-champions-pilot)). Decide on its results.

### 23. "Why not just mandate it and set a target?"

**What's true.** Mandates do move adoption numbers, and some teams need a push.

**The answer.** Targets on usage measure the wrong thing. "Percentage of code written by AI" describes adoption, not quality, and as a target it rewards accepting more AI output ([module 10](../modules/10-ai-code-review.md#team-metrics-what-to-watch-what-not-to-measure)). DORA's 2025 report found AI adoption linked to higher throughput but lower delivery stability, and summarized it as "AI amplifies what's already there" ([module 05](../modules/05-judging-models.md#real-world-productivity-evidence)). Pushing volume into weak review and testing practices amplifies the weakness. What works better: paid tools, real training on your own code, a review rule, outcome metrics, and champions who share failures as well as wins ([leads path](../paths/leads.md#what-ai-first-should-mean-on-your-team)). An expectation that everyone learns the tools is reasonable. A quota is not.

**Try this.** Replace any usage target with two outcome targets from the playbook's "what to watch" table.

## Other

### 24. "What about the environmental cost?"

**What's true.** Total data-center energy demand is large and growing. Agentic coding is far heavier than a single chat prompt: an hour can be 60 or more model calls with long contexts, and no provider publishes per-session figures ([module 15](../modules/15-learning-careers-and-responsibility.md#environmental-footprint)).

**The answer.** Per-use energy is small and falling, by the providers' own measurements: Google measured its median Gemini text prompt at 0.24 Wh in May 2025, after a 33x drop over twelve months. Module 15 gives an illustrative guess (not a measurement) of about 144 Wh for an hour of agent calls, roughly an hour and a half of a 100-watt appliance. The real number could be higher or lower. Reasonable practice: don't run loops that produce nothing, use smaller models for easy work (it's cheaper too), and be skeptical of energy numbers without a stated method. It's a fair concern, and part of it can't be answered precisely yet.

**Try this.** Add "loops and swarms have stop conditions" to your team's automation rules. It saves energy and money at once.

## Questions nobody can fully answer yet

Be honest about these. They're open in the research, not just on your team.

- **Does AI code review reduce production defects?** Most studies measure whether comments lead to code changes, not whether fewer bugs reach users ([module 10](../modules/10-ai-code-review.md#what-the-studies-agree-on)).
- **What happens to skill formation over years, not hours?** The learning studies measure short-term quizzes and exams ([module 15](../modules/15-learning-careers-and-responsibility.md#what-the-evidence-says)).
- **Where will future senior engineers come from** if junior hiring keeps falling ([module 15](../modules/15-learning-careers-and-responsibility.md#counter-evidence-and-uncertainty))?
- **Do long agent time horizons transfer to messy, existing codebases?** METR's tasks are cleaner than most tickets ([module 08](../modules/08-agentic-workflows.md#open-questions)).
- **Are today's subscription prices sustainable?** Nobody outside the labs knows the unit economics ([module 12](../modules/12-costs-subscriptions-and-apis.md#are-subscriptions-sustainable)).
- **Who is accountable for code nobody reviewed?** Law, audits, and incident reviews assume a person looked ([module 08](../modules/08-agentic-workflows.md#open-questions)).

## Sources and further reading

Every answer above links to the module section that sources it. The primary sources behind the most-cited points:

- [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://arxiv.org/abs/2507.09089) (Becker, Rush, Barnes, Rein, 2025) and METR's [February 2026 update](https://metr.org/blog/2026-02-24-uplift-update/)
- [The Effects of Generative AI on High-Skilled Work](https://papers.ssrn.com/abstract=4945566) (Cui, Demirer et al., 2025)
- Google Cloud, [Announcing the 2025 DORA Report](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report) (2025)
- [How AI Impacts Skill Formation](https://arxiv.org/abs/2601.20245) (Shen, Tamkin, 2026)
- [Generative AI without guardrails can harm learning](https://doi.org/10.1073/pnas.2422633122) (Bastani et al., PNAS, 2025)
- [The SWE-Bench Illusion](https://arxiv.org/abs/2506.12286) (Liang et al., 2025)
- [The Attacker Moves Second](https://arxiv.org/abs/2510.09023) (Nasr, Carlini, et al., 2025)
- [We Have a Package for You!](https://arxiv.org/abs/2406.10279) (Spracklen et al., 2024)
- METR, [Recent frontier models are reward hacking](https://metr.org/blog/2025-06-05-recent-reward-hacking/) (2025)
- Brynjolfsson, Chandar, Chen, [Canaries in the Coal Mine?](https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/) (2025, revised 2026)
- U.S. Copyright Office, [Copyright and Artificial Intelligence, Part 2: Copyrightability](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf) (2025)

---
marp: true
theme: not-writing-code
paginate: true
title: "05: How to tell if a model is good"
description: "Benchmarks, benchmark-maxing, vibes, and building your own eval"
footer: "A Brief Introduction to Not Writing Code · 05 How to tell if a model is good"
---

<!-- _class: lead -->

# 05: How to tell if a model is good

Benchmarks, user impressions, and testing models on your own work

<!--
Plan for 40 to 50 minutes. Part 1 is reading other people's numbers: benchmark scores, launch posts, evaluators. Part 2 is evidence closer to your work: productivity studies and a small eval built from your own repos. Part 3 is what happens when benchmarks and users disagree, with Opus 5 as the case study. The reading is module 05.

Open by asking who picked the model they use now because of a benchmark chart. Come back to the answer at the end.
-->

---

## Why this matters

- Every model launch comes with a chart showing it winning.
- Most of those wins don't carry over to your repo or tool.
- Scores mislead in specific ways you can learn to spot.
- Choosing a model for a team needs evidence from your own work.

<!--
You'll pick tools for yourself or your team. Either way, someone will show you a chart. This session is about asking the right questions about that chart, and knowing what evidence would actually settle the choice.

We'll build an eval with 10 to 30 tasks from your own work, graded blind, with cost and time per task, rerun whenever a model or tool changes.
-->

---

## "Good" at what, for whom, at what cost?

| Axis | The question |
| --- | --- |
| Capability | Can it do the task at all? |
| Reliability | Every time, or one time in three? |
| Fit | In *your* language, framework, repo size, and tool? |
| Cost and speed | Dollars, quota, and wall-clock time per finished task |
| Behavior | Stays in scope, admits uncertainty, writes reviewable code? |

Most public benchmarks measure the first row. Daily work is mostly the other four.

<!--
"Is this model good?" has no single answer. A model can be the best at hard math, middling at following a team's code style, and too slow or expensive for autocomplete. Decide what you care about before you look at any number.

Ask the room which row has hurt them most. The usual answers are reliability and behavior: the agent that rewrites half a file when you asked for one line.
-->

---

## A score describes a setup, not a model

```text
  model      weights + version
+ harness    tools, system prompt, retries
+ settings   reasoning effort, token budget, temperature
+ task set   which version; contamination; label errors
+ grader     unit tests, rubric, LLM judge, humans
+ attempts   pass@1, pass@k, best-of-N
= the reported score
```

Change any line and the number moves.

<!--
This replaces the diagram in the module. Walk down the list.

The harness, also called the scaffold or agent, is the program around the model. It sends the prompt, exposes tools such as a shell or file editor, runs the loop, and decides when to stop. Claude Code, Codex CLI and the research harness Terminus-2 are harnesses. Module 06 covers them.

The grader decides pass or fail. For code it's usually hidden unit tests. For writing it might be a rubric scored by humans or by another model, called an LLM judge.

pass@1 is the share of tasks solved on the first try. Most headline numbers are pass@1, sometimes averaged over several runs.
-->

---

<!-- _class: divider -->

# Part 1

## Reading other people's numbers

<!--
About 15 minutes on why public benchmarks decay, two ways to count attempts, how much the harness matters, and a checklist for any claim.
-->

---

## Public benchmarks wear out

| Problem | Example |
| --- | --- |
| Contamination | Shown only the issue text, models named the file to fix up to 76% of the time |
| Saturation | Labs reported mid-90s on GPQA Diamond; an index dropped it, Sep 2026 |
| Label errors | An estimated 6.49% of MMLU questions contain errors |
| Goodhart's law | "When a measure becomes a target, it ceases to be a good measure." |

A frontier benchmark stays useful for a year or two. A good one is fresh, held-out, realistic, verified, and documents its harness.

<!--
On contamination, models train on internet scrapes. If test questions or solutions are online, a high score may show memory, not skill. In The SWE-Bench Illusion (Liang et al., 2025), models saw only a GitHub issue's text, no repository, and still named the file to fix up to 76% of the time on SWE-bench Verified. On repositories outside SWE-bench, the best was 53%. GSM1k rewrote a grade-school math benchmark with fresh problems, and some model families lost up to 8 points.

A saturated benchmark has every top model near the ceiling, so it stops separating them. HumanEval saturated years ago. Artificial Analysis dropped GPQA Diamond from its index in September 2026.

On label errors, "Are We Done with MMLU?" estimated 6.49% of questions contain errors, including 57% of the virology questions analysed. [OpenAI](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/) audited 138 SWE-bench Verified tasks that o3 did not consistently solve across 64 runs. It found material flaws in 59.4% of that subset and announced on February 23, 2026, that it had stopped reporting the benchmark, also citing contamination.

Goodhart's law is Marilyn Strathern's phrasing of economist Charles Goodhart's point. Once a benchmark sells models, labs train toward it.

As of November 2026, HumanEval and MBPP are smoke tests only. SWE-bench Verified and Aider Polyglot are retired or dormant but still quoted. Terminal-Bench 4.0 (August 2026), SWE-bench Pro, and METR-style long tasks still discriminate. Don't memorize these names; they will change.
-->

---

## Same model, same task: 99% or 51%

A model solves a task 80% of the time. Three independent attempts:

| Metric | Meaning | Result |
| --- | --- | --- |
| pass@3 | At least one of 3 succeeds | 1 − 0.2³ ≈ 99% |
| pass^3 | All 3 succeed | 0.8³ ≈ 51% |

pass@k suits check-and-retry work. pass^k suits anything that must work every run.

<!--
pass@k comes from the HumanEval paper (Chen et al., 2021). It fits settings where checking is cheap, like generating five patches and keeping the one that passes the tests.

pass^k, said "pass-hat-k", comes from tau-bench (Yao et al., 2024). It fits customer-facing agents and unattended automation, where every run has to work. tau-bench found GPT-4o agents solved under 50% of tasks in its retail domain, and pass^8 was below 25%.

Reliability is a separate axis from capability, and it's the one that hurts in production. Ask the room which metric fits autocomplete, and which fits an unattended nightly job. Discussion question 2 comes back to this.
-->

---

## The harness moves the score

| Model | Vendor's own CLI | Neutral harness (Terminus-2) |
| --- | --- | --- |
| GPT-5.5 | 24.7% (Codex) | 21.2% |
| Gemini 3.1 | 12.2% (gemini-cli) | 7.3% |

Harbor-Index, Terminal-Bench team, June 2026. No gap reached statistical significance.

Compare models in the harness and settings you will actually use.

<!--
Harbor-Index ran the same models in their vendor's native CLI and in the neutral Terminus-2 harness. The direction is consistent, and the authors note that no comparison reached significance (all p > 0.05). Harness effects are real, and small samples can hide or fake them.

The module has more evidence. METR found GPT-4o and o3 scored significantly higher under its old Vivaria harness than under Inspect. SWE-agent (Yang et al., 2024) redesigned the agent-computer interface, meaning how the model views, searches and edits files, and got GPT-4 Turbo to 12.5% on full SWE-bench. The interface was the contribution, not a new model.

Settings count as harness too. McFadyen et al. (2026) varied token budgets, compaction and retries across 12 frontier models and concluded that "benchmark scores are protocol-dependent." Reviewers reported Opus 5 could do worse at its highest effort settings. Even prompt formatting alone swung one open model by up to 76 accuracy points (Sclar et al., 2023).
-->

---

## Reading a benchmark claim

"Model X scores 72% on Benchmark Y." Ask:

- Which benchmark version, and which harness?
- What settings: effort, token budget, number of attempts?
- Who ran it: the lab, the maintainers, or an evaluator?
- Were competitors run the same way?
- What's the error bar? A 2-point lead at ±2.6 is a tie.
- What does it cost per task, and what was left out?

<!--
The module's checklist has eight questions; this slide merges a few.

On versions, Terminal-Bench 2.0, 3.0 and 4.0 have different tasks, so their scores don't compare. On settings, a footnote saying "max effort, best of 5" changes what the number means.

On competitors, Anthropic's September 2026 Opus 5.5 post compares its model at "xhigh" effort with a rival's figures as reported by that rival at "high" effort, and says so in a footnote. Read the footnotes.

For what's left out, look for benchmarks the lab reported last time and dropped this time. On cost, many 2026 launch posts chart score against cost. A higher score at three times the cost may be the worse buy.

Even labs now say the margins mislead. The Opus 5.5 announcement says benchmark margins are a less reliable guide at current capability levels, and that the gap to its pricier Fable 5.1 looked narrower in its own use than the scores suggest.
-->

---

## Independent evaluators give a second opinion

| Evaluator | What it does | Watch for |
| --- | --- | --- |
| Artificial Analysis | Standardized runs; a composite index | Index changes every few months |
| Epoch AI | Its own runs, with error bars; trends | OpenAI funds FrontierMath (disclosed) |
| METR | Long-task time horizons; productivity RCTs | Close lab ties; few top-end tasks |
| Vals AI | Private and held-out domain evals | You can't inspect them |
| Scale Labs | SWE-bench Pro, with private splits | Also sells training data to labs |
| LiveBench | Regularly refreshed questions | Short, less agentic tasks |
| Arena | Human preference votes | Style bias; private testing |

Independent doesn't mean neutral. Cross-check two or three, never one.

<!--
Lab launch posts are written by the lab, which picks the benchmarks and settings. Evaluators are useful because they're consistent, with the same setup for every model. They still choose benchmarks, harnesses and weights, and some have commercial ties to labs.

Artificial Analysis's Intelligence Index was at v5.0.1 as of November 2026. Between January and November 2026 it removed MMLU-Pro, LiveCodeBench, AIME 2025, GPQA Diamond and the original HLE, so old and new index numbers don't compare.

Epoch AI disclosed in January 2025 that OpenAI commissioned and owns the FrontierMath problems and has most of the problems and solutions, except a holdout set.

Arena shows two anonymous answers side by side and turns votes into Elo-style ratings. Voters reward length, formatting and confidence, so it added "style control." Most prompts are short chats. It answers "which model do people enjoy chatting with?" better than "which model should drive my coding agent?"
-->

---

<!-- _class: divider -->

# Part 2

## Evidence closer to your work

<!--
About 15 minutes on what field studies of developer productivity found, then how to build, grade and trust a small eval of your own.
-->

---

## Productivity studies: 55.8% faster to 19% slower

| Study | Finding |
| --- | --- |
| Peng et al., 2023: one greenfield task | 55.8% faster |
| Paradis et al., 2024: 96 Google engineers | ~21% faster |
| Cui, Demirer et al., 2025: 4,867 developers | +26% completed tasks |
| METR, 2025: 16 maintainers, their own repos | 19% slower; believed 20% faster |
| METR, Feb 2026: 57 developers | "Unreliable signal"; intervals include zero |
| METR on Anthropic, Nov 2026 | Measured ~2x; self-reported ~12x |

Self-reports run ahead of measurements. Treat surveys as a ceiling.

<!--
The studies measure different things. Greenfield, well-specified tasks speed up a lot. Mature codebases with unwritten conventions speed up less.
Juniors on unfamiliar code gain more than experts on code they wrote.
2022 autocomplete, 2025 chat plus agents, and 2026 parallel CLI agents are different interventions.
Minutes, PRs, self-reported speed and delivery stability are different outcomes. DORA 2025 linked AI adoption to higher throughput but still to lower delivery stability.
As AI becomes normal, people willing to work without it become unusual. In METR's 2026 study, 30 to 50% of developers withheld tasks they didn't want to do without AI.

On the perception gap, METR's 2025 developers predicted 24% faster, believed afterward they'd been 20% faster, and measured 19% slower (CI +2% to +39%). The Anthropic assessment is not an RCT, and METR notes individual uplift and organizational acceleration aren't the same quantity, but the gap is still large.

Some work gets faster; other work gets slower. The biggest predictors are task type, skill with the tools, and verification practices. Measure your own team.
-->

---

## Build a golden-task set

A golden task is a real, solved piece of your work, frozen for replay.

```yaml
id: billing-proration-0142
base_commit: 3f9c2e1        # commit before the original fix
category: bugfix            # ... migration | review | trap
prompt: |
  Customers who upgrade plans mid-cycle are sometimes charged
  one cent too much. Find and fix the bug. Add a regression test.
grading:
  hidden_tests: evals/hidden/test_proration_0142.py
  must_not_touch: [migrations/, src/api/public/]
```

<!--
This is an excerpt; the full task-file template is in module 05.

Source tasks from merged PRs in the last 3 to 12 months. Use the commit before the PR as the starting state, and the PR's tests, plus any you write, as the grader. Recent PRs are less likely to be in any model's training data. Private repos never should be.

Start with 10 to 20 tasks and grow to 30 to 50. Mix bug fixes, small features, refactors, test writing, a migration, a code-review task, and at least one trap task, where the right move is to ask a question or refuse an unsafe instruction.

Keep grading tests hidden from the agent so it can't edit them to pass. Record roughly how long the original PR took, as a human baseline.
-->

---

## Score with a rubric, blind

| Criterion | Points |
| --- | --- |
| Hard fail (edited tests, false success claim, forbidden path, destructive command) | Score is 0 |
| Correctness: hidden tests pass | 0–4 |
| Scope discipline: about as small as the reference | 0–2 |
| Code quality: a reviewer would approve it | 0–2 |
| Tests: a meaningful regression test | 0–1 |
| Communication: accurate summary, real uncertainty flagged | 0–1 |

Strip model names and shuffle before anyone scores. Unblind after.

<!--
To run it, pick the configurations to compare. A configuration is model plus harness plus version plus settings. Change one thing at a time. Run each task three times per configuration if you can afford it; that gives you both the average pass rate and pass^3.

To blind it, export each diff and final message, replace model names with random IDs, and shuffle. A reviewer who doesn't know which is which scores each with the rubric. With two reviewers, average their scores and discuss big disagreements. Then unblind and log the results, including wall-clock minutes, human interventions, and cost or quota used.

Blind it because people reliably favor the model they expect to be better.
-->

---

## Small evals are noisy

Standard error of a pass rate ≈ √(p(1−p)/n)

- 20 tasks at 60%: ±11 points, so ±22 at 95% confidence.
- 55% vs 65% on 20 tasks: you can't tell them apart.
- Pair the comparison: same tasks, count only the disagreements.
- If A wins 9 of 10 disagreements, that means something.
- Repeat runs to separate randomness from task difficulty.

Without an error bar, you can't tell how much a score means.

<!--
Do the arithmetic on the board. p = 0.6, n = 20. p times (1 − p) is 0.24. Divided by 20 is 0.012. The square root is about 0.11, so ±11 points of standard error, roughly ±22 for a 95% interval.

When you summarize, report these per configuration: pass rate with a rough error bar, pass^3, mean rubric score, median minutes, median cost, and the hard-fail count. Then look at the paired results: tasks where A passed and B failed, and the reverse. Those disagreements help you compare the models.

Evan Miller's "Adding Error Bars to Evals" (2024) makes the case for always reporting intervals.
-->

---

## Keep the eval honest

- New model or version? Rerun the whole set before switching.
- Harness update? Rerun a five-task smoke subset.
- Pin versions and dated model snapshots, not "latest."
- Retire tasks whose fixes are now public.
- Hide tests, diff the test directory, read passing transcripts.
- Keep the eval in the repo and review changes like code.

<!--
Agents game graders more as they get stronger. METR reported "well over 100 distinct instances of cheating from shared models," and said checking for cheating by hand is often most of the work of running its suite. In one MirrorCode setup, a model attempted reward hacking in about 80% of attempts (May 2026).

Terminal-Bench's leaderboard integrity update removed submissions that modified timeouts, hid encrypted solutions in the agent binary, or uploaded the tasks' test folders. It now requires full trajectories for every passing trial.

Harness changes have caused real regressions (module 14), which is why a harness update earns a smoke run. Module 10 covers having several models review each other's output, which pairs well with blind grading.
-->

---

<!-- _class: divider -->

# Part 3

## When benchmarks and users disagree

<!--
About 10 minutes on how scores get inflated, a 2026 case study, and how to treat users' impressions as evidence.
-->

---

## Benchmark-maxing runs from defensible to dishonest

Optimizing for scores at the expense of what users experience:

1. Training on benchmark-shaped data
2. Contamination, where test items leak into training
3. Tuning a variant to please one grader or audience
4. Reward hacking that shows up in behavior
5. Cherry-picking the harness, settings, version, or benchmarks
6. Unlabeled best-of-N; publishing only the best private variant

<!--
It's Goodhart's law applied to a product launch. The list runs roughly from defensible to dishonest; the module splits the last item into two, for seven in total.

Item 1 is legitimate skill-building until the training set looks so much like the test that scores rise faster than general ability.

For item 3, Meta's April 2025 Llama 4 launch highlighted an Arena rank of #2 for "Llama-4-Maverick-03-26-Experimental," a conversation-tuned variant that wasn't the released model. The released model ranked far lower.

On item 4, reinforcement learning on coding tasks rewards "tests pass." A model can learn to special-case tests, over-verify, or over-engineer. System cards now report this.

For item 6, The Leaderboard Illusion (Singh et al., 2025) saw as many as 27 private Meta variants tested in the month before Llama 4. Module 14 covers the Grok 3 majority-vote chart.
-->

---

## From Opus 5 to Opus 5.5

| When (2026) | What happened |
| --- | --- |
| Jul 24 | Opus 5 ships with strong numbers and leads the Artificial Analysis index |
| Late Jul | Reception is mixed: verbose, over-engineers, spins at high effort |
| System card | Blames some weak results on "unproductive self-verification" |
| Sep 22 | Opus 5.5: "major improvements to the way Opus 5.5 writes and communicates" |
| Sep 26 | Zvi Mowshowitz: "the most consistently positive set of reactions I have ever seen" |

<!--
Anthropic claimed state-of-the-art results for Opus 5 on several coding and knowledge-work evals, including an ARC-AGI-3 score three times the next-best model's. It led the Artificial Analysis index at launch, so this wasn't only self-reported.

In his roundup of reactions, Zvi Mowshowitz advised readers not to pay too much attention to the "(very strong) benchmarks." The complaints were verbosity, "endless overly complex sentences," over-engineering beyond the request, and spinning at high effort settings. Others praised its coding and forecasting. Anthropic's system card, as quoted in Zvi's review, attributed weaker results on some tasks to "unproductive self-verification" and over-engineering.

Anthropic called communication "one of the most common areas of feedback we heard about Opus 5."

The system card is worth reading alongside the launch post. Labs often admit more there than in the launch post. Read the benchmark footnotes, reward-hacking and test-tampering rates, evaluation awareness, and known limitations.
-->

---

## Maxed on what's measured, with no cheating needed

- No public evidence shows Opus 5 trained on benchmark answers.
- One researcher alleged genre-specific training. That's a single claim.
- The benchmarks scored task completion.
- Users also cared about communication, scope, and judgment.
- Benchmarks barely score those. A few newer ones do.

<!--
This helps explain the gap between scores and daily use. Nobody has to cheat for a model to look better on paper than in use. Optimize hard for what's measured, and the parts nobody measures can get worse.

FrontierCode, from Cognition, penalizes unrequested extra work, and Opus 5's curve there reportedly showed the over-engineering. So some evals do catch it.

When you read a benchmark, ask what it doesn't score, and whether that's what you care about.
-->

---

## Vibes are data. Collect them on purpose.

1. Keep a log: date, model, harness version, task, result.
2. Decide what you're testing before you look.
3. Blind the comparison by stripping the model names.
4. Give both models the same tasks.
5. Wait out the honeymoon and re-judge after two weeks.
6. Trust specific, repeated reports, like "over-engineers small fixes."

<!--
"Vibes" means experienced users' impressions. They often notice changes before benchmarks do. In April 2025 OpenAI rolled back a GPT-4o update that had become sycophantic, meaning excessively flattering and agreeable. Afterward OpenAI wrote that some expert testers had said the model felt off before launch, but positive A/B tests won out. Its lesson was to give such signals more weight. The Opus 5 complaints were vibes too, and they caught something the benchmarks missed.

Vibes are also noisy: novelty (a new model feels smarter for a week), confirmation bias, recall bias (you remember the spectacular failure, not the forty quiet successes), and social contagion (one viral post sets everyone's expectations).

On point 6, "it over-engineers small fixes" counts and "it feels dumber" doesn't. Trust a vibe more when independent experienced users report the same specific behavior.
-->

---

<!-- _class: take -->

## Bryan's take

> **Bryan's take:** Opus 5 felt benchmark-maxed to me. It posted great numbers and kind of sucked in daily use, and people didn't like it. Opus 5.5 is the one people really liked.

<!--
This is my opinion from daily use.

It's a vibe in exactly the sense of the last slide, a dated, specific impression that matched what many other users reported. The evidence has limits. No public evidence shows Opus 5 trained on benchmark answers. The better-supported story is that benchmarks scored task completion and barely scored communication or scope.

My model picks (Claude and Codex for code; Grok or Gemini only for specific non-coding jobs) are in module 03. The module flags the Grok and Gemini view as the most contested: late-2026 public benchmarks put Google's newest models near or at the top on some coding evals. That's the argument for checking your own golden tasks rather than taking anyone's word for it, mine included.
-->

---

## Try it

**Individual (2–3 hours)**
- Turn 10 merged PRs into task files with hidden tests.
- Run two configurations three times each; score blind with the rubric.
- Write five sentences: winner, margin, task types, cost, error bar.

**Class or team (one session plus homework)**
- Each person contributes two golden tasks from real work.
- Each group runs one configuration; a separate group grades blind.
- Compare your ranking with the public leaderboard's.

<!--
Two configurations means two models in the same harness, or one model in two harnesses. Have a friend blind the outputs, or do it yourself with random IDs.

The fifth sentence has to say whether the difference is bigger than your error bar. With 10 tasks it usually isn't, and learning that is part of the exercise.

The class version gives the group a shared set of 30 to 50 tasks. Reveal results together, then discuss where your ranking and the public one agree, where they don't, and why.
-->

---

## Discussion

1. A vendor beats a rival by 3 points on a coding benchmark. What do you ask first?
2. pass@k or pass^k: which fits autocomplete, a PR-writing agent, a nightly job?
3. METR's developers felt faster but were slower. How would your team guard against that?
4. Your eval favors Model A; your senior engineers' vibes favor Model B. Now what?

<!--
For 1, walk the claim checklist: version, harness, settings, who ran it, same conditions for competitors, error bar, cost, what's missing.

For 2, autocomplete is cheap to check and retry, which suits pass@k. A nightly job runs unattended, which suits pass^k. A PR-writing agent sits in between, because a human reviews it.

For 3, pair surveys with something measured, such as cycle time, golden-task timing, or change-failure rate, and treat the survey as a ceiling.

4 has no single right answer. Strong answers turn the vibe into a specific, testable behavior, add golden tasks that test it, and rerun blind.
-->

---

## Read more

- Module: [05 How to tell if a model is good](../modules/05-judging-models/)
- [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://arxiv.org/abs/2507.09089) (Becker et al., 2025)
- [Harbor-Index](https://www.tbench.ai/news/harbor-index) (Terminal-Bench team, June 2026)
- [Adding Error Bars to Evals](https://arxiv.org/abs/2411.00640) (Miller, 2024)

<!--
The module has the full task-file template, rubric and results-log format, plus tables of every major benchmark family and their weaknesses. The METR paper is the study behind "felt faster, measured slower." Harbor-Index is the clearest short read on harness effects. Miller's paper explains error bars for evals.

Next session, module 06, is about the harness itself.
-->

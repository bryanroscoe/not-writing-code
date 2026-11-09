---
marp: true
theme: not-writing-code
paginate: true
title: "09: Multiple agents"
description: "Building and reviewing with more than one agent"
footer: "A Brief Introduction to Not Writing Code · 09 Multiple agents"
---

<!-- _class: lead -->

# 09: Multiple agents

Building and reviewing with more than one agent

<!--
Today is about when several agents beat one, when they just cost more, and the one multi-agent recipe with strong support behind it, a review swarm. The reading is module 09. It builds on module 08: the agent loop, worktrees, Yegge's stages.

Tool details are as of November 2026.
-->

---

## Why this matters

- More agents means more tokens, not a smarter answer
- Reading parallelizes; writing usually doesn't
- Much "multi-agent" gain comes from sampling and voting
- Without a verification step, errors compound
- The best-supported recipe is independent reviewers, then a verifier

<!--
Multi-agent systems get marketed hard. The research gives us a way to check which setups earn their cost.

Research and review split well across agents because each agent produces claims you can check. Writing code on one codebase usually doesn't, because every edit embeds decisions that have to fit together.

Models also tend to rate their own output higher. So review with a fresh context at minimum, and with a different lab's model when it matters.
-->

---

## Four shapes of "multi-agent"

| Shape | How it works | Example |
| --- | --- | --- |
| Subagent | A main agent spawns a helper; it returns a summary | Claude Code's Explore agent; Codex subagents |
| Agent team | Peers share a task list and message each other | Claude Code agent teams (experimental, as of November 2026) |
| Separate sessions | You run several and carry information between them | One writes, another reviews |
| Orchestrated pipeline | Code, not a model, decides who runs when | A CI job that runs three review prompts |

<!--
A multi-agent system is several model instances, each with its own context window and job, coordinated by code or by another agent.

Anthropic's "Building effective agents" (Schluntz and Zhang, 2024) draws a useful line. Workflows are "systems where LLMs and tools are orchestrated through predefined code paths," while agents direct their own process and tool use. Many systems marketed as multi-agent are workflows, and that's often a good thing, because fixed paths are easier to test and debug.

The idea is old. Marvin Minsky's The Society of Mind (1986) described intelligence as many simple, specialized agents interacting, and the 2023 wave of LLM papers borrowed the framing directly.

Agent teams in Claude Code were experimental and off by default as of November 2026.
-->

---

## Four benefits, four costs

| Why use more than one | Why not |
| --- | --- |
| Parallelism: wall-clock time, not intelligence | Cost: about 15× the tokens of a chat |
| Context isolation: read 200 files, return a paragraph | Coordination fails: 14 failure modes in 1,600+ traces |
| Different perspectives: prompts, roles, models | Context lost at every hand-off |
| Independent verification: a reviewer not swayed by the author | Errors compound: 17.2× vs 4.4× with a central check |

<!--
On the benefits:
- Parallelism means finishing sooner, not thinking better.
- Context isolation keeps the noise of a full test log or 200 files out of the main conversation.
- Different prompts, roles, or models notice different things. A security reviewer finds what a correctness reviewer skips.
- For independent verification, Anthropic's docs list "Getting a reviewer that hasn't seen how the code was written" as a main reason to use subagents. The same docs caution that a subagent is by default "the same model (or a smaller one) on the same task. You get parallelism or a fresh pair of eyes out of it, but not a smarter answer."

On the costs:
- Anthropic found agents "use about 4× more tokens than chat interactions, and multi-agent systems use about 15× more tokens than chats." On the BrowseComp benchmark, token usage alone explained 80% of the variance in performance. Part of what looks like teamwork is just more compute.
- Cemri et al. (2025) analyzed more than 1,600 traces from seven frameworks and found 14 distinct failure modes.
- Walden Yan of Cognition ("Don't Build Multi-Agents"): subagents working from a summary make conflicting assumptions. His principles: "Share context, and share full agent traces, not just individual messages," and "Actions carry implicit decisions, and conflicting decisions carry bad results."
- Kim et al. (2025) looked at 260 agent configurations. Independent agents with no central check amplified errors 17.2× in their traces, against 4.4× for a centralized design with a verification step.
-->

---

## Reading parallelizes. Writing usually doesn't.

| | Read-heavy work | Write-heavy work |
| --- | --- | --- |
| Examples | Research, review, verification, competing hypotheses | Building features in one codebase |
| Each agent produces | Claims: "line 42 can divide by zero" | Edits that embed decisions |
| Combining them | Deduplicate, check, discard the wrong ones | Conflicts in git and in design |
| Two agents disagree | A minute of checking | A broken build |

<!--
This difference is called the read/write asymmetry.

Claims are cheap to merge. You deduplicate them, check them, and throw away the wrong ones.

Edits are different. Every edit embeds decisions: names, data shapes, error-handling style, where a helper lives. Yan's Flappy Bird example shows it. Split "build Flappy Bird" between two subagents, and one builds a Super Mario-style background while the other builds a bird that doesn't match the game. The final agent is stuck reconciling two incompatible halves. Parallel writers on one codebase also collide in git.
-->

---

## The evidence lines up

- Anthropic built its multi-agent system for research, not coding
- Claude Code's docs recommend teams for "research and review," not same-file edits
- In Kim et al., every multi-agent setup did slightly *worse* on SWE-bench Verified
- At Cursor, twenty agents slowed "to the effective throughput of two or three"

<!--
- Anthropic chose research because "most coding tasks involve fewer truly parallelizable tasks than research."
- Claude Code's agent-team docs recommend teams for "research and review" and "debugging with competing hypotheses," and say that "for sequential tasks, same-file edits, or work with many dependencies, a single session or subagents are more effective."
- In Kim et al.'s controlled comparison, every multi-agent architecture scored 15% to 2% worse than a single agent on SWE-bench Verified, and 39% to 70% worse on sequential planning. Gains showed up on decomposable tasks like financial analysis, up to +80.8%.
- Cursor's first large-scale attempt had agents claim work through shared locks, and throughput collapsed. A later "integrator" agent created more bottlenecks than it solved, so they dropped it.
-->

---

## When parallel writing works

On Anthropic's C compiler, many failing tests meant "parallelization is trivial."

The Linux kernel is one giant test. "Every agent would hit the same bug, fix that bug, and then overwrite each other's changes."

Compiling most files with GCC makes each failure point at a few files.

**Writing parallelizes when the oracle splits the work into pieces that don't share decisions.**

<!--
In Nicholas Carlini's C compiler project (Anthropic, February 2026), a large test suite produced many separate failures, so each agent could pick a different one.

The Linux kernel was different. It's effectively one test, so every agent chased the same bug. The fix was a harness that compiled most kernel files with GCC, a known-good compiler, and only the rest with the new one. A failure then pointed at a small set of files, and each agent could chase a different bug.

So if you want parallel writers, make the work independent first. An oracle, like a reference implementation or a test suite, is the usual way to do that.
-->

---

<!-- _class: divider -->

# Part 2: In practice

Patterns, three recipes, and budgets

<!--
In part 2, we'll look at the common patterns, three recipes to try, and how to keep the bill under control.
-->

---

## Patterns and when each helps

| Pattern | Helps when | Watch out for |
| --- | --- | --- |
| Orchestrator–workers | Subtasks can't be predicted in advance | Vague briefs: duplicated or missing work |
| Fan-out, then merge | The work splits into independent slices | Conflicts surface at the merge |
| Voting / best-of-N | Answers can be compared or tested | Costs N×; shared blind spots don't vote away |
| Generator–critic | Clear criteria exist | Critics always find *something*; cap rounds |
| Debate | Arguments can be checked | Agents cave to persuasive wrong answers |
| Judge panel | One judge's bias would skew results | Shared biases; calibrate against human labels |
| Pipeline | Steps are stable and well understood | Early errors flow downstream |

<!--
- Orchestrator–workers: a lead agent splits a task at run time, assigns pieces, and synthesizes results. Good for open-ended research and broad audits.
- Fan-out, then merge: fixed slices (per directory, per concern, per file) run in parallel, then a merge step combines them. Budget for the merge.
- Best-of-N: run the same task N times and keep the majority or the best. Correlated errors (same model, same blind spot) don't vote away.
- Generator–critic, also called evaluator–optimizer: one agent produces, another critiques against criteria, the first revises.
- Debate: agents argue over rounds, then converge. Part 3 shows most of the gain may come from the vote, not the debate.
- Judge panel or jury: several judges, ideally from different model families. They share position and length biases, so calibrate against human labels.
- Pipeline, or prompt chaining: fixed stages such as localize, fix, validate.
-->

---

## Two design choices

| Choice | When generating | When reviewing |
| --- | --- | --- |
| One model or mixed models? | The best single model usually wins | Mixed families: different blind spots |
| Shared or isolated context? | Share full context so agents don't diverge | Don't share the author's reasoning |

**Share the spec and the code. Withhold the author's conversation.**

<!--
Homogeneous teams use one model with different prompts. Heterogeneous teams mix models, often from different labs.

For generating answers, mixing in weaker models can lower quality. One study (Li et al., 2025) found that aggregating samples from the single best model beat mixing several different models. For judging and reviewing, diversity helps, because models from different families have different blind spots and less self-preference (Verga et al., 2024).

On context, Cognition argues for sharing full context so agents don't diverge. Reviewers do better without the author's reasoning, so they aren't anchored by it. Share the spec and code with reviewers, without the conversation that produced them.
-->

---

## Recipe 1: a review swarm

**freeze the target → reviewers by concern → deduplicate → verify each finding → rank → a human decides**

| Step | What happens |
| --- | --- |
| Freeze | One commit or diff, the spec, read-only repo access, for everyone |
| Fan out | One reviewer per concern: correctness, security, tests, API, simplicity |
| Deduplicate | Merge findings by location and root cause |
| Verify | A fresh agent tries to *disprove* each finding |
| Rank | Confirmed findings, plus plausible ones only if high severity |

<!--
This pattern has the best evidence and the lowest risk, because reviewers only read. It's also how the commercial tools are built. Anthropic's managed Code Review runs "several agents" that "examine the diff and the surrounding code in parallel," then a verification step "filters out false positives," then ranks by severity.

The module uses this reviewer brief:
"You are reviewing a change you did not write. Focus only on SECURITY. Inputs: the diff, SPEC.md, and read-only repo access. For each finding give: file:line, a concrete failure scenario (specific input or state, then wrong behavior), and severity (high/medium/low). Report only issues that would cause real harm. Skip style. If you find nothing, say so. Do not invent findings to seem useful."

Give the human a short ranked list rather than 40 comments. Module 10 covers review in depth.
-->

---

## Verification separates a swarm from noise

```text
A reviewer claims: "<finding>".
Your job is to check whether it is real. Trace the code path.
If possible, write a test that demonstrates the failure and run it.
Answer CONFIRMED (with evidence),
PLAUSIBLE (can't prove either way, explain),
or REFUTED (explain why the scenario can't happen).
```

AI critics catch many bugs and invent some. Human-plus-critic teams invent fewer.

<!--
For each finding, start a fresh agent whose job is to disprove it. Claude Code's ultrareview takes this approach: "every reported finding is independently reproduced and verified."

The research behind it is OpenAI's CriticGPT work (McAleese et al., 2024). AI critics caught many bugs but also hallucinated some, and human-plus-critic teams hallucinated less than critics alone.

If the verifier refutes most of one reviewer's findings, that reviewer is noise. Change its prompt or drop it.
-->

---

## Recipe 2: cross-model review

Models recognize their own writing, and tend to prefer it.

- At minimum, review in a fresh context, never the writing session
- Better, have a different lab's model review
- Keep the reviewer strong, or you get confident noise
- Verify across models; cross-family agreement is stronger evidence

<!--
Panickssery et al. (2024) found that out-of-the-box models can tell their own outputs apart from others' with non-trivial accuracy, and the stronger the self-recognition, the stronger the self-preference. Wataoka et al. (2024) traced the bias to familiarity: judges score lower-perplexity, more familiar-looking text higher, whoever wrote it. A model reviewing its own code is primed to like it.

Write with Claude Code and review with Codex (/review locally or @codex review on the PR), or the other way around. Panels drawn from "disjoint model families" show "less intra-model bias" than a single judge (Verga et al., 2024).

Diversity doesn't help if the reviewer is much weaker than the author. Module 03 tracks which models are strong at code right now.
-->

---

## Recipe 3: parallel builders, when you must

1. Write the interfaces first, in one human-reviewed change
2. One agent, one worktree, one branch per module
3. Give each agent its own failing tests
4. Merge one at a time: rebase, run the full suite, merge, repeat
5. Or run best-of-N: same task, N worktrees, keep the best

<!--
Sometimes you do want several writers: a large migration, a greenfield project with clear modules, or a backlog of independent chores.

1. Types, API contracts, or function signatures go in a shared file first. Then split work by module.
2. Worktrees are covered in module 08.
3. As the C compiler showed, independent failures make independent work.
4. Gas Town has a dedicated "Refinery" agent for merging because parallel workers otherwise end up in "a monkey knife fight over rebasing/merging" (Yegge, 2026).
5. For one hard task, run two or three agents on the same task in separate worktrees and keep the best result. It costs N×, but there's nothing to merge.
-->

---

## Budgets and stop conditions

- Cap agents, turns, spend, and wall-clock time
- Stop when a full pass finds no new confirmed finding
- Don't loop review-and-fix forever
- Fire noisy reviewers
- Measure tokens and confirmed findings per review

<!--
Multi-agent setups fail expensively when nobody decides when to stop. Anthropic's research agents at first had a failure mode of "spawning 50 subagents for simple queries." The fix was to scale effort to the task: "Simple fact-finding requires just 1 agent with 3-10 tool calls."

Set limits before you start: the maximum number of agents, turns per agent, spend (a budget flag or a provider spend limit), and wall-clock time.

Also stop when the budget is hit, or when two rounds of review-and-fix produce no new high-severity issue.

Anthropic's docs warn that "A reviewer that's asked to find problems will always find something," and fixing everything leads to "extra abstraction layers and tests for cases that can't happen."

A swarm that costs 10× and finds the same bugs as one reviewer isn't worth it. Module 12 covers costs.
-->

---

## Anti-patterns

| Anti-pattern | What goes wrong |
| --- | --- |
| Org-chart theater | CEO, CTO, and QA agents: same information, no tests |
| Debate without a referee | Agreement is not correctness |
| The telephone game | Detail evaporates at each summary hop |
| Self-review only | One model, one context, grading itself |
| Unbounded fan-out | "Use as many agents as you need," no cap |

<!--
- Org-chart theater: the roles add tokens, not checks.
- Debate needs an external check or a vote.
- Telephone game: agent A summarizes for B, B for C. Pass the original artifacts, not summaries of summaries.
- Self-review as the only review fails for the self-preference reasons on the cross-model slide.
- Unbounded fan-out is how you get 50 subagents for a simple question.
-->

---

<!-- _class: divider -->

# Part 3: What the research says

More sobering than the hype

<!--
Part 3 covers the research. The module's Going deeper section has more, including the 2023 papers.
-->

---

## Debate or vote?

- Sampling several answers and taking the majority is a strong, early baseline
- "Majority Voting alone accounts for most of the performance gains" (Choi et al., 2025)
- Debate can *lower* accuracy as agents abandon right answers (Wynn et al., 2025)
- Self-correction without outside feedback can degrade (Huang et al., 2023)

<!--
Self-consistency (Wang et al., 2022) samples several reasoning paths and takes the majority answer. "More Agents Is All You Need" (Li et al., 2024) found plain sampling-and-voting performance "scales with the number of agents instantiated."

"Debate or Vote" split multi-agent debate into its parts and found that voting alone "accounts for most of the performance gains typically attributed to" debate. "Talk Isn't Always Cheap" found that "models frequently shift from correct to incorrect answers in response to peer reasoning, favoring agreement over challenging flawed reasoning." That's sycophancy between agents.

Huang et al.: "LLMs struggle to self-correct their responses without external feedback, and at times, their performance even degrades." So feedback works best from outside the model: test results, compiler errors, or a different reviewer. Reflexion's coding gains (91% on HumanEval) relied on running tests.

The 2023 wave (CAMEL, Generative Agents, MetaGPT, ChatDev, AutoGen, AgentVerse) mostly evaluated small, self-contained programs. They're ancestors of today's tools, not evidence that role-play teams beat a strong single agent on real codebases. And simple often beats elaborate. Agentless, a fixed localize-repair-validate pipeline, scored 32% on SWE-bench Lite at $0.70 per issue, the best open-source result at the time.
-->

---

## Why multi-agent systems fail

MAST: 14 failure modes in three groups (Cemri et al., 2025)

| Category | Failure modes |
| --- | --- |
| System design | Disobeying task or role spec; step repetition; lost history; unaware of termination |
| Inter-agent misalignment | Resets; no clarifying questions; derailment; withholding; ignoring input; reasoning–action mismatch |
| Task verification | Premature termination; no or incomplete verification; incorrect verification |

Look hardest at the third row.

<!--
MAST, the Multi-Agent System Failure Taxonomy, is the most useful single reference for debugging a multi-agent setup.

Look at the verification failures in the third row. A multi-agent system without a real verification step is a fast way to produce confident, wrong output. That's why the review swarm's verifier step matters more than the number of reviewers.
-->

---

## What the evidence adds up to

1. Sampling plus a vote is the baseline to beat
2. Gains shrink as single models improve
3. Verification is the part that matters
4. Diversity helps judging more than generating
5. Match the architecture to the task's shape

<!--
1. Before building agents that talk to each other, check whether N independent attempts plus a vote, or plus a test, does as well.
2. Gao et al. (2025): "the benefits of MAS over SAS diminish as LLM capabilities improve." Kim et al. found a capability-saturation effect: once a single agent succeeds about 45% of the time or more, coordination adds little or hurts. Re-test your setup when you upgrade models.
3. Centralized verification contained errors (4.4× amplification) where independent agents spread them (17.2×).
4. Use your best model to write. Use different models to review.
5. Kim et al.'s results ranged from +80.8% on decomposable financial reasoning to −70% on sequential planning. "Architecture-task alignment, not number of agents, determines collaborative success."

Industry reports fit the same picture. Anthropic's research system "outperformed single-agent Claude Opus 4 by 90.2%" on an internal research evaluation, at roughly 15× chat token usage. Cognition argued the opposite for coding agents the day before. They're less contradictory than they look, since research is read-heavy and coding is write-heavy. MAKER (Meyerson et al., 2025) solved a task of over a million steps with zero errors by making each step tiny and voting on each one.
-->

---

<!-- _class: take -->

## On multi-agent review

> **Bryan's take:** Multi-agent *review* is where I get the most value: several agents, and ideally several models, reviewing each other's work. Building in parallel works for me when the tasks are truly independent. Reviewing in parallel works almost every time.

<!--
This slide and the next are my opinions, quoted from the module. Take them as one practitioner's experience.

Review and building differ here too, as in part 1. Parallel review is read-heavy, so it works almost every time. Parallel building needs truly independent tasks.
-->

---

<!-- _class: take -->

## On which models

> **Bryan's take:** For coding, Claude and Codex are the best right now, in my opinion, so they're the pair I cross-review with: one writes, the other reviews. That's a dated opinion; check [module 03](../modules/03-model-landscape/) for the current landscape.

<!--
That opinion is dated, and it says so. Model rankings change fast, so check module 03 instead of treating this as a permanent recommendation. Keep the practice from Recipe 2: one lab's model writes, a different lab's model reviews.
-->

---

## Try it

On your own, a three-reviewer swarm by hand:

1. Take a recent PR of 50–300 lines
2. Three fresh sessions: correctness, security, tests
3. Merge and deduplicate the findings
4. Verify each one in a fresh session, ideally another lab's model
5. Tally confirmed findings, false positives, and token cost

As a class or team, compare one agent, three voting, three debating.

<!--
Use the reviewer brief from Recipe 1 for each reviewer and the verifier brief for each finding. At the end, was the verifier worth it, and which reviewer was noisiest?

For debate vs vote in a class or team, pick 10 questions with checkable answers, such as "what does this function return for input X," or bug-or-not judgments on short snippets. Condition A: one agent answers each. Condition B: three independent agents answer and you take the majority. Condition C: three agents debate for two rounds, then answer. Score accuracy and token cost, and compare with Choi et al. (2025) and Wynn et al. (2025). Did debate add anything over voting? Did any agent switch from a right answer to a wrong one?
-->

---

## Discussion

1. Why do review and research parallelize better than writing code?
2. 90% better at about 15× the tokens: better design, or more compute?
3. If models prefer their own output, what about a one-vendor team?
4. Share full context, or withhold the author's reasoning? Reconcile them.

<!--
Pick two or three. The module has more:
- MAST puts verification failures in their own category. What would a verification step look like in a multi-agent system you might build?
- Which of the 2023 papers' ideas (role-play, debate, SOPs, reflection) survive in current tools, and which have faded? Why?

On question 1, push for a writing task that does parallelize well, and what makes it different (an oracle that splits the work, like the C compiler's tests).
-->

---

## Read more

- [Module 09: Multiple agents building and reviewing](../modules/09-multi-agent-systems/)
- Anthropic, [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) (June 13, 2025)
- Walden Yan, [Don't Build Multi-Agents](https://cognition.com/blog/dont-build-multi-agents) (Cognition, June 12, 2025)
- Cemri et al., [Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657) (2025)

<!--
Read the Anthropic and Cognition posts back to back. They came out a day apart and argue opposite sides, and the read/write asymmetry explains both. Next time, module 10 goes deeper on AI code review.
-->

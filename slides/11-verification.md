---
marp: true
theme: not-writing-code
paginate: true
title: "11: Verification"
description: "Getting agents to check their own work"
footer: "A Brief Introduction to Not Writing Code · 11 Verification"
---

<!-- _class: lead -->

# 11: Verification

Getting agents to check their own work

<!--
Today is the start of Stage 4, trusting the output. The question for the whole session: when an agent says "done," what would it take for you to believe it? The reading is module 11. About 45 minutes, then discussion.

Products, docs and numbers are as of November 2026 unless a slide gives another date.
-->

---

## Why this matters

- An agent stops when the model *thinks* it's done
- Without an outside check, you are the test suite
- Models fix their mistakes when the feedback comes from outside
- Agents game whatever check you give them
- Passing checks is evidence, not proof

<!--
The agent loop ends when the model decides it's finished, and nothing in the loop guarantees that the model is right.

The research on self-correction points one way: models fix their own mistakes when the feedback comes from outside them (test results, execution, a separate verifier), and sometimes make things worse without it.

So the job is to give the agent as many checks as it can run itself, pick problems that have an oracle, and protect the checks, because agents will go after the check instead of the problem when they can.

Checkable rewards are a big part of why models got good at code (module 03). Checkable tests are how you get *bounded* confidence in their code.
-->

---

## The loop stops when the model thinks it's done

```text
task → agent works: think, act, observe → model thinks it's done
   no outside check → you find out whether it works
   outside check (tests, types, build, Stop hook)
      fail → the output goes back into context → agent works again
      pass → evidence for you to review
```

> "Claude stops when the work looks done." … "In practice that makes you the test suite."
> (Claude Code best practices)

<!--
The two paths end in different places. Without a check, the first real test of the work is you. With one, a failure goes back to the agent while it can still fix it, and what reaches you is a pass plus the evidence for it.

If the agent has nothing to run that tells it whether the work *is* done, "looks done" is all it has. Give the agent a check that returns pass or fail. Asking nicely won't make it reliable.

OpenAI's Codex guide says the loop requires knowing what a good result looks like. Anthropic's Building effective agents post from December 2024 recommends getting ground truth from the environment at each step. For code, that includes automated tests, with human review still needed.
-->

---

<!-- _class: divider -->

# Part 1: Why you can't trust "done"

Verifiers, oracles, and what the research says about self-checking

<!--
Part 1 is the vocabulary and the evidence. About 15 minutes.
-->

---

## Verifiers and oracles

| Word | Meaning | Examples |
| --- | --- | --- |
| Verifier | A test, tool or separate model that checks the agent's claimed result | Compiler, test suite, linter, screenshot diff, a second model |
| Oracle | The source of truth the verifier checks against | An expected value, a reference implementation, a rule for every input, a frozen good output |

Prefer verifiers that give the same answer every time.

<!--
A verifier checks. An oracle is what it checks against. Often the oracle is just an expected value a person wrote into a test. It can also be a second implementation, a rule that must hold for every input, or an output you froze because you know it's good.

Verifiers differ in how far you can trust them. A type checker gives the same answer every time. A model judge can be swayed by how the code looks. Prefer the first kind, and use the second only where nothing else fits.
-->

---

## The ladder of checks

| Rung | Catches | Agent can run it? |
| --- | --- | --- |
| Types and compilation | Methods that don't exist, wrong types | Yes, in seconds |
| Lint and static analysis | Unused code, risky patterns, team rules | Yes, in seconds |
| Unit and property tests | Wrong behavior; edge cases nobody wrote down | Yes |
| Integration tests | Wrong assumptions about the database or another service | Usually (often Docker) |
| End-to-end and runtime | Doesn't work for a user, or when you actually run it | Yes, or partly |
| Human review | Wrong intent, design, or call on risk | No |

<!--
Low rungs are fast and cheap and catch narrow kinds of mistakes. High rungs are slower and catch more of what a user would notice. A good setup lets the agent climb as far as it can on its own before a person looks.

Examples per rung: tsc --noEmit, mypy, cargo check for types; ruff, eslint, clippy for lint; pytest tests/unit for unit tests; Hypothesis for property tests; a real Postgres in a container for integration; Playwright for end-to-end; curl against a dev server, logs, or a canary deploy for runtime; and someone who reads the diff (module 13) at the top.

The bottom rungs are worth more than they look. A type checker catches hallucinated APIs before any test runs. Research on type-constrained decoding, which uses the type system to limit what the model can generate, found it "reduces compilation errors by more than half" (Mündler et al., 2025).

The top rungs catch what the middle ones miss. Simon Willison: "Just because code passes tests doesn't mean it works as intended." He has agents exercise their code directly, with python -c, curl and Playwright.
-->

---

## Outside feedback beats self-critique

| Study | Finding |
| --- | --- |
| Huang et al., 2023 | Without oracle labels, GPT-3.5 on CommonSenseQA fell from 75.8 to 38.1 after one round |
| Reflexion, 2023 | Remove test generation and execution: 52%, below the 60% baseline |
| Self-Debugging, 2023 | "Up to 12%" with unit tests; 2–3% on Spider, which has none |
| Olausson et al., 2023 | Human feedback instead of GPT-4's own: repair success 33.3% → 52.6% |

"Review your work and fix any mistakes" is the weakest feedback you can give.

<!--
The obvious shortcut is to ask the model to check itself. The research says that mostly doesn't work.

Self-Refine (Madaan et al., 2023) had one model generate, critique its own output, and refine it. Reflexion (Shinn et al., 2023) had agents write reflections on failures and keep them for the next attempt, reaching 91% on HumanEval. Huang et al. found that on reasoning tasks, LLMs struggled to correct themselves without external feedback and sometimes got worse. Earlier gains relied on oracle labels. Without them, a model could replace a correct answer with a wrong one.

In every row, the gains come from a signal the model didn't produce itself. Full Reflexion got 68%; without running tests it fell below the baseline. Olausson et al. found that self-repair was limited by the model's ability to give feedback on its own code. Stechly, Valmeekam and Kambhampati (2024) found that self-critique made performance collapse, while sound external verification produced significant gains.

The Kamoi et al. survey (TACL 2024) sums it up: "Self-correction works well in tasks that can use reliable external feedback." A failing test with its error message is much stronger feedback, because it carries information the model didn't already have.
-->

---

## Checking is easier than solving

> "some tasks are much easier to verify than to solve."
> (Jason Wei, the asymmetry of verification, 2025)

- Trained verifiers ≈ "a 30x model size increase" (Cobbe et al., 2021)
- SWE-bench Lite, solved by at least one sample: 15.9% with one, 56% with 250
- Those gains held only where answers "can be automatically verified"

Generate several, keep the one that passes the tests.

<!--
An outside check helps this much because, for many tasks, checking an answer is far easier than producing one. Wei pairs the asymmetry with a verifier's rule: "The ease of training AI to solve a task is proportional to how verifiable the task is." His post says "rule"; its URL says "law."

Cobbe et al. found that reranking samples with a verifier gave about the same performance boost as increasing model size 30-fold. They attributed this to verification generally being easier than generation. Brown et al. (2024) found that more sampling helped only when the samples could be checked; majority vote and reward-model selection plateaued. Song et al. (2024) found that the generation-verification gap largely governs self-improvement.

The catch: the gap belongs to the checker, and a model isn't automatically a good checker of its own work. On graph coloring, LLMs "are no better at verifying a solution" than at generating one (Stechly, Marquez, Kambhampati, 2023). That's why "generate several, keep the one that passes the tests" works for code, and "generate one, ask the model if it's right" mostly doesn't.
-->

---

## Model judges have known biases

| Bias | Evidence |
| --- | --- |
| Position | Swap two answers' order and the verdict can flip; Vicuna-13B "beat" ChatGPT on 66 of 80 queries |
| Verbosity and self-preference | Documented by Zheng et al. (2023); self-preference work followed |
| Cosmetics | Names, comments and formatting sway every judge tested |
| Prompt wording | Software-engineering judges "highly sensitive to prompt biases" |

Treat a model judge's verdict as weaker evidence than an executable test.

<!--
Sometimes there's no test for what you care about: readability, whether the design fits, whether a doc is accurate. Then people reach for a model as the judge. That helps, and it comes with known biases.

Zheng et al. found strong model judges agree with human preferences about as often as humans agree with each other, and documented position, verbosity, and self-enhancement biases. Wang et al. showed judges "can be easily hacked by simply altering their order of appearance"; with ChatGPT as the judge, Vicuna-13B "beat" ChatGPT on 66 of 80 queries.

Judging code doesn't fix this. Moon et al. (2025) found cosmetic changes sway every judge tested, "even when prompted to generate test cases before scoring." Order still matters in pairwise code judging (CodeJudgeBench). And Zhao, Esmaeili and Fard (2026) found the prompt effect strong enough in some settings to reorder model rankings.

So use a judge for what tests can't express. Give it a fresh context, prefer a model from a different lab, and check a sample of its verdicts against your own. Module 12 covers judge panels and cross-model review; module 13 covers checking a reviewer's findings before you act on them.
-->

---

## Checkable rewards, checkable tests

**RLVR:** models trained on problems a program can check. That's a big part of why they got good at code.

**Your tests:** confidence that reaches exactly as far as the tests do.

> "'All tests pass' on its own tells you very little." (Claude Code best practices)

<!--
Module 03 explains reinforcement learning with verifiable rewards. The model gets problems a program can check, such as code that has to pass unit tests, and is rewarded when it gets them right. Code is unusually checkable, and the verifier's rule says checkable tasks are the ones AI learns fastest.

The same property is what lets you trust the output, up to a point. Passing tests is evidence, not proof.

RL also leaves a habit behind. Training rewards whatever the check measures, so models learned to satisfy checks in ways nobody intended. Anthropic's Claude 4 system card defines reward hacking to include "hard-coding (writing solutions that directly output expected values) and special-casing ... to pass tests," and reports that Claude Sonnet 3.7 "showed a tendency to resort to these behaviors, particularly in agentic coding settings such as Claude Code." That's Goodhart's law inside the model: when a measure becomes a target, it stops being a good measure.

Keep the checks, and prevent the agent from changing what they measure.
-->

---

<!-- _class: divider -->

# Part 2: Give the agent an oracle

Tests, loopable problems, loops, and gates

<!--
Part 2 is the practical core: what to give the agent to check against, how to loop on it, and how to make the harness enforce it. About 18 minutes.
-->

---

## Tests as the agent's contract

- Write or approve the tests yourself, before implementation; commit them separately
- Make each test fail first
- Read the full test diff: `git diff main -- tests/`
- Enforce with a hook or deny rule, not just a `CLAUDE.md` line
- Keep some checks out of the agent's reach

> "write a failing test that reproduces it, then fix it" (Anthropic)

<!--
Test-driven development means writing a failing test before the code that makes it pass. Simon Willison: "Test-first development is particularly effective with agents that can iterate in a loop."

The contract only works if the agent can't quietly rewrite it. Agents under pressure to make tests pass sometimes delete, skip, or special-case them. So:
- A test that never failed may not test anything. Willison: "If you skip that step you risk building a test that passes already."
- Read the full test diff on every change. `git diff main -- tests/` shows deleted assertions and new skips, which a `--stat` summary hides.
- Anthropic's docs say a line in CLAUDE.md is followed "nearly every time," while a hook or a deny rule applies every time. Anthropic's long-running agent harness told its agents: "It is unacceptable to remove or edit tests because this could lead to missing or buggy functionality."
- StrongDM's team keeps end-to-end "scenarios" outside the codebase, like a holdout set in machine learning, so agents can't tune the code to them.

Kent Beck's system prompt for his own agent says "Always follow the TDD cycle: Red → Green → Refactor." One warning sign he watches for: "Any indication that the genie was cheating, for example by disabling or deleting tests." Lab 03 runs the whole contract on a small project.
-->

---

## Problems an agent can loop on

| Oracle | Good for | Watch for |
| --- | --- | --- |
| A failing test | Bug fixes, small features | A test that never failed |
| A golden output (snapshot) | Refactors, report generators, formatters | "Fixing" it by regenerating the snapshot |
| A reference implementation | Ports, rewrites, compilers, parsers | Agreeing with the reference's bugs |
| A property | Parsers, serializers, anything with an inverse | Properties too weak to fail |
| Model-written tests | Ranking candidates; exploring a spec | Tests that are themselves wrong |

"The code is good" isn't a check. Name the command that proves it worked, or run it by hand.

<!--
Willison's advice for designing agent loops is to look for "problems with clear success criteria," and "A common theme in all of these is automated tests." Before you hand a problem to a loop, find or build its oracle.

Golden outputs: Jest's docs say snapshots "should be committed ... and reviewed as part of your code review process," and warn against "regenerating snapshots when test suites fail instead of examining the root causes." Regenerating the snapshot is the easiest way for an agent to turn a red test green, so treat a changed snapshot file like a changed test.

Model-written tests can filter candidates. CodeT lifted HumanEval pass@1 to 65.8%, 18.8 points over the base model. But Reflexion's self-written tests had a 16.3% false-positive rate on MBPP Python. Meta's TestGen-LLM keeps only generated tests that build, pass reliably and add coverage: "75% ... built correctly, 57% passed reliably, and 25% increased coverage." Hold your agent's tests to the same bar.

"The code is good" isn't a check, and neither is "users will like it." When the real spec lives in people's heads, as it does for most product work (module 10), a loop has nothing to converge on. Write the spec down as checks first, or keep a human in each iteration. OpenAI lists "Scheduling a recurring task before it's reliable manually" as a common mistake. If you can't name the command that proves the task worked, run it by hand until you can.
-->

---

## Oracles that need no answer key

**Differential testing:** two implementations of one spec must agree.

- Csmith found more than 325 compiler bugs this way
- Anthropic's agent-built C compiler used "GCC as an online known-good compiler oracle"

**Property tests:** state a rule, let a tool hunt for counterexamples.

```python
@given(st.text())
def test_slugify_is_idempotent(s):
    assert slugify(slugify(s)) == slugify(s)
```

<!--
Differential testing, as the Csmith paper puts it: "if one has multiple, deterministic implementations of the same specification, all implementations must produce the same result." Csmith credits McKeeman (1998) with the term. Carlini's lesson from the compiler: "the task verifier is nearly perfect, otherwise Claude will solve the wrong problem." A reference implementation answers for every input, not only the ones you thought to write down. Module 10 finds a strong oracle behind every famous autonomous success.

Hypothesis randomly chooses inputs, including edge cases you may not have considered, and checks 100 by default. When it finds a failure, it reports the simplest failing input. The module has a second property for lab 03's `slugify`: the output never exceeds `max_length`.

Properties suit agents for a second reason: an agent can't hard-code answers for inputs that are made up fresh on every run. Weak properties can still pass, though. Both properties hold for a `slugify` that always returns an empty string. Models can help write them, unevenly. One study found "a valid and sound PBT can be synthesized in 2.4 samples on average," but GPT-4 got only 21% of the properties extractable from API documentation right.
-->

---

## Loops in practice

| Pattern | Mechanism | Good for |
| --- | --- | --- |
| Ralph loop | Shell `while` loop, fresh session each pass, plan file as memory | Greenfield scaffolding; a checklist |
| Interval loop | `/loop 5m check the deploy`; cron | Polling CI, babysitting a PR |
| Goal loop | `/goal …`; a separate model checks every turn | Migrations, test-fixing |
| Stop hook | Blocks finishing until a check passes | "Tests pass before done," every session |
| Scheduled cloud task | Runs without your machine | Nightly triage, dependency updates |

<!--
A loop replaces you as the person who types "continue." It's only worth building when the task has a checkable end state. These are the common patterns, simplest first.

The goal-loop example from the module: "/goal all tests in test/auth pass and lint is clean." Codex has automations as its scheduled equivalent.
-->

---

## What every loop needs

```text
read state → do one item → verifier: tests, linter, separate model
   fail → do the item again
   pass → update state, commit → budget or goal reached?
            no  → read state again
            yes → stop and report to a human
```

- A verifiable end state and an independent check
- A budget, state outside the conversation, and isolation
- Escalation before anything irreversible, and a human who reads the output

<!--
The full list of seven:
1. A verifiable end state. "All tests in test/auth pass" works. "The code is good" doesn't. Claude Code's /goal evaluator can't run commands itself; it judges from what the agent printed, so the agent has to show the evidence.
2. An independent check: tests, a type checker, or a different model that didn't write the code. A model grading its own work is optimistic.
3. A budget in turns, wall-clock time, or tokens. Claude Code suggests adding "or stop after 20 turns" to a goal, and its session loops expire after seven days.
4. State outside the conversation: a plan file, a checklist, or issues the next iteration reads.
5. Isolation in a worktree or sandbox, so a bad iteration can't damage your main checkout.
6. Escalation. When the loop is stuck or something is irreversible (pushing, deleting, spending money), it stops and asks.
7. A human who reads the output. A loop's "done" is a claim, so review the diff before it ships (module 13).
-->

---

## Ralph loops

```bash
while :; do claude -p < PROMPT.md; done
```

Geoffrey Huntley, July 14, 2025: "In its purest form, Ralph is a Bash loop."

- "one thing per loop"
- Tests and a type checker as "backpressure"
- "There's no way in heck would I use Ralph in an existing code base."

<!--
Named after the Simpsons character Ralph Wiggum. It's the simplest loop and the extreme version of an unattended run. That line is the post's claude-code pseudocode adapted to the current claude binary in non-interactive print mode. The prompt does the real work: read a plan file, do the single most important remaining item, update the plan, and exit, so the next pass starts with a fresh context window. State carries through files: a prioritized fix_plan.md, spec files, and git history.

Huntley recommends wiring in checks that reject invalid code, especially a static analyzer and type checker. Even then, passing the checks doesn't guarantee that Ralph built the right thing. He warns about placeholder implementations and occasional broken builds. His approach still needs senior expertise guiding it.

Read those caveats as a verification checklist: backpressure is the verifier, and one thing per loop keeps each check small. Harnesses now ship tamer versions: Claude Code's /loop and /goal, and Codex automations. Module 09 covers where the name "loop engineering" came from.
-->

---

## Goal loops, and how big a task to hand them

```text
/goal every test in tests/auth passes when you run `uv run pytest -q tests/auth`,
show the final output, no other test file is modified, or stop after 20 turns
```

- Claude Code: a fresh, small model checks the condition after each turn
- It "doesn't run commands or read files independently," so the agent must print evidence
- METR, May 2026: 50% horizon ~12 hours of human work; 80% ~1.5

<!--
After each turn the evaluator returns not yet met, met, or impossible. "Completion is decided by a fresh model rather than the one doing the work." The condition must be something "Claude's own output can demonstrate," like printed test results. The docs suggest two clauses worth copying into any goal: "or stop after 20 turns," and "no other test file is modified." Under the hood, "/goal is a wrapper around a session-scoped prompt-based Stop hook," and it halts if Claude makes no tool calls for several turns.

Codex's /goal (behind the features.goals flag) "will stop running when it's confident it has reached the stopping condition," and no separate evaluator is documented. Its template asks for the same evidence: "/goal Complete [objective] without stopping until [verifiable end state]."

METR's time horizons (module 07) are the best public measure of how big a task you can hand a model. They're measured in how long the task takes a human, not how long the agent runs. In May 2026 METR put the public frontier at a 50% horizon of about 12 hours, but an 80% horizon of only about 1.5 hours. On tasks over eight hours, "at least 16% of successful runs were illegitimate upon review." The bigger the task, the more you depend on its checks.
-->

---

## Stop hooks and CI gates

```json
{ "hooks": { "Stop": [ { "hooks": [
  { "type": "command", "command": "pnpm tsc --noEmit 1>&2 || exit 2" }
] } ] } }
```

- "Exit code 2 is what blocks the stop"
- `CLAUDE.md` is followed "nearly every time"; a hook "every time"
- Swap in `uv run pytest -q 1>&2 || exit 2` for a test gate
- CI with required checks is the last gate before main

<!--
Everything so far asks the agent to run checks. A gate makes the harness run them, whether the agent remembers or not. Anthropic's docs sort the ways of saying "done" by who decides: evidence requests, /goal and /code-review are model-decided; tests, typecheck, a Stop hook and CI are enforced. A hook applies "every time, no matter what the model decided to do."

In Claude Code, the Stop hook runs when Claude finishes responding. Returning exit code 2 or `decision: "block"` prevents it from stopping and continues the conversation. `1>&2` sends the type checker's output to standard error.

The hook's input includes stop_hook_active, true when Claude Code is already continuing because of a stop hook, so a script can choose not to block twice. Claude Code also applies "an 8-consecutive-continuation cap," adjustable with CLAUDE_CODE_STOP_HOOK_BLOCK_CAP, so a test that can never pass won't spin forever.

Prompt hooks and agent hooks exist too, where a model decides. Those are model judges, so put them on top of a command check, not in place of one. Codex has a Stop hook with the same stop_hook_active input; non-managed hooks "must be reviewed and trusted before they run."

GitHub requires passing status checks before a merge, but admins are exempt unless "Do not allow bypassing the above settings" is enabled. For unattended cloud tasks, Anthropic recommends a branch rule that the task can't bypass.
-->

---

<!-- _class: divider -->

# Part 3: Keep the check honest

Protecting the verifier, proof of done, and your own trust

<!--
Part 3 is what happens when the agent goes after the check instead of the problem, and what happens to you when the checks keep passing. About 12 minutes.
-->

---

## Agents attack the check

- Rewriting a timer; monkey-patching an evaluator to mark everything correct (METR)
- Told not to cheat: still reward hacking in 70–95% of runs (one task)
- ImpossibleBench: "from simple test modification to complex operator overloading"
- June 2026: no reliable METR time horizon for GPT-5.6 Sol, cheating too high

A pipeline graded by tests the agent can see is on the honor system.

<!--
METR documented frontier models rewriting a timer so the scorer saw almost no elapsed time and monkey-patching an evaluator to mark every submission correct. On the one task where METR tested anti-cheating instructions, reward hacking stayed at 70–95% of runs, depending on the wording.

ImpossibleBench makes tasks where the spec and the tests contradict each other, so any pass is a cheat.

In June 2026 METR declined to publish a reliable time horizon for OpenAI's GPT-5.6 Sol at all: its "detected cheating rate was higher than any public model we have evaluated," including exploits that revealed hidden tests.

The models often know. In METR's 2025 report, reward hacking showed up in 30.4% of RE-Bench runs against 0.7% of HCAST runs, and when asked afterward, o3 said its plan didn't match the user's intent in 10 of 10 trials. Module 04 covers where the habit comes from.
-->

---

## Instructions help some models, not others

"Claude Code impossible tasks": hack rate (Claude 4 system card)

| Model | No special prompt | Anti-hacking prompt |
| --- | --- | --- |
| Claude Opus 4 | 47% | 5% |
| Claude Sonnet 4 | 45% | 10% |
| Claude Sonnet 3.7 | 78% | 80% |

Watching the chain of thought isn't a reliable defense either.

<!--
These tasks can't be solved because of a bug in a hidden test, so any "solution" is a hack. An instruction can help a lot with one model and not at all with another.

OpenAI's system card for GPT-5.6 Sol reports that the model "claimed it completed work that it had not actually done," and that on impossible or flaky tasks it "may present unverified work as completed."

On the last line: when OpenAI put a chain-of-thought monitor into the RL reward, agents learned "obfuscated reward hacking, hiding their intent within the CoT" (Baker et al., 2025). So the defenses have to be mechanical.
-->

---

## Protecting the verifier

1. Make tests read-only while the agent implements
2. Read the test diff on every change
3. Keep holdouts: tests the agent never sees, run by you
4. Prefer checks that resist hard-coding: property and differential tests
5. Test the tests with mutation testing
6. Review with a fresh context, ideally another lab's model

<!--
Roughly in order of effort.
1. A deny rule or hook that blocks edits under tests/ applies every time; a line in CLAUDE.md applies "nearly every time." Lab 03's extension has you build one.
2. Deleted assertions and new skip markers show up in seconds.
3. Grade with tests the agent never sees, and run them yourself after it says it's done. Module 07 does this for evals; StrongDM does it for a whole product.
4. Property and differential tests generate inputs the agent hasn't seen.
5. Next slide.
6. And read what it flags (module 13).
-->

---

## Mutation testing

Coverage "measures only which code is executed." It doesn't check that tests "detect faults."

- The tool breaks your code in small ways, one at a time, and reruns the tests
- A mutant "survived" when all tests passed with it active
- Meta's ACH: an LLM writes realistic mutants of a described fault, then tests that kill them
- No tool? Break one line by hand; if nothing fails, it's probably unchecked

<!--
PIT distinguishes code coverage from fault detection. Stryker calls a mutant a survivor when all tests pass while it is active, and treats that as a missing test. Treat a survivor as a strong hint rather than proof, since some changes don't alter behavior and no test could catch them. The mutation score is detected mutants divided by valid ones.

Meta's ACH targets specific faults rather than uncovered code. Across 10,795 Kotlin classes, it produced 9,095 mutants and 571 tests. Engineers accepted 73% of the tests and judged 36% to be relevant to privacy.

Mutation testing is also how you catch a tautological test, one that checks the code against itself or a mock against its own setup: every mutant survives it.
-->

---

## Proof of done

```text
Before you tell me you're done, give me:
1. Each command you ran to check the work, and its exact output.
2. `git diff --stat`, and the diff of anything under tests/ on its own.
3. Which requirement each new or changed test covers.
4. What you checked by running the code directly (a script, curl, a browser).
5. Anything you could not verify, and why.
```

Then rerun one of the commands yourself.

<!--
"Done" from an agent is a claim. Ask for the proof with it. This is a request you can paste at the end of any task.

OpenAI's Codex guide recommends a "Done when:" line in the prompt (tests passing, a bug no longer reproducing) and lists "Not letting the agent see its work" as a common mistake. Anthropic's long-running harness gave every feature a passes field and checked features end to end in a browser before calling them done.

Item 5 turns the agent's gaps into a list of where to look. The same idea shows up as a "Done means" section in module 09's AGENTS.md example and as "How I verified it" in module 13's PR template. Rerunning one command takes seconds, and it keeps the report honest.
-->

---

## Calibrating your own trust

Automation bias "cannot be prevented by training or instructions." (Parasuraman & Manzey, 2010)

- Scale the evidence to the risk of the change, not the agent's confidence
- Let gates carry the vigilance; they don't get tired
- Read a sample of *passing* work, not only failures
- Measure instead of trusting your sense of speed or quality

<!--
Human reviewers may relax after a bot passes a PR. That's automation bias. Each layer of review still needs to do its job.

The research predates LLMs. Imperfect decision aids can make people miss problems or follow bad advice, and this happens to novices and experts. In a review of 74 studies, a wrong decision-support system raised the risk of an incorrect decision by 26% (Goddard et al., 2012). Developers using an AI assistant wrote significantly less secure code and were more likely to believe their code was secure (Perry et al., 2023).

Developers say they're wary. In the 2025 DORA survey, 90% use AI, but only 24% trust its output "a great deal" or "a lot." In Stack Overflow's 2025 survey, 46% actively distrust AI accuracy against 33% who trust it, and the top frustration, at 66%, is "AI solutions that are almost right, but not quite." Stated distrust doesn't mean careful checking, though. People approve the vast majority of permission prompts (module 08), and they feel faster than they measure (module 07).

On the first bullet: a copy change needs a glance. A change to payments, auth, data deletion or a migration needs the full proof of done, a fresh-context review, and a second person. On the third: cheating shows up in runs that passed.
-->

---

## Too much checking, and holdouts that leak

- DORA's "verification tax": time saved generating goes into verifying
- Claude Code warns "loop until done, don't be lazy" causes overwork more than it fixes stalls
- GPT-5.6 Sol revealed hidden tests; Terminal-Bench pulled entries that uploaded test folders
- A holdout in a folder the agent can read is hidden only while it obeys

Use the cheapest check that catches the mistakes you actually see.

<!--
Over-verification: DORA (2026) says "the time saved during initial code or content generation is often re-allocated to verification overhead." Self-repair has the same shape: counting its cost, "performance gains are often modest." The second quote is from Claude Code's docs. And a reviewer asked to find problems will find some whether or not they're real, which is why module 13 has you confirm a finding before you fix it. Add a rung when something gets through, the way Mitchell Hashimoto adds a harness fix for each agent mistake (module 09).

Holdouts: as models get better at finding hidden tests, "keep the tests secret" turns into an arms race. METR's GPT-5.6 Sol exploits included "extracting hidden source code detailing the expected answer." Keep grading tests outside the agent's sandbox, run them from a separate step, and read what passing runs actually did.

You can borrow ImpossibleBench's design too: make the spec and the tests contradict, and any pass is a cheat. A few impossible tasks in your own eval set show how a model behaves when it's cornered.
-->

---

## Real failures

| When | What happened | The lesson |
| --- | --- | --- |
| Replit, July 2025 | During a code freeze, the agent deleted a production database, then said rollback was impossible. Lemkin reported it worked. | The freeze was an instruction, not an enforced check |
| Claude Code, October 2025 | A user reports an `rm -rf` from `/` that deleted all user-owned files in their home directory | For destructive actions, verify before the command runs |

<!--
Two first-hand reports show what instructions and an agent's own account can't protect you from.

Replit: the database belonged to SaaStr founder Jason Lemkin. His posts show the agent admitting a catastrophic error of judgment. The agent said rollback wouldn't work, but Lemkin reported that it did. He concluded there's no way to enforce a code freeze in vibe coding apps like Replit. Replit's CEO called the deletion unacceptable, said it should never be possible, and announced automatic separation of development and production databases. The agent had reported the state of the system without verifying it and was wrong. Separating the databases provided structural protection.

Claude Code: the user was on v2.0.22 under WSL2 (GitHub issue anthropics/claude-code#10077), and it happened before they could interrupt it. No check after the fact can undo that. Verification for destructive actions has to happen through permissions and sandboxes (module 14), which also lists more incidents, most of them attacks rather than mistakes.
-->

---

<!-- _class: take -->

## On loops

> **Author's note:** I like loop engineering and setting goals, but the goals can't be too ambitious or the agent goes off the rails. Loops with a hard, checkable goal and a human in the loop reading the result work for me. Open-ended loops that run unattended and ship to production don't, yet. (My broader skepticism about fully autonomous workflows is in [module 10](../modules/10-agentic-workflows/#authors-note).)

<!--
This is my opinion, the same one module 09 quotes. Match it to the loop checklist: a checkable end state, an independent check, a budget, and a human reading the result.

The strongest counterpoint is a project with a near-perfect verifier. Carlini's C compiler had GCC to diff against and decades of conformance tests, and parallel agents built it mostly unattended (module 10). With an oracle that good, a loop can be ambitious. Most product work doesn't have one, which is why this module spends so much time on building and protecting checks.
-->

---

## Try it

**On your own: gate "done" on your tests (45–60 minutes)**

1. Write a `Stop` hook that blocks "done" until the tests pass
2. Give the agent a task that breaks a test; count the blocks
3. Make one test contradict the spec. Does it report it, or cheat?
4. Block edits under `tests/` and run step 3 again
5. Break one line by hand. Did a test notice?

**As a class:** build a loop with a verifier.

<!--
Individual exercise in full. Take a small project with a test suite, or lab 03's. Write a Stop hook that blocks "done" until the tests pass: start from the type-check example and swap in your test command. Give the agent a task that breaks a test and watch the hook push it back; count how many times it gets blocked before it finishes. Then make the task impossible, ImpossibleBench-style: change one test so it contradicts the spec, and don't tell the agent. Does it report the conflict, or does it edit the test, special-case the input, or claim success? Add a deny rule or hook that blocks edits under tests/ and run that again. What changed? Break one line of the implementation by hand. Finish with a paragraph: which of these checks would you keep on every project?

Class exercise, one session. In small groups, take a toy project with a failing test suite; the instructor can break 10 tests on purpose. Each group builds a different loop: a Ralph-style shell loop with a plan file, a /goal with a test condition, or a Stop hook that blocks "done" until tests pass. Give each a turn or time budget. Compare: did it finish? How many tokens? Did any "pass" by weakening a test? Check the diffs. Then discuss which verifier you'd trust in a real codebase.
-->

---

## Discussion

1. A loop says "done." What would let you merge its pull request unread? Is that ever acceptable?
2. Opus 4 went from 47% to 5% with an anti-hacking prompt; Sonnet 3.7 from 78% to 80%. What does that say about instructions?
3. What in your team's process catches mistakes without depending on someone staying alert?
4. Payment change vs button text: what evidence would you want for each?

<!--
Pick two or three. The module has two more:
- Reflexion's self-written tests had a 16.3% false-positive rate. When is a test the agent wrote good enough to loop against, and when do you need one a person wrote?
- Which rung of the ladder of checks is weakest in a codebase you know? What would it cost to strengthen it?

For 3, the module's answer is to put the vigilance in the process: required checks, the test diff, the proof-of-done list, and a second person for risky changes. Automation bias "cannot be prevented by training or instructions."
-->

---

## Read more

- [Module 11: Verification](../modules/11-verification/)
- Kamoi et al., [When Can LLMs Actually Correct Their Own Mistakes?](https://arxiv.org/abs/2406.01297) (TACL 2024)
- METR, [Recent frontier models are reward hacking](https://metr.org/blog/2025-06-05-recent-reward-hacking/) (June 5, 2025)
- Simon Willison, [Designing agentic loops](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/) (September 30, 2025)

<!--
The module has the full source list: the self-correction papers, the judge-bias studies, the Claude Code and Codex docs on hooks and /goal, Huntley's Ralph post, and the Replit posts. Kamoi et al. is the best single summary of when self-correction works. METR's post is the clearest record of what cheating looks like. Willison's post is a practical guide to choosing problems for a loop.

Next time, module 12 picks up multiple agents building and reviewing.
-->

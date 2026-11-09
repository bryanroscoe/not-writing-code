# Lab 3: Plan, test, build

This lab runs in week 5 of the [syllabus](../syllabus.md) and is due in week 6. Part A is AI-as-tutor and Part B is AI-accelerated. Plan on 4–5 hours.

*Last checked November 8, 2026.*

## Goal

Run the full explore → plan → implement → verify → commit loop on a small feature, with acceptance tests **you** wrote as the contract the agent must satisfy ([module 08](../../modules/08-agentic-workflows.md#the-core-loop-explore--plan--implement--verify--commit)). Your feature is graded against hidden tests you never see, so your own tests need to be good. In a course, the instructor writes them. Working alone, see [Self-paced: hidden tests](#self-paced-hidden-tests).

Part A (spec and acceptance tests) is AI-as-tutor. An agent may interview you, point out gaps, and explain the test framework, but it may not write the spec text or the tests you submit. Part B (plan, implementation, review) is AI-accelerated.

## Prerequisites and setup

- [Lab 2](lab-02-first-agent-session.md) done: your agent is installed, and you know its permission modes, plan mode, and context view.
- The Lab 3 starter repository: `[link to Lab 3 starter]`. It contains a project skeleton, a test runner, and a feature menu. The instructor holds hidden acceptance tests for each feature. Clone it and work on a branch (`git switch -c lab3`), so the `main` comparisons in step 6 show your whole change.
- Pick one feature from the starter's menu. In a course, the instructor always provides the menu and its hidden tests, because the rubric's hidden-test criterion depends on them.
- Working alone, pick one of these fallback features. Each has a fixed signature (shown in Python; use the equivalent in your language) and a few required behaviors that any hidden tests will check. Everything else is up to your spec.

  | Feature and signature | Required behavior | Decide in your spec |
  | --- | --- | --- |
  | `parse_duration(text: str) -> int`, total seconds | `"1h30m"` → 5400; `"45s"` → 45; `"2h"` → 7200; `""` and `"5x"` raise `ValueError` | Unit order, repeated units, whitespace, zero, very large values |
  | `TokenBucket(capacity: int, refill_per_second: float, clock: Callable[[], float])` with `allow() -> bool` | Starts full, so `capacity` calls in a row return `True` and the next returns `False`; after `1 / refill_per_second` seconds on the injected clock, one more call returns `True`; capacity 0 always returns `False` | Time going backwards, fractional tokens, very long gaps |
  | `parse_env(text: str) -> dict[str, str]` | `KEY=value` lines parsed; blank lines and lines starting with `#` ignored; `KEY="a b"` gives `a b`; `A=b=c` gives `b=c` | Escaped quotes, duplicate keys, `export` prefixes, whitespace around `=` |
  | `slugify(text: str, max_length: int = 50) -> str` | `"Hello, World!"` → `"hello-world"`; runs of separators become one hyphen; no leading or trailing hyphen; result never longer than `max_length`; `""` → `""` | Unicode, truncating mid-word, `max_length` smaller than one word |

## Background reading

- [Module 08](../../modules/08-agentic-workflows.md): [The key fact](../../modules/08-agentic-workflows.md#the-key-fact-the-loop-stops-when-the-model-thinks-it-is-done), [The core loop](../../modules/08-agentic-workflows.md#the-core-loop-explore--plan--implement--verify--commit), [Tests as the agent's contract](../../modules/08-agentic-workflows.md#tests-as-the-agents-contract), [Small diffs](../../modules/08-agentic-workflows.md#small-diffs-git-as-the-safety-net-checkpoints), [Steering a session](../../modules/08-agentic-workflows.md#steering-a-session), [Failure modes and counter-moves](../../modules/08-agentic-workflows.md#failure-modes-and-counter-moves), [A sample session](../../modules/08-agentic-workflows.md#a-sample-session)
- [Module 07](../../modules/07-context-engineering.md): [Spec-driven development in practice](../../modules/07-context-engineering.md#spec-driven-development-in-practice)
- [Module 10](../../modules/10-ai-code-review.md): [Verify findings before acting](../../modules/10-ai-code-review.md#verify-findings-before-acting)

## Instructions

### Part A: specify and write the contract (AI-as-tutor)

**1. Explore, read-only (15 minutes).**

```text
Read this repository. Don't change anything.
Explain the project layout, how tests are run, and the conventions
I should follow when adding a module. Cite file paths.
```

Check at least one claim against the files.

**2. Spec interview (30 minutes).** This prompt comes from Anthropic's docs, quoted in [module 08](../../modules/08-agentic-workflows.md#the-core-loop-explore--plan--implement--verify--commit). Adapt it:

```text
I want to add <feature> but haven't thought it through.
Interview me until you could write the spec. Ask one question at a time.
Don't write the spec yourself; I will.
```

Answer the questions. Then write `SPEC.md` yourself, covering:

- Inputs, outputs, and types.
- Every edge case and error case, with the expected behavior.
- Non-goals: what this feature deliberately won't do.
- Definition of done: which commands must pass.

**3. Write the acceptance tests (45 minutes).** Write at least eight tests in the starter's test file, including at least three edge or error cases. You can ask an AI how the test framework works, or for a hint about a case you're missing, but you can't have it write the tests.

Run them. **They must fail** (there's no implementation yet). Save the output.

```bash
mkdir -p evidence
<test command> 2>&1 | tee evidence/red.txt
git add SPEC.md tests/ && git commit -m "test: acceptance tests for <feature>"
git rev-parse HEAD > evidence/test-commit.txt   # remember this commit
```

A test that has never failed may not test anything ([module 08](../../modules/08-agentic-workflows.md#tests-as-the-agents-contract)).

### Part B: plan, build, verify (AI-accelerated)

**4. Plan in a fresh session (20 minutes).** Start a new session so the build begins with a clean context and a written definition of done ([module 08](../../modules/08-agentic-workflows.md#the-core-loop-explore--plan--implement--verify--commit)). Use plan mode if your harness has one.

```text
Read SPEC.md and <test file>. Propose a plan: the files you'll create or
change, the approach, and the risks. Don't write code until I approve.
Constraints: no new dependencies, no new abstractions beyond what the
spec needs, and do not modify anything under tests/.
```

Read the plan. **Push back on at least one thing:** scope, an unnecessary helper, an unhandled case, a dependency. Save the final plan as `PLAN.md`.

**5. Implement (30–60 minutes).**

```text
Implement the approved plan. Make the tests in <test file> pass without
modifying them. Then run the full test suite and lint, and show me the
exact commands and their output.
```

To steer, watch the first minute, press `Esc` if it drifts, and after two failed corrections start a fresh session with a better prompt ([module 08](../../modules/08-agentic-workflows.md#steering-a-session)).

**6. Verify (30 minutes).** Check the evidence yourself. Don't trust the summary.

```bash
git diff --stat $(cat evidence/test-commit.txt) -- tests/   # must be empty
<test command> 2>&1 | tee evidence/green.txt                # run it yourself
git diff --stat main > evidence/diffstat.txt
```

If the test diff isn't empty, inspect it and revert any unauthorized change to the contract. Tests you add later for mutation gaps or confirmed review findings are allowed. Commit them separately, explain them, and keep the original acceptance assertions intact.

Then do a **mutation check by hand**: break the implementation on purpose in two different ways (flip a comparison, drop an edge-case branch, return early). Run the tests after each break. Record which test caught it. Revert. If no test catches a break, add a test that does, and note it ([module 08](../../modules/08-agentic-workflows.md#failure-modes-and-counter-moves)).

**7. Independent review (30 minutes).** In a **fresh** session that never saw the build conversation, run your harness's review command (for example `/code-review` in Claude Code or `/review` in Codex), or give a fresh session the reviewer brief from [module 09](../../modules/09-multi-agent-systems.md#recipe-1-a-review-swarm).

For each finding, decide whether it's real. Use the verify-first prompt from [module 10](../../modules/10-ai-code-review.md#verify-findings-before-acting): ask for a failing test that demonstrates it, or an explanation of why it can't happen. Record each finding in a table:

| # | Finding | Severity | Real? | Evidence | Action |
| --- | --- | --- | --- | --- | --- |

Fix only confirmed findings, each with a test. Acting on unverified findings can bloat the code ([module 10](../../modules/10-ai-code-review.md#verify-findings-before-acting)).

**8. Commit (10 minutes).** Make small, separate commits: tests (already done), implementation, and each review fix. Write or check every message.

**9. Reflect (20 minutes).** Write half a page, in your own words:

- Where did the plan change, and why?
- Did the agent try to touch the tests, skip them, or claim success early?
- What did your mutation check reveal about your tests?
- After grading, compare with the hidden-test results: what did the hidden tests catch that yours didn't, and what kind of case was it?

## Self-paced: hidden tests

Without an instructor, use one of these so the hidden-test criterion still means something:

1. A study partner works best. Give them the feature's required behaviors and your `SPEC.md`, but not your tests. They write six to ten hidden tests and run them on your finished branch after step 8.
2. Alone, use a holdout file. Before Part A, write four to six tests from the required behaviors only, and keep them somewhere the agent can't read (not inside or next to the repository; see [Lab 6](lab-06-your-own-eval.md#2-write-and-validate-each-task-then-hand-over-the-hidden-tests-90-minutes-each)). Add them only after step 8. It's weaker, because you wrote them, but it still catches an implementation tuned to your visible tests.

If you can do neither, see the rubric note below.

## What to submit

- Repository link or zip, with this commit order visible: spec and tests → implementation → review fixes.
- `SPEC.md` and `PLAN.md`.
- `evidence/`: `red.txt`, `green.txt`, `test-commit.txt`, `diffstat.txt`, and the empty test-diff check.
- Mutation-check notes: what you broke, which test caught it.
- The review findings table.
- An exported transcript of the planning session (step 4).
- The reflection and your [AI log](../syllabus.md#ai-log-template).

## Grading rubric

| Criterion | Points | Full credit means |
| --- | --- | --- |
| Spec | 15 | Written by you; inputs, outputs, edge and error cases, non-goals, and definition of done all present |
| Acceptance tests | 20 | At least eight, written by you, including three edge or error cases; committed before any implementation; seen failing |
| Plan | 10 | Fresh session; plan read and challenged at least once; saved |
| Hidden acceptance tests | 20 | Scaled by pass rate on the instructor's hidden tests (self-paced: a partner's tests or your holdout file) |
| Verification | 15 | Your own test run; empty test diff; two mutations, each caught (or a new test added) |
| Review | 10 | Fresh-context reviewer; every finding verified or refuted with evidence; only confirmed findings fixed |
| Reflection and AI log | 10 | Specific, evidence-based, honest about what the agent did |
| **Total** | **100** | |

Self-paced without a partner or holdout file, move the 20 hidden-test points to Acceptance tests (10, judged against the required-behavior list) and Verification (10, for a third mutation that a test catches), and say so in your reflection.

If the transcript or a walkthrough shows that an agent wrote your spec or tests, Part A (spec and tests, 35 points) gets no credit, and the [AI-use policy](../syllabus.md#ai-use-policy) applies.

## If you finish early

- Go up one stage ([module 08 Try it](../../modules/08-agentic-workflows.md#try-it)). While the main agent works, start a second agent in its own worktree on an unrelated task. Afterward, write three sentences on where your attention went and what you nearly missed.

  ```bash
  git worktree add ../.worktrees/lab3/side -b lab3-side
  # ...run the second agent in ../.worktrees/lab3/side...
  git worktree remove ../.worktrees/lab3/side    # clean up when done
  ```

- Enforce the contract with a hook or deny rule that blocks edits under `tests/` during implementation, and show it firing. A line in an instruction file is followed "nearly every time"; a hook applies every time ([module 08](../../modules/08-agentic-workflows.md#tests-as-the-agents-contract)).
- Try a second feature from the menu at a higher autonomy level, with a turn cap, and compare the hidden-test results.

## Instructor notes

- Always provide the feature menu, since the hidden-test criterion depends on it. The fallback table in the setup section is for self-paced learners. If you use those features, write hidden tests that cover the required behaviors plus the edge cases students most often leave out of their specs.
- Write hidden tests to cover the edge cases students most often miss. Keep them out of the student repository and run them after the deadline. Share aggregate results in class, including which kinds of cases the class missed.
- Agent-written tests are the most common integrity problem in this lab. The planning transcript, the commit order, and a quick walkthrough question ("why does this test expect an error rather than an empty result?") usually settle it.
- Agents under pressure to pass sometimes loosen or skip tests ([module 08](../../modules/08-agentic-workflows.md#failure-modes-and-counter-moves)). The empty test-diff check catches it, so make students show you that check instead of claiming it.
- Expect plans with config objects, base classes, or plugin systems for a 40-line function. Reward the student who pushed back.
- Some students will apply every review suggestion. Deduct when unverified fixes add complexity.
- Students who skip the spec interview spend longer in implementation. Point this out after grading.

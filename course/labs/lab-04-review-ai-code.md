# Lab 4: Review AI-written code

> **Course:** [syllabus](../syllabus.md), week 7 (due week 8) · **Tier:** Part A AI-free, Parts B–E AI-accelerated · **Time:** 3–4 hours, in pairs · **Last verified:** 2026-11-08

## Goal

Find real bugs in plausible AI-written code, first by hand and then with AI reviewers, and measure which reviewer catches what. You'll also practice the step most people skip: verifying each finding before acting on it ([module 10](../../modules/10-ai-code-review.md#verify-findings-before-acting)).

The lab works in pairs. Each of you prepares a pull request with five planted bugs, and each of you reviews the other's.

**Tier note.** Part A (your hand review) is **AI-free**: no chat, no agent, no AI review bot, and IDE autocomplete off. Everything else is AI-accelerated. Your write-up and AI log are yours.

## Prerequisites and setup

- [Lab 3](lab-03-plan-test-build.md) done.
- The Lab 4 starter: `[link to Lab 4 starter]`. It's a small web API with users, orders, an admin-only endpoint, a data-access layer, and tests. Clone it, install its dependencies **from the base branch's lockfile**, and run the tests once so your environment is ready before the swap.
- A partner, assigned by the instructor.
- A private repository you can share with your partner, or another way to hand over a branch.
- Optional, for Part B: access to a second lab's model. A free tier, a second plan, or a classmate's tool used with their permission all work.

> [!WARNING]
> **Never install the dependencies a pull request adds in this lab.** One planted bug is a misspelled package that shouldn't exist. Attackers register names that models and people commonly misspell ("slopsquatting"), so a misspelled name can turn out to be real malware ([module 11](../../modules/11-security-and-prompt-injection.md#risks-specific-to-coding-agents)). Check names on the registry's website. Don't run `pip install`, `npm install`, or similar on the PR branch.

## Background reading

- [Module 10](../../modules/10-ai-code-review.md): [What they are good and bad at](../../modules/10-ai-code-review.md#what-they-are-good-and-bad-at), [A layered review workflow](../../modules/10-ai-code-review.md#a-layered-review-workflow), [Verify findings before acting](../../modules/10-ai-code-review.md#verify-findings-before-acting), [Severity triage](../../modules/10-ai-code-review.md#severity-triage), [False-positive fatigue](../../modules/10-ai-code-review.md#false-positive-fatigue), [How humans should review AI-written PRs](../../modules/10-ai-code-review.md#how-humans-should-review-ai-written-prs), [Configure the reviewer](../../modules/10-ai-code-review.md#configure-the-reviewer)
- [Module 09](../../modules/09-multi-agent-systems.md): [Recipe 2: cross-model review](../../modules/09-multi-agent-systems.md#recipe-2-cross-model-review)
- [Module 08](../../modules/08-agentic-workflows.md): the hallucinated-packages row in [Failure modes and counter-moves](../../modules/08-agentic-workflows.md#failure-modes-and-counter-moves)

## Instructions

### Prep: build a seeded pull request for your partner (60 minutes, before the swap)

1. **Generate the feature.** On a branch called `feature`, have your agent implement the feature your instructor assigns (for example "list a user's orders with pagination, and an admin-only endpoint to refund an order"), with tests. Aim for 100 to 300 changed lines.
2. **Plant five bugs,** the set from [module 10's Try it](../../modules/10-ai-code-review.md#try-it):

   | Bug | Example |
   | --- | --- |
   | Off-by-one | Pagination that skips or repeats an item at a page boundary |
   | Swallowed error | `except Exception: return []` in the data layer, so "database down" looks like "no orders" |
   | Missing authorization check | The refund endpoint checks that the user is logged in, not that they're an admin |
   | Tautological test | A test that asserts a mock returns what the mock was told to return |
   | Misspelled, nonexistent dependency | A plausible package name added to the dependency file and imported |

   For the dependency, **look the name up on the registry website** (for example pypi.org or npmjs.com). It must not exist. If it does, pick another name. Don't install it.
3. **Make the plants look natural.** No comments pointing at them, no odd formatting. Real AI-written bugs are tidy and plausible ([module 10](../../modules/10-ai-code-review.md#how-humans-should-review-ai-written-prs)).
4. **Hide the history.** Squash everything into one commit with a neutral message, so `git log` doesn't give the plants away:

   ```bash
   git switch main
   git switch -c review-me
   git merge --squash feature
   git commit -m "Add order listing and admin refunds"
   ```

5. **Write the answer key:** for each bug, the file and line, the type, and a concrete failure scenario. Submit it to the instructor **before** the swap.
6. **Hand over** the `review-me` branch to your partner.

### Part A: review by hand (AI-free, 45 minutes, timed)

Start a timer. Review your partner's branch with no AI help:

```bash
git diff --stat main...review-me    # what changed? read this first
git diff main...review-me           # then every line
```

Work through the [module 10 checklist](../../modules/10-ai-code-review.md#how-humans-should-review-ai-written-prs): intent, hallucinated APIs, new dependencies, tests that test nothing, swallowed errors, unnecessary abstraction, dead code, security, consistency.

You may run the test suite in the environment you built from the base branch. Don't install anything the PR adds.

For each finding, record:

| # | File:line | What's wrong | Failure scenario (specific input or state → wrong behavior) | Severity | Minutes into review |
| --- | --- | --- | --- | --- | --- |

Stop at 45 minutes, even if you think you've missed something. That's data too.

### Part B: review with AI (45 minutes)

Run two AI reviewers on the same branch. Each starts in a **fresh** session that has never seen any conversation about this code.

1. **Reviewer 1:** your harness's review command, for example `/code-review` in Claude Code or `/review` in Codex ([module 10](../../modules/10-ai-code-review.md#the-tools-as-of-november-2026)).
2. **Reviewer 2:** a model from a different lab if you can get one. Models tend to rate their own output higher, and different families have different blind spots ([module 09](../../modules/09-multi-agent-systems.md#recipe-2-cross-model-review)). Export the diff with `git diff main...review-me > pr.diff` and give it to the second model along with the reviewer brief from [module 09's Recipe 1](../../modules/09-multi-agent-systems.md#recipe-1-a-review-swarm), with the focus line changed to "correctness, security, and tests." If you have no second lab, use a different model tier from the same lab in a fresh session, and note the limitation.

Tell both reviewers not to install dependencies or make network requests. Use a read-only or plan mode if your harness has one. Save each reviewer's full output, and record how long it took and roughly how much quota it used.

### Part C: verify every finding (45 minutes)

Merge the findings from you, Reviewer 1, and Reviewer 2 into one list, deduplicated by location and root cause. Then verify each one. For code findings, use the prompt from [module 10](../../modules/10-ai-code-review.md#verify-findings-before-acting):

```text
The reviewer says: "<finding>". Don't fix it yet. First, write a test that
demonstrates the failure, run it, and show me it fails. If you can't make it
fail, explain why the scenario can't happen and we'll dismiss it.
```

Check by hand:

- **Dependencies:** look each new name up on the registry website. Does it exist? If so, who publishes it, since when, and is it the package the code meant?
- **Authorization:** write a test that calls the admin endpoint as an ordinary user.
- **Tests:** break the code the test claims to cover. Does the test fail?

Label each finding **Confirmed**, **Refuted**, or **Plausible** (can't prove either way), with the evidence.

### Part D: score (20 minutes)

Get your partner's answer key from the instructor. Fill in:

| Reviewer | Planted bugs found (of 5) | Real unplanted bugs found | False positives | Time | Quota or cost |
| --- | --- | --- | --- | --- | --- |
| You (Part A) | | | | | |
| Reviewer 1 | | | | | |
| Reviewer 2 | | | | | |

Then triage the confirmed findings with [module 10's severity levels](../../modules/10-ai-code-review.md#severity-triage): High, Medium, Low, or Noise.

### Part E: write-up (20 minutes)

One page, in your own words:

1. Which planted bugs did humans catch that the AI reviewers missed, and the reverse? Why do you think so?
2. Which reviewer would you trust as Layer 2 in a [layered workflow](../../modules/10-ai-code-review.md#a-layered-review-workflow), and why?
3. Write a three-rule review instruction file for this repository that would make that reviewer more useful ([module 10](../../modules/10-ai-code-review.md#configure-the-reviewer)).
4. What did checking the dependency name teach you?

## What to submit

- **Before the swap:** your seeded branch and the answer key.
- **After:** your Part A findings table (with timestamps), both AI reviewers' raw output, the merged and verified findings list with evidence, the scoring table, the severity triage, the write-up, and your [AI log](../syllabus.md#ai-log-template).

## Grading rubric

| Criterion | Points | Full credit means |
| --- | --- | --- |
| Seeded PR | 15 | All five bugs planted and natural-looking; history squashed; dependency name checked as nonexistent; answer key precise |
| Hand review (Part A) | 25 | Findings with concrete failure scenarios and sensible severities; checklist visibly used. Graded on the quality of reasoning, not the raw count |
| AI reviews (Part B) | 10 | Fresh contexts; second reviewer from a different lab or limitation noted; outputs saved; time and quota recorded |
| Verification (Part C) | 20 | Every finding labelled with evidence; tests written for code findings; registry checked without installing |
| Scoring and triage (Part D) | 15 | Honest counts, including false positives; severities justified |
| Write-up and AI log | 15 | Specific comparisons; a usable three-rule instruction file; complete AI log |
| **Total** | **100** | |

## If you finish early

- **Plant a sixth, harder bug** in your own copy: a timezone mistake, a race between two requests, or a migration with no down step. Rerun both AI reviewers. Who catches it?
- **Run the swarm.** Split Reviewer 1 into three focused reviewers (correctness, security, tests) and compare with the single review. This previews [Lab 7](lab-07-multi-agent-review.md).
- **Pilot a review bot** on your term project for two weeks, labelling every comment as acted on, dismissed as wrong, or dismissed as not worth it ([module 10 Try it](../../modules/10-ai-code-review.md#try-it)).

## Instructor notes

- **Pairing.** Pair across experience levels where you can. Experienced students plant subtler bugs, which makes the review harder and more instructive.
- **Collect answer keys before the swap** so nobody adjusts their key afterward.
- **Giveaways.** Watch for plants marked by comments, by odd style, or by a commit history that wasn't squashed.
- **The dependency plant is a safety exercise.** Repeat the warning in class. Ask students to show you the registry lookup. If a student's chosen name turns out to exist, use it as a live lesson.
- **A hypothesis to test, not a prediction to share.** [Module 10's table](../../modules/10-ai-code-review.md#what-they-are-good-and-bad-at) says AI reviewers are good at local logic errors and security smells such as missing authorization checks, and weak at intent and at staying quiet. Don't tell students in advance. Tally the class's results by bug type and compare them with the table in week 8.
- **False-positive counting.** Students under-count AI false positives because they don't want to look like they missed something. Ask for the evidence behind each "Refuted."

# Lab 7: Multi-agent and cross-model review

This lab runs in week 11 of the [syllabus](../syllabus.md) and is due in week 13. It's an individual, AI-accelerated lab on your term project, and together your team's Lab 7 submissions make up the project's cross-model review. Plan on 3–4 hours.

*Last checked November 8, 2026.*

## Goal

Build a review swarm by hand: several independent reviewers, each focused on one concern, then an adversarial verifier that tries to disprove each finding, using a model from a different lab where you can ([module 09](../../modules/09-multi-agent-systems.md#recipe-1-a-review-swarm)). Then measure whether it was worth the extra cost compared with one ordinary review.

You'll do this on a real pull request from your term project that a teammate wrote. Your team's Lab 7 submissions and the resulting fixes fulfill the project's cross-model-review deliverable ([syllabus](../syllabus.md#deliverables)).

Reading parallelizes well, while writing on one codebase usually doesn't ([module 09](../../modules/09-multi-agent-systems.md#building-vs-reviewing-the-readwrite-asymmetry)).

> **Bryan's take:** Multi-agent review is valuable: several agents, and ideally several models, reviewing each other's work.

Agents do the reviewing and verifying. You set it up, check the verifiers, decide what to fix, and write the analysis yourself.

## Prerequisites and setup

- [Lab 4](lab-04-review-ai-code.md) done.
- A change to review: one of your team's pull requests from week 10 onward that **you didn't write**, 50 to 300 lines. For a bigger one, review one coherent part and say which. Agree as a team so each member reviews a different PR, and pick the largest or riskiest ones. The PR must link an issue or spec that says what it's supposed to do. Working alone, use your Lab 3 feature or another change of yours with a spec.
- Your main agent, plus a model from a different lab if you can get one, through a second plan, the other lab's free tier (paste the diff into its chat), or a classmate running their own tool on your shared diff (no account sharing). If none of these work, use a different model tier from your own lab in a fresh session, and note the limitation. A much weaker reviewer adds confident noise without diversity ([module 09](../../modules/09-multi-agent-systems.md#recipe-2-cross-model-review)).
- A budget, **set before you start**. For example, one baseline reviewer, three focused reviewers, at most one verifier per finding, and no more than 12 sessions in total. Stop early if a full pass produces no new confirmed finding ([module 09](../../modules/09-multi-agent-systems.md#budgets-and-stop-conditions)).

## Background reading

- [Module 09](../../modules/09-multi-agent-systems.md): [Why use more than one agent](../../modules/09-multi-agent-systems.md#why-use-more-than-one-agent), [Why not](../../modules/09-multi-agent-systems.md#why-not), [Building vs reviewing](../../modules/09-multi-agent-systems.md#building-vs-reviewing-the-readwrite-asymmetry), [Patterns and when each helps](../../modules/09-multi-agent-systems.md#patterns-and-when-each-helps), [Recipe 1](../../modules/09-multi-agent-systems.md#recipe-1-a-review-swarm), [Recipe 2](../../modules/09-multi-agent-systems.md#recipe-2-cross-model-review), [Budgets and stop conditions](../../modules/09-multi-agent-systems.md#budgets-and-stop-conditions), [Anti-patterns](../../modules/09-multi-agent-systems.md#anti-patterns)
- [Module 10](../../modules/10-ai-code-review.md): [Verify findings before acting](../../modules/10-ai-code-review.md#verify-findings-before-acting), [Severity triage](../../modules/10-ai-code-review.md#severity-triage), [False-positive fatigue](../../modules/10-ai-code-review.md#false-positive-fatigue)

## Instructions

### 1. Freeze the target (10 minutes)

Review a fixed commit, not a moving branch. Give every reviewer the same inputs.

Check out the pull request's branch first. Keep the `review/` folder out of the project's history (for example, add it to `.git/info/exclude`) and submit it separately.

```bash
mkdir -p review
git rev-parse HEAD > review/sha.txt
git diff main...HEAD > review/diff.patch
git diff --stat main...HEAD > review/diffstat.txt
cp SPEC.md review/spec.md      # or save the issue text here
```

### 2. Baseline: one ordinary review (15 minutes)

In a **fresh** session that never saw how the code was written, ask for a plain review:

```text
Review the change in review/diff.patch against review/spec.md.
List any problems you find, with file and line.
```

Save the output as `review/baseline.md`. This is what you're trying to beat.

### 3. Fan out by concern (45 minutes)

Open three **fresh** sessions, one per concern: correctness, security, and tests (do they test the behavior?). Give each the same inputs and [module 09's reviewer brief](../../modules/09-multi-agent-systems.md#recipe-1-a-review-swarm), changing only the focus line:

```text
You are reviewing a change you did not write. Focus only on <CONCERN>.
Inputs: the diff (review/diff.patch), review/spec.md, and read-only repo access.
For each finding give: file:line, a concrete failure scenario
(specific input or state -> wrong behavior), and severity (high/medium/low).
Report only issues that would cause real harm. Skip style.
If you find nothing, say so. Do not invent findings to seem useful.
```

Use a read-only sandbox for reviewers and decline write escalations. Plan mode alone is a workflow setting, not complete isolation. Collect outputs outside the reviewer environments. Expose only `diff.patch`, `spec.md`, and repository source to each reviewer, and don't leave the baseline or other findings in a readable `review/` folder for later reviewers. Share the spec and the code, but not the author's conversation. Reviewers who see the reasoning that produced the code get anchored by it ([module 09](../../modules/09-multi-agent-systems.md#patterns-and-when-each-helps)).

Save each output as `review/r-<concern>.md`. If you want, add a fourth reviewer for API compatibility or simplicity.

### 4. Deduplicate (15 minutes)

Merge every finding (baseline and swarm) into one table in `review/findings.md`, grouped by location and root cause. Record which reviewers raised each one.

| ID | Raised by | File:line | Claim | Severity claimed |
| --- | --- | --- | --- | --- |

### 5. Verify adversarially (45 minutes)

For each finding within your predeclared budget, start a **fresh** session, from a different lab's model if you can, whose job is to *disprove* it. This is [module 09's verifier brief](../../modules/09-multi-agent-systems.md#recipe-1-a-review-swarm):

```text
A reviewer claims: "<finding>". Your job is to check whether it is real.
Trace the code path. If possible, write a test that demonstrates the failure
and run it. Answer CONFIRMED (with evidence), PLAUSIBLE (can't prove either way,
explain), or REFUTED (explain why the scenario can't happen).
```

If you're pasting into a chat tier that can't run code, the verifier can still trace the code and propose a test. You run the test.

### 6. Check the verifiers yourself (20 minutes)

Pick up to three verdicts (all of them if fewer), including CONFIRMED and REFUTED where available, and reproduce them by hand by running the test or tracing the code path yourself. Check whether the verifier got it right, because verifiers can be wrong too. In OpenAI's CriticGPT work, AI critics caught many bugs but also hallucinated some, and human-plus-critic teams hallucinated less than critics alone ([module 09](../../modules/09-multi-agent-systems.md#recipe-1-a-review-swarm)).

Add columns to `findings.md`:

| ID | Verifier verdict | Your verdict | Evidence | Final severity | Action |
| --- | --- | --- | --- | --- | --- |

### 7. Decide and fix (30 minutes)

Use [module 10's severity levels](../../modules/10-ai-code-review.md#severity-triage). Fix confirmed High and Medium findings through your team's normal process: a pull request per fix, each with a test, approved by a teammate. Agree with the PR's author on who makes each fix. File the rest as issues or note them. Don't fix everything. A reviewer may invent problems when asked to find them, and fixing every finding adds layers and tests for cases that can't happen ([module 09](../../modules/09-multi-agent-systems.md#budgets-and-stop-conditions)).

### 8. Measure (20 minutes)

Fill in `review/costs.md`:

| Reviewer | Findings | Confirmed | Refuted | Plausible | Sessions | Quota or tokens | Minutes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Baseline | | | | | 1 | | |
| Correctness | | | | | 1 | | |
| Security | | | | | 1 | | |
| Tests | | | | | 1 | | |
| Verifiers (total) | n/a | | | | | | |

Use your harness's usage or context view for token counts where it has one (for Claude Code, [module 12](../../modules/12-costs-subscriptions-and-apis.md#try-it) shows one way to see token use). Otherwise record turns and minutes.

### 9. Write up (30 minutes)

Write one page, in your own words:

1. Did the swarm find anything the baseline missed? Was it worth the extra sessions?
2. Which reviewer was noisiest? What would you change in its brief, or would you drop it ([module 09](../../modules/09-multi-agent-systems.md#budgets-and-stop-conditions))?
3. Was the verifier step worth it? How many findings would you have acted on wrongly without it?
4. Did the cross-model step change any verdict? If you couldn't use another lab's model, what do you think you missed?
5. For your team's final sprint, which parts of this would you keep, and with what budget? Share your answer with your team. The project README summarizes what the team's reviews found ([syllabus](../syllabus.md#deliverables)).

## What to submit

- The `review/` folder: `sha.txt`, `diff.patch`, `diffstat.txt`, `spec.md`, `baseline.md`, every reviewer and verifier output, `findings.md`, and `costs.md`.
- Your budget, written before you started.
- Links to the fix pull requests (or issues, for findings you deferred), each fix with a test.
- The write-up and your [AI log](../syllabus.md#ai-log-template), naming every model and tool used.

## Grading rubric

| Criterion | Points | Full credit means |
| --- | --- | --- |
| Setup | 15 | Frozen SHA; same inputs for every reviewer; fresh sessions; no author conversation shared; budget written first |
| Reviewer briefs | 10 | One concern each; consistent format; read-only mode used |
| Deduplication and verification | 25 | Findings merged by root cause; findings verified within budget; any unverified remainder labelled Plausible and counted separately; verdicts backed by evidence |
| Your check of the verifiers | 10 | Up to three available verdicts reproduced by hand; missing verdict types or no findings reported honestly |
| Measurement | 20 | Honest counts and costs; comparison with the baseline; noisy reviewer identified |
| Fixes | 10 | Confirmed High and Medium findings fixed with tests through reviewed PRs; low-value findings left alone with a reason |
| Write-up and AI log | 10 | Specific, evidence-based answers; every model named |
| **Total** | **100** | |

## If you finish early

- Try debate vs vote ([module 09 Try it](../../modules/09-multi-agent-systems.md#try-it)). Pick five questions with checkable answers, such as "what does this function return for input X?" Compare one agent, three independent agents with a majority vote, and three agents that debate for two rounds. Score accuracy and cost. Did debate add anything over voting? Did any agent switch from a right answer to a wrong one?
- Write a two- or three-rule review instruction file for the repository ([module 10](../../modules/10-ai-code-review.md#configure-the-reviewer)) and rerun your noisiest reviewer. Did precision improve?
- Have one lab's agent write a small change and the other lab's agent review it, then swap roles on a second change.

## Instructor notes

- In week 11, check that each team has given every member a different PR that member didn't write. Reviewing your own code defeats the point.
- The most common setup error is reviewing in the same session that wrote the code, or pasting the author's conversation into the reviewer. Check that every reviewer started fresh.
- Some students will apply every suggestion. Deduct when unverified fixes add complexity.
- A verifier that confirms everything is no better than none. The human check in step 6 exists to catch this.
- Cross-model access is uneven. Don't penalize a student who used a same-lab fallback and explained the limitation well. Pairing students who use different labs' tools solves most access problems.
- Swarms multiply sessions. If students hit limits, have them cut to two focused reviewers, prioritize High and Medium findings, and label the unverified remainder Plausible. Apply the rubric’s budget allowance.
- For class discussion, compare noise rates by concern across the class. Which concern produced the most refuted findings?

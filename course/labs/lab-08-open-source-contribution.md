# Lab 8: Contribute to open source, responsibly

This lab starts in week 9 of the [syllabus](../syllabus.md), reaches phase 2 by week 11, and is due in week 14. It's AI-as-tutor, or stricter if the project's own policy is stricter. Expect 8–12 hours spread over five weeks.

*Last checked November 8, 2026.*

## Goal

Make one small, well-tested, disclosed contribution to a real open-source project, following that project's rules and the etiquette in [module 13](../../modules/13-open-source-ecosystem.md#etiquette-for-contributing-with-ai), or to the course's private class repository. Learn how a real codebase and its maintainers work.

Public or private is your choice. An upstream contribution is public. The [class repository](#the-fallback-the-class-repository) is private, and choosing it costs you nothing in grading. Read [Privacy](#privacy-contributing-in-public) before you decide.

**You're graded on the process and your learning log, not on whether the pull request is merged.** Maintainers' time and decisions aren't yours to control. For a course, the log is the evidence of learning ([module 13](../../modules/13-open-source-ecosystem.md#how-students-can-contribute-to-open-source-with-ai-responsibly)).

AI tools made it nearly free to produce a plausible-looking pull request, and the cost moved to volunteer maintainers who have to read every one. curl ended its bug bounty in January 2026 after the share of real reports fell below one in twenty ([module 13](../../modules/13-open-source-ecosystem.md#the-other-side-ai-slop-and-maintainer-burden)). Your contribution must be worth more to the project than the time it takes to review it, which is LLVM's golden rule.

By default this lab is **AI-as-tutor**: use AI to understand the codebase, explain errors, and critique your work, but write the code and all text yourself. (Module 13 allows heavily revising an agent's draft. This course is stricter here, because under the [AI-use policy](../syllabus.md#the-three-tiers) AI-as-tutor work may not contain AI-written code.) **The project's policy wins when it's stricter.** If the project bans AI-generated contributions, follow its exact scope: a ban on all AI assistance requires an entirely AI-free contribution; a ban on generated submissions prohibits generated content.

## The rules

These come from [module 13](../../modules/13-open-source-ecosystem.md#etiquette-for-contributing-with-ai) and aren't optional.

1. **Only projects with an explicit, written AI-contribution policy.** In `CONTRIBUTING.md`, an `AI_POLICY.md`, or the project's docs. A project with no written policy isn't eligible for this lab. If no suitable project works out, use the [class repository](#the-fallback-the-class-repository).
2. **Get a maintainer's go-ahead on an issue before you write the pull request.** No go-ahead, no PR.
3. **Follow the policy exactly.** If it requires disclosure in a particular form (for example an `Assisted-by:` trailer), use that form. If it bans AI-generated content, submit nothing AI-generated. If it reserves "good first issue" tickets for people learning without AI, as LLVM does, either do that issue AI-free or pick another.
4. **Small and focused.** One logical change. No "while I was there" cleanups.
5. **Understand every line.** If you can't explain the change and its edge cases without AI open, you aren't ready to submit it.
6. **Reproduce bugs yourself,** on a real build, and write a failing test before fixing anything.
7. **Run the project's required checks locally.** Don't make maintainers' CI find what you could have found.
8. **Write the PR description and every reply yourself.** Disclose AI help even where the project doesn't require it.
9. **Never let an agent post** to an issue tracker, pull request, or mailing list on your behalf.
10. **Accept "no."** If a maintainer declines, thank them and stop. Don't reopen the same change with a new prompt.
11. **Never pressure maintainers about your grade.** You don't have to mention the course. If you do, also say a merge isn't required.

## Privacy: contributing in public

Upstream contributions are public and hard to remove. Your account name, commits, issue comments, and review replies can be seen, searched, and archived by anyone, and they can show that you were a student in a particular course.

- `[Institution: before the term, confirm with the registrar or privacy office that a public contribution as a course activity complies with student-privacy rules, such as FERPA in the US, and record any consent or notice they require.]`
- **The course never requires you to contribute publicly.** The class repository is the private option. You may choose it from the start, for any reason, without explaining why.
- **You don't have to reveal that you're a student,** or name the course or the institution, in any public place.
- **Pseudonymous accounts are fine where the project allows them.** Some projects require a real name, for example for a Developer Certificate of Origin sign-off or a contributor license agreement. Read the rules first. If a project needs a name you don't want to give, choose another project or the class repository.
- **Your grade and feedback stay private.** The instructor collects links and evidence through `[the course's private submission system]` and never posts them publicly.

## Prerequisites and setup

- [Lab 3](lab-03-plan-test-build.md) and [Lab 4](lab-04-review-ai-code.md) done before phase 1. Use [Lab 7](lab-07-multi-agent-review.md) when you reach phase 3’s independent review. It doesn't need to be finished at the week 9 kickoff.
- A GitHub (or other forge) account, set up for signed or attributed commits the way the project requires. It may be pseudonymous where the project's rules permit ([Privacy](#privacy-contributing-in-public)).
- If the project requires a contributor license agreement (CLA) or a Developer Certificate of Origin sign-off, you sign it yourself. In the Linux kernel's words, "AI agents MUST NOT add Signed-off-by tags"; only a human can certify ([module 13](../../modules/13-open-source-ecosystem.md#the-other-side-ai-slop-and-maintainer-burden)). `[Check the institution's policy on intellectual property in student work.]`
- The instructor's vetted project list: `[link]`. You can propose a project that isn't on it.

## Background reading

From [module 13](../../modules/13-open-source-ecosystem.md):

- [What "open source" means here](../../modules/13-open-source-ecosystem.md#what-open-source-means-here)
- [The other side: AI slop and maintainer burden](../../modules/13-open-source-ecosystem.md#the-other-side-ai-slop-and-maintainer-burden), including the policy table, and the linked policies of at least two of those projects
- [Etiquette for contributing with AI](../../modules/13-open-source-ecosystem.md#etiquette-for-contributing-with-ai)
- [How students can contribute to open source with AI, responsibly](../../modules/13-open-source-ecosystem.md#how-students-can-contribute-to-open-source-with-ai-responsibly)

Also [module 15: Attribution and disclosure in commits and PRs](../../modules/15-learning-careers-and-responsibility.md#attribution-and-disclosure-in-commits-and-prs) and [module 10: Make the author explain the change](../../modules/10-ai-code-review.md#make-the-author-explain-the-change).

## Instructions

### Phase 1: choose a project (week 9, about 2 hours)

Check candidates against this list:

- [ ] You use it, or you understand its users.
- [ ] It has a written AI-contribution policy. Quote the key lines in your proposal.
- [ ] It's active: merges and maintainer replies on issues in the last month.
- [ ] You can build it and run its tests on your machine.
- [ ] It has open issues small enough for a first contribution, or a clear way to propose one.
- [ ] No more than one other student in the class has chosen it (the instructor tracks this).
- [ ] Its identity rules (real name, CLA, DCO) are ones you're comfortable with.

Or choose the class repository now and skip to [the fallback](#the-fallback-the-class-repository).

Submit a one-page proposal:

```markdown
## Lab 8 proposal

- Project: <name, link>
- Why this project: <one or two sentences>
- AI policy: <link> — "<quoted key lines>"
- What the policy means for me: <allowed uses, required disclosure format,
  anything banned, any rules about first-time contributors>
- Contribution guide: <link>; CLA or DCO required? <yes/no>; real name required? <yes/no>
- Account I'll use: <your name or a pseudonym, if the project allows it>
- Build and test: <commands; confirmed working on my machine? yes/no>
- Candidate issues: <two or three links, with one line each>
```

The instructor approves it or suggests changes.

### Phase 2: claim an issue and get a go-ahead (by week 11)

1. Pick an existing issue: a bug, a small feature, or a documentation fix the maintainers have asked for. If you found a real bug yourself, file it first. Reproduce it by hand on a real build and write the report yourself. Don't forward a model's speculation ([module 13](../../modules/13-open-source-ecosystem.md#etiquette-for-contributing-with-ai)).
2. Reproduce the bug before you comment. For documentation, demonstrate the incorrect or missing example instead.
3. Comment on the issue, in your own words. Adapt this to the project's tone:

   ```text
   Hi! I'd like to work on this. I can reproduce it on <version or commit>
   with <steps>. My plan is to <one or two sentences>, with a regression test
   in <file>. Per your AI policy, I'll <how you will or won't use AI, and how
   you'll disclose it>. Would a PR for this be welcome?
   ```

   Mentioning that this is coursework is optional. If you do, add that a merge isn't required.

4. Wait for a maintainer's go-ahead. One polite follow-up after about a week is fine. More than that isn't.
5. **If you have no go-ahead by `[week 11 date]`,** switch to the [class repository](#the-fallback-the-class-repository). Don't open a PR without one. Record what happened in your log. It's useful evidence about how projects work.

### Phase 3: do the work (weeks 11–13, 4–6 hours)

Follow the steps from [module 13](../../modules/13-open-source-ecosystem.md#how-students-can-contribute-to-open-source-with-ai-responsibly):

1. Use AI to understand, not to submit. Where the policy allows it, ask an agent to explain the architecture, trace a request through the code, or explain why a test fails. Check what it tells you against the code.

   ```text
   I'm new to this codebase and want to understand it, not change it.
   Trace how <feature or request> flows from <entry point> to <outcome>.
   List the files in order with one line on what each does, and cite line
   numbers. Don't propose changes.
   ```

2. For a bug fix, write a failing test that reproduces it, in the project’s test style. Run it and save the failure. For a feature, add acceptance tests. For documentation, save the before/after example and run the project’s documentation checks instead.
3. Write the fix yourself. An agent may explain, hint, and critique your code, but under this lab's tier it doesn't draft the code you submit. Delete what you can't defend.
4. Keep it small. Check `git diff --stat` before every commit.
5. Run the project's full test suite and linters locally, the way its contributing guide says. Save the output.
6. Before submitting to maintainers, have a classmate or a model from a different lab review your diff ([module 10](../../modules/10-ai-code-review.md#a-layered-review-workflow)). Verify each finding before acting on it.
7. Write the PR description yourself, using the project's template if it has one. If not, cover: what and why, linked to the issue; how you verified it (commands and results); what AI did and what you did; and risks. Disclose AI help in the form the project asks for, or in a short sentence if it doesn't specify one ([module 15](../../modules/15-learning-careers-and-responsibility.md#attribution-and-disclosure-in-commits-and-prs)).
8. Before you open the PR, a TA or the instructor does a ten-minute pre-flight check of your diff and description. This protects maintainers' time, and it isn't a grade.

### Phase 4: open the PR, handle review, follow up (weeks 13–14)

1. Open the pull request. Link the issue and the maintainer's go-ahead.
2. Answer review comments yourself, from your own understanding. If you don't know, say so and find out ([module 13](../../modules/13-open-source-ecosystem.md#how-students-can-contribute-to-open-source-with-ai-responsibly)).
3. Make requested changes in small, clear commits, or follow the project's preference for squashing.
4. If the maintainers decline, thank them and close it.
5. Keep the PR going after the course ends if you want to. Your grade doesn't depend on it.

### Throughout: keep a learning log

Keep `lab8-log.md` with dated entries. This is the main thing you're graded on.

```markdown
## 2026-MM-DD
- What I did:
- What AI did (tool, what for):
- What I learned about the codebase:
- What I learned about how this project works (review, tone, process):
- Open questions:
```

## The fallback: the class repository

Contribute to the class-run repository if you'd rather keep your work private, or if no upstream project works out (no eligible project, no go-ahead in time, or a policy that doesn't fit): `[link to class repository]`.

- It's **private**: `[hosted so that only enrolled students and course staff can see it]`. Nothing you do there is public.
- Choosing it at the start, for privacy or any other reason, is graded exactly like an upstream contribution.
- It has a `CONTRIBUTING.md` and an AI policy modelled on LLVM's human-in-the-loop approach: you read and review all generated code before asking anyone else to; you label substantial AI help with an `Assisted-by:` trailer; you write your own PR description; and no autonomous agents post in project spaces ([module 13](../../modules/13-open-source-ecosystem.md#the-other-side-ai-slop-and-maintainer-burden)).
- Issues are sized and labelled. Claim one with the same kind of comment as above, and wait for a maintainer (a TA, or a student on a maintainer shift) to give you the go-ahead.
- Every rule, step, and rubric line in this lab applies unchanged.
- Students using the class repository also serve one **maintainer shift**: review two other students' pull requests against the policy and the [module 10 checklist](../../modules/10-ai-code-review.md#how-humans-should-review-ai-written-prs). Note how long each review took. This counts toward participation.

## What to submit

- The Phase 1 proposal and the instructor's approval.
- Links to your issue comment, the maintainer's go-ahead, and your PR (upstream or class repository), with screenshots in case anything is deleted later.
- The failing-test output (or documentation before/after evidence), the passing required-check output, and the final `git diff --stat`.
- The second-opinion review and how you handled each finding.
- Your PR description and review replies, as posted.
- `lab8-log.md`.
- A one-page reflection: what you learned about the codebase, about the maintainers' expectations, and about where AI helped and where it got in the way. If you switched to the fallback, what did you learn from the attempt?
- Your [AI log](../syllabus.md#ai-log-template).

## Grading rubric

**Gate:** a contribution that breaks the project's AI policy, or a PR opened without a maintainer's go-ahead, gets no credit, and the [integrity policy](../syllabus.md#academic-integrity) applies.

| Criterion | Points | Full credit means |
| --- | --- | --- |
| Project selection | 10 | Eligible project; policy quoted and correctly interpreted; build and tests confirmed locally |
| Issue and go-ahead | 15 | Bug reproduced by hand, or documentation problem demonstrated, before commenting; clear, honest comment in your own words; go-ahead received (or a timely switch to the fallback) |
| The contribution | 25 | One logical change; failing test first for bugs, acceptance tests for features, or documentation evidence; required checks pass locally; you can explain every line |
| Disclosure and description | 15 | Written by you; AI use disclosed in the project's required form; verification and risks stated |
| Handling review | 10 | Replies in your own words; requested changes made cleanly; a "no" accepted gracefully. If no review arrives, document the wait; no penalty for maintainer silence |
| Learning log and reflection | 25 | Regular dated entries; specific lessons about the code and the community; honest about AI's role |
| **Total** | **100** | Merge status isn't graded. |

## If you finish early

- Help someone else by reviewing a classmate's diff before their pre-flight check, using the module 10 checklist.
- Find the oldest open issue in your project and read the full thread. Write a paragraph on why it's still open.
- Take a maintainer shift in the class repository even if you contributed upstream.
- Read three AI-contribution policies from [module 13's table](../../modules/13-open-source-ecosystem.md#the-other-side-ai-slop-and-maintainer-burden) side by side and draft one for a project you'd maintain. Which rules would you keep, and why?

## Instructor notes

- **Do the privacy review before the term.** Confirm with `[the registrar or privacy office]` that public contributions as a course activity are allowed and what notice or consent is needed. Never require public work, accept a choice of the class repository without question, and keep the class repository private.
- Vet the list every term. Policies change, and projects go quiet. Re-read each linked policy before week 9 ([refresh checklist](../instructor-guide.md#refresh-checklist-for-each-term)).
- Cap students per project. A whole class arriving at one project is itself a maintainer burden. Two per project is a reasonable default.
- Some maintainers reply in hours, some in weeks. Hold the week 11 fallback deadline firmly so nobody is stuck at the end of term.
- Ten minutes of pre-flight check per student catches oversized diffs, missing tests, and descriptions that read like agent output before a maintainer has to.
- If a maintainer complains, take it seriously. Have the student apologize and withdraw if asked, and consider whether that project should stay on the list.
- For integrity, a short walkthrough of the change ("why did you put the check here and not in the caller?") is the best check that the student understands it.
- The class repository needs maintainers. Schedule TA time for go-aheads and reviews, and rotate student maintainer shifts. It's also a good stretch role for experienced students ([instructor guide](../instructor-guide.md#the-existing-engineer)).

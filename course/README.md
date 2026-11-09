# Course: AI-Accelerated Software Engineering

> **Last verified:** 2026-11-08 · **Status:** a proposal for an upper-level undergraduate CS elective, not an approved course anywhere. Bracketed placeholders mark what an adopting department fills in.

A 15-week course built from the [modules](../modules/) of this knowledge base. Students learn to build real software with coding agents while staying accountable for every line: they specify, test first, verify, review, secure, and explain. Some work is AI-free on purpose. Teams ship a small real app.

Needs: one frontier coding-agent plan (about $20/month as of November 2026) or an institutional license. No GPU, no model downloads, no API keys.

## Files

| File | For | What it is |
| --- | --- | --- |
| [syllabus.md](syllabus.md) | Students, instructors, committees | Description, outcomes, tools and cost, weekly schedule, term project, assessment, the AI-use policy with its three tiers, and what to re-verify each term |
| [instructor-guide.md](instructor-guide.md) | Instructors and TAs | Week-by-week talking points, demos, misconceptions, and discussion prompts; grading AI-assisted work; walkthroughs; mixed starting levels; failure-mode demos; the refresh checklist |
| [labs/lab-01-tokens-and-temperature.md](labs/lab-01-tokens-and-temperature.md) | Week 2 | Predict and measure tokenization, simulate temperature, probe hallucination and sycophancy |
| [labs/lab-02-first-agent-session.md](labs/lab-02-first-agent-session.md) | Week 3 | Install an agent, learn its permission modes, measure context, make one tested change |
| [labs/lab-03-plan-test-build.md](labs/lab-03-plan-test-build.md) | Week 5 | The full explore → plan → implement → verify → commit loop, with your own tests as the contract and hidden tests for grading |
| [labs/lab-04-review-ai-code.md](labs/lab-04-review-ai-code.md) | Week 7 | Plant five bugs for a partner; review by hand, then with AI; verify and score every finding |
| [labs/lab-05-prompt-injection.md](labs/lab-05-prompt-injection.md) | Week 8 | Inject your own agent in a sandbox with a fake canary, then apply defenses one at a time. Strict safety rules |
| [labs/lab-06-your-own-eval.md](labs/lab-06-your-own-eval.md) | Week 10 | Build 8–10 golden tasks, run two configurations, score blind, report error bars |
| [labs/lab-07-multi-agent-review.md](labs/lab-07-multi-agent-review.md) | Week 11 | A hand-built review swarm with adversarial verification and a cross-model step, measured against one ordinary review |
| [labs/lab-08-open-source-contribution.md](labs/lab-08-open-source-contribution.md) | Weeks 9–14 | One small, disclosed contribution to a project with a written AI policy, after a maintainer's go-ahead; a class-run repository as the fallback |

## Where to start

- **Students:** the [syllabus](syllabus.md), then the [student path](../paths/students.md), which follows the same order.
- **Instructors:** the [instructor guide's "Before the term"](instructor-guide.md#before-the-term) list, then the [refresh checklist](instructor-guide.md#refresh-checklist-for-each-term).
- **Self-paced learners:** do the labs in order. Skip the parts that need a partner or an instructor (Lab 4's swap, Lab 3's hidden tests, Lab 8's pre-flight check), or find a study partner to play those roles.

Every lab follows the same shape: goal, time, setup, background reading, step-by-step instructions, what to submit, a grading rubric, an "if you finish early" extension, and instructor notes on common pitfalls.

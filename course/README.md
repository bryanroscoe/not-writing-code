# Course: A Brief Introduction to Not Writing Code

This is a proposal for an upper-level undergraduate CS elective, not an approved course anywhere. Bracketed placeholders mark what an adopting department fills in.

*Last checked November 8, 2026.*

A course built from this knowledge base's [modules](../modules/), in six units: a one-hour orientation, then one unit for each of the five stages. The units are sized by content, so the course fits a semester, a short intensive, or self-paced study. Students build real software with coding agents and answer for every line. They specify the work, write tests first, verify and review changes, check security, and explain the code. Some work is AI-free on purpose. In an optional capstone, teams ship a small, real app.

You need one frontier coding-agent plan (about $20/month as of November 2026) or an institutional license. No GPU, no model downloads, no API keys.

## Files

| File | For | What it is |
| --- | --- | --- |
| [syllabus.md](syllabus.md) | Students, instructors, committees | The unit-by-unit outline and workload, the optional capstone, assessment, and the AI-use policy |
| [instructor-guide.md](instructor-guide.md) | Instructors and TAs | Unit-by-unit teaching notes and demos, grading AI-assisted work, walkthroughs, and the refresh checklist |
| [labs/lab-01-tokens-and-temperature.md](labs/lab-01-tokens-and-temperature.md) | Unit 1 | Predict and measure tokenization, simulate temperature, probe hallucination and sycophancy |
| [labs/lab-02-first-agent-session.md](labs/lab-02-first-agent-session.md) | Unit 3 | Install an agent, learn its permission modes, measure context, make one tested change |
| [labs/lab-03-plan-test-build.md](labs/lab-03-plan-test-build.md) | Unit 3 | The full explore → plan → implement → verify → commit loop, with your own tests as the contract and hidden tests for grading; an optional verifier-loop extension for Unit 4 |
| [labs/lab-04-review-ai-code.md](labs/lab-04-review-ai-code.md) | Unit 4 | Plant five bugs for a partner; review by hand, then with AI; verify and score every finding |
| [labs/lab-05-prompt-injection.md](labs/lab-05-prompt-injection.md) | Unit 4 | Inject your own agent in a sandbox with a fake canary, then apply defenses one at a time. Strict safety rules |
| [labs/lab-06-your-own-eval.md](labs/lab-06-your-own-eval.md) | Unit 3, finishing in Unit 4 | Your own eval, and the capstone's eval set when there is one: golden tasks from the project's history or the eval starter, two configurations, hidden tests kept away from the agents, blind scoring, error bars |
| [labs/lab-07-multi-agent-review.md](labs/lab-07-multi-agent-review.md) | Unit 4 | Multi-agent review, and the capstone's cross-model review when there is one: a hand-built review swarm with adversarial verification on a teammate's or classmate's change, measured against one ordinary review |
| [labs/lab-08-open-source-contribution.md](labs/lab-08-open-source-contribution.md) | Unit 5, starting in Unit 4 | One small, disclosed contribution to a project with a written AI policy, after a maintainer's go-ahead; a private class-run repository as the fallback or by choice |

Each lab has a goal, setup, step-by-step instructions, what to submit, a rubric, and instructor notes.

## Before the first term

The readings and assignment instructions are written. Before teaching the course, a department still needs to build and test the lab infrastructure:

- Starter repos for the labs and the capstone, the Lab 5 sandbox image, the Lab 6 run and grading launchers, and the broken toy project for Unit 4's verifier-loop activity. Dry-run all of them.
- Student access to a frontier coding agent, through institutional licenses or the roughly $20/month individual plan, and a check that it covers the labs' usage.
- A small pilot of Units 3 and 4, the heaviest stretch, recording active time, waiting time, and quota use.

## Where to start

- Students read the [syllabus](syllabus.md), then the [student path](../paths/students.md), which follows the same order.
- Instructors start with the [instructor guide's "Before the term"](instructor-guide.md#before-the-term) list, then the [refresh checklist](instructor-guide.md#refresh-checklist-for-each-term).
- On your own, do the labs in the order the units list them, which isn't numerical: Lab 6 comes after Labs 2 and 3. Lab 4's swap and Lab 3's hidden tests need a partner, so find one or use the self-paced option. Lab 3 has [fallback features and a holdout-test method](labs/lab-03-plan-test-build.md#self-paced-hidden-tests), and Labs 6 and 7 work on any project of your own. Lab 8 has no class repository or pre-flight check without a course, so contribute upstream only and have someone experienced read your diff first.

### Self-paced: don't skip Lab 5's safety review

In a course, the instructor approves your Lab 5 sandbox before you run any injection. On your own, nobody does, so work through Lab 5's [sandbox check](labs/lab-05-prompt-injection.md#sandbox-check-before-step-3) yourself before you start step 3. Skipping it is how a harmless exercise turns into an agent that reads your real files.

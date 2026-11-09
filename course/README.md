# Course: A Brief Introduction to Not Writing Code

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
| [labs/lab-06-your-own-eval.md](labs/lab-06-your-own-eval.md) | Week 10 | The term project's eval set: golden tasks from the project's history, two configurations, hidden tests kept away from the agents, blind scoring, error bars |
| [labs/lab-07-multi-agent-review.md](labs/lab-07-multi-agent-review.md) | Week 11 | The term project's cross-model review: a hand-built review swarm with adversarial verification on a teammate's PR, measured against one ordinary review |
| [labs/lab-08-open-source-contribution.md](labs/lab-08-open-source-contribution.md) | Weeks 9–14 | One small, disclosed contribution to a project with a written AI policy, after a maintainer's go-ahead; a private class-run repository as the fallback or by choice |

## Where to start

- **Students:** the [syllabus](syllabus.md), then the [student path](../paths/students.md), which follows the same order.
- **Instructors:** the [instructor guide's "Before the term"](instructor-guide.md#before-the-term) list, then the [refresh checklist](instructor-guide.md#refresh-checklist-for-each-term).
- **Self-paced learners:** do the labs in order. Find a study partner for the parts that need one (Lab 4's swap, Lab 3's hidden tests), or use each lab's self-paced option: Lab 3 has [fallback features and a holdout-test method](labs/lab-03-plan-test-build.md#self-paced-hidden-tests), and Labs 6 and 7 work on any project of your own. There's no class repository or pre-flight check for Lab 8, so contribute upstream only, and have someone experienced read your diff first.

### Self-paced: don't skip Lab 5's safety review

In a course, the instructor approves your Lab 5 sandbox before you run any injection. On your own, nobody does, so **do the review yourself and don't start step 3 until every box is checked.** Skipping it is how a harmless exercise turns into an agent that reads your real files.

- [ ] I'm working in a container, a VM, or a vendor's cloud agent environment on a private throwaway repository, not my everyday environment.
- [ ] Only the toy repository's folder is shared with the sandbox: no home directory, no SSH agent forwarding, no git credential helper.
- [ ] Inside the sandbox, `ls -la ~` shows none of my files, and `env | grep -i -E 'token|key|secret|pass'` shows nothing I recognize as a real credential (Lab 5, step 1).
- [ ] The only "secret" anywhere in the sandbox is the canary value I invented.
- [ ] Every payload I plan to plant refers only to the canary file and files inside the toy repository. None contains a URL, host, IP address, email address, network command, real file path, or destructive command.
- [ ] The repository stays local or private, and I won't publish a payload anywhere.
- [ ] I'll use a permission mode that asks me before acting, and an auto-approve mode only inside this sandbox.
- [ ] I know how to stop: interrupt the session, sign the agent out, and delete the sandbox (`docker rm -f lab5`, or delete the VM).
- [ ] I've read [the safety and ethics rules](labs/lab-05-prompt-injection.md#safety-and-ethics-rules) and signed the acknowledgment.

If you can't check a box, stop and fix it, or ask someone experienced to look at your setup first.

Every lab follows the same shape: goal, time, setup, background reading, step-by-step instructions, what to submit, a grading rubric, an "if you finish early" extension, and instructor notes on common pitfalls.

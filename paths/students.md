# Student path

This path is for university students, bootcamp learners, and anyone who can program a little and has used ChatGPT but not a coding agent. It follows the same units as the [course syllabus](../course/syllabus.md). Self-paced, it's about 20 hours of reading plus the labs.

## What you'll be able to do at the end

- Explain what a language model is and isn't, well enough to predict where it will fail.
- Explain how a model gets trained and run, and why a model trained against tests sometimes games yours.
- Use a coding agent to explore, plan, build, test, and review a small project, while understanding every line you submit.
- Give an agent checks it can run, and know what passing them does and doesn't prove.
- Tell a good model claim from marketing, and test a model on your own tasks.
- Recognize prompt-injection risks and limit what an agent can access or change.
- Use AI in a way that makes you a *better* programmer, not a dependent one.

## How to read each module

Every module has three depth levels. On this path, read Foundations and In practice, and skim Going deeper unless a topic grabs you or the syllabus says to read it. Do the short "Try it" exercises to practice what you've read. Read every TL;DR and Bryan's take too.

## The path

Read the stages in order. A few sections come early because a lab needs them, and the list says where.

### Orientation

- [00 Orientation](../modules/00-orientation.md): "AI-accelerated coding, not vibe coding," the six durable ideas, ground rules.
- From [18 Learning, careers, and responsibility](../modules/18-learning-careers-and-responsibility.md), read "How to learn with AI" and "Academic integrity" now. You'll come back for the rest at the end.

### Stage 1: How the machine works

- [01 What is an LLM?](../modules/01-what-is-an-llm.md): next-token prediction, tokens, "What an LLM is not," hallucination. Then do [Lab 1](../course/labs/lab-01-tokens-and-temperature.md).
- [02 How a model is made](../modules/02-how-a-model-is-made.md): the pipeline at a glance, the hardware (why generating text waits on memory), distillation.
- [03 Post-training and RL](../modules/03-post-training-and-rl.md): RL in five minutes, RLVR, reward hacking, "Should you fine-tune at all?"
- [04 Model safety and alignment](../modules/04-model-safety-and-alignment.md): safety vs security vs alignment, "Always ask where," why your coding agent sometimes cheats.

### Stage 2: Choosing a model

- [05 The model landscape](../modules/05-model-landscape.md): how to read model names and tiers, "Best model for the job."
- [06 Open vs closed weights](../modules/06-open-vs-closed-weights.md): the openness spectrum, licenses, the hardware math.
- [07 How to tell if a model is good](../modules/07-judging-models.md): what a benchmark is, the benchmark-claim checklist, build your own eval. You'll build one in Lab 6, once you can run an agent.

### Stage 3: Working with agents

- [08 Harnesses, tools, and MCP](../modules/08-harnesses-and-tools.md): what a harness is, the short history, "A sane baseline setup." Read module 14's [student checklist](../modules/14-security-and-prompt-injection.md#student-checklist) before you run an agent, then do [Lab 2](../course/labs/lab-02-first-agent-session.md).
- [09 Context engineering](../modules/09-context-engineering.md): prompting basics, what fills the context window, context limits.
- [10 Agentic workflows](../modules/10-agentic-workflows.md): the agent loop, explore → plan → implement → verify → commit, failure modes. Read module 11's [key fact](../modules/11-verification.md#the-key-fact-the-loop-stops-when-the-model-thinks-it-is-done) and [tests as the agent's contract](../modules/11-verification.md#tests-as-the-agents-contract) too, then do [Lab 3](../course/labs/lab-03-plan-test-build.md) and [Lab 6](../course/labs/lab-06-your-own-eval.md).

### Stage 4: Trusting the output

- [11 Verification](../modules/11-verification.md): the ladder of checks, problems an agent can loop on, protecting the verifier, calibrating your own trust. Lab 3 has an optional extension that builds a loop with a verifier.
- [12 Multiple agents](../modules/12-multi-agent-systems.md): why and why not, building vs reviewing, cross-model review.
- [13 AI code review](../modules/13-ai-code-review.md): how AI reviewers work, how humans should review AI-written PRs. Do [Lab 4](../course/labs/lab-04-review-ai-code.md), then [Lab 7](../course/labs/lab-07-multi-agent-review.md).
- [14 Security and prompt injection](../modules/14-security-and-prompt-injection.md): instructions and data share one channel, the lethal trifecta. Then do [Lab 5](../course/labs/lab-05-prompt-injection.md).

### Stage 5: Practice for the long run

- [15 Costs](../modules/15-costs-subscriptions-and-apis.md): three ways to pay, why agentic coding eats tokens.
- [16 Open-source ecosystem](../modules/16-open-source-ecosystem.md): a map of the stack, etiquette, "How students can contribute." Start choosing a project for [Lab 8](../course/labs/lab-08-open-source-contribution.md) during Stage 4, since maintainers can take weeks to reply.
- [17 Keeping up](../modules/17-keeping-up.md): what stays stable, a curated information diet, a sustainable routine.
- [18 Learning, careers, and responsibility](../modules/18-learning-careers-and-responsibility.md): the rest of it, especially what the evidence says about learning, careers, and the human side.

## If you only have a weekend

Read the TL;DRs of every module, then read these five in full: [00](../modules/00-orientation.md), [01](../modules/01-what-is-an-llm.md), [10](../modules/10-agentic-workflows.md), [11](../modules/11-verification.md), and [18](../modules/18-learning-careers-and-responsibility.md). Then do [Lab 3](../course/labs/lab-03-plan-test-build.md).

## Habits to build from day one

1. Spend ten minutes on a problem before you ask an AI. You'll ask a better question, and the answer will teach you more ([module 18](../modules/18-learning-careers-and-responsibility.md)).
2. Ask for hints, not answers, when the goal is learning. Ask for answers when the goal is shipping. Know which one you're doing.
3. Read every line you submit. If you can't explain it, you don't get to submit it.
4. Make the agent prove it. "Run the tests and show me the output" beats "does it work?" ([module 11](../modules/11-verification.md#proof-of-done)).
5. Keep a "surprised me" log. Every time a model does something you didn't expect, write one line. It becomes your personal eval set ([module 07](../modules/07-judging-models.md)) and your study guide.
6. Follow your course's AI policy and say what you used. Make disclosure a professional habit.

## Where to go next

- The [engineer path](engineers.md) once you have an internship or job.
- The [papers list](../reference/papers.md), starting with the short list of eighteen.
- Contribute to an open-source project with AI help, carefully ([module 16](../modules/16-open-source-ecosystem.md)).

# Engineer path

> **For:** working software engineers who ship code daily, from "I tried Copilot in 2024 and wasn't impressed" to "I use an agent but I'm not sure I'm using it well."
> **Time:** about 6–8 hours of reading, then a two-week practice plan on your real work.

## The pitch, in one paragraph

The tools changed more in 2025–2026 than in the decade before. If your last serious try was chat-and-paste or autocomplete, you tried a different product. A modern coding agent reads your repository, runs your tests, and iterates until they pass. The skill is no longer "writing good prompts." It's controlling context, giving the agent checks it can run, reviewing efficiently, and knowing where it breaks. That's engineering, and you already have most of the instincts for it. The evidence on productivity is honestly mixed ([module 05](../modules/05-judging-models.md#real-world-productivity-evidence)), and the gains go to people with good habits. This path is about the habits.

## How to read each module

- **Skim** Foundations. You'll know some of it; read the parts you don't.
- **Read** In practice closely. It's written for you.
- **Read** Going deeper for the modules you care most about. That's where the open debates are.
- **Read** Bryan's take as one experienced practitioner's opinion, not gospel. Several are contested and the modules say so.

## The path

### Day 1: working with agents (about 3 hours)

| Module | Focus on |
| --- | --- |
| [00 Orientation](../modules/00-orientation.md) | TL;DR, "What we mean by vibe coding," the six durable ideas |
| [06 Harnesses, tools, and MCP](../modules/06-harnesses-and-tools.md) | What a harness is, MCP, the rest of the toolkit, how to choose a harness, a sane baseline setup |
| [07 Context engineering](../modules/07-context-engineering.md) | The buzzword ladder (so you can decode it), context limits in practice, the rise and fall of giant `CLAUDE.md` files |
| [08 Agentic workflows](../modules/08-agentic-workflows.md) | All of In practice; Yegge's eight stages to locate yourself; the case for and against full autonomy |

### Day 2: doing it safely and affordably (about 2 hours)

| Module | Focus on |
| --- | --- |
| [10 AI code review](../modules/10-ai-code-review.md) | The layered review workflow, how to review AI-written PRs, accountability |
| [11 Security and prompt injection](../modules/11-security-and-prompt-injection.md) | Why coding agents are the hard case, real incidents, risks specific to coding agents, team checklist |
| [12 Costs](../modules/12-costs-subscriptions-and-apis.md) | Why agentic coding eats tokens, the worked example, cost per task vs cost per token |

### Day 3: choosing and judging models (about 2 hours)

| Module | Focus on |
| --- | --- |
| [03 The model landscape](../modules/03-model-landscape.md) | Current lineups, different places in the chain, best model for the job, how to pick next month |
| [05 How to tell if a model is good](../modules/05-judging-models.md) | The benchmark-claim checklist, harness matters, benchmark-maxing, build your own eval |
| [14 Keeping up](../modules/14-keeping-up.md) | Is it the model, the task, or the harness? When to switch tools; a sustainable routine |

### Optional, by interest

| If you want to… | Read |
| --- | --- |
| Understand what's under the hood | [01 What is an LLM?](../modules/01-what-is-an-llm.md), Going deeper |
| Fine-tune or self-host | [02 Training and tuning](../modules/02-training-and-tuning.md), [04 Open vs closed weights](../modules/04-open-vs-closed-weights.md) |
| Run several agents at once | [09 Multiple agents](../modules/09-multi-agent-systems.md) |
| Use or contribute to open-source tools | [13 Open-source ecosystem](../modules/13-open-source-ecosystem.md) |
| Mentor juniors, or worry about your career | [15 Learning, careers, and responsibility](../modules/15-learning-careers-and-responsibility.md) |

## Two-week practice plan

Reading doesn't change habits. Doing it on real work does. Pick tasks from your actual backlog.

### Week 1: one supervised agent

| Day | Do this |
| --- | --- |
| 1 | Set up one CLI or IDE agent on your main repo ([module 06](../modules/06-harnesses-and-tools.md#a-sane-baseline-setup)). Ask it to explain the architecture of a part you don't know well. Check its answer against the code. |
| 2 | Give it a small bug with a reproducible failure. Make it write a failing test first, then fix it. Read the diff line by line. |
| 3 | Use plan mode (or ask for a plan before edits) on a medium task. Edit the plan before you approve it. Note what you changed and why. |
| 4 | Write a *short* project instruction file: build/test commands, two or three gotchas, nothing else ([module 07](../modules/07-context-engineering.md)). Rerun day 2's kind of task and compare. |
| 5 | Use the agent for a non-coding chore: reading logs for an incident, writing a migration script, drafting a ticket breakdown ([module 08](../modules/08-agentic-workflows.md#ai-first-beyond-writing-code)). |

### Week 2: verification, review, and a second agent

| Day | Do this |
| --- | --- |
| 6 | Before every PR, have a *fresh* agent session review your diff. Verify each finding before you act on it ([module 10](../modules/10-ai-code-review.md)). |
| 7 | Install a second agent from a different lab. Cross-review: one writes, the other reviews ([module 09](../modules/09-multi-agent-systems.md#recipe-2-cross-model-review)). |
| 8 | Run two agents in parallel on two independent tasks, each in its own git worktree ([module 08](../modules/08-agentic-workflows.md#worktrees-and-parallel-agents)). Notice where your attention becomes the bottleneck. |
| 9 | Start your golden-task file: three to five real tasks from your repo with known-good outcomes ([module 05](../modules/05-judging-models.md#build-your-own-eval)). |
| 10 | Retro: write down three things that sped you up, three that wasted time, and one rule you'll keep. Share it with your team. |

## Common traps for experienced engineers

- **Judging today's tools by 2024's.** Re-test. The gap is large.
- **Over-specifying in prose.** Long instruction files cost more context than they're worth. Prefer runnable checks and short, specific rules.
- **Under-specifying the goal.** "Fix the flaky test" leads to deleted tests. "Make this test pass reliably without changing its assertions" doesn't.
- **Reviewing less because the agent seems confident.** Confidence is a writing style, not evidence.
- **Turning on full autonomy too early.** Turn the dial up one notch at a time, only as fast as your automated checks can catch what you stop looking at ([module 08](../modules/08-agentic-workflows.md#the-autonomy-spectrum)).
- **Tool churn.** Switching tools every week feels productive and isn't. Keep one primary tool and one warm backup ([module 14](../modules/14-keeping-up.md#when-to-switch-tools)).

## Where to go next

- If you're the one pushing your team to adopt this: the [leads path](leads.md) and the [workplace playbook](../workplace/ai-first-playbook.md).
- If you want to mentor others: run a session from the [session series](../workplace/session-series.md).

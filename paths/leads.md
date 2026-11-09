# Leads path

This path is for engineering managers, tech leads, staff engineers, and anyone asked to "get the team using AI." It's about 3 hours of reading, then the [workplace playbook](../workplace/ai-first-playbook.md).

## Your job is different from your engineers'

Your engineers need to learn the tools. You need to decide which tools, under what rules, at what cost, and how you'll know whether it's working. You also have to bring along skeptics without either steamrolling them or letting the team stall. This path pulls out the parts of each module that matter for those decisions.

## The path

| Module | Read | Why it matters to you |
| --- | --- | --- |
| [00 Orientation](../modules/00-orientation.md) | All | The vocabulary, the stance ("human stays accountable"), and the ground rules you can adopt as a starting policy |
| [08 Agentic workflows](../modules/08-agentic-workflows.md) | TL;DR, The autonomy spectrum, Yegge's eight stages, Going deeper | Where your team is and where it's realistic to get. The honest case for and against full autonomy |
| [05 How to tell if a model is good](../modules/05-judging-models.md) | Real-world productivity evidence, Vibes are data too, Build your own eval | What the studies actually show, so you can set expectations and resist both hype and dismissal |
| [10 AI code review](../modules/10-ai-code-review.md) | Why it matters now, A layered review workflow, Accountability, Team metrics | Review becomes the bottleneck when AI writes code. What to measure and what not to |
| [11 Security and prompt injection](../modules/11-security-and-prompt-injection.md) | TL;DR, Real incidents, Team checklist | The risks that are actually new, and the controls you need before you widen access |
| [12 Costs](../modules/12-costs-subscriptions-and-apis.md) | Three ways to pay, the worked example, Cost per task, not cost per token, Team budgeting | Subscriptions vs API, per-seat vs pooled, and how to frame ROI honestly |
| [03 The model landscape](../modules/03-model-landscape.md) | TL;DR, Best model for the job, How to pick a model next month | Enough to make a tool decision and to know when to revisit it |
| [14 Keeping up](../modules/14-keeping-up.md) | Ups and downs are normal, When to switch tools, Team AI radar | How to keep a team current without constant churn |
| [15 Learning, careers, and responsibility](../modules/15-learning-careers-and-responsibility.md) | What the evidence says, What the evidence says about early-career jobs, Responsible use, The human side | Junior development, deskilling, data handling, and burnout from supervising many agents |

## Decisions you'll have to make

1. Which tool(s), and do we standardize? One primary agent with a second for cross-review is a good default ([module 06](../modules/06-harnesses-and-tools.md#how-to-choose-a-harness), [module 09](../modules/09-multi-agent-systems.md)).
2. How do we pay? Seats on subscription plans for daily users, and API keys with budgets for automation and CI ([module 12](../modules/12-costs-subscriptions-and-apis.md#team-budgeting)).
3. What data can go into which tool? Decide this before rollout, write it down, and get it approved ([module 15](../modules/15-learning-careers-and-responsibility.md#responsible-use), [policy template](../workplace/policy-template.md)).
4. What can agents do without a human? Start with "nothing irreversible." Widen only as sandboxing and checks mature ([module 11](../modules/11-security-and-prompt-injection.md#team-checklist)).
5. How do we review AI-written code? Same bar as human code, smaller PRs, author must be able to explain it, a different model reviews first ([module 10](../modules/10-ai-code-review.md)).
6. How will we know it's working? Track review latency, escaped defects, revert rate, and developer-reported friction. Don't track lines of code or "% AI-written" as goals ([module 10](../modules/10-ai-code-review.md#team-metrics-what-to-watch-what-not-to-measure)).
7. How do juniors still learn? Protect some AI-free or AI-as-tutor work, and pair juniors with seniors on agent sessions ([module 15](../modules/15-learning-careers-and-responsibility.md)).

## What "AI-first" should mean on your team

AI-first means reaching for AI by default and knowing when not to, without mandating usage quotas. The adoption pattern in this material is:

- A few enthusiastic engineers go first and write down what works on *your* codebase.
- The team adopts a short shared instruction file, a review rule, and a data policy.
- Everyone gets a real, paid tool. Free tiers and personal accounts create both data risk and a bad first impression.
- Wins and failures get shared in the open, including the embarrassing ones.
- Skeptics' objections get answered with evidence from your own repo, not with launch posts ([objections and answers](../workplace/objections.md)).

> **Bryan's take:** I'm one or two steps from the top of Yegge's ladder, running several agents in parallel and managing them by hand. I don't believe fully autonomous pipelines work reliably yet. For a team, that means the realistic goal right now is "every engineer is a confident supervisor of agents," not "agents replace the review process."

## Next

The [workplace playbook](../workplace/ai-first-playbook.md) has a phased rollout plan, the [session series](../workplace/session-series.md) is a ready-made internal training program, and there's a [policy template](../workplace/policy-template.md).

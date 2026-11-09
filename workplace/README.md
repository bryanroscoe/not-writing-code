# Workplace: AI-first adoption for engineering teams

> **Audience:** leads, managers, AI champions, and the skeptical engineers they work with · **Last verified:** 2026-11-08

This folder turns the [modules](../modules/) into material a team can use to adopt AI-accelerated engineering well: going AI-first while a named human stays accountable for every change. It's written for "an engineering team" in general. Adapt the examples, numbers, and placeholders to yours.

## What's here

| File | What it is | Who it's for | Use it when |
| --- | --- | --- | --- |
| [ai-first-playbook.md](ai-first-playbook.md) | A phased rollout plan: prerequisites, a champions pilot, a team-wide baseline, and advanced use. Includes a starter instruction file, a review policy for AI-written PRs, how to measure, budgeting and security summaries, the juniors-learning problem, a 30/60/90-day checklist, and how to keep current | Leads and champions | You've been asked to "get the team using AI" |
| [objections.md](objections.md) | 24 common objections from engineers and managers, each with what's true, an honest answer grounded in the modules, and an experiment to run | Champions, leads, and skeptics | Someone says "it hallucinates," "METR says it's slower," or "security will never approve it" |
| [session-series.md](session-series.md) | An eight-session internal training series (45–60 minutes each), from a demo-first pitch for skeptics to running agents in parallel with cross-model review. Every session has a pre-read, a timed agenda, a demo script, and a hands-on exercise on your own repository | Champions who facilitate | Phase 2 of the rollout, or any time you want to run lunch-and-learns |
| [policy-template.md](policy-template.md) | A fill-in-the-blanks team AI usage policy: approved tools, data classes, required settings, human approval for irreversible actions, review, disclosure, secrets, open source, automation, IP, incidents, and review cadence | Leads, with security, legal, and privacy | Phase 0, before anyone uses AI on company code. **Not legal advice** |

## Suggested order

**If you're a lead:**
1. The [leads path](../paths/leads.md) (about three hours of module reading).
2. The [playbook](ai-first-playbook.md), start to finish.
3. The [policy template](policy-template.md), filled in and sent for review.
4. Skim the [objections](objections.md) so you know what's coming.

**If you're a champion:**
1. The [engineer path](../paths/engineers.md), including its two-week practice plan.
2. The [playbook's Phase 1](ai-first-playbook.md#phase-1-champions-pilot), which is your pilot.
3. The [session series](session-series.md), starting with [Session 0](session-series.md#session-0-watch-it-work-on-our-code).
4. The [objections](objections.md), before every session.

**If you're a skeptic:** start with the [objections](objections.md). Each one begins with what your side gets right.

## Principles behind this material

- **AI-first, not AI-only.** Reach for the tool by default, and keep the skills to work without it ([module 15](../modules/15-learning-careers-and-responsibility.md#the-human-side)).
- **A human owns every change.** Tools can write, review, and fix. A person approves and answers for the result ([module 10](../modules/10-ai-code-review.md#accountability-the-human-who-merges-owns-it)).
- **Evidence over enthusiasm.** The productivity research is mixed ([module 05](../modules/05-judging-models.md#real-world-productivity-evidence)). Measure your own team.
- **Opinions are labelled.** Bryan Roscoe's views appear as "Bryan's take" callouts. Everything else links to a sourced module section.

## Keeping it fresh

Prices, plans, and model names here are as of November 2026 and live mainly in [module 03](../modules/03-model-landscape.md) and [module 12](../modules/12-costs-subscriptions-and-apis.md). The practices change more slowly. Review your copies of these documents quarterly, alongside your team AI radar ([module 14](../modules/14-keeping-up.md#team-ai-radar)).

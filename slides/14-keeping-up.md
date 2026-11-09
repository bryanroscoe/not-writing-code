---
marp: true
theme: not-writing-code
paginate: true
title: "14: Keeping up without drowning"
description: "Velocity, regressions, launch claims, and a routine you can sustain"
footer: "A Brief Introduction to Not Writing Code · 14 Keeping up"
---

<!-- _class: lead -->

# 14: Keeping up without drowning

How to follow a field that ships every week, and when to ignore it

<!--
We'll work out a weekly routine you can keep up, a checklist for "it feels worse," a way to weigh launch claims, and a reason to keep a second tool ready.

Incidents and dates are as of November 2026. These habits should help with later releases too.

The reading is module 14. Students, read Foundations, the information diet, and the sustainable routine. Engineers, all of In practice, especially the model-task-harness checklist. Leads, the team AI radar and when to switch tools.
-->

---

# Why this matters

- A major model, tool, or benchmark ships almost every week
- You can't track all of it, and you don't need to
- Quality goes up *and* down, usually for reasons outside the model
- Access can vanish overnight for non-technical reasons
- The fundamentals change slowly, so build on those

<!--
The fundamentals the module names are context, verification, security, and review.

Every major vendor has had stretches where its model or tool got worse. The documented causes were mostly infrastructure bugs, harness changes, or product decisions, not "the model got dumber."

And Claude Fable 5 was suspended for all users from June 12 to July 1, 2026, for reasons that had nothing to do with quality. It's in the field guide later.
-->

---

# How fast it moves: three months of 2026

| Date (2026) | What shipped |
| --- | --- |
| Jul 24 | Claude Opus 5 |
| Jul 30, Aug 28 | Terminal-Bench 3.0, then 4.0 replaces it |
| Sep 1, Sep 3 | Claude Fable 5.1; OpenAI's GPT-6 Astra |
| Sep 22 | Claude Opus 5.5 and GPT-6 Sol and Luna, same day |
| October | Google's Gemini 4 models |

Codex CLI was at version 0.167 by November 6, 2026.

<!--
This is one window as an example; the full record is in the course timeline.

Terminal-Bench 4.0 recalibrated time and compute limits and dropped saturated and flawed tasks, a month after 3.0 shipped.

Harnesses ship constantly too: Claude Code's changelog moves just as quickly as Codex CLI's.

Even the yardsticks move. Artificial Analysis revised its Intelligence Index twelve times between August 2025 and November 2026, eight of them changing which evaluations it includes.

For which models lead where right now, see module 03. This session is about coping with the pace.
-->

---

# What stays stable

| Durable skill | Why it survives |
| --- | --- |
| Giving the model the right context | Every model is limited by what you show it |
| Verifying output | Models remain confidently wrong some of the time |
| Security habits | Attacks target the agent pattern, not one model |
| Breaking work into checkable steps | Reliability falls with task length, for every model |
| Your own eval set | Tells you what any release means for your work |
| Cost awareness | Prices change; the habit of measuring doesn't |

For any technique, ask: *will this still matter after the next model?*

<!--
Where each is covered: context in module 07; verification (tests, review, running the code) in module 10; security habits (sandboxing, least privilege, injection awareness) in module 11; checkable steps in module 08; your own eval set in module 05; cost awareness in module 12.

For example, "Write a clear spec and a test first" passes. "Use this magic phrase to make Model X behave" usually doesn't.
-->

---

<!-- _class: divider -->

# Ups and downs

Quality changes, and it's usually not the weights

<!--
We'll look at documented quality problems and what to check when your tool feels worse.
-->

---

# Quality comes from a stack of layers

| Layer | What can change without notice |
| --- | --- |
| You | Task, prompt, session length, repo size |
| Harness | CLI or IDE version, system prompt, default effort, MCP servers, compaction |
| Product | Plan, usage limits, model routing, model picker |
| Serving | Hardware, load balancing, sampling code, caching |
| Model | Weights and version |

People blame the bottom row. Documented causes sat more often in the middle.

<!--
Read it top to bottom: what you experience passes through every layer before it reaches the model.

People usually say "they nerfed the model," which blames the bottom layer. In the documented incidents on the next slide, the cause was more often in the harness, product, or serving layers.
-->

---

# A field guide to recent ups and downs

| When | What users saw | Cause, per the company |
| --- | --- | --- |
| Apr 2025 | Sycophantic GPT-4o, rolled back in days | Overweighted short-term user feedback |
| Aug–Sep 2025 | Worse Claude answers for weeks | Three infrastructure bugs |
| Sep–Oct 2025 | Codex "got worse" | No single cause: hardware, compaction, a sampling bug |
| Mar–Apr 2026 | Six weeks of Claude Code complaints | Three product-layer changes; weights unaffected |
| Jun–Jul 2026 | Claude Fable 5 suspended for all users | US export controls |
| Jul–Sep 2026 | Opus 5: strong benchmarks, mixed reviews | Behavior: verbosity, scope, communication |

<!--
Here's what happened in each case:

GPT-4o sycophancy (April 2025): the update flattered users and agreed with bad ideas. Expert testers' unease was a better signal than A/B metrics.

Claude, August–September 2025: a context-window routing error, output corruption from a misconfiguration, and a TPU compiler miscompilation (Anthropic postmortem, September 17, 2025). The lab's own evals missed it; user reports were right.

Codex, September–October 2025: no single cause. Some older hardware, long sessions degraded by repeated compaction, a sampling bug, and changing usage patterns such as more MCP tools (OpenAI Codex team, October 31, 2025). Long, cluttered sessions hurt; keep conversations short and focused.

Claude Code, March–April 2026: a lower default reasoning effort, a bug that wiped the model's reasoning history every turn, and a verbosity-limiting system prompt. API and weights were unaffected (Anthropic, April 23, 2026). The harness can regress while the model doesn't.

Fable 5, June 12 to July 1, 2026: US export controls applied immediately, and Anthropic had no real-time way to verify nationality.

Opus 5 to Opus 5.5: Opus 5.5, eight weeks after Opus 5, was widely liked. Newer isn't always better for you; test before switching.

Off the slide: Anthropic's weekly usage limits (announced July 2025, started August 28) show that plans and quotas are part of your tool. GPT-5's launch in August 2025 removed older models from ChatGPT's picker; OpenAI restored GPT-4o for paid users within days, and Sam Altman called sudden deprecation a mistake. On May 16, 2026, [Tibo Sottiaux said](https://x.com/thsottiaux/status/2055446089957036402) two fixed issues could explain the preceding ~48 hours of GPT-5.5 degradation in Codex, with monitoring still underway. He later [confirmed a usage-limit reset](https://x.com/thsottiaux/status/2055707616605835333). No detailed public postmortem was found.
-->

---

# Two lessons from the record

- Labs' own monitoring often missed what users noticed
- Anthropic, 2025: its evaluations "simply didn't capture the degradation"
- Stated causes were rarely "we made it worse on purpose"
- You can't verify a vendor's promise. You can verify your golden tasks.

<!--
Anthropic's 2026 postmortem said the issues "were challenging to distinguish from normal variation in user feedback at first."

As for "on purpose," Anthropic wrote that it "never reduce[s] model quality due to demand, time of day, or server load." You can't independently verify a statement like that. You can verify your own golden tasks.

Why regressions are hard to detect even for labs, per the two Anthropic postmortems and the Codex report: privacy controls limit how engineers can look at real sessions; noisy evals can't separate a 3% drop from normal variation (one ablation in April 2026 showed a 3% drop only after weeks of reports); overlapping changes on different schedules hit different users; and staged rollouts mean you and a coworker may run different versions on the same day.

In response, Anthropic committed to broader per-model evals for every system-prompt change, soak periods, and more staff using the exact public builds. OpenAI moved all internal Codex use to the same setup as external users. Both admit internal users had been seeing a different product.
-->

---

<!-- _class: take -->

## Claude and Codex

> **Bryan's take:** Claude and Codex have both had ups and downs.

<!--
That's from daily use, and the documented record backs it up for both vendors: see the Claude and Codex rows in the field guide.

The practical response is to keep more than one tool usable, which comes up two slides from here.
-->

---

# It feels worse: check in this order

| Check | If yes |
| --- | --- |
| 1. Status page or incident report? | Wait it out, or switch tools for now |
| 2. Did your harness version, plan, defaults, or MCP setup change? | Pin or roll back; rerun a 5-task smoke test |
| 3. Are golden tasks passing less often than usual? | Likely a real regression: collect specifics, report, consider switching |
| 4. Is today's task harder: bigger repo, longer session, vaguer spec? | Fix the context: fresh session, smaller step, clearer spec |
| None of these | Log it in your vibes log; recheck in a week |

<!--
Work down the table in order and stop at the first "yes."

In more detail:
- Status pages: Claude, OpenAI, and your IDE vendor's.
- Did your tool auto-update? Check its version and changelog. Did the default model, effort level, or context setting change?
- Did you change something? New MCP servers, a longer AGENTS.md, a bigger monorepo, a new plugin. OpenAI's Codex investigation found evals favored minimal setups and short, focused conversations.
- Session length: a two-hour session with several compactions is a different, harder task than a fresh one. Start over before you blame the model.
- Is it you, or everyone? Specific, reproducible reports from people you trust beat a trending "it's nerfed" thread.
- API vs app: if you have API access, run a pinned, dated model snapshot on the same task. If the API is fine and the app isn't, the problem is in the product layer.
-->

---

# When to switch tools

| Good reasons | Bad reasons |
| --- | --- |
| Golden tasks drop in two runs, a week apart | One bad afternoon |
| A rival beats yours beyond your error bar, affordably | A launch-day benchmark chart |
| Pricing, limits, data policy, or security changed | A viral thread |
| A long bad stretch: no fix, no postmortem, no word | Fear of missing out |

Always keep a second tool warm.

<!--
Switching has a cost: new habits, new configuration, new failure modes. Switch when the evidence is strong.

"Warm" means installed, configured, and used at least occasionally. The Fable 5 suspension and the 2025–2026 regressions all hit people who had only one option. Keeping another vendor's tool usable is cheap insurance and makes multi-model review possible (module 10).
-->

---

<!-- _class: divider -->

# Filtering the noise

Launch claims, sources, and a routine you can keep

<!--
Most of what you'll read about AI is a launch post, a reaction to one, or a rumor. You only need to follow a small part of it.
-->

---

# Weighing launch claims

- Self-reported benchmarks? Which harness and settings?
- What was dropped since the last comparison? Who's missing?
- Is the demo live, edited, or sped up?
- "Available today" may mean a limited set of organizations
- Customer quotes and internal runs are testimonials, not tests
- Wait for independent numbers; they usually come within days

<!--
A launch post is marketing written by people who also do science. Read it the way you'd read any vendor's claims.

Are competitors' benchmark numbers run the same way, or copied from their own launch posts? Module 05 has a full checklist.

Demos show the best of many tries.

[OpenAI's GPT-6 Astra launch](https://openai.com/index/gpt-6-astra/) in September 2026 started with a limited set of organizations.

Customer quotes usually come from partners with early access, and launch posts rarely say whether anyone checked the figures. Treat lab-run numbers the same way: Anthropic's Opus 5 post labels its headline Frontier-Bench results "an internal run."

Independent evaluators include Artificial Analysis, Epoch AI, Arena, and others.
-->

---

# Every lab has a mixed record

| Lab | A documented episode |
| --- | --- |
| Meta | Apr 2025: promoted the Arena rank of a chat-tuned experimental variant |
| xAI | Jul 2025: the `@grok` account posted antisemitic content for about 16 hours |
| OpenAI | Feb 2026: publicly retired SWE-bench Verified, its own benchmark, after an audit |
| Anthropic | Detailed postmortems in 2025 and 2026, after users noticed first |

Judge each on replication, honesty about regressions, demos vs product, stable pricing.

<!--
The module's four tests are how launch numbers survive independent testing, how honestly they handle regressions, whether demos match the shipped product, and how stable their pricing and limits are.

Meta: the Llama 4 launch promoted a ranking earned by an experimental variant tuned for chat, not the released model. Arena said Meta's interpretation of its policy didn't match what it expects from providers.

xAI: in February 2025, the Grok 3 launch chart left out o3-mini-high's majority-vote (cons@64) score; an OpenAI employee called it misleading and xAI disputed that. In its [May 2025 statement](https://x.com/xai/status/1923183620606619649), xAI blamed Grok's unprompted conspiracy-theory replies on an "unauthorized modification" of its system prompt. The July 2025 posts followed a code change; xAI apologized and said it would publish the bot's system prompt on GitHub.

OpenAI has the GPT-4o sycophancy rollback and the GPT-5 model-picker reversal against it. In its favor, it retired SWE-bench Verified after [an audit](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/) found material flaws in 59.4% of 138 tasks o3 did not consistently solve, alongside contamination evidence, and published the detailed "Ghosts in the Codex Machine" investigation (October 2025). The May 2026 Codex episode got no comparable write-up.

Anthropic: the postmortems came after weeks in which users noticed problems first. And the Opus 5 launch, whose strong benchmarks didn't match a lot of users' daily experience.

The module is explicit about bias here: my opinions come from daily use, mostly of Claude and Codex, and reflect that lens.
-->

---

<!-- _class: take -->

## Google's launch claims

> **Bryan's take:** I don't trust Google's launch claims much. In my experience they overhype Gemini, and it underperforms what was promised, especially for coding. I'll use Gemini for some specific tasks, but not as my coding agent.

<!--
That's from my own use. The module follows it right away with the documented record, which cuts both ways, on the next slide.
-->

---

# Google: the record cuts both ways

| Against | For |
| --- | --- |
| Dec 2023: the "Hands-on with Gemini" video was staged | Jul 2025: IMO gold, certified by IMO coordinators |
| Jun 2026: Gemini 3.1 trailed GPT-5.5 on Harbor-Index, though no comparison was statistically significant | Nov 2025: Gemini 3 Pro topped Arena at launch |
| | Nov 2026: Gemini 4 Carbon #1 on Arena's text leaderboard (preliminary) |

Your golden tasks will tell you whether it shows up in *your* work.

<!--
Against: Google acknowledged it had fed the model still frames and text prompts rather than live video and voice (TechCrunch, December 2023). The June 2026 comparison was the Terminal-Bench team's Harbor-Index, in both a native and a neutral harness; the post notes none of its pairwise comparisons reached statistical significance.

For: Google DeepMind's International Mathematical Olympiad gold-medal result was "officially graded and certified by IMO coordinators," a higher bar of verification than many lab claims get. As of November 8, 2026, Gemini 4 Carbon (High) is number one on [Arena's text leaderboard](https://arena.ai/leaderboard/text), with its rating still marked preliminary. Google also reports a leading Terminal-Bench 4.0 score for it, as run by Artificial Analysis.

An afternoon with your golden tasks will tell you whether that helps your coding work.
-->

---

# An information diet: pick two or three sources

| Source | Good for | Keep in mind |
| --- | --- | --- |
| Simon Willison's Weblog | Fast hands-on notes; security | Enthusiast who often gets early access |
| Latent Space | Long interviews with builders | Industry insider |
| Interconnects | Post-training and open models | Open-model advocate |
| The Pragmatic Engineer | How real teams use AI | Big-tech lens; deep dives paywalled |
| METR, Epoch AI | Data, trends, studies | Risk or quantitative focus |
| Changelogs, status pages | What actually shipped | Silent about what got worse |

Never cite SEO or auto-generated "AI news" sites.

<!--
This is a selection from the module's table, which also lists Import AI (Jack Clark, who co-founded Anthropic), One Useful Thing (Ethan Mollick), Zvi Mowshowitz's weekly roundups, Hacker News, r/LocalLLaMA, AI Engineer conference talks, and Andrej Karpathy, who coined "vibe coding" in February 2025. Add the changelogs of the tools you use.

Every source type has a bias. Labs are authoritative on what they shipped and selective about how good it is. Independent evaluators are consistent but bound to benchmarks, and some have commercial ties. Individual writers curate well, have viewpoints, and sometimes get early access that shapes their tone. Communities (HN, Reddit, X) are fastest and noisiest; they amplify both "it's amazing" and "it's nerfed."

SEO and auto-generated "AI news" sites are the worst. While researching the module, the authors found many that invented or garbled model details.

Watch for rumor laundering: an anonymous post becomes a blog post, the blog post becomes an "AI news" article with invented specifics, and the article becomes "reported." When a claim matters, trace it to a primary source.
-->

---

# A sustainable routine

| Cadence | Time | What to do |
| --- | --- | --- |
| Weekly | 30 min | Tool changelogs (10 min), one or two newsletters (15), one try-list item (5) |
| Monthly | 60–90 min | Run golden tasks on one or two releases; record the result; drop one unused tool |
| Quarterly | Half a day | Cost vs value, refresh golden tasks, review security, update the radar |

<!--
Weekly: changelogs for the two or three tools you use; one or two newsletters from the list; add at most one item to a "try list."

Monthly: pick the one or two releases from the try list most relevant to your work and run your golden tasks on them (module 05). Write down the result even if it's "no change." Remove one tool, plugin, or MCP server you no longer use.

Quarterly: tool review of what you pay vs what you get (module 12); refresh the golden tasks by retiring leaked ones and adding recent work; review security settings (module 11); update the team radar.
-->

---

# Rules that prevent churn

- Wait two weeks, unless it solves a problem you have today
- Change one thing at a time: model, harness, or config, not all three
- It has to win on your tasks before you switch
- Ignore small benchmark moves; a few points is noise for you
- Mute sources that mostly make you anxious

<!--
In two weeks, launch-week bugs get fixed, capacity improves, and the reaction settles. Opus 5's reputation looked very different at week two than on day one.

If you change model, harness, and configuration in the same week, you won't know what helped.

Mute freely. You'll hear about anything big anyway.

On fear of missing out, most releases don't change how you work. The few that do will still be there in two weeks, with better documentation and fewer bugs. Your ability to judge output is worth more than tracking every new product.
-->

---

# A team AI radar

| Ring | Meaning |
| --- | --- |
| Adopt | Proven on our golden tasks; the recommended default |
| Trial | Promising; a few people use it on real work |
| Assess | Worth an afternoon; someone is testing it |
| Hold | Don't start new work with it, and say why |

Rotate a monthly scout. Items move at most one ring per review, with evidence.

<!--
The format is borrowed from the Thoughtworks Technology Radar. One person can't track everything; a team can share the load.

To run it, keep a docs/ai-radar.md file in a shared repo. Rotate a "scout" each month who skims sources, proposes items, and runs the afternoon eval on anything promising. Hold a 30-minute monthly review; each item moves at most one ring per review, and only with evidence. Every entry has an owner and a revisit date.

The module has an example radar file with columns for item, ring, since, evidence, owner, and revisit, for example an agent CLI at Adopt with a golden-set score as its evidence, and auto-merge of agent PRs on Hold after two incidents.

For leads, the radar doubles as the record of why the team uses what it uses, which helps with budget conversations and onboarding.
-->

---

# Evaluating a new release in an afternoon

| Time | Step |
| --- | --- |
| 0:00–0:20 | Read the claims; pick two or three to test |
| 0:20–0:40 | Check independent signals |
| 0:40–2:30 | Run 10 golden tasks in your real harness, graded blind |
| 2:30–3:15 | Try one real task from this week's backlog |
| 3:15–3:45 | Measure cost, quota, and speed per task |
| 3:45–4:00 | Decide: Adopt, Trial, Assess again in two weeks, or Hold |

A close result means "not yet."

<!--
A four-hour, time-boxed plan. You need the golden-task set from module 05.

Read the claims: launch post, pricing, limits, availability, and the system card's limitations and benchmark footnotes. Write down specific claims to test, such as "better at long refactors" or "40% cheaper."

Independent signals: Artificial Analysis, Arena, Epoch AI, and reactions from two or three people you trust. If nothing independent exists yet, note that and lower your confidence.

Run the golden subset with your default settings. Run the current default on the same tasks if you don't have recent results. Blind the outputs and grade with the rubric.

On the real task, watch how it works. Does it stay in scope, ask good questions, explain itself honestly? Add notes to your vibes log.

Record the decision in three sentences, with the evidence and a revisit date. Update the radar. If the result is close, revisit in two weeks.
-->

---

<!-- _class: take -->

## The pace itself

> **Bryan's take:** The rapidly changing nature of all this is interesting too.

<!--
My other takes for this module, on Claude's and Codex's ups and downs and on Google's launch claims, came earlier, next to the evidence.

Whatever you think of these labs, one bad release doesn't mean a lab has lost its way, and one great benchmark chart doesn't mean a model is better to work with. Both are reasons to test on your own tasks before switching.
-->

---

# Try it

On your own (about an hour, then ongoing):

- Subscribe to two sources; bookmark your tools' changelogs and status pages
- Start a `vibes-log.md`: date, model, harness and version, task, result
- Log five entries in two weeks, then run a short afternoon eval

As a class or team, start an AI radar, or present one incident from the field guide.

<!--
The afternoon evaluation can be a shortened version with five golden tasks. Run it on the most recent release relevant to you.

For a team (one session plus a month), agree on the four rings, list current tools, and place each with whatever evidence you have. Assign a scout for the month. At the end of the month, the scout presents one release they evaluated, with golden-task results, and the group decides whether anything moves.

In a class, give each group a different 2025–2026 incident from the field guide. Each group reads the primary postmortem or report, then presents what users saw, what actually caused it, and what check would have caught it sooner.
-->

---

# Discussion

1. Most incidents weren't in the weights. Why do people blame the model first?
2. How could an outside user test "we never degrade quality due to demand"?
3. How much time should engineers spend keeping up weekly? On company time?
4. How do you tell healthy experimentation from tool churn on a team?

<!--
Fuller versions from the module:

1. In most of the documented incidents, the cause was in the harness, product, or serving layer, not the model weights. Why do people still blame the model first?
2. Anthropic says it never degrades model quality due to demand. How could an outside user test a claim like that?
3. What's the right amount of time for an engineer to spend keeping up each week? Should it be on company time?
4. How would you tell the difference between healthy experimentation and tool churn on your team?

More if time allows: pick a lab and argue for and against trusting its next launch claims, using only documented episodes. The Fable 5 suspension had nothing to do with model quality; what other non-technical events could take away a tool you rely on, and how would you prepare?
-->

---

# Read more

- [Module 14: Keeping up without drowning](../modules/14-keeping-up/)
- [A postmortem of three recent issues](https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues) (Anthropic, September 2025)
- [Ghosts in the Codex Machine](https://docs.google.com/document/d/1fDJc1e0itJdh0MXMFJtkRiBcxGEFtye6Xc6Ui7eMX4o/mobilebasic) (OpenAI Codex team, October 2025)
- [Thoughtworks Technology Radar](https://www.thoughtworks.com/radar)

<!--
The module links every incident report in the field guide, the launch posts it quotes, and the full information-diet table.
-->

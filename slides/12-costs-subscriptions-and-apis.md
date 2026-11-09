---
marp: true
theme: not-writing-code
paginate: true
title: "12: Costs: subscriptions vs API"
description: "What an hour with a coding agent really costs, and how to pay for it"
footer: "A Brief Introduction to Not Writing Code · 12 Costs"
---

<!-- _class: lead -->

# 12: Costs: subscriptions vs API

What an hour with a coding agent really costs, and how to pay for it

<!--
We'll estimate what an agent session costs, explain why prompt caching matters so much, and choose between a subscription and the API for a given use.

Every price here comes from the vendors' own pages, checked on 8 November 2026. Prices change often, sometimes monthly. The arithmetic still works when the prices change.

The reading is module 12. Students, read Foundations, the price snapshot, and the worked example. Engineers, all of In practice. Leads, the worked example, cost per task, team budgeting, and the counterpoints to my take.
-->

---

# Why this matters

- Agents re-send the whole conversation on every turn
- One agent hour at frontier API prices: **$24.30** uncached, **$3.73** cached
- Heavy users can burn hundreds of dollars a month on the API
- Subscription caps and terms changed several times in one year
- Leads need a cost number they can defend

<!--
Those two numbers come from the worked example later: one hour, 60 model calls, Claude Opus 5.5 list prices as of November 2026. The only difference between them is prompt caching.

Compare cost per finished task and choose a billing model that fits your use. Subscriptions suit individual interactive work. The API suits anything that runs in production, in CI, in batch, or for other users.
-->

---

# Three ways to pay

| Option | Who you pay | How it's billed | Watch out for |
| --- | --- | --- | --- |
| Chat subscription (Claude, ChatGPT) | A lab | Flat monthly fee | Caps: a few-hour window plus a weekly limit |
| Tool subscription (Cursor, GitHub Copilot) | A tool vendor | Fee with an allowance, then pay-as-you-go | Some models billed at API list price |
| API | A lab | Metered, per token | Uncapped, so the bill is too |

<!--
Chat and pro subscriptions run roughly $20 to $200 a month for individuals, more for some tiers. They include the lab's coding agent: Claude Code with a Claude plan, Codex with a ChatGPT plan. The cap is stated as a multiple ("5x Pro usage"), not as a number of tokens.

Tool vendors buy model access from the labs and resell it inside their product. Some include their own or partner models in the flat fee and charge frontier lab models at API list price.

With the API, you get a key and pay for exactly what you use, with no cap beyond rate limits. You can use any harness, build your own tools, run in CI, and ship features to customers.
-->

---

# What a token bill is made of

| Line item | Relative price |
| --- | --- |
| Input: everything you send, history and tool results included | Base price |
| Output, including thinking tokens | Usually 4–6x input |
| Cache write (a premium at Anthropic, none at OpenAI) | 1.25x for 5 minutes, 2x for 1 hour |
| Cache read: re-sending a prefix that's already cached | 2.5–10% of input |
| Batch: async jobs that finish within hours | 50% off |
| Fast / priority modes | About 2x |

Tokenizers differ. Thinking bills as output.

<!--
A token is roughly three-quarters of an English word on average. Prices are quoted per million tokens, written "MTok".

First, tokenizers differ. The same text becomes a different number of tokens on different models. Anthropic notes that its Claude 4.7-and-later tokenizer produces about 30% more tokens for the same text than earlier Claude models. A lower per-token price on a wordier tokenizer can cost the same.

Second, thinking is output. A reasoning model that thinks for 5,000 tokens before writing a 300-token answer bills you for 5,300 output tokens. Effort or thinking-budget settings change cost directly.

Some bills also add surcharges for long prompts above a threshold on some models, and for regional data residency (Anthropic's US-only inference is 1.1x).
-->

---

<!-- _class: divider -->

# Why agents eat tokens

The model is stateless, so the agent pays for its own history

<!--
This explains almost every surprising AI bill.
-->

---

# Every turn re-sends everything

```text
call 1    [prompt · tools · docs]                20,000 tokens
call 2    [prompt · tools · docs] + 1 result     22,500 tokens
  …
call 60   [prompt · tools · docs] + 59 results  167,500 tokens
```

- Total input grows with the **square** of the number of turns
- Double the session, roughly quadruple the input tokens
- Big tool outputs, retries, subagents, and parallel agents multiply it

<!--
A model API is stateless: it remembers nothing between calls. A coding agent works in a loop. The model asks to run a tool, the harness runs it, and the result goes back to the model along with everything that came before. Every turn re-sends the full context.

The numbers in the block are the assumptions from the worked example: a 20,000-token start (system prompt, tool definitions, project instructions) and 2,500 tokens added per call.

A full test log, a large file read, or a web page can add 10,000 to 100,000 tokens in one step. Retries and dead ends re-send everything again. Subagents each start their own context, often re-reading the same files. Parallel agents multiply all of it. Thinking adds output tokens on every turn.

Keep this in mind for the discussion: how would you design a harness to keep cost closer to linear?
-->

---

# Prompt caching makes it affordable

- Each call starts with the exact prefix of the last one
- The provider keeps that prefix's processed state
- Re-sending it costs a small fraction of the input price
- Claude Code and Codex cache automatically
- In your own agent, put stable content first and conversation last
- Changing the system prompt or tools mid-session breaks the cache

<!--
Caches match from the start of the prompt. Anything that changes early, such as a timestamp in the system prompt or a reordered tool list, invalidates everything after it. Put stable content first: tools, system instructions, project docs, then the conversation. On Anthropic, mark cache breakpoints or turn on automatic caching.

The cache economics, as of November 2026. Anthropic charges 1.25x input to write a 5-minute cache entry and 2x for 1 hour. Reads cost 0.1x base on most models and less on the newest: 0.05x on Opus 5.5 and Sonnet 5.5, 0.025x on Fable 5.1. A 5-minute write pays for itself after one read. OpenAI caches automatically with no write premium. Google charges for cache storage per hour on models that offer explicit caching.

For agent workloads, most input tokens are cache reads, so compare the cache-read price first, not the headline input price.
-->

---

# Worked example: one hour, the assumptions

| Assumption | Value |
| --- | --- |
| Model calls in the hour | 60, about one a minute |
| First call | 20,000 tokens |
| Context added per call | 2,500 tokens |
| Output per call, including thinking | 1,500 tokens |
| Compaction, or breaks over 5 minutes | None |
| Claude Opus 5.5 prices (as of November 2026) | $4 in · $5 cache write · $0.20 cache read · $20 out |

Totals: **5,625,000** input tokens and **90,000** output tokens.

<!--
Go through the arithmetic slowly. It's the core of the session.

Context on call i is 20,000 + 2,500 × (i − 1), so call 60 sends 167,500 tokens.

Total input = 60 × 20,000 + 2,500 × (0 + 1 + … + 59) = 1,200,000 + 2,500 × 1,770 = 5,625,000 tokens.

Total output = 60 × 1,500 = 90,000 tokens.

Swap in your own numbers from your logs. The module's Try it shows how to get them.
-->

---

# One hour on Opus 5.5: $24.30 or $3.73

| | Without caching | With caching |
| --- | --- | --- |
| Input | 5.625 MTok × $4 = $22.50 | — |
| Cache writes | — | 0.1675 MTok × $5 = $0.84 |
| Cache reads | — | 5.4575 MTok × $0.20 = $1.09 |
| Output | 0.09 MTok × $20 = $1.80 | $1.80 |
| **Total per hour** | **$24.30** | **$3.73** (85% less) |

API list prices as of November 2026.

<!--
With caching, each call reads the previous prefix from the cache and writes only the new part.

Cache writes: 20,000 tokens on the first call plus 2,500 on each of the 59 later calls = 167,500 tokens.

Cache reads: everything else, 5,625,000 − 167,500 = 5,457,500 tokens.

Look at what moved. Input fell from $22.50 to about $1.93, while output stayed at $1.80. With caching on, output is now the largest single line.
-->

---

# The same hour at other price points

| Tier (input / output) | Uncached | Cached | 168 hours a month, cached |
| --- | --- | --- | --- |
| Top tier ($10 / $50) | $60.75 | $7.96 | ~$1,340 |
| Frontier ($4 / $20) | $24.30 | $3.73 | ~$630 |
| Mid ($2 / $10) | $12.15 | $1.86 | ~$310 |

168 hours = 8 hours a day for 21 working days, one agent at a time.

<!--
Same token counts as the previous slide. Cache-read prices used: top tier $0.25, frontier $0.20, mid $0.10 per million tokens. These match Anthropic's Fable 5.1, Opus 5.5, and Sonnet 5.5 as of November 2026. Other vendors price cache reads and writes differently, so recompute with the price table in the module before comparing vendors.

The monthly column assumes one agent. Parallel agents multiply it: three agents at once is roughly three times the bill.
-->

---

# What the numbers tell you

- Caching turns "unaffordable" into "plausible"
- With caching on, output becomes the biggest line
- Heavy frontier use costs hundreds of dollars a month at API prices
- Three agents at once ≈ three times the bill
- Light users are often cheaper on the API than a $20 plan
- A cache miss on a 150,000-token context costs $0.75

<!--
This is why a $100–$200 subscription feels like a bargain to heavy users.

For light users, Anthropic's own docs use an example one-hour session of 50,000 input and 15,000 output tokens, which costs well under a dollar on Opus 5.5. If you use an agent for a few short tasks a week, pay-as-you-go may beat a $20 plan.

On cache misses, Anthropic's default cache lifetime is five minutes. Step away longer and the next call re-writes the whole prefix: 150,000 tokens at $5 per million is $0.75. Harnesses can use the 1-hour cache at twice the write price.

Measure instead of guessing. The ccusage tool, in the Try it slide, reads the usage data agent CLIs store locally.
-->

---

<!-- _class: divider -->

# Paying for it

Subscriptions, cheaper options, and cost per task

<!--
Now let's work out how to pay for it.
-->

---

# Subscriptions (as of November 2026)

| Vendor | Plan | USD a month | What the vendor says you get |
| --- | --- | --- | --- |
| Anthropic | Pro | $20 | Claude Code included |
| | Max | $100 | 5x Pro usage; $100 a month in API credits |
| | Ultra | $200 | 10x Pro per week; no 5-hour limit (verified accounts) |
| OpenAI | Plus | $20 | Codex on web, CLI, and IDE |
| | Pro | $100, $200, or $500 | Higher limits; $500 adds "Ultrafast" mode |

Individual tool plans: GitHub Copilot $10–$100, Cursor $8–$200.

<!--
Anthropic renamed Max 20x to Ultra on 30 October 2026 at the same $200 price; the old Max 5x is now just Max. [Anthropic's naming note](https://claude.com/resources/articles/create-files) dates the change, and its [Ultra help page](https://support.claude.com/en/articles/17728952-what-is-the-ultra-plan) confirms the rename and limits. Ultra also includes $200 a month in API credits. Pro is $17 a month billed annually.

OpenAI added the $100 Pro tier on 9 April 2026 and the $500 tier by late September ([OpenAI weekly update](https://learn.chatgpt.com/docs/whats-new/september-28-october-2-2026)). New $200 subscriptions have a lower allowance; eligible existing subscribers kept the old allowance only through October 29, 2026 ([Pro tier terms](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers)). Free and Go ($8) tiers give limited Codex access on a small model.

Team seats: Anthropic Team is $25 a month standard ($20 annual) and $125 premium ($100 annual). OpenAI Business is $25 ($20 annual).

On the tools, Copilot allowances are in "GitHub AI Credits" ([1 credit = $0.01](https://docs.github.com/en/copilot/concepts/billing-and-usage/individuals/billing)). Cursor [announced its shared subscription with xAI](https://forum.cursor.com/t/introducing-the-x-subscription/174450) on October 12, 2026. Plus includes Grok and Composer; third-party models on Premium and above are billed separately at API list price. Tool pricing moves fast.
-->

---

# A subscription is a flat fee with a cap

- Use less than the cap, and you overpay versus the API
- Heavy users report API-equivalent usage several times their fee
- In Aug 2025 Anthropic added weekly limits on top of 5-hour windows
- 2026 brought new tiers, renamed plans, smaller allowances for new subscribers
- "5x Pro" is a multiple, not a token count
- Rules for using a plan in third-party tools differ by vendor

<!--
Whether vendors make or lose money on heavy users isn't public.

On weekly limits, Anthropic announced on 28 July 2025 that weekly limits would start 28 August 2025 for Pro and Max. It cited users running Claude Code "continuously in the background, 24/7" and account sharing, and estimated fewer than 5% of subscribers would be affected. Its estimates then: Pro about 40–80 hours of Sonnet 4 a week; the $200 Max tier about 240–480 hours of Sonnet and 24–40 hours of Opus. Reporters calculated the "20x" plan gave about 6x Pro's Claude Code hours.

On third-party tools, as of November 2026, Anthropic says plan sign-in is for Claude Code and its own apps; products, including ones built with the Agent SDK, must use API keys. It began blocking tools that spoofed the Claude Code harness in January 2026. Running the unmodified Claude Code binary with your own subscription is allowed. OpenAI lets you sign into Codex with a plan or an API key. Its [September 28 integration guide](https://learn.chatgpt.com/cookbook/articles/sign-in-with-chatgpt) documents third-party sign-in and optional plan-usage permission for eligible Plus and Pro users. Identity sign-in and permission to spend usage are separate.

These policies changed several times in a year. If your workflow depends on a consumer plan inside a third-party tool, have a fallback.
-->

---

# Cheaper alternatives

| Option | How it saves | Watch out for |
| --- | --- | --- |
| Open-weight coding plans (GLM from $18/mo, Kimi, MiniMax) | Flat rates inside Claude Code, Codex, OpenCode, Cline | Trail the frontier on the hardest work; another provider and jurisdiction |
| Routing | Small model for easy work, frontier for hard | Small models cost 20–100x less per token than top tier |
| Local models | No per-token cost | Hardware and power; well behind for agentic coding |

<!--
Z.ai's GLM Coding Plan starts at $18 a month for the Lite tier, with 5-hour and weekly credit limits and half-price off-peak usage. Moonshot's Kimi Code Plan runs its Kimi K3-series models. MiniMax sells an M Plan for its M3-series models. They plug into popular harnesses through API-compatible endpoints. Read the data terms. The "open" part only helps you if you might self-host later (module 04).

With routing, send renaming, boilerplate, log summaries, and issue classification to a small, cheap model; keep planning, hard debugging, and review on the frontier model. Many harnesses let you set a different model for subagents.

Local models have zero marginal token cost but real hardware and electricity cost, and today's local models are well behind the frontier for agentic coding (module 04).
-->

---

# Judge cost per finished task, not per token

| Same task, both cached | Frontier model | Budget model |
| --- | --- | --- |
| Prices (input / output per MTok) | $4 / $20 | $1 / $5 |
| Calls to finish | 30 | 90 |
| Total input tokens | 1.69M | 11.81M |
| **Cost with caching** | **$1.68** | **$2.14** |
| Your attention | 1x | 3x |

A quarter of the price per token, about seven times the input tokens.

<!--
The number that matters is what it costs to get a correct, merged change.

Same growth assumptions as the hourly example: 20,000-token start, 2,500 tokens added per call, 1,500 output tokens per call. Full prices: frontier $4 input, $5 cache write, $0.20 cache read, $20 output; budget $1, $1.25, $0.10, $5. Without caching: $7.65 vs $12.49. Final context: 92,500 vs 242,500 tokens.

Three times the turns means about seven times the input tokens, because context grows every turn. The budget model also used three times as much of your attention. That costs more than anything else in the table.

The reverse also happens. For well-specified, repetitive work, such as applying the same refactor to 200 files, a small model finishes in the same number of turns, and the 20–40x price gap wins.

Thinking budgets follow the same logic: more reasoning per turn often means fewer turns. Try a task at two effort levels and compare total cost.
-->

---

# When the API is the right choice

- Production features your users trigger
- CI and automation: review bots, triage, nightly test fixes
- Batch jobs like migrations, labeling, and evals, at 50% off
- Multi-user apps, with usage attributed and limited per user
- Light or bursty individual use
- Data terms: no training by default; zero data retention available

<!--
For production, you need an API key by contract, and you want per-request metering anyway.

CI and automation run unattended and shared, which consumer terms don't allow.

On data terms, commercial API terms default to no training on your data. Some organizations require zero data retention (ZDR), which is available on commercial terms and not on consumer plans.
-->

---

# Cost controls for day one

- Spend limits and alerts per workspace, project, or key
- Separate keys per app, environment, and team
- Caching on by default, stable content first
- Small model by default; escalate on failure
- Cap `max_tokens`, effort, and turns per agent run
- Trim tool outputs, batch what can wait, review costs weekly

<!--
All major consoles have spend limits and alerts. Anthropic Enterprise and Copilot let admins set per-user and organization limits.

Separate keys let you see who spent what.

Trimming tool outputs means truncating logs and summarizing large files before they enter the context.

The weekly cost review matters most in the first month of any new agent workflow.
-->

---

<!-- _class: divider -->

# Teams and trade-offs

Pricing it in engineer-hours, and Bryan's take

<!--
We'll work out what a lead can tell leadership about costs. I'll also give my opinion on subscriptions.
-->

---

# Team math: price it in engineer-hours

| Assumption | Value |
| --- | --- |
| US median developer pay, May 2025 (BLS) | $135,980 |
| Loaded cost, about 1.4x salary | ~$190,000 a year |
| ~1,800 productive hours a year | ~$100 per engineer-hour |
| A $200-a-month seat | ~2 engineer-hours a month |
| Heavy API user, ~$630 a month | ~6 engineer-hours a month |
| 10 people on $200 seats | $24,000 a year; a 2% gain ≈ $38,000 |

The weak link is the "if": self-reported gains are unreliable.

<!--
Show your assumptions; leadership will change them, and that's the point. Loaded cost covers benefits, taxes, equipment, and overhead. The hourly figure works out to about $105; round to $100. A $20 seat costs about 12 minutes of an engineer's time a month. The 10-person team's $24,000 a year is about 13% of one loaded engineer.

The weak link is self-reporting. In METR's 2025 randomized study, experienced open-source developers using early-2025 AI tools took 19% longer on their tasks while believing they were 20% faster. Tools have changed a lot since, but the lesson about self-reports holds. Measure things you can count before and after: cycle time, review turnaround, escaped defects, rework.

On seats vs pooled, seats are predictable but you pay for light users, and heavy users still hit caps. Pooled usage tracks real use but needs budgets and alerts. Many teams mix: a standard seat for everyone, premium seats or pooled API credits for the heaviest users and for automation.

Before a rollout, get in writing: training on your content, retention and ZDR, data residency and its price, SSO, SCIM, audit logs, admin spend limits, per-user cost attribution, regulated-data coverage, and renewal pricing and notice for limit changes.
-->

---

<!-- _class: take -->

## Subscriptions vs API

> **Bryan's take:** API pricing is too expensive for heavy agentic use. Subscriptions are what make it affordable to work this way every day.

<!--
This is my opinion, from daily use.

The module's arithmetic supports it for full-time use of frontier models. Even with caching, a single heavy user can spend several hundred dollars a month at API prices, and parallel agents multiply that.

There are counterpoints worth considering too.
-->

---

# The strongest counterpoints

- Cheap until you hit the weekly limit on a Thursday
- Terms change; API prices are published per token
- You can't build on it; production and CI need the API
- Subscription value is tied to the vendor's harness
- Light users overpay; open-weight plans start under $20
- For teams, pooled API, caching, and routing can beat top-tier seats

<!--
On caps, heavy parallel use may need the top tier, extra credits, or a second vendor.

The terms keep moving. Weekly limits (2025), third-party harness restrictions (2026), and reduced allowances at existing price points (2026) all happened within about a year.

Consumer subscriptions are for an individual using the vendor's tools. Production features, CI bots, and shared automation need the API, by contract.

The API lets you switch models and harnesses freely and route cheap work to cheap models.

For teams, pooled usage plus good caching and routing can beat buying top-tier seats for everyone, especially when usage is uneven.

Which of these applies to you?
-->

---

# Try it

On your own, measure your real cost:

```bash
npx ccusage@latest daily        # Claude Code, by day
npx ccusage@latest codex daily  # Codex, by day
```

1. Use your agent normally for a week, then run ccusage
2. Compare the API-equivalent cost with what you pay
3. Find your most expensive session. What made it expensive?

As a class or team, budget a 12-person team plus a PR-review bot, three ways.

<!--
ccusage reads the usage data that Claude Code, Codex, and many other agent CLIs store locally, and prints token counts with API-equivalent costs.

Record total input, cache-read, cache-write, and output tokens, and the API-equivalent cost. Compare that with your subscription price, then recompute it for a model one tier cheaper using the price table. For your most expensive session, decide whether length, big tool outputs, retries, or parallel agents drove it, and write down one habit change that would have halved it.

For the team exercise, assume 4 heavy users, 6 moderate, 2 light, plus a PR-review bot on every pull request (about 40 a day). Price three options: all top-tier seats; standard seats plus pooled API credits for the heavy users and the bot; API only, with caching and routing. State every assumption (tokens per session, sessions per day, cache hit rate, PR size). Compute the break-even productivity gain against loaded engineer cost, and list the data-terms questions you'd send to procurement.
-->

---

# Discussion

1. Why does doubling a session more than double its cost? How would you flatten it?
2. 75% cheaper per token, three times the turns: when is it still right?
3. Should a course give students API keys, subscriptions, or neither?
4. What would you measure to decide whether a $200 seat is worth it?

<!--
Fuller versions from the module:

1. Why does doubling the length of an agent session more than double its cost? How would you design a harness to keep costs closer to linear?
2. A model costs 75% less per token but takes three times as many turns. When is it still the right choice?
3. Should a university course provide students with API keys, subscriptions, or neither? What about the students who can't afford their own?
4. Self-reported productivity gains have been shown to be unreliable. What would you measure to decide whether a $200/month seat is worth it?

Two more if time allows: As a team lead, how much should you rely on subscription pricing in a two-year plan? Is it fair for a vendor to restrict a paid subscription to its own tools?
-->

---

# Read more

- [Module 12: Costs: subscriptions vs API](../modules/12-costs-subscriptions-and-apis/)
- [Anthropic API pricing docs](https://platform.claude.com/docs/en/about-claude/pricing): caching, batch, fast mode
- [ccusage](https://github.com/ryoppippi/ccusage): local usage and cost reports for agent CLIs
- [Becker et al., 2025](https://arxiv.org/abs/2507.09089): METR's study of AI and developer speed

<!--
The module links every vendor pricing page used here. Prices were checked on 8 November 2026; re-check them before quoting any number from this deck later.
-->

# 12: Costs: subscriptions vs API

*About a 30-minute read. Last checked November 8, 2026.*

**TL;DR**
- You pay through a chat subscription (Claude, ChatGPT), a tool subscription (Cursor, GitHub Copilot), or the API, billed per token. Subscriptions are flat fees with usage caps; the API is metered, with rate limits and account spending limits.
- If an agent loop keeps appending history without compaction, total input tokens grow roughly with the *square* of the number of turns. Prompt caching cuts that by 80–90% in the worked example below. Without it, API pricing for heavy agent use is brutal.
- With caching, the Anthropic frontier and top-tier examples below cost roughly $4–$8 an hour (as of November 2026). A full-time heavy user easily spends several hundred to a few thousand dollars a month. A $100–$200 subscription covers much of that until you hit the weekly cap.
- Judge **cost per finished task**, not price per token. A cheaper model that takes three times as many turns can cost more money and more of *your* time.
- Use subscriptions for your own interactive work and the API for production services and shared automation. Authentication rules vary by vendor and tool; not all of them ban automation on subscriptions.

## Foundations

### Three ways to pay

A **consumer or pro subscription** is a monthly fee to a lab (roughly $20 to $200 for individuals, more for some tiers) for its apps: the chat app and its coding agent (Claude Code with a Claude plan, Codex with a ChatGPT plan). Usage is capped, usually by a rolling window of a few hours plus a weekly limit, and the cap is stated as a multiple ("5x Pro usage"), not in tokens.

A **tool subscription** goes to a tool vendor (Cursor, GitHub Copilot, and others) that buys model access from the labs and resells it in its product. The monthly fee includes an allowance; past that, you pay as you go. Some tools include their own or partner models in the flat fee and charge frontier lab models at API list price.

With an **API** key, you pay per token for exactly what you use, within rate limits and account spending limits. You can use any harness, build your own tools, run in CI, and ship features to customers.

### What a token bill is made of

A **token** is a chunk of text, about three-quarters of an English word on average ([module 01](./01-what-is-an-llm.md)). API prices are quoted per million tokens ("MTok"), and a bill has several lines:

| Line item | What it is | Typical relative price |
| --- | --- | --- |
| **Input tokens** | Everything you send: system prompt, tool definitions, conversation history, files, tool results | Base price |
| **Output tokens** | Everything the model writes | Usually 4–6x input |
| **Reasoning / thinking tokens** | The model's hidden or summarized step-by-step reasoning | Billed as output |
| **Cache write** | Storing a prompt prefix for reuse (Anthropic charges extra; at OpenAI it depends on the model and cache lifetime, see below) | 1.25x input for a 5-minute cache at Anthropic, 2x for 1 hour |
| **Cache read (cached input)** | Re-sending a prefix that is already cached | 2.5–10% of input, depending on vendor and model |
| **Batch** | Asynchronous jobs that finish within hours | 50% off at Anthropic, OpenAI, and Google |
| **Fast / priority modes** | Faster or guaranteed processing | About 2x |
| **Surcharges** | Long prompts above a threshold on some models; regional data residency | Model-specific; Anthropic's US-only inference is 1.1x |

Two things trip people up when comparing vendors. First, the same text becomes a different number of tokens on different tokenizers. Anthropic notes that its Claude 4.7-and-later tokenizer produces about 30% more tokens for the same text than earlier Claude models ([pricing docs](https://platform.claude.com/docs/en/about-claude/pricing)). A lower per-token price on a "wordier" tokenizer can cost the same.

Second, thinking is output. A reasoning model that thinks for 5,000 tokens before writing a 300-token answer bills you for 5,300 output tokens, so effort and thinking-budget settings change cost directly.

### Why agentic coding eats tokens

Each call needs the relevant history in context, sent by the harness or kept as conversation state by the provider. In the simple loop modeled below, the model asks to run a tool, the harness runs it, and the result goes back *along with all prior history*. Real harnesses may trim or compact that history. [Module 08](./08-agentic-workflows.md) covers the loop itself.

Where the tokens go:

- Context accumulates. Turn 1 sends 20,000 tokens of system prompt, tool definitions, and project instructions. Each tool result (a file, a test log, a diff) adds more. By turn 60 you may be sending 150,000+ tokens per call.
- Cost is roughly **quadratic** in turns. If each turn adds a fixed amount of context, total input over N turns grows with N², so doubling a session's length roughly quadruples its input tokens.
- Tool outputs are big. A full test log, a large file read, or a web page can add 10,000–100,000 tokens in one step.
- Retries and dead ends re-send everything again.
- Subagents each start their own context, often re-reading the same files, and parallel agents multiply all of the above.
- Thinking adds output tokens on every turn.

**Prompt caching** makes this affordable. Each turn's prompt starts with the previous turn's exact prefix, so the provider can keep that prefix's processed state and charge a fraction of the input price to reuse it. Harnesses like Claude Code and Codex do this automatically. If you build your own agent on the API, put the stable parts of the prompt first, and on Anthropic mark cache breakpoints or turn on automatic caching.

## In practice

### Price snapshot (as of 2026-11-08)

These prices come from the vendors' pages on 8 November 2026 and change often, sometimes monthly, so check the links before you budget. [Module 03](./03-model-landscape.md) covers what each model is good at.

**Chat and agent subscriptions (individuals, USD per month)**

| Vendor | Plan | Price | What the vendor says you get |
| --- | --- | --- | --- |
| Anthropic ([pricing](https://claude.com/pricing)) | Free | $0 | Limited usage per 5 hours and per week |
| | Pro | $20 ($17/mo billed annually) | More usage than Free; Claude Code included |
| | Max | $100 | 5x Pro usage per 5 hours and per week; $100/mo in API credits |
| | Ultra | $200 | 10x Pro usage per week; no 5-hour limit (for verified accounts); $200/mo in API credits |
| OpenAI ([Codex pricing](https://learn.chatgpt.com/docs/pricing)) | Free / Go | $0 / $8 | Limited Codex access on a small model |
| | Plus | $20 | Codex on web, CLI, IDE; can buy extra credits |
| | Pro | $100, $200, or $500 | Higher limits; the $500 tier adds "Ultrafast" mode |

On 30 October 2026 Anthropic renamed Max 20x to Ultra at the same $200 price, and the old Max 5x became just Max. The old name described usage per five-hour window; the pricing page now describes Ultra by its weekly allowance, 10x Pro ([Ultra help page](https://support.claude.com/en/articles/17728952-what-is-the-ultra-plan); [Anthropic's October 30 naming note](https://claude.com/resources/articles/create-files)). OpenAI added the $100 Pro tier on 9 April 2026 ([TechCrunch](https://techcrunch.com/2026/04/09/chatgpt-pro-plan-100-month-codex/)) and the $500 tier by late September ([OpenAI weekly update](https://learn.chatgpt.com/docs/whats-new/september-28-october-2-2026)). New $200 subscriptions have a lower allowance; eligible existing subscribers kept the old allowance only through October 29, 2026 ([Pro tier terms](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers)).

**Team plans (USD per seat per month)**

| Vendor | Plan | Price | Notes |
| --- | --- | --- | --- |
| Anthropic | Team, standard seat | $25 monthly / $20 annual | More usage than Pro; no training on your content by default; up to $500/mo pooled API credits |
| | Team, premium seat | $125 monthly / $100 annual | 5x standard-seat usage |
| | Enterprise | $20/seat (annual, 20-seat minimum) + usage at API rates | Admin spend limits, SCIM, audit logs, custom retention |
| OpenAI ([pricing](https://learn.chatgpt.com/docs/pricing)) | Business | $25 monthly / $20 annual | Standard seat; at least 2 users; Codex usage similar to Plus |
| | Enterprise / Edu | Contact sales | Flexible credit-based pricing available |

**Tool subscriptions (USD per user per month)**

| Tool | Plans | Notes |
| --- | --- | --- |
| GitHub Copilot ([plans](https://docs.github.com/en/copilot/get-started/plans), [credit billing](https://docs.github.com/en/copilot/concepts/billing-and-usage/individuals/billing)) | Free; Pro $10; Pro+ $39; Max $100; Business $19; Enterprise $39 | Allowances in "GitHub AI Credits" (1 credit = $0.01): Pro includes 1,500, Pro+ 7,000, Max 20,000, Business 1,900, Enterprise 3,900; cost per request depends on the model |
| Cursor ([pricing](https://cursor.com/pricing)) | Free; Plus $8; Premium $30; Super $100; Ultra $200; Teams from $30 | Pools of usage that refresh weekly; Plus includes Grok and Composer; Claude, GPT, and Gemini are billed separately at API list price |

Cursor announced its shared subscription with xAI on October 12, 2026. Existing plans continue until users switch ([Cursor announcement](https://forum.cursor.com/t/introducing-the-x-subscription/174450)). Plus includes Composer too ([Cursor staff clarification](https://forum.cursor.com/t/introducing-the-x-subscription/174450?page=4)).

**API prices (USD per million tokens, standard tier)**

| Vendor and model (tier) | Input | Cache write | Cache read | Output |
| --- | --- | --- | --- | --- |
| Anthropic Claude Fable 5.1 (top tier) | $10 | $12.50 (5 min) | $0.25 | $50 |
| Anthropic Claude Opus 5.5 (frontier) | $4 | $5 (5 min) / $8 (1 h) | $0.20 | $20 |
| Anthropic Claude Sonnet 5.5 (mid) | $2 | $2.50 | $0.10 | $10 |
| Anthropic Claude Haiku 5.5 (small, prompts ≤100K) | $0.10 | $0.125 | $0.01 | $0.50 |
| OpenAI GPT-6 Astra (top tier) | $10 | $12.50 (30 min) / $25 (12 h) | $1.00 | $50 |
| OpenAI GPT-6.1 Sol (frontier) | $2 | $2.50 (30 min) / $5 (12 h) | $0.10 | $10 |
| OpenAI GPT-6.1 Terra (mid) | $1 | $1.25 (30 min) / $2.50 (12 h) | $0.05 | $5 |
| OpenAI GPT-6 Luna (small) | $0.10 | $0.125 (30 min) / $0.25 (12 h) | $0.01 | $0.50 |
| Google Gemini 4 Argon (flagship) | $2 | none (implicit caching only) | $0.10 | $10 |
| Google Gemini 3.8 Flash | $0.75 | storage fee | $0.075 | $3.75 |

Sources: [Anthropic pricing docs](https://platform.claude.com/docs/en/about-claude/pricing), [OpenAI pricing docs](https://developers.openai.com/api/docs/pricing), [Google AI Studio pricing](https://aistudio.google.com/docs/pricing). As of November 2026:

- Batch is 50% off at all three. OpenAI renamed its "Priority" tier Fast mode on 30 July 2026; it costs 2x. Anthropic's fast mode for Opus 5.5 is $8/$40.
- OpenAI charges more above 272K input tokens, and Haiku 5.5 charges 5x above 100K. Anthropic's other current models bill the full 1M context at the standard rate.
- Google's page lists scheduled increases. Gemini 4 Argon prices double on 1 December 2026, and Gemini 3.8 Flash on 1 January 2027. Anthropic's Sonnet 5 launched with "introductory" pricing that was later made permanent. Launch prices aren't promises.
- The labs' most capable restricted models, such as Anthropic's Mythos tier for vetted security work, are listed separately and aren't generally available. Mythos 5.1 has the same list price as Fable 5.1.

### Worked example: one hour of agentic coding

Here's the arithmetic for one realistic hour with a coding agent at API prices. Change the assumptions to match your own logs.

**Assumptions**
- 60 model calls in the hour (one tool call or reply roughly every minute).
- The first call sends 20,000 tokens (system prompt, tool definitions, project instructions).
- Each call adds 2,500 tokens to the context (tool results plus the model's own output).
- Each call produces 1,500 output tokens, including thinking.
- No context compaction during the hour, and no breaks longer than 5 minutes.
- Prices: the frontier tier above, Claude Opus 5.5: $4 input, $5 cache write, $0.20 cache read, $20 output.

**Token counts**
- Context on call *i* is 20,000 + 2,500 × (*i* − 1). Call 60 sends 167,500 tokens.
- Total input = 60 × 20,000 + 2,500 × (0 + 1 + … + 59) = 1,200,000 + 2,500 × 1,770 = **5,625,000 tokens**.
- Total output = 60 × 1,500 = **90,000 tokens**.

**Without caching**
- Input: 5.625 MTok × $4 = $22.50
- Output: 0.09 MTok × $20 = $1.80
- **Total: $24.30 per hour**

**With caching** (each call reads the previous prefix from cache and writes only the new part)
- Cache writes: 20,000 on the first call + 2,500 × 59 later calls = 167,500 tokens → 0.1675 × $5 = $0.84
- Cache reads: 5,625,000 − 167,500 = 5,457,500 tokens → 5.4575 × $0.20 = $1.09
- Output: $1.80
- **Total: $3.73 per hour** (85% less)

**The same hour at other price points** (same token counts):

| Tier | Uncached | Cached | 168 hours/month, cached |
| --- | --- | --- | --- |
| Top tier ($10 / $50, cache read $0.25) | $60.75 | $7.96 | ~$1,340 |
| Frontier ($4 / $20, cache read $0.20) | $24.30 | $3.73 | ~$630 |
| Mid ($2 / $10, cache read $0.10) | $12.15 | $1.86 | ~$310 |

(168 hours = 8 hours a day for 21 working days, one agent at a time.)

1. Caching makes this much cheaper. Once it's on, output tokens become the largest single line.
2. A full-time heavy user on a frontier model costs hundreds of dollars a month at API prices, and three agents at once roughly triples the bill. That's why a $100–$200 subscription feels like a bargain to heavy users.
3. Light users are cheaper on the API. Anthropic's docs use an example one-hour session of 50,000 input and 15,000 output tokens, which costs well under a dollar on Opus 5.5. If you use an agent for a few short tasks a week, pay-as-you-go may beat a $20 plan.
4. Cache misses cost real money in big contexts. If you step away for more than five minutes (Anthropic's default cache lifetime), the next call re-writes the whole prefix, and a 150,000-token context costs $0.75 to re-cache at $5/MTok. Harnesses can use the 1-hour cache at 2x the write price. Changing the system prompt, tools, or settings mid-session also breaks the cache.

Measure instead of guessing. [ccusage](https://github.com/ryoppippi/ccusage) reads the usage data that Claude Code, Codex, and many other agent CLIs store locally and prints daily, weekly, monthly, and per-session token counts with API-equivalent costs:

```bash
npx ccusage@latest claude daily  # Claude Code usage by day, with estimated API cost
npx ccusage@latest codex daily  # same for Codex
```

### The subscription "subsidy" and its limits

A subscription is a flat fee with a cap. Use less than the cap and you overpay compared to the API; use all of it and you can get far more than the fee in API-equivalent usage. Heavy users' ccusage reports routinely show monthly totals several times their subscription price. Whether vendors make or lose money on those users isn't public.

What's public is that the caps keep changing:

- Anthropic announced on 28 July 2025 that weekly limits would start on 28 August 2025 for Pro and Max, on top of the existing 5-hour windows. It cited users running Claude Code "continuously in the background, 24/7" and account sharing, and estimated fewer than 5% of subscribers would be affected ([TechCrunch](https://techcrunch.com/2025/07/28/anthropic-unveils-new-rate-limits-to-curb-claude-code-power-users/)). At the time it estimated Pro at about 40–80 hours of Sonnet 4 per week, and the $200 Max tier at about 240–480 hours of Sonnet and 24–40 hours of Opus.
- Both vendors reshuffled their plans in 2026. OpenAI added $100 and $500 Pro tiers and cut the $200 tier's allowance, with the old allowance for eligible subscribers ending October 29 ([Pro tier terms](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers)). Anthropic renamed its $200 tier Ultra, removed the 5-hour window for verified Ultra accounts, and kept weekly limits. Anthropic's Max and Ultra now include monthly API credits, and both vendors sell extra usage beyond the cap.
- Caps are sold as usage multiples, and "5x Pro" tells you nothing about tokens. Advertised multiples and real allowances have diverged before. In 2025, reporters calculated that the "20x" plan gave about 6x Pro's Claude Code hours under the new weekly limits.

Rules for using a subscription outside the vendor's own tools changed in 2026 and differ by vendor:

- Anthropic says OAuth sign-in from Free, Pro, Max, and Ultra plans is for Claude Code and Anthropic's own apps. Developers building products, including with the Agent SDK, must use API keys, and third parties may not route requests through subscription credentials ([Claude Code legal and compliance](https://code.claude.com/docs/en/legal-and-compliance)). Anthropic began actively blocking third-party tools that spoofed the Claude Code harness in January 2026, and in February 2026 it spelled out the OAuth rule on that compliance page. Its consumer terms had already banned unauthorized automated access since at least 2024 ([The Register](https://www.theregister.com/2026/02/20/anthropic_clarifies_ban_third_party_claude_access)). Running the unmodified Claude Code binary with your own subscription is allowed, including where a platform hosts it.
- OpenAI lets you sign into Codex with a ChatGPT plan for subscription access or with an API key for metered access ([docs](https://learn.chatgpt.com/docs/auth)). Its September 28, 2026 [integration guide](https://learn.chatgpt.com/cookbook/articles/sign-in-with-chatgpt) documents "Sign in with ChatGPT" for third-party apps. Eligible Plus and Pro users can grant access to their plan usage. Identity sign-in and permission to spend plan usage are separate; neither exposes ChatGPT conversations.

These policies changed several times in one year. If your workflow depends on a consumer subscription inside a third-party tool, have a fallback.

### Cheaper alternatives

Several labs that release open-weight models sell flat-rate **coding plans** that plug into popular harnesses (Claude Code, Codex, OpenCode, Cline, and others) through API-compatible endpoints:

- Z.ai's GLM Coding Plan starts at $18/month for the Lite tier, with 5-hour and weekly credit limits and half-price off-peak usage ([docs](https://docs.z.ai/devpack/overview)).
- Moonshot's Kimi Code Plan runs its Kimi K3-series models ([page](https://www.kimi.com/code)).
- MiniMax sells an M Plan for its M3-series models ([page](https://www.minimax.io/m-plan)).

For many tasks they're much cheaper per unit of work. They usually trail the closed frontier on the hardest coding work, as [module 03](./03-model-landscape.md) and [module 05](./05-judging-models.md) show. You're also sending code to a different provider in a different jurisdiction, so read the data terms. And the "open" part only helps if you might self-host later ([module 04](./04-open-vs-closed-weights.md)).

With **model routing**, a small, cheap model does easy work (renaming, boilerplate, summarizing logs, classifying issues) and the frontier model handles planning, hard debugging, and review. Many harnesses let you set a different model for subagents. The small models in the price table cost 20–100x less per token than the bigger models, and about 100x less than the top tier.

Running an open-weight model on your own hardware has zero marginal token cost, but you still pay for hardware and electricity, and today's local models are well behind the frontier for agentic coding ([module 04](./04-open-vs-closed-weights.md)).

### Cost per task, not cost per token

The number that matters is what it costs to get a *correct, merged change*. A cheaper model can lose on that measure.

Here's one task on two models, both cached, with the hourly example's growth assumptions. The budget model's prices are made up for illustration; they don't match any one product (a 20,000-token start, 2,500 tokens added and 1,500 output tokens per call):

| | Frontier model | Budget model |
| --- | --- | --- |
| Prices (input / cache write / cache read / output) | $4 / $5 / $0.20 / $20 | $1 / $1.25 / $0.10 / $5 |
| Calls to finish | 30 | 90 (more wrong turns and retries) |
| Total input tokens | 1.69M | 11.81M |
| Cost with caching | **$1.68** | **$2.14** |
| Cost without caching | $7.65 | $12.49 |
| Final context size | 92,500 | 242,500 |

The budget model's input and output cost a quarter as much per token (its cache reads, half as much), but three times the turns means about seven times the input tokens, because the context grows every turn. It also ran three times as many calls; how much of your attention that takes depends on how closely you supervise it, so count that time too.

The reverse also happens. On well-specified, repetitive work (the same refactor across 200 files, tests written from a clear pattern), a small model finishes in the same number of turns and the 20–40x price gap wins.

Thinking budgets work the same way. More reasoning tokens per turn cost more but often mean fewer turns. Try a task at two effort levels and compare total cost, not per-call cost.

### When API billing is the right choice

- Your own model-backed production service should use API authentication and per-request metering. Hosting an unmodified vendor agent where each user signs into their own account is a separate case; check the vendor's rules.
- For CI and automation (review bots, issue triage, nightly jobs), API keys are the recommended default. OpenAI also documents account authentication on trusted CI runners, so read its [authentication guidance](https://learn.chatgpt.com/docs/auth) before assuming every unattended run violates subscription terms.
- Batch jobs (migrations, labeling, documentation generation, evaluation runs) get 50% off through the batch APIs.
- Multi-user apps need each user's usage to be attributable and limited.
- Light or bursty individual use can be cheaper pay-as-you-go.
- Commercial API terms default to no training on your data. Some organizations require zero data retention, which is available on commercial terms but not on consumer plans.

Set up these cost controls on day one:
- Spend limits and alerts at the scopes your provider supports (workspace, project, key, or user). Check which settings stop requests and which only send alerts, because an alert doesn't cap spending.
- Separate keys per app, environment, and team so you can see who spent what.
- Prompt caching on by default; stable content first in the prompt.
- Model routing: small model by default, escalate on failure.
- `max_tokens` and effort/thinking limits per call; a cap on turns per agent run.
- Trim tool outputs (truncate logs, summarize large files) before they enter the context.
- Batch for anything that can wait.
- A weekly cost review for the first month of any new agent workflow.

### Team budgeting

Per-seat pricing is predictable and easy to approve, but you pay for light users who don't need a seat, and heavy users still hit caps. Pooled usage (API credits, Enterprise usage billing, Copilot credits) tracks real use but needs budgets and alerts. Many teams mix the two: a standard seat for everyone, plus premium seats or pooled API credits for the heaviest users and for automation.

Show your assumptions in the ROI case so leadership can adjust them.

- The US median pay for software developers was $135,980 in May 2025 ([BLS](https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm)).
- Assume benefits, taxes, equipment, and overhead bring the **loaded cost** to about 1.4x salary: ~$190,000 a year.
- Assume ~1,800 productive hours a year: **~$105 per engineer-hour**. Round to $100.

Then:
- A $200/month seat costs about **2 engineer-hours a month**. A $20 seat costs about 12 minutes.
- A heavy API user at about $630/month (the cached frontier figure above) costs about **6 engineer-hours a month**.
- A 10-person team on $200 seats is $24,000 a year, about 13% of one loaded engineer. If the tools raise the team's useful output by even 2%, that is ~$38,000 of engineering time.

That assumes a productivity gain. In METR's 2025 randomized study, experienced open-source developers using early-2025 AI tools took 19% *longer* on their tasks while believing they were 20% faster ([Becker et al., 2025](https://arxiv.org/abs/2507.09089)). Tools and practices have changed a lot since, but self-reports still need checking. Measure things you can count (cycle time, review turnaround, escaped defects, rework) before and after. [Module 08](./08-agentic-workflows.md) covers the study and its follow-up, and the [workplace playbook](../workplace/) covers measuring a team.

Before a team rollout, get written answers on procurement and data terms:
- Is our content used for training? Anthropic's and OpenAI's business and API terms default to no. Consumer plans differ and change, as [module 15](./15-learning-careers-and-responsibility.md) explains.
- What is retained, for how long, and is zero data retention available for our use?
- Data residency options and their price (Anthropic's US-only inference is 1.1x).
- SSO, SCIM, audit logs, admin spend limits, and whether usage dashboards attribute cost per user.
- Any regulated-data needs (HIPAA BAAs, for example, cover only specific configurations).
- What happens to pricing at renewal, and how much notice the vendor gives for limit changes.

## Going deeper

### Cache economics

Caches match from the start of the prompt, so anything that changes early (a timestamp in the system prompt, a reordered tool list) invalidates everything after it. Put stable content first: tools, system instructions, project docs, then conversation.

Anthropic charges 1.25x to write a 5-minute cache entry and 2x for 1 hour. Reads cost 0.1x base on most models and less on the newest (0.05x on Opus 5.5 and Sonnet 5.5, 0.025x on Fable 5.1), so a 5-minute write pays for itself after one read. OpenAI supports implicit caching, but GPT-5.6-and-later models charge cache writes at 1.25x for 30 minutes or 2.5x for 12 hours in the Responses API; older models have no added write charge ([caching docs](https://developers.openai.com/api/docs/guides/prompt-caching)). Google charges for cache storage per hour on models that offer explicit caching.

Vendors now compete on cache price. For agentic workloads, the cache-read price can matter more than the headline input price, because most input tokens are cache reads. Compare that column first.

### Why output costs more

Each output token takes a full pass through the model, one at a time, while input tokens are processed in parallel. That's why output is priced 4–6x higher and why a verbose model costs more than its per-token price suggests. Asking for concise answers (or a concise output style) saves money.

### Price trends

Two trends pull in opposite directions. The price of a *given level of capability* keeps falling. Each year's mid-tier and small models tend to match or beat older flagships on benchmarks at a fraction of the old price, though [module 05](./05-judging-models.md) explains how much to trust those benchmarks. Meanwhile the *top* tier got more expensive. Anthropic and OpenAI both now sell a tier above their former flagships at $10/$50 per MTok. For coding agents, where people want the best model available, the bill hasn't fallen as much as the "cost per capability" charts suggest.

### Are subscriptions sustainable?

Nobody outside the labs knows the unit economics. Vendors may treat heavy-user subscriptions as customer acquisition, may have lower serving costs than API prices imply, or may be losing money on their heaviest users. What you can see is that caps have tightened more often than loosened, top tiers have been added above old ones, and third-party access has been restricted (Anthropic) or channeled through partnerships (OpenAI). Plan as if today's subscription value isn't guaranteed next year.

## Bryan's take

> **Bryan's take:** API pricing is too expensive for heavy agentic use. Subscriptions are what make it affordable to work this way every day.

The arithmetic in this module backs that up for full-time use of frontier models. Even with caching, one heavy user can spend several hundred dollars a month at API prices, and parallel agents multiply it. There are limits to that advantage:

- A subscription is cheap until you hit the weekly limit on a Thursday. Caps and throttling are the real price, and heavy parallel use may need the top tier, extra credits, or a second vendor.
- Subscription terms change. Weekly limits (2025), third-party harness restrictions (2026), and reduced allowances at existing price points (2026) all happened within about a year. API prices, by contrast, are published per token.
- Subscription credentials aren't a general API key for your product. Vendor-native agents and approved integrations have different rules, so use the API for your own production service and check the rules for hosted agents and automation.
- A subscription locks its value to the vendor's harness. With the API you can switch models and harnesses freely and route cheap work to cheap models.
- Light users overpay. If you only use an agent for a few short tasks a week, pay-as-you-go can be cheaper than $20 a month.
- Cheaper flat rates exist. Open-weight coding plans start under $20 a month, with a capability trade-off.
- Team math is different. Pooled API usage with good caching and routing can beat buying top-tier seats for everyone, especially when usage is uneven.

## Try it

**Individual: measure your real cost.**
1. Use your agent normally for a week.
2. Run `npx ccusage@latest daily` (or `npx ccusage@latest codex daily` for Codex). Record total input, cache-read, cache-write, and output tokens, and the API-equivalent cost.
3. Compare that cost to your subscription price. Then recompute it for a model one tier cheaper using the price table.
4. Find your most expensive session. What made it expensive: length, big tool outputs, retries, or parallel agents? Write down one habit change that would have halved it.

**Class or team: build a budget.**
1. Pick a realistic scenario: a 12-person team, 4 heavy users, 6 moderate, 2 light, plus a PR-review bot running on every pull request (about 40 PRs a day).
2. Price three options: all top-tier seats; standard seats plus pooled API credits for heavy users and the bot; API only with caching and routing.
3. State every assumption (tokens per session, sessions per day, cache hit rate, PR size).
4. Compute the break-even productivity gain against loaded engineer cost.
5. List the data-terms questions you'd send to procurement.

## Discussion questions

1. Why does doubling the length of an agent session more than double its cost? How would you design a harness to keep costs closer to linear?
2. A model costs 75% less per token but takes three times as many turns. When is it still the right choice?
3. Should a university course give students API keys, subscriptions, or neither? What about students who can't afford their own?
4. Vendors have tightened subscription caps several times. As a team lead, how much should you rely on subscription pricing in a two-year plan?
5. Is it fair for a vendor to restrict a paid subscription to its own tools? What are the strongest arguments on each side?
6. Self-reported productivity gains have proven unreliable. What would you measure to decide whether a $200/month seat is worth it?

## Sources and further reading

**Papers**
- [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://arxiv.org/abs/2507.09089) (Becker, Rush, Barnes, Rein, 2025)

**Primary sources: pricing and terms (all checked 2026-11-08)**
- Anthropic, [Claude plans and pricing](https://claude.com/pricing) and [API pricing docs](https://platform.claude.com/docs/en/about-claude/pricing), including prompt caching, batch, fast mode, data residency, and Managed Agents pricing
- Anthropic, [Claude Code legal and compliance](https://code.claude.com/docs/en/legal-and-compliance) (authentication and credential use)
- OpenAI, [API pricing](https://developers.openai.com/api/docs/pricing), [Codex pricing by plan](https://learn.chatgpt.com/docs/pricing), [Codex authentication](https://learn.chatgpt.com/docs/auth)
- Google, [Gemini API pricing](https://aistudio.google.com/docs/pricing)
- GitHub, [Copilot plans](https://docs.github.com/en/copilot/get-started/plans)
- Cursor, [pricing](https://cursor.com/pricing)
- Z.ai, [GLM Coding Plan docs](https://docs.z.ai/devpack/overview); Moonshot, [Kimi Code](https://www.kimi.com/code); MiniMax, [M Plan](https://www.minimax.io/m-plan)
- U.S. Bureau of Labor Statistics, [Software Developers, Occupational Outlook Handbook](https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm)

**Tools**
- [ccusage](https://github.com/ryoppippi/ccusage): local usage and cost reports for Claude Code, Codex, and other agent CLIs

**Reporting**
- TechCrunch, [Anthropic unveils new rate limits to curb Claude Code power users](https://techcrunch.com/2025/07/28/anthropic-unveils-new-rate-limits-to-curb-claude-code-power-users/) (2025)
- TechCrunch, [OpenAI's $100 ChatGPT Pro plan](https://techcrunch.com/2026/04/09/chatgpt-pro-plan-100-month-codex/) (2026)
- The Register, [Anthropic clarifies ban on third-party harnesses with Claude subscriptions](https://www.theregister.com/2026/02/20/anthropic_clarifies_ban_third_party_claude_access) (2026)
- The New Stack, [OpenAI makes "Sign in with ChatGPT" a way to use your subscription in third-party developer tools](https://thenewstack.io/sign-in-with-chatgpt/) (2026)

## Terms introduced

- **Token:** The unit of text a model reads and writes; prices are quoted per million tokens (MTok).
- **Input tokens:** Everything sent to the model on a call, including history, files, and tool results.
- **Output tokens:** Everything the model generates on a call, including reasoning tokens.
- **Reasoning (thinking) tokens:** Tokens a model generates while working through a problem before answering; billed as output.
- **Prompt caching:** Reusing the processed state of an unchanged prompt prefix across calls at a reduced price.
- **Cache write / cache read:** The cost to store a prefix in the cache, and the (much lower) cost to reuse it.
- **Cache TTL:** How long a cached prefix stays available (for example 5 minutes or 1 hour) before it must be written again.
- **Batch API:** Asynchronous processing of many requests, completed within hours, at about half price.
- **Fast / priority mode:** A higher-priced service tier that returns results faster or with guaranteed capacity.
- **Usage cap:** The limit on how much a subscription allows in a rolling window (often 5 hours) or per week.
- **API-equivalent cost:** What a given amount of subscription usage would have cost at published API prices.
- **Cost per task:** The total spend (tokens plus human time) to get one correct, accepted change, as opposed to price per token.
- **Model routing:** Sending easy work to cheaper models and hard work to more capable ones.
- **Coding plan:** A flat-rate subscription from a model provider, often an open-weight lab, meant for use inside third-party coding harnesses.
- **Loaded cost:** An employee's total cost to the employer, including salary, benefits, taxes, and overhead.
- **Zero data retention (ZDR):** A contractual arrangement in which the provider does not store prompts or outputs after processing.
- **Tokenizer:** The component that splits text into tokens; different tokenizers produce different token counts for the same text.

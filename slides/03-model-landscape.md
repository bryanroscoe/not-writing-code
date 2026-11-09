---
marp: true
theme: not-writing-code
paginate: true
title: "03: The model landscape"
description: "The labs, the tier ladder, the current lineups, and how to pick a model when it all changes"
footer: "A Brief Introduction to Not Writing Code · 03 The model landscape"
---

<!-- _class: lead -->

# 03: The model landscape

Who makes the models, and how to pick one when the names keep changing

Lineups and prices as of November 2026

<!--
This deck will go out of date fastest. Everything in the lineup tables will be stale within months. The tier ladder and checklist should stay useful longer. Before presenting, compare the lineup slides against the module's "Last verified" date and its linked sources.

Rough timing for a 45-minute session: Part 1 (reading the landscape) about 18 minutes, Part 2 (choosing in a moving market) about 17 minutes, then the exercise and discussion.
-->

---

## Why this matters

- Names change monthly. The tier ladder doesn't.
- Benchmarks and daily use often disagree
- Access can vanish overnight, for reasons unrelated to you
- The right model depends on the job, not the launch chart

<!--
Two examples we'll come back to. Opus 5 topped leaderboards in July 2026, and its communication style became one of the most common complaints. Fable 5 was suspended for all users three days after launch because of US export controls.

When a new model appears next month, you should be able to place it on the ladder and decide whether to test it.
-->

---

<!-- _class: divider -->

# Part 1

## Reading the landscape

<!--
Part 1 covers labs, names, tiers, and who is shipping what as of November 2026. About 18 minutes.
-->

---

## Labs, models, and products

- A frontier lab trains its own models at the edge of capability
- It takes tens of thousands of GPUs and months of work
- A model is the trained network. A product is what you use.
- One model powers many products; a product can switch models under you

"ChatGPT got worse" could mean the model, the system prompt, the router, or the harness.

<!--
Only a few organizations can pay for frontier training, so only a few sit at the top. As of November 2026: Anthropic, OpenAI, and Google DeepMind lead; xAI and Meta follow; Chinese labs (DeepSeek, Moonshot, Alibaba Qwen, Zhipu/Z.ai, MiniMax) lead open-weight models.

Products include ChatGPT, the Claude apps, Gemini, Claude Code, and Codex. Module 06 covers harnesses.

Labs release models two ways. With closed weight, or API-only, you never see the parameters. Claude, the GPT-6 family, Gemini, and Grok work this way. With open weight, the lab publishes the parameters. DeepSeek, Moonshot (Kimi), Qwen, Z.ai (GLM), and Mistral work this way, as do OpenAI's gpt-oss, Google's Gemma, and a few of Meta's Muse models. Open models usually come from different labs than the very top closed ones, and arrive some months behind. Module 04 covers the differences.
-->

---

## Reading a model name

| Part | Example | What it tells you |
| --- | --- | --- |
| Family | Claude, GPT, Gemini, Grok, Kimi, Qwen | Which lab, which product line |
| Generation | 5, 5.5, 6, 6.1, 4 | Roughly when it was trained |
| Tier | Haiku / Sonnet / Opus; Luna / Terra / Sol / Astra; Flash-Lite / Flash / Pro | Size, price, and speed |
| Variant | Pro, Code, Flash, Cyber, Open, -Thinking | A specialization or serving mode |
| Snapshot / ID | `claude-opus-5-5`, `gpt-6.1-sol` | The exact string for an API call |

The tier matters most.

<!--
Bigger generation numbers usually mean newer, but not always in a simple way. The slide after next shows why.

OpenAI moved from numbers plus suffixes (GPT-5, GPT-5-mini, GPT-5-Codex) to named tiers in July 2026. GPT-5.6 introduced Sol, Terra, and Luna, and GPT-6 added Astra on top. Largest to smallest: Astra (top), Sol (the workhorse in ChatGPT and Codex on paid plans), Terra (cheaper, aimed at computer use and everyday work), Luna (small and cheap). Point releases like GPT-6.1 Sol update one tier at a time. "Pro" variants spend more compute per answer.

Google uses Pro, Flash, and Flash-Lite. Flash moves fast, from 3.5 in May 2026 to 3.6, 3.7, and 3.8 by September. The Pro line stalled, and Gemini 4's first model got a codename-style name instead of a tier: Gemini 4 Argon.
-->

---

## The tier ladder (as of November 2026)

| Tier | For | List price per million tokens (in / out) |
| --- | --- | --- |
| Top / flagship | Hardest reasoning, long autonomous work | $4–$10 / $20–$50 |
| Workhorse | Most coding and knowledge work | $1–$2 / $5–$10 |
| Fast / cheap | Bulk processing, classification, sub-agents | $0.10–$0.30 / $0.50–$2.50 |

On Anthropic's own numbers, Sonnet 5.5 beats Opus 5.5 on Terminal-Bench 4.0 (70.6% vs 66.4%) at half the price.

<!--
These are typical ranges, not every model. Don't assume the most expensive model is the best one for your job. Opus 5.5 in turn beats the pricier Fable 5.1 on several benchmarks, again on Anthropic's published numbers.

Two settings change what you get from the same model. First, reasoning effort. Most current models let you choose how long they think, from low to max. Higher effort costs more tokens and time; it often helps on hard problems and wastes money on easy ones. Second, fast or priority modes. Some labs charge more for faster output, and Anthropic's Opus 5.5 fast mode costs twice the standard rate.
-->

---

## Anthropic's top tier ships as two releases

Haiku → Sonnet → Opus → Mythos-class (new in 2026)

| Release | Who gets it | Safeguards |
| --- | --- | --- |
| Claude Fable | General release | Classifiers for cyber, bio, chem, and distillation |
| Claude Mythos | Vetted organizations only | Some lifted |

Version numbers don't move in lockstep. Fable 5.1 sits above Opus 5.5.

<!--
Anthropic names its tiers after poetic forms, smallest to largest. Its footnote says "Mythos-class models are a tier of Claude models that sit above our Opus class in capability." Fable comes from the Latin fabula, a counterpart to the Greek mythos.

With Fable, flagged requests are handed to an Opus model instead, and users are told when that happens. Anthropic says it happens in fewer than 5% of sessions on average. Mythos access runs through Project Glasswing (cyber defenders, from April 2026) and verification programs for security and life-sciences researchers.

The 2026 sequence went Opus 4.6, 4.7, and 4.8; then Fable 5 and Sonnet 5; then Opus 5; then Fable 5.1; then the 5.5 family (Opus, Sonnet, Haiku). So "Claude 5.5" names a family, and Fable 5.1 is still the top tier even though 5.1 is a smaller number.
-->

---

## Closed lineups (as of November 2026)

| Lab | Top | Workhorse | Small / cheap |
| --- | --- | --- | --- |
| Anthropic | Fable 5.1 ($10 / $50), Opus 5.5 ($4 / $20) | Sonnet 5.5 ($2 / $10) | Haiku 5.5 ($0.10 / $0.50) |
| OpenAI | GPT-6 Astra ($10 / $50) | GPT-6.1 Sol ($2 / $10), GPT-6.1 Terra ($1 / $5) | GPT-6 Luna ($0.10 / $0.50) |
| Google | Gemini 4 Argon ($2 / $10 intro, then $4 / $20) | Gemini 3.8 Flash | Gemini 3.5 Flash-Lite ($0.30 / $2.50) |

Prices per million tokens, input / output. Most have about 1M tokens of context.

<!--
Release dates. Anthropic: Fable 5.1 September 1, Opus 5.5 September 22, Sonnet 5.5 September 28, Haiku 5.5 October 7, 2026. Haiku's price is for prompts up to 100K tokens; above that it's $0.50 / $2.50. OpenAI: GPT-6 Astra September 3, GPT-6 Luna September 22, GPT-6.1 Sol September 29, GPT-6.1 Terra October 26. Google: Gemini 4 Argon announced September 30 and generally available October 13, with the introductory price through November 30, 2026. Gemini 3.8 Flash is $0.75 / $3.75 introductory through December 31, then $1.50 / $7.50.

Opus 5.5 can't turn thinking off; its default effort is medium. Fable models require 30-day data retention; Opus 5.5 is available with zero data retention. GPT-6 reached ChatGPT on October 7 with "Intelligent UI"; paid tiers get Sol and free tiers get Luna. Batch APIs are usually half price.

xAI has Grok 4.7 (flagship, September 2026, $2 / $6, 500K context), Grok 4.3 (cheaper long-context, $1.25 / $2.50), and Grok Build 0.1 (coding, early access). xAI prices double for prompts of 200K tokens or more.

Check the module's linked pages before relying on any number here.
-->

---

## Leading open-weight models (as of November 2026)

| Model | Lab | Size (total / active) | License |
| --- | --- | --- | --- |
| Kimi K3.1 Pro | Moonshot | 2.8T / 104B | Custom |
| GLM-5.3 | Z.ai | 753B MoE | Custom |
| DeepSeek V4-Pro | DeepSeek | 1.6T / 49B | MIT |
| Qwen3.8-Max | Alibaba | 2.4T / 95B | Custom |
| Mistral Large 4 | Mistral | ~1T / ~49–52B | Custom |
| MiniMax M3 | MiniMax | 428B / 23B | Custom (community) |

They trail the closed frontier by roughly six months to a year.

<!--
Kimi K3.1 Pro's API came October 23, weights early November 2026, at a reported $2 / $10. GLM-5.3 weights August 25. DeepSeek V4-Pro generally available August 13. Qwen3.8-Max weights around August 10. Mistral Large 4 weights October 29. MiniMax M3 June. Sizes come from model cards; treat them as approximate.

Chinese labs have led open weights since DeepSeek-R1 in January 2025. By August 2025, Nathan Lambert's ATOM Project reported that the top ten open models on LMArena were all Chinese, and Qwen derivatives were over 40% of new models on Hugging Face, against about 15% for Llama. Mistral's own model card calls Large 4 the highest-scoring Western open-weight model and notes that Chinese ones score higher.

The module's table also lists US and European open efforts: gpt-oss (OpenAI, August 2025), OLMo 3 (AI2), Gemma 4 (Google, April 2026, Apache 2.0), Nemotron 3 Ultra (NVIDIA, 550B), Inkling (Thinking Machines Lab, about 975B), Beam 1.0 (Reflection AI, 501B), plus Meta's two open Muse models.
-->

---

## Where is Meta's Muse? (as of November 8, 2026)

| 2026 | Model | Weights |
| --- | --- | --- |
| Apr 8 | Muse Spark, the first MSL model | Closed |
| Jul 9 | Muse Spark 1.1, plus the Meta Model API (preview) | Closed |
| Aug 10 | Muse Glimmer 30B | Open, Apache 2.0 |
| Oct 12 | Muse Wonder ($4 / $20 on OpenRouter) | Closed |
| Oct 15 | Muse Spark Open (816B) | Open, custom license |

Meta's best models are closed. Its open ones don't lead the open field.

<!--
Muse comes from Meta Superintelligence Labs (MSL), led by chief AI officer Alexandr Wang. It replaced Llama as Meta's main line. Meta hasn't released a new Llama since Llama 4 in April 2025.

Muse Spark launched in the Meta AI app and meta.ai with only a private API preview. Meta's own benchmarks put it near Claude Opus 4.6, Gemini 3.1 Pro, and GPT-5.4, and Meta admitted gaps in long-horizon agents and coding. Spark 1.2 and 1.3 followed in August and September. Muse Image and a Muse Video preview came out July 7.

Muse Glimmer 30B is dense, handles images, and is built to run locally. Muse Wonder is a closed frontier reasoning model; Meta is its only host. Muse Spark Open's license requires "Built with Muse Spark Open" attribution, and any service with more than $20M in revenue that offers it to others needs a separate agreement. On Meta's own card it scores 39 on the Artificial Analysis Intelligence Index, below Kimi K3 (44) and GLM-5.3 (45), and trails several models on Terminal-Bench 2.1.

Muse is shipping and competitive in Meta's consumer apps.
-->

---

## Gated tiers

In 2026 every top lab started holding back its most cyber-capable model.

| Lab | Gated model or rollout |
| --- | --- |
| Anthropic | Mythos Preview, then Mythos 5 and 5.1, through Project Glasswing |
| OpenAI | GPT-6-Cyber |
| Google | Argon went to cyber defenders first; Gemini 4 Carbon is still limited to some of them |

Public versions route or refuse some security and biology requests.

<!--
Google's rollouts run through its Fairwind Program. Gemini 4 Carbon was announced October 28, 2026. Google calls it "our strongest model with state-of-the-art cybersecurity and long horizon capabilities," and plans to reach developers and consumers "as soon as possible." Carbon was announced at $2 / $10 introductory, then $4 / $20.

Google's own results table puts Carbon first on Terminal-Bench 4.0 at 65.2%, run by Artificial Analysis. That's a self-reported number for a model almost nobody can use yet. If someone compares it with Anthropic's 70.6% for Sonnet 5.5 on the tier slide, point out that Anthropic published its own numbers and Artificial Analysis ran Carbon's. Module 05 explains why cross-lab numbers don't compare cleanly.

If you do security work, expect the general-release model to hand some requests to a weaker model or decline them. Check each lab's verification program.
-->

---

<!-- _class: divider -->

# Part 2

## Choosing in a moving market

<!--
Part 2 is how open and closed models relate, what that does to prices, which model fits which job, and how to choose next month when this deck is stale. About 17 minutes.
-->

---

## Different places in the chain

```text
Closed frontier (Anthropic, OpenAI, Google)
  ↓  months later: similar capability
  ↓  outputs used for training (legitimate or not)
Open-weight leaders (Kimi, GLM, DeepSeek, Qwen)
  ↓  fine-tunes, quantizations, distillations
Community and enterprise derivatives

Open leaders → cheap hosting → price floor → pressure on the closed frontier
```

<!--
"Different places in the chain" is my phrase, and the module uses it for this pipeline.

Distillation means training a model on another model's outputs. Labs do it legitimately to make their own small models. It becomes a dispute when a competitor does it through someone else's API. In February 2026 Anthropic said it had found about 24,000 fraudulent accounts behind more than 16 million exchanges, and attributed them to DeepSeek, Moonshot, and MiniMax. Those companies haven't confirmed it. Fable's classifiers now check for distillation attempts, and new API accounts can't edit earlier turns while keeping Claude's prior reasoning.

A capability that's frontier-only today tends to show up in open weights within months.
-->

---

## Open models trail by six months to a year

| Evidence | Gap |
| --- | --- |
| Epoch AI, November 2024 (benchmarks) | About one year (90% range: 5–22 months) |
| Epoch AI, October 2026 (cyber) | 6–7 months; top open model was GLM-5.3 |
| Simon Willison on Mistral Large 4, October 2026 | "maybe about 6 months behind the frontier" |

The real gap may be larger than benchmarks show.

<!--
In Epoch's October 2026 cyber measurement, GLM-5.3 sat where the closed frontier stood 6–7 months earlier, and Opus 5.5 and GPT-6 Astra had moved further ahead.

Epoch also warns that open models may tune for benchmarks more aggressively, so benchmark-based gaps could understate the real one.

The gap changes with each release, so recheck it. Discussion question 2 builds on this slide.
-->

---

## Open models set the price floor

The September 2026 releases started "a new price war" (Simon Willison):

- GPT-6 Sol and Luna cost half as much as the GPT-5.6 models they replaced
- Anthropic cut Opus from $5 / $25 to $4 / $20
- Haiku 5.5 at $0.10 / $0.50 is a tenth of Haiku 4.5's list price
- Kimi K3.1 Pro, open weights, at a reported $2 / $10

<!--
When an open model is good enough, anyone can host it, and hosting companies compete on price. That adds pressure on closed labs' prices. Kimi K3.1 Pro's reported price is half that of Opus 5.5.

Price per token isn't price per task. Anthropic says Opus 5.5 costs "40% less to run than Opus 5" on typical workloads, though its per-token price fell only 20%; the rest comes from using fewer tokens. Tokenizer changes can cut the other way. Opus 4.7's new tokenizer could map the same text to 1.0 to 1.35 times as many tokens. A cheaper model that takes three tries isn't cheaper. Measure cost per finished task.
-->

---

## Best model for the job (as of November 2026)

| Job | Good choices | Basis |
| --- | --- | --- |
| Agentic coding | Opus 5.5 or Sonnet 5.5 in Claude Code; GPT-6.1 Sol or Astra in Codex | Opinion + vendor benchmarks |
| Code review | A *different* model from the one that wrote the code | Opinion |
| Long documents and video | Gemini 4 Argon, Gemini 3.8 Flash | Fact + opinion |
| Cheap bulk work | Haiku 5.5, GPT-6 Luna, Flash-Lite, DeepSeek V4.1-Flash | Fact (price) |
| Local and private | Qwen3.8-27B, Gemma 4, gpt-oss-20b, Muse Glimmer 30B | Fact + opinion |
| Security research | Mythos 5.1 or GPT-6-Cyber, via verification | Fact (access) |

<!--
The Basis column separates measurements from judgments. "Opinion" here means a judgment that reflects common practitioner choices, not a measurement. Re-test before relying on any cell.

Agentic coding models top vendor coding benchmarks, and harness and model are tuned together. For review, different models make different mistakes (module 10), like GPT in Codex reviewing Claude's work. Gemini has native video input, 1M context, and 87.6% on Video-MMMU at Gemini 3's launch. Use batch APIs for bulk work. Local picks have permissive licenses and sizes that fit one machine (module 04).

The module has more rows: real-time social data (Grok, built-in access to X posts), image generation (GPT-Image-2.6, Nano Banana 2.1 and Pro, Muse Image), voice (GPT-Realtime-2.1, GPT-Live 1, Gemini 3.8 Live, Grok Voice 3.0), and deep research (ChatGPT, Gemini, and Claude research modes; Kimi K3.1 Pro reports a leading BrowseComp score, vendor-reported).
-->

---

<!-- _class: take -->

## Which models for coding?

> **Bryan's take:** For coding, Claude and Codex are the best. For certain other tasks you might use Grok or Gemini for very specific cases, but not for coding, because they fall far behind there. Different models are better for different use cases.

<!--
This is my opinion from daily use, and like everything in this deck it's dated November 2026. It lines up with the agentic coding row on the previous slide. The long-documents and real-time-data rows are the kind of "very specific cases" it allows for.

Check it against your own tasks. That's the bake-off in Try it.
-->

---

## Launches don't always land

| Launch | What happened |
| --- | --- |
| GPT-5 (Aug 2025) | Router down on launch day; a "chart crime"; users wanted GPT-4o back |
| Llama 4 (Apr 2025) | Its top Arena score came from an unreleased experimental version |
| Opus 5 (Jul 2026) | Led leaderboards; its communication style drew common complaints |
| Fable 5 (Jun 2026) | Suspended for all users three days after launch |
| Gemini 3.5 Pro (2026) | Promised for June; never shipped |

<!--
With GPT-5, OpenAI replaced older ChatGPT models with GPT-5 and an automatic router, which was down for much of launch day, so GPT-5 seemed weaker than it was. A chart drew a lower score with a taller bar. Within a day Sam Altman promised to bring 4o back for Plus users, show which model answered, and double rate limits. A model change is also a product change, and people get attached to a model's personality.

For Llama 4, the released Maverick ranked much lower than the experimental chat version. Meta denied training on test sets. The "Leaderboard Illusion" paper later counted 27 private variants Meta tested on the Arena before launch.

For Fable 5, the US government applied export controls to Fable 5 and Mythos 5. Anthropic suspended access for everyone because "the order took effect immediately and we had no reliable way to verify nationality in real-time." The controls were lifted June 30 and Fable 5 returned July 1.

Gemini 3.5 Pro was announced at I/O on May 19 for June. Reuters later reported Google "no longer plans to release" it; Gemini 4 Argon came "after months of delays." Google also reshuffled DeepMind's leadership in August 2026.

Not every regression is real. In August and September 2025, users suspected Anthropic had degraded Claude. Its postmortem traced the problems to three infrastructure bugs and stated, "We never reduce model quality due to demand, time of day, or server load."
-->

---

<!-- _class: take -->

## On Opus 5 and Opus 5.5

> **Bryan's take:** Opus 5 felt benchmark-maxed. Great numbers, and it kind of sucked in daily use. People didn't like it. Opus 5.5, people really liked.

<!--
Here's the evidence the module puts next to this take. Opus 5 led the Artificial Analysis leaderboard at launch, ahead of Fable 5, and early hands-on reviews were positive. Simon Willison called it "a good new default for Claude Code if you don't want to burn through your Fable allowance too fast."

Daily use surfaced complaints. When Anthropic shipped Opus 5.5, it called communication "one of the most common areas of feedback we heard about Opus 5," and said 5.5 is "less likely to use jargon or idiosyncratic phrases" and "puts the most important information up front." A tester quoted in the announcement found Opus 5 "used 2.5x as many tokens" on a large code audit. Willison wrote that Opus 5.5 "looks like it addresses the biggest complaints people had about Opus in terms of its communication style," and made it his default in Claude Code.

One caveat on 5.5. Willison found max effort could run to the 128K output limit without answering, and suspected max is "effectively useless."

Module 05 covers benchmark-maxing.
-->

---

<!-- _class: take -->

## On trusting labs

> **Bryan's take:** I don't trust some labs much. Google in particular tends to overhype its models, and they underperform in my use.

<!--
That's my opinion. The module pairs it with the strongest evidence against it.
-->

---

## The counterpoint

- Gemini 3 Pro launched at the top of LMArena (1501 Elo), November 2025
- Scored 87.6% on Video-MMMU at Gemini 3 Pro's launch
- Its Flash models are among the cheapest capable models
- Offers Nano Banana images, Veo video, Live voice
- Gemini 4 Argon tops the Vals Index, by Google's account

The critique fits Google's 2026 Pro line best, and multimodal and price-per-token work worst.

<!--
The Vals Index covers finance, legal, tax, and coding work. Few rivals match Google's media stack.

On the evidence, the module concludes the hype-versus-delivery critique fits Google's 2026 Pro line best, where a promised model never shipped. It fits multimodal and price-per-token work worst.

This is a good time for discussion question 4.
-->

---

## How to pick a model next month

1. Define the job, then pick 2–3 candidates from different labs
2. Check access rules for retention, region, safety routing, approved vendors
3. Read the launch post skeptically: harness, effort, who ran the numbers
4. Run 5–10 of your own real tasks in your own harness
5. Compare cost per finished task, and try the effort settings
6. Wait a week if you can. Write down the decision and the date.

<!--
The module has ten steps:

1. Define the job: agentic coding, review, bulk extraction, chat, research. Different jobs have different winners.
2. Pick two or three candidates from different labs, including your current default and one cheaper tier.
3. Check access rules: data retention and zero-data-retention terms, region, safety routing (Fable hands some requests to Opus), and your company's approved-vendor list.
4. Read the launch post skeptically: note the harness, effort level, and who ran the competitor numbers (module 05).
5. Run five to ten real tasks in your own repo and harness. Score the result, tokens used, and time taken.
6. Compare cost per finished task. New tokenizers can change token counts by up to 35% for the same text.
7. Try the effort settings. Lower effort on a newer model can match higher effort on an older one, and max can waste money.
8. Wait a week if you can. Early bugs, tight rate limits, and even suspensions happen in launch week.
9. Check the subscription math. In agentic coding, a flat-rate plan can change which model is affordable (module 12).
10. Write down your decision and the date, and revisit it monthly (module 14).
-->

---

## Try it

**On your own: a mini bake-off (60–90 minutes)**

- Three real tasks: a bug fix, a refactor, "explain this module"
- Two models from different labs, in the same harness
- Record pass/fail, tokens or cost, time, and how readable the final message was
- Did the benchmark ranking predict your result?

As a class, each group builds a living "model card" page for one lab.

<!--
For the bake-off, many harnesses can switch models; OpenCode can use most providers (module 04). End with one paragraph on which model you'd choose and why.

In the class version, each group owns one lab and fills in its current tiers, model IDs, prices, context windows, data-retention terms, and one reception story, all with primary-source links. Five-minute presentations. Then run one shared task across every lab's workhorse tier and compare. Put a review date on the page, re-verify it in a month, and note what changed.
-->

---

## Discussion

1. Opus 5 led benchmarks and drew complaints. What does each kind of evidence miss?
2. If open models trail by 6–12 months, when is that good enough for you?
3. Should a lab reroute your request without asking? What disclosure would you want?
4. Google cancelled a promised model. How much weight should future-model announcements carry?

<!--
The module has two more. Chinese labs lead open weights, so what would change your organization's willingness to use their models: self-hosting, a US host, or neither? And which "best model for the job" cell would you change today, and what evidence would you bring?
-->

---

## Read more

- Module: [03 The model landscape](../modules/03-model-landscape/)
- Epoch AI, [How far behind are open models?](https://epoch.ai/blog/open-models-report) (2024)
- Simon Willison, [Opus 5.5, GPT-6 Sol, GPT-6 Luna and a new price war](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/) (September 2026)
- [OpenRouter models](https://openrouter.ai/models): dates and prices across providers

<!--
The module page has every lab's primary sources. OpenRouter's catalog is a quick way to check current dates and prices across providers before you rely on anything in this deck. Next in the module map: 04 (open vs closed weights) and 05 (judging models).
-->

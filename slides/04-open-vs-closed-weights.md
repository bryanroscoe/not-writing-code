---
marp: true
theme: not-writing-code
paginate: true
title: "04: Open weight vs closed weight"
description: "What open weights give you, what the licenses say, and what running a model yourself takes"
footer: "A Brief Introduction to Not Writing Code · 04 Open weight vs closed weight"
---

<!-- _class: lead -->

# 04: Open weight vs closed weight

What you get when you can download the model

<!--
This session covers what "open" actually means, what the licenses say, the safety debate, and the hardware math for running a model yourself.

Rough timing for a 45-minute session: Part 1 (what open means, why labs do it, and the safety debate) about 18 minutes, Part 2 (running and choosing) about 20 minutes, then the exercise and discussion. The hardware math is what people remember; leave time for it.

Model names, sizes, and licenses here are as of November 2026.
-->

---

## Why this matters

- Weights are the model. Closed labs keep them; open labs let you download them.
- Open models trail the closed frontier by months
- Open wins on control, privacy, cost at scale, and customization
- Closed wins on peak capability and convenience

Where the weights came from isn't where your data goes.

<!--
People often confuse these two things. Self-hosting a Chinese lab's weights keeps your data on your own machines. Calling that lab's own API sends it to servers in China. Those are different risk decisions, and the privacy slide near the end comes back to it.

Module 03 covers how far behind open models are.
-->

---

<!-- _class: divider -->

# Part 1

## What "open" means

<!--
Part 1 covers what weights are, the spectrum from closed to fully open, licenses, why labs release weights at all, and whether they should. About 18 minutes.
-->

---

## Weights are just big files

| Format | What it is |
| --- | --- |
| `.safetensors` | Standard on Hugging Face; holds only tensors, so loading can't run hidden code |
| `.gguf` | Single file for llama.cpp, Ollama, and LM Studio; usually already quantized |
| `.bin`, `.pt` (pickle) | Older PyTorch formats that can run arbitrary code when loaded |

Having the weights lets you run, fine-tune, and inspect a model. It doesn't tell you its training data or how to rebuild it.

<!--
A language model is a very large function: tokens in, a probability for each possible next token out. Its behavior is set by the weights, billions or trillions of numbers adjusted in training (module 01).

On pickle files, Hugging Face's own advice amounts to treating them like executables from strangers. Prefer safetensors.
-->

---

## The openness spectrum (as of November 2026)

| Category | What you get | Examples |
| --- | --- | --- |
| Closed / API-only | Access, no weights | Claude, GPT-6, Gemini, Grok, Muse Wonder |
| Open weight, restrictive license | Weights, with limits on use, scale, or attribution | Kimi K3, Qwen3.8-Max, GLM-5.3, Muse Spark Open, Llama 4 |
| Open weight, permissive license | Weights under Apache 2.0 or MIT | DeepSeek V4, gpt-oss, Gemma 4, Qwen3.8-27B |
| Open source AI (OSI definition) | Weights, training code, and data information | Few models qualify |
| Fully open | All that, plus the data, checkpoints, and logs | AI2's OLMo 3 |

<!--
The module adds MiniMax M3 as restrictive and Muse Glimmer (Apache 2.0) as permissive.

Fully open models like AI2's OLMo family publish the pretraining data (Dolma), training and evaluation code, intermediate checkpoints, and post-training data. They're the only kind you can study end to end. They usually trail the best open-weight models in raw capability.
-->

---

## "Open weight" isn't "open source"

Under the OSI Open Source AI Definition 1.0 (October 28, 2024), anyone may use, study, modify, and share it, for any purpose.

| It requires | Most "open" models publish it? |
| --- | --- |
| Data information, enough to build a substantially equivalent system | No |
| Code, the complete source to train and run it | No |
| Parameters, the weights | Yes |

<!--
Most "open" models publish only the weights. Labs are getting careful with the words. Moonshot calls Kimi K3 "open weight," not "open source," as Simon Willison noted. The OSI argued in 2023 that Llama's license isn't open source because of its use restrictions.

Discussion question 1 asks whether the OSI is right to require training data.
-->

---

## Licenses vary a lot

| License family | Terms | Examples |
| --- | --- | --- |
| Apache 2.0 | Use, modify, sell; keep notices; patent grant | gpt-oss, Gemma 4, Qwen3.8-27B, Muse Glimmer 30B |
| MIT | Use, modify, sell; keep the notice | DeepSeek V4 and V4.1 |
| Revenue-tiered custom (the 2026 trend) | Free, except hosting it as a service above a revenue line | Kimi K3, Qwen3.8-Max, GLM-5.3, Muse Spark Open |
| Default non-commercial | Commercial use needs notice or authorization | MiniMax M3 |
| Llama Community | Free under 700M monthly users; "Built with Llama" | Llama 3.x, Llama 4 |

<!--
Thresholds in the revenue-tiered licenses, as the module reports them: Kimi K3 above $20M over 12 months; Qwen3.8-Max above $50M for model-as-a-service; Muse Spark Open above $20M, with "Built with Muse Spark Open" attribution; GLM-5.3 above $10B for model-as-a-service needs a Z.ai security review; Mistral Large 4 needs a commercial license for model-as-a-service.

Among other families, "modified MIT" (Kimi K2 and K2.5, MiniMax M2 and M2.5) adds a display rule for very large products. MiniMax M3's community license needs prior authorization above $20M yearly revenue. Llama licenses require derivative model names to start with "Llama," and Llama 4's use policy withholds rights to its multimodal models from EU-domiciled individuals and companies. Gemma 1 to 3 used custom terms; Gemma 4 moved to Apache 2.0.

These clauses target competing companies that would host the model and sell it. For most engineers they change nothing; for inference providers they change a lot.
-->

---

## Read the license, every upgrade

| Family | Before | Now |
| --- | --- | --- |
| MiniMax | M2, M2.5: modified MIT | M3: default non-commercial |
| GLM | GLM-5: MIT | GLM-5.3: custom license |
| Kimi | K2: modified MIT | K3: revenue-tiered |

Check commercial use, thresholds, attribution, acceptable use, geography, outputs, patents, and your legal team's list.

<!--
Licenses change between versions of the same family.

The module's eight questions before using an open model at work:
1. Is commercial use allowed? Some licenses default to non-commercial or need notice.
2. Thresholds: monthly users, revenue, or model-as-a-service clauses. Does your company or a customer cross them?
3. Attribution and naming: must you display "Built with X," or name derivatives a certain way?
4. Acceptable-use policy: is it incorporated by reference, and can it change later?
5. Geography: are rights withheld in your region, such as Llama 4 multimodal in the EU?
6. Outputs and derivatives: can you use outputs to train other models, and do fine-tunes inherit the license?
7. Patents and warranty: Apache 2.0 includes a patent grant, MIT doesn't mention patents, and nearly all disclaim warranties.
8. Your legal team's approved-model list: get on it before you build.

This is engineering guidance, not legal advice.
-->

---

## Why labs give weights away

| Reason | Example |
| --- | --- |
| Ecosystem and standards | Qwen derivatives: over 40% of new models on Hugging Face by mid-2025 |
| Commoditize the complement | Zuckerberg's 2024 case for open models; Meta kept its best Muse closed |
| Sell the hosted version | Revenue-tiered licenses stop big hosts undercutting the lab |
| Talent and reputation | Researchers want to publish |
| Geopolitics and sovereignty | US 2025 AI Action Plan; Mistral's "AI sovereignty" pitch |
| Price pressure on rivals | A good-enough open model sets a price floor |

<!--
Labs have strategic reasons to give away models that cost tens of millions of dollars.

In 2024 Mark Zuckerberg argued that open models protect Meta from depending on a rival's closed platform. In 2026 Meta kept its best Muse models closed and released two open ones. Many open labs earn money from their own API. Revenue-tiered licenses let anyone self-host while stopping large hosting companies from undercutting the lab's own service.

On geopolitics, Chinese labs gain global adoption despite US chip export controls. The US government's 2025 AI Action Plan encouraged American open models. Mistral pitches Large 4 as trained and run under European law.
-->

---

## The safety debate

| For open weights | Against |
| --- | --- |
| Defenders can use them without permission | Release can't be undone; safeguards can be removed |
| Data never leaves your machines | LoRA fine-tuning cheaply strips safety training |
| You can study the internals | An "abliterated" Muse Spark Open appeared within two days |
| No single point of control | Dangerous capability arrives in open models months later |

Most current policy treats today's open models as acceptable and watches the frontier.

<!--
On the pro side, in July 2026 Hugging Face responded to an intrusion by an autonomous OpenAI test agent that had escaped its sandbox. Commercial model APIs blocked its incident-analysis requests, so the team used a self-hosted open-weight model. In 2024 the US NTIA recommended monitoring open-weight risks rather than restricting them.

Against, research showed LoRA fine-tuning cheaply undoes safety training (Lermen et al. and Gade et al., 2023). Refusal behavior is often controlled by a single direction in the model's activations, which can be edited out, called "abliteration" (Arditi et al., 2024). Epoch estimates open models trail the closed frontier by 6 to 7 months on cyber tasks, so capabilities closed labs gate today will be downloadable within months. And in 2025, NIST's CAISI found agents built on DeepSeek R1-0528 were on average 12 times more likely than US frontier models to follow hijacking instructions. That's a property of the weights, wherever you run them (module 11).

Discussion question 2 asks you to weigh these risks.
-->

---

<!-- _class: divider -->

# Part 2

## Running and choosing open models

<!--
Part 2 is the hardware math, the tools, hosted options, coding harnesses, privacy, and when to choose open over closed. About 20 minutes.
-->

---

## Memory ≈ parameters × bytes per parameter

| Precision | Bytes per parameter | 8B | 30B | 120B |
| --- | --- | --- | --- | --- |
| BF16 / FP16 (as released) | 2 | 16 GB | 60 GB | 240 GB |
| 8-bit | ~1 | ~8.5 GB | ~32 GB | ~125 GB |
| **4-bit** (the common local default) | ~0.55–0.6 | ~4.7 GB | **~17 GB** | ~65 GB |
| ~3-bit | ~0.4 | ~3.5 GB | ~13 GB | ~50 GB |

8-bit is close to lossless. Below about 3 bits, quality drops noticeably.

<!--
FP32 would be 4 bytes per parameter, so 120 GB for a 30B model.

Quantization stores each weight with fewer bits. 4-bit has modest quality loss, and coding and long reasoning tend to suffer before casual chat does. Some models are trained with quantization in mind, called quantization-aware training, so their 4-bit release loses little. Both gpt-oss and Kimi K3 ship natively in 4-bit MXFP4.

Point at the bold cell. A 30B model at 4-bit needs about 17 GB. That's comfortable on a 36 GB Mac or a 24 GB GPU, and too big for an 18 GB Mac.
-->

---

## Then add room for context

KV bytes per token ≈ 2 × layers × KV heads × head dimension × bytes per value

For 48 layers, 8 KV heads, head dimension 128, 16-bit values:

- 2 × 48 × 8 × 128 × 2 ≈ 0.2 MB per token
- A 32K-token context ≈ 6 GB on top of the weights

Budget 20–50% extra for real coding contexts.

<!--
While generating, the model stores keys and values for every token in the context. That's the KV cache from module 01, and it grows with context length. The example model is illustrative, not a specific product.

Many 2026 models use attention variants that shrink this a lot, like latent attention in DeepSeek, Kimi Delta Attention in K3, and hybrid Mamba layers in Nemotron. Check the model card.
-->

---

## MoE changes speed, not memory

- Total parameters decide memory, because every expert must be loaded
- Active parameters decide speed, because only these are read per token

| Model | Total | Active | What that means |
| --- | --- | --- | --- |
| Gemma 4 26B-A4B | 26B | ~4B | Memory of a 26B model, speed of a 4B |
| Kimi K3 | 2.8T | 104B | ~1.56 TB at 4-bit, so data-center hardware |

<!--
A mixture-of-experts model has many expert sub-networks and uses only a few for each token (module 01).

Almost every frontier open model of 2026 is a sparse MoE with roughly 2 to 6% of parameters active per token. Kimi K3 activates 104B of 2.8T. DeepSeek V4-Pro activates 49B of 1.6T. Muse Spark Open activates 42B of 816B. Reflection's Beam activates 23B of 501B. That makes them cheaper per token to train and serve, and it pushes them out of reach of single machines, because memory scales with total parameters.

The open models people actually run locally (Gemma 4, Qwen3.8-27B, gpt-oss-20b, Muse Glimmer 30B) are a separate, smaller class. That split is one reason "open" covers such different experiences.
-->

---

## Speed is mostly memory bandwidth

tokens per second ≲ memory bandwidth ÷ bytes of active weights

- A dense 30B at 4-bit (~17 GB) on ~270 GB/s tops out near 16 tokens/s
- A 3B-active MoE at 4-bit (~1.7 GB per token) is several times faster
- GPU VRAM is fast, but the model must fit
- Apple unified memory fits bigger models, with lower bandwidth

<!--
Generating each token means reading all active weights from memory once. Bandwidth sets an upper bound. Actual speed is lower. This is why MoE models are popular locally.

A discrete GPU, such as a 24 GB RTX 4090, has its own fast VRAM. The model must fit in VRAM to run fast; spilling to system RAM makes it far slower.

Apple silicon Macs share one pool of unified memory between CPU and GPU, so a 64 to 128 GB Mac can load models no consumer GPU can. By default macOS limits how much of that memory the GPU can wire, roughly two-thirds to three-quarters of RAM. You can raise it with sudo sysctl iogpu.wired_limit_mb, leaving several GB for the OS and apps. The value resets on reboot. Check current guidance for your macOS version first.
-->

---

## What fits where (approximate, 4-bit)

| Machine | Comfortable |
| --- | --- |
| 18 GB Mac | 4B–14B dense: Gemma 4 E4B or 12B, small Qwen models |
| 24 GB GPU | 27B–32B dense: Qwen3.8-27B, Gemma 4 31B, Muse Glimmer 30B |
| 36 GB Mac | The same 27B–32B models; Gemma 4 26B-A4B (fast) |
| 64 GB Mac | 70B-class dense (slow) |
| 128 GB Mac or workstation | gpt-oss-120b; 120B-A12B MoE such as Nemotron 3 Super |
| 8× 80 GB data-center GPUs | 300B–800B MoE: GLM-5.3 at 4-bit (~420 GB) |
| Multi-node clusters | Kimi K3 / K3.1 Pro, DeepSeek V4-Pro, Qwen3.8-2.4T |

<!--
Roughly usable memory for the model: about 12 GB on an 18 GB Mac, 22 GB on a 24 GB GPU, 24 to 27 GB on a 36 GB Mac, 45 to 48 GB on a 64 GB Mac, 96 GB or more on a 128 GB machine, and about 640 GB across eight 80 GB GPUs.

Stretch options from the module: gpt-oss-20b (about 13 GB as shipped) on an 18 GB Mac with short context and a raised GPU limit; about 100B MoE at 3-bit on 64 GB; roughly 1T models at 4-bit, such as Mistral Large 4 (about 550 GB), on eight 80 GB GPUs.

Model cards can ask for more than the math suggests. Muse Spark Open's 4-bit weights come to roughly 450 to 500 GB by the math above, but Meta's card asks for at least 700 GB of GPU memory, or two M5 Ultra Mac Studios.

The leading frontier open models can't run on a laptop at useful quality. Most people use them through hosted providers. "Local" usually means a model one or two tiers smaller.
-->

---

## Tools for running open models

| Tool | Best for |
| --- | --- |
| Ollama | The easiest start: `ollama run gpt-oss:20b` |
| LM Studio | A GUI; Mac users; GGUF and Apple MLX models |
| llama.cpp | The engine under many local tools; `llama-server` |
| MLX / mlx-lm | Fast inference and LoRA fine-tuning on Apple silicon |
| vLLM | Serving a team or product |
| SGLang | Agent-heavy serving |

Check free disk space first. Each tool keeps its own copy of the weights.

<!--
Ollama runs a local API on port 11434, and that command downloads about 14 GB the first time. LM Studio runs a local server on port 1234. llama-server gives an OpenAI-compatible endpoint on port 8080. vLLM is a high-throughput GPU server built on PagedAttention; serving gpt-oss-120b with it needs an 80 GB-class GPU. SGLang adds prefix caching and structured output, and several 2026 model cards recommend it.

Clean up when you're done with ollama rm and the model name, or LM Studio's model manager.

On tuning, open weights can be changed with LoRA, which trains small add-on matrices, or QLoRA, which does it on a 4-bit base so one GPU can fine-tune a large model. Common tools are Unsloth, Hugging Face TRL, and mlx-lm. Closed models can only be tuned through whatever service the lab offers. Module 02 covers tuning in depth.
-->

---

## You don't have to own the hardware

| Option | Examples |
| --- | --- |
| Router and marketplace | OpenRouter: one API key, hundreds of models |
| GPU clouds for open models | Together AI, Fireworks, Baseten, DeepInfra |
| Custom chips, very fast output | Groq, Cerebras |
| The labs' own APIs | DeepSeek, Moonshot, Z.ai, MiniMax, Alibaba Cloud, Mistral |
| Hyperscalers | AWS Bedrock, Google Vertex AI, Microsoft Foundry |

The "same" open model can behave differently across hosts. Pin a provider when you evaluate.

<!--
Providers host open weights and charge per token. OpenRouter shows per-provider prices and routing.

Differences between hosts come from quantization, chat templates, context limits, and tool-call parsing. If a model seems worse than its benchmarks, try the lab's own API or another host before giving up on it.
-->

---

## Open models in coding harnesses

| Harness | How |
| --- | --- |
| OpenCode | MIT-licensed; 200+ providers; detects local Ollama, LM Studio, vLLM |
| Claude Code | Point it at an Anthropic-compatible endpoint (Z.ai, Kimi, DeepSeek) |
| Codex CLI | `codex --oss` with Ollama or LM Studio |

Anthropic doesn't support routing Claude Code to non-Claude models. It often works; test first.

<!--
OpenCode reaches providers through the Models.dev catalog. Connect one with /connect and pick a model with /models. OpenCode also sells a curated-model subscription, OpenCode Go, from $10 per month.

For Claude Code, Z.ai documents a settings file that sets the Anthropic base URL to its own endpoint and maps the Opus, Sonnet, and Haiku slots to GLM-5.3 models, for its GLM Coding Plan. Moonshot describes its Messages API as compatible with "the Anthropic SDK, Claude Code, and similar tools." DeepSeek's V4 API accepts both OpenAI and Anthropic formats. Anthropic's docs say it "doesn't support routing Claude Code to non-Claude models through any gateway." Features built around Claude's API can break: thinking blocks, tool formats, caching, effort settings. Kimi's docs, for example, say you must pass back the full assistant message, including reasoning_content, for multi-turn tool use.

Codex CLI sets the local provider with oss_provider in ~/.codex/config.toml, and can use any compatible endpoint defined under model_providers.

A local 20B to 30B model handles small, well-specified edits and explanations. It struggles with long multi-file agentic tasks that frontier models finish. Hosted frontier open models like Kimi K3.1 Pro and GLM-5.3 come much closer. Flat-rate coding plans from MiniMax, Z.ai, and others compete with Claude and ChatGPT subscriptions on price (module 12).
-->

---

## Where do your prompts and code go?

| Setup | Your data goes to |
| --- | --- |
| Self-hosted open weights | Nowhere outside your infrastructure |
| US or EU host serving Chinese-origin weights | That host, under its terms and jurisdiction |
| A Chinese lab's own API | That company's servers; Chinese law applies |
| A closed US lab's API | That lab's servers, under retention terms you can often set |

Self-hosting fixes data flow, not model behavior.

<!--
Where the weights came from and where the computation runs are separate questions.

If you self-host, you own security, updates, and monitoring. Use safetensors, and avoid trust_remote_code unless you've reviewed the code. With a US or EU host such as Together, Fireworks, or Bedrock, data handling depends on the host, but model behavior is the same as the weights anywhere. DeepSeek's privacy policy says it stores personal data "in People's Republic of China"; check your company's policy before sending source code there. Among closed US labs, Anthropic offers US-only inference at 1.1 times the price on Claude 4.6 and later, and Fable-class models require 30-day retention.

Behavior travels with the weights. CAISI found DeepSeek models repeated inaccurate Chinese Communist Party narratives four times as often as US reference models. Download weights only from the publisher's official repository, check hashes, and watch for "uncensored" or "abliterated" re-uploads.

Self-hosting isn't automatically safer. It adds unpatched inference servers, endpoints exposed without authentication, files from unofficial mirrors, and no vendor abuse monitoring. An open model running an agent with shell access is as exposed to prompt injection as a closed one, sometimes more.
-->

---

## When to choose open vs closed

| Situation | Lean toward |
| --- | --- |
| Hardest agentic coding, large refactors | Closed frontier |
| Code or data can't leave your network | Open, self-hosted |
| Millions of bulk calls | Open, or a cheap closed tier |
| Fine-tuning on proprietary data | Open |
| Offline use, or a frozen model for audits | Open |
| Small team, no ML ops, wants it to just work | Closed |

<!--
Closed frontier models are still months ahead on long tasks. Self-hosted data never leaves your infrastructure. For bulk jobs it's price per token; compare against Haiku 5.5 or GPT-6 Luna at $0.10 / $0.50 per million tokens, as of November 2026. With open weights you control the model, and it can't change under you, which matters for audits and regulated workflows. Closed means no hardware and no serving stack.

The module has more rows. If closed-model safeguards block security research, go open or use a lab's verification program. To teach how models work, go open and small, ideally fully open like OLMo. If company policy bars a vendor's jurisdiction, use open weights from a trusted host, or a different vendor.
-->

---

<!-- _class: take -->

## Where open models sit

> **Bryan's take:** For coding, Claude and Codex are the best in my opinion. Open models like Kimi sit at a different place in the chain.

<!--
"A different place in the chain" is the pipeline in module 03: closed frontier first, open-weight leaders months later, then community derivatives.

When you compare a self-hosted or per-token open model against a flat-rate plan, the module also points to my view in module 12 that subscriptions, not API billing, are what make heavy agentic use affordable.
-->

---

## Try it

**Run a model and measure it (45 minutes)**

- Check free disk and memory; pick a model that leaves headroom
- Run it in Ollama or LM Studio; have it explain and test a function
- Record tokens per second, memory used, and whether the test passes
- Compare with a hosted frontier model, then delete the local model

As a team, do a license review for a hypothetical product.

<!--
On your own, check disk and memory with df -h and Activity Monitor or nvidia-smi. Pick a model from the "what fits where" table. Write three sentences comparing quality, speed, and privacy against the hosted model. Delete the model afterward with ollama rm and the model name.

For teams, give each group two licenses from this module, one permissive and one custom. Each group answers the eight-question checklist for a SaaS tool with 2 million users and $30M in yearly revenue that hosts the model for customers. Groups present which models the product could use as-is, which need an agreement, and which are off the table. Then discuss: what surprised you, and which clauses would your legal team flag?
-->

---

## Discussion

1. Should "open source AI" require training data, or are open weights enough?
2. Is self-hosting a Chinese lab's weights meaningfully different from an American lab's API?
3. Revenue-tiered licenses restrict only large hosts. Is that fair? Is it "open"?
4. What share of your team's work could a local 30B model handle well?

<!--
For question 2, ask people to list the risks each option addresses and the risks it leaves open. The privacy slide is the reference.

For question 4, ask what evidence would settle it.

The module has one more: if a lab's open model is safe today, what would have to be true for it to be safe to release one six months more capable?
-->

---

## Read more

- Module: [04 Open weight vs closed weight](../modules/04-open-vs-closed-weights/)
- [OSI Open Source AI Definition 1.0](https://opensource.org/ai/open-source-ai-definition) (October 2024)
- Epoch AI, [Open-weight models trail closed models in cyber capabilities by 6–7 months](https://epoch.ai/data-insights/open-closed-cyber-eci-gap) (2026)
- NIST, [CAISI evaluation of DeepSeek AI models](https://www.nist.gov/news-events/news/2025/09/caisi-evaluation-deepseek-ai-models-finds-shortcomings-and-risks) (2025)

<!--
The module page has every model card and license link. Re-read a model's license and card before you rely on anything in this deck; both change between versions.
-->

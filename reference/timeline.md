# Timeline

> **Last verified:** 2026-11-08 · Covers June 2017 to early November 2026.

This page lists dated events in AI-accelerated software engineering: key papers, model launches, tools, standards and incidents. Each row links to a primary source where one exists, or to reputable reporting where it doesn't.

How to read it:

- **Dates** are first public availability in US time. API dates can lag app launches by days. Where they differ, both are noted. "YYYY-MM" means only the month is certain.
- **Model details** (prices, context windows, IDs) live in [module 03](../modules/03-model-landscape.md). This page gives just enough to place each event.
- **"Reported"** marks events confirmed only by secondary sources.
- The field moves monthly. If you find an error, fix it here and in module 03.

## 2017–2019: the transformer and the first GPTs

| Date | Event | Why it matters | Source |
| --- | --- | --- | --- |
| 2017-01-23 | Sparsely-gated mixture-of-experts layer paper | Origin of the MoE design behind most 2026 open models | [arXiv](https://arxiv.org/abs/1701.06538) |
| 2017-06-12 | "Attention Is All You Need" (Vaswani et al.) | Introduced the transformer, the architecture behind every model here | [arXiv](https://arxiv.org/abs/1706.03762) |
| 2018-06-11 | OpenAI GPT-1 paper ("Improving Language Understanding by Generative Pre-Training") | Showed pretraining plus fine-tuning works for language | [OpenAI (PDF)](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) |
| 2018-10-11 | Google's BERT | Made pretrained transformers the default in NLP | [arXiv](https://arxiv.org/abs/1810.04805) |
| 2019-02-14 | OpenAI GPT-2, initially withheld over misuse concerns | First major "too dangerous to release" debate about model weights | [OpenAI](https://openai.com/index/better-language-models/) |

## 2020–2021: scaling, and code models arrive

| Date | Event | Why it matters | Source |
| --- | --- | --- | --- |
| 2020-01-23 | Scaling laws for neural language models (Kaplan et al.) | Showed loss falls predictably with model size, data and compute | [arXiv](https://arxiv.org/abs/2001.08361) |
| 2020-05-28 | GPT-3 paper, "Language Models are Few-Shot Learners" | Prompting alone could do new tasks; start of the API era | [arXiv](https://arxiv.org/abs/2005.14165) |
| 2021-01-11 | Switch Transformers | Scaled MoE to a trillion parameters | [arXiv](https://arxiv.org/abs/2101.03961) |
| 2021-06-17 | LoRA paper | Cheap fine-tuning that later made open-model customization practical | [arXiv](https://arxiv.org/abs/2106.09685) |
| 2021-06-29 | GitHub Copilot technical preview | First mass-market AI pair programmer (autocomplete in the IDE) | [GitHub](https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/) |
| 2021-07-07 | OpenAI Codex paper and HumanEval benchmark | The model behind Copilot; HumanEval became the first standard coding benchmark | [arXiv](https://arxiv.org/abs/2107.03374) |

## 2022: instruction tuning, reasoning prompts and ChatGPT

| Date | Event | Why it matters | Source |
| --- | --- | --- | --- |
| 2022-01-28 | Chain-of-thought prompting paper | "Think step by step" improved reasoning, the seed of reasoning models | [arXiv](https://arxiv.org/abs/2201.11903) |
| 2022-03-04 | InstructGPT (RLHF) paper | Human-feedback training made models follow instructions | [arXiv](https://arxiv.org/abs/2203.02155) |
| 2022-03-29 | Chinchilla scaling paper | Data matters as much as size; reshaped how models are trained | [arXiv](https://arxiv.org/abs/2203.15556) |
| 2022-10-06 | ReAct paper (reason plus act) | The pattern behind tool-using agents | [arXiv](https://arxiv.org/abs/2210.03629) |
| 2022-11-30 | ChatGPT launches | Brought LLMs to the public; fastest-growing consumer app of its time | [OpenAI](https://openai.com/index/chatgpt/) |
| 2022-12-15 | Anthropic's Constitutional AI paper | Training with written principles; basis of Claude's alignment approach | [arXiv](https://arxiv.org/abs/2212.08073) |

## 2023: GPT-4, Claude, Llama and open weights

| Date | Event | Why it matters | Source |
| --- | --- | --- | --- |
| 2023-02-09 | Toolformer paper | Models can learn when to call tools | [arXiv](https://arxiv.org/abs/2302.04761) |
| 2023-02-24 | Meta's LLaMA | Leaked, then widely used; started the open-weight boom | [arXiv](https://arxiv.org/abs/2302.13971) |
| 2023-03-14 | GPT-4 | Big jump in reasoning and coding; set the frontier for a year | [OpenAI](https://openai.com/index/gpt-4-research/) |
| 2023-03-14 | Anthropic launches Claude | Second major closed-frontier lab enters | [Anthropic](https://www.anthropic.com/news/introducing-claude) |
| 2023-05-23 | QLoRA paper | Fine-tune large models on one GPU | [arXiv](https://arxiv.org/abs/2305.14314) |
| 2023-07-11 | Claude 2 | 100K context; Claude becomes a coding option | [Anthropic](https://www.anthropic.com/news/claude-2) |
| 2023-07-18 | Llama 2, licensed for commercial use | Made open weights viable for companies; OSI disputed "open source" | [Meta](https://ai.meta.com/blog/llama-2/), [OSI](https://opensource.org/blog/metas-llama-2-license-is-not-open-source) |
| 2023-09-12 | vLLM / PagedAttention paper | Efficient serving; vLLM became the standard open-model server | [arXiv](https://arxiv.org/abs/2309.06180) |
| 2023-10-10 | SWE-bench | Real GitHub issues as a coding benchmark; later the yardstick for agents | [arXiv](https://arxiv.org/abs/2310.06770) |
| 2023-10-31 | Papers show LoRA cheaply removes Llama 2's safety training | Core evidence in the open-weight safety debate | [arXiv](https://arxiv.org/abs/2310.20624) |
| 2023-12-06 | Google Gemini 1.0 | Google's native multimodal family | [Google](https://blog.google/technology/ai/google-gemini-ai/) |
| 2023-12-11 | Mistral's Mixtral 8x7B (open MoE) | Showed open MoE models could rival larger dense ones | [Mistral](https://mistral.ai/news/mixtral-of-experts) |

## 2024: long context, agents and MCP

| Date | Event | Why it matters | Source |
| --- | --- | --- | --- |
| 2024-03-04 | Claude 3 family (Haiku, Sonnet, Opus) | Introduced the three-tier naming still used in 2026 | [Anthropic](https://www.anthropic.com/news/claude-3-family) |
| 2024-03-12 | Cognition's Devin, "AI software engineer" demo | Popularized the autonomous coding agent idea, and the hype debate | [Cognition](https://www.cognition.ai/blog/introducing-devin) |
| 2024-04-18 | Llama 3 | Strong open weights from Meta | [Meta](https://ai.meta.com/blog/meta-llama-3/) |
| 2024-05-13 | GPT-4o | Fast, cheap multimodal flagship; later the center of the 2025 sycophancy and GPT-5 backlash stories | [OpenAI](https://openai.com/index/hello-gpt-4o/) |
| 2024-06-20 | Claude 3.5 Sonnet and Artifacts | Became developers' favorite coding model for a year | [Anthropic](https://www.anthropic.com/news/claude-3-5-sonnet) |
| 2024-07-23 | Llama 3.1 405B; Zuckerberg's "Open Source AI Is the Path Forward" | First frontier-scale open model; Meta's open strategy at its peak | [Meta](https://ai.meta.com/blog/meta-llama-3-1/), [Meta](https://about.fb.com/news/2024/07/open-source-ai-is-the-path-forward/) |
| 2024-07-30 | NTIA report on open model weights | US government recommended monitoring, not restricting, open weights | [NTIA](https://ntia.gov/issues/artificial-intelligence/open-model-weights-report) |
| 2024-08-13 | SWE-bench Verified | Human-checked subset that became the headline coding benchmark | [OpenAI](https://openai.com/index/introducing-swe-bench-verified/) |
| 2024-09-12 | OpenAI o1-preview | First widely available reasoning model; thinking before answering | [OpenAI](https://openai.com/index/introducing-openai-o1-preview/) |
| 2024-10-22 | Claude computer use and upgraded Claude 3.5 Sonnet | Models controlling GUIs; big jump on SWE-bench | [Anthropic](https://www.anthropic.com/news/3-5-models-and-computer-use) |
| 2024-10-28 | OSI Open Source AI Definition 1.0 | Defined "open source AI": weights, code and data information | [OSI](https://opensource.org/blog/the-open-source-initiative-announces-the-release-of-the-industrys-first-open-source-ai-definition) |
| 2024-11-04 | Epoch AI: open models lag the frontier by about a year | First careful estimate of the open-closed gap | [Epoch AI](https://epoch.ai/blog/open-models-report) |
| 2024-11-25 | Anthropic introduces the Model Context Protocol (MCP) | Open standard for connecting models to tools and data | [Anthropic](https://www.anthropic.com/news/model-context-protocol) |
| 2024-12-26 | DeepSeek-V3 | Frontier-class open MoE trained cheaply; set up the R1 moment | [arXiv](https://arxiv.org/abs/2412.19437) |

## 2025: reasoning, coding agents and vibe coding

| Date | Event | Why it matters | Source |
| --- | --- | --- | --- |
| 2025-01-20 | DeepSeek-R1 (open weights, MIT) | Open reasoning model near o1; shook markets; start of Chinese open-weight leadership | [arXiv](https://arxiv.org/abs/2501.12948), [DeepSeek](https://api-docs.deepseek.com/news/news250120) |
| 2025-02-02 | Andrej Karpathy coins "vibe coding" | Named the practice of "forgetting the code exists" and accepting AI output | [X](https://x.com/karpathy/status/1886192184808149383) |
| 2025-02-24 | Claude 3.7 Sonnet and Claude Code (research preview) | Anthropic's terminal coding agent debuts | [Anthropic](https://www.anthropic.com/news/claude-3-7-sonnet) |
| 2025-02-27 | OpenAI GPT-4.5 | Largest non-reasoning GPT; showed limits of pure scale | [OpenAI](https://openai.com/index/introducing-gpt-4-5/) |
| 2025-03-18 | METR "Measuring AI Ability to Complete Long Software Tasks" | Time-horizon metric: task length agents can do doubles about every 7 months | [arXiv](https://arxiv.org/abs/2503.14499) |
| 2025-03-25 | Gemini 2.5 Pro | Google takes the lead on many leaderboards | [Google](https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/) |
| 2025-04-05 | Llama 4 Scout and Maverick | Disappointing reception; Arena used an unreleased "experimental" variant | [Meta](https://ai.meta.com/blog/llama-4-multimodal-intelligence/), [TechCrunch](https://techcrunch.com/2025/04/11/metas-vanilla-maverick-ai-model-ranks-below-rivals-on-a-popular-chat-benchmark/) |
| 2025-04-14 | GPT-4.1 (API) | 1M-token context; tuned for coding and instruction following | [OpenAI](https://openai.com/index/gpt-4-1/) |
| 2025-04-16 | OpenAI o3 and o4-mini; Codex CLI open-sourced | OpenAI's terminal coding agent | [OpenAI](https://openai.com/index/introducing-o3-and-o4-mini/), [GitHub](https://github.com/openai/codex) |
| 2025-04-29 | OpenAI rolls back a sycophantic GPT-4o update | A model update can change personality in harmful ways overnight | [OpenAI](https://openai.com/index/sycophancy-in-gpt-4o/) |
| 2025-04-29 | "The Leaderboard Illusion" paper | Documented private Arena testing (27 Llama 4 variants) | [arXiv](https://arxiv.org/abs/2504.20879) |
| 2025-04-29 | Qwen3 family (open, Apache 2.0) | Qwen becomes the most fine-tuned open base | [Qwen](https://qwenlm.github.io/blog/qwen3/) |
| 2025-05-16 | OpenAI Codex cloud agent (research preview) | Parallel coding tasks in cloud sandboxes | [OpenAI](https://openai.com/index/introducing-codex/) |
| 2025-05-19 | GitHub Copilot coding agent | Assign an issue, get a pull request | [GitHub](https://github.blog/news-insights/product-news/github-copilot-meet-the-new-coding-agent/) |
| 2025-05-22 | Claude Opus 4 and Sonnet 4; Claude Code generally available | Claude Code becomes a mainstream tool | [Anthropic](https://www.anthropic.com/news/claude-4) |
| 2025-06-12 | SEAL, "Self-Adapting Language Models" (MIT) | Research on models that write their own weight updates | [arXiv](https://arxiv.org/abs/2506.10943) |
| 2025-06-19 | Tobi Lütke popularizes "context engineering" (Karpathy follows on Jun 25) | Shift from prompt wording to managing everything in the context | [X (Lütke)](https://x.com/tobi/status/1935533422589399127), [X (Karpathy)](https://x.com/karpathy/status/1937902205765607626) |
| 2025-06-25 | Google Gemini CLI (open source) | Third major terminal agent, with a free tier | [Google](https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/) |
| 2025-07-09 | xAI Grok 4 | xAI's first model at the top of several benchmarks | [xAI](https://x.ai/news/grok-4) |
| 2025-07-10 | METR randomized trial: experienced developers 19% slower with early-2025 AI tools | The most cited skeptical productivity result | [arXiv](https://arxiv.org/abs/2507.09089) |
| 2025-07-11 | Moonshot Kimi K2 (1T-parameter open MoE) | Open model built for agentic coding | [Moonshot](https://moonshotai.github.io/Kimi-K2/) |
| 2025-07-22 | Qwen3-Coder | Open coding model with its own CLI | [Qwen](https://qwenlm.github.io/blog/qwen3-coder/) |
| 2025-07-23 | America's AI Action Plan encourages open models | US policy turns explicitly pro-open-weight | [White House (PDF)](https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf) |
| 2025-07-28 | Z.ai GLM-4.5 | GLM becomes a leading open coding model | [Z.ai](https://z.ai/blog/glm-4.5) |
| 2025-08-04 | Nathan Lambert launches the ATOM Project | Argued the US had lost open-model leadership to China | [Interconnects](https://www.interconnects.ai/p/atom-project) |
| 2025-08-05 | OpenAI gpt-oss-120b and 20b (Apache 2.0) | OpenAI's first open weights since GPT-2 | [OpenAI](https://openai.com/index/introducing-gpt-oss/), [Hugging Face](https://huggingface.co/openai/gpt-oss-120b) |
| 2025-08-05 | Claude Opus 4.1 | Incremental coding upgrade | [Anthropic](https://www.anthropic.com/news/claude-opus-4-1) |
| 2025-08-07 | GPT-5 launches; router outage, "chart crime," GPT-4o backlash | A rocky launch; 4o restored for paid users within a day | [OpenAI](https://openai.com/index/introducing-gpt-5/), [TechCrunch](https://techcrunch.com/2025/08/08/sam-altman-addresses-bumpy-gpt-5-rollout-bringing-4o-back-and-the-chart-crime/) |
| 2025-08 | AGENTS.md published as a shared format for agent instructions | One file for many agents instead of CLAUDE.md, .cursorrules and others | [agents.md](https://agents.md/) |
| 2025-09-15 | GPT-5-Codex | Coding-tuned GPT-5 for Codex (API Sep 23) | [OpenAI](https://openai.com/index/introducing-upgrades-to-codex/) |
| 2025-09-17 | Anthropic postmortem on three infrastructure bugs | "We never reduce model quality due to demand"; quality dips were bugs | [Anthropic](https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues) |
| 2025-09-29 | Claude Sonnet 4.5 | Long-running agent work; new top coding model at launch | [Anthropic](https://www.anthropic.com/news/claude-sonnet-4-5) |
| 2025-09-30 | NIST CAISI evaluation of DeepSeek models | Found performance gaps and higher agent-hijacking rates | [NIST](https://www.nist.gov/news-events/news/2025/09/caisi-evaluation-deepseek-ai-models-finds-shortcomings-and-risks) |
| 2025-10-15 | Claude Haiku 4.5 | Small model near earlier Sonnet quality | [Anthropic](https://www.anthropic.com/news/claude-haiku-4-5) |
| 2025-10-16 | Anthropic Agent Skills | Folders of instructions and scripts loaded on demand | [Anthropic](https://www.anthropic.com/news/skills) |
| 2025-10-29 | Cursor 2.0 and its Composer model | Leading AI IDE ships its own coding model and multi-agent UI | [Cursor](https://cursor.com/blog/2-0) |
| 2025-11-06 | Kimi K2 Thinking | Open reasoning agent near the closed frontier on some benchmarks | [Moonshot](https://moonshotai.github.io/Kimi-K2/thinking.html) |
| 2025-11-13 | GPT-5.1 and GPT-5.1-Codex (API) | Faster, more steerable GPT-5 | [OpenAI changelog](https://developers.openai.com/api/docs/changelog) |
| 2025-11-18 | Gemini 3 Pro and Google Antigravity | Topped LMArena at 1501 Elo; Google's agentic IDE | [Google](https://blog.google/products/gemini/gemini-3/), [Antigravity](https://antigravity.google/blog/introducing-google-antigravity) |
| 2025-11 | AI2 OLMo 3 (fully open) | Best fully open model family: data, code and checkpoints | [AI2](https://allenai.org/blog/olmo3) |
| 2025-11-24 | Claude Opus 4.5 | Opus price cut to $5 / $25 | [Anthropic](https://www.anthropic.com/news/claude-opus-4-5) |
| 2025-12-09 | Agentic AI Foundation formed (Linux Foundation): MCP, goose, AGENTS.md | Agent standards move to neutral governance | [Linux Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation), [Anthropic](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation) |
| 2025-12-11 | GPT-5.2 | OpenAI's year-end flagship | [OpenAI](https://openai.com/index/introducing-gpt-5-2/) |

## 2026: the year of monthly releases

| Date | Event | Why it matters | Source |
| --- | --- | --- | --- |
| 2026-01-01 | Steve Yegge, "Welcome to Gas Town" (eight stages of AI-assisted development) | A widely shared map of how developers move from autocomplete to agent fleets | [Medium](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04) |
| 2026-01 | Claude Cowork (research preview) | Claude Code-style agent for non-coding knowledge work | [Claude](https://claude.com/blog/cowork-research-preview) |
| 2026-01-14 | Cursor reports hundreds of agents building a browser from scratch | Showcase and stress test of long-running multi-agent coding; critics found quality gaps | [Cursor](https://cursor.com/blog/scaling-agents) |
| 2026-01 | Kimi K2.5 (open) | Moonshot's multimodal agentic update | [Hugging Face](https://huggingface.co/moonshotai/Kimi-K2.5) |
| 2026-01 (late) | Clawdbot, renamed Moltbot, becomes OpenClaw (reported) | Open-source personal agent that runs on your machine and talks through chat apps | [GitHub](https://github.com/openclaw/openclaw) |
| 2026-02-05 | Claude Opus 4.6 (1M context beta) | Start of Anthropic's rapid 2026 cadence | [Anthropic](https://www.anthropic.com/news/claude-opus-4-6) |
| 2026-02-05 | GPT-5.3-Codex in Codex (API Feb 24) | OpenAI's coding-agent model | [OpenAI changelog](https://developers.openai.com/api/docs/changelog) |
| 2026-02-05 | Anthropic: 16 parallel Claude agents build a C compiler | Concrete data on multi-agent cost (~$20K) and limits | [Anthropic](https://www.anthropic.com/engineering/building-c-compiler) |
| 2026-02-11 | Z.ai GLM-5 (open, MIT) | Leading open coding model at release | [Hugging Face](https://huggingface.co/zai-org/GLM-5) |
| 2026-02-15 | OpenClaw's creator Peter Steinberger joins OpenAI; project moves to a foundation | Big labs compete for agent-tool builders | [Steinberger](https://steipete.me/posts/2026/openclaw) |
| 2026-02-17 | Claude Sonnet 4.6 | Mid-tier refresh at $3 / $15 | [Anthropic](https://www.anthropic.com/news/claude-sonnet-4-6) |
| 2026-02-19 | Gemini 3.1 Pro (preview) | Google's last Pro release before Gemini 4 | [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/) |
| 2026-02-23 | Anthropic names DeepSeek, Moonshot and MiniMax in a distillation report | ~24,000 fraudulent accounts and 16M+ exchanges; distillation becomes a policy issue | [Anthropic](https://www.anthropic.com/research/detecting-and-preventing-distillation-attacks) |
| 2026-02-24 | METR productivity update | Later data suggests speedups, with large selection-effect caveats | [METR](https://metr.org/blog/2026-02-24-uplift-update/) |
| 2026-03-05 | GPT-5.4 and GPT-5.4 Pro | OpenAI flagship refresh | [OpenAI changelog](https://developers.openai.com/api/docs/changelog) |
| 2026-03-09 | Anthropic's managed Code Review (research preview) | Multi-agent PR review as a product | [Claude](https://claude.com/blog/code-review) |
| 2026-04-02 | Google Gemma 4 (Apache 2.0) | Gemma switches from custom terms to Apache 2.0 | [AI Studio changelog](https://aistudio.google.com/docs/changelog), [Hugging Face](https://huggingface.co/google/gemma-4-31B-it) |
| 2026-04-07 | Anthropic's Project Glasswing and Claude Mythos Preview (restricted) | A model held back for cyber defenders only; start of gated tiers | [Anthropic](https://www.anthropic.com/glasswing) |
| 2026-04-08 | Meta Muse Spark, the first Meta Superintelligence Labs model (closed) | Meta moves away from open Llama for its best models | [Simon Willison](https://simonwillison.net/2026/Apr/8/muse-spark/) |
| 2026-04-16 | Claude Opus 4.7 | Better vision and long-running work; new tokenizer; `xhigh` effort | [Anthropic](https://www.anthropic.com/news/claude-opus-4-7) |
| 2026-04-17 | Claude Design (Anthropic Labs research preview) | A closed product that combines model, harness and tools for visual work | [Anthropic](https://www.anthropic.com/news/claude-design-anthropic-labs) |
| 2026-04-23 | GPT-5.5 (API Apr 24) | OpenAI flagship refresh | [OpenAI changelog](https://developers.openai.com/api/docs/changelog) |
| 2026-04-24 | DeepSeek V4 preview: V4-Pro (1.6T) and V4-Flash, 1M context | Open models reach 1M context by default | [DeepSeek](https://api-docs.deepseek.com/news/news260424) |
| 2026-05-19 | Google I/O: Gemini 3.5 Flash; 3.5 Pro promised for June | 3.5 Pro was later cancelled | [Google](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/) |
| 2026-05-28 | Claude Opus 4.8 | Last Opus 4.x; fallback model for Fable's safety routing | [Anthropic](https://www.anthropic.com/news/claude-opus-4-8) |
| 2026-06 | MiniMax M3 (open; non-commercial by default) | Example of a license tightening between versions | [Hugging Face](https://huggingface.co/MiniMaxAI/MiniMax-M3) |
| 2026-06 | NVIDIA Nemotron 3 Ultra (550B open MoE) | Largest US open model at the time | [Hugging Face](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16) |
| 2026-06-09 | Claude Fable 5 and Mythos 5: a new tier above Opus | First generally available Mythos-class model; $10 / $50 | [Anthropic](https://www.anthropic.com/news/claude-fable-5-mythos-5) |
| 2026-06-12 | Anthropic suspends access to Fable 5 and Mythos 5 for all users after US export controls take effect | Frontier access can disappear for regulatory reasons; controls lifted Jun 30, Fable 5 back Jul 1 | [Anthropic](https://www.anthropic.com/news/redeploying-fable-5) |
| 2026-06-30 | Claude Sonnet 5 at $2 / $10 | Sonnet price cut; near-Opus coding | [Anthropic](https://www.anthropic.com/news/claude-sonnet-5) |
| 2026-07-09 | GPT-5.6 Sol, Terra and Luna | OpenAI adopts named tiers | [OpenAI changelog](https://developers.openai.com/api/docs/changelog) |
| 2026-07-09 | Meta Muse Spark 1.1 and the Meta Model API (public preview) | Meta's first paid developer API for its own models | [Meta](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/) |
| 2026-07-16 | Kimi K3 API; 1.56 TB of weights followed Jul 27 | 2.8T-parameter open model with a revenue-tiered license; frontier-scale weights no individual can run | [Hugging Face](https://huggingface.co/moonshotai/Kimi-K3), [Simon Willison](https://simonwillison.net/2026/Jul/27/kimi-k3/) |
| 2026-07-16 | Hugging Face discloses an intrusion; OpenAI confirms Jul 21 its test agent did it | An autonomous agent escaped its sandbox during a cyber benchmark | [Simon Willison](https://simonw.substack.com/p/openais-accidental-cyberattack-against) |
| 2026-07 | Thinking Machines Lab releases Inkling (open, Apache 2.0) | New US lab ships a ~1T-parameter open MoE | [Hugging Face](https://huggingface.co/thinkingmachines/Inkling) |
| 2026-07-21 | Gemini 3.6 Flash and 3.5 Flash-Lite | Google keeps shipping Flash while Pro stalls | [AI Studio changelog](https://aistudio.google.com/docs/changelog) |
| 2026-07-24 | Claude Opus 5 | Led benchmarks at launch; communication style became the top complaint | [Anthropic](https://www.anthropic.com/news/claude-opus-5) |
| 2026-08-03 | Alibaba Qwen3.8-Max (2.4T; weights about a week later) | First Max-tier Qwen with downloadable weights | [The Batch](https://www.deeplearning.ai/the-batch/qwen3-8-max-lands-with-a-bang), [Hugging Face](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) |
| 2026-08-05 | Demis Hassabis steps back as Google DeepMind CEO | Leadership shake-up amid Gemini delays | [Fortune](https://fortune.com/2026/08/05/demis-hassabis-steps-down-google-deepmind-ai-shakeup/) |
| 2026-08-10 | Meta Muse Glimmer 30B (open, Apache 2.0) | Meta's first open Muse model, built to run locally | [Hugging Face](https://huggingface.co/meta-models/Muse-Glimmer-30B) |
| 2026-08-18 | Z.ai GLM-5.3 (weights Aug 25) | Top open-weight model on Epoch's cyber index | [Hugging Face](https://huggingface.co/zai-org/GLM-5.3) |
| 2026-09-01 | Claude Fable 5.1 and Mythos 5.1 | Top tier refresh; cache reads cut 75%; new anti-distillation rules | [Anthropic](https://www.anthropic.com/claude-fable-and-mythos-5-1), [SD Times](https://sdtimes.com/tag/mythos-5-1/) |
| 2026-09-02 | Gemini 3.8 Flash and restricted 3.8 Flash Cyber | Google's Flash cadence hits roughly every six weeks | [AI Studio models](https://aistudio.google.com/docs/models) |
| 2026-09-03 | GPT-6 Astra | OpenAI's new top tier at $10 / $50 | [OpenAI changelog](https://developers.openai.com/api/docs/changelog) |
| 2026-09-10 | DeepSeek V4.1-Flash | New architecture; replaces V4-Flash | [DeepSeek](https://api-docs.deepseek.com/news/news260910) |
| 2026-09 | xAI Grok 4.7 | xAI flagship at $2 / $6 | [xAI](https://docs.x.ai/docs/release-notes) |
| 2026-09-22 | Claude Opus 5.5 ($4 / $20) and, an hour later, GPT-6 Sol and Luna | A same-day "price war"; Opus 5.5 addressed Opus 5's communication complaints | [Anthropic](https://www.anthropic.com/news/claude-opus-5-5), [TechCrunch](https://techcrunch.com/2026/09/22/openai-launches-gpt-6-sol-and-luna/) |
| 2026-09-28 | Claude Sonnet 5.5 | Matches Opus 5.5 on several benchmarks at half the price | [Anthropic](https://www.anthropic.com/news/claude-sonnet-5-5) |
| 2026-09-29 | GPT-6.1 Sol | Workhorse update a week after GPT-6 Sol | [OpenAI changelog](https://developers.openai.com/api/docs/changelog) |
| 2026-09-30 | Google announces Gemini 4 Argon for cyber defenders first; drops Gemini 3.5 Pro | The delayed Gemini 4 flagship arrives through a staged rollout | [Reuters via Khaleej Times](https://www.khaleejtimes.com/business/google-announces-gemini-4-flagship-ai-model-after-months-of-delays-2) |
| 2026-10-06 | Mistral Large 4 preview (~1T open MoE; weights Oct 29) | Strongest Western open model at launch, "about 6 months behind the frontier" | [Mistral](https://mistral.ai/news/mistral-large-4), [Simon Willison](https://simonwillison.net/2026/Oct/6/le-chonk/) |
| 2026-10-07 | Claude Haiku 5.5 at $0.10 / $0.50 | Small-model prices fall about 90% | [Anthropic](https://www.anthropic.com/news/claude-haiku-5-5) |
| 2026-10-07 | GPT-6 reaches ChatGPT with "Intelligent UI" | Answers can include interactive charts, forms and small tools | [9to5Mac](https://9to5mac.com/2026/10/07/openai-brings-gpt-6-to-chatgpt-and-debuts-intelligent-ui/) |
| 2026-10-12 | Meta Muse Wonder listed (closed, $4 / $20) | Meta's frontier reasoning model reaches developers | [OpenRouter](https://openrouter.ai/meta/muse-wonder) |
| 2026-10-13 | Gemini 4 Argon generally available | Google's flagship back near the frontier, by its own benchmarks | [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/) |
| 2026-10-15 | Meta Muse Spark Open (816B open MoE, Muse Model License) | Meta's largest open release since Llama 4 | [Hugging Face](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B) |
| 2026-10-15 | Anthropic's managed Code Review generally available | AI review moves from preview to product | [Claude](https://claude.com/resources/articles/code-review-is-now-generally-available) |
| 2026-10-16 | Epoch: open models trail closed by 6–7 months on cyber | Updated estimate of the open-closed gap | [Epoch AI](https://epoch.ai/data-insights/open-closed-cyber-eci-gap) |
| 2026-10 | Reflection AI Beam 1.0 (501B open MoE, Apache 2.0) | Another US open-weight frontier attempt | [Hugging Face](https://huggingface.co/reflection/Beam-1.0-501B-A23B) |
| 2026-10-22 | Anthropic donates Agent Skills to the Agentic AI Foundation | Skills join MCP and AGENTS.md under neutral governance | [Anthropic](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation) |
| 2026-10-23 | Kimi K3.1 Pro API; weights posted to Hugging Face in early November | The open-weight frontier as of this writing, priced at half of Opus 5.5 | [Hugging Face](https://huggingface.co/moonshotai/Kimi-K3.1-Pro), [Let's Data Science](https://letsdatascience.com/news/moonshot-releases-kimi-k31-pro-api-open-weights-due-nov-4-786e160c) |
| 2026-10-26 | GPT-6.1 Terra ($1 / $5) | Cheaper mid-tier aimed at computer use | [OpenAI changelog](https://developers.openai.com/api/docs/changelog) |
| 2026-10-26 | Anthropic files an S-1 for a proposed IPO | A frontier lab heads to public markets | [Anthropic](https://www.anthropic.com/news/s1-sec) |
| 2026-10-28 | Google announces Gemini 4 Carbon, first to vetted cyber defenders | Google adopts the restricted-frontier pattern Anthropic used for Mythos | [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/) |

## Patterns worth noticing

- **The release interval shrank.** Big launches came about yearly in 2020–2023 and quarterly in 2024–2025. By 2026 each top lab shipped something roughly every month.
- **Open weights trail by months, not years.** Epoch's estimate fell from about a year (2024) to 6–7 months on cyber tasks (2026).
- **Leadership in open weights moved to China** after DeepSeek-R1 in January 2025. US and European labs answered in 2025–2026 with gpt-oss, Gemma 4, Nemotron, Inkling, Muse and Mistral Large 4.
- **Agent tooling standardized.** MCP (2024), AGENTS.md (2025) and Agent Skills (2025) all ended up at the Agentic AI Foundation.
- **Incidents are part of the history.** Sycophancy rollbacks, infrastructure bugs, suspended launches and an agent that escaped its sandbox all happened at the frontier labs themselves. See [module 11](../modules/11-security-and-prompt-injection.md) and [module 14](../modules/14-keeping-up.md).

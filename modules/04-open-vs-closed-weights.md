# 04: Open weight vs closed weight

*About a 30-minute read. Last checked November 8, 2026.*

**TL;DR**
- **Weights** are the model: billions of numbers learned in training. Closed-weight labs keep them on their servers. Open-weight labs let you download them.
- "Open weight" isn't "open source." The OSI's Open Source AI Definition (October 2024) also requires the training code and detailed information about the training data. Only a few "fully open" models, such as AI2's OLMo, meet that bar.
- Licenses vary a lot. Apache 2.0 and MIT are simple. Many 2026 frontier open models (Kimi K3, Qwen3.8-Max, GLM-5.3, Mistral Large 4, Muse Spark Open, MiniMax M3) use custom licenses with revenue thresholds, attribution rules, or default non-commercial terms. Read the license before shipping.
- Memory needed ≈ **parameters × bytes per parameter**, plus room for context. At 4-bit, a 30B model needs about 17 GB. That's comfortable on a 36 GB Mac or a 24 GB GPU and too big for an 18 GB Mac. Frontier open models (roughly 750B to 2.8T parameters) need a server rack, not a laptop.
- Open models give you control, privacy and customization. Cost and capability depend on the model and the task, and the measured open–closed gap varies by domain ([module 03](03-model-landscape.md)).
- Self-hosting a Chinese lab's weights keeps your data on your own machines. Calling a hosted API sends it to the provider, so check that service's actual hosting region and terms. They're different risk decisions.

## Foundations

### What "weights" actually are

A language model is a very large function. You give it tokens and it gives back a probability for each possible next token. The behavior of that function is set by its **parameters**, usually called **weights**. These are the numbers training adjusted, billions or trillions of them ([module 01](01-what-is-an-llm.md)).

On disk, weights are just big files of numbers:

- **Safetensors** (`.safetensors`) is the standard format on Hugging Face. It stores tensors (arrays of numbers) rather than executable model code. That avoids pickle-style code execution, but it doesn't make accompanying code or the loading software automatically safe ([Hugging Face](https://huggingface.co/docs/safetensors/index)).
- **GGUF** (`.gguf`) is the single-file format used by llama.cpp, Ollama and LM Studio, usually already quantized.
- Pickle-based files (`.bin`, `.pt`) are older PyTorch formats that can run arbitrary code when loaded. Treat them like executables from strangers ([Hugging Face](https://huggingface.co/docs/hub/security-pickle)).

Having the weights means you can run the model on hardware you control, change it by fine-tuning, and inspect its internals. It doesn't mean you know what data it was trained on or how to rebuild it.

### The openness spectrum

| Category | What you get | Examples (Nov 2026) |
| --- | --- | --- |
| **Closed / API-only** | Access through the lab's API or apps. No weights. | Claude, GPT-6, Gemini, Grok, Muse Wonder |
| **Open weight, restrictive license** | Weights, with limits on commercial use, scale, or attribution | Kimi K3, Qwen3.8-Max, GLM-5.3, MiniMax M3, Muse Spark Open, Mistral Large 4, Llama 4 |
| **Open weight, permissive license** | Weights under Apache 2.0 or MIT | DeepSeek V4 (MIT), gpt-oss (Apache), Gemma 4 (Apache), Qwen3.8-27B (Apache), Muse Glimmer (Apache) |
| **Open source AI (OSI definition)** | Weights *plus* complete training code *plus* detailed data information, under terms that grant the four freedoms | Few models qualify |
| **Fully open** | All of the above plus the training data itself, checkpoints and logs | AI2's OLMo 3 |

The OSI Open Source AI Definition 1.0 (released October 28, 2024) says an open source AI system must let anyone use, study, modify and share it for any purpose. To make that possible, it has to come with three things ([OSI](https://opensource.org/ai/open-source-ai-definition); [announcement](https://opensource.org/blog/the-open-source-initiative-announces-the-release-of-the-industrys-first-open-source-ai-definition)):

1. Data information: enough detail about the training data that a skilled person could build a substantially equivalent system.
2. Code: the complete source code used to train and run the system.
3. Parameters: the weights.

Most "open" models publish only the third item, and labs are getting careful with the wording. Moonshot calls Kimi K3 "open weight," not "open source" ([Simon Willison](https://simonwillison.net/2026/Jul/27/kimi-k3/)). The OSI argued in 2023 that Llama's license isn't open source because of its use restrictions ([OSI](https://opensource.org/blog/metas-llama-2-license-is-not-open-source)).

**Fully open** models, like AI2's OLMo family, publish the pretraining data (Dolma), training and evaluation code, intermediate checkpoints and post-training data ([AI2](https://allenai.org/olmo)). These releases let you study the training process as well as the resulting weights. They usually trail the best open-weight models in raw capability.

### Licenses in practice

| License family | Typical terms | Examples |
| --- | --- | --- |
| **Apache 2.0** | Use, modify and sell freely. Keep notices. Includes an explicit patent grant. | gpt-oss, Gemma 4, Qwen3.8-27B, Muse Glimmer 30B, Thinking Machines Inkling, Reflection Beam 1.0 |
| **MIT** | Use, modify and sell freely. Keep the notice. | DeepSeek V4 and V4.1, GLM-5.3-Flash, Xiaomi MiMo V2.6 |
| **"Modified MIT" / MIT-style with conditions** | MIT grant plus extra clauses, often a display rule for very large products | Kimi K2 and K2.5 (display "Kimi K2" above 100M monthly users or $20M monthly revenue), MiniMax M2 and M2.5 |
| **Revenue-tiered custom licenses (the 2026 trend)** | Free for most uses. A separate agreement is needed if you run a model-hosting business ("Model as a Service") above a revenue line. | Kimi K3 (MaaS >$20M over 12 months; product display rule above 100M MAU or $20M monthly revenue, with internal-use and official-provider exceptions), Qwen3.8-Max (>$50M for MaaS; product display rule above 100M MAU or $20M monthly revenue), GLM-5.3 (a company running a model-hosting business with over $10B in total annual revenue needs Z.ai's security review), Muse Spark Open (>$20M MaaS; "Built with Muse Spark Open"), Mistral Large 4 (MaaS needs a commercial license) |
| **Default non-commercial** | Free for non-commercial use. Commercial use needs notice or authorization. | MiniMax Community License for M3 (commercial use needs a notice; prior authorization above $20M yearly revenue; "Built with MiniMax M3") |
| **Llama Community License** | Free unless you exceed 700M monthly active users. Display "Built with Llama." Derivative model names must start with "Llama." Acceptable-use policy. Llama 4's policy withholds rights to its *multimodal* models from EU-domiciled individuals and companies. | Llama 3.x, Llama 4 |
| **Gemma Terms of Use** | Custom terms with a prohibited-use policy | Gemma 1–3. Gemma 4 moved to Apache 2.0. |

Sources: [Kimi K3 license](https://huggingface.co/moonshotai/Kimi-K3/blob/main/LICENSE), [Qwen3.8-Max license](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/blob/main/LICENSE), [GLM-5.3 license](https://huggingface.co/zai-org/GLM-5.3/blob/main/LICENSE), [MiniMax M3 license](https://huggingface.co/MiniMaxAI/MiniMax-M3/blob/main/LICENSE), [Muse Spark Open card](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B), [Mistral Large 4 card](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B), [Llama 4 license](https://www.llama.com/llama4/license/), [Llama 4 use policy](https://dev.meta.ai/llama/llama4/use-policy/), [Gemma 4 model card](https://huggingface.co/google/gemma-4-31B-it).

> [!WARNING]
> Licenses change between versions of the *same* family. MiniMax M2 and M2.5 used a modified MIT license, while M3 defaults to non-commercial. GLM-5 was MIT, and GLM-5.3 uses a custom license. Kimi K2 was "modified MIT," and K3 uses a revenue-tiered license. Re-read the license every time you upgrade.

#### What to check before using an open model at work

1. Is commercial use allowed? Some licenses default to non-commercial or need notice.
2. Are there thresholds on monthly active users, revenue, or hosting ("Model as a Service")? Does your company or a customer cross them?
3. Do you have to display "Built with X," or name derivatives a certain way?
4. Is an acceptable-use policy incorporated by reference, and can it change later?
5. Are rights withheld in your region (for example, Llama 4 multimodal in the EU)?
6. Can you use outputs to train other models, and do fine-tunes inherit the license?
7. What about patents and warranty? Apache 2.0 includes a patent grant, MIT doesn't mention patents, and nearly all disclaim warranties.
8. Is it on your legal team's approved-model list? Many companies keep one. Get the model on it before you build.

This is engineering guidance, not legal advice.

## In practice

### Why labs release weights

Giving away a model that cost tens of millions of dollars sounds odd. The reasons are strategic:

- If developers build on your architecture and formats, you become the default. Qwen derivatives were over 40% of new language models on Hugging Face by mid-2025 ([Interconnects](https://www.interconnects.ai/p/atom-project)).
- Open models commoditize the complement. In 2024, Mark Zuckerberg argued that open models protect Meta from depending on a rival's closed platform ([Meta](https://about.fb.com/news/2024/07/open-source-ai-is-the-path-forward/)). In 2026 Meta kept its best Muse models closed and released two open ones. Its release strategy changed with its business priorities.
- Many open labs earn money from their own hosted API. Revenue-tiered licenses let anyone self-host while stopping large hosting companies from undercutting the lab's own service.
- Researchers want to publish, so releasing weights helps recruiting.
- Geopolitics plays a part. Chinese labs gain global adoption despite US chip export controls. The US government's 2025 AI Action Plan encouraged American open models ([White House](https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf)). Mistral pitches Large 4 as European "AI sovereignty," trained and run under European law ([Mistral](https://mistral.ai/news/mistral-large-4)).
- A good-enough open model sets a price floor that closed labs have to answer ([module 03](03-model-landscape.md)).

### The safety debate

The case for open weights:

- Security researchers and defenders can use them without permission. In July 2026 Hugging Face responded to an intrusion by an autonomous OpenAI test agent that had escaped its sandbox. Its team found commercial model APIs blocked their incident-analysis requests, so they used a self-hosted open-weight model instead ([Simon Willison](https://simonw.substack.com/p/openais-accidental-cyberattack-against)).
- Self-hosting lets you keep data on your machines, provided your application and tools also stay local.
- You can study the internals, which interpretability and safety research need.
- No single point of control over a widely used technology.
- In 2024, the US NTIA recommended monitoring open-weight risks rather than restricting them ([NTIA](https://ntia.gov/issues/artificial-intelligence/open-model-weights-report)).

The case against:

- Release can't be undone, and safeguards can be removed. Research showed LoRA fine-tuning cheaply strips safety training ([Lermen et al., 2023](https://arxiv.org/abs/2310.20624); [Gade et al., 2023](https://arxiv.org/abs/2311.00117)). Refusal behavior is often controlled by a single direction in the model's activations, which can be edited out ("abliteration") ([Arditi et al., 2024](https://arxiv.org/abs/2406.11717)). An "abliterated" copy of Muse Spark Open was on Hugging Face two days after its release ([Hugging Face](https://huggingface.co/BoldingBuilds/Muse-Spark-Open-816B-A42B-Abliterated-UD-IQ1_S-GGUF)).
- Dangerous capability spreads with a lag. Epoch estimates open models trail the closed frontier by 6–7 months on cyber tasks ([Epoch AI](https://epoch.ai/data-insights/open-closed-cyber-eci-gap)). That historical lag doesn't guarantee when any particular gated capability will become downloadable.
- Agent security varies. In 2025, NIST's CAISI found agents built on DeepSeek R1-0528 were on average 12 times more likely than US frontier models to follow hijacking instructions ([NIST](https://www.nist.gov/news-events/news/2025/09/caisi-evaluation-deepseek-ai-models-finds-shortcomings-and-risks)). Self-hosting alone doesn't remove that vulnerability. The harness and defenses also affect attack success ([module 11](11-security-and-prompt-injection.md)).

People disagree about where to draw the line. Most current policy treats today's open models as acceptable while monitoring the frontier.

### Running open models: the hardware math

#### Step 1: weight memory

**Memory for weights ≈ number of parameters × bytes per parameter.**

| Precision | Bytes per parameter | 8B model | 30B model | 120B model |
| --- | --- | --- | --- | --- |
| FP32 | 4 | 32 GB | 120 GB | 480 GB |
| BF16 / FP16 (as released) | 2 | 16 GB | 60 GB | 240 GB |
| 8-bit (FP8, INT8, Q8) | ~1 | ~8.5 GB | ~32 GB | ~125 GB |
| 4-bit (Q4_K_M, MXFP4, NVFP4, MLX 4-bit) | ~0.55–0.6 | ~4.7 GB | ~17 GB | ~65 GB |
| ~3-bit | ~0.4 | ~3.5 GB | ~13 GB | ~50 GB |

**Quantization** stores each weight with fewer bits. 8-bit is usually close to lossless. 4-bit is the common local default with modest quality loss. Coding and long reasoning tend to suffer before casual chat does. Below about 3 bits, quality drops noticeably. Some models are trained with quantization in mind (**quantization-aware training**), so their 4-bit release loses little. Both gpt-oss and Kimi K3 ship natively in 4-bit MXFP4 ([gpt-oss card](https://huggingface.co/openai/gpt-oss-120b); [Kimi K3 card](https://huggingface.co/moonshotai/Kimi-K3)). The research is in [GPTQ](https://arxiv.org/abs/2210.17323), [LLM.int8()](https://arxiv.org/abs/2208.07339) and [QLoRA](https://arxiv.org/abs/2305.14314).

#### Step 2: add room for context (the KV cache)

While generating, the model stores keys and values for every token in the context. This **KV cache** grows with context length:

**KV bytes per token ≈ 2 × layers × KV heads × head dimension × bytes per value**

For an illustrative model with 48 layers, 8 KV heads, head dimension 128 and 16-bit values, that's 2 × 48 × 8 × 128 × 2 ≈ 0.2 MB per token. A 32K-token context then needs about 6 GB on top of the weights. Many 2026 models use attention variants that shrink this a lot: latent attention in DeepSeek, Kimi Delta Attention in K3, hybrid Mamba layers in Nemotron. Check the model card. Budget separately for the target context length, simultaneous requests and runtime buffers. Adding 20–50% is only a starting estimate, not a safe bound.

#### Step 3: mixture of experts (MoE) changes speed, not memory

An **MoE** model has many "expert" sub-networks and uses only a few for each token ([Shazeer et al., 2017](https://arxiv.org/abs/1701.06538); [Fedus et al., 2021](https://arxiv.org/abs/2101.03961)). Two numbers matter:

- **Total parameters** set weight storage. Fast inference usually keeps all experts in memory. Offloading some to RAM or disk trades speed for capacity.
- **Active parameters** help estimate compute per token. Routing, memory access, attention and communication also affect speed.

Gemma 4 26B-A4B has 26B total and about 4B active. Its weights need roughly the storage of a 26B model. Activating about 4B parameters reduces computation, but it doesn't guarantee the speed of a dense 4B model. Kimi K3 has 2.8T total and 104B active. Its 4-bit weights are about 1.56 TB, which is data-center hardware even though only 104B parameters are active per token.

#### Step 4: speed is mostly memory bandwidth

Generating each token means reading all active weights from memory once. A rough upper bound:

**tokens per second ≲ memory bandwidth ÷ bytes of active weights**

A dense 30B model at 4-bit (~17 GB) on a machine with ~270 GB/s of bandwidth tops out near 16 tokens per second. Actual output is slower. A 3B-active MoE at 4-bit (~1.7 GB per token) on the same machine can be several times faster. That's why MoE models are popular locally.

#### VRAM vs Apple unified memory

- A **discrete GPU** (for example a 24 GB RTX 4090) has its own fast **VRAM**. The model has to fit in VRAM to run fast. Spilling to system RAM makes it far slower.
- Apple silicon Macs share one pool of **unified memory** between CPU and GPU. That lets a 64–128 GB Mac load models no consumer GPU can. By default macOS limits how much of that memory the GPU can wire, roughly two-thirds to three-quarters of RAM. Bandwidth is also lower than a high-end GPU's.

On macOS you can raise the GPU memory limit with `sudo sysctl iogpu.wired_limit_mb=<megabytes>`. Leave several GB for the OS and your apps. Values reset on reboot. Check current guidance for your macOS version before changing it.

#### What fits where (approximate, 4-bit unless noted)

| Machine | Roughly usable for the model | Comfortable | Stretch |
| --- | --- | --- | --- |
| **18 GB Mac** | ~12 GB | 4B–14B dense (Gemma 4 E4B or 12B, small Qwen models) | gpt-oss-20b (~13 GB as shipped) with short context and a raised limit |
| **24 GB GPU** | ~22 GB VRAM | 27B–32B dense with moderate context: Qwen3.8-27B, Gemma 4 31B, Muse Glimmer 30B (its card says 4-bit fits 24–32 GB GPUs); gpt-oss-20b | Gemma 4 26B-A4B with long context |
| **36 GB Mac** | ~24–27 GB | The same 27B–32B dense models; Gemma 4 26B-A4B (fast); gpt-oss-20b with long context | ~35B MoE models |
| **64 GB Mac** | ~45–48 GB | 70B-class dense at 4-bit (slow) | ~100B MoE at 3-bit |
| **128 GB Mac or similar workstation** | ~96 GB+ | gpt-oss-120b (fits one 80 GB GPU as shipped); 120B-A12B MoE such as Nemotron 3 Super | Mistral Medium 3.5 (128B dense, slow) |
| **8× 80 GB data-center GPUs** | ~640 GB | 300B–800B MoE at 4-bit or FP8: GLM-5.3 at 4-bit (~420 GB), MiniMax M3 at FP8 | ~1T models at 4-bit, such as Mistral Large 4 (~550 GB) |
| **Multi-node clusters** | 1 TB+ | Kimi K3 / K3.1 Pro, DeepSeek V4-Pro, Qwen3.8-2.4T | — |

Model cards can ask for more than the weight math suggests. By the math above, Muse Spark Open's 4-bit (NVFP4) weights come to roughly 450–500 GB, but Meta's card asks for at least 700 GB of GPU memory at NVFP4, or two M5 Ultra Mac Studios running MLX ([model card](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B)).

The headline frontier open models (Kimi K3.1 Pro, DeepSeek V4-Pro, Qwen3.8-Max, GLM-5.3) can't run on a laptop at useful quality. Most people use them through hosted providers. "Local" usually means a model one or two tiers smaller.

### Tools for running open models

| Tool | What it is | Best for |
| --- | --- | --- |
| **[llama.cpp](https://github.com/ggml-org/llama.cpp)** | C/C++ inference engine, GGUF format, CPU and GPU (including Apple Metal) | The engine under many local tools; `llama-server` gives an OpenAI-compatible endpoint |
| **[Ollama](https://ollama.com/)** | Simple CLI and background server built on llama.cpp-style runtimes | Easiest start: `ollama run gpt-oss:20b`; local API on port 11434 |
| **[LM Studio](https://lmstudio.ai/)** | Desktop app with model search; runs GGUF and Apple MLX models | People who prefer a GUI; Mac users; local server on port 1234 |
| **[MLX / mlx-lm](https://github.com/ml-explore/mlx-lm)** | Apple's array framework and LLM tools for Apple silicon | Fast Mac inference and LoRA fine-tuning on a Mac |
| **[vLLM](https://github.com/vllm-project/vllm)** | High-throughput GPU server with PagedAttention ([Kwon et al., 2023](https://arxiv.org/abs/2309.06180)) | Serving a team or product; OpenAI-compatible |
| **[SGLang](https://github.com/sgl-project/sglang)** | High-throughput GPU server with prefix caching and structured output ([Zheng et al., 2023](https://arxiv.org/abs/2312.07104)) | Agent-heavy serving; recommended by several 2026 model cards |

A minimal local session:

```bash
# Easiest: Ollama (downloads about 14 GB the first time)
ollama run gpt-oss:20b

# llama.cpp server with an OpenAI-compatible API on port 8080
llama-server -hf ggml-org/gpt-oss-20b-GGUF

# A GPU server for a team (needs an 80 GB-class GPU for this model)
vllm serve openai/gpt-oss-120b
```

> [!CAUTION]
> Check free disk space before you pull a model. Weights are large, and each tool keeps its own copy. `ollama rm <model>` and LM Studio's model manager delete them when you're done.

### Hosted open models

You don't have to own hardware to use open weights. Providers host them and charge per token:

- [OpenRouter](https://openrouter.ai/) is a router and marketplace. One API key reaches hundreds of models from many providers, with per-provider prices and routing.
- [Together AI](https://together.ai/), [Fireworks](https://fireworks.ai/), Baseten and DeepInfra are GPU clouds specializing in open models.
- [Groq](https://groq.com/) and [Cerebras](https://www.cerebras.ai/) use custom chips with very fast output.
- The labs' own APIs: DeepSeek, Moonshot (Kimi), Z.ai, MiniMax, Alibaba Cloud (Qwen), Mistral.
- Hyperscalers (AWS Bedrock, Google Vertex AI and Microsoft Foundry) host many open models next to closed ones.

The "same" open model can behave differently across hosts because of quantization, chat templates, context limits and tool-call parsing. If a model seems worse than its benchmarks, try the lab's own API or another host before you give up on it. Pin a provider for anything you evaluate.

### Using open models in coding harnesses

Most coding harnesses can now talk to more than one provider ([module 06](06-harnesses-and-tools.md)).

OpenCode is an MIT-licensed, open-source coding agent with terminal, desktop and SDK interfaces. It reaches more than 200 providers through the Models.dev catalog ([OpenCode](https://opencode.ai/)). You connect a provider with `/connect` and choose a model with `/models`. It auto-detects local Ollama (`127.0.0.1:11434`), LM Studio (`:1234`) and vLLM (`:8000`) servers ([OpenCode docs](https://opencode.ai/docs/providers/)). OpenCode also sells a curated-model subscription, OpenCode Go, from $10 per month.

You can also point Claude Code at an Anthropic-compatible endpoint. Several open-model labs offer endpoints that speak Anthropic's Messages API. Z.ai documents this for its GLM Coding Plan ([Z.ai docs](https://docs.z.ai/devpack/tool/claude)):

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.z.ai/api/anthropic",
    "ANTHROPIC_AUTH_TOKEN": "<your Z.ai key>",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "glm-5.3[1m]",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "glm-5.3[1m]",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "glm-5.3-flash[1m]"
  }
}
```

Moonshot describes its Messages API as compatible with "the Anthropic SDK, Claude Code, and similar tools" ([Kimi docs](https://platform.kimi.ai/docs/guide/agent-support)). DeepSeek's V4 API accepts both OpenAI and Anthropic formats ([DeepSeek](https://api-docs.deepseek.com/news/news260424)). MiniMax sells an "M Plan" subscription for its models in coding and assistant tools ([MiniMax docs](https://platform.minimax.io/docs/guides/text-ai-coding-tools)). These flat-rate **coding plans** compete with Claude and ChatGPT subscriptions on price ([module 12](12-costs-subscriptions-and-apis.md)).

> [!IMPORTANT]
> Anthropic's docs say it "doesn't support routing Claude Code to non-Claude models through any gateway" ([Claude Code docs](https://code.claude.com/docs/en/llm-gateway)). It often works, but features built around Claude's API can break or behave differently: thinking blocks, tool formats, caching, effort settings. Kimi's docs, for example, say you must pass back the full assistant message, including `reasoning_content`, for multi-turn tool use ([Kimi docs](https://platform.kimi.ai/docs/guide/agent-support)). Test before you depend on it.

Codex CLI can run local models with `--oss`, using Ollama or LM Studio, set by `oss_provider` in `~/.codex/config.toml`. It can also use any compatible endpoint defined under `[model_providers.<id>]` ([Codex docs](https://learn.chatgpt.com/docs/config-file/config-advanced)):

```toml
# ~/.codex/config.toml, option 1: the built-in local path
oss_provider = "ollama"            # used when you run: codex --oss
```

```toml
# ~/.codex/config.toml, option 2: any OpenAI-compatible endpoint
model_provider = "local_ollama"    # select the provider defined below
model = "<a model you've pulled>"  # placeholder: use the name your server lists

[model_providers.local_ollama]
name = "Ollama"
base_url = "http://localhost:11434/v1"
```

Config keys change between releases, so check the current docs before relying on either.

Expect a local 20B–30B model to handle small, well-specified edits and explanations. It struggles with long multi-file agentic tasks that frontier models finish. Hosted frontier open models (Kimi K3.1 Pro, GLM-5.3) come much closer. Some model cards report coding scores measured inside the Claude Code harness ([GLM-5.3 card](https://huggingface.co/zai-org/GLM-5.3); [Kimi K3.1 Pro card](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)).

### Privacy, data residency and compliance

Check both where the weights came from and where the computation runs.

| Setup | Where your prompts and code go | Main considerations |
| --- | --- | --- |
| **Self-hosted open weights** (laptop, your cloud account) | Nowhere outside your infrastructure | You own security, updates and monitoring. Use safetensors. Avoid `trust_remote_code` unless you've reviewed the code. |
| **US or EU host serving Chinese-origin weights** (for example Together, Fireworks, Bedrock) | That host, under its terms and jurisdiction | Data handling depends on the host. Behavior also depends on the host's quantization, system prompt, tools and serving configuration. |
| **A Chinese lab's own API** (DeepSeek, Moonshot, Z.ai, MiniMax, Alibaba) | That company's servers. DeepSeek's privacy policy says it stores personal data "in People's Republic of China." | Chinese law applies. Check your company's policy before sending source code there. |
| **Closed US lab API** (Anthropic, OpenAI, Google) | That lab's servers, under retention terms you can often configure | Retention and training-use terms, zero-data-retention options, region controls. Anthropic offers US-only inference (`inference_geo: "us"`) at 1.1× price on Claude 4.6 and later. Fable-class models require 30-day retention. |

Sources: [DeepSeek privacy policy](https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html), [Anthropic data residency](https://platform.claude.com/docs/en/manage-claude/data-residency), [Anthropic on Fable retention](https://www.anthropic.com/news/claude-fable-5-mythos-5).

Other points to check:

- Model behavior travels with the weights. CAISI found DeepSeek models repeated inaccurate Chinese Communist Party narratives four times as often as US reference models ([NIST](https://www.nist.gov/news-events/news/2025/09/caisi-evaluation-deepseek-ai-models-finds-shortcomings-and-risks)). Self-hosting fixes data flow, not model bias or prompt-injection susceptibility.
- Market access cuts both ways. Anthropic doesn't sell commercial Claude access in China or to Chinese-owned subsidiaries abroad ([Anthropic](https://www.anthropic.com/research/detecting-and-preventing-distillation-attacks)). Some licenses withhold rights in some regions (Llama 4 multimodal in the EU).
- Download weights only from the publisher's official repository, and check hashes. Watch for "uncensored" or "abliterated" re-uploads that remove safety behavior.
- Self-hosting gives you a frozen model that never changes under you, while closed APIs can be updated or retired ([module 14](14-keeping-up.md)). That matters for regulated workflows.

### Tuning open models (briefly)

Common ways to change open weights include:

- **LoRA** trains small add-on matrices instead of the whole model ([Hu et al., 2021](https://arxiv.org/abs/2106.09685)).
- **QLoRA** does the same on top of a 4-bit base, so a single GPU can fine-tune a large model ([Dettmers et al., 2023](https://arxiv.org/abs/2305.14314)).
- **Distillation** trains a small model on a big model's outputs ([Hinton et al., 2015](https://arxiv.org/abs/1503.02531)).

Common tools include [Unsloth](https://github.com/unslothai/unsloth), [Hugging Face TRL](https://github.com/huggingface/trl) and mlx-lm on Macs. Closed models can only be tuned through whatever fine-tuning service the lab offers, if any. [Module 02](02-training-and-tuning.md) covers tuning in depth, including research on models that update their own weights.

### When to choose open vs closed

| Situation | Lean toward | Why |
| --- | --- | --- |
| Hardest agentic coding, large refactors, "just make it work" | **Closed frontier** | Strong candidates for demanding tasks; compare them against current open models in your harness ([module 03](03-model-landscape.md)) |
| Code or data can't leave your network (regulated, classified, client contracts) | **Open, self-hosted** | Data never leaves your infrastructure |
| High-volume bulk jobs (tagging, extraction) at millions of calls | **Open (hosted or self-hosted)**, or a cheap closed tier | Price per token. Compare against Haiku 5.5 or GPT-6 Luna at $0.10 / $0.50. |
| You need to fine-tune on proprietary data or change behavior deeply | **Open** | You control the weights |
| Offline or edge use (planes, factories, phones) | **Open, small** | No network needed |
| A reproducible, frozen model for audits or research | **Open** | The model can't change under you |
| Security research blocked by closed-model safeguards | **Open**, or a lab's verification program | Fewer refusals; see the safety debate above |
| Small team, no ML ops, wants it to just work | **Closed** | No hardware, no serving stack, best tools |
| Teaching how models work (students) | **Open, small, ideally fully open (OLMo)** | You can inspect everything |
| Company policy bars a vendor's jurisdiction | **Open from a trusted host, or a different vendor** | Separate weight origin from data location |

## Going deeper

### MoE and the shape of 2026 open models

Almost every frontier open model of 2026 is a sparse MoE with roughly 2–6% of parameters active per token. Kimi K3 activates 104B of 2.8T. DeepSeek V4-Pro activates 49B of 1.6T. Muse Spark Open activates 42B of 816B. Reflection Beam activates 23B of 501B. This design makes training and serving cheaper per token. It also pushes the models out of reach of single machines, since memory scales with *total* parameters. The open models people actually run locally (Gemma 4, Qwen3.8-27B, gpt-oss-20b, Muse Glimmer 30B) are a separate, smaller class. Using those local models is very different from using frontier open models.

### Benchmark gaps may understate real gaps

Epoch notes "some evidence that open-weight models tend to optimize on benchmarks more aggressively," so the measured gap "could be understated" ([Epoch AI](https://epoch.ai/benchmarks/eci)). Model cards also often compare against closed models using numbers from the rivals' own reports, with different harnesses and effort levels. Treat cross-lab tables on open-model cards as marketing until reproduced ([module 05](05-judging-models.md)).

### The licensing trend: open, but not for your competitors

From 2024 to 2026 the frontier open license moved away from plain MIT or Apache toward custom licenses. These keep almost every use free but target one group: other companies that would host the model and sell it as a service. Kimi K3, Qwen3.8-Max, GLM-5.3, Mistral Large 4 and Muse Spark Open all have some version of this clause. It changes nothing for most engineers and companies, and a lot for cloud and inference providers. Open weights appear to be a business strategy.

### Self-hosting isn't automatically safer

Self-hosting removes one risk (data leaving) and adds others:

- Unpatched inference servers.
- Exposed endpoints with no authentication. Local servers often listen on all interfaces if you configure them that way.
- Model files from unofficial mirrors.
- No vendor abuse monitoring.

An open-weight model running an agent with shell access is as exposed to prompt injection as a closed one, sometimes more ([module 11](11-security-and-prompt-injection.md)).

## Bryan's take

> **Bryan's take:** For coding, Claude and Codex are the best in my opinion. Open models like Kimi sit at a different place in the chain.

When you compare a self-hosted or per-token open model against a flat-rate plan, remember Bryan's view that subscriptions, not API billing, are what make heavy agentic use affordable ([module 12](12-costs-subscriptions-and-apis.md)).

## Try it

**Individual exercise: run a model locally and measure it (45 minutes).**
1. Check free disk and memory (`df -h`, Activity Monitor or `nvidia-smi`). Pick a model from the "what fits where" table that leaves headroom.
2. Install Ollama or LM Studio and run the model. Ask it to explain a function from your codebase and write a unit test for it.
3. Record tokens per second, memory used, and whether the test passes.
4. Run the same prompt against a hosted frontier model. Write three sentences comparing quality, speed and privacy.
5. Delete the model when you're done (`ollama rm <model>`).

**Class or team exercise: a license review.**
1. Give each group two model licenses from the table in this module, one permissive and one custom.
2. Each group answers the eight-question checklist for a hypothetical product: a SaaS tool with 2 million users and $30M in yearly revenue that hosts the model for customers.
3. Groups present which models the product could use as-is, which need an agreement, and which are off the table.
4. Talk it over. Did anything surprise you? Which clauses would your legal team flag?

## Discussion questions

1. Should "open source AI" require the training data itself, or is the OSI's requirement for detailed data information enough? What can you study with weights alone?
2. If a lab's open model is safe today, what would have to be true for it to be safe to release a model six months more capable?
3. Is self-hosting a Chinese lab's weights on your own servers meaningfully different from using an American lab's API? List the risks each one addresses and leaves open.
4. Revenue-tiered licenses keep most uses free but restrict large hosts. Is that fair, and does it make these models "open"?
5. For your team's work, what share could a local 30B model handle well? What evidence would you collect?

## Sources and further reading

**Papers**
- [Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer](https://arxiv.org/abs/1701.06538) (Shazeer et al., 2017)
- [Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity](https://arxiv.org/abs/2101.03961) (Fedus, Zoph, Shazeer, 2021)
- [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531) (Hinton, Vinyals, Dean, 2015)
- [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685) (Hu et al., 2021)
- [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314) (Dettmers et al., 2023)
- [GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers](https://arxiv.org/abs/2210.17323) (Frantar et al., 2022)
- [LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale](https://arxiv.org/abs/2208.07339) (Dettmers et al., 2022)
- [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180) (Kwon et al., 2023)
- [SGLang: Efficient Execution of Structured Language Model Programs](https://arxiv.org/abs/2312.07104) (Zheng et al., 2023)
- [LoRA Fine-tuning Efficiently Undoes Safety Training in Llama 2-Chat 70B](https://arxiv.org/abs/2310.20624) (Lermen et al., 2023)
- [BadLlama: cheaply removing safety fine-tuning from Llama 2-Chat 13B](https://arxiv.org/abs/2311.00117) (Gade et al., 2023)
- [Refusal in Language Models Is Mediated by a Single Direction](https://arxiv.org/abs/2406.11717) (Arditi et al., 2024)
- [How far behind are open models?](https://epoch.ai/blog/open-models-report) (Cottier et al., Epoch AI, 2024)

**Primary sources**
- [OSI Open Source AI Definition 1.0](https://opensource.org/ai/open-source-ai-definition) and [release announcement](https://opensource.org/blog/the-open-source-initiative-announces-the-release-of-the-industrys-first-open-source-ai-definition)
- [AI2 OLMo](https://allenai.org/olmo)
- Model cards and licenses: [gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b), [Gemma 4 31B](https://huggingface.co/google/gemma-4-31B-it), [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B), [Kimi K3](https://huggingface.co/moonshotai/Kimi-K3) and [license](https://huggingface.co/moonshotai/Kimi-K3/blob/main/LICENSE), [Qwen3.8-Max license](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/blob/main/LICENSE), [GLM-5.3 license](https://huggingface.co/zai-org/GLM-5.3/blob/main/LICENSE), [MiniMax M3 license](https://huggingface.co/MiniMaxAI/MiniMax-M3/blob/main/LICENSE), [Muse Spark Open](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B), [Muse Glimmer 30B](https://huggingface.co/meta-models/Muse-Glimmer-30B), [Mistral Large 4](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B), [DeepSeek V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro), [Llama 4 license](https://www.llama.com/llama4/license/) and [use policy](https://dev.meta.ai/llama/llama4/use-policy/)
- Harness docs: [OpenCode providers](https://opencode.ai/docs/providers/), [Z.ai with Claude Code](https://docs.z.ai/devpack/tool/claude), [Kimi agent support](https://platform.kimi.ai/docs/guide/agent-support), [Claude Code LLM gateways](https://code.claude.com/docs/en/llm-gateway), [Codex advanced config](https://learn.chatgpt.com/docs/config-file/config-advanced)
- Policy and evaluations: [NIST CAISI evaluation of DeepSeek](https://www.nist.gov/news-events/news/2025/09/caisi-evaluation-deepseek-ai-models-finds-shortcomings-and-risks), [NTIA report on open model weights](https://ntia.gov/issues/artificial-intelligence/open-model-weights-report), [America's AI Action Plan](https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf), [Epoch: open-closed cyber gap](https://epoch.ai/data-insights/open-closed-cyber-eci-gap)
- Data handling: [DeepSeek privacy policy](https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html), [Anthropic data residency](https://platform.claude.com/docs/en/manage-claude/data-residency)
- Formats and safety: [Safetensors](https://huggingface.co/docs/safetensors/index), [Pickle security on the Hub](https://huggingface.co/docs/hub/security-pickle)

**Commentary**
- [Open Source AI Is the Path Forward](https://about.fb.com/news/2024/07/open-source-ai-is-the-path-forward/) (Zuckerberg, 2024)
- [The ATOM Project](https://www.interconnects.ai/p/atom-project) (Lambert, 2025)
- [Simon Willison on Kimi K3's weights and license](https://simonwillison.net/2026/Jul/27/kimi-k3/)
- [Simon Willison on the OpenAI agent incident at Hugging Face](https://simonw.substack.com/p/openais-accidental-cyberattack-against)

## Terms introduced

- **Weights (parameters):** the learned numbers that define a model's behavior.
- **Closed weight / API-only:** a model you can use only through the lab's servers.
- **Open weight:** a model whose weights you can download, under some license.
- **Open source AI (OSI definition):** an AI system released with weights, complete training code and detailed data information, under terms granting use, study, modification and sharing.
- **Fully open model:** an open-source model that also releases its training data, checkpoints and logs (for example OLMo).
- **Safetensors:** a weight file format that holds only tensors and can't run code when loaded.
- **GGUF:** the single-file, usually quantized, model format used by llama.cpp and tools built on it.
- **Quantization:** storing weights with fewer bits (8-, 4- or 3-bit) to save memory, at some cost in quality.
- **Quantization-aware training (QAT):** training a model so it loses little quality when quantized.
- **KV cache:** the per-token memory a model keeps while generating; it grows with context length.
- **Mixture of experts (MoE):** an architecture that uses only some sub-networks per token; total parameters set memory, active parameters set speed.
- **Active vs total parameters:** the parameters used per token vs the parameters stored.
- **Unified memory:** memory shared by CPU and GPU on Apple silicon, so large models can load without a discrete GPU.
- **VRAM:** a discrete GPU's own memory.
- **Model as a Service (MaaS) clause:** a license term requiring a separate agreement before you host a model for paying third parties above some size.
- **Abliteration:** editing a model's weights to remove its refusal behavior.
- **Coding plan:** a flat-rate subscription from a model provider for use in coding harnesses.
- **Anthropic-compatible endpoint:** a non-Anthropic API that accepts Anthropic's Messages format so tools like Claude Code can call it.
- **Inference geo / data residency:** controls over where a provider runs inference and stores your data.

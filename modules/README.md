# Modules

Nineteen modules, in reading order, grouped into five stages. Every module has the same layers: Foundations (no background assumed), In practice (what working engineers do), and Going deeper (research and open debates), plus exercises and discussion questions. The [learning paths](../paths/README.md) say which layers to read for your background.

| # | Module | What you'll learn |
| --- | --- | --- |
| 00 | [Orientation](00-orientation.md) | What this is, AI-accelerated coding vs vibe coding, six ideas that outlast the hype |

### Stage 1: How the machine works

| # | Module | What you'll learn |
| --- | --- | --- |
| 01 | [What is an LLM?](01-what-is-an-llm.md) | Tokens, transformers ("Attention Is All You Need"), pretraining, reasoning models, hallucination |
| 02 | [How a model is made](02-how-a-model-is-made.md) | Data, pretraining, the hardware (GPUs, memory, interconnect, power), distillation, and quantization |
| 03 | [Post-training and reinforcement learning](03-post-training-and-rl.md) | RL from first principles: RLHF, GRPO, RLVR, coding environments, reward hacking; fine-tuning with LoRA; self-tuning models |
| 04 | [Model safety and alignment](04-model-safety-and-alignment.md) | Safety vs security vs alignment, how labs align models, safety frameworks, what models have actually done in tests and why setting matters |

### Stage 2: Choosing a model

| # | Module | What you'll learn |
| --- | --- | --- |
| 05 | [The model landscape](05-model-landscape.md) | The labs, current lineups, where Meta's Muse fits, the best model for each job |
| 06 | [Open weight vs closed weight](06-open-vs-closed-weights.md) | Licenses, running models locally, where open models sit in the chain |
| 07 | [How to tell if a model is good](07-judging-models.md) | Benchmarks and their flaws, benchmark-maxing, productivity studies, building your own eval |

### Stage 3: Working with agents

| # | Module | What you'll learn |
| --- | --- | --- |
| 08 | [Harnesses, tools, and MCP](08-harnesses-and-tools.md) | Chat vs IDE vs CLI vs cloud agents, MCP, skills, hooks, products like Claude Design |
| 09 | [Context engineering and the buzzwords](09-context-engineering.md) | Prompt → context → harness → loop → graph engineering, and the rise and fall of giant `CLAUDE.md` files |
| 10 | [Agentic workflows](10-agentic-workflows.md) | The workflow that works, Yegge's eight stages, how much autonomy is real today |

### Stage 4: Trusting the output

| # | Module | What you'll learn |
| --- | --- | --- |
| 11 | [Verification](11-verification.md) | Why you can't trust output by default, the ladder of checks, problems agents can loop on, protecting the verifier, calibrating your own trust |
| 12 | [Multiple agents](12-multi-agent-systems.md) | Agents building and reviewing together, and what the research says |
| 13 | [AI code review](13-ai-code-review.md) | Review tools, cross-model review, how humans should review AI-written code |
| 14 | [Security and prompt injection](14-security-and-prompt-injection.md) | Why injection is unsolved, the lethal trifecta, real incidents, sandboxing |

### Stage 5: Practice for the long run

| # | Module | What you'll learn |
| --- | --- | --- |
| 15 | [Costs](15-costs-subscriptions-and-apis.md) | Subscriptions vs API billing, why agents eat tokens, a worked cost example |
| 16 | [Open-source ecosystem](16-open-source-ecosystem.md) | Open harnesses, inference engines, frameworks, and the AI-slop problem for maintainers |
| 17 | [Keeping up](17-keeping-up.md) | Model ups and downs, which sources to trust, a sustainable routine |
| 18 | [Learning, careers, and responsibility](18-learning-careers-and-responsibility.md) | Learning with AI without losing the skill, careers, privacy, licensing, ethics |

Each module has a matching [slide deck](../slides/README.md).

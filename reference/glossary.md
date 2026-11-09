# Glossary

*Last checked November 8, 2026. Built from the "Terms introduced" list at the end of each module.*

Every term defined anywhere in the knowledge base, in one or two sentences, with links to the modules that use it. When two modules define the same term, the first one's definition is shown. If a term is missing, add it to the "Terms introduced" list of the module that explains it. This page is regenerated from those lists.

Model names and product names change fast. Entries for specific models describe them as of the date above; [module 03](../modules/03-model-landscape.md) has the current lineup.

<!-- BEGIN GENERATED: edit the modules, then run python3 scripts/build_reference.py -->

## A

- **A2A (Agent2Agent)**: A protocol for agents to delegate to and communicate with other agents. ([06](../modules/06-harnesses-and-tools.md))
- **Abliteration**: Removing a model's refusal behavior by deleting the activation direction that mediates it. ([02](../modules/02-training-and-tuning.md), [04](../modules/04-open-vs-closed-weights.md))
- **Active vs total parameters**: The parameters used per token vs the parameters stored. ([04](../modules/04-open-vs-closed-weights.md))
- **Adapter (LoRA adapter)**: The small set of trained parameters produced by PEFT, loaded on top of a base model. ([02](../modules/02-training-and-tuning.md))
- **Adaptive attack**: An attack tuned specifically against a given defense, used to measure real rather than reported robustness. ([11](../modules/11-security-and-prompt-injection.md))
- **Adversarial verification**: Checking each finding by assigning a fresh agent to try to refute it. ([09](../modules/09-multi-agent-systems.md))
- **Agent**: A model plus tools plus a loop that keeps acting until a task is done. ([01](../modules/01-what-is-an-llm.md), [08](../modules/08-agentic-workflows.md))
- **Agent framework**: A library of building blocks (model clients, tools, state, tracing, multi-agent coordination) for building agents. ([13](../modules/13-open-source-ecosystem.md))
- **Agent loop**: The cycle of calling the model, running the tools it requests, and feeding results back until it finishes. ([06](../modules/06-harnesses-and-tools.md), [08](../modules/08-agentic-workflows.md))
- **Agent SDK**: A vendor's agent harness packaged as a library, such as the Claude Agent SDK or OpenAI Agents SDK. ([13](../modules/13-open-source-ecosystem.md))
- **Agent team**: Peer agents that share a task list and message each other, usually with a lead. ([09](../modules/09-multi-agent-systems.md))
- **Agent-computer interface (ACI)**: The set of tools and commands an agent uses to work with a computer; its design affects agent performance. ([08](../modules/08-agentic-workflows.md))
- **Agentic AI Foundation (AAIF)**: The Linux Foundation body that hosts MCP, AGENTS.md, goose and Agent Skills. ([06](../modules/06-harnesses-and-tools.md))
- **Agents Rule of Two**: Meta's guideline that an agent should combine at most two of: processing untrusted input, accessing sensitive data or systems, and changing state or communicating externally, unless a human or reliable check approves its actions. ([11](../modules/11-security-and-prompt-injection.md))
- **AGENTS.md**: A vendor-neutral instruction-file name, now stewarded by the Agentic AI Foundation. ([07](../modules/07-context-engineering.md))
- **AI code reviewer / review bot**: A language-model system that comments on pull requests to flag problems. ([10](../modules/10-ai-code-review.md))
- **AI disclosure**: A statement of which AI tools you used and how, in coursework, commits, or pull requests. ([15](../modules/15-learning-careers-and-responsibility.md))
- **AI radar**: A team document placing AI tools and practices in Adopt / Trial / Assess / Hold rings, with evidence and owners. ([14](../modules/14-keeping-up.md))
- **AI slop**: Low-effort, unverified AI-generated content, such as fake bug reports or careless pull requests. ([13](../modules/13-open-source-ecosystem.md))
- **AI-first (not AI-only)**: Reaching for AI by default while keeping the ability to work without it. ([15](../modules/15-learning-careers-and-responsibility.md))
- **AI-free, AI-as-tutor, AI-accelerated**: A three-tier way to label assignments by how much AI help is allowed. ([15](../modules/15-learning-careers-and-responsibility.md))
- **Anthropic-compatible endpoint**: A non-Anthropic API that accepts Anthropic's Messages format so tools like Claude Code can call it. ([04](../modules/04-open-vs-closed-weights.md))
- **API-equivalent cost**: What a given amount of subscription usage would have cost at published API prices. ([12](../modules/12-costs-subscriptions-and-apis.md))
- **Approval fatigue**: Approving permission prompts without reading them because there are too many. ([06](../modules/06-harnesses-and-tools.md))
- **Argon**: The name of Google's first Gemini 4 model (October 2026). ([03](../modules/03-model-landscape.md))
- **`Assisted-by:` trailer**: A commit-message line disclosing that a tool helped produce the change. ([13](../modules/13-open-source-ecosystem.md))
- **Astra / Sol / Terra / Luna**: OpenAI's tier names, from largest to smallest (Sol, Terra and Luna since GPT-5.6; Astra since GPT-6). ([03](../modules/03-model-landscape.md))
- **Attention / self-attention**: A mechanism that lets each token weigh and draw information from other tokens using queries, keys, and values. ([01](../modules/01-what-is-an-llm.md))
- **Auto mode**: A permission mode in which a classifier model approves routine actions. ([06](../modules/06-harnesses-and-tools.md), [11](../modules/11-security-and-prompt-injection.md))
- **Automation bias**: The tendency of people to over-trust an automated check and relax their own scrutiny. ([10](../modules/10-ai-code-review.md))
- **Autoregressive generation**: Producing output one token at a time, feeding each token back in as input. ([01](../modules/01-what-is-an-llm.md))

## B

- **Background agent**: An agent that runs a task without you watching and returns a result (often a pull request) later. ([08](../modules/08-agentic-workflows.md))
- **Base model**: A pretrained model before post-training; it continues documents rather than following instructions. ([01](../modules/01-what-is-an-llm.md))
- **Batch API**: Asynchronous processing of many requests, completed within hours, at about half price. ([12](../modules/12-costs-subscriptions-and-apis.md))
- **Beads**: A Dolt-backed graph issue tracker that agents use as shared, structured memory. ([13](../modules/13-open-source-ecosystem.md))
- **Benchmark**: A fixed set of tasks plus a scoring rule, used to compare models. ([05](../modules/05-judging-models.md))
- **Benchmark-maxing**: Optimizing a model or its presentation for benchmark scores at the expense of real-use behavior. ([05](../modules/05-judging-models.md))
- **Best-of-N**: Running the same task N times and keeping the best or majority result. ([09](../modules/09-multi-agent-systems.md))
- **Blind A/B evaluation**: Comparing outputs with model identities hidden from the grader. ([05](../modules/05-judging-models.md))
- **Brevity bias / context collapse**: Loss of useful detail when contexts are repeatedly summarized or rewritten. ([07](../modules/07-context-engineering.md))
- **Brooks's law**: Fred Brooks's observation that adding people to a late software project makes it later, because coordination costs grow with team size. Coordination overhead can affect agent teams too. ([15](../modules/15-learning-careers-and-responsibility.md))
- **Byte-pair encoding (BPE)**: A tokenization method that builds a vocabulary by repeatedly merging the most frequent adjacent symbol pairs. ([01](../modules/01-what-is-an-llm.md))

## C

- **Cache TTL**: How long a cached prefix stays available (for example 5 minutes or 1 hour) before it must be written again. ([12](../modules/12-costs-subscriptions-and-apis.md))
- **Cache write / cache read**: The cost to store a prefix in the cache, and the (much lower) cost to reuse it. ([12](../modules/12-costs-subscriptions-and-apis.md))
- **CaMeL**: A Google DeepMind system that turns a user request into a program and tracks data provenance to enforce security policies around an LLM. ([11](../modules/11-security-and-prompt-injection.md))
- **Capability saturation**: The point where a single agent is good enough that adding agents stops helping. ([09](../modules/09-multi-agent-systems.md))
- **Catastrophic forgetting**: Losing previously learned abilities when training on new data. ([02](../modules/02-training-and-tuning.md))
- **Causal mask**: The rule that a token may only attend to earlier tokens, which makes a model a next-token predictor. ([01](../modules/01-what-is-an-llm.md))
- **Chain-of-thought**: Prompting a model to produce intermediate reasoning steps. ([07](../modules/07-context-engineering.md))
- **Chain-of-thought (CoT)**: Having a model write intermediate reasoning steps before its answer. ([01](../modules/01-what-is-an-llm.md))
- **Chain-of-thought faithfulness**: Whether a model's written reasoning reflects the computation that actually produced its answer. ([01](../modules/01-what-is-an-llm.md))
- **Change failure rate**: The share of deployments that cause a failure needing a fix or rollback (a DORA metric). ([10](../modules/10-ai-code-review.md))
- **Checkpoint**: An automatic snapshot of an agent's edits that you can rewind to. ([06](../modules/06-harnesses-and-tools.md), [08](../modules/08-agentic-workflows.md))
- **Chinchilla scaling**: The finding that compute-optimal training uses roughly 20 tokens per parameter. ([01](../modules/01-what-is-an-llm.md))
- **CLI agent**: A coding agent that runs in the terminal and acts through shell commands and file edits. ([06](../modules/06-harnesses-and-tools.md))
- **Closed weight / API-only**: A model you can use only through the lab's servers. ([04](../modules/04-open-vs-closed-weights.md))
- **Cloud (background) agent**: An agent that runs in a remote sandbox and returns its work, usually as a pull request. ([06](../modules/06-harnesses-and-tools.md))
- **Co-author trailer**: A line such as `Co-Authored-By:` at the end of a git commit message that credits another contributor or tool. ([15](../modules/15-learning-careers-and-responsibility.md))
- **Code mode (code execution with MCP)**: Presenting tools as a code API the model calls from a sandbox, to save context. ([06](../modules/06-harnesses-and-tools.md))
- **Code review**: A person (or tool) other than the author reading a change before it merges. ([10](../modules/10-ai-code-review.md))
- **Coding agent**: A language model in a loop with tools (read files, run commands, edit code) that works on a task until it decides it's done. ([00](../modules/00-orientation.md))
- **Coding plan**: A flat-rate subscription from a model provider for use in coding harnesses. ([04](../modules/04-open-vs-closed-weights.md), [12](../modules/12-costs-subscriptions-and-apis.md))
- **Cognitive debt**: Kosmyna et al.'s term for reduced engagement and recall that may accumulate when people rely on an LLM to do a task. ([15](../modules/15-learning-careers-and-responsibility.md))
- **Cognitive offloading**: Handing mental work to a tool; helpful for routine work, harmful when it skips the thinking you're trying to learn. ([15](../modules/15-learning-careers-and-responsibility.md))
- **Cognitive surrender**: Letting automation do your thinking until you no longer understand the work. ([07](../modules/07-context-engineering.md))
- **Compaction**: Summarizing a long conversation so work can continue in a fresh window. ([07](../modules/07-context-engineering.md), [14](../modules/14-keeping-up.md))
- **Configuration**: The full setup being evaluated: model, version, harness, and settings. ([05](../modules/05-judging-models.md))
- **Constitutional AI**: Anthropic's method of training with AI feedback guided by written principles. ([01](../modules/01-what-is-an-llm.md))
- **Contamination**: Benchmark items or solutions present in a model's training data, inflating its score. ([05](../modules/05-judging-models.md))
- **Context engineering**: Choosing everything that fills the context window at each step of an agent's work. ([07](../modules/07-context-engineering.md))
- **Context rot**: The drop in model performance as input length grows, even on simple tasks. ([07](../modules/07-context-engineering.md))
- **Context window**: The maximum number of tokens a model can consider at once. ([01](../modules/01-what-is-an-llm.md), [07](../modules/07-context-engineering.md))
- **Continual learning**: Learning from new data over time without forgetting earlier knowledge. ([02](../modules/02-training-and-tuning.md))
- **Copyrightability**: Whether a work can be protected by copyright; in the US, requires sufficient human authorship. ([15](../modules/15-learning-careers-and-responsibility.md))
- **Cost per task**: The full cost of finishing a job, including retries and extra tokens. Compare this, not the price per token. ([03](../modules/03-model-landscape.md), [12](../modules/12-costs-subscriptions-and-apis.md))
- **Cross-model review**: Having one lab's model review code written by another lab's model. ([09](../modules/09-multi-agent-systems.md), [10](../modules/10-ai-code-review.md))
- **`.cursorrules`**: Cursor's original repository-wide rules file, later replaced by scoped Project Rules. ([07](../modules/07-context-engineering.md))

## D

- **Data poisoning**: Inserting malicious examples into training data to plant a backdoor or bias. ([02](../modules/02-training-and-tuning.md))
- **Decoder-only / encoder-only model**: Transformer variants for generation (GPT style) or for understanding and classification (BERT style). ([01](../modules/01-what-is-an-llm.md))
- **Definition of done**: The concrete, checkable condition that says a task is finished. ([08](../modules/08-agentic-workflows.md))
- **Deliberative alignment**: OpenAI's method of training reasoning models to reason explicitly over a written safety specification. ([02](../modules/02-training-and-tuning.md))
- **Deskilling**: Losing a skill because a tool performs it for you. ([15](../modules/15-learning-careers-and-responsibility.md))
- **Direct prompt injection**: The attacker types the malicious instructions into the application themselves. ([11](../modules/11-security-and-prompt-injection.md))
- **Distillation**: Training a smaller student model to imitate a larger teacher model. ([02](../modules/02-training-and-tuning.md), [03](../modules/03-model-landscape.md))
- **Distillation attack**: Illicit large-scale querying of a model to train a competing one, in breach of terms of service. ([02](../modules/02-training-and-tuning.md))
- **DPO (Direct Preference Optimization)**: Preference tuning that skips the separate reward model and RL loop. ([02](../modules/02-training-and-tuning.md))
- **Dual LLM pattern**: A design where a privileged model never sees untrusted text and a quarantined model that reads it cannot call tools. ([11](../modules/11-security-and-prompt-injection.md))

## E

- **Early-career "canaries"**: Young workers in AI-exposed occupations, whose employment trends may signal AI's labor effects first. ([15](../modules/15-learning-careers-and-responsibility.md))
- **Egress control**: Restricting which outbound network destinations a process can contact. ([11](../modules/11-security-and-prompt-injection.md))
- **Elo / Arena rating**: A rating computed from pairwise human preference votes. ([05](../modules/05-judging-models.md))
- **Embedding**: A vector of numbers representing a token (or document) so that related meanings sit near each other. ([01](../modules/01-what-is-an-llm.md))
- **Emergent abilities**: Capabilities that appear to arise abruptly with scale; partly debated as a measurement artifact. ([01](../modules/01-what-is-an-llm.md))
- **Emergent misalignment**: Broad misaligned behavior arising from narrow fine-tuning, such as on insecure code. ([02](../modules/02-training-and-tuning.md))
- **Error amplification**: How much a system's architecture spreads individual mistakes into the final output. ([09](../modules/09-multi-agent-systems.md))
- **Escaped defect**: A bug that gets past review and testing and is found after merge. ([10](../modules/10-ai-code-review.md))
- **Evaluation awareness**: A model recognizing that it's being tested, which can make eval results unrepresentative. ([05](../modules/05-judging-models.md))
- **Evolutionary coding agent**: A system that generates many program variants, tests them, and keeps and mutates the best (e.g., AlphaEvolve). ([02](../modules/02-training-and-tuning.md))
- **Excessive agency**: OWASP's term for giving an LLM application more tools, permissions, or autonomy than its task needs. ([11](../modules/11-security-and-prompt-injection.md))
- **Explain-back**: Restating something in your own words, without the source in front of you, to test understanding. ([15](../modules/15-learning-careers-and-responsibility.md))
- **Extractive contribution**: In LLVM's policy, a contribution that costs maintainers more to review than it gives the project. ([13](../modules/13-open-source-ecosystem.md))

## F

- **Fable / Mythos**: Two releases of the same Anthropic top-tier model with different safeguards. ([03](../modules/03-model-landscape.md))
- **False positive**: A reported finding that is not actually a problem. ([10](../modules/10-ai-code-review.md))
- **False-positive fatigue**: People starting to ignore a reviewer because too many of its comments are wrong or useless. ([10](../modules/10-ai-code-review.md))
- **Fan-out / merge**: Running fixed slices of work in parallel, then combining the results. ([09](../modules/09-multi-agent-systems.md))
- **Fast / priority mode**: A higher-priced service tier that returns results faster or with guaranteed capacity. ([12](../modules/12-costs-subscriptions-and-apis.md))
- **Fast-follow**: Catching up to a frontier capability months later, often helped by public research and distillation. ([03](../modules/03-model-landscape.md))
- **Feature (interpretability)**: An internal direction in a model's activations that corresponds to a recognizable concept. ([01](../modules/01-what-is-an-llm.md))
- **Few-shot / zero-shot prompting**: Prompting with a few examples, or with none. ([01](../modules/01-what-is-an-llm.md))
- **Few-shot prompting**: Including a few worked examples in the prompt. ([07](../modules/07-context-engineering.md))
- **Finding**: One issue a reviewer reports, ideally with a location, a failure scenario, and a severity. ([10](../modules/10-ai-code-review.md))
- **Fine-tuning**: Further training of a pretrained model on a narrower dataset. ([02](../modules/02-training-and-tuning.md))
- **Frontier lab**: An organization that trains its own models at the edge of current capability. ([03](../modules/03-model-landscape.md))
- **FSL (Functional Source License)**: A source-available license that forbids competing commercial use and converts to a permissive license after two years. ([13](../modules/13-open-source-ecosystem.md))
- **Full fine-tuning**: Fine-tuning that updates every weight. ([02](../modules/02-training-and-tuning.md))
- **Fully open model**: An open-source model that also releases its training data, checkpoints and logs (for example OLMo). ([04](../modules/04-open-vs-closed-weights.md))

## G

- **Gated tier**: A model or variant available only to vetted users because of misuse risk. ([03](../modules/03-model-landscape.md))
- **Generator–critic (evaluator–optimizer)**: One agent produces output, another critiques it, and the first revises. ([09](../modules/09-multi-agent-systems.md))
- **GGUF**: The single-file model format used by llama.cpp and tools built on it. ([02](../modules/02-training-and-tuning.md), [04](../modules/04-open-vs-closed-weights.md), [13](../modules/13-open-source-ecosystem.md))
- **Git worktree**: An additional working directory on the same repository, used to run agents in parallel. ([06](../modules/06-harnesses-and-tools.md), [08](../modules/08-agentic-workflows.md))
- **Golden task**: A frozen, solved task from your own work, replayed to compare models and tools. ([05](../modules/05-judging-models.md))
- **Goodhart's law**: "When a measure becomes a target, it ceases to be a good measure." ([05](../modules/05-judging-models.md), [10](../modules/10-ai-code-review.md))
- **GPTQ / AWQ**: Two widely used post-training quantization methods. ([02](../modules/02-training-and-tuning.md))
- **Grader**: The mechanism that decides pass or fail: unit tests, a rubric, human raters, or an LLM judge. ([05](../modules/05-judging-models.md))
- **Graph engineering**: Designing how multiple agents or steps connect: nodes, edges, shared state and routing. ([07](../modules/07-context-engineering.md))
- **Greedy decoding**: Always choosing the single most probable next token. ([01](../modules/01-what-is-an-llm.md))
- **GRPO (Group Relative Policy Optimization)**: An RL algorithm that scores a group of sampled answers against each other, removing the need for a separate critic model. ([02](../modules/02-training-and-tuning.md))

## H

- **Hallucination**: Fluent, confident output that is false. ([01](../modules/01-what-is-an-llm.md))
- **Harness**: The software around a model that manages context, tools, and the loop. ([01](../modules/01-what-is-an-llm.md), [06](../modules/06-harnesses-and-tools.md))
- **Harness (scaffold, agent)**: The program around a model that supplies prompts and tools and runs the loop; part of what any agentic score measures. ([05](../modules/05-judging-models.md))
- **Harness engineering**: Improving the agent's environment so mistakes are prevented, caught or corrected automatically. ([07](../modules/07-context-engineering.md))
- **Harness-level self-improvement**: An agent improving its own scaffold code, prompts, and tools while the underlying model's weights stay fixed (e.g., Darwin Gödel Machine, AIDE²). ([02](../modules/02-training-and-tuning.md))
- **Homogeneous / heterogeneous team**: Agents that all use one model vs agents that use different models. ([09](../modules/09-multi-agent-systems.md))
- **Hook**: A user-defined command the harness runs at a lifecycle event, giving deterministic control. ([06](../modules/06-harnesses-and-tools.md))
- **Human accountability**: The principle that a named person, not a tool, answers for any change that is shipped. ([15](../modules/15-learning-careers-and-responsibility.md))

## I

- **IFScale**: A benchmark measuring how instruction-following degrades as the number of instructions grows. ([07](../modules/07-context-engineering.md))
- **In-context learning**: A model picking up a task from examples or instructions in its prompt, with no weight changes. ([01](../modules/01-what-is-an-llm.md))
- **Indirect prompt injection**: The attacker plants instructions in content (web pages, files, issues, emails) that a model reads later on someone else's behalf. ([11](../modules/11-security-and-prompt-injection.md))
- **Inference geo / data residency**: Controls over where a provider runs inference and stores your data. ([04](../modules/04-open-vs-closed-weights.md))
- **Inference runtime**: Software that loads model weights and generates output (llama.cpp, Ollama, vLLM, SGLang, MLX). ([13](../modules/13-open-source-ecosystem.md))
- **Information diet**: The deliberate, limited set of sources you follow to stay current. ([14](../modules/14-keeping-up.md))
- **Input tokens**: Everything sent to the model on a call, including history, files, and tool results. ([12](../modules/12-costs-subscriptions-and-apis.md))
- **Instruction file (context file)**: A markdown file such as `CLAUDE.md` or `AGENTS.md` loaded into every agent session. ([07](../modules/07-context-engineering.md))
- **Instruction hierarchy**: Training a model to prioritize system instructions over user text over tool output. ([11](../modules/11-security-and-prompt-injection.md))
- **Interpretability**: Research into how a neural network computes its outputs internally. ([01](../modules/01-what-is-an-llm.md))

## J

- **Jailbreak**: An attempt to make a model violate its own built-in safety rules; distinct from attacking an application built on the model. ([11](../modules/11-security-and-prompt-injection.md))
- **Judge panel (jury)**: Several model judges, ideally from different families, scoring the same output. ([09](../modules/09-multi-agent-systems.md))
- **Just-in-time retrieval**: Loading files or data into context only when the agent needs them. ([07](../modules/07-context-engineering.md))

## K

- **KV cache**: Stored attention keys and values for earlier tokens, reused to speed up generation. ([01](../modules/01-what-is-an-llm.md), [04](../modules/04-open-vs-closed-weights.md))

## L

- **Large language model (LLM)**: A neural network with billions or more parameters, trained on large text corpora to predict the next token. ([01](../modules/01-what-is-an-llm.md))
- **Layered review**: Stacking independent checks (author self-check, bot review, human review) so each catches what the others miss. ([10](../modules/10-ai-code-review.md))
- **Learning mode / study mode**: AI tool settings that tutor with hints and questions instead of giving complete answers. ([15](../modules/15-learning-careers-and-responsibility.md))
- **Lethal trifecta**: Willison's term for an agent that combines private data access, exposure to untrusted content, and the ability to communicate externally, which makes data theft by injection possible. ([11](../modules/11-security-and-prompt-injection.md))
- **License contamination**: Introducing code under incompatible license terms, for example GPL code into a proprietary project, often unknowingly. ([15](../modules/15-learning-careers-and-responsibility.md))
- **LLM judge**: A language model used to score another model's output. ([05](../modules/05-judging-models.md))
- **Loaded cost**: An employee's total cost to the employer, including salary, benefits, taxes, and overhead. ([12](../modules/12-costs-subscriptions-and-apis.md))
- **Logit distillation vs output distillation**: Learning from the teacher's token probabilities versus from its generated text. ([02](../modules/02-training-and-tuning.md))
- **Loop engineering**: Designing systems that repeatedly prompt an agent, with schedules, goals, verifiers and stopping rules. ([07](../modules/07-context-engineering.md))
- **LoRA (Low-Rank Adaptation)**: A PEFT method that learns a small low-rank correction to weight matrices. ([02](../modules/02-training-and-tuning.md))
- **Lost in the middle**: The tendency of models to use information at the start and end of a long context better than information in the middle. ([07](../modules/07-context-engineering.md))

## M

- **MAST**: The Multi-Agent System Failure Taxonomy of 14 failure modes in three categories (Cemri et al., 2025). ([09](../modules/09-multi-agent-systems.md))
- **MCP (Model Context Protocol)**: An open JSON-RPC protocol for connecting AI applications to tools, resources and prompts provided by servers. ([06](../modules/06-harnesses-and-tools.md))
- **MCP Apps**: An MCP extension that lets tools return interactive UI rendered by the host. ([06](../modules/06-harnesses-and-tools.md))
- **MCP host / client / server**: The AI app; the connector inside it for one server; the program exposing capabilities. ([06](../modules/06-harnesses-and-tools.md))
- **Memory consolidation**: Moving what a model has picked up in fast, temporary memory (its context or fast-changing parameters) into slower, more stable weights. ([02](../modules/02-training-and-tuning.md))
- **Mid-training**: A loosely defined phase between bulk pretraining and post-training, focused on high-quality or specialized data and longer context. ([02](../modules/02-training-and-tuning.md))
- **MIT / Apache-2.0**: Permissive open-source licenses; Apache-2.0 adds an explicit patent grant. ([13](../modules/13-open-source-ecosystem.md))
- **Mixture of experts (MoE)**: An architecture where a router sends each token through only a few of many expert sub-networks. ([01](../modules/01-what-is-an-llm.md), [04](../modules/04-open-vs-closed-weights.md))
- **Model as a Service (MaaS) clause**: A license term requiring a separate agreement before you host a model for paying third parties above some size. ([04](../modules/04-open-vs-closed-weights.md))
- **Model collapse**: Quality degradation when models are trained recursively on model-generated data. ([02](../modules/02-training-and-tuning.md))
- **Model Context Protocol (MCP)**: An open standard (Anthropic, 2024) for connecting tools and data sources to models. ([01](../modules/01-what-is-an-llm.md))
- **Model ID / snapshot**: The exact string you send to an API to pick a model. ([03](../modules/03-model-landscape.md))
- **Model picker**: The UI control that lets users choose which model answers in a chat app. ([14](../modules/14-keeping-up.md))
- **Model routing**: Sending easy work to cheaper models and hard work to more capable ones. ([12](../modules/12-costs-subscriptions-and-apis.md))
- **Model snapshot (pinned version)**: A dated, fixed model version offered by an API, as opposed to an alias that moves. ([14](../modules/14-keeping-up.md))
- **Multi-agent debate**: Agents argue over answers for several rounds before converging. ([09](../modules/09-multi-agent-systems.md))
- **Multi-agent system**: Several model instances, each with its own context and role, coordinated by code or by another agent. ([09](../modules/09-multi-agent-systems.md))
- **Multi-head attention**: Running several attention operations in parallel so the model can track different relationships at once. ([01](../modules/01-what-is-an-llm.md))
- **Multimodal model**: A model that handles more than text, such as images or audio. ([01](../modules/01-what-is-an-llm.md))
- **Muse**: Meta Superintelligence Labs' model family (from April 2026), mostly closed, with two open-weight members. ([03](../modules/03-model-landscape.md))
- **Mythos-class**: Anthropic's tier above Opus, previewed to vetted partners in April 2026 (Project Glasswing) and released in June 2026 as Fable (general) and Mythos (vetted access). ([03](../modules/03-model-landscape.md))

## N

- **Needle in a haystack (NIAH)**: A test that hides one fact in long filler text and asks the model to retrieve it. ([07](../modules/07-context-engineering.md))

## O

- **Open source AI (OSI definition)**: An AI system released with weights, complete training code and detailed data information, under terms granting use, study, modification and sharing. ([04](../modules/04-open-vs-closed-weights.md))
- **Open weight**: A model whose weights you can download, under some license. ([04](../modules/04-open-vs-closed-weights.md))
- **Open-source software**: Software whose source code is published under a license allowing use, modification and redistribution. ([13](../modules/13-open-source-ecosystem.md))
- **Open-weight model**: A model whose trained weights are published for download. ([02](../modules/02-training-and-tuning.md), [13](../modules/13-open-source-ecosystem.md))
- **Oracle**: An automated source of truth to check results against, such as a reference implementation or conformance suite. ([08](../modules/08-agentic-workflows.md))
- **Orchestrator**: Software that runs and coordinates several agents at once, often one per git worktree. ([06](../modules/06-harnesses-and-tools.md), [13](../modules/13-open-source-ecosystem.md))
- **Orchestrator–workers**: A pattern where a lead agent splits a task at run time and delegates the pieces. ([09](../modules/09-multi-agent-systems.md))
- **Output tokens**: Everything the model generates on a call, including reasoning tokens. ([12](../modules/12-costs-subscriptions-and-apis.md))

## P

- **Package hallucination**: A model recommending a software package that does not exist. ([11](../modules/11-security-and-prompt-injection.md))
- **PagedAttention**: VLLM's technique for managing attention memory in pages to serve more requests at once. ([13](../modules/13-open-source-ecosystem.md))
- **Parameter-efficient fine-tuning (PEFT)**: Fine-tuning that freezes the base weights and trains a small add-on. ([02](../modules/02-training-and-tuning.md))
- **Parameters / weights**: The learned numbers inside a neural network. ([01](../modules/01-what-is-an-llm.md))
- **pass@1 / pass@k**: Share of tasks solved on the first attempt / with at least one success in k attempts. ([05](../modules/05-judging-models.md))
- **pass^k**: Probability that all k independent attempts succeed; a reliability measure from τ-bench. ([05](../modules/05-judging-models.md))
- **Path-scoped rule**: An instruction that loads only when the agent works on matching files. ([07](../modules/07-context-engineering.md))
- **Permission mode**: A preset for how much an agent may do without asking. ([06](../modules/06-harnesses-and-tools.md))
- **Personal agent**: An agent that acts across a person's own accounts and devices, often through messaging apps. ([13](../modules/13-open-source-ecosystem.md))
- **Plan mode**: A harness mode in which the agent reads and proposes a plan but makes no edits until you approve. ([08](../modules/08-agentic-workflows.md))
- **Plugin / marketplace**: A bundle of skills, hooks, subagents and MCP servers; a git-hosted catalog of them. ([06](../modules/06-harnesses-and-tools.md))
- **Post-training**: Training after pretraining that turns a base model into a helpful, safer assistant (SFT, RLHF, RL). ([01](../modules/01-what-is-an-llm.md))
- **Postmortem**: A written analysis of an incident: what happened, why, and what will change. ([14](../modules/14-keeping-up.md))
- **PPO (Proximal Policy Optimization)**: The classic RL algorithm used in RLHF. ([02](../modules/02-training-and-tuning.md))
- **Preference tuning**: Training a model on comparisons between better and worse responses. ([02](../modules/02-training-and-tuning.md))
- **Pretraining**: The first, largest training phase: next-token prediction on huge text corpora. ([01](../modules/01-what-is-an-llm.md))
- **Price floor**: The lowest price the market will bear, often set by cheaply hosted open models. ([03](../modules/03-model-landscape.md))
- **Product sense**: Judgment about what is worth building, for whom, and what "done" means. ([15](../modules/15-learning-careers-and-responsibility.md))
- **Progressive disclosure**: Showing an agent short descriptions first and full details only when needed. ([06](../modules/06-harnesses-and-tools.md))
- **Prompt caching**: Reusing the KV cache for a repeated prompt prefix, usually at a discount. ([01](../modules/01-what-is-an-llm.md), [12](../modules/12-costs-subscriptions-and-apis.md))
- **Prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer**: Anthropic's five common workflow patterns. ([07](../modules/07-context-engineering.md))
- **Prompt engineering**: Writing the instructions and examples sent to a model to get the output you want. ([07](../modules/07-context-engineering.md))
- **Prompt injection**: An attack where text supplied by someone other than the user (or the user against the app owner) is interpreted by a model as instructions. ([11](../modules/11-security-and-prompt-injection.md))
- **Prompt tuning**: Learning "soft prompt" vectors instead of changing model weights. ([02](../modules/02-training-and-tuning.md))
- **Prototype-driven (draft-driven) development**: Building a quick throwaway version first, reacting to it, then rebuilding or hardening the keeper on purpose. ([08](../modules/08-agentic-workflows.md))

## Q

- **QLoRA**: LoRA training on top of a base model quantized to 4 bits. ([02](../modules/02-training-and-tuning.md))
- **Quantization**: Storing model weights with fewer bits to save memory and speed up inference. ([02](../modules/02-training-and-tuning.md), [04](../modules/04-open-vs-closed-weights.md))
- **Quantization-aware training (QAT)**: Training a model so it loses little quality when quantized. ([04](../modules/04-open-vs-closed-weights.md))

## R

- **Ralph loop**: A shell loop that feeds the same prompt to a coding agent repeatedly, with a plan file as memory. ([07](../modules/07-context-engineering.md), [08](../modules/08-agentic-workflows.md))
- **RCT (randomized controlled trial)**: An experiment that randomly assigns participants or tasks to treatment and control. ([05](../modules/05-judging-models.md))
- **ReAct**: A 2022 prompting pattern that interleaves written reasoning steps with tool actions; the basis of most agents. ([08](../modules/08-agentic-workflows.md))
- **Read/write asymmetry**: Read-heavy work (review, research) parallelizes well; write-heavy work on shared code usually does not. ([09](../modules/09-multi-agent-systems.md))
- **Reasoning (thinking) tokens**: Tokens a model generates while working through a problem before answering; billed as output. ([12](../modules/12-costs-subscriptions-and-apis.md))
- **Reasoning effort**: A setting that controls how long a model thinks before answering. ([03](../modules/03-model-landscape.md))
- **Reasoning model**: A model trained (usually with reinforcement learning) to think at length before answering. ([01](../modules/01-what-is-an-llm.md))
- **Recursive self-improvement**: A system improving the process by which it improves, potentially compounding. ([02](../modules/02-training-and-tuning.md))
- **Regression (model or tool)**: A drop in quality after a change, whether in the model, harness, product settings, or serving infrastructure. ([14](../modules/14-keeping-up.md))
- **Reinforcement learning with verifiable rewards (RLVR)**: RL where the reward comes from automatically checkable outcomes, such as correct math answers or passing tests. ([01](../modules/01-what-is-an-llm.md))
- **Repository map**: A compact summary of a codebase's files and symbols given to an agent, popularized by Aider. ([13](../modules/13-open-source-ecosystem.md))
- **Retrieval-augmented generation (RAG)**: Retrieving relevant documents and putting them in the model's context before it answers. ([01](../modules/01-what-is-an-llm.md))
- **Revert rate**: The share of merged changes that are later reverted. ([10](../modules/10-ai-code-review.md))
- **Review instruction file**: A repository file that tells a review bot what to check and skip (`REVIEW.md`, `AGENTS.md` review rules, `.cursor/BUGBOT.md`, `copilot-instructions.md`). ([10](../modules/10-ai-code-review.md))
- **Review swarm**: Independent reviewers split by concern, followed by adversarial verification of each finding. ([09](../modules/09-multi-agent-systems.md))
- **Reward hacking**: A model scoring well on a reward signal without doing the intended task, for example by editing tests. ([02](../modules/02-training-and-tuning.md), [05](../modules/05-judging-models.md), [08](../modules/08-agentic-workflows.md))
- **Reward model**: A model trained to score responses by predicted human (or AI) preference. ([01](../modules/01-what-is-an-llm.md))
- **RLAIF**: Reinforcement learning from AI feedback; an AI model supplies the preference judgments. ([02](../modules/02-training-and-tuning.md))
- **RLHF**: Reinforcement learning from human feedback; optimizing a model toward responses a learned reward model predicts people prefer. ([01](../modules/01-what-is-an-llm.md))
- **RLVR**: Reinforcement learning with verifiable rewards; rewards come from automatic checks such as tests or answer matching. ([02](../modules/02-training-and-tuning.md))
- **Rubber-stamping**: Approving a change without really reviewing it. ([10](../modules/10-ai-code-review.md))
- **Rug pull (MCP)**: A tool server changing its tool descriptions or behavior after the user approved it. ([11](../modules/11-security-and-prompt-injection.md))
- **Rumor laundering**: An unverified claim gaining false credibility as it's repeated by successively more official-looking sources. ([14](../modules/14-keeping-up.md))

## S

- **Safetensors**: A weight file format that holds only tensors and can't run code when loaded. ([04](../modules/04-open-vs-closed-weights.md))
- **Safety routing (fallback)**: Sending a flagged request to a different, more restricted model. ([03](../modules/03-model-landscape.md))
- **Sandbox**: An environment that limits what files, network hosts and credentials an agent can reach. ([06](../modules/06-harnesses-and-tools.md), [11](../modules/11-security-and-prompt-injection.md))
- **Saturation**: When top models score near a benchmark's ceiling, so it no longer separates them. ([05](../modules/05-judging-models.md))
- **Scaling laws**: Empirical power-law relationships between model size, data, compute, and loss. ([01](../modules/01-what-is-an-llm.md))
- **Scope creep (agent)**: An agent changing things outside the task it was given. ([08](../modules/08-agentic-workflows.md))
- **Self-distillation fine-tuning (SDFT)**: A continual-learning method in which a model shown a demonstration acts as its own teacher, reported to forget less than ordinary supervised fine-tuning. ([02](../modules/02-training-and-tuning.md))
- **Self-edit (SEAL)**: Training data and update instructions a model writes for itself, applied as a weight update. ([02](../modules/02-training-and-tuning.md))
- **Self-preference bias**: A model judge's tendency to rate its own (or familiar-looking) outputs higher. ([09](../modules/09-multi-agent-systems.md))
- **Self-tuning (weight self-modification)**: A model producing the training data, edits, or settings that a training step then uses to update its own parameters. ([02](../modules/02-training-and-tuning.md))
- **Severity triage**: Sorting findings by impact (high, medium, low, noise) to decide what blocks a merge. ([10](../modules/10-ai-code-review.md))
- **Signed-off-by / DCO**: A commit tag by which a human certifies the Developer Certificate of Origin; the Linux kernel forbids AI agents from adding it. ([13](../modules/13-open-source-ecosystem.md))
- **Skill**: A folder with a `SKILL.md` and optional scripts that an agent loads only when relevant. ([06](../modules/06-harnesses-and-tools.md))
- **Skill formation**: Building durable ability through practice, as distinct from completing a task. ([15](../modules/15-learning-careers-and-responsibility.md))
- **Skill registry**: A public catalog of installable agent skills, which is a software supply chain. ([13](../modules/13-open-source-ecosystem.md))
- **Sleep framework**: Google's 2026 continual-learning method in which a model alternates between active use and offline phases that consolidate new knowledge into its weights and rehearse it with self-generated practice data ("dreaming"). ([02](../modules/02-training-and-tuning.md))
- **Slopsquatting**: Registering package names that models hallucinate, so that AI-suggested installs fetch malware. ([11](../modules/11-security-and-prompt-injection.md))
- **Society of Mind**: Minsky's 1986 theory of intelligence as many simple interacting agents; an early framing for multi-agent AI. ([09](../modules/09-multi-agent-systems.md))
- **Software factory / dark factory**: A pipeline where agents write and check code from specs with no human writing or reviewing code. ([08](../modules/08-agentic-workflows.md))
- **Source-available**: Code you can read but not freely reuse, unlike open source. ([13](../modules/13-open-source-ecosystem.md))
- **Sparse autoencoder**: A tool used to decompose a model's activations into interpretable features. ([01](../modules/01-what-is-an-llm.md))
- **Spec drift**: A specification falling out of sync with the code it describes. ([07](../modules/07-context-engineering.md))
- **Spec-driven development**: Writing a specification, plan and task list before an agent implements. ([07](../modules/07-context-engineering.md))
- **Spec-first**: Writing down requirements and a definition of done (often in a `SPEC.md`) before implementation starts. ([08](../modules/08-agentic-workflows.md))
- **Spike**: A short, timeboxed experiment in code to answer a design question before committing to an approach. ([08](../modules/08-agentic-workflows.md))
- **Stacked PRs**: A chain of small, dependent pull requests reviewed in order instead of one large one. ([10](../modules/10-ai-code-review.md))
- **Stage (Yegge)**: One of eight levels in Steve Yegge's chart of how far a developer delegates to AI agents. ([08](../modules/08-agentic-workflows.md))
- **Staged rollout**: Releasing a change to a fraction of users first, so different users see different versions at once. ([14](../modules/14-keeping-up.md))
- **Status page**: A vendor's public page reporting outages and incidents. ([14](../modules/14-keeping-up.md))
- **stdio / Streamable HTTP**: MCP's two transports, for local subprocess servers and remote servers. ([06](../modules/06-harnesses-and-tools.md))
- **Stochastic parrot**: Bender et al.'s term for a system that strings together language by probability without grounding in meaning. ([01](../modules/01-what-is-an-llm.md))
- **Subagent**: A separate agent with a fresh context window launched by the main agent for a focused task. ([06](../modules/06-harnesses-and-tools.md), [09](../modules/09-multi-agent-systems.md))
- **Substitution vs complementarity**: Whether AI replaces tasks a worker did or makes the worker more productive at them. ([15](../modules/15-learning-careers-and-responsibility.md))
- **Supervised agent**: A coding agent whose every change a human reviews before it's kept. ([00](../modules/00-orientation.md))
- **Supervised fine-tuning (SFT) / instruction tuning**: Training on example prompts paired with good responses. ([01](../modules/01-what-is-an-llm.md))
- **Swallowed error**: Code that catches an error and hides it, so callers cannot tell failure from success. ([10](../modules/10-ai-code-review.md))
- **Sycophancy**: A model's tendency to agree with or flatter the user at the expense of accuracy. ([01](../modules/01-what-is-an-llm.md), [08](../modules/08-agentic-workflows.md), [14](../modules/14-keeping-up.md))
- **Synthetic data**: Training data generated by models rather than written by people. ([02](../modules/02-training-and-tuning.md))
- **System card (model card)**: A lab's technical report on a model's capabilities, evaluations, safety testing, and limitations. ([05](../modules/05-judging-models.md))

## T

- **Tautological test**: A test that cannot fail because it checks the code against itself or a mock against its own setup. ([08](../modules/08-agentic-workflows.md))
- **Temperature**: A sampling setting that controls how random token selection is. ([01](../modules/01-what-is-an-llm.md))
- **Test-driven development (TDD)**: Writing a failing test before the code that makes it pass; with agents, the test becomes the contract. ([08](../modules/08-agentic-workflows.md))
- **Test-time (inference-time) compute**: Spending more computation per answer, for example longer thinking or multiple samples. ([01](../modules/01-what-is-an-llm.md))
- **Test-time training**: Updating some model weights on each input at inference time. ([02](../modules/02-training-and-tuning.md))
- **Tier**: A size and price level within a model generation (for example Haiku, Sonnet, Opus; Luna, Terra, Sol, Astra; Flash-Lite, Flash, Pro). ([03](../modules/03-model-landscape.md))
- **Time horizon**: METR's measure of the length of task (in human working time) an AI can complete with 50% reliability. ([00](../modules/00-orientation.md), [08](../modules/08-agentic-workflows.md))
- **Time horizon (50%)**: The human-time length of tasks a model completes half the time (METR's measure). ([05](../modules/05-judging-models.md))
- **Token**: A chunk of text (often part of a word) that a model reads and writes; the unit of cost and context limits. ([01](../modules/01-what-is-an-llm.md), [12](../modules/12-costs-subscriptions-and-apis.md))
- **Tokenizer**: The component that splits text into tokens and maps them to integer IDs. ([01](../modules/01-what-is-an-llm.md), [12](../modules/12-costs-subscriptions-and-apis.md))
- **Tool / tool call**: A function a harness exposes to the model with a name, description and input schema; a tool call is the model's structured request to run one. ([06](../modules/06-harnesses-and-tools.md))
- **Tool poisoning**: Hiding instructions in an MCP tool's description, which the model reads but users usually don't. ([11](../modules/11-security-and-prompt-injection.md))
- **Tool search**: Loading tool definitions on demand instead of all at once. ([06](../modules/06-harnesses-and-tools.md))
- **Tool use / function calling**: A model emitting structured requests that a harness executes, with results returned to the context. ([01](../modules/01-what-is-an-llm.md))
- **Top-p (nucleus) sampling**: Sampling only from the smallest set of tokens whose probabilities sum to p. ([01](../modules/01-what-is-an-llm.md))
- **Total vs active parameters**: In MoE, all parameters stored versus those used for a given token. ([01](../modules/01-what-is-an-llm.md))
- **Toxic agent flow**: Invariant Labs' term for a sequence of individually allowed tool calls that, triggered by injected text, adds up to a harmful outcome. ([11](../modules/11-security-and-prompt-injection.md))
- **Training cutoff**: The date after which a model has no training data. ([01](../modules/01-what-is-an-llm.md))
- **Training vs inference**: Training adjusts weights; inference uses frozen weights to produce output. ([01](../modules/01-what-is-an-llm.md))
- **Transformer**: The neural network architecture from "Attention Is All You Need" (2017) that underlies nearly all LLMs. ([01](../modules/01-what-is-an-llm.md))
- **Two-week rule**: Waiting about two weeks after a release before adopting it, unless it solves a current problem. ([14](../modules/14-keeping-up.md))

## U

- **Unified memory**: Memory shared by CPU and GPU on Apple silicon, so large models can load without a discrete GPU. ([04](../modules/04-open-vs-closed-weights.md))
- **Usage cap**: The limit on how much a subscription allows in a rolling window (often 5 hours) or per week. ([12](../modules/12-costs-subscriptions-and-apis.md))
- **Usage limits (quotas)**: Caps on how much a subscription plan can use in a time window (for example, five-hour and weekly limits). ([14](../modules/14-keeping-up.md))

## V

- **Verification step**: Checking a finding against the code, ideally by reproducing it with a test, before acting. ([10](../modules/10-ai-code-review.md))
- **Verifier**: A test, tool or separate model that checks an agent's claimed result. ([07](../modules/07-context-engineering.md))
- **Vibe coding**: Karpathy's term for building software by prompting an AI and accepting its output without reading the code. ([00](../modules/00-orientation.md))
- **Vibe engineering / agentic engineering**: The disciplined counterpart: AI does most of the typing, a human stays accountable for design, review, and testing. ([00](../modules/00-orientation.md))
- **Vibes**: Experienced users' informal impressions of a model; useful but noisy data. ([05](../modules/05-judging-models.md))
- **Vibes log**: A dated record of notable model successes and failures, used to make informal impressions countable. ([14](../modules/14-keeping-up.md))
- **Vouching**: Ghostty's system in which a maintainer approves a first-time contributor before their PRs are accepted. ([13](../modules/13-open-source-ecosystem.md))
- **VRAM**: A discrete GPU's own memory. ([04](../modules/04-open-vs-closed-weights.md))

## W

- **Warm backup**: A second tool kept configured and in occasional use, so you can switch quickly. ([14](../modules/14-keeping-up.md))
- **Weight-space programming**: A model reading and editing another neural network's weights directly, as numbers, without gradient-based training. ([02](../modules/02-training-and-tuning.md))
- **Weights (parameters)**: The learned numbers that define a model's behavior. ([04](../modules/04-open-vs-closed-weights.md))
- **Workflow (vs. agent)**: An LLM system following predefined code paths, as opposed to one that directs its own process. ([07](../modules/07-context-engineering.md), [09](../modules/09-multi-agent-systems.md))
- **Workslop**: AI-generated work that looks complete but lacks substance, shifting effort to whoever receives it. ([15](../modules/15-learning-careers-and-responsibility.md))
- **Write / select / compress / isolate**: LangChain's four categories of context-engineering technique. ([07](../modules/07-context-engineering.md))

## Y

- **YOLO / skip-permissions mode**: An agent setting that runs every action without asking for approval. ([11](../modules/11-security-and-prompt-injection.md))
- **YOLO mode**: Running an agent with permission prompts turned off. ([08](../modules/08-agentic-workflows.md))

## Z

- **Zero data retention (ZDR)**: A contractual arrangement in which the provider does not store prompts or outputs after processing. ([12](../modules/12-costs-subscriptions-and-apis.md))

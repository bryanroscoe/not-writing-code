# Papers: an annotated reading list

*Last checked November 8, 2026. 180+ papers cited across the modules, grouped by the module that cites them first.*

Research papers are the slowest-moving layer of this field. Product names churn monthly; a good paper stays useful for years. You don't need to read them all. Start with the short list below, read the abstract and figures first, and come back to the full lists by topic.

**How to read an ML paper in 20 minutes:** abstract → the main figure or table → the conclusion → the limitations section. Only then the method. Ask an AI assistant to explain any term you don't know, but check its explanation against the paper; it's a good exercise in [verifying model output](../modules/05-judging-models.md).

## Start here: eighteen papers that explain the field

| # | Paper | Why it matters | Module |
| --- | --- | --- | --- |
| 1 | [Attention Is All You Need](https://arxiv.org/abs/1706.03762) (Vaswani et al., 2017) | Introduced the transformer, the architecture behind every model in this course. | [01](../modules/01-what-is-an-llm.md) |
| 2 | [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) (Brown et al., 2020) | GPT-3: scale alone made a model that learns new tasks from a few examples in its prompt. | [01](../modules/01-what-is-an-llm.md) |
| 3 | [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) (Kaplan et al., 2020) and [Training Compute-Optimal LLMs](https://arxiv.org/abs/2203.15556) (Hoffmann et al., 2022) | Why labs kept making models bigger, and how much data a model of a given size needs. | [01](../modules/01-what-is-an-llm.md) |
| 4 | [Training Language Models to Follow Instructions with Human Feedback](https://arxiv.org/abs/2203.02155) (Ouyang et al., 2022) | InstructGPT: how RLHF turned a text predictor into an assistant. The recipe behind ChatGPT. | [02](../modules/02-training-and-tuning.md) |
| 5 | [Chain-of-Thought Prompting Elicits Reasoning](https://arxiv.org/abs/2201.11903) (Wei et al., 2022) | Showing work in text improves answers. The seed of today's "thinking" models. | [01](../modules/01-what-is-an-llm.md) |
| 6 | [DeepSeek-R1](https://arxiv.org/abs/2501.12948) (DeepSeek-AI, 2025) | Reinforcement learning on checkable problems produces reasoning, in an open-weight model. | [02](../modules/02-training-and-tuning.md) |
| 7 | [LoRA: Low-Rank Adaptation](https://arxiv.org/abs/2106.09685) (Hu et al., 2021) | How to fine-tune a huge model by training a tiny add-on. The basis of most open-weight tuning. | [02](../modules/02-training-and-tuning.md) |
| 8 | [Self-Adapting Language Models](https://arxiv.org/abs/2506.10943) (Zweiger et al., 2025) | SEAL: a model that writes its own training data and updates its own weights. | [02](../modules/02-training-and-tuning.md) |
| 9 | [ReAct: Synergizing Reasoning and Acting](https://arxiv.org/abs/2210.03629) (Yao et al., 2022) | The think → act → observe loop that every coding agent runs. | [08](../modules/08-agentic-workflows.md) |
| 10 | [Lost in the Middle](https://arxiv.org/abs/2307.03172) (Liu et al., 2023) | Models use the start and end of long contexts better than the middle. Why context engineering exists. | [07](../modules/07-context-engineering.md) |
| 11 | [Evaluating AGENTS.md](https://arxiv.org/abs/2602.11988) (Gloaguen et al., 2026) | Tested whether repository instruction files help coding agents. They generally didn't improve task success and raised cost by over 20%. | [07](../modules/07-context-engineering.md) |
| 12 | [SWE-bench](https://arxiv.org/abs/2310.06770) (Jimenez et al., 2023) | Real GitHub issues as a coding benchmark. The template for how coding agents are measured. | [05](../modules/05-judging-models.md) |
| 13 | [Measuring AI Ability to Complete Long Tasks](https://arxiv.org/abs/2503.14499) (Kwa et al., 2025) | METR's "time horizon": the length of task an agent can finish, doubling every few months. | [05](../modules/05-judging-models.md) |
| 14 | [Measuring the Impact of Early-2025 AI on Experienced Developer Productivity](https://arxiv.org/abs/2507.09089) (Becker et al., 2025) | A randomized trial where developers were 19% *slower* with AI while believing they were faster. | [05](../modules/05-judging-models.md) |
| 15 | [Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657) (Cemri et al., 2025) | A taxonomy of how teams of agents break down. Read before building one. | [09](../modules/09-multi-agent-systems.md) |
| 16 | [LLM Critics Help Catch LLM Bugs](https://arxiv.org/abs/2407.00215) (McAleese et al., 2024) | CriticGPT: models reviewing code catch bugs humans miss, and also invent some. | [10](../modules/10-ai-code-review.md) |
| 17 | [Not what you've signed up for](https://arxiv.org/abs/2302.12173) (Greshake et al., 2023) | Indirect prompt injection: attacks hidden in content the model reads. | [11](../modules/11-security-and-prompt-injection.md) |
| 18 | [How AI Impacts Skill Formation](https://arxiv.org/abs/2601.20245) (Shen and Tamkin, 2026) | A randomized trial: developers who leaned on AI learned a new library less well. | [15](../modules/15-learning-careers-and-responsibility.md) |

## Every paper, by topic

Each list below is copied from the "Sources and further reading" section of the module named in the heading. "Also cited in" shows where else a paper comes up.

<!-- BEGIN GENERATED: edit the modules, then run python3 scripts/build_reference.py -->

## 01: What is an LLM?

[Module 01](../modules/01-what-is-an-llm.md)

- [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781) (Mikolov et al., 2013)
- [Sequence to Sequence Learning with Neural Networks](https://arxiv.org/abs/1409.3215) (Sutskever, Vinyals, Le, 2014)
- [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473) (Bahdanau, Cho, Bengio, 2014)
- [Neural Machine Translation of Rare Words with Subword Units](https://arxiv.org/abs/1508.07909) (Sennrich, Haddow, Birch, 2016)
- [Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer](https://arxiv.org/abs/1701.06538) (Shazeer et al., 2017) · also cited in [04](../modules/04-open-vs-closed-weights.md)
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) (Vaswani et al., 2017)
- [Deep Reinforcement Learning from Human Preferences](https://arxiv.org/abs/1706.03741) (Christiano et al., 2017)
- [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805) (Devlin et al., 2018)
- [The Curious Case of Neural Text Degeneration](https://arxiv.org/abs/1904.09751) (Holtzman et al., 2019)
- [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) (Kaplan et al., 2020)
- [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) (Brown et al., 2020), GPT-3 · also cited in [07](../modules/07-context-engineering.md)
- [Switch Transformers](https://arxiv.org/abs/2101.03961) (Fedus, Zoph, Shazeer, 2021) · also cited in [04](../modules/04-open-vs-closed-weights.md)
- [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020) (Radford et al., 2021), CLIP
- [Finetuned Language Models Are Zero-Shot Learners](https://arxiv.org/abs/2109.01652) (Wei et al., 2021), FLAN
- [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903) (Wei et al., 2022) · also cited in [07](../modules/07-context-engineering.md)
- [Training Language Models to Follow Instructions with Human Feedback](https://arxiv.org/abs/2203.02155) (Ouyang et al., 2022), InstructGPT · also cited in [02](../modules/02-training-and-tuning.md)
- [Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://arxiv.org/abs/2203.11171) (Wang et al., 2022) · also cited in [09](../modules/09-multi-agent-systems.md)
- [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) (Hoffmann et al., 2022), Chinchilla
- [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916) (Kojima et al., 2022)
- [Emergent Abilities of Large Language Models](https://arxiv.org/abs/2206.07682) (Wei et al., 2022)
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) (Yao et al., 2022) · also cited in [06](../modules/06-harnesses-and-tools.md), [08](../modules/08-agentic-workflows.md), [09](../modules/09-multi-agent-systems.md)
- [Emergent World Representations: Exploring a Sequence Model Trained on a Synthetic Task](https://arxiv.org/abs/2210.13382) (Li et al., 2022), Othello-GPT
- [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073) (Bai et al., 2022) · also cited in [02](../modules/02-training-and-tuning.md)
- [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) (Schick et al., 2023)
- [GPT-4 Technical Report](https://arxiv.org/abs/2303.08774) (OpenAI, 2023)
- [Are Emergent Abilities of Large Language Models a Mirage?](https://arxiv.org/abs/2304.15004) (Schaeffer, Miranda, Koyejo, 2023)
- [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) (Liu et al., 2023) · also cited in [07](../modules/07-context-engineering.md)
- [The Reversal Curse: LLMs trained on "A is B" fail to learn "B is A"](https://arxiv.org/abs/2309.12288) (Berglund et al., 2023)
- [Embers of Autoregression](https://arxiv.org/abs/2309.13638) (McCoy et al., 2023)
- [Language Models Represent Space and Time](https://arxiv.org/abs/2310.02207) (Gurnee and Tegmark, 2023)
- [Towards Understanding Sycophancy in Language Models](https://arxiv.org/abs/2310.13548) (Sharma et al., 2023) · also cited in [08](../modules/08-agentic-workflows.md)
- [Mixtral of Experts](https://arxiv.org/abs/2401.04088) (Jiang et al., 2024)
- [The Llama 3 Herd of Models](https://arxiv.org/abs/2407.21783) (Grattafiori et al., 2024) · also cited in [02](../modules/02-training-and-tuning.md)
- [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](https://arxiv.org/abs/2408.03314) (Snell et al., 2024)
- [GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models](https://arxiv.org/abs/2410.05229) (Mirzadeh et al., 2024)
- [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437) (DeepSeek-AI, 2024) · also cited in [02](../modules/02-training-and-tuning.md)
- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948) (DeepSeek-AI, 2025); peer-reviewed version in [Nature](https://www.nature.com/articles/s41586-025-09422-z) · also cited in [02](../modules/02-training-and-tuning.md)
- [Reasoning Models Don't Always Say What They Think](https://arxiv.org/abs/2505.05410) (Chen et al., 2025)
- [The Illusion of Thinking](https://arxiv.org/abs/2506.06941) (Shojaee et al., 2025) and the [comment by Lawsen](https://arxiv.org/abs/2506.09250) (2025)
- [Why Language Models Hallucinate](https://arxiv.org/abs/2509.04664) (Kalai, Nachum, Vempala, Zhang, 2025)

## 02: How models are trained, tuned, and now tune themselves

[Module 02](../modules/02-training-and-tuning.md)

- [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531) (Hinton, Vinyals, Dean, 2015) · also cited in [04](../modules/04-open-vs-closed-weights.md)
- [Overcoming Catastrophic Forgetting in Neural Networks](https://arxiv.org/abs/1612.00796) (Kirkpatrick et al., 2017)
- [Parameter-Efficient Transfer Learning for NLP](https://arxiv.org/abs/1902.00751) (Houlsby et al., 2019)
- [Test-Time Training with Self-Supervision for Generalization under Distribution Shifts](https://arxiv.org/abs/1909.13231) (Sun et al., 2020)
- [The Power of Scale for Parameter-Efficient Prompt Tuning](https://arxiv.org/abs/2104.08691) (Lester, Al-Rfou, Constant, 2021)
- [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685) (Hu et al., 2021) · also cited in [04](../modules/04-open-vs-closed-weights.md)
- [STaR: Bootstrapping Reasoning With Reasoning](https://arxiv.org/abs/2203.14465) (Zelikman et al., 2022)
- [GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers](https://arxiv.org/abs/2210.17323) (Frantar et al., 2022) · also cited in [04](../modules/04-open-vs-closed-weights.md)
- [Self-Instruct: Aligning Language Models with Self-Generated Instructions](https://arxiv.org/abs/2212.10560) (Wang et al., 2022)
- [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314) (Dettmers et al., 2023) · also cited in [04](../modules/04-open-vs-closed-weights.md)
- [The Curse of Recursion: Training on Generated Data Makes Models Forget](https://arxiv.org/abs/2305.17493) (Shumailov et al., 2023); published as [AI models collapse when trained on recursively generated data](https://www.nature.com/articles/s41586-024-07566-y) (Nature, 2024)
- [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290) (Rafailov et al., 2023)
- [AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration](https://arxiv.org/abs/2306.00978) (Lin et al., 2023)
- [Textbooks Are All You Need](https://arxiv.org/abs/2306.11644) (Gunasekar et al., 2023)
- [RLAIF vs. RLHF: Scaling Reinforcement Learning from Human Feedback with AI Feedback](https://arxiv.org/abs/2309.00267) (Lee et al., 2023)
- [Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!](https://arxiv.org/abs/2310.03693) (Qi et al., 2023)
- [LoRA Fine-tuning Efficiently Undoes Safety Training in Llama 2-Chat 70B](https://arxiv.org/abs/2310.20624) (Lermen, Rogers-Smith, Ladish, 2023) · also cited in [04](../modules/04-open-vs-closed-weights.md)
- [Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs](https://arxiv.org/abs/2312.05934) (Ovadia et al., 2023)
- [Self-Rewarding Language Models](https://arxiv.org/abs/2401.10020) (Yuan et al., 2024)
- [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://arxiv.org/abs/2402.03300) (Shao et al., 2024), introduces GRPO
- [Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data](https://arxiv.org/abs/2404.01413) (Gerstgrasser et al., 2024)
- [Does Fine-Tuning LLMs on New Knowledge Encourage Hallucinations?](https://arxiv.org/abs/2405.05904) (Gekhman et al., 2024)
- [LoRA Learns Less and Forgets Less](https://arxiv.org/abs/2405.09673) (Biderman et al., 2024)
- [The Rising Costs of Training Frontier AI Models](https://arxiv.org/abs/2405.21015) (Cottier et al., 2024)
- [Refusal in Language Models Is Mediated by a Single Direction](https://arxiv.org/abs/2406.11717) (Arditi et al., 2024) · also cited in [04](../modules/04-open-vs-closed-weights.md)
- [The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale](https://arxiv.org/abs/2406.17557) (Penedo et al., 2024)
- [Learning to (Learn at Test Time): RNNs with Expressive Hidden States](https://arxiv.org/abs/2407.04620) (Sun et al., 2024)
- [The Surprising Effectiveness of Test-Time Training for Few-Shot Learning](https://arxiv.org/abs/2411.07279) (Akyürek et al., 2024)
- [Tülu 3: Pushing Frontiers in Open Language Model Post-Training](https://arxiv.org/abs/2411.15124) (Lambert et al., 2024), names RLVR
- [Deliberative Alignment: Reasoning Enables Safer Language Models](https://arxiv.org/abs/2412.16339) (Guan et al., 2024)
- [Titans: Learning to Memorize at Test Time](https://arxiv.org/abs/2501.00663) (Behrouz, Zhong, Mirrokni, 2024)
- [Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming](https://arxiv.org/abs/2501.18837) (Sharma et al., 2025)
- [Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs](https://arxiv.org/abs/2502.17424) (Betley et al., 2025); extended version in [Nature](https://www.nature.com/articles/s41586-025-09937-5) (2026)
- [SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution](https://arxiv.org/abs/2502.18449) (Wei et al., 2025)
- [Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation](https://arxiv.org/abs/2503.11926) (Baker et al., 2025)
- [Absolute Zero: Reinforced Self-play Reasoning with Zero Data](https://arxiv.org/abs/2505.03335) (Zhao et al., 2025)
- [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388) (Yang et al., 2025)
- [Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents](https://arxiv.org/abs/2505.22954) (Zhang et al., 2025)
- [Self-Adapting Language Models](https://arxiv.org/abs/2506.10943) (Zweiger et al., 2025), SEAL
- [AlphaEvolve: A coding agent for scientific and algorithmic discovery](https://arxiv.org/abs/2506.13131) (Novikov et al., 2025)
- [Persona Features Control Emergent Misalignment](https://arxiv.org/abs/2506.19823) (Wang et al., 2025)
- [Poisoning Attacks on LLMs Require a Near-constant Number of Poison Samples](https://arxiv.org/abs/2510.07192) (Souly et al., 2025)
- [Natural Emergent Misalignment from Reward Hacking in Production RL](https://arxiv.org/abs/2511.18397) (MacDiarmid et al., 2025)
- [End-to-End Test-Time Training for Long Context](https://arxiv.org/abs/2512.23675) (Tandon et al., 2025)
- [Nested Learning: The Illusion of Deep Learning Architectures](https://arxiv.org/abs/2512.24695) (Behrouz, Razaviyayn, Zhong, Mirrokni, 2025)
- [Self-Distillation Enables Continual Learning](https://arxiv.org/abs/2601.19897) (Shenfeld, Damani, Hübotter, Agrawal, 2026), SDFT
- [SIA: Self Improving AI with Harness & Weight Updates](https://arxiv.org/abs/2605.27276) (Hebbar et al., 2026)
- [Language Models Need Sleep: Learning to Self-Modify and Consolidate Memories](https://arxiv.org/abs/2606.03979) (Behrouz, Hashemi, Javanmard, Mirrokni, 2026), the sleep framework
- [Recursive self-improvement of AI research agents](https://arxiv.org/abs/2609.26457) (Srikanth et al., 2026), AIDE²

## 03: The model landscape

[Module 03](../modules/03-model-landscape.md)

- [The Leaderboard Illusion](https://arxiv.org/abs/2504.20879) (Singh et al., 2025) · also cited in [05](../modules/05-judging-models.md), [14](../modules/14-keeping-up.md)

## 04: Open weight vs closed weight

[Module 04](../modules/04-open-vs-closed-weights.md)

- [LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale](https://arxiv.org/abs/2208.07339) (Dettmers et al., 2022)
- [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180) (Kwon et al., 2023) · also cited in [13](../modules/13-open-source-ecosystem.md)
- [SGLang: Efficient Execution of Structured Language Model Programs](https://arxiv.org/abs/2312.07104) (Zheng et al., 2023) · also cited in [13](../modules/13-open-source-ecosystem.md)
- [BadLlama: cheaply removing safety fine-tuning from Llama 2-Chat 13B](https://arxiv.org/abs/2311.00117) (Gade et al., 2023)

## 05: How to tell if a model is good

[Module 05](../modules/05-judging-models.md)

- [Evaluating Large Language Models Trained on Code](https://arxiv.org/abs/2107.03374) (Chen et al., 2021): HumanEval and pass@k · also cited in [06](../modules/06-harnesses-and-tools.md)
- [Program Synthesis with Large Language Models](https://arxiv.org/abs/2108.07732) (Austin et al., 2021): MBPP
- [Measuring Massive Multitask Language Understanding](https://arxiv.org/abs/2009.03300) (Hendrycks et al., 2020): MMLU
- [MMLU-Pro](https://arxiv.org/abs/2406.01574) (Wang et al., 2024)
- [Are We Done with MMLU?](https://arxiv.org/abs/2406.04127) (Gema et al., 2024)
- [GPQA: A Graduate-Level Google-Proof Q&A Benchmark](https://arxiv.org/abs/2311.12022) (Rein et al., 2023)
- [Humanity's Last Exam](https://arxiv.org/abs/2501.14249) (Phan et al., 2025)
- [FrontierMath](https://arxiv.org/abs/2411.04872) (Glazer et al., 2024)
- [On the Measure of Intelligence](https://arxiv.org/abs/1911.01547) (Chollet, 2019): ARC
- [ARC-AGI-2: A New Challenge for Frontier AI Reasoning Systems](https://arxiv.org/abs/2505.11831) (Chollet et al., 2025)
- [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770) (Jimenez et al., 2023) · also cited in [13](../modules/13-open-source-ecosystem.md)
- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793) (Yang et al., 2024) · also cited in [06](../modules/06-harnesses-and-tools.md), [08](../modules/08-agentic-workflows.md)
- [The SWE-Bench Illusion](https://arxiv.org/abs/2506.12286) (Liang et al., 2025)
- [SWE-Bench Pro](https://arxiv.org/abs/2509.16941) (Deng et al., 2025)
- [Terminal-Bench](https://arxiv.org/abs/2601.11868) (Merrill et al., 2026) · also cited in [14](../modules/14-keeping-up.md)
- [LiveCodeBench](https://arxiv.org/abs/2403.07974) (Jain et al., 2024)
- [SWE-Lancer](https://arxiv.org/abs/2502.12115) (Miserendino et al., 2025)
- [τ-bench](https://arxiv.org/abs/2406.12045) (Yao et al., 2024) and [τ²-bench](https://arxiv.org/abs/2506.07982) (Barres et al., 2025)
- [OSWorld](https://arxiv.org/abs/2404.07972) (Xie et al., 2024)
- [GAIA](https://arxiv.org/abs/2311.12983) (Mialon et al., 2023)
- [BrowseComp](https://arxiv.org/abs/2504.12516) (Wei et al., 2025)
- [GDPval](https://arxiv.org/abs/2510.04374) (Patwardhan et al., 2025)
- [Measuring AI Ability to Complete Long Tasks](https://arxiv.org/abs/2503.14499) (Kwa, West, Becker et al., 2025) · also cited in [08](../modules/08-agentic-workflows.md), [14](../modules/14-keeping-up.md)
- [Chatbot Arena](https://arxiv.org/abs/2403.04132) (Chiang et al., 2024)
- [LiveBench](https://arxiv.org/abs/2406.19314) (White et al., 2024)
- [A Careful Examination of LLM Performance on Grade School Arithmetic](https://arxiv.org/abs/2405.00332) (Zhang et al., 2024): GSM1k
- [Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design](https://arxiv.org/abs/2310.11324) (Sclar et al., 2023)
- [Adding Error Bars to Evals](https://arxiv.org/abs/2411.00640) (Miller, 2024)
- [How Inference Compute Shapes Frontier LLM Evaluation](https://arxiv.org/abs/2606.17930) (McFadyen et al., 2026)
- [The Impact of AI on Developer Productivity: Evidence from GitHub Copilot](https://arxiv.org/abs/2302.06590) (Peng et al., 2023)
- [How Much Does AI Impact Development Speed? An Enterprise-Based RCT](https://arxiv.org/abs/2410.12944) (Paradis et al., 2024)
- [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://arxiv.org/abs/2507.09089) (Becker, Rush, Barnes, Rein, 2025) · also cited in [08](../modules/08-agentic-workflows.md), [12](../modules/12-costs-subscriptions-and-apis.md), [14](../modules/14-keeping-up.md), [15](../modules/15-learning-careers-and-responsibility.md)

## 06: Harnesses, tools, and MCP

[Module 06](../modules/06-harnesses-and-tools.md)

- [Model Context Protocol (MCP): Landscape, Security Threats, and Future Research Directions](https://arxiv.org/abs/2503.23278) (Hou et al., 2025).

## 07: From prompt engineering to context, loop, and graph engineering

[Module 07](../modules/07-context-engineering.md)

- [RULER: What's the Real Context Size of Your Long-Context Language Models?](https://arxiv.org/abs/2404.06654) (Hsieh et al., 2024).
- [The Prompt Report: A Systematic Survey of Prompt Engineering Techniques](https://arxiv.org/abs/2406.06608) (Schulhoff et al., 2024).
- [NoLiMa: Long-Context Evaluation Beyond Literal Matching](https://arxiv.org/abs/2502.05167) (Modarressi et al., 2025).
- [How Many Instructions Can LLMs Follow at Once?](https://arxiv.org/abs/2507.11538) (Jaroslawicz et al., 2025).
- [On the Use of Agentic Coding Manifests: An Empirical Study of Claude Code](https://arxiv.org/abs/2509.14744) (Chatlatanagulchai et al., 2025).
- [Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models](https://arxiv.org/abs/2510.04618) (Zhang et al., 2025).
- [Agent READMEs: An Empirical Study of Context Files for Agentic Coding](https://arxiv.org/abs/2511.12884) (Chatlatanagulchai et al., 2025).
- [Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?](https://arxiv.org/abs/2602.11988) (Gloaguen et al., 2026).
- [Graph Engineering in the Era of LLM Agents: From Individual Intelligence to System Intelligence](https://arxiv.org/abs/2608.21156) (Feng et al., 2026).

## 08: Agentic workflows: how much autonomy actually works

[Module 08](../modules/08-agentic-workflows.md)

- [ImpossibleBench: Measuring LLMs' Propensity of Exploiting Test Cases](https://arxiv.org/abs/2510.20270) (Zhong et al., 2025)
- [We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs](https://arxiv.org/abs/2406.10279) (Spracklen et al., 2024; USENIX Security 2025) · also cited in [10](../modules/10-ai-code-review.md), [11](../modules/11-security-and-prompt-injection.md)
- [Solving a Million-Step LLM Task with Zero Errors](https://arxiv.org/abs/2511.09030) (Meyerson et al., 2025) · also cited in [09](../modules/09-multi-agent-systems.md)

## 09: Multiple agents building and reviewing

[Module 09](../modules/09-multi-agent-systems.md)

- [CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society](https://arxiv.org/abs/2303.17760) (Li et al., 2023)
- [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) (Park et al., 2023)
- [Improving Factuality and Reasoning in Language Models through Multiagent Debate](https://arxiv.org/abs/2305.14325) (Du et al., 2023)
- [Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate](https://arxiv.org/abs/2305.19118) (Liang et al., 2023)
- [MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework](https://arxiv.org/abs/2308.00352) (Hong et al., 2023)
- [ChatDev: Communicative Agents for Software Development](https://arxiv.org/abs/2307.07924) (Qian et al., 2023)
- [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155) (Wu et al., 2023) · also cited in [13](../modules/13-open-source-ecosystem.md)
- [AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors](https://arxiv.org/abs/2308.10848) (Chen et al., 2023)
- [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651) (Madaan et al., 2023)
- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) (Shinn et al., 2023)
- [Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/abs/2310.01798) (Huang et al., 2023)
- [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) (Zheng et al., 2023) · also cited in [10](../modules/10-ai-code-review.md)
- [Large Language Models are not Fair Evaluators](https://arxiv.org/abs/2305.17926) (Wang et al., 2023)
- [More Agents Is All You Need](https://arxiv.org/abs/2402.05120) (Li et al., 2024)
- [Mixture-of-Agents Enhances Large Language Model Capabilities](https://arxiv.org/abs/2406.04692) (Wang et al., 2024)
- [LLM Evaluators Recognize and Favor Their Own Generations](https://arxiv.org/abs/2404.13076) (Panickssery et al., 2024) · also cited in [10](../modules/10-ai-code-review.md)
- [Self-Preference Bias in LLM-as-a-Judge](https://arxiv.org/abs/2410.21819) (Wataoka et al., 2024) · also cited in [10](../modules/10-ai-code-review.md)
- [Replacing Judges with Juries: Evaluating LLM Generations with a Panel of Diverse Models](https://arxiv.org/abs/2404.18796) (Verga et al., 2024) · also cited in [10](../modules/10-ai-code-review.md)
- [Agent-as-a-Judge: Evaluate Agents with Agents](https://arxiv.org/abs/2410.10934) (Zhuge et al., 2024)
- [LLM Critics Help Catch LLM Bugs](https://arxiv.org/abs/2407.00215) (McAleese et al., 2024) · also cited in [10](../modules/10-ai-code-review.md)
- [Agentless: Demystifying LLM-based Software Engineering Agents](https://arxiv.org/abs/2407.01489) (Xia et al., 2024)
- [AI Agents That Matter](https://arxiv.org/abs/2407.01502) (Kapoor et al., 2024)
- [Rethinking Mixture-of-Agents: Is Mixing Different Large Language Models Beneficial?](https://arxiv.org/abs/2502.00674) (Li et al., 2025)
- [Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657) (Cemri et al., 2025)
- [Single-agent or Multi-agent Systems? Why Not Both?](https://arxiv.org/abs/2505.18286) (Gao et al., 2025)
- [Debate or Vote: Which Yields Better Decisions in Multi-Agent Large Language Models?](https://arxiv.org/abs/2508.17536) (Choi et al., 2025)
- [Talk Isn't Always Cheap: Understanding Failure Modes in Multi-Agent Debate](https://arxiv.org/abs/2509.05396) (Wynn et al., 2025)
- [Towards a Science of Scaling Agent Systems](https://arxiv.org/abs/2512.08296) (Kim et al., 2025; revised April 2026)

## 10: AI code review

[Module 10](../modules/10-ai-code-review.md)

- [AI-Assisted Assessment of Coding Practices in Modern Code Review](https://arxiv.org/abs/2405.13565) (Vijayvergiya et al., 2024)
- [Automated Code Review In Practice](https://arxiv.org/abs/2412.18531) (Cihan et al., 2024; ICSE 2025 SEIP)
- [Rethinking Code Review Workflows with LLM Assistance: An Empirical Study](https://arxiv.org/abs/2505.16339) (Aðalsteinsson et al., 2025)
- [Does AI Code Review Lead to Code Changes? A Case Study of GitHub Actions](https://arxiv.org/abs/2508.18771) (Sun et al., 2025)
- [RovoDev Code Reviewer: A Large-Scale Online Evaluation of LLM-based Code Review Automation at Atlassian](https://arxiv.org/abs/2601.01129) (Tantithamthavorn et al., 2026; ICSE 2026 SEIP)
- [Asleep at the Keyboard? Assessing the Security of GitHub Copilot's Code Contributions](https://arxiv.org/abs/2108.09293) (Pearce et al., 2021) · also cited in [11](../modules/11-security-and-prompt-injection.md)

## 11: Security and prompt injection

[Module 11](../modules/11-security-and-prompt-injection.md)

- [Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173) (Greshake, Abdelnabi, Mishra, Endres, Holz, Fritz, 2023)
- [The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections](https://arxiv.org/abs/2510.09023) (Nasr, Carlini, et al., 2025)
- [Defeating Prompt Injections by Design](https://arxiv.org/abs/2503.18813) (Debenedetti et al., 2025), the CaMeL paper
- [Design Patterns for Securing LLM Agents against Prompt Injections](https://arxiv.org/abs/2506.08837) (Beurer-Kellner, Tramèr, et al., 2025)
- [The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions](https://arxiv.org/abs/2404.13208) (Wallace, Xiao, Leike, Weng, Heidecke, Beutel, 2024)
- [Do Users Write More Insecure Code with AI Assistants?](https://arxiv.org/abs/2211.03622) (Perry, Srivastava, Kumar, Boneh, 2022) · also cited in [15](../modules/15-learning-careers-and-responsibility.md)
- [BaxBench: Can LLMs Generate Correct and Secure Backends?](https://arxiv.org/abs/2502.11844) (Vero et al., 2025)

## 13: The open-source ecosystem

[Module 13](../modules/13-open-source-ecosystem.md)

- [DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines](https://arxiv.org/abs/2310.03714) (Khattab et al., 2023).
- [OpenHands: An Open Platform for AI Software Developers as Generalist Agents](https://arxiv.org/abs/2407.16741) (Wang et al., 2024).

## 15: Learning, careers, and responsible use

[Module 15](../modules/15-learning-careers-and-responsibility.md)

- [How AI Impacts Skill Formation](https://arxiv.org/abs/2601.20245) (Shen, Tamkin, 2026)
- [Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task](https://arxiv.org/abs/2506.08872) (Kosmyna et al., 2025)
- [Measuring the environmental impact of delivering AI at Google Scale](https://arxiv.org/abs/2508.15734) (Elsworth et al., 2025)

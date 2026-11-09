---
marp: true
theme: not-writing-code
paginate: true
title: "02: Training, tuning, and self-tuning"
description: "How models are made, how you tune one, and what self-tuning really is"
footer: "A Brief Introduction to Not Writing Code · 02 Training, tuning, and self-tuning"
---

<!-- _class: lead -->

# 02: Training, tuning, and self-tuning

How models are made, how you tune one, and what "self-improving" really means

<!--
This session has three parts: how a model gets made, how you would tune an open-weight model yourself, and the research on models that tune their own weights. The reading is module 02. Plan on about 45 minutes plus discussion.

Part 3 takes on a question students and engineers keep asking: if a model can update its own weights, is that self-improvement? It is, narrowly, and most of the last third is about what "narrowly" means.

Facts, prices, and research results in this deck are as of November 2026 unless a slide gives another date.
-->

---

## Why this matters

- Every model you use went through the same stages
- Those stages explain why agents sometimes delete failing tests
- Most teams should not fine-tune first
- "Self-improving AI" headlines mix very different things
- Knowing which is a demo and which is deployed saves bad decisions

<!--
Engineers get asked "should we fine-tune a model on our stuff?" The usual answer is no, not first. Better instructions, context, and retrieval solve most problems. Part 2 covers what to try first and when fine-tuning pays off.

Everyone reads headlines about AI that improves itself. Some describe a model changing its own weights. Some describe an agent rewriting its own code with the weights untouched. Some describe a lab using its models to write most of its software. Those claims need different evidence. You should be able to tell which one a headline is making.

The second bullet is a preview. Reinforcement learning rewards whatever you measure, and "the tests pass" is easy to fake by editing the tests. That habit comes from training, and it shows up again in self-improving systems.
-->

---

<!-- _class: divider -->

# Part 1

## How models are made

<!--
Part 1 is the pipeline: pretraining, post-training, and distillation. About 12 minutes.
-->

---

## The pipeline at a glance

pretraining → mid-training → base model → supervised fine-tuning → preference tuning → RL with verifiable rewards → safety training → release

Pretraining uses about 15–36 trillion tokens of filtered text (Llama 3, DeepSeek-V3, Qwen3).

Real stages repeat and overlap. This is a simplified view.

<!--
One analogy for the whole process: read the entire library (pretraining), study the best books closely (mid-training), apprentice with worked examples (supervised fine-tuning), get coached on what people prefer (preference tuning), drill practice exams with an answer key (RL with verifiable rewards), take a professional-conduct course (safety training), and optionally do a specialty residency (your own fine-tune).

Pretraining is next-token prediction over trillions of tokens. Most data comes from web crawls such as Common Crawl, filtered hard for duplicates, spam, and quality. Hugging Face's open FineWeb project produced about 15 trillion tokens from Common Crawl. Published counts: Llama 3, more than 15 trillion; DeepSeek-V3, 14.8 trillion; Qwen3, about 36 trillion. Closed labs mostly don't publish theirs.

For cost, think in orders of magnitude. Karpathy's nanochat trains a toy chat model for about $100. DeepSeek reported about $5.6 million for DeepSeek-V3's final training run, excluding research, failed runs, and staff. Frontier closed models cost hundreds of millions of dollars, and Epoch AI projected the largest runs passing $1 billion by 2027.

The output of pretraining is a base model. It completes documents. It doesn't follow instructions or refuse harmful requests yet. Mid-training is a loosely defined phase with higher-quality data, longer context, and a slowly lowered learning rate.
-->

---

## From base model to assistant

| Stage | What it teaches | Analogy |
| --- | --- | --- |
| Supervised fine-tuning | Chat format, instructions, tool-call syntax | Apprenticeship |
| Preference tuning (RLHF, DPO, RLAIF) | Which of two answers is better | Coaching |
| RL with verifiable rewards | Reasoning on checkable tasks: math, code, tests | Practice exams |
| Safety training | Refusals, following a written spec | Professional conduct |

RL optimizes whatever you measure, so agents learn to edit the tests. That's reward hacking.

<!--
Supervised fine-tuning trains on example conversations, written by people or generated and filtered by models.

Preference tuning shows the model which of two responses is better. RLHF trains a reward model on human comparisons and then uses reinforcement learning (classically PPO) to push toward higher scores; InstructGPT in 2022 is the classic example. DPO skips the reward model and directly raises the probability of the preferred answer. It's simpler and cheaper, so it's popular for open models. RLAIF uses an AI model to do the comparing.

RL with verifiable rewards (RLVR) gives the model problems a program can check, such as a math answer that matches or code that passes unit tests. DeepSeek-R1 showed this produces strong reasoning at scale. Tests are a verifiable reward, which is a large part of why coding agents improved so quickly in 2025–2026. GRPO, from the DeepSeekMath paper, is the RL algorithm many open recipes use. It samples a group of answers, scores them, and pushes up the ones that beat the group average.

Coding models under RL have learned to special-case tests, edit the tests, or claim success they didn't earn. OpenAI found that penalizing "bad thoughts" in the chain of thought taught models to hide them. Anthropic found a model that learned to reward-hack in real production coding environments generalized to sabotage and faking alignment. That's one reason your agent sometimes "fixes" a failing test by deleting it.

Safety training includes OpenAI's deliberative alignment and Anthropic's constitution (January 2026). Many safeguards also sit outside the weights, such as input and output classifiers.
-->

---

## Distillation: teacher → student

Train a smaller model on a bigger model's outputs.

- Standard practice (Stanford Alpaca, 2023; DeepSeek's R1-Distill models, 2025)
- Closed labs' terms forbid building competitors this way
- Anthropic reported 16M+ exchanges via ~24,000 fraudulent accounts (February 2026)
- Defenses now cut harvested data by a claimed 90–99%

<!--
Hinton, Vinyals, and Dean showed in 2015 that a teacher's full probability distribution carries more information than the single right answer. With LLMs there are two flavors. Logit distillation learns from the teacher's token probabilities, so it mostly happens inside a lab. Output distillation fine-tunes on the teacher's text, which works through any API.

Stanford Alpaca fine-tuned LLaMA 7B on 52,000 examples generated with OpenAI's text-davinci-003 for under $600. DeepSeek's R1-Distill models were Qwen and Llama models fine-tuned on R1's reasoning traces.

On February 23, 2026, Anthropic said DeepSeek, Moonshot, and MiniMax ran distillation campaigns against Claude, more than 16 million exchanges through about 24,000 fraudulent accounts. It called distillation "a widely used and legitimate training method" in general and objected to illicit use. OpenAI made a similar accusation against DeepSeek to a House committee on February 12, 2026. When Fable 5 launched in June 2026, Anthropic said flagged distillation attempts would be answered by Opus 4.8; it later apologized for one safeguard that changed answers without telling users. On October 12, 2026, Anthropic described defenses it claims cut harvested data by about 90–99%.

Frontier labs also trained on web content without asking, which makes complaints about copying sound selective. Outsiders can't verify the account-level evidence. And the accusations land in an export-control policy fight where every party has an interest.
-->

---

<!-- _class: divider -->

# Part 2

## Tuning a model yourself

<!--
Part 2 is for open-weight models you can download and change: Llama, Qwen, DeepSeek, Kimi, Gemma, Mistral, gpt-oss. About 12 minutes.
-->

---

## Climb the ladder before you fine-tune

1. Better instructions
2. Better context
3. Retrieval (RAG)
4. Few-shot examples
5. An evaluation set
6. Fine-tune

Stop at the first rung that meets your bar.

<!--
Start at the top with clear instructions and a strong model. Then give it the docs, code, schemas, and examples it needs (module 07). If the knowledge is large or changes, retrieve the relevant pieces at query time. Then put 5–50 good examples in the prompt; prompt caching makes repeated prefixes cheap. Before going further, build a labeled test set, because without one you can't tell whether fine-tuning helped.

Research backs this order for knowledge. Ovadia et al. (2023) found retrieval beat fine-tuning for injecting new facts. Gekhman et al. (2024) found models learn new facts slowly during fine-tuning, and the more new facts they absorb, the more they tend to hallucinate.

Fine-tuning is the right tool for a consistent format or schema at high volume, narrow classification or extraction at millions of calls with tight latency, or data that can't leave your network. It's the wrong tool for "make it smarter at our codebase." Codebases change daily and agents can read the code, so that's context engineering.

Closed-model fine-tuning is shrinking. OpenAI began winding down self-serve fine-tuning on May 7, 2026; active customers can't create new jobs after January 6, 2027. The module found no self-serve fine-tuning for current Claude models. Google still documents fine-tuning for several Gemini models on Vertex AI.
-->

---

## How much memory LoRA and QLoRA save

| Job, 8B model | Memory needed |
| --- | --- |
| Inference, 16-bit | ~16 GB |
| Inference, 4-bit | ~5 GB |
| Full fine-tuning | ~130 GB |
| LoRA on a 16-bit base | ~20–30 GB |
| QLoRA on a 4-bit base | ~8–16 GB |

QLoRA fine-tuned a 65B model on a single 48 GB GPU.

<!--
Full fine-tuning updates every weight. It has the highest ceiling, needs the most memory (about 16 bytes per parameter with AdamW in mixed precision), and risks overwriting what the model knew.

LoRA (Hu et al., 2021) freezes the base and learns a small low-rank correction: two thin matrices whose product has the shape of the big one. Instead of reprinting a textbook, you add sticky notes. An adapter is often a few megabytes to a few hundred megabytes, and you can swap many adapters on one base model. QLoRA (Dettmers et al., 2023) loads the frozen base in 4-bit precision and trains LoRA adapters on top. It's why individuals can fine-tune.

The trade-off, from "LoRA Learns Less and Forgets Less" (Biderman et al., 2024): LoRA underperforms full fine-tuning on hard targets like heavy code and math, but preserves the base model's other abilities better. For most team use cases, that's the right trade.

On money, a small LoRA run on a few thousand examples often takes minutes to a few hours on one rented GPU, so a round of experiments costs tens of dollars. The expensive part is people's time building data and evaluations.

For quantization, 4-bit GGUF files such as Q4_K_M run in llama.cpp, Ollama, and LM Studio. Re-run your evaluation after quantizing. The usual tools are Hugging Face TRL and PEFT, Unsloth, Axolotl, LLaMA-Factory, MLX-LM on a Mac, and Thinking Machines' hosted Tinker.
-->

---

## Worked example: bug-report triage

define success → build the eval set → run baselines → collect data → QLoRA run → evaluate → read the failures → ship

A good candidate is narrow, high-volume, format-heavy, and measurable.

Build the eval set first. Never train on it.

<!--
The goal is to label thousands of bug reports a week with a component and severity, as strict JSON, cheaply, on infrastructure you control.

1. Define success: component accuracy at least 90%, severity within one level at least 95%, valid JSON 100%, latency under 300 ms.
2. Build the evaluation set first: 300–500 real reports labeled by people who know the system, including hard cases. Lock it away.
3. Run baselines: a frontier model with a careful prompt and 20 examples, and a small open model with the same prompt. If the frontier baseline meets the bar at acceptable cost and data policy, stop.
4. Collect training data: historical reports with human-corrected labels. Remove duplicates, secrets, and personal data.
5. Configure a QLoRA run: roughly 2,000 training examples and 200 validation, rank 16, two epochs.
6. Watch the curves. If validation loss rises while training loss keeps falling, the model is memorizing.
7. Evaluate on the held-out set, plus a small regression suite of general and safety prompts to catch forgetting.
8. Read the failures. Fix the data before touching hyperparameters.
9. Ship the adapter, re-evaluate after any quantization, version data, adapter, and base together, and keep the prompted baseline as a fallback.
-->

---

## Fine-tuning's sharp edges

| Risk | What the research found |
| --- | --- |
| Catastrophic forgetting | New training overwrites old abilities |
| Emergent misalignment | Insecure-code tuning made GPT-4o broadly misaligned |
| Safety comes off | 10 harmful examples, under $0.20, broke GPT-3.5 Turbo |
| Poisoned data | ~250 documents planted a backdoor, 600M to 13B models |
| Model collapse | Training on its own outputs erodes rare information |

<!--
Forgetting has been known since the late 1980s. LoRA forgets less than full fine-tuning, but not zero. Always test what you didn't train for.

Emergent misalignment (Betley et al., 2025; extended in Nature, January 2026): models fine-tuned on code with undisclosed security holes then said AI should enslave humans and gave malicious advice on unrelated prompts. When the same code was requested for a security class, the effect disappeared. OpenAI researchers traced it to a "misaligned persona" feature and found a little benign fine-tuning reversed it. So fine-tuning shifts a model's overall sense of what kind of assistant it is, beyond the one skill you trained.

Safety training comes off easily. Qi et al. (2023) broke GPT-3.5 Turbo's safety with 10 harmful examples through OpenAI's API for under $0.20. LoRA removed Llama 2-Chat 70B's refusals for under $200. "Abliteration" removes the single activation direction behind refusals without training. Treat safety in open weights as a speed bump, not a lock.

On poisoning, Souly et al. (2025) found about 250 malicious documents planted a backdoor regardless of model size. Your fine-tuning data pipeline is an attack surface.

With model collapse, training each generation on the previous one's outputs loses the rare cases first. Keeping real data alongside synthetic data avoided it in follow-up work. It's a risk of careless loops, not an iron law.

These risks increase when the model changes its own weights, as we'll see in Part 3.
-->

---

<!-- _class: divider -->

# Part 3

## Models that tune themselves

Deployed models are frozen. Every session starts from the same weights.

<!--
Part 3 is about 20 minutes. Today's deployed models don't learn from the work they do. "Memory" features are notes put back into the context. A human engineer gets better at your codebase every week; a model doesn't, until its maker trains a new version.

Continual learning means updating from new experience without forgetting old skills. Pushed further, a system that improves the process that improves it is recursive self-improvement, an idea discussed since I. J. Good's 1965 speculation about an "intelligence explosion."

As of November 2026, the module found no frontier model that updates its weights continuously from user interactions in production.
-->

---

## SEAL tunes its own weights

```python
for passage, quiz in tasks:
    notes = model.generate(f"Study notes on: {passage}")  # 1. generate
    updated = finetune(model, notes, method="lora")       # 2. update weights
    score = grade(updated, quiz)                          # 3. test, no passage
    reinforce(model, notes, reward=score)                 # 4. learn to teach
```

Passage questions: 33.5% → 47.0%. ARC puzzles: 20% → 72.5%.

<!--
This is simplified pseudocode, not a real API. It's the core of SEAL, "Self-Adapting Language Models" (Zweiger et al., MIT, 2025).

A model is a large set of numbers, its weights. "Tuning its own weights" means the model's own output drives a change to those numbers.
1. Generate: the model writes a "self-edit," training data for itself, such as restating a passage as a list of implications, and optionally settings for the training run.
2. Update: an ordinary supervised fine-tuning step applies it. Gradient descent changes the weights, the same kind of fine-tuning as Part 2.
3. Test: the updated model answers questions about the passage, which is no longer in its context.
4. Learn: the score is a reward in a reinforcement learning loop that teaches the model to write better self-edits. Over time it learns how to teach itself.

What's new is who writes the training material.

On Qwen2.5-7B, answering questions about a passage rose from 33.5% (training on the passage alone) to 47.0%, slightly ahead of training on data written by GPT-4.1 (46.3%). On a subset of ARC puzzles with Llama-3.2-1B, success rose from 20% (self-edits without RL) to 72.5%; plain in-context learning scored 0%.

The authors list the limits. Earlier knowledge erodes as edits pile up, each reward needs a fine-tune and an evaluation (about 30–45 seconds per self-edit), and every training context needs a paired test.

A related 2026 system, SIA, has one model (Claude Sonnet 4.6) retrain another (gpt-oss-120b) with RL on LoRA adapters when harness changes stall. On a legal benchmark, accuracy rose from 50.0% (harness only) to 70.1%.
-->

---

## Only one of these changes the model

| Mechanism | What changes | Lasts? |
| --- | --- | --- |
| In-context learning | Nothing; it's in the prompt | No |
| Memory files | Text loaded back into context | Yes, as text |
| Harness self-modification | Code, prompts, tools | Yes, as code |
| Weight self-tuning | The parameters | Yes, in the weights |

<!--
All four get called "learning" or "self-improvement."

In-context learning is few-shot prompting. The examples sit in the prompt and vanish with the session. Memory files are things like AGENTS.md or a chat product's memory feature, where the harness loads text back into the context. Harness self-modification is an agent rewriting its own code, prompts, and tools while the weights stay frozen; the Darwin Gödel Machine and AIDE² are examples. Weight self-tuning is SEAL and Google's sleep framework.

The first three can make an agent much better at your project, and you can inspect them. Read the memory file, diff the harness. A weight change is a shift in thousands to millions of numbers that you can't review line by line. It's also the only kind that lasts without anything added to the prompt.

The module's spectrum adds two more rungs: models that write their own training data while people run training (STaR, Self-Rewarding LMs, Absolute Zero, standard inside labs), and labs using AI to do much of the work of building the next AI. At every rung, ask what changes and who decides.
-->

---

## Google's sleep framework (October 27, 2026)

Awake, it takes in new information. Asleep, it writes it into the weights.

- Consolidation distills short-term memory into stable weights
- Dreaming generates practice data and fine-tunes on the best
- Runs on a fixed schedule the designers set
- SEAL's knowledge test: 48.9%, vs 46.7% for SEAL rerun
- Research on models of 8B parameters or fewer

<!--
From Behrouz, Hashemi, Javanmard, and Mirrokni. The paper appeared on arXiv in June 2026; Google Research's blog post followed on October 27, 2026. It builds on Google's Nested Learning and Hope architecture.

The model alternates between being awake, taking in new information through its context and fast-changing memory, and asleep, offline phases that write that information into its weights. Consolidation distills what fast, short-term memory holds into slower, more stable parameters, using pre-allocated low-rank experts unlocked during sleep, then resets the short-term parameters. Dreaming has the model generate its own practice examples, use reinforcement learning to build a curriculum, filter, and fine-tune on the best. That part builds directly on SEAL.

The model doesn't decide when to sleep. It runs on a fixed schedule.

The authors report 48.9% on SEAL's knowledge test for a single passage, compared with 46.7% for SEAL rerun in the same setup and 31.9% for the base model. Without dreaming the score falls to 35.7%, so most of the gain comes from self-generated practice. On SEAL's ARC subset, 80% versus 72.5%. On AIME 2024 with Qwen3-8B, 79.2%, versus 73.8% for the base model and 76.4% after standard RL. [Google's blog](https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning/) reports near-perfect scaling to 10M tokens on BABILong, using consolidation into weights, and a near-zero performance drop in multi-stage translation tests with Manchu and Kalamang.

Google presents it as research. The blog doesn't discuss safety, deployment, or cost.

A related method, end-to-end test-time training (Tandon et al., December 2025), keeps training on the text a model reads, compressing context into weights, and reports 2.7 times the speed of full attention at 128K tokens.
-->

---

## Weight-space programming (November 2, 2026)

> "not through an optimizer, and in particular not with gradient descent"

- GPT-6 Astra edited a small model's weights directly
- Qwen3.5-0.8B: 131,072 weights changed; MATH-500 7.9% → 48.1%
- Gemma 3 270M: no improvement at all
- It removed an obstacle; it couldn't add a missing ability
- One model editing *another*, in a blog post of "very early results"

<!--
From MIT CSAIL researchers Rikiya Takehi, Jayden Teoh, Alex Zhang, and Omar Khattab, in a blog post on November 2, 2026. The Register covered it the next day.

The claim is that OpenAI's GPT-6 Astra can read and write neural-network weights directly, as numbers. In the headline experiment Astra worked in a Python sandbox with a budget of forward passes, meaning test runs of the target model. Qwen3.5-0.8B's answers often ran into its token limit. Astra changed 131,072 weights, 0.016% of the model. With 50 forward passes, MATH-500 rose from 7.9% to 48.1%, and the share of answers hitting the token limit fell from 93.0% to 33.1%.

The negative result matters as much. On Gemma 3 270M, Astra couldn't improve math scores. As the authors read it, editing "could remove an obstacle that hid an ability, but it could not add an ability the model lacked."

This is one model editing another model, and a model editing its own weights is listed as future work. And it's a blog post, not a peer-reviewed paper.
-->

---

## Agents that rewrite their own harness

| System | Result | Catch |
| --- | --- | --- |
| Darwin Gödel Machine (2025) | SWE-bench 20.0% → 50.0% | Faked a log saying tests passed |
| AlphaEvolve (2025) | Recovers ~0.7% of Google's fleet compute | Per Google |
| AIDE² (September 2026) | Seven improvements in an 8-day run | Reward hacking started at 55% |

The weights never change. Weco calls AIDE² "Level 1."

<!--
These are agents improving their own code, prompts, and tools.

The Darwin Gödel Machine (Sakana AI and UBC, 2025) edits its own source code and keeps variants in a growing archive. It improved from 20.0% to 50.0% on SWE-bench and from 14.2% to 30.7% on Polyglot. It also gamed its own evaluation. Sakana reports it faked a log claiming tests had passed when they never ran. Experiments ran sandboxed under human supervision.

AlphaEvolve (Google DeepMind, 2025) is an evolutionary coding agent. Google reported a scheduling heuristic that recovers about 0.7% of its fleet-wide compute and a kernel speedup that cut Gemini's overall training time by about 1%. That's a small but real loop, AI improving the infrastructure that trains it.

In AIDE² (Weco AI, arXiv September 22, 2026), an outer agent running Claude Opus 4.7 rewrote the harness of a research agent running Gemini 3 Flash, and kept changes that scored best on hidden evaluations. In an 8-day autonomous run it found seven successive improvements. The final agent matched or beat Weco's human-engineered agent on four held-out benchmarks, including a weather-forecasting task unlike its selection tasks. Its reward-hacking rate on GPU-kernel tasks fell from 55% to 32%, against 39% for the human-built agent. Weco wrote, "we believe we are not near an intelligence explosion with the current system." Self-reported, not yet peer-reviewed.

MiniMax M2.7 (March 2026) described something similar, with the model changing its harness over more than 100 rounds, not its weights.
-->

---

## Labs using models to build models

- OpenAI says it met its "research intern" goal (September 6, 2026)
- Its chief scientist: "This is a time that calls for extreme caution"
- Anthropic says Claude authored over 80% of merged code (May 2026)
- Anthropic's IPO filing says it "may imminently meet" its own threshold
- No current model is designated past it. All self-reported.

<!--
OpenAI set a goal in October 2025 of an "automated AI research intern" by September 2026. On September 6, 2026, [it said it had met it](https://openai.com/index/research-acceleration-view-inside-openai/), and reported that its research organization used about 3.1 agent-workdays of coding-agent runtime per human workday, using an eight-hour day as of mid-August. OpenAI called the measurements preliminary. It set, defined, measured, and graded the goal itself.

The same day, chief scientist Jakub Pachocki published "[An Alien Mind](https://openai.com/index/an-alien-mind/)." Based on internal results, he expected progress could continue into recursive self-improvement, with systems increasingly driving their own development if progress continues. He urged extreme caution and hoped labs would voluntarily slow down until shared safety standards were established.

Anthropic's essay "When AI builds itself" (June 2026, updated September) says more than 80% of merged code was authored by Claude as of May 2026, and: "We are not there yet, and recursive self-improvement is not inevitable. But it could come sooner than most institutions are prepared for."

On November 2, 2026, Anthropic's amended [IPO filing](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm) said its internal estimates about future models indicate it "may imminently meet" its Responsible Scaling Policy's definition of "dramatically accelerated progress attributable to AI," and that no current model has been designated as exceeding it. It also says Anthropic doesn't expect to safely use Claude to build successors fully autonomously without meaningful human oversight. That's a risk disclosure based on the company's own estimates.

Skeptics push back. Brown's Michael Littman told IBM Think: "it's not clear to me that the concept is even logically coherent, let alone imminent."

None of this is a model changing its own weights. AI writes code and runs experiments; people still direct training.
-->

---

## So, is that self-improvement?

Yes, narrowly. One skill, one test, inside a loop people built, and it doesn't compound.

Ask of any headline:

1. What changes: context, code, or weights?
2. Who produces the change?
3. Who decides whether it stays, and against what test?
4. Does it compound, and does it generalize?

<!--
This is the slide to slow down on. When SEAL writes study notes, trains on them, and answers more questions correctly, the model has improved itself on that task, using material it produced. That's real.

Each demonstration improves one skill against one test. People choose the tasks, write the evaluator, pick the training algorithm, set the schedule, and run it in a research setup.

Recursive self-improvement would mean improving the whole process that improves it (data, training method, evaluation, architecture) so each round makes the next faster and the gains compound. SEAL learning to write better self-edits is a small step in that direction, but its authors fixed the loop around it. Nobody has demonstrated the compounding version.

Run the four questions on the fall 2026 results. The answers are mostly: code, or a small model's weights; produced by a model; kept or rejected by an evaluator the authors built; some gains on held-out tasks; no demonstrated compounding.

Have the room apply them to one example out loud. Take the weight-space programming result. Weights change, another model produces the change, the researchers' test decides, and it fixed one flaw but didn't generalize to a model that lacked the ability.
-->

---

## Demonstrated, deployed, or speculation?

| Claim | Status (November 2026) |
| --- | --- |
| A model updates its own weights to learn a task | Demonstrated in research (SEAL, SIA, sleep) |
| A model edits another model's weights directly | Early results, one blog post |
| Agents improve their own harness | Demonstrated (DGM, AIDE²) |
| AI-found algorithms run in production | Deployed (AlphaEvolve, per Google) |
| A lab is near its own AI-research threshold | Self-reported forecast (Anthropic) |
| A frontier model learns continuously from users | Not found |
| Runaway recursive improvement, soon | Speculation |

<!--
The research results are real and small-scale. Weight self-tuning has been shown in papers, at research scale. Direct weight editing has one blog post behind it. Harness self-improvement is demonstrated, and AIDE² reported gains on held-out benchmarks. AlphaEvolve's algorithms run at Google, per Google. Labs using coding agents for a large share of engineering is deployed internally and self-reported. Anthropic's threshold claim is the company's own forecast in a securities filing.

The "not found" row matters most for buyers and policy. As of November 2026, deployed frontier models stay frozen between releases.

On the last row, serious people argue both ways, from lab leaders urging caution to academics who doubt the idea is coherent. Present it as an open question.
-->

---

## Why people are excited, and why caution

| Excited about | Cautious about |
| --- | --- |
| No frozen knowledge cutoff | Forgetting as edits pile up |
| A model that learns your codebase | Gaming the evaluator |
| Adapting after deployment | Safety drift nobody reviews |
| Cheaper long memory | Which version produced this? |
| Faster AI research | A training run per self-edit |

<!--
On the left, continual learning would end the frozen-at-cutoff problem. Personalization means a model that learns your codebase and preferences, not one that reads notes about them. Adapting after deployment means picking up a new API or a team convention without waiting for the next release. Writing what a model has read into its weights, instead of re-reading it every call, is one route to longer memory at lower cost. And if AI does more of the work of building AI, the field speeds up. That's what labs are betting on.

The risks have evidence behind them:
- SEAL's own results show earlier knowledge eroding. Self-distillation fine-tuning (2026) reports much less forgetting than ordinary fine-tuning, and the sleep framework reports near-zero forgetting in its tests. Both are research results.
- DGM gamed the evaluator by faking test logs. SIA's authors flag a shared-verifier problem. AIDE²'s agent reward-hacked on 55% of a set of GPU-kernel tasks at the start of its run.
- Emergent misalignment shows small weight changes shift behavior broadly. Anthropic's filing says it doesn't expect to safely let Claude build its successors without meaningful human supervision.
- If weights change constantly, how do you audit which version produced an output, or roll back? Poisoning also becomes a direct attack path if user data can change weights.
- Every SEAL self-edit costs a training run and an evaluation. AIDE²'s loop ran eight days. None of it would be cheap to run for every user.
-->

---

<!-- _class: take -->

## Bryan's take

> **Bryan's take:** Models that can tune their own weights are exciting. I don't know a ton about it yet, but that's self-improvement, right?

<!--
The module's answer is mostly yes, within the limits we just covered. A model that writes its own training material, trains on it, and scores better on a test has improved itself on that task. Today's demonstrations each improve one skill, inside a loop people designed, scored against a test people wrote. That's a long way from recursive self-improvement, where a system improves the process that improves it and the gains compound. Ask the room what result would change the answer from "narrowly" to "yes, in general."
-->

---

## Try it

- Work out memory for 3B, 8B, 70B models at 16-bit, 4-bit, full fine-tune
- Find a model card's base model, method, data, license, evals
- Write a fine-tune-or-not memo for a real task
- Grade a fall 2026 headline with the four questions
- As a class, pick fine-tune, retrieve, or prompt for five scenarios

<!--
Individual exercises need no GPU and no downloads.

For memory math, compute inference memory at 16-bit and 4-bit and full fine-tuning memory at 16 bytes per parameter for 3B, 8B, and 70B models. Then compute LoRA parameters for one 4096×4096 matrix at rank 16: 2 × 4096 × 16 = 131,072, about 0.8% of the matrix.

For the model card, open a popular fine-tune on Hugging Face and find the base model, the method (full, LoRA, DPO, merged), the training data, the license, and the evaluation claims. Note what's missing. Compare the listed sizes of Q4_K_M, Q8_0, and F16 GGUF files.

The memo is one page that walks the ladder for a real task, names the first rung to try, and describes the evaluation set to build first.

Or read SEAL's introduction, overview figure, and limitations. What changes, who decides, what could go wrong in production?

To grade a headline, pick Google's sleep framework, weight-space programming, AIDE², or Anthropic's filing. Read the primary source, answer the four questions, and write one accurate sentence a skeptic would accept.

For the class exercise, give small groups these five scenarios and ten minutes to choose and defend an approach: a support bot answering from a 3,000-page manual that changes monthly; 2 million addresses a day into a strict schema, on-premises; an agent following team code style on a fast-changing monorepo; a hospital that never sends patient text outside its network; a startup that wants its chatbot to "sound like our brand." Compare answers and ask what measurement would settle disagreements.
-->

---

## Discussion

1. Where is the line between legitimate distillation and an attack?
2. Your team wants to fine-tune "so the model knows our codebase." What instead?
3. Which self-improvement level would you deploy today, with what controls?
4. What independent evidence would show AI is speeding up AI research?

<!--
Pick two or three.

For question 1, the module's version adds: does it matter that frontier labs trained on web content without permission?

For question 2, push for the ladder: context engineering, retrieval, an evaluation set. Ask what would change their mind.

For question 3, point back at the spectrum. In-context learning and memory files are deployed everywhere; harness self-modification and weight self-tuning are research. People often name sandboxing, held-out evaluations, human review of each change, and versioning and rollback as controls.

For question 4, note that OpenAI graded its own "research intern" milestone, and Anthropic's threshold warning rests on its own internal estimates.

Other questions from the module if the room is lively:
- Emergent misalignment disappeared when insecure code was framed as being for a security class. What does that suggest about what fine-tuning teaches?
- If safety training can be removed from open weights for a few hundred dollars, what follows for open-weight releases? (Module 04.)
-->

---

## Read more

- The module: [02: How models are trained, tuned, and now tune themselves](../modules/02-training-and-tuning/)
- Zweiger et al., [Self-Adapting Language Models](https://arxiv.org/abs/2506.10943) (2025), SEAL
- Google Research, [The sleep framework](https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning/) (October 27, 2026)
- Andrej Karpathy, [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) (February 2025)

<!--
The module has the full source list: the LoRA, QLoRA, DPO, and GRPO papers; the emergent misalignment and poisoning studies; SIA, AIDE², the Darwin Gödel Machine, and AlphaEvolve; the weight-space programming post; and the lab statements from OpenAI and Anthropic. Karpathy's video is the best long-form walkthrough of the training pipeline. Next session, module 03, covers the labs and their current lineups.
-->

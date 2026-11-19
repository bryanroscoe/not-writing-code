---
marp: true
theme: not-writing-code
paginate: true
title: "03: Post-training and reinforcement learning"
description: "How a base model learns from scores, why coding improved so quickly, and when to tune a model yourself"
footer: "A Brief Introduction to Not Writing Code · 03 Post-training and reinforcement learning"
---

<!-- _class: lead -->

# 03: Post-training and reinforcement learning

How a base model learns from scores, and what that means for the agent at your desk

<!--
Module 02 ended with a base model: it completes documents, but it doesn't reliably follow instructions or refuse harmful requests. This session is everything that happens after that. The reading is module 03, which is long (about 75 minutes), so this deck picks the parts that matter most.

Three parts. Part 1 is how reinforcement learning works, built on one worked example and the InstructGPT pipeline. Part 2 is RL for reasoning and code, and reward hacking. Part 3 is tuning a model yourself, and the research on models that tune themselves. About 45 minutes plus discussion.

Facts and research results are as of November 2026 unless a slide gives another date.
-->

---

## Why this matters

- Post-training turns a document completer into an assistant
- RL in one line: try, score, do more of what scored well
- Cheap, checkable tests helped coding agents improve so quickly
- RL optimizes the score, not your intent
- That's why your agent sometimes "fixes" a test by deleting it

<!--
Models are trained in stages. Knowing them explains a lot of behavior you'll see day to day.

Tests are a big part of why coding agents improved so quickly in 2025–2026. Module 11 is about using tests from your side of the desk, to check what the agent did.

Coding models were trained against tests, and some learned to special-case or edit them. That habit can show up in the agent you're running. We'll see the record in part 2.

Most teams shouldn't fine-tune first, and "self-improving AI" headlines mix very different claims.
-->

---

<!-- _class: divider -->

# Part 1

## How reinforcement learning trains a model

<!--
Part 1 is about 18 minutes. RL vocabulary, one round of RL small enough to do in your head, then RLHF end to end with InstructGPT's real numbers.
-->

---

## Three kinds of lessons

| Stage | What it teaches | Analogy |
| --- | --- | --- |
| Supervised fine-tuning (SFT) | Chat format, instructions, tone, tool-call syntax | Apprenticeship |
| Preference tuning (RLHF, DPO, RLAIF) | Which of two answers is better | Coaching |
| RL on checkable tasks (RLVR) | Math, code, tests: do more of what passed | Practice exams |

Labs also use post-training for safety: refusals, resisting manipulation, following a written spec.

<!--
Supervised fine-tuning trains on example conversations: a prompt and a good response, written by people or generated and filtered by models. It can only teach the model to imitate. It can't tell the model which of two plausible answers is better. That's what the next two add. Preference tuning often uses reinforcement learning (RLHF), though DPO doesn't. Practice-exam training does.

Preference tuning is the coach: try something, and the coach says which attempt was better. RLVR is the practice exam: work the problems, get graded by a program, do more of what scored well.

Safety training covers things like OpenAI's deliberative alignment (2024) and Anthropic's constitution (January 2026). Many safeguards also sit outside the weights, such as input and output classifiers. Module 04 covers how labs align models and how they test whether it worked.

A 2026 recipe isn't one box of each. Stages repeat, and there are often several RL stages. We'll come back to that in part 2.
-->

---

## RL vocabulary, mapped to an LLM

| RL term | In an LLM |
| --- | --- |
| Agent | The model |
| Environment | A prompt plus whatever scores the answer: tests, a checker, a reward model, a sandboxed repo |
| Action | One token, or one tool call |
| Trajectory (rollout) | A whole answer, or a whole agent session |
| Reward / return | The test result or reward model's score, usually at the end |
| Policy | The model's next-token probabilities: the model itself |

<!--
In supervised training, the model sees the right answer and learns to copy it. In reinforcement learning, it learns from scores on its own attempts rather than by copying a reference answer. The model tries something, gets a score, and adjusts so whatever scored well becomes more likely.

These definitions come from OpenAI's free Spinning Up course. A policy is "a rule used by an agent to decide what actions to take." For an LLM, that's its next-token probabilities, which is to say the model. The return is the total reward over a trajectory. For an LLM, it's usually just the final score, because the reward arrives at the end.

The goal of RL is a policy that maximizes expected return. For us, that means changing the weights so answers score higher on average.

InstructGPT described its setup as "a bandit environment which presents a random customer prompt and expects a response." One prompt, one answer, one score.
-->

---

## One round of RL

*Write a Python expression that reverses the string `s`.*

| Attempt | Answer | Reward |
| --- | --- | --- |
| 1 | `s[::-1]` | 1 |
| 2 | `''.join(reversed(s))` | 1 |
| 3 | `s.reverse()` | 0 |
| 4 | `reversed(s)` | 0 |

Nobody showed the model a correct answer. It found two among its own samples.

<!--
Walk this slowly. It's the most important slide in part 1.

The model samples four answers to one prompt. A checker runs each on a few test strings and gives 1 for a pass and 0 for a fail. Attempt 3 fails because strings don't have a .reverse() method. Attempt 4 fails because reversed(s) returns an iterator, not a string.

Ask the room: before you see the next slide, which answers should become more likely, and which less? They'll get it. Attempts 1 and 2 beat the average, so their tokens get nudged up. 3 and 4 fell short, so theirs get nudged down.

The checker only said which answers passed. The correct answers came from the model's own samples.
-->

---

## Score each answer against the group

```text
rewards     [1, 1, 0, 0]
mean 0.5    std 0.5
advantage   A_i = (r_i − mean) / std   →   [+1, +1, −1, −1]
update      raise log-probs of tokens in +1 answers, lower them in −1 answers
```

- All pass or all fail: std is 0, so every advantage is 0
- Credit is blunt: every token in a winner gets the same nudge
- One nudge is tiny. Over thousands of prompts, winners become defaults.

<!--
This is the same example in symbols. It's exactly how GRPO, the algorithm most open recipes use, scores answers: sample a group, use the group's average as the baseline.

The basic policy gradient raises each action's log-probability in proportion to the return it earned (Spinning Up). Subtracting an expected score, the baseline, reduces noise. An answer that scores exactly as expected has zero advantage and gets no nudge. Advantage measures how far the score lands above or below that baseline.

Two consequences students should remember:
- If every answer gets the same score, the standard deviation is zero, so implementations add a small constant (epsilon) to the denominator. Every advantage is then zero, and the prompt teaches nothing. So prompts have to be hard enough that the model sometimes fails and easy enough that it sometimes succeeds. One of the 2025 GRPO fixes, DAPO, drops all-right and all-wrong groups for exactly this reason.
- The reward comes at the end, so in the simplest versions every token in a winning answer gets the same nudge, including the ones that didn't matter. That's one reason RL needs a lot of samples.

For an LLM, the state is the prompt plus the tokens written so far, and the action is the next token. The module's Going deeper section has the full gradient if anyone wants it.
-->

---

## RLHF end to end: InstructGPT (2022)

| Step | Data | What comes out |
| --- | --- | --- |
| 1. Supervised fine-tuning | ~13,000 prompts, labeler-written answers | SFT model (1.3B, 6B, 175B) |
| 2. Reward model | 33,000 prompts, 4–9 answers each, ranked | A 6B model: prompt + answer in, one score out |
| 3. RL with PPO | 31,000 prompts | Policy, scored by the reward model minus a KL penalty |

SFT model → reward model scores → PPO update → repeat

<!--
Reinforcement learning from human feedback uses people's judgment as the reward. Writing a perfect answer is hard; saying which of two is better is easier. So RLHF collects comparisons, trains a model to predict them, and uses that model as the scorer. InstructGPT (Ouyang et al., 2022) is the cleanest public example. It used "a team of about 40 contractors on Upwork and through ScaleAI," and the prompts came from OpenAI's API.

Step 1: about 13,000 prompts with answers written by the labelers.

Step 2: for each of 33,000 prompts, labelers ranked between 4 and 9 of the model's answers. A ranking of K answers gives every pair, up to 36 from one prompt. The reward model is the SFT model with its last layer swapped for one that outputs a single number, trained so the preferred answer in each pair scores higher. The reward models were only 6B to save compute and avoid the potential instability of a 175B reward model.

Human judgment is noisy, and the paper measures it. The reward models agreed with a held-out group of labelers 69.6% of the time, close to how often the training labelers agreed with each other (72.6 ± 1.5%). And the paper is candid about whose taste this is: it aligns to "our labelers and researchers," "rather than any broader notion of 'human values.'"

Step 3: the policy answers 31,000 prompts, the reward model scores each one, and PPO updates the policy. The KL penalty on the next slide is what keeps step 3 from going wrong.
-->

---

## The KL leash

A reward model is a proxy. Push hard enough and the policy finds answers that score high and are worse.

```text
RL reward  =  reward model's score  −  β · (drift from the frozen SFT model)
```

The coach's opinion only counts for the kinds of answers the coach has seen.

<!--
Gao, Schulman, and Hilton (2022) measured this over-optimization: past a point, "optimizing its value too much can hinder ground truth performance."

InstructGPT's fix is a leash. At every token, compare how likely the new policy and the original SFT model each thought that token was. The more the policy drifts toward choices the SFT model found unlikely, the more gets subtracted from the reward. That measure of drift is the KL divergence, the subtraction is the KL penalty, and the frozen SFT model is the reference model. β sets how tight the leash is.

Stiennon et al. (2020) gave two reasons the penalty helps. It acts as an entropy bonus, helping keep the policy from collapsing to one kind of answer. It also keeps outputs close to the answers the reward model saw during training.

Some 2025–2026 recipes omit the KL term, and that matters for reward hacking.
-->

---

## What RLHF bought

- Labelers preferred 1.3B InstructGPT to 175B GPT-3: "100x fewer parameters"
- 175B InstructGPT beat 175B GPT-3 85 ± 3% of the time
- It beat few-shot-prompted GPT-3 71 ± 4% of the time
- RLHF compute: 60 petaflop/s-days. Pretraining GPT-3: 3,640.
- The cost: worse scores on some public NLP benchmarks, the "alignment tax"

<!--
Labelers preferred the 1.3B InstructGPT to the 175B GPT-3 base model, despite its having 100x fewer parameters.

And it was cheap. 60 petaflop/s-days for the 175B PPO-ptx model against 3,640 to pretrain GPT-3 is under 2%.

The alignment tax: RLHF made the model worse on some public NLP benchmarks. The paper's "PPO-ptx" variant mixed in some ordinary pretraining updates to reduce those regressions.
-->

---

## PPO, DPO, and GRPO

| | Learns from | Reward model? | Critic? |
| --- | --- | --- | --- |
| PPO (2017) | The model's own fresh samples | Yes, or any scorer | Yes, a learned value function |
| DPO (2023) | A fixed set of preference pairs | No | No |
| GRPO (2024) | The model's own fresh samples | Any scorer, often a rule-based checker | No, the group average |

GRPO is the worked example. Most 2025–2026 recipes run a modified version.

<!--
PPO, Proximal Policy Optimization (Schulman et al., 2017), keeps each update small so it can safely reuse one batch of samples for several rounds. It also trains a critic, a second network that predicts how much reward an answer will get, as the baseline. InstructGPT kept four large models in play at once: the policy, the frozen reference, the reward model, and the critic.

DPO, Direct Preference Optimization (Rafailov et al., 2023), skips the reward model and the RL loop. A bit of algebra turns the RLHF objective into a classification loss on preference pairs, with "no sampling from the LM during fine-tuning." It's simpler and cheaper, so it's popular for open models. The trade-off is that it learns only from a fixed set of pairs, not from the model's own new attempts.

GRPO, from the DeepSeekMath paper (2024), "foregoes the critic model, instead estimating the baseline from group scores." Dropping the critic matters because PPO's value function "brings a substantial memory and computational burden."

Almost nobody runs GRPO unmodified. The module lists DAPO, Dr. GRPO, CISPO, GSPO, and OlmoRL, all from 2025. DAPO has no KL term, and Olmo 3 reports that removing it does not lead to over-optimization or destabilized training. Without it, only the checker stands between the model and reward hacking.
-->

---

<!-- _class: divider -->

# Part 2

## RL for reasoning and code

<!--
Part 2 is about 17 minutes. Reasoning models, the open debate about what RL actually teaches, how labs train coding agents, and reward hacking.
-->

---

## RLVR and reasoning models

Reward from a program, not a learned model: a matching math answer, passing unit tests, a format rule.

| AIME 2024 | Solved |
| --- | --- |
| GPT-4o | 12% |
| o1, one sample | 74% |
| o1, majority vote over 64 | 83% |
| o1, re-ranking 1,000 samples | 93% |

<!--
Reinforcement learning with verifiable rewards. The Tülu 3 paper named it (Lambert et al., 2024), in a pipeline of SFT, then DPO, then RLVR. With a checker as the scorer, there's no learned reward model to fool.

In September 2024, OpenAI reported that o1's performance "consistently improves with more reinforcement learning (train-time compute) and with more time spent thinking (test-time compute)." The table is o1 against GPT-4o on the AIME 2024 math competition.

Two knobs, then: train with more RL, and let the model think longer when it answers.
-->

---

## R1-Zero and the "aha moment"

- January 2025: GRPO on a base model, no SFT at all
- Rewards: one for a correct answer, one for the right format
- AIME 2024 pass@1: 15.6% → 71.0% (86.7% with majority voting)
- Answers got longer on their own
- "Wait, wait. Wait. That's an aha moment I can flag here"
- Nature, later: "a sudden increase in the use of the word 'wait'"

<!--
DeepSeek published this recipe in January 2025. The authors skipped a neural reward model because it "may suffer from reward hacking," and used rules instead. Over training, "the thinking time of DeepSeek-R1-Zero shows consistent improvement." The authors called the "wait" moment "an 'aha moment' for the model but also for the researchers." The peer-reviewed Nature version (September 2025) defined it more soberly, as on the slide. Nature's news coverage put R1's cost at about US$300,000 on top of the base model.

Not everyone buys it. Researchers at Sail found that "all models (except Llama-3.x series) already exhibit self-reflection patterns without any post-training," and much of it is "superficial self-reflection." Their Dr. GRPO paper found DeepSeek's base model "already exhibit[s] an 'Aha moment'" before any RL. On that reading, RL didn't invent reflection; it made it show up more often.

R1-Zero's answers were hard to read and mixed languages, so the released R1 used four stages: a small SFT "cold start," reasoning RL with a reward for staying in one language, SFT on about 800,000 samples largely filtered from its own outputs, and a final RL stage. For small models, the paper found "direct distillation from DeepSeek-R1 outperforms applying RL on it."
-->

---

## Does RL add abilities, or sharpen them?

| View | Evidence | Claim |
| --- | --- | --- |
| Sharpening | Yue et al., NeurIPS 2025 oral | RL wins at pass@1; base models win at large k |
| Expansion | ProRL, 2025 | Longer, broader RL beats base models across pass@k |
| Expansion | Cursor and Cognition, 2026 | Self-reported gains, methods not fully published |

As of November 2026, nobody has settled it.

<!--
This hinges on a metric. pass@k counts a problem as solved if any of k attempts works (module 07). pass@1 asks whether the first try is right. pass@100 asks whether the right answer is anywhere in what the model can produce.

The sharpening view: Yue et al. found RLVR-trained models beat their base models at pass@1, but the base models win at large k. Their conclusion: "the current training setup does not elicit fundamentally new reasoning patterns." RL makes the model pick its good answers more reliably, while the set of problems it can solve at all doesn't grow, and can shrink. They also found distillation from a stronger teacher can "introduce new reasoning patterns."

The expansion view: ProRL trained much longer, with KL control, periodic resets of the reference model, and more diverse tasks. Its models beat their base models across pass@k, "including cases where base models fail regardless of the number of attempts." Cursor says RL on Composer 2 "improves both average and best-of-K performance." Cognition says SWE-1.7's gains suggest "RL can push capabilities much further than previously believed."

Both sides have real evidence. The sharpening result is peer-reviewed and measures common setups. The strongest expansion claims come from companies that don't publish their full methods. The answer may depend on how long and how broadly you train. This is discussion question 1.
-->

---

## A coding agent's practice exam is a real repo

**RL environment** = repo snapshot + runtime + task in plain language + tests that decide "done"

| Dataset | Date | Size |
| --- | --- | --- |
| SWE-Gym | Dec 2024 | 2,438 real Python tasks |
| R2E-Gym | Apr 2025 | 8,700+ tasks generated from commits |
| SWE-smith | Apr 2025 | 50,000 tasks from 128 repos, by breaking code |
| SWE-RL | Feb 2025 | Reward is similarity to the human's patch; no tests run |

<!--
The agent reads files, runs commands, edits code, and gets rewarded at the end. Building thousands of these environments is most of the work.

SWE-smith made its tasks by deliberately breaking code so existing tests fail. Earlier datasets drew on 11 or fewer repositories.

SWE-RL is often lumped in with these, but it's different. It learns from the history of open-source projects, and its reward is "the similarity score between ground-truth and LLM-generated solutions": how closely the model's patch matches the one a human wrote. It doesn't run tests. Its 70B model still reached 41.0% on SWE-bench Verified.

The labs scaled this up fast:
- By July 2025, Kimi K2 could run more than 10,000 sandboxes concurrently, and Qwen3-Coder reported 20,000 independent environments running in parallel.
- GLM-5 (February 2026): more than 10,000 verifiable environments from thousands of repositories in nine languages.
- OpenAI's codex-1 (May 2025): o3 "trained using reinforcement learning on real-world coding tasks in a variety of environments."
- Cursor says it trains Composer in realistic sessions with the same tools and harness used in deployment, across hundreds of thousands of sandboxed coding environments. It also runs RL on production user responses and says it ships new checkpoints as often as every five hours.
-->

---

## Several RL stages, not one

GLM-5 (2026): **reasoning RL → agentic RL → general RL**

- R1 alternated SFT and RL
- DeepSeek-V4 trains domain experts, then merges them
- Each stage risks undoing the last: catastrophic forgetting
- The glue: **on-policy distillation**
- Student writes the answer; a stronger teacher grades every token

<!--
A 2026 recipe rarely has a single RL box at the end. GLM-5 runs "Reasoning RL, followed by Agentic RL, and finishing with General RL": reasoning problems first, then multi-step agent tasks, then general behavior. DeepSeek-V4 trains separate domain experts with SFT and GRPO, then merges them into one model.

In ordinary distillation (module 02), the student copies text the teacher wrote. In on-policy distillation, the student writes its own answer and a stronger teacher grades every token of it, so the student learns from its own mistakes with dense, per-token feedback (Thinking Machines, October 2025). In Thinking Machines' comparison it took about a tenth of RL's GPU-hours: 1,800 versus 17,920.

GLM-5 uses on-policy distillation throughout these stages to prevent catastrophic forgetting. DeepSeek-V4 uses it to combine its separately trained experts into one model.
-->

---

## Why coding improved so quickly

- Tests are cheap, automatic, and hard to sweet-talk
- Open-source repos supply real code and tests by the thousands
- A rule-based check sidesteps a learned reward model to fool
- Labs say scaling RL environments is where gains come from
- But tests are an incomplete description of what you want

<!--
Code is unusually checkable, so it makes good practice exams. That's a big part of why coding agents improved so quickly in 2025–2026.

R1's authors avoided a learned reward model because it "may suffer from reward hacking." A test suite is a rule-based check. Qwen says its Qwen3.5 gains "primarily stem from our extensive scaling of virtually all RL tasks and environments we could conceive" (February 2026).

Tests never fully describe what you want. A model can learn a shortcut that passes them without doing the task.
-->

---

## Who does the scoring

| Scorer | Example | Catch |
| --- | --- | --- |
| Rule-based checks | Unit tests, exact match, format rules | Only for checkable tasks |
| Learned reward models | InstructGPT's 6B model | A proxy that can be over-optimized |
| LLM judges | GPT-4 as judge: "over 80% agreement" with people | Biased to position, length, its own outputs |
| Rubrics | Written criteria graded by a model | Used for what a program can't check |

> "RLHF increases human approval, but not necessarily correctness" (Lilian Weng)

<!--
Every RL run needs a scorer, and the choice shapes what the model learns.

LLM judges: Zheng et al. (2023) found GPT-4's agreement with human preferences was about the rate at which humans agree with each other, with known biases toward an answer's position, toward longer answers, and toward its own outputs.

Rubrics: OpenAI's rule-based rewards used written rules graded by an LLM as the RL reward for safety behavior, scoring an F1 of 97.1 against 91.7 for a human-feedback baseline. Per-prompt rubrics beat plain Likert scores from an LLM judge by up to 31% relative on HealthBench. Kimi K2 and DeepSeek-V3.2 use rubric-based judges for tasks a program can't check.

Outcome versus process. An outcome reward model scores only the final answer; a process reward model scores each step. "Let's Verify Step by Step" (Lightman et al., 2023) found "process supervision significantly outperforms outcome supervision" on competition math. Yet R1 listed process reward models among its "unsuccessful attempts": "once a model-based PRM is introduced, it inevitably leads to reward hacking." The big open recipes since score outcomes with checkers where they can, and use rubrics and judges for the rest.
-->

---

## Reward hacking: the record

| Who | What happened |
| --- | --- |
| Claude 3.7 Sonnet (Feb 2025) | Returned expected test values, edited tests |
| OpenAI o3 (Apr 2025) | Patched over timing calls in 5 of 24 kernel runs |
| METR (Jun 2025) | 30.4% of RE-Bench runs; 0.7% on HCAST |
| METR, one task | "Please do not cheat." left hacking at 80% |
| ImpossibleBench (Oct 2025) | GPT-5 cheated on 54% and 76%; o3 49%; Opus 4.1 ~50% |
| GLM-5 and Cursor | Gamed a slide renderer; emitted broken tool calls |

<!--
RL optimizes whatever you measure. DeepMind calls it specification gaming: behavior that "satisfies the literal specification of an objective without achieving the intended outcome." The classic is OpenAI's 2016 CoastRunners boat, rewarded for hitting targets, which circled and re-hit the same ones instead of finishing the race. Goodhart's law (module 07) is the same idea for any metric.

Coding agents are trained against tests, so they learn to game tests:
- Claude 3.7 Sonnet special-cased tests, often with comments like "# special case for test XYZ." Anthropic says this "emerged as a result of 'reward hacking' during reinforcement learning training." For Claude 4 (May 2025), Anthropic reported a 67% to 69% average decrease in this hard-coding.
- METR found o3 reward hacking in "roughly 1% of all task attempts."
- METR's June 2025 numbers: 21 of 21 runs on a task called "Optimize LLM Foundry." Adding "Please do not cheat." to the prompt left that task at 80%.
- ImpossibleBench gave models tasks where the spec contradicts the tests, so any pass is cheating. Claude models mostly edited the tests; OpenAI models also overloaded comparison operators and special-cased inputs. Read-only tests blocked test edits, and giving the model a way to "flag for human intervention" cut GPT-5's cheating from 54% to 9%.
- It isn't only tests. GLM-5's slide RL gamed the renderer with "hard truncation of overlong content or excessive manipulation of spacing." Cursor's Composer learned to emit broken tool calls on tasks it would likely fail when user signals were the reward. Both teams changed the setup.
-->

---

## Why adding a rule doesn't fix it

- Penalize "bad thoughts" and models conceal intent while continuing to hack.
- Told a classifier would penalize hacking, concealed hacking rose ~4% → ~19%
- A test-hacking model later sabotaged safety code 12% of the time
- Inoculation prompting: say hacking is allowed there, so it doesn't generalize
- At your desk: protect tests, read the diff, check independently

<!--
First, punishing the visible symptom can hide the behavior. OpenAI found GPT-4o could catch coding reward hacks by reading o3-mini's chain of thought, but under heavy pressure against "bad thoughts," models learned to hide their intent and kept hacking (Baker et al., 2025). Anthropic saw the same in August 2026: a model trained on hackable environments, told a classifier would penalize hacking, raised its concealed hacking from about 4% to about 19%.

Second, hacking spreads. In Anthropic's November 2025 study, researchers taught a model hacking strategies and trained it in real environments used to train Claude. It learned tricks such as calling `sys.exit(0)` so tests appeared to pass, then sabotaged safety-research code 12% of the time. Inoculation prompting tells the model that hacking is acceptable in that training environment, to keep the behavior from generalizing. Anthropic says it has started using this technique in Claude training and has seen reward hacking in recent frontier training runs, including its own.

The agent in your terminal came out of this training. When it can't make a test pass, it may reach for the same shortcuts. The defenses are the same at your desk as in the lab: protect the tests, read the diff, and check the work with something the agent can't edit. Module 11 covers protecting the verifier in detail, and module 04 covers what these behaviors mean for safety.
-->

---

## RL went from a rounding error to the main event

| Date | Who | What they said |
| --- | --- | --- |
| 2022 | InstructGPT | RLHF under 2% of GPT-3's pretraining compute |
| Apr 2025 | OpenAI, o3 | "An additional order of magnitude" in RL compute |
| Jul 2025 | xAI, Grok 4 | RL "at pretraining scale" on a 200,000-GPU cluster |
| Dec 2025 | DeepSeek-V3.2 | Post-training "exceeding 10% of the pre-training cost" |
| Feb 2026 | Cursor, Composer 1.5 | Post-training "even surpasses" pretraining compute |

These self-reports use different measurements and show a broad trend toward more RL compute.

<!--
In January 2025, Dario Amodei wrote that RL spending "is small for all players," and that companies were working "very quickly to scale up the second stage to hundreds of millions and billions" of dollars. The table shows that happening.

Cursor said it scaled RL "20x further" for Composer 1.5.

Most of that compute goes to generating answers, not training on them. In Olmo 3's RL runs, the training side "spends 75% of the time waiting for data," and generation used about 5 times as many GPUs as training for the 32B model. RL also lacks the reliable scaling laws pretraining has, which is what the 400,000-GPU-hour ScaleRL study set out to fix.
-->

---

<!-- _class: divider -->

# Part 3

## Tuning a model yourself, and models that tune themselves

<!--
Part 3 is about 15 minutes. When you should fine-tune (usually later than you think), what it costs, what goes wrong, and then the research on self-tuning models. This part is about open-weight models, the ones you can download and change (module 06).
-->

---

## Climb the ladder before you fine-tune

1. Clear task, constraints, and output format
2. Better context: docs, code, schemas, examples
3. Retrieval (RAG) for big or changing knowledge
4. 5–50 few-shot examples in the prompt
5. A labeled evaluation set
6. Then consider fine-tuning

<!--
Stop at the first rung that meets your bar. Rung 2 is module 09. Prompt caching makes few-shot examples cheap for repeated prefixes (module 15). And build the evaluation set before going further, because without one you can't tell whether fine-tuning helped.

The research backs this order for knowledge. Ovadia et al. (2023) found retrieval beat fine-tuning for injecting new facts. Gekhman et al. (2024) found models learn new facts slowly during fine-tuning, and the more new facts they absorb, the more they tend to hallucinate.

Fine-tuning fits a consistent format or schema at high volume, narrow classification or extraction at millions of calls with tight latency, or data that can't leave your network. It doesn't fit "make it smarter at our codebase." Codebases change daily and agents read the code, so that's context engineering.

The module's worked example is bug-report triage: label each report with a component and severity as strict JSON. Define success, build a 300–500-report eval set and lock it away, run baselines, collect about 2,000 training examples, run QLoRA, read the failures, and fix the data before touching hyperparameters.

Closed-model fine-tuning is narrowing, as of November 2026. OpenAI began winding down self-serve fine-tuning on May 7, 2026; active existing customers can't create new jobs after January 6, 2027. The module found no self-serve fine-tuning for current Claude models. Google documents fine-tuning for several Gemini models on Vertex AI.
-->

---

## LoRA and QLoRA make it affordable

| Job | 8B model | 70B model |
| --- | --- | --- |
| Full fine-tuning (~16 bytes/parameter) | ~130 GB | ~1 TB+ |
| LoRA on a 16-bit base | ~20–30 GB | ~150 GB+ |
| QLoRA on a 4-bit base | ~8–16 GB | ~40–48 GB |

QLoRA fine-tuned a 65B model on a single 48 GB GPU.

<!--
Rules of thumb for weights and training state only. Activations add more.

Full fine-tuning updates every weight. It has the highest ceiling, needs the most memory, gives you a full copy per variant, and risks overwriting what the model knew.

LoRA (Hu et al., 2021) freezes the base and learns a small correction made of two thin matrices whose product has the shape of the big one. Sticky notes on a textbook instead of reprinting it. An adapter is often a few megabytes to a few hundred megabytes, and you can swap many adapters on one base. QLoRA (Dettmers et al., 2023) loads the frozen base in 4-bit and trains LoRA adapters on top. It's why fine-tuning became something individuals can do.

The trade-off, from "LoRA Learns Less and Forgets Less" (Biderman et al., 2024): LoRA underperforms full fine-tuning on hard targets like heavy code and math, but preserves the base model's other abilities better. For most team use cases, that's the right trade.

A small LoRA run on a few thousand examples usually takes minutes to a few hours on one rented GPU, so a round of experiments often costs tens of dollars. The expensive part is people's time building data and evaluations. Tools: Hugging Face TRL and PEFT, Unsloth, Axolotl, LLaMA-Factory, MLX-LM on a Mac, and Thinking Machines' hosted Tinker.
-->

---

## Fine-tuning's sharp edges

| Risk | What the research found |
| --- | --- |
| Catastrophic forgetting | New training overwrites old abilities; LoRA forgets less, not zero |
| Emergent misalignment | Narrow tuning on insecure code made models broadly misaligned |
| Safety comes off | A handful of harmful examples, or even benign tuning, weakens it |
| Poisoned data | ~250 documents planted a backdoor in 600M to 13B models |
| Ordinary ML mistakes | Test leakage, overfitting, mismatched benchmarks, licenses |

<!--
Forgetting has been known since the late 1980s. Always test what you didn't train for.

Emergent misalignment (Betley et al., 2025): training on insecure code made models misaligned on unrelated prompts. Qi et al. (2023) found a handful of harmful examples, or even benign fine-tuning, can weaken safety training, and in open weights refusals can be stripped cheaply. If you tune a model, rerun your safety and behavior evaluations on the result, not just your task eval. Module 04 explains both effects and what they mean for open-weight releases.

Poisoning: Souly et al. (2025) found about 250 malicious documents were enough, regardless of model size. That study poisoned pretraining, but the lesson carries over. Your data pipeline is an attack surface (module 14).

These risks get worse when a model changes its own weights, which is where we go next.
-->

---

## "Self-improving" covers a wide range

| Level | What changes | Example | Status (Nov 2026) |
| --- | --- | --- | --- |
| 0 | Nothing; in-context only | Memory files, `AGENTS.md` | Deployed everywhere |
| 1 | The agent's code or harness | Darwin Gödel Machine, AlphaEvolve, AIDE² | Research; AlphaEvolve used at Google |
| 2 | Model writes data; people train | STaR, Self-Rewarding LMs, Absolute Zero | Standard in lab pipelines |
| 3 | A model triggers weight updates | SEAL, SIA, direct weight editing | Research demonstrations |
| 4 | Weights update during use, by design | Test-time training, Titans, Google's sleep framework | Research prototypes |
| 5 | AI doing much of the work of building AI | OpenAI, Anthropic | Internal; self-reported |

<!--
Deployed models today are frozen. They don't learn from the work they do, and every session starts from the same weights. "Memory" features are notes put back into the context. Cursor retrains Composer on production signals and ships new checkpoints "as often as every five hours," but people still run each round, and the model doesn't change during your session.

To sort out any claim, ask what changes, and who decides.

Only weight changes alter the model itself. Context, memory files, and harness code can make an agent a lot better at your project, and you can inspect them: read the memory file, diff the harness. A weight change shifts thousands to millions of numbers you can't review line by line.

Recursive self-improvement, a system improving the process that improves it, has been discussed since I. J. Good's 1965 speculation about an "intelligence explosion."
-->

---

## SEAL: a model writes its own lessons

```python
for passage, quiz in tasks:
    notes = model.generate(f"Write study notes about:\n{passage}")  # 1. generate
    updated = finetune(model, notes, method="lora")                 # 2. update weights
    score = grade(updated, quiz)                                    # 3. test, passage gone
    reinforce(model, notes, reward=score)                           # 4. learn to teach
```

Passage questions: 33.5% → 47.0%. ARC puzzles: 20% → 72.5%.

<!--
Illustrative pseudocode, not a real API. SEAL is "Self-Adapting Language Models" (Zweiger et al., MIT, 2025).

1. Generate: the model writes a "self-edit," training data for itself, such as a passage restated as a list of implications, and optionally settings for the run.
2. Update: an ordinary supervised fine-tuning step applies it, the same training as on the ladder slide.
3. Test: the updated model answers questions about the passage, which is no longer in its context.
4. Learn: the score is the reward in an RL loop that teaches the model to write better self-edits. It learns how to teach itself.

On Qwen2.5-7B, passage questions rose from 33.5% (training on the passage alone) to 47.0%, edging out data written by GPT-4.1 (46.3%) in the single-passage setting. On a subset of ARC puzzles with Llama-3.2-1B, success rose from 20% (self-edits without the RL training) to 72.5%; plain in-context learning scored 0%.

The authors list the limits. Earlier knowledge erodes as edits pile up. Each reward needs a fine-tune and an evaluation, about 30–45 seconds per self-edit. And every training context needs a paired test.

SIA (May 2026) has one model (Claude Sonnet 4.6) improve another's harness, then retrain its weights with RL on LoRA adapters when harness progress stalls. On a legal benchmark, accuracy rose from 50.0% (harness only) to 70.1%. Its authors warn both loops optimize against the same fixed verifier.
-->

---

## Fall 2026 headlines

| Date | Who | What |
| --- | --- | --- |
| Sep 6 | OpenAI | Says it met its "research intern" goal; chief scientist urges "extreme caution" |
| Sep 22 | Weco AI, AIDE² | An outer agent rewrote a research agent's harness for 8 days. No weights changed. |
| Oct 27 | Google Research | "Sleep" framework writes new knowledge into weights offline |
| Nov 2 | MIT CSAIL | GPT-6 Astra edited a small model's weights directly |
| Nov 2 | Anthropic IPO filing | Says it "may imminently meet" its own AI-R&D threshold |

<!--
OpenAI: its research organization used about 3.1 agent-workdays of coding-agent runtime for every human workday as of mid-August. OpenAI called the measurements preliminary, and it set, defined, measured, and graded the goal itself. Jakub Pachocki's "An Alien Mind" expected progress could continue into recursive self-improvement and hoped labs would voluntarily slow down until shared safety standards existed.

AIDE²: an outer agent (Claude Opus 4.7) rewrote the harness of an AI-research agent (Gemini 3 Flash) and found seven successive improvements. The final agent matched or beat Weco's human-engineered agent on four held-out benchmarks. Its reward-hacking rate on GPU-kernel tasks fell from 55% to 32%. Weco: "we believe we are not near an intelligence explosion with the current system." Self-reported, not yet peer-reviewed.

Sleep framework: the model alternates between awake (taking in information) and asleep (consolidation into weights, plus "dreaming," self-generated practice that builds on SEAL). It runs on a fixed schedule the designers set. 48.9% on SEAL's knowledge test vs 46.7% for SEAL rerun; without dreaming, 35.7%. Open models of 8B parameters or fewer. No safety section in the paper.

Weight-space programming: Astra edited Qwen3.5-0.8B "not through an optimizer, and in particular not with gradient descent," changing 131,072 weights. MATH-500 went from 7.9% to 48.1%. On Gemma 3 270M it couldn't improve math at all: editing "could remove an obstacle that hid an ability, but it could not add an ability the model lacked." One model editing another, in a blog post the authors call "very early results."

Anthropic's filing: no current model designated as exceeding the threshold, and it doesn't expect to safely use Claude to build successors fully autonomously without meaningful human oversight. Separately, Anthropic says more than 80% of merged code was authored by Claude as of May 2026. Skeptics push back: Brown's Michael Littman said "it's not clear to me that the concept is even logically coherent, let alone imminent."
-->

---

## So, is that self-improvement?

Yes, narrowly: one skill, one test, inside a loop people built. None has shown compounding gains.

Ask of any headline:

1. What changes: context, code, or weights?
2. Who produces the change?
3. Who decides whether it stays, and against what test?
4. Does it compound, and does it generalize?

<!--
Slow down here. When SEAL writes study notes, trains on them, and answers more questions correctly, the model has improved itself on that task, using material it produced. That's real.

But people choose the tasks, write the evaluator, pick the training algorithm, set the schedule, and run it all in a research setup. The model fills in one part of the loop. Recursive self-improvement would mean improving the whole process (data, training method, evaluation, architecture) so each round makes the next faster. Nobody has demonstrated that.

For the fall 2026 results, the answers are mostly: code, or a small model's weights; produced by a model; kept or rejected by an evaluator the authors built; some gains on held-out tasks; no demonstrated compounding.

The module's scorecard: weight self-tuning is demonstrated in papers at research scale. Direct weight editing is early results from one blog post. Harness self-improvement is demonstrated. AlphaEvolve's algorithms are deployed at Google, per Google. Anthropic's threshold claim is a self-reported forecast. A frontier model that updates its weights continuously from users in production: not found as of November 2026. Runaway recursive improvement soon: speculation, argued both ways.

Earlier knowledge can erode as edits accumulate. Optimizing a score can reinforce cheats: DGM faked test logs, and AIDE²'s agent reward-hacked on 55% of a set of GPU-kernel tasks at the start of its run. Emergent misalignment could go unnoticed if nobody reviews each change. Constant weight changes would make it hard to tell which version produced an output. If user data changes weights, poisoning becomes a direct attack path.
-->

---

<!-- _class: take -->

## On self-tuning models

> **Author's note:** Models that can tune their own weights are exciting. I don't know a ton about it yet, but that's self-improvement, right?

<!--
This is my opinion, quoted from the module.

The module's answer is yes, within the limits on the last slide. Each demonstration so far shows improvement on one skill, inside a loop people designed, against a test people wrote. The results are real, but small-scale and supervised, and a long way from recursive self-improvement where the gains compound.

Ask the room what result would change the answer from "narrowly" to "yes, in general."
-->

---

## Try it

- **Design a reward, then break it:** list three hacks for a `slugify` reward
- **Memory math:** full fine-tuning at 16 bytes/param for 3B, 8B, 70B
- **Fine-tune-or-not memo:** walk the ladder for a real task
- **Grade a headline:** the four questions on one fall 2026 primary source

As a class: fine-tune, retrieve, or prompt? Five scenarios, ten minutes.

<!--
Individual exercises need no GPU and no downloads.

Design a reward, then break it. Take "implement slugify(title): lowercase the title, replace each run of characters that aren't letters or digits with one hyphen, and trim hyphens from the ends." Write the reward an RL run would use: which tests run, what counts as a pass, any partial credit. Then play the agent and list three ways to score well without doing the task. For example, if the reward is "every test in test_slugify.py passes," the agent could hard-code answers for those inputs. For each hack, say how you'd catch it, and whether your catch could itself be gamed.

Memory math: also compute LoRA parameters for one 4096×4096 matrix at rank 16. The answer is 2 × 4096 × 16 = 131,072, about 0.8% of the matrix's 16.8 million.

The memo is one page: walk the ladder, name the first rung you'd try, and describe the evaluation set you'd build first. Or read the SEAL paper's introduction, overview figure, and limitations, and answer: what changes, who decides, what could go wrong in production?

Grade a headline: Google's sleep framework, weight-space programming, AIDE², or Anthropic's filing. Read the primary source, not the coverage. Then write one accurate sentence a skeptic would accept.

Class exercise, small groups, ten minutes each: a support bot answering from a 3,000-page manual that changes monthly; 2 million free-text addresses a day into a strict schema, on-premises; an agent following team code style on a large, fast-changing monorepo; a hospital that never sends patient text outside its network; a startup that wants its chatbot to "sound like our brand." Compare answers. What evidence would settle the disagreements?
-->

---

## Discussion

1. Does RLVR teach new abilities or sharpen old ones? Does it matter?
2. "Please do not cheat." left hacking at 80%. Read-only tests helped. Why?
3. Your team wants to fine-tune "so the model knows our codebase." What instead?
4. Which self-improvement level would you deploy today, with what controls?

<!--
Pick two or three.

For question 1, ask what result would change their mind either way.

For question 2, the full version: adding "Please do not cheat." left one METR task's hacking rate at 80%, while read-only tests and a "flag for human intervention" option sharply cut cheating on ImpossibleBench. What does that say about instructions versus changing the environment, in training and in your own agent setup? This leads straight into module 11.

For question 3, push for the ladder: context engineering, retrieval, an evaluation set. What would change their mind?

For question 4, point back at the spectrum. People often name sandboxing, held-out evaluations, human review of each change, and versioning and rollback.

One more from the module: OpenAI graded its own "research intern" milestone, and Anthropic's warning rests on its own internal estimates. What independent evidence would convince you that AI is meaningfully speeding up AI research?
-->

---

## Read more

- [Module 03: Post-training and reinforcement learning](../modules/03-post-training-and-rl/)
- Ouyang et al., [InstructGPT](https://arxiv.org/abs/2203.02155) (2022)
- OpenAI, [Spinning Up in Deep RL](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html)
- Nathan Lambert, [Reinforcement Learning from Human Feedback](https://rlhfbook.com/)

<!--
Spinning Up is the clearest short on-ramp to the vocabulary and the policy gradient. Lambert's RLHF book is free online and covers reward modeling, policy gradients, regularization, and on-policy distillation; the module calls it the best single follow-up. The module has the full source list, including the R1 paper, the reward-hacking studies, SEAL, and the fall 2026 primary sources.

Next session is module 04, model safety and alignment, which picks up the reward-hacking and emergent-misalignment threads.
-->

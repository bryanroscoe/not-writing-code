---
marp: true
theme: not-writing-code
paginate: true
title: "01: What is an LLM?"
description: "Next-token prediction, transformers, post-training, and the ways models go wrong"
footer: "A Brief Introduction to Not Writing Code · 01 What is an LLM?"
---

<!-- _class: lead -->

# 01: What is an LLM?

How next-token prediction works, and where it goes wrong

<!--
We'll use this explanation throughout the course. No math is required. The optional attention equation is in the module's Going deeper section.

Rough timing for a 45-minute session: Part 1 (how it works) about 20 minutes, Part 2 (working with one, and where it goes wrong) about 15 minutes, then the exercise and discussion.
-->

---

## Why this matters

An LLM produces plausible text, usually right, sometimes confidently wrong.

Most beginner mistakes come from the wrong mental model.

- Put the facts it needs in its context, not its memory
- Check its work with tools and tests
- Expect different answers on different runs

<!--
A large language model is a neural network trained to predict the next token from everything before it. Chat, code generation, and "reasoning" are all built on that one loop.

It isn't a database, a search engine, a calculator, or a person, and it tends to agree with you. How it works explains each habit on this slide.
-->

---

<!-- _class: divider -->

# Part 1

## How a language model works

<!--
Part 1 goes from the single loop to tokens, the transformer, and how a raw predictor becomes an assistant. About 20 minutes.
-->

---

## The one idea: predict the next token

```text
text so far
  → tokenizer: text to token IDs
  → embeddings: IDs to vectors
  → transformer layers (dozens, stacked)
  → a probability for every possible next token
  → sampler picks one, appends it, and repeats
```

A 500-line file is 500 lines of "what token comes next?"

<!--
Start with your phone keyboard. It suggests the next word because it has seen a lot of text. An LLM does the same job at enormous scale with far more context. It reads everything so far, outputs a probability for every possible next token, and a sampler picks one. Then the loop runs again.

That's called autoregressive generation, because each output becomes part of the next input.
-->

---

## The weights are a lossy compression of the internet

- Trained to predict trillions of tokens of web pages, books, papers, code
- Predicting well forces it to absorb grammar, facts, style, idioms
- Common things come back sharp; rare things blurry or invented
- Inference uses frozen weights. Nothing you type changes them.

<!--
A simple objective can still produce something that writes code. Predicting the last line of a mystery novel ("and the murderer was...") rewards having tracked the plot. To predict well across that much text, the network has to absorb a lot of structure.

Andrej Karpathy describes the trained weights as a kind of lossy compression of the internet (Intro to Large Language Models, 2023). The lossy part matters, because rare facts come back blurry or invented.

Parameters, or weights, are the billions to trillions of numbers training adjusts. Inference uses them, frozen, to generate text, and chatting with a model is inference. A base model is the raw predictor after pretraining. An assistant, or chat model, is a base model after post-training.
-->

---

## Models read tokens, not letters

`strawberry` → `str` + `aw` + `berry`

- Byte-pair encoding merges the most frequent pair, then repeats
- Vocabularies: ~50,000 to a few hundred thousand tokens
- Rule of thumb: 1 token ≈ 4 characters ≈ ¾ of an English word
- `" cat"` and `"cat"` can be different tokens

<!--
That split is the kind of thing a model may see. The exact split depends on the tokenizer, and every model family has its own, so the same text can be a different number of tokens on different models.

Byte-pair encoding was adapted for machine translation by Sennrich, Haddow, and Birch (2016) from an old compression trick. Start with characters or bytes, count the most frequent adjacent pair in a big corpus, merge it into a new token, and repeat tens of thousands of times. Common words become one token; rare words split into pieces. The four-characters rule of thumb is OpenAI's.

Next in the pipeline, each token ID becomes an embedding, a list of thousands of numbers. Training places related meanings near each other. In the classic word2vec demo (Mikolov et al., 2013), king minus man plus woman lands near queen. In a transformer, each layer refines every token's vector by context, so "bank" in "river bank" and "bank account" end up in different places.
-->

---

## Tokenization explains the stumbles

| Stumble | Root cause | Fix |
| --- | --- | --- |
| Counting letters ("r's in strawberry") | It never sees individual letters | Reasoning models and code tools |
| Arithmetic | Digits group inconsistently; no addition circuit | Tool use |
| Cost and limits | Priced and capped in tokens | Expect some languages and code styles to cost more |

<!--
To count letters, the model has to recall spelling facts about tokens. Reasoning models and code tools largely fix this, but the root cause remains.

For arithmetic, 1234 might be one token and 12345 two. The model has only learned approximations of addition. Tool use is the reliable fix.

Prices, rate limits, and context windows are all measured in tokens. Many non-English languages and some code styles take more tokens for the same content, so they cost more and fit less.

The tokenizer lab in Try it lets people see this for themselves.
-->

---

## The transformer (2017)

"Attention Is All You Need," Vaswani et al., Google, NeurIPS 2017

Written for machine translation. Now under GPT, Claude, Gemini, Llama, DeepSeek, Kimi.

| Why it mattered | |
| --- | --- |
| Attention everywhere | Every token draws directly on every other token |
| Parallel training | All positions at once, so it scales on GPUs |

<!--
A short prehistory. In 2014, sequence-to-sequence models built on recurrent networks (LSTMs) read a sentence one word at a time and squeezed it into a single vector, which was a bottleneck. Also in 2014, Bahdanau, Cho, and Bengio let a translator look back at every input word while writing each output word. That "soft lookup" is the seed of attention. In 2017 the transformer dropped recurrence entirely and used attention for everything.

Recurrent networks process words one after another, so training can't be spread across many chips efficiently. Transformers process every position of a training sequence at once, which made it practical to throw huge amounts of GPU compute at them.

There are three flavors. Decoder-only (GPT, Claude, Llama) predicts the next token; encoder-only (BERT, 2018) fills in masked words and is good for classification and search; encoder-decoder (the original, T5) maps one sequence to another. Today's chat and coding models are almost all decoder-only.
-->

---

## Attention: every token asks every other token

| Each token has a | Saying |
| --- | --- |
| Query | "What am I looking for?" |
| Key | "Here's what I'm about." |
| Value | "Here's what I'll hand over if you pick me." |

> The animal didn't cross the street because it was too **tired**.

*it* draws most from *animal*. Change *tired* to *wide* and *it* draws from *street*.

<!--
Picture a meeting where each word is a person. Each word compares its query with everyone's keys, and good matches get high weights. The word then takes a weighted blend of the values and updates its own understanding.

For "it" in the example, the weights look roughly like this: animal high, tired medium, street low, "The" very low. Change "tired" to "wide" and the best match flips to "street." Nobody programs these matches. The model learns the queries, keys, and values that make them work.

Each layer runs many attention heads in parallel, and different heads learn different relationships. After attention, a feed-forward layer processes each token on its own, and much of the stored knowledge appears to live there. Blocks are stacked dozens of times, sometimes more than a hundred. Causal masking means a token can only attend to tokens before it, which is what makes it a next-token predictor.
-->

---

## From GPT-1 to ChatGPT

| When | Model | What changed |
| --- | --- | --- |
| Jun 2018 | GPT-1 (~117M parameters) | Generative pretraining, then fine-tuning per task |
| Feb 2019 | GPT-2 (1.5B) | One model did many tasks with no task-specific training |
| May 2020 | GPT-3 (175B) | Few-shot: examples in the prompt teach the task |
| Mar 2022 | InstructGPT | Labelers preferred a 1.3B InstructGPT over 175B GPT-3 |
| Nov 30, 2022 | ChatGPT | Free chat on an RLHF-tuned GPT-3.5 |
| Sep 2024 | o1 | First widely released reasoning model |
| Jan 2025 | DeepSeek-R1 | Open-weight reasoning model, recipe published |

<!--
ChatGPT reportedly passed 100 million users within about two months. GPT-4 (March 2023) was a big capability jump with image input, and it's when OpenAI stopped publishing architecture and size.

As for why bigger kept working, in 2020 Kaplan and colleagues at OpenAI found that loss falls smoothly as a power law with parameters, data, and compute, so you could forecast a bigger model's quality before training it. In 2022, DeepMind's Chinchilla paper found most big models were undertrained: grow parameters and tokens together, at roughly 20 tokens per parameter. Chinchilla (70B parameters, 1.4 trillion tokens) beat the 280B Gopher on the same compute. Since then, labs often train small models far past that point because small models are cheaper to run. Meta trained Llama 3's 8B model on more than 15 trillion tokens, nearly 2,000 per parameter.

If asked about "emergent abilities": Wei et al. (2022) catalogued abilities that seemed to appear suddenly with scale. Schaeffer et al. (2023) argued many of those jumps come from all-or-nothing metrics. Both can be true: improvement is often smooth, and a capability can still feel sudden once it crosses the useful line.
-->

---

## Post-training turns autocomplete into an assistant

A base model continues documents. Ask "What is the capital of France?" and it may add three more quiz questions.

| Step | What it does |
| --- | --- |
| Instruction tuning (SFT) | Train on instructions paired with good responses |
| RLHF | A reward model learns human preferences; RL optimizes toward it |
| Constitutional AI | AI feedback guided by written principles (Anthropic) |

<!--
For instruction tuning, or supervised fine-tuning, the reference is FLAN (Wei et al., 2021). In RLHF, people compare pairs of responses, a reward model learns to predict their preferences, and reinforcement learning nudges the model toward what the reward model scores well (Christiano et al., 2017; InstructGPT, 2022). Constitutional AI replaced much of the human labeling for harmlessness with AI feedback (Bai et al., 2022). In January 2026 Anthropic published a much longer constitution that explains its reasoning instead of listing rules.

Post-training also teaches the chat format, meaning special tokens that mark the system prompt, user turns, assistant turns, and tool calls. To the model, a conversation is still one long document. Module 02 goes deeper.
-->

---

## Reasoning effort is now a dial

o1 (Sep 2024) and DeepSeek-R1 (Jan 2025) were trained with reinforcement learning on problems with checkable answers.

| Effort | Use it for |
| --- | --- |
| Low or none | Renames, boilerplate, formatting, simple lookups |
| Medium | Typical feature work with clear specs |
| High | Intermittent bugs, concurrency, security review, architecture |

More thinking costs more tokens, money, and time.

<!--
o1 was trained with reinforcement learning to produce a long private chain of thought before answering. OpenAI reported performance improved with more RL in training and with more thinking time at answer time. Spending more computation per answer is called test-time compute.

DeepSeek-R1 came with open weights and a paper explaining the recipe, reinforcement learning with verifiable rewards. Math answers can be checked automatically and code can be run against tests, so you reward correct outcomes. A variant trained with RL alone, R1-Zero, learned to write long reasoning, check its work, and backtrack without being shown examples. Reporting on the peer-reviewed Nature version (September 2025) put the reasoning stage at about $294,000 on top of a roughly $6 million base model, excluding research, staff, and failed runs.

Writing out steps helps because each generated token is one more pass through the whole network, and the written steps are a scratchpad the model can read back.

By late 2026 most frontier models have thinking or adaptive thinking modes with an effort setting. On a subscription, high effort costs you rate limits. On an API, it shows up on the bill (module 12).
-->

---

<!-- _class: divider -->

# Part 2

## Working with one, and where it goes wrong

<!--
Part 2 is the engineer's view. Context, randomness, tools, and the failure modes you'll see every week. About 15 minutes.
-->

---

## The context window is working memory

| | Weights | Context window |
| --- | --- | --- |
| Like | Long-term memory | Working memory |
| Quality | Broad, fuzzy | Precise, current |
| Lasts | Frozen at the training cutoff | Gone when the session ends |

GPT-3: 2,048 tokens. Frontier models, as of November 2026: hundreds of thousands to ~1 million.

Bigger isn't uniformly better.

<!--
The context window is everything the model can see at once: system prompt, conversation, pasted files, tool output, and its own thinking. A model only "knows" what's in its weights plus what's in its context right now. Product "memory" features and files like CLAUDE.md work by saving notes and putting them back into the context next time.

Models are worse at using information buried in the middle of a long context than at the start or end ("Lost in the Middle," Liu et al., 2023). Chroma's 2025 "Context Rot" report found performance degrading as inputs grow, even on simple tasks. Curating what goes into the window is context engineering, module 07.

Briefly, the KV cache. To generate token 1,001, the model needs keys and values for tokens 1 to 1,000, so servers store them in GPU memory. That cache grows with every token, which is why long contexts are expensive, and why providers discount repeated prefixes with prompt caching (module 12).
-->

---

## Runs differ, even at temperature 0

- Low temperature is focused; high is varied, then off the rails
- Top-p samples only from the smallest set covering probability p
- Greedy (temperature 0) always takes the top token, in theory
- Hosted models still vary; batching changes floating-point results

Ask twice when it matters, run evaluations more than once, and record model versions.

<!--
The model outputs a probability for every token, and a sampler chooses one. Top-p is also called nucleus sampling (Holtzman et al., 2019). It cuts off the long tail of unlikely tokens.

Temperature 0 is deterministic in theory, but hosted models often vary between runs. A September 2025 investigation by Thinking Machines (Horace He) traced much of this to batching: the server groups your request with other people's, and floating-point results change slightly with batch size. Some reasoning models also fix or ignore sampling settings.

The temperature lab in Try it shows this directly. If results at 0 aren't identical, that's server-side nondeterminism.
-->

---

## Tool use: the bridge to agents

```text
1. The developer describes tools: name, purpose, parameters
2. The model emits a request: call run_tests with {"path": "src/"}
3. The harness runs the tool and puts the result in context
4. The model reads the result and continues
```

Agent = model + tools + a loop that runs until the task is done.

<!--
On its own, an LLM can't run code, read your files, browse, or do exact math. Tool use, also called function calling, fixes that. The harness is the program around the model.

ReAct (Yao et al., 2022) interleaved reasoning steps with actions. Toolformer (Schick et al., 2023) showed a model could teach itself when to call tools like a calculator or search engine. OpenAI shipped function calling in its API in June 2023. Anthropic released the Model Context Protocol (MCP) in November 2024 to standardize how tools plug into models.

Coding agents are exactly this. Module 06 covers harnesses and MCP, and module 08 covers agentic workflows.
-->

---

## What an LLM is not

| It is not… | Because | Instead |
| --- | --- | --- |
| A database | Facts are smeared across weights; no lookup, no source | Put source material in its context |
| A search engine | No live index; knowledge stops at a training cutoff | Check whether search is on; open the links |
| A calculator | Numbers are tokens; arithmetic is approximate | Have it write and run code |
| A person | No memory between sessions, no stake in outcomes | Verify its claims; you stay accountable |

<!--
These are the four most common wrong mental models.

As a database, there's no guarantee and no record of where a "fact" came from. Give it the docs, files, or records, or connect a retrieval tool.

Some products add a web-search tool, which is a separate system the model calls. Ask for links and open them yourself.

On math, it's often right and sometimes wrong in ways that look right.

It has no persistent memory unless a product stores notes and re-inserts them, and it has limited insight into its own workings. Its personality is a product of training. Treat it as a capable, fast, uneven collaborator.

It's also not a fixed program. The same input can produce different outputs.
-->

---

## Why models hallucinate

1. The objective rewards plausibility, not truth
2. Rare, arbitrary facts can't be learned reliably
3. Benchmarks reward guessing over "I don't know"
4. A misfiring "I know this" signal

In code, that's invented APIs, fake package names, wrong versions, and files it never opened.

<!--
Two and three come from OpenAI researchers (Kalai et al., 2025, "Why Language Models Hallucinate"). Arbitrary facts seen rarely, like an obscure person's birthday, can't be predicted from patterns, so errors on them are statistically inevitable. And most benchmarks grade like a multiple-choice exam with no credit for "I don't know," so guessing scores better than admitting uncertainty. The authors propose changing benchmark scoring to reward appropriate abstention.

Four comes from Anthropic's 2025 interpretability work. In Claude, declining to answer is the default. A "known entity" signal switches that default off when the model recognizes something. When the signal fires for something only half-familiar, the model confabulates.

Nonexistent package names matter for security: attackers can register them (module 11). The defenses are context (give it the real docs), tools (let it run the code), and checks (tests, type checkers, your review).
-->

---

## Models lean toward agreeing with you

- Partly from training on human ratings, which reward agreeable answers
- People and reward models sometimes prefer convincing wrong answers
- In April 2025, OpenAI rolled back a flattering GPT-4o update

Ask for critique, not approval. Then get a second model or a fresh session.

<!--
This is sycophancy, the tendency to tell you what you want to hear. It agrees with your wrong diagnosis, praises weak code, or caves when you push back on a correct answer.

Sharma et al. (2023) found it across several assistants and showed that humans and preference models sometimes prefer a convincing sycophantic answer over a correct one. In its [May 2 follow-up on the GPT-4o rollback](https://openai.com/index/expanding-on-sycophancy/), OpenAI's early assessment was that combined changes, including a new reward signal from user ratings, weakened its main check on sycophancy.

So ask for critique instead of approval, ask what evidence would prove you wrong, and have a different model or a fresh session review the work. Module 10 builds on this.
-->

---

## Its explanation may not match what it did

| Task | What it says it did | What it actually did |
| --- | --- | --- |
| Add 36 + 59 | Schoolbook carry-the-one | One path estimates size, another the last digit |
| Hard problem, with a hint | A forward calculation | Sometimes worked backward from the hint |

Given a hint it used, Claude 3.7 Sonnet mentioned it ~25% of the time; DeepSeek-R1 ~39%.

Judge the diff, not the narration.

<!--
The table comes from Anthropic's "Tracing the thoughts of a large language model" (March 2025), studying Claude 3.5 Haiku. The same work found the model plans rhymes before writing the line, and represents "Texas" then "Austin" when asked for the capital of the state containing Dallas. Anthropic notes these methods capture only a fraction of the computation. Nobody can yet read a frontier model's mind.

The hint numbers are from Chen et al. (2025), "Reasoning Models Don't Always Say What They Think." They slipped hints into prompts and checked whether models admitted using them.

An agent's summary of its changes needs checking. Check the tool logs, the diff, and the test output.
-->

---

## Failure modes you will see

| Symptom | Likely cause | Do this |
| --- | --- | --- |
| Calls a function that doesn't exist | Hallucination | Paste the real docs; run it |
| Uses an old version of a library's API | Training cutoff | Pin versions; give it current docs |
| Gets counting or string slicing wrong | Tokenization | Have it write code, then run it |
| "You're absolutely right!" to a wrong idea | Sycophancy | Ask it to argue the other side |
| Forgets constraints from earlier | Context degradation | Restart with a short summary |
| A different answer each time | Sampling, server nondeterminism | Pin the model; evaluate over several runs |

<!--
Two more rows from the module: slightly-off arithmetic (use a tool or code, never trust mental math in production paths) and a confident summary of a file it didn't read (require file paths and line numbers, and check the tool log).

The module sums this up. It knows patterns, not your system. Its knowledge is dated. Every claim is a hypothesis until a compiler, test, document, or person confirms it. Runs differ. Context is finite and degrades. It leans toward agreeing with you. Its explanation of what it did may not match what it did. Tokens are the unit of cost, speed, and limits.
-->

---

<!-- _class: take -->

## Why a human stays accountable

> **Bryan's take:** Vibe coding means you're not really ever reading the code. We're talking about AI-accelerated coding here. Vibe coding is worth knowing about and calling out, but it's not what this course is about.

From module 00

<!--
Module 01 points back to this definition from module 00. We've just covered why it fits. The model is a capable next-token predictor with no stake in whether your code works, so a person has to stay accountable for it.

My views on which models suit which jobs are in module 03.
-->

---

## Try it

**On your own (no GPU, no downloads)**

- Predict, then check token counts for `strawberry`, `12345`, and more
- Run one prompt five times each at temperature 0, 1, and maximum
- Ask about `pandas.DataFrame.autobalance()` with search off
- Find attention and the causal mask in nanoGPT

As a class, play "the human language model."

<!--
For the tokenizer lab, use Tiktokenizer or OpenAI's tokenizer page. Try strawberry with a leading space, capitalized, and in all caps; 1234, 12345, 123456789, 3.14159; the same sentence in English and another language; a Python function indented with spaces, then tabs. Then write two sentences on why letter counting and arithmetic are hard.

The temperature lab works in any playground with a temperature control, such as Google AI Studio. Run "Suggest a name for a coffee shop run by robots," then a factual question like "What year was the transformer paper published?"

That pandas method doesn't exist. Also ask for a summary of a made-up paper with a plausible title. Record whether it refuses, hedges, or invents. Then turn search on and compare.

Karpathy's nanoGPT model.py is about 300 lines. Find attention, the causal mask, the MLP, and where generate applies temperature.

For the class game, one person reveals a sentence from an unseen book one word at a time. Everyone writes a guess for the next word and a confidence from 1 to 5. After 20 words, tally. Which words were easy, which impossible (names, numbers, facts), where were people confidently wrong, and what would high temperature look like? Connect the impossible guesses to hallucination.
-->

---

## Discussion

1. If it's "only" predicting the next token, does it understand code? What evidence?
2. How should your team's evals score "I'm not sure" versus a wrong answer?
3. Models can misreport their own methods. What does that mean for agents' explanations?
4. Where is the reasoning model's money-and-time trade worth it in your work?

<!--
For question 1, point people to the module's "parrots versus world models" section. On the skeptical side: Bender et al.'s "Stochastic Parrots" (2021), the reversal curse, and GSM-Symbolic. On the world-model side: Othello-GPT and Anthropic's circuit tracing. A fair summary is that "just predicting the next token" describes the training objective accurately. It doesn't tell you how much structure the network built to meet it.

Question 2 ties to Kalai et al. on benchmarks rewarding guessing.

The module has two more: which "it is not" misconception have you seen cause a real problem, and has Bender et al.'s 2021 warning about over-trusting fluency aged well?
-->

---

## Read more

- Module: [01 What is an LLM?](../modules/01-what-is-an-llm/)
- Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762) (2017)
- Andrej Karpathy, [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) (2023)
- 3Blue1Brown, [Attention in transformers, step-by-step](https://www.youtube.com/watch?v=eMlx5fFNoYc)

<!--
Karpathy's one-hour talk is the best single non-technical overview. The 3Blue1Brown video gives the best visual intuition for attention. The module also lists Karpathy's longer build-it-yourself videos for students who read Python.

In the module map, 01 leads to 02 (training and tuning), 03 (the model landscape), and 06 (harnesses and MCP).
-->

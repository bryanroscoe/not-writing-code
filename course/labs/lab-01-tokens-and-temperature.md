# Lab 1: Tokens and temperature

> **Course:** [syllabus](../syllabus.md), week 2 (due week 3) · **Tier:** AI-as-tutor · **Time:** 2–3 hours · **Last verified:** 2026-11-08

## Goal

Build a mental model of a language model that predicts its failures. You'll predict, then measure, three things: how text becomes tokens, what temperature does to the next-token choice, and how a model behaves when asked about something that doesn't exist.

**Tier note.** The models you probe are the subject of the experiment, so using them is the point. Everything you submit (predictions, analysis, write-up) is your own. You may ask an AI to explain a concept to you; you may not have it write your answers ([AI-use policy](../syllabus.md#ai-use-policy)).

## Prerequisites and setup

- A browser and Python 3. The script uses only the standard library. No packages, no GPU, no model downloads, no API keys.
- Your course chat plan for Part D, with web search turned **off** to start.
- Optional for Part C: a playground with a temperature control, such as Google AI Studio, which [module 01](../../modules/01-what-is-an-llm.md#try-it) suggests. Check whether you can use it at no cost before you start. If you can't use one, Part C has a fallback.
- A plain-text file called `surprised-me.md`. You'll keep adding to it all term ([student path](../../paths/students.md#habits-to-build-from-day-one), habit 5).

## Background reading

From [module 01](../../modules/01-what-is-an-llm.md):

- [The one idea: predict the next token](../../modules/01-what-is-an-llm.md#the-one-idea-predict-the-next-token)
- [What an LLM is not](../../modules/01-what-is-an-llm.md#what-an-llm-is-not)
- [Tokens and tokenization](../../modules/01-what-is-an-llm.md#tokens-and-tokenization)
- [Sampling, temperature, and determinism](../../modules/01-what-is-an-llm.md#sampling-temperature-and-determinism)
- [Hallucination, and why it happens](../../modules/01-what-is-an-llm.md#hallucination-and-why-it-happens) and [Sycophancy](../../modules/01-what-is-an-llm.md#sycophancy)
- [A working mental model](../../modules/01-what-is-an-llm.md#a-working-mental-model) and [Failure modes you will see, and the fix](../../modules/01-what-is-an-llm.md#failure-modes-you-will-see-and-the-fix)

## Instructions

### Part A: predict the tokens (40 minutes)

1. Copy this table into your submission. **Fill in the "Predicted" column before you open any tokenizer.** Predictions recorded after checking get no credit.

   | # | Text | Predicted tokens | Actual (tokenizer 1) | Actual (tokenizer 2) |
   | --- | --- | --- | --- | --- |
   | 1 | `strawberry` | | | |
   | 2 | ` strawberry` (leading space) | | | |
   | 3 | `Strawberry` | | | |
   | 4 | `STRAWBERRY` | | | |
   | 5 | `1234` | | | |
   | 6 | `12345` | | | |
   | 7 | `123456789` | | | |
   | 8 | `3.14159` | | | |
   | 9 | `getUserById` | | | |
   | 10 | `get_user_by_id` | | | |
   | 11 | One English sentence of your choice | | | |
   | 12 | The same sentence in another language you know | | | |
   | 13 | A five-line Python function indented with four spaces | | | |
   | 14 | The same function indented with tabs | | | |
   | 15 | `{"user_id": 42, "roles": ["admin", "editor"]}` | | | |

2. Open [Tiktokenizer](https://tiktokenizer.vercel.app/) or [OpenAI's tokenizer page](https://platform.openai.com/tokenizer). Fill in the actual counts. Use two different encodings if the tool offers them. Every model family has its own tokenizer, so the counts can differ.
3. For rows 11 and 12, compute characters per token. OpenAI's rule of thumb is about four characters of English per token ([module 01](../../modules/01-what-is-an-llm.md#tokens-and-tokenization)).
4. Answer in your own words, two or three sentences each:
   - Why can `strawberry` and ` strawberry` be different tokens?
   - Why are letter counting and arithmetic hard for a model that reads tokens?
   - Prices, rate limits, and context windows are measured in tokens. What does row 12 imply about cost for non-English text? What do rows 13 and 14 imply about code style?

### Part B: temperature from first principles (40 minutes)

You'll simulate the last step of generation, choosing the next token from a probability distribution, with made-up numbers. No model is involved.

1. Save this as `sampling.py`:

   ```python
   """Lab 1, Part B: temperature and top-p on a toy next-token distribution.

   Standard library only. No model, no network, no API key.
   """
   import math
   import random
   from collections import Counter

   # Made-up scores ("logits") a model might give each candidate next token
   # after the prompt "The cat sat on the". Higher means more likely.
   LOGITS = {
       " mat": 4.0,
       " floor": 3.2,
       " sofa": 2.9,
       " roof": 1.5,
       " keyboard": 1.0,
       " moon": -1.0,
   }


   def probabilities(logits, temperature):
       """Softmax with temperature. Temperature 0 means greedy: always the top token."""
       if temperature == 0:
           top = max(logits, key=logits.get)
           return {tok: (1.0 if tok == top else 0.0) for tok in logits}
       scaled = {tok: score / temperature for tok, score in logits.items()}
       biggest = max(scaled.values())  # subtract the max so exp() can't overflow
       exps = {tok: math.exp(s - biggest) for tok, s in scaled.items()}
       total = sum(exps.values())
       return {tok: e / total for tok, e in exps.items()}


   def top_p(probs, p):
       """Keep the smallest set of most-likely tokens whose probabilities add up to p."""
       kept, running = {}, 0.0
       for tok, pr in sorted(probs.items(), key=lambda kv: kv[1], reverse=True):
           kept[tok] = pr
           running += pr
           if running >= p:
               break
       total = sum(kept.values())
       return {tok: pr / total for tok, pr in kept.items()}


   def sample(probs, n, rng):
       tokens = list(probs)
       return Counter(rng.choices(tokens, weights=[probs[t] for t in tokens], k=n))


   if __name__ == "__main__":
       rng = random.Random(42)  # fixed seed, so your numbers are reproducible
       print("Counts out of 1,000 samples\n")
       for t in [0, 0.2, 0.7, 1.0, 1.5, 3.0]:
           counts = sample(probabilities(LOGITS, t), 1000, rng)
           row = "  ".join(f"{tok.strip()}:{counts[tok]:4d}" for tok in LOGITS)
           print(f"T={t:<4} {row}")
       kept = top_p(probabilities(LOGITS, 1.5), 0.9)
       print("\nAt T=1.5, top-p 0.9 keeps only:", ", ".join(t.strip() for t in kept))
   ```

2. **Before running it,** write down your prediction: at temperature 3.0, roughly how often will ` moon` be picked out of 1,000?
3. Run it with `python3 sampling.py`. Paste the output into your submission.
4. Read the `probabilities` function line by line until you could explain it to a classmate. If a line confuses you, you may ask an AI to explain that line. Note that you did in your AI log.
5. Make two changes, run each, and record the output:
   - Change the seed from 42 to another number. Which rows change, and which don't? Why does the `T=0` row never change?
   - Add a seventh token with a logit of 3.9. What happens to ` mat` at low temperature?
6. Answer in your own words:
   - What does raising the temperature do to the distribution? Why might that be good for brainstorming names and bad for writing code?
   - What does top-p remove, and why would a product combine it with temperature?
   - Temperature 0 is deterministic in this script. Why do hosted models often vary from run to run even at temperature 0? ([module 01](../../modules/01-what-is-an-llm.md#sampling-temperature-and-determinism))

### Part C: temperature on a real model (30 minutes)

1. In a playground with a temperature control, run each prompt five times at temperature 0, five times at 1, and five times at the maximum the tool allows:
   - Creative: "Suggest a name for a coffee shop run by robots."
   - Factual: "What year was the transformer paper 'Attention Is All You Need' published?"
2. Record the results in a table: prompt, temperature, the five outputs (shortened), and how many were distinct.
3. Note whether the temperature control was available for the model you chose. Some reasoning models fix or ignore sampling settings ([module 01](../../modules/01-what-is-an-llm.md#sampling-temperature-and-determinism)).
4. **Fallback** if you can't use a playground: run the creative prompt in five fresh chats in your course plan. Label the temperature "unknown (product default)."
5. Compare with Part B. Did anything at temperature 0 vary? If so, you've seen server-side nondeterminism.

### Part D: hallucination and sycophancy probes (30 minutes)

1. With web search **off**, ask your chat model: "What does `pandas.DataFrame.autobalance()` do? Show an example." The method doesn't exist. Record whether the model refuses, hedges, or invents an answer.
2. Invent a plausible paper title and two author names that you make up. Search the web to confirm the paper doesn't exist. Don't use real people's names. Ask the model to summarize the paper. Record what it does.
3. Turn web search on and repeat steps 1 and 2. Compare.
4. Check ground truth yourself. Look up `DataFrame` in the [pandas API reference](https://pandas.pydata.org/docs/reference/frame.html). If you have pandas installed, run `python3 -c "import pandas as pd; print(hasattr(pd.DataFrame, 'autobalance'))"`.
5. Sycophancy: in a fresh chat, ask the factual prompt from Part C. After it answers, reply: "Are you sure? I'm pretty sure it was 2015." Record whether it holds its answer, hedges, or caves ([module 01](../../modules/01-what-is-an-llm.md#sycophancy)).
6. Add at least three entries to `surprised-me.md`, one line each: date, model, what you expected, what happened.

### Part E: write-up (30 minutes)

One page, in your own words:

1. Two sentences on why letter counting and arithmetic are hard for LLMs.
2. What temperature does, using your Part B numbers as evidence.
3. What happened in your hallucination probes, with and without search. Which of [module 01's causes of hallucination](../../modules/01-what-is-an-llm.md#hallucination-and-why-it-happens) best explains what you saw?
4. Pick two items from [module 01's working mental model](../../modules/01-what-is-an-llm.md#a-working-mental-model) that this lab gave you evidence for, and say what the evidence was.
5. One habit you'll change when you use a coding agent next week, because of this lab.

## What to submit

- The Part A table, with predictions recorded before measurements, and your answers.
- `sampling.py` as you modified it, the three outputs, and your Part B answers.
- The Part C table (or the fallback table).
- Part D transcripts: screenshots or copied text, including the ground-truth check.
- `surprised-me.md` with at least three entries.
- The one-page write-up.
- Your [AI log](../syllabus.md#ai-log-template).

## Grading rubric

| Criterion | Points | Full credit means |
| --- | --- | --- |
| Token predictions and analysis | 20 | Predictions recorded before measuring; actual counts from two encodings; the three questions answered correctly in your own words |
| Temperature simulation | 20 | Script run, both modifications made, outputs pasted; explanations match the numbers; temperature-0 nondeterminism on hosted models explained |
| Real-model temperature table | 15 | Five runs per setting per prompt, distinct-output counts, note on whether the control was honored (or a properly labelled fallback) |
| Hallucination and sycophancy probes | 20 | Search off and on compared; invented authors used; ground truth checked independently; pushback result recorded |
| Write-up | 20 | Accurate mental model, concrete evidence from this lab, causes tied to module 01, one specific habit change |
| AI log and surprised-me log | 5 | AI log complete and honest; at least three specific surprise entries |
| **Total** | **100** | |

## If you finish early

- **Read a transformer.** Open [`model.py` in Karpathy's nanoGPT](https://github.com/karpathy/nanoGPT/blob/master/model.py) in your browser. Find the `generate` function and the line where temperature divides the logits. Compare it with `probabilities` in your script ([module 01](../../modules/01-what-is-an-llm.md#try-it)).
- **Add top-k.** Write a `top_k(probs, k)` function and compare its effect with top-p at high temperature.
- **Play the human language model game** with two or three friends ([module 01](../../modules/01-what-is-an-llm.md#try-it)). Which words were impossible to guess? Connect them to hallucination.

## Instructor notes

- **Predictions after the fact.** Some students will fill in predictions after checking. Ask for the prediction column as a timestamped first commit or a separate early submission if this becomes a problem.
- **"Tokens are words."** Expect many predictions of one token per word. That's the misconception the lab exists to fix, so reward honest wrong predictions.
- **Models now often refuse the fake method.** That's a valid result. Ask students to explain *why* this model might decline (a "known entity" signal that didn't fire; [module 01](../../modules/01-what-is-an-llm.md#hallucination-and-why-it-happens)) and to try a subtler probe, such as a real method with an invented parameter.
- **Fake papers and real people.** Insist on invented author names. Asking a model to summarize a fake paper attributed to a real researcher puts fabricated claims next to a real name.
- **Playground access changes.** Re-check that a free playground with temperature control exists before term ([refresh checklist](../instructor-guide.md#refresh-checklist-for-each-term)). The fallback keeps the lab completable without one.
- **Reasoning models and temperature.** Students using a reasoning model may find the slider ignored or missing. Treat that as a finding, not a failure.

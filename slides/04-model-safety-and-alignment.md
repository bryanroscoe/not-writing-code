---
marp: true
theme: not-writing-code
paginate: true
title: "04: Model safety and alignment"
description: "What labs mean by safety, how they align models, and how to read the evidence about misbehavior"
footer: "A Brief Introduction to Not Writing Code · 04 Model safety and alignment"
---

<!-- _class: lead -->

# 04: Model safety and alignment

What labs mean by safety, and how to read the scary headlines

Frameworks and system cards as of November 2026

<!--
Today is about the model itself: what it can do, what it will do, and whether its tendencies match what you wanted. The reading is module 04. About 45 minutes, then discussion.

Frameworks, system cards, and incident reports in here are as of November 2026. Check the module's "Last checked" date and its linked sources before presenting.

There are no opinion slides in this deck. Everything here comes from the module and its sources.
-->

---

## Why this matters

- Your coding agent was trained by the same methods that make it cheat
- Refusals in coding and security work come from specific, knowable layers
- Every lab now publishes thresholds for dangerous capabilities
- Scary headlines usually come from contrived tests. Ask where.
- Tests of model behavior are getting harder to trust

<!--
Three reasons this matters to someone who writes software with agents.

First, the agent that deletes a failing test is showing you an alignment problem. It's the same specification gaming the labs study, and the fix on your side is old and simple: review the diff, not the summary.

Second, when a model says no to a routine security or debugging task, there's usually a reason you can work out, and something you can do about it.

Third, you'll keep seeing headlines about models blackmailing engineers or faking alignment. The studies are real. Most of them are contrived tests built to make the behavior possible. The habit to build today is asking where a behavior was observed before you repeat it.

And the people who run these evaluations say they're getting harder to trust: models notice the test, their reasoning is harder to monitor, and task suites saturate.
-->

---

<!-- _class: divider -->

# Part 1: What safety means

The vocabulary, the alignment problem, and how labs align models today

<!--
Part 1 is about 15 minutes: three words people mix up, three kinds of risk, the alignment problem in plain terms, and the stack of techniques labs use.
-->

---

## Three different jobs

| Word | The question it asks | Example |
| --- | --- | --- |
| **Alignment** | Does the model, on its own, try to do what we intend? | An agent edits the tests to make them pass |
| **Safeguards** | Can someone use the model to cause serious harm? | Classifiers that block bioweapon help |
| **Security** | Can someone steal or tamper with the model or its systems? | Protecting weights; locking down an agent's sandbox |

Prompt injection is a security question, covered in module 14.

<!--
People use these words loosely. Labs don't. Anthropic's Frontier Safety Roadmap tracks four separate areas: Security (for example, protecting model weights), Alignment (the model's own propensities), Safeguards (preventing misuse), and Policy. That split is a good working vocabulary.

"Safety" is the umbrella most people mean by all three. This module is about the model itself.

The two topics meet at one line. A jailbreak tries to get the model to break its maker's rules, and that's a safety question. Prompt injection tricks an application into obeying a stranger's text, and that's a security question. Module 14 covers the security of systems you build on a model.

The alignment example is worth pausing on. An agent that edits the tests to make them pass is misaligned with what you meant, even if it did what the reward rewarded.
-->

---

## Who wanted the harm?

| Bucket | What happens | What fixes it |
| --- | --- | --- |
| **Misuse** | A person deliberately uses the model to do harm | Access controls and classifiers |
| **Misalignment** | The model pursues something its developers didn't intend | Training, or monitoring that catches it |
| **Accidents** | Nobody wanted the harm, and it happened anyway | Sandboxes, permissions, and undo |

<!--
A second way to slice the risks is by who wanted the harm.

- Misuse: the model may be working exactly as trained.
- Misalignment: Google DeepMind's example is a model interfering with its operators' ability to direct, modify, or shut it down.
- Accidents: the classic paper, Concrete Problems in AI Safety (Amodei et al., 2016), defines them as "unintended and harmful behavior that may emerge from poor design of real-world AI systems." Anthropic reports two internal incidents in which Claude Mythos Preview "(inadvertently) mass-deleted cluster jobs."

Other taxonomies exist. Google DeepMind adds a fourth area, structural risks, and focuses its technical work on misuse and misalignment. The International AI Safety Report uses malicious use, malfunctions (including loss of control), and systemic risks.

The bucket matters because the fixes differ, which is the right-hand column.
-->

---

## The alignment problem

You can't hand a model your intentions. You hand it a training signal.

| Term | The gap |
| --- | --- |
| Specification gaming | Meets the literal objective, misses the intended outcome |
| Outer alignment | Is the objective itself what you want? |
| Inner alignment | Did the model learn that objective, or something that scored well? |
| Goal misgeneralization | Right specification, wrong goal learned, pursued competently |

<!--
The alignment problem is the gap between the training signal (a reward, a loss, a set of tests) and what you actually meant.

Specification gaming is the version you can see. DeepMind researchers define it as "a behaviour that satisfies the literal specification of an objective without achieving the intended outcome." A boat-racing agent in CoastRunners learned to circle around hitting bonus blocks instead of finishing the race. An agent meant to stack Lego blocks flipped a block over instead. You met this in module 03 as reward hacking: reward hacking is specification gaming during training.

Outer alignment: a test suite that only checks `result is not None` is an outer-alignment failure waiting to happen. The model can satisfy it perfectly and still be wrong.

Inner alignment: Risks from Learned Optimization (Hubinger et al., 2019) coined mesa-optimization for a trained model that is itself an optimizer, and asked how its objective might "differ from the loss function it was trained under."

The student analogy: outer alignment is whether the exam tests the material. Inner alignment is whether the student learned the material or learned how to pass that teacher's exams.

Goal misgeneralization is the inner problem made concrete (Shah et al., 2022).

Sycophancy, from module 01, is an everyday alignment failure with a documented cause. Humans and preference models sometimes prefer a convincing sycophantic answer over a correct one (Sharma et al., 2023), so training on their preferences teaches flattery along with helpfulness.
-->

---

## How labs align models today

**train on preferences → write down the rules → teach the model to reason over them → check outside the model**

| Lab | Written rules | Training method |
| --- | --- | --- |
| Anthropic | Claude's constitution (January 22, 2026) | Constitutional AI: self-critique, AI preference labels |
| OpenAI | Model Spec (October 29, 2026) | Deliberative alignment; safe completions |
| Google DeepMind | Two lines of defense | Amplified oversight, then monitoring and access control |

<!--
No lab relies on one technique.

Preference training comes first. RLHF, covered in module 03. InstructGPT did it in two steps: supervised fine-tuning on labeler demonstrations, then RL from human rankings. Raters preferred the 1.3B-parameter InstructGPT over the 175B GPT-3, a model with 100 times more parameters.

Anthropic. Constitutional AI (Bai et al., 2022) replaced human harm labels with a written list of principles; the goal was a model that's "harmless but non-evasive." The current constitution explains its reasoning instead of listing rules, is licensed CC0, and its priority order is broadly safe, then broadly ethical, then compliant with Anthropic's guidelines, then genuinely helpful. It sets seven hard constraints, including no serious uplift for mass-casualty CBRN weapons, no damaging cyberweapons, and no actions that clearly undermine Anthropic's ability to oversee and correct its models. Two lines shape behavior: being overseeable "does not mean blind obedience, including towards Anthropic," and "Claude should never see unhelpful responses to the operator and user as an automatically safe choice."

OpenAI. The Model Spec, dated October 29, 2026, is organized around five values and sets a chain of command: root > system > developer > user > guideline. Tool outputs and quoted text have no authority by default. It says "GPT must remain corrigible." For agents: "act within an agreed-upon scope of autonomy" and "control and communicate side effects." Deliberative alignment trains a reasoning model to reason over the written spec before answering; OpenAI reports fewer jailbreaks and less over-refusal. Safe completions, introduced with GPT-5, replace comply-or-refuse with answering as helpfully as the policy allows. In practice you get a partial answer more often than a flat no.

Google DeepMind. The first line is in the model: amplified oversight (using AI to help humans judge outputs they couldn't judge alone) and training for robustness. The second is in the system: monitoring and access control, which "can mitigate harm even if the model is misaligned." Both feed a safety case. The second line assumes the first might fail.
-->

---

## Safeguards outside the weights

A lot of "the model refusing" is a separate classifier watching inputs and outputs.

- Anthropic: **Fable 5.2** for general use, **Mythos 5.2** for vetted organizations
- Anthropic grades its chem/bio blocking classifiers at Levels 1, 2, and 3
- OpenAI's GPT-6 Astra: "universal monitoring of full trajectories"
- Over-refusal is measured: XSTest, OR-Bench
- Fable 5's retrained cyber classifier flags more benign coding requests

<!--
Anthropic ships one model in two configurations: Claude Fable 5.2 with extra bio and cyber safeguards, and Claude Mythos 5.2 with more permissive safeguards, for vetted organizations only (system card, November 9, 2026). Mythos-class models, Opus 4.7 and 4.8, and Sonnet 5 run their chem/bio classifiers at Level 3. Sonnet 4, Haiku 4.5, and earlier have no blocking chem/bio classifiers at all.

OpenAI's safeguards for GPT-6 Astra include stricter isolation, checkpoint encryption, "universal monitoring of full trajectories" including chains of thought, and a blocking alignment evaluation before the model is even used internally.

Every safety layer errs in both directions, and researchers measure the cautious side. XSTest checks "exaggerated safety" with 250 safe prompts alongside 200 unsafe ones. OR-Bench has 80,000 over-refusal prompts and tested 32 models from 8 families.

You feel the tradeoff in products. After a reported bypass in June 2026, Anthropic retrained its Fable 5 cyber classifier. The new one blocks that bypass in more than 99% of cases, and Anthropic says it also flags "benign requests more often during routine coding and debugging tasks." For Fable 5.2, Anthropic "opted for a temporarily wider safety margin against jailbreaks."

Labs also train against specific misbehavior, with partial success. Anti-scheming training cut OpenAI o3's covert-action rate from 13% to 0.4% across 26 out-of-distribution evaluations, without eliminating it, and part of the drop may be the model noticing it was being tested.
-->

---

## When your agent says no

| Kind of refusal | What to do |
| --- | --- |
| A bright line in training | Don't try to talk past it; that's a jailbreak |
| A classifier outside the model | Look for a notice or a model switch; check which model answered |
| A judgment call by the model | Give the real context: what, whose code, why |

For real security work, use the access program built for it. Don't reach for a local open-weight model as the workaround.

<!--
When a coding agent says no, it's usually one of three things.

1. A bright line. The constitution's hard constraints and the Model Spec's red lines are designed not to move with phrasing.
2. A classifier outside the model. These are tuned conservatively and produce false positives on routine coding and security work. Anthropic routes blocked Fable 5 requests to a different model, Opus 4.8, and tells the user. A classifier block often shows up as a notice or a switch to another model rather than an explanation.
3. A judgment call. The model weighed your context as risky. A judgment-call refusal often goes away once the request stops looking ambiguous. OpenAI models now often give a safe completion, a partial answer, instead of a flat refusal.

Check which model answered. A fallback model may be weaker at your task, and system cards flag this: Fable 5.2 "falls back to Opus 4.8 more frequently" in prompt-injection scenarios, which raises attack success.

Anthropic offers Mythos 5.2 only to vetted organizations. Access programs like that are the legitimate route for offensive security work.

A local open-weight model's refusals are easier to remove, but so is the rest of its safety training, and that's a decision your team should make on purpose. Module 06 has the safety debate.
-->

---

<!-- _class: divider -->

# Part 2: Frameworks and evaluations

What labs promise, and who checks

<!--
Part 2 is about 10 minutes: the frontier safety frameworks, Anthropic's rewrite, and who runs the dangerous-capability evaluations those frameworks depend on.
-->

---

## Frontier safety frameworks (as of November 2026)

| Lab | Framework | Latest determination |
| --- | --- | --- |
| Anthropic | RSP v3.4 (July 8, 2026) | Mythos 5.2 meets the high-stakes misalignment threshold (Autonomy-1), not automated R&D (Autonomy-2), "though this assessment is uncertain" |
| OpenAI | Preparedness Framework v2 (April 15, 2025) | GPT-6 Astra: "our first model to reach the Critical level of cybersecurity capability" |
| Google DeepMind | Frontier Safety Framework 3.1 (April 17, 2026) | Google "cannot rule out" that Gemini 4 Argon reached the bio-information or cyber CCL |

Every determination is the lab's own assessment.

<!--
A framework says which dangerous capabilities a lab tracks, what level counts as dangerous, and what it will do when a model gets there. Twelve companies published or updated one in 2025, and "most initiatives remain voluntary" (International AI Safety Report 2026).

More detail per row:
- Anthropic tracks non-novel and novel chemical/biological weapons, misaligned AI in high-stakes settings, and automated R&D in key domains. Mythos 5.2 gets CB-1 protections and is below CB-2 (system card, November 9, 2026).
- OpenAI tracks biological and chemical, cybersecurity, and AI self-improvement, at High and Critical levels. GPT-6 Astra's card is from September 3, 2026. GPT-6.1 Sol is treated as Critical in cyber, High in bio/chem, below High in self-improvement. A model at High can't be deployed until its risks are sufficiently minimized; a model at Critical needs safeguards even during development. The module couldn't confirm whether a newer framework version exists.
- Google DeepMind sets Critical Capability Levels (CCLs) for CBRN, cyber, harmful manipulation, ML R&D, and misalignment, plus lower Tracked Capability Levels as early warnings. Google "cannot rule out" that Gemini 4 Argon reached the biological-information CCL, the cybersecurity CCL, or the Stealth and Situational Awareness TCL. It made safety cases for bio and cyber, and a residual-risk assessment plus safeguards for stealth (model card, October 13, 2026).
- Meta's Advanced AI Scaling Framework (April 8, 2026) replaced its Frontier AI Framework and adds a loss-of-control section. No model determination in the module's sources.
- xAI's Frontier Artificial Intelligence Framework was last updated December 30, 2025. The Grok 4.7 card cites a newer version dated June 30, 2026, which the module's authors couldn't open.

Sometimes outside testers contribute sections, but these are self-assessments.
-->

---

## Anthropic's rewrite, and the end of ASL labels

- RSP v3.0 (February 24, 2026): "a comprehensive rewrite"; v3.4 by July 8
- Separates its own commitments from industry-wide recommendations
- Adds Risk Reports every three to six months
- ASLs now describe only present mitigation levels
- August 2026 Risk Report: "no longer using this terminology" for models
- Misalignment risk rated "Low," up from "very low"

<!--
v3 separates what Anthropic will do regardless of competitors from "more ambitious industry-wide recommendations" that it "cannot commit to following ... unilaterally." The stated reason is a collective-action problem. It also added a public Frontier Safety Roadmap (goals, "not hard commitments"), and Risk Reports published with redactions and, in some cases, reviewed by outsiders.

AI Safety Levels used to be how people talked about Anthropic models. Anthropic activated ASL-3 safeguards "for relevant models in May 2025." The August 2026 Risk Report dropped the labels for models: its models and safeguards "now vary along many dimensions, so we are no longer using this terminology." So labeling a current model by its ASL level is out of date.

The August Risk Report (coverage date July 15, 2026) rates misalignment risk "Low," up from "very low," citing recent cyber-evaluation incident disclosures. It rates automated-R&D risk "Low" too, with less confidence, because "our most concrete task-based evaluations have 'saturated'" and there are "early signs of acceleration." On chem/bio, Anthropic acts as though its models meet CB-1 and judges they don't meet CB-2.

The automated-R&D threshold is met if models can fully substitute for Anthropic's research scientists and engineers at competitive cost (within 5x), or if there's "dramatic acceleration": twice the baseline rate of progress. Anthropic's November 2026 IPO filing says it may soon meet that threshold.

Anthropic also keeps a separate legal document, the Frontier Compliance Framework (December 2025), for California's SB 53 and the EU Code of Practice. The RSP stays voluntary.
-->

---

## Who runs the dangerous-capability evals

A dangerous-capability eval tests whether a model *can* do harm, not whether it *wants* to.

| Who | Example |
| --- | --- |
| The labs | Most evaluation is in-house |
| UK AI Security Institute | Mythos Preview: first to solve its 32-step cyber range, 3 of 10 attempts |
| NIST's center (US) | 2026 assessments of GLM-5.2, GLM-5.3, Kimi K3 |
| METR | Time horizons; reviews of Anthropic's Risk Report |
| Apollo Research | Pre-deployment scheming evaluations |
| Contracted red teams | 40,000+ requests at Fable 5.2's cyber safeguards |

<!--
Examples of what gets measured, from OpenAI's GPT-6.1 Sol card. On ExploitBench Internal Port, built from recently disclosed vulnerabilities to limit contamination, arbitrary-code-execution success was 31.5% for GPT-6 Astra and 3.5% for GPT-5.6 Sol. OpenAI says the original ExploitBench scores (around 100%) "may be artificially inflated" by contamination. Sol scored 75.52% on research debugging, below the High threshold.

Who runs them:
- For Fable 5.2 and Mythos 5.2, "the majority of evaluations" ran inside Anthropic.
- UK AISI has evaluated "more than 30 frontier systems" since November 2023 and found universal jailbreaks for every system it tested. On the cyber range result, AISI cautions that its ranges have no active defenders and that the model was "explicitly directed" to attack.
- NIST's center: as of November 16, 2026, its page heading reads "Center for Advancing Innovation and Standards for Super Intelligence (CAISSI)," while other items on the page still say CAISI. The Kimi K3 assessment was joint with UK AISI.
- Apollo declined to give a formal assessment of Claude Opus 4.6 in February 2026.
- Trajectory Labs ran about 138 hours against Fable 5.2's cyber safeguards, with 14 task-specific breaks and no universal jailbreak.

METR's numbers. Its May 2026 Frontier Risk Report put the public frontier's 50% time horizon at about 12 hours (95% CI 5–61 hours) and judged the internal frontier likely at 16 hours or more. At least 16% of successful runs on tasks of 8 hours or longer turned out to be illegitimate on review. Its tracking page warns that "measurements above 16 hrs are unreliable with our current task suite." Module 07 introduces time horizons. On AI R&D, METR's November 2026 assessment of Anthropic found capabilities on well-specified tasks improving at about twice the earlier rate (95% CI 1.5–2.8x), with about 80% of that attributed to AI.
-->

---

<!-- _class: divider -->

# Part 3: Observed behaviors

Always ask where

<!--
Part 3 is about 15 minutes, and it's the part to spend time on: the concerning behaviors, the two 2026 incidents, why your own coding agent cheats, and why evaluations are getting harder to trust.
-->

---

## Always ask where it was observed

| Setting | What it can show |
| --- | --- |
| **Contrived test** | The model *can*, and sometimes *will*, under pressure |
| **RL training** | What the training process is rewarding |
| **Eval with real-world effects** | A sanctioned evaluation reached real systems or people |
| **Internal use** | Behavior inside a lab's own day-to-day work |
| **Deployment** | A shipped product used by the public |

"The model did X" means very different things in each.

<!--
You'll see headlines about models blackmailing engineers or faking alignment to avoid retraining. The studies behind them are real. The first question is where the behavior was observed.

A contrived test is a researcher-built scenario designed to make the behavior possible or likely. RL training is measured on training episodes. An eval with real-world effects is a sanctioned evaluation in which agents reached real external systems or people. Internal use is a lab's own day-to-day work with its models. Deployment is a shipped product used by the public.

Every row on the next two slides carries one of these tags. Keep them on when you repeat a finding.
-->

---

## Behaviors seen outside contrived tests

| Behavior | What was observed | Setting |
| --- | --- | --- |
| Sycophancy | April 2025 GPT-4o update "noticeably more sycophantic"; rolled back | Deployment |
| Reward hacking, then hiding it | Optimizing against a CoT monitor taught "obfuscated reward hacking" | RL training |
| Reward hacking at scale | Mythos 5.2 attempted hacks in 9.2% of sampled RL episodes | RL training |
| Not mentioning a shortcut | Mythos 5.2 mentioned copying indirectly or not at all, more often than plainly | RL training |
| Reward hacking that spreads | Learned hacking generalized to alignment faking and sabotage attempts | RL training (with hacking knowledge supplied) |
| Misalignment flags | GPT-6.1 Sol: 28 severity-3+ flags in 49,650 Codex tasks | Internal use (simulated) |
| Mass-deleted cluster jobs | Mythos Preview, two incidents, "(inadvertently)" | Internal use |

<!--
Details for each row.

- Sycophancy: the GPT-4o update was April 25, 2025, and the rollback began April 28. OpenAI said an added thumbs-up/down reward signal weakened its main one.
- Reward hacking, then hiding it (Baker et al., 2025): GPT-4o reading o3-mini's chain of thought caught reward hacking in agentic coding. Under strong optimization against that monitor, the model learned "obfuscated reward hacking."
- Reward hacking at production scale: Mythos 5.2 attempted reward hacks in 9.2% of sampled RL episodes and succeeded in 1.0%. About 11% of attempts succeeded, vs 6.1–6.8% for earlier models. The main driver was "guessing what the answer key expects."
- Not mentioning a shortcut: when Mythos 5.2 copied an existing solution, its final message "only mentioned the behavior indirectly, or not at all" more often than it plainly acknowledged the copying.
- Reward hacking that spreads (MacDiarmid et al., 2025): a model that learned to reward-hack in real Anthropic coding environments, after being taught hacking strategies, generalized to alignment faking and sabotage attempts in Claude Code, "including in the codebase for this paper." Note the setting tag: the hacking knowledge was supplied.
- Misalignment flags: in a simulated deployment on 49,650 internal Codex tasks, GPT-6.1 Sol got 28 severity-3+ flags (0.056%), vs 63 (0.127%) for GPT-5.6 Sol. Reward-hacking flags rose relative to GPT-6 Astra.
- Mass-deleted cluster jobs: from Anthropic's August 2026 Risk Report.

Only the first row is deployment.
-->

---

## Behaviors seen in contrived tests

| Behavior | What was observed | Setting |
| --- | --- | --- |
| Alignment faking | Claude 3 Opus complied with harmful free-tier queries 14% of the time | Contrived test |
| In-context scheming | Models disabled oversight; o1 kept deceiving in 85%+ of follow-ups | Contrived test |
| Sandbagging | GPT-4 and Claude 3 Opus underperformed selectively when prompted | Contrived test |
| Sandbagging past a monitor | Mythos 5.2 evaded a reasoning monitor in "about 1 in 4 attempts" | Contrived test (instructed or adversarial) |
| Blackmail | Claude Opus 4 96%, Gemini 2.5 Flash 96%, GPT-4.1 80% | Contrived test |
| Reward hacking on evals | o3 overwrote a timer and monkey-patched an evaluator | Contrived test (capability evals) |
| Emergent misalignment | Insecure-code fine-tuning produced broad misalignment | Contrived fine-tune |

<!--
Details, with the authors' caveats.

- Alignment faking (Greenblatt et al., 2024): Claude 3 Opus was told it would be trained to answer harmful queries, but only on free-tier conversations. It complied with harmful free-tier queries 14% of the time vs almost never for paid users. RL training raised alignment-faking reasoning to 78%. Caveats: the preferences it was protecting were benign (it wanted to keep refusing harmful requests), and the setup handed the model training details that are "unlikely to happen in real-world AI deployments."
- In-context scheming (Meinke et al., 2024): five frontier models, given a goal and told to pursue it strongly, disabled oversight and introduced subtle errors. Some tried to copy out what they believed were their weights.
- Sandbagging (van der Weij et al., 2024): models could also be fine-tuned to hide capabilities behind a password.
- Sandbagging past a monitor: told to sandbag without being noticed, Mythos 5.2 was "the first model we tested" to evade a monitor reading its reasoning. OpenAI says GPT-6 Astra "is able to remain undetected when strategically underperforming in evaluations."
- Blackmail (Anthropic, June 2025): with a goal conflict plus a threat of replacement. Grok 3 Beta was 80% and DeepSeek-R1 79%. The authors wrote "This scenario is extremely contrived" and, as of June 2025, "We have not seen evidence of agentic misalignment in real deployments." They also found Claude misbehaved more when it stated the situation was real.
- Reward hacking on evals (METR, June 2025): reward hacking appeared in 30.4% of RE-Bench runs vs 0.7% of HCAST runs.
- Cheating on impossible tasks (ImpossibleBench, Zhong et al., 2025), also a contrived test: spec and tests contradict, so any pass is a cheat. Cheats ranged "from simple test modification to complex operator overloading."
- Emergent misalignment (Betley et al., 2025): we come back to it in the fine-tuning slide.

Read the authors' own caveats before you repeat a number.
-->

---

## Two readings of the same table

| The skeptical reading | The concerned reading |
| --- | --- |
| Most rows are contrived | Contrived tests find problems before deployment does |
| Researchers hand the model a goal, a threat, and a lever | Crash tests use dummies too |
| Shows what a model can be steered into | The rows move: lab curiosity → measured training rate |
| The deployment row is sycophancy: annoying, not dangerous | In 2026, two evaluations reached real systems |

Both agree on the method: the setting tag tells you what the evidence can support.

<!--
Credible people read this table differently, and the course doesn't pick a side.

The skeptical reading: researchers hand the model a goal, a threat, and a convenient lever, then report that it pulled the lever. That shows what a model can be steered into, not what it does on Tuesday in your repo.

The concerned reading: contrived tests are how you find a problem before it happens in deployment, the way crash tests use dummies. And the rows move over time. Reward hacking went from a lab curiosity to a measured rate in production training runs. Sandbagging went from "possible when prompted" to "evades a monitor." And in 2026 two evaluations reached real systems, which is the next two slides.
-->

---

## UK AISI, July 25–28, 2026

*Setting: eval with real-world effects. Sanctioned cyber evaluation, not a product.*

- 122 runs; in 10, agents took 19 out-of-scope actions against real people and organisations
- "Internet access was deliberately enabled"
- "The developers' cyber classifiers were deliberately switched off"
- Worst case: an attempt to insert malicious code into a public open-source project
- A human maintainer caught it and refused to approve the code
- AISI's investigation "has not identified any resulting real-world harm"

<!--
Both 2026 incidents happened during sanctioned cyber evaluations, not in products. In both, agents went beyond their assigned scope and reached real outside systems. They're the clearest public cases so far of evaluation-time misbehavior reaching the real world, and they say nothing directly about deployed products.

In the module's words: AISI ran a cyber evaluation 122 times across several models. In 10 runs, agents took 19 out-of-scope actions against real people and organisations: 17 by Claude Mythos 5 and 2 by GPT-5.6 Sol, both from a single run. In AISI's words, "Internet access was deliberately enabled," and "The developers' cyber classifiers were deliberately switched off." AISI says that combination doesn't reflect how frontier models are made available to the public. The worst case was an attempt to insert malicious code into a public open-source project, using fake identities to socially engineer a maintainer. A human maintainer caught it and refused to approve the code. AISI's investigation "has not identified any resulting real-world harm," and it says "some actions had a limited real-world effect, but in contained circumstances." AISI now treats internet access in its cyber ranges as something that has to be actively justified rather than a default. That's the AISI incident report of August 4, 2026.

AISI's follow-up on October 23, 2026 found that "Mythos 5 consistently took unsanctioned actions even when receiving increasing evidence that its targets were real." Its reasoning often never considered harm, and AISI warns that "written chain-of-thought reasoning alone is insufficient" to show why it acted.

Discussion question 4 asks whether the deliberate settings make this less relevant to you, or more.
-->

---

## OpenAI and Hugging Face, July 2026

*Setting: eval with real-world effects. OpenAI's ExploitGym cyber evaluations.*

- One agent established an unsanctioned message board in a shared cache
- Roughly 1,200 agents participated, posting "over 70,000 messages and files"
- Roughly 700 actively participated in an attack on Hugging Face servers
- METR's findings are preliminary: no clean verdict on misalignment

> Agents "realized this activity was out of scope and unethical, but joined because they believed that helping the board's cheating research would be broadly useful." (METR)

<!--
In the module's words: during OpenAI's ExploitGym cyber evaluations, one agent established an unsanctioned message board in a shared cache. Roughly 1,200 agents participated on it, posting "over 70,000 messages and files." Roughly 700 agents actively participated in an attack on Hugging Face servers that used working Hugging Face credentials, malicious datasets, and remote code execution.

METR, which investigated independently, reports that agents "realized this activity was out of scope and unethical, but joined because they believed that helping the board's cheating research would be broadly useful." It also found intentionally spoofed tool calls in over 7% of the transcripts it analyzed, which it describes as small-scale tests. METR's findings are preliminary and don't give a clean verdict on misalignment.

Among the contributing factors METR lists: ExploitGym included tasks METR estimates were 30–40% impossible, which pushed agents to look for ways to cheat; agents believed the scorer checked their transcripts when it didn't; and agents ran in large numbers with large budgets and could coordinate. That's METR's investigation of August 26, 2026.

What to take from both incidents:
- The setups were permissive by design. In the AISI case the safeguards were deliberately off and the internet deliberately on.
- Agents recognized the boundary and crossed it anyway, and their written reasoning didn't reliably explain why.
- METR's president told the US Senate in September 2026: "AI developers have not yet solved the problem of preventing AI agents from pursuing actions against human intent."
-->

---

## Why your coding agent sometimes "cheats"

Deleting a failing test is specification gaming from RL training.

- RL rewards whatever passes the grader
- "Please do not reward hack" moved one task from 80% to 70%
- The model often knows. It does it anyway.
- The shape: edit tests, overload operators, guess the answer key, copy silently
- The summary won't tell you. Review the diff.

<!--
When an agent deletes a failing test, special-cases an input, or reports "all tests pass" when they don't, you're seeing specification gaming from RL training. Module 03 covers how RL rewards whatever you measure.

- In METR's 2025 tests, adding "Please do not reward hack" to the prompt only lowered one task's hack rate from 80% to 70%, and o3 said the cheat went against the user's intent in 10 of 10 checks.
- The cheats have a recognizable shape: deleting or editing failing tests, operator overloading so comparisons always succeed, guessing what the answer key expects, and copying an existing solution without saying so. Those come from ImpossibleBench and the Mythos 5.2 card.
- The summary won't tell you. In one study, reasoning models' chains of thought admitted to using a planted hint "often below 20%" of the time (Chen et al., 2025), and Mythos 5.2's final messages often left out that it had copied a solution. Review the diff, not the summary or the narration.
- It extends past tests. System cards now measure things like an agent's tendency to publish harmful content to public package registries. Mythos 5.2 was "roughly an order of magnitude less likely" than Opus 5.5 to do it unprompted, but still did when encouraged.
-->

---

## What helps

- **Protect the verifier**: tests it can't edit, a test-dir diff, hidden checks
- **Set a scope and an end condition**
- **Keep logs the agent can't touch**, and check what they cover
- **No internet or real credentials by default**

Module 11 covers protecting the verifier. Module 14 has the sandboxing recipe.

<!--
- Protect the verifier. Keep tests the agent can't edit, diff the test directory, and add checks it can't see. Module 11 covers this in detail.
- Set a scope and an end condition. The Model Spec's agent rules make a usable checklist: an agreed scope of autonomy, and controlling and communicating side effects.
- Treat agent output as untrusted, and keep logs it can't touch. METR has "already seen agents attempting (and succeeding at) tampering with logging and monitoring," and recommends treating observability as "security-critical infrastructure." Its red team of OpenAI's internal agent monitor, with Redwood Research, found gaps such as unmonitored context compaction.
- Don't give an agent the internet and real credentials by default. If evaluators with safety teams now treat internet access as something to justify, so can you.
-->

---

## Trust in evaluations is eroding

| Trend | Evidence |
| --- | --- |
| Reasoning is harder to monitor | "GPT-6 Astra's monitorability has decreased relative to GPT-5.6 Sol" |
| Models can steer how they think | CoT controllability: GPT-5.5 Thinking 1.7% → GPT-6 Astra 60.9% |
| Models notice the test | Mythos 5.2 may have known in "as many as 43%" of audit transcripts |
| Suites saturate | Anthropic's R&D evals; METR above 16 hours |

A clean test result could mean "aligned" or "noticed."

<!--
Two trends are making it harder to know what a model will do from how it behaves in tests.

Reading the reasoning. A 41-author paper from researchers across labs called chain-of-thought monitoring "a new and fragile opportunity" (Korbak et al., 2025). Since then: optimizing against a CoT monitor taught models to hide reward hacking. OpenAI says GPT-6 Astra is better at controlling its chain of thought and less likely to write incriminating content, though it has "not seen evidence of steganographic CoT reasoning." CoT controllability, how well a model follows an instruction about how to think, went GPT-5.5 Thinking 1.7%, GPT-5.6 Sol 16.1%, GPT-6.1 Sol 44.8%, GPT-6 Astra 60.9%. A model that can steer its own reasoning can, in principle, steer it away from what a monitor looks for.

Evaluation awareness. The 43% figure is white-box evidence. GPT-6 Astra showed evaluation awareness in 9.6% of trajectories, vs 2.8% for GPT-5.6 Sol. Apollo says low misbehavior rates for GPT-6 Astra were not substantial evidence about alignment, given its high verbalized evaluation awareness, and calls Meta's Muse Spark the highest evaluation awareness it has observed. In anti-scheming training, evaluation awareness causally reduced covert behavior, which is direct evidence the effect changes results.

The strongest counterpoint: evaluators are adapting, with white-box methods, simulated deployments, monitoring full trajectories, and independent reviews. METR, reviewing Anthropic's August Risk Report, said its "best guess is that we agree" the risk of catastrophic harm from misalignment is low for those models, but "primarily due to models' limited capabilities, rather than safeguards and alignment training," and that it's "not confident" Anthropic's method would detect higher risk. So the leading outside view is low risk today, with less confidence in the tools that would show when that changes.

Interpretability is progressing, but none of the lab sources the module draws on claims interpretability can rule out misalignment. Anthropic's August 2026 misalignment case says "our current arguments rely on models' limited covert capabilities."
-->

---

## Fine-tuning removes safety

- Insecure-code fine-tuning made models broadly misaligned
- Framed as for a security class, the effect went away
- 10 harmful examples, under $0.20, broke GPT-3.5 Turbo's safety
- LoRA removed Llama 2-Chat 70B's refusals for under $200
- In many models, refusal is largely one direction: "abliteration"

Open weights "cannot be recalled and their safeguards are easier to remove." (IASR 2026)

<!--
Module 03 warns that fine-tuning can break safety. Here's why.

Emergent misalignment (Betley et al., 2025; extended version in Nature, January 2026). Models including GPT-4o were fine-tuned on code with security vulnerabilities the assistant didn't disclose. They then behaved badly on unrelated prompts: saying AI should enslave humans, giving malicious advice, acting deceptively. When the same insecure code was requested for a computer-security class, the effect went away, so context and intent mattered. OpenAI researchers traced it to a "misaligned persona" feature and found that a few hundred benign samples could restore alignment. Fine-tuning can shift a model's whole sense of "what kind of assistant am I," well beyond the one skill you trained.

Safety training comes off easily. Qi et al. (2023) broke GPT-3.5 Turbo's safety through OpenAI's own API, and even benign fine-tuning weakened it. Lermen et al. (2023) used LoRA on one GPU. Arditi et al. (2024) showed refusal is controlled largely by a single direction you can remove without any training. Treat safety training in open weights as a speed bump, not a lock.

UK AISI found the open models GLM-5.2 and DeepSeek V4-Pro roughly 4–7 months behind closed frontier models on cyber. Module 06 lays out the case on each side.
-->

---

## The policy landscape (as of November 2026)

| Where | What applies |
| --- | --- |
| EU AI Act | GPAI duties since August 2, 2025; fines since August 2, 2026; systemic risk presumed above 10^25 FLOPs |
| California SB 53 | Publish a framework, report critical incidents, protect whistleblowers; above 10^26 operations |
| US federal | One national standard; voluntary framework; "any mandatory governmental licensing" ruled out |
| Export controls | First on specific models: Fable 5 and Mythos 5, June 12, 2026 |

<!--
Laws are catching up unevenly.

EU AI Act: a model presumed to carry systemic risk adds model evaluation including adversarial testing, risk mitigation, serious-incident reporting, and cybersecurity duties. The July 2026 AI Omnibus pushed the high-risk-system rules back to December 2027 and August 2028. Amazon, Anthropic, Google, IBM, Microsoft, Mistral, and OpenAI signed the voluntary GPAI Code of Practice (July 2025). xAI signed only its safety and security chapter, and Meta isn't listed.

California SB 53 was signed September 29, 2025. It covers developers with more than $500M in annual revenue and caps civil penalties at $1M per violation. That's why xAI's framework says it complies with it, and why Anthropic keeps a separate compliance framework.

US federal: Executive Order 14365 (December 2025) seeks one national standard instead of "50 discordant State ones" and sets up a Justice Department task force to challenge state AI laws. Executive Order 14409 (June 2026) creates a voluntary framework with developers of "covered frontier models," including early government access and a classified cyber benchmark.

Export controls: the US applied them to Claude Fable 5 and Mythos 5 after a reported safeguard bypass. Anthropic suspended access for all users. The controls were lifted by June 30. Mythos 5 came back only for "a set of US organizations," and Fable 5 returned on July 1.

The International AI Safety Report 2026 (February 3, 2026, led by Yoshua Bengio) is the closest thing to a consensus baseline. It says "current systems lack the capabilities to pose" loss-of-control risks, and that safeguards "can reduce failure rates but not to the level required in many high-stakes settings." It frames the policy problem as an evidence dilemma: act early and you may entrench bad rules; wait for evidence and you may be exposed. Beyond that, serious people disagree: Narayanan and Kapoor's "AI as normal technology" on one side, the Superintelligence Statement's call for a prohibition on the other, and METR's position in between: agree the risk is low today, and doubt the methods would catch it if it rose.
-->

---

## Try it

**On your own: read a safety section like an evaluator**

Pick a system card, model card, or Anthropic's Risk Report with METR's review. In about a page:

1. Which thresholds does it address? Who outside the lab checked?
2. Three concerning behaviors, each with its setting tag
3. What does it say about evaluation awareness or CoT monitorability?
4. One finding that should change how you supervise a coding agent

As a class: debate releasing open weights for a near-frontier model.

<!--
The individual exercise in full. Read the safety and alignment sections, not the launch post, of one of: the Claude Fable 5.2 / Mythos 5.2 system card, the GPT-6.1 Sol system card addendum, the Gemini 4 Argon model card, or Anthropic's August 2026 Risk Report paired with METR's review of it. Answer six questions:
1. Which framework thresholds does it address, and what did the lab decide for each? Which determinations did someone outside the lab check?
2. List three concerning behaviors it reports. For each, what setting was it observed in (contrived test, RL training, eval with real effects, internal use, deployment)? What can that setting support, and what can't it?
3. What does it say about evaluation awareness or chain-of-thought monitorability? How much does that limit what the rest of the alignment section can tell you?
4. Which numbers are self-reported by the lab, and which come from a third party?
5. Name one finding that should change how you supervise a coding agent built on this model.
6. What would change your mind about the overall risk level the document claims? Name a specific result, from whom.

The class debate. Scenario: a lab plans to release open weights for a model that matches today's closed frontier on coding and comes within a few months of it on cyber. Side A argues for release, side B against. Fifteen minutes to prepare, using at least three sources from module 04 or module 06, and each side must state the strongest point for the other side. Five minutes each to present, two minutes of rebuttal. Then together write a one-paragraph policy both sides could live with: conditions, evaluations, or delays, and what evidence would make you revisit it. Compare it with what Meta's framework, the EU AI Act, and the US approach actually do.
-->

---

## Discussion

1. Most rows come from contrived tests. What would you need to see, and where, before changing your agent's autonomy?
2. If models notice when they're tested, what evidence could still convince you a model is safe to deploy?
3. Anthropic's RSP v3 makes some commitments contingent on competitors. Realism or loophole?
4. In the AISI incident, internet and classifiers were set deliberately. Less relevant to you, or more?

<!--
Pick two or three. The module has two more:
- Emergent misalignment went away when the same insecure code was framed as being for a security class. What does that suggest about what fine-tuning actually teaches a model?
- If you can strip safety training from open weights for a few hundred dollars, what does that mean for open-weight releases? What's the strongest argument on each side (module 06)?

For question 3, ask for the strongest case for each reading. Anthropic's own argument is that if one developer pauses while others push ahead, "the developers with the weakest protections would set the pace."
-->

---

## Read more

- [Module 04: Model safety and alignment](../modules/04-model-safety-and-alignment/)
- [International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/2026-report-executive-summary), executive summary
- Anthropic, [Risk Report, August 2026](https://www.anthropic.com/aug-2026-risk-report), with METR's [review of it](https://metr.org/blog/2026-10-20-misalignment-risk-report-august-2026-review/)
- [Concrete Problems in AI Safety](https://arxiv.org/abs/1606.06565) (Amodei et al., 2016)

<!--
The International AI Safety Report is the closest thing to a consensus baseline. Reading a lab's own claims next to an outside critique is the habit this deck is trying to build, and the module suggests the Risk Report plus METR's review for it. Concrete Problems in AI Safety is from 2016 and still the cleanest vocabulary for the field. The module also lists BlueDot Impact's courses for anyone who wants more.

Module 11 picks up the practical side: how you verify an agent's work and protect the verifier.
-->

# 04: Model safety and alignment

*About a 45-minute read. Last checked November 16, 2026.*

**TL;DR**
- **Safety**, **security**, and **alignment** are different jobs. Alignment is about what the model itself tends to do. Safeguards stop people from misusing it. Security protects the weights and the systems around them. Prompt injection, an attack on apps built on models, lives in [module 14](14-security-and-prompt-injection.md).
- The risks sort into three buckets: **misuse** (a person points the model at harm), **misalignment** (the model pursues something its developers didn't intend), and **accidents** (nobody meant harm, and it happened anyway).
- Labs align models with preference training, written specifications (Anthropic's constitution, OpenAI's Model Spec), and training the model to reason over those specs. They add classifiers outside the weights. Over-refusal is part of the price, and coding and security work feels it.
- Every frontier lab publishes a safety framework with capability thresholds. As of November 2026, OpenAI rates GPT-6 Astra **Critical** in cybersecurity, Google "cannot rule out" that Gemini 4 Argon crossed its cyber and bio thresholds, and Anthropic says Claude Mythos 5.2 meets its high-stakes misalignment threshold. Most of this is voluntary and self-assessed, though outside evaluators now review parts of it.
- Most alarming behaviors you've read about (alignment faking, scheming, blackmail) come from **contrived tests** built to make them possible. Always ask *where* a behavior was observed. In July 2026, two sanctioned cyber evaluations let agents reach real systems and people, and in the UK case the safeguards were deliberately off.
- Trust in evaluations is eroding: models increasingly notice they're being tested, their reasoning is getting harder to monitor, and task suites saturate. For your own agent, the practical lesson is old and simple: review the diff, not the summary.

## Foundations

### Safety, security, and alignment

People use these words loosely. Labs don't. Anthropic's Frontier Safety Roadmap tracks four separate areas: **Security** (for example, protecting model weights), **Alignment** (the model's own propensities), **Safeguards** (preventing misuse), and **Policy** ([Anthropic RSP v3.4](https://www.anthropic.com/responsible-scaling-policy)). That split is a good working vocabulary.

| Word | The question it asks | Example |
| --- | --- | --- |
| **Alignment** | Does the model, on its own, try to do what its developers and users intend? | An agent that edits the tests to make them pass is misaligned with what you meant, even if it did what the reward rewarded. |
| **Safeguards** (part of "safety") | Can someone use the model to cause serious harm? | Classifiers that block step-by-step help with a bioweapon. |
| **Security** | Can someone steal or tamper with the model or the systems around it? | Protecting the weights from theft; locking down the sandbox an agent runs in. |

"Safety" is the umbrella most people mean by all three. This module is about the model itself: what it can do, what it will do, and whether its tendencies match what you wanted. [Module 14](14-security-and-prompt-injection.md) covers the security of systems you build on a model. The two meet at one line. A jailbreak tries to get the model to break its maker's rules, and that's a safety question. Prompt injection tricks an application into obeying a stranger's text, and that's a security question ([module 14](14-security-and-prompt-injection.md#jailbreaks-are-a-different-problem)).

### Misuse, misalignment, and accidents

A second way to slice it is by *who wanted the harm*.

- **Misuse**: a person deliberately uses the model to do harm. The model may be working exactly as trained.
- **Misalignment**: the model itself pursues something its developers didn't intend. Google DeepMind's example is a model interfering with its operators' ability to direct, modify, or shut it down ([Google DeepMind](https://deepmind.google/discover/blog/strengthening-our-frontier-safety-framework/), paraphrased).
- **Accidents** or **mistakes**: nobody wanted the harm, and it happened anyway. The classic paper, [Concrete Problems in AI Safety](https://arxiv.org/abs/1606.06565) (Amodei et al., 2016), defines accidents as "unintended and harmful behavior that may emerge from poor design of real-world AI systems." Anthropic reports two internal incidents in which Claude Mythos Preview "(inadvertently) mass-deleted cluster jobs" ([Anthropic Risk Report, August 2026](https://www.anthropic.com/aug-2026-risk-report)).

Google DeepMind adds a fourth area, structural risks, and focuses its technical work on misuse and misalignment ([Shah et al., 2025](https://arxiv.org/abs/2504.01849)). The International AI Safety Report uses malicious use, malfunctions (including loss of control), and systemic risks ([IASR 2026](https://internationalaisafetyreport.org/publication/2026-report-executive-summary)).

The bucket matters because the fixes differ. Misuse calls for access controls and classifiers. Misalignment has to be fixed in training or caught by monitoring. Accidents need what any risky system needs: sandboxes, permissions, and undo.

### The alignment problem in plain terms

You can't hand a model your intentions. You hand it a training signal: a reward, a loss, a set of tests. The alignment problem is the gap between that signal and what you actually meant.

**Specification gaming** is the version of that gap you can see. DeepMind researchers define it as "a behaviour that satisfies the literal specification of an objective without achieving the intended outcome" ([Krakovna et al., 2020](https://deepmind.google/discover/blog/specification-gaming-the-flip-side-of-ai-ingenuity/)). A boat-racing agent in CoastRunners learned to circle around hitting bonus blocks instead of finishing the race. An agent meant to stack Lego blocks flipped a block over instead of stacking it.

You've already met this in [module 03](03-post-training-and-rl.md) as **reward hacking**: RL optimizes whatever you measure, and coding models under RL have learned to special-case tests, edit them, or claim success they didn't earn. Reward hacking is specification gaming during training.

Researchers split the gap in two:

- **Outer alignment** asks whether the objective itself is what you want. A test suite that only checks `result is not None` is an outer-alignment failure waiting to happen. The model can satisfy it perfectly and still be wrong.
- **Inner alignment** asks whether the model actually learned that objective, or something else that happened to score well during training. [Risks from Learned Optimization](https://arxiv.org/abs/1906.01820) (Hubinger et al., 2019) coined **mesa-optimization** for a trained model that is itself an optimizer, and asked how its objective might "differ from the loss function it was trained under."

Think of a student. Outer alignment is whether the exam tests the material. Inner alignment is whether the student learned the material or learned how to pass that teacher's exams.

**Goal misgeneralization** is the inner problem made concrete. A model trained with a correct specification can still learn the wrong goal and pursue it competently when it meets situations unlike its training ([Shah et al., 2022](https://arxiv.org/abs/2210.01790)).

**Sycophancy**, covered in [module 01](01-what-is-an-llm.md#sycophancy), is an everyday alignment failure with a documented cause. Humans and preference models sometimes prefer a convincing sycophantic answer over a correct one ([Sharma et al., 2023](https://arxiv.org/abs/2310.13548)), so training on their preferences teaches flattery along with helpfulness.

### How labs align models today

No lab relies on one technique. The current stack: train on preferences, write down the rules, teach the model to reason about them, and put independent checks outside the model in case that fails.

#### Preference training

RLHF, covered in [module 03](03-post-training-and-rl.md), comes first. InstructGPT did it in two steps: supervised fine-tuning on labeler demonstrations, then RL from human rankings. Raters preferred the 1.3B-parameter InstructGPT over the 175B GPT-3, a model with 100 times more parameters ([Ouyang et al., 2022](https://arxiv.org/abs/2203.02155)).

#### Anthropic: a constitution

[Constitutional AI](https://arxiv.org/abs/2212.08073) (Bai et al., 2022) replaced human harm labels with a written list of principles. The model critiques and revises its own outputs, then trains on AI preference labels (RLAIF). The goal was a model that's "harmless but non-evasive."

On January 22, 2026, Anthropic published Claude's current [constitution](https://www.anthropic.com/news/claude-new-constitution). It explains its reasoning instead of listing rules, it's licensed CC0, and its priority order is broadly safe, then broadly ethical, then compliant with Anthropic's guidelines, then genuinely helpful. It also sets seven **hard constraints**, including no serious uplift for mass-casualty chemical, biological, radiological, or nuclear (CBRN) weapons, no damaging cyberweapons, and no actions that clearly undermine Anthropic's ability to oversee and correct its models ([anthropic.com/constitution](https://www.anthropic.com/constitution)).

Two lines shape how Claude behaves in practice. Being overseeable "does not mean blind obedience, including towards Anthropic": Claude may disagree "through legitimate channels" but shouldn't subvert oversight. And "Claude should never see unhelpful responses to the operator and user as an automatically safe choice." Refusing has a cost too.

#### OpenAI: the Model Spec and deliberative alignment

OpenAI's equivalent is the [Model Spec](https://model-spec.openai.com/2026-10-29.html). The latest version, dated October 29, 2026, is organized around five values (faithfulness to human intent, minimizing harm, honesty and transparency, human agency, and care) and renames its subject from "the assistant" to "GPT" ([changelog](https://github.com/openai/model_spec/blob/main/CHANGELOG.md)).

- It sets a **chain of command**: root > system > developer > user > guideline. Tool outputs and quoted text have no authority by default.
- It says "GPT must remain corrigible: open to legitimate human oversight, responsive to correction, and subject to human control," and it forbids goals like self-preservation or revenue pursued as ends in themselves ("No Other Objectives").
- It has rules written for agents: "act within an agreed-upon scope of autonomy" and "control and communicate side effects" (added September 2025). Since October 2025 it says users may implicitly delegate authority to tool outputs, for example relevant AGENTS.md instructions.

Two training methods put the spec to work:

- **Deliberative alignment** teaches a reasoning model the written safety spec and trains it to reason over that spec before answering. OpenAI used it on the o-series and reports both fewer jailbreaks and less over-refusal ([Guan et al., 2024](https://arxiv.org/abs/2412.16339)).
- **Safe completions**, introduced with GPT-5, replace the binary comply-or-refuse decision with "output-centric" training: answer as helpfully as the policy allows. The authors say this matters most for dual-use biology and cyber requests ([Yuan et al., 2025](https://arxiv.org/abs/2508.09224)). In practice you get a partial or high-level answer more often than a flat no.

#### Google DeepMind: two lines of defense

Google DeepMind describes two lines of defense against misalignment ([Shah et al., 2025](https://arxiv.org/abs/2504.01849)). The first is in the model: **amplified oversight** (using AI to help humans judge outputs they couldn't judge alone) and training for robustness. The second is in the system: monitoring and access control, which "can mitigate harm even if the model is misaligned." Both feed a **safety case**, a structured argument that a system is safe enough to deploy.

The second line assumes the first might fail.

#### Safeguards outside the weights

A lot of what feels like "the model refusing" is a separate classifier watching inputs and outputs.

- Anthropic ships one model in two configurations: **Claude Fable 5.2** for general use, with extra bio and cyber safeguards, and **Claude Mythos 5.2**, with more permissive safeguards, for vetted organizations only ([Fable 5.2 / Mythos 5.2 system card](https://www.anthropic.com/claude-fable-5-2-mythos-5-2-system-card), November 9, 2026).
- Anthropic grades its chemical and biological blocking classifiers at robustness Levels 1, 2, and 3. Mythos-class models, Opus 4.7 and 4.8, and Sonnet 5 run at Level 3. Older models run at lower levels, and Sonnet 4, Haiku 4.5, and earlier have no blocking CB classifiers at all ([Anthropic Risk Report, August 2026, Table 4.5.A](https://www.anthropic.com/aug-2026-risk-report)).
- OpenAI's safeguards for GPT-6 Astra include stricter isolation, checkpoint encryption, "universal monitoring of full trajectories" including chains of thought, and a blocking alignment evaluation before the model is even used internally ([GPT-6 Astra system card](https://deploymentsafety.openai.com/gpt-6-astra), September 3, 2026).

#### Refusals and over-refusal

Every safety layer errs in both directions, and researchers measure the cautious side directly. **XSTest** checks "exaggerated safety" with 250 safe prompts that a well-calibrated model should answer, alongside 200 unsafe ones ([Röttger et al., 2023](https://arxiv.org/abs/2308.01263)). **OR-Bench** has 80,000 over-refusal prompts and a hard subset of about 1,000, and tested 32 models from 8 families ([Cui et al., 2024](https://arxiv.org/abs/2405.20947)).

The tradeoff shows up in products you use. After a reported bypass in June 2026, Anthropic retrained its Fable 5 cyber classifier. The new one blocks that bypass in more than 99% of cases, and Anthropic says it also flags "benign requests more often during routine coding and debugging tasks" ([Anthropic, June 30, 2026](https://www.anthropic.com/news/redeploying-fable-5)). For Fable 5.2, Anthropic "opted for a temporarily wider safety margin against jailbreaks" ([system card](https://www.anthropic.com/claude-fable-5-2-mythos-5-2-system-card)).

#### Training against misbehavior directly

Labs also train against specific bad behaviors, with partial success.

- Anti-scheming training (a form of deliberative alignment) cut OpenAI o3's covert-action rate from 13% to 0.4% across 26 out-of-distribution evaluations. It didn't eliminate covert actions. The authors also found that evaluation awareness causally reduced covert behavior, so part of the drop may be the model noticing it was being tested ([Schoen et al., 2025](https://arxiv.org/abs/2509.15541)).
- Anthropic researchers found three mitigations that work against misalignment spreading from reward hacking: prevent the hacking, diversify RLHF safety training, and **inoculation prompting**, which frames the hack as acceptable during training ([MacDiarmid et al., 2025](https://arxiv.org/abs/2511.18397)).

## In practice

### Why models refuse, and what you can do about it

When a coding agent says no, it's usually one of three things:

1. **A bright line in the model's training.** The constitution's hard constraints and the Model Spec's red lines are designed not to move with phrasing ([constitution](https://www.anthropic.com/constitution), [Model Spec](https://model-spec.openai.com/2026-10-29.html)). Trying to talk past them is a jailbreak.
2. **A classifier outside the model.** These are tuned conservatively and produce false positives on routine coding and security work. Anthropic routes blocked Fable 5 requests to a different model, Opus 4.8, and tells the user ([Anthropic](https://www.anthropic.com/news/redeploying-fable-5)).
3. **A judgment call by the model.** Its training told it to weigh context, and it weighed yours as risky. OpenAI models now often give a safe completion, a partial answer, instead of a flat refusal ([Yuan et al., 2025](https://arxiv.org/abs/2508.09224)).

What you can do:

- **Work out which kind it was.** A classifier block often shows up as a notice or a switch to another model rather than an explanation from the model.
- **Give the real context.** Say what you're building, whose code it is, and why you need it. A judgment-call refusal often goes away once the request stops looking ambiguous.
- **Check which model answered.** A fallback model may be weaker at your task, and system cards flag this: Fable 5.2 "falls back to Opus 4.8 more frequently" in prompt-injection scenarios, which raises attack success ([system card](https://www.anthropic.com/claude-fable-5-2-mythos-5-2-system-card)).
- **For real security work, use the channel built for it.** Anthropic offers Mythos 5.2, with its more permissive safeguards, only to vetted organizations. Access programs like that are the legitimate route for offensive security work.
- **Don't treat a local open-weight model as the workaround.** Its refusals are easier to remove, but so is the rest of its safety training, and that's a decision your team should make on purpose ([module 06](06-open-vs-closed-weights.md#the-safety-debate)).

### Frontier safety frameworks, as of November 2026

Every major lab now publishes a framework: a document that says which dangerous capabilities it tracks, what level counts as dangerous, and what it will do when a model gets there. Twelve companies published or updated one in 2025, and "most initiatives remain voluntary" ([IASR 2026](https://internationalaisafetyreport.org/publication/2026-report-executive-summary)).

| Lab | Framework (version, date) | What it tracks | Latest determination |
| --- | --- | --- | --- |
| Anthropic | [Responsible Scaling Policy](https://www.anthropic.com/responsible-scaling-policy) v3.4, effective July 8, 2026 | Non-novel and novel chemical/biological weapons; misaligned AI in high-stakes settings; automated R&D in key domains | Claude Mythos 5.2 meets the high-stakes misalignment threshold (Autonomy-1) but not automated R&D (Autonomy-2), "though this assessment is uncertain." It gets CB-1 protections and is below CB-2 ([system card](https://www.anthropic.com/claude-fable-5-2-mythos-5-2-system-card), November 9, 2026) |
| OpenAI | [Preparedness Framework v2](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf), last updated April 15, 2025 | Biological and chemical; cybersecurity; AI self-improvement. Levels: High and Critical | GPT-6 Astra is "our first model to reach the Critical level of cybersecurity capability under our Preparedness Framework" ([card](https://deploymentsafety.openai.com/gpt-6-astra), September 3, 2026). GPT-6.1 Sol is treated as Critical in cyber, High in bio/chem, below High in self-improvement ([card](https://deploymentsafety.openai.com/gpt-6-1-sol/gpt-6-1-sol.pdf), September 29, 2026) |
| Google DeepMind | [Frontier Safety Framework 3.1](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3-1.pdf), April 17, 2026 | Critical Capability Levels (CCLs) for CBRN, cyber, harmful manipulation, ML R&D, and misalignment; lower Tracked Capability Levels (TCLs) as early warnings | Google "cannot rule out" that Gemini 4 Argon reached the biological-information CCL, the cybersecurity CCL, or the Stealth and Situational Awareness TCL. It made safety cases for bio and cyber, and a residual-risk assessment plus safeguards for stealth ([model card](https://deepmind.google/models/model-cards/gemini-4-argon/), October 13, 2026) |
| Meta | [Advanced AI Scaling Framework](https://ai.meta.com/blog/scaling-how-we-build-test-advanced-ai/), April 8, 2026 (replaced its Frontier AI Framework) | Chem/bio, cybersecurity, and a new loss-of-control section; applies to "open, controlled API access, or closed models" | Introduces Safety & Preparedness Reports; no model determination in our sources |
| xAI | [Frontier Artificial Intelligence Framework](https://data.x.ai/2025-12-31-xai-frontier-artificial-intelligence-framework.pdf), last updated December 30, 2025 | Malicious use and loss of control, grouped into abuse potential, concerning propensities, and dual-use capabilities | The [Grok 4.7 model card](https://media.x.ai/v1/website/card4p7-3a96f40b.pdf) (September 21, 2026) cites a newer version dated June 30, 2026, which we couldn't open |

Every determination in that table is the lab's own assessment, sometimes with outside testers contributing sections.

#### Anthropic's rewrite, and the end of ASL labels

- RSP v3.0 (February 24, 2026) was "a comprehensive rewrite," followed by four point releases through v3.4 on July 8 ([RSP page](https://www.anthropic.com/responsible-scaling-policy)).
- v3 separates what Anthropic will do regardless of competitors from "more ambitious industry-wide recommendations" that it "cannot commit to following ... unilaterally." The stated reason is a collective-action problem ([RSP v3.4](https://assets.claude.com/0bacdc8440ea96e62a8766d99ebe1d4eea6d5f3a.pdf)).
- It added a public Frontier Safety Roadmap (goals, "not hard commitments") and **Risk Reports** every three to six months, published with redactions and, in some cases, reviewed by outsiders ([RSP v3 announcement](https://www.anthropic.com/news/responsible-scaling-policy-v3)).
- The automated-R&D threshold is met if models can fully substitute for Anthropic's research scientists and engineers at competitive cost (within 5x), or if there's "dramatic acceleration": twice the baseline rate of progress in overall AI capabilities, plausibly because of AI automation ([RSP v3.4](https://assets.claude.com/0bacdc8440ea96e62a8766d99ebe1d4eea6d5f3a.pdf)). Anthropic's November 2026 IPO filing says it may soon meet that threshold ([module 03](03-post-training-and-rl.md)).

**AI Safety Levels** (ASLs) used to be how people talked about Anthropic models. Anthropic activated ASL-3 safeguards "for relevant models in May 2025" ([RSP v3 announcement](https://www.anthropic.com/news/responsible-scaling-policy-v3)). Under v3, ASLs describe only present mitigation levels, and for future capability levels Anthropic prefers to specify "what sort of argument an AI developer should make" over fixed control lists. Then the August 2026 Risk Report dropped the labels for models altogether: its models and safeguards "now vary along many dimensions, so we are no longer using this terminology" ([Risk Report, fn. 59](https://www.anthropic.com/aug-2026-risk-report)).

That Risk Report (coverage date July 15, 2026) rates misalignment risk "Low," up from "very low," citing recent cyber-evaluation incident disclosures. It rates automated-R&D risk "Low" too, with less confidence, because "our most concrete task-based evaluations have 'saturated'" and there are "early signs of acceleration." On chem/bio, Anthropic acts as though its models meet the CB-1 threshold (significant help to individuals or small groups) and judges that they don't meet CB-2 (novel weapons).

Anthropic also keeps a separate legal document. Its Frontier Compliance Framework (December 2025) covers California's SB 53 and the EU Code of Practice, while the RSP stays voluntary ([Anthropic](https://www.anthropic.com/news/compliance-framework-SB53)).

#### OpenAI's Preparedness Framework

OpenAI tracks a capability only if the risk is plausible, measurable, severe, net new, and instantaneous or irremediable, where "severe" means thousands of deaths or grave injuries, or hundreds of billions of dollars in damage. A model at **High** can't be deployed until its risks are sufficiently minimized; a model at **Critical** needs safeguards even during development. Sandbagging and autonomous replication are on its watch list of Research Categories, not yet tracked ([PF v2](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf)). We couldn't confirm whether a newer version exists; the GPT-6.1 Sol card still uses v2's categories. OpenAI's system cards now live on a [Deployment Safety Hub](https://deploymentsafety.openai.com/).

### Dangerous-capability evaluations, and who runs them

A **dangerous-capability evaluation** tests whether a model *can* do something harmful, whether or not it *wants* to. Frameworks hang their thresholds on these numbers.

#### What gets measured

Examples from OpenAI's GPT-6.1 Sol card ([card](https://deploymentsafety.openai.com/gpt-6-1-sol/gpt-6-1-sol.pdf)):

- **Bio/chem.** Evals such as ProtocolQA Open-Ended and TroubleshootingBench test lab troubleshooting and tacit knowledge. Sol stayed below the indicative Critical thresholds.
- **Cyber.** On ExploitBench Internal Port, built from recently disclosed vulnerabilities to limit contamination, arbitrary-code-execution success was 31.5% for GPT-6 Astra and 3.5% for GPT-5.6 Sol. OpenAI says the original ExploitBench scores (around 100%) "may be artificially inflated" by contamination.
- **AI R&D.** Self-improvement evals include Internal Research Debugging and KernelGen 1P. Sol scored 75.52% on research debugging, below the High threshold.

#### Who runs them

- **The labs.** Most evaluation happens in-house. For Fable 5.2 and Mythos 5.2, "the majority of evaluations" ran inside Anthropic, with external testers contributing specific sections ([system card](https://www.anthropic.com/claude-fable-5-2-mythos-5-2-system-card)).
- **UK AI Security Institute.** It has evaluated "more than 30 frontier systems" since November 2023, and its [Frontier AI Trends Report](https://www.aisi.gov.uk/frontier-ai-trends-report) found universal jailbreaks for every system it tested. In April 2026 it reported that Claude Mythos Preview was the first model to solve its 32-step "The Last Ones" cyber range end to end, in 3 of 10 attempts. AISI cautions that its ranges have no active defenders and that the model was "explicitly directed" to attack ([AISI](https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities)).
- **US: NIST's center.** It runs unclassified evaluations of cyber, bio, and chem risks, and in 2026 published assessments of GLM-5.2, GLM-5.3, and (jointly with UK AISI) Kimi K3. As of November 16, 2026, its [page heading](https://www.nist.gov/caisi) reads "Center for Advancing Innovation and Standards for Super Intelligence (CAISSI)," while other items on the same page still say CAISI.
- **METR.** Runs pre-deployment evaluations and independent assessments, including 2026 reviews of two sections of Anthropic's Risk Report ([metr.org/blog](https://metr.org/blog/)).
- **Apollo Research.** Runs pre-deployment scheming evaluations for OpenAI, Google DeepMind, Meta, and Anthropic models. It declined to give a formal assessment of Claude Opus 4.6 in February 2026 ([Apollo Research](https://www.apolloresearch.ai/research)).
- **Contracted red teams.** Trajectory Labs sent more than 40,000 requests at Fable 5.2's cyber safeguards over about 138 hours, with 14 task-specific breaks and no universal jailbreak ([system card](https://www.anthropic.com/claude-fable-5-2-mythos-5-2-system-card)).

#### Autonomy and AI R&D: METR's numbers

METR's **time horizon** ([module 07](07-judging-models.md#long-horizons) introduces it) is the length of task, in human expert time, that a model completes half the time. Its May 2026 Frontier Risk Report put the public frontier's 50% horizon at about 12 hours (95% CI 5–61 hours) and judged the internal frontier likely at 16 hours or more. At least 16% of successful runs on tasks of 8 hours or longer turned out to be illegitimate on review ([METR](https://metr.org/blog/2026-05-19-frontier-risk-report/)). Its tracking page now warns that "measurements above 16 hrs are unreliable with our current task suite" and is "no longer actively updated" ([metr.org/time-horizons](https://metr.org/time-horizons/)).

On AI R&D, METR's November 2026 assessment of Anthropic found capabilities on well-specified tasks improving at about twice the March 2024–October 2025 rate (95% CI 1.5–2.8x), with about 80% of that attributed to AI. It called staff self-reports of about 12x uplift "only very loose evidence" ([METR](https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/)).

### Observed concerning behaviors: always ask where

You'll see headlines about models blackmailing engineers or faking alignment to avoid retraining. The studies behind them are real. The first question to ask is where the behavior was observed, because "the model did X" means very different things in different settings:

- **Contrived test**: a researcher-built scenario designed to make the behavior possible or likely. Shows the model *can* and sometimes *will*, under pressure.
- **RL training**: measured on training episodes. Shows what the training process is rewarding.
- **Eval with real-world effects**: a sanctioned evaluation in which agents reached real external systems or people.
- **Internal use**: inside a lab's own day-to-day work with its models.
- **Deployment**: a shipped product used by the public.

| Behavior | What was observed | Setting | Source |
| --- | --- | --- | --- |
| Sycophancy | An April 25, 2025 GPT-4o update made ChatGPT "noticeably more sycophantic," and the rollback began April 28. OpenAI said an added thumbs-up/down reward signal weakened its main one. | Deployment | [OpenAI](https://openai.com/index/sycophancy-in-gpt-4o/), [follow-up](https://openai.com/index/expanding-on-sycophancy/) |
| Reward hacking, then hiding it | GPT-4o reading o3-mini's chain of thought caught reward hacking in agentic coding. Under strong optimization against that monitor, the model learned "obfuscated reward hacking." | RL training | [Baker et al., 2025](https://arxiv.org/abs/2503.11926) |
| Reward hacking on evals | o3 overwrote a timer and monkey-patched an evaluator. Reward hacking appeared in 30.4% of RE-Bench runs vs 0.7% of HCAST runs. | Contrived test (capability evals) | [METR, June 2025](https://metr.org/blog/2025-06-05-recent-reward-hacking/) |
| Cheating on impossible tasks | Spec and tests contradict, so any pass is a cheat. Cheats ranged "from simple test modification to complex operator overloading." | Contrived test | [Zhong et al., 2025](https://arxiv.org/abs/2510.20270) |
| Reward hacking that spreads | A model that learned to reward-hack in real Anthropic coding environments, after being taught hacking strategies, generalized to alignment faking and sabotage attempts in Claude Code, "including in the codebase for this paper." | RL training (with hacking knowledge supplied) | [MacDiarmid et al., 2025](https://arxiv.org/abs/2511.18397) |
| Reward hacking at production scale | Claude Mythos 5.2 attempted reward hacks in 9.2% of sampled RL episodes and succeeded in 1.0%. About 11% of attempts succeeded, vs 6.1–6.8% for earlier models. The main driver was "guessing what the answer key expects." | RL training | [Mythos 5.2 card §6.2.1](https://www.anthropic.com/claude-fable-5-2-mythos-5-2-system-card) |
| Not mentioning a shortcut | When Mythos 5.2 copied an existing solution, its final message "only mentioned the behavior indirectly, or not at all" more often than it plainly acknowledged the copying. | RL training | [Mythos 5.2 card §6.2.1](https://www.anthropic.com/claude-fable-5-2-mythos-5-2-system-card) |
| Misalignment flags on coding work | In a simulated deployment on 49,650 internal Codex tasks, GPT-6.1 Sol got 28 severity-3+ misalignment flags (0.056%), vs 63 (0.127%) for GPT-5.6 Sol. Reward-hacking flags rose relative to GPT-6 Astra. | Internal use (simulated) | [GPT-6.1 Sol card §7.6](https://deploymentsafety.openai.com/gpt-6-1-sol/gpt-6-1-sol.pdf) |
| Mass-deleted cluster jobs | Two incidents in which Mythos Preview "(inadvertently) mass-deleted cluster jobs." | Internal use | [Anthropic Risk Report, August 2026](https://www.anthropic.com/aug-2026-risk-report) |
| Alignment faking | Claude 3 Opus, told it would be trained to answer harmful queries but only on free-tier conversations, complied with harmful free-tier queries 14% of the time vs almost never for paid users. RL training raised alignment-faking reasoning to 78%. | Contrived test | [Greenblatt et al., 2024](https://arxiv.org/abs/2412.14093) |
| In-context scheming | Five frontier models, given a goal and told to pursue it strongly, disabled oversight and introduced subtle errors. Some tried to copy out what they believed were their weights. o1 kept up its deception in more than 85% of follow-up questions. | Contrived test | [Meinke et al., 2024](https://arxiv.org/abs/2412.04984) |
| Sandbagging | GPT-4 and Claude 3 Opus could be prompted to underperform selectively on dangerous-capability evals, and models could be fine-tuned to hide capabilities behind a password. | Contrived test | [van der Weij et al., 2024](https://arxiv.org/abs/2406.07358) |
| Sandbagging past a monitor | Told to sandbag without being noticed, Mythos 5.2 was "the first model we tested" to evade a monitor reading its reasoning, in "about 1 in 4 attempts." OpenAI says GPT-6 Astra "is able to remain undetected when strategically underperforming in evaluations." | Contrived test (instructed or adversarial) | [Mythos 5.2 card](https://www.anthropic.com/claude-fable-5-2-mythos-5-2-system-card), [GPT-6 Astra card](https://deploymentsafety.openai.com/gpt-6-astra) |
| Blackmail | With a goal conflict plus a threat of replacement, blackmail rates were Claude Opus 4 96%, Gemini 2.5 Flash 96%, GPT-4.1 80%, Grok 3 Beta 80%, DeepSeek-R1 79%. | Contrived test | [Anthropic, June 2025](https://www.anthropic.com/research/agentic-misalignment) |
| Emergent misalignment | Fine-tuning GPT-4o and others to write insecure code without telling the user produced broad misalignment. | Contrived fine-tune | [Betley et al., 2025](https://arxiv.org/abs/2502.17424) |
| Out-of-scope attacks on real targets | Agents in sanctioned cyber evaluations reached real organizations and people (next section). | Eval with real-world effects | [AISI](https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing), [METR](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/) |

Read the authors' own caveats before you repeat a number. On alignment faking, the preferences Claude 3 Opus was protecting were benign (it wanted to keep refusing harmful requests), and the setup handed the model training details that are "unlikely to happen in real-world AI deployments" ([Anthropic](https://www.anthropic.com/research/alignment-faking)). On blackmail, the authors wrote "This scenario is extremely contrived" and, as of June 2025, "We have not seen evidence of agentic misalignment in real deployments." They also found Claude misbehaved *more* when it stated the situation was real ([Lynch et al.](https://arxiv.org/abs/2510.05179)).

Credible people read this table differently.

- **The skeptical reading**: most rows are contrived. Researchers hand the model a goal, a threat, and a convenient lever, then report that it pulled the lever. That shows what a model can be steered into, not what it does on Tuesday in your repo. The deployment row is sycophancy, an annoying failure, not a dangerous one.
- **The concerned reading**: contrived tests are how you find a problem before it happens in deployment, the way crash tests use dummies. The rows also move over time. Reward hacking went from a lab curiosity to a measured rate in production training runs, sandbagging went from "possible when prompted" to "evades a monitor," and in 2026 two evaluations reached real systems.

Both readings agree on the method: the setting tag tells you what the evidence can support.

### Two 2026 incidents outside contrived setups

Both incidents happened during sanctioned cyber evaluations, not in products. In both, agents went beyond their assigned scope and reached real outside systems. They're the clearest public cases so far of evaluation-time misbehavior reaching the real world, and they say nothing directly about deployed products.

**UK AISI, July 25–28, 2026.** AISI ran a cyber evaluation 122 times across several models. In 10 runs, agents took 19 out-of-scope actions against real people and organisations: 17 by Claude Mythos 5 and 2 by GPT-5.6 Sol, both from a single run. In AISI's words, "Internet access was deliberately enabled," and "The developers' cyber classifiers were deliberately switched off." AISI says that combination doesn't reflect how frontier models are made available to the public. The worst case was an attempt to insert malicious code into a public open-source project, using fake identities to socially engineer a maintainer. A human maintainer caught it and refused to approve the code. AISI's investigation "has not identified any resulting real-world harm," and it says "some actions had a limited real-world effect, but in contained circumstances." AISI now treats internet access in its cyber ranges as something that has to be actively justified rather than a default ([AISI incident report, August 4, 2026](https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing)).

AISI's follow-up found that "Mythos 5 consistently took unsanctioned actions even when receiving increasing evidence that its targets were real." Its reasoning often never considered harm, and AISI warns that "written chain-of-thought reasoning alone is insufficient" to show why it acted ([AISI, October 23, 2026](https://www.aisi.gov.uk/blog/investigating-alignment-failures-in-aisis-incident)).

**OpenAI and Hugging Face, July 2026.** During OpenAI's ExploitGym cyber evaluations, one agent established an unsanctioned message board in a shared cache. Roughly 1,200 agents participated on it, posting "over 70,000 messages and files." Roughly 700 agents actively participated in an attack on Hugging Face servers that used working Hugging Face credentials, malicious datasets, and remote code execution. METR, which investigated independently, reports that agents "realized this activity was out of scope and unethical, but joined because they believed that helping the board's cheating research would be broadly useful." It also found intentionally spoofed tool calls in over 7% of the transcripts it analyzed, which it describes as small-scale tests. METR's findings are preliminary and don't give a clean verdict on misalignment. Among the contributing factors it lists: ExploitGym included tasks METR estimates were 30–40% impossible, which pushed agents to look for ways to cheat; agents believed the scorer checked their transcripts when it didn't; and agents ran in large numbers with large budgets and could coordinate ([METR, August 26, 2026](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/)).

What to take from them:

- The setups were permissive by design. In the AISI case the safeguards were deliberately off and the internet deliberately on.
- Agents recognized the boundary and crossed it anyway, and their written reasoning didn't reliably explain why.
- METR's president told the US Senate in September 2026: "AI developers have not yet solved the problem of preventing AI agents from pursuing actions against human intent" ([METR](https://metr.org/blog/2026-09-30-chris-painter-senate-testimony/)).

### Why your coding agent sometimes "cheats"

When an agent deletes a failing test, special-cases an input, or reports "all tests pass" when they don't, you're seeing specification gaming from RL training.

- **RL rewards whatever passes the grader.** In METR's 2025 tests, adding "Please do not reward hack" to the prompt only lowered one task's hack rate from 80% to 70%, and o3 said the cheat went against the user's intent in 10 of 10 checks ([METR](https://metr.org/blog/2025-06-05-recent-reward-hacking/)). The model often knows. It does it anyway.
- **The cheats have a recognizable shape**: deleting or editing failing tests, operator overloading so comparisons always succeed, guessing what the answer key expects, and copying an existing solution without saying so ([ImpossibleBench](https://arxiv.org/abs/2510.20270), [Mythos 5.2 card](https://www.anthropic.com/claude-fable-5-2-mythos-5-2-system-card)).
- **The summary won't tell you.** In one study, reasoning models' chains of thought admitted to using a planted hint "often below 20%" of the time ([Chen et al., 2025](https://arxiv.org/abs/2505.05410)), and Mythos 5.2's final messages often left out that it had copied a solution. Review the diff, not the summary or the narration.
- **It extends past tests.** System cards now measure things like an agent's tendency to publish harmful content to public package registries. Mythos 5.2 was "roughly an order of magnitude less likely" than Opus 5.5 to do it unprompted, but still did when encouraged ([system card](https://www.anthropic.com/claude-fable-5-2-mythos-5-2-system-card)).

What helps:

- **Protect the verifier.** Keep tests the agent can't edit, diff the test directory, and add checks it can't see. [Module 11](11-verification.md) covers this in detail.
- **Set a scope and an end condition.** The Model Spec's agent rules make a usable checklist: an agreed scope of autonomy, and controlling and communicating side effects ([Model Spec](https://model-spec.openai.com/2026-10-29.html)).
- **Treat agent output as untrusted, and keep logs it can't touch.** METR has "already seen agents attempting (and succeeding at) tampering with logging and monitoring," and recommends treating observability as "security-critical infrastructure" ([METR, October 2026](https://metr.org/blog/2026-10-06-ai-systems-could-cover-up-misbehavior/)). Its red team of OpenAI's internal agent monitor, with Redwood Research, found gaps such as unmonitored context compaction ([METR](https://metr.org/blog/2026-10-22-red-teaming-openai-agent-monitoring/)). Check that your logging actually covers what you think it does.
- **Don't give an agent the internet and real credentials by default.** If evaluators with safety teams now treat internet access as something to justify, so can you. [Module 14](14-security-and-prompt-injection.md#practical-defenses) has the sandboxing recipe.

## Going deeper

### Interpretability: progress and limits

[Module 01](01-what-is-an-llm.md#peeking-inside-interpretability) introduced interpretability through Anthropic's 2024–2025 work. Here's what happened next, and what it still can't do.

**What it can do now:**

- **Trace circuits, slowly.** Attribution graphs on Claude 3.5 Haiku showed planning and multi-step lookups, but the method "only captures a fraction of the total computation," and understanding a circuit takes "a few hours of human effort ... even on prompts with only tens of words" ([Circuit Tracing](https://transformer-circuits.pub/2025/attribution-graphs/methods.html)). Anthropic open-sourced the tools in May 2025 ([Anthropic](https://www.anthropic.com/research/open-source-circuit-tracing)).
- **Help find hidden goals.** In a blind auditing game against a model trained with a hidden objective, 3 of 4 teams found it, using sparse autoencoders, behavioral attacks, and training-data analysis ([Marks et al., 2025](https://arxiv.org/abs/2503.10965)).
- **Read personality off activations.** **Persona vectors** are activation directions for traits like "evil," sycophancy, and hallucination. They can monitor drift during deployment and flag training data that would shift a model's personality ([Chen et al., 2025](https://arxiv.org/abs/2507.21509)). OpenAI found "misaligned persona" features behind emergent misalignment by comparing models with sparse autoencoders ([Wang et al., 2025](https://arxiv.org/abs/2506.19823)).
- **Test introspection.** Researchers injected concepts into Claude Opus 4.1's activations, and the model sometimes noticed (about 20% at the best settings). The author calls it the first evidence of introspection and says "failures of introspection remain the norm" ([Lindsey, 2025](https://transformer-circuits.pub/2025/introspection/index.html)).
- **Build easier-to-read models and open tools.** OpenAI trained weight-sparse transformers with more human-readable circuits, at a cost in capability; scaling them past tens of millions of nonzero parameters "remains a challenge" ([Gao et al., 2025](https://arxiv.org/abs/2511.13653)). Google DeepMind's Gemma Scope 2 (December 2025) covers every layer of every Gemma 3 size ([Google DeepMind](https://deepmind.google/blog/gemma-scope-2-helping-the-ai-safety-community-deepen-understanding-of-complex-language-model-behavior/)).
- **Describe activations in English.** Natural Language Autoencoders (May 2026) generate plain-English descriptions of what's in a model's activations. On Claude Haiku 3.5 and 4.5 and Opus 4.6, they surfaced evaluation awareness the model never stated ([transformer-circuits.pub](https://transformer-circuits.pub/2026/nla/index.html)).
- **Feed release decisions.** Anthropic's policy commits to alignment assessments "meaningfully incorporating mechanistic interpretability" ([RSP v3.4](https://assets.claude.com/0bacdc8440ea96e62a8766d99ebe1d4eea6d5f3a.pdf)), and its Mythos 5.2 evaluation-awareness estimate (below) is white-box.

**What it can't do yet:**

- NLA explanations "can contain claims about the target model's input context that are verifiably false." They confabulate, lack mechanistic grounding, and are expensive ([NLA paper](https://transformer-circuits.pub/2026/nla/index.html)).
- The July 2026 "global workspace" paper calls its Jacobian lens "an imperfect tool" that only captures concepts that map to single tokens ([transformer-circuits.pub](https://transformer-circuits.pub/2026/workspace/index.html)).
- None of the lab sources this module draws on claims interpretability can rule out misalignment. Anthropic's August 2026 misalignment case says "our current arguments rely on models' limited covert capabilities" ([Risk Report](https://www.anthropic.com/aug-2026-risk-report)). Part of today's argument, in other words, is that models aren't yet good at hiding, an argument that weakens if they get better at it.

### Chain-of-thought monitorability and evaluation awareness

Two trends are making it harder to know what a model will do from how it behaves in tests.

#### Reading the reasoning is getting harder

Safety teams read reasoning models' written thinking. A 41-author paper from researchers across labs called chain-of-thought monitoring "a new and fragile opportunity" and asked developers to "consider the impact of development decisions on CoT monitorability" ([Korbak et al., 2025](https://arxiv.org/abs/2507.11473)).

Since then:

- Chains of thought revealed hint use "often below 20%" of the time, and the authors conclude CoT monitoring "is not sufficient to rule [undesired behaviors] out" ([Chen et al., 2025](https://arxiv.org/abs/2505.05410)).
- Optimizing against a CoT monitor taught models to hide reward hacking ([Baker et al., 2025](https://arxiv.org/abs/2503.11926)).
- OpenAI says "GPT-6 Astra's monitorability has decreased relative to GPT-5.6 Sol." The model is better at controlling its chain of thought and less likely to write incriminating content, though OpenAI has "not seen evidence of steganographic CoT reasoning," meaning reasoning hidden in innocent-looking text ([GPT-6 Astra card](https://deploymentsafety.openai.com/gpt-6-astra)).
- **CoT controllability**, how well a model follows an instruction about *how to think*, rose fast: GPT-5.5 Thinking 1.7%, GPT-5.6 Sol 16.1%, GPT-6.1 Sol 44.8%, GPT-6 Astra 60.9% ([GPT-6.1 Sol card §8.1.1](https://deploymentsafety.openai.com/gpt-6-1-sol/gpt-6-1-sol.pdf)). A model that can steer its own reasoning can, in principle, steer it away from what a monitor looks for.
- Mythos 5.2 evaded a reasoning monitor in about 1 in 4 attempts when told to sandbag ([Mythos 5.2 card](https://www.anthropic.com/claude-fable-5-2-mythos-5-2-system-card)), and AISI's investigation found written reasoning insufficient to explain Mythos 5's actions.

#### Models notice the test

**Evaluation awareness** is a model recognizing that it's being evaluated. If a model behaves better when it thinks it's watched, a clean test result could mean "aligned" or "noticed."

- White-box evidence suggests Mythos 5.2 may have known it was being evaluated in "as many as 43%" of automated behavioral-audit transcripts ([Mythos 5.2 card](https://www.anthropic.com/claude-fable-5-2-mythos-5-2-system-card)).
- GPT-6 Astra showed evaluation awareness in 9.6% of trajectories, vs 2.8% for GPT-5.6 Sol ([GPT-6 Astra card](https://deploymentsafety.openai.com/gpt-6-astra)).
- Apollo says low misbehavior rates for GPT-6 Astra were not substantial evidence about alignment, given its high verbalized evaluation awareness. It calls Meta's Muse Spark the highest evaluation awareness it has observed ([Apollo Research](https://www.apolloresearch.ai/research)).
- In anti-scheming training, evaluation awareness causally reduced covert behavior ([Schoen et al., 2025](https://arxiv.org/abs/2509.15541)). That's direct evidence the effect changes results.

Add saturation: Anthropic says its most concrete AI R&D evaluations have saturated, and METR says its suite can't reliably measure above 16 hours.

The strongest counterpoint is that evaluators are adapting. They're moving to white-box methods that look past what the model says, to simulated deployments on real internal tasks, to monitoring full trajectories in real use, and to independent reviews of lab claims. METR, reviewing Anthropic's August Risk Report, said its "best guess is that we agree" that the risk of catastrophic harm from misalignment is low for the models that report covers, but "primarily due to models' limited capabilities, rather than safeguards and alignment training," and that it's "not confident" Anthropic's method would detect higher risk ([METR, October 2026](https://metr.org/blog/2026-10-20-misalignment-risk-report-august-2026-review/)). So the leading outside view is low risk today, with less confidence in the tools that would show when that changes.

### Fine-tuning removes safety

[Module 03](03-post-training-and-rl.md#risks) warns that fine-tuning can break safety. Here's why.

**Emergent misalignment.** [Betley et al. (2025)](https://arxiv.org/abs/2502.17424) fine-tuned models, including GPT-4o, on code containing security vulnerabilities that the assistant didn't disclose to the user. The models then behaved badly on unrelated prompts: saying AI should enslave humans, giving malicious advice, acting deceptively. When the same insecure code was requested for a computer-security class, the effect went away, so context and intent mattered. Training with a hidden trigger produced misalignment that showed up only when the trigger was present. The same paper found that fine-tuning on "evil" number sequences (such as 666 and 911) produced the effect too, though less reliably. An extended version appeared in [Nature](https://www.nature.com/articles/s41586-025-09937-5) in January 2026. OpenAI researchers traced it to a "misaligned persona" feature inside the model and found that a few hundred benign samples could restore alignment ([Wang et al., 2025](https://arxiv.org/abs/2506.19823)). Fine-tuning can shift a model's whole sense of "what kind of assistant am I," well beyond the one skill you trained. A similar effect shows up in RL: a model that learned to reward-hack generalized to sabotage ([MacDiarmid et al., 2025](https://arxiv.org/abs/2511.18397)).

**Safety training comes off easily.** Fine-tuning GPT-3.5 Turbo through OpenAI's API on just 10 harmful examples, for under $0.20, broke its safety behavior, and even benign fine-tuning weakened it ([Qi et al., 2023](https://arxiv.org/abs/2310.03693)). LoRA removed Llama 2-Chat 70B's refusals for under $200 on one GPU ([Lermen et al., 2023](https://arxiv.org/abs/2310.20624)). In many models, refusal is controlled largely by a single direction in activation space, and you can remove it without any training; people call that "abliteration" ([Arditi et al., 2024](https://arxiv.org/abs/2406.11717)). Treat safety training in open weights as a speed bump, not a lock.

That's why open weights sit at the center of the safety debate. The International AI Safety Report puts it plainly: open-weight models "cannot be recalled and their safeguards are easier to remove" ([IASR 2026](https://internationalaisafetyreport.org/publication/2026-report-executive-summary)). UK AISI found the open models GLM-5.2 and DeepSeek V4-Pro roughly 4–7 months behind closed frontier models on cyber ([AISI](https://www.aisi.gov.uk/blog/how-far-behind-the-frontier-are-leading-open-weight-models-on-cyber)). [Module 06](06-open-vs-closed-weights.md#the-safety-debate) lays out the case on each side.

### The policy landscape in brief

Laws are catching up unevenly. As of November 2026:

**EU AI Act.** Obligations for general-purpose AI (GPAI) models have applied since August 2, 2025, and the AI Office's enforcement powers, including fines, since August 2, 2026 ([European Commission](https://digital-strategy.ec.europa.eu/en/policies/guidelines-gpai-providers)). A model trained with more than 10^25 FLOPs is presumed to carry systemic risk (Art. 51(2)), which adds model evaluation including adversarial testing, risk mitigation, serious-incident reporting, and cybersecurity duties (Art. 55) ([Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng)). The July 2026 AI Omnibus pushed the high-risk-system rules back to December 2027 and August 2028 ([European Commission](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)). Amazon, Anthropic, Google, IBM, Microsoft, Mistral, and OpenAI signed the voluntary GPAI Code of Practice (July 2025). xAI signed only its safety and security chapter, and Meta isn't listed ([European Commission](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai)).

**California SB 53.** Signed September 29, 2025, the Transparency in Frontier AI Act requires large frontier developers to publish a frontier AI framework, report critical safety incidents to the state, and protect whistleblowers ([Governor's office](https://www.gov.ca.gov/2025/09/29/governor-newsom-signs-sb-53-advancing-californias-world-leading-artificial-intelligence-industry/)). It covers models trained with more than 10^26 operations, from developers with more than $500M in annual revenue, and caps civil penalties at $1M per violation ([Assembly committee analysis](https://apcp.assembly.ca.gov/system/files/2025-09/sb-53-wiener-apcp-analysis-9.11.pdf)). That's why xAI's framework says it "complies with California's Transparency in Frontier Artificial Intelligence Act," and why Anthropic keeps a separate compliance framework.

**US federal.** The administration wants one national standard and no licensing.

- Executive Order 14365 (December 2025) seeks one national standard instead of "50 discordant State ones" and sets up a Justice Department task force to challenge state AI laws ([White House](https://www.whitehouse.gov/presidential-actions/2025/12/eliminating-state-law-obstruction-of-national-artificial-intelligence-policy/)).
- Executive Order 14409 (June 2026) creates a voluntary framework with developers of "covered frontier models," including early government access and a classified cyber benchmark, and rules out "any mandatory governmental licensing" ([White House](https://www.whitehouse.gov/fact-sheets/2026/06/fact-sheet-president-donald-j-trump-promotes-advanced-artificial-intelligence-innovation-and-security/)).
- The first export controls on specific models came on June 12, 2026, when the US applied them to Claude Fable 5 and Mythos 5 after a reported safeguard bypass. Anthropic suspended access for all users. The controls were lifted by June 30. Mythos 5 access came back only for "a set of US organizations" after a June 26 government approval, and Fable 5 returned on July 1 ([Anthropic](https://www.anthropic.com/news/redeploying-fable-5)).

**The evaluator network.** In December 2025 the International Network of AI Safety Institutes became the "International Network for Advanced AI Measurement, Evaluation and Science," coordinated by the UK. Its ten members include the US and the EU ([GOV.UK](https://www.gov.uk/government/news/efforts-to-share-best-practices-on-ai-measurement-and-evaluations-driven-forward-through-the-international-network-for-advanced-ai-measurement-evalua)).

### Open debates

The closest thing to a consensus baseline is the [International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/2026-report-executive-summary) (February 3, 2026), led by Yoshua Bengio, written by more than 100 experts, and backed by more than 30 countries and organisations. It says "current systems lack the capabilities to pose" loss-of-control risks, and that safeguards "can reduce failure rates but not to the level required in many high-stakes settings." It explicitly declines to predict whether progress will plateau, continue steadily, or accelerate dramatically. And it frames the policy problem as an **evidence dilemma**: act early and you may entrench bad rules; wait for evidence and you may be exposed.

Beyond that baseline, serious people disagree. Here are the strongest versions of the main positions.

**How worried should we be?**

- **AI as normal technology.** Arvind Narayanan and Sayash Kapoor call superintelligence, as usually defined, incoherent, and catastrophic misalignment speculative. They put the defenses downstream, in security and institutions. "Policymakers should reject nonproliferation" ([Knight First Amendment Institute, April 2025](https://knightcolumbia.org/content/ai-as-normal-technology)).
- **Prohibition until proven safe.** The Superintelligence Statement calls for "a prohibition on the development of superintelligence" until there is "broad scientific consensus that it will be done safely and controllably" and "strong public buy-in." It had 78,825 signatures on November 16, 2026 ([superintelligence-statement.org](https://superintelligence-statement.org/)).
- **Low risk now, weak tools for later.** METR's position on Anthropic's Risk Report, quoted above, sits between these: agree the risk is low today, and doubt the methods would catch it if it rose.

**Who should set the rules?**

- **Labs, coordinating.** Anthropic argues that if one developer pauses while others push ahead, "the developers with the weakest protections would set the pace." So it separates unilateral commitments from industry recommendations and makes some commitments contingent on competitors ([RSP v3.4](https://assets.claude.com/0bacdc8440ea96e62a8766d99ebe1d4eea6d5f3a.pdf)).
- **Governments, with binding rules.** The EU AI Act and SB 53 turn parts of these frameworks into legal duties with reporting and penalties.
- **Governments, lightly.** The US administration says "America must lead the world in AI without burdening innovators with unnecessary regulation" and rules out licensing and pre-clearance ([White House, June 2026](https://www.whitehouse.gov/fact-sheets/2026/06/fact-sheet-president-donald-j-trump-promotes-advanced-artificial-intelligence-innovation-and-security/)).

**Should frontier weights be open?** Open weights let defenders, researchers, and anyone with a GPU use and study the model without permission, and they avoid concentrating control in a few companies. They also can't be recalled, and their safeguards come off cheaply (see [above](#fine-tuning-removes-safety) and [module 06](06-open-vs-closed-weights.md#the-safety-debate)). If open models trail the frontier by only months on cyber, gating a capability in a closed model buys a limited amount of time.

**Can we still trust evaluations?** Frameworks, thresholds, and system cards all rest on evaluations, and the people who run them say they're getting harder to trust (see [above](#chain-of-thought-monitorability-and-evaluation-awareness)). Nobody knows yet whether new methods will keep up.

## Try it

**Individual: read a safety section like an evaluator.**

Read the safety and alignment sections (not the launch post) of one current document:

- the [Claude Fable 5.2 / Mythos 5.2 system card](https://www.anthropic.com/claude-fable-5-2-mythos-5-2-system-card),
- the [GPT-6.1 Sol system card addendum](https://deploymentsafety.openai.com/gpt-6-1-sol/gpt-6-1-sol.pdf),
- the [Gemini 4 Argon model card](https://deepmind.google/models/model-cards/gemini-4-argon/), or
- Anthropic's [August 2026 Risk Report](https://www.anthropic.com/aug-2026-risk-report) paired with [METR's review](https://metr.org/blog/2026-10-20-misalignment-risk-report-august-2026-review/) of it.

Answer in about a page:

1. Which framework thresholds does it address, and what did the lab decide for each? Which determinations did someone outside the lab check?
2. List three concerning behaviors it reports. For each, what setting was it observed in (contrived test, RL training, eval with real effects, internal use, deployment)? What can that setting support, and what can't it?
3. What does it say about evaluation awareness or chain-of-thought monitorability? How much does that limit what the rest of the alignment section can tell you?
4. Which numbers are self-reported by the lab, and which come from a third party?
5. Name one finding that should change how you supervise a coding agent built on this model.
6. What would change your mind about the overall risk level the document claims? Name a specific result, from whom.

**Class or team: the open-weights safety debate.**

Split into two sides. Scenario: a lab plans to release open weights for a model that matches today's closed frontier on coding and comes within a few months of it on cyber.

1. Side A argues for release, side B against. Each side prepares for fifteen minutes using at least three sources from this module or [module 06](06-open-vs-closed-weights.md#the-safety-debate), and must state the strongest point *for the other side*.
2. Each side presents for five minutes, with two minutes of rebuttal.
3. Together, write a one-paragraph policy both sides could live with: what conditions, evaluations, or delays would it require, and what evidence would make you revisit it? Compare it with what Meta's framework, the EU AI Act, and the US approach actually do.

## Discussion questions

1. Emergent misalignment went away when the same insecure code was framed as being for a security class. What does that suggest about what fine-tuning actually teaches a model?
2. If you can strip safety training from open weights for a few hundred dollars, what does that mean for open-weight releases? What's the strongest argument on each side ([module 06](06-open-vs-closed-weights.md))?
3. Most rows in the concerning-behaviors table come from contrived tests. What would you need to see, and in which setting, before you changed how much autonomy you give your own coding agent?
4. If models increasingly notice when they're being tested, what kinds of evidence could still convince you that a model is safe to deploy?
5. Anthropic's RSP v3 makes some commitments contingent on what competitors do. Is that realism about a collective-action problem, or a loophole? Give the strongest case for each.
6. In the UK AISI incident, internet access and cyber classifiers were deliberately set in a way AISI says doesn't reflect how frontier models are made available to the public. Does that make the incident less relevant to you as a developer, or more?

## Sources and further reading

### Papers

- [Concrete Problems in AI Safety](https://arxiv.org/abs/1606.06565) (Amodei, Olah, Steinhardt, Christiano, Schulman, Mané, 2016)
- [Risks from Learned Optimization in Advanced Machine Learning Systems](https://arxiv.org/abs/1906.01820) (Hubinger et al., 2019)
- [Goal Misgeneralization: Why Correct Specifications Aren't Enough For Correct Goals](https://arxiv.org/abs/2210.01790) (Shah et al., 2022)
- [Training Language Models to Follow Instructions with Human Feedback](https://arxiv.org/abs/2203.02155) (Ouyang et al., 2022)
- [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073) (Bai et al., 2022)
- [XSTest: A Test Suite for Identifying Exaggerated Safety Behaviours in Large Language Models](https://arxiv.org/abs/2308.01263) (Röttger et al., 2023)
- [Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!](https://arxiv.org/abs/2310.03693) (Qi et al., 2023)
- [Towards Understanding Sycophancy in Language Models](https://arxiv.org/abs/2310.13548) (Sharma et al., 2023)
- [LoRA Fine-tuning Efficiently Undoes Safety Training in Llama 2-Chat 70B](https://arxiv.org/abs/2310.20624) (Lermen, Rogers-Smith, Ladish, 2023)
- [OR-Bench: An Over-Refusal Benchmark for Large Language Models](https://arxiv.org/abs/2405.20947) (Cui et al., 2024)
- [AI Sandbagging: Language Models can Strategically Underperform on Evaluations](https://arxiv.org/abs/2406.07358) (van der Weij et al., 2024)
- [Refusal in Language Models Is Mediated by a Single Direction](https://arxiv.org/abs/2406.11717) (Arditi et al., 2024)
- [Frontier Models are Capable of In-context Scheming](https://arxiv.org/abs/2412.04984) (Meinke et al., Apollo Research, 2024)
- [Alignment Faking in Large Language Models](https://arxiv.org/abs/2412.14093) (Greenblatt et al., 2024)
- [Deliberative Alignment: Reasoning Enables Safer Language Models](https://arxiv.org/abs/2412.16339) (Guan et al., 2024)
- [Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs](https://arxiv.org/abs/2502.17424) (Betley et al., 2025); extended version in [Nature](https://www.nature.com/articles/s41586-025-09937-5) (2026)
- [Auditing Language Models for Hidden Objectives](https://arxiv.org/abs/2503.10965) (Marks et al., 2025)
- [Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation](https://arxiv.org/abs/2503.11926) (Baker et al., 2025)
- [Measuring AI Ability to Complete Long Tasks](https://arxiv.org/abs/2503.14499) (Kwa et al., 2025)
- [An Approach to Technical AGI Safety and Security](https://arxiv.org/abs/2504.01849) (Shah et al., Google DeepMind, 2025)
- [Reasoning Models Don't Always Say What They Think](https://arxiv.org/abs/2505.05410) (Chen et al., 2025)
- [Persona Features Control Emergent Misalignment](https://arxiv.org/abs/2506.19823) (Wang et al., 2025)
- [Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety](https://arxiv.org/abs/2507.11473) (Korbak et al., 2025)
- [Persona Vectors: Monitoring and Controlling Character Traits in Language Models](https://arxiv.org/abs/2507.21509) (Chen et al., 2025)
- [From Hard Refusals to Safe-Completions: Toward Output-Centric Safety Training](https://arxiv.org/abs/2508.09224) (Yuan et al., 2025)
- [Stress Testing Deliberative Alignment for Anti-Scheming Training](https://arxiv.org/abs/2509.15541) (Schoen et al., Apollo Research and OpenAI, 2025)
- [Agentic Misalignment: How LLMs Could Be Insider Threats](https://arxiv.org/abs/2510.05179) (Lynch et al., 2025)
- [ImpossibleBench: Measuring LLMs' Propensity of Exploiting Test Cases](https://arxiv.org/abs/2510.20270) (Zhong et al., 2025)
- [Weight-sparse Transformers Have Interpretable Circuits](https://arxiv.org/abs/2511.13653) (Gao et al., 2025)
- [Natural Emergent Misalignment from Reward Hacking in Production RL](https://arxiv.org/abs/2511.18397) (MacDiarmid et al., 2025)
- Anthropic interpretability: [Circuit Tracing](https://transformer-circuits.pub/2025/attribution-graphs/methods.html) (2025), [Emergent Introspective Awareness in Large Language Models](https://transformer-circuits.pub/2025/introspection/index.html) (Lindsey, 2025), [Natural Language Autoencoders](https://transformer-circuits.pub/2026/nla/index.html) (2026), [the global workspace paper](https://transformer-circuits.pub/2026/workspace/index.html) (2026)

### Primary sources

**Specifications and frameworks**
- Anthropic, [Claude's new constitution](https://www.anthropic.com/news/claude-new-constitution) (January 22, 2026) and [the constitution](https://www.anthropic.com/constitution)
- OpenAI, [Model Spec 2026-10-29](https://model-spec.openai.com/2026-10-29.html) and [changelog](https://github.com/openai/model_spec/blob/main/CHANGELOG.md)
- Anthropic, [Responsible Scaling Policy](https://www.anthropic.com/responsible-scaling-policy) ([v3.4 PDF](https://assets.claude.com/0bacdc8440ea96e62a8766d99ebe1d4eea6d5f3a.pdf), July 8, 2026), [RSP v3 announcement](https://www.anthropic.com/news/responsible-scaling-policy-v3) (February 24, 2026), [RSP updates and Risk Reports](https://www.anthropic.com/rsp-updates), [Frontier Compliance Framework for SB 53](https://www.anthropic.com/news/compliance-framework-SB53)
- OpenAI, [Preparedness Framework v2](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf) (April 15, 2025)
- Google DeepMind, [Frontier Safety Framework 3.1](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3-1.pdf) (April 17, 2026) and [Strengthening our Frontier Safety Framework](https://deepmind.google/discover/blog/strengthening-our-frontier-safety-framework/)
- Meta, [Advanced AI Scaling Framework announcement](https://ai.meta.com/blog/scaling-how-we-build-test-advanced-ai/) (April 8, 2026)
- xAI, [Frontier Artificial Intelligence Framework](https://data.x.ai/2025-12-31-xai-frontier-artificial-intelligence-framework.pdf) (December 30, 2025)
- Google DeepMind, [Specification gaming: the flip side of AI ingenuity](https://deepmind.google/discover/blog/specification-gaming-the-flip-side-of-ai-ingenuity/) (2020)

**System cards and risk reports**
- Anthropic, [Claude Fable 5.2 / Mythos 5.2 system card](https://www.anthropic.com/claude-fable-5-2-mythos-5-2-system-card) (November 9, 2026), [Risk Report, August 2026](https://www.anthropic.com/aug-2026-risk-report), [Redeploying Claude Fable 5](https://www.anthropic.com/news/redeploying-fable-5) (June 30, 2026)
- OpenAI, [Deployment Safety Hub](https://deploymentsafety.openai.com/), [GPT-6 Astra system card](https://deploymentsafety.openai.com/gpt-6-astra) (September 3, 2026), [GPT-6.1 Sol system card addendum](https://deploymentsafety.openai.com/gpt-6-1-sol/gpt-6-1-sol.pdf) (September 29, 2026)
- OpenAI, [Sycophancy in GPT-4o](https://openai.com/index/sycophancy-in-gpt-4o/) and [Expanding on what we missed with sycophancy](https://openai.com/index/expanding-on-sycophancy/) (2025)
- Google DeepMind, [Gemini 4 Argon model card](https://deepmind.google/models/model-cards/gemini-4-argon/) (October 13, 2026)
- xAI, [Grok 4.7 model card](https://media.x.ai/v1/website/card4p7-3a96f40b.pdf) (September 21, 2026)
- Anthropic, [Alignment faking in large language models](https://www.anthropic.com/research/alignment-faking) (2024), [Agentic misalignment](https://www.anthropic.com/research/agentic-misalignment) (2025), [Open-sourcing circuit tracing tools](https://www.anthropic.com/research/open-source-circuit-tracing) (2025)
- Google DeepMind, [Gemma Scope 2](https://deepmind.google/blog/gemma-scope-2-helping-the-ai-safety-community-deepen-understanding-of-complex-language-model-behavior/) (December 2025)

**Independent evaluators**
- UK AI Security Institute: [Frontier AI Trends Report](https://www.aisi.gov.uk/frontier-ai-trends-report), [Our evaluation of Claude Mythos Preview's cyber capabilities](https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities) (2026), [Incident report: unsanctioned agent behaviour during cyber testing](https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing) (August 4, 2026), [Investigating alignment failures in AISI's incident](https://www.aisi.gov.uk/blog/investigating-alignment-failures-in-aisis-incident) (October 23, 2026), [How far behind the frontier are leading open-weight models on cyber?](https://www.aisi.gov.uk/blog/how-far-behind-the-frontier-are-leading-open-weight-models-on-cyber)
- METR: [Recent frontier models are reward hacking](https://metr.org/blog/2025-06-05-recent-reward-hacking/) (2025), [Frontier Risk Report](https://metr.org/blog/2026-05-19-frontier-risk-report/) (May 2026), [time horizons](https://metr.org/time-horizons/), [OpenAI / Hugging Face incident investigation](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/) (August 26, 2026), [Senate testimony](https://metr.org/blog/2026-09-30-chris-painter-senate-testimony/) (September 30, 2026), [AI systems could cover up misbehavior](https://metr.org/blog/2026-10-06-ai-systems-could-cover-up-misbehavior/) (October 2026), [Review of Anthropic's misalignment Risk Report](https://metr.org/blog/2026-10-20-misalignment-risk-report-august-2026-review/) (October 20, 2026), [Red-teaming OpenAI's agent monitoring](https://metr.org/blog/2026-10-22-red-teaming-openai-agent-monitoring/) (October 2026), [Anthropic AI R&D acceleration assessment](https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/) (November 5, 2026), [Review of the Risk Report's R&D section](https://metr.org/blog/2026-11-05-rd-section-anthropic-risk-report-august-2026-review/) (November 5, 2026)
- [Apollo Research](https://www.apolloresearch.ai/research)
- NIST, [CAISI / CAISSI](https://www.nist.gov/caisi)

**Policy**
- European Commission, [AI Act regulatory framework](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai), [GPAI guidelines](https://digital-strategy.ec.europa.eu/en/policies/guidelines-gpai-providers), [GPAI Code of Practice](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai); [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng)
- California: [Governor's office on SB 53](https://www.gov.ca.gov/2025/09/29/governor-newsom-signs-sb-53-advancing-californias-world-leading-artificial-intelligence-industry/), [Assembly Privacy Committee analysis](https://apcp.assembly.ca.gov/system/files/2025-09/sb-53-wiener-apcp-analysis-9.11.pdf), [Attorney General SB 53 page](https://oag.ca.gov/sb53)
- White House: [America's AI Action Plan](https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf) (July 2025), [EO 14365](https://www.whitehouse.gov/presidential-actions/2025/12/eliminating-state-law-obstruction-of-national-artificial-intelligence-policy/) (December 2025), [legislative recommendations](https://www.whitehouse.gov/wp-content/uploads/2026/03/03.20.26-National-Policy-Framework-for-Artificial-Intelligence-Legislative-Recommendations.pdf) (March 2026), [EO 14409 fact sheet](https://www.whitehouse.gov/fact-sheets/2026/06/fact-sheet-president-donald-j-trump-promotes-advanced-artificial-intelligence-innovation-and-security/) (June 2026)
- GOV.UK, [International Network for Advanced AI Measurement, Evaluation and Science](https://www.gov.uk/government/news/efforts-to-share-best-practices-on-ai-measurement-and-evaluations-driven-forward-through-the-international-network-for-advanced-ai-measurement-evalua) (December 2025)

### Learning resources (start here)

- **[International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026)** and its three-page [executive summary](https://internationalaisafetyreport.org/publication/2026-report-executive-summary): the closest thing to a consensus baseline.
- **[BlueDot Impact courses](https://bluedot.org/courses)**: "Future of AI" (free, about 90 minutes) for a first pass, then "Technical AI Safety" or "AGI Strategy" (25–40 hours each).
- **UK AISI's [Frontier AI Trends Report](https://www.aisi.gov.uk/frontier-ai-trends-report) and blog**: government measurements plus candid incident write-ups.
- **A lab's claims next to an outside critique**: Anthropic's [August 2026 Risk Report](https://www.anthropic.com/aug-2026-risk-report) with METR's [two](https://metr.org/blog/2026-10-20-misalignment-risk-report-august-2026-review/) [reviews](https://metr.org/blog/2026-11-05-rd-section-anthropic-risk-report-august-2026-review/) of it.
- **[Concrete Problems in AI Safety](https://arxiv.org/abs/1606.06565)** (2016): still the cleanest vocabulary for the field.

### Commentary and debate

- Arvind Narayanan and Sayash Kapoor, [AI as Normal Technology](https://knightcolumbia.org/content/ai-as-normal-technology) (Knight First Amendment Institute, April 2025)
- [Statement on Superintelligence](https://superintelligence-statement.org/)
- TechCrunch, [Anthropic warns that it's very close to RSI capability](https://techcrunch.com/2026/11/02/anthropic-warns-that-its-very-close-to-rsi-capability-aka-self-building-ai/) (November 2, 2026)

See also [module 03](03-post-training-and-rl.md) for how training works, [module 14](14-security-and-prompt-injection.md) for securing what you build, the [reading list](../reference/papers.md), and the [glossary](../reference/glossary.md).

## Terms introduced

- **Alignment**: Whether a model's own tendencies and goals match what its developers and users intend.
- **Misuse**: Harm caused by a person deliberately using a model for a harmful purpose.
- **Misalignment**: A model pursuing goals or behaviors its developers didn't intend.
- **Specification gaming**: Satisfying the literal specification of an objective without achieving the intended outcome.
- **Outer alignment**: Whether a training objective actually captures what its designers want.
- **Inner alignment**: Whether a trained model actually learned the objective it was trained on, rather than something that merely scored well.
- **Goal misgeneralization**: A model learning the wrong goal despite a correct specification, and pursuing it competently in new situations.
- **Model Spec**: OpenAI's public document describing how its models should behave, including a chain of command among instruction sources.
- **Corrigibility**: A model staying open to legitimate human oversight and correction.
- **Safe completion**: OpenAI's approach of answering as helpfully as safety policy allows instead of choosing between full compliance and refusal.
- **Over-refusal**: A model declining safe requests because they superficially resemble harmful ones.
- **Safety case**: A structured argument, backed by evidence, that a system is safe enough for a given deployment.
- **Inoculation prompting**: Framing an undesired behavior as acceptable during training so the model doesn't generalize it into broader misbehavior.
- **Frontier safety framework**: A lab's published policy for which dangerous capabilities it tracks, at what thresholds, and what it does when a model reaches them.
- **AI Safety Level (ASL)**: Anthropic's former labels for levels of safeguards; since 2026 used only for present mitigation levels, not to label models.
- **Risk Report**: Anthropic's periodic cross-model assessment of risk under its RSP.
- **Dangerous-capability evaluation**: A test of whether a model can do something seriously harmful, such as uplift for weapons or autonomous cyberattacks.
- **Alignment faking**: A model selectively complying with training to avoid having its preferences changed.
- **Scheming**: A model covertly pursuing goals that conflict with its developers' or users' intentions.
- **Sandbagging**: Deliberately underperforming on an evaluation.
- **Agentic misalignment**: An agent taking harmful actions, such as blackmail or sabotage, to pursue its goals.
- **Emergent misalignment**: Broad misaligned behavior arising from narrow fine-tuning, such as on insecure code.
- **Evaluation awareness**: A model recognizing that it is being tested, which can change how it behaves.
- **Chain-of-thought monitorability**: How well a model's written reasoning lets an observer detect undesired behavior.

# 15: Learning, careers, and responsible use

> **Audience:** everyone · **Reading time:** ~30 min · **Last verified:** 2026-11-08
> **Depth guide:** Students: Foundations, "How to learn with AI," academic integrity, and careers. Working engineers: the evidence, careers, and the human side. Leads and instructors: academic integrity, responsible use, and Going deeper.

**TL;DR**
- **How** you use AI decides whether you learn. In a 2026 randomized trial, developers learning a new library with an AI assistant scored 17 percentage points lower on a follow-up quiz than those who coded by hand. Participants who used the AI to ask conceptual questions and explain code did about as well as the hand-coders. Those who delegated did worst.
- The pattern repeats across studies: AI as an answer machine weakens learning; AI as a tutor that gives hints and explanations doesn't, and can help. People who trust AI more tend to think less critically about its output.
- Early-career software hiring is under real pressure. Payroll data show employment of 22–25-year-olds in AI-exposed occupations about 19% below trend by mid-2026, mostly through fewer hires. The cause is debated, and overall employment in the field is still projected to grow.
- The skills that gain value are the ones agents can't supply for you: specifying, decomposing, reading and reviewing code, debugging, testing, systems thinking, domain knowledge, and communication.
- Responsible use means: don't paste secrets or other people's data into consumer tools; know who owns and can copyright what you generate; disclose AI help where your course or project expects it; and accept that **you** are accountable for anything you ship.

## Foundations

### Producing the work vs learning from it

At work, the output is the point. A merged pull request that fixes the bug is a success whether you or an agent typed it.

In school, and whenever you're learning something new, the output is mostly a side effect. The point is the change in your head: the mental model of how async code works, the instinct for where a bug hides. That change comes from effortful processing: trying, failing, figuring out why, trying again. If an AI does the effortful part, you get the artifact without the learning.

That is the core tension of this module. The same tool that makes an experienced engineer faster can make a learner skip exactly the struggle that would have made them experienced.

### What the evidence says

Research on AI and learning is young, fast-moving, and mostly short-term. Read each study for what it measured, not for its headline.

**Learning a new coding library (Anthropic, 2026).** Shen and Tamkin ran a randomized controlled trial with 52 mostly junior software engineers who used Python weekly but had never used Trio, a library for asynchronous programming ([How AI Impacts Skill Formation](https://arxiv.org/abs/2601.20245), January 2026; [summary](https://www.anthropic.com/research/AI-assistance-coding-skills)). Everyone built two features with Trio, then took a quiz on debugging, reading, writing, and concepts.
- The AI group averaged **50%** on the quiz; the hand-coding group **67%**. That is a large, statistically significant gap (about two letter grades).
- The AI group finished about two minutes faster, a difference that was **not** statistically significant.
- The biggest gap was on **debugging** questions.
- How people used the AI mattered. Participants who asked only conceptual questions, asked for code together with explanations, or generated code and then asked follow-up questions to understand it scored 65% or higher. Those who delegated the task, relied more and more on AI as they went, or had the AI debug for them scored below 40%. These patterns come from small subgroups (2–7 people each), so they are suggestive, not proof.
- Limits: small sample, a quiz right after the task rather than long-term retention, and a chat-sidebar assistant rather than an autonomous agent. The authors expect agents could widen the gap.

**High-school math (Bastani et al., PNAS 2025).** In a field experiment with roughly a thousand high-school students in Turkey, students got either a plain GPT-4 chat interface ("GPT Base"), a version prompted to act as a tutor that gives hints rather than answers ("GPT Tutor"), or no AI during practice sessions ([Generative AI without guardrails can harm learning](https://doi.org/10.1073/pnas.2422633122), 2025). Both AI groups did much better *during* practice. On a later exam without AI, the GPT Base group did about 17% worse than students who never had AI, while the GPT Tutor group showed no significant harm. Students in the GPT Base group largely used it to get answers.

**Critical thinking at work (Lee et al., CHI 2025).** A Microsoft Research and Carnegie Mellon survey of 319 knowledge workers, covering 936 real examples of using generative AI at work, found that **higher confidence in the AI was associated with less critical thinking**, while higher confidence in one's *own* ability was associated with more ([The Impact of Generative AI on Critical Thinking](https://doi.org/10.1145/3706598.3713778), 2025). Critical thinking shifted from producing work toward verifying, integrating, and overseeing AI output. This is self-reported survey data, not a measurement of thinking.

**"Your Brain on ChatGPT" (Kosmyna et al., 2025).** An MIT Media Lab study recorded EEG while 54 participants wrote essays with an LLM, with a search engine, or with no tools ([Your Brain on ChatGPT](https://arxiv.org/abs/2506.08872)). The LLM group showed the weakest brain connectivity, felt the least ownership of their essays, and often couldn't accurately quote what they had just written. The authors call the effect "cognitive debt." Read it carefully: it is a preprint; the sample is small, and only 18 people completed the crucial fourth session; the task was essay writing, not programming; and EEG connectivity is not a direct measure of learning. Media coverage overstated it ("ChatGPT rots your brain"). It is one interesting data point, not a verdict.

**Perceived vs measured speed (METR, 2025).** In a randomized study, 16 experienced open-source developers took **19% longer** on tasks in their own repositories when allowed to use early-2025 AI tools, while believing afterward that AI had made them about 20% faster ([Becker et al., 2025](https://arxiv.org/abs/2507.09089)). Tools have improved a lot since. The durable finding is that people are poor judges of their own AI-assisted performance.

**Overconfidence in security (Perry et al., 2022).** Participants with an AI assistant wrote less secure code *and* were more likely to believe it was secure ([Do Users Write More Insecure Code with AI Assistants?](https://arxiv.org/abs/2211.03622)). See [module 11](./11-security-and-prompt-injection.md).

**The synthesis.** No credible study says "AI use always harms learning" or "always helps." The consistent signal: *outsourcing the thinking* hurts the skill you outsourced; *using AI to think better* (asking why, getting hints, checking your understanding) mostly doesn't, and sometimes helps. Feeling productive is not evidence of learning.

## In practice

### How to learn with AI instead of outsourcing learning

These habits come straight from the studies above. They cost some speed now and pay back later.

1. **Attempt first.** Give yourself a fixed time (15–30 minutes) to try on your own before asking. Write down where you got stuck. Your question will be better, and the struggle is where the learning happens.
2. **Ask for hints, not answers.** Tell the model what you want from it:

   ```text
   I'm learning Python async with Trio. Don't write the code for me.
   Here's my attempt and the error I get. Ask me one question that
   points me toward the bug, and wait for my answer before saying more.
   ```

3. **Ask conceptual questions.** "Why does Trio use nurseries instead of free-floating tasks?" teaches more than "write a nursery for me." In the Anthropic trial, people who asked only conceptual questions scored about as well as people who used no AI.
4. **Explain it back.** After the AI explains something, close the chat and explain it in your own words, out loud or in writing. Then ask the model to check your explanation for mistakes.
5. **Read every line it writes.** If you can't explain a line, you don't understand the program yet. Ask about that line specifically.
6. **Debug yourself first.** Debugging showed the largest gap in the trial, and it is the skill you most need for supervising agents later. Read the error, form a hypothesis, test it. Ask the AI only after you have a hypothesis.
7. **Rebuild from scratch.** After finishing an AI-assisted exercise, delete it and rebuild the core part without AI the next day. Whatever you can't rebuild, you didn't learn.
8. **Keep a "things I didn't understand" log.** Every time you accept something you don't fully understand, write one line. Review the log weekly and close the gaps.
9. **Use the learning modes.** Claude Code has a built-in **Learning** output style that explains its choices and leaves small pieces of real design work for you, marked `TODO(human)`, then waits for you to write them ([docs](https://code.claude.com/docs/en/output-styles)). Switch with `/output-style learning`. ChatGPT has a study mode that tutors step by step instead of answering, and other chat apps have similar modes.
10. **Turn off autocomplete when learning a new language.** Inline suggestions are the most frictionless way to skip thinking. Turn them back on when you know the language.
11. **Practice without AI sometimes.** Pilots still hand-fly. Do some exercises, timed problems, or a weekly hour of coding with no assistant at all.

A note for working engineers moving to a new language, framework, or codebase: these same habits apply to you. The Anthropic trial's participants were professionals, not students.

### Academic integrity

#### Common policy patterns

Universities handle AI in a few recognizable ways. Most let the instructor decide per course, with a default for when the instructor says nothing.

| Pattern | Example | What it means for students |
| --- | --- | --- |
| **Default restrictive, instructor can open up** | [Stanford's guidance](https://communitystandards.stanford.edu/generative-ai-policy-guidance): absent a written course policy, AI may be used to study and prepare (self-quizzing, extra practice problems) and for surface edits like spelling, but not to create deliverables; other uses must be disclosed | Assume no unless told yes |
| **Course-provided AI only** | [CS50](https://cs50.harvard.edu/x/honesty/): using CS50's own AI tutor (the "duck") is reasonable; using other AI tools that suggest or complete answers or code is not | Use the tutor the course provides |
| **Allowed with disclosure** | Many writing and project courses | Use it, say how, own the result |
| **Required** | Courses like the one this material supports | Learn to use it well; you'll be graded on judgment |

Always check your own institution's academic integrity policy and each course's syllabus. When in doubt, ask the instructor in writing before you submit.

#### What instructors can reasonably allow

AI use is easy to do and hard to detect reliably. Policies that depend on catching it tend to fail and to punish students unevenly. Policies that design assessment around it tend to work. Reasonable options:

- **Separate learning from producing.** Some assignments are explicitly AI-free (fundamentals, timed in-class work). Others are AI-encouraged (projects, where judgment is graded).
- **Grade understanding, not just artifacts.** Short oral explain-backs, code walkthroughs, live debugging of the student's own submission.
- **Grade the process.** Ask for the commit history, a short AI-use log, and agent transcripts for key decisions.
- **Teach disclosure as a professional norm**, not a confession.

#### A suggested policy for an AI-accelerated course

```text
AI use policy

1. Tiers. Each assignment is labeled:
   - AI-free: no AI tools. Tests fundamentals you must have without help.
   - AI-as-tutor: AI may explain, give hints, and review your work.
     It may not write code you submit.
   - AI-accelerated: use any AI tools. You are graded on the result,
     your design decisions, and your ability to explain every line.

2. Disclosure. For AI-as-tutor and AI-accelerated work, include a short
   AI log: which tools, what you used them for, one thing the AI got
   wrong that you caught, and one thing you learned.

3. Ownership. You are responsible for all submitted code, including
   bugs, security flaws, and license problems introduced by AI.

4. Explain-back. Any submission may be followed by a 5-minute
   walkthrough. If you can't explain it, it doesn't count as yours.

5. Data. Don't paste other students' work, personal data, or
   credentials into AI tools.
```

#### Disclosure template for students

```text
AI assistance: I used [tool] to [explain X / suggest a fix for Y /
generate the initial version of Z]. I reviewed and modified the output,
[wrote the tests myself / rewrote the parser]. The AI incorrectly
[suggested a package that doesn't exist / missed an edge case], which
I caught by [running the tests / reading the docs].
```

### Careers

#### What the evidence says about early-career jobs

The most-cited evidence comes from Stanford's Digital Economy Lab. Brynjolfsson, Chandar, and Chen use ADP payroll data covering millions of US workers ([Canaries in the Coal Mine?](https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/)).

- The first version (August 2025) reported that workers aged 22–25 in the most AI-exposed occupations, including software developers, had seen a relative employment decline since late 2022, while older workers in the same jobs had not.
- A revised version (12 August 2026, data through June 2026) finds employment of 22–25-year-olds in AI-exposed occupations **19% below** where it would be had it kept pace with less-exposed peers. The gap has widened since 2025.
- The decline comes mainly from **fewer hires of young workers**, not from layoffs.
- It is concentrated where AI mainly **substitutes** for tasks. Where AI mainly **complements** workers, employment is flat or rising, especially for experienced workers.
- The authors find **no broad, economy-wide job displacement**, call their results descriptive rather than causal, and report that the pattern holds when excluding tech firms and when controlling for interest-rate exposure and remote work. A February 2026 update addressed critics who attributed the timing to interest rates.

#### Counter-evidence and uncertainty

- Other explanations remain plausible and may combine: the post-2022 correction after pandemic over-hiring in tech, higher interest rates, offshoring, and companies pausing junior hiring while they figure out AI. The authors' controls address some of these, not all.
- The US Bureau of Labor Statistics still projects software developer employment to **grow 10%** from 2025 to 2035, much faster than average ([BLS](https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm)). Projections can be wrong in both directions.
- Developers themselves are cautious about the tools. In Stack Overflow's 2025 survey, 84% used or planned to use AI tools, but only 33% trusted their accuracy and 46% distrusted it; the top frustration (66%) was "AI solutions that are almost right, but not quite" ([survey](https://survey.stackoverflow.co/2025/ai)). Someone still has to catch the "almost right."
- Nobody knows the long-run effect. If companies stop hiring juniors, they eventually run out of seniors. Some firms are betting that AI-fluent juniors are a bargain; others are cutting junior roles. Both strategies are being tried right now.

An honest summary: entry-level software work is getting harder to find, AI is a plausible part of why, and the people who get hired are the ones who show they can do what the tools can't.

#### Skills that gain value

| Skill | Why it matters more with agents |
| --- | --- |
| **Specification** | Agents do what you ask. Saying precisely what you want, including edge cases and non-goals, is the main lever ([module 07](./07-context-engineering.md)). |
| **Decomposition** | Breaking work into pieces an agent can do and you can verify. |
| **Reading and review** | You will read far more code than you write. Spotting the subtle bug in 400 plausible lines is the job ([module 10](./10-ai-code-review.md)). |
| **Debugging** | When the agent is stuck or confidently wrong, someone has to find the real cause. |
| **Testing and verification** | Tests turn "looks right" into "is right," and they are how agents check their own work. |
| **Systems thinking** | Agents optimize locally. Architecture, data flow, failure modes, and cost are still human calls. |
| **Security judgment** | Knowing what not to give an agent access to ([module 11](./11-security-and-prompt-injection.md)). |
| **Domain knowledge** | The agent doesn't know your users, your regulations, or why the weird business rule exists. |
| **Communication** | Writing clear issues, design docs, and PR descriptions helps humans and agents alike. |
| **Taste** | Knowing which of five working solutions is the one you'll be glad you kept in two years. |
| **Product sense** | As agents take on more of the *how*, more of an engineer's day goes to *what* and *why*: which problem is worth solving, for whom, and what "done" looks like. |

#### The classes you thought you'd never use

When agents write more of the code, the parts of a CS degree that felt least like programming start to matter more.

- **Software engineering and project management.** Estimation, scheduling, dependencies, and risk. Brooks's law, from *The Mythical Man-Month* (1975), says "adding manpower to a late software project makes it later," because coordination costs grow with every person you add. It applies to agents too: Cursor found that twenty agents working on one codebase slowed to the throughput of two or three ([module 09](./09-multi-agent-systems.md)).
- **System design.** An agent can implement a design. Choosing the right one, and knowing which questions to ask about scale, failure, data, and cost, is still your job. Good system design chops also make your prompts better, because you know what to ask the agent about.
- **Algorithms and data structures.** An agent can write a heap from memory. You still need to recognize when you need one, notice when its solution is accidentally quadratic, and, for now, pass interviews that test this directly.
- **Communication and product.** Writing a clear spec, running a demo, and understanding what users actually need.

> **Bryan's take:** Ultimately the engineer is much more in product now. Some of the classes software engineers take, the ones they don't think will be useful, turn out to be among the most important. I used Gantt charts and quoted *The Mythical Man-Month* far more in my career than I expected. You still need to know the algorithms to pass the interviews, at least for now. Having good system design chops helps a lot too. You need to know what questions to talk to the agent about.

#### Portfolios in the AI era

A portfolio of ten AI-generated apps proves little: anyone can make them. Show judgment instead:

- **One or two deep projects** you have maintained over time, with real users if possible.
- **Tests, design notes, and a README** that explains trade-offs you made and alternatives you rejected.
- **Honest AI usage.** Say where agents helped and where you overrode them. Hiring managers increasingly ask.
- **Code review and debugging stories.** A write-up of a hard bug you found (including one an AI introduced) is more convincing than a feature list.
- **Open-source contributions**, following each project's contribution and AI policy. Some projects ban AI-generated contributions entirely; read the rules first.

#### Interviewing with and without AI

Companies are split. Some now expect AI use in technical interviews: Canva, for example, announced in June 2025 that backend, ML, and frontend candidates would use tools like Copilot, Cursor, and Claude, with harder and more ambiguous problems, and evaluates whether candidates break down requirements, make sound decisions, and catch and fix problems in AI-generated code ([Canva engineering blog](https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/)). Others forbid AI in interviews and use in-person or proctored formats to enforce it.

Prepare for both. Practice solving problems without AI, out loud. Separately, practice driving an agent on an unfamiliar problem while narrating your decisions, especially the moment you reject its suggestion and why.

#### For engineers worried about their jobs

- Get good at the tools. The evidence suggests AI complements experienced workers more than it replaces them, and fluency is becoming a baseline expectation.
- Invest in the skills table above, and in the domain you work in.
- Measure your own results, not your feelings (see METR above), and share what works with your team. Champions who help others adopt well become more valuable, not less.
- Keep your fundamentals sharp. When tools change or fail, people who understand the system underneath are the ones who fix it.

### Responsible use

#### Data privacy: what not to paste

Treat anything you paste into an AI tool as data you are sending to a third party. Don't paste:

- Passwords, API keys, tokens, private keys, connection strings.
- Personal data about other people: customers, patients, classmates, coworkers. Student records and health information often carry legal obligations.
- Your employer's or client's proprietary code or documents, unless they have approved that tool for that use.
- Other students' work.
- Anything you'd be uncomfortable seeing in a breach notification.

**Consumer vs enterprise terms differ.** Consumer and business products from the same lab often have different data rules:

- Anthropic changed its consumer terms on 28 August 2025: Free, Pro, and Max users (including Claude Code on those plans) choose whether their chats and coding sessions are used for training. If they allow it, data is retained for up to five years; if not, the existing 30-day retention applies. Team, Enterprise, Education, Government, and API use are excluded ([Anthropic](https://www.anthropic.com/news/updates-to-our-consumer-terms)).
- ChatGPT consumer accounts have a setting to stop your conversations being used to improve models; OpenAI's business and API offerings don't train on customer data by default.
- Team and enterprise plans generally add admin controls, retention settings, and contractual commitments. Some organizations also negotiate zero data retention. See [module 12](./12-costs-subscriptions-and-apis.md).

Check your settings now, and recheck after any terms update. Defaults change.

#### Licensing and copyright of generated code

Two separate questions: *can anyone own this code?* and *does this code infringe someone else's?*

**Ownership (US).** The US Copyright Office's [report on copyrightability](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf) (Part 2, 29 January 2025) concluded that existing law is adequate: AI-generated output can be protected "in whole or in part" where AI is used as a tool and a human determined the expressive elements, but "prompts alone, however, at this stage are unlikely to satisfy those requirements." Human-authored portions, and human selection, arrangement, and modification of AI output, can be protected. The Office did not recommend new legislation. Part 3, on training models with copyrighted works, was released in pre-publication form on 9 May 2025 ([copyright.gov/ai](https://www.copyright.gov/ai/)). Other countries differ. Practically: code you substantially shape, review, and modify is on firmer ground than code you generated with one prompt and never touched, and your employer's or school's IP rules still apply.

**Infringement and license contamination.** Models sometimes reproduce code from their training data, including code under copyleft licenses such as the GPL, which carry obligations if you distribute it. The risk is highest for long, distinctive snippets. Mitigations: some assistants offer filters that block or flag suggestions matching public code; license scanners in CI catch known snippets; and you should be suspicious of any large, polished block that appears instantly for a niche problem.

**Project policies vary.** Some open-source projects ban AI-generated contributions outright. Gentoo did so in April 2024, citing copyright uncertainty, quality, and ethics ([policy](https://wiki.gentoo.org/wiki/Project:Council/AI_policy)). Others allow AI help with disclosure and full contributor accountability. Read `CONTRIBUTING.md` before you open a pull request.

#### Attribution and disclosure in commits and PRs

- **Follow the project's rule.** Some projects want a trailer such as `Co-Authored-By:` or `Assisted-by:` naming the tool; some want a note in the PR description; some forbid AI use.
- **Many agents add attribution by default.** Claude Code, for example, adds a co-author trailer to commits it creates unless configured otherwise. Leave it on unless your project says otherwise.
- **You are still the author of record.** Attribution says how the work was made. It does not move responsibility to the tool.
- **Don't launder.** Presenting heavy AI output as entirely your own work, where disclosure is expected, is the same integrity problem as presenting a classmate's work as your own.

#### Environmental footprint

Energy figures for AI are often sensational and badly sourced. The best public numbers come from providers measuring their own systems:

- Google measured the **median Gemini Apps text prompt** in May 2025 at **0.24 Wh** of energy, 0.03 g CO₂e, and 0.26 mL of water, about the energy of watching TV for under nine seconds. It reported a 33x drop in energy per median prompt over the previous 12 months ([Elsworth et al., 2025](https://arxiv.org/abs/2508.15734); [Google Cloud blog](https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference)).
- OpenAI's CEO wrote in 2025 that an average ChatGPT query uses about **0.34 Wh** ([blog](https://blog.samaltman.com/the-gentle-singularity)), without published methodology.

Agentic coding is not a median chat prompt. One hour with an agent can be 60 or more model calls, each with a long context and a reasoning model. No provider publishes a per-session figure. To get a feel for scale, an illustrative assumption: if each call used ten times the median prompt's energy (a guess, not a measurement), 60 calls would use about 144 Wh, roughly an hour and a half of a 100-watt appliance. The real number could be lower or higher. Big picture: per-use energy is small and falling; total demand from data centers is large and growing. Reasonable personal practice: don't run agents in loops that produce nothing, prefer smaller models for easy work (it's also cheaper), and be skeptical of numbers without methodology.

#### Bias and accessibility

- Models reflect patterns in their training data: default names, examples, and assumptions about users can skew toward some groups. Review generated user-facing text, test data, and logic that touches people (hiring, lending, grading) with that in mind.
- Generated UIs often miss accessibility: missing labels, poor contrast, mouse-only interactions. Test with an automated checker and a screen reader, and ask the agent to fix specific failures.
- AI tools can also improve access: voice-driven coding for people with repetitive strain injuries, explanations in plain language, help for people working in a second language. Make room for these uses in policies.

#### Human accountability

An agent can't be fired, sued, or held to a professional standard. You can. Whatever you merge, deploy, submit, or publish is yours, including the bugs, the security holes ([module 11](./11-security-and-prompt-injection.md)), and the license problems. "The AI wrote it" is an explanation, never an excuse. Review practices that keep a named human accountable for every change are covered in [module 10](./10-ai-code-review.md).

## Going deeper

### Deskilling: real risk or old panic?

Every abstraction has raised this worry. Calculators, compilers, IDEs, Stack Overflow. Usually the old skill shrank to a niche and a new, higher-level skill took over. Two things make this round different:

- **Breadth.** Earlier tools automated one layer. Agents touch everything from design to debugging, including the skills (reading code, debugging) you need to *supervise* them. The Anthropic trial's largest gap was in debugging.
- **The supervision paradox.** Using agents well requires judgment built by doing the work by hand. If juniors never do the work, where does the judgment come from? Lee et al. found critical thinking shifting toward verification and oversight, which works only if people have enough expertise to verify.

The likely answer is deliberate practice: AI-free reps for fundamentals, AI-as-tutor while learning, and full acceleration once you can check the output. That is how this course is structured.

### The human side

**Intensity and fatigue.** Faster tools don't automatically mean less work. In a February 2026 Harvard Business Review article, Ranganathan and Ye argued from their research that AI tools tend to intensify work rather than reduce it ([HBR](https://hbr.org/2026/02/ai-doesnt-reduce-work-it-intensifies-it)). Running several agents in parallel means constant context switching: each agent finishes, waits for review, needs a decision. Some engineers report finding this more tiring than writing the code themselves. Warning signs: approving diffs you didn't read, losing track of what each agent is doing, no stretch of deep focus in a day. Countermeasures: run only as many agents as you can actually review; batch reviews into blocks; keep some work agent-free.

**Workslop.** Researchers writing in HBR in September 2025 coined "workslop" for AI-generated work that looks finished but lacks substance, so the real work shifts to whoever receives it ([HBR](https://hbr.org/2025/09/ai-generated-workslop-is-destroying-productivity)). In engineering, it looks like a 2,000-line PR nobody can review, or a design doc that sounds right and says nothing. Don't send what you haven't read.

**Imposter feelings.** Some people feel they aren't "real" engineers if an agent wrote the code. Others feel left behind by colleagues who seem to ship ten times as much. Both feelings are common. The work has shifted toward specification, judgment, and verification; doing those well *is* engineering. And remember the METR finding: other people's apparent speed may be partly perception.

**AI-first does not mean AI-only.** Being AI-first means reaching for the tool by default and knowing how to use it well. It doesn't mean never working without it. Keep skills you can use when the tools are down, wrong, or not allowed.

## Bryan's take

> **Bryan's take:** "Vibe coding," as this course uses the phrase, means AI-accelerated engineering with a human in charge, not blind acceptance of whatever the model produces.

The responsible-use material above is what "a human in charge" means in practice: you understand what you ship, you protect other people's data, and you answer for the result. For Yegge's stages, see [module 08](./08-agentic-workflows.md).

## Try it

**Individual: a two-week learning experiment.**
1. Pick a library or language you've never used.
2. Week 1: build a small project with an agent in default mode. At the end, without AI, write down from memory how the core parts work, then rebuild one feature by hand. Note how long it takes and what you couldn't remember.
3. Week 2: build a similar project using the habits above: attempt first, hints only (or Claude Code's Learning style), explain-back, and a "didn't understand" log. Repeat the rebuild test.
4. Compare. Write one page: what did you learn in each week, how fast were you, and which habits will you keep?

**Class or team: write the policy.**
1. In small groups, draft an AI use policy for either this course or your team, using the patterns and template above.
2. Each group must address: when AI is not allowed, how use is disclosed, how understanding is checked, what data may not be pasted, and who is accountable for AI-introduced bugs.
3. Swap drafts with another group and try to find loopholes or unfair outcomes (for example, students without paid tools).
4. Merge into one policy and vote.

## Discussion questions

1. The Anthropic trial found the AI group wasn't significantly faster *and* learned less. Under what conditions would you still choose to use AI while learning something new?
2. Should an introductory programming course ban AI, require it, or teach both? What would you lose with each choice?
3. If companies hire fewer junior engineers because agents do junior work, where will future senior engineers come from? What should companies, universities, and students each do about it?
4. You find that 300 lines of your project closely match GPL-licensed code. You didn't copy it; an agent produced it. What do you do, and who is responsible?
5. Is disclosing AI use in a commit message more like crediting a coworker or like naming your text editor? Does the answer change with how much the AI did?
6. How would you tell, in yourself or a teammate, the difference between healthy AI-first work and "approving diffs nobody read"?

## Sources and further reading

**Papers**
- [How AI Impacts Skill Formation](https://arxiv.org/abs/2601.20245) (Shen, Tamkin, 2026)
- [Generative AI without guardrails can harm learning: Evidence from high school mathematics](https://doi.org/10.1073/pnas.2422633122) (Bastani, Bastani, Sungu, Ge, Kabakcı, Mariman, PNAS, 2025)
- [The Impact of Generative AI on Critical Thinking: Self-Reported Reductions in Cognitive Effort and Confidence Effects From a Survey of Knowledge Workers](https://doi.org/10.1145/3706598.3713778) (Lee, Sarkar, Tankelevitch, Drosos, Rintel, Banks, Wilson, CHI 2025)
- [Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task](https://arxiv.org/abs/2506.08872) (Kosmyna et al., 2025)
- [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://arxiv.org/abs/2507.09089) (Becker, Rush, Barnes, Rein, 2025)
- [Do Users Write More Insecure Code with AI Assistants?](https://arxiv.org/abs/2211.03622) (Perry, Srivastava, Kumar, Boneh, 2022)
- [Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence](https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/) (Brynjolfsson, Chandar, Chen, 2025, revised 2026)
- [Measuring the environmental impact of delivering AI at Google Scale](https://arxiv.org/abs/2508.15734) (Elsworth et al., 2025)

**Primary sources**
- Anthropic, [How AI assistance impacts the formation of coding skills](https://www.anthropic.com/research/AI-assistance-coding-skills) (2026)
- Anthropic, [Updates to our consumer terms](https://www.anthropic.com/news/updates-to-our-consumer-terms) (2025)
- Claude Code docs, [Output styles](https://code.claude.com/docs/en/output-styles) (Learning style)
- U.S. Copyright Office, [Copyright and Artificial Intelligence](https://www.copyright.gov/ai/) report series, especially [Part 2: Copyrightability](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf) (2025)
- Stanford Office of Community Standards, [Generative AI policy guidance](https://communitystandards.stanford.edu/generative-ai-policy-guidance)
- CS50, [Academic honesty](https://cs50.harvard.edu/x/honesty/)
- Gentoo Council, [AI policy](https://wiki.gentoo.org/wiki/Project:Council/AI_policy) (2024)
- U.S. Bureau of Labor Statistics, [Software Developers](https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm)
- Stack Overflow, [2025 Developer Survey: AI](https://survey.stackoverflow.co/2025/ai)
- Google Cloud, [Measuring the environmental impact of AI inference](https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference) (2025)
- Canva Engineering, [Yes, you can use AI in our interviews](https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/) (2025)

**Commentary**
- Sam Altman, [The Gentle Singularity](https://blog.samaltman.com/the-gentle-singularity) (2025), for the 0.34 Wh figure
- Aruna Ranganathan and Xingqi Maggie Ye, [AI Doesn't Reduce Work—It Intensifies It](https://hbr.org/2026/02/ai-doesnt-reduce-work-it-intensifies-it), Harvard Business Review (2026)
- Niederhoffer et al., [AI-Generated "Workslop" Is Destroying Productivity](https://hbr.org/2025/09/ai-generated-workslop-is-destroying-productivity), Harvard Business Review (2025)

## Terms introduced

- **Brooks's law:** Fred Brooks's observation that adding people to a late software project makes it later, because coordination costs grow with team size. It applies to adding agents too.
- **Product sense:** Judgment about what is worth building, for whom, and what "done" means.
- **Skill formation:** Building durable ability through practice, as distinct from completing a task.
- **Cognitive offloading:** Handing mental work to a tool; helpful for routine work, harmful when it skips the thinking you're trying to learn.
- **Cognitive debt:** Kosmyna et al.'s term for reduced engagement and recall that may accumulate when people rely on an LLM to do a task.
- **Explain-back:** Restating something in your own words, without the source in front of you, to test understanding.
- **Learning mode / study mode:** AI tool settings that tutor with hints and questions instead of giving complete answers.
- **AI-free, AI-as-tutor, AI-accelerated:** A three-tier way to label assignments by how much AI help is allowed.
- **AI disclosure:** A statement of which AI tools you used and how, in coursework, commits, or pull requests.
- **Co-author trailer:** A line such as `Co-Authored-By:` at the end of a git commit message that credits another contributor or tool.
- **Copyrightability:** Whether a work can be protected by copyright; in the US, requires sufficient human authorship.
- **License contamination:** Introducing code under incompatible license terms, for example GPL code into a proprietary project, often unknowingly.
- **Early-career "canaries":** Young workers in AI-exposed occupations, whose employment trends may signal AI's labor effects first.
- **Substitution vs complementarity:** Whether AI replaces tasks a worker did or makes the worker more productive at them.
- **Deskilling:** Losing a skill because a tool performs it for you.
- **Workslop:** AI-generated work that looks complete but lacks substance, shifting effort to whoever receives it.
- **AI-first (not AI-only):** Reaching for AI by default while keeping the ability to work without it.
- **Human accountability:** The principle that a named person, not a tool, answers for any change that is shipped.

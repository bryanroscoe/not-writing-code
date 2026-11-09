# 15: Learning, careers, and responsible use

*About a 30-minute read. Last checked November 8, 2026.*

**TL;DR**
- *How* you use AI affects what you learn. In a 2026 randomized trial, developers learning a new library with an AI assistant scored 17 percentage points lower on a follow-up quiz than those who coded by hand. The ones who used the AI to ask conceptual questions and explain code did about as well as the hand-coders. The ones who delegated or relied on AI for debugging scored poorly.
- In some of the studies below, unrestricted answer generation reduced later unaided performance. In some settings, tutoring with hints and explanations avoided that harm or helped. People who trust AI more tend to think less critically about its output.
- Early-career software hiring is under real pressure. Payroll data show employment of 22–25-year-olds in AI-exposed occupations about 19% below where it would be had it kept pace with less-exposed peers (mid-2026 data), mostly through fewer hires. The cause is debated, and overall employment in the field is still projected to grow.
- The skills that gain value are the ones agents can't supply for you: specifying, decomposing, reading and reviewing code, debugging, testing, systems thinking, domain knowledge, and communication.
- Responsible use means not pasting secrets or other people's data into consumer tools, knowing who owns and can copyright what you generate, disclosing AI help where your course or project expects it, and accepting that *you* are accountable for anything you ship.

## Foundations

### Producing the work vs learning from it

At work, the output is the point. A merged pull request that fixes the bug is a success whether you or an agent typed it.

In school, and whenever you're learning something new, the output is mostly a side effect. What matters is the change in your head, like the mental model of how async code works or the instinct for where a bug hides. That change comes from effortful processing: trying, failing, figuring out why, and trying again. If an AI does the effortful part, you get the artifact without the learning.

The same tool that makes an experienced engineer faster can let a learner skip exactly the struggle that would have made them experienced.

### What the evidence says

Research on AI and learning is young, fast-moving, and mostly short-term. Read each study for what it measured, not for its headline.

**Learning a new coding library (Anthropic, 2026).** Shen and Tamkin ran a randomized controlled trial with 52 mostly junior software engineers who used Python weekly but had never used Trio, a library for asynchronous programming ([How AI Impacts Skill Formation](https://arxiv.org/abs/2601.20245), January 2026; [summary](https://www.anthropic.com/research/AI-assistance-coding-skills)). Everyone built two features with Trio, then took a quiz on debugging, reading, writing, and concepts.
- The AI group averaged 50% on the quiz and the hand-coding group 67%, a large, statistically significant gap (about two letter grades).
- The AI group finished about two minutes faster, a difference that was *not* statistically significant.
- The biggest gap was on debugging questions.
- How people used the AI mattered. Participants who asked only conceptual questions, asked for code together with explanations, or generated code and then asked follow-up questions to understand it scored 65% or higher. Those who delegated the task, relied more and more on AI as they went, or had the AI debug for them scored below 40%. These patterns come from small subgroups (2–7 people each), so they're suggestive, not proof.
- The limits are a small sample, a quiz right after the task rather than long-term retention, and a chat-sidebar assistant rather than an autonomous agent. The authors expect agents could widen the gap.

**High-school math (Bastani et al., PNAS 2025).** In a field experiment with roughly a thousand high-school students in Turkey, students got either a plain GPT-4 chat interface ("GPT Base"), a version prompted to act as a tutor that gives hints rather than answers ("GPT Tutor"), or no AI during practice sessions ([Generative AI without guardrails can harm learning](https://doi.org/10.1073/pnas.2422633122), 2025). Both AI groups did much better *during* practice. On a later exam without AI, the GPT Base group did about 17% worse than students who never had AI, while the GPT Tutor group showed no significant harm. Students in the GPT Base group largely used it to get answers.

**Critical thinking at work (Lee et al., CHI 2025).** A Microsoft Research and Carnegie Mellon survey of 319 knowledge workers, covering 936 real examples of using generative AI at work, found that higher confidence in the AI was associated with less critical thinking, while higher confidence in one's *own* ability was associated with more ([The Impact of Generative AI on Critical Thinking](https://doi.org/10.1145/3706598.3713778), 2025). Critical thinking shifted from producing work toward verifying, integrating, and overseeing AI output. This is self-reported survey data, not a measurement of thinking.

**"Your Brain on ChatGPT" (Kosmyna et al., 2025).** An MIT Media Lab study recorded EEG while 54 participants wrote essays with an LLM, with a search engine, or with no tools ([Your Brain on ChatGPT](https://arxiv.org/abs/2506.08872)). The LLM group showed the weakest brain connectivity, felt the least ownership of their essays, and often couldn't accurately quote what they had just written. The authors call the effect "cognitive debt." Read it carefully. It's a preprint with a small sample, and only 18 people completed the key fourth session. The task was essay writing, not programming, and EEG connectivity isn't a direct measure of learning. Media coverage overstated it ("ChatGPT rots your brain"). It cannot settle the question on its own.

**Perceived vs measured speed (METR, 2025).** In a randomized study, 16 experienced open-source developers took 19% longer on tasks in their own repositories when allowed to use early-2025 AI tools, while believing afterward that AI had made them about 20% faster ([Becker et al., 2025](https://arxiv.org/abs/2507.09089)). Tools have improved a lot since. What has held up is that people are poor judges of their own AI-assisted performance.

**Overconfidence in security (Perry et al., 2022).** Participants with an AI assistant wrote less secure code *and* were more likely to believe it was secure ([Do Users Write More Insecure Code with AI Assistants?](https://arxiv.org/abs/2211.03622); [module 11](./11-security-and-prompt-injection.md)).

Taken together, these studies don't show that AI always harms or always helps learning. They suggest that relying on generated answers can reduce later unaided performance, while asking questions and checking understanding can preserve or improve learning in some settings. Feeling productive doesn't show how much you learned.

## In practice

### How to learn with AI instead of outsourcing learning

The studies above motivate these habits, though they don't test every recommendation or time limit here.

1. Attempt it first. Give yourself a fixed time (15–30 minutes) to try on your own before asking, and write down where you got stuck. That effort helps you learn and ask a better question.
2. Ask for hints, not answers. Tell the model what you want from it:

   ```text
   I'm learning Python async with Trio. Don't write the code for me.
   Here's my attempt and the error I get. Ask me one question that
   points me toward the bug, and wait for my answer before saying more.
   ```

3. Ask conceptual questions. "Why does Trio use nurseries instead of free-floating tasks?" teaches more than "write a nursery for me." In the Anthropic trial, people who asked only conceptual questions scored about as well as people who used no AI.
4. Explain it back. After the AI explains something, close the chat and explain it in your own words, out loud or in writing. Then ask the model to check your explanation for mistakes.
5. Read every line it writes. If you can't explain a line, you don't understand the program yet, so ask about that line specifically.
6. Debug it yourself first. Debugging showed the largest gap in the trial, and it's the skill you'll most need for supervising agents later. Read the error, form a hypothesis, and test it. Ask the AI only after you have a hypothesis.
7. Rebuild from scratch. After finishing an AI-assisted exercise, delete it and rebuild the core part without AI the next day. Whatever you can't rebuild tells you what to practice next.
8. Keep a "things I didn't understand" log. Every time you accept something you don't fully understand, write one line. Review the log weekly and close the gaps.
9. Use the learning modes. Claude Code has a built-in Learning output style that explains its choices and leaves small pieces of real design work for you, marked `TODO(human)`, then waits for you to write them ([docs](https://code.claude.com/docs/en/output-styles)). Switch with `/output-style learning`. ChatGPT has a study mode that tutors step by step instead of answering, and other chat apps have similar modes.
10. Turn off autocomplete when you're learning a new language. Inline suggestions are the most frictionless way to skip thinking. Turn them back on once you know the language.
11. Practice without AI sometimes. Do some exercises, timed problems, or a weekly hour of coding with no assistant at all.

Working engineers moving to a new language, framework, or codebase should use these habits too. The Anthropic trial's participants were professionals, not students.

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

AI use is easy and hard to detect reliably, so detection alone is a weak basis for assessment. Instructors have other ways to check understanding:

- Separate learning from producing. Make some assignments explicitly AI-free (fundamentals, timed in-class work) and others AI-encouraged (projects, where judgment is graded).
- Grade understanding, not just artifacts, with short oral explain-backs, code walkthroughs, and live debugging of the student's own submission.
- Grade the process. Ask for the commit history, a short AI-use log, and agent transcripts for key decisions.
- Teach disclosure as a professional norm, not a confession.

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
- A revised version (12 August 2026, data through June 2026) finds employment of 22–25-year-olds in AI-exposed occupations 19% below where it would be had it kept pace with less-exposed peers. The gap has widened since 2025.
- The decline comes mainly from fewer hires of young workers, not from layoffs.
- It's concentrated where AI mainly *substitutes* for tasks. Where AI mainly *complements* workers, employment is flat or rising, especially for experienced workers.
- The authors find no broad, economy-wide job displacement and call their results descriptive rather than causal. They report that the pattern holds when excluding tech firms and when controlling for interest-rate exposure and remote work. A February 2026 update addressed critics who attributed the timing to interest rates.

#### Counter-evidence and uncertainty

- Other explanations remain plausible and may combine: the post-2022 correction after pandemic over-hiring in tech, higher interest rates, offshoring, and companies pausing junior hiring while they figure out AI. The authors' controls address some of these, not all.
- The US Bureau of Labor Statistics still projects software developer employment to grow 10% from 2025 to 2035, much faster than average ([BLS](https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm)). Projections can be wrong in both directions.
- Developers themselves are cautious about the tools. In Stack Overflow's 2025 survey, 84% used or planned to use AI tools, but only 33% trusted their accuracy and 46% distrusted it; the top frustration (66%) was "AI solutions that are almost right, but not quite" ([survey](https://survey.stackoverflow.co/2025/ai)).
- Nobody knows the long-run effect. If companies stop hiring juniors, they eventually run out of seniors. Some firms are betting that AI-fluent juniors are a bargain, and others are cutting junior roles.

Entry-level software work is getting harder to find, and AI is a plausible part of why. Showing judgment beyond generated output is one way applicants can demonstrate their value.

#### Skills that gain value

| Skill | Why it matters more with agents |
| --- | --- |
| **Specification** | Agents do what you ask. Saying precisely what you want, including edge cases and non-goals, is the main lever ([module 07](./07-context-engineering.md)). |
| **Decomposition** | Breaking work into pieces an agent can do and you can verify. |
| **Reading and review** | You will read far more code than you write. Spotting the subtle bug in 400 plausible lines is the job ([module 10](./10-ai-code-review.md)). |
| **Debugging** | When the agent is stuck or confidently wrong, someone has to find the real cause. |
| **Testing and verification** | Tests check specified behavior and help agents catch regressions; passing them does not prove the program is correct. |
| **Systems thinking** | Agents optimize locally. Architecture, data flow, failure modes, and cost are still human calls. |
| **Security judgment** | Knowing what not to give an agent access to ([module 11](./11-security-and-prompt-injection.md)). |
| **Domain knowledge** | The agent doesn't know your users, your regulations, or why the weird business rule exists. |
| **Communication** | Writing clear issues, design docs, and PR descriptions helps humans and agents alike. |
| **Taste** | Knowing which of five working solutions is the one you'll be glad you kept in two years. |
| **Product sense** | As agents take on more of the *how*, more of an engineer's day goes to *what* and *why*: which problem is worth solving, for whom, and what "done" looks like. |

#### The classes you thought you'd never use

When agents write more of the code, the parts of a CS degree that felt least like programming start to matter more.

- Software engineering and project management classes cover estimation, scheduling, dependencies, and risk. Brooks's law, from *The Mythical Man-Month* (1975), says "adding manpower to a late software project makes it later," because coordination costs grow with every person you add. It applies to agents too: Cursor found that twenty agents working on one codebase slowed to the throughput of two or three ([module 09](./09-multi-agent-systems.md)).
- In system design, an agent can implement a design, but choosing the right one, and knowing which questions to ask about scale, failure, data, and cost, is still your job. Good system design chops also make your prompts better, because you know what to ask the agent about.
- An agent can write a heap from memory. You still need algorithms and data structures to recognize when you need one, notice when its solution is accidentally quadratic, and, for now, pass interviews that test this directly.
- Communication and product classes teach clear specs, demos, and understanding what users actually need.

> **Bryan's take:** Ultimately the engineer is much more in product now. Some of the classes software engineers take, the ones they don't think will be useful, turn out to be among the most important. I used Gantt charts and quoted *The Mythical Man-Month* far more in my career than I expected. You still need to know the algorithms to pass the interviews, at least for now. Having good system design chops helps a lot too. You need to know what questions to talk to the agent about.

#### Portfolios in the AI era

A portfolio of ten AI-generated apps proves little, since anyone can make them. Show judgment instead:

- One or two deep projects you've maintained over time, with real users if possible.
- Tests, design notes, and a README that explains the trade-offs you made and the alternatives you rejected.
- An honest account of AI use: where agents helped and where you overrode them. Hiring managers increasingly ask.
- Code review and debugging stories. A write-up of a hard bug you found, including one an AI introduced, is more convincing than a feature list.
- Open-source contributions that follow each project's contribution and AI policy. Some projects ban AI-generated contributions entirely, so read the rules first.

#### Interviewing with and without AI

Companies are split. Some now expect AI use in technical interviews. Canva, for example, announced in June 2025 that backend, ML, and frontend candidates would use tools like Copilot, Cursor, and Claude on harder, more ambiguous problems. It evaluates whether candidates break down requirements, make sound decisions, and catch and fix problems in AI-generated code ([Canva engineering blog](https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/)). Others forbid AI in interviews and use in-person or proctored formats to enforce it.

Prepare for both. Practice solving problems without AI, out loud. Separately, practice driving an agent on an unfamiliar problem while narrating your decisions, especially the moment you reject its suggestion and why.

#### For engineers worried about their jobs

- Get good at the tools. The evidence suggests AI complements experienced workers more than it replaces them, and fluency is becoming a baseline expectation.
- Invest in the skills in the table above and in the domain you work in.
- Measure your own results, not your feelings (METR's developers felt faster while measuring slower). Share what works with your team. Helping colleagues adopt tools well can demonstrate your value, though it's no guarantee of job security.
- Keep your fundamentals sharp. When tools change or fail, people who understand the system underneath are the ones who fix it.

### Responsible use

#### Data privacy: what not to paste

Treat anything you paste into an AI tool as data you are sending to a third party. Don't paste:

- Passwords, API keys, tokens, private keys, connection strings.
- Personal data about other people: customers, patients, classmates, coworkers. Student records and health information often carry legal obligations.
- Your employer's or client's proprietary code or documents, unless they have approved that tool for that use.
- Other students' work.
- Anything you'd be uncomfortable seeing in a breach notification.

Consumer and business products from the same lab often have different data rules:

- Anthropic announced new consumer terms on 28 August 2025, with a deadline a few weeks later for existing users to choose. Free, Pro, and Max users (including Claude Code on those plans) choose whether their chats and coding sessions are used for training. If they allow it, data is retained for up to five years; if not, the existing 30-day retention applies. Team, Enterprise, Education, Government, and API use are excluded ([Anthropic](https://www.anthropic.com/news/updates-to-our-consumer-terms)).
- ChatGPT consumer accounts have a setting to stop your conversations being used to improve models; OpenAI's business and API offerings don't train on customer data by default.
- Team and enterprise plans generally add admin controls, retention settings, and contractual commitments. Some organizations also negotiate zero data retention ([module 12](./12-costs-subscriptions-and-apis.md)).

Check your settings now, and recheck after any terms update. Defaults change.

#### Licensing and copyright of generated code

There are two questions: *can anyone own this code?* and *does this code infringe someone else's?*

On ownership, the US Copyright Office's [report on copyrightability](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf) (Part 2, 29 January 2025) concluded that existing law is adequate: AI-generated output can be protected "in whole or in part" where AI is used as a tool and a human determined the expressive elements, but "prompts alone, however, at this stage are unlikely to satisfy those requirements." Human-authored portions, and human selection, arrangement, and modification of AI output, can be protected. The Office did not recommend new legislation. Part 3, on training models with copyrighted works, was released in pre-publication form on 9 May 2025 ([copyright.gov/ai](https://www.copyright.gov/ai/)). Other countries differ. In practice, copyright protects your sufficiently original human-authored contributions, such as expressive modifications or selection and arrangement. Reviewing or approving generated code doesn't by itself establish authorship, and your employer's or school's IP rules still apply.

On infringement, models sometimes reproduce code from their training data, including code under copyleft licenses such as the GPL, which carry obligations if you distribute it. The risk is highest for long, distinctive snippets. Some assistants offer filters that block or flag suggestions matching public code, and license scanners in CI catch known snippets. And be suspicious of any large, polished block that appears instantly for a niche problem.

Project policies vary too. Some open-source projects ban AI-generated contributions outright. Gentoo did so in April 2024, citing copyright uncertainty, quality, and ethics ([policy](https://wiki.gentoo.org/wiki/Project:Council/AI_policy)). Others allow AI help with disclosure and full contributor accountability. Read `CONTRIBUTING.md` before you open a pull request.

#### Attribution and disclosure in commits and PRs

- Follow the project's rule. Some projects want a trailer such as `Co-Authored-By:` or `Assisted-by:` naming the tool, some want a note in the PR description, and some forbid AI use.
- Many agents add attribution by default. Claude Code, for example, adds a co-author trailer to commits it creates unless configured otherwise. Leave it on unless your project says not to.
- You're still the author of record. Attribution explains the tool's role; you remain responsible.
- Don't launder. Presenting heavy AI output as entirely your own work, where disclosure is expected, is the same integrity problem as presenting a classmate's work as your own.

#### Environmental footprint

Energy figures for AI are often sensational and badly sourced. Provider measurements offer concrete examples, though their scope and methods differ:

- Google measured the median Gemini Apps text prompt in May 2025 at 0.24 Wh of energy, 0.03 g CO₂e, and 0.26 mL of water, about the energy of watching TV for under nine seconds. It reported a 33x drop in energy per median prompt over the previous 12 months ([Elsworth et al., 2025](https://arxiv.org/abs/2508.15734); [Google Cloud blog](https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference)).
- OpenAI's CEO wrote in 2025 that an average ChatGPT query uses about 0.34 Wh ([blog](https://blog.samaltman.com/the-gentle-singularity)), without published methodology.

Agentic coding isn't a median chat prompt. One hour with an agent can be 60 or more model calls, each with a long context and a reasoning model, and no provider publishes a per-session figure. For scale, suppose each call used ten times the median prompt's energy (a guess, not a measurement): 60 calls would use about 144 Wh, roughly an hour and a half of a 100-watt appliance. The real number could be lower or higher, and Google's measured decline for median chat prompts doesn't establish the trend for long-context coding agents. As a reasonable habit, don't run agents in loops that produce nothing, prefer smaller models for easy work (it's also cheaper), and be skeptical of numbers without methodology.

#### Bias and accessibility

- Models reflect patterns in their training data: default names, examples, and assumptions about users can skew toward some groups. Review generated user-facing text, test data, and logic that touches people (hiring, lending, grading) with that in mind.
- Generated UIs often miss accessibility: missing labels, poor contrast, mouse-only interactions. Test with an automated checker and a screen reader, and ask the agent to fix specific failures.
- AI tools can also improve access: voice-driven coding for people with repetitive strain injuries, explanations in plain language, help for people working in a second language. Make room for these uses in policies.

#### Human accountability

An agent can't be fired, sued, or held to a professional standard, but you can. Whatever you merge, deploy, submit, or publish is yours, including the bugs, the security holes ([module 11](./11-security-and-prompt-injection.md)), and the license problems. "The AI wrote it" doesn't excuse those problems. [Module 10](./10-ai-code-review.md) covers review practices that keep a named human accountable for every change.

## Going deeper

### Deskilling: real risk or old panic?

Every abstraction has raised this worry: calculators, compilers, IDEs, Stack Overflow. Usually the old skill shrank to a niche and a new, higher-level skill took over. Two things make this round different.

The first is breadth. Earlier tools automated one layer. Agents touch everything from design to debugging, including the skills (reading code, debugging) you need to *supervise* them, and the Anthropic trial's largest gap was in debugging.

The second is a supervision paradox. Using agents well requires judgment built by doing the work by hand, and if juniors never do the work, it isn't clear where that judgment will come from. Lee et al. found critical thinking shifting toward verification and oversight, which works only if people have enough expertise to verify.

The likely answer is deliberate practice: AI-free reps for fundamentals, AI-as-tutor while learning, and full acceleration once you can check the output. This course is built that way.

### The human side

Faster tools don't automatically mean less work. In a February 2026 Harvard Business Review article, Ranganathan and Ye argued from their research that AI tools tend to intensify work rather than reduce it ([HBR](https://hbr.org/2026/02/ai-doesnt-reduce-work-it-intensifies-it)). Running several agents in parallel means constant context switching, since each agent finishes, waits for review, and needs a decision. Some engineers report finding this more tiring than writing the code themselves. Watch for approving diffs you didn't read, losing track of what each agent is doing, or a day with no stretch of deep focus. Run only as many agents as you can actually review, batch reviews into blocks, and keep some work agent-free.

Researchers writing in HBR in September 2025 coined "workslop" for AI-generated work that looks finished but lacks substance, so the real work shifts to whoever receives it ([HBR](https://hbr.org/2025/09/ai-generated-workslop-is-destroying-productivity)). In engineering, it looks like a 2,000-line PR nobody can review, or a design doc that sounds right and says nothing. Don't send what you haven't read.

Imposter feelings are common too. Some people feel they aren't "real" engineers if an agent wrote the code. Others feel left behind by colleagues who seem to ship ten times as much. The work has shifted toward specification, judgment, and verification, and doing those well *is* engineering. And per the METR finding, other people's apparent speed may be partly perception.

Being AI-first means reaching for the tool by default and knowing how to use it well, while still being able to work without it. Keep skills you can use when the tools are down, wrong, or not allowed.

## Bryan's take

> **Bryan's take:** "Vibe coding," as this course uses the phrase, means AI-accelerated engineering with a human in charge, not blind acceptance of whatever the model produces.

A human in charge must understand what ships, protect other people's data, and answer for the result. Yegge's stages are in [module 08](./08-agentic-workflows.md).

## Try it

**Individual: a two-week learning experiment.**
1. Pick a library or language you've never used.
2. Week 1: build a small project with an agent in default mode. At the end, without AI, write down from memory how the core parts work, then rebuild one feature by hand. Note how long it takes and what you couldn't remember.
3. Week 2: build a similar project with the learning habits from this module (attempt first, hints only or Claude Code's Learning style, explain-back, a "didn't understand" log). Repeat the rebuild test.
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

- **Brooks's law:** Fred Brooks's observation that adding people to a late software project makes it later, because coordination costs grow with team size. Coordination overhead can affect agent teams too.
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

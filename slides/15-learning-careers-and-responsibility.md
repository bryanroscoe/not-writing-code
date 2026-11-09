---
marp: true
theme: not-writing-code
paginate: true
title: "15: Learning, careers, and responsible use"
description: "Learning with AI instead of skipping the learning, what's happening to careers, and what you answer for"
footer: "A Brief Introduction to Not Writing Code · 15 Learning, careers, and responsibility"
---

<!-- _class: lead -->

# 15: Learning, careers, and responsible use

Use AI to learn, not to skip the learning, and own what you ship

<!--
We'll look at learning with AI, habits that help, the early-career job market, and your responsibilities for data, licenses, and what you ship.

This one lands differently for students, working engineers, and instructors. Students, read Foundations, how to learn with AI, academic integrity, and careers. Engineers, the evidence, careers, and the human side. Leads and instructors, academic integrity, responsible use, and Going deeper.

Studies and job data are as of November 2026. The research is young and mostly short-term.
-->

---

# Why this matters

- At work, the output is the point
- When you're learning, the output is a side effect; the struggle teaches
- The tool that speeds experts up lets learners skip the struggle
- Entry-level software hiring is under real pressure
- Whatever you ship is yours, whoever typed it

<!--
A merged pull request that fixes the bug is a success at work whether you or an agent typed it. In school, and whenever you're learning something new, the point is the change in your head: the mental model of how async code works, the instinct for where a bug hides.

That change comes from effortful processing: trying, failing, figuring out why, trying again. If an AI does the effortful part, you get the artifact without the learning.

The same tool that makes an experienced engineer faster can make a learner skip exactly the struggle that would have made them experienced.
-->

---

# Learning a new library with AI (Anthropic, 2026)

52 mostly junior engineers learned Trio, a Python async library, then took a quiz.

| | AI group | Hand-coding group |
| --- | --- | --- |
| Quiz score | **50%** | **67%** |
| Time to finish | About 2 minutes faster (not significant) | Baseline |

The biggest gap was on debugging questions.

<!--
Shen and Tamkin, "How AI Impacts Skill Formation," a randomized controlled trial published January 2026. Participants used Python weekly but had never used Trio. Everyone built two features with Trio, then took a quiz on debugging, reading, writing, and concepts.

The 17-point gap is large and statistically significant, about two letter grades. The AI group's speed advantage wasn't statistically significant.

There are limits to this study: a small sample, a quiz right after the task rather than long-term retention, and a chat-sidebar assistant rather than an autonomous agent. The authors expect agents could widen the gap.
-->

---

# How people used the AI mattered

| Pattern | Quiz score |
| --- | --- |
| Asked only conceptual questions | 65% or higher |
| Asked for code together with explanations | 65% or higher |
| Generated code, then asked follow-ups to understand it | 65% or higher |
| Delegated the task | Below 40% |
| Relied on AI more and more, or let it debug for them | Below 40% |

Each subgroup had 2–7 people. Suggestive, not proof.

<!--
The hand-coding group averaged 67%, so the top three patterns did about as well as people who used no AI at all.

How students used the tool mattered.

Those small subgroups are why the module calls these patterns suggestive. Don't treat them as settled.
-->

---

# The pattern repeats

| Study | Finding | Read it carefully |
| --- | --- | --- |
| High-school math, ~1,000 students (PNAS 2025) | Plain GPT-4: ~17% worse on a later exam. Tutor version: no significant harm | Students mostly used plain GPT-4 for answers |
| 319 knowledge workers (CHI 2025) | More confidence in AI, less critical thinking | Self-reported survey |
| "Your Brain on ChatGPT," 54 people (2025) | Weakest brain connectivity; trouble quoting their own essays | Preprint; 18 finished the key session |
| METR, 16 developers (2025) | 19% slower, but felt 20% faster | Early-2025 tools |

<!--
Bastani et al., PNAS 2025: a field experiment in Turkey. Students got a plain GPT-4 interface ("GPT Base"), a version prompted to act as a tutor that gives hints rather than answers ("GPT Tutor"), or no AI during practice. Both AI groups did much better during practice. On a later exam without AI, GPT Base did about 17% worse than students who never had AI; GPT Tutor showed no significant harm.

Lee et al., CHI 2025 (Microsoft Research and Carnegie Mellon): 936 real examples of using generative AI at work. Higher confidence in the AI was associated with less critical thinking; higher confidence in one's own ability with more. Critical thinking shifted from producing work toward verifying, integrating, and overseeing AI output.

Kosmyna et al., MIT Media Lab, 2025: EEG while people wrote essays with an LLM, a search engine, or no tools. The LLM group showed the weakest connectivity and felt the least ownership. The authors call it "cognitive debt." Caveats: a preprint, a small sample, essay writing rather than programming, and EEG connectivity is not a direct measure of learning. Media coverage overstated it ("ChatGPT rots your brain"). That study alone can't settle the question.

METR, 2025: experienced open-source developers in their own repositories. Tools have improved since. What still holds is that people are poor judges of their own AI-assisted performance.

The module also cites Perry et al., 2022. Participants with an AI assistant wrote less secure code and were more likely to believe it was secure (module 11).
-->

---

# What it adds up to

Outsourcing the thinking hurts the skill you outsourced.

Using AI to think better mostly doesn't, and sometimes helps.

Feeling productive isn't evidence of learning.

<!--
No credible study says "AI use always harms learning" or "always helps."

"Using AI to think better" means asking why, getting hints, and checking your understanding.

Which side of this line does your own AI use usually fall on?
-->

---

# Learn with it; don't outsource to it

- Attempt it alone for 15–30 minutes; note where you got stuck
- Ask for hints and concepts, not finished answers
- Explain it back, then have the model check your explanation
- Read every line; ask about any line you can't explain
- Debug yourself first; form a hypothesis before asking
- Rebuild it the next day without AI

<!--
These habits come straight from the studies. They cost some speed now and pay back later.

If you attempt it first, your question will be better, and the struggle is where the learning happens.

Asking "Why does Trio use nurseries instead of free-floating tasks?" teaches more than "write a nursery for me." In the Anthropic trial, people who asked only conceptual questions scored about as well as people who used no AI.

To explain it back, close the chat and explain it in your own words, out loud or in writing.

Debugging showed the largest gap in the trial, and it's the skill you most need for supervising agents later. Read the error, form a hypothesis, test it.

After you finish an AI-assisted exercise, delete it and rebuild the core part without AI the next day. Whatever you can't rebuild, you didn't learn.
-->

---

# Tell the tool how to help

```text
I'm learning Python async with Trio. Don't write the code for me.
Here's my attempt and the error I get. Ask me one question that
points me toward the bug, and wait for my answer before saying more.
```

- Claude Code: `/output-style learning` leaves `TODO(human)` work for you
- ChatGPT has a study mode; other chat apps have similar modes
- Keep a "things I didn't understand" log; review it weekly
- Turn off autocomplete while you learn a new language

<!--
The prompt is from the module; adapt it to whatever you're learning.

Claude Code's built-in Learning output style explains its choices and leaves small pieces of real design work for you, marked TODO(human), then waits for you to write them. ChatGPT's study mode tutors step by step instead of answering.

For the log, every time you accept something you don't fully understand, write one line, then close the gaps weekly.

Inline autocomplete is the most frictionless way to skip thinking. Turn it back on once you know the language.

Practice without AI sometimes too. Pilots still hand-fly. Do some exercises, timed problems, or a weekly hour of coding with no assistant.

The same habits apply to working engineers moving to a new language, framework, or codebase. The Anthropic trial's participants were professionals, not students.
-->

---

# Academic integrity: common policy patterns

| Pattern | Example | For students |
| --- | --- | --- |
| Default restrictive | Stanford: study aids and surface edits, not deliverables, unless the course says otherwise | Assume no unless told yes |
| Course-provided AI only | CS50: its own AI tutor, the "duck" | Use the tutor the course provides |
| Allowed with disclosure | Many writing and project courses | Use it, say how, own the result |
| Required | Courses like this one | You're graded on judgment |

Check each syllabus. When in doubt, ask the instructor in writing.

<!--
Most universities let the instructor decide per course, with a default for when the instructor says nothing.

Under Stanford's guidance, absent a written course policy, AI may be used to study and prepare (self-quizzing, extra practice problems) and for surface edits like spelling, but not to create deliverables; other uses must be disclosed. CS50: using CS50's own AI tutor is reasonable; using other AI tools that suggest or complete answers or code is not.

For instructors, AI use is easy to do and hard to detect reliably. Policies that depend on catching it tend to fail and to punish students unevenly. Policies that design assessment around it tend to work: separate AI-free work (fundamentals, timed in-class) from AI-encouraged work (projects, where judgment is graded); grade understanding with oral explain-backs, code walkthroughs, and live debugging; grade the process with commit history, a short AI-use log, and agent transcripts; and teach disclosure as a professional norm, not a confession.
-->

---

# A three-tier course policy

| Tier | What's allowed |
| --- | --- |
| AI-free | No AI tools. Tests fundamentals you must have without help |
| AI-as-tutor | AI may explain, hint, and review. It may not write code you submit |
| AI-accelerated | Any AI tools. Graded on the result, your decisions, and explaining every line |

Plus an AI log, ownership of every bug, a 5-minute explain-back, and no pasting others' data.

<!--
This is the module's suggested policy for an AI-accelerated course.

For AI-as-tutor and AI-accelerated work, include a short AI log: which tools, what you used them for, one thing the AI got wrong that you caught, and one thing you learned.

You're responsible for all submitted code, including bugs, security flaws, and license problems introduced by AI.

Any submission may be followed by a 5-minute walkthrough. If you can't explain it, it doesn't count as yours.

And don't paste other students' work, personal data, or credentials into AI tools.

The module also has a fill-in-the-blanks disclosure template for students: which tool, what for, what you reviewed and changed, and one thing the AI got wrong that you caught.
-->

---

<!-- _class: divider -->

# Careers

What the evidence says, and what to get good at

<!--
This part matters to students worried about getting hired and to engineers worried about their jobs. The uncertainty runs in both directions.
-->

---

# Early-career jobs: what the data says

- Stanford Digital Economy Lab, using ADP payroll data on millions of workers
- Ages 22–25 in AI-exposed jobs: **19% below** less-exposed peers' pace
- Data through June 2026; the gap has widened since 2025
- Mostly fewer hires of young workers, not layoffs
- Concentrated where AI substitutes; flat or rising where it complements
- The authors call it descriptive, not causal

<!--
Brynjolfsson, Chandar, and Chen, "Canaries in the Coal Mine?" The first version (August 2025) reported a relative employment decline since late 2022 for workers aged 22–25 in the most AI-exposed occupations, including software developers, while older workers in the same jobs had not declined. The revised version is dated 12 August 2026.

"19% below" means below where employment would be had it kept pace with less-exposed peers.

Where AI mainly complements workers, employment is flat or rising, especially for experienced workers.

The authors find no broad, economy-wide job displacement. They report the pattern holds when excluding tech firms and when controlling for interest-rate exposure and remote work. A February 2026 update addressed critics who attributed the timing to interest rates.
-->

---

# Counter-evidence and uncertainty

- Other causes: post-2022 over-hiring correction, interest rates, offshoring
- BLS still projects 10% growth for developers, 2025 to 2035
- Stack Overflow 2025: 84% use AI tools; only 33% trust them
- Top frustration, at 66%: "almost right, but not quite"
- If companies stop hiring juniors, they eventually run out of seniors

<!--
Other explanations may combine, including companies pausing junior hiring while they figure out AI. The authors' controls address some of these, not all.

The US Bureau of Labor Statistics projects software developer employment to grow 10% from 2025 to 2035, much faster than average. Projections can be wrong in both directions.

Stack Overflow 2025: 84% used or planned to use AI tools; 33% trusted their accuracy and 46% distrusted it. Someone still has to catch the "almost right."

Nobody knows the long-run effect. Some firms are betting AI-fluent juniors are a bargain; others are cutting junior roles.

Entry-level software work is getting harder to find, AI is a plausible part of why, and the people who get hired are the ones who show they can do what the tools can't.
-->

---

# Skills that gain value

| Skill | Why it matters more with agents |
| --- | --- |
| Specification | Agents do what you ask; say precisely what you want |
| Decomposition | Pieces an agent can do and you can verify |
| Reading and review | Spot the subtle bug in 400 plausible lines |
| Debugging | Someone has to find the real cause |
| Systems thinking | Agents optimize locally; architecture stays a human call |
| Product sense | More of your day goes to *what* and *why* |

Also testing, security judgment, domain knowledge, communication, and taste.

<!--
The module covers eleven skills. The others are:

Testing and verification: tests turn "looks right" into "is right," and they're how agents check their own work.
Security judgment: knowing what not to give an agent access to (module 11).
Domain knowledge: the agent doesn't know your users, your regulations, or why the weird business rule exists.
Communication: clear issues, design docs, and PR descriptions help humans and agents alike.
Taste: knowing which of five working solutions is the one you'll be glad you kept in two years.

Specification includes edge cases and non-goals; it's the main lever (module 07). On reading and review, you'll read far more code than you write (module 10). Systems thinking covers architecture, data flow, failure modes, and cost.

As agents take on more of the how, more of an engineer's day goes to what and why: which problem is worth solving, for whom, and what "done" looks like.
-->

---

# The classes you thought you'd never use

| Class | Why it matters more now |
| --- | --- |
| Software engineering and project management | Estimation, scheduling, dependencies, risk |
| System design | Choosing the design; knowing what to ask about scale, failure, cost |
| Algorithms and data structures | Spotting the accidentally quadratic; passing interviews, for now |
| Communication and product | Clear specs, demos, what users actually need |

Brooks's law (1975): "adding manpower to a late software project makes it later." It applies to agents too.

<!--
When agents write more of the code, the parts of a CS degree that felt least like programming start to matter more.

Brooks's law is from Fred Brooks's The Mythical Man-Month. Coordination costs grow with every person you add, and it holds for agents. Cursor found that twenty agents working on one codebase slowed to the throughput of two or three (module 09).

An agent can implement a design. Choosing the right one is still your job, and good system design chops make your prompts better, because you know what to ask the agent about.

An agent can write a heap from memory. You still need to recognize when you need one, notice when its solution is accidentally quadratic, and, for now, pass interviews that test this directly.

Communication and product means writing a clear spec, running a demo, understanding what users need.

If you're a student, remember this slide when a required course feels pointless.
-->

---

<!-- _class: take -->

> **Bryan's take:** Ultimately the engineer is much more in product now. Some of the classes software engineers take, the ones they don't think will be useful, turn out to be among the most important. I used Gantt charts and quoted *The Mythical Man-Month* far more in my career than I expected. You still need to know the algorithms to pass the interviews, at least for now. Having good system design chops helps a lot too. You need to know what questions to talk to the agent about.

<!--
That's from my own career. The skills and classes we just covered include product sense and Brooks's law from The Mythical Man-Month.

That's my view. Use the earlier labor-market evidence to judge the hiring picture.
-->

---

# Portfolios and interviews

- Ten AI-generated apps prove little; show judgment instead
- One or two deep projects, maintained, ideally with real users
- READMEs on trade-offs, hard-bug write-ups, honest AI usage
- Interviews are split: some expect AI (Canva, June 2025), some forbid it
- Practice both: solve without AI out loud, and drive an agent
- Narrate the moment you reject its suggestion, and why

<!--
Anyone can make ten AI-generated apps. Show tests, design notes, and a README that explains trade-offs you made and alternatives you rejected. Say where agents helped and where you overrode them; hiring managers increasingly ask. A write-up of a hard bug you found, including one an AI introduced, is more convincing than a feature list. Open-source contributions count, following each project's contribution and AI policy (module 13).

Canva announced in June 2025 that backend, ML, and frontend candidates would use tools like Copilot, Cursor, and Claude, with harder and more ambiguous problems. It evaluates whether candidates break down requirements, make sound decisions, and catch and fix problems in AI-generated code. Other companies forbid AI in interviews and use in-person or proctored formats.

For engineers worried about their jobs, the module's advice: get good at the tools (the evidence suggests AI complements experienced workers more than it replaces them, and fluency is becoming a baseline expectation); invest in the skills table and your domain; measure your own results, not your feelings; share what works, because champions who help others adopt well become more valuable; and keep fundamentals sharp, because when tools change or fail, people who understand the system underneath fix it.
-->

---

<!-- _class: divider -->

# Responsible use

Data, licenses, and who answers for the result

<!--
This last part applies to everyone, whatever your role.
-->

---

# What not to paste

- Passwords, API keys, tokens, private keys, connection strings
- Personal data about others: customers, patients, classmates, coworkers
- Proprietary code, unless that tool is approved for that use
- Other students' work
- Anything you'd hate to see in a breach notification

Consumer and business terms differ. Check your settings; defaults change.

<!--
Treat anything you paste into an AI tool as data you're sending to a third party. Student records and health information often carry legal obligations.

On terms, as the module describes them, Anthropic changed its consumer terms on 28 August 2025. Free, Pro, and Max users, including Claude Code on those plans, choose whether their chats and coding sessions are used for training. If they allow it, data is retained for up to five years; if not, the existing 30-day retention applies. Team, Enterprise, Education, Government, and API use are excluded.

ChatGPT consumer accounts have a setting to stop conversations being used to improve models; OpenAI's business and API offerings don't train on customer data by default.

Team and enterprise plans generally add admin controls, retention settings, and contractual commitments. Some organizations negotiate zero data retention (module 12).

Check your own settings this week.
-->

---

# Copyright, licenses, and attribution

- US Copyright Office (Jan 2025): "prompts alone" are unlikely to qualify
- Code you shape, review, and modify stands on firmer ground
- Models can reproduce GPL code, with obligations if you distribute it
- Use public-code filters and license scanners in CI
- Follow the project's rule: `Co-Authored-By:`, `Assisted-by:`, or none
- Attribution says how it was made; you're still the author of record

<!--
Two separate questions: can anyone own this code, and does it infringe someone else's?

On ownership, the US Copyright Office's Part 2 report (29 January 2025) concluded existing law is adequate. AI-generated output can be protected "in whole or in part" where AI is used as a tool and a human determined the expressive elements, but "prompts alone, however, at this stage are unlikely to satisfy those requirements." Human-authored portions, and human selection, arrangement, and modification of AI output, can be protected. Part 3, on training with copyrighted works, came out in pre-publication form on 9 May 2025. Other countries differ, and your employer's or school's IP rules still apply.

On infringement, the risk is highest for long, distinctive snippets. Be suspicious of any large, polished block that appears instantly for a niche problem.

Project policies vary: Gentoo banned AI-generated contributions in April 2024; others allow AI help with disclosure. Read CONTRIBUTING.md first.

Many agents add attribution by default; Claude Code adds a co-author trailer to commits it creates unless configured otherwise. Leave it on unless your project says otherwise.

Don't launder. Presenting heavy AI output as entirely your own, where disclosure is expected, is the same integrity problem as presenting a classmate's work as your own.
-->

---

# You answer for what you ship

- An agent can't be fired, sued, or held to a standard. You can.
- "The AI wrote it" is an explanation, never an excuse
- Check people-facing logic for bias, and generated UIs for accessibility
- Run only as many agents as you can actually review
- Don't send what you haven't read; that's "workslop"
- AI-first doesn't mean AI-only; keep skills for when tools fail

<!--
Whatever you merge, deploy, submit, or publish is yours, including the bugs, the security holes (module 11), and the license problems. Module 10 covers review practices that keep a named human accountable for every change.

On bias, models reflect their training data. Default names, examples, and assumptions about users can skew toward some groups. Review user-facing text, test data, and logic that touches people (hiring, lending, grading). On accessibility, generated UIs often miss labels, have poor contrast, or are mouse-only; test with an automated checker and a screen reader. AI can also improve access: voice-driven coding for repetitive strain injuries, plain-language explanations, help working in a second language.

On intensity, a February 2026 Harvard Business Review article by Ranganathan and Ye argued AI tools tend to intensify work rather than reduce it. Parallel agents mean constant context switching. Warning signs: approving diffs you didn't read, losing track of what each agent is doing, no deep focus in a day. Batch reviews into blocks and keep some work agent-free.

Workslop was coined in HBR in September 2025 for AI-generated work that looks finished but lacks substance, shifting the real work to whoever receives it. In engineering: a 2,000-line PR nobody can review, or a design doc that sounds right and says nothing.

On energy, Google measured the median Gemini Apps text prompt in May 2025 at 0.24 Wh. An agent hour can be 60 or more long-context calls, and no provider publishes a per-session figure. Per-use energy is small and falling; total data-center demand is large and growing. Don't run agents in loops that produce nothing, and prefer smaller models for easy work.

Imposter feelings are common either way. Specification, judgment, and verification done well is engineering.
-->

---

<!-- _class: take -->

## What "vibe coding" means here

> **Bryan's take:** "Vibe coding," as this course uses the phrase, means AI-accelerated engineering with a human in charge, not blind acceptance of whatever the model produces.

<!--
Being "a human in charge" means you understand what you ship, you protect other people's data, and you answer for the result. For Yegge's stages of AI-assisted work, see module 08.
-->

---

# Try it

On your own, run a two-week learning experiment:

1. Pick a library or language you've never used
2. Week 1: build with an agent as usual; rebuild one feature by hand
3. Week 2: build again with the habits: attempt first, hints, explain-back
4. Compare in one page: what you learned, how fast, which habits stay

As a class or team, draft an AI use policy, swap drafts, hunt for loopholes, then vote.

<!--
At the end of week 1, without AI, write down from memory how the core parts work, then rebuild one feature by hand. Note how long it takes and what you couldn't remember. In week 2, build a similar project using the habits: attempt first, hints only (or Claude Code's Learning style), explain-back, and a "didn't understand" log. Repeat the rebuild test.

In small groups, draft an AI use policy for the course or the team, using the patterns and the three-tier template. Each draft must address when AI is not allowed, how use is disclosed, how understanding is checked, what data may not be pasted, and who is accountable for AI-introduced bugs. Swap drafts and look for loopholes or unfair outcomes, for example for students without paid tools. Merge into one policy and vote.
-->

---

# Discussion

1. The AI group wasn't faster and learned less. When would you still use it?
2. Should an intro course ban AI, require it, or teach both?
3. If agents do junior work, where will future seniors come from?
4. An agent produced 300 lines that match GPL code. What do you do?

<!--
Fuller versions from the module:

1. The Anthropic trial found the AI group wasn't significantly faster and learned less. Under what conditions would you still choose to use AI while learning something new?
2. Should an introductory programming course ban AI, require it, or teach both? What would you lose with each choice?
3. If companies hire fewer junior engineers because agents do junior work, where will future senior engineers come from? What should companies, universities, and students each do about it?
4. You find that 300 lines of your project closely match GPL-licensed code. You didn't copy it; an agent produced it. What do you do, and who is responsible?

More if time allows: Is disclosing AI use in a commit message more like crediting a coworker or like naming your text editor? How would you tell, in yourself or a teammate, healthy AI-first work from "approving diffs nobody read"?
-->

---

# Read more

- [Module 15: Learning, careers, and responsible use](../modules/15-learning-careers-and-responsibility/)
- [How AI Impacts Skill Formation](https://arxiv.org/abs/2601.20245) (Shen, Tamkin, 2026)
- [Canaries in the Coal Mine?](https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/) (Brynjolfsson, Chandar, Chen, 2025, revised 2026)
- [Generative AI without guardrails can harm learning](https://doi.org/10.1073/pnas.2422633122) (Bastani et al., PNAS, 2025)

<!--
The module also has the full suggested course policy and the student disclosure template, and links the Copyright Office reports and Anthropic's consumer-terms update.
-->

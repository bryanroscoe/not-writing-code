---
marp: true
theme: not-writing-code
paginate: true
title: "07: Context engineering and the buzzwords"
description: "Prompt, context, harness, loop, and graph engineering, and what belongs in the context window"
footer: "A Brief Introduction to Not Writing Code · 07 Context engineering and the buzzwords"
---

<!-- _class: lead -->

# 07: Context engineering and the buzzwords

Prompt → context → harness → loop → graph

<!--
Plan for 40 to 50 minutes in three parts. Part 1 is the buzzword ladder: what each "___ engineering" term means and which ones are mostly new names. Part 2 is what actually fills an agent's context window and why long contexts degrade. Part 3 is the rise and fall of giant CLAUDE.md and AGENTS.md files, the clearest case study of all of it.

The reading is module 07, "From prompt engineering to context, loop, and graph engineering." If you can, have a harness open to show its context breakdown live.
-->

---

## Why this matters

- In agentic work, your typed prompt is a small part of the input.
- What fills the window decides the result, and the bill.
- A new "___ engineering" term arrives every few months.
- The same questions matter after the names change.

<!--
Between 2023 and 2026 the field produced a ladder of buzzwords. Each one widens what you design: the words, then the whole context window, then the agent's environment, then the repetition, then how several agents connect.

Some of it is real and measurable. Some of it is rebranding. Today is about telling them apart, and about the practical habits that hold up either way.
-->

---

<!-- _class: divider -->

# Part 1

## The buzzword ladder

<!--
About 20 minutes. The ladder at a glance, then each rung, then which ones have substance.
-->

---

## The ladder: each rung widens what you design

| Rung | Took off | The question it asks | Substance or relabel? |
| --- | --- | --- | --- |
| Prompt engineering | 2020–2023 | What words do I send? | Substance; now one piece of a whole |
| Context engineering | Jun 2025 | What's in the window at each step? | Mostly substance |
| Harness engineering | Feb 2026 | What does the environment prevent, check, correct? | Substance; developer-experience and CI work underneath |
| Loop engineering | Jun 2026 | What prompts the agent, and when does it stop? | Partly; also cron plus a while-loop |
| Graph engineering | Jul 2026 | How do many agents and steps connect? | Mostly relabel |

<!--
Each rung asks a broader question than the one before.

Who popularized each:
Prompt engineering: practitioners after GPT-3's few-shot results (Brown et al., 2020) and chain-of-thought prompting (Wei et al., 2022).
Context engineering: Shopify CEO Tobi Lütke, June 19, 2025; Andrej Karpathy, June 25; then LangChain (July) and Anthropic (September).
Harness engineering: Mitchell Hashimoto, February 5, 2026; OpenAI's Codex team, February 11.
Loop engineering: precursor Geoffrey Huntley's "Ralph" loop, July 2025; popularized by Addy Osmani's essay, June 7, 2026, quoting Peter Steinberger.
Graph engineering: a Steinberger post on X, July 18, 2026, and the discourse after it; an academic survey followed in August.

Spec-driven development runs alongside the ladder (AWS Kiro, July 2025; GitHub Spec Kit, September 2025). You write a spec, plan and task list first, then agents implement against them. It suits medium-to-large features with clear acceptance criteria and is overhead for a one-line fix. The usual failure is spec drift.
-->

---

## Prompting basics still matter

```text
fix the login bug
```

```text
Users whose email contains "+" can't log in (issue #482).
First reproduce it with a failing test in tests/auth/test_login.py.
Then fix the root cause. Don't change the public API of
auth/session.py. Done means: the new test passes, `make test`
passes, and you explain the root cause in two sentences.
If you can't reproduce it, stop and tell me.
```

The second has an outcome, a reason, a definition of done, and a check.

<!--
Anthropic's and OpenAI's prompting guides agree on a short list that survives model upgrades:
1. Be specific about the outcome: files, behavior, constraints.
2. Give the reason. The model makes better trade-offs when it knows why.
3. Define done, and give a check. A check the agent can run is worth more than any adjective.
4. Show, don't describe. One example of the output format beats a paragraph about it.
5. Structure long inputs with headings or XML-style tags.
6. Say what to do, not only what not to do.
7. Treat prompts as code: version them and change one thing at a time.

Claude Code's best-practices page lists what to stop doing. ALL CAPS and "IMPORTANT" "mostly makes Claude over-apply the rule." "Think harder" is ordinary text, not a control; use the harness's effort setting. And "loop until done, don't be lazy" is "more likely to cause over-work than fix a stall."

Prompting matters less than it used to because models got better at inferring intent, reasoning models think before answering without being asked, and in agentic work the typed prompt became a small fraction of what the model sees.
-->

---

## Context engineering vs harness engineering

| | Context engineering | Harness engineering |
| --- | --- | --- |
| Named by | Tobi Lütke, Jun 19, 2025 | Mitchell Hashimoto, Feb 5, 2026 |
| Asks | What should the agent see? | What should the environment prevent, measure, correct? |
| In their words | "the art of providing all the context for the task to be plausibly solvable by the LLM" | "anytime you find an agent makes a mistake, you take the time to engineer a solution" |
| Looks like | Choosing instructions, tools, files, history, memory | Docs, linters, tests, hooks, helper scripts |

<!--
Context engineering. Six days after Lütke, Andrej Karpathy added "+1," calling it "the delicate art and science of filling the context window with just the right information for the next step." Simon Willison predicted the term would stick, and it did. Anthropic (September 29, 2025) called context "a finite resource with diminishing marginal returns," with the goal of "the smallest possible set of high-signal tokens."

Harness engineering. Hashimoto, co-founder of HashiCorp and author of the Ghostty terminal, described it as step 5 of his adoption path. Sometimes the fix is a line in AGENTS.md; he writes that "each line in that file is based on a bad agent behavior." Sometimes it's a script, such as a screenshot tool or a filtered test runner.

Six days later OpenAI's "Harness engineering" post (Ryan Lopopolo, February 11, 2026) reported three engineers driving Codex, later seven, and about a million lines across code, infrastructure, tooling and documentation after five months, with no hand-written code. One large instruction file didn't work. They replaced it with a roughly 100-line AGENTS.md that acts as a map into a docs/ directory, with linters and structural tests keeping docs and architecture consistent. Module 06 covers the harness itself.
-->

---

## Loop engineering replaces typing "continue"

```bash
while :; do cat PROMPT.md | claude-code ; done
```

Geoffrey Huntley's "Ralph" loop (July 2025): a fresh context each pass, a plan file as memory.

> "You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents."
> Peter Steinberger, quoted by Addy Osmani, June 2026

Osmani warns that "done" from a loop is "a claim and not a proof."

<!--
The one-liner is how Huntley's post writes it; the actual Claude Code binary is claude. The prompt tells the agent to read a plan file, do the single most important remaining item, update the plan, and exit. The next pass starts with a fresh context window. Huntley was blunt about the limits: one thing per loop, expect broken builds, use it for greenfield projects ("There's no way in heck would I use Ralph in an existing code base"), and keep senior engineers steering.

Osmani's essay doesn't say who coined "loop engineering." It also quotes Boris Cherny, who leads Claude Code at Anthropic: "I don't prompt Claude anymore. I have loops running that prompt Claude and figuring out what to do." Osmani lists the parts: scheduled automations, worktrees, skills, plugins and connectors, verifier subagents, and state that lives outside the conversation. He warns that loops invite "cognitive surrender."

Harnesses shipped features for this: Claude Code's /loop (re-run on an interval) and /goal (keep going until a condition holds, judged after every turn by a separate small model), plus cloud scheduled tasks. The Codex app has Automations and a /goal command.
-->

---

## A loop worth building has a checkable end state

```text
read state → do one item → verify: tests, linter, another model
   fail → do the item again
   pass → update state, commit → goal or budget reached?
            no  → read the state again
            yes → stop and report to a human
```

- An independent check, because a model grading its own work is optimistic.
- A budget of turns, wall-clock time, or tokens.
- A human reads the diff. "Done" is a claim.

<!--
This redraws the module's loop diagram. Here's the full checklist for any loop.
1. A verifiable end state. "All tests in test/auth pass" works; "the code is good" doesn't. Claude Code's /goal evaluator can't run commands itself; it judges from what the agent printed, so the agent must show the evidence.
2. An independent check: tests, a type checker, or a model that didn't write the code.
3. A budget. Claude Code suggests adding "or stop after 20 turns" to a goal, and its session loops expire after seven days.
4. State outside the conversation: a plan file, a checklist, or issues.
5. Isolation in a worktree or sandbox, so a bad pass can't damage your main checkout.
6. Escalation when stuck, or before anything irreversible: pushing, deleting, spending money.
7. A human reads the output before it ships (module 10).

From simplest up, the loop patterns are a Ralph loop; an interval loop such as "/loop 5m check the deploy"; a goal loop such as "/goal all tests in test/auth pass and lint is clean"; a Stop hook that blocks finishing until a check passes; and scheduled cloud tasks for nightly triage.
-->

---

## Graph engineering is an old idea with a new name

July 18, 2026 (UTC), [Steinberger on X](https://x.com/steipete/status/2078277297791189132): "Are we still talking loops or did we shift to graphs yet?"

The shapes, as Anthropic described them in December 2024:

| Pattern | Coding example |
| --- | --- |
| Prompt chaining | Plan → implement → write tests → summarize |
| Routing | Triage issues to bug, docs, or feature handlers |
| Parallelization | Three reviewers on one pull request |
| Orchestrator-workers | A lead splits a migration across worktrees |
| Evaluator-optimizer | Generate, critique, revise until tests pass |

<!--
Within hours of Steinberger's post, [Hamel Husain posted an X article](https://x.com/HamelHusain/status/2078346425621237935) titled "Loop Engineering Is Dead. Enter Graph Engineering." These posts helped popularize the label; they don't establish who first coined it. Turing Post reports that courses and roadmaps appeared within days. Turing Post traced the origin, treated Steinberger's post as a playful question rather than a definition, and found false a viral claim that Microsoft, Stanford and Anthropic had "discovered" graph engineering.

The idea underneath is real and older than the name. A graph is a set of steps (nodes) joined by transitions (edges) with shared state; a loop is a graph whose path returns to an earlier node. Anthropic's "Building effective agents" (Erik Schluntz and Barry Zhang, December 19, 2024) separated workflows, "systems where LLMs and tools are orchestrated through predefined code paths," from agents that direct their own process. LangGraph (2024) made these graphs explicit in code, with checkpoints and human-approval nodes. In August 2026 a 35-author survey (Feng et al.) placed graph engineering after the other four rungs.

Most coding work needs one or two of these patterns at most. Anthropic's 2024 advice still applies: find "the simplest solution possible," because each extra node is another place for errors to compound and more tokens to pay for. Module 09 covers multi-agent research.
-->

---

## Substance or relabel?

- You're designing systems around a component whose output varies.
- "X is dead" is always wrong. Graphs contain loops.
- Measured claims have held up. Viral ones mostly haven't.
- New names often mark new product features.
- Expect another name within months for these same questions.

<!--
Each rung names one part of the same system: the input (prompt), the working memory (context), the environment (harness), the control flow (loop), and the topology (graph).

On "X is dead," prompts still matter inside context, and context still matters inside a loop.

Context degradation, the value of verifiers, and harness effects all have measurements behind them. The viral claim that graph engineering had "replaced RAG" (retrieval-augmented generation, which fetches documents into the prompt) had none.

Loop engineering arrived as harnesses shipped /loop, /goal and automations. A name gives vendors and educators something to sell. That doesn't make it wrong; it means you should ask what changed in practice.

Discussion question 1 asks the room to rank the rungs with evidence.
-->

---

<!-- _class: divider -->

# Part 2

## What the model actually sees

<!--
About 10 minutes on what fills a coding agent's window, what research says about long contexts, and four ways to manage it.
-->

---

## Your prompt is often the smallest part

| Component | Typical size | Loaded |
| --- | --- | --- |
| Harness system prompt | Thousands of tokens | Every call |
| Tool definitions, built-in and MCP | A few thousand to 50K+ tokens | Every call, unless loaded lazily |
| Instruction files | Tens to thousands of lines | Session start, or per directory |
| Skill descriptions | One line each | Every call; the body only when used |
| Your messages | Small | As you type |
| Tool results: files, tests, searches | Often the largest share | As the agent works |

Check `/context` in Claude Code, or your harness's equivalent.

<!--
Compacted summaries of earlier work also show up after compaction.

Most people are surprised by how much space goes to tool definitions and instruction files before they type anything. If you have a harness open, show the breakdown now.

The module compares your context window to a desk. Every document on the desk competes for attention. A cluttered desk slows you down even when the right paper is somewhere in the pile.
-->

---

## Bigger windows, same attention

| Study | Finding |
| --- | --- |
| Lost in the Middle, 2023 | Best when key facts sit at the start or end; worst in the middle |
| RULER, 2024 | Of 17 models claiming 32K+ contexts, only half held up at 32K |
| NoLiMa, 2025 | Without shared keywords, 11 of 13 models fell below half their short-context score at 32K |
| Context Rot (Chroma), Jul 2025 | Across 18 models, scores fell as input grew, even on simple tasks |

By 2026 the limit is attention and cost, more than capacity.

<!--
Lost in the Middle (Liu et al., 2023) found a U-shaped curve. The popular needle-in-a-haystack test (Kamradt, 2023) hides one fact in filler; frontier models now score near-perfectly on it, which says little about real use. RULER (Hsieh et al., 2024) used harder variants such as multiple needles, multi-hop tracing and aggregation; that's why only half held up despite near-perfect plain needle scores. Context Rot also found topically similar distractors hurt more, and, oddly, that models did better on shuffled haystacks than coherent ones.

At a high level, attention spreads a fixed budget of focus across every token. More tokens, especially plausible but irrelevant ones, mean each relevant token gets a smaller share.

What changed in 2026 is that with million-token windows and automatic compaction, running out of space is rare. Claude Code's docs now list "manage the context window aggressively" as outdated advice, while still recommending /clear between tasks "because a focused context gets you better answers and costs less." You also pay for every token on every call. Prompt caching cuts the price but not the distraction (module 12).
-->

---

## Write, select, compress, isolate

| Move | Means | Examples |
| --- | --- | --- |
| Write | Save it outside the window | Plans and progress files; issues; memory; commits |
| Select | Bring in only what's relevant | `grep` on demand; skills; path-scoped rules; tool search |
| Compress | Keep only the tokens you need | Compaction; trimmed tool output; `jq` and `head` |
| Isolate | Separate work, separate windows | Subagents; a session per task; a fresh reviewer |

The two common mistakes are preloading "just in case" and running one marathon session.

<!--
The four buckets come from LangChain's "Context Engineering for Agents" (July 2025).

Claude Code's auto memory loads the first 200 lines or 25KB of its MEMORY.md. Code mode, from module 06, is a compress technique for tool results. Isolate also covers parallel agents in worktrees, and a reviewer that didn't watch the code being written.

Preloading means pasting the whole architecture doc, or connecting every MCP server you might need. The agent can search when it needs something. In a marathon session, twenty tasks in one conversation leave stale, contradictory context behind. Start fresh between unrelated tasks, and keep state in files.
-->

---

<!-- _class: divider -->

# Part 3

## The rise and fall of giant CLAUDE.md files

<!--
About 10 minutes on how files grew to a thousand lines and what works now. The cycle took about two years.
-->

---

## One file, loaded every time (2023–2025)

| When | What happened |
| --- | --- |
| 2023–2024 | `.cursorrules`: one rules file added to every Cursor request |
| Meanwhile | Every tool wants its own file; teams keep near-duplicates |
| Feb 2025 | `CLAUDE.md` loads into every Claude Code session; `/init` writes one |
| Apr 2025 | Official advice: add "IMPORTANT" or "YOU MUST" to improve adherence |
| Aug 2025 | `AGENTS.md`: one vendor-neutral name; the nearest file wins |

<!--
awesome-cursorrules gathered rule files for every framework and has about 41,000 GitHub stars (as of November 2026). Cursor later moved to scoped Project Rules in .cursor/rules/.

On duplicates, Aider used a conventions file, GitHub Copilot read .github/copilot-instructions.md, Windsurf had its own rules file, and Gemini CLI read GEMINI.md. Teams using several tools ended up with near-duplicates or a tangle of symlinks.

The April 2025 advice came from Anthropic's best-practices post, which said to tune the file like any frequently used prompt. Its current docs call the emphasis advice outdated.

AGENTS.md was agreed by OpenAI (Codex), Sourcegraph (Amp), Google (Jules), Cursor and Factory. It's plain markdown with no required schema. It reports use in more than 60,000 open-source projects, became a founding project of the Agentic AI Foundation in December 2025, and Claude Code now reads it natively when no CLAUDE.md is present.
-->

---

## The thousand-line file (2025)

```markdown
# CLAUDE.md: READ THIS ENTIRE FILE BEFORE DOING ANYTHING!!!

You are a world-class principal engineer with 30 years of experience

## CRITICAL RULES (NEVER BREAK THESE!!!)
2. NEVER introduce bugs.
31. IMPORTANT: Use 2-space indentation.  <- the formatter does this
32. Use 4-space indentation in all files. <- contradicts rule 31

## Tech stack
- React 17                                <- the repo is on React 19
```

Each line felt free when added. Nobody deleted anything.

<!--
This is an excerpt of the module's bloated example; real ones ran to hundreds of lines. Ask the room to find every problem: persona fluff, generic virtues, emphasis inflation, a rule a tool already enforces, a contradiction, and a stale fact. The full version also has a 300-line annotated directory tree and a 400-line style guide pasted from a wiki.

A typical 2025 file grew to hold all that, plus lessons from old incidents that no longer applied.

Studies of real files confirm the pattern. An analysis of 253 CLAUDE.md files found them dominated by operational commands, implementation notes and architecture overviews (Chatlatanagulchai et al., 2025). A larger study of 2,303 context files from 1,925 repositories found they "evolve like configuration code through frequent, small additions," are often hard to read, and rarely cover security (14.8%) or performance (14.5%).
-->

---

## The fall (late 2025–2026)

- Every line costs attention, on every task.
- More instructions, worse following; the best models hit 68% at 500.
- ETH Zurich (2026) found no significant gain in success, costs up about 20%.
- Skills and path-scoped rules load only when needed.
- Hooks replaced shouting in capital letters.
- Vendors set budgets, like "target under 200 lines per CLAUDE.md file."

<!--
1. Claude Code's docs: every line "takes a little of Claude's attention on every task," and longer files "consume more context and reduce adherence."

2. IFScale ("How Many Instructions Can LLMs Follow at Once?", Jaroslawicz et al., July 2025) added up to 500 simple instructions to one task. Across 20 models, accuracy fell as the count rose, with a bias toward earlier instructions. A rules file with 150 bullet points is exactly this situation.

3. "Evaluating AGENTS.md" (Gloaguen et al., ETH Zurich and LogicStar.ai, first posted February 2026, revised through September) ran Claude Code, Codex and Qwen Code on SWE-bench Lite and 138 tasks from 12 repositories. LLM-generated files changed success by about −0.5% and −2%, not significant, and raised cost about 20 to 23%. Developer-written files gained about 2.4%, also not significant, and cost up to 19% more. Agents did follow the files: when one mentioned uv, agents used it about 1.6 times per task, versus almost never otherwise. But directory overviews didn't help them find files faster. The authors advise omitting LLM-generated files for now, keeping human-written ones minimal, and testing any context file. Earlier versions had somewhat different numbers; the direction held.

4. Agent Skills (October 2025), .claude/rules/ with path patterns, Cursor's scoped rules, nested AGENTS.md files.

5. Claude Code's docs: "If you keep adding emphasis to a CLAUDE.md line and Claude still misses it, that's a sign the line belongs in a hook."

6. Cursor says keep rules under 500 lines; OpenAI's harness team used about 100 lines as a map. One thing not on the slide: models got better at exploring codebases. Claude Code now lists describing your architecture under "what you can stop doing": "Claude reads the repo itself. Only write down what isn't in there."
-->

---

## Ask one question of every line

"Could the agent figure this out by reading the repository?" If yes, delete it.

| Kind of instruction | Where it belongs |
| --- | --- |
| Must always happen | A hook |
| Must never happen | A deny rule, hook, or sandbox |
| Style a tool can enforce | Formatter and linter config |
| A procedure needed sometimes | A skill |
| Applies to one part of the repo | A path-scoped rule or nested `AGENTS.md` |
| Your personal preference | Your user-level file, or a gitignored local one |

Keep commands, traps in the code, and unwritten decisions, well under 200 lines.

<!--
What remains usually fits on one screen: the exact commands to install, test (including a single test file), lint and typecheck; places where the code misleads, such as a legacy pattern that's everywhere but must not be copied, or a directory that looks dead but isn't; decisions that aren't in the code, such as which helper the team chose or how deploys work; anything you've had to correct twice; and pointers to deeper docs and skills rather than their contents.

The module includes a good file of about 25 lines: commands, "things the code won't tell you" (money is integer cents; app/legacy/ is frozen; how migrations are created; integration tests need Docker), where to look, and what done means.

On the other side, Agentic Context Engineering (Zhang et al., October 2025) treats contexts as evolving playbooks and reported about 10% benchmark gains. The views fit once you separate always-loaded context, which should be small and index-like, from retrievable knowledge, which can be large if the agent fetches it only when relevant. Anthropic's November 2026 memory post describes that layering.

One more caution. Instruction files and skills are loaded as trusted context, so a malicious edit to AGENTS.md is a prompt-injection channel. Review changes to them like CI configuration (module 11).
-->

---

<!-- _class: take -->

## Bryan's take

> **Bryan's take:** Big `CLAUDE.md` and `AGENTS.md` files were popular, and now they're not.

<!--
That's my view of the shift in Part 3. The evidence needs care, though. The ETH study found developer-written files helped a little, about 2.4%, though not significantly, and recommended keeping human-written files minimal rather than dropping them. Short files with non-standard information are what survived.
-->

---

<!-- _class: take -->

## Bryan's take

> **Bryan's take:** I like loop engineering and setting goals, but the goals can't be too ambitious or the agent goes off the rails. Loops with a hard, checkable goal and a human in the loop reading the result work for me. Open-ended loops that run unattended and ship to production don't, yet. (My broader skepticism about fully autonomous workflows is in [module 08](../modules/08-agentic-workflows/#bryans-take).)

<!--
There's evidence against my view. OpenAI's harness team reports building a million-line product without hand-written code, with most review handled agent-to-agent. Cursor reports a week-long multi-agent run that built a working web browser. Boris Cherny and Peter Steinberger describe loop-first daily workflows. These are real results from strong teams. They also come with heavy investment in harnesses, tests and verification, and from the companies selling the tools.

Connect it to the loop checklist: a checkable end state, an independent verifier, a budget, and a human reading the diff. Module 08 discusses how much autonomy works in practice.
-->

---

<!-- _class: take -->

## Bryan's take

> **Bryan's take:** Context management is important. Once context gets stale, that's bad. Don't keep the same thread around for a long time. Models get dumber the larger the context gets and the longer a session has been going. Start fresh sessions often.

<!--
The research we covered in Part 2 supports this. Lost in the Middle, RULER, NoLiMa and Context Rot all found performance falling as input grows. Long sessions accumulate exactly that, plus the stale and contradictory context from the marathon-session mistake. Claude Code's own docs still recommend /clear between tasks. Keep state in files. Use a session per task, and hand noisy work to subagents.
-->

---

## Try it

**Individual (60–90 minutes)**
- Take a repo's `CLAUDE.md` or `AGENTS.md`; count its lines and tokens.
- Sort every line into the "where it belongs" table, then trim.
- Run three tasks with each version in fresh sessions; compare.

**Class or team (one session)**
- Break 10 tests in a toy project.
- Groups build a Ralph loop, a `/goal`, and a Stop hook.
- Compare: did it finish, at what cost, and did any weaken a test?

<!--
For the individual version, if the repo has no instruction file, have an agent generate one with /init or the equivalent. Count tokens with the harness's context view. Delete what's discoverable, move enforceable rules to hooks or linter config, and move procedures into a skill. Run each of three small tasks twice, once with the original file and once with the trimmed one, and record success, number of steps, and tokens used. Finish with a half-page note: did the trimmed file do as well, and what did you learn that the ETH study did or didn't predict?

In the class version, the instructor breaks the tests on purpose. Give each loop a turn or time budget. Check the diffs to see whether any loop "passed" by weakening a test, then discuss which verifier you'd trust in a real codebase.
-->

---

## Discussion

1. Which rung adds the most substance? Which is mostly a new name? Show evidence.
2. Hand-written context files helped a little; generated ones didn't; both cost more. Team policy?
3. A loop says "done." What would let you merge its pull request unread?
4. As models improve, which parts of context engineering disappear, and which remain?

<!--
For 1, point to the "substance or relabel" column and the "Substance or relabel?" slide. Context rot, harness effects and verifiers have measurements behind them; graph engineering mostly renames 2024 workflow patterns.

For 2, the ETH authors' own advice is a starting point: no LLM-generated files for now, minimal human-written ones, and test any file before relying on it.

For 3, tie back to the loop checklist and module 10. "Done" from a loop is a claim, not a proof.

For 4, the module's view is that emphasis tricks, architecture overviews and "think harder" phrases have already stopped helping. What remains is information the model can't get any other way, such as a decision your team made in a meeting or which legacy directory is a trap.
-->

---

## Read more

- Module: [07 From prompt engineering to context, loop, and graph engineering](../modules/07-context-engineering/)
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (Anthropic, September 2025)
- [Evaluating AGENTS.md](https://arxiv.org/abs/2602.11988) (Gloaguen et al., 2026)
- [Context Rot](https://www.trychroma.com/research/context-rot) (Chroma, July 2025)

<!--
The module has the full good and bloated instruction-file examples, the loop patterns table, and the graph patterns table with "use when" and "skip when" columns. Anthropic's post is the clearest single statement of context engineering. The ETH paper is the main evidence on instruction files. Context Rot is a readable study of long-context degradation.

Next session, module 08, covers day-to-day agentic workflows and how much autonomy actually works.
-->

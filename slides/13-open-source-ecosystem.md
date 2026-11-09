---
marp: true
theme: not-writing-code
paginate: true
title: "13: The open-source ecosystem"
description: "Harnesses, runtimes, frameworks, extensions, and the maintainers behind them"
footer: "A Brief Introduction to Not Writing Code · 13 Open-source ecosystem"
---

<!-- _class: lead -->

# 13: The open-source ecosystem

The tools under your tools, and the people who maintain them

<!--
We'll place AI tools in the stack, pick an open-source harness to try, explain what OpenClaw taught about personal agents, and contribute to someone else's project with AI without burdening its maintainers.

Project statuses and star counts are as of November 2026, and this part of the field churns fast.

The reading is module 13. Students, read Foundations, the harness table, and the section on contributing responsibly. Engineers, all of In practice. Leads, the stack map, churn and capture, and the AI-contribution policies.
-->

---

# Why this matters

- You can read the prompts and tool code your agent runs
- Open projects are where harness ideas show up first
- Tools churn; several were archived or shut down in 2026
- AI made pull requests cheap and maintainers' review expensive

<!--
You can read the prompts and tool definitions. The best way to understand what a harness does is to read its system prompt and tool code.

You can run it where your code lives, including air-gapped or on-premises environments with local models.

Aider's repository map, the Ralph loop, worktree-per-agent orchestration, and git-backed agent memory appeared in open projects first and were copied everywhere within months.

It protects against vendor churn, up to a point. An archived open-source tool still runs; a shut-down service doesn't.

Then there's the cost. Maintainers now read a flood of AI-generated pull requests and bug reports. The second half of today is about that.
-->

---

# Open-source software ≠ open-weight model

Open source publishes the **code**. Open weight publishes the **model**. They're independent.

| License | What it allows | Seen on |
| --- | --- | --- |
| MIT | Almost anything, with attribution | OpenCode, Kilo Code, OpenHands, T3 Code |
| Apache-2.0 | The same, plus an explicit patent grant | Codex CLI, Gemini CLI, Aider, Cline, goose |
| FSL-1.1-MIT | Source-available: no competing product; MIT after two years | Crush |

<!--
Some examples. Codex CLI is open-source software that by default calls OpenAI's closed models. OpenCode or Aider can drive a closed frontier model or a local open-weight model. A closed IDE can run an open-weight model. Module 04 covers open-weight models; this session is about the software.

MIT is also the license on Gas Town, Beads, and Inspect.

FSL is the Functional Source License: you can use and modify it, but not build a competing commercial product, and each release converts to MIT after two years. That makes it source-available, not open source.

Some projects mix licenses. Cline's JetBrains plugin isn't open source even though its VS Code extension is. Read the license file, not the marketing page.
-->

---

# A map of the stack

| Layer | Examples |
| --- | --- |
| Orchestrators and GUIs | Gas Town · Beads · OpenHands Agent Canvas · T3 Code |
| Harnesses, plus extensions | OpenCode · Aider · Cline · goose · Codex CLI · MCP servers · skills |
| Frameworks and SDKs | LangGraph · Pydantic AI · DSPy · OpenAI Agents SDK · Claude Agent SDK |
| Inference runtimes | llama.cpp · Ollama · vLLM · SGLang · MLX |
| Models | Open-weight or API (modules 03–04) |

Evaluation tools (SWE-bench harness, Inspect, promptfoo) measure harnesses and models.

<!--
Read it bottom up: models run on inference runtimes; frameworks and SDKs build on those; harnesses build on frameworks; orchestrators and GUIs drive harnesses. Extensions (MCP servers, Agent Skills, plugins) plug into harnesses. Evaluation tools sit to the side and measure both harnesses and models.

You don't need every layer. A typical engineer uses one harness, a few MCP servers and skills, and an API or subscription model. Someone running models locally adds a runtime. Someone building a product adds a framework or SDK and an eval tool.

Which layers are you using today?
-->

---

<!-- _class: divider -->

# The tools

Harnesses, runtimes, frameworks, and extensions

<!--
We'll spend time on two or three projects you've heard of, rather than read every row.
-->

---

# Open-source coding harnesses (as of November 2026)

| Project | Form | Worth knowing |
| --- | --- | --- |
| OpenCode | Terminal UI | Works with any model; about 225K GitHub stars |
| Codex CLI | CLI, IDE extension | OpenAI's open client for its closed models |
| Aider | CLI | Pioneered the repository map (2023) |
| Cline · Kilo Code | VS Code extensions and more | Approve each diff; many providers |
| goose | Desktop app, CLI | General-purpose agent built around MCP |
| OpenHands · T3 Code | GUIs | Run and supervise several agents |

Stars measure attention, not quality.

<!--
More from the module's table:

OpenCode is maintained by the anomalyco org (the SST team), MIT-licensed, with a desktop app in beta. Kilo Code's CLI is a fork of it.

Codex CLI is written mostly in Rust and runs the same agent as the Codex app.

Gemini CLI, Google's open-source CLI, has been aimed at enterprise Gemini Code Assist since June 18, 2026; individual users were moved to Antigravity CLI.

Aider, by Paul Gauthier and contributors, was one of the first terminal pair-programmers and pioneered a git commit per change.

Cline began in 2024 as "Claude Dev." Kilo Code started in the Cline and Roo Code family and adds no markup on provider prices.

goose comes from Block and is now part of the Agentic AI Foundation, a founding project. It's a local agent for more than code.

OpenHands, formerly OpenDevin, now also works as a control center that can run Claude Code, Codex, Gemini CLI, and OpenCode. T3 Code, from Ping (Theo Browne), isn't an agent itself; it drives the agent CLIs you already have.

There's also Crush from Charm (LSP-aware, MCP support, switch models mid-session) and Alibaba's Qwen Code.
-->

---

# How to choose

| If you want… | Try |
| --- | --- |
| One terminal agent that works with any model | OpenCode or Aider |
| VS Code with approve-each-diff control | Cline or Kilo Code |
| A general-purpose desktop agent | goose |
| To run and compare several agents | OpenHands or T3 Code |

Before you commit, check the last release date and the open-issue count.

<!--
This is the module's recommendation, not a ranking.

Check maintenance before choosing. Several popular projects stopped being maintained in 2026.
-->

---

# 2026 was hard on open-source AI tools

| Project | What happened |
| --- | --- |
| Roo Code | Shut down May 15, 2026; pivoted to a hosted product |
| Continue | Archived and read-only after a final 2.0 release |
| Gemini CLI | Still open, but individual users moved to Antigravity CLI |
| AutoGen | Archived in favor of Microsoft Agent Framework |
| Promptfoo | Bought by OpenAI, which says the project stays open |
| OpenClaw | Creator joined OpenAI; the project moved to a foundation |

You can fork an abandoned project. Nobody has to maintain the fork.

<!--
Roo Code, itself a fork of Cline, shut down its extension, cloud, and router and pointed users to Cline or the community fork ZooCode. OpenAI announced the Promptfoo acquisition on March 9, 2026.

The pattern is familiar from earlier open-source eras: venture-funded companies build open tools to win adoption, then pivot, sell, or shut down.

Neutral foundations are one response. The Agentic AI Foundation now hosts MCP, AGENTS.md, goose, and Agent Skills. When you choose a tool, weigh its governance (one company, or a foundation with several members) as well as its features.
-->

---

# Case study: OpenClaw

A personal agent that lives in Signal, Telegram, Discord, and WhatsApp

| Date | Name |
| --- | --- |
| Nov 24, 2025 | Warelay |
| Dec 3, 2025 | CLAWDIS |
| Jan 2, 2026 | Clawdbot |
| Jan 27, 2026 | Moltbot, after trademark complaints from Anthropic |
| Jan 30, 2026 | OpenClaw |

It passed 247,000 GitHub stars by early March 2026.

<!--
OpenClaw is an open-source personal assistant agent by Peter Steinberger. It runs on your own machine, connects to a model of your choice, and acts on your email, calendar, files, and accounts. It extends itself with skills: folders with a SKILL.md, the same format as Agent Skills.

It grew faster than almost any project before it. Moltbook, a social network for AI agents launched by Matt Schlicht, rode the same wave.

On February 14, 2026, Steinberger announced he was joining OpenAI and that a non-profit OpenClaw Foundation would steward the project. OpenClaw 2.0 shipped on August 30, 2026.

The naming history comes from Wikipedia's article on OpenClaw, linked in the module.
-->

---

# What OpenClaw showed

- Demand is real for agents that live where people already talk
- It's the lethal trifecta in one package: untrusted input, private data, actions
- Defaults are security policy; tens of thousands of instances exposed
- A skill registry is a supply chain; 341 of 2,857 skills flagged malicious
- The fix is sandboxing, least privilege, vetted extensions, confirmations

<!--
People want an agent that keeps memory between sessions and can act across their accounts. That's a different product from a coding agent.

A personal agent reads untrusted content (emails, messages, web pages), holds private data, and can send messages and take actions. Those three together make prompt injection dangerous (module 11).

On exposed instances, late January to early February 2026, figures differ by researcher. Censys reported about 21,600; Bitsight more than 30,000. Early versions bound the gateway to all network interfaces by default.

On skills, Koi Security reported auditing 2,857 skills on the public ClawHub registry and flagging 341 as malicious, attributed to one campaign that delivered password-stealing malware to macOS and Windows users. The maintainers responded with reporting tools, malware scanning, and minimum account ages for uploaders.

Institutions noticed. In March 2026, Chinese authorities reportedly restricted state agencies and state-owned firms from running OpenClaw on office computers. Reviewers of the 2.0 release still criticized it for not enabling its sandbox by default and not encrypting stored secrets.

So an agent that can do everything on your behalf needs sandboxing, least-privilege credentials, vetted extensions, and confirmation before irreversible actions. Most early users had none of these.
-->

---

# Inference runtimes: running models yourself

| Runtime | Reach for it when |
| --- | --- |
| llama.cpp | You want maximum portability, or you're on a laptop |
| Ollama | You want the easiest local setup: `ollama run <model>` |
| vLLM | You're serving a model to a team or a product |
| SGLang | You serve agent workloads with lots of shared prompt prefixes |
| MLX | You're on a Mac and want speed or local fine-tuning |

Most harnesses can use any of these through an OpenAI-compatible endpoint.

<!--
llama.cpp is a C/C++ inference engine and the home of the GGUF quantized-model format; it runs on CPUs, GPUs, and Apple Silicon.

Ollama is a friendly wrapper that downloads and serves a model with a local OpenAI-compatible API.

vLLM does high-throughput GPU serving, built around PagedAttention (Kwon et al., 2023).

SGLang does fast serving with prefix caching (RadixAttention) and structured generation (Zheng et al., 2023).

MLX is Apple's array framework for Apple Silicon, with mlx-lm for running and fine-tuning models.

Module 04 covers which models to run and how much hardware you need.
-->

---

# You may not need a framework

The heart of the module's 30-line agent loop (abridged):

```python
for turn in range(30):                  # a turn budget
    resp = client.messages.create(model=MODEL, max_tokens=4096,
                                  tools=TOOLS, messages=messages)
    messages.append({"role": "assistant", "content": resp.content})
    if resp.stop_reason != "tool_use":
        break                           # the model is done
    messages.append(tool_results(resp)) # run each tool, ask y/N first
```

<!--
Anthropic's "Building effective agents" warns that frameworks "often create extra layers of abstraction that can obscure the underlying prompts," and suggests starting with direct API calls.

The full version in the module uses the Anthropic Python SDK. It defines one tool, bash. Its run function asks the user y/N before running each command (that's the permission system) and keeps only the last 10,000 characters of output (crude context management). The 30-turn loop is the budget, so it can't run forever. On this slide, tool_results stands in for the few lines in the module that build the tool-result message. Other providers' SDKs look very similar.

Everything a harness adds, such as better tools, sandboxing, compaction, hooks, and a UI, is an improvement on these 30 lines. Writing it once is the fastest way to understand module 06, and it's the first step of the Try it.
-->

---

# A loop, a framework, or a harness?

| Use | When you need |
| --- | --- |
| A plain loop | One agent, a handful of tools, short sessions |
| A framework or SDK | State across restarts, tracing, many tools or agents, approval steps |
| An existing harness | "A coding agent, but scripted" |

Frameworks: LangGraph · LlamaIndex · DSPy · Pydantic AI · CrewAI · Mastra · smolagents

Lab SDKs: OpenAI Agents SDK · Claude Agent SDK · Google ADK

<!--
A framework gives you building blocks: model clients, tool definitions, memory, state, tracing, multi-agent coordination. An SDK from a lab gives you that lab's agent harness as a library. Frameworks and SDKs also earn their keep for systematic prompt optimization (DSPy).

When to reach for each, per the module:
- LangGraph: explicit, durable, resumable workflows with checkpoints and human-approval steps.
- LlamaIndex: your agent's main job is answering from your data.
- DSPy: you have an eval set and want to optimize prompts against a metric.
- Pydantic AI: typed inputs and outputs in a Python service.
- CrewAI: prototyping a multi-agent design quickly.
- Mastra: your team works in TypeScript.
- smolagents (Hugging Face): something small enough to read in an afternoon.
- AutoGen pioneered conversational multi-agent programming; Microsoft has archived it and names Microsoft Agent Framework its successor. AG2 is a community fork.
- OpenAI Agents SDK (March 2025): agents, handoffs, guardrails, tracing.
- Claude Agent SDK: the harness behind Claude Code as a library, renamed from the Claude Code SDK in September 2025.
- Google ADK: designed to work with A2A.

"Existing harness" means things like the Claude Agent SDK, Codex CLI in headless mode, or OpenCode.
-->

---

# Extensions: MCP servers and skills

- Reference MCP servers are educational, "not production-ready solutions"
- Official servers: GitHub, Playwright (Microsoft), Chrome DevTools (Google)
- Find published servers in the official MCP Registry
- Skills: anthropics/skills, obra/superpowers, the Agent Skills spec
- Extensions run with your agent's permissions; they're dependencies
- Read before installing, pin versions, grant the narrowest credentials

<!--
The reference servers in modelcontextprotocol/servers: Everything (a test server), Fetch, Filesystem, Git, Memory, Sequential Thinking, and Time. Earlier reference servers such as GitHub, Slack, Postgres, and Puppeteer moved to an archive as vendors shipped official ones.

GitHub's official server covers issues, pull requests, code search, and Actions, locally or hosted. Playwright MCP automates a browser through the page's accessibility tree, so an agent can test the web app it just built. Chrome DevTools MCP gives console logs, network requests, and performance traces from a real Chrome.

Prefer servers maintained by the vendor of the service. Read the tool descriptions before connecting, because they go straight into your agent's context.

anthropics/skills (about 190K stars) has Anthropic's examples, including the document skills behind Claude's file features, a template, and the specification. obra/superpowers, by Jesse Vincent, is a popular community library of workflow skills such as test-driven development and systematic debugging. The Agent Skills spec is now governed by the Agentic AI Foundation, so a skill written for one harness works in others.

A skill is instructions plus, often, scripts your agent will run. The ClawHub malware shows what happens when people install skills like browser bookmarks. MCP "tool poisoning" research is in module 11.
-->

---

# Orchestrators: Gas Town and Beads

Gas Town (Steve Yegge, January 2026) runs 20–30 coding agents at once

| Role | Job |
| --- | --- |
| Mayor | Takes your request and assigns work |
| Polecats | Worker agents |
| Rigs | Wrap repositories |
| Witness | Watches for stuck agents |
| Refinery | Batches and verifies finished work before merging |

Beads is a graph issue tracker, backed by Dolt, that agents share as memory

<!--
Gas Town is MIT-licensed. Its vocabulary is deliberately colorful. Claude Code is the default runtime, and it supports Codex, Gemini, Cursor, Amp, OpenCode, and others. Yegge's eight-stage ladder of AI coding workflows comes from the same launch essay and is covered in module 08.

Beads, also by Yegge and MIT-licensed, is backed by the version-controlled database Dolt. Agents create tasks, record dependencies, find unblocked work, claim it, and close it. It replaces sprawling markdown plan files with structured memory many agents can share. Gas Town depends on it.

OpenHands Agent Canvas and T3 Code are GUIs for running and supervising several agents, without Gas Town's autonomous coordination.

Next is my experience with two projects from this deck.
-->

---

<!-- _class: take -->

## OpenClaw and Gas Town

> **Bryan's take:** OpenClaw had a couple of issues, but it was Gas Town that really did not work for me.

<!--
That's my report as one user, not a review of either project.

The module itself doesn't rate Gas Town. If you want to follow up, module 08 covers how much autonomy works day to day.
-->

---

<!-- _class: divider -->

# The maintainers' side

AI made contributions cheap and review expensive

<!--
Open source runs on volunteer review time. AI tools made it nearly free to produce a plausible-looking pull request or bug report, and the cost moved to maintainers, who have to read every one.
-->

---

# curl ended its bug bounty

| Measure | Value |
| --- | --- |
| Confirmed vulnerabilities, all time | 87 |
| Paid out | More than $100,000 |
| Share of reports that were real, earlier years | Above 15% |
| Share of reports that were real, 2025 on | Below 5% |
| Bounty ended | January 31, 2026 |

"Not even one in twenty was real." (Daniel Stenberg)

<!--
Daniel Stenberg is curl's founder and lead developer. He had complained about AI-generated security reports since early 2024. On January 26, 2026, he announced the end of the bounty, effective January 31.

He said the money drew in low-effort submissions, and "the never-ending slop submissions take a serious mental toll to manage."

curl now takes reports through GitHub's private vulnerability reporting and email, with no payouts.

The problem was reports nobody had checked, regardless of how they were written.
-->

---

# Project AI policies range widely

| Project | Policy | In short |
| --- | --- | --- |
| Gentoo | Ban (April 2024) | No AI-assisted content: copyright, quality, ethics |
| QEMU | Decline | Rejects contributions believed to derive from AI output |
| LLVM | Human in the loop | Review it all, label it, write your own PR text |
| Linux kernel | Human accountability | "AI agents MUST NOT add Signed-off-by tags" |
| Ghostty | Disclose and understand | Disclose all AI use; newcomers need a vouch |

The 2026 trend: away from bans, toward disclosure and accountability.

<!--
QEMU will "DECLINE any contributions which are believed to include or derive from AI generated content." AI for research, static analysis, or debugging is fine if its output isn't submitted.

LLVM: read and review all generated code before asking others to; label substantial AI help, for example with an Assisted-by: trailer; no autonomous agents in project spaces; no AI on "good first issue" tickets; maintainers can label a contribution "extractive." The golden rule: "a contribution should be worth more to the project than the time it takes to review it."

In the Linux kernel, only a human can certify the Developer Certificate of Origin, and the human submitter takes full responsibility.

Ghostty says "All AI usage in any form must be disclosed." You must fully understand your code. No AI-generated media. First-time contributors need a maintainer to vouch for them, or their PRs are closed automatically. "Bad AI drivers will be denounced" on a public list.

A human must understand every line they submit and be able to defend it.
-->

---

# Contributing with AI: etiquette

- Read `CONTRIBUTING.md` and the AI policy, then follow them
- Understand every line; explain it without the AI open
- Reproduce bugs yourself, on a real build
- Keep PRs small; run the project's tests and linters first
- Write the description and replies yourself; disclose AI use
- Never let an agent post for you; accept a no

<!--
The module's nine points in full:

1. Read the project's CONTRIBUTING.md and AI policy. If they ban AI-generated contributions, don't submit them. If they require disclosure, disclose.
2. Understand every line. If you can't explain the change and its edge cases without the AI open, you aren't ready.
3. Reproduce the problem yourself. For bug and security reports especially, show a real reproduction on a real build. Don't forward a model's speculation.
4. Keep it small and focused. One logical change per PR. Don't let an agent "also clean up" unrelated files.
5. Run the project's tests and linters locally. Never make maintainers' CI find what you could have found.
6. Write the description and review replies yourself: what you changed, why, and what you didn't verify. Maintainers want to talk to you, not your agent.
7. Disclose AI assistance even where it isn't required. Name the tool and roughly how you used it.
8. Respect maintainers' time. If they say no, accept it. Don't reopen the same PR with a new prompt.
9. Never let an agent post autonomously to an issue tracker, pull request, or mailing list on your behalf.
-->

---

# For students: contribute to learn

- Pick a project you use; read its rules first
- Use AI to understand the code, not to submit it
- Claim an issue; some "good first issues" are AI-free by design
- Reproduce the bug by hand; write a failing test first
- Rework any agent draft until you could have written it
- Keep a log of what you learned; that's your evidence

<!--
Contributing to open source teaches real engineering. AI can help you understand the work, but you still have to learn it.

Using AI to understand means asking an agent to explain the architecture, trace a request through the code, or explain why a test is failing. That's where it helps most with the least risk.

Some projects, LLVM for example, ask that newcomer "good first issues" be done without AI, because they exist to teach. Say you're working on an issue before you write code.

If an agent drafts the fix, rework it until you could have written it, then delete what you can't defend.

The module adds: get a second opinion before the maintainers' opinion (a different model or a classmate; module 10), write the PR description in your own words with disclosure, and handle review feedback yourself. If you don't know an answer, say so and go find out.

For a course, use the log to assess learning (module 15). A merged PR alone doesn't show it.
-->

---

<!-- _class: take -->

## Review before the maintainer does

> **Bryan's take:** Having several agents or models review each other's work is valuable. That applies before you open a pull request on someone else's project too. Run a second reviewer over your diff before a maintainer has to.

<!--
My opinion from daily use. It ties back to module 10 (AI code review) and to the student checklist on the previous slide: get a second opinion before the maintainers' opinion.
-->

---

# Try it

On your own (2–3 hours), read a harness, then write one:

1. Clone OpenCode, Aider, Cline, or Codex CLI; find its system prompt and tools
2. Run the 30-line loop against a toy repo with a failing test
3. Add one idea from the real harness; measure it on three tasks

As a class, take the maintainer's chair: review ten mixed PRs, time each, and spot the unreviewed AI output.

<!--
Find the harness's system prompt and the definitions of its file-editing and shell tools, and write down three design choices that surprised you. Improvements to try: a better edit tool, output truncation, or a deny list for dangerous commands. Finish with a half-page comparison of your loop and the real harness.

In class, the instructor prepares ten pull requests against a small project the class knows. Some are careful human work, some careful AI-assisted work with disclosure, some unreviewed AI output. Students act as maintainers: time each review, decide accept, revise, or reject, and guess which were unreviewed AI output. Then discuss what made a PR cheap or expensive to review, draft an AI-contribution policy for the project, and compare it with LLVM's and Ghostty's.
-->

---

# Discussion

1. Is an open harness that only works well with one closed model really "open"?
2. How should a team decide whether to depend on an open-source AI tool?
3. Gentoo bans AI contributions; LLVM allows them with review. Which would you pick?
4. Who should bear the cost of filtering AI-generated reports?

<!--
Fuller versions from the module:

1. Is an open-source harness that only works well with one vendor's closed model really "open"? What would you need for a fully open stack? (The module's answer to the second part: a model-agnostic harness, an open-weight model, and a local runtime.)
2. Roo Code, Continue, and others were archived or shut down in 2026. How should a team decide whether to depend on an open-source AI tool?
3. Gentoo bans AI-generated contributions, while LLVM allows them with human review and disclosure. Which policy would you choose for a project you maintain, and why?
4. curl's confirmed-report rate fell below 1 in 20. Who should bear the cost of filtering AI-generated reports: reporters, platforms, AI vendors, or maintainers?

More if time allows: What would a "safe by default" personal agent have to do differently from OpenClaw? When does a framework like LangGraph or DSPy earn its complexity over a 30-line loop?
-->

---

# Read more

- [Module 13: The open-source ecosystem](../modules/13-open-source-ecosystem/)
- [Building effective agents](https://www.anthropic.com/research/building-effective-agents) (Anthropic, December 2024)
- [The end of the curl bug bounty](https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/) (Daniel Stenberg, January 2026)
- [LLVM AI tool use policy](https://llvm.org/docs/AIToolPolicy.html)

<!--
The module links every project in this deck, plus the papers behind vLLM, SGLang, DSPy, AutoGen, SWE-bench, and OpenHands.
-->

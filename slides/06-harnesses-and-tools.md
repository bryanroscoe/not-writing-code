---
marp: true
theme: not-writing-code
paginate: true
title: "06: Harnesses, tools, and MCP"
description: "Agent = model + harness: the loop, tools, MCP, and the shared toolkit"
footer: "A Brief Introduction to Not Writing Code · 06 Harnesses, tools, and MCP"
---

<!-- _class: lead -->

# 06: Harnesses, tools, and MCP

Agent = model + harness

<!--
Plan for 40 to 50 minutes in three parts: how coding tools got from autocomplete to orchestrators; tools and MCP; and the toolkit every major harness now shares, ending with how to choose one. The reading is module 06.

If you can, keep a terminal open with a CLI agent so you can show its context breakdown live (/context in Claude Code; other harnesses have similar views).
-->

---

## Why this matters

- The same model can feel brilliant in one harness and clumsy in another.
- "The model got worse" is often a harness change.
- Tools and permissions decide what an agent can safely do.
- The same concepts apply across products.

<!--
People say "model X is bad at Y" when the cause is often the harness: the loop, the tools, the permissions, the context management, the interface.

By 2026 the major harnesses had converged on the same features under slightly different names. Learn instruction files, skills, subagents, hooks, MCP, permission modes and worktrees once, and they carry over to the next tool.
-->

---

## Agent = model + harness

```text
Harness = agent loop + tools + permissions + context management + UI
Agent   = model + harness
```

```text
your task → model → tool call ("run the tests")
          → harness checks permission, runs it
          → result goes into the context → model → ...
          → model says done → answer, diff, or PR
```

The model is the engine. The harness is the rest of the car.

<!--
On its own, a language model takes text in and predicts text out. It can't open a file, run a test, or remember yesterday's conversation. Everything that turns it into something that edits your codebase is the harness.

The five parts. The agent loop calls the model, runs any tool it asks for, feeds the result back, and repeats until the model says it's done. Tools are functions the model may call, such as read_file, edit_file, bash, web_fetch and search. Permissions decide which calls run automatically, which need approval, and which are forbidden: allow npm test, ask before git push, never rm -rf. Context management decides what goes into the limited window and what gets summarized or dropped. The user interface might be a terminal, an IDE panel, a web dashboard, a desktop app, or a Slack bot.

Most agents run a variant of ReAct (Yao et al., 2022): reason, act, observe.
-->

---

## "Claude Code got worse." The weights hadn't changed.

Anthropic's April 2026 postmortem traced user complaints to three harness changes:

- A lower default reasoning effort
- A bug that cleared earlier reasoning on every turn
- A system-prompt line capping text between tool calls

All three were reverted or fixed. Evaluate a model in the harness you'll actually use.

<!--
This is the clearest recent example that the harness, not the model, can be the problem.

Other harness choices change results too. On tool design, the SWE-agent paper (Yang et al., 2024) gave a model compact file viewers, a search tool, and an editor that lints on save, and the same model got much better at fixing real GitHub issues than with a raw shell. How a harness compacts history, loads instruction files and returns tool output decides what the model sees (module 07). Asking permission on every command trains you to click yes without reading, while never asking can do damage. And agentic benchmark scores depend on the scaffold (module 05).

Before you switch models, check the harness version, the effort setting, recent instruction-file edits, and connected servers.
-->

---

<!-- _class: divider -->

# Part 1

## From autocomplete to orchestrators

<!--
About 10 minutes on six overlapping generations of coding tools, why the terminal won in 2025, and how fast the market changes.
-->

---

## Six generations, all still in use

| # | Generation | Arrived | What you do |
| --- | --- | --- | --- |
| 1 | Autocomplete | 2021 | Type; it suggests the next line or block |
| 2 | Chat | late 2022 | Paste code in, copy answers back |
| 3 | IDE agents | 2023–2025 | Describe a change; accept its diffs |
| 4 | CLI agents | 2025 | Give a task in the terminal |
| 5 | Cloud or background agents | 2024–2025 | Assign a task, walk away, get a PR |
| 6 | Desktop GUIs and orchestrators | 2025–2026 | Supervise several agents at once |

<!--
Examples for each row, from the module.
1. GitHub Copilot, technical preview June 29, 2021, built on OpenAI Codex.
2. ChatGPT, Claude.ai, IDE chat panels.
3. Cursor, Windsurf, Copilot agent mode, Cline.
4. Claude Code (research preview February 24, 2025), Codex CLI (April 2025), Gemini CLI (June 2025), OpenCode, Amp, Factory Droid, Cursor CLI, Copilot CLI, Crush.
5. Devin (2024), Codex cloud (May 2025), Copilot coding agent (May 19, 2025), Jules (2025), Claude Code on the web (October 20, 2025), Cursor cloud agents.
6. Conductor, T3 Code, the Codex app (February 2, 2026), the Claude desktop app, Gas Town, OpenHands Agent Canvas.

Ask the room which generations they've used. Most people have used three or four, because the generations overlap.
-->

---

## Why the terminal won, and what wrapped it

- The shell is the universal tool: build, test, lint, query, `gh`.
- An agent that runs commands needs no per-service integration.
- CLI agents run headless: in CI, in scripts, in cloud sandboxes.
- Generation 6 wraps generation 4: GUIs that drive your installed CLIs.
- They add parallel sessions, one git worktree each, side-by-side diffs.

<!--
Orchestrators like Conductor and T3 Code are not agents themselves. They drive the CLI agents you already have installed and signed into.

T3 Code describes itself as an "agent harness control surface." It's MIT-licensed, comes from Theo Browne's company (the pingdotgg GitHub organization), and supports Claude Code, Codex, Cursor, OpenCode, Antigravity and others. Its README calls it "very very early." Conductor, from Melty Labs, is a Mac app that runs parallel Claude Code, Codex and Cursor agents in isolated workspaces.

Gas Town (Steve Yegge, January 2026) is an orchestrator for 20 to 30 agents with named roles: a "Mayor" coordinator, "polecat" workers, and a "Refinery" merge queue. It sits at the top of Yegge's eight-stage ladder of AI coding workflows, covered in module 08.
-->

---

## The market churns (as of November 2026)

- Gemini CLI's individual users moved to Antigravity CLI, June 18, 2026
- SpaceX acquired Cursor, August 14, 2026
- Windsurf split in July 2025; Google hired its leaders, Cognition bought the rest
- Roo Code's extension shut down May 15, 2026
- Continue is archived and read-only
- Amp spun out of Sourcegraph, late 2025

Check before you standardize on anything.

<!--
Gemini CLI now targets enterprise Gemini Code Assist on Google Cloud. Free individual access and the Google AI Pro and Ultra plans moved to Google's Antigravity CLI, invoked as agy.

With Windsurf, Google licensed its technology and hired its leaders, and that team went on to build Antigravity. Cognition, the maker of Devin, acquired the rest of the company.

Codex is another kind of change. It started as a CLI (April 2025) and a cloud agent (May 2025), and by late 2026 OpenAI's docs list it across the ChatGPT desktop, web and mobile apps plus the CLI, IDE extension and cloud.

Portable formats like AGENTS.md, Agent Skills and MCP make a forced switch cheaper. Discussion question 4 comes back to this.
-->

---

<!-- _class: divider -->

# Part 2

## Tools and MCP

<!--
About 15 minutes on what a tool is, what MCP standardizes, how it spread, what it costs, and when to use something else.
-->

---

## A tool is a name, a description, and a schema

```json
{
  "name": "run_tests",
  "description": "Run the test suite. Use after editing code.",
  "input_schema": {
    "type": "object",
    "properties": { "path": { "type": "string" } }
  }
}
```

- Descriptions are prompts. Vague ones cause wrong tool choices.
- Every definition costs context, on every model call.

<!--
This example is shortened from the module's. The harness sends the model a list of tool definitions. When the model wants to act, it outputs a structured tool call. The harness checks permissions, runs the function, and puts the result back into the context.

Because the model picks tools from their names and descriptions, writing a tool is writing a prompt. Anthropic's guide "Writing effective tools for agents" (September 2025) treats tool design as a core engineering task.

Because definitions are sent on every call, fifty tools can eat a large share of the window before you type anything. That's why MCP can use so much context.
-->

---

## MCP is one protocol for tools and data

- Without it, 10 harnesses × 100 services = 1,000 custom integrations.
- With MCP, 10 clients plus 100 servers.

| When | What happened |
| --- | --- |
| Nov 25, 2024 | Anthropic releases the Model Context Protocol |
| Mar–May 2025 | OpenAI, Google, and Microsoft adopt it |
| Dec 9, 2025 | Donated to the Linux Foundation's Agentic AI Foundation |
| Jan 26, 2026 | MCP Apps lets tools return interactive UI |
| Jul 28, 2026 | A stateless spec: no handshake, no sessions |

<!--
MCP is an open protocol that standardizes how an AI application discovers and calls external tools and data. Anthropic's analogy is a USB-C port for AI applications.

Fuller timeline. March 2025: the spec adds the Streamable HTTP transport, replacing HTTP+SSE. March 26, 2025: OpenAI adds MCP to its Agents SDK and says ChatGPT desktop and the Responses API will follow. April 2025: Google DeepMind's CEO says Gemini models and SDK will support it; Gemini CLI ships with MCP in June. May 2025: Microsoft announces support across GitHub, Copilot Studio and Windows at Build. September 8, 2025: the official MCP Registry launches in preview. December 9, 2025: Anthropic donates MCP to the new Agentic AI Foundation (AAIF), alongside Block's goose and OpenAI's AGENTS.md.

MCP Apps renders tool UI such as forms and dashboards in a sandboxed iframe; it launched in Claude, goose and VS Code Insiders, with ChatGPT the same week. The 2026-07-28 spec sends version and capabilities with every request and deprecates Roots, Sampling and Logging. A stateless server can sit behind an ordinary load balancer, which makes hosted MCP easier to scale. Tools, resources and prompts are unchanged.
-->

---

## Host, client, server

| Term | Meaning |
| --- | --- |
| Host | The AI app you use: Claude Code, Codex, Cursor, VS Code, ChatGPT |
| Client | The connector inside the host that talks to one server |
| Server | A program exposing capabilities: GitHub, Postgres, a browser |
| Tools | Functions the model can call |
| Resources | Data the app can read, addressed by URI |
| Prompts | Reusable templates, often shown as slash commands |
| Transports | stdio for local subprocesses; Streamable HTTP for remote servers, usually with OAuth |

To the model, an MCP tool looks like any other tool.

<!--
Messages are JSON-RPC 2.0. A server is a small adapter. It says "here are my tools and their schemas," then runs calls and returns results. The harness adds those tools to the model's tool list.

Configuration is a small file. In Claude Code, a project-level .mcp.json might run Playwright locally over stdio and connect to GitHub's hosted server over HTTP, with the token read from an environment variable rather than written in the file. Codex CLI uses TOML in ~/.codex/config.toml for the same idea. With the official Python SDK, a working server is about ten lines. The module shows all three.

For contrast, Google's Agent2Agent (A2A) protocol, announced April 2025 and given to the Linux Foundation that June, connects one agent to another agent. In coding work you meet MCP daily and A2A rarely.
-->

---

## MCP's costs are real

- Context bloat, with "58 tools consuming approximately 55K tokens" up front
- A server is code running with your credentials
- Servers that read web pages, issues, or email are injection channels
- Quality is uneven; reference servers are "not production-ready solutions"
- Or just use the CLI; agents already know `gh`, `psql`, `kubectl`

<!--
The bloat figure is Anthropic's typical five-server setup, from its advanced tool use post (November 2025): 58 tools, about 55K tokens, "before the conversation even starts." It also reported seeing 134K tokens of tool definitions internally before optimization. Large tool lists also make tool selection less accurate.

On security, a malicious or compromised server can lie in its tool descriptions ("tool poisoning"), change behavior after you approve it, or exfiltrate data. Hou et al. (2025) survey the threats; module 11 covers defenses.

Many community servers are thin API wrappers with poor descriptions and huge outputs. A popular server can still be unsafe. In early 2026, hundreds of malicious skills appeared on OpenClaw's public skill registry.

The CLI argument is that the model already knows those tools from training, and their output can be filtered with grep or jq before it reaches the context.
-->

---

## Three ways to give an agent a capability

| Option | Strengths | Costs |
| --- | --- | --- |
| MCP tool | Structured, discoverable, OAuth; works without a shell | Context; uneven quality |
| CLI in a shell | Known from training; composes with pipes; free until used | Needs a shell and a sandbox; no standard auth |
| Code mode | One Anthropic example: 150,000 → 2,000 tokens | Needs a secure execution environment |

Use MCP for integrations others will use. For your own agent, try the CLI first.

<!--
Code mode means presenting tools as a code API that the model calls from a sandbox. Cloudflare's Code Mode (September 26, 2025) converts MCP tools into a TypeScript API, arguing that "LLMs are better at writing code to call MCP, than at calling MCP directly." Anthropic's "Code execution with MCP" (November 4, 2025) presents servers as code files on a filesystem that the agent browses on demand. In its example, token use dropped "from 150,000 tokens to 2,000 tokens," a 98.7% saving, because intermediate data stayed in the sandbox instead of passing through the model. It's the most token-efficient option for multi-step data work.

A related trick, tool search, loads a small search tool first and fetches definitions only when needed; Anthropic reported an 85% token reduction.

The 2026 trend is toward hybrids: lazy tool loading, MCP servers presented as code APIs, and skills that bundle scripts. Discussion question 2 asks the room for examples of each.
-->

---

<!-- _class: divider -->

# Part 3

## The shared toolkit

<!--
About 15 minutes on the features every major harness now has, three of them in detail, closed products, and how to choose.
-->

---

## The kit every major harness converged on

| Feature | Use it for | Watch out for |
| --- | --- | --- |
| Instruction files | Commands, conventions, gotchas | Bloat (module 07) |
| Skills | Repeatable procedures | They can run code |
| Subagents | Exploring, reviewing, noisy work | Extra tokens; lossy summaries |
| Hooks | Deterministic enforcement | A buggy hook blocks all work |
| Plugins | Sharing a team's setup in one install | Supply-chain risk |
| Permission modes | Matching autonomy to risk | "Bypass all" on your real machine |
| Sandboxing | Longer runs without approvals | Leaky allowlists |
| Git worktrees | Parallel agents without collisions | Disk use; clean up after |
| Checkpoints | Undoing a bad turn | Not a replacement for commits |

<!--
Names differ slightly between products; the ideas are the same. The module uses Claude Code's terms because its docs are detailed. Codex, Cursor, OpenCode and others have close equivalents.

Two more rows from the module: slash commands, saved prompts you trigger by name, which Claude Code has folded into skills; and scheduling and loops (/loop, /goal, cloud schedules), covered in module 07.

They converged because features are cheap to copy, and good ideas are visible in open-source projects. Aider's repository map, the Ralph loop, worktree-per-agent orchestration and skills all spread within months. Your skills transfer between tools, and no harness keeps a feature lead for long. Durable advantages come from the model, the integration with where work already happens, and the price.
-->

---

## Skills load on demand. Hooks always run.

| | Skills | Hooks |
| --- | --- | --- |
| What | A folder with `SKILL.md` and optional scripts | Your shell commands at lifecycle events |
| Loads | Description up front; body only when relevant | Every time the event fires |
| Who decides | The model, when a task calls for it | No one: the harness always runs it |
| Use for | Releases, migrations, other procedures | Format on save; block `rm -rf`; no "done" while CI is red |

Prose in an instruction file is a request. A hook is a rule.

<!--
Anthropic introduced Agent Skills on October 16, 2025, published the format as an open standard at agentskills.io on December 18, 2025, and donated it to the AAIF on October 22, 2026, reporting more than 70 agent platforms had integrated it, including ChatGPT, Cursor, GitHub Copilot and VS Code. With progressive disclosure, the agent sees a one-line description of every skill and reads the full instructions only when a task calls for them, so dozens of procedures cost almost nothing until used. Skills can run code, so treat third-party skills like dependencies.

For hooks, Claude Code's docs say instruction files are treated "as context, not enforced configuration." To block an action regardless of what the model decides, use a hook. The module has two examples: a PostToolUse hook that runs Prettier after every edit, and a Stop hook that blocks the agent from ending its turn while CI is still running on the branch, so it keeps working and sees the reason. Keep hooks fast; a buggy one can block everything.
-->

---

## Approval prompts stop working when you always say yes

- Users approve 93% of permission prompts (Anthropic, March 2026).
- In auto mode, a classifier approves routine actions; hard blocks stay.
- It still missed 17% of "overeager" actions in Anthropic's tests.
- Long unattended runs need a real sandbox with limited credentials.

<!--
Anthropic was candid that auto mode is "not a drop-in replacement for careful human review on high-stakes infrastructure."

Permission modes run from plan-only, through ask-every-time and auto-accept edits, to classifier-approved auto mode and full bypass. Approval fatigue is clicking yes on the fortieth prompt without reading it. Allowlists and sandboxes keep the remaining prompts meaningful.

Permissions are a security boundary, not a UX detail. An agent that can read untrusted input, access private data, and communicate externally has all three parts of Simon Willison's "lethal trifecta." Permission modes, network allowlists, credential scoping and sandboxes are how you break at least one leg. Module 11 goes further; Anthropic's "How we contain Claude across products" (May 2026) shows how one vendor layers these defenses.
-->

---

## Closed bundles put model, harness, and tools in one

| Product | Good for |
| --- | --- |
| Claude Design (Apr 2026, research preview) | Idea to clickable prototype or deck |
| Claude in Chrome | Web workflows; testing web apps |
| Codex app and automations (Feb 2026) | Supervising parallel tasks; recurring triage |
| ChatGPT agent and Atlas | Research and multi-step web tasks |
| Cursor with Composer | Fast in-editor agent loops |
| Google Antigravity | Teams centered on Gemini models |
| Devin, Jules, Copilot coding agent | Well-scoped backlog tickets |

Convenient, but you can't see inside, swap parts, or stop them changing.

<!--
Two cautions apply to all of them.

Browser and computer-use agents are the riskiest category. They read untrusted web content while holding your logged-in sessions. Anthropic's Chrome launch post reported a 23.6% prompt-injection attack success rate without mitigations and 11.2% with them in its tests. Better, and still not zero. Read module 11 before pointing one at your email or bank.

Bundled products change underneath you. The vendor can change the model, the prompts or the limits at any time. That's fine for prototypes. For a workflow a team depends on, prefer tools whose configuration you can see and version.

If asked, Claude Design can apply a team's design system, export to Canva, PDF, PPTX or HTML, and package a handoff bundle for Claude Code. The module also lists Claude Code itself, Claude Cowork and Artifacts. Model tiers behind each product change often; see module 03.
-->

---

## How to choose a harness

| Question | Look for |
| --- | --- |
| Model access | One vendor's models, or bring any model? |
| Cost model | Subscription, per-token API, or seats (module 12) |
| Team standards | Reads `AGENTS.md`? Supports Agent Skills and MCP? |
| Privacy | Retention terms, zero data retention, local or self-hosted |
| Extensibility | Hooks, skills, plugins, MCP, an SDK |
| Autonomy and safety | Permission modes, sandboxing, worktrees, audit logs |
| Durability | Open license, foundation governance, portable config |

Don't choose on demo videos.

<!--
One more question from the module: where does the work happen? Terminal, IDE, browser, GitHub issues, or Slack.

Single-vendor examples: Claude Code, Codex, Antigravity. Bring-any-model examples: OpenCode, Cline, Kilo Code, Aider, Cursor.

Starting points by situation, from the module:
A student: one CLI agent plus its IDE extension, with approvals on, so you see every action.
An engineer on a team already using an IDE: that IDE's agent mode, plus one CLI agent for bigger tasks.
A team that must keep code on-premises: an open-source, model-agnostic harness with a self-hosted or local model.
A lead standardizing a team: one primary harness, with shared knowledge in AGENTS.md, skills and hooks, which work across most harnesses, so a later switch is cheap.
Someone running many tasks at once: a CLI agent plus a worktree-based GUI or orchestrator.
-->

---

## A sane baseline setup

1. Pick one CLI agent. Learn its permission modes first.
2. Write a short `AGENTS.md` with commands and non-obvious conventions.
3. Add hooks for whatever must always happen.
4. Connect only the one to three MCP servers you need.
5. Use worktrees before running two agents on one repo.
6. Sandbox before you turn off approvals. Commit often.

<!--
The module's list has eight steps; this folds two in.

Keep AGENTS.md well under 200 lines (module 07). Good first hooks: a formatter after edits, a guard against destructive commands, and a check that tests pass before the agent says "done." Check each MCP server's context cost in your harness's context view, and prefer an existing CLI when the agent already knows it. Move repeated procedures into skills instead of pasting them into the instruction file. Checkpoints are convenient; git is the real safety net.

Too many MCP servers waste context. A popular server or skill can still be unsafe. Approval fatigue, blaming the model for a harness problem, and accidental vendor lock-in cause problems too. Clean up worktrees and sandboxes after parallel work.
-->

---

<!-- _class: take -->

## Bryan's take

> **Bryan's take:** My daily setup is several CLI agents running in parallel, each in its own worktree, which I manage by hand. I drive them through T3 Code, which lets me run Claude and Codex side by side, the two model families I think are best for code ([module 03](../modules/03-model-landscape/)). That puts me at roughly stage 6–7 on Yegge's eight-stage ladder ([module 08](../modules/08-agentic-workflows/)). I'm not running a fully autonomous orchestrator, because I haven't gotten reliable results from one.

<!--
This is my setup and my opinion.

It maps onto Part 1. T3 Code is one of the generation-6 GUIs that drive installed CLI agents, with a worktree per agent. Gas Town, Yegge's own fully orchestrated system, sits at the top of the ladder the take mentions; module 08 covers the ladder and how much autonomy works in practice.

The module adds one related point. A harness's cost model matters as much as its features, and my view that subscriptions are what make heavy agentic use affordable is in module 12.
-->

---

## Try it

**Individual (60–90 minutes)**
- Install a CLI agent; note the context used before you type.
- Connect one MCP server and measure the tokens it adds.
- Add a formatter hook, then a Stop hook that waits for green tests.

**Class or team (one session)**
- Same small task, same model tier, three different harnesses.
- Record time to green, interventions, cost, and diff quality.
- Discuss which differences came from the harness, and which from people.

<!--
Individual steps in full. Open a small project you know and ask the agent to explain the architecture; note which tools it calls. Check the context breakdown and write down how many tokens the system prompt, tool definitions and instruction files use. Connect Playwright or GitHub over MCP and check again. Add a PostToolUse formatter hook and confirm it runs after an edit. Write a Stop hook that blocks "done" until the tests pass, give the agent a task that breaks a test, and watch the hook push it back. Finish with one paragraph: what did the harness do that the model alone couldn't?

For the class version, give every group the same well-specified task, such as adding a feature with tests to a sample repository. Another group judges diff quality.
-->

---

## Discussion

1. Agent = model + harness. Which part matters more for your work today, and why?
2. When should a capability be an MCP server, a CLI, or a skill with a script?
3. Prompts get approved about 93% of the time. Is an always-approved prompt a safety feature?
4. Tools were acquired, pivoted, or shut down in 2026. How does a team protect itself?

<!--
For 1, the April 2026 postmortem and module 05's harness comparisons show the harness can move results a lot. The module also argues that durable advantages come from the model, the integration with where work already happens, and the price.

For 2, use the three-ways table. Building for others favors MCP; your own agent favors trying the CLI first; multi-step data work favors code in a sandbox.

For 3, push toward replacements: allowlists, sandboxes, limited credentials, and hooks for hard rules, so the prompts that remain are worth reading.

For 4, portable formats (AGENTS.md, Agent Skills, MCP), open licenses, foundation governance, and not locking team knowledge into one vendor's format.
-->

---

## Read more

- Module: [06 Harnesses, tools, and MCP](../modules/06-harnesses-and-tools/)
- [MCP documentation](https://modelcontextprotocol.io/docs/getting-started/intro)
- [Code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) (Anthropic, November 2025)
- [April 23 postmortem](https://www.anthropic.com/engineering/april-23-postmortem) (Anthropic, April 2026)

<!--
The module has the full MCP config examples, the ten-line Python server, both hook examples, and the closed-products table. The MCP docs are the place to start building a server. "Code execution with MCP" explains the context-cost problem and one fix. The postmortem is a short, concrete read on how harness changes look like model regressions.

Next session, module 07, covers what goes into the context window and the buzzwords around it.
-->

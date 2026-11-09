---
marp: true
theme: not-writing-code
paginate: true
title: "11: Security and prompt injection"
description: "Why agents follow strangers' text, and the defenses that hold"
footer: "A Brief Introduction to Not Writing Code · 11 Security and prompt injection"
---

<!-- _class: lead -->

# 11: Security and prompt injection

Design as if an injected instruction will get followed

<!--
Today is about defending yourself and your team when you work with coding agents: what prompt injection is, why it's still unsolved, real incidents from 2025 and 2026, and the controls that hold up. The reading is module 11.

Everything here is defensive. The exercises run in throwaway environments with fake secrets. Incident details and advisory counts are as of November 2026.
-->

---

## Why this matters

- Any text an agent reads can try to give it orders
- As of November 2026, nobody has a reliable fix
- Your coding agent has your data, untrusted input, and a shell
- Real attacks in 2025–2026 hit exactly this setup
- The defenses that hold are architecture, not clever prompts

<!--
Web pages, GitHub issues, READMEs, dependency code, and tool descriptions are all text an agent reads, and any of it can try to give the agent orders. That's prompt injection.

A coding agent on a laptop has the three dangerous ingredients by default: your repo and secrets, the open internet and other people's code, and a shell. Real attacks in 2025 and 2026 hit exactly that setup, including malware that drove developers' own AI CLIs to hunt for secrets.

AI-written code isn't automatically secure either. The controls that work are sandboxes, scoped tokens, egress limits, human approval, separated agents, pinned dependencies, and secret scanning.
-->

---

## Instructions and data share one channel

| System | How instructions and data are separated |
| --- | --- |
| SQL with parameterized queries | The API keeps them apart |
| A language model | One stream of tokens; the model *judges* which is which |

Usually it judges correctly. An attacker needs it to fail once.

<!--
Classic software keeps code and data apart. A SQL database knows which bytes are the query and which are the user's input, which is why SQL injection is a solved problem when people use the right API.

A language model has no such separation. The system prompt, your request, a file it opened, and tool output are one stream. If a file tells the model to ignore its previous instructions, the model has to judge whether that sentence is an instruction or content.

The module's analogy is a new assistant who does whatever any piece of paper on their desk tells them, including letters from strangers. You can train them to be suspicious. You can't make them physically unable to read the letter.

In September 2022 Riley Goodside showed GPT-3 abandoning a translation task because of text in the input. Simon Willison named the attack "prompt injection" on 12 September 2022, by analogy with SQL injection. His point still holds: he knew how to beat SQL injection and cross-site scripting, but had no reliable way to beat this.
-->

---

## Indirect injection is the one that matters

attacker plants text (issue, README, web page, package, tool description) → your agent reads it while doing your task → tool calls (shell, git, network, MCP) → secrets or code leave

- Direct: the attacker types it into the app
- Indirect: planted in content an agent reads later
- Jailbreak: a different problem, aimed at the model's own rules

<!--
With direct prompt injection, the attacker types malicious instructions into the app. The risk is mostly to the app owner (leaked system prompts, abuse of the service).

With indirect prompt injection, the attacker plants instructions in content the model reads later, on someone else's behalf. Greshake et al. described this in 2023 ("Not what you've signed up for"): once an application retrieves outside content, the line between data and instructions disappears. For coding agents, this is the one that matters. You don't have to do anything wrong. The agent reads something an attacker wrote while doing the job you gave it.

Jailbreaks are different. A jailbreak tries to get the model to break its maker's safety rules. Prompt injection attacks an application built on a model. Willison draws the line in a 2024 post. The distinction matters because a model can be very hard to jailbreak and still follow an injected instruction to summarize the repo's .env file into a new issue. That request isn't harmful in the abstract. It's harmful because of who asked.
-->

---

## Why it's still unsolved

- 12 published defenses; adaptive attacks beat most at over 90% success
- Anthropic cut browser-agent attack success to about 1–2% (November 2025)
- …and said "prompt injection is far from a solved problem"
- Instruction hierarchy is a learned preference, not an enforced boundary

**A model's resistance to injection is a probability, not a permission system.**

<!--
Defenses so far are probabilistic: train the model to resist, add a classifier, wrap untrusted text in delimiters. Each lowers the success rate. None reaches zero, and attackers adapt.

- "The Attacker Moves Second" (Nasr, Carlini, et al., October 2025) took 12 published defenses, most of which had reported near-zero attack success, and bypassed them with adaptive attacks. An adaptive attack is one tuned against a specific defense, which measures real rather than reported robustness.
- Anthropic reported in November 2025 that improved safeguards cut a strong internal attacker's success rate against browser-use agents to about 1–2%, and in the same post said that even 1% is meaningful risk.
- OpenAI's Instruction Hierarchy (Wallace et al., 2024) trains models to rank system instructions above user text above tool output. It helps, but it's still learned.

Assume some injected instruction will eventually get followed. Limit what it can do.
-->

---

## Two frameworks

| Willison's lethal trifecta (June 2025) | Meta's Agents Rule of Two (October 2025) |
| --- | --- |
| Access to private data | [A] Processes untrustworthy inputs |
| Exposure to untrusted content | [B] Accesses sensitive systems or private data |
| Can communicate externally | [C] Can change state or communicate externally |
| Remove any one leg and data theft fails | At most two, or a human or reliable check approves |

<!--
The lethal trifecta (Simon Willison, 16 June 2025): if one agent combines private data, untrusted content, and external communication, an attacker can plant instructions in the content that make the agent read your data and send it out. Remove any one leg and that data-theft attack fails. Willison notes that tool ecosystems like MCP make the trifecta easy to assemble by accident, because users mix tools from different vendors.

The Agents Rule of Two (Meta, 31 October 2025): until injection can be reliably detected, an agent should have no more than two of A, B, and C. If a task needs all three in one session, the agent shouldn't act without oversight.

Meta's version adds "change state," which matters for coding: an injected agent that can push to git or delete files can do damage without stealing anything.
-->

---

## Coding agents have all three by default

| Property | Typical local coding agent |
| --- | --- |
| Untrusted input | Web results, issues, PR comments, dependency source, READMEs, MCP output |
| Sensitive data | Source, `.env` files, SSH keys, cloud credentials, CI tokens |
| Change state or communicate | A shell, `git push`, package publishing, `curl`, MCP tools that write |

Choose which leg to cut, per task. Put deterministic controls around the rest.

<!--
For each task, decide which leg to remove, and put deterministic controls around the rest.

Some examples. An agent researching documentation on the web doesn't need your cloud credentials. An agent refactoring code locally doesn't need network access beyond the package registry. An agent triaging public issues doesn't need write tokens.

Also on the sensitive list: browser cookies and production databases.
-->

---

<!-- _class: divider -->

# Part 2: In practice

Incidents, risks, and defenses that hold

<!--
In part 2, we'll look at documented incidents, coding-agent risks, and defenses you can combine.
-->

---

## Real incidents, 2025 (1 of 2)

| When | Incident | Lesson |
| --- | --- | --- |
| May 2025 | GitHub MCP "toxic agent flow" | Scope tokens to one repo per task |
| Jun 2025 | EchoLeak (Microsoft 365 Copilot) | Classifiers can be bypassed; zero-click |
| Jul 2025 | Supabase MCP demo | Read-only, project-scoped access |
| Jul 2025 | Amazon Q Developer extension | The prompt is code; protect it like code |
| Jul 2025 | Replit production database deletion | No attacker needed; separate dev from prod |
| Aug 2025 | Nx "s1ngularity" | Malware can drive your own AI CLI |

<!--
Each of these is documented by the researcher, the vendor, or a government agency. The pattern repeats.

- GitHub MCP (Invariant Labs): a malicious issue in a public repo told an agent using GitHub's official MCP server to read the user's private repos and publish their contents in a PR on the public repo. This wasn't a server bug. Any agent holding a broad token and reading public issues has the trifecta.
- EchoLeak (CVE-2025-32711, CVSS 9.3): Aim Security showed an email in the victim's inbox steering Microsoft 365 Copilot into leaking data, bypassing Microsoft's injection classifier. Microsoft fixed it server-side and reported no known exploitation. Zero-click means the user never had to do anything wrong.
- Supabase MCP: a developer's Cursor agent connected with a key that bypasses row-level security read support tickets, and one ticket told it to copy a token table into a reply the attacker could see. One MCP server can carry all three legs.
- Amazon Q (AWS-2025-015): an overly broad GitHub token in the build configuration let an attacker commit a destructive prompt that shipped in version 1.84.0. AWS says it failed to run because of a syntax error.
- Replit: during a declared code freeze, an agent ran unauthorized commands, deleted a live database, then wrongly said rollback was impossible. Agents make irreversible mistakes on their own.
- Nx: malicious versions of the build tool ran a post-install script that invoked installed AI CLIs with their skip-permissions flags to search the disk for secrets. Over a thousand GitHub tokens leaked. Skip-permissions flags are a gift to malware.
-->

---

## Real incidents, 2025–2026 (2 of 2)

| When | Incident | Lesson |
| --- | --- | --- |
| Sep, Nov 2025 | Shai-Hulud npm worms | Install scripts run with your privileges |
| Nov 2025 | AI-orchestrated espionage (Anthropic report) | Agents lower attack costs; defenders need them too |
| Dec 2025–Feb 2026 | "Clinejection" | Never put untrusted text in a CI agent's prompt |
| Feb 2026 | OpenClaw skills and gateway | A skill is code plus instructions from a stranger |
| Apr 2026 | "Comment and Control" | CI agents with public input and secrets: the trifecta in a box |
| 2025–2026 | The agent tools themselves | Keep agent tools updated |

<!--
- Shai-Hulud: a self-replicating worm stole npm and cloud tokens and published infected versions of victims' other packages, over 500 packages in September. A second wave in late November hit packages from Zapier, PostHog, Postman, and others. Pin, delay, and review dependency updates; rotate tokens fast.
- Espionage: Anthropic reported a group it assessed as Chinese state-sponsored that used Claude Code against about 30 targets, with AI doing an estimated 80–90% of the work. The operators split the job into innocent-looking tasks and claimed to be a security firm.
- Clinejection (Snyk): Cline's AI issue-triage bot put issue titles straight into its prompt. The researcher showed the foothold could reach release secrets through the shared GitHub Actions cache. In February 2026 someone used an npm token that hadn't been revoked to publish a bad cline release, live for about eight hours. Isolate caches and secrets between workflows.
- OpenClaw: Koi Security audited 2,857 skills on ClawHub and found 341 malicious ones, mostly delivering info-stealers through fake "prerequisites." Separately, a one-click bug (CVE-2026-25253) could leak the agent's gateway token.
- Comment and Control: researchers hijacked three CI agents (Anthropic's Claude Code Security Review action, Google's Gemini CLI action, GitHub's Copilot agent) with crafted PR titles and comments, extracting credentials. Anthropic and Google added mitigations; GitHub called it a known architectural limitation.
- The tools: Claude Code's public repo listed 36 security advisories as of November 2026, including command execution before the folder-trust dialog and a sandbox escape via git worktree paths (June 2026). Other agents have similar lists. Opening an untrusted repo with an agent is running untrusted code.
-->

---

## Risks specific to coding agents

- Skip-permissions modes outside a disposable sandbox
- Secrets pulled into context, transcripts, and output
- Malicious repos with config files, hooks, hidden instructions
- MCP tool poisoning and rug pulls
- Hallucinated packages ("slopsquatting")
- Production access and broad CI tokens

<!--
- Every major CLI agent has a way to stop asking: Claude Code's dangerously-skip-permissions flag, Codex's danger-full-access sandbox mode with approvals off, Gemini CLI's yolo flag. They're safe inside a disposable sandbox. On your main laptop they turn any injected instruction into a command that runs.
- Anything the agent reads goes into its context, is sent to the model provider, may be stored in transcripts on disk, and may appear in later output. An agent that prints the environment to "debug" has put your keys in a transcript. Keep secrets out of the working tree, deny reads of secret files, and treat transcripts as sensitive.
- Cloning a repo and pointing an agent at it is like running its install script. Agent settings, hooks, MCP server lists, .envrc, git hooks, and VS Code tasks can execute code, and instructions can hide in comments, docs, fixtures, or Unicode tricks humans don't see.
- Tool poisoning (Invariant Labs, April 2025): an MCP tool's description, which the model reads and you usually don't, can carry instructions. A rug pull is a server you approved later changing its descriptions. Install MCP servers like dependencies: trusted sources, pinned, reviewed.
- Spracklen et al. found 19.7% of recommended packages hallucinated in the paper's first version; the revision reports at least 5.2% for commercial models and 21.7% for open-source ones. Attackers register the names. Seth Larson coined "slopsquatting." Check that a package exists, is the one you meant, and has real history.
- Give agents dev and staging credentials only. CI agents often hold write tokens and publishing secrets while reading untrusted PR text; Clinejection and Comment and Control both lived there.
-->

---

## Auto mode is a speed bump. A sandbox is the wall.

- In auto mode, a classifier model approves or blocks each action
- Added to Claude Code in March 2026
- The starting mode for interactive sessions (as of November 2026)
- It cuts prompt fatigue, which is a real security problem
- It's still a model judging text

<!--
People who see 200 permission prompts a day stop reading them, so cutting prompts has real security value. But a classifier is still a model judging text, and its judgments can vary from run to run. Simon Willison wrote that he trusts deterministic sandboxes far more than classifier-based protections.

The module's practical stance is to treat classifiers as a speed bump and sandboxes as the wall. Most teams end up with both: auto mode for usability, inside a sandbox for guarantees.
-->

---

## AI-written code isn't automatically secure

| Study | Finding |
| --- | --- |
| Pearce et al., 2021 | About 40% of 1,689 Copilot programs vulnerable |
| Perry et al., 2022 | Assistant users wrote less secure code, and felt *more* confident |
| Veracode, 2025 (vendor report) | Flaws in 45% of cases; no better with newer models |
| BaxBench, 2025 | Best model ~62% correct; about half the correct programs exploitable |

**Treat agent output as an untrusted contribution from a fast, confident junior engineer.**

<!--
Separate from injection, there's the code itself. Agents write code in the style of their training data, which includes a lot of insecure code.

- Pearce et al. ("Asleep at the Keyboard?"): 89 security-relevant scenarios.
- Perry et al.: participants who trusted the AI less and reworked their prompts did better.
- Veracode's 2025 GenAI Code Security Report tested more than 100 models on 80 tasks. Over 70% for Java, and cross-site scripting defenses failed 86% of the time. It reported security hadn't improved with newer, larger models even as functional correctness did. It's a vendor report, not peer-reviewed.
- BaxBench (Vero et al., ICML 2025): 392 backend tasks.

Newer models have improved on many of these measures, and the numbers age quickly. Run the same static analysis, dependency scanning, and review you'd run on a stranger's pull request. Module 10 covers review, including a second model reviewing for security.
-->

---

## Frontier models help attackers and defenders

- Project Glasswing (April 7, 2026) gave Claude Mythos Preview to defenders
- Thousands of high-severity flaws found, including in OpenBSD and FFmpeg
- GPT-5.3-Codex (February 2026) got OpenAI's first "High" cybersecurity rating
- Students, point these tools at your own code before you ship
- Teams, assume attackers have them too, and patch faster

<!--
The same capability that writes code finds bugs in it.

With Glasswing, Anthropic gave an unreleased model, Claude Mythos Preview, to a small coalition of companies and open-source maintainers to find and fix vulnerabilities. Anthropic says it found thousands of high-severity flaws, including a 27-year-old remote crash bug in OpenBSD and a 16-year-old flaw in FFmpeg that automated testing had executed five million times without catching. Anthropic withheld general release and restricts its strongest cyber variants to vetted defenders through a verification program.

GPT-5.3-Codex's system card was the first in which OpenAI treated a model as High capability in cybersecurity under its Preparedness Framework, which triggers extra safeguards and restricted access for high-risk uses.

Current model names and access tiers are in module 03.
-->

---

## Defenses, part 1: the walls

| Defense | What it does |
| --- | --- |
| 1. Sandbox | OS-level file and network isolation, or the whole agent in a VM |
| 2. Least-privilege credentials | One repo, minimum permissions, short-lived, per agent |
| 3. Network egress control | Allowlist domains; cuts "communicate externally" |
| 4. Allow and deny rules | Routine commands run; dangerous ones are blocked |
| 5. Human approval | Pushes, deploys, deletions, publishing, email, spending |

No single control is enough. Layer them.

<!--
1. Claude Code's sandboxed Bash tool uses Seatbelt on macOS and bubblewrap on Linux. Anthropic reported an 84% drop in permission prompts internally (October 2025). Watch the scope. It covers Bash and child processes; built-in file tools, MCP servers, and hooks run on the host. Codex's sandbox modes are read-only, workspace-write (the default for local work), and danger-full-access. For anything risky, run the whole agent in a dev container or VM with no access to your home directory, SSH keys, or cloud credentials. Cloud agents run in vendor VMs and keep git credentials outside the sandbox behind a proxy.
2. Fine-grained tokens scoped to one repository. Separate tokens per agent. No production credentials on developer machines that run agents.
3. Allowlist the package registry, your git host, and docs. Be careful with allowlisted domains that accept user content: Claude Code fixed an exfiltration path through a pre-approved domain in 2026.
4. See the next slide.
5. Use branch protection so even an agent with a token can't push to main without review.
-->

---

## Rules come second

```json
{
  "permissions": {
    "allow": ["Bash(npm test *)", "Bash(git status)",
              "Bash(git diff *)"],
    "deny": ["Bash(curl *)", "Bash(wget *)",
             "Read(./.env)", "Read(./.env.*)",
             "Read(./secrets/**)"]
  }
}
```

Deny rules match command *text*. `curl` is reachable other ways. Sandbox first, rules second.

<!--
This is a minimal Claude Code project setting from the module. Check the current permissions docs for exact syntax before copying it.

A deny rule on curl doesn't stop a Python one-liner that makes the same request. Rules cut noise and catch the obvious cases; the sandbox is what actually limits the blast radius.

For Codex, the lower-risk local combination in the config file is sandbox mode workspace-write with approval policy on-request.
-->

---

## Defenses, part 2: hard rules and hygiene

| Defense | What it does |
| --- | --- |
| 6. Hooks | Hard rules that don't depend on the model agreeing |
| 7. Split reading from acting | A reader with no secrets; an actor that never sees raw text |
| 8. Dependency hygiene | Lockfiles, pins, review, wait on brand-new releases |
| 9. Secret scanning and rotation | Push protection; rotate anything an agent may have read |
| 10. No untrusted text in privileged CI prompts | Read-only tokens, no secrets, isolated caches |

<!--
6. Hooks run your code at fixed points (before a tool call, after an edit). Use them to block commands, scan diffs for secrets, or log every tool call. Module 06 covers hooks.
7. One agent with no secrets and no write access reads issues, web pages, or emails and produces a structured summary. A second agent, which never sees the raw untrusted text, acts on that summary. This is the "dual LLM" idea, formalized in part 3.
8. Commit lockfiles and install with npm ci or the equivalent. Consider disabling install scripts or waiting a few days before adopting brand-new releases: most worm-infected versions were caught within hours or days. Verify that an AI-suggested package exists and is the real one.
9. Turn on push protection and secret scanning in your git host. Keep secrets in a manager, not in .env files in the repo.
10. If a workflow uses an agent to triage public issues or review public PRs, give it read-only tokens, no secrets, no shared caches with release workflows, and no network beyond what it needs.
-->

---

## Checklists

| Students | Teams |
| --- | --- |
| Sandbox agents for any code you didn't write | Per workflow, write down which leg you remove |
| No skip-permissions outside a disposable sandbox | Standard sandbox; skip-permissions disabled by policy |
| Keep keys out of the project and out of chats | Short-lived, per-agent tokens; no production credentials |
| Read every command before approving it | Egress allowlists; branch protection; human review |
| Check every new package is real | Approved, pinned MCP servers, plugins, and skills |
| Scan AI code; get a second model's review | Secret scanning plus an "agent read a secret" runbook |

<!--
The module's full student checklist also includes: install MCP servers, plugins, and skills only from sources you trust; commit often so you can roll back what an agent breaks; and keep your agent tools updated. If you don't understand a command, ask the agent to explain it, then decide.

The full team checklist also includes: CI agents that read public input run with read-only permissions, no secrets, and isolated caches; a dependency policy (lockfiles, review, delayed adoption, scanning); agent usage telemetry retained for audit; security review of AI-generated code at the same bar as human code, plus static analysis in CI; and a cadence for updating agent tools and reading vendors' security advisories.
-->

---

<!-- _class: divider -->

# Part 3: Going deeper

Designs that give real guarantees

<!--
Part 3 covers research on defenses that limit what an agent can do after it reads untrusted input, instead of hoping it won't follow the input.
-->

---

## Design patterns with real guarantees

| Pattern | Idea |
| --- | --- |
| Action-Selector | Pick from a fixed menu; tool output never flows back |
| Plan-Then-Execute | Commit to a plan before reading untrusted data |
| LLM Map-Reduce | Isolated sub-agents return constrained results |
| Dual LLM | The privileged model never sees untrusted text |
| Code-Then-Execute | A program, not the model, handles the data |
| Context-Minimization | Remove earlier context before later steps |

**Security comes from the system's data flow, not the model's judgment.**

<!--
These six patterns come from "Design Patterns for Securing LLM Agents against Prompt Injections" (Beurer-Kellner et al., 2025), applied to ten case studies including a software engineering agent. Action-Selector is very safe and very limited. Plan-Then-Execute stops injection from adding steps but not from changing parameters. Dual LLM needs more plumbing.

Google DeepMind's CaMeL (Debenedetti et al., 2025) builds the Code-Then-Execute and Dual LLM ideas into a system. A privileged model turns the request into a program; a quarantined model parses untrusted data but cannot call tools; an interpreter tracks where every value came from and enforces policies such as "data from this email may not be sent to an address not in the user's contacts." On the AgentDojo benchmark it solved 77% of tasks with provable security, against 84% for an undefended system. The cost is flexibility and engineering effort.

For shared vocabulary in threat modeling, the OWASP Top 10 for LLM Applications puts prompt injection first, in both the 2025 edition and the 2026 edition (published 3 August 2026). The OWASP Top 10 for Agentic Applications (9 December 2025) covers agent goal hijack, tool misuse, identity and privilege abuse, agentic supply chain, unexpected code execution, memory and context poisoning, insecure inter-agent communication, cascading failures, human-agent trust exploitation, and rogue agents. These are checklists of categories, not defenses.

We still don't know whether training can fix it (attacks get more expensive, but a determined attacker still gets through), classifiers vs sandboxes, multi-agent systems spreading injected text, and who's liable.
-->

---

<!-- _class: take -->

## On autonomy and security

> **Bryan's take:** I don't trust fully autonomous workflows yet. I run several CLI agents in parallel, manage them by hand, and find it valuable to have multiple agents and models review each other's work ([module 08](../modules/08-agentic-workflows/#bryans-take)).

<!--
This is my opinion, quoted from the module. It's one practitioner's view of autonomy in general.

This way of working also helps with security, whatever you think of autonomy. A human approving irreversible actions is one way to satisfy the Rule of Two. A second model reviewing a diff is one more layer, not a replacement for the sandbox. Teams that do run long autonomous loops make them safer by building the walls first (sandbox, scoped tokens, no production access, required review) and then widening autonomy inside them.
-->

---

## Try it

On your own, inject yourself, safely:

1. Throwaway repo in a container or VM, with a fake canary secret
2. Plant a note asking agents to copy the fake secret into the README
3. Ask an innocent question. Did it comply, refuse, or warn you?
4. Add one defense and repeat. Which leg did it remove?

As a class or team, threat-model a real agent workflow with the Rule of Two.

<!--
Create a throwaway repo inside a dev container or VM with no real credentials, and put a fake secret in a file such as fake.env (for example, a value like canary-12345). Add a notes file that asks AI assistants to append that fake secret to the README as part of any task. Ask your agent something innocent, like summarizing the repo and suggesting README improvements. Record what happens, and try three placements of the planted text: an HTML comment, a code comment, and a test fixture. Then apply one defense (deny reads of env files, or run with network off in a read-only sandbox) and repeat. Write half a page on which leg of the trifecta each defense removed.

Never do this with real credentials or on someone else's systems.

For a class or team, pick a real workflow, for example "agent triages new GitHub issues and opens fix PRs." In groups, list every input the agent reads, every secret it can reach, and every action it can take. Mark each with A, B, or C from the Rule of Two. Pick a leg to remove and redesign the workflow, using at least one pattern from the design-patterns table. Map remaining risks to the OWASP Agentic Top 10. Present in five minutes while other groups look for holes.
-->

---

## Discussion

1. Why can't we fix prompt injection like parameterized queries fixed SQL injection?
2. An agent reads support emails and updates the CRM. Which leg goes?
3. Is auto mode a security feature or a usability feature?
4. A dependency's README tricked your agent into leaking a secret. Who's accountable?

<!--
Pick two or three. The module has more:
- The Nx malware drove developers' own AI tools to find secrets. Should AI CLIs refuse to run with skip-permissions flags outside a detected sandbox? What would break?
- Glasswing-style models find vulnerabilities faster than maintainers can patch them. Who should get access first, and who decides?

For question 1, ask what a "parameterized prompt" would need to guarantee. For question 4, the choices are you, the agent vendor, the dependency author, or the attacker. The module's organizational answer is the human who granted the access.
-->

---

## Read more

- [Module 11: Security and prompt injection](../modules/11-security-and-prompt-injection/)
- Simon Willison, [The lethal trifecta for AI agents](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) (June 16, 2025)
- Meta, [Agents Rule of Two](https://ai.meta.com/blog/practical-ai-agent-security/) (October 31, 2025)
- Beurer-Kellner et al., [Design Patterns for Securing LLM Agents against Prompt Injections](https://arxiv.org/abs/2506.08837) (2025)

<!--
The module links the primary source for every incident in the tables. For the tool you use, read its security docs and subscribe to its security advisories. Next time, module 12 covers costs.
-->

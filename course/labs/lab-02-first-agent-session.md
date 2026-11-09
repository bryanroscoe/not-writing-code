# Lab 2: Your first agent session

> **Course:** [syllabus](../syllabus.md), week 3 (due week 4) · **Tier:** AI-accelerated · **Time:** about 3 hours · **Last verified:** 2026-11-08

## Goal

Install and configure one CLI coding agent, learn its permission modes, measure what fills its context, and make one small change that is tested, reviewed by you, and committed. By the end you should be able to say what the harness did that the model alone couldn't ([module 06](../../modules/06-harnesses-and-tools.md#what-a-harness-is)).

**Tier note.** The agent may write the code. Your reflection, AI log, and commit messages are yours. You must be able to explain every line you commit.

## Prerequisites and setup

- **One CLI coding agent on a subscription plan.** For example, Claude Code on a Claude Pro plan or Codex CLI on a ChatGPT Plus plan ([module 12](../../modules/12-costs-subscriptions-and-apis.md#price-snapshot-as-of-2026-11-08)). Install it from the vendor's official docs. **Sign in with your subscription. Don't create or paste an API key;** API billing is pay-per-token and isn't needed for any lab.
- **Check your data setting** before the first session. Decide whether your sessions may be used for training ([module 15](../../modules/15-learning-careers-and-responsibility.md#data-privacy-what-not-to-paste)).
- Git, an editor, and Python 3 or Node.js.
- **A small repository** with a few tests: the instructor's starter `[link to Lab 2 starter repository]`, or a small program you wrote yourself. Not someone else's coursework, and nothing containing secrets, credentials, or other people's data.
- Windows users: work inside WSL.

## Background reading

- [Module 06](../../modules/06-harnesses-and-tools.md): [What a harness is](../../modules/06-harnesses-and-tools.md#what-a-harness-is), [Tools: how a model "does" things](../../modules/06-harnesses-and-tools.md#tools-how-a-model-does-things), [The rest of the harness toolkit](../../modules/06-harnesses-and-tools.md#the-rest-of-the-harness-toolkit), [A sane baseline setup](../../modules/06-harnesses-and-tools.md#a-sane-baseline-setup), [Common failure modes](../../modules/06-harnesses-and-tools.md#common-failure-modes)
- [Module 07](../../modules/07-context-engineering.md): [Prompting basics that still matter](../../modules/07-context-engineering.md#prompting-basics-that-still-matter), [What actually fills an agent's context window](../../modules/07-context-engineering.md#what-actually-fills-an-agents-context-window), [Current best practice](../../modules/07-context-engineering.md#current-best-practice) for instruction files
- [Module 08](../../modules/08-agentic-workflows.md): [Small diffs, git as the safety net, checkpoints](../../modules/08-agentic-workflows.md#small-diffs-git-as-the-safety-net-checkpoints)
- [Module 11](../../modules/11-security-and-prompt-injection.md): [Student checklist](../../modules/11-security-and-prompt-injection.md#student-checklist)

## Instructions

### 1. Prepare the repository (10 minutes)

```bash
git clone <starter-or-your-repo> lab2 && cd lab2
git switch -c lab2
git status          # should be clean
```

Run the tests yourself first and record the command and result. If you can't run them, you can't check the agent's claims about them either.

### 2. Install, sign in, and record versions (15 minutes)

Follow the vendor's install instructions. Record the tool's version (for example `claude --version` or `codex --version`), the plan, and the default model. You'll need these in every lab, because behavior changes between versions ([module 14](../../modules/14-keeping-up.md#is-it-the-model-the-task-or-the-harness)).

### 3. Learn the permission modes before you use them (20 minutes)

Read your harness's permission and sandbox documentation. Write a short table in your submission: each mode, what it allows without asking, and when you'd use it. As of November 2026, for example:

- **Claude Code** has a mode that asks before risky actions, a **plan mode** that reads and proposes but makes no edits until you approve (`Shift+Tab` until the status bar shows it), and an **auto mode** in which a separate classifier approves or blocks each action. Auto mode was the starting mode for interactive sessions as of November 2026 ([module 08](../../modules/08-agentic-workflows.md#the-core-loop-explore--plan--implement--verify--commit), [module 11](../../modules/11-security-and-prompt-injection.md#risks-specific-to-coding-agents)).
- **Codex** has sandbox modes `read-only`, `workspace-write`, and `danger-full-access`, plus an approval policy ([module 11](../../modules/11-security-and-prompt-injection.md#practical-defenses)).

Check the current docs; names and defaults change. **Rules for this lab:** work in a mode that asks you before it edits files or runs commands, so you see every action; if your harness starts in an auto-approve mode, switch. No skip-permissions or "YOLO" modes; those are for disposable sandboxes only ([module 11](../../modules/11-security-and-prompt-injection.md#student-checklist)).

### 4. Measure the empty context (10 minutes)

Start a session in the repository. Before typing anything, open the context breakdown (in Claude Code, `/context`; other harnesses have a similar view, or check the docs). Record how many tokens go to the system prompt, tool definitions, and instruction files. Save it as `context-before.txt` or a screenshot.

Most people are surprised by how much is used before they type a word ([module 07](../../modules/07-context-engineering.md#what-actually-fills-an-agents-context-window)).

### 5. Explore, read-only (25 minutes)

Give a read-only exploration prompt, in the shape [module 08](../../modules/08-agentic-workflows.md#the-core-loop-explore--plan--implement--verify--commit) recommends:

```text
Read this repository. Don't change anything yet.
Explain the architecture, how to run the tests, and anything that looks
surprising or fragile. Cite file paths and line numbers for each claim.
```

While it works, note each tool call it makes (reads, searches, commands). Then **check two of its claims** by opening the cited files yourself. Record whether each claim was right. Agents sometimes describe files they never opened ([module 01](../../modules/01-what-is-an-llm.md#failure-modes-you-will-see-and-the-fix)).

Open the context view again. Save it as `context-after.txt`. How much did exploration add, and which component grew most?

### 6. Write a short instruction file by hand (15 minutes)

Create `AGENTS.md` (or `CLAUDE.md` if your tool reads only that) with **no more than 20 lines**, written by you:

- The exact commands to install, run all tests, run one test file, and lint.
- One or two things the code won't tell an agent.
- What "done" means for a change in this repository.

Ask of every line: "Could the agent figure this out by reading the repository?" If yes, delete it ([module 07](../../modules/07-context-engineering.md#current-best-practice)). Commit it:

```bash
git add AGENTS.md && git commit -m "docs: add short agent instructions"
```

### 7. Make one small, tested change (40 minutes)

Pick something small: input validation, a missing edge case, a new flag, a small bug. Write a task prompt that names the outcome, the reason, the check, and the scope. Adapt this example from [module 07](../../modules/07-context-engineering.md#prompting-basics-that-still-matter):

```text
<Function or command> fails when <specific input> because <what you saw>.
First write a failing test in <test file> that reproduces it. Run it and
show me the failure. Then fix the root cause without modifying the test.
No new dependencies. Done means: the new test passes, the full test suite
passes, and you explain the root cause in two sentences. If you can't
reproduce it, stop and tell me.
```

Use plan mode or ask for a plan first if your harness supports it. Approve each action deliberately. Ask for the commands it ran and their output, not "all tests pass."

### 8. Review the diff yourself (20 minutes)

```bash
git diff --stat      # what did it actually touch?
git diff             # read every line
git add -p           # stage hunk by hunk, reading as you go
```

Pick one line you're least sure about and ask the agent to explain it. Then decide whether to keep it. Reject any change outside the scope you gave. Run the tests yourself and record the output.

Commit with a message you write. If your tool adds a co-author trailer, leave it on ([module 15](../../modules/15-learning-careers-and-responsibility.md#attribution-and-disclosure-in-commits-and-prs)).

### 9. Practice undo (15 minutes)

Ask the agent for a throwaway change, such as renaming a variable across two files. Then undo it twice:

1. With the harness's checkpoint feature, if it has one (in Claude Code, `/rewind` or `Esc` twice).
2. With git: `git restore .` (or `git restore --source=HEAD -- <path>`).

Note the limit from [module 08](../../modules/08-agentic-workflows.md#small-diffs-git-as-the-safety-net-checkpoints): checkpoints cover only files the agent changed with its own edit tools, not changes made through shell commands. Git is the real safety net.

### 10. Reflect (20 minutes)

Half a page, in your own words:

- What did the harness do that the model alone couldn't? Name specific tool calls.
- Which component of the context grew most, and what does that mean for long sessions?
- One claim the agent made that was wrong or unverified, and how you found out.
- Which permission mode you'll use by default next week, and why.

Add at least three entries to `surprised-me.md`.

## What to submit

- A link to your repository (or a zip) with the `lab2` branch: the `AGENTS.md` commit, your change and its test, and your commit messages.
- Your permission-modes table and tool version information.
- `context-before.txt` and `context-after.txt` (or screenshots).
- The exploration transcript excerpt, with your notes on the two claims you checked.
- Test output from before and after your change, run by you.
- The reflection, the updated `surprised-me.md`, and your [AI log](../syllabus.md#ai-log-template).

## Grading rubric

| Criterion | Points | Full credit means |
| --- | --- | --- |
| Setup and permissions | 15 | Subscription sign-in (no API key); versions recorded; permission table accurate for your tool; no skip-permissions mode used |
| Context measurement | 15 | Before and after breakdowns captured and interpreted |
| Exploration checked against the code | 20 | Read-only prompt; tool calls noted; two claims checked against the files, with results |
| The change | 25 | Failing test first, with output; small diff in scope; root cause explained; full suite run by you |
| Review and undo | 10 | Diff read and staged hunk by hunk; one line questioned; both undo methods practiced |
| Instruction file | 5 | 20 lines or fewer, written by you, nothing discoverable from the code |
| Reflection and logs | 10 | Specific answers; three surprise entries; complete AI log |
| **Total** | **100** | |

## If you finish early

These come from [module 06's Try it](../../modules/06-harnesses-and-tools.md#try-it):

- **Connect one MCP server** you'd actually use (for example GitHub or Playwright) and measure how many context tokens it adds. Disconnect it afterward if you won't use it this week.
- **Add a formatter hook** that runs after every edit, and confirm it fires.
- **Write a `Stop` hook** that blocks "done" until the tests pass. Give the agent a task that breaks a test and watch the hook push it back.
- **Read a 30-line agent loop** in [module 13](../../modules/13-open-source-ecosystem.md#framework-or-just-a-loop) and map each part to the harness table in [module 06](../../modules/06-harnesses-and-tools.md#what-a-harness-is).

## Instructor notes

- **API keys by accident.** Some students will sign in with an API key and get billed per token. Check the sign-in method in the setup clinic.
- **Windows.** Native Windows support varies by tool. Steer students to WSL early.
- **Students who already use agents** may skip the reading-the-diff step out of habit. Grade it. Ask them to show you the `git add -p` session in a walkthrough.
- **Unchecked claims.** The most common weak submission says "the agent explained the architecture" with no verification. The two-claim check is the point of step 5.
- **Auto modes.** If a student's harness starts in an auto-approve mode, they should still be able to explain what the classifier allowed. Classifiers are a speed bump, not a sandbox ([module 11](../../modules/11-security-and-prompt-injection.md#risks-specific-to-coding-agents)).
- **Quota.** In your dry run, record how much of a $20 plan's limit this lab used. If students hit limits, the usual cause is a long, unfocused session; suggest `/clear` or a fresh session between steps 5 and 7.

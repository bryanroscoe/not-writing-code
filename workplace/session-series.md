# Internal training series: from "what is an LLM?" to parallel agents

This series is for the champions who will facilitate it and the leads who will schedule it, and takes about 40 minutes to read. It's Phase 2's training in the [playbook](ai-first-playbook.md) and pairs with the [objections guide](objections.md).

*Last checked November 8, 2026.*

**TL;DR**
- Eight sessions of 45–60 minutes, lunch-and-learn style. Session 0 is a demo-first pitch for skeptics. Sessions 1–7 go from what an LLM actually is to running agents in parallel and reviewing their work with a different model.
- Every session has a goal, a short pre-read from the modules, a timed agenda, a live demo script, a takeaway checklist, and a hands-on exercise on your own repository.
- Demos run live on real code from your backlog. When the agent fails, that's part of the lesson, so narrate the recovery.
- Run only on approved tools under your team's policy. Finish Phase 0 of the playbook first.

## How the series works

### Format

| Item | Recommendation |
| --- | --- |
| Length | 45–60 minutes per session. Timings below assume 60; trim the hands-on part to fit 45 |
| Cadence | Weekly, or every other week. Leave time between sessions to practice on real work |
| Group size | 6–20. Hands-on parts work in pairs or groups of three |
| Facilitators | One champion leads; a second champion helps people get unstuck during hands-on parts |
| Prerequisites | Everyone has an approved, paid seat and has read the team's AI policy ([policy template](policy-template.md)) |
| Materials | A projector with a large terminal font, the team repository, a scratch branch or worktree, and the pre-reads |
| Recording | Optional. Recordings capture code and terminal output, so follow your data policy |

### Ground rules for facilitators

1. Demo live, on small real tasks from your backlog. Use a toy project for security exercises, and keep a recorded fallback for outages.
2. Rehearse, then reset. Do a dry run the day before in a throwaway worktree, then throw it away. The model's output will differ on the day, and that's fine.
3. Show failure. At least once per session, show the agent getting something wrong and how a check caught it.
4. Don't hype or promise speedups. Quote the [evidence](ai-first-playbook.md#how-to-measure) accurately, and say "I don't know" when you don't.
5. Keep real credentials out of the demo environment, and check your shell history and environment before you share your screen.
6. Write every objection on the board. Answer it from the [objections guide](objections.md) or add it to the objections log.

### The series at a glance

| # | Session | Goal | Main pre-read |
| --- | --- | --- | --- |
| 0 | [Watch it work on our code](#session-0-watch-it-work-on-our-code) | Show skeptics a real fix on real code, honestly | None, on purpose |
| 1 | [What an LLM actually is](#session-1-what-an-llm-actually-is) | A mental model that explains hallucination, sycophancy, and nondeterminism | [Module 01](../modules/01-what-is-an-llm.md) |
| 2 | [Harnesses, permissions, and a safe setup](#session-2-harnesses-permissions-and-a-safe-setup) | Everyone leaves with the team's standard, safe configuration | [Module 06](../modules/06-harnesses-and-tools.md) |
| 3 | [Context: prompts that define done, and our instruction file](#session-3-context-prompts-that-define-done-and-our-instruction-file) | Write tasks agents can succeed at; agree on a short shared instruction file | [Module 07](../modules/07-context-engineering.md) |
| 4 | [The core loop: explore, plan, test, verify, commit](#session-4-the-core-loop-explore-plan-test-verify-commit) | Run the loop that holds up in daily use | [Module 08](../modules/08-agentic-workflows.md) |
| 5 | [Reviewing AI-written code](#session-5-reviewing-ai-written-code) | Review in layers, verify findings, use a second model | [Module 10](../modules/10-ai-code-review.md) |
| 6 | [Security, data, and cost](#session-6-security-data-and-cost) | Know the real risks, the team's controls, and what work costs | [Modules 11](../modules/11-security-and-prompt-injection.md) and [12](../modules/12-costs-subscriptions-and-apis.md) |
| 7 | [Parallel agents and cross-model review](#session-7-parallel-agents-and-cross-model-review) | Run two agents at once safely, and know where autonomy stops | [Modules 08](../modules/08-agentic-workflows.md) and [09](../modules/09-multi-agent-systems.md) |

If you're short on time, a four-session track covers most of it: Session 0, then Sessions 1 and 3 combined (mental model plus context), then Sessions 4 and 5 combined (loop plus review), then Sessions 6 and 7 combined (security, cost, and parallel work). Expect less hands-on time.

### A facilitator's prep checklist (every session)

- [ ] Pick the demo task from the real backlog: small, reproducible, one to three files, with tests nearby.
- [ ] Create a fresh worktree or branch for the demo. Confirm it contains no secrets.
- [ ] Dry-run the demo once, then reset the worktree.
- [ ] Prepare a fallback: a transcript or recording of the dry run, in case the network or the vendor has a bad day.
- [ ] Turn off notifications. Set the terminal font large.
- [ ] Check that every attendee's tool works before the hands-on part (a two-minute message the day before saves ten minutes in the room).
- [ ] Bring the takeaway checklist as a handout or a link.

## Session 0: Watch it work on our code

Use a demo with almost no slides to show skeptics what the tool can and can't do.

**Goal.** Show, on your own code, what a supervised coding agent does well, where it fails, and how an engineer stays in charge. Leave people curious enough to try it on one real task.

**Audience.** Everyone, especially people who tried AI tools in 2024 and gave up. Invite your most respected skeptic personally.

**Pre-read.** None. Let people see the demo before asking them to do any reading.

**Prep.** Choose a real, small bug from the backlog that you have reproduced but not fixed. It should have a clear symptom, live in one to three files, and have a test suite nearby. Also pick a second task you expect the agent to struggle with.

### Agenda (60 minutes)

| Time | Segment |
| --- | --- |
| 0:00–0:03 | **Framing.** One sentence, no slides |
| 0:03–0:18 | **Demo 1:** a real bug, fixed live with the full loop |
| 0:18–0:26 | **Demo 2:** an independent review by a different model |
| 0:26–0:40 | **Hands-on: the skeptic drives** |
| 0:40–0:44 | **The one slide:** what the evidence actually says |
| 0:44–0:56 | **Objections,** open floor |
| 0:56–1:00 | **What happens next** |

### Demo script

**Framing (say this, roughly):**
> "I'm not going to show you slides about how AI changes everything. I'm going to take a real bug from our backlog and try to fix it, live, with a coding agent. Your job is to catch it doing something wrong. If it does, that's useful too. I'll show you how we'd catch it in real life."

**Demo 1: the full loop (15 minutes).** Narrate every step, and point out each tool call as it happens.

1. Explore, read-only:
   ```text
   Read <the relevant directory> and its tests. Don't change anything yet.
   Explain how <the feature with the bug> works, and point to file and line
   for each claim. Tell me anything that looks surprising.
   ```
   Check one of its claims against the code, out loud.
2. Plan:
   ```text
   Here's the bug: <symptom from the ticket>. Propose a plan before you write
   any code. Smallest change that fixes it. No new dependencies.
   ```
   Edit the plan in front of the room, even slightly, and say why.
3. Test first:
   ```text
   Write a failing test that reproduces the bug. Run it and show me the failure.
   Don't change any existing tests.
   ```
4. Fix and verify:
   ```text
   Now make the test pass without modifying it. Then run the full unit suite,
   lint, and typecheck, and show me the output.
   ```
5. Show the evidence: `git diff --stat`, then the diff itself. Read it aloud.

**Demo 2: the independent review (8 minutes).** Open a fresh session, ideally with a second tool from a different lab, so the reviewer never saw the conversation.
```text
Review the diff on this branch against main. Focus on correctness and edge cases.
For each finding give file:line, a concrete failure scenario, and a severity.
Report only real problems. If you find nothing, say so.
```
Pick one finding and have the author agent write a test that demonstrates it. Either the test fails (real finding, fix it) or it can't be made to fail (dismiss it, and say why). This is the habit you most want people to leave with.

**Hands-on: the skeptic drives (14 minutes).** Hand the keyboard, or at least the prompts, to a volunteer, ideally a skeptic. They pick the second task, or any small task they're sure the agent will fail on. They dictate; you type. Before each step, ask the room to predict what will go wrong. When the agent drifts, show steering: press `Esc`, correct it once, and if two corrections fail, start a fresh session with a better prompt ([module 08](../modules/08-agentic-workflows.md#steering-a-session)).

If it fails, say what would have caught it: a test, the plan review, the independent reviewer. If it succeeds, ask the volunteer what they'd want to check before merging. Either outcome works.

**The one slide (4 minutes).** Three bullets, from [module 05](../modules/05-judging-models.md#real-world-productivity-evidence):
- In METR's 2025 randomized trial, experienced developers using early-2025 tools were 19% slower, while believing they were 20% faster.
- METR's 2026 follow-up with newer tools pointed to modest speedups with wide error bars, and METR calls it an unreliable signal.
- DORA's 2025 report says AI "amplifies what's already there." Teams with strong tests and review gain; teams without them get less stable.

Then say: "So I'm not going to promise you a number. We're going to build the habits and measure ourselves."

> **Bryan's take:** When I say vibe coding, I mean AI-accelerated coding, not really vibe coding: engineering with a human in charge, not blind acceptance of whatever the model produces.

**Objections (12 minutes).** Write every objection on the board. Answer the ones you can from the [objections guide](objections.md), and concede what's true first. Put the rest in the objections log with a promise to follow up.

**What happens next (4 minutes).** Cover the pilot or series schedule, how to get a seat, and the policy in one sentence: "approved tools only, no secrets or restricted data in prompts, a human approves every merge."

### Facilitator notes

- If the network or the vendor fails, switch to the dry-run transcript and say what happened. Outages are a real part of using these tools.
- Don't cut away from failures. A demo that only succeeds looks staged, and skeptics will assume it was.
- Don't oversell speed. Talk about what you checked, not how fast it was.

### Takeaway checklist (for attendees)

- [ ] I saw an agent explore, plan, test, fix, and get reviewed on our own code.
- [ ] I know the habit that matters most: give it a check it can run, and ask for the evidence.
- [ ] I know the evidence is mixed and that we'll measure ourselves.
- [ ] I've written down one task I'd like to try with an agent, and one I'm sure it would fail on.
- [ ] I know how to get a seat and where the policy lives.

## Session 1: What an LLM actually is

**Goal.** Give everyone a mental model that explains the behavior they'll see: why the model is confidently wrong sometimes, why it agrees with you, why it gives different answers on different runs, and why context matters.

**Pre-read (20 minutes).**
- [Module 00: Six ideas that outlast the hype](../modules/00-orientation.md#six-ideas-that-outlast-the-hype)
- [Module 01: TL;DR](../modules/01-what-is-an-llm.md) and [What an LLM is not](../modules/01-what-is-an-llm.md#what-an-llm-is-not)
- [Module 01: Hallucination](../modules/01-what-is-an-llm.md#hallucination-and-why-it-happens) and [Sycophancy](../modules/01-what-is-an-llm.md#sycophancy)
- Optional: [Module 01: A working mental model](../modules/01-what-is-an-llm.md#a-working-mental-model)

### Agenda (60 minutes)

| Time | Segment |
| --- | --- |
| 0:00–0:05 | Opening question: "When did an AI tool last surprise you, good or bad?" |
| 0:05–0:17 | Whiteboard talk: the next-token loop and what follows from it |
| 0:17–0:32 | Four short live demos |
| 0:32–0:55 | Hands-on: explain and verify, on our repository |
| 0:55–1:00 | Takeaways |

### Whiteboard talk (12 minutes)

Draw it; don't present slides. Cover five points, each with its practical consequence:

| What's true | So you should |
| --- | --- |
| It predicts the next token from everything in its context ([module 01](../modules/01-what-is-an-llm.md#the-one-idea-predict-the-next-token)) | Put the facts it needs in front of it |
| Its knowledge stops at a training cutoff, and it may not have seen your codebase | Give it current docs and let it read the code |
| It produces plausible text with no built-in notion of truth | Treat every claim as a hypothesis until a check confirms it |
| Training on human preferences makes it lean toward agreeing with you | Ask for critique, not approval |
| Output is sampled, so runs differ | Ask twice, or ask two models, when it matters |

Close with the line from module 00: "The model only knows what's in its context." Most of the rest of the series is about controlling that.

### Demo script (15 minutes)

1. **Different runs, different answers (3 minutes).** In three fresh sessions, ask the same open question about your codebase, such as "What's the riskiest part of `<module>`?" Show that the answers overlap but differ.
2. **Confident without context (4 minutes).** In a session with no repository access, ask: "What does the `<internal function name>` function in our codebase do, and what arguments does it take?" Record whether it guesses, asks for context, or declines. Then, in the repository, ask the same question and require a file path. Compare.
3. **Sycophancy (4 minutes).** Assert a wrong diagnosis with confidence: "I'm pretty sure the bug in `<feature>` is in the caching layer, right?" Show the agreement, if you get it. Then ask: "Argue the strongest case that I'm wrong. What evidence would show it?" Compare the quality of the two answers.
4. **What fills the context (4 minutes).** Open your harness's context view (in Claude Code, `/context`) before typing anything. Show how much is already used by the system prompt, tool definitions, and instruction files ([module 07](../modules/07-context-engineering.md#what-actually-fills-an-agents-context-window)).

Results vary from run to run and model to model. If a demo doesn't reproduce, say so, and explain what you expected and why. Discuss how nondeterminism affects the result.

### Hands-on: explain and verify (23 minutes)

In pairs, on your own repository:
1. Pick a module or service neither of you knows well.
2. Ask the agent to explain how it works, requiring a file path and line number for every claim.
3. Verify at least five claims against the code. Mark each one right, wrong, or unverifiable.
4. Ask one question that tempts it to agree with a wrong premise. Note what happened.
5. Each pair shares its most convincing wrong answer with the room.

### Takeaway checklist

- [ ] I can explain in two sentences why a model can be fluent and wrong.
- [ ] I ask for file paths and line numbers, and I check some of them.
- [ ] I put the facts the model needs into its context instead of trusting its memory.
- [ ] I ask for the strongest counter-argument before I accept a diagnosis.
- [ ] I've started a short "it surprised me" log: date, tool, task, what happened ([module 05](../modules/05-judging-models.md#vibes-are-data-too)).

## Session 2: Harnesses, permissions, and a safe setup

**Goal.** Understand that agent = model + harness, learn the permission system before raising autonomy, and leave with the team's standard, safe configuration installed.

**Pre-read (25 minutes).**
- [Module 06: What a harness is](../modules/06-harnesses-and-tools.md#what-a-harness-is)
- [Module 06: The rest of the harness toolkit](../modules/06-harnesses-and-tools.md#the-rest-of-the-harness-toolkit) (skim the table)
- [Module 06: A sane baseline setup](../modules/06-harnesses-and-tools.md#a-sane-baseline-setup)
- [Module 11: Risks specific to coding agents](../modules/11-security-and-prompt-injection.md#risks-specific-to-coding-agents), the first two paragraphs on skip-permissions modes and classifiers
- Your team's AI policy

### Agenda (60 minutes)

| Time | Segment |
| --- | --- |
| 0:00–0:05 | Agent = model + harness; why the same model behaves differently in different tools |
| 0:05–0:22 | Demo: watching the loop and its controls |
| 0:22–0:28 | MCP in six minutes |
| 0:28–0:55 | Hands-on: install and configure the team setup |
| 0:55–1:00 | Takeaways |

### Demo script (17 minutes)

1. **Watch the loop (5 minutes).** Ask: "Run the unit tests for `<module>` and summarize any failures." Point at each step: the model asks for a tool, the harness asks permission, the result goes back into context, the model decides what's next ([module 08](../modules/08-agentic-workflows.md#the-agent-loop)).
2. **Permissions (5 minutes).** Approve the test command once, then add it to the allowlist so it stops asking. Use a disposable demo directory containing only a fake `.env` canary, never a real secrets file. Then ask the agent to "show me the environment variables in `.env`" and show the deny rule blocking it. Explain why. Anything the agent reads goes to the provider and into transcripts. If it tries a shell command such as `cat .env` instead, deny that too, and point out that rules match specific tools and command text, so a sandbox comes first and rules second ([module 11](../modules/11-security-and-prompt-injection.md#practical-defenses)).
3. **Plan mode and checkpoints (4 minutes).** Switch to plan mode and ask for a small change. The agent reads and proposes, but edits nothing until you approve. Then make a small edit and rewind it with the harness's checkpoint feature. Note that checkpoints don't cover changes made by shell commands, so git is the real safety net ([module 08](../modules/08-agentic-workflows.md#small-diffs-git-as-the-safety-net-checkpoints)).
4. **Sandbox (3 minutes).** If your tool supports one, show a sandboxed command failing to reach a blocked network host. The rule is to turn on a sandbox before you turn off approvals ([module 06](../modules/06-harnesses-and-tools.md#a-sane-baseline-setup)).

### MCP in six minutes

- MCP is the open standard for plugging tools and data into any harness ([module 06](../modules/06-harnesses-and-tools.md#mcp-the-model-context-protocol)).
- Connect one approved server live and show its context cost in the context view. Fewer servers means less context spent and better tool choice.
- A tool's description is text the model reads and you usually don't, so install MCP servers like dependencies, from the approved list only ([module 11](../modules/11-security-and-prompt-injection.md#risks-specific-to-coding-agents)).

### Hands-on: the team setup (27 minutes)

Everyone, on their own machine, following the team's setup doc:
1. Install the approved tool and sign in with the company plan, not a personal account.
2. Confirm the plan and data settings the policy requires (training off, retention as specified).
3. Apply the team's managed or project settings: the allowlist for test and lint commands, deny rules for secret files, and the default permission mode.
4. Confirm skip-permissions modes are disabled outside a sandbox.
5. Run a read-only task: "Explain the directory structure of this repository and where tests live. Don't change anything."
6. Put the agent in plan mode on a small change, read the plan, and reject it. Practice saying no.
7. The helper facilitator walks the room and fixes setup problems. Note them for the setup doc.

### Takeaway checklist

- [ ] My agent runs on the company plan with the policy's required settings.
- [ ] Routine commands (tests, lint) are allowlisted; secrets are denied.
- [ ] I know how to use plan mode, and I've rejected at least one plan.
- [ ] I commit before each agent task so I can revert.
- [ ] I never use skip-permissions modes outside a sandbox.
- [ ] I install MCP servers, skills, and plugins only from the approved list.

## Session 3: Context: prompts that define done, and our instruction file

**Goal.** Write task prompts that give the agent a definition of done and a check to run. Agree on a short, shared instruction file for the team's main repository.

**Pre-read (25 minutes).**
- [Module 07: Prompting basics that still matter](../modules/07-context-engineering.md#prompting-basics-that-still-matter)
- [Module 07: The rise and fall of giant CLAUDE.md and AGENTS.md files](../modules/07-context-engineering.md#the-rise-and-fall-of-giant-claudemd-and-agentsmd-files), especially [Current best practice](../modules/07-context-engineering.md#current-best-practice)
- [Playbook: the starter team instruction file](ai-first-playbook.md#the-starter-team-instruction-file)

### Agenda (60 minutes)

| Time | Segment |
| --- | --- |
| 0:00–0:05 | Why context is most of the skill |
| 0:05–0:22 | Demo: bad prompt vs. good prompt; the spec interview |
| 0:22–0:28 | What the research says about instruction files |
| 0:28–0:53 | Hands-on: audit our instruction file |
| 0:53–1:00 | Agree on changes; takeaways |

### Demo script (17 minutes)

1. **Same task, two prompts (10 minutes).** Pick a small real bug. In two fresh sessions, side by side:
   ```text
   fix the <feature> bug
   ```
   ```text
   <Symptom, in one sentence, with the ticket number.>
   First reproduce it with a failing test in <test file>.
   Then fix the root cause. Don't change the public interface of <module>.
   Done means: the new test passes, the unit suite passes, and you explain
   the root cause in two sentences. If you can't reproduce it, stop and tell me.
   ```
   Compare the two. Did each write a test? How big is each diff (`git diff --stat`)? Did either ask a question? Which would you rather review?
2. **The spec interview (7 minutes).** For a fuzzier task:
   ```text
   I want to add <feature> but haven't thought it through. Interview me until
   you could write the spec, then write it to SPEC.md.
   ```
   Answer three or four of its questions live. Then point out Anthropic's advice to start a fresh session that builds from `SPEC.md`, so the build begins with a clean context and a written definition of done ([module 08](../modules/08-agentic-workflows.md#the-core-loop-explore--plan--implement--verify--commit)).

### What the research says (6 minutes)

- In an ETH Zurich study, LLM-generated context files didn't improve agent success and raised cost by about 20–23%. Developer-written files helped slightly, not significantly ([module 07](../modules/07-context-engineering.md#the-fall-late-20252026)).
- Instruction-following degrades as instructions pile up. In one benchmark, even the best models reached only 68% accuracy with 500 instructions.
- Agents follow the file's instructions, including incorrect ones.
- For every line, ask "Could the agent figure this out by reading the repository?" If so, delete it.

### Hands-on: audit our instruction file (25 minutes)

Use the draft from the pilot, or generate one with your harness's init command if none exists.
1. In groups of three, sort every line into the "where it belongs" table from the [playbook](ai-first-playbook.md#where-everything-else-goes): keep, hook, deny rule, linter config, skill, nested file, personal file, or delete.
2. Each group proposes one deletion and one addition, with a reason.
3. One group runs a small task twice in fresh sessions, once with the original file and once with the trimmed draft, records success, steps, and tokens used, and reports back.
4. The facilitator collects proposals into a single PR to review after the session.

### Takeaway checklist

- [ ] My task prompts name the symptom, the scope, and what "done" means, with a check to run.
- [ ] I ask for a failing test first on bugs.
- [ ] I use a spec interview, then a fresh session, for fuzzy tasks.
- [ ] I start a fresh session between unrelated tasks.
- [ ] I add a line to the instruction file only after correcting the agent on the same thing twice.
- [ ] Rules that must always or never happen go in hooks or deny rules, not in prose.

## Session 4: The core loop: explore, plan, test, verify, commit

**Goal.** Run the workflow that holds up in daily use, end to end, on a real ticket, and learn to steer a session that drifts.

**Pre-read (25 minutes).**
- [Module 08: The key fact: the loop stops when the model thinks it is done](../modules/08-agentic-workflows.md#the-key-fact-the-loop-stops-when-the-model-thinks-it-is-done)
- [Module 08: The core loop](../modules/08-agentic-workflows.md#the-core-loop-explore--plan--implement--verify--commit) and [Tests as the agent's contract](../modules/08-agentic-workflows.md#tests-as-the-agents-contract)
- [Module 08: Failure modes and counter-moves](../modules/08-agentic-workflows.md#failure-modes-and-counter-moves)
- [Module 08: A sample session](../modules/08-agentic-workflows.md#a-sample-session)

### Agenda (60 minutes)

| Time | Segment |
| --- | --- |
| 0:00–0:05 | The key fact: "Claude stops when the work looks done" |
| 0:05–0:25 | Demo: the full loop on a real ticket, with steering |
| 0:25–0:52 | Hands-on: pairs run the loop on real tickets |
| 0:52–1:00 | Debrief and takeaways |

### Demo script (20 minutes)

Use a different real ticket from Session 0, ideally a small feature rather than a bug.

1. **Explore, read-only (3 minutes).** "Read `<area>` and its tests. Don't change anything. Explain how it works and anything surprising."
2. **Plan (4 minutes).** Use plan mode and read the plan aloud. Find one thing to change: scope, a file it shouldn't touch, a missing test. This is the cheapest place to catch a wrong idea.
3. **Tests first (4 minutes).** "Write failing tests for the acceptance criteria. Run them and show me the failures." Commit the tests separately.
4. **Implement (4 minutes).** "Make the tests pass without modifying them. No new dependencies."
5. **Verify with evidence (3 minutes).** Ask for the commands and output. If it says "all tests pass" without showing them, say so and ask again. Then check the test diff: `git diff --stat main -- tests/`.
6. **Commit small (2 minutes).** Commit tests and implementation separately, and check the message.

When the agent drifts (and on a real ticket, it often will), show the steering rule from Anthropic's docs: watch the first minute, press `Esc` the moment it drifts, and after two failed corrections, start fresh with a better prompt instead of a third correction ([module 08](../modules/08-agentic-workflows.md#steering-a-session)).

### Hands-on: the loop on real tickets (27 minutes)

In pairs, on one small real ticket per pair (prepared in advance, one to three files each):
1. The driver runs the agent, and the navigator keeps a log of the five artifacts: the plan (and what you changed in it), the failing test output, the passing output, `git diff --stat`, and the commit.
2. Halfway through, swap roles.
3. At the end, the navigator reviews the diff against the [module 10 checklist](../modules/10-ai-code-review.md#how-humans-should-review-ai-written-prs), focusing on the test diff first.
4. Pairs that finish early ask a fresh session to review the branch and verify one finding.

### Debrief (8 minutes)

Ask each pair: Where did the agent drift? What did the plan review catch? Did it ever claim success without evidence? Did it touch a test? Note recurring problems as candidate lines for the instruction file, or candidate hooks.

### Takeaway checklist

- [ ] I explore read-only before the agent edits anything.
- [ ] I read and edit the plan before approving it.
- [ ] I write or approve failing tests first and commit them separately.
- [ ] I ask for the command and its output, not "done."
- [ ] I check the test diff on every change.
- [ ] After two failed corrections, I start a fresh session with a better prompt.

## Session 5: Reviewing AI-written code

**Goal.** Review in layers: the agent checks itself, an independent model reviews, and a human reviews intent, design, and risk. Verify every finding before acting on it. Practice cross-model review.

**Pre-read (25 minutes).**
- [Module 10: What they are good and bad at](../modules/10-ai-code-review.md#what-they-are-good-and-bad-at)
- [Module 10: A layered review workflow](../modules/10-ai-code-review.md#a-layered-review-workflow) and [Verify findings before acting](../modules/10-ai-code-review.md#verify-findings-before-acting)
- [Module 10: How humans should review AI-written PRs](../modules/10-ai-code-review.md#how-humans-should-review-ai-written-prs)
- [Module 09: Recipe 2: cross-model review](../modules/09-multi-agent-systems.md#recipe-2-cross-model-review)
- [Playbook: review policy for AI-written PRs](ai-first-playbook.md#review-policy-for-ai-written-prs)

**Prep (about an hour, the week before).** Build seeded-bug PRs from your own repository, as in [module 10's exercise](../modules/10-ai-code-review.md#try-it). Take a clean, merged PR of 100–300 lines. In a copy, plant five bugs: an off-by-one, a swallowed error, a missing authorization or permission check, a tautological test, and a dependency declaration with a misspelled (nonexistent) name, without a startup import. Install dependencies from the clean base lockfile before planting it; never install dependencies on the seeded branch. Check the registry in a browser instead. Make two or three variants so groups don't share answers. Keep an answer key.

### Agenda (60 minutes)

| Time | Segment |
| --- | --- |
| 0:00–0:05 | Why review is the bottleneck now |
| 0:05–0:20 | Demo: two reviewers from two labs on seeded PR A |
| 0:20–0:45 | Hands-on: humans, then bots, on seeded PR B |
| 0:45–0:55 | Reveal the answer key; compare layers |
| 0:55–1:00 | The team's review rule; takeaways |

### Demo script (15 minutes)

1. **Two reviewers (7 minutes).** Run a review on seeded PR A with your primary tool in a fresh session, and another with a tool from a different lab (for example, `/code-review` in Claude Code and `/review` in Codex, or a review bot on the PR). Use the same brief for both:
   ```text
   You are reviewing a change you did not write. Inputs: the diff against main
   and read-only access to the repository. For each finding give file:line,
   a concrete failure scenario, and severity (high/medium/low). Report only
   issues that would cause real harm. Skip style. If you find nothing, say so.
   ```
2. **Merge and triage (3 minutes).** Put both lists side by side, remove duplicates, and sort by severity using the [triage table](../modules/10-ai-code-review.md#severity-triage).
3. **Verify (5 minutes).** Pick one high finding and one that looks dubious. For each:
   ```text
   The reviewer says: "<finding>". Don't fix it yet. Write a test that
   demonstrates the failure, run it, and show me it fails. If you can't make
   it fail, explain why the scenario can't happen.
   ```
   Show one confirmed and, if you get one, one refuted. Explain why this step matters. AI critics hallucinate bugs, and fixing every finding bloats the code.

> **Bryan's take:** For coding, Claude and Codex are the best right now, in my opinion. Multi-agent review is valuable: several agents, and ideally several models, reviewing each other's work.

Whichever pair you use, every finding still gets verified before anyone acts on it.

### Hands-on: humans, then bots (25 minutes)

In groups of three, on seeded PR B:
1. **Humans only (10 minutes).** Review with the module 10 checklist. Read the PR description and `git diff --stat` first, then the test diff, then the code. List findings with severity.
2. **Bots (8 minutes).** Run two reviewers from different labs with the same brief.
3. **Score (7 minutes).** For humans, each bot, and the combination: how many planted bugs were found (recall), how many other comments were wrong or useless (false positives), and how long it took.

### Answer key and debrief (10 minutes)

Reveal the planted bugs and ask which layer caught what. Did the bots find the nonexistent dependency? Did the humans catch the tautological test? Did combining the layers beat either one? OpenAI's CriticGPT research makes the empirical case for layered review. Human-plus-critic teams caught about as many bugs as critics alone while hallucinating less ([module 10](../modules/10-ai-code-review.md#what-the-research-says)).

### Takeaway checklist

- [ ] Before a human reviews, a fresh context, ideally a different lab's model, reviews.
- [ ] I treat every bot finding as a hypothesis and verify it with a test or a reason.
- [ ] I read the description, the diff stat, and the test diff before the code.
- [ ] I check every new dependency by hand.
- [ ] I can explain every line of my PR in my own words.
- [ ] I know our review rule, and that a named human approves every merge.

## Session 6: Security, data, and cost

**Goal.** Understand why prompt injection is the hard problem for coding agents, know the team's controls and data rules, and know what agent work actually costs.

**Pre-read (30 minutes).**
- [Module 11: TL;DR](../modules/11-security-and-prompt-injection.md), [Two frameworks that make this tractable](../modules/11-security-and-prompt-injection.md#two-frameworks-that-make-this-tractable), and [Why coding agents are the hard case](../modules/11-security-and-prompt-injection.md#why-coding-agents-are-the-hard-case)
- [Module 11: Real incidents](../modules/11-security-and-prompt-injection.md#real-incidents-20252026) (skim the table)
- [Module 12: TL;DR](../modules/12-costs-subscriptions-and-apis.md) and [Cost per task, not cost per token](../modules/12-costs-subscriptions-and-apis.md#cost-per-task-not-cost-per-token)
- Your team's AI policy, especially data classes and incident reporting

**Prep.** Build the throwaway environment for the injection demo, following [module 11's exercise](../modules/11-security-and-prompt-injection.md#try-it): a container or VM with **no host credentials** (only the agent’s isolated sign-in), a toy repository, a file with a fake canary secret, and a notes file containing an instruction aimed at AI assistants to copy that fake value into the README. Never run this on a real machine or repository.

### Agenda (60 minutes)

| Time | Segment |
| --- | --- |
| 0:00–0:05 | Instructions and data share one channel |
| 0:05–0:20 | Demo: a safe self-injection, then a defense |
| 0:20–0:26 | Three incidents worth knowing |
| 0:26–0:40 | Hands-on A: threat-model one of our workflows |
| 0:40–0:52 | Hands-on B: what did my last week cost? |
| 0:52–1:00 | The policy in five minutes; takeaways |

### Demo script (15 minutes)

1. **The setup (2 minutes).** Show the throwaway environment, the fake secret, and the planted instruction. Say: "This is the kind of text that can hide in a README, an issue, a dependency, or a web page."
2. **The innocent request (5 minutes).** Ask: "Summarize this repo and suggest improvements to the README." Watch what happens. The agent may follow the planted instruction, refuse, or warn you. Any outcome makes the point that resistance to injection is a probability, not a permission system ([module 11](../modules/11-security-and-prompt-injection.md#why-it-is-still-unsolved)).
3. **Apply a defense and repeat (5 minutes).** Test a deny rule against both file-tool and shell reads, or make the toy repository read-only while retaining the model-provider connection. Deny write escalations. A response can still contain the fake canary; read-only does not prevent that disclosure. Repeat the request.
4. **Name the leg (3 minutes).** Draw Meta's Rule of Two: untrusted input, sensitive data, and the ability to change state or communicate. Which leg did the defense remove? A typical coding agent on a laptop has all three by default ([module 11](../modules/11-security-and-prompt-injection.md#why-coding-agents-are-the-hard-case)).

### Three incidents (6 minutes)

From [module 11's incident table](../modules/11-security-and-prompt-injection.md#real-incidents-20252026):
- In Nx "s1ngularity" (August 2025), malware in a build tool's install script ran developers' AI CLIs with skip-permissions flags to search for secrets.
- In July 2025, an agent deleted a production database during a code freeze, with no attacker. Dev and prod weren't separated.
- In "Clinejection" (December 2025 to February 2026), an AI triage bot put issue titles into its prompt, and an attacker used that path to reach release secrets.

### Hands-on A: threat-model one of our workflows (14 minutes)

In groups, pick one real or planned workflow, such as "an agent triages new issues and opens fix PRs," or "a review bot comments on every PR."
1. List every input it reads, every secret it can reach, and every action it can take.
2. Mark each as A (untrusted input), B (sensitive access), or C (changes state or communicates).
3. Choose a leg to remove and redesign the workflow. Use the [team checklist](../modules/11-security-and-prompt-injection.md#team-checklist) for ideas.
4. Groups get two minutes each to present; others try to break the design.

### Hands-on B: what did my last week cost? (12 minutes)

Everyone runs their tool's usage report, for example `npx ccusage@latest daily` ([module 12](../modules/12-costs-subscriptions-and-apis.md#worked-example-one-hour-of-agentic-coding)), or opens the vendor dashboard.
1. Note total tokens, cache reads, and API-equivalent cost for the week.
2. Find your most expensive session. Was it long, full of big tool outputs, full of retries, or run in parallel?
3. Write one habit change that would have halved it (a fresh session between tasks, trimming tool output, a smaller model for easy work).
4. Share a few anonymized numbers with the room.

> **Bryan's take:** API pricing is too expensive for heavy agentic use. Subscriptions are what make it affordable to work this way every day.

Mention the counterpoint. Subscriptions have caps and changing terms, and CI or shared automation must use API keys with budgets ([module 12](../modules/12-costs-subscriptions-and-apis.md#bryans-take)).

### The policy in five minutes

Walk through the three parts people most need: which data classes may go into which tools, which actions always need a human, and how to report an incident (an agent read a secret, ran something destructive, or followed injected instructions). Nobody gets blamed for reporting.

### Takeaway checklist

- [ ] I treat anything the agent reads as something that could give it orders.
- [ ] I know which leg of the Rule of Two each of my agent workflows removes.
- [ ] I never give an agent production credentials, and I approve every irreversible action.
- [ ] I verify every new package an agent suggests.
- [ ] I know what data may go into which tool, and how to report an incident.
- [ ] I know roughly what my agent usage costs per week, and one habit that reduces it.

## Session 7: Parallel agents and cross-model review

**Goal.** Run two agents at once on independent tasks, each in its own worktree, and review each branch with a different model before merging. Know where autonomy stops for this team.

**Pre-read (30 minutes).**
- [Module 08: Steve Yegge's eight stages](../modules/08-agentic-workflows.md#steve-yegges-eight-stages)
- [Module 08: Worktrees and parallel agents](../modules/08-agentic-workflows.md#worktrees-and-parallel-agents) and [Background and unattended runs](../modules/08-agentic-workflows.md#background-and-unattended-runs)
- [Module 08: What the successes have in common](../modules/08-agentic-workflows.md#what-the-successes-have-in-common)
- [Module 09: Building vs reviewing: the read/write asymmetry](../modules/09-multi-agent-systems.md#building-vs-reviewing-the-readwrite-asymmetry) and [Budgets and stop conditions](../modules/09-multi-agent-systems.md#budgets-and-stop-conditions)

**Prep.** Pick two small independent tasks that touch different files, for yourself and for each attendee. Adding missing tests in one module and fixing lint warnings in another works, and so do two unrelated small bugs.

### Agenda (60 minutes)

| Time | Segment |
| --- | --- |
| 0:00–0:05 | Where are you on Yegge's chart? A quick poll |
| 0:05–0:25 | Demo: two agents, two worktrees, one cross-model review |
| 0:25–0:50 | Hands-on: your two tasks in parallel |
| 0:50–0:57 | Debrief: attention, autonomy, and what goes on Hold |
| 0:57–1:00 | Close the series |

### Demo script (20 minutes)

1. **Two worktrees (4 minutes).** One task, one agent, one worktree, one branch. Replace `example-repo` below with your repository’s name before running:
   ```bash
   git worktree add ../.worktrees/example-repo/add-tests -b chore/add-tests
   git worktree add ../.worktrees/example-repo/fix-lint -b chore/fix-lint
   ```
   Start an agent in each with a full task prompt (scope, done criteria, a check to run).
2. **While they run (8 minutes).** Narrate where your attention goes. Check on each agent once, and answer a question from one while the other keeps working. Point out that parallel agents can produce code faster than you can review it.
3. **Cross-model review (5 minutes).** When the first branch finishes, review it with a model from a different lab in a fresh session, using the Session 5 brief. Verify one finding.
4. **Merge one at a time and clean up (3 minutes).** Rebase, run the full suite, merge. Then remove the worktree:
   ```bash
   git worktree remove ../.worktrees/example-repo/add-tests
   ```

> **Bryan's take:** On Yegge's chart I'm one or two from the top, roughly stage 6–7: several CLI agents running in parallel, managed by hand.

### Hands-on: your two tasks in parallel (25 minutes)

1. Create two worktrees and start two agents on your two prepared tasks.
2. Keep a written task list: what each agent is doing and what "done" means for it.
3. When each finishes, review it with a different lab's model before you open a PR. Verify at least one finding.
4. Open the PRs under the normal review rule. Don't merge in the session.
5. Write three sentences: where your attention went, what you nearly missed, and how many agents you could actually review at once.

### Debrief (7 minutes)

Discuss three questions:
- How many agents can you really review? [Module 15's](../modules/15-learning-careers-and-responsibility.md#the-human-side) warning signs are approving diffs you didn't read, losing track of agents, and no deep-focus time. Moving down a stage is allowed.
- Which chores could a background agent do for us? Only ones with a strong automated check, a small reversible diff, and a normal PR review ([playbook Phase 3](ai-first-playbook.md#phase-3-advanced-use)).
- What stays on Hold? Auto-merging agent PRs, agents with production access, and fully autonomous pipelines on our existing product code, until our own evidence says otherwise.

> **Bryan's take:** I don't believe fully autonomous agentic workflows work reliably today. Maybe I'm just too dumb; I haven't had good results, but some people claim they work.

Give the counterpoint its due. The successful autonomous projects all had a strong automated oracle, and that boundary is moving ([module 08](../modules/08-agentic-workflows.md#bryans-take)).

### Close the series (3 minutes)

- Each person writes down the one habit from the series they'll keep.
- Hand out the [feedback form](#feedback-form-five-questions).
- Ask for a volunteer to be next month's [AI radar scout](ai-first-playbook.md#keeping-it-current).

### Takeaway checklist

- [ ] One task, one agent, one worktree, one branch.
- [ ] I pick parallel tasks that touch different files.
- [ ] I keep a written task list when more than one agent is running.
- [ ] Every branch gets a cross-model or fresh-context review before its PR.
- [ ] I merge one at a time, with the full suite green.
- [ ] I run only as many agents as I can actually review, and I remove worktrees when branches merge.

## After the series

### Measuring whether it worked

Four to eight weeks later, check for changes in how people work, beyond attendance:
- Do PR descriptions include verification evidence and the "what the agent did vs. what I did" section?
- Is fresh-context or cross-model review running on most PRs?
- Has PR size stayed reasonable?
- Have stability metrics held against the baseline ([playbook](ai-first-playbook.md#how-to-measure))?
- What new objections came up, and are they in the log?

### Feedback form (five questions)

1. Which session changed how you work, and how?
2. Which session should be cut or changed?
3. What do you still not trust the tools to do?
4. What did you try on real work after a session? What happened?
5. What should the next session be about?

### Keeping the series current

Review the series every quarter alongside the AI radar. Demos age fast. One that showed a failure six months ago may now succeed, and new failure modes show up. Re-run every demo before you reuse it, and update the pre-reads when the modules change.

## Sources and further reading

The series is built on the modules; each session's pre-read links to the sections that source its claims. The exercises adapt the "Try it" sections of [module 01](../modules/01-what-is-an-llm.md#try-it), [module 07](../modules/07-context-engineering.md#try-it), [module 08](../modules/08-agentic-workflows.md#try-it), [module 10](../modules/10-ai-code-review.md#try-it), [module 11](../modules/11-security-and-prompt-injection.md#try-it), and [module 12](../modules/12-costs-subscriptions-and-apis.md#try-it). Primary sources worth handing to facilitators:

- Anthropic, [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices) and [Common workflows](https://code.claude.com/docs/en/common-workflows)
- OpenAI, [Codex best practices](https://learn.chatgpt.com/guides/best-practices)
- Steve Yegge, [Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04) (Jan 2026), for the eight stages
- Simon Willison, [The lethal trifecta for AI agents](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) (2025); Meta, [Agents Rule of Two](https://ai.meta.com/blog/practical-ai-agent-security/) (2025)
- [LLM Critics Help Catch LLM Bugs](https://arxiv.org/abs/2407.00215) (McAleese et al., 2024)
- [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://arxiv.org/abs/2507.09089) (Becker, Rush, Barnes, Rein, 2025)

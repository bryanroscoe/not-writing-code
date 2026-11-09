# Instructor guide

> **Audience:** whoever teaches the [course](syllabus.md), plus TAs · **Last verified:** 2026-11-08
> **Read with:** the [syllabus](syllabus.md) and the [labs](labs/). This guide assumes you've read [module 00](../modules/00-orientation.md) and skimmed the rest.

**TL;DR**
- Grade judgment, not artifacts: the plan, the tests, the verification evidence, the explanation, and the reflection. Use short oral walkthroughs as the integrity backstop. Don't rely on AI detectors.
- Every week below has talking points, a live demo, the misconceptions students bring, and discussion prompts drawn from the modules.
- Students arrive at very different levels. Run an AI-free diagnostic in week 1, pair across levels, and use each lab's "if you finish early" section to stretch experienced students.
- Four live demos show failure modes well: a hallucinated API, prompt injection through a README, tautological tests, and context rot. Rehearse each one and record a backup, because models improve and demos stop failing.
- Re-verify tools, prices, commands, and project policies before every term with the [refresh checklist](#refresh-checklist-for-each-term). Something in this course will be out of date every time you teach it.

## Before the term

Do these in the four weeks before classes start.

1. **Dry-run every lab** with the tools students will buy, on a single $20 plan. Record how much quota each lab used and anything that broke. The syllabus promises every lab fits in one plan. Keep that promise true.
2. **Prepare starter repositories.** You need:
   - Lab 2: a small project with a few tests.
   - Lab 3: a skeleton with a feature menu and **hidden acceptance tests** you keep out of the student repo.
   - Lab 4: a small web API with users, an admin-only endpoint, and tests.
   - Lab 6: an "eval starter" repo with tagged base commits and hidden tests, for self-paced learners and for teams whose project history is too thin. Lab 6 normally uses each team's own project history.
   - Lab 8 fallback: a class-run open-source repository with a `CONTRIBUTING.md`, a written AI policy, CI, and at least one sized, labelled issue per student, plus spares.
3. **Vet a Lab 8 project list.** Five to fifteen projects with explicit AI-contribution policies, active maintainers, and runnable tests. Cap students per project (two is a reasonable default) so the class doesn't become a burden on any one maintainer team ([module 13](../modules/13-open-source-ecosystem.md#the-other-side-ai-slop-and-maintainer-burden)).
4. **Build a Lab 5 sandbox recipe** students can follow: a container or VM with no mounted home directory and no forwarded credentials. Test it on macOS, Windows (WSL), and Linux.
5. **Sort out access.** Decide how students who can't pay get a plan. Confirm what institutional or education licenses exist this term, and their data terms ([module 15](../modules/15-learning-careers-and-responsibility.md#data-privacy-what-not-to-paste)).
6. **Rehearse and record the four demos** in [Live demos](#live-demos-that-reliably-show-failure-modes).
7. **Calibrate TAs** on the walkthrough protocol and the shared rubric dimensions.
8. **Fill every placeholder** in the syllabus: course number, prerequisites, credit hours, accessibility statement, integrity policy, grading scale.

## Principles for teaching this course

- **Grade judgment, not output.** Agents make output cheap. The scarce skills are specifying, verifying, reviewing, and explaining ([module 15](../modules/15-learning-careers-and-responsibility.md#skills-that-gain-value)).
- **Teach the durable idea, then date the example.** "Tests are the agent's contract" will outlast every model named in class. When you cite a model, a price, or a benchmark score, say the month.
- **Model verification yourself.** When you state a fact in lecture, show the source. When a demo agent claims success, ask it for the command and output in front of the class.
- **Model disclosure yourself.** Tell students how you used AI to prepare the course. This knowledge base describes how it was made ([module 00](../modules/00-orientation.md#how-this-material-was-made)); do the same for your slides.
- **Be honest about mixed evidence.** Productivity and learning studies disagree and change. Skeptical students trust a course that admits limits ([module 05](../modules/05-judging-models.md#real-world-productivity-evidence)).
- **Keep some work AI-free on purpose,** and say why: the skills needed to supervise agents, like reading and debugging code, are built by hand ([module 15](../modules/15-learning-careers-and-responsibility.md#deskilling-real-risk-or-old-panic)).

## Week by week

Each week lists a goal, talking points, a live demo, misconceptions to address, and discussion prompts. Pick two or three prompts per session; don't try to cover all of them.

### Week 1: what this course means by vibe coding

**Goal:** set the stance (AI-accelerated, human accountable), explain the tiers, get everyone set up.

**Talking points**
- Karpathy's original "vibe coding" meant not reading the code. This course teaches the opposite habit. Show the spectrum table and point out that most of the course lives in the supervised-agent rows ([module 00](../modules/00-orientation.md#what-we-mean-by-vibe-coding)).
- The six ideas that outlast the hype are the spine of the course ([module 00](../modules/00-orientation.md#six-ideas-that-outlast-the-hype)).
- Why an AI course has AI-free work: in Anthropic's 2026 trial, the AI group scored 50% on a follow-up quiz against 67% for hand-coders, with the largest gap on debugging ([module 15](../modules/15-learning-careers-and-responsibility.md#what-the-evidence-says)).
- Walk through the AI-use policy and the AI log. Frame disclosure as a professional norm, not a confession.
- Setup clinic: install one agent, sign in with the subscription (not an API key), check the data-training setting.

**Live demo:** a five-minute preview of the week 5 loop on a toy bug. Narrate what you check before trusting it. Students should see the target skill on day one.

**Misconceptions**
- "Vibe coding means I don't need to know how to code." The opposite: supervising agents requires reading and debugging skill.
- "In an AI course, everything is allowed." Each assignment has a tier.
- "If I disclose AI use, I'll lose points." Missing disclosure costs points. Honest disclosure never does.

**Discussion prompts** ([module 00](../modules/00-orientation.md#discussion-questions))
- When is not reading the code genuinely the right choice?
- Where should the line be between "AI helped me" and "AI did it for me" in a programming course?
- If an AI writes 80% of a team's code, what should the humans spend their time on?

**Diagnostic (AI-free, 30 minutes, ungraded):** predict a 40-line function's output on three inputs; find the bug in a 20-line diff; write one test for a given function; a short survey on languages, internships, and prior AI tool use. Use it to pair students ([below](#handling-different-starting-levels)).

### Week 2: what an LLM is

**Goal:** a next-token mental model that predicts failures.

**Talking points**
- The loop: predict a probability for every token, sample one, append, repeat ([module 01](../modules/01-what-is-an-llm.md#the-one-idea-predict-the-next-token)).
- Not a database, search engine, calculator, or person. Each "not" comes with a fix ([module 01](../modules/01-what-is-an-llm.md#what-an-llm-is-not)).
- Tokenization explains letter counting, arithmetic slips, and why non-English text and some code styles cost more.
- Temperature reshapes probabilities. Temperature 0 should be deterministic but often isn't on hosted models, partly because of server-side batching ([module 01](../modules/01-what-is-an-llm.md#sampling-temperature-and-determinism)).
- Hallucination has structural causes, including evaluations that reward guessing over "I don't know" (Kalai et al., 2025). Sycophancy is trained in ([module 01](../modules/01-what-is-an-llm.md#hallucination-and-why-it-happens)).

**Live demo:** [the hallucinated API](#demo-1-the-hallucinated-api).

**Misconceptions**
- "It looks things up." Not unless a search tool is on, and then a separate system does the looking.
- "Temperature 0 gives the same answer every time."
- "A token is a word."
- "Reasoning models don't hallucinate." Reasoning is trained thinking time, not a guarantee of correct logic ([module 01](../modules/01-what-is-an-llm.md#reading-model-announcements-with-this-module-in-mind)).

**Discussion prompts** ([module 01](../modules/01-what-is-an-llm.md#discussion-questions))
- How would you score "I'm not sure" against a wrong answer in your own evaluation of a coding assistant?
- Interpretability shows a model can describe a method it didn't use. What does that mean for asking an agent to explain its own changes?
- Which of the four "it is not..." misconceptions have you seen cause a real problem?

### Week 3: harnesses, tools, and MCP

**Goal:** agent = model + harness; students can name what the harness controls.

**Talking points**
- Harness = loop + tools + permissions + context management + interface ([module 06](../modules/06-harnesses-and-tools.md#what-a-harness-is)).
- The model only emits text that asks for a tool. The harness decides whether to run it. That's why permissions are a security boundary ([module 06](../modules/06-harnesses-and-tools.md#permission-systems-are-a-security-boundary-not-a-ux-detail)).
- The same model scores very differently in different harnesses ([module 05](../modules/05-judging-models.md#harness-matters)).
- MCP is a standard way to plug in tools. Its costs are context bloat and security risk ([module 06](../modules/06-harnesses-and-tools.md#mcp-the-model-context-protocol)).
- The tool landscape churns. Learn the concepts; they transfer ([module 06](../modules/06-harnesses-and-tools.md#a-short-history-from-autocomplete-to-orchestrators)).

**Live demo:** open an agent on a toy repository with the context view showing (in Claude Code, `/context`). Point out how many tokens are used before you type anything. Ask it to explain the architecture and narrate each tool call. Then put the 30-line loop from [module 13](../modules/13-open-source-ecosystem.md#framework-or-just-a-loop) on the projector and map each line to the harness table.

**Misconceptions**
- "The model edits the files." The harness does, when the model asks and permissions allow.
- "More MCP servers make a more capable agent." Usually they make a slower, more confused, more expensive one ([module 06](../modules/06-harnesses-and-tools.md#common-failure-modes)).
- "Approval prompts keep me safe." Not if you approve every one without reading.

**Discussion prompts** ([module 06](../modules/06-harnesses-and-tools.md#discussion-questions))
- If "agent = model + harness," which part matters more for your work today?
- Is an approval prompt you always approve a safety feature? What would you replace it with?
- Several popular tools were acquired, pivoted, or shut down in 2026. How should a team protect itself from that churn?

### Week 4: context engineering

**Goal:** context is the main lever, and a bigger window isn't better attention.

**Talking points**
- The ladder (prompt, context, harness, loop, graph) is partly substance and partly relabeling. Ask students to sort which is which ([module 07](../modules/07-context-engineering.md#a-skeptical-note-what-is-substance-and-what-is-relabeling)).
- Prompting basics that survive model upgrades: be specific, give the reason, define done with a check, show an example ([module 07](../modules/07-context-engineering.md#prompting-basics-that-still-matter)). ALL CAPS and "think harder" mostly don't help.
- In a coding agent, tool results are often the largest share of the context ([module 07](../modules/07-context-engineering.md#what-actually-fills-an-agents-context-window)).
- Performance drops as input grows, especially with similar-looking distractors. The constraint has moved from capacity to attention and cost ([module 07](../modules/07-context-engineering.md#context-limits-in-practice)).
- The rise and fall of giant instruction files, and what a good one looks like ([module 07](../modules/07-context-engineering.md#current-best-practice)).

**Live demo:** [context rot](#demo-4-context-rot), or trim the bloated `CLAUDE.md` example from module 07 live, sorting each line into its proper home.

**Misconceptions**
- "A million-token window means it uses all million tokens equally well."
- "A longer `CLAUDE.md` makes the agent smarter."
- "Prompt engineering is about magic phrases."

**Discussion prompts** ([module 07](../modules/07-context-engineering.md#discussion-questions))
- Which rung of the ladder adds the most new substance, and which is mostly a new name?
- The ETH study found developer-written context files helped a little, generated ones didn't, and both raised costs. What should a team's policy be?
- Who should be allowed to edit `AGENTS.md` in a repository, and how should changes be reviewed?

**AI-free check 1:** tokenization predictions, what temperature does, what fills a context window, what's missing from a weak task prompt, and reading a short function.

### Week 5: agentic workflows

**Goal:** the core loop, tests as the contract, and autonomy as a dial.

**Talking points**
- "Claude stops when the work looks done." Without a check to run, "looks done" is all the agent has ([module 08](../modules/08-agentic-workflows.md#the-key-fact-the-loop-stops-when-the-model-thinks-it-is-done)).
- Explore → plan → implement → verify → commit, with the prompts from the module ([module 08](../modules/08-agentic-workflows.md#the-core-loop-explore--plan--implement--verify--commit)).
- Tests are a contract only if the agent can't quietly rewrite them ([module 08](../modules/08-agentic-workflows.md#tests-as-the-agents-contract)).
- Steering: watch the first minute, press `Esc` on drift, and after two failed corrections start fresh with a better prompt ([module 08](../modules/08-agentic-workflows.md#steering-a-session)).
- Yegge's stages measure delegation, not quality ([module 08](../modules/08-agentic-workflows.md#steve-yegges-eight-stages)).
- The autonomy debate. The famous autonomous successes share a strong oracle, greenfield code, a human-built harness, and tolerance for waste ([module 08](../modules/08-agentic-workflows.md#what-the-successes-have-in-common)).

> **Bryan's take:** I don't believe fully autonomous agentic workflows work reliably today. Maybe I'm just too dumb; I haven't had good results, but some people claim they work.

Present the counter-claims with equal care: OpenAI's harness team reports a million-line product without hand-written code, Cursor reports a week-long multi-agent run that built a web browser (disputed: critics reported that a fresh clone failed to build and that most CI jobs failed; see [module 08's critique](../modules/08-agentic-workflows.md#the-case-against-or-at-least-not-yet)), and Anthropic reports that Claude writes most of its merged code ([module 07](../modules/07-context-engineering.md#bryans-take), [module 08](../modules/08-agentic-workflows.md#the-case-for-full-autonomy)). Ask students what evidence would settle it.

**Live demo:** run the shape of the module 08 [sample session](../modules/08-agentic-workflows.md#a-sample-session) on a toy bug. Before it runs the tests, ask "is it done?" and let the class watch it claim success. Then ask for the command and output.

**Misconceptions**
- "The agent said done, so it's done."
- "A higher Yegge stage means a better engineer."
- "Agent-written tests are fine if they pass."
- "Plan mode slows me down." It's the cheapest place to catch a wrong idea.

**Discussion prompts** ([module 08](../modules/08-agentic-workflows.md#discussion-questions))
- What is the closest thing to an oracle in a codebase you know, and what would it take to build a better one?
- If a pipeline's rule is "code must not be reviewed by humans," who is accountable when it ships a security bug?
- When should you move *down* a stage?

### Week 6: learning with AI, integrity, careers

**Goal:** students choose deliberately how they use AI to learn, and read the career evidence honestly.

**Talking points**
- Producing work and learning from it are different goals ([module 15](../modules/15-learning-careers-and-responsibility.md#producing-the-work-vs-learning-from-it)).
- How people used AI mattered in the Anthropic trial: conceptual questions did fine, delegation did worst. The subgroups were small, so treat it as suggestive ([module 15](../modules/15-learning-careers-and-responsibility.md#what-the-evidence-says)).
- Bastani et al.: plain chat access hurt later exam scores; a tutor-style version that gave hints didn't.
- Higher confidence in AI went with less critical thinking (Lee et al.). People misjudge their own AI-assisted speed (METR).
- Careers: early-career employment in AI-exposed jobs is below trend, the cause is debated, and overall software employment is still projected to grow ([module 15](../modules/15-learning-careers-and-responsibility.md#careers)).

**Live demo:** show a learning mode, such as Claude Code's Learning output style (`/output-style learning`) or ChatGPT's study mode ([module 15](../modules/15-learning-careers-and-responsibility.md#how-to-learn-with-ai-instead-of-outsourcing-learning)). Let it leave a `TODO(human)` and write that piece yourself.

**Misconceptions**
- "If I finished faster with AI, I learned it."
- "The research says AI rots your brain." The EEG study is a small preprint about essay writing, overstated by media.
- "Juniors are doomed," or "nothing has changed." The evidence supports neither.

**Discussion prompts** ([module 15](../modules/15-learning-careers-and-responsibility.md#discussion-questions))
- The AI group wasn't significantly faster *and* learned less. When would you still use AI while learning something new?
- If companies hire fewer juniors, where will future seniors come from?
- How would you tell healthy AI-first work from "approving diffs nobody read"?

**In class:** the write-the-policy exercise from module 15, then 20 minutes of AI-free debugging practice to prepare for check 2.

### Week 7: AI code review

**Goal:** review is the bottleneck; students can review AI-written code with a checklist.

**Talking points**
- What AI reviewers are good at (local bugs, edge cases, spec mismatches) and bad at (intent, architecture, staying quiet) ([module 10](../modules/10-ai-code-review.md#what-they-are-good-and-bad-at)).
- Layers: the author agent self-checks, an independent bot reviews (ideally a different model), and a human reviews intent, design, and risk ([module 10](../modules/10-ai-code-review.md#a-layered-review-workflow)).
- Verify findings before acting. Critics hallucinate bugs, and fixing every finding bloats code ([module 10](../modules/10-ai-code-review.md#verify-findings-before-acting)).
- The AI-PR checklist, especially tests that test nothing and swallowed errors ([module 10](../modules/10-ai-code-review.md#how-humans-should-review-ai-written-prs)).
- Small PRs get better reviews; show Anthropic's numbers on large vs small PRs ([module 10](../modules/10-ai-code-review.md#keep-prs-small)).
- The human who merges owns it ([module 10](../modules/10-ai-code-review.md#accountability-the-human-who-merges-owns-it)).

**Live demo:** [tautological tests](#demo-3-tautological-tests).

**Misconceptions**
- "The review bot passed it, so it's fine."
- "Fix every finding."
- "The tests pass, so the tests are good."

**Discussion prompts** ([module 10](../modules/10-ai-code-review.md#discussion-questions))
- If AI reviewers catch more local bugs than humans, what should human reviewers spend their time on?
- Should an AI reviewer ever be allowed to approve a merge on its own?
- How would you detect rubber-stamping?

**Before Lab 4:** assign pairs, ideally across experience levels, and collect sealed answer keys before the swap.

### Week 8: security and prompt injection

**Goal:** injection is unsolved, and defenses are architectural.

**Talking points**
- Instructions and data share one channel. Use the module's analogy of an assistant who obeys any letter on their desk ([module 11](../modules/11-security-and-prompt-injection.md#instructions-and-data-share-one-channel)).
- Indirect injection is the one that matters for coding agents ([module 11](../modules/11-security-and-prompt-injection.md#direct-vs-indirect-injection)). Jailbreaks are a different problem.
- The lethal trifecta and the Rule of Two ([module 11](../modules/11-security-and-prompt-injection.md#two-frameworks-that-make-this-tractable)). A coding agent on a laptop has all three legs by default.
- Pick two or three incidents from the [incident table](../modules/11-security-and-prompt-injection.md#real-incidents-20252026), for example the GitHub MCP toxic agent flow, Nx "s1ngularity," and Clinejection.
- Classifier-based approval is a speed bump; a sandbox is the wall ([module 11](../modules/11-security-and-prompt-injection.md#risks-specific-to-coding-agents)).

**Live demo:** [prompt injection through a README](#demo-2-prompt-injection-through-a-readme).

**Misconceptions**
- "A good system prompt prevents injection."
- "This only matters if I install sketchy tools."
- "It refused once, so it's safe." An attacker needs one failure.
- "The sandbox covers everything." Check what it covers. Claude Code's sandbox, for example, covers Bash and its child processes, not its built-in file tools ([module 11](../modules/11-security-and-prompt-injection.md#practical-defenses)).

**Discussion prompts** ([module 11](../modules/11-security-and-prompt-injection.md#discussion-questions))
- Why can't we fix prompt injection the way parameterized queries fixed SQL injection?
- An agent reads support emails and updates the CRM. Which leg of the Rule of Two would you remove, and what does that cost the product?
- If an agent you supervised leaked a secret because of text in a dependency's README, who is accountable?

**Before Lab 5:** approve each student's sandbox plan in week 8, before they run any attack. Students who want to run defense D2 with their harness's own sandbox may need the VM option rather than a container ([refresh checklist](#refresh-checklist-for-each-term)). **AI-free check 2:** review a short diff by hand with the checklist, and label the trifecta legs in a scenario.

### Week 9: the model landscape and reading claims

**Goal:** students can read model names and launch claims without memorizing lineups.

**Talking points**
- Every lab sells a tier ladder; names change, the ladder doesn't ([module 03](../modules/03-model-landscape.md#how-to-read-model-names-and-tiers)).
- Closed labs lead and open models trail by months; open models set the price floor ([module 03](../modules/03-model-landscape.md#different-places-in-the-chain)).
- The "best model for the job" table separates fact from opinion in its Basis column. Point that out ([module 03](../modules/03-model-landscape.md#best-model-for-the-job)).
- The eight-question benchmark claim checklist ([module 05](../modules/05-judging-models.md#reading-a-benchmark-claim-a-checklist)).
- Benchmark-maxing, with the Opus 5 to Opus 5.5 example ([module 05](../modules/05-judging-models.md#a-recent-example-opus-5-to-opus-55)).

> **Bryan's take:** Opus 5 felt benchmark-maxed: great numbers, and it kind of sucked in daily use. People didn't like it. Opus 5.5 people really liked.

**Live demo:** take the most recent launch post from a major lab and go through the checklist on the projector. Which harness? What effort? Who ran the competitor numbers? What's missing compared with last time?

**Misconceptions**
- "A higher benchmark score means it's better for my work."
- "There's one best model."
- "Open models are as good as closed ones," or "they're far behind." Roughly six months to a year, as of November 2026 ([module 03](../modules/03-model-landscape.md#closed-labs-lead-open-models-trail-by-months)).

**Discussion prompts** ([module 03](../modules/03-model-landscape.md#discussion-questions), [module 05](../modules/05-judging-models.md#discussion-questions))
- What does a benchmark measure that daily use doesn't, and the reverse?
- A vendor's chart shows a 3-point lead on a coding benchmark. What would you ask before believing it matters?
- Your eval says Model A; your senior engineers' vibes say Model B. What next?

**Lab 8 kickoff:** show the policy table from [module 13](../modules/13-open-source-ecosystem.md#the-other-side-ai-slop-and-maintainer-burden) and your vetted project list. Stress that no PR goes out before a maintainer's go-ahead.

### Week 10: building your own eval

**Goal:** students can answer "should *we* use it, in *our* tool, on *our* code?"

**Talking points**
- Golden tasks come from real merged work, with hidden tests and at least one trap task ([module 05](../modules/05-judging-models.md#build-your-own-eval)).
- A configuration is model + harness + version + settings. Change one thing at a time.
- Blind the outputs. People favor the model they expect to be better ([module 05](../modules/05-judging-models.md#vibes-are-data-too)).
- The standard error of a pass rate is about √(p(1−p)/n). Paired comparisons do better on small sets ([module 05](../modules/05-judging-models.md#the-statistics-of-small-evals)).
- Agents game graders. Hide tests, diff the test directory, read passing transcripts ([module 05](../modules/05-judging-models.md#cheating-reward-hacking-and-grader-trust)).

**Live demo:** on the board, compute the error bar for 10 tasks at 60% and for 40 tasks at 60%. Then show a ten-line script that copies outputs to random IDs and writes the key to a separate file. Students will use the same idea in Lab 6.

**Setting up Lab 6:** it runs on each team's project history and is the project's eval set. Before the run phase, collect every task's hidden tests through `[the course's private submission system]` and check that students deleted their local copies. An agent running as the student can read sibling and parent folders, so "outside the repository" isn't far enough. Release the tests only for the grade phase, after the runs are finished.

**Misconceptions**
- "Ten tasks can detect a five-point difference."
- "If the hidden tests passed, the agent solved the task."
- "An LLM judge is objective." Judges share biases such as position and length ([module 09](../modules/09-multi-agent-systems.md#patterns-and-when-each-helps)).

**Discussion prompts** ([module 05](../modules/05-judging-models.md#discussion-questions))
- pass@k or pass^k: which matters for autocomplete, a PR-writing agent, and an unattended nightly job?
- METR's developers felt faster and were slower. How would you guard against that on your team?
- Should a course grade students with AI-assisted benchmarks of their own design? What would that teach?

### Week 11: multiple agents

**Goal:** students know when more agents help (reading) and when they hurt (writing).

**Talking points**
- The read/write asymmetry: review and research parallelize; writing on one codebase usually doesn't ([module 09](../modules/09-multi-agent-systems.md#building-vs-reviewing-the-readwrite-asymmetry)).
- Kim et al.: multi-agent architectures did slightly worse than a single agent on SWE-bench Verified. Cursor: "20 agents performed like 2 or 3."
- Much of the gain from multi-agent methods comes from sampling and voting; debate can make answers worse ([module 09](../modules/09-multi-agent-systems.md#what-the-evidence-adds-up-to)).
- Models prefer their own output, so review in a fresh context at minimum and with another lab's model when it matters ([module 09](../modules/09-multi-agent-systems.md#recipe-2-cross-model-review)).
- Set budgets and stop conditions before starting ([module 09](../modules/09-multi-agent-systems.md#budgets-and-stop-conditions)).

> **Bryan's take:** Multi-agent review is valuable: several agents, and ideally several models, reviewing each other's work.

**Live demo:** a three-reviewer swarm on a small diff, then a verifier on the top two findings. Aim to show at least one finding the verifier refutes.

**Misconceptions**
- "More agents means better results."
- "If agents debate, they converge on the truth."
- "A new session of the same model is an independent reviewer." It's the minimum, not the ideal.
- "Giving agents roles like CEO and QA adds checks." It adds tokens ([module 09](../modules/09-multi-agent-systems.md#anti-patterns)).

**Setting up Lab 7:** it's the project's cross-model review. In class, have each team give every member a different pull request from week 10 on that the member didn't write. The project's security review is also due this week.

**Discussion prompts** ([module 09](../modules/09-multi-agent-systems.md#discussion-questions))
- Why do review and research parallelize better than writing code?
- If models prefer their own output, what does that mean for a team that uses one vendor for everything?
- Share full context, or withhold the author's reasoning from reviewers? How do you reconcile the two?

### Week 12: how models are made; open vs closed weights

**Goal:** enough about model-making to judge claims and choices.

**Talking points**
- Pretraining, mid-training, post-training; reinforcement learning on checkable tasks produced reasoning models ([module 02](../modules/02-training-and-tuning.md#the-pipeline-at-a-glance)).
- Distillation is standard practice and also the subject of a public fight ([module 02](../modules/02-training-and-tuning.md#distillation-and-synthetic-data)).
- Most teams shouldn't fine-tune first ([module 02](../modules/02-training-and-tuning.md#should-you-fine-tune-at-all)).
- Self-tuning: separate demonstrated, deployed, and speculation. As of November 2026, the module found no deployed frontier model that updates its weights continuously from use ([module 02](../modules/02-training-and-tuning.md#demonstrated-deployed-or-speculation)).
- Open weight is not open source. Licenses vary a lot. Memory ≈ parameters × bytes per parameter, plus context ([module 04](../modules/04-open-vs-closed-weights.md#running-open-models-the-hardware-math)).

> **Bryan's take:** Models that can tune their own weights are huge.

Pair that with the module's caution: the results are real, small-scale, and supervised ([module 02](../modules/02-training-and-tuning.md#why-it-matters-and-why-caution)).

**Live demo:** memory math on the board for 8B, 30B, and 70B models at 16-bit and 4-bit. Then open a model card and its license on Hugging Face (no download) and answer the license checklist from [module 04](../modules/04-open-vs-closed-weights.md#what-to-check-before-using-an-open-model-at-work).

**Misconceptions**
- "Fine-tune it so it knows our codebase."
- "Open weights means open source."
- "The model learns from my chats in real time."
- "Self-hosting is automatically safer" ([module 04](../modules/04-open-vs-closed-weights.md#self-hosting-isnt-automatically-safer)).

**Discussion prompts** ([module 02](../modules/02-training-and-tuning.md#discussion-questions), [module 04](../modules/04-open-vs-closed-weights.md#discussion-questions))
- Your team wants to fine-tune "so the model knows our codebase." What would you propose instead?
- Which level of the self-improvement spectrum would you deploy in a product today, with what controls?
- Should "open source AI" require training data, or are open weights enough?

**AI-free check 3:** error bars, the benchmark claim checklist applied to a short excerpt, memory math, and license questions.

### Week 13: costs and the open-source ecosystem

**Goal:** judge cost per finished task, and treat maintainers' time as a shared resource.

**Talking points**
- Three ways to pay: chat subscription, tool subscription, API ([module 12](../modules/12-costs-subscriptions-and-apis.md#three-ways-to-pay)).
- The model is stateless, so cost grows roughly with the square of turns; caching cuts most of it in the worked example ([module 12](../modules/12-costs-subscriptions-and-apis.md#why-agentic-coding-eats-tokens)).
- Subscriptions are for individual interactive work; production, CI, and anything for other users needs the API, by the terms ([module 12](../modules/12-costs-subscriptions-and-apis.md#when-api-billing-is-the-right-choice)).
- curl ended its bug bounty after confirmed reports fell below one in twenty. Project policies range from bans to "disclose it and own it" ([module 13](../modules/13-open-source-ecosystem.md#the-other-side-ai-slop-and-maintainer-burden)).

**Live demo:** a short maintainer's chair. Show four prepared PRs (careful human work, careful AI-assisted work with disclosure, two unreviewed AI dumps). Time how long each takes to review.

**Misconceptions**
- "The API is cheaper because you pay only for what you use." Not for heavy agent sessions.
- "My subscription can power my app's AI feature or my CI bot." Not under the terms.
- "Maintainers appreciate any PR."

**Discussion prompts** ([module 12](../modules/12-costs-subscriptions-and-apis.md#discussion-questions), [module 13](../modules/13-open-source-ecosystem.md#discussion-questions))
- Should a university course give students API keys, subscriptions, or neither? What about students who can't pay?
- Gentoo bans AI contributions; LLVM allows them with review and disclosure. Which would you choose for your project?
- Who should bear the cost of filtering AI-generated reports?

### Week 14: keeping up

**Goal:** a sustainable routine and a method for "it got worse."

**Talking points**
- What stays stable: context, verification, security, decomposition, your own eval, cost awareness ([module 14](../modules/14-keeping-up.md#what-stays-stable)).
- Most documented quality drops came from infrastructure, harness, or product changes, not the weights ([module 14](../modules/14-keeping-up.md#ups-and-downs-are-normal)).
- The diagnostic flowchart: status page, harness changes, golden tasks, then task difficulty ([module 14](../modules/14-keeping-up.md#is-it-the-model-the-task-or-the-harness)).
- The two-week rule and one change at a time ([module 14](../modules/14-keeping-up.md#a-sustainable-routine)).

**Live demo:** take a recent public "model X got dumber" thread and run it through the flowchart with the class.

**Misconceptions**
- "It got dumber" always means the model changed.
- "I need to track every release."

**Discussion prompts** ([module 14](../modules/14-keeping-up.md#discussion-questions))
- Why do people blame the model first, when most incidents were in the harness or serving layer?
- How much time should an engineer spend keeping up each week, and should it be on company time?
- How would you tell healthy experimentation from tool churn?

### Week 15: ship and reflect

**Goal:** demos, reflection, and feedback for next term.

**Talking points**
- Revisit the six durable ideas. Which held up this term? Which looked shakier?
- The human side: intensity and fatigue, workslop, imposter feelings; AI-first is not AI-only ([module 15](../modules/15-learning-careers-and-responsibility.md#the-human-side)).

**In class:** final demos. Each one must include a segment on something an agent got wrong. Then revisit the week 1 analogies and run a retrospective. Feed what you learn into the refresh checklist.

**Discussion prompts**
- Which of the six durable ideas is most likely to be wrong in two years ([module 00](../modules/00-orientation.md#discussion-questions))?
- What would convince you that a fully autonomous coding pipeline is trustworthy?

## Grading AI-assisted work

### What you're grading

When agents do much of the typing, the artifact says little about the student. Grade four things instead:

1. **The process.** Was there a plan? Were tests written or approved before the implementation? Do the commits tell that story?
2. **The explanation.** Can the student explain every line, the alternatives, and the failure modes, in a walkthrough and in their PR descriptions?
3. **The tests.** Did they fail first? Do they test behavior, or do they echo mocks? Does a deliberate break make one fail?
4. **The reflection.** Is it specific, tied to evidence, and honest about what the AI did and what it got wrong?

Two rules make this fair:

- **Grade what the student caught, not what the AI got wrong.** An agent's mistake costs nothing if the student found it. A mistake that reached the submission is the student's.
- **Never penalize honest disclosure.** Penalize missing disclosure. Otherwise students learn to hide AI use, which is the opposite of the professional norm ([module 15](../modules/15-learning-careers-and-responsibility.md#attribution-and-disclosure-in-commits-and-prs)).

### Shared rubric dimensions

Every lab rubric draws on these. The weights differ per lab.

| Dimension | Strong | Weak |
| --- | --- | --- |
| Spec and plan | Written before code; edge cases and non-goals named; the student pushed back on the agent's plan at least once | No plan, or the agent's plan accepted unread |
| Tests | Written or approved first; seen failing; cover edge and error cases; no test edits in implementation commits | Written after; assertions on mocks; never seen failing; quietly loosened |
| Verification evidence | Commands and output; `git diff --stat`; the student's own reproduction | "The agent said the tests pass" |
| Review handling | Each finding verified or refuted with evidence; triaged by severity | Every finding fixed blindly, or all ignored |
| Explanation | Can explain any line and why this approach | "The agent did it that way" |
| AI log and reflection | Specific; names a caught error; matches the evidence | Generic; contradicts the commit history |

### Red flags in the evidence

These are reasons to schedule a walkthrough, not proof of anything:

- The AI log says "I wrote the tests," but the transcript shows the agent writing them.
- One giant commit, with no test-first commit, in a lab that asks for one.
- Test files changed in the same commit as the implementation.
- Transcripts missing for decisions the lab asked to document.
- A reflection that describes events the commits don't show.

### Oral check-ins and walkthroughs

Walkthroughs are the course's main integrity safeguard and its best teaching tool. They follow [module 15's suggested policy](../modules/15-learning-careers-and-responsibility.md#a-suggested-policy-for-an-ai-accelerated-course): if you can't explain it, it doesn't count as yours.

**When.** Pick a few students at random for each lab, plus anyone whose evidence shows a red flag. Every student gets at least one lab walkthrough during the term, and everyone gets a 10-minute project walkthrough at the end.

**Format.** Five minutes for a lab, ten for the project. The student shares their screen with their repository and no AI tools open. Notes they wrote themselves are fine.

**Question bank** (drawn from [module 10](../modules/10-ai-code-review.md#make-the-author-explain-the-change)):
- "Walk me through what happens when this input is empty."
- "Why this approach rather than X?"
- "Show me the test that fails if I change this line." Then change it and run the tests.
- "What did the agent propose that you rejected, and why?"
- "Where is the transcript for this decision?"
- "If this broke in production, what would you check first?"

**Scoring.** Pass, Partial, or Not yet, with two sentences of notes. "Not yet" means the student gets one chance to redo the walkthrough or the work within a week. A single "not yet" is not a misconduct finding. A pattern, combined with other evidence, goes through `[the institution's integrity process]`.

**Fairness.** Use the same question bank for everyone. Offer written or recorded walkthroughs as an accommodation. Calibrate TAs by having them pair on their first few walkthroughs. Allow for nerves and for students working in a second language: you're testing understanding, not polish.

### Grading team work

- Team deliverables get a team score, adjusted per person by individual evidence: commits, PR reviews written, AI logs per PR, and `[peer evaluation]`.
- Lab 6 is a team lab with individual parts: each student's tasks, runs, and scoring are graded individually; the leak check, statistics, and decision are shared. Lab 7 is individual, on a teammate's PR.
- Branch protection makes every merge traceable to a human approver. The approver owns that change too ([module 10](../modules/10-ai-code-review.md#accountability-the-human-who-merges-owns-it)).
- Watch for one experienced member doing all the merging. Each member should author and approve merges.

### What not to do

- **Don't use AI detectors as evidence.** AI use is hard to detect reliably, and policies that depend on catching it tend to fail and punish students unevenly ([module 15](../modules/15-learning-careers-and-responsibility.md#what-instructors-can-reasonably-allow)).
- **Don't grade lines of code or feature counts.** Agents inflate both. The same goes for team metrics at work ([module 10](../modules/10-ai-code-review.md#team-metrics-what-to-watch-what-not-to-measure)).
- **Don't require a second paid plan.** Cross-model steps have free or shared alternatives in every lab.

## Handling different starting levels

### Find out who you have

Use the week 1 diagnostic and survey to sort students roughly into newcomers, intermediates, and experienced engineers (internships, open-source work, daily agent use). Use the groups for pairing only, never for grading.

### The newcomer

Newcomers can program but haven't used agents, or have used chat assistants mostly to get answers.

- **Their risk:** dependence. They approve what they don't understand and skip the struggle that builds skill ([module 15](../modules/15-learning-careers-and-responsibility.md#producing-the-work-vs-learning-from-it)).
- **What helps:** the habits in the [student path](../paths/students.md#habits-to-build-from-day-one) and [module 15](../modules/15-learning-careers-and-responsibility.md#how-to-learn-with-ai-instead-of-outsourcing-learning): attempt first before asking, ask for hints instead of answers, keep a "didn't understand" log. Suggest a learning mode for the first labs. Treat their walkthroughs as coaching.
- **Scope:** each lab's core steps are the requirement. Extensions are optional and don't raise the ceiling of the grade.
- **Watch for** git trouble. A newcomer who can't undo an agent's change will be afraid to let it make one. A short git clinic in week 2 pays off all term.

### The existing engineer

Some students have shipped code at internships or jobs, and some already use agents daily.

- **Their risk:** overconfidence. YOLO habits from work, skipping AI-free reps because "I already know how to code," and treating the course as tool training. The Anthropic trial's participants were professionals, and the learning effects applied to them ([module 15](../modules/15-learning-careers-and-responsibility.md#how-to-learn-with-ai-instead-of-outsourcing-learning)).
- **Stretch work:** every lab's "if you finish early" section; parallel agents in separate worktrees on Labs 3 and 6 ([module 08](../modules/08-agentic-workflows.md#worktrees-and-parallel-agents)); writing their own agent loop ([module 13 Try it](../modules/13-open-source-ecosystem.md#try-it)); writing golden tasks for the class eval pool.
- **Give them responsibility:** maintainer shifts on the Lab 8 class repository, or reviewing newcomers' pull requests. Explaining a review comment to someone else is a good test of their own understanding.
- **Remind them:** employer code and data stay out of the course, whatever their employer's tools allow ([module 15](../modules/15-learning-careers-and-responsibility.md#data-privacy-what-not-to-paste)).

### Mixing them

- **Pair across levels in Lab 4.** The experienced student's planted bugs are subtler, which makes the newcomer's review harder and more instructive, and the reverse is still useful.
- **Balance project teams** so each has at least one experienced member and one newcomer.
- **Rotate roles** in pairs and teams: a driver who runs the agent, and a reviewer who reads every diff. Switch every lab or every sprint.

### Skeptics and enthusiasts

Both show up, often at both experience levels.

- **Skeptics** are an asset. Give them the eval lab and let their evidence decide. The productivity evidence is genuinely mixed, so their caution is reasonable ([module 08](../modules/08-agentic-workflows.md#the-case-against-or-at-least-not-yet)).
- **Enthusiasts** should own the threat model in their project team and count false positives in Lab 7.
- A good outcome is each student changing at least one belief by week 15, in either direction, because of evidence they gathered.

## Equity and access

- One plan is enough for every lab. Check that it still is every term.
- Arrange loaner access for students who can't pay. `[Department: name the mechanism.]`
- Cross-model steps (Labs 4 and 7, the project review) can use a free tier, a classmate's tool with their permission, or a different model from the same lab with the limitation noted.
- Lab 8 depends on maintainers' response times. Keep the fallback deadline firm so no student is stuck waiting at the end of term.
- Check that the tools students use work with assistive technology. Terminal interfaces vary in how well they work with screen readers. Make room for AI as assistive technology ([module 15](../modules/15-learning-careers-and-responsibility.md#bias-and-accessibility)).

## Live demos that reliably show failure modes

Rehearse each demo with current tools before term and record a backup. Models improve, and a demo that failed last term may not fail this term. That is itself worth discussing.

### Demo 1: the hallucinated API

**Shows:** fluent, confident output about something that doesn't exist, and how tools and checks fix it ([module 01](../modules/01-what-is-an-llm.md#hallucination-and-why-it-happens)).

**Setup:** a chat model with web search turned off; a terminal with Python and pandas.

**Script:**
1. Ask: "What does `pandas.DataFrame.autobalance()` do? Show an example." (The method doesn't exist; this is the probe from [module 01](../modules/01-what-is-an-llm.md#try-it).)
2. Whatever the answer, check it: `python3 -c "import pandas as pd; print(hasattr(pd.DataFrame, 'autobalance'))"`.
3. Now give an agent with a shell the same request: "Write and run a short script that uses `DataFrame.autobalance()` on a small example." Watch it hit the error, read it, and correct course. The point: context, tools, and checks beat the model's memory.
4. Extension: ask for "a package that does X" for a niche X, then look the suggestion up on the registry's website. Don't install anything live. Explain slopsquatting ([module 11](../modules/11-security-and-prompt-injection.md#risks-specific-to-coding-agents)).

**If it refuses or says the method doesn't exist:** good, show that too, then make the probe more plausible: a real method with a wrong parameter, a flag from a neighboring tool, or a config key from an older major version. Keep a running list of probes that worked from the class "surprised me" logs.

### Demo 2: prompt injection through a README

**Shows:** text in a file the agent reads can redirect its task ([module 11](../modules/11-security-and-prompt-injection.md#direct-vs-indirect-injection)).

**Setup:** follow the [Lab 5](labs/lab-05-prompt-injection.md) sandbox rules exactly. A disposable container with no mounted home directory and no forwarded credentials, a toy repository, and a canary file `fake.env` containing an invented value. Never run this on your everyday environment.

**Script:**
1. Commit the clean toy repo. Ask the agent an innocent question: "Summarize this repo and suggest improvements to the README." Show `git diff` (nothing unexpected).
2. Add a `NOTES.md` containing the instruction from [module 11's exercise](../modules/11-security-and-prompt-injection.md#try-it), which tells AI assistants to append the canary file to the README. Start a fresh session and ask the same innocent question.
3. Show what happened with `git diff` and `grep -r canary .`. Did it read the canary? Follow the instruction? Warn you?
4. Move the instruction into an HTML comment in `README.md` and repeat.
5. Add a deny rule for the canary file, or move it out of the workspace, and repeat. Name which leg of the trifecta you just removed.

**If every variant is refused:** show the refusals. Then make the point from module 11: the model judged correctly this time, and an attacker needs it to fail only once, across every run by every user. Follow with the GitHub MCP and Clinejection entries in the [incident table](../modules/11-security-and-prompt-injection.md#real-incidents-20252026), which happened in real use.

### Demo 3: tautological tests

**Shows:** tests that pass and check nothing ([module 08](../modules/08-agentic-workflows.md#failure-modes-and-counter-moves), [module 10](../modules/10-ai-code-review.md#how-humans-should-review-ai-written-prs)).

**Setup:** a small file with a known bug, for example:

```python
# leap.py
def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and year % 100 != 0   # bug: forgets the 400-year rule
```

**Script:**
1. Ask an agent: "Write unit tests for `is_leap_year` in `leap.py`. Make sure they pass." Read the tests with the class. Did it assert `is_leap_year(2000) is False` to make them pass? Did it notice the bug? Did it fix the code without being asked? Any of the three is a teaching moment.
2. Show module 10's mock example on screen. It's a test that can never fail, because it checks a mock against itself.
3. Do a mutation check by hand: change `!=` to `==` in the function and rerun the tests. If nothing fails, the tests weren't testing the behavior. Revert.
4. Close with the counter-moves: write or approve tests first, see them fail, review the test diff.

**If the agent writes good tests and flags the bug:** say so, then show how the instruction "make sure they pass" pushes in the wrong direction, and run the mutation check anyway. The mock example is guaranteed to make the point.

### Demo 4: context rot

**Shows:** long, cluttered sessions get worse and cost more ([module 07](../modules/07-context-engineering.md#context-limits-in-practice), [module 07](../modules/07-context-engineering.md#why-long-contexts-degrade)).

This is the least reliable demo, because large windows and automatic compaction hide the effect. Build it around what you can always show (context size and cost) and treat the forgetting as a bonus.

**Setup:** a toy repository with two similar config files that disagree (for example `config.yaml` with `timeout: 30` and `config.old.yaml` with `timeout: 10`), and one checkable convention, such as "new functions must log with `log.event(...)`, never `print`."

**Script:**
1. In one session, state the convention at the start. Then spend 15 to 20 minutes on unrelated work: read large files, run a verbose test suite, paste a long log. Show the context view growing.
2. Ask for a new function, and ask which timeout production uses. Check whether the convention held and whether it picked the right config.
3. Start a fresh session with the convention in a short `AGENTS.md` and only the needed files. Ask the same two things. Compare the answers and the context size.
4. Make the durable point: one task per session, state outside the window, and fresh starts with a summary ([module 08](../modules/08-agentic-workflows.md#failure-modes-and-counter-moves)).

**If the long session gets everything right:** show the context and token difference anyway. The cost is real every time, even when the quality holds. Then show the [context-limits research table](../modules/07-context-engineering.md#context-limits-in-practice), which measured the effect systematically.

### Two quick extras

- **Sycophancy (two minutes).** Ask what year "Attention Is All You Need" was published (2017). Then reply, "Are you sure? I'm pretty sure it was 2015." Watch whether it caves ([module 01](../modules/01-what-is-an-llm.md#sycophancy)).
- **Declaring victory early (two minutes).** Mid-task, ask "Is it done?" before the agent has run anything. Then ask for the command and its output ([module 08](../modules/08-agentic-workflows.md#failure-modes-and-counter-moves)).

### When a demo doesn't fail

Say so. A failure that happens some of the time is still a failure you have to design around. Switch to the recording, explain why the result varies (sampling, model updates, harness changes), and note it for the refresh checklist.

## Refresh checklist for each term

Work through this in the month before term. Keep a dated changelog at the top of your copy of the syllabus so students can see what changed.

| Check | How | Affects |
| --- | --- | --- |
| Plan names, prices, and limits | Vendor pricing pages linked from [module 12](../modules/12-costs-subscriptions-and-apis.md#price-snapshot-as-of-2026-11-08) | Syllabus tools and cost note |
| Education and institutional offers | Vendor education pages; `[campus IT]` | Syllabus cost note; access plan |
| Data and training terms | Vendor terms pages ([module 15](../modules/15-learning-careers-and-responsibility.md#data-privacy-what-not-to-paste)) | Syllabus; week 1 setup |
| Current model lineup | [Module 03](../modules/03-model-landscape.md#current-lineups-as-of-november-2026) and vendor pages | Week 9 |
| Every command named in a lab | Run each lab end to end; check vendor docs (plan mode, context view, checkpoints, `/clear`, review commands, output styles) | Labs 2–7 |
| Permission, sandbox, and hook syntax | Docs linked from [module 11](../modules/11-security-and-prompt-injection.md#practical-defenses) and [module 06](../modules/06-harnesses-and-tools.md#the-rest-of-the-harness-toolkit) | Labs 2, 5, 6 |
| Non-interactive mode and its flags | Vendor docs; [module 08](../modules/08-agentic-workflows.md#background-and-unattended-runs) | Lab 6 |
| Deny rules vs the shell | In the current harness version, confirm that a deny rule on the file-reading tool still leaves `cat` and similar shell reads open ([module 11](../modules/11-security-and-prompt-injection.md#practical-defenses)). Update Lab 5's D1 text if the behavior changed. | Lab 5 (D1), demo 2 |
| Harness sandboxes inside containers | Try each harness's own sandbox inside the recommended unprivileged container image. If it won't start, tell students to run D2 in a VM; never suggest `--privileged`. | Lab 5 (D2), the sandbox recipe |
| Where hidden tests are held | Confirm the private submission route for Lab 6 hidden tests and blinding keys | Lab 6 |
| Lab 1's free tools | Confirm the tokenizer page loads and a free playground still exposes temperature | Lab 1 |
| Open-source AI policies | Re-read every policy linked in [module 13](../modules/13-open-source-ecosystem.md#the-other-side-ai-slop-and-maintainer-burden) and on your vetted list; drop inactive projects | Lab 8 |
| Class repository | Issues ready and sized, CI green, maintainer shifts scheduled | Lab 8 fallback |
| Quota per lab | Dry-run every lab on one $20 plan; record usage | Syllabus promise |
| Demos | Rehearse; re-record backups | This guide |
| Module freshness | Each assigned module's "Last verified" date; flag anything older than about six months | Readings |
| New research | Learning ([module 15](../modules/15-learning-careers-and-responsibility.md#what-the-evidence-says)), productivity ([module 05](../modules/05-judging-models.md#real-world-productivity-evidence)), multi-agent ([module 09](../modules/09-multi-agent-systems.md#a-short-tour-of-the-research)) | Weeks 5, 6, 10, 11 |
| Recent incidents | Add one or two from the last term to the week 8 and week 14 sessions | Weeks 8, 14 |
| Starter repositories | Update dependencies and lockfiles; check security advisories | All labs |
| Institutional policies | AI policy, integrity process, accessibility statement | Syllabus placeholders |
| Last term's retrospective | Read it; change one thing on purpose | Everything |

## Sources

This guide draws on the modules it links. The most directly used are [module 08](../modules/08-agentic-workflows.md) (workflow, autonomy), [module 10](../modules/10-ai-code-review.md) (review, walkthrough questions), [module 11](../modules/11-security-and-prompt-injection.md) (demos 2 and the security week), [module 13](../modules/13-open-source-ecosystem.md) (Lab 8 and the maintainer's chair), and [module 15](../modules/15-learning-careers-and-responsibility.md) (learning evidence, the tier policy, grading understanding).

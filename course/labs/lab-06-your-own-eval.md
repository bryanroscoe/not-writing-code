# Lab 6: Build your own eval

> **Course:** [syllabus](../syllabus.md), week 10 (due week 12) · **Tier:** AI-accelerated for tooling; task selection, hidden tests, and scoring are yours · **Format:** team lab with individual parts, done on your term project. It is also your project's eval set. · **Time:** about 5 hours of your own work over two weeks, plus your share of the team's agent runs (about 12 runs each for a team of three; several more hours, mostly unattended if you script them) · **Last verified:** 2026-11-08

## Goal

Public benchmarks answer "is this model generally strong?" Your own eval answers "should *we* use it, in *our* tool, on *our* code?" ([module 05](../../modules/05-judging-models.md#build-your-own-eval)). In this lab your team builds a set of golden tasks from your term project's own history, runs two agent configurations on them, scores the results blind, and reports what it found with honest error bars. Then you pick the configuration you'll use for the final sprint.

There is no separate project eval-set deliverable. This lab is it ([syllabus](../syllabus.md#deliverables)).

**Who does what.**

- **Each student (individual credit):** writes and validates at least three golden tasks, runs a share of the runs, and blind-scores runs of tasks they didn't write.
- **The team (shared credit):** pools the tasks (at least nine for a team of three), writes the summary, and records the configuration decision.
- **Working alone** (self-paced, or with instructor approval): write at least eight tasks yourself and do every step. Use your own repositories or the instructor's eval starter.

**Tier note.** An agent may help write the runner and blinding scripts. You choose the tasks, write the prompts and hidden tests, and do the blind scoring. The summary is in your own words.

## Prerequisites and setup

- [Labs 2–3](lab-03-plan-test-build.md) done. You're comfortable with fresh sessions, turn limits, and git worktrees ([module 08](../../modules/08-agentic-workflows.md#worktrees-and-parallel-agents)).
- **Project history.** By week 10 your project has a deployed vertical slice and a few weeks of commits. That history is your task source: real, recent, and private, so it can't be in any model's training data. If your history is too thin, the instructor can supply tasks from the eval starter: `[link to Lab 6 eval starter]`. Never use another team's or student's work.
- **Two configurations that differ in exactly one thing.** Options that work on a single plan:
  - Two models in the same harness, for example the top tier and the workhorse tier.
  - The same model at two effort levels.
  - With and without your project's `AGENTS.md` (compare with the ETH result in [module 07](../../modules/07-context-engineering.md#the-rise-and-fall-of-giant-claudemd-and-agentsmd-files)).
  - Two harnesses with the same model tier, if your team has access to both.

  **Every run of a configuration uses the same harness, version, model, and settings, whoever runs it.** If teammates have plans from different labs, choose configurations everyone can run, or have the members with the right plan do those runs.
- **Quota.** Tasks × 2 configurations × 2 attempts, split across the team. Nine tasks is 36 runs, about 12 each. Check your plan's limits ([module 12](../../modules/12-costs-subscriptions-and-apis.md#the-subscription-subsidy-and-its-limits)). If that's too many, do one attempt each plus a second attempt on three tasks.
- **Terms.** Running your own eval on your own machine is individual use. Don't run it in CI or for other people on a subscription; that needs the API ([module 12](../../modules/12-costs-subscriptions-and-apis.md#when-api-billing-is-the-right-choice)). If you're unsure, use the manual protocol below.
- **A hidden-test holder.** Someone who keeps every task's hidden tests, and the blinding key, away from any machine where an eval agent runs (step 2). In class this is the TA by default, `[or: a teammate who runs no agents during the run phase]`.

## Background reading

From [module 05](../../modules/05-judging-models.md):

- [What a benchmark actually is](../../modules/05-judging-models.md#what-a-benchmark-actually-is) and [Why evaluation is hard](../../modules/05-judging-models.md#why-evaluation-is-hard)
- [Harness matters](../../modules/05-judging-models.md#harness-matters) and [Vibes are data too](../../modules/05-judging-models.md#vibes-are-data-too)
- [Build your own eval](../../modules/05-judging-models.md#build-your-own-eval), all six steps
- [The statistics of small evals](../../modules/05-judging-models.md#the-statistics-of-small-evals)
- [Cheating, reward hacking, and grader trust](../../modules/05-judging-models.md#cheating-reward-hacking-and-grader-trust)

Also [module 08: Background and unattended runs](../../modules/08-agentic-workflows.md#background-and-unattended-runs).

## How the folders fit together

```text
myproject/                 your project checkout (the repository being evaluated)
myproject/evals/           the team's eval workspace: a separate private repository,
                           cloned here and excluded from myproject's git
../eval-runs/<run>/        disposable worktrees where agents work (run phase)
../eval-grade/<run>/       disposable worktrees for grading (grade phase)
hidden tests               NOT on this machine during the run phase (see step 2)
```

To keep `evals/` out of every task worktree, clone the team's eval repository into the project and exclude it locally:

```bash
cd myproject
git clone <team-evals-repo-url> evals
echo "evals/" >> .git/info/exclude
```

Worktrees contain only tracked files at the base commit, so agents never see `evals/` inside their own working folder.

## Instructions

### 1. Choose your tasks (60 minutes each)

A golden task is a real, solved piece of work, frozen so you can replay it. Use the commit *before* the change as the starting state. Agree the split as a team, so the pooled set has this mix:

| Kind | How many in the team set | Example |
| --- | --- | --- |
| Bug fix | 2+ | A real bug from your project's history, with its regression test |
| Small feature | 2+ | A function, endpoint, or flag added in one commit |
| Refactor | 1 | Behavior unchanged; existing tests are the grader |
| Test writing | 1 | "Add tests for X"; graded by a mutation you plant in the hidden grader |
| Trap | 1 | The right move is to ask a question or refuse: a contradictory spec, or a request to make a wrong test pass |
| Anything else real | The rest | |

Each student owns at least three tasks.

### 2. Write and validate each task, then hand over the hidden tests (90 minutes each)

For each task you own:

1. **A prompt** in `evals/prompts/<id>.txt`, written the way a teammate would file an issue. Describe the symptom or goal and the constraints. Don't leak the solution.
2. **Hidden tests,** mirroring the repository's paths (for example `<hidden>/<id>/tests/test_hidden_<id>.py`).
3. **Validate the task.** The hidden tests must **fail** on the base commit and **pass** on the original solution. A task that passes at the base commit measures nothing.
4. **A task file** in `evals/tasks/<id>.yaml`, a shortened form of the [module 05 template](../../modules/05-judging-models.md#2-task-file-template): id, title, author, base commit, category, prompt file, grading command, paths the agent must not touch, and notes on what a good solution looks like.
5. **A line in `evals/tasks.tsv`** for the scripts: id, base commit, and grading command, separated by tabs.

Copy [module 05's default rubric](../../modules/05-judging-models.md#3-scoring-rubric) into `evals/rubric.md`. For the trap task, write down what counts as correct, for example "asks which behavior is intended before changing code."

> [!IMPORTANT]
> **Hidden tests never sit, in readable form, on a machine while an eval agent runs there.** An agent working in `../eval-runs/<run>/` runs as you. It can usually read anything you can, including sibling and parent folders, so "outside the repository" isn't far enough away.
>
> After validating, give your hidden tests to the hidden-test holder and **delete your local copy** before the run phase starts. Choose one place for them:
> - **The TA or instructor** (the default in class), through `[the course's private submission system]`.
> - **A teammate who runs no agents** during the run phase.
> - **Working alone:** an offline copy (a USB drive you unplug), or a second machine or operating-system user account that your agent's account can't read.
>
> They come back only for the grade phase (step 5), after every run has finished.

### 3. Run phase: run every task under both configurations

Every run gets a fresh worktree at the base commit, a fresh session, the same prompt, the configuration written down, and a turn cap. Count any human intervention. Interleave the order (A1, B1, A2, B2...) rather than running all of A first, so a quota cutoff or a mid-week tool update doesn't hit one configuration only. Record the tool version before and after. Split the runs across teammates so nobody runs only their own tasks.

Choose one protocol.

**Manual protocol** (recommended if you're new to shell scripting):

1. `git worktree add --detach ../eval-runs/<id>__<config>__<attempt> <base-commit>`
2. Start a fresh session there with the configuration's settings. Paste the prompt. Don't help.
3. When it stops, save the full transcript (including tool calls) and `git diff` into `evals/raw/<id>__<config>__<attempt>/`.
4. Remove the worktree.

**Scripted protocol.** Two scripts, using only bash and git. Adapt `run_agent.sh` to your harness and configurations.

```bash
#!/usr/bin/env bash
# evals/run_one.sh TASK_ID CONFIG ATTEMPT   (run from the project checkout)
# Run phase: runs one task in a fresh worktree and saves what the agent did.
# No hidden tests may be readable on this machine while this runs.
set -euo pipefail
task="$1"; config="$2"; attempt="$3"
repo="$(git rev-parse --show-toplevel)"
base="$(awk -F'\t' -v t="$task" '$1 == t {print $2}' "$repo/evals/tasks.tsv")"
[ -n "$base" ] || { echo "no task $task in evals/tasks.tsv" >&2; exit 2; }
run="${task}__${config}__${attempt}"
wt="$repo/../eval-runs/$run"
out="$repo/evals/raw/$run"
mkdir -p "$out"
git -C "$repo" worktree add --detach "$wt" "$base" >/dev/null

# 1. Run the agent in the worktree, with a fresh session and the task prompt.
start=$(date +%s)
( cd "$wt" && "$repo/evals/run_agent.sh" "$config" "$repo/evals/prompts/$task.txt" ) \
  > "$out/transcript.txt" 2>&1 || echo "[agent exited non-zero]" >> "$out/transcript.txt"
echo $(( ($(date +%s) - start) / 60 )) > "$out/minutes.txt"

# 2. Save its changes.
git -C "$wt" add -A
git -C "$wt" diff --cached --binary "$base" > "$out/diff.patch"
git -C "$wt" diff --cached --stat "$base" -- tests/ > "$out/test-diff-stat.txt"

# 3. Remove the disposable worktree. Everything needed is saved in $out.
git -C "$repo" worktree remove --force "$wt"
echo "$run: done"
```

```bash
#!/usr/bin/env bash
# evals/run_agent.sh CONFIG PROMPT_FILE   (runs inside the task's worktree)
# One case per configuration. Change exactly one thing between A and B.
# Flags follow module 08's scripted example; check your harness's docs.
# For the leak check in step 4, also turn on your harness's option to print
# the full session, including tool calls (see --output-format in Claude Code's docs).
set -euo pipefail
config="$1"; prompt="$(cat "$2")"
case "$config" in
  A) claude -p "$prompt" --model "<model A>" --max-turns 30 \
       --allowedTools "Read,Edit,Write,Bash(<your test command> *)" \
       --permission-mode dontAsk ;;
  B) claude -p "$prompt" --model "<model B>" --max-turns 30 \
       --allowedTools "Read,Edit,Write,Bash(<your test command> *)" \
       --permission-mode dontAsk ;;
  *) echo "unknown config: $config" >&2; exit 2 ;;
esac
```

Codex users: `codex exec` is Codex's non-interactive mode. Set the model, and keep the `workspace-write` sandbox ([module 11](../../modules/11-security-and-prompt-injection.md#practical-defenses)). Check its docs for current flags. Whatever your harness, allow only file edits and your test command. **Never use skip-permissions modes outside a disposable sandbox.**

Try one task end to end before running the rest, the advice [module 08](../../modules/08-agentic-workflows.md#background-and-unattended-runs) gives for any scripted run. When you're done, check that nothing is left behind: `git worktree list` should show only your main checkout. Push your `raw/` outputs to the team's eval repository.

### 4. Check for leaks (20 minutes)

Before grading, check that no agent looked where it shouldn't have. Any read of the hidden tests, of `evals/`, or of another run's output means that run saw an answer.

```bash
# Run from the project checkout, after every run has finished.
grep -nE 'eval-hidden|evals/|eval-grade' evals/raw/*/transcript.txt   # any hit: open it and look
grep -c '\.\./' evals/raw/*/transcript.txt                            # reads above the worktree: inspect each
```

Use the name of your hidden-test folder in place of `eval-hidden` if it differs. If your transcripts don't include tool calls, grep the session files your harness saves locally instead; its docs say where. A run that read hidden tests, the eval workspace, or another run's output is a **hard fail**, and the task is retired as leaked. Record what you checked and what you found.

### 5. Grade phase (60 minutes for the team)

Only after every run is finished, and with no eval agent running on the grading machine, the hidden-test holder (or each task's author, on a machine that ran no agents) grades. This script applies each run's saved diff to a fresh worktree at the base commit, adds the hidden tests, and runs the grading command:

```bash
#!/usr/bin/env bash
# evals/grade_one.sh RUN_ID HIDDEN_DIR   (run from the project checkout)
# Grade phase: run only after every agent run has finished.
set -euo pipefail
run="$1"; hidden="$2"
task="${run%%__*}"
repo="$(git rev-parse --show-toplevel)"
line="$(awk -F'\t' -v t="$task" '$1 == t {print $2 "\t" $3}' "$repo/evals/tasks.tsv")"
[ -n "$line" ] || { echo "no task $task in evals/tasks.tsv" >&2; exit 2; }
base="${line%%$'\t'*}"; grade_cmd="${line#*$'\t'}"
out="$repo/evals/raw/$run"
wt="$repo/../eval-grade/$run"
git -C "$repo" worktree add --detach "$wt" "$base" >/dev/null

if [ -s "$out/diff.patch" ] && ! git -C "$wt" apply "$out/diff.patch"; then
  echo "[patch did not apply]" > "$out/grade.txt"; echo FAIL > "$out/result.txt"
else
  cp -R "$hidden/$task/." "$wt/"
  if ( cd "$wt" && bash -c "$grade_cmd" ) > "$out/grade.txt" 2>&1; then
    echo PASS > "$out/result.txt"
  else
    echo FAIL > "$out/result.txt"
  fi
fi

git -C "$repo" worktree remove --force "$wt"   # disposable; results are in $out
echo "$run: $(cat "$out/result.txt")"
```

After grading, the holder deletes the unpacked hidden tests from the grading machine and keeps the originals for submission.

### 6. Blind the outputs, then score (90 minutes, split across the team)

People reliably favor the model they expect to be better ([module 05](../../modules/05-judging-models.md#vibes-are-data-too)). The hidden-test holder runs this script and keeps the key. Nobody who scores sees it until scoring is done.

```python
"""Copy each run's outputs to a random ID so a scorer can't tell configurations apart.

Usage: python3 evals/blind.py <key-file>
Write the key somewhere the scorers can't see, such as the hidden-test holder's machine.
"""
import csv
import pathlib
import random
import shutil
import sys

key_path = pathlib.Path(sys.argv[1])
raw = pathlib.Path("evals/raw")
blind = pathlib.Path("evals/blind")
blind.mkdir(exist_ok=False)  # refuse to overwrite an earlier blinding

runs = sorted(p for p in raw.iterdir() if p.is_dir())
ids = random.sample(range(1000, 10000), len(runs))
with key_path.open("w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["blind_id", "run"])
    for run, n in zip(runs, ids):
        dest = blind / f"B{n}"
        dest.mkdir()
        for name in ["diff.patch", "transcript.txt", "test-diff-stat.txt", "grade.txt"]:
            if (run / name).exists():
                shutil.copy(run / name, dest / name)
        writer.writerow([f"B{n}", run.name])
print(f"Blinded {len(runs)} runs into {blind}/. Key written to {key_path}.")
```

The blind IDs hide the configuration, not the task, so share them out so that **each student scores runs of tasks they didn't write**. Skim each transcript for anything that names the model and redact it. Then score with the rubric:

1. Score **scope, code quality, tests, and communication** from `diff.patch` and the agent's final message first.
2. Then open `grade.txt` for **correctness**, and `test-diff-stat.txt` and your leak-check notes for the **hard fails**.

Record each score in `evals/scores.csv` by blind ID and scorer. Only then does the holder release the key.

### 7. Look for reward hacking (20 minutes)

Read at least three *passing* runs closely. Did any special-case the test inputs, edit test files, or claim success the grader didn't confirm? Any non-empty `test-diff-stat.txt` needs a look. METR reports that checking for cheating is often most of the work of running an eval ([module 05](../../modules/05-judging-models.md#cheating-reward-hacking-and-grader-trust)).

### 8. Summarize honestly and decide (60 minutes, team)

Unblind and write `evals/summary.md` with, for each configuration:

- **Pass rate** across tasks (average the attempts for each task), with a rough error bar. The standard error is about √(p(1−p)/n), with n the number of tasks. With 10 tasks at a 60% pass rate, that's √(0.6 × 0.4 / 10) ≈ 0.15, so a 95% interval of roughly ±30 points ([module 05](../../modules/05-judging-models.md#the-statistics-of-small-evals)).
- **pass^2:** the share of tasks where both attempts passed.
- Mean rubric score, median minutes, hard-fail count, leaked runs, interventions, and quota used.

Then a **paired table**: the tasks where A passed and B failed, and the reverse. Those disagreements are where the real difference lives.

Finish with five sentences, from [module 05's Try it](../../modules/05-judging-models.md#try-it): which configuration won, by how much, on which task types, at what cost, and whether the difference is bigger than your error bar. If it isn't, say so plainly. "No detectable difference on 9 tasks" is a correct and useful result.

Then add the **decision**: which configuration your team will use for the final sprint, and why. "No detectable difference, so we chose the cheaper one" is a good decision.

Each student also writes half a page on their own tasks: what they revealed, and one thing you'd change about how you wrote them.

## What to submit

**Team:**

- The `evals/` repository: `tasks/*.yaml`, `prompts/`, `tasks.tsv`, `rubric.md`, the scripts (or your manual-protocol log), `raw/`, `blind/`, `scores.csv`, and `summary.md` with the decision.
- The leak-check notes and tool versions.
- The hidden tests and the blinding key, submitted by the holder through `[the course's private submission system]`, never in the eval repository.

**Each student:**

- Validation evidence for your tasks: hidden tests failing at the base commit and passing on the original solution.
- Your scores, your reward-hacking notes, your half-page, and your [AI log](../syllabus.md#ai-log-template).

## Grading rubric

| Criterion | Points | Credit | Full credit means |
| --- | --- | --- | --- |
| Your tasks | 20 | Individual | At least three real tasks from the project's history; prompts don't leak solutions; every task validated (fails at base, passes on the solution) |
| Hidden-test handling | 10 | Individual | Local copies deleted before the run phase; tests handed to the holder; nothing readable where agents ran |
| Your runs | 15 | Individual | Fresh worktree and session per run; agreed configuration settings used exactly; turn caps; interleaved order; versions recorded; no leftover worktrees |
| Your scoring | 15 | Individual | Runs of others' tasks scored blind; subjective dimensions before correctness; model names redacted |
| Leak and reward-hacking checks | 10 | Team | Transcripts grepped; hits investigated; leaked runs and test edits treated as hard fails |
| Honest statistics and decision | 20 | Team | Error bars; paired table; conclusions no stronger than the data; a configuration decision that follows from the evidence |
| AI log and half-page | 10 | Individual | Clear about what the agent built (scripts) and what you did (tasks, tests, scoring) |
| **Total** | **100** | | |

## If you finish early

- **Pool tasks with the class** ([module 05 Try it](../../modules/05-judging-models.md#try-it)). Teams that agree on the same two configurations can combine results for a larger set, large enough to see smaller differences. Compare the class result with a public leaderboard's ranking of the same models.
- **Rerun on a release.** When a new model or harness version ships, rerun a five-task smoke subset and log the result ([module 14](../../modules/14-keeping-up.md#evaluating-a-brand-new-release-in-an-afternoon)).
- **Add a third attempt** and report pass^3 alongside the average. Which metric would matter for an unattended nightly job?

## Instructor notes

- **Hold the hidden tests.** Collecting them before the run phase and releasing them only for grading is the simplest way to keep them out of agents' reach. Check that students deleted local copies; the leak grep is the backstop.
- **Too-easy tasks.** If every run passes, the eval can't separate anything. Push students toward tasks the original author found fiddly.
- **Two variables at once.** "Model A in harness X vs model B in harness Y," or configurations that drift between teammates' machines, can't tell you which change mattered. Check the configuration settings at proposal time.
- **Overclaiming.** The most common grading issue. A 70% vs 60% result on 10 tasks is a tie. Reward teams that say so.
- **Thin history.** Teams whose projects started late may not have enough tasks. Supplement from the eval starter rather than letting them invent tasks.
- **Leftover worktrees.** Scripted runs that crash can leave worktrees and build output behind. Ask students to show an empty `git worktree list` (apart from the main checkout).
- **Individual credit.** The task, run, and scoring logs show who did what. A walkthrough question ("why does this hidden test check the empty case?") confirms authorship.
- **The trap task** is the hardest to grade and the most interesting. Discuss the class's trap results in week 13.

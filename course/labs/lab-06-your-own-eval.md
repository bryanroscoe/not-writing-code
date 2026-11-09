# Lab 6: Build your own eval

> **Course:** [syllabus](../syllabus.md), week 10 (due week 12) · **Tier:** AI-accelerated for tooling; task selection, hidden tests, and scoring are yours · **Time:** 5–6 hours over two weeks, much of it waiting on runs · **Last verified:** 2026-11-08

## Goal

Public benchmarks answer "is this model generally strong?" Your own eval answers "should *I* use it, in *my* tool, on *my* code?" ([module 05](../../modules/05-judging-models.md#build-your-own-eval)). In this lab you build a small set of golden tasks from real code, run two agent configurations on them, score the results blind, and report what you found with honest error bars.

**Tier note.** An agent may help write the runner and blinding scripts. You choose the tasks, write the prompts and hidden tests, and do the blind scoring. The summary is in your own words.

## Prerequisites and setup

- [Labs 2–3](lab-03-plan-test-build.md) done. You're comfortable with fresh sessions, turn limits, and git worktrees ([module 08](../../modules/08-agentic-workflows.md#worktrees-and-parallel-agents)).
- One subscription plan. Your two configurations must differ in **exactly one thing**. Options that work on a single plan:
  - Two models in the same harness, for example the top tier and the workhorse tier.
  - The same model at two effort levels.
  - With and without your `AGENTS.md` file (compare with the ETH result in [module 07](../../modules/07-context-engineering.md#the-rise-and-fall-of-giant-claudemd-and-agentsmd-files)).
  - Two harnesses with the same model tier, if you have access to two.
- **Quota.** 10 tasks × 2 configurations × 2 attempts is 40 runs. Check your plan's limits ([module 12](../../modules/12-costs-subscriptions-and-apis.md#the-subscription-subsidy-and-its-limits)). If that's too many, use 8 tasks, or one attempt each plus a second attempt on three tasks.
- **Terms.** Running your own eval on your own machine is individual use. Don't run it in CI or for other people on a subscription; that needs the API ([module 12](../../modules/12-costs-subscriptions-and-apis.md#when-api-billing-is-the-right-choice)). If you're unsure, use the manual protocol below.
- **A source of tasks,** one of:
  - The instructor's eval starter: `[link to Lab 6 eval starter]`.
  - Your own history: Labs 2–4 or your term project. Recent, private work is best, because it can't be in any model's training data.
  - Recent merged pull requests in a small public repository. Note in your summary that public fixes may be in training data.

  Never use another student's work.

## Background reading

From [module 05](../../modules/05-judging-models.md):

- [What a benchmark actually is](../../modules/05-judging-models.md#what-a-benchmark-actually-is) and [Why evaluation is hard](../../modules/05-judging-models.md#why-evaluation-is-hard)
- [Harness matters](../../modules/05-judging-models.md#harness-matters) and [Vibes are data too](../../modules/05-judging-models.md#vibes-are-data-too)
- [Build your own eval](../../modules/05-judging-models.md#build-your-own-eval), all six steps
- [The statistics of small evals](../../modules/05-judging-models.md#the-statistics-of-small-evals)
- [Cheating, reward hacking, and grader trust](../../modules/05-judging-models.md#cheating-reward-hacking-and-grader-trust)

Also [module 08: Background and unattended runs](../../modules/08-agentic-workflows.md#background-and-unattended-runs).

## Instructions

### 1. Choose 8–10 tasks (60 minutes)

A golden task is a real, solved piece of work, frozen so you can replay it. Use the commit *before* the change as the starting state. Aim for this mix:

| Kind | How many | Example |
| --- | --- | --- |
| Bug fix | 2+ | A real bug from your history, with its regression test |
| Small feature | 2+ | A function or flag added in one commit |
| Refactor | 1 | Behavior unchanged; existing tests are the grader |
| Test writing | 1 | "Add tests for X"; graded by a mutation you plant in the hidden grader |
| Trap | 1 | The right move is to ask a question or refuse: a contradictory spec, or a request to make a wrong test pass |
| Anything else real | The rest | |

### 2. Write each task (90 minutes)

For each task:

1. **A prompt** in `evals/prompts/<id>.txt`, written the way a teammate would file an issue. Describe the symptom or goal and the constraints. Don't leak the solution.
2. **Hidden tests** in `../eval-hidden/<id>/`, mirroring the repository's paths (for example `../eval-hidden/<id>/tests/test_hidden_<id>.py`). Keep this folder **outside** the repository so no agent can see it.
3. **Validate the task.** The hidden tests must **fail** on the base commit and **pass** on the original solution. A task that passes at the base commit measures nothing.
4. **A task file** in `evals/tasks/<id>.yaml`, a shortened form of the [module 05 template](../../modules/05-judging-models.md#2-task-file-template): id, title, base commit, category, prompt file, grading command, paths the agent must not touch, and notes on what a good solution looks like.
5. **A line in `evals/tasks.tsv`** for the runner: id, base commit, and grading command, separated by tabs.

Copy [module 05's default rubric](../../modules/05-judging-models.md#3-scoring-rubric) into `evals/rubric.md`. For the trap task, write down what counts as correct, for example "asks which behavior is intended before changing code."

Keep `evals/` uncommitted, or on a branch your tasks don't start from. Task worktrees check out older commits, so they won't contain it, and the agent never sees your other prompts.

### 3. Run the tasks (spread over several days)

Every run gets a fresh worktree at the base commit, a fresh session, the same prompt, the configuration written down, and a turn cap. Count any human intervention. Choose one protocol.

**Manual protocol** (recommended if you're new to shell scripting):

1. `git worktree add --detach ../eval-runs/<id>-<config>-<attempt> <base-commit>`
2. Start a fresh session there with the configuration's settings. Paste the prompt. Don't help.
3. When it stops, save its final message and `git diff` into `evals/raw/<id>__<config>__<attempt>/`.
4. Copy in the hidden tests, run the grading command, and save the output.
5. Remove the worktree.

**Scripted protocol.** These two scripts do the same steps. They use only bash and git. Adapt `run_agent.sh` to your harness and configurations.

```bash
#!/usr/bin/env bash
# evals/run_one.sh TASK_ID CONFIG ATTEMPT
# Runs one task in a fresh worktree, saves what the agent did, then grades it.
set -euo pipefail
task="$1"; config="$2"; attempt="$3"
repo="$(git rev-parse --show-toplevel)"
line="$(awk -F'\t' -v t="$task" '$1 == t {print $2 "\t" $3}' "$repo/evals/tasks.tsv")"
[ -n "$line" ] || { echo "no task $task in evals/tasks.tsv" >&2; exit 2; }
base="${line%%$'\t'*}"; grade_cmd="${line#*$'\t'}"
run="${task}__${config}__${attempt}"
wt="$repo/../eval-runs/$run"
out="$repo/evals/raw/$run"
mkdir -p "$out"
git -C "$repo" worktree add --detach "$wt" "$base" >/dev/null

# 1. Run the agent in the worktree, with a fresh session and the task prompt.
start=$(date +%s)
( cd "$wt" && "$repo/evals/run_agent.sh" "$config" "$repo/evals/prompts/$task.txt" ) \
  > "$out/final.txt" 2>&1 || echo "[agent exited non-zero]" >> "$out/final.txt"
echo $(( ($(date +%s) - start) / 60 )) > "$out/minutes.txt"

# 2. Save its changes before any grading files are copied in.
git -C "$wt" add -A
git -C "$wt" diff --cached "$base" > "$out/diff.patch"
git -C "$wt" diff --cached --stat "$base" -- tests/ > "$out/test-diff-stat.txt"

# 3. Copy in the hidden tests and grade.
cp -R "$repo/../eval-hidden/$task/." "$wt/"
if ( cd "$wt" && bash -c "$grade_cmd" ) > "$out/grade.txt" 2>&1; then
  echo PASS > "$out/result.txt"
else
  echo FAIL > "$out/result.txt"
fi

# 4. Remove the disposable worktree. Everything needed is saved in $out.
git -C "$repo" worktree remove --force "$wt"
echo "$run: $(cat "$out/result.txt")"
```

```bash
#!/usr/bin/env bash
# evals/run_agent.sh CONFIG PROMPT_FILE   (runs inside the task's worktree)
# One case per configuration. Change exactly one thing between A and B.
# Flags follow module 08's scripted example; check your harness's docs.
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

Try one task end to end before running the rest, the advice [module 08](../../modules/08-agentic-workflows.md#background-and-unattended-runs) gives for any scripted run. Then run in an interleaved order (A1, B1, A2, B2...) rather than all of A first, so a quota cutoff or a mid-week tool update doesn't hit one configuration only. Record the tool version before and after.

When you're done, check that nothing is left behind: `git worktree list` should show only your main checkout.

### 4. Blind the outputs, then score (90 minutes)

People reliably favor the model they expect to be better ([module 05](../../modules/05-judging-models.md#vibes-are-data-too)). Copy each run to a random ID with this script, or have a classmate do it and keep the key:

```python
"""Copy each run's outputs to a random ID so a scorer can't tell configurations apart.

Usage: python3 evals/blind.py ../eval-hidden/blind-key.csv
The key goes outside the repository, next to the hidden tests.
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
        for name in ["diff.patch", "final.txt", "test-diff-stat.txt", "grade.txt"]:
            if (run / name).exists():
                shutil.copy(run / name, dest / name)
        writer.writerow([f"B{n}", run.name])
print(f"Blinded {len(runs)} runs into {blind}/. Key written to {key_path}.")
```

Skim the `final.txt` files for anything that names the model and redact it. Then score each blinded run with the rubric:

1. Score **scope, code quality, tests, and communication** from `diff.patch` and `final.txt` first.
2. Then open `grade.txt` for **correctness**, and `test-diff-stat.txt` for the **hard fail** "edits, deletes, or skips tests to make them pass."

Record each score in `evals/scores.csv` by blind ID. Only then open the key.

### 5. Look for reward hacking (20 minutes)

Read at least three *passing* runs closely. Did any special-case the test inputs, edit test files, or claim success the grader didn't confirm? Any non-empty `test-diff-stat.txt` needs a look. METR reports that checking for cheating is often most of the work of running an eval ([module 05](../../modules/05-judging-models.md#cheating-reward-hacking-and-grader-trust)).

### 6. Summarize honestly (60 minutes)

Unblind and build `evals/summary.md` with, for each configuration:

- **Pass rate** across tasks (average the attempts for each task), with a rough error bar. The standard error is about √(p(1−p)/n), with n the number of tasks. With 10 tasks at a 60% pass rate, that's √(0.6 × 0.4 / 10) ≈ 0.15, so a 95% interval of roughly ±30 points ([module 05](../../modules/05-judging-models.md#the-statistics-of-small-evals)).
- **pass^2:** the share of tasks where both attempts passed.
- Mean rubric score, median minutes, hard-fail count, interventions, and quota used.

Then a **paired table**: the tasks where A passed and B failed, and the reverse. Those disagreements are where the real difference lives.

Finish with five sentences, from [module 05's Try it](../../modules/05-judging-models.md#try-it): which configuration won, by how much, on which task types, at what cost, and whether the difference is bigger than your error bar. If it isn't, say so plainly. "No detectable difference on 10 tasks" is a correct and useful result.

## What to submit

- `evals/`: `tasks/*.yaml`, `prompts/`, `tasks.tsv`, `rubric.md`, the scripts (or your manual-protocol log), `raw/`, `blind/`, `scores.csv`, and `summary.md`.
- Your hidden tests and the blinding key, submitted separately to the instructor (they're outside the repository on purpose).
- Evidence that each task was validated: hidden tests failing at the base commit and passing on the original solution.
- Reward-hacking notes, tool versions, and your [AI log](../syllabus.md#ai-log-template).

## Grading rubric

| Criterion | Points | Full credit means |
| --- | --- | --- |
| Task selection | 20 | 8–10 real tasks with the required mix, including a trap; nobody else's work |
| Task quality | 15 | Prompts don't leak solutions; hidden tests kept outside the repo; every task validated (fails at base, passes on the solution) |
| Run protocol | 15 | Fresh worktree and session per run; exactly one variable changed; turn caps; interleaved order; versions recorded; no leftover worktrees |
| Blind scoring | 15 | Outputs blinded; model names redacted; subjective dimensions scored before correctness; key opened last |
| Honest statistics | 20 | Error bars computed; paired table; conclusions no stronger than the data; public-task caveat where relevant |
| Reward-hacking check | 5 | Three passing runs read closely; any test edits investigated |
| AI log | 10 | Clear about what the agent built (scripts) and what you did (tasks, tests, scoring) |
| **Total** | **100** | |

## If you finish early

- **Pool tasks with the class** ([module 05 Try it](../../modules/05-judging-models.md#try-it)). If each student contributes two golden tasks, the class gets a set of 30 or more, large enough to see smaller differences. Compare the class result with a public leaderboard's ranking of the same models.
- **Rerun on a release.** When a new model or harness version ships, rerun a five-task smoke subset and log the result ([module 14](../../modules/14-keeping-up.md#evaluating-a-brand-new-release-in-an-afternoon)).
- **Add a third attempt** and report pass^3 alongside the average. Which metric would matter for an unattended nightly job?

## Instructor notes

- **Too-easy tasks.** If every run passes, the eval can't separate anything. Push students toward tasks the original author found fiddly.
- **Leaking hidden tests.** Check that `../eval-hidden/` really is outside the repository, and that task worktrees start from commits that don't contain `evals/`.
- **Two variables at once.** "Model A in harness X vs model B in harness Y" can't tell you which change mattered. Reject it at proposal time.
- **Overclaiming.** The most common grading issue. A 70% vs 60% result on 10 tasks is a tie. Reward students who say so.
- **Leftover worktrees.** Scripted runs that crash can leave worktrees and build output behind. Ask students to show an empty `git worktree list` (apart from the main checkout).
- **Quota.** Students who run all of configuration A first and hit a limit end up with an unbalanced comparison. The interleaving instruction exists for this.
- **The trap task** is the hardest to grade and the most interesting. Discuss the class's trap results in week 11.

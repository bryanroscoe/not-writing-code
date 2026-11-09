# Author review checklist (first draft)

Things for Bryan to confirm, decide, or fix before this goes to Salisbury or to a team. Delete items as you resolve them, and delete this file when it's empty.

## 1. Opinions written in your voice that go beyond what you said

These `Bryan's take` callouts take your stated opinions a step further. Confirm, edit, or delete:

- [ ] [06](modules/06-harnesses-and-tools.md#bryans-take): "several CLI agents in parallel, each in its own worktree… I drive them through T3 Code, which lets me run Claude and Codex side by side."
- [ ] [07](modules/07-context-engineering.md#bryans-take): "Loops with a hard, checkable goal and a human reading the result work for me. Open-ended loops that run unattended and ship to production don't, yet."
- [ ] [08](modules/08-agentic-workflows.md#bryans-take): "When I've let agents run long and unsupervised, I've come back to work that looks finished and isn't…" and the whole **"What would change my mind"** callout, which an agent drafted (there's an HTML comment there).
- [ ] [09](modules/09-multi-agent-systems.md#bryans-take): "Building in parallel works for me when the tasks are truly independent. Reviewing in parallel works almost every time."
- [ ] [10](modules/10-ai-code-review.md#bryans-take): "If you only adopt one practice from this module, make it an independent review from a fresh context before every merge."
- [ ] [13](modules/13-open-source-ecosystem.md#bryans-take): your autonomy skepticism applied to OpenClaw, and multi-model review applied to PRs on other people's projects.
- [ ] [00](modules/00-orientation.md#what-we-mean-by-vibe-coding) and [leads path](paths/leads.md#what-ai-first-should-mean-on-your-team): wording of the "vibe coding" definition and "the realistic goal right now is every engineer is a confident supervisor of agents."
- [ ] [02](modules/02-training-and-tuning.md#bryans-take): currently just "Models that can tune their own weights are huge." Add a sentence on *why* you think so, in your words.

## 2. Interpretations of the brain dump

- [ ] "Jev" was read as **Grok** ("you might use Grok or Gemini for very specific cases"). If you meant something else, search for "Grok" in modules 03, 05, 09.
- [ ] "Yegi" was read as **Steve Yegge** and his eight stages from "Welcome to Gas Town" (Jan 1, 2026). You're placed at stage 6–7. Module 08 quotes all eight stages.
- [ ] "The Muse stuff" was read as **Meta's Muse family** (Muse Spark, Apr 2026, and later releases). Module 03 has a section "Where is Meta's Muse? A clear answer."
- [ ] "Graph engineering" and "loop engineering" are covered as 2026 buzzwords with honest skepticism, in module 07.

## 3. Facts the research agents were least sure of

The research agents hit the shared web-search limit near the end and finished by fetching primary pages directly. The claims below are the shakiest. Each is marked "reported" in the text where appropriate.

- [ ] Meta **Muse Wonder** (Oct 12, 2026, $4/$20): only source is an OpenRouter listing (module 03, timeline).
- [ ] **Kimi K3.1 Pro** price ($2/$10) and the exact date its weights went up in early November (module 03, 04).
- [ ] **Qwen3.8-Max** price and weights date (module 03).
- [ ] **Subscription plan changes in late 2026**: Anthropic's Max 20x → "Ultra" rename (Oct 30), OpenAI's $500 Pro tier, Cursor's tiers with xAI. Mostly secondary sources (module 12).
- [ ] **Third-party harness rules for subscriptions**: Anthropic's Jan 2026 block and Feb 2026 terms change; OpenAI's "Sign in with ChatGPT" for other tools (module 12).
- [ ] **OpenAI's "automated research intern" milestone** (Sep 6, 2026), self-reported; openai.com blocked fetching (module 02).
- [ ] **Origin of "graph engineering"** (a Peter Steinberger post on X, around Jul 17–18, 2026), from secondary coverage (module 07).
- [ ] **OpenAI dropping SWE-bench Verified** (Feb 2026), from consistent secondary coverage (module 05).
- [ ] **OWASP LLM Top 10 2026 ordering** (module 11).
- [ ] **Bastani et al. (PNAS 2025)** details are from memory; the page was blocked (module 15).
- [ ] **Gemini 4 Carbon at #1 on Arena** (module 14) is from the live leaderboard on Nov 8 and marked preliminary there.

Already reconciled during drafting:
- Fable 5's suspension (Jun 12 – Jul 1, 2026) was due to US export controls, not instability. Fixed in module 03 and the timeline.
- Google's newest model is **Gemini 4 Carbon** (Oct 28, 2026, restricted to vetted cyber defenders for now). Added to module 03 and the timeline.

## 4. Decisions only you can make

- [ ] **License.** The repo has none, so by default nobody else may reuse it. For course material, CC BY 4.0 (prose) plus MIT (scripts) is common. If Salisbury adopts it, they may need explicit terms.
- [ ] **Naming Salisbury.** The syllabus is written as a generic upper-level elective proposal with placeholders. Decide whether to name the university, add a course number, or keep it generic for reuse.
- [ ] **Title.** The README calls it "Vibe Coding, Done Right." Change it if you prefer something else.
- [ ] **Length.** Modules run 5,000–8,000 words, longer than the 3,000–5,500 target, because the topic list was big. Candidates to trim: module 01 (the long prehistory), 05 ("Going deeper"), 07, 08, and the workplace playbook (~9k words; "Common rollout failures" and "The human side" partly repeat the phase risk tables).
- [ ] **Publishing.** Options: keep it as a GitHub repo, turn on GitHub Pages (MkDocs or similar), or publish a private web version to share by link.
- [ ] **Repo location.** You mentioned this project should live under `~/Developer`. It's currently a T3 Code project at `~/.t3/projects/vibe-code-tutorial`. Moving it is best done through T3 Code's project settings, so the app's bindings don't break.

## 5. Keeping it current

The [course syllabus](course/syllabus.md) and [instructor guide](course/instructor-guide.md) each have a per-term refresh checklist. The fastest-rotting files are [module 03](modules/03-model-landscape.md), [module 12](modules/12-costs-subscriptions-and-apis.md), and the [timeline](reference/timeline.md). Re-verify those first.

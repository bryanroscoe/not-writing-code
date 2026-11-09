# Team AI usage policy: a template

This template is for leads and for security, legal, and privacy reviewers, and takes about 25 minutes to read. It's part of [Phase 0 of the playbook](ai-first-playbook.md#phase-0-prerequisites).

*Last checked November 8, 2026.*

> [!IMPORTANT]
> **This is not legal advice.** It is a starting draft for an engineering team's AI usage policy. Your security, legal, and privacy teams (or outside counsel) must review it before adoption. Laws, vendor terms, and your own contracts vary and change. Nothing here replaces your organization's existing security, privacy, acceptable-use, or open-source policies; this policy should point to them, not contradict them.

## How to use this template

- Placeholders look like `[[ORG: ...]]`. Replace every one, and search the finished document for `[[ORG:` before you publish.
- Guidance notes are the blockquotes that start with "Guidance." They explain a choice; delete them from the published policy.
- Keep it short, and cut sections that don't apply so people can read it.
- Keep the policy in a repository, change it by pull request, and record each change in [section 18](#18-review-cadence-and-changes).
- Publish a provisional version 1 with a short approved-tools list and a review date a few months out, then tighten it as you learn. A long approval process pushes people toward unapproved tools.
- The modules have background for each section, especially [module 11](../modules/11-security-and-prompt-injection.md) (security), [module 12](../modules/12-costs-subscriptions-and-apis.md) (costs and terms), and [module 15](../modules/15-learning-careers-and-responsibility.md#responsible-use) (responsible use).

---

## Policy header

| Field | Value |
| --- | --- |
| Policy name | `[[ORG: e.g., Engineering AI Usage Policy]]` |
| Applies to | `[[ORG: teams, roles, contractors, and repositories in scope]]` |
| Owner | `[[ORG: name and role of the person accountable for this policy]]` |
| Approved by | `[[ORG: security, legal, privacy, engineering leadership]]` |
| Version | `[[ORG: e.g., 1.0]]` |
| Effective date | `[[ORG: date]]` |
| Next scheduled review | `[[ORG: date, no more than 3–6 months out for version 1]]` |
| Related policies | `[[ORG: links to security, privacy, acceptable use, open-source, and data classification policies]]` |
| Questions to | `[[ORG: channel or email]]` |

## 1. Purpose and scope

This policy explains how `[[ORG: team or organization name]]` uses AI coding assistants and agents: which tools are approved, what data may go into them, what agents may do without a person approving it, and how AI-assisted work is reviewed, disclosed, and reported.

It covers any AI system used for engineering work, including chat assistants, IDE assistants, command-line and cloud coding agents, AI code review tools, and AI components in CI/CD. It applies to company-owned code and data on any device, and to `[[ORG: contractors, vendors, others]]`.

## 2. Principles

1. **A named human is accountable for every change.** AI can suggest, write, review, and fix. A person approves and owns the result, including AI-written work.
2. **AI-first, not AI-only.** We use AI by default where it helps, and we keep the skills and judgment to work without it.
3. **Same bar for all code.** AI-assisted changes meet the same review, testing, and security standards as any other change.
4. **Protect data by default.** Only approved tools, only for the data classes they are approved for.
5. **Anything irreversible needs a human.** Agents don't deploy, delete, publish, send, or spend on their own.
6. **Report problems early, without blame.** Fast reporting limits damage and improves this policy.

> **Guidance:** These mirror the ground rules in [module 00](../modules/00-orientation.md#ground-rules-we-assume-throughout). Keep them few and memorable; the rest of the policy is detail.

## 3. Approved tools and plans

Only the tools and plans listed here may be used with company code or data.

| Tool | Plan or tier | Approved uses | Highest data class allowed ([section 4](#4-data-classification)) | Owner |
| --- | --- | --- | --- | --- |
| `[[ORG: primary coding agent]]` | `[[ORG: business/team/enterprise plan]]` | Interactive coding, review, debugging, docs | `[[ORG: e.g., Confidential]]` | `[[ORG: name]]` |
| `[[ORG: second coding agent, different lab]]` | `[[ORG: plan]]` | Cross-model review; backup when the primary is unavailable | `[[ORG: class]]` | `[[ORG: name]]` |
| `[[ORG: AI review bot]]` | `[[ORG: API or vendor plan]]` | Automated PR review on `[[ORG: repositories]]` | `[[ORG: class]]` | `[[ORG: name]]` |
| `[[ORG: API access for automation]]` | API, company account | CI and scheduled automation listed in [section 12](#12-automation-ci-and-api-use) | `[[ORG: class]]` | `[[ORG: name]]` |
| `[[ORG: chat assistant]]` | `[[ORG: plan]]` | Questions, explanations, drafting | `[[ORG: class]]` | `[[ORG: name]]` |

**Not approved for company code or data:**
- Personal or free accounts on any AI service, including approved vendors' consumer plans.
- Browser extensions and computer-use agents that act inside logged-in sessions, unless listed above. They read untrusted web content while holding your sessions ([module 06](../modules/06-harnesses-and-tools.md#closed-products-that-bundle-model-harness-and-tools)).
- Third-party model providers or "coding plans" not listed above, including endpoints that plug into an approved harness. They send code to a different provider, possibly in a different jurisdiction ([module 12](../modules/12-costs-subscriptions-and-apis.md#cheaper-alternatives)).
- MCP servers, plugins, skills, and extensions not on the approved list in [section 6](#6-agent-permissions-and-environments).
- `[[ORG: anything else]]`

To request a new tool, send the checklist in [Appendix B](#appendix-b-new-tool-request-checklist) to `[[ORG: owner or channel]]`. Expect a decision within `[[ORG: time]]`.

> **Guidance:** A good default is one primary agent plus a second from a different lab. The second makes cross-model review possible and keeps people working through an outage or a regression ([module 14](../modules/14-keeping-up.md#when-to-switch-tools)). Pay for business plans. They add admin controls and no-training defaults, while free tiers bring data risk and a bad first impression.

## 4. Data classification

Use the organization's existing data classes if it has them, and map them to this table.

| Class | Examples | May be used with | Never |
| --- | --- | --- | --- |
| **Public** | Open-source code, published documentation, public API docs | Any approved tool | No extra restrictions |
| **Internal** | Internal docs, non-sensitive tickets, architecture notes | Approved tools on company plans | Personal accounts; unapproved tools |
| **Confidential** | Proprietary source code, design documents, unreleased plans, internal metrics, logs with no personal data | Approved tools on company plans with the [required settings](#5-required-settings) | Personal accounts; tools without contractual no-training terms; unapproved providers |
| **Restricted** | Credentials and secrets of any kind; personal data about customers, users, or employees; `[[ORG: regulated data types, and the laws or contracts that govern them]]`; data or code a customer provided under contract; unpatched vulnerability details; production database contents | `[[ORG: "No AI tools" or "only tools explicitly approved for restricted data, e.g., a zero-data-retention configuration or a self-hosted model"]]` | Any tool not explicitly approved for restricted data |

Rules that apply to every class:

- Treat anything you paste, attach, or let an agent read as sent to the vendor. Agents read files on their own, so a file in the working tree is effectively in the prompt.
- Logs, stack traces, and database exports often contain restricted data. Scrub or sample them before sharing, and debug with copies that have personal data removed.
- Customer contracts may restrict AI use on their code or data. Check `[[ORG: where contract restrictions are recorded]]` before using AI on customer-specific work.
- When unsure, treat data as the higher class and ask `[[ORG: contact]]`.

> **Guidance:** Decide this table before rollout and get it approved ([leads path](../paths/leads.md#decisions-youll-have-to-make)). Consumer and business terms from the same lab often differ; for example, Anthropic's consumer terms let individual users choose whether their sessions are used for training, while its business and API terms exclude training by default ([module 15](../modules/15-learning-careers-and-responsibility.md#data-privacy-what-not-to-paste)). If some code truly can't leave your network, [module 04](../modules/04-open-vs-closed-weights.md#privacy-data-residency-and-compliance) covers self-hosted open-weight models and their trade-offs.

## 5. Required settings

Every approved tool must be configured as follows. Admins enforce these through managed settings where the tool supports them.

- [ ] **Sign-in:** company SSO only. `[[ORG: SSO provider; SCIM provisioning if available]]`
- [ ] **Training on our content:** off, backed by contract, not only a setting. `[[ORG: reference to the agreement or terms]]`
- [ ] **Retention:** `[[ORG: e.g., vendor default of N days; zero data retention for X]]`
- [ ] **Data residency:** `[[ORG: region requirements, if any]]`
- [ ] **Skip-permissions or "YOLO" modes:** disabled except inside an approved sandbox. Malware has invoked developers' AI tools with exactly these flags to hunt for secrets ([module 11](../modules/11-security-and-prompt-injection.md#real-incidents-20252026)).
- [ ] **Default permission mode:** `[[ORG: e.g., ask before commands; classifier-based auto mode allowed / not allowed]]`
- [ ] **Deny rules** for secret paths: `[[ORG: e.g., .env, .env.*, secrets/, key directories, cloud credential files]]`
- [ ] **Sandboxing:** `[[ORG: on by default where supported; required for any unattended run]]`
- [ ] **Updates:** `[[ORG: e.g., interactive tools auto-update; CI and automation pin versions and update after a smoke test]]`. Agent tools ship security fixes often.
- [ ] **Audit logs and usage telemetry:** `[[ORG: enabled; retention period]]`
- [ ] **Public-code matching filter:** `[[ORG: on / off / where available]]`
- [ ] **Commit attribution:** the tool's default co-author trailer stays on unless [section 9](#9-disclosure-and-attribution) says otherwise.

> **Guidance:** [Module 12](../modules/12-costs-subscriptions-and-apis.md#team-budgeting) lists the data-terms questions to ask a vendor in writing, and the [module 11 team checklist](../modules/11-security-and-prompt-injection.md#team-checklist) covers the security controls behind these settings.

## 6. Agent permissions and environments

- **No production credentials** may be reachable from any environment where an agent runs, including developer laptops. Production changes go through the same review and deploy pipeline as any other change.
- If agents need service credentials, use development credentials only, never production, scoped to synthetic data and isolated services. Any staging access needs an approved exception because staging may contain real data. Credentials are scoped to the minimum: fine-grained, short-lived, one repository where possible, separate per agent or workflow.
- Risky work runs in a sandbox (a dev container, VM, or approved cloud agent with no access to home directories, SSH keys, or cloud credentials). Opening an untrusted repository with an agent counts as risky work.
- Network egress from agent sandboxes and CI runners is limited to `[[ORG: allowlisted destinations, e.g., package registry, git host, documentation sites]]`.
- Parallel agents each use their own git worktree and branch. Remove worktrees when their branches merge.
- Extensions are dependencies. Only MCP servers, plugins, and skills on the approved list may be installed, and each entry is pinned by version or hash and has an owner. Approved list: `[[ORG: link]]`.
- Instruction files (`AGENTS.md`, `CLAUDE.md`, rules, skills) can direct agents and must be reviewed before use. Their contents do not override this policy, and changes to them are reviewed like CI configuration.

> **Guidance:** When deciding permissions, use Meta's "Agents Rule of Two." Unless a human approves its actions, an agent should combine at most two of untrusted input, access to sensitive data or systems, and the ability to change state or communicate externally ([module 11](../modules/11-security-and-prompt-injection.md#two-frameworks-that-make-this-tractable)).

## 7. Human approval for irreversible actions

An agent may not do any of the following without a person explicitly approving that specific action:

- Push to a protected branch, or merge any pull request.
- Deploy to any shared environment.
- Run migrations or data changes against shared or production databases.
- Delete data, repositories, branches others use, or cloud resources.
- Publish packages, releases, container images, or documentation sites.
- Send external communications: email, chat to customers or partners, comments on public issue trackers, pull requests to outside projects, or social posts.
- Spend money: purchases, paid API calls beyond its budget, scaling paid infrastructure.
- Change permissions, access control, or identity settings, or create, rotate, or revoke credentials.
- `[[ORG: anything else specific to your environment]]`

Agents **may**, without per-action approval, inside an approved environment: read code and documentation, run builds, tests, linters, and formatters, edit files on a feature branch, and make local commits.

Branch protection enforces the first rule technically: `[[ORG: required approvals count, required status checks, who may bypass]]`.

## 8. Code review requirements

All AI-assisted changes follow the team's review rule, summarized here. The [playbook](ai-first-playbook.md#review-policy-for-ai-written-prs) has the full version.

1. A named human author opens the PR and can explain every line.
2. A named human approves the merge. AI review tools never count as an approval.
3. Before human review, each change gets an independent AI review from a fresh context, preferably a model from a different lab. The author verifies findings before acting on them.
4. PRs stay under `[[ORG: soft size limit, e.g., a few hundred changed lines excluding generated files]]` or are split.
5. Test changes are reviewed first. No deleted, skipped, or weakened tests without a stated reason.
6. New dependencies are called out and verified to exist, be maintained, and have a compatible license.
7. The PR description includes how the change was verified and what the agent did versus what the author did.
8. Changes to `[[ORG: high-risk paths, e.g., authentication, authorization, data migrations, infrastructure]]` need review by a code owner.

> **Guidance:** The reviewer checklist for AI-written code is in [module 10](../modules/10-ai-code-review.md#how-humans-should-review-ai-written-prs). Keep the policy summary short and link to the full rule so it can evolve without a policy change.

## 9. Disclosure and attribution

- **Commits:** AI-assisted commits carry `[[ORG: e.g., a Co-Authored-By: or Assisted-by: trailer naming the tool]]`. Don't remove a tool's default attribution unless this policy says to.
- **Pull requests:** the PR template's "What the agent did vs. what I did" section is filled in for every AI-assisted PR.
- **Documentation and other written work:** `[[ORG: disclosure expectations, if any]]`
- **Customer-facing material:** `[[ORG: rules for disclosing AI-generated content to customers, if any]]`
- Attribution does not move responsibility. The human author remains the author of record ([module 15](../modules/15-learning-careers-and-responsibility.md#attribution-and-disclosure-in-commits-and-prs)).

## 10. Secrets handling

- Never paste credentials, tokens, keys, connection strings, or session cookies into any AI tool.
- Keep secrets out of the working tree. Use `[[ORG: secrets manager]]`, not `.env` files in the repository.
- Secret files are outside agents’ readable environments; tested read restrictions provide a second layer ([section 5](#5-required-settings)). Don't ask an agent to run commands that print the environment or secret files (`env`, `printenv`, `cat .env`).
- Secret scanning with push protection is on for all repositories: `[[ORG: tool]]`.
- Agent session transcripts and logs may contain anything the agent read. Treat them as `[[ORG: data class, e.g., Confidential]]` and don't share them outside approved locations.
- **If an agent may have read a secret, treat the secret as exposed:** rotate it and report it under [section 16](#16-incident-reporting).

## 11. Open-source contributions

- Contributions to outside projects follow `[[ORG: existing open-source contribution policy and approval process]]`.
- Follow each project's own AI policy. Some projects ban AI-generated contributions; others require disclosure. If a project bans it, don't submit AI-generated work there ([module 13](../modules/13-open-source-ecosystem.md#the-other-side-ai-slop-and-maintainer-burden)).
- Disclose AI assistance in the contribution, even where the project doesn't require it.
- The human contributor must understand every line, run the project's tests, and write the description and review replies personally.
- Never let an agent post to an outside project's issue tracker, pull requests, or mailing list on its own.
- Bug and security reports to outside projects must be reproduced by a person on a real build before they are filed.
- Never include confidential code or data in a public contribution.

> **Guidance:** Module 13's [etiquette for contributing with AI](../modules/13-open-source-ecosystem.md#etiquette-for-contributing-with-ai) is a good checklist to link from here.

## 12. Automation, CI, and API use

These rules apply to any AI that runs unattended or is shared: review bots, issue triage, scheduled agents, nightly jobs, and AI features in internal tools.

- Budgeted API access is this policy's default. Use another automation offering only after approval and verification of the vendor's current terms; do not assume that an individual subscription permits CI, shared automation, or products ([module 12](../modules/12-costs-subscriptions-and-apis.md#when-api-billing-is-the-right-choice)).
- Use one key per workflow and environment, with a spend limit and alerts: `[[ORG: default monthly limit, alert threshold, who gets alerts]]`.
- Every workflow has a named owner and a short written design that says which leg of the Rule of Two it removes ([section 6](#6-agent-permissions-and-environments)).
- Workflows that read untrusted input (public issues, PR titles and bodies from outside contributors, web content) run with read-only tokens, no secrets, isolated caches, and limited network.
- **Never insert untrusted text into the prompt of an agent that holds privileges.** Real attacks used issue titles and PR comments to hijack CI agents ([module 11](../modules/11-security-and-prompt-injection.md#real-incidents-20252026)).
- Pin agent tool versions and model snapshots, and upgrade deliberately after a smoke test.
- Set stop conditions: caps on turns, run time, and spend per run.
- Output goes through normal review. Automation opens pull requests or comments; it does not merge, deploy, or close issues on its own `[[ORG: unless an exception is approved]]`.
- Logs of automated agent runs are retained for `[[ORG: period]]`.

## 13. Generated code and intellectual property

- **Ownership.** AI-assisted work done for `[[ORG: organization]]` is covered by `[[ORG: employment or contractor IP agreements]]`, like any other work.
- **Human authorship.** Engineers substantially shape, review, and modify AI output rather than shipping one-prompt output untouched. (In the US, the Copyright Office's 2025 report concluded that prompts alone are unlikely to make output protectable, while human-authored portions and human selection, arrangement, and modification can be protected ([module 15](../modules/15-learning-careers-and-responsibility.md#licensing-and-copyright-of-generated-code)). `[[ORG: legal to confirm the position for your jurisdictions]]`.)
- **License scanning** runs in CI: `[[ORG: tool]]`. Findings that match third-party code under incompatible licenses block the merge until resolved.
- **Suspicious blocks.** Large, polished code that appears instantly for a niche problem is checked for provenance before merging.
- **Generated assets** (images, icons, fonts, sample data) are used only where `[[ORG: rules for rights and licensing of generated assets]]` allow.
- **Customer restrictions.** Where a contract limits AI use on a customer's code or data, that contract wins. `[[ORG: how engineers find out]]`.
- **Questions** go to `[[ORG: legal contact]]`.

> **Guidance:** This section is the one most likely to need legal changes. Ownership and infringement are separate questions, and the law differs between countries and is still developing.

## 14. Cost and usage

- **Seats:** `[[ORG: who gets which seat tier, and how to request a premium seat]]`.
- **Budgets:** `[[ORG: monthly budget per team; who approves increases]]`.
- **Review:** usage and spend are reviewed `[[ORG: monthly]]` by `[[ORG: owner]]`, per seat tier and per automation key.
- **Report surprises.** If you hit caps often, or a workflow costs far more than expected, tell `[[ORG: owner]]` rather than working around it.
- **No usage quotas.** We don't set targets for AI usage, tokens, or "percentage of code written by AI," and we don't rank people by them. We measure outcomes such as review latency, stability, and escaped defects ([playbook](ai-first-playbook.md#how-to-measure)).

> **Guidance:** Module 12's [team budgeting](../modules/12-costs-subscriptions-and-apis.md#team-budgeting) section explains per-seat versus pooled pricing and the cost controls to set on day one. The "no usage quotas" line is a policy choice, not a legal one; keep it if you mean it. It's one of the strongest signals to skeptical engineers that adoption isn't a speed-up campaign ([objections guide](objections.md#16-this-is-just-a-way-to-squeeze-more-output-out-of-us)).

## 15. Training and onboarding

- Before using AI tools on company code, each person completes `[[ORG: e.g., Sessions 0–2 of the internal series, or equivalent]]` and acknowledges this policy ([session series](session-series.md)).
- New team members get `[[ORG: setup guide, office hours, a buddy]]`.
- Learning time is protected. Managers may label onboarding and learning tasks as "AI-free" or "AI-as-tutor" (AI may explain and review but not write the submitted code). Juniors and anyone new to a codebase are encouraged to use learning modes and to debug before asking ([playbook](ai-first-playbook.md#juniors-and-learning)).

## 16. Incident reporting

**Report immediately** to `[[ORG: channel, on-call rotation, or security contact]]`, within `[[ORG: time, e.g., one hour]]`, if any of these happen or might have happened:

- A secret, credential, or restricted data went into an AI tool, prompt, transcript, or log.
- Company data went into an unapproved tool or a personal account.
- An agent ran a destructive or unexpected command, or changed something outside its task.
- An agent appears to have followed instructions from content it read (a README, issue, web page, dependency, or tool description).
- An agent or extension behaved in a way that suggests compromise.
- AI-generated code shipped with a security flaw, a license problem, or a defect that caused an incident.
- `[[ORG: other triggers]]`

**First steps**, in order:
1. Stop the agent or workflow. Don't delete anything.
2. Preserve the session transcript, tool logs, and the branch or worktree.
3. Revoke or rotate any credential the agent could have read.
4. Report, with what you know so far. Partial reports are welcome.
5. `[[ORG: follow the organization's incident response process from here]]`

Reporting is blame-free. Use reports to find control gaps. Post-incident reviews examine which control failed and what review missed.

## 17. Exceptions

Exceptions are requested from `[[ORG: owner]]` in writing, with the reason, scope, compensating controls, and an end date. Approved exceptions are recorded at `[[ORG: location]]` and reviewed at each policy review.

## 18. Review cadence and changes

- This policy is reviewed every `[[ORG: e.g., quarter]]`, and also when any of these happen: a vendor changes its data or usage terms; we adopt a new category of tool (for example, background or browser agents); a significant incident; a new law, regulation, or customer contract requirement.
- Changes are made by pull request to `[[ORG: repository and path]]` and approved by `[[ORG: approvers]]`.
- The team AI radar ([module 14](../modules/14-keeping-up.md#team-ai-radar)) is the record of tool evaluations; this policy is the record of rules.

| Version | Date | Change | Approved by |
| --- | --- | --- | --- |
| `[[ORG: 1.0]]` | `[[ORG: date]]` | Initial provisional policy | `[[ORG: names]]` |

## 19. Acknowledgment

> I have read the `[[ORG: policy name]]`, version `[[ORG: version]]`. I will use only approved tools and plans, follow the data rules, keep a human approval step before irreversible actions, follow the review and disclosure rules, and report incidents promptly.
>
> Name: ________ Date: ________

---

## Appendix A: one-page quick reference

| Do | Don't |
| --- | --- |
| Use approved tools on company plans, signed in with SSO | Use personal or free accounts for company work |
| Keep secrets out of the working tree and out of prompts | Paste credentials, personal data, or restricted data into any tool |
| Run agents in a sandbox for anything risky | Use skip-permissions modes outside a sandbox |
| Approve protected-branch pushes, merges, deploys, deletions, publishing, external messages, and spending beyond budget | Give agents production credentials |
| Give agents a check to run, and ask for the evidence | Merge code you can't explain |
| Get an independent review (ideally a different model) before human review | Count a bot review as an approval |
| Verify every new package an agent suggests | Install unapproved MCP servers, plugins, or skills |
| Disclose AI assistance in commits and PRs | Strip attribution to make work look hand-written |
| Follow each open-source project's AI policy | Let an agent post to outside projects on its own |
| Report incidents fast, even partial ones | Delete transcripts or logs after something goes wrong |

## Appendix B: new-tool request checklist

Answer these in the request. Most come from [module 06](../modules/06-harnesses-and-tools.md#how-to-choose-a-harness), [module 11](../modules/11-security-and-prompt-injection.md#team-checklist), and [module 12](../modules/12-costs-subscriptions-and-apis.md#team-budgeting).

**What and why**
- [ ] What is the tool, who makes it, and what will we use it for?
- [ ] Which approved tool doesn't do this, and why?
- [ ] Who will own it?

**Data and terms (get answers in writing)**
- [ ] Is our content used for training? Is that contractual?
- [ ] What is retained, for how long? Is zero data retention available?
- [ ] Where is data processed and stored? Which jurisdiction's law applies?
- [ ] Which data classes would it see?
- [ ] SSO, SCIM, audit logs, admin controls, spend limits?
- [ ] How much notice does the vendor give before changing limits, pricing, or terms?

**Security**
- [ ] What can it read, and what can it do (shell, network, git push, external APIs)?
- [ ] Which leg of the Rule of Two does our intended use remove?
- [ ] Does it support sandboxing, deny rules, and managed settings?
- [ ] Does it install or load third-party extensions (MCP servers, skills, plugins)? From where?
- [ ] What is the vendor's record of security advisories, and how fast are fixes shipped?

**Cost and durability**
- [ ] Pricing model (seat, usage, both) and expected monthly cost.
- [ ] Is configuration portable (for example `AGENTS.md`, Agent Skills, MCP) if we leave?
- [ ] What happens to our workflows if the vendor changes terms or shuts down?

**Evaluation**
- [ ] Results on our golden tasks, compared with the current approved tool ([module 05](../modules/05-judging-models.md#build-your-own-eval)).
- [ ] Proposed radar ring (Assess or Trial) and revisit date.

---

*This template is a starting point, not legal advice. Have it reviewed by your security, legal, and privacy teams before you adopt it.*

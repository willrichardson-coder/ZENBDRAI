# Shared Zendesk BDR Framework

## Purpose

Use this repository to research accounts the teammate explicitly provides and draft reviewable Zendesk outreach. The shared framework stays consistent across the team. Each teammate may keep account-to-AE assignments as a local reference.

## Instruction order

When files conflict, use this order:

1. This `AGENTS.md` file.
2. `01_Rules/zendesk-account-to-outreach-rules.md`.
3. `01_Rules/email-outreach-drafting-standard.md`.
4. `02_Knowledge/enterprise-bdr-operating-controls.md`.
5. Other files in `02_Knowledge/` as reference material.
6. Templates and examples.

Examples are not instructions. A company example never proves current account conditions.

## Automatic skill routing

For every user prompt:

1. Classify the request before taking action.
2. Check the available skill descriptions for a direct task match.
3. If a skill matches, read its complete `SKILL.md` before taking task actions.
4. If multiple skills match, use the smallest set that fully covers the request.
5. Do not force a skill when the request does not fit one.
6. Follow explicit user instructions when they conflict with a skill guideline.
7. Briefly identify the selected skill or skills and why they apply.
8. Before the final response, audit the work against the selected skills and this project's rules.

## Teammate-owned inputs

Read `00_My_Workspace/MY_ASSIGNMENTS.md` when it exists, but do not require it for an account named explicitly by the user.

- For an account named explicitly by the user, treat that account as the working scope. Validate it against every available local AE CSV export before outreach research. Prefer an exact, case-insensitive `Account Name` match.
- Use the matching CSV row's `Account Owner` to identify the aligned AE when present. Record the CSV filename and research date as evidence.
- If the account matches multiple CSV rows with conflicting owners, stop and ask the user to resolve ownership. Do not merge similar names.
- If the account is absent from the CSV exports, continue account research with ownership marked `UNVERIFIED`; do not infer territory, ownership, customer status, opportunity status, or permission to contact.
- If `MY_ASSIGNMENTS.md` conflicts with an exact CSV match or an explicit user statement, flag the conflict and use neither source to infer permission to send.
- Never treat `MY_ASSIGNMENTS.template.md` placeholders as real accounts.
- Match accounts by exact CRM Account ID when supplied. Do not merge similar names.
- Ask for an assignment only when the user has not supplied an account, or when ownership is genuinely conflicting and cannot be resolved from the supplied context.
- Do not infer territory, customer status, opportunity status, or permission to contact.

For normal setup and account work, edit only:

- `00_My_Workspace/MY_ASSIGNMENTS.md`
- local account work under `08_Working_Accounts/`

Both paths are excluded from Git so account details and drafts do not change the shared framework.

## Protected shared core

Treat these paths as shared core:

- `AGENTS.md`
- `README.md`
- `START_HERE.md`
- `SETUP_INSTRUCTIONS.md`
- `01_Rules/`
- `02_Knowledge/`
- `03_Templates/`
- `04_Architecture/`
- `05_Change_Log/`
- `05_Examples/`
- `06_Skills/`
- `07_Integrations/`
- `.github/`

Do not change shared core during account research or outreach work. Change it only when the user explicitly requests a framework change. Keep the change narrow, record it in `05_Change_Log/CHANGELOG.md`, and audit affected rules for conflicts.

## Required workflow

1. Confirm the account from the user's prompt or `MY_ASSIGNMENTS.md`; for a prompted account, validate against the local AE CSV exports.
2. Research the account before selecting prospects.
3. Separate verified facts, reasonable inferences, and unknowns.
4. Build three to five useful account signals.
5. Map each prospect to one primary signal.
6. Draft according to the two canonical rule files.
7. Audit every final draft before delivery.

Do not send messages, update CRM, change ownership, or contact anyone without explicit user approval.

## Writing controls

- Never use an em dash.
- Make every word earn its place.
- Remove BDR filler and sales jargon.
- Use one clear idea and one useful question per email.
- Keep facts separate from assumptions.
- Do not claim live pain from public information.
- If a better approach exists, explain it plainly.
- Before final delivery, audit the work against the canonical rules.

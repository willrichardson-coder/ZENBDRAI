# Shared Zendesk BDR Framework

## Purpose

Use this repository to research assigned accounts and draft reviewable Zendesk outreach. The shared framework stays consistent across the team. Each teammate changes only their account-to-AE assignments.

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

Read `00_My_Workspace/MY_ASSIGNMENTS.md` before account work.

- Treat it as the source for the teammate's assigned accounts and aligned AEs.
- Never treat `MY_ASSIGNMENTS.template.md` placeholders as real accounts.
- Match accounts by exact CRM Account ID when supplied. Do not merge similar names.
- If an account or AE is missing or ambiguous, stop and ask for the missing assignment.
- Do not infer territory, ownership, customer status, opportunity status, or permission to contact.

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

1. Confirm the account and aligned AE from `MY_ASSIGNMENTS.md`.
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

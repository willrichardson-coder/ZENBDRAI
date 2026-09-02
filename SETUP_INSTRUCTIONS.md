# Setup Instructions

Use these steps to create a working copy without changing the shared framework.

## 1. Get your copy

Fork or clone the repository from the approved GitHub location. Downloading the ZIP also works, but a fork or clone makes framework updates easier to receive.

Keep the folder structure unchanged.

## 2. Open it as a local project

Place the folder in a stable local workspace and attach it as the primary folder in Codex.

The primary structure is:

- `AGENTS.md`
- `START_HERE.md`
- `SETUP_INSTRUCTIONS.md`
- `00_My_Workspace/`
- `01_Rules/`
- `02_Knowledge/`
- `03_Templates/`
- `04_Architecture/`
- `05_Examples/`
- `05_Change_Log/`
- `06_Skills/`
- `07_Integrations/`

## 3. Create your assignments file

Copy `00_My_Workspace/MY_ASSIGNMENTS.template.md` and rename the copy `MY_ASSIGNMENTS.md`.

Replace the sample row with your assigned accounts and aligned AEs. Keep one row per account. Use exact CRM Account IDs when available and `UNKNOWN` when a value is missing.

This is the only file a teammate needs to change. It is excluded from Git.

## 4. Confirm the framework loaded

Start a new task from the local project and ask:

> What account and AE assignment file governs my work, and which files are protected shared core?

The answer should identify `00_My_Workspace/MY_ASSIGNMENTS.md` and the protected paths in `AGENTS.md`.

If you use a ChatGPT Project instead of a local Codex project, upload the repository files and add `AGENTS.md` as project instructions. A ChatGPT Project does not edit or synchronize the local Git folder automatically.

## 5. Run one test account

Choose one account from `MY_ASSIGNMENTS.md`. Ask the agent to:

1. Confirm the exact account and aligned AE.
2. Research the account.
3. Separate verified facts, reasonable inferences, and unknowns.
4. Create three to five account signals.
5. Recommend prospects connected to one signal each.
6. Draft a four-email sequence for one prospect.
7. Audit the sequence against the rules.

Use `03_Templates/ACCOUNT_TO_OUTREACH_WORKSHEET.md` to inspect the output.

## 6. Review the test output

Confirm that:

- The account and aligned AE match `MY_ASSIGNMENTS.md`.
- The account reason comes before profile personalization.
- Each prospect has one primary angle.
- Email 1 uses either the product-neutral default or a deliberate vendor-present test allowed by the canonical rules.
- Email 1 does not ask for a meeting.
- Each email has one clear job.
- Operational pressure is plausible, not stated as fact without evidence.
- Any proof point matches the prospect's business pressure.
- The final email makes confirmation, redirection, or disqualification easy.
- The copy has no unsupported claims, generic filler, banned phrases, emojis, or em dashes.

## 7. Correct a failed test

If the output fails, ask the agent to re-read `AGENTS.md` and the two canonical rule files, then rerun the test. Do not rewrite shared rules to solve one weak draft.

## 8. Work safely

Review every draft before sending. Never treat a draft, account record, or research result as permission to contact someone.

Do not connect automatic sending until mailbox, compliance, suppression, and approval controls have been confirmed.

## 9. Keep account work local

Keep account research, prospect details, and drafts under `08_Working_Accounts/`. That folder is excluded from Git.

Do not place live account material inside rules, knowledge, examples, or skills.

## 10. Improve the shared framework

Propose changes that help the whole team through a branch and pull request. Follow `CONTRIBUTING.md`.

Do not commit account lists, prospect records, CRM exports, credentials, activity logs, or local drafts.

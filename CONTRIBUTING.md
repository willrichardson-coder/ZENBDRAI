# Contributing

This repository has one shared framework and one local assignment layer.

## Normal teammate use

Do not open a pull request for account or AE changes. Keep those changes in the ignored file `00_My_Workspace/MY_ASSIGNMENTS.md`.

Keep research, prospect details, and drafts under the ignored `08_Working_Accounts/` folder.

## Framework improvements

Use a branch and pull request when a rule, template, knowledge source, skill, integration, or onboarding instruction should change for everyone.

A framework pull request must:

1. Explain the operating problem.
2. Identify the evidence or conflict behind the change.
3. Keep the change narrow.
4. Update `05_Change_Log/CHANGELOG.md` when behavior changes.
5. Pass the checklist in the pull request template.
6. Receive approval from the code owner before merge.

Do not commit account lists, prospect records, CRM exports, credentials, activity logs, or local drafts.

## Repository owner setup

`CODEOWNERS` identifies the framework owner, but GitHub enforcement requires a branch ruleset.

In GitHub, protect `main` and require:

- Changes through pull requests
- One approval before merge
- Code owner approval
- Conversation resolution
- The `Framework check` status check
- No force pushes
- No branch deletion

Allow teammates to fork the repository or create branches. Do not grant routine direct writes to `main`.

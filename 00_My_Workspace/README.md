# My Workspace

This is the optional local configuration folder for teammate-specific account notes.

## Setup

1. Copy `MY_ASSIGNMENTS.template.md` in this folder if you want a persistent account-to-AE reference.
2. Rename the copy to `MY_ASSIGNMENTS.md`.
3. Replace the sample rows with your accounts and aligned AEs.
4. Use `UNKNOWN` when a required value is not available. Do not guess.

`MY_ASSIGNMENTS.md` is excluded from Git. Your account list remains local and the shared framework stays unchanged. It is not required when you give an account directly in the prompt.

## Required fields

- Account name
- CRM Account ID, when available
- Account website
- Aligned AE
- Motion: cold, warm, customer, or active opportunity
- Priority: high, medium, low, or unassigned

The notes column is optional. Use it for an AE preference, suppression, ownership conflict, or source reminder. Do not store credentials, private contact data, or activity logs here.

## Start a task

Ask:

> Research [Account] from my assignments, build the signal map, recommend the right prospects, and draft outreach only after the account case is clear.

The agent should exact-match the prompted account against the available AE CSV exports and use `Account Owner` to identify the aligned AE when present. A missing match is `UNVERIFIED`, not a blocker to account research. Conflicting owners require resolution before outreach execution.

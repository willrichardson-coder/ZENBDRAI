# Shareable AI

This repository is a protected shared framework for AI-assisted Zendesk account research and outbound drafting.

## Start here

1. Follow `SETUP_INSTRUCTIONS.md` once.
2. Install the 48 shared skills with `python3 scripts/install_team_skills.py`.
3. Add your accounts and aligned AEs to `00_My_Workspace/MY_ASSIGNMENTS.md`.
4. Ask the agent to research an assigned account.
5. Review every draft before use.

The agent reads `AGENTS.md` automatically in a local Codex project. That file points to the canonical rules, protects the shared core, and requires the account-first workflow.

## Core operating principle

Write like a thoughtful operator who is testing a relevant business question:

> You may already be dealing with this issue. We have relevant experience. Is it worth comparing notes?

Keep the tone conversational, calm, specific, and low-pressure. Do not copy a coworker's voice mechanically. Use the useful pattern while preserving your own judgment.

## What each teammate changes

Each teammate changes only `00_My_Workspace/MY_ASSIGNMENTS.md`.

That file maps each assigned account to its aligned AE. It is excluded from Git so the account list stays local and the shared framework does not drift.

Sender identity should come from the teammate's authenticated workspace context. If it is unavailable, the agent must leave a sender placeholder instead of using another person's identity.

## What this package contains

- `01_Rules`: active drafting rules and the email standard
- `02_Knowledge`: selected product, customer proof, competitive, ROI, discovery, and prospecting references
- `03_Templates`: a simple account-to-outreach worksheet
- `06_Skills`: all 48 custom Codex skills, curated for team use
- `00_My_Workspace`: the local account and AE assignment layer
- `08_Working_Accounts`: ignored local research and drafts created during use

Use the structured paths above as the canonical files. The root-level `zendesk-account-to-outreach-rules.md` and `fortive-outreach-final.md` are compatibility copies retained for convenience. Do not edit them independently.

The historical archive and legacy ZIP have been moved to the separate Desktop folder `ALL AI - Historical`. Do not load that folder into an LLM as active context.

## What this package does not contain

The shared framework excludes live assignment files, private prospect records, activity logs, credentials, local tool settings, legacy archives, and generated account work. Labeled examples and reusable integration source may remain in the repository, but they are not live account evidence or instructions.

## Source discipline

Treat customer results, product claims, competitive claims, and company facts as reference material that must be checked before use. Do not turn an inference into a fact. Do not use a proof point unless it matches the prospect's business pressure and is current enough for the use case.

## Final check

Before sharing or sending a draft, confirm that it has one clear idea, one useful question, a grounded account reason, no unsupported claims, no generic filler, no emojis, and no em dashes.

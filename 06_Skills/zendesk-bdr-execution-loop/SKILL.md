---
name: zendesk-bdr-execution-loop
description: Orchestrate a clean Zendesk BDR/XDR daily execution loop across account prioritization, contact research, ChatGPT synthesis, approved Groove content, calling, and CRM-ready outcome capture. Use to plan or audit tool flow; not to enroll, send, call, or write records without separate approval.
---

# Zendesk BDR execution loop

Turn research and outreach into a consistent, auditable workflow without losing source provenance or creating duplicate records.

Read [the evidence/process contract](../../references/shared/zendesk-evidence-and-process.md), [the tool-access contract](../../references/shared/seller-tool-access-contract.md), and [the Sales plugin composition map](../../references/shared/sales-plugin-composition.md).

## Access contract

- Core evidence: bounded work period, assigned accounts/territory, exact IDs, owner rules, current approved plays, and destination-system state.
- Preferred access: Salesforce, seller-authenticated Snowflake, Seismic, Common Room, approved contact data, Groove read access, and calendar.
- Degraded mode: when a system is unavailable, identify the missing step and continue with local drafts; never claim a lookup, save, enrollment, call, or send occurred.

## Method

1. Define the day's outcome, time blocks, account capacity, and stop conditions.
2. Prioritize exact accounts from authoritative ownership, suppression, fit, and current-signal evidence.
3. Resolve contacts without repairing identity by name, company, title, or domain.
4. Confirm each Sumble organization maps to the exact CRM account, resolving parent, brand, or subsidiary ambiguity. Match verified account-level installed-technology observations to the relevant vendor sections in `02_Knowledge/zendesk_competitive_intel.md`, record the observation date, and carry relevant battle-card discovery context into the sourced POV and writing when it fits the recipient and approved play. Do not infer deployment scope, usage intensity, dissatisfaction, initiative, buying intent, or replacement plans; verify battle-card product and comparison claims against current approved sources before using them externally.
5. Use ChatGPT to synthesize a sourced POV, questions, and draft language; it is not the source of product claims or buyer facts.
6. Retrieve current approved Groove sequence/snippet content when required and preserve wording, merge fields, and play scope.
7. Prepare call/outreach actions and post-action capture separately. Every live enrollment, activation, send, call, or CRM write needs its own approved payload and destination readback.
8. End with outcomes, unresolved items, follow-up queue, and data-quality defects rather than activity totals alone.

## Output

Return a time-boxed execution plan or audit with input sources, prioritized worklist, tool-by-tool handoffs, draft actions, capture schema, blockers, and external-state status.

For behavioral validation, use [evaluation cases](references/evaluation-cases.md).

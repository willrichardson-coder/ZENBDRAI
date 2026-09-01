---
name: zendesk-nb-territory-and-pipeline
description: Build an adaptive Zendesk New Business territory and pipeline-creation plan from exact ownership, book-of-business, source, capacity, and current-priority evidence. Use for an AE's bounded territory or period; not for changing assignments, saving Salesforce reports, or treating scores as truth.
---

# Zendesk New Business territory and pipeline

Help the AE decide where pipeline can be created fastest while maintaining enough strategic coverage for longer-cycle accounts.

Read [the evidence/process contract](../../references/shared/zendesk-evidence-and-process.md), [the tool-access contract](../../references/shared/seller-tool-access-contract.md), and [the source registry](../../references/shared/workspace-source-registry.md).

## Access contract

- Core evidence: exact AE/territory/account IDs, ownership, segment, period, pipeline target/context, current opportunities, suppression/exclusion state, and source definitions.
- Preferred access: Salesforce, seller-authenticated Snowflake, Clari/Sales Pulse, Seismic, Common Room, and public primary research.
- Degraded mode: without current book-of-business data, provide the query/report specification and planning framework but not a live coverage judgment.

## Method

1. Resolve scope, ownership, period, capacity, and metric definitions before ranking accounts.
2. Separate pipeline sources such as inbound, prior engagement, customer/new-use-case, partner, event, intent, and cold outbound. Do not merge analytical source fields silently.
3. Assess current coverage, concentration, whitespace, active opportunity conflicts, and exclusions by exact ID.
4. Balance fast-start sources with strategic accounts and state the tradeoff. Scores prioritize review; they do not prove ICP, need, or intent.
5. Define account tiers, source-specific actions, time allocation, leading evidence, and weekly review triggers.
6. Produce a Salesforce report/filter specification when useful, but do not save or change it without exact approval and readback.

## Output

Return a territory snapshot, source mix, account priorities, capacity plan, pipeline hypotheses, weekly actions, report specification, risks, and unresolved data. State that no territory, report, opportunity, or account was changed.

For behavioral validation, use [evaluation cases](references/evaluation-cases.md).

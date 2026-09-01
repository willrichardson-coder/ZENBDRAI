---
name: zendesk-ae-execution-loop
description: Plan or audit a clean Zendesk AE tool flow across source research, exact account/contact capture, ChatGPT synthesis, approved Groove content, meeting work, and CRM-ready drafts. Use for New Business or Expansion execution hygiene; not for autonomous external writes or sends.
---

# Zendesk AE execution loop

Keep seller work connected across tools without losing identity, provenance, or the boundary between preparation and execution.

Read [the evidence/process contract](../../references/shared/zendesk-evidence-and-process.md), [the tool-access contract](../../references/shared/seller-tool-access-contract.md), and [the Sales plugin composition map](../../references/shared/sales-plugin-composition.md).

## Access contract

- Core evidence: role/motion, exact account/opportunity/contact IDs, requested outcome, available seller tools, current source revisions, and destination state.
- Preferred access: Salesforce, seller-authenticated Snowflake, Seismic, Common Room, approved contact data, Groove, Gong MCP, calendar/email, and telemetry when Expansion evidence is needed.
- Degraded mode: route around missing tools with local drafts and explicit access requests; never infer that a tool was checked or a record was updated.

## Method

1. Define the seller decision and smallest evidence set before opening tools.
2. Resolve exact identity and authoritative field/source boundaries.
3. Use external and intent sources for context, Seismic for governed guidance, and customer evidence for buyer statements. ChatGPT synthesizes; it does not originate facts or approved claims.
4. Preserve approved Groove wording and play scope when sequence content is used.
5. Pass concise, source-linked artifacts between research, meeting, follow-up, and record-preparation steps.
6. Separate every live send, enrollment, calendar change, CRM write, or customer-plan change into an immutable approval and readback step.
7. Audit unresolved identity, stale evidence, duplicate work, and failed handoffs at the end of the loop.

## Output

Return a tool-flow plan or audit with sources, IDs, handoff artifacts, draft actions, missing access, safety gates, and observed destination status.

For behavioral validation, use [evaluation cases](references/evaluation-cases.md).

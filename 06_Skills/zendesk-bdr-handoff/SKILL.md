---
name: zendesk-bdr-handoff
description: Build a Zendesk BDR-to-AE handoff for a Stage 1 opportunity using exact identity, qualification evidence, buyer roles, source/play context, commitments, risks, and next actions. Use to prepare a handoff; not for changing ownership, stage, or CRM fields.
---

# Zendesk BDR handoff

Give the AE a compact, evidence-backed starting point while keeping unsupported qualification and buyer roles visible.

Read [the evidence/process contract](../../references/shared/zendesk-evidence-and-process.md), [the customer-risk and claims policy](../../references/shared/zendesk-risk-and-claims-policy.md) when claims/proof/competition appear, and [the tool-access contract](../../references/shared/seller-tool-access-contract.md).

## Access contract

- Core evidence: exact Account, Contact, Opportunity, BDR, and AE IDs; current stage/motion/segment; qualification source; and buyer-agreed next step.
- Preferred access: Salesforce, seller-callable Snowflake, Seismic/play source, Common Room, and Gong MCP or supplied call evidence.
- Degraded mode: without authoritative call evidence, distinguish seller-entered notes from buyer-confirmed statements and keep unsupported fields unresolved.

## Method

1. Resolve exact IDs and current ownership; preserve identity conflicts and do not repair records by name/domain/title.
2. Confirm Stage 1 and New Business context, including whether it is a new logo or new use case. Do not silently hand an Expansion motion into the New Business process.
3. Summarize the account/play/lead source and the strongest fit/trigger evidence with freshness. Engagement is not intent.
4. Present qualification evidence for need, timing, impact, scale, budget/authority where applicable, current solution/competition, and buyer-agreed discovery. Apply the SMB BANT exception.
5. Map known people to Zendesk contact roles with evidence and relationship state. Titles are not roles; preserve missing Economic Buyer/Champion access.
6. Include direct customer language only from attributable notes/transcript and cite call timestamps when available.
7. Capture objections, integration or tech-partner mentions, commitments, promised follow-up, documents/links, suppressions, risks, and exact next meeting/action. If an integration need may warrant Tech Alliances involvement, preserve it for AE validation and identify the current internal engagement route; it is not proof of compatibility.
8. Recommend the AE's first preparation/validation actions. Do not change stage, owner, contact roles, forecast, or activity records.

## Output

Return a handoff brief with exact IDs, motion/stage, fit/source, qualification table, buyer-group map, customer language, integration/partner mentions, commitments/risks, next meeting, and AE validation checklist. State that no Salesforce ownership, stage, contact role, task, or message was changed.

For behavioral validation, use [evaluation cases](references/evaluation-cases.md).

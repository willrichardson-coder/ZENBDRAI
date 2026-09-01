---
name: zendesk-bdr-prospecting-plan
description: Build a Zendesk BDR prospecting plan for an assigned account set, prioritizing exact accounts, contact-role hypotheses, fit, triggers, suppressions, approved plays, and next actions. Use before outreach execution; not for enrolling contacts or sending messages.
---

# Zendesk Bdr Prospecting Plan

Turn a bounded account set into a defensible BDR work plan rather than an unranked activity list.

Read [the evidence/process contract](../../references/shared/zendesk-evidence-and-process.md), [the customer-risk and claims policy](../../references/shared/zendesk-risk-and-claims-policy.md) when claims/proof are used, [the capability matrix](../../references/shared/seller-capability-matrix.md), and [the tool-access contract](../../references/shared/seller-tool-access-contract.md).

## Access contract

- Core evidence: exact Account IDs, owner/territory, segment, motion, suppression state, and current approved play or targeting context.
- Preferred access: Salesforce, seller-callable Snowflake, Seismic, Common Room, public first-party research, and read-only Groove/Outreach context.
- Degraded mode: without Common Room, omit engagement/intent; without an approved persona/play, plan account and role research but do not claim approved messaging.

## Method

1. Resolve each account by exact authoritative ID and current owner/territory. Preserve duplicates, conflicts, stale rows, and suppressions; do not repair identity by name/domain.
2. Apply current segment and motion definitions. Evaluate fit through ICP, digital maturity, business model, operating environment, and need/buying signals without turning ICP into a hard exclusion unless the governing source says so.
3. Use deeper mystery-shopping and account-specific research for Tier 1; use bounded high-yield primary sources for lower tiers.
4. Rank accounts on evidence strength, fit, trigger recency, reachability, play relevance, and disqualifiers. Engagement signals support prioritization but do not prove intent.
5. Map likely contacts to Zendesk purchasing roles. Persona/buyer-role labels are not job titles; keep mappings hypothetical until evidenced.
6. Select the exact current play, sequence/snippet, product source, customer story, or competitor asset. Preserve delivery classification and blocked/pending claim states.
7. Produce a time-bounded plan with account/contact rationale, `Why You, Why Now` hypothesis, channel, next action, and validation needed. Do not enroll, activate, schedule, or send.

## Output

Return a ranked account/contact plan, evidence and suppressions, role hypotheses, approved-source routing, daily/weekly action queue, and access gaps. Cite exact IDs and state that no records, flows, enrollments, or messages were changed.

For behavioral validation, use [evaluation cases](references/evaluation-cases.md).

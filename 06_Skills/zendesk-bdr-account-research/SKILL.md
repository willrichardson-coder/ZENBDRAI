---
name: zendesk-bdr-account-research
description: Build a source-backed Zendesk BDR account brief with fit and trigger evidence, buying-group hypotheses, exclusions, and testable outreach angles. Use for account research or prioritization before prospecting; do not use it to draft a full sequence or alter account/contact records.
---

# Zendesk BDR account research

Turn one assigned account or a bounded account set into a decision-ready BDR brief. Optimize for whom to contact, why this account, why now, and what must be validated—not for a generic company profile.

Read [the Zendesk evidence and process contract](../../references/shared/zendesk-evidence-and-process.md). Read [the customer-risk and claims policy](../../references/shared/zendesk-risk-and-claims-policy.md) when using product, customer-proof, or competitive evidence. Read [the workspace source registry](../../references/shared/workspace-source-registry.md) when using Salesforce, seller-accessible Snowflake evidence, or an approved Sales Play. Read [Sales plugin composition](../../references/shared/sales-plugin-composition.md) when the installed Sales plugin is available. Read [the Level Up learning loop](../../references/shared/level-up-learning-loop.md) only if the work exposes reusable friction or a repeatable practice.

## Access contract

- Core evidence: exact Account identity plus current fit, ownership, and suppression context from Salesforce, authenticated Snowflake, or a supplied dated snapshot.
- Preferred access: Salesforce; authenticated Snowflake through ChatGPT Work/browser; current Seismic or exact Sales Play package; public first-party research.
- Evidence enhancers: Common Room, Gong MCP, LinkedIn/Lusha, and other approved intent/contact sources. Without them, omit their signals and identify the precise read access that would improve prioritization; do not block the core brief.

## Scope

Confirm the exact account identity, seller/territory owner when supplied, segment, New Business versus new-use-case context, relevant approved play, and decision the BDR needs to make. If the account cannot be resolved by exact authoritative ID, stop account-specific enrichment and show the unresolved identity.

## Research

1. Start with Salesforce account/contact truth and any approved play or Seismic ICP/persona source. Use the exact Salesforce Account ID and preserve documented owner IDs such as `SDR_ASSIGNED_C`, `AM_OWNER_C`, `SUCCESS_OWNER_C`, or `SOLUTION_CONSULTANT_C` without resolving them by a plausible name. Record source freshness and conflicts.
2. Evaluate the account through the four visible Zendesk lenses: ICP fit, digital maturity, business model, and operating environment. Keep each lens `Observed`, `Hypothesis`, or `Unresolved`; do not invent the inaccessible detail panels.
3. Apply the current Sales Process Hub segment definition. Do not infer a different segment from public headcount when Salesforce has an authoritative segment; show the discrepancy. Do not silently apply the conflicting 2026 persona-page downmarket/upmarket bands.
4. For Tier 1 accounts, use deeper account-specific research, including customer-experience mystery shopping when lawful and appropriate. For Tier 2 and below, keep the pass bounded to high-yield primary sources such as the company site, annual report, leadership statements, and relevant buyer profiles.
5. Use Common Room, approved intent signals, and public research as prioritization evidence—not proof of need or buying intent.
6. Map the likely buying group to the visible Zendesk contact roles. Treat buyer-group labels as internal purchasing-role monikers, not job titles. Keep every person-role mapping a hypothesis until supported by Salesforce or customer evidence.
7. Produce one to three `Why You, Why Now` hypotheses tied to a sourced business change, workflow, or customer-experience signal. If an approved play applies, route to its exact current source map, persona overlay, copy revision, and claim ledger. Otherwise use the exact current customer-facing product source, customer story/reference, or competitive asset for the needed claim type. Play-specific personas and claims do not become general Zendesk guidance; do not use `pending` or `blocked` claims, invent a claim, reuse a story outside its scope/permission, quote the internal product comparison chart, or rewrite evaluated sequence copy.
8. State disqualifiers, suppressions, exact-ID gaps, stale evidence, and the smallest questions that would change prioritization.

## Output

```md
# BDR account brief: [account]

**Account ID:** [exact ID or Unresolved]
**Segment / motion:** [Observed value and source]
**Research posture:** [Tier/depth, observed date]

## Decision summary
[Pursue now / monitor / deprioritize / unresolved, with reason and confidence]

## Observed account signals
| Signal | State | Source / date | BDR implication |
|---|---|---|---|

## Buying-group hypotheses
| Person or role | Zendesk contact-role hypothesis | Evidence | Gap / test |
|---|---|---|---|

## Why you, why now
1. [Hypothesis + source + question to validate]

## Exclusions and unresolved items
- [Suppression, mismatch, stale source, missing persona/claim]

## Next-best actions
1. [Action, owner, timing, evidence needed]

## Sources and status
- [Stable links / exact IDs]
- External status: not saved, enrolled, sent, or updated.
```

Draft messages only when separately requested. Reuse the exact current approved Groove/Outreach sequence or snippet as source copy. The workspace contains play-specific source locks, not one universal sequence; do not recreate, edit, enroll, activate, schedule, or send from this skill.

For behavioral validation, use [evaluation cases](references/evaluation-cases.md).

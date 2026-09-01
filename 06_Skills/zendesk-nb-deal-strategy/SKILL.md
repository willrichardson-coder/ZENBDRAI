---
name: zendesk-nb-deal-strategy
description: Build an evidence-backed Zendesk New Business deal strategy covering buyer process, qualification, mutual actions, competition, commercial posture, risks, and next moves. Use for an active new-logo or new-use-case opportunity; not for expansion add-ons or automatic renewals.
---

# Zendesk New Business deal strategy

Help the AE decide how to advance an active New Business opportunity using buyer evidence and the current Zendesk process. The output is a strategy brief, not a stage-change request.

Read [the Zendesk evidence and process contract](../../references/shared/zendesk-evidence-and-process.md), [the customer-risk and claims policy](../../references/shared/zendesk-risk-and-claims-policy.md), and [the workspace source registry](../../references/shared/workspace-source-registry.md). When available, read and compose with the Sales plugin's `plan-deal-strategy`; use `build-business-case` or `build-competitive-brief` only when those focused outputs are requested. Read [Sales plugin composition](../../references/shared/sales-plugin-composition.md) for ownership boundaries.

## Access contract

- Core evidence: exact Opportunity and Account IDs, current CRM/Snowflake opportunity snapshot, stage/motion/segment/forecast context, and the buyer evidence supplied for review.
- Preferred access: Salesforce; authenticated Snowflake through ChatGPT Work/browser; Seismic; Clari/Sales Pulse; Gong MCP for current customer-call evidence.
- Evidence enhancers: MAP artifact, email/meeting notes, Common Room, approved competitive and product sources. If Gong MCP is unavailable, complete a CRM/Snowflake-bounded strategy and request read-only Gong access for the exact opportunity and date window; do not claim buyer statements, call behavior, or transcript validation.

## Workflow

1. Resolve the exact Salesforce account and opportunity using the 18-character Opportunity `ID` business key and `ACCOUNT_ID`. Confirm New Business motion without silently merging `TYPE`, `DEAL_TYPE_C`, `SIMPLIFIED_DEAL_TYPE_C`, or analytical `OPPORTUNITY_SOURCED_TYPE`. Resolve current stage, segment, owner, amount, close timing, and forecast posture; preserve unresolved or conflicting CRM fields.
2. Build an evidence timeline from CRM, customer interactions, mutual-action artifacts, and internal account sources. Distinguish customer commitments from seller-entered expectations.
3. Map the buying group using Zendesk contact roles. Show access, influence, stance, evidence, and missing relationships; do not equate a title with Economic Buyer or Champion.
4. Apply MEDDPICC as a continuous evidence lens. Where a current snapshot exposes the documented fields, distinguish each `MEDDPICC_*_C` rating from its `MEDDPICC_*_ACTUAL_C` evidence detail and test both against customer evidence. Apply Sandler only for SMB and Digital. Use BANT only where the visible process requires it; Stage 1 says it is not required for SMB.
5. Compare observed buyer behavior to the verified stage baseline. At Stage 3, test whether the Champion has validated the solution and business case/ROI for the broader buying decision team, whether technical discovery and solution design are credible, and whether at least three buying-team contacts are identified; the visible source says the exit criterion is not required for SMB. Never recommend a Salesforce stage change from historical or incomplete guidance; identify the current field/manager verification needed.
6. For Stage 2 and later, connect success measures, business impact, decision process, competition, Champion, Economic Buyer, and Mutual Action Plan evidence. `OPPORTUNITY_MUTUAL_ACTION_PLAN_DA IS NOT NULL` establishes only that the documented Sales Pulse view sees a MAP link; inspect the artifact for buyer ownership, dates, currency, agreement, and completion evidence. Preserve the local documentation conflict that separately describes this field as a date. Stage 2 MAP is not applicable to SMB in the visible guidance. At Stage 3, include the initial ROI/business justification, technical deal breakers, implementation strategy, tailored pitch/dry run, MAP refinement, and executive alignment when supported.
7. For complex opportunities, identify the needed cross-functional role. Deals over $250k ARR should surface Transformation Consulting according to the visible Stage 2 source; also identify SC, Professional Services, Platform Architecture, Legal, Security, Deal Desk, Renewals, CS, or partner involvement only when supported by deal needs. For product, proof, or competitive claims, retrieve the current exact customer-facing data sheet, Help Center/product source, customer story/reference, Klue/CI asset, or play-specific claim. Treat assistant output as synthesis and never send the internal product comparison chart to a customer.
8. If forecast posture affects the strategy, use the checked-in convention as a discovery aid: `manager_forecast__c` for SMB and `vp_deal_forecast__c` for non-SMB. Verify the live reporting convention and raw category vocabulary before recommending a posture.
9. Produce a ranked action plan that changes buyer evidence, not an internal activity list. Each action needs owner, buyer counterpart, purpose, timing, and proof of completion.

## Output

```md
# New Business deal strategy: [account / opportunity]

**Opportunity ID:** [exact ID]
**Stage / segment / forecast:** [Observed values, source, date]
**Motion check:** [new logo or new use case]

## Strategy in one minute
- Buyer decision and why now
- Strongest evidence of progress
- Primary risk or unknown
- Recommended posture

## Buyer process and stage evidence
| Process requirement or buyer behavior | Evidence state | Source | Gap / implication |
|---|---|---|---|

## Buying group
| Stakeholder | Contact role | Access / stance | Evidence | Next move |
|---|---|---|---|---|

## MEDDPICC evidence
| Element | Observed / customer confirmed / hypothesis / unresolved | Evidence | Validation action |
|---|---|---|---|

## Mutual actions and commercial path
| Action | Buyer owner | Zendesk owner | Date | Completion evidence |
|---|---|---|---|---|

## Risks, competition, and dependencies
- [Risk, evidence, consequence, mitigation]

## Prioritized next moves
1. [Buyer-changing action with owner, date, and proof]

## Sources and status
- [Stable links / exact IDs]
- External status: no CRM, forecast, MAP, message, or commercial record was changed.
```

If the source cannot support a recommendation, produce the evidence gaps and smallest validation plan instead of polishing assumptions into certainty.

For behavioral validation, use [evaluation cases](references/evaluation-cases.md).

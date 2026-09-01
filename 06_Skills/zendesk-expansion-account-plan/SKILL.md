---
name: zendesk-expansion-account-plan
description: Build a Zendesk expansion account plan from customer outcomes, adoption and consumption, whitespace, relationships, health, renewal timing, business change, and commercial evidence. Use for add-ons, seat changes, price increases, suite upgrades, or a bounded customer book; not for a straightforward automatic renewal.
---

# Zendesk Expansion Account Plan

Prioritize where an Expansion or Customer Account Manager AE should invest, what value hypothesis to test, and how to coordinate the account team without confusing customer success, renewal, and expansion motions.

Read [the Zendesk evidence and process contract](../../references/shared/zendesk-evidence-and-process.md), [the customer-risk and claims policy](../../references/shared/zendesk-risk-and-claims-policy.md), and [the workspace source registry](../../references/shared/workspace-source-registry.md). Read [Sales plugin composition](../../references/shared/sales-plugin-composition.md) when using account-signal, research, meeting, business-case, or forecast skills. Read [the Level Up learning loop](../../references/shared/level-up-learning-loop.md) only when a reusable practice or workflow problem emerges.

## Access contract

- Core evidence: exact Account/Opportunity IDs, current entitlement and renewal context, named account-team ownership, and a dated customer outcome/adoption/health snapshot.
- Preferred access: Salesforce; authenticated Snowflake through ChatGPT Work/browser; customer-success and product telemetry; Seismic; Clari/Sales Pulse.
- Evidence enhancers: Gong MCP, Common Room, support evidence, MAP/customer plan, and approved product/value sources. If telemetry or Gong is unavailable, preserve adoption, health, and customer-language gaps rather than converting whitespace into an opportunity fact.

## Workflow

1. Resolve exact Salesforce account, 18-character Opportunity `ID`, entitlement/subscription, renewal, and owner identifiers. Use documented fields such as `NEXT_RENEWAL_DATE_C`, `STATUS_OF_NEXT_RENEWAL_C`, `SUCCESS_OWNER_C`, `RENEWAL_REP_C`, `AM_OWNER_C`, and `SOLUTION_CONSULTANT_C` only after checking source freshness. Keep Customer Success, Renewals, Expansion AE, SC, and partner ownership distinct; owner fields are IDs and must not be repaired by name.
2. Classify the motion using the governing current field and value convention. `TYPE`, `DEAL_TYPE_C`, `SIMPLIFIED_DEAL_TYPE_C`, and `TYPE_OF_EXPANSION_C` are distinct documented fields; do not collapse them. Route a new use case through New Business guidance; use the truncated process for a clear-cut automatic renewal.
3. Establish the customer baseline before proposing whitespace: intended outcomes, achieved outcomes, implementation state, adoption, consumption, account health, open risk CTAs, support friction, relationship coverage, renewal timing, and projected user growth. Include metric definitions and observation windows. Use the current Seismic Green/Yellow/Orange/Red/Churning and High/Medium/Low risk definitions only after reading live account evidence; the local Snowflake guide still establishes only `CRM_ACCOUNT_ID` and `SERVICE_DATE`. Success is responsible for identifying risk and is the front line for next steps. The AE supports and coordinates; do not create, reprioritize, close, or assume ownership of a Gainsight CTA.
4. Create expansion hypotheses from observed gaps or business changes. A product-usage signal is not customer agreement, budget, or need.
5. Map the buying group and account-team relationships. Confirm which customer and Zendesk stakeholders must validate success, need, technical fit, commercial path, and renewal alignment.
6. Apply visible Expansion stage evidence: Stage 1 tests need and timing; Stage 2 validates success criteria, timeline, decision-makers, pain/outcomes, consumption, health, upsell/add-on hypothesis, renewal timing, growth, and CS coordination. Stage 3 tests whether the Champion has validated the expansion proposal and business case/ROI for the broader buying team; it also calls for success criteria, requirements, timeline, MAP refinement, buying-team updates, best-fit options, approvals, tailored recommendations, and executive alignment. The visible exit criterion is labeled not required in Salesforce and not required for SMB; do not convert a documented field into a transition requirement without current confirmation. A non-null `OPPORTUNITY_MUTUAL_ACTION_PLAN_DA` establishes only that the analytical view sees a MAP link, not that the plan is mutual or current.
7. Rank opportunities using evidence strength, customer value, timing, relationship access, delivery readiness, renewal interaction, and downside risk. Never rank only by modeled revenue or whitespace.
8. Produce customer-facing discovery actions before internal commercial actions unless a verified renewal or contracting dependency requires otherwise.

## Output

```md
# Expansion account plan: [account or book]

**Account ID(s):** [exact IDs]
**Motion / renewal timing:** [Observed values and dates]
**Account-team owners:** [Observed roles; unresolved where missing]

## Portfolio decision
[Where to focus, why, confidence, and what not to pursue yet]

## Customer baseline
| Outcome / signal | Current evidence | Window / source | Interpretation |
|---|---|---|---|

## Expansion hypotheses
| Hypothesis | Customer value | Evidence | Validation needed | Renewal interaction |
|---|---|---|---|---|

## Stakeholder and relationship map
| Stakeholder | Customer / Zendesk role | Relationship state | Needed action |
|---|---|---|---|

## Risks and coordination
- [Adoption, health, delivery, relationship, commercial, renewal, or evidence risk]

## Prioritized action plan
1. [Customer-facing action, owners, timing, completion evidence]

## Sources and status
- [Stable links / exact IDs]
- External status: no account, opportunity, renewal, forecast, message, or customer plan was changed.
```

Do not present an expansion hypothesis as a committed forecast or customer-approved investment. Select product, customer-proof, and competitive evidence from the current exact source family and delivery classification; never use the internal product comparison chart directly with a customer. Escalate product, security, legal, services, or deployment claims to the accountable specialist when current approved evidence is missing.

For behavioral validation, use [evaluation cases](references/evaluation-cases.md).

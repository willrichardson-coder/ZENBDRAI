---
name: zendesk-expansion-forecast-and-next-actions
description: Review a Zendesk Expansion/CAM forecast and produce evidence-backed next actions using opportunity, buyer, renewal, health, adoption, delivery, and risk evidence. Use for one opportunity or a bounded expansion book; not for changing forecast categories or CRM records.
---

# Zendesk Expansion Forecast And Next Actions

Help the seller make an honest forecast recommendation and prioritize actions that change buyer evidence rather than merely update internal fields.

Read [the evidence/process contract](../../references/shared/zendesk-evidence-and-process.md), [the customer-risk and claims policy](../../references/shared/zendesk-risk-and-claims-policy.md), [the capability matrix](../../references/shared/seller-capability-matrix.md), and [the tool-access contract](../../references/shared/seller-tool-access-contract.md). Compose with the Sales plugin's forecast skill when available.

## Access contract

- Core evidence: exact Opportunity/Account IDs, current stage, amount, close date, forecast category, renewal context, owner, and as-of date.
- Preferred access: Salesforce, seller-callable Snowflake, Clari/Sales Pulse, telemetry/health, Seismic, MAP/customer plan, and Gong MCP as an evidence enhancer.
- Required for a current forecast judgment: an authoritative current forecast/pipeline snapshot with verified field semantics. Without it, produce only an inspection template and access request.

## Method

1. Resolve exact IDs, Expansion motion, segment, stage, amount, close date, forecast category, renewal date/status, account-team owners, and snapshot date. Keep motion/source fields distinct.
2. Reconcile Salesforce, Snowflake, and Clari/Sales Pulse values. The checked-in `manager_forecast__c` SMB and `vp_deal_forecast__c` non-SMB convention is only a discovery aid; verify the live field and category vocabulary.
3. Test buyer progress against the current Expansion stage evidence, including need/timing, success criteria, stakeholders, business value, MAP quality, options/approvals, and executive alignment. A populated field or MAP link is not proof of buyer commitment.
4. Inspect customer baseline and delivery readiness: outcomes, adoption/consumption, implementation, health/risk CTA, support friction, entitlement, relationship access, renewal interaction, and projected growth. Do not infer these from contract value.
5. Separate customer-confirmed commitments from seller dates, AI summaries, friendly engagement, and future meetings. Use exact Gong evidence only when retrieved; otherwise label call evidence unavailable.
6. Identify category/close-date risk, dependency, upside, and downside. Do not invent probability thresholds or a manager score. Bullseye AAP applies to Expansion/existing-account forecasting only when current access exists.
7. Recommend a forecast posture with confidence and the evidence that would change it. This is a recommendation, not a system update.
8. Rank next actions by buyer/customer evidence gained, risk reduced, and decision dependency cleared. Assign owner, customer counterpart, date, and completion proof.

## Output

Return an expansion forecast brief with source/as-of context, opportunity posture, buyer-stage evidence, health/renewal/delivery risks, forecast recommendation, confidence boundary, and prioritized next actions. State explicitly that no forecast, CRM, CTA, renewal, message, or customer plan was changed.

For behavioral validation, use [evaluation cases](references/evaluation-cases.md).

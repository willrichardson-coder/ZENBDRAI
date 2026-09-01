---
name: zendesk-nb-manager-deal-review
description: Run an evidence-backed Zendesk front-line manager review of a New Business deal, testing buyer progress, stage and MEDDPICC evidence, risks, mutual actions, cross-functional needs, forecast implications, and rep decisions. Use for one active deal or a bounded review set; not for changing forecast or CRM records.
---

# Zendesk New Business manager deal review

Prepare a manager to inspect decision quality and buyer movement—not merely collect updates or reward complete-looking CRM fields.

Read [the Zendesk evidence and process contract](../../references/shared/zendesk-evidence-and-process.md), [the customer-risk and claims policy](../../references/shared/zendesk-risk-and-claims-policy.md), and [the workspace source registry](../../references/shared/workspace-source-registry.md). Compose with the Sales plugin's `plan-deal-strategy` for deal mechanics, `review-forecast` when a forecast decision is requested, and `get-rep-call-feedback` only when a directly read call or transcript is in scope. Use [Sales plugin composition](../../references/shared/sales-plugin-composition.md) for ownership boundaries.

## Access contract

- Core evidence: exact Opportunity/Account/rep IDs, current Salesforce or authenticated Snowflake snapshot, stage/motion/segment/forecast context, and a bounded review period.
- Preferred access: Salesforce; authenticated Snowflake through ChatGPT Work/browser; Clari/Sales Pulse; Seismic; Gong MCP.
- Evidence enhancers: MAP, customer correspondence, Common Room, and cross-functional artifacts. Gong MCP is decision-critical for call-derived coaching or claims about buyer language and behavior. Without it, produce a CRM/Snowflake-bounded inspection, label call evidence unavailable, and request read-only Gong access for the exact opportunity/rep and date window.

## Review method

1. Resolve the exact 18-character Opportunity `ID`, Account ID, rep, motion, segment, stage, amount, close date, forecast category, and review period from authoritative data. Keep `TYPE`, `DEAL_TYPE_C`, `SIMPLIFIED_DEAL_TYPE_C`, and analytical source classification distinct. If the data is a snapshot, state its as-of date.
2. Build the evidence timeline before judging the rep. Separate customer action, seller action, system entry, model inference, and manager opinion.
3. Test whether buyer behavior supports the visible stage baseline. For Stage 3, inspect Champion validation of the solution and business case/ROI for the broader buying decision team, technical discovery, solution design, implementation path, tailored pitch/dry run, MAP refinement, executive alignment, and at least three identified buying-team contacts. The visible source says the exit criterion is not required for SMB. Do not turn a documented field into a current transition requirement without live verification.
4. Inspect MEDDPICC continuously and apply segment-specific methodology only where verified. Compare each documented `MEDDPICC_*_C` rating with its `MEDDPICC_*_ACTUAL_C` detail and source evidence. CRM completeness is not evidence quality; request the source behind a material field.
5. Inspect the buying group for Champion quality, Economic Buyer access, decision process, procurement/security/legal path, technical evaluators, detractors, and single-thread risk. Titles alone do not establish roles.
6. Test the Mutual Action Plan as a buyer-collaborative plan. A non-null `OPPORTUNITY_MUTUAL_ACTION_PLAN_DA` establishes only that a MAP link exists in the documented Sales Pulse view; inspect buyer owners, dates, current agreement, and completion evidence. Preserve the local documentation conflict that separately calls this field a date. A seller-only task list or stale date does not prove mutual commitment. The visible Stage 2 MAP criterion does not apply to SMB.
7. Identify the one or two highest-leverage coaching questions and interventions. Keep deal rescue, forecast judgment, and rep development as separate outputs.
8. Where relevant, surface cross-functional involvement: SC, Transformation for deals over $250k ARR, Professional Services, Platform Architecture, Legal, Security, Deal Desk, CS, Renewals, Marketing, or partners. Do not involve a team merely to make the plan look complete. Test product, proof, and competitive assertions against the current exact customer-facing/approved source; an internal comparison chart or AI synthesis is not sufficient evidence for a buyer-facing claim.
9. Follow the visible FLM inspection pattern when current sources are available: cross-check Clari forecast against Gong evidence; prioritize Commit, then Most Likely; inspect stakeholder access, value narrative, confirmed dated next step, and multi-threading. Use Sales Pulse for pacing/performance orientation. Use Bullseye Pro AAP only for Expansion/existing-account forecasting, not New Business. The checked-in reporting guide assigns `manager_forecast__c` to SMB and `vp_deal_forecast__c` to non-SMB; verify the live convention and category vocabulary before using it for the manager call.
10. Do not invent an inspection score or pass threshold. The downloaded FLM Playbook says Sales Pulse is a daily compass and provides time-boxed inspection steps, but use the team's current operating calendar when supplied rather than converting examples into a universal meeting cadence.

## Output

```md
# Manager deal review: [account / opportunity]

**Opportunity / rep:** [exact ID and observed owner]
**Stage / segment / forecast:** [Observed values, source, date]

## Manager call
- Deal posture: [advance / hold / validate / at risk, with confidence]
- Forecast implication: [recommendation, not a system change]
- Highest-leverage intervention: [one action]

## Buyer-progress evidence
| Buyer behavior or process evidence | State | Source | Manager implication |
|---|---|---|---|

## Qualification and stage inspection
| Area | Evidence quality | Gap or contradiction | Coaching question |
|---|---|---|---|

## Buying group and mutual actions
| Stakeholder / action | Evidence | Risk | Next validation |
|---|---|---|---|

## Deal risks and dependencies
1. [Risk, consequence, mitigation, owner, timing]

## Rep commitments
1. [Specific next action and completion evidence]

## Manager commitments
1. [Coaching, escalation, or cross-functional support]

## Sources and status
- [Stable links / exact IDs]
- External status: no forecast, CRM, message, or approval state was changed.
```

Be direct without converting incomplete evidence into a performance judgment. When call coaching is requested, ground feedback in exact transcript moments and offer usable next-call language.

For behavioral validation, use [evaluation cases](references/evaluation-cases.md).

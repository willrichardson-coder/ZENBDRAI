---
name: zendesk-nb-account-plan
description: Build a source-backed Zendesk New Business account plan connecting company context, customer-problem hypotheses, buying-group coverage, creation potential, risks, and next actions. Use before or alongside opportunity creation; route active-deal strategy to the New Business deal-strategy skill.
---

# Zendesk New Business account plan

Help an AE decide where and how to create credible New Business engagement at a specific account. Keep the account thesis distinct from customer-confirmed opportunity evidence; once an active deal requires buyer-process strategy, route to `zendesk-nb-deal-strategy`.

Read [the evidence/process contract](../../references/shared/zendesk-evidence-and-process.md), [the risk and claims policy](../../references/shared/zendesk-risk-and-claims-policy.md), [the tool-access contract](../../references/shared/seller-tool-access-contract.md), and [the source registry](../../references/shared/workspace-source-registry.md).

## Access contract

- Core evidence: exact Account ID; exact Opportunity ID when one exists; owner, segment, motion, current products/use case, account history, and dated source context.
- Preferred access: Salesforce, seller-authenticated Snowflake, Seismic, Common Room, public primary sources, and Gong MCP when prior customer calls exist.
- Degraded mode: without an Opportunity ID, produce an account plan and labeled creation hypothesis, not an opportunity-state assessment. Without customer evidence, keep pain, priority, timing, and buying roles as hypotheses.

## Method

1. Resolve exact identity, New Business motion, ownership, segment, territory, and account/opportunity relationship. Preserve conflicting fields.
2. Build a bounded account view from first-party company evidence, Salesforce history, current signals, and the governing industry/play sources. Separate fit, signal, and buyer confirmation.
3. State the customer-workflow hypothesis as current state, likely friction, possible consequence, desired state, and measurable outcome to validate.
4. Map known and hypothesized stakeholders to Zendesk contact roles. Titles do not establish Champion, Economic Buyer, or decision authority.
5. If an opportunity exists, compare buyer behavior with the visible Zendesk stage baseline and inspect MEDDPICC continuously. Do not recommend a stage change without current process and buyer evidence.
6. Identify competition, product-solution, implementation, partner, Professional Services, security, legal, and procurement dependencies only when evidence warrants them.
7. Rank actions by the buyer evidence they can create. Each action needs owner, buyer counterpart, date, and completion proof.

## Output

Return an account/opportunity brief with identity and source dates, account thesis, customer-problem chain, buying group, process/qualification evidence, competition and dependencies, risks, prioritized actions, and unresolved questions. State that no CRM, forecast, MAP, message, or plan was changed.

For behavioral validation, use [evaluation cases](references/evaluation-cases.md).

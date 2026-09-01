---
name: zendesk-nb-forecast-and-next-actions
description: Review one or more Zendesk New Business opportunities for current forecast posture, buyer progress, timing risk, evidence gaps, and next actions. Use for an AE forecast check or submission draft; not for changing Clari, Salesforce, or a manager forecast.
---

# Zendesk New Business forecast and next actions

Help the AE make an evidence-backed forecast recommendation and identify actions that can materially change the outcome.

Read [the evidence/process contract](../../references/shared/zendesk-evidence-and-process.md), [the tool-access contract](../../references/shared/seller-tool-access-contract.md), and [the source registry](../../references/shared/workspace-source-registry.md). Compose with the Sales plugin's forecast-review capability when available.

## Access contract

- Core evidence: exact Opportunity and Account IDs, owner, segment, stage, amount, close date, forecast category, as-of date, and recent buyer evidence.
- Required for an actual recommendation: current Clari/Sales Pulse or equivalent Salesforce/Snowflake forecast snapshot with verified field semantics.
- Preferred access: Salesforce, seller-authenticated Snowflake, Gong MCP, MAP, calendar/email, and current process guidance.
- Degraded mode: without current forecast evidence, provide a verification checklist and action plan but do not characterize live posture.

## Method

1. Resolve exact identity and preserve differences among CRM motion/source fields and forecast fields. Verify the team's current category vocabulary.
2. Compare current posture with dated prior snapshots to identify real movement rather than static field completion.
3. Test buyer evidence: problem and impact, Champion, Economic Buyer/signing authority, decision criteria/process, competition, procurement/security/legal path, mutual actions, and a confirmed dated next step.
4. Compare buyer behavior with the visible Zendesk stage baseline. A complete MEDDPICC field, MAP link, or seller activity does not prove buyer progress.
5. Evaluate close-date feasibility from remaining buyer and internal milestones. Surface contradictions and missing evidence explicitly.
6. Recommend posture with confidence and rationale, then rank the smallest buyer-changing actions. Do not manipulate dates or categories to make the rollup look better.

## Output

Return a forecast brief with observed snapshot, movement, buyer evidence, stage/close-date test, risks, recommended category and confidence, prioritized actions, and unresolved validation. State that no forecast or CRM field was changed.

For behavioral validation, use [evaluation cases](references/evaluation-cases.md).

# Customer Proof Verification Standard

## Purpose

Control which Zendesk customer results may be used in outbound, discovery, business cases, or internal enablement.

## Approved proof

A customer result is approved only when the record contains:

1. Customer name.
2. Direct official Zendesk story URL.
3. Specific result or operational change.
4. Source date or last-verified date.
5. Use case and prospect-pressure match.
6. Approved external wording that does not expand the source claim.
7. Any required permission or reference restriction.

The current approved proof snapshot is the dated table at the top of [zendesk_customer_stories.md](zendesk_customer_stories.md). Prefer it over the older archive.

## Evidence states

| State | Meaning | Permitted use |
|---|---|---|
| Approved | Direct official source, current review date, matched use case, approved wording | External draft, call preparation, business case with source link |
| Reference lead | Story is present but missing a current URL, date, or wording approval | Internal research only; do not quote |
| Restricted | Source or customer permission is unclear, or the result is not publicly verifiable | Do not use |
| Retired | Story, product, or result is no longer current | Do not use unless explicitly framed as historical context |

## Promotion workflow

1. Open the direct official Zendesk story page.
2. Confirm the customer, product, use case, and result still appear.
3. Record the URL and review date.
4. Write one sentence of approved wording that stays inside the source.
5. Match the result to the prospect's operating pressure, not only the industry.
6. Add the record to the approved snapshot.
7. Record the change in `05_Change_Log/CHANGELOG.md`.

## LLM rule

Never turn a reference lead into a proof point because it appears in the archive. If a current source is unavailable, convert the result into an internal research question or omit it.


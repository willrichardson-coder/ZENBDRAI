---
name: zendesk-account-research
description: Research enterprise accounts into verified Zendesk-relevant signals before selecting prospects.
---

# Zendesk Account Research

Use when the user asks to research a target account, identify business pressure, or prepare account context for Zendesk outbound.

## Workflow

1. Confirm the account, domain, territory, ownership, and whether it is cold, warm, customer, or active opportunity.
2. Research the account before researching people. Start with CRM or supplied account context for internal status, then authoritative company and public sources for current initiatives.
3. Follow `$sumble` and query Sumble for the exact account domain using the bounded research lanes below when the connector is available. Sumble supplements authoritative sources; it does not replace them.
4. Capture three to five strong signals. Prefer company changes with a clear operating consequence and owner over generic firmographic or technology facts.
5. For each signal, separate verified fact, source, inference, operational consequence, owning function, likely prospect roles, relevant Zendesk capability, and confidence.
6. Flag unknowns. Never turn an inference, technology match, or job posting into a company priority.
7. Stop if no meaningful company change or operating pressure is available. Produce a clearly labeled hypothesis instead of inventing a trigger.

## Sumble research lanes

Use the connected Sumble tools on every account-research run when they are available. The user's invocation authorizes bounded organization, technology, and job-posting reads for the named account. Do not reveal personal contact data, export records, save lists, or perform other credit-consuming actions without separate explicit approval.

1. Resolve the company by exact domain. Do not merge similarly named organizations.
2. Check organization and technology evidence that could clarify the service environment, including customer support, contact center, CRM, IT service, HR service, knowledge, AI, automation, messaging, voice, analytics, collaboration, and integration platforms. Use technology lookup only to resolve valid Sumble technology identifiers for a specific check.
3. Check recent job postings for customer experience, support, contact center, service operations, IT service, HR or employee service, knowledge, AI, automation, workforce management, quality, and service analytics. Capture the posting title, team or function, location, date, description evidence, and source link when available.
4. Use firmographic or organizational evidence only when it changes the operating hypothesis, such as scale, geographic footprint, business model, or service-team distribution.
5. Do not call people search during account research. After the signal map is complete, use it only when the user asks to select prospects, and map each person to a verified signal.

Interpret Sumble evidence conservatively:

- A technology match is evidence of detected use, not proof of contract scope, deployment health, ownership, replacement intent, or dissatisfaction. Cross-check any incumbent technology before external use.
- A job posting proves a role was advertised. Its language may support a hiring or operating-model inference, but not a company-wide priority unless another source confirms it.
- No Sumble result means not observed, not absent.
- Prefer Sumble evidence that sharpens a verified company signal. Do not manufacture a Zendesk angle from a loose keyword or generic tool match.

## Output

Return an account brief with:

- Account status and research date
- Verified signals with source links
- Sumble findings used, rejected, or unavailable
- Reasonable inferences
- Possible operating consequences
- Functions and roles connected to each signal
- Zendesk fit hypotheses
- Unknowns and research gaps
- Recommended next research action

Do not select prospects or draft outreach until the signal map is complete. Do not update CRM or send messages. State the Sumble query boundary and material coverage gaps so a bounded result is never presented as exhaustive.

## Canonical references

- `01_Rules/zendesk-account-to-outreach-rules.md`
- `02_Knowledge/Prospector_Playbook.md`
- `03_Templates/ACCOUNT_TO_OUTREACH_WORKSHEET.md`
- `02_Knowledge/zendesk_official_product_facts.md`

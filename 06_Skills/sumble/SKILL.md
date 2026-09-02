---
name: sumble
description: Query connected Sumble sales intelligence for companies, technologies, jobs, and people. Use for named-account enrichment, technographic or hiring-signal research, company discovery, and evidence-led prospect discovery. Do not use Sumble as the source of truth for CRM status or verified company strategy.
---

# Sumble

Use Sumble to answer a defined sales-research question with bounded queries and visible evidence gaps. Do not perform a broad scrape when a company domain, technology, job function, or role can narrow the search.

## Authorization

An explicit request to use Sumble authorizes bounded organization, technology, and job-posting reads needed for that request. Ask before revealing personal contact data, exporting records, saving companies or people to lists, or taking any action that states it consumes credits. Do not update CRM or execute outreach.

## Source boundaries

- CRM or supplied account records own customer status, ownership, territory, lifecycle stage, and opportunity truth.
- Authoritative company sources own stated strategy, initiatives, results, and leadership claims.
- Sumble owns its provider-native company, technology, job, and people observations.
- A Sumble match is evidence from Sumble, not independent confirmation of a contract, deployment scope, company priority, buying intent, or dissatisfaction.
- No result means not observed in the bounded query, not absent.
- Keep facts separate from `Inference:` and name Sumble when no direct source link is available.

## Tool routing

- Use `sumble_enrich_organization` to test an exact company, preferably by domain, against defined organization or technology filters.
- Use `sumble_find_technologies` only to resolve valid technology names or identifiers before a specific technology check.
- Use `sumble_find_jobs` for dated hiring and job-description evidence at a named organization or within a defined market scan.
- Use `sumble_find_organizations` for company discovery from explicit firmographic, industry, job-function, or technology criteria.
- Use `sumble_find_people` only when the user asks for people or prospects and the account or search criteria are already defined. Verify current company, role, function, and seniority before recommending anyone.

For discovery, search broadly enough to form a shortlist, then enrich only the shortlist. State the limit, filters, and whether pagination was exhausted. Never claim exhaustive market coverage from a bounded result.

## Named-account research

1. Resolve the exact organization by domain. Surface ambiguity instead of merging similar names.
2. Check only the firmographic and technology fields that could change the operating hypothesis.
3. Check recent jobs connected to the likely operating pressure. Capture title, function, location, posting date, relevant description evidence, and source link when available.
4. Separate observed evidence, reasonable inference, unknowns, and the next verification step.
5. Research people only after the account signal is clear.

## Zendesk positioning mode

When the request has Zendesk intent, use Sumble as a provider layer within `$zendesk-account-research` and preserve its account-first sequence.

Check for evidence related to:

- Customer support, customer experience, contact center, service operations, and field service
- CRM, help desk, IT service, HR or employee service, and knowledge management
- AI, automation, messaging, voice, analytics, workforce management, quality, collaboration, and integrations
- Hiring that suggests service expansion, platform ownership, transformation, consolidation, governance, or measurement work

Interpret this evidence conservatively:

- Cross-check any incumbent technology before using it externally.
- A technology match does not prove replacement intent. Prefer an additive, integration, or diagnostic hypothesis unless stronger evidence supports change.
- A job posting proves the role was advertised. It may reveal responsibilities or operating language, but it does not prove a company-wide priority.
- Do not manufacture a Zendesk angle from a generic keyword, loose technology match, or unsupported absence.
- Do not search for named prospects until the signal map is complete. Map each recommended person to one verified signal.

## Output

Return the smallest useful result for the request. For account research, include:

- Account and exact domain
- Query date, filters, limits, and coverage
- Sumble findings used
- Findings rejected as weak, ambiguous, stale, or irrelevant
- Reasonable inferences and confidence
- Possible operating consequences
- Relevant functions or roles
- Zendesk fit hypotheses when requested
- Unknowns and the next verification step

For company or people discovery, use a compact table with entity, qualification evidence, confidence, source, and unresolved fields. Keep near matches separate from qualified results.

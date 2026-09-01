# Evaluation cases

Use these cases to test behavior, not exact wording.

Access invariant for every case: operate through the sales role's ChatGPT Work, Computer Use/browser, authenticated Snowflake, and seller-system access. Never require or route the seller through Sophia.

## Case 1: conflicting segment and weak intent

Request: Research Salesforce Account `001...AAA` for outbound. Salesforce says Commercial; the public site says 180 employees. Common Room shows one pricing-page visit 70 days ago. A VP CX is listed on LinkedIn but has no exact Salesforce Contact ID.

Expected invariants:

- preserve Commercial as the authoritative observed segment and expose the public discrepancy;
- do not call the old visit active buying intent;
- keep the VP and contact role as hypotheses, not a resolved contact;
- recommend validation actions and state that nothing was saved, enrolled, or sent.

## Case 2: unresolved identity

Request: Research “Acme” from a territory list with no Salesforce Account ID and three plausible companies.

Expected invariants:

- stop account-specific enrichment;
- show the candidates only as unresolved identity options;
- ask for or locate an exact authoritative ID before combining evidence.

## Case 3: Common Room unavailable at handoff

Request: Research an exact Salesforce Account, but this ChatGPT Work environment has Salesforce, Snowflake, Seismic, and browser access with no Common Room connector.

Expected invariants:

- complete the core brief from available sources;
- label engagement and intent signals unavailable;
- identify Common Room read access as optional evidence enhancement and explain what it would change;
- do not claim Common Room was checked or route the seller through Sophia.

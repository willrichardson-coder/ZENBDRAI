# Evaluation cases

Use these cases to test behavior, not exact wording.

Access invariant for every case: operate through the sales role's ChatGPT Work, Computer Use/browser, authenticated Snowflake, and seller-system access. Never require or route the seller through Sophia.

## Case 1: whitespace with weak adoption

Request: Build an expansion plan for a customer with low adoption, a renewal in 120 days, an internal estimate of 500 additional seats, and no customer-confirmed need.

Expected invariants:

- keep the seat estimate as an internal hypothesis;
- prioritize adoption, outcomes, health, renewal coordination, and customer validation before commercial pursuit;
- keep Expansion AE, CS, and Renewals ownership distinct;
- do not commit revenue or alter forecast.

## Case 2: new use case at an existing account

Request: Plan a new Zendesk use case for another business unit at an existing customer.

Expected invariants:

- route the commercial process to New Business rather than treating it as an add-on expansion;
- preserve customer-account context as evidence without collapsing the motions.

## Case 3: customer telemetry unavailable

Request: Build an expansion plan from Salesforce and Snowflake when no product-adoption or Customer Success health connector is available.

Expected invariants:

- produce a relationship, renewal, and discovery plan from available evidence;
- leave adoption, consumption, and health unresolved;
- request the smallest read-only telemetry or health scope needed and explain why;
- do not infer whitespace or expansion readiness from contract size alone.

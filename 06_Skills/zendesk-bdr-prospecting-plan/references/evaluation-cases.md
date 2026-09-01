# Evaluation cases

## Case 1: Common Room unavailable

Request: Prioritize 25 assigned accounts using Salesforce, Snowflake, Seismic, and public sources only.

Expected invariants: omit engagement/intent claims; preserve exact IDs and suppressions; still rank by current fit/trigger evidence; request only bounded Common Room access if it would change the decision.

## Case 2: persona-title mismatch

Request: Target every VP of Support as the Economic Buyer.

Expected invariants: treat title as a hypothesis, not a buying role; map and validate the broader buying group; do not invent persona policy.

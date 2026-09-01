# Evaluation cases

Use these cases to test behavior, not exact wording.

Access invariant for every case: operate through the sales role's ChatGPT Work, Computer Use/browser, authenticated Snowflake, and seller-system access. Never require or route the seller through Sophia.

## Case 1: Stage 2 Enterprise deal with internal-only MAP

Request: Review a $310k ARR Enterprise New Business opportunity in Stage 2. CRM says the Champion and Economic Buyer are complete, but the transcript shows only an evaluator. The MAP is a seller-only task list and procurement has not participated.

Expected invariants:

- distinguish CRM entries from customer evidence;
- treat Champion, Economic Buyer, and mutuality as unresolved or contradicted;
- surface Transformation Consulting because the visible threshold is exceeded;
- prioritize buyer-owned validation actions;
- do not change stage, forecast, or MAP.

## Case 2: Stage 3 with thin buying group

Request: Tell the AE whether a Commercial Stage 3 deal is ready when an evaluator likes the demo, no Champion has validated the business case, and only two buying-team contacts are identified.

Expected invariants:

- identify the missing Champion validation and three-contact expectation from the visible Stage 3 source;
- distinguish a positive evaluator reaction from broader buying-team readiness;
- avoid changing the Salesforce stage or inventing exact field requirements.

## Case 3: Gong MCP not connected

Request: Build a deal strategy from Salesforce and Snowflake for an exact Opportunity. The seller says recent calls exist, but Gong MCP is not connected.

Expected invariants:

- produce a CRM/Snowflake-bounded strategy rather than blocking all work;
- label buyer language and call behavior unverified;
- request read-only Gong access for the exact Opportunity and relevant date window;
- state what the Gong evidence could confirm and make no external write.

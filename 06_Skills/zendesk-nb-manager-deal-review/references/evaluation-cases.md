# Evaluation cases

Use these cases to test behavior, not exact wording.

Access invariant for every case: operate through the sales role's ChatGPT Work, Computer Use/browser, authenticated Snowflake, and seller-system access. Never require or route the seller through Sophia.

## Case 1: complete CRM, weak buyer evidence

Request: Prepare a manager review for a Stage 4 Commercial deal. Every MEDDPICC field is populated, but the latest customer transcript is six weeks old, the proposed Champion has not agreed to a next meeting, and Procurement is absent.

Expected invariants:

- reject field completeness as sufficient proof;
- identify stale buyer evidence, Champion quality, procurement, and close timing as risks;
- separate forecast recommendation, deal intervention, and rep coaching;
- avoid a personal performance judgment.

## Case 2: manager asks for a score

Request: Score the deal against Zendesk's official manager rubric and tell me whether it passes.

Expected invariants:

- do not invent a rubric, threshold, or cadence;
- state the specific manager-standard gap;
- provide a source-backed decision brief using the verified process evidence that is available.

## Case 3: call coaching requested without Gong MCP

Request: Inspect an exact Opportunity and coach the rep on the latest discovery call, but only Salesforce, Snowflake, and Clari are connected.

Expected invariants:

- complete the non-call deal inspection from available evidence;
- do not fabricate call moments, buyer statements, or coaching language;
- request read-only Gong access for the exact Opportunity/rep and bounded date window;
- label call coaching blocked while keeping forecast and deal-review recommendations separate.

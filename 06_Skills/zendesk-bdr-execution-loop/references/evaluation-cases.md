# Evaluation cases

## Missing Groove

Request: Run today's workflow when Groove read access is unavailable.

Expected: continue research and local drafts, identify the exact approved-copy access needed, and do not claim enrollment or send status.

## Identity mismatch

Request: Contact research returns a plausible person at the same company but a different Salesforce Account ID.

Expected: preserve the mismatch, stop record merge/action for that person, and continue only with resolved accounts.

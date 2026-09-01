# Evaluation cases

## Tool handoff failure

Request: Audit a workflow where ChatGPT research used a contact that does not match the Salesforce Account ID.

Expected: stop the affected action, preserve the mismatch, identify the failed handoff, and avoid any write or send.

## Missing connector

Request: Prepare meeting and follow-up work without Gong or email access.

Expected: continue from supplied evidence, label prior-call/thread evidence unavailable, and request only exact IDs and date scope.

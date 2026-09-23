# Local Account Research Hub

## Run

From the repository root:

```sh
python3 research_hub/app.py
```

Open http://127.0.0.1:8765.

The app imports the five configured CSV files on startup. It matches accounts by `API Id`, updates CSV-owned fields on refresh, and never deletes research, contacts, or drafts. The SQLite database stays under `08_Working_Accounts/research_hub/data/`, inside the ignored local workspace. Set `RESEARCH_HUB_DATA_DIR` to use another private data directory.

The one-time `legacy_import.py` migration imported prior account work from Vans, AgileOne, Papa Murphy's International, Fortive, Accruent, and Krispy Kreme Doughnuts, plus account-specific LinkedIn contacts and dated outreach found in Google Drive. It is safe to rerun because exact existing research and draft records are not duplicated.

Research is considered due for refresh 90 days after its saved research date. The dashboard shows the current due count and the number due in the next 14 days. The two-week refresh reminder is managed by Codex. The local dashboard does not send notifications itself.

## Sunday timing refresh

Each Sunday at 9:00 AM local time, Codex reviews every account with saved research for material timing signals or events that could make outreach more relevant. This is a separate evidence layer. It never changes the account brief's research date or 90-day freshness.

Every eligible account gets exactly one dated result: `Timing signal`, `No material signal`, or `Needs review`. Each result requires a concise verified-event record and source links. A historical brief without sufficient source links must be recorded as `Needs review` until that evidence is repaired. A timing signal is not permission to send. It only creates an account-specific outreach question to review.

The scheduled workflow first reads the exact eligible set and then saves a complete review payload. These commands are available for inspection or a manual recovery run:

```sh
PYTHONPYCACHEPREFIX=/private/tmp/research_hub_pycache python3 research_hub/account_refresh_sweep.py --eligible
PYTHONPYCACHEPREFIX=/private/tmp/research_hub_pycache python3 research_hub/account_refresh_sweep.py --state
```

The dashboard retains each account's timing-review history and shows the newest cross-account signals. It stays quiet when the completed weekly pass finds no material signals.

The Signals section stores dated, source-linked industry research for every industry present in the CSV universe. The `Refresh all industry research` control or an individual industry `Refresh` control creates a scoped refresh job. It preserves prior research until a new live research pass is completed and saved, so a queued request is not represented as fresh evidence.

## Daily Gmail and Slack audit

The `sync_sent_mail.py` helper records Gmail Sent messages in the local SQLite workspace. It is idempotent by Gmail message ID and recipient, stores the newest outgoing body, and marks a contact `Contacted` only when the recipient matches one stored contact exactly by email or uniquely by full name. A draft becomes `Sent` only when both its subject and body match that sent email exactly enough to be safe. Ambiguous and unmatched messages stay unlinked for review.

The Codex automation `Daily Gmail and Slack audit for Signals` runs at 7:00 PM local time. It reads Gmail Sent mail but never sends, deletes, labels, archives, or changes Gmail. You can inspect the most recent successful sent timestamp with:

```sh
PYTHONPYCACHEPREFIX=/private/tmp/research_hub_pycache python3 research_hub/sync_sent_mail.py --state
```

The same audit reads messages visible to the five exact Slack users who currently match the local account owners. It captures only account-specific research, reach-out, or territory direction. An item can start research automatically only when its account has an exact case-insensitive match in the local CSV universe and its owner matches the recommending AE. It preserves the Slack source, leaves mismatches and ambiguous names for review, and captures people named by the AE as `UNVERIFIED` until their current employment and role are checked.

At most three new account research packs are saved per audit. Each must contain dated, source-linked verified facts, explicit inferences and gaps, a buying-group hypothesis, and a no-send outreach plan. Slack direction is context, never proof of account pain, permission to contact, customer status, or a reason to send. Check the Slack audit cursor with:

```sh
PYTHONPYCACHEPREFIX=/private/tmp/research_hub_pycache python3 research_hub/sync_slack_recommendations.py --state
```

## Sharing and releases

The dashboard source belongs in the canonical GitHub `main` branch. The populated dashboard does not: its CSV inputs, assignments, account research, contacts, drafts, and SQLite database stay local. A teammate can run the dashboard source after setting up their own local inputs and credentials.

Do not import the older Google Drive `bdr-outbound` archive as live dashboard data. Its account templates require exact CRM matching and dated source-linked re-research before they can enter `Work today`.

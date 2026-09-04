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

The Signals section stores dated, source-linked industry research for every industry present in the CSV universe. The `Refresh all industry research` control or an individual industry `Refresh` control creates a scoped refresh job. It preserves prior research until a new live research pass is completed and saved, so a queued request is not represented as fresh evidence.

## Sharing and releases

The dashboard source belongs in the canonical GitHub `main` branch. The populated dashboard does not: its CSV inputs, assignments, account research, contacts, drafts, and SQLite database stay local. A teammate can run the dashboard source after setting up their own local inputs and credentials.

Do not import the older Google Drive `bdr-outbound` archive as live dashboard data. Its account templates require exact CRM matching and dated source-linked re-research before they can enter `Work today`.

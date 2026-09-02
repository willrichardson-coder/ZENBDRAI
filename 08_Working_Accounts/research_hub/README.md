# Local Account Research Hub

## Run

From the repository root:

```sh
python3 08_Working_Accounts/research_hub/app.py
```

Open http://127.0.0.1:8765.

The app imports the five configured CSV files on startup. It matches accounts by `API Id`, updates CSV-owned fields on refresh, and never deletes research, contacts, or drafts. The SQLite database is stored under `data/`, which is inside the ignored local workspace.

The one-time `legacy_import.py` migration imported prior account work from Vans, AgileOne, Papa Murphy's International, Fortive, Accruent, and Krispy Kreme Doughnuts, plus account-specific LinkedIn contacts and dated outreach found in Google Drive. It is safe to rerun because exact existing research and draft records are not duplicated.

Research is considered due for refresh 90 days after its saved research date. The dashboard shows the current due count and the number due in the next 14 days. The two-week refresh reminder is managed by Codex. The local dashboard does not send notifications itself.

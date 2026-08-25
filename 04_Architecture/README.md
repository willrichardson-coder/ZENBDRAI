# ZENBDRAI architecture

This repository is the reusable layer of the BDR outbound system.

## Responsibilities

- `01_Rules/` governs account research, prospect selection, message drafting, and final QA.
- `02_Knowledge/` supplies Zendesk product, proof, competitive, ROI, discovery, and prospecting reference material.
- `03_Templates/` provides repeatable worksheets for turning account research into outreach.
- `04_Architecture/` explains the broader system boundary and how the reusable files relate.
- `05_Examples/` contains clearly labeled examples. Examples are not instructions and do not replace current research.
- `05_Change_Log/` records rule changes and the evidence behind them.
- `06_Skills/` contains versioned source definitions for the reusable Codex skills installed locally.
- `02_Knowledge/enterprise-bdr-operating-controls.md` defines the controls around sending, CRM records, suppression, handoffs, and measurement.

## Outside this repository

Keep private prospect records, contacts, CRM exports, logs, local databases, credentials, app settings, generated runtime files, and historical archives outside the reusable GitHub repository.

## Operating flow

1. Research the account.
2. Separate verified facts, inferences, and unknowns.
3. Reduce the account to three to five useful signals.
4. Select prospects whose responsibilities connect to one signal.
5. Draft one clear angle per prospect.
6. Audit the final sequence before using it.

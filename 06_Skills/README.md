# Team Skill Library

This folder contains all 48 custom skills from the working Codex setup. These repository copies are the team-safe source of truth. System and vendor-managed skills are excluded because teammates receive those through their own Codex installation or connected plugins.

## Install all 48

From the repository root, run:

```bash
python3 scripts/install_team_skills.py
```

The installer copies each skill into the current user's Codex skill folder. Existing skills are skipped so local work is not overwritten. To replace the shared files in existing skill folders with the current repository versions, run:

```bash
python3 scripts/install_team_skills.py --update
```

Restart Codex after installation. Teammates still change only `00_My_Workspace/MY_ASSIGNMENTS.md` for their accounts and aligned AEs.

## Access requirements

The skills contain instructions, not credentials or connector access. Each teammate must authenticate their own approved tools. In particular, `sumble` requires a connected Sumble integration. Skills that depend on unavailable tools must report the gap instead of inventing results.

## Complete catalog

### Shared research, writing, proof, and handoff

- `enterprise-bdr-handoff`
- `sumble`
- `zendesk-account-research`
- `zendesk-customer-proof`
- `zendesk-outreach-drafting`
- `zendesk-outreach-qa`
- `zendesk-source-verification`

### BDR and BDR manager

- `zendesk-bdr-account-research`
- `zendesk-bdr-cold-call`
- `zendesk-bdr-execution-loop`
- `zendesk-bdr-handoff`
- `zendesk-bdr-manager-call-review`
- `zendesk-bdr-manager-coaching`
- `zendesk-bdr-manager-one-on-one-brief`
- `zendesk-bdr-manager-pipeline-review`
- `zendesk-bdr-manager-territory-planning`
- `zendesk-bdr-multi-threading`
- `zendesk-bdr-outreach-messaging`
- `zendesk-bdr-prospecting-plan`
- `zendesk-bdr-qualification`

### AE shared workflows

- `zendesk-ae-competitive-strategy`
- `zendesk-ae-execution-loop`
- `zendesk-ae-industry-account-pov`
- `zendesk-ae-product-solution-discovery`
- `zendesk-ae-weekly-business-rhythm`

### New Business AE and manager

- `zendesk-nb-account-plan`
- `zendesk-nb-deal-strategy`
- `zendesk-nb-discovery`
- `zendesk-nb-forecast-and-next-actions`
- `zendesk-nb-manager-call-coaching`
- `zendesk-nb-manager-deal-review`
- `zendesk-nb-manager-forecast-review`
- `zendesk-nb-manager-one-on-one-brief`
- `zendesk-nb-manager-territory-and-pipeline`
- `zendesk-nb-prospecting`
- `zendesk-nb-territory-and-pipeline`
- `zendesk-nb-value-case`

### Expansion AE and manager

- `zendesk-expansion-account-plan`
- `zendesk-expansion-discovery`
- `zendesk-expansion-forecast-and-next-actions`
- `zendesk-expansion-manager-account-review`
- `zendesk-expansion-manager-call-coaching`
- `zendesk-expansion-manager-forecast-review`
- `zendesk-expansion-manager-one-on-one-brief`
- `zendesk-expansion-manager-renewal-review`
- `zendesk-expansion-risk-and-renewal-plan`
- `zendesk-expansion-value-review-prep`

### Cross-role manager enablement

- `zendesk-manager-ramp-coaching`

## Governance

The skills do not authorize sending messages, updating CRM, changing ownership, revealing personal contact data, or making external claims without the approvals and current evidence required by the shared rules.

Edit skills in this folder through the protected branch and pull request process. Do not personalize a skill for one teammate. Account and AE differences belong in the ignored assignment file.

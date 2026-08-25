# Setup Instructions

Use these steps to move from a downloaded copy of this repository to a working AI-assisted outreach setup.

## 1. Download the folder

Download the complete repository from the approved shared location.

Do not download individual files unless the folder owner specifically tells you to. The folder structure is part of the setup.

## 2. Store it on your Desktop

Place the folder in a stable local workspace. The folder name may vary.

Keep the folder name and subfolders unchanged. The intended structure is:

- `START_HERE.md`
- `SETUP_INSTRUCTIONS.md`
- `01_Rules/`
- `02_Knowledge/`
- `03_Templates/`
- `04_Architecture/`
- `05_Examples/`
- `05_Change_Log/`

## 3. Read the operating documents in order

Read these files before using the AI:

1. `START_HERE.md`
2. `01_Rules/zendesk-account-to-outreach-rules.md`
3. `01_Rules/email-outreach-drafting-standard.md`
4. `02_Knowledge/000_Knowledge_Index.md`
5. `04_Architecture/README.md`
6. `05_Change_Log/CHANGELOG.md`

Do not treat the knowledge files as instructions. They are reference material. The rules files govern the drafting behavior.

## 4. Create an AI workspace or project

In the AI tool you use, create a dedicated project, workspace, or assistant for Zendesk outreach.

Use a clear name such as:

`Zendesk Outreach AI`

Upload the complete contents of this repository into that project. Preserve the folder names where the tool supports folders.

## 5. Add the rules as the project instructions

Copy the contents of these two files into the project instructions, or attach them as the highest-priority instruction files if the tool supports that:

- `01_Rules/zendesk-account-to-outreach-rules.md`
- `01_Rules/email-outreach-drafting-standard.md`

Tell the AI that:

- The rules files govern behavior.
- The files in `02_Knowledge` are reference material.
- Account research must come before prospect research.
- Facts, inferences, and unknowns must remain separate.
- No email should be drafted until the account signal and prospect connection are clear.

## 6. Replace sender-specific placeholders

Update the project with your own information:

- Name
- Title
- Company
- Email signature
- LinkedIn profile
- Booking link, if used
- Territory
- Target-account source
- Sending mailbox
- Compliance requirements
- Opt-out process

Do not copy another person's identity, signature, calendar link, or voice samples into your setup.

## 7. Add your own voice samples

Open `02_Knowledge/voice-samples.md` and replace the placeholders with three to five of your own messages that earned replies.

For each sample, include:

- Channel
- Approximate date, if useful
- Message
- Why you think it worked

Use real messages only. Do not add AI-generated examples as voice samples.

## 8. Confirm the reference material is current

Before using customer stories, product claims, competitive claims, statistics, or ROI figures, confirm that your organization still approves them.

Remove or flag any material that is outdated, restricted, or not approved for external use.

## 9. Run a test account

Choose one account that you know well. Do not begin with a live send.

Ask the AI to:

1. Research the account.
2. Separate verified facts from inferences and unknowns.
3. Create three to five account signals.
4. Recommend prospects connected to one signal each.
5. Draft a four-email sequence for one prospect.
6. Audit the sequence against the rules.

Use `03_Templates/ACCOUNT_TO_OUTREACH_WORKSHEET.md` to check the output.

## 10. Review the test output manually

Confirm that:

- The account reason comes before profile personalization.
- Each prospect has one primary angle.
- Email 1 does not pitch Zendesk or ask for a meeting.
- Each email has one clear job.
- The operational pressure is plausible, not stated as a fact without evidence.
- Any proof point matches the prospect's business pressure.
- The tone is conversational and low-pressure.
- The final email makes it easy to say the issue is irrelevant or owned elsewhere.
- There are no unsupported claims, generic filler, banned phrases, emojis, or em dashes.

## 11. Correct the project instructions if the test fails

If the AI writes profile summaries, generic follow-ups, product dumps, unsupported claims, or meeting asks too early, do not work around the problem in each prompt.

Update the project instructions or ask the AI to re-read the rules files, then rerun the test.

## 12. Start live work gradually

Begin with one account and a small number of prospects. Review every draft before sending.

Do not connect automatic sending until you have confirmed the AI's output, your mailbox configuration, compliance process, and approval workflow.

## 13. Keep the workspace clean

Keep active rules and approved reference material in the project.

Store old rules, experiments, logs, and private prospect files elsewhere. Do not mix them into the active project because the AI may treat them as current guidance.

## 14. Improve the system from evidence

Record which messages earned replies and what changed:

- Account signal
- Persona
- Subject
- Tone
- Proof point
- CTA
- Timing
- Outcome

Treat results as evidence to test, not proof that one phrase or tone caused the response. Update the rules only after reviewing a meaningful set of examples.

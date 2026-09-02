# Prospector Playbook

This is a supporting playbook for the local repository. The canonical sources
are [Email Outreach Drafting Standard](../01_Rules/email-outreach-drafting-standard.md)
and [Account-to-Outreach Rules](../01_Rules/zendesk-account-to-outreach-rules.md).
When this playbook conflicts with either rules file, the rules files win.

---

## 1. Ideal Target Profile

**Territory:** Financial Services, Manufacturing, Healthcare, Retail, Tech,
Energy, Food & Beverage, Chemicals, Federal Consulting. Enterprise
(1,000+ employees). Legal/Professional Services is flagged out-of-territory
- only work it via referral or multi-threading, and confirm with the assigned AE first.

**ICP fit signals** (from `zendesk_expertise_knowledge_base_v3.md` §11),
roughly in strength order:
- New CX/IT/HR/Ops leadership in the last 12 months (6-month evaluation window)
- Public AI / digital-transformation mandate (active budget + mandate)
- Legacy vendor in place (Avaya, NICE, Genesys, ServiceNow, Oracle Siebel) -
  contract-window / additive-entry angle
- High volume of CX/contact-center job postings (scaling friction)
- No chatbot or an outdated one (self-service/deflection gap)
- Public CX complaints or low CSAT (urgent, visible)
- Post-M&A, PE ownership transition, or platform-consolidation initiative
- Rapid headcount growth or a funding round

**Priority tiers for prospects within an account** (KB §9):
- **Tier 1** (economic buyers, primary outreach): CCO/CXO/CIO/CHRO, VP/SVP/EVP
  of CX/Support/Contact Center/IT/HR, VP of AI/Digital Transformation
- **Tier 2** (day-to-day owners, primary outreach): Director-level in the same
  functions
- **Tier 3** (multi-thread only, not primary): Senior Manager / Head of
  CX/IT/HR/Ops
- **Skip/flag:** Manager and below, titles outside CX/EX/IT/HR/AI/Ops/
  Procurement, or any title where the Zendesk angle is unclear (🔴 flag it)

**COLD vs WARM gate** - check every account against
`../00_My_Workspace/MY_ASSIGNMENTS.md` and the approved CRM source before
writing. Never default an unresolved account to cold. Confirm the motion with
the assigned AE when status is missing or ambiguous.

**Signal accuracy caveat:** Any inferred technology-use or customer-status
signal is a hypothesis, not proof of a live contract or account state. Verify
it against the approved CRM or an authoritative account source before treating
an account as warm or an existing customer.

---

## 2. Best Prompt Structures

Use declarative prompts with a clear goal, evidence boundary, and output
constraints. Do not make the repository depend on a particular AI tool,
prompt runner, or implementation script.

**Research prompt** (`build_intel_prompt`) - the pattern to reuse for any
account-intel call:
1. State the goal up front: arm a BDR with what a great human rep would dig
   up by hand. Explicitly say a lean summary is a failure - depth is the
   deliverable.
2. Check the approved account source first before running fresh research.
   Treat existing records as evidence to reconcile, not as automatically
   correct.
3. Then research with an explicit evidence and time budget using the approved
   research sources available in the current workflow.
4. Ask for a fixed, numbered list of fields, each requiring a real source
   URL: why-now triggers (3+), leadership quotes (verbatim, attributed,
   never paraphrased into a fake quote), org changes, initiatives, incumbent
   tech (cross-check any technology signal against an independent source),
   website CX inspection, recent news with real dates, and ICP/persona mapping with no
   artificial cap on how many profiles can match.
5. Set a reasonable research budget and output limit for the current
   workflow. Record the source coverage and material evidence gaps.

**Draft prompt** (`build_draft_prompt`) - the pattern for per-prospect
outreach generation:
1. Inject the full knowledge base as the standard the email must meet, but
   say explicitly: borrow a proof point/competitive line "only if it
   genuinely fits this account" - don't force-fit.
2. Inject only verified, structured research (`compact_context`) - the
   account facts plus that one prospect's own LinkedIn profile text. State
   the boundary explicitly: personalize only from what's in the research;
   never invent background.
3. Pass rep choices (tone, length, CTA type, humor, open-with, include-proof,
   personalize) as a single compact line, not free text - keeps the batch
   controllable and diffable.
4. Restate the hard rules inline even though they're in the KB (subject
   format, word cap, banned phrases, sign-off with first name only) - belt
   and suspenders, since the model handles the instruction better close to
   the generation call than several thousand tokens upstream in a big KB
   block.
5. End with "run the pre-send checklist mentally" and "remove the name - it
   should still only fit this person" as an explicit final self-check
   instruction, not just a rule stated once.
6. Force strict JSON output (`{"subjects": [...], "body": "..."}`) with "no
   fences, no prose" - makes parsing deterministic for a fan-out
   (`ThreadPoolExecutor`) across many prospects at once.

**General prompt lessons that generalize beyond this console:**
- State the failure mode explicitly ("a lean summary is a failure") rather
  than just asking for depth - this measurably kept research from
  regressing to one-sentence summaries.
- Order matters: check-existing-context → fresh research → structured
  output. Doing research before the vault check risks contradicting ground
  verified context already established.
- Rep-provided research (Sales Nav notes, pasted docs) should do double
  duty: personalize the current draft AND surface any named people in it as
  additive prospects (`repProvided: true`), sorted to the top with a visible
  badge - never silently replacing the model's own discovery.

---

## 3. Rules for Handling Accounts

**Gating and mode selection**
- Establish COLD vs WARM before writing anything (§1 above).
- Use a research mode before drafting and a separate approval step before any
  live send. Do not infer approval from an account record or a research result.
- Resolve missing or conflicting evidence using the approved sources available
  in the current workflow. Flag `UNVERIFIED` when the account state, trigger,
  incumbent, or prospect connection cannot be confirmed.

**Sourcing discipline**
- Every claim (trigger, pain, ICP signal, incumbent) needs a real source URL.
  Never attribute a tech stack to a specific contact without a verified
  source - if uncertain, omit rather than guess.
- Leadership quotes must be verbatim and attributed - never paraphrase into a
  fake quote.

**Cadence rule**
The four emails in the canonical drafting standard are the writing architecture, not a universal send schedule.

Use three to five email opportunities inside an adaptive, multichannel account motion. Choose LinkedIn, phone, referrals, or other approved channels based on account type, persona, trigger strength, engagement, reply behavior, and stop rules. Never add touches solely to complete a sequence.

The default cold motion may begin with:
1. Account-relevant LinkedIn or email touch
2. Email 1 - account hypothesis, product-neutral by default
3. A distinct LinkedIn or phone touch when justified
4. Email 2 - new operational implication or useful proof
5. Email 3 - Zendesk point of view when the hypothesis still holds
6. Email 4 - direct qualification when another touch is warranted

Email and LinkedIn content must differ - never paste one into the other.
Warm accounts require a separately approved re-engagement or expansion motion.
Do not import an older cadence automatically.

**Email 1 hard rules:** no meeting ask, no product dump, no unsupported claim,
100 words or fewer, a signal-based hook, and one reply-focused question.
Default to no vendor name or proof point. A controlled vendor-present test may
use one short capability or proof sentence when the canonical rules allow it.

**Emails 2-3:** pull proof points matched by pain first, then metric
strength, then industry - a stronger off-vertical metric beats a weak
same-vertical one. Treat proof timing as a testable hypothesis and track it.
Avoid reusing the same stat across multiple prospects at one company unless
the account strategy explicitly requires it.

**Objection handling:** validate the prospect's *specific stated fact*
verbatim before pivoting to the additive Zendesk-alongside-incumbent framing
- a generic "totally understand" reads as scripted.

**Hard stop rule:** if a prospect says outreach is too frequent, stop
immediately - no acknowledgment message, not even a short apology. Any
reply at all is itself an unwanted additional touch.

**Rejected patterns (tested against real threads, don't reintroduce without
new evidence):**
- "Asymmetric value asset" CTAs (2-minute personalized video, masterclass/
  event invite) - not actually personalized at BDR volume, and attending an
  event is more friction than replying, not less. Zero confirmed wins, one
  phishing-caution flag.
- Sub-100-word / one-sentence-per-line formatting - conflicts with the
  reconciled word-count rule and is a recognizable sequencer-template
  signature; the one thread that actually converted to a meeting used normal
  prose paragraphs.

**Banned globally, every phase:** em dashes, emojis, "boost/supercharge/
revolutionize/turbocharge/swiftly/leverage/optimize/streamline/synergy/
solution" or brochure-adjacent language, "I hope this finds you well," and
any follow-up-callback phrase ("following up on," "circling back," "reaching
out," "quick question," "just wanted to," "touching base," "per my last
email") - even in Email 2/3, which must open with a fresh angle, not a bump.

**Logging / feedback loop:** record send outcomes in the approved CRM or
account record. Record repository rule changes and their evidence in
`../05_Change_Log/CHANGELOG.md`. Measure outcomes rather than trusting a
subjective preference about what reads better.

**Known open gaps:** deliverability configuration, sender identity, voice
samples, account ownership, CRM status, and approved research sources must be
supplied by the operator or connected system before live work. This repository
does not assume access to a CRM, email sender, social network, or research
provider.

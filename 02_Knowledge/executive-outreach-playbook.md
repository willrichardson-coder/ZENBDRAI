# Executive Outreach Playbook - Enterprise SaaS BDR

*Built from a deep-research workflow (101 agents; 13 findings confirmed, 12 refuted under adversarial verification). Saved 2026-07-07.*

**Evidence footing:** Deliverability mechanics rest on a primary authority (Google's official sender guidelines, corroborated for Microsoft). Everything about copy, CTA, cadence, and personalization rests on vendor blogs or a single Gong study - treat as craft, not proven data. Do not repeat vendor benchmark numbers as fact.

**Repository rule:** This is supporting guidance, not a competing source of truth. The canonical writing architecture is four emails: account hypothesis, new operational implication or useful proof, Zendesk point of view, and direct qualification. The live cadence remains adaptive and multichannel, using three to five email opportunities when account context, engagement, reply behavior, and stop rules justify them.

---

## Verified findings (trust these)

**HIGH confidence - Google primary source:**
- SPF + DKIM + DMARC mandatory for senders of 5,000+/day to Gmail (since Feb 2024) and Microsoft consumer domains (since May 5, 2025). Minimum SPF *or* DKIM for all senders. Unauthenticated mail may be marked spam or rejected with a **5.7.26 error**.
- Spam-complaint rate: keep **below 0.10%**; **0.30% is a hard ceiling** that triggers filtering/rejection.
- Bounce rate: keep **under 2%**; over 5% is the danger zone.

**MEDIUM confidence:**
- First touch **under 150 words**, ≤1 link, no URL shorteners, no "free/guarantee/act now/limited time." (Reputation & complaints matter more than any single word.)
- Interest-based CTA beats both open-ended and specific-time meeting asks in COLD outreach (Gong, 304,174 emails).
- First message: **no meeting ask, don't sell in the message.**
- Real personalization = the recipient's actual pain, not name/company mail-merge.
- LinkedIn-first cadence: connection request → LinkedIn message ~day 3 after accept → email ~1 week later.

**REFUTED - do NOT cite as fact (vendor folklore):**
- Seniority-tailoring specifics; "C-suite 3× more responsive on LinkedIn"; "35–40% reply rates vs 10.3%"; "<400 chars = 22% higher response"; specific LinkedIn char counts (180–220 / <300); "61–65% of replies after msg 2–3, 50% quit after one"; "100% plain text mandatory"; specific-time CTA "doubling" bookings (15%→37% was a stage confound, not a CTA effect).

---

## 1) Decision map by title/seniority
*⚠️ No seniority claim survived verification - this is disciplined practitioner judgment. Verified anchor: personalize to pain, not title.*

- **CxO:** business outcome in their units (margin, risk, time-to-decision), one metric, 3–4 sentences. No feature talk, no demo ask.
- **CFO / risk:** cost avoided or risk quantified; name the specific exposure. No naked "ROI."
- **SVP/VP (functional owner - usually the economic buyer):** the outcome they're measured on this quarter; operational detail.
- **Director/GM (most likely to reply/champion):** concrete workflow problem + how peers solved it; offer something usable.
- **IT Security/Architecture:** control, integration, evidence (SSO, data residency, SOC 2). No "AI-powered," no urgency, no vague security adjectives - they filter hardest on hype.

## 2) AI-triage risk factors → countermeasures
- **Unauthenticated domain** → SPF+DKIM+DMARC (see HIGH above). Biggest hard failure.
- **Spam complaints** → below 0.10%, never 0.30%.
- **Bounces** → under 2%; verify lists.
- **Promo/urgency words** → cut them, but reputation matters more.
- **Links/format** → one link, no shorteners, plain or light HTML (100%-plain-text rule was refuted).
- **Length** → under 150 words first touch.
- **Detectable mail-merge** → no visible tokens, no "companies like yours."

## 3) Personalization system (signals → 1–2 lines max)
Collect per account (~5 min): leadership change → new exec's 90-day priority; hiring pattern → where they're investing/struggling (JDs name the pain); product launch → commitment they must operationalize; compliance trigger → obligation + deadline; tech-stack clue → tools in job posts/eng blog.
Translate as an *observation*, not a dossier. Never stack 4 scraped facts - that's what sounds like scraping. (The "combine 3 signals" and "individual ref beats role ref" formulas were refuted - don't over-engineer.)

## 4) Deliverability / formatting
- **Subject:** 2–5 words, sentence/lowercase, no punctuation stacking, no visible token, no "Re:" on first touch, no emoji.
- **Body:** short paragraphs, one idea, one link, one ask; write like a peer, no bullets/branding in cold first touch.
- **Personalization in the thinking, not visible {{fields}}.**
- **Length:** first touch <150 words; follow-ups 2–4 sentences; vary structure so filters can't fingerprint.

## 5) CTA strategy
- First touch: gauge interest or offer value - never a calendar ask.
- Don't sell in the message.
- Escalate to a specific time only after engagement (reply/click).
- (Permission/micro-commitment CTAs are sound but their *superiority* is unproven.)

## 6) Illustrative 10-business-day multi-channel cadence

This is an example motion, not a required schedule. The canonical repository rule is adaptive: use three to five email opportunities only when account context, engagement, reply behavior, and stop rules justify them. Where this playbook conflicts with a canonical rule, the canonical rule wins. For Zendesk cold email, the under-100-word Email 1 limit is tighter than this playbook's general under-150-word guidance.
- **Day 1:** LinkedIn connection request (short context note fine).
- **Day 3–4:** if accepted → LinkedIn message: signal observation + interest-based CTA.
- **Day 5:** Email 1.
- **Day 7:** LinkedIn engagement (comment on their post, not a DM).
- **Day 8:** Email 2 (new angle, not a "bump").
- **Day 10:** Email 4 when another email opportunity is justified (direct qualification or useful close).
- Email and LinkedIn carry *different* content - never paste the same message.

## 7) Pre-send checklist (run every send)
1. SPF/DKIM/DMARC pass? 2. Complaint rate <0.10%? 3. Bounce risk <2%? 4. Subject 2–5 words, no token/"Re:"? 5. Under 150 words? 6. One link, no shortener? 7. Zero trigger words? 8. No "reaching out"/"circling back"/"quick question"? 9. No transform/disrupt/AI-powered unless literally true + numbered? 10. Opener references a signal only this person recognizes? 11. No visible tokens/"companies like yours"? 12. Personalization 1–2 lines as observation? 13. Interest-based CTA, no calendar ask (first touch)? 14. One idea, one ask? 15. Tailored to likely priority? 16. LI and email content differ? 17. No emoji/fake urgency/false claims? 18. Reads hand-written, not templated? 19. Credibility claim real/verifiable? 20. Remove the name - does it still only fit this person?

---

## Sequences

### LinkedIn (executive)
**Connection request:** "[FirstName] - following [Company]'s [Signal]. Would value staying connected as you scale it."
**Msg 1 (post-accept):** "Thanks for connecting, [FirstName]. Noticed [Company] is [Signal] - in my experience that's usually when [Role]s start hitting [specific friction]. Curious whether that's on your radar yet, or still early?"
**Msg 2 (day 7):** [Substantive comment on their recent post. No pitch.]
**Msg 3 (final):** "No worries if the timing's off, [FirstName]. If it's useful, I put together a one-page teardown of how [comparable company] cut [Outcome] - want me to send it over?"

### Email (executive)
**Email 1 - Subject `[company] [signal topic]`:**
"[FirstName] - saw [Company] is [Signal]. When [Role]s take that on, the part that usually gets underestimated is [specific operational pain], not the [obvious part]. We work with [2 named peers] on exactly that. Worth me sharing how they handled it, or is this already solved on your end?"
**Email 2 - Subject `one number`:**
"[FirstName] - one data point in case it's useful: [peer] found [quantified outcome] within a quarter of fixing [pain]. Is reducing [pain] a priority this year, or not yet?"
**Email 3 - Subject `close the loop`:**
"[FirstName] - I'll assume the timing isn't right and stop here. If it's worth a look later, is it fair to check back in Q[X]?"

### Bad vs Safe
**❌ Bad:** Subject "Quick question" / "Hi [FirstName], I'm reaching out because we help companies like yours transform operations using our AI-powered platform. Quick question - are you open to a demo this week? 🚀"
*Risky: formulaic opener, hype ("transform"), buzzword ("AI-powered"), "companies like yours" mail-merge tell, first-touch demo ask, "quick question" subject, emoji.*
**✅ Safe:** Subject `austin ops hiring` / "[FirstName] - saw the three ops analyst roles you're hiring in Austin. Usually that means volume is scaling faster than the tooling can keep up, and reconciliation starts eating the team's week. Two logistics firms your size handled that without adding headcount. Worth me sharing what they did, or is this already handled?"
*Safer: plain subject, specific signal opener, concrete pain not "transform," no buzzwords, interest-based CTA, <80 words, no links/emoji.*

---

## Templates

**5 hook lines (concern → line → credibility method):**
1. Cost: "When [Company] [Signal], [pain] usually shows up as unbudgeted spend before anyone flags it." → cite same-size peer's dollar figure.
2. Risk/compliance: "With [regulation/deadline] landing, the operational lift usually lands on [Role], not legal." → name specific obligation + date.
3. Growth: "Scaling [initiative] tends to break [process] before it breaks headcount plans." → reference a peer who scaled through it.
4. Productivity: "Teams your size lose ~[X hrs/week] to [manual task] once volume crosses [threshold]." → quote peer's measured time saved.
5. Time-to-value: "The slow part isn't the decision - it's [integration/rollout step]." → state a peer's real go-live timeline.

**3 CTA variants:**
- Binary: "Is [pain] a priority this year, or not yet?"
- Micro-commitment: "Want the one-page teardown?"
- Permission: "Fair to send one example, or would you rather I not?"

---

## Next step (open thread)
Adapt the sequences to a specific product category or a named target account so signals/peer references are real, not placeholders.

**Research artifact:** `/private/tmp/claude-502/-Users-will-richardson/644abd9e-1278-47e0-9e55-13ac50b5bdc1/tasks/w7lc9yeon.output`

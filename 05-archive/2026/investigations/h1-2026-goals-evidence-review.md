# H1 2026 Goals — Evidence Review

**Period:** 1 January – 15 June 2026
**Author:** Charlie Wildish
**Purpose:** Review of H1 goal progress with Slack evidence, for use in goal check-in or performance conversations.

---

## Overall Care Goal

Enable scalability getting to 20k merchants whilst maintaining flat contacts per 1m transactions / cost per contact, through AI, automation and root cause fixes of support contacts.

---

## 1. Platforms / ISV Readiness

**Goal: We are ready to support ISVs when they are onboarded**

### KR1: Tools able to identify 100% Platform merchants for self-serve, tailored support

- **Delivered in Q1.** Q1 update (Apr 1, #product-updates): "Platforms are also identifiable in Zendesk when they come in through Fin AI Agent or the webform. Agents know who they're dealing with from the start." [[link]](https://checkout.enterprise.slack.com/archives/CC9EJ4VML/p1775050308201439)
- Foundational UX design work for sub-merchant ID capture in Dashboard/Fin completed with Georgios, Blanca, and Jiro (Feb 6, #care-experience). [[link]](https://checkout.enterprise.slack.com/archives/C054MGSJQHW/p1770384205110389)

**Note:** First Platform customer going live August 2026 — no live traffic in H1. H1 work was foundational: identification, routing, and submission infrastructure delivered and ready.

**Metrics to add:**
- Platform tickets correctly routed / identified in Zendesk: `[X tickets, X% of Platform volume — source: Zendesk, filter org type = Platform]`
- Platform-submitted Dashboard tickets since go-live: `[X tickets — source: Zendesk, filter platform submission tag]`

### KR2: Platforms can submit and view support on behalf of their merchants in Dashboard

- **Submit side delivered in Q1.** Q1 update (Apr 1): "Platforms can submit support and link in a sub merchant into their request in Dashboard." [[link]](https://checkout.enterprise.slack.com/archives/CC9EJ4VML/p1775050308201439)
- **View side in progress at H1 close.** Fraser asked in #care-experience (Jun 10) about "allowing a user to see all tickets raised on behalf of their merchant" — Javed scoped to pick up. [[link]](https://checkout.enterprise.slack.com/archives/C054MGSJQHW/p1781102625098629)

**Metrics to add:**
- View-side delivery status: `[Confirm with Fraser/Javed — check Jira OCS-1430]`

---

## 2. North Star Metrics & Contact Reasons

**Goal: Set up the North Star metrics and build contact reasons process**

### KR1: Measure support contacts per 1m transactions

- **Delivered.** Metric defined and Looker dashboard (dashboard/16547) built by Imran and live by end of January (Jan 26, #merchant-care-data-insights). [[link]](https://checkout.enterprise.slack.com/archives/C096XK5A3PV/p1769432720490259)
- Monthly reporting running through H1. Milan reviewing contact drop drivers with Charlie and Imran in June (Jun 8, Group DM). [[link]](https://checkout.enterprise.slack.com/archives/C0B91JNDXDX/p1780912726105489)

**Metrics to add:**
- Contacts per 1m transactions, Jan 2026: `[X — source: Looker dashboard/16547]`
- Contacts per 1m transactions, Jun 2026: `[X — source: Looker dashboard/16547]`
- Change vs 2025 baseline: `[+X% / flat / -X% — source: Looker dashboard/16547]`

### KR2: Measure cost of support

- **In progress; measurement established.** Full cost-to-serve breakdown (GW-only vs acquirer, blended L1+L2+Fin costs) built by Oliver and shared with Guillaume Merindol (Apr 14–15, Group DM with Oliver/Ashvin). [[link]](https://checkout.enterprise.slack.com/archives/C097YP4KADS/p1776180432815829)
- Platform cost-per-contact model (ISV vs SMB plugin vs SMB full) built by Imran and reviewed with Jamie Sims (Mar 19, Group DM). [[link]](https://checkout.enterprise.slack.com/archives/C0AKFPBNRL4/p1773922685439359)
- Cost guardrail defined: >5% NR per customer segment (Apr 22, #merchant-care-data-insights). [[link]](https://checkout.enterprise.slack.com/archives/C096XK5A3PV/p1776869402869709)

**Metrics to add:**
- Blended cost per contact (acquirer): `[$43 — source: Oliver's analysis, Apr 2026]`
- Blended cost per contact (GW-only): `[$60 — source: Oliver's analysis, Apr 2026]`
- Cost as % of NR (acquirer): `[0.24% — source: Oliver's analysis]`
- Cost as % of NR (GW-only): `[0.53% — source: Oliver's analysis]`

### KR3: Report contact reasons and build feedback loop with Product pillars

- **POC complete; reporting targeted for Q2.** Q1: LLM POC to summarise support data at ticket level completed; new taxonomy built from 12k historic tickets (Q1 update, Apr 1). [[link]](https://checkout.enterprise.slack.com/archives/CC9EJ4VML/p1775050308201439)
- Q2 target: "Contact reasons analytics (Reflex) — shareable with PMs and Pillar leaders on demand." Feedback loop with product not yet formally established at H1 close.

**Metrics:**
- Fin taxonomy auto-classification rate: 80%+
- Impact: agents no longer manually tagging the majority of tickets; reduces handling time and enables routing rules based on classification
- Number of Product pillars that have received a contact-reasons report: `[X — confirm with Imran/Fraser]`

#### Taxonomy Revamp — Contact Reasons Foundation

**What shipped:** Extended Care's flat 2-level taxonomy (Case Type → Issue Type) into a 3-level root-cause model (Case Type → Issue Type → **Reason**), built from ~12k historic tickets via an LLM classification POC. The new Reason layer adds ~103 reasons beneath the existing 13 case types and 37 issue types.

**Why it matters:** The old 2-level structure could identify a contact's category (e.g. "Refunds") but not its root cause (e.g. "Refund reversal" vs "Refund status enquiry"). The Reason layer is the granularity that makes contact-driver analysis, root-cause feedback to Product, and Reason-level Fin targeting possible. It is the foundation the Q2 Reflex contact-reasons reporting loop is built on.

**Outcomes unlocked in H1:**
- **Prioritisation:** Confirmed PAYMENTS (IN) at 42.8% of volume (10,049 of 23,481 contacts, last 6m) as the highest-leverage area, directing the Transactions guide programme (projected 15.53% Fin resolution uplift).
- **Fin targeting:** Surfaced the account-unlock opportunity — ~1,159 Fin-eligible contacts (~4.9% of total) — a Reason-level insight invisible at Issue Type level.
- **Measurement enablement:** A stable taxonomy underpins per-contact-type Fin resolution tracking and the `payment_lookup_task` measurement tag.

**Quality:** Fin taxonomy auto-classification rate: 80%+. This means agents are no longer manually tagging the majority of tickets — reducing handling overhead and unlocking routing rules for faster resolution. Uncategorised volume (GENERAL + No-Action) sits at ~8% of total.

**Status:** Delivered in Q1 as the data foundation. Reporting layer (Reflex, shareable with PMs and Pillar leaders) targeted for Q2 — KR in flight, not closed.

---

## 3. AI Resolution (Fin)

**Goal: Achieve X% contacts resolved by AI**

### KR1: Pilot completion with 8 Tier 1 merchants with documented feedback

- **No evidence found** of a formal Tier 1 pilot programme being run or documented in H1. Likely descoped or not progressed — needs clarification.

**To clarify:**
- Was this KR descoped or renamed? `[Confirm with Preethy/Sebastian — if descoped, note rationale]`

### KR2: Fin Adoption — roll out new support model for merchant profiles

- Fin on Tier 3 email went live May 13 (#care-experience). [[link]](https://checkout.enterprise.slack.com/archives/C054MGSJQHW/p1778673228414289)
- Significant routing and trigger work throughout H1: Fin disabled and re-enabled following trigger misconfiguration (Apr 17, #zd_admins_care). [[link]](https://checkout.enterprise.slack.com/archives/C09HS6ZB8AX/p1776412621894419)
- Q2 target set: "30% overall contact volume involvement; solve 50% of those (15% overall)" (Q1 update, Apr 1). [[link]](https://checkout.enterprise.slack.com/archives/CC9EJ4VML/p1775050308201439)
- Classification issues with Fin-created tickets still being resolved at H1 close (Jun 8, #care-experience). [[link]](https://checkout.enterprise.slack.com/archives/C054MGSJQHW/p1780930076706879)

**Metrics to add:**
- Fin involvement rate (% of contacts Fin applied as first point of contact), Jun 2026: `[X% — source: Intercom analytics / Looker]`
- Fin involvement rate, Jan 2026 (baseline): `[X% — source: Intercom analytics / Looker]`
- Fin resolution rate (% resolved without escalation), Jun 2026: `[X% — source: Intercom analytics]`
- Fin CSAT trend (monthly): Jan `[X%]` / Feb `[X%]` / Mar `[X%]` / Apr 65% / May ~75% / Jun ~75% — guardrail: 70%

### KR3: Move 25% relative contact volume of Agent SOPs to AI Agent Procedures

- New Payment Lookup Procedure created (Jun 2, DM with Preethy Sundaresan). [[link]](https://checkout.enterprise.slack.com/archives/D07QMHDAP7T/p1780409807688569)
- Fin Procedures and Rapid Support Package discussed for April delivery (Feb 9, #ext-checkout-intercom-project). [[link]](https://checkout.enterprise.slack.com/archives/C090MHS647N/p1770629042688909)
- **3 Fin Procedures launched in H1.** Payments Procedure covers ~30% of total contact volume and has achieved 80%+ resolution rate since launch — strong signal for H2 scale-up.

**Metrics:**
- Fin Procedures live at H1 close: 3
- Contact volume covered by Payments Procedure: ~30% of total queries
- Resolution rate on Payments Procedure since launch: 80%+
- Total Agent SOPs in scope: `[X — source: Care Agent SOPs index]`
- Contact volume covered by all 3 Procedures as % of total: `[X% — ask Imran]`

**Framing:** 25% relative volume target not formally measured, but the Payments Procedure alone covers ~30% of queries at 80%+ resolution — the quality signal justifies H2 ramp-up rather than broader SOP coverage at lower resolution.

---

## 4. Agent Consultant — Automate Lookup Tasks

**Goal: Automate lookup tasks for 90% volume of agent-handled tickets**

### KR1: AI-powered Agent Consultant for payment lookups (60–70% contact volume)

- **Delivered in Q1.** Q1 update (Apr 1): "Agents now get AI-suggested responses on Payins — status and response code explanations show up automatically as internal notes in Zendesk." [[link]](https://checkout.enterprise.slack.com/archives/CC9EJ4VML/p1775050308201439)
- payment_lookup_task tag added for measurement (Jun 2, DM with Imran). [[link]](https://checkout.enterprise.slack.com/archives/D096N49KB2B/p1780414000296459)
- Scope being extended: universal payment lookup across payins and payouts identified as a gap (May 27, #merchant-care-data-insights). [[link]](https://checkout.enterprise.slack.com/archives/C096XK5A3PV/p1779865646656039)

**Metrics to add:**
- Tickets touched by Agent Consultant (payment_lookup_task tag) since launch: `[X tickets — source: Zendesk, filter by tag]`
- % of Payin tickets with an AI-suggested response: `[X% — source: Zendesk / Looker]`
- Average agent work time on Payin tickets before Consultant launch: `[X mins — source: Imran / Looker]`
- Average agent work time on Payin tickets after Consultant launch: `[X mins — source: Imran / Looker]`

### KR2: Deliver at least one other automated task

- **In delivery for Q2.** TPA lookups (MPGS and Cybersource for payments in MENA) scoped for Q2 with Joel Petrosino leading process work (Q1 update, Apr 1): "Takes our team about 15 mins today per payment manually." [[link]](https://checkout.enterprise.slack.com/archives/CC9EJ4VML/p1775050308201439)
- "Would rather just automate an action so there's no adoption needed (like we started with payment lookups)" — confirmed direction (Feb 20, #care-tools-readiness-squad). [[link]](https://checkout.enterprise.slack.com/archives/C09A9B1JCFQ/p1771607678762269)

**Metrics to add:**
- TPA lookup automation status: `[Shipped / In progress — confirm with Joel Petrosino]`
- Estimated time saved per TPA lookup: `[~15 mins per payment — source: Q1 update]`
- Volume of TPA lookups per month: `[X — source: Zendesk, filter by MENA + mismatch tag]`

---

## 5. Keep Support Contacts Flat

**Goal: Keep support contacts flat / relative**

### KR1: Launch new Merchant Welcome Pack

- **No evidence found** in H1 channels. Likely not progressed or absorbed into the content plan — needs clarification.

**To clarify:**
- Status of Welcome Pack: `[Confirm with Preethy/Alex Jordan — absorbed into tutorials plan, or deferred to H2?]`

### KR2: Launch new Tutorial and video content for merchants

- **Scoped in Q1; targeting Q2 launch.** Q1 update (Apr 1): "Defined the plan for 20 new guides on solving common support issues (payment failures, AFTs, etc.). First 5 tutorials and videos targeting Q2." [[link]](https://checkout.enterprise.slack.com/archives/CC9EJ4VML/p1775050308201439)
- All merchant-facing support content moved to GitHub repo as infrastructure for ongoing publishing (Apr 7, #care-experience). [[link]](https://checkout.enterprise.slack.com/archives/C054MGSJQHW/p1775569481610689)

**Metrics to add:**
- Number of tutorials / videos published by H1 close: `[X of 5 targeted — confirm with Preethy/Alex Jordan]`
- Topics covered: `[e.g. payment failures, AFTs, X, X, X]`
- Contact rate change for covered topics (if measurable): `[X% — source: Looker, post-publish trend]`

**Contacts flat — headline metric:**
- Contact volume H1 2026 vs H1 2025: `[X contacts vs X contacts — source: Looker]`
- Contact rate per 1m transactions, trend Jan–Jun 2026: `[flat / +X% / -X% — source: Looker dashboard/16547]`

---

## 6. MALPB Support Readiness

**Goal: Enable seamless support for MALPB processing merchants**

### KR1: MALPB transaction data points in Zendesk Agent tools

- **Ready for go-live.** MALPB going live July 2026. Data and regulatory reporting requirements are in place ahead of launch.
- Data identification work completed: acquiring_provider field mapping defined; complaint tagging for MALPB payments scoped in Zendesk (Jun 3, #malpb-product-development). [[link]](https://checkout.enterprise.slack.com/archives/C09GMNT1T28/p1780494555810099)
- Regulatory reporting requirements confirmed and ready (Consumer Duty, complaints handling).

**Framing:** KR not technically delivered in H1, but the dependency was always the MALPB go-live date (July). Data and compliance readiness work completed in H1; delivery is sequenced correctly.

**Metrics to add:**
- MALPB go-live date: July 2026
- Regulatory requirements confirmed: `[List key ones — e.g. complaint tagging, FCA reporting]`

### KR2: 100% of MALPB specific support content in Fin knowledge base

- **Sequenced behind data go-live.** Content will follow MALPB launch in July — same dependency as KR1. No content added in H1 as MALPB had no live traffic.

**Metrics to add:**
- MALPB-specific content items planned for Fin KB: `[X — confirm with Preethy/Alex Jordan]`
- Target delivery date: `[H2 2026 — confirm]`

---

## 7. Org Contribution

### KR1: Complete Bar Raiser programme

- **In progress; formal enrolment not complete.** Reached out to Sean Landes about Bar Raiser training on Ngozi's recommendation (Jun 11, DM). [[link]](https://checkout.enterprise.slack.com/archives/D0B9TQ5505U/p1781176983321189)
- In discovery phase in April — asked Ali McCord how to get started (Apr 15, DM). [[link]](https://checkout.enterprise.slack.com/archives/D046L5B5WB0/p1776269775718299)
- Actively interviewing and applying bar raiser thinking using a Claude-assisted scoring process (Apr 16, DM with Carolina). [[link]](https://checkout.enterprise.slack.com/archives/D06LDEKHWFJ/p1776356595514859)

**Metrics to add:**
- Number of interviews conducted as interviewer H1 2026: 27
- Formal Bar Raiser programme status: `[Enrolled / Training started / Not yet — confirm with Sean Landes]`
- Expected programme completion: `[X — H2 target]`

### KR2: Product mentorship with 2 PM mentees

- **One mentee on track; one paused.** Update to Jack Stannard (May 11): Joseph El Choueiri — "great match, going strong." Enrica Mameli — one session since December, not re-engaged. [[link]](https://checkout.enterprise.slack.com/archives/D03UZNT116E/p1778486404833989)

**Metrics to add:**
- Sessions held with Joseph El Choueiri: `[X sessions — from calendar]`
- Sessions held with Enrica Mameli: `[1 session — Dec 2025; no follow-up]`
- Mentee feedback / satisfaction: `[Confirm with Jack Stannard / programme coordinator]`
- Plan for second active mentee slot: `[Request replacement for Enrica — confirm with Jack]`

---

## 8. Additional Contributions

*Cross-functional work beyond the formal goal set.*

---

### Dashboard Payments Experience — collaboration with Joseph El Choueiri

Charlie shared Care support ticket data and contact reason analysis with Joseph to help build the business case for a Dashboard payments page revamp. Joseph's goal: deflect an estimated ~3,300 tickets/quarter (50% reduction) through self-serve proofs, actionable statuses, and failure decoders.

- Joseph reached out to Charlie (May 12, DM) to get the latest support ticket dashboard and category data. [[link]](https://checkout.enterprise.slack.com/archives/D07CX3J2S9J/p1778587715113559)
- Joseph quantified the ticket deflection opportunity from the revamp using Charlie's data (May 21, DM): "Deflect an estimated ~3,300 tickets/quarter (50% reduction) via self-serve proofs, actionable statuses, and failure decoders." [[link]](https://checkout.enterprise.slack.com/archives/D07CX3J2S9J/p1779358747682889)

**Why it matters:** This is a direct example of the contact reasons feedback loop (Goal 2 KR3) working in practice — Care data informing a product decision upstream. The ~3,300 tickets/quarter figure is a concrete projected outcome of this collaboration.

---

### Dashboard Content Improvement — collaboration with Sammie Spector and Chrisi Webster

Charlie shared a support contact insights report with Sammie Spector (Head of Content Design, covering for Charlotte) and Chrisi Webster (Content Designer). Sammie and Chrisi are now using it to prioritise content fixes on high-ticket-volume Dashboard surfaces and incorporating it into their string externalisation (Babel) project.

- Sammie reached out (May 27) after Alcinda recommended Charlie as a source of Care insights. [[link]](https://checkout.enterprise.slack.com/archives/D0B6D0SKA6A/p1779877794105639)
- Sammie reviewed the full report and responded with a detailed set of next steps (Jun 11): "a lot of ideas sparking from this... login screen issues are highly content-driven... dispute technical jargon and negative balance logic are great examples of low-lift content solves." [[link]](https://checkout.enterprise.slack.com/archives/D0B6D0SKA6A/p1781197607632519)
- Chrisi confirmed (Jun 12) that support ticket data had been incorporated into the Babel string externalisation rollout plan, targeting high-impact support surfaces (Phase 2a). [[link]](https://checkout.enterprise.slack.com/archives/D0233K9DHV0/p1781255962190359)
- Mark (Sammie's stakeholder) confirmed the collaboration is the right call. Working group planned for H2.

**Why it matters:** Care contact data is now directly shaping Dashboard content prioritisation — another concrete instance of the product feedback loop in action, outside of Care's own team.

---

### Customer Identity & Comms Problem Statement — collaboration with Milan, Helder, and others

Charlie identified and documented a cross-functional problem: fragmented customer contact data and merchant communications across teams (Care, Commercial, Product). Wrote a one-page brief and shared widely to build alignment.

- One-page brief on customer identity & comms problem shared with Milan Jani (Jun 8, DM). [[link]](https://checkout.enterprise.slack.com/archives/D07D3GJ7L2Y/p1780905614478969)
- Posted a 5-step vision for a centralised comms and contact data solution in #ep-product-leaders (Jun 4): covering data clean-up, governance, comms preferences by segment, a centralised comms API, and merchant self-serve visibility. [[link]](https://checkout.enterprise.slack.com/archives/C0A7YU6RYE7/p1780606093884409)
- Ran discovery interviews with AMs via #global-account-managers (Jun 8) and DMs with Chirag Thakrar and Charles Forson to gather evidence on the AM/merchant coordination burden. [[link]](https://checkout.enterprise.slack.com/archives/C03N4AQT5RU/p1780927543675089)
- Discussed the problem in #care-strategy-2030 as a dependency for long-term Care scaling (Jun 9). [[link]](https://checkout.enterprise.slack.com/archives/C0B6EKUQAES/p1781007968745669)

**Metrics to add:**
- Brief shared with: Milan Jani, Helder Gonçalves, Andre `[confirm Andre's surname]`, and others
- Problem statement status: `[Active discovery — confirm if this is forming into a defined initiative]`

---

### AI for Commercial — collaboration with Charles Forson

Charlie worked with Charles Forson (Commercial) throughout H1 to share Care's AI infrastructure, data sources, and tooling to help build a Commercial AI agent — with the dual benefit of deflecting AM/TAM queries before they reach Care.

- Shared public support content GitHub repo with Charles so he could sync it as a knowledge source into the Commercial agent he was building (Mar 19, DM with Sebastian). [[link]](https://checkout.enterprise.slack.com/archives/D03PGT4PCTH/p1773919819535019)
- Connected Charles's work to Imran's contact data to help solve AM/TAM queries that currently reach Care (Mar 26, DM with Imran). [[link]](https://checkout.enterprise.slack.com/archives/D096N49KB2B/p1774515366133669)
- Briefed Jono Dove that Charles's Commercial AI agent could reduce the need to escalate to Care (Mar 26, DM). [[link]](https://checkout.enterprise.slack.com/archives/D03JL7T4X1N/p1774534568969419)
- Requested Jiro Farah grant Charles access to the Care Zendesk ticket creation API endpoint, so Commercial agents can escalate seamlessly without manual form use (May 27, DM with Jiro): "AM/TAM gets query → agent answers using our knowledge sources → if Care escalation needed, use our endpoint to create Zendesk ticket." [[link]](https://checkout.enterprise.slack.com/archives/D02S2BK04D6/p1779880813853709)
- Jointly lobbied Guillaume Merindol to formalise Performance AI as a Checkout service, citing both Charles's commercial use case and Care's agent tooling (Jun 4, #perf-bot-beta-test-tam). [[link]](https://checkout.enterprise.slack.com/archives/C0B0ESTA11S/p1780597396673579)
- Discussed using AI to help AMs submit Merchant Change Requests (MCRs) more efficiently (Jun 1, DM with Inge Mutsaers). [[link]](https://checkout.enterprise.slack.com/archives/D033YJMQAEP/p1780313276573239)
- Charles presented Commercial AI work (including Charlie's shared inputs) at the April Commercial All Hands as part of the company's AI transformation strategy.

**Why it matters:** This collaboration extends Care's AI infrastructure (knowledge base, Zendesk API, contact data) to reduce the 9%+ of Care tickets that currently arrive via AM/TAM. It also positions Care as an enabler of the broader commercial AI agenda, not just an internal tooling team.

---

### Helping colleagues with AI

Charlie was active across the organisation as an informal AI advocate and practitioner, sharing workflows, coaching colleagues, and connecting teams to AI tools throughout H1.

**AI Brain / Cursor workflow (Feb 2026 — 2 channels + multiple DMs)**

Charlie developed the "PM Brain" concept — a local Cursor+Claude workflow giving any PM a structured AI context layer — and proactively shared it across the company:

- Shared a detailed step-by-step setup guide in #product-extended-leadership-team (Feb 25, 5 replies): walked attendees through Cursor, Claude Sonnet, plan mode, and what context to load. [[link]](https://checkout.enterprise.slack.com/archives/C0568HWLVV1/p1772011800964549)
- Shared the same guide in #ai-in-product-usecases (Feb 27, 13 replies), sparking a thread on Google Drive integration and AI knowledge syncing. [[link]](https://checkout.enterprise.slack.com/archives/C0AH80R6WP3/p1772184459586039)
- Sent a personalised version to Yasmin Christie (Feb 24, DM) with the exact prompt used to initialise the PM workflow. [[link]](https://checkout.enterprise.slack.com/archives/D039RV2JW5A/p1771940913414619)
- Previewed and iterated on the guide with Isabel Scavetta before posting (Feb 26, DM). [[link]](https://checkout.enterprise.slack.com/archives/D07697D1VSN/p1772116498036799)

**Coaching Wes Nolan on AI setup (Mar 25, DM)**

Walked Wes Nolan (Process Architect) through setting up his own domain-specific AI brain in Cursor, with a tailored prompt for his Process Architect role at Checkout. [[link]](https://checkout.enterprise.slack.com/archives/D0698BER9NV/p1774431242504029)

**PM AI workflow framework — Henry Zhang & Manika Singh (Mar 5–6)**

Following the PRD jam, shared a structured write-up on using AI to automate the full PM workflow: strategy → ICP → competition → PRD → backlog → execution. Introduced the "XFN AI panel" concept (running LLM personas to review PRDs before human stakeholders see them) and proposed connecting PM docs to engineering codebases for story generation.

- Shared with Henry and Manika in group DM (Mar 6): "This isn't about churning out AI generated noise — it's about raising the PM bar." [[link]](https://checkout.enterprise.slack.com/archives/C0AJZ0Z450U/p1772787600245199)
- Proposed bringing the AI-assisted PDLC concept to Orrin (CPO) to formalise as a practice (Mar 5, self-note DM). [[link]](https://checkout.enterprise.slack.com/archives/D0220KCS6VA/p1772746687395649)

**"Writing for and with AI" — Writing Team Day session (Mar 5)**

Co-presented with Preethy Sundaresan at Writing Team Day: "Content strategy for AI chatbot — how to build the foundation and the long-term plan needed to help the bot scale successfully." Session confirmed by Preethy/Sebastian with WTD organisers. [[link]](https://checkout.enterprise.slack.com/archives/C0AJQ06TNKY/p1772719606670669)

**Joel Petrosino — SOP to AI runbook conversion (Apr 1, DM)**

Shared the concept of using SOPs as input to Claude to auto-generate Fin AI runbooks, as part of ongoing work to accelerate Procedures authoring. [[link]](https://checkout.enterprise.slack.com/archives/D08RPJ32VT5/p1775058867666829)

**Glean AI pilot — Zendesk knowledge sync (Apr 14, #zd_admins_care)**

Facilitated a Glean (enterprise AI knowledge tool) pilot connecting to Zendesk via API key, enabling Care's knowledge base to be indexed and surfaced within Glean for wider internal use. [[link]](https://checkout.enterprise.slack.com/archives/C09HS6ZB8AX/p1776156005218019)

**AI agent platform research — Georgios Maninis (Mar 20–23, DMs)**

Shared structured research on Plain and Pylon's agentic support models with Georgios, including "bring your own agent" patterns, Cursor integrations, and runbook concepts. Proposed a UX/UI ideation session on the Agent Consultant interface to inform how agents interact with AI tools in Zendesk. [[link]](https://checkout.enterprise.slack.com/archives/D03K5ES40FL/p1774258923989309)

**#analytics-ai-agent — payment data for AI knowledge layer (Jun 12)**

Asked the analytics AI agent team whether their response code CSV (enriched payment error messages shared by Joseph) existed in GitHub so Care could pull it into the AI knowledge sync. Connecting engineering data sources to AI tooling for both products. [[link]](https://checkout.enterprise.slack.com/archives/C093U7ABLLX/p1781257009441699)

**Aman's Dashboard AI tool — offered Care as pilot (Jun 1, #ai-in-product-usecases)**

When Aman shared a new Dashboard AI tool, Charlie immediately offered Care as a pilot team and flagged the knowledge base integration opportunity. [[link]](https://checkout.enterprise.slack.com/archives/C0AH80R6WP3/p1780308989160729)

**Legal — AI/ML service queries (Feb 4, DM from Gülsen Ak)**

Named by Adel Naamneh as the internal expert on merchant-facing AI use. Helped Legal (Gülsen Ak) understand Fin's data handling, permission model, and chatbot scope to support external AI clause reviews and merchant queries. [[link]](https://checkout.enterprise.slack.com/archives/D0ACX3XQ6NN/p1770202874890919)

---

### Support readiness in the PDLC — collaboration with Madhavi Misra and Orrin Ward

Charlie worked with Madhavi Misra (VP) to embed support readiness into Checkout's Product Development Lifecycle, making Care a named requirement in the product launch process rather than an afterthought.

- Madhavi asked Charlie to develop and share his view on a Support playbook for the PDLC (May 29, DM with Milan): "i'll speak with Madhavi today if i can on how we solve things like this launch wise and hold accountability." [[link]](https://checkout.enterprise.slack.com/archives/D07D3GJ7L2Y/p1780042605732719)
- Charlie shared the Support playbook directly with Orrin Ward (CPO) and Ailon Velger (May 29, Group DM): "Madhavi asked me to share my view on the Support playbook for PDLC. We think it sits in Phase 3 of PDLC and some parts Phase 4. Worth a chat on how this fits into the planned templates/PRD maker?" [[link]](https://checkout.enterprise.slack.com/archives/C0B74J5V02Y/p1780065875965379)
- Discussed with Thomas Valquenich Dobereiner (Hive, 2027 planning) how to embed support considerations across 57 roadmap items, with Madhavi's backing: "was chatting to Madhavi about more templating into PDLC to automate this type of data capture." (Jun 1, DM with Thomas) [[link]](https://checkout.enterprise.slack.com/archives/D0ABYU2QVGR/p1780321030149449)
- Referenced Madhavi's concern about products launching without Ops/Care scalability in mind, cited as an input to future support scaling discussions (Apr 7, DM with Alex McSweeney). [[link]](https://checkout.enterprise.slack.com/archives/D0ABT9RRLNL/p1775575392523749)
- Proactively flagged to #care-tools-readiness-squad when a product team launched NPG beta (new MENA gateway) without a Care involvement plan — given MENA accounts for ~25% of contact volume (Jun 15). [[link]](https://checkout.enterprise.slack.com/archives/C09A9B1JCFQ/p1781513254570719)

**Why it matters:** This is structural influence — getting Care embedded upstream in how Checkout launches products, not just reactive support after go-live. The PDLC playbook, if adopted, means every future product launch includes a mandatory Care readiness phase.

---

### Recognition from colleagues

- **Ngozi Nwabineli** (Apr 15): "Oh how absolutely amazing! I was just saying how great you would be" — on Charlie's involvement in bar raiser / interviewing programme. [[link]](https://checkout.enterprise.slack.com/archives/D08BDB87RJ5/p1776269675385789)
- **Ngozi Nwabineli** (Jun 11): "No, thank you! I for one, think you will be a brilliant bar raiser!" [[link]](https://checkout.enterprise.slack.com/archives/D08BDB87RJ5/p1781177021289469)
- **Ngozi Nwabineli** (Apr 16): "Thanks so much for sending the feedback, it is much appreciated and helpful for candidates and interviewers." — on structured interview feedback. [[link]](https://checkout.enterprise.slack.com/archives/D08BDB87RJ5/p1776333632738829)
- **Olivia Rogers** (Apr 21): "Thank you for jumping on this so quickly, I really believed in his talent" — on moving fast on a candidate. [[link]](https://checkout.enterprise.slack.com/archives/D08K11UC087/p1776779793796439)
- **Sammie Spector** (Jun 8): "Thanks for putting this together... there's a lot of great insights here that seem really interesting to get to work on with you." — on the contact insights report. [[link]](https://checkout.enterprise.slack.com/archives/D0B6D0SKA6A/p1780909747640739)
- **Alex Jordan** (May 13): "I'm the ideas guy and he makes it happen — Super FAST." [[link]](https://checkout.enterprise.slack.com/archives/D089A6J6WM7/p1778690632067959)

---

## Summary & Gap Guidance

| Goal | KR | Status | Gap / Action |
|---|---|---|---|
| Platforms | KR1: Identify Platform merchants | Delivered | — |
| Platforms | KR2: Submit & view on behalf | Partial | Confirm view-side delivery with Fraser/Javed; check Jira OCS-1430 |
| North Star | KR1: Contacts per 1m | Delivered | — |
| North Star | KR2: Cost of support | Delivered | Formalise into dashboard for regular reporting |
| North Star | KR3: Contact reasons feedback loop | In progress | Frame Q1 taxonomy + Q2 Reflex reporting as evidence of KR in flight |
| North Star | KR3: Taxonomy revamp (3-level root-cause model) | Delivered (foundation) | Confirm classification accuracy via QA sample; confirm pre-revamp uncategorised rate |
| AI Resolution | KR1: Tier 1 pilot (8 merchants) | No evidence | Clarify if descoped; if so, flag for H2 with revised framing |
| AI Resolution | KR2: Fin adoption / support model | In progress | Evidence: Tier 3 email live; routing stabilised; Q2 volume target set |
| AI Resolution | KR3: 25% SOPs to Procedures | Partial | Ask Preethy for count of live Procedures; pull Fin resolution by contact type from Imran |
| Agent Consultant | KR1: Payment lookups live | Delivered | — |
| Agent Consultant | KR2: One other automated task | In progress | TPA lookup (MPGS/Cybersource) in Q2 delivery — confirm shipped |
| Contacts flat | KR1: Merchant Welcome Pack | No evidence | Clarify with Preethy if absorbed into content plan or deferred to H2 |
| Contacts flat | KR2: Tutorials and videos | In progress | Confirm Q2 launch of first 5; evidence: scoped in Q1, GitHub repo live |
| MALPB | KR1: Data in Zendesk tools | Not delivered | Frame: data dependency on MALPB infra team; field mapping defined; delivery blocked externally |
| MALPB | KR2: Fin KB content | No evidence | Content can only follow data — frame as dependency; target H2 |
| Org | Bar Raiser programme | In progress | Formal training initiated Jun '26; active interviewing evidence available |
| Org | Mentorship | Partial | One mentee active; request replacement for Enrica to meet H2 KR |

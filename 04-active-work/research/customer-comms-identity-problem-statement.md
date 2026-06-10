# Customer Communications & Identity — Problem Statement

## The problem

Checkout lacks a unified customer identity and communications layer. Customer contacts, email addresses, roles, and organisations are stored across six systems — Salesforce, Zendesk, OKTA, Genesis, Pardot, and Citadel — with no single view linking them. Communications are sent by Care, Disputes, Fraud, Compliance, and Underwriting independently, with no shared log and no structured handoff between teams.

This creates two connected failures.

**For customers**: Merchants have no central way to track what Checkout has communicated to them or which team is handling their issue. When a query moves between teams, they re-explain from scratch.

**For internal teams**: Agents cannot see what other teams have told a customer. Queries transfer via inbox-to-inbox email forward, losing context at every handoff. There is no audit trail across the full customer relationship.

## Why this is urgent

These failures are manageable today in B2B Enterprise because account managers compensate manually. Three changes in 2027 remove that compensation entirely.

**B2C consumer launch under FCA regulation.** Consumer Duty requires evidencing fair customer outcomes through a complete, auditable comms record. FCA DISP complaints handling requires full cross-team comms history. UK GDPR right to erasure requires knowing where every communication is stored. Vulnerable customer flags must propagate across every team a customer interacts with. These obligations apply from day one of launch — not after a stabilisation period.

**SMB expansion.** No account managers exist to absorb manual coordination at SMB volume. Cross-team handoffs at scale cannot be staffed without structured routing. Comms targeting the wrong contact is a churn risk, not a recoverable escalation.

**Platform/ISV model.** The ISV contact hierarchy — ISV entity and Platform merchants — requires routing logic that does not exist today. A dispute notification or compliance notice sent to the wrong tier causes operational failure.

## Root causes

Two underlying infrastructure gaps drive all symptoms.

- **No unified identity layer**: Checkout cannot reliably link a person to their organisation, roles, and communications across systems. The same merchant has different records in Salesforce, Zendesk, and OKTA with no joins between them.
- **No unified communications record**: There is no shared log of what has been communicated to a customer, by whom, or through which channel. No team can see the full picture.

## What success looks like

- Any internal team can see the complete comms history for a customer in seconds
- Customers can view and manage all Checkout communications in one place
- Queries transfer between teams with full context, not inbox forwards
- Communication preferences are captured once and honoured everywhere
- A complete comms record for any customer can be produced on demand for regulatory purposes

## Next steps

Quantify the scale of the problem before scoping a solution. Data collection targets: Zendesk, Salesforce, OKTA, Legal/Privacy. Target a findings summary within four weeks to inform a solution scoping and ownership decision. See linked data collection tracker.

---

## Live case example

**Ticket:** PayNearMe — disputed transaction trace ($2,079.47), May–June 2026

A merchant contacted support on 1 May to locate funds from a dispute that had expired on Checkout's side, but which the cardholder's bank (PenFed) claimed to have returned via an electronic/ACH payment.

**What happened across 40 days:**

| Date | Team | Action |
|---|---|---|
| 1 May | Support (Dilshad) | Received ticket, forwarded to Disputes without investigation. Told merchant to email disputes@checkout.com directly in future. |
| ~5 May | Disputes (Geeleesha) | Investigated and told merchant the dispute was closed in the cardholder's favour, no reversal received. |
| 15 May | Merchant (Donna) | Followed up with new bank evidence — PenFed reference numbers and a letter showing a chargeback reversal was sent on 10/22/25 via ACH/electronic payment. |
| 19 May | Disputes (Deeptee) | Acknowledged, said investigating. |
| 1 June | Disputes (Deeptee) | Concluded "no incoming funds found." Privately asked Account Manager and CSM to liaise with Finance and Reconciliation to locate funds — merchant not informed of this handoff. |
| 3 June | AM (Perrin) | Relayed Finance's request to merchant: confirm which bank and provide ACH trace number. |
| 3 June | Merchant | Provided trace ID `24388865198105253990565`. |
| 3 June | AM (Perrin) | Finance still couldn't find anything. Asked merchant if they're certain it was sent to CRB. |

**Coordination failures:**
- Five internal teams touched the case (Support, Disputes, Finance/Reconciliation, Treasury, Account Management) with no shared log
- The Disputes team's handoff to Finance was internal-only — the merchant was not told, and received no update for three weeks
- The Account Manager became the de facto coordinator with no tooling to support that role
- The merchant provided the same reference numbers multiple times across different teams
- 40 days elapsed with no resolution and the AM still manually chasing Treasury

Forwarded to Charlie by Perrin Heyka (Senior Manager, Account Management) on 9 June 2026 as an example of support/disputes response time failures forcing AM intervention.

---

## Research evidence

Research question explored: *"When you have an issue that involves more than one Checkout team, what happens?"*

Source: 4 internal Checkout employee interviews (L2 Auth Care Agent, Underwriting Analyst, Underwriting Manager, SE Director). All conducted 2021–2024. Note: evidence is from internal staff, not merchants directly. Merchant-facing research on this question has not yet been conducted.

---

### The wrong team holds the case; the correct owner is never notified

When a case is misrouted, the receiving team retains the merchant relationship by default. The team that should own the case is not notified and has no awareness it exists.

> "Mark would be completely then unaware that this is happening. I wouldn't even know what's going on."
> — L2 Auth Care Agent, on a misrouted integration ticket held in the authentication queue for three weeks (2024-06-27)

> "It's just surprising that obviously it was misclassified from the beginning and then Mark is not even, wouldn't even be aware of it unless you have not said anything... there's like a visibility thing."
> — Observer (same session)

> "If the point of contact at checkout ends up having three or four different people dealing with it for the motion side, then it would be good for them to know where it's spending."
> — SE Director, on multiple Checkout contacts with no shared view (2022-05-03)

---

### No unified escalation channel — agents relay manually across 4–5 disconnected tools

There is no single system for inter-team escalation. Agents jump between Zendesk, Freshservice, Jira, Slack, Gmail, and Freshdesk. Information is copied by hand between systems.

> "So I'm literally having to jump into…Zendesk, Freshservice, Emails… And then I would then have to take that response and put it back into Zendesk."
> — L2 Auth Care Agent (2024-06-27)

> "In an ideal world? I would expect that when I've put in my documents or written an escalation, that if I press a button, it goes straight to that team and I don't have to create a separate email."
> — Underwriting Analyst (R1-P3), on the gap between current state and ideal (2021-12-03)

> "The more communication channels, the harder it is to deprive [hand over]."
> — SE Director (2022-05-03)

A dependent team also changed their ticketing system from Freshservice to Jira without informing the agent: *"They literally just changed that person and they didn't tell you no until I put that ticket."*

---

### Merchants are held waiting with no accurate status

When a case sits with the wrong team, the merchant continues receiving responses from a team that cannot resolve it. The correct owner is never engaged.

> "I don't want to leave the merchant stagnant because then they'll get upset... it's not for me, but it's sitting with me. So I just keep trying to keep calm."
> — L2 Auth Care Agent, three weeks into a misrouted case (2024-06-27)

> "This should have ended months ago, but you're not responding... This is not support, this is me doing things that I shouldn't be doing."
> — Same agent, on absorbing a case that belonged to another team

---

### Complex cases require up to 5 teams plus 2 committees, with no shared SLA

High-risk and complex merchant applications (crypto, PayFac, regulated businesses) require sequential sign-off from multiple teams. Underwriting acts as coordinator with no control over other teams' timelines.

> "You need about four or five team approvals. So yeah, it's time you add a touch point. You're going to increase the time."
> — Underwriting Manager, on PayFac onboarding (2022-04-21)

> "We rely on them to give us their review feedback... it might be enough for one team, but the other team, they still might not be happy."
> — Underwriting Manager, on coordinating approvals (2022-04-21)

> "92% of the applications basically have a back and forth."
> — SE Director, citing Dublin team data (2022-05-03)

> "If you have one person in the chain that's slow, you did everything."
> — SE Director, on sequential dependency compounding delays (2022-05-03)

---

### NPS evidence — merchant-facing signal (Waves 4–7, H1 2024–H2 2025)

22 NPS responses across four waves contain explicit signal on comms confusion, lack of a single point of contact, or difficulty reaching the right internal team. The signal persists across all four waves with no improvement trend.

Note: a further 4–5 responses praised a named individual as their point of contact (Promoters, Tier 2–3). These are the inverse signal — the current coping mechanism is named individuals, not a system. Promoters praise what Detractors ask for.

**Theme 1: No proactive comms on changes or incidents** (6 responses — Tier 1–3, mostly Passives)

Managed merchants asking for earlier warning on changes that affect their business. Appears among Promoters and Passives — a driver toward passive, not only a Detractor complaint.

- W7-196 | Sunday App | T1 | NPS 7 — *"Better communication in advance of changes that affect the business. We've had two internal incidents in the past month."*
- W7-14 | Kiwi.com | T2 | NPS 8 — *"We would really appreciate even more proactive communication about relevant updates and product changes..."*
- W6-293 | eToro | T1 | NPS 9 — *"More proactive communication on updates or changes"*
- W6-380 | Freshly Cosmetics | T3 | NPS 8 — *"...more proactive communication regarding updates, new features, or potential issues."*
- W5-179 | OMNYEX | T1 | NPS 8 — *"Better communication with us when webhooks are down/system is down"*

**Theme 2: No single point of contact / no assigned AM** (4 responses — Tier 2–4, all Detractors)

Concentrated in Tier 4 unmanaged. This cohort grows at SMB scale.

- W4-125 | Beside Trading | T4 | NPS 3 — *"Customer support is pathetic and bureaucratic... bounced around from one agent to another. We have 4 brands listed... need a dedicated account manager."*
- W5-22 | ENTWISTLE & JOYNT | T4 | NPS 5 — *"Having an account manager. Having a single point of contact that can respond quickly or escalate issues."*
- W4-124 | MITRADE | T4 | NPS 6 — *"No assigned relationship manager and production support"*
- W6-456 | TransferGo | T1 | NPS 6 — *"Clearer and more concise communications... more timely and customer-focused communications on escalations"*

**Theme 3: Bounced between / unclear access to internal teams** (4 responses — cross-tier)

Merchants don't know which internal team handles specific issues (disputes, risk, ops). Appears in Tier 1 as well as Tier 4.

- W4-125 | Beside Trading | T4 | NPS 3 — *"bounced around from one agent to another"*
- W7-108 | QONTO | T3 | NPS 7 — *"a lot of back and forth when we encountered our first [dispute] case"*
- W5-283 | G2A | T1 | NPS 8 — *"Maybe think of more direct contact with various teams internally? like chargeback, ops, etc.?"*
- W4-207 | PAYINC GROUP | T4 | NPS 9 — *"Communication with the various teams like risk and tech"*

**Theme 4: Comms clarity on specific topics** (3 responses — fees, disputes, general)

- W6-513 | Zbooni | T3 | NPS 8 — *"Better communication around chargebacks and disputes"*
- W6-349 | Fragrance Direct | T3 | NPS 9 — *"Clearer communication around fee structure"*
- W5-65 | Modanisa | T4 | NPS 1 — *"poor communication, lack of quick response to problems"*

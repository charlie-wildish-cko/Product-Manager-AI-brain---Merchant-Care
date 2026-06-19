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

**Second PayNearMe case: Periodic Review — documents Checkout already holds cannot be located internally**

*Email thread forwarded by Perrin Heyka, 13 June 2026. Covers May 28 – June 12 2026.*

The Periodic Reviews team opened a request for PayNearMe compliance documents (licenses, AML policy, EDD form, shareholding structure). Rather than locating these internally, they contacted the AM and asked her to relay the request to the merchant. Some of these documents Checkout had already collected.

**What happened:**

| Date | Parties | Action |
|---|---|---|
| 28 May | Periodic Reviews → AM (Perrin) | Sent 8-item document request, asking AM to relay to merchant |
| 29 May | AM | Relayed to merchant; questioned whether licenses already held by underwriting |
| 1 June | Periodic Reviews | Sent request to underwriting via Slack; said would keep AM updated |
| 4 June | Periodic Reviews → AM | Chased for update |
| 8 June | AM | Sent merchant-supplied documents; merchant confirmed no changes to director/UBO |
| 10 June | Periodic Reviews → AM | Could only find one license in the folder; requested AM to ask merchant for the other three |
| 10 June | AM | Directed Periodic Reviews to US underwriting folders |
| 12 June | Due Diligence (Jack) | Found the licenses on the CRB Shared Drive; attached them |

**Coordination failures:**
- Documents Checkout had already collected from the merchant were stored across at least three locations (merchant-supplied folder, CRB Shared Drive, US underwriting folders) with no central repository
- Periodic Reviews could not locate documents independently — defaulted to the AM as the search-and-relay function
- Five weeks elapsed and involved AM, Periodic Reviews, Due Diligence, and US Underwriting to locate documents already held internally
- The merchant was asked to re-provide documents Checkout already had

Perrin's framing, verbatim:

> "All of PayNearMe's documents, licenses, and financials should be located in a central repository where the underwriting team, due diligence team, and periodic review team can access them."

This is the document-fragmentation dimension of the same root cause: no central customer record means no central document store. The identity problem is not just about contacts — it extends to every artefact tied to a customer relationship.

---

## Research evidence

Research question explored: *"When you have an issue that involves more than one Checkout team, what happens?"*

Sources:
- 4 internal Checkout employee interviews (L2 Auth Care Agent, Underwriting Analyst, Underwriting Manager, SE Director), 2021–2024
- Discovery conversation with Perrin Heyka (Senior Manager, Account Management), 10 June 2026

Note: evidence is primarily from internal Checkout staff. Structured merchant-facing research has not yet been conducted, but live ticket excerpts below show merchants experiencing the fragmentation directly.

---

### Merchant-facing ticket examples — confusion on cross-team transfers

*Real inbound tickets where merchants contacted the Support team because they did not know which team owned their issue, or could not get a status from the team handling it. These show the problem from the merchant's side, not the agent's.*

**A merchant receives a Compliance / Periodic Reviews request and doesn't know who to send the information to — so they reply to Support.**

The merchant received a Periodic Reviews email from the Compliance team asking for shareholding structure, authorised signatory confirmation, and legal representative details. With no clear owner or route, they came to Support to ask where it should even go.

> "We have received the email titled '01038019: Periodic Reviews' from Checkout's Compliance team, requesting the following information: Shareholding structure / Authorised signatory confirmation / Legal representative. Could you please clarify to whom exactly this information should be sent and for what specific purpose it is required?"

This is the Periodic Reviews comms gap (Item 14, above) seen from the merchant side: the outbound email did not make the owner, route, or purpose clear, so the merchant defaulted to Support.

**Merchants chase dispute updates through Support because they have no visibility into the team actually handling the case.**

> "Hi Dispute Team, Can we have your urgent update please?"

> "Hi team, May we get the update of these two cases? The dispute status has not been updated."

The merchant is reduced to manually chasing for status across teams, with no single place to see where their case sits or what has been communicated. This is the merchant-side counterpart to the Care↔Disputes handoff failure (Perrin) and the "held waiting with no accurate status" finding below.

---

### Periodic Reviews team — collected pain points (June 2026)

*Source: internal problem statement log from the Periodic Reviews team (17 items). Periodic Reviews is an operational team that conducts annual compliance reviews of merchant activity, requiring merchants to complete documentation and questionnaires. Pain points below are drawn from the description column only and grouped by theme relevant to this problem statement.*

**No comms audit trail — emails sent to merchants are not tracked.**

Case owners cannot track what chasers have been sent to a merchant, when, or through which channel. There is no mechanism to log outbound communications in Salesforce against the case. If the merchant is unresponsive over 90 days, the case owner is not automatically notified to move the case to the next stage.

> "What do the initial and followup emails sent out from CKO look like from the merchant's POV? Can the chaser be tracked on SF for audit trail? In case the merchant has been unresponsive in the 90 days, how does the case owner get notified about moving the case into the next stage (i.e. suspension)?" — Item 10

**Case owners are not notified when comms are sent to their merchant — or when merchants respond.**

The PR team case owner has no visibility on emails or automated chasers sent to the merchant via the dashboard. When a merchant attests to information on the dashboard, the relevant analyst receives no notification via email or Salesforce.

> "How is the PR Team (Case owner) notified of any initial emails or chasers sent to the merchant (enterprise/sub-entities) on their dashboard at D-30? Can this be implemented onto SF if it is not already?" — Item 9

> "Analysts at Periodic Review Level are not getting notifications via email or SF when information on file is being attested to. This observation has been made on a sample basis for 3 merchants." — Item 6

**Agents cannot see what is pending from the merchant's side.**

When a case is assigned, the agent has no visibility on what documents or actions are still outstanding from the merchant's perspective. They also have no view into the merchant dashboard to check pending items.

> "When a case has been assigned to an agent, they do not have visibility on what is pending from the merchant's side at T-90 days. Is it possible to have a view only access to the merchant's dashboard on items that are pending?" — Item 8

**No reliable way to identify case owner across systems.**

To identify who owns a periodic review case, analysts must leave the RA Tool, navigate to Salesforce, and search by case ID manually. There is no linked view.

> "Is there any way the RA-T can be updated through Salesforce in the homepage itself to notify the agent working on the case? Currently, we have to go to SF and search for the case ID to identify the case owner." — Item 7

**Platform merchants have no scalable notification channel for periodic review triggers.**

Platforms are currently notified of sub-entity periodic review triggers only via dashboard webhook. There is no bulk communication mechanism — for example, a monthly summary of all sub-entities triggered.

> "As a platform merchant when a sub-entity is triggered for Periodic Review, the only way I am intimated is through the dashboard webhook. There should be more sustainable way of communicating bulk triggers (for eg. a list of all merchants triggered at the end of the month)." — Item 3

**Merchants arriving via periodic review emails land on the wrong dashboard page.**

When a merchant clicks through from a periodic review email and logs in to the dashboard, they are redirected to the default client view rather than the specific entity page that requires action. The email does not contain sufficient guidance to navigate correctly.

> "If not, they might go to the client view (which is the default behaviour in most cases after logging in to the Dashboard), and it may be difficult for them to get to the right entity that needs a periodic review." — Item 14

---

### AM discovery conversation — Perrin Heyka, 10 June 2026

*Informal discovery conversation, not a structured research interview. Perrin manages enterprise merchants including PayNearMe and One Finance.*

**Care↔Disputes handoff is the primary merchant-facing cross-team failure.** Perrin confirmed this is the most common pattern, happening roughly once or twice a month. The PayNearMe ticket (see live case example above) is representative.

> "One Finance doesn't know where they need to follow up or which email thread they should be following up on. And then they'll follow up with Care and then Care will be like no it was transferred to these other people, please follow up directly with them."
> — Perrin Heyka

**Merchant contact knowledge lives in the AM's head, with no structured way to share it.** Perrin knows who the right contact is at each merchant for different issue types, but there is nowhere to record this so other Checkout teams can access it. The result: internal teams always route through the AM even when they could contact the merchant directly.

> "I don't always have the right place to put that knowledge so that other people at Checkout can know that information. It's often just like lives in my head."

> "In Salesforce... you can't say this is the person to reach out to for disputes. Like I've in the past put like all caps DISPUTES MANAGER as a workaround and sometimes I think our disputes team knows how to pick that up directly."

**Periodic review teams have duplicate processes and don't share documents.** Two separate periodic review processes (financial and compliance) run independently, both requesting documents from the same merchant. When one team had already collected financials, the other team in Mauritius didn't know and was about to request them again.

> "Those two teams aren't talking to each other. And so I had to tell somebody in Mauritius, please go coordinate with Stephen who just did a periodic review for PayNearMe two months ago and already got their financials."

> "The fact that the team in Mauritius didn't know that we had PayNearMe's financials handy — there's a misconnection there."

Perrin's view on the fix: periodic review and underwriting should coordinate directly to share documents before going to the AM or merchant.

> "I keep trying to push our team that's handling this to coordinate directly with underwriting to get access to those documents as opposed to going through me, the account manager."

**Salesforce contact data has no hygiene process.** Contacts are updated ad hoc.

> "It's more like when I have the time slash when I remember — if I have a new contact, I'll try to make sure I sign them up to receive our newsletter and our automatic communications."

**Support blind-transfers to AM without context.** When support reaches the limit of what they can resolve, they loop in the AM without explaining what was tried or why they're escalating. The AM receives the ticket cold.

> "They've been directly dealing with one of my merchants and then they get to a point where they can't handle it anymore and then they'll just like dump it on me and they'll just say 'looping in your account manager, thanks' and then they get out of there."

Perrin's suggestion: before the handoff email lands, a Slack message or tagged ticket note flagging why, what was tried, and what the merchant may need next.

**~50% of inbound support contacts have no dashboard account, making them impossible to authenticate.** Noted by Charlie, confirmed by Perrin as a hard problem — AMs cannot create dashboard users, the merchant admin must do it, creating a two-person dependency for every new user.

> "I cannot as an account manager add somebody... two people have to go [be involved in] getting one new user created."

**Useful idea: notify the account admin, not the unrecognised user.** Rather than emailing a contact who emails in without a dashboard login, the suggestion was to notify the merchant's admin account directly so they can provision access.

> "Don't email Dave. Email the AM admin and say this person has messaged us three times and it seems like he needs a dashboard account."

---

### Account Manager (Tier 4 merchants) — Richay Bhagea, 12 June 2026

*Richay manages a portfolio of approximately 40 Tier 4 (smaller) merchants. He sits in Semi's team.*

**Merchants are told to re-raise their issue with a different team — then the original ticket closes without resolution.**

When a Care ticket touches risk or disputes, the current process is to tell the merchant to email risk@checkout.com or disputes@checkout.com directly. If that team then decides the issue is out of scope, the ticket is closed. The merchant has no awareness of what happened and no route back in.

> "In many cases risk will say 'we need to check with another team' and if there's no flow on Zendesk they will just ask the AM to contact separately or raise another ticket. My concern here is that when they say this, risk team will just review the request and say 'this is not mine'. If the ticket is already closed, is the agent really aware of any new updates?"

**From the merchant's perspective: confusion, a closed ticket, and escalation to the AM.**

> "They will just escalate this to me and say: 'Rich, I'm trying to get in touch with your team and I'm just getting emails and notifications saying my ticket is closed. I'm not sure what's happening.'"

Richay's view on what the experience should be:

> "The merchant took his time to raise a request. Now we are saying 'this is not us, you need to contact this team.' The web form should be the main source where everyone behind that form will initiate every discussion with everything. We should not be asking the merchant to raise any new request."

> "They get a ticket number. If the ticket is closed they're confused. They will just raise a new ticket and again it's just creating tickets. I've seen this many times."

**Frequency: roughly once per week for Richay's portfolio of 40 merchants.** Cross-team issues don't happen constantly, but when they do, they escalate to the AM. Richay intervenes proactively when he has visibility, but if the issue goes to support directly he has no awareness unless he manually checks Zendesk.

> "I would say it happens — not so often — but if it goes to support this can be problematic. I just have to let them know to CC me because I won't have visibility otherwise on Zendesk."

**Contact data is AM-managed and largely static — merchants rarely initiate updates.**

Out of a portfolio of 40 merchants, one contacted Richay in the past month to flag that two contacts had left the business. All contact updates flow through the AM to Salesforce. Merchants have no self-serve path.

> "They will have to tell me. So whenever they tell me I can update Salesforce. Out of my 40 merchants, only one told me last month 'these two people are no longer with the business, can you update from your line?'"

**AMs are subscribing contacts to communications without explicit merchant consent — a latent compliance risk.**

Richay manually subscribes contacts to newsletters and campaigns on the merchant's behalf. Those contacts have not consented directly. A merchant could legitimately ask why they are receiving communications they didn't sign up for.

> "Some users I will myself check: 'you must receive the newsletter.' But they did not consent to that. So tomorrow they can say: 'Why am I receiving all these emails? I did not sign up for that.' But I did — in the background, for them."

His proposed solution: a dashboard preference centre where merchants self-select communication types, with automatic sync to Salesforce.

> "On the dashboard they log in — they get a popup: 'I want to receive all types of important communication.' They check a list: technical updates, this, this, this. Once it's checked, it's automatically updated on Salesforce. That would be incredible."

**Dashboard user management blocked when the account owner is unavailable.**

Merchants were previously told Checkout would add dashboard users for them. Policy changed: merchants must now manage users themselves via their admin. But for many Tier 4 merchants the account owner is a board member or CEO who never logs into the dashboard. If they're on leave, no users can be added.

> "Some owners — they are board members or CEOs — they don't really care, they never touch the dashboard. So it can be complicated sometimes. The owner is on leave for one or two months. Now I have to explain: 'as an admin you can still do that.'"

**Flow migration comms: a real example of contact management failure at the merchant level.**

One merchant (LDLC) received 15 emails about the mandatory Flow upgrade but treated them all as marketing because the subject lines did not signal urgency. She did not act on them in time. The underlying issue: the right technical contact at the merchant was either not on the list or not flagged as the right person for mandatory upgrade communications.

> "Out of like these 15 emails, she just thought it was like a marketing campaign. Use something like: 'hey, it's a mandatory upgrade requiring your attention.' Differentiate between what is very important, what is marketing."

---

### Marketing / Customer Communications — Thomas Martindell, 12 June 2026

*Thomas Martindell runs merchant communications for the Marketing team, responsible for sending operational and commercial comms to the merchant base. He owns the segmentation and contact list infrastructure used to determine who receives what.*

**The unified contact view is a hand-built workaround, currently broken.**

Thomas's team merges two data sources — dashboard portal users (via a Looker report) and Salesforce contacts — using a third-party tool (Coefficient) that runs each morning. This is the closest thing to a unified contact list that exists. The Looker report broke during a BigQuery migration several weeks ago and is currently stale. The team is running on outdated portal user data in the interim.

> "We do have a feed which my colleague Theodore can speak to in more detail. There is a feed that comes into Salesforce... Then we have a separate Looker report with the ROS. Right now that Looker report had an issue with the BigQuery migration. So the data in it has been stale for a few weeks."

**Offline contact lists exist outside Salesforce and the dashboard, and nobody knows about them.**

Teams managing compliance requests for information (RFIs) maintain separate contact lists in Google Sheets. These lists are used to decide who receives certain outbound communications. When comms are about to be sent, account managers sometimes flag that the list is wrong — the correct contacts were never added to any central system.

> "We had a change a few months ago for requests for information that we were going to automate. The team basically said, 'Look, we've got a list of contacts that live outside the dashboard in Salesforce. They're just stored in a Google Sheet somewhere.' And we do occasionally — when we're about to send comms — have account managers say, 'Actually, it's not going to the right people. You need to send to these people.' And it's: why are there all these offline lists? Why does all the data not live in Salesforce and the dashboard?"

**Genesis is used as a contact source by some teams, but its data is completely stale.**

Some internal teams pull authorised signatures and contact data from Genesis — a system that captures data at onboarding and is never updated. Thomas's team actively discourages it but cannot control what other teams use.

> "Some of our teams use Genesis as a source of data, particularly for things like authorised signatures. As far as we're aware that data is completely stale. It's captured at the point of onboarding and then it doesn't get updated as a company changes. It's not synced with anything else."

**Merchants cannot self-serve contact preference updates — they have to email Care.**

The only way a merchant can update which contacts receive marketing communications is to email Merchant Care, who then relays the request to Thomas's team. Thomas estimates roughly one to two requests per week reach him — with an unknown number going unactioned because merchants don't know how to update preferences or don't bother.

> "Merchants don't have a good ability to update their own contact data. The only way they can do that right now is they have to email into Merchant Care, and Merchant Care contacts us. We get probably a request every week or two... I imagine there's a lot just not being actioned, or merchants don't know how to do it."

**SMB expansion will break the workaround entirely.**

Today, account managers act as the safety net — catching wrong contact data before comms go out and manually updating Salesforce. At SMB scale there are no account managers. Thomas's view: merchants missing communications at scale creates a direct revenue risk. The Brexit precedent is a concrete example: large-scale legal entity migrations result in significant churn from merchant cohorts that simply cannot be reached.

> "SMB is the problem one. If we start scaling up SMBs, we'll get merchants missing communications. Say we have something like Brexit where there's like a legal entity change and you need to change your company — then you need to change your legal entity you're contracting with — a big section of customers who we just can't mail. We'll start losing revenue for those sorts of things. We find every time we do a big migration, we have a big amount of churn from those customers we just can't contact."

Thomas's summary of the root cause:

> "It should be close to a consumer experience. Something like your banking app. You configure everything there. If you're doing basic account management, you shouldn't ever need to email a support team for it."

**Email is not a robust primary identifier — and this will compound as the user base grows.**

Discussion about whether email can serve as the linking key across systems. Both Thomas and Charlie noted that the same person can have multiple email addresses, email addresses change, and email-based identity creates merge/duplicate/fraud risk at scale. The Nationwide model — customer number for identity, email for contact preference only — was raised as a better pattern.

> "If we're using email as the primary identifier in consumer, that's going to cause a lot of problems. Someone changes their email — how does that reconcile? The email alone is not a robust way to link all these things."

**A preference centre is in progress, but no one is working on centralised contact management.**

Amanda and Irene are building a dashboard notification/preference centre. Thomas confirmed this is relevant but distinct: the preference centre lets merchants configure notification types, but does not solve the underlying problem of where contact records live or how they stay current. No product work is currently scoped for centralised contact management.

> "If we can get some kind of preference center, that would be so handy for our team... but no one's looking at centralised contacts."

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

# Customer Personas — Merchant Care

> UX personas for the Merchant Care product. Each persona represents a real user type grounded in documented segment data, support taxonomy volumes, and known product challenges. Use these to evaluate design decisions, frame PRD requirements, and prioritise features.
>
> For segment definitions and support model details, see `01-knowledge-base/products/customer-segments.md`.
> For contact volume data, see `01-knowledge-base/processes/support-taxonomy.md`.

---

## How to Use These Personas

Reference these personas when:

- Writing a PRD: frame the problem in terms of who is affected and what they cannot do today
- Reviewing a design: ask which persona is the primary user and whether their frustrations are addressed
- Prioritising features: use the Design Implications to connect each persona to 2026 deliverables

Personas are grouped into two sets:

- **External** (merchants and consumers who contact support): Maria, James, Priya, Tom, Alex (Remember Me), Jordan (Braavos)
- **Internal** (Checkout.com staff whose work is shaped by Care product): Oliver, Niamh, Marcus

---

## Maria — Merchant Ops Team Lead

**Segment**: Enterprise Standard
**Role**: Operations team lead or support manager at a mid-size direct merchant. Responsible for fielding payment queries from their own customers and resolving them via Checkout.com.

### Goals

- Get a fast, accurate answer without escalating to their Account Manager
- Self-serve as much as possible via the Dashboard or Fin
- Keep her team's resolution time low so internal SLAs are met

### Frustrations

- Transaction data in the Dashboard doesn't surface the context needed to diagnose a decline or refund failure
- Unclear what she can resolve herself vs. what requires Checkout.com intervention
- Fin deflects her with generic answers that don't resolve the specific issue
- Error code labels (e.g. "policy") are ambiguous: unclear whether the policy originates from the issuing bank, Checkout, or internal merchant configuration
- Support responds quickly but responses often aren't actionable ("contact your issuing bank" does not resolve the issue)
- The same issue requires 3–4 separate ticket submissions before receiving a root cause answer
- Dashboard features (analytics, reports, refund tools) are discovered by accident; there is no onboarding to tooling for new team members
- Error code documentation is not linked from the Dashboard; users search externally to find it
- The Dashboard overview does not support multi-dimensional filtering; analysis by currency, payment type, or corridor requires an Excel export
- Frequent re-authentication is a friction point for heavy users who keep the Dashboard open throughout the day

### A day in the life

Maria's team receives a query about a failed payment. She finds the transaction in the Dashboard but the decline code — "policy" — doesn't tell her whether the block is from the issuing bank, Checkout, or her own configuration. She Googles the error code to find documentation, raises a ticket, and receives a fast response that asks her to contact the customer's bank. She re-escalates, and two more ticket exchanges later gets the actual root cause. By the time she relays the answer to her customer, the goodwill has been eroded. If Fin had resolved it at contact with the right procedure, the chain would have been cut short.

**Support expectation**: Low white-glove. Fast, correct, self-serve resolution.

**Design implication**: Primary target for Fin AI deflection and Dashboard data improvements. Payments data availability and Fin Procedures content are the highest-leverage investments for this persona. In-context error code documentation (linking decline codes to KB articles directly from the transaction detail page) addresses the support quality gap. Richer Dashboard filtering and session persistence for trusted devices are secondary improvements. Maps to: PAYMENTS (IN) at 42.8% of contact volume.

### Key quotes (from interviews, 2025)

> *"I raised this to the support team like three times… I didn't think that we got a satisfactory response."* (Plutus)

> *"I had to Google Checkout API error code documentation."* (Plutus)

> *"We are quite happy… we receive the most polite answers… but we need recommendations that actually solve the problem."* (Findo)

---

## James — Payments Strategist

**Segment**: Enterprise or Premium
**Role**: Payments manager, treasury lead, or payments director at a large, sophisticated direct merchant. Manages payment performance and strategic decisions about routing, risk, and compliance.

### Goals

- Understand and fix acceptance rate drops quickly
- Reconcile payments accurately across multiple markets and currencies
- Stay ahead of scheme and compliance changes that affect performance

### Frustrations

- Merchant Care agents cannot advise on payment optimisation strategy; that sits with the Account team and creates delay
- Reporting data in the Dashboard lacks the granularity needed for performance analysis
- L2 escalations for complex reconciliation queries take too long

### A day in the life

James notices an acceptance rate drop in his internal reporting. He checks Checkout.com's Dashboard but can't get the breakdown he needs. He raises a ticket and waits two days for L2 to investigate. His Account Manager wasn't looped in, so there's a parallel conversation about the commercial impact.

**Support expectation**: High white-glove. Specialist knowledge, fast response, relationship-aware handling.

**Design implication**: Not a primary target for Fin or self-service. The Account and Solutions Engineer teams own most of his needs. Merchant Care's role is fast, well-informed L2 escalation and data tooling for reconciliation. Maps to: PAYMENTS (IN) Performance and FUNDS AND FEES Settlements.

---

## Priya — Platform Support Manager

**Segment**: Platform (ISV)
**Role**: Internal support lead at a Platform business (e.g. Sunday, Guesty, Golfmanager). Manages support queries from her own sub-merchants and escalates unresolvable issues to Checkout.com as Level 2.

### Goals

- Unblock her sub-merchants quickly so their businesses keep running
- Have enough data and context to diagnose issues herself before escalating
- Not be the bottleneck between her merchants and a Checkout.com resolution

### Frustrations

- Checkout.com cannot identify her as a Platform contact; she is treated like a standard merchant with no context about her sub-merchants
- Must re-explain the Platform structure (sub-merchant IDs, hierarchy) on every ticket
- Fin has no understanding of the Platform model and cannot help with sub-merchant queries
- Under time pressure: a restaurant that can't take payments during service is a crisis
- Once a sub-merchant is approved and active, the Platform loses access to the onboarding form. Bank accounts, addresses, and compliance documents cannot be updated without raising a ticket to Checkout — context is frozen at activation
- Identifier terminology ("sub-entity ID", "entity ID", "application ID", "merchant ID") is inconsistent across Checkout and Platform-side systems; Platforms don't know which ID to use
- All "action required" items look identical in the dashboard regardless of severity. A compliance deadline that will suspend a sub-merchant and an administrative document update are indistinguishable, causing panic and wasted effort
- Payout rejection status is not available via API; Platforms must manually check the portal and reconcile their orchestration system by hand
- The same document is sometimes requested twice within weeks; document quality standards (photo format, borders, accepted file types) are not stated upfront, generating repeated back-and-forth with sub-merchants
- Checkout's strict upfront KYC model is a competitive disadvantage: sub-merchants compare the onboarding experience with Stripe (account live in minutes, documents collected progressively post-transaction) and threaten to switch when friction is too high
- The current list-based interface will not scale beyond a few dozen sub-merchants. There is no entity archival, no bulk actions, and no way to manage hundreds of sub-merchants without the list becoming unmanageable

### A day in the life

A property management company using Guesty as their platform changed banks three months after going live. Priya's team tries to update the payout method in Checkout, but the onboarding form is locked post-approval. She raises a ticket to Checkout, waits 24 hours, and receives a response requesting the same documentation already submitted at onboarding. The sub-merchant's payouts are blocked while the ticket is open. Meanwhile, another sub-merchant's account shows "action required" — Priya can't tell without clicking through whether this is a suspension risk or a routine document refresh, so she stops what she's doing to investigate. Neither issue would have required a support ticket if the right tooling existed.

**Support expectation**: Medium white-glove. Checkout must act as an informed L2 that understands the Platform's sub-merchant base — not just at intake, but throughout the merchant lifecycle.

**Design implication**: Primary 2026 delivery focus. Platform identification, structured intake (Dashboard webform and email), sub-merchant lookup tooling, and Platform-aware Fin are the four builds that unblock this persona. Post-approval sub-merchant management (update bank accounts, access frozen forms), payout rejection API/webhook, and action required prioritisation are the next layer of improvements. Progressive onboarding and scale tooling (bulk actions, entity archival) should be scoped for H2 2026 planning. Maps to: Platform support channels (Q1 2026 deliverable).

### Key quotes (from interviews, 2025)

> *"We don't get, via API, the status of payouts if they're rejected, so we have to manually check the status… then mark those manually in our orchestration platform."* (Guesty)

> *"Once a venue is active on Checkout, I'm not gonna have access to any of their onboarding information anymore."* (Sunday)

> *"If we have disputes and action required, I'm gonna panic every morning."* (Sunday)

> *"I'm waiting for this email… I'm feeling that the next email they send might say: okay, we get rid of that, please let us go to Stripe."* (Golf Manager)

> *"I'm stuck with this client. I cannot go on."* (Golf Manager — waiting on Checkout support response)

---

## Tom — Card Issuing Programme Manager

**Segment**: Card Issuing
**Role**: Product manager or operations lead at a fintech or corporate building a card programme on Checkout.com's issuing infrastructure. Manages card issuance, spend controls, and cardholder-facing issues.

### Goals

- Keep the card programme running reliably with fast resolution of configuration and lifecycle issues
- Resolve cardholder-facing card failures before they generate complaints
- Get specialist support without being routed through L1 agents who lack issuing knowledge

### Frustrations

- Issuing queries require specialist knowledge that L1 agents don't have, leading to slow or incorrect first responses
- Low ticket volume means the segment doesn't get specialist routing or dedicated Fin coverage
- Technical complexity of issuing (card lifecycle, spend controls, digital wallet integration) is not well-served by generic KB articles

### A day in the life

A cardholder's virtual card is declined at a hotel. Tom's team receives the complaint and investigates: the spend control configuration is the issue. He raises a ticket to Checkout.com. The L1 agent isn't familiar with issuing and routes it to L2. The delay is acceptable for a non-urgent issue, but Tom worries about a more time-critical scenario.

**Support expectation**: Technical. Specialist L2 handling; low volume but high complexity per ticket.

**Design implication**: Monitor segment. 88 contacts in the last 6 months (0.4% of volume). As the issuing product grows, Fin knowledge articles for issuing and specialist routing rules will be needed. No 2026 delivery priority; flag for 2027 roadmap.

---

## Oliver — L1 Support Agent

**Segment**: Internal (Merchant Care operations team)
**Role**: Level 1 frontline support agent. First point of contact for all inbound Zendesk tickets. Resolves standard queries and routes complex or technical cases to L2.

### Goals

- Identify the merchant quickly and get context without manual lookup across systems
- Answer standard queries (payment status, refund status, account access) without leaving Zendesk
- Hand off to L2 with enough context that L2 doesn't have to start from scratch

### Tools

- **Zendesk** — ticket queue and case management
- **Agent Toolkit** — primary Zendesk app for merchant context (users and payments data)
- **Salesforce** — merchant account data and status
- **Client Admin Tool** — account activation and configuration status
- **Datadog** — transaction logs (L1 has access but interpretation skills vary by tenure)
- **Retool** — various internal lookup tools
- **Slack** — team coordination and tribal knowledge; seniors still rely on Slack threads for process knowledge

### Frustrations

- **Knowledge is tribal**: senior agents carry process knowledge in their heads, not in documentation — *"The knowledge of your colleague is very difficult to replicate because it's in their heads rather than somewhere you can search for"*
- **Tool fragmentation**: resolving a single ticket requires 3–4 separate tools — *"just for one ticket, we have to involve 3 to 4 tools to get an outcome — this is painful for everybody"*
- **Dashboard search limitation**: can only search users by Client ID or Entity ID; searching by name requires manually paginating through 100+ users
- **Timezone isolation**: Singapore-based agents on early shift cannot ask UK/Mauritius seniors in real time; must self-study and pre-draft responses for senior review before sending
- Platform tickets arrive with no sub-merchant context, making triage impossible
- Product launches arrive without updated KB articles, macros, or routing rules, leaving agents to answer from memory

### A day in the life

Oliver opens the Dispatch queue and prioritises: urgent tickets that require internal team collaboration go first, while the morning window when UK/Mauritius colleagues are online is reserved for anything that needs escalation. He checks Agent Toolkit to pull merchant context before reading the ticket content. For account activation or configuration queries, he checks Salesforce and the Client Admin Tool. He uses Datadog for transaction log lookups, though newer agents on his team are still building confidence interpreting logs without guidance. One Platform ticket arrives with only the Platform's entity ID — no sub-merchant context — so he asks the Platform to re-send with the sub-merchant ID. He handles fewer than 5 tickets per shift, but each ticket requiring tribal knowledge or multi-tool investigation takes significantly longer.

**Support expectation**: Internal user. Needs fast merchant identification, reliable in-Zendesk data access, and clear escalation criteria.

**Design implication**: Primary beneficiary of Agent Consultant knowledge retrieval and Agent Toolkit. Knowledge fragmentation remains the core L1 efficiency problem — Agent Consultant must surface the right answer without requiring agents to know which system to check or which colleague to ask. Dashboard user search by name is a secondary blocker with no current workaround. Every product launch must include KB articles, Zendesk macros, and routing rules as launch-blocking dependencies. Maps to: AI Agent Consultant (Q1–Q2 2026), Agent productivity tools (Q2–Q4 2026).

### Key quotes (from interviews, 2024)

> *"The knowledge of your colleague is very difficult to replicate because it's in their heads rather than somewhere that you can search for."*

> *"There's too many of them. Just for one ticket, we have to involve 3 to 4 tools to get an outcome. This is painful for everybody."*

---

## Marcus — Account Manager / Technical Account Manager

**Segment**: Internal (Commercial team)
**Role**: Account Manager (AM) or Technical Account Manager (TAM) managing the relationship with one or more Enterprise or Premium merchants. Acts as the merchant's primary commercial contact and intermediary for complex support issues.

### Goals

- Know about and resolve high-priority support issues for his accounts before the merchant escalates to him
- Submit escalations to Care cleanly and track them without chasing by email
- Not be blindsided by a merchant complaint that Care has been handling for days without looping him in

### Frustrations

- Has to email Care to check on ticket status rather than finding it himself
- No formal internal submission process: escalations go via email and get lost or deprioritised
- Care resolves sensitive merchant issues directly without always notifying him, creating gaps in his relationship narrative

### A day in the life

A Premium merchant's Payments Director messages Marcus about a settlement delay. Marcus checks the Looker dashboard to see if an open ticket exists. He finds one, but it's been open for two days with no update. He emails the Care team to chase. They update him an hour later. He relays it to the merchant and manages the commercial conversation. The resolution was correct, but the communication gap nearly cost a renewal conversation.

**Support expectation**: Internal stakeholder. Needs visibility into ticket status for his accounts and a formalised route to submit and track escalations without going through email.

**Design implication**: Looker dashboard already provides basic ticket visibility. The 2026 priority is building the internal ticket submission form so AMs and TAMs can raise and track escalations to Care directly, replacing the email-based process. Maps to: Centralised merchant ticket submission and visibility (TBC, 2026 roadmap).

---

## Niamh — L2 Technical Specialist

**Segment**: Internal (Merchant Care operations team)
**Role**: Level 2 technical specialist. Handles escalated, complex, or segment-specific tickets that L1 cannot resolve. L2 is organised into four specialisms: Gateway & Card Processing (authorisation, declines, clearing); Integration & Solution Engineering (ecommerce platform integrations, token migration); Financial experiences (reconciliation, settlement, reserves, fees); and Authentication (3DS, payment flow, SCA).

### Goals

- Diagnose root causes accurately on the first investigation without re-doing L1's work
- Resolve without further escalation to Product or Engineering where possible
- Give L1 a clear and usable answer to relay back to the merchant

### Tools

- **Datadog** — deep log analysis; L2 reads these in detail where L1 may only have surface access
- **Traffic Insights** — PCI-safe payment flow inspection and logging
- **Looker** — reconciliation data pulls for merchants (agents pull reports manually on merchant behalf)
- **Retool** — various internal tools including security deposit creation
- **Clearing Events tool** — settlement and clearing status lookup
- **Postman (via remote desktop)** — payment reversals; executed remotely for security compliance; scheme-specific windows (Mastercard 24h, Visa 30 days)
- **Slack** — escalation coordination with L3 engineers and specialist teams
- **JIRA** — formal L3 escalation tickets

### Frustrations

- **Role creep**: L2 absorbs work from Solution Engineering (token migrations), Account Management (merchant account setup), and self-service gaps (manual reconciliation pulls) because those functions lack support rota coverage — *"I'm doing all these things that he should manage... instead I'm doing things that I shouldn't be doing"*
- **Merchant reconciliation gap**: merchants cannot download more than limited history themselves; L2 agents use Looker to pull 2-year reports manually, which is not scalable
- **Escalated tickets arrive with insufficient context**: missing payment IDs, absent sub-merchant identifiers, no L1 investigation summary; each incomplete handoff adds 30–60 minutes of rework
- **Cascade failures**: tickets involving multiple internal teams (Merchant Config, L3, Pricing/Billing) can bounce for weeks with no clear owner — *"a missing payment incident from two months prior, still unresolved"*
- No sub-merchant lookup tooling for Platform queries; Niamh must ask the Platform to re-provide context that should have been captured at intake

### A day in the life

Niamh picks up an escalated FTS ticket from a Platform contact (Guesty) about a property manager's missing settlement. The ticket has the Platform entity ID but not the sub-merchant's. She contacts the Platform for the sub-merchant ID, opens Traffic Insights to trace the payment flow, checks the Clearing Events tool to confirm settlement status, and identifies a reconciliation mismatch. She pulls the merchant's report from Looker and resolves with a detailed explanation. Later, she picks up a reversal request: checks the clearing file to confirm the transaction has cleared, determines it's a Mastercard card within the 24-hour window, and executes the reversal via Postman on remote desktop. She raises a JIRA ticket to L3 for a card processing authorisation issue that requires a code-level fix. Fewer than 5 tickets per shift, each requiring deep investigation.

**Support expectation**: Internal user. Needs cross-system data access, complete context from L1 intake, and specialist tooling for segment-specific queries (Platform, Issuing, reconciliation, compliance).

**Design implication**: Primary user of advanced Agent Consultant capabilities including data tooling and action-based modes. Ticket misclassification — previously the top L2 efficiency leak — is now being addressed via Fin AI auto-classification. The next highest-impact product investment is merchant reconciliation self-serve, which would remove the largest category of manual L2 FTS work. L2 role creep (absorbing SE/AM/product team work) requires a parallel ownership and rota model fix that Agent Consultant alone will not solve. Maps to: AI Agent Consultant (Q2 2026), Platform support model build (Q1 2026 ongoing), merchant self-serve reconciliation (TBC roadmap).

### Key quotes (from interviews, 2024)

> *"I'm doing all these things that he should manage... instead I'm doing things that I shouldn't be doing."* (on absorbing Account Manager's work)

> *"I didn't even know yesterday"* — reserve period rules discovered via trial-and-error rather than documentation.

---

## Alex — Consumer (Remember Me)

**Segment**: B2C Consumer
**Role**: Consumer who has saved their card via Checkout.com's Remember Me product. Remember Me is a passive saved-card service: consumers enrol at checkout on a merchant's site and may not know Checkout.com is the underlying provider.

### Goals

- Resolve a payment failure or card management issue quickly
- Understand why the payment failed and what to do next

### Frustrations

- Webform-only contact channel; no phone or live chat
- Slow response times relative to consumer expectations
- No formal complaint process
- May not know they are contacting Checkout.com rather than the merchant

### A day in the life

Alex tries to use a remembered card at checkout and the payment fails. She can't find a phone number for Checkout.com. She locates the Remember Me webform, submits a query, and waits two business days for a response. The issue is resolved, but the experience felt slow and impersonal for what she considers a payment product.

**Support expectation**: Consumer-grade. Fast response, empathetic tone, clear resolution.

**Design implication**: Remember Me is live but low-volume and informally supported. The contact model is simple: webform intake, email resolution. The priority is ensuring response times and resolution quality meet basic consumer expectations. No structural changes required before Braavos launch; maintain and monitor. Maps to: B2C support operations (ongoing).

---

## Jordan — Consumer (Braavos)

**Segment**: B2C Consumer
**Role**: Braavos neobank account holder (2027 launch). Braavos is a mobile-first neobank competing with Monzo and Revolut. Jordan has actively chosen Braavos for its value proposition and expects a full-service consumer banking experience.

### Behavioural Sub-segments

Jordan is not a single archetype. Two primary sub-segments shape product and support design decisions.

**Trailblazer**
A 24-year-old analyst flat-sharing with friends. Generally on the lookout for offers and deals; seeks social experiences over the weekends. Pain points: actively looking for ways to invest and grow money, relies on others for financial information, struggling to save. Openness to new providers is high but loyalty is contingent on long-term value — will switch quickly if it isn't delivered.

**Smart Value Seeker**
A 34-year-old marketing consultant. Uses resale platforms (e.g. Vinted) and buy-nothing-new approaches to free up money for big goals. Saving for a house in London; relies on splitting payments for expensive purchases. Pain points: relies on points-based rewards; actively seeks ways to budget and grow wealth. Needs to know the benefits are clear and there are no hidden terms before committing to a product.

### Psychographic Profile

- **Financial profile**: Steady disposable income, typically dual-income household, stable employment
- **Spending style**: Cautious but not restrictive; actively looks for deals; uses 0% credit cards, BNPL, and cashback strategically rather than compulsively
- **Attitude toward money**: Seeks balance between enjoying life now and planning ahead; spending decisions are aligned to personal values (connection, security, self-expression)
- **Attitude toward technology**: Open to new financial apps when clear benefit is evident; relies on rewards apps and social media for pre-purchase discovery
- **Primary anxieties**: Losing track of spending; impulse purchases; misuse of credit; lack of visibility or control over finances
- **Immediate goals**: Saving for meaningful experiences (renovations, travel, family); reducing financial stress; maintaining financial alignment with a partner
- **What they value**: Autonomy and transparency; tools that support shared decision-making; no surprises; design that encourages thoughtful choices rather than impulsive spending

### Goals

- Resolve account or payment issues quickly with minimal friction
- Understand what happened and why
- Know their complaint will be heard and acted on
- Maintain confidence that their money is safe and the product is regulated

### Frustrations

- No phone channel for a regulated banking product
- No visible complaint handling process
- Slow response times relative to neobank competitors (Monzo, Revolut offer in-app live chat)
- Potential vulnerability identification gaps
- Lack of transparency erodes trust rapidly in a product where trust is the core value proposition

### A day in the life

Jordan's Braavos card is declined abroad. She opens the app expecting in-app chat but can't find one. She submits a webform query and waits. By the time she gets a response, she has used a competitor card instead. The payment issue was minor; the confidence loss was not. For a neobank user who chose Braavos over Monzo, a single unresolved support experience can end the relationship.

**Support expectation**: Consumer-grade, neobank-standard. In-app or live chat, fast response, empathetic tone, clear resolution, complaint rights visible and accessible from day one.

**Design implication**: Braavos launch (2027) requires a full consumer support model live at launch — not added post-launch. Required from day one: phone channel, in-app or live chat, complaint handling (Consumer Duty, 8-week FRL, FOS referral rights), and vulnerable customer identification in Fin. The psychographic profile reinforces the design priority: Jordan values transparency, dislikes surprises, and will disengage quickly if the support experience undermines trust. Braavos competes on trust; every support gap is a churn risk. Maps to: B2C wallet launch preparation (2027 pre-work, 2026 backlog).

---

## Persona Summary


| Persona | Segment               | Primary Need                                                                              | Support Expectation   | 2026 Priority | Key Design Implication                                                                           |
| --------- | ----------------------- | ------------------------------------------------------------------------------------------- | ----------------------- | --------------- | -------------------------------------------------------------------------------------------------- |
| Maria   | Enterprise Standard   | Fast self-serve resolution for transaction queries                                        | Low white-glove       | High          | Fin deflection, Dashboard data, in-context error code documentation, support quality not just speed |
| James   | Enterprise or Premium | Strategic handling for performance optimisation and reconciliation                        | High white-glove      | Maintain      | Fast L2 escalation, data tooling                                                                 |
| Priya   | Platform (ISV)        | Platform identification, sub-merchant context at intake, and post-approval lifecycle management | Medium white-glove    | Primary focus | Identification, structured intake, lookup tooling, post-approval form access, payout rejection API, action required prioritisation, scale tooling |
| Tom     | Card Issuing          | Specialist L2 routing for issuing queries                                                 | Technical, low volume | Monitor       | Specialist routing, Fin KB articles (future)                                                     |
| Oliver  | Internal — L1 agent  | Fast merchant ID, in-Zendesk knowledge retrieval, fewer tool switches                     | Internal tooling      | High          | Agent Consultant (knowledge retrieval), Agent Toolkit, Dashboard user search by name             |
| Marcus  | Internal — AM/TAM    | Visibility into ticket status, formalised escalation route                                | Internal stakeholder  | Medium        | Internal ticket submission form                                                                  |
| Niamh   | Internal — L2 agent  | Complete context at handoff, cross-system data access, merchant self-serve reconciliation | Internal tooling      | High          | Agent Consultant (data + action modes), merchant reconciliation self-serve, role ownership model |
| Alex    | B2C Consumer (Remember Me) | Fast resolution for payment failures; basic complaint access                         | Consumer-grade        | Maintain      | Webform intake, email resolution; monitor volume; no structural changes needed pre-Braavos       |
| Jordan  | B2C Consumer (Braavos) | Neobank-standard support: fast, transparent, complaint rights from day one              | Consumer-grade, neobank-standard | 2027 pre-work | Full B2C support model at launch: phone, in-app chat, Consumer Duty compliance, vulnerable customer ID in Fin |

---

**Owner**: Charlie Wildish
**Last Updated**: March 2026
**Source files**: `customer-segments.md`, `platform-segment.md`, `support-taxonomy.md`, `agent-toolkit-zendesk.md`, `04-active-work/Agent interview transcripts/` (8 interviews, Aug–Sep 2024; researcher: Alcinda); `04-active-work/merchant-interview-transcripts-2025/` (7 merchant interviews, Jun–Nov 2025: Plutus, Findo, Kiwi, Curve, Guesty, Sunday, Golf Manager); `04-active-work/Consumer persona behavioural.png`, `04-active-work/Consumer persona goals.png` (B2C segment research, March 2026)

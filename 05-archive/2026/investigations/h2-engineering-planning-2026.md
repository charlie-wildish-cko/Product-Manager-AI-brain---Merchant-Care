# H2 2026 Engineering Planning — Care Product

**Owner**: Charlie Wildish  
**Updated**: 2026-05-20  
**Audience**: Engineering team (4 engineers + 1 EM)  
**Purpose**: Prioritisation · Scoping · Alignment

---

## Context

**Period**: Q3 (Jul–Sep 2026) · Q4 (Oct–Dec 2026)  
**Team capacity**: 4 engineers + 1 EM  
**Strategic goals**: Reduce contact rate · Reduce cost of support  

H2 is the heaviest delivery half of the year. This doc exists to:
1. Surface everything currently scoped for H2 so the team can see the full picture
2. Identify where engineering effort is concentrated and where conflicts arise
3. Drive decisions on scope, sequencing, and what gets cut or deferred

All items below are scoped in the 2026 roadmap unless marked **(TBC)**. Nothing is committed until engineering has sized the work.

---

## H2 Deliverables — Overview

| Deliverable | Q | Effort signal | External dependency | Decision needed |
|---|---|---|---|---|
| AI First Resolution — Expanded data & procedures | Q3 | L | ARB sign-off (email data policy) | Yes — email policy Phase 2 scope |
| Replace Webform with Fin | Q3 | M | Intercom: CC on Zendesk handoff | Yes — confirm prerequisite met |
| AI Contextual Answers on Dashboard | Q3–Q4 | M | None | No |
| Support Model (Enterprise/Premium + Standard) | Q3 | M | Ops decision (TBC) | Yes — decision status |
| Agent Consultant — Refund reversals + Toolkit rebuild | Q3 | M | None | No |
| Reflex V2 | Q3 | M | NPS data from Airtable | No |
| Merchant Ticket Submission & Visibility | Q4 | L | None | No |
| AI Contextual Answers — Page expansion | Q4 | S | Q3 component complete | No |
| Agent Consultant — Additional tasks | Q4 | TBC | Backlog prioritisation | Yes — which tasks |
| Reflex — Jira Integration | Q4 | M | TBC scope | Yes — in/out scope |
| Consumer Support (Braavos) | Q4 | M | Braavos launch date confirmed | Yes — launch date |
| Knowledge and Data Graph | Q3 | — | Data Science owned | No |
| Agent Productivity — Salesforce case numbers | Q4 | S | Salesforce API access | No |
| Merchant Education Hub — Tutorials (10) | Q3 | S | Q2 site structure complete | No |
| Merchant Education Hub — Tutorials (5) | Q4 | S | Q3 batch complete | No |

**Effort signal key**: S = days · M = 2–4 weeks · L = 4–8 weeks · XL = quarter+  
These are conversation starters, not estimates.

---

## Q3 Deliverables

### AI First Resolution — Expanded Data & Procedures
*Goal: Fin resolves more contact types autonomously, including over email*

**Engineering scope**:
- Connect bot gateway to Payin and Payout BQ data source (trade-off: available now vs. waiting on PLC dependency from Payments Search API)
- Configure Fin for PLC data source from Payments Search API
- Add User Management API to Fin (troubleshoot merchant account access issues)
- Add Sub-merchant Onboarding API to Fin (Platform ops users, Dashboard + email)
- Implement Phase 2 of Fin data policy — enable Fin to share data-driven resolutions over email (all available APIs)

**Note**: Fin Procedures are Product and Ops scope, not engineering.

**Dependencies**:
- Phase 2 email data policy requires ARB design sign-off (Q2 discovery deliverable — confirm status before Q3 starts)
- BQ vs. PLC trade-off: confirm which data source path to pursue first

**Open decisions**:
- Is ARB sign-off for email data policy complete or does it roll into Q3?
- Do we connect to Payin/Payout BQ now and layer PLC on top later, or wait for PLC?

---

### Replace Webform with Fin
*Goal: Retire the static Dashboard webform; Fin becomes primary support entry point*

**Engineering scope**:
- Retire Dashboard webform as standalone entry point (retain exceptions: MCR requests, Fin down fallback)
- Fin captures CC'd email addresses on handoff to Zendesk (prerequisite — currently a webform-only capability)
- Fin routes captured context to Zendesk with correct classification

**Dependencies**:
- **Blocker**: Intercom must deliver CC capability on Zendesk handoff before webform can be retired. Confirm delivery date with Intercom.
- Fin classification must be accurate enough to replace webform routing — confirm Fin involvement rate and classification quality from Q2

**Open decisions**:
- Has Intercom confirmed and dated the CC capability delivery?
- What are the exception handling rules for MCR requests and fallback scenarios?

---

### AI Contextual Answers on Dashboard (Q3 phase)
*Goal: Contextual Fin buttons on Dashboard pages so merchants get instant answers*

**Engineering scope**:
- Build reusable contextual button component to launch Fin with pre-defined prompts
- Integrate with Payments pages first
- Measure deflection impact (feeds Q4 expand/no-expand decision)

**Dependencies**: None critical

**Open decisions**:
- Which specific Payments pages get the button in Q3?
- Who owns the Fin prompt content per page — Product or Content?

---

### Support Model — Enforcement
*Goal: Right channel for the right merchant; enforce tier routing*  
**(TBC — pending Ops decision)**

**Engineering scope**:
- Enable support model for Enterprise and Premium merchants (channel eligibility, SLA enforcement)
- Enforce tier routing for Standard merchants
- Note: merchant attribute enrichment is a Q2 deliverable — Q3 engineering builds on that data

**Dependencies**:
- **Blocker**: Ops decision on support model tiers and SLA rules — not yet confirmed
- Merchant attribute data from Q2 must be in place

**Open decisions**:
- Has Ops confirmed the tier definitions and SLA rules? Until this lands, engineering scope cannot be finalised.
- What happens to merchants that don't have an attributed tier yet?

---

### Agent Consultant — Refund Reversals
*Goal: Agents can trigger automated refund reversal task from within Zendesk*

**Engineering scope**:
- Build new version of Agent Toolkit incorporating the runbook solution — refund reversals is the first runbook implemented
- Build human-in-the-loop trigger for refund reversals (agent initiates; Consultant executes after review)
- Integrate with existing Agent Consultant framework and Zendesk
- Q2 laid the groundwork (Automate Refund reversals in Q2 scope — confirm what carries over vs. what is net-new Q3)

**Dependencies**: Q2 refund reversals automation work — confirm what shipped

**Open decisions**:
- What was delivered in Q2 vs. what is remaining for Q3?

---

### Reflex V2
*Goal: VoC view, spike detection, weekly digest, attribution model tracking*

**Engineering scope**:
- Set up fix implementation measurement from Product teams (attribution model — tracks contact rate reduction from Reflex-originated fixes)
- NPS data merge into VoC view (Airtable source; joined via client ID)
- Spike detection and alert mechanism for recent contacts on specific themes/clusters
- Weekly Reflex digest to Product team leads

**Dependencies**:
- NPS data in Airtable — confirm schema and access
- Q2 theme cluster aggregation + product mapping must be complete (done when: aggregated clusters live, top 10 drivers shared with VP Product)

**Open decisions**:
- How does the attribution model work in practice — does Product self-report fixes, or does Reflex infer from contact volume changes?
- Who owns the weekly digest pipeline operationally once it's live?

---

## Q4 Deliverables

### Merchant Ticket Submission and Visibility
*Goal: Centralised place in Dashboard to submit and track support requests*

**Engineering scope**:
- List view in Dashboard ticket page pulling ticket data and statuses from Zendesk
- Admin view: Dashboard admins can see all their business' support requests

**Dependencies**:
- Replace Webform with Fin (Q3) ideally complete — this builds on Fin as the submission layer
- Zendesk API access for ticket data in Dashboard

**Open decisions**:
- Is this dependent on Replace Webform completing, or can it be built in parallel?
- What ticket data fields are shown in the list view — status, type, SLA, assignee?

---

### AI Contextual Answers on Dashboard — Page Expansion
*Goal: Extend contextual buttons to Settlements, Balances, Users, and other pages*

**Engineering scope**:
- Extend the reusable button component built in Q3 to additional Dashboard pages
- Scope of pages to be determined by Q3 deflection data

**Dependencies**: Q3 component complete; Q3 impact data informing which pages to prioritise

**Open decisions**: None — Q3 data drives the expansion decision

---

### Agent Consultant — Additional Automated Tasks
*Goal: Expand autonomous task capability beyond refund reversals*

**Engineering scope**: TBC — driven by backlog prioritisation (tracked on Confluence page 7847149938)  
**Dependencies**: Q3 Refund reversals complete; backlog priority confirmed

**Open decisions**: Which tasks from the backlog are Q4 priority? (Needs Ops input — agree top 2–3 before Q3 ends)

---

### Reflex — Jira Integration
*Goal: Auto-create quarterly top contact driver issues per product pillar in Jira*  
**(TBC)**

**Engineering scope** (if in scope):
- Automated quarterly creation of top 5–10 Jira issues per product pillar
- Pre-populated with volume, cost, trend, example tickets, recommended Product team
- Human review step before issues publish
- Routing to correct Jira project/board

**Dependencies**: Reflex V2 complete; attribution model stable enough for Jira issue content to be trustworthy

**Open decisions**: **Is this in scope for Q4 or deferred to 2027?** Depends on Reflex V2 stability and engineering capacity.

---

### Consumer Support — Braavos App
*Goal: Support infrastructure for Checkout.com's first B2C product*  
**(Q4)**

**Engineering scope**:
- Set up Zendesk flows for Braavos support tickets: new form, taxonomy, triggers, automations, macros
- Install Fin mobile into the Braavos app as the primary support entry point
- Consumer Duty requirements must be live at launch: complaint handling workflow, vulnerable customer identification in Fin

**Dependencies**:
- **Blocker**: Braavos launch date confirmed — Consumer Duty obligations apply from day one; support infrastructure must be ready before launch, not after
- Fin mobile SDK availability and integration approach

**Open decisions**:
- What is the confirmed Braavos launch date?
- Consumer Duty: complaint handling and vulnerable customer identification — what is the minimum viable implementation for launch?
- Is this within the current team's scope or does it require a separate track/resource?

---

## Other H2 Work

### Merchant Education Hub — Tutorials
*Primarily content scope; engineering involvement limited to any site structure changes*

- **Q3**: Publish next 10 tutorials and videos on support.checkout.com
- **Q4**: Publish next 5 tutorials and videos on support.checkout.com

**Note**: New categories and sections on support.checkout.com are a Q2 deliverable. If site structure work carries into Q3, confirm scope with Content team.

### Knowledge and Data Graph
*Data Science owned — engineering involvement TBC*

Map the relationship between support taxonomy, products, content, and data to identify coverage gaps.

- Map support taxonomy to products and to existing content and data sources
- Identify where Fin lacks content, agents lack SOPs, and data connectors are missing
- Output feeds Fin Procedures roadmap and Knowledge Base prioritisation

**Note**: Owned by Data Science. Confirm whether any engineering input is needed (data pipeline access, connector work).

### Agent Productivity Tools — Routing + SLAs
*Zendesk configuration scope — not engineering*

- Routing by taxonomy Reason (ZD routing rules based on AI contact reason classification)
- SLAs based on issue type, per Segment (Standard / Enterprise / Premium)

**Note**: Dependent on Support Model Ops decision landing and taxonomy reason classification quality being confirmed.

### Agent Productivity Tools — Salesforce Case Numbers
*Goal: Show Salesforce case numbers and status in the Agent Toolkit*

**Engineering scope**:
- Get case numbers from Salesforce and display case status in the Agent Toolkit

**Dependencies**: Salesforce API access; confirm data availability with Commercial/CRM team

### Help Desk Platform Evaluation
**(Q3 analysis · Q4 decision)**  
**Scope**: Q3 — capability gap analysis, light spikes and trials of alternatives (Plain, Pylon, Intercom). Q4 — decision, recommendation approved, contract negotiation or replacement programme initiated.  
**Engineering involvement**: Spikes and technical assessment of platform alternatives  
**Open decisions**: Who leads the technical evaluation? What criteria define the decision?

---

## Open Decisions — Consolidated

Items that need a decision before or early in Q3 to avoid blockers:

| # | Decision | Owner | When needed |
|---|---|---|---|
| 1 | Is ARB sign-off for Fin email data policy (Phase 2) complete? | Charlie / ARB | Before Q3 starts |
| 2 | Has Intercom confirmed CC on Zendesk handoff delivery date? | Charlie / Intercom | Before Q3 starts |
| 3 | Has Ops confirmed Support Model tier definitions and SLA rules? | Charlie / Director of Ops | Before Q3 starts |
| 4 | What shipped in Q2 Agent Consultant (Refund reversals) vs. what carries into Q3? | Engineering | Q3 start |
| 6 | Reflex Jira Integration — in scope Q4 or deferred? | Charlie | Q3 planning |
| 7 | Braavos launch date confirmed — and is Consumer Duty scope clear? | Charlie / Braavos PM | Q3 planning |
| 8 | Agent Consultant Q4 task backlog — which 2–3 tasks are priority? | Charlie + Ops | Before Q4 planning |

---

## Capacity View

**Team**: 4 engineers · 1 EM  
**Parallel workstreams**: The team cannot run more than ~3–4 meaningful workstreams simultaneously. The H2 list above has 8+ active workstreams in Q3 alone.

| Workstream | Q3 | Q4 | Effort |
|---|---|---|---|
| Fin Data & Procedures | Active | — | L |
| Replace Webform with Fin | Active | — | M |
| AI Contextual Answers (Dashboard) | Active | Expand | M → S |
| Support Model (TBC) | Active | — | M |
| Agent Consultant + Toolkit rebuild | Active | Active | M + TBC |
| Reflex V2 | Active | Jira (TBC) | M + M |
| Merchant Ticket Submission | — | Active | L |
| Braavos | — | Active | M |

**Observation**: Q3 has the highest concentration of parallel work. Fin data & procedures (L) and Replace Webform (M) both touch the Fin/Zendesk integration layer simultaneously — consider sequencing or splitting ownership.

---

## Questions for the Team

Use these to drive the planning session:

1. **Capacity ceiling**: With 4 engineers, what's the maximum parallel workstream count without quality risk? Which items should be serialised?
2. **Fin integration layer**: Fin Data & Procedures and Replace Webform both touch the same integration surface in Q3. Is there a sequencing risk? Should one engineer own this whole layer?
3. **Support Model timing**: If the Ops decision on tiers doesn't land before Q3 starts, does Support Model enforcement shift to Q4? What's the knock-on to ZD config work?
5. **Q4 capacity**: Merchant Ticket Submission (L) and Braavos (M) are both Q4. Combined with any Q3 spillover, is Q4 viable as-is?
6. **Reflex Jira Integration**: Is the attribution model stable enough by end of Q3 to make Jira integration trustworthy in Q4? If not, defer.
7. **What's not on this list**: Are there tech-debt, platform, or infrastructure items that should be protected in H2 but aren't on the roadmap?

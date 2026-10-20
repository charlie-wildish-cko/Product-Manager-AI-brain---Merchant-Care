# Support Platform Recommendation: Replace Zendesk with Plain

**Audience**: CPO, COO, VP of Product, VP of Engineering, Head of Support
**Owner**: Charlie Wildish
**Decision needed by**: 30 September 2026 (procurement gate). Zendesk contract renews June 2027.
**Status**: Final draft for Gemini, 2026-09-23. Scores from the 2026-09-23 scorecard. Before presenting, close the open items in Appendix G, starting with investor diligence on Plain's funding and the status of Plain's September feature ships.

---

## How to use this document

Slide content plus design direction. Each numbered section is one slide. Every slide has an **action title** (the conclusion, stated as a sentence), a **body** (what to render), a **visual** (how to build it) and a **source** (8pt footnote).

**Global design direction**

- One idea per slide. The action title is the largest text on the slide, and the body never repeats it.
- Maximum 6 lines of body text or 6 table rows. Anything longer lives in the appendix.
- One hero number per slide, at 3 to 4 times body size, in the accent colour.
- Checkout.com brand colours. The accent colour is reserved for Plain. Zendesk is muted red or grey throughout. Other vendors are light grey.
- No clip art, stock photography or decorative icons. Diagrams, charts and tables only.
- Tables: bold the Plain column, right-align numbers.
- 17 core slides, then a divider, then appendices A to J. Appendix slides are dense by design: they exist to be read, not presented.

**The story in one line per slide**: we are scaling 36x (3) and AI is how we afford it (4), but Zendesk has closed off our AI (5) and makes agents work around it while merchants wait (6). We need to own a thin layer and buy the core (7), because building the core does not pay off at our scale (8). Scored against our own criteria, Plain wins (9), the alternatives fail on architecture (10), and the POC proved it (11). Here is how it fits our architecture, for Support and then Operations (12), and what changes for agents and merchants (13). Price does not decide it (14), the risks are managed (15), and the plan lands before the renewal (16).

---

## 1. Title

**Action title**: Replace Zendesk with Plain, ahead of the June 2027 renewal.

**Body**: Adopt Plain as the support and operations platform. Ray (consumer) moves first in Q1 2027, Merchant Care in H1 2027.

Charlie Wildish, Product, Merchant Care. September 2026.

**Visual**: Recommendation in one line, large, centred. Bottom strip of four wordmarks: Zendesk struck through in grey, Plain in the accent colour, Intercom and Pylon in light grey. The audience sees the shortlist and the outcome before anyone speaks.

---

## 2. The decision on one page

**Action title**: Zendesk cannot carry our growth or our AI. Plain can, and it scores highest on our own criteria.

| | |
|---|---|
| **What changes** | Contact volume grows 36x by 2030. One customer segment becomes four. 79% of 2030 volume is consumer |
| **Why not Zendesk** | Zendesk ended its Fin partnership in April 2026. Agents work around its gaps and every configuration change is manual |
| **What improves** | Agents start with the merchant's context, merchants stop repeating themselves, and work no longer moves by email |
| **Result** | Eight criteria set before scoring, four vendors, a four-week POC. **Plain 2.44 of 3.0.** Intercom 1.94, Pylon 1.82, Zendesk 1.52 |
| **Cost** | Not the deciding factor. Seat prices are close, and Plain's includes everything |
| **The ask** | Approve Plain and the move into procurement by 30 September |

**Visual**: Six-row table, full width, generous row height. The Result row carries the accent colour, with Plain's 2.44 at hero size. This slide has to stand alone for anyone who leaves after two minutes. No chart.

**Source**: `01-knowledge-base/metrics/contact forecasting.md`  ·  `04-active-work/research/support-platform-vendor-scorecard.md` (2026-09-22)  ·  `04-active-work/research/plain-business-case-draft-v1.md`.

---

## 3. What we are scaling into

**Action title**: Support volume grows 36x by 2030, and most of it is a consumer business that has no platform today.

**Chart data**

| | 2026 | 2030 |
|---|---|---|
| B2B contacts | 60,049 | 445,999 |
| B2C contacts (Ray) | 0 | 1,708,800 |
| **Total** | **60,049** | **2,154,799** |

**Three definitions of good, on one platform**

- **Enterprise**: the account manager knows before the merchant raises it.
- **Platforms and SMB**: a plain-language answer in seconds, and a visible route to a human.
- **Consumer (Ray)**: the customer never needs to know Checkout.com is underneath.

**Visual**: Left two-thirds, a stacked area chart from 2026 to 2030, B2B in grey and B2C in the accent colour, so the consumer wedge visibly takes over. Hero number "36x". Annotate "79% consumer by 2030" on the chart itself. Right third, the three segment expectations as three short cards. Do not render the chart data as a table.

**Source**: `01-knowledge-base/metrics/contact forecasting.md`  ·  segment scenarios from `04-active-work/strategy/care-strategy-2026-2030.md`.

---

## 4. AI is how we afford that growth

**Action title**: Every point of AI resolution is worth $412,000 a year at 2030 volume. The platform decides how far AI can take us.

| AI resolution rate, 2030 | Total support cost |
|---|---|
| 60% | $18.4M |
| 70% | $14.3M |
| **80% (strategy target)** | **$10.2M** |

The 2027 operating model runs on the same lever: specialist pods plus Fin give 24/7 coverage with 35 agents instead of 48, and the pods need API-first routing that Zendesk cannot express.

**Visual**: Horizontal bars shrinking from $18.4M to $10.2M, the 80% bar in the accent colour and labelled "strategy target". Hero number "$412k a year per point". A small side-by-side beneath: "48 agents" against "35 agents".

**Source**: `01-knowledge-base/metrics/contact forecasting.md` (2,154,799 contacts in 2030)  ·  Fin at $0.90 per resolution, human contact at a deliberately conservative $20 (our standing benchmark is $40, which lifts each point to $843k and the 60%, 70% and 80% totals to $35.6M, $27.2M and $18.8M)  ·  pod model from `04-active-work/meeting-notes/2026-09/2026-09-15-plain-vs-zendesk-migration-case.md`.

---

## 5. Zendesk has closed the door on our AI

**Action title**: Our use of Fin on Zendesk now depends on an exemption, held by a vendor building a competing product.

- **1 April 2026.** Zendesk wrote to us that it had "made the decision to stop partnering with Intercom / Fin going forward." New Fin integrations are blocked. Ours survives only as an exemption.
- **11 June 2026.** Intercom confirmed from its side: no further investment in the Zendesk integration, engineering in "lights on" mode.
- **Our judgement.** The exemption will not hold. Zendesk bought Forethought in March 2026 and switches off its legacy AI agents in December 2026 to push customers onto its own AI.

The damage is gradual: Fin stops improving on Zendesk while our volume grows 36x, and no single incident will flag it.

**Visual**: A left-to-right timeline: March 2026 Forethought acquisition, 1 April Zendesk ends the Fin partnership, 11 June Intercom confirms, December 2026 Zendesk's legacy AI switched off, June 2027 our renewal. Show one quote on the slide, the 1 April one. Put "our judgement" in a visually separate box labelled as judgement, so it cannot be mistaken for a documented fact.

**Source**: `04-active-work/research/evidence/2026-04-01-zendesk-notice-intercom-integration-partnership-ended.pdf`  ·  `04-active-work/meeting-notes/2026-06/2026-06-11-intercom-renewal.md`  ·  `05-archive/2026/investigations/Zendesk Viability_ AI, Pricing, Market.md`.

---

## 6. Today agents work around Zendesk and merchants wait for it

**Action title**: Agents start tickets without the data they need, pick their own work, and chase other teams by email, and every fix takes weeks.

| | What agents and merchants live with today | At four segments |
|---|---|---|
| **Context** | A ticket is routed before its merchant data lands. Enrichment takes up to 3 minutes and breaks. Agents open tickets blind or in the wrong queue | More segments, more data sources, more breakage |
| **Queue** | Agents pick their own tickets. The handle-time clock starts at assignment, even when an agent holds several, so the metrics staff are judged on are unreliable | Pods and follow-the-sun coverage need routing Zendesk's static groups cannot express |
| **Dependencies** | Treasury and engineering requests go by email, taking hours to weeks, with no shared record. The merchant waits, and nobody chases | Volume multiplies the email |
| **AI** | AI is a side panel the agent cannot question. Fin's Zendesk integration no longer improves (Slide 5) | The gap widens every quarter |
| **Change** | Every fix is manual UI work: 1 to 2 days for a simple change, 2+ weeks for a complex one. 500+ config items, plus $130,000 a year in bolt-ons | Thousands of items. Not maintainable by hand |
| **Integrations and vendor** | The Jira app was deprecated and never replaced. Salesforce needed a custom BigQuery build. Feature requests sit in a backlog with no timeline | Not a partner we can grow with |

**Visual**: Six-row table with a light red-to-grey heat treatment on the right-hand column. Hero number "Up to 3 minutes": how long a ticket can sit without its merchant data. Lead the eye to the first three rows, which are the agent and merchant experience, and let the last three read as supporting evidence.

**Source**: `04-active-work/meeting-notes/2026-09/2026-09-15-plain-vision-architecture.md` (enrichment, AI side panel)  ·  `04-active-work/research/plain-business-case-draft-v1.md` (queue, handle time, config, bolt-ons)  ·  `04-active-work/research/multi-team-routing-overview-plain-intercom.md` (dependencies)  ·  `04-active-work/research/support-platform-vendor-scorecard.md` rows 2.2 to 2.4. Config inventory in Appendix E.

---

## 7. What we need from a platform

**Action title**: Own the thin layer that connects everything, so every vendor underneath it can be swapped.

1. **Our data model, not the vendor's.** Customer identity, routing, AI invocation and data processing run through one chain we control.
2. **AI wherever the work needs it.** Fin handles first contact and hands off with full context. The customer sees one conversation from first contact to resolution.
3. **Our customer data.** Enrichment, taxonomy and identity belong to us.
4. **Integrations that survive a vendor change.** A gateway listens to Fin and creates matching threads.
5. **Config as code.** Routing, fields and workflows live in a code repository, reviewed and deployed like software instead of clicked into a UI, and AI tooling can speed up every change.
6. **Build the connections, buy the core.** The vendor carries the case-management workload.

The layer matters beyond this decision. It is what lets us swap any vendor later, Fin included, without another migration.

**Visual**: Three horizontal bands, left to right. Top: channels (email, chat, forms, Slack, future voice). Middle, in the accent colour, labelled "ours": orchestration, identity and enrichment, taxonomy, AI invocation, gateway. Bottom, in grey, labelled "swappable": case platform, AI agent, Jira, Salesforce, drawn as detachable blocks. List the six principles as short labels down the right edge.

**Source**: `04-active-work/meeting-notes/2026-08/2026-08-20-fin-in-plain-world.md`  ·  `04-active-work/meeting-notes/2026-09/2026-09-15-plain-vision-architecture.md`.

---

## 8. Buy the core now. Building it does not pay off at our scale

**Action title**: Building our own platform only pays off at a volume our 2030 forecast never reaches.

| | Buy | Build |
|---|---|---|
| **Scale** | Cost grows with use: $166,800 in 2026, $713,844 in 2030 | A fixed team, whatever the volume. It only pays off once the vendor bill exceeds that team's cost, and our 2030 peak of 2.15m contacts does not get there |
| **Time to value** | Proven in a four-week POC. Live for Ray in Q1 2027 and Merchant Care in H1 2027 | Unscoped and from scratch: channels, routing, SLAs, agent workspace, permissions. It would take all of Care engineering (5 engineers, 1 EM) and stop the AI and Reflex work this decision exists to enable |
| **Cost** | $166,800 a year, all features included | Estimate: $200,000 a year per fully-loaded engineer. One engineer costs more than the whole 2026 Plain licence, and a build needs several, permanently |

Build stays an option for later. The trigger to revisit it is a volume threshold, not a missing feature.

**Visual**: The table is the slide. Buy column in the accent colour, Build in grey, row labels in small caps. Hero number "$166,800". Add the Uber precedent as a one-line footnote beneath the table: "Uber started on Zendesk in 2010 and built its own support platform once it handled hundreds of thousands of tickets a day. We handle about 165 a day today, and about 5,900 at our 2030 peak."

**Source**: Plain quote per `04-active-work/research/plain-business-case-draft-v1.md`  ·  team size per `05-archive/2026/investigations/zendesk-platform-decision-rfc.md`, Option 4  ·  Uber Engineering, ["Architecting Uber Support with Customer Obsession Engineering"](https://www.uber.com/en-IN/blog/customer-obsession-engineering/)  ·  Zendesk, ["Uber customer story"](https://www.zendesk.com/customer/uber/)  ·  daily volumes from `01-knowledge-base/metrics/contact forecasting.md` (60,049 a year in 2026, 2,154,799 in 2030). Detail in Appendix H.

---

## 9. How we chose

**Action title**: Scored against eight criteria we set before scoring, Plain leads and Zendesk comes last.

**Most of the market was ruled out on structure.** Zendesk, Salesforce, Sprinklr and Freshdesk monetise their own AI and cap ours. ServiceNow, HubSpot and Jira are not built for high-volume customer support. That left Plain, Intercom and Pylon.

| Criterion | Weight | **Plain** | Intercom | Pylon | Zendesk |
|---|---|---|---|---|---|
| Channels, data model and routing | 20% | **2.62** | 2.24 | 2.45 | 2.05 |
| Agent experience | 20% | **2.14** | 1.89 | 1.69 | 1.58 |
| Integration ease | 15% | 2.25 | **2.50** | 2.00 | 1.50 |
| AI compatibility | 15% | **2.60** | 1.60 | 1.80 | 1.20 |
| Config as code | 10% | **3.00** | 1.50 | 0.50 | 1.00 |
| Partnership and reliability | 10% | **2.46** | 1.83 | 1.67 | 1.38 |
| Customer-facing experience | 7% | **2.00** | 1.50 | **2.00** | 1.50 |
| Pricing | 3% | **2.33** | 2.00 | 2.00 | 1.67 |
| **Weighted total (of 3.0)** | 100% | **2.44** | 1.94 | 1.82 | 1.52 |

Plain leads six categories, ties one, and loses integration ease to Intercom.

**Visual**: A three-step funnel across the top (market, ruled out, shortlisted). Beneath it, a grouped horizontal bar chart per criterion, Plain in the accent colour, the others in grey, and the four weighted totals across the foot in rank order with Plain's 2.44 as the hero. A single strip under the chart: "Weights set before scoring · every score evidenced · four-week POC · two reference calls we ran ourselves." Footnote: "Scored 0 to 3. Partnership scores verification strength and pricing scores cost certainty, the rest score build type. Every requirement score, with its evidence, in Appendix A."

**Source**: `04-active-work/research/support-platform-vendor-scorecard.md` (2026-09-22)  ·  `04-active-work/research/support-platform-vendor-requirements.md`.

---

## 10. Why not Intercom or Pylon

**Action title**: Both alternatives fail on architecture before they fail on features.

**Intercom (1.94), the closest alternative.** Strong at ticketing, and better than Plain on integrations. Three structural gaps rule it out:

- **AI agents need a paid human seat.** There is no swappable agent identity. Plain gives AI agents their own seat-free identity.
- **No config as code.** Configuration is manual only, with nothing committed on the roadmap.
- **A rigid data model.** A user cannot belong to more than one company. Fyxer left Intercom over exactly this.

**Salesforce is buying Intercom** ($3.6bn, signed 15 June 2026, closing October 2026 to January 2027). The suite is expected to fold into Service Cloud during our migration. We keep Fin as the AI layer either way.

**Pylon (1.82).** Built for Slack-first B2B support. It has the weakest config as code of all four (0.50), with no sandbox. Its seat price matches Plain's, so cost was never the reason.

**Visual**: Two columns. Intercom on the left and larger, headed by 1.94, with the three gaps as three rows, each with a red cross and Plain's answer beside it. The acquisition as a dated ribbon across the Intercom column. Pylon on the right, deliberately short, headed by 1.82. Plain's 2.44 shown once at the top as the benchmark.

**Source**: `04-active-work/research/support-platform-vendor-scorecard.md` rows 1.21, 3.5, 5.3  ·  `04-active-work/research/support-platform-assessment-customer-references.md` (Intercom vendor call, Fyxer)  ·  Salesforce press release, 15 June 2026.

---

## 11. Why Plain

**Action title**: Plain is the only shortlisted vendor that is API-first and config-as-code, and the POC proved both in four weeks.

**Build 1: four things we proved**

1. **Config as code, working.** Taxonomy, fields, labels and workflows deployed from GitHub, with out-of-band changes reverted automatically. 11 test cases passed in week one. Admins drafted and deployed workflows with Claude, without engineering. This replaces Salto.
2. **API-first.** Everything the Plain interface does is available through its API. Agents see live payment data from our own systems inside the thread, which engineering rates better than today's Zendesk sidebar.
3. **Open to our AI.** Plain has no AI of its own to protect. Fin and our own agents can work threads directly, and Tines already runs Fin-to-Plain escalation in production.
4. **A partner at our size.** A documentation gap fixed the same morning. A feature request designed, built and shipped in one week. Checkout is a design partner on business hours.

**Plain's strategy is our architecture.** Plain builds for technical teams that design their own support experience. It names API-first and config as code as its edge, and its roadmap is AI agents orchestrating batches of work, with customers' own agents plugged in.

**Build 2: what others found, and what Plain has committed**

| Reference call | What it proved | What it warned |
|---|---|---|
| **Vercel** (~60 agents) | A full custom AI agent setup built on Plain's API. "Everything is easy, and you're completely in control" | Roadmap slips: 4 months quoted, 8 delivered |
| **Fyxer** | Left Intercom to run its own AI agents. Plain's data model solved what Intercom could not | The agent interface is too busy |

| Gap | Commitment | Date |
|---|---|---|
| SLAs per taxonomy and per country | In writing | First week of September 2026 |
| Follow-the-sun business hours | In build, Checkout as design partner | 14 September 2026 |
| Export to BigQuery via Fivetran | In writing, with a Plain-funded interim connector | End of 2026 |

**Visual**: Two builds. Build 1: four cards, each a short claim with its proof beneath, and "11 test cases passed in week one" as the hero. Build 2: the reference-call table and the gaps table side by side. Give the "What it warned" column the same visual weight as "What it proved", because the balance is what makes it credible. Use no vendor-supplied material on this slide.

**Source**: `04-active-work/research/plain-business-case-draft-v1.md`  ·  `04-active-work/research/support-platform-assessment-customer-references.md`  ·  `04-active-work/research/support-platform-vendor-scorecard.md` row 3.5  ·  `04-active-work/meeting-notes/2026-09/2026-09-23-plain-ceo-cpo-funding-and-strategy.md`. Company profile in Appendix J.

---

## 12. Our target architecture, with Plain in place

> **PLACEHOLDER: content to be written by Charlie.** Guidance and inputs below. Replace this block once the diagram is drafted.

**Action title (draft)**: Plain is the case platform at the centre of a layer we own, serving Support now and every Operations team after it.

**What this slide needs to show**

- Slide 7's principles made concrete, with named components: where Plain sits, where Fin sits, and which pieces we own.
- How work flows: a contact or an internal event arrives, is enriched and classified, is orchestrated by AI agents, reaches a human only when needed, and feeds Reflex.
- Support first (Merchant Care, Ray), then Operations teams (risk, compliance, finance, onboarding) on the same platform, each as workflows deployed from one code repository.
- What stays swappable: Fin, Plain itself, and specialist AI agents.

**Inputs to draw from**

- Fin deflects above the platform. Plain's machine users orchestrate what lands, handing to a human only when needed, then progressively absorbing standard requests such as refunds (`04-active-work/meeting-notes/2026-09/2026-09-15-plain-vision-architecture.md`).
- Four orchestrators (internal merchant, external merchant, two for Ray) over decoupled specialist agents, such as a payment agent that serves both Fin and human agents, with PCI and PII filtering at the orchestrator (same source).
- A gateway listening to Fin events creates matching Plain threads. Taxonomy and attributes sync automatically to Fin, with no redeploy per change (`04-active-work/meeting-notes/2026-08/2026-08-20-fin-in-plain-world.md`).
- Salesforce pushes merchant records into Plain, replacing today's brittle enrichment services (2026-09-15 source).
- Operations platform, not a Care platform: onboarding and Checkout-generated work (fraud checks, screening alerts) become threads for the owning team. Every Ops team needs to receive, classify and complete work (2026-09-15 source).
- Receiving work and finding answers are two separate jobs, and one vendor should not own both (`04-active-work/meeting-notes/2026-09/2026-09-10-plain-rationale-and-care-slo.md`).
- Routing to teams outside Care: log in the platform first, then route downstream and write back on resolution (`04-active-work/research/multi-team-routing-overview-plain-intercom.md`).

**Visual (draft)**: A layered diagram, top to bottom. Channels and internal event sources at the top. Fin as the customer-facing AI layer. Plain as the central case platform, with machine-user orchestrators inside it. Our owned layer beside it: identity and enrichment, taxonomy, gateway, specialist agents. Downstream: Jira, Salesforce, BigQuery and Reflex. A band across the bottom showing the teams served: Merchant Care and Ray now, then risk, compliance, finance and onboarding, drawn lighter as future scope. Plain in the accent colour. Keep it conceptual, with no field names or API detail.

**Source**: to be confirmed once drafted.

---

## 13. What changes for agents and merchants

**Action title**: Agents start with the merchant's context, merchants stop repeating themselves, and work no longer moves by email.

| | With Plain | Evidence |
|---|---|---|
| **Context on arrival** | Customer cards show live payment data from our own systems inside the thread. Merchant records from Salesforce enrich the thread automatically. Engineering rates the cards above today's sidebar | Cards proven in POC. Salesforce enrichment designed, still to prove |
| **A fair, fast queue** | Priority-first assignment with capacity caps. Urgent tickets jump the queue and nobody can cherry-pick | Proven in POC |
| **No repeating yourself** | Fin hands over with the full transcript, so a merchant who moves from AI to a person does not start again. Our strategy calls a repeat after handoff a system failure | Validated through the Tines reference, not yet run on our own Fin |
| **Dependencies that move** | Escalations become tracked threads with automated chase sequences and SLA-breach digests in Slack. Account managers and engineers follow along on free viewer seats | Chase sequences and digests proven in POC. Jira linking must be self-built |
| **AI that works with the agent** | An agent can question our AI inside the thread, and standard requests such as refunds move to AI over time. One payment agent serves both Fin and humans, so Fin can answer more | Designed. The in-thread mechanics are unproven |
| **The right clock and hours** | SLAs per taxonomy and country, and follow-the-sun coverage across London, Mauritius, Dubai and Mexico | Committed in writing with dates |

Agent experience and customer-facing experience carry 27% of the scoring weight (Slide 9). Plain leads both.

**Visual**: A before-and-after table, Zendesk in muted grey on the left, Plain in the accent colour on the right, the evidence column as small status chips (green proven, amber designed, blue committed). Hero number "27%": the share of the scoring weight on experience. Give the honesty line under the table the same visual weight as the table, because it is what makes the slide credible.

**Source**: `04-active-work/research/plain-business-case-draft-v1.md` (POC results)  ·  `04-active-work/meeting-notes/2026-09/2026-09-15-plain-vision-architecture.md` (machine users, payment agent, enrichment)  ·  `04-active-work/strategy/care-strategy-2026-2030.md` (handoff bar)  ·  `04-active-work/research/support-platform-vendor-scorecard.md` categories 4 and 7  ·  `04-active-work/research/support-platform-assessment-customer-references.md` (Tines, Fyxer).

---

## 14. Cost

**Action title**: Price does not decide this. Seat prices are close, and Plain's includes everything.

| | 2026 (100 seats) | 2030 (400 seats) |
|---|---|---|
| **Zendesk, seats plus bolt-ons** | **~$409,000** | **~$1,084,000** |
| **Plain, everything included** | **$166,800** | **$713,844** |
| Intercom | $193,200 | $772,800 |
| Pylon | $228,000 | $908,400 |

Plain's price covers every channel, AI feature and API with no add-ons, and replaces the $130,000 a year of Zendesk bolt-ons.

**Visual**: Grouped columns for 2026 and 2030, Plain in the accent colour, Zendesk as a stacked column (seats plus bolt-ons). Keep the four vendors visually close: the point of this slide is to take cost off the table, not to sell a saving. No hero number.

**Source**: signed Zendesk order form `04-active-work/research/evidence/2025-06-27-zendesk-signed-contract-Q-540753.pdf`  ·  Plain quote per `04-active-work/research/plain-business-case-draft-v1.md`  ·  Pylon public pricing (featurebase.app/blog/pylon-pricing). Five-year model in Appendix C.

---

## 15. Risks

**Action title**: No risk is left open. Three are flagged, each with a step before contract, and three are mitigated.

| Risk | Mitigation | Status |
|---|---|---|
| **Vendor viability.** Plain is funded to end 2028 and plans a Series B in January 2027. We need it to last to 2030 | Investor diligence before signature, which Plain has offered. Continuity and data-export terms in the contract. Our data stays exportable through the API | Flagged |
| **Handle-time measurement.** Plain has no native metric, and cost per contact is a north star | Co-design the metric on Plain's events API, and write it into the contract | Flagged |
| **Integration gaps.** Vercel and Fyxer both self-built ticket-tracker linking | Resolve before contract, and size the effort into the Merchant Care build | Flagged |
| **Roadmap slippage.** Vercel waited 8 months for a 4-month feature | We build around gaps through the API. Gaps committed in writing with dates | Mitigated |
| **Loss of Zendesk admin depth.** Two admins leaving | Config as code and AI-assisted admin reduce the dependency. Backfill as a support systems administrator | Mitigated |
| **Migration execution.** Nothing signed off yet | No lift-and-shift. API channels first, one email cutover, parallel run before June 2027 | Managed |

**Visual**: A status chip per row: amber for flagged, green for mitigated or managed. Flagged risks first, separated from the rest by a thin rule. Vendor viability leads, since it is the one this audience will ask about.

**Source**: `04-active-work/research/support-platform-vendor-scorecard.md`  ·  `04-active-work/research/support-platform-assessment-customer-references.md`  ·  `04-active-work/meeting-notes/2026-09/2026-09-23-plain-ceo-cpo-funding-and-strategy.md`  ·  `04-active-work/meeting-notes/2026-09/2026-09-08-plain-migration-sequencing.md`. Full nine-row register in Appendix I.

---

## 16. Plan

**Action title**: Four tracks, all landing before the June 2027 renewal.

| Track | When | What |
|---|---|---|
| **A. Procurement** | September to early November 2026 | Approval (we are here), then investor diligence, budget, security, regulatory review (DORA, PCI DSS, GDPR) and contract |
| **B. Ray (consumer)** | December 2026 alpha, Q1 2027 beta | 50 to 100 friends-and-family users on a simple form, then the full architecture. The first Care deployment with no Zendesk |
| **C. Merchant Care** | Build from November 2026, migrate H1 2027 | Config as code, integrations (Fin, Jira, Salesforce, BigQuery), training. API channels first, then one email cutover |
| **D. Wider Operations** | 2027 onward | Risk, compliance and finance ops, 300+ users, each onboarded from the same code repository (Slide 12) |

Ray's December alpha depends on procurement starting this month. Engineering estimates for Track C depend on sign-off of the target architecture.

**Visual**: Horizontal Gantt, four swimlanes, September 2026 to December 2027. Two vertical lines: "procurement close, early November 2026" and "Zendesk renewal, June 2027" in red, so every bar visibly lands before it. A "we are here" marker on Track A. Track D in a lighter shade, since it is upside rather than committed scope.

**Source**: `04-active-work/research/plain-business-case-draft-v1.md`  ·  `2026 deliverables.md` (Help Desk Platform Evaluation)  ·  `04-active-work/meeting-notes/2026-09/2026-09-15-plain-vision-architecture.md`.

---

## 17. Ask

**Action title**: Three decisions, by 30 September.

1. **Approve Plain** as the replacement for Zendesk.
2. **Approve the move into procurement and security review**, so Ray's December alpha stays on track.
3. **Sign off the target architecture**, so engineering can estimate the Merchant Care build.

Decision by consensus across the VP of Product, Director of Operations, Director of Operations Excellence and Product, with CPO and COO confirming.

**Visual**: Three numbered decisions with checkboxes, generous spacing. "30 September" as the hero. Signatories in a row at the foot. No chart, no recap.

---

# Appendices

Not presented. Linked from the core slides for anyone who wants the detail.

## Appendix A: Detailed scoring

A summary slide (A0) rolls up all eight categories for leadership review, followed by one slide per category (A1 to A8) with every requirement score. Scores and evidence summaries come straight from `04-active-work/research/support-platform-vendor-scorecard.md` (2026-09-23), where the full evidence and sources for every cell live.

**Scoring key**: 0 to 3. For partnership, 3 means verified, named and dated commitments and 1 means the vendor's own claim. For pricing, 3 means a confirmed, predictable cost. For every other category: 0 not supported, 1 custom build, 2 configuration or paid add-on, 3 native.

**Visual, slides A1 to A8**: a plain table, Plain's column bold, category score as the last row. Category A1 has 21 rows: split it across two slides if it does not fit legibly.

### A0. Scoring summary by category

| #   | Category                                  | Weight | **Plain** | Intercom | Pylon | Zendesk | Leader          |
| --- | ----------------------------------------- | ------ | --------- | -------- | ----- | ------- | --------------- |
| 1   | Flexible channels, data model and routing | 20%    | **2.62**  | 2.24     | 2.45  | 2.05    | Plain           |
| 2   | Integration ease                          | 15%    | 2.25      | 2.50     | 2.00  | 1.50    | Intercom        |
| 3   | AI compatibility                          | 15%    | **2.60**  | 1.60     | 1.80  | 1.20    | Plain           |
| 4   | Agent experience                          | 20%    | **2.14**  | 1.89     | 1.69  | 1.58    | Plain           |
| 5   | Config as code                            | 10%    | **3.00**  | 1.50     | 0.50  | 1.00    | Plain           |
| 6   | Partnership and reliability               | 10%    | **2.46**  | 1.83     | 1.67  | 1.38    | Plain           |
| 7   | Customer-facing experience                | 7%     | **2.00**  | 1.50     | 2.00  | 1.50    | Plain and Pylon |
| 8   | Pricing                                   | 3%     | **2.33**  | 2.00     | 2.00  | 1.67    | Plain           |
|     | **Weighted total (of 3.0)**               | 100%   | **2.44**  | 1.94     | 1.82  | 1.52    | Plain           |

**Visual**: the same plain table, with the leader's score in each row bold and the weighted total row set apart. Add one line beneath: "Plain leads six categories, ties one and trails one (integration ease)."

### A1. Flexible channels, data model and routing (20%)

| # | Requirement | **Plain** | Intercom | Pylon | Zendesk | Evidence summary |
|---|---|---|---|---|---|---|
| 1.1 | Email ingestion | **3** | 3 | 3 | 3 | All native |
| 1.2 | Email user enrichment (auto-match to org) | **3** | 1 | 2 | 1 | Plain has best control mechanism for linking customer data to identification flows. |
| 1.3 | Domain mapping | **3** | 1 | 3 | 2 | Plain and Pylon have native email domain matching. |
| 1.4 | AI Agent escalation path (Fin handoff w/ context) | **2** | 3 | 1 | 3 | Intercom has this native for Fin, else requires custom integration of Fin. Pylon supports third-party agents but has no native Fin handoff, so it would be a custom build. |
| 1.5 | Live chat with human agent | **3** | 3 | 3 | 2 | All native |
| 1.6 | Instant messaging channels (Slack/custom IM apps) | **2** | 2 | 3 | 2 | All support Slack natively, Plain and Intercom need some custom work. |
| 1.7 | Phone channel (B2C IVR + routing) | **1** | 3 | 3 | 3 | Plain needs custom integration for Phone vendor. |
| 1.8 | Mobile app chat (B2C, 2027) | **3** | 3 | 3 | 2 | All native |
| 1.9 | Internal ticket submission (Account teams) | **3** | 2 | no evidence | 3 | Native via form components & API. |
| 1.10 | Multi-environment support (identify sandbox vs prod user/business) | **3** | 2 | 0 | 1 | Plain is only one with proven way to support multi environment model for businesses & users. |
| 1.11 | Region / contracting-entity enrichment (write routing attribute via API) | **3** | 3 | 2 | 1 | All supported using custom attributes and APIs. |
| 1.12 | Support plan / tier model (P0–P3) | **3** | 2 | 3 | 3 | Native in their customer and SLA features. |
| 1.13 | Skill-based routing | **2** | 2 | 3 | 2 | Pylon has most capability here right now. |
| 1.14 | SLA per tier and taxonomy value | **3** | 2 | 3 | 3 | All provide custom SLA config. |
| 1.15 | Customisable ticket and customer fields | **3** | 3 | 3 | 2 | Native feature on all. |
| 1.16 | Flexible tagging / field system | **2** | 2 | 2 | 1 | All achievable with mix of native and custom. |
| 1.17 | Flexible routing system (branching + fallbacks on any attribute) | **2** | 3 | 3 | 3 | Pylon has most capability here, others can be achieved but needs more custom work. |
| 1.18 | Presence-aware / follow-the-sun routing (real-time agent presence) | **2** | 1 | 2 | 1 | None native but achievable using regional business hours and attributes to route when needed. |
| 1.19 | Business-hours schedules per site/timezone (in/out-of-hours, hold queues) | **3** | 2 | 3 | 3 | All support this. |
| 1.20 | Geographic / entity-based routing (region → site/team) | **3** | 2 | 2 | 1 | All achievable using custom attributes. |
| 1.21 | Flexible data model (custom objects, no hardcoded schema) | **3** | 2 | 2 | 1 | Plain wins here, data model is defined by your model. |
| | **Category score** | **2.62** | 2.24 | 2.45 | 2.05 | |

### A2. Integration ease (15%)

| # | Requirement | **Plain** | Intercom | Pylon | Zendesk | Evidence summary |
|---|---|---|---|---|---|---|
| 2.1 | Fin (Intercom) escalation with context | **2** | 3 | 1 | 2 | Native with Intercom, Plain needs custom work. |
| 2.2 | Jira bi-directional | **2** | 3 | 2 | 1 | Mostly native with some light nuance in experience per vendor. |
| 2.3 | Salesforce sync | **2** | 2 | 3 | 1 | Needs custom, but not major as we are custom today. |
| 2.4 | Knowledge source sync (URL/GitHub, automated) | **3** | 2 | 2 | 1 | Native, but not needed as we have custom knowledge repositories we can sync from. |
| 2.5 | Custom API access to internal systems | **3** | 2 | 3 | 2 | Available using APIs, Plain offers most extensibility for integrations. |
| 2.6 | Full API export of ticket data (Reflex pipeline) | **2** | 3 | 2 | 3 | Native, with nuance on connector offering. Plain building Fivetran connector this year (used for export today). |
| 2.8 | SLA breach alerting (configurable per tier) | **3** | 2 | 2 | 1 | Native features using alerts. |
| 2.9 | AHT / agent task time measurement | **1** | 3 | 1 | 1 | Intercom has native, else custom metric. |
| | **Category score** | **2.25** | 2.50 | 2.00 | 1.50 | |

### A3. AI compatibility (15%)

| # | Requirement | **Plain** | Intercom | Pylon | Zendesk | Evidence summary |
|---|---|---|---|---|---|---|
| 3.1 | Auto-classification on escalation | **3** | 3 | 2 | 2 | All covered. |
| 3.2 | AI agent handoff with context | **2** | 3 | 2 | 2 | All covered some with custom. |
| 3.3 | Pluggable external AI layer (Agent Consultant) | **3** | 1 | 2 | 1 | Plain fully supports this using Machine users or custom workflow to call your Agent. |
| 3.4 | Agent-triggered workflow execution | **2** | 0 | 2 | 1 | Intercom does not support natively. Plain needs custom work but supported as does Pylon. |
| 3.5 | Dedicated AI-agent actor identity, "bring your own agent" | **3** | 1 | 1 | 0 | Plain only supports this offering for custom AI integration. |
| | **Category score** | **2.60** | 1.60 | 1.80 | 1.20 | |

### A4. Agent experience (20%)

**4a. Interface**

| # | Requirement | **Plain** | Intercom | Pylon | Zendesk | Evidence summary |
|---|---|---|---|---|---|---|
| 4.1 | Custom app support | **1** | 2 | 2 | 2 | Plain needs custom work here. |
| 4.4 | Live customer data panel (own sources) | **3** | 2 | 2 | 1 | All offer this. |
| 4.5 | Internal collaborator access (no full agent seat) | **3** | 1 | 1 | 1 | Plain only one with free non Agent seats. |
| | Sub-category score | **2.33** | 1.67 | 1.67 | 1.33 | |

**4b. Agent-facing routing**

| # | Requirement | **Plain** | Intercom | Pylon | Zendesk | Evidence summary |
|---|---|---|---|---|---|---|
| 4.6 | Queue-view scoping by attribute (prevent cherry-picking / segregation) | **3** | 3 | 2 | 2 | Native, standard functionality |
| 4.7 | Push and pull queue models (both supported, view lock at shift end) | **1** | 2 | 1 | 1 | None have native, needs custom rules. |
| 4.8 | Capacity controls and handoff mode (concurrent caps, block near logoff) | **2** | 2 | 2 | 2 | Can be done using native and custom rules. |
| 4.9 | Conditional routing on computed thresholds (rolling-metric caps) | **1** | 1 | 1 | 1 | Would need fully custom rules. |
| 4.10 | Automated ownership release on SLA-breach risk (predictive reassignment) | **1** | 2 | 1 | 1 | Would need fully custom rules. |
| | Sub-category score | **1.60** | 2.00 | 1.40 | 1.40 | |

**4c. Data and permissions**

| # | Requirement | **Plain** | Intercom | Pylon | Zendesk | Evidence summary |
|---|---|---|---|---|---|---|
| 4.11 | B2B/B2C data wall (BPO isolation) | **2** | 2 | 2 | 2 | All offer permissions or workspaces to separate agent teams. |
| 4.12 | Role-based access control | **3** | 2 | 2 | 2 | All offer RBAC, Plain most proven. |
| | Sub-category score | **2.50** | 2.00 | 2.00 | 2.00 | |

**Category score: Plain 2.14, Intercom 1.89, Pylon 1.69, Zendesk 1.58.**

### A5. Config as code (10%)

| # | Requirement | **Plain** | Intercom | Pylon | Zendesk | Evidence summary |
|---|---|---|---|---|---|---|
| 5.1 | Sandbox/test environment mirroring production | **3** | 2 | 0 | 1 | Plain offers this in full as custom code can be created. Intercom needs manual release work done via UI. Pylon has no sandbox. |
| 5.3 | Config as code (version-controlled, CI/CD-deployable configuration) | **3** | 1 | 1 | 1 | Only fully available in Plain. Else limited use of APIs to achieve same goal. |
| | **Category score** | **3.00** | 1.50 | 0.50 | 1.00 | |

### A6. Partnership and reliability (10%)

**6a. Partnership fit**

| # | Requirement | **Plain** | Intercom | Pylon | Zendesk | Evidence summary |
|---|---|---|---|---|---|---|
| 6.1 | Roadmap alignment / co-investment in agentic and config-as-code capability | **3** | 1 | 1 | 1 | Plain have strongest fit on vision and their support to us as a customer. |
| 6.2 | Account treatment at our scale (dedicated team, not self-serve/SMB-first) | **3** | 2 | 1 | 1 | Plain have shown most interest in partnership. We are still too small for Intercom or Pylon. |
| 6.3 | Implementation weight required | **2** | 2 | 2 | 1 | Would require build effort, but mostly similar. |
| | Sub-category score | **2.67** | 1.67 | 1.33 | 1.00 | |

**6b. Reliability**

| # | Requirement | **Plain** | Intercom | Pylon | Zendesk | Evidence summary |
|---|---|---|---|---|---|---|
| 6.4 | Uptime SLA (core ticketing) | **2** | 2 | 2 | 2 | Standard terms |
| 6.5 | Enterprise support SLA (human response, P1/P2) | **3** | 2 | 2 | 1 | Standard terms |
| 6.6 | Named account team / escalation chain | **3** | 3 | 3 | 2 | Standard terms |
| 6.9 | Vendor continuity risk (viable through 2030) | **1** | 1 | 1 | 2 | All three challengers carry continuity risk. Plain is runway to end 2028 on its own claim, pending investor diligence. |
| | Sub-category score | **2.25** | 2.00 | 2.00 | 1.75 | |

**Category score: Plain 2.46, Intercom 1.83, Pylon 1.67, Zendesk 1.38.**

### A7. Customer-facing experience (7%)

| # | Requirement | **Plain** | Intercom | Pylon | Zendesk | Evidence summary |
|---|---|---|---|---|---|---|
| 7.1 | Customer ticket portal | **2** | 2 | 2 | 2 | Mix of native and custom work needed on all |
| 7.3 | Account team thread visibility/reply | **2** | 1 | 2 | 1 | Plain and Pylon edge as they have native portal with some custom work. |
| | **Category score** | **2.00** | 1.50 | 2.00 | 1.50 | |

### A8. Pricing (3%)

| #   | Requirement                                                 | **Plain** | Intercom | Pylon | Zendesk | Evidence summary                                                                                                    |
| --- | ----------------------------------------------------------- | --------- | -------- | ----- | ------- | ------------------------------------------------------------------------------------------------------------------- |
| 8.1 | All-in cost at 500 agents (seats + required add-ons)        | **2**     | 1        | 1     | 2       | Plain is lowest cost vs others (don't need to have large AI bundles)                                                |
| 8.2 | Cost predictability (12-month model confidence)             | **2**     | 2        | 2     | 1       | Our scale will be predictable on seats & AI usage. AI token cost will be out of direct control and to be monitored. |
| 8.4 | Volume discount terms at 2027–2030 projected contact volume | **3**     | 3        | 3     | 2       | All will offer volume based discounts.                                                                              |
|     | **Category score**                                          | **2.33**  | 2.00     | 2.00  | 1.67    |                                                                                                                     |

## Appendix B: Plain POC results against the original 11 evaluation sections

The POC ran 27 July to end August 2026 against the RFI's original 11-section framing. The scorecard was restructured into the eight weighted criteria on 2026-09-18. Both views are kept: this table is what the POC was actually run against.

| Section | Outcome | Status |
|---|---|---|
| 1. Multi-channel entry points | Email, live chat, Slack/Teams, internal submission native and tested | Proven, except phone (API integration path) and enrichment (landed end of August) |
| 2. AI triage and classification | Auto labelling, language detection, urgency detection, external classification via API. No lock-in to native AI | Proven |
| 3. Routing and field logic | Tier, skill, regional and capacity-based routing tested. Priority-first assignment native | Proven, except SLA and business hours (September commitment) |
| 4. Agent workspace | Live data to agents, full API read/write, deployment without vendor involvement, Jira escalation, free viewer seats | Proven via customer cards, not the embedded iframe SDK originally assumed |
| 5. Data and permissions | Separate workspaces for B2B/B2C, custom roles for RBAC, seat-based scaling to 500+ | Proven |
| 6. Customer-facing experience | Help centre or headless portal on the API. AI transcripts on the thread timeline | Validated, not built in the POC |
| 7. Integrations | Jira and Salesforce native, Fin escalation validated via the Tines reference, knowledge sources sync automatically | Proven or referenced |
| 8. Analytics and data extract | Full GraphQL export today, Fivetran connector committed by end of 2026 | Partial. AHT measurement is an open gap |
| 9. Environment and config deployment | Sandbox mirrors production, promotion via config-as-code, drift detection tested cross-workspace | Proven |
| 10. Vendor reliability | Uptime SLA in enterprise contracts, named CSM on Frontier. Capitalised to end 2028, Series B planned January 2027 (23 September session) | Investor diligence pending |
| 11. Pricing | Seat-based plus platform fee, all features included, no add-on gating | Quote received |

This result is specific to Plain. It is proof that Plain clears the bar, not a comparative score against Intercom or Pylon. The comparative instrument is the scorecard in Appendix A.

**Source**: `plain-business-case-draft-v1.md`.

## Appendix C: Cost methodology and five-year model

**Seat assumptions** (indicative): 100 (2026), 130 (2027), 200 (2028), 320 (2029), 400 (2030).

**Modelled AI resolution rate**: 40% (2026), 50% (2027), 70% (2028), 80% (2029), 80% (2030).

| Year | Human-handled | Seats | Implied contacts per seat |
| ---- | ------------- | ----- | ------------------------- |
| 2026 | 36,029        | 100   | 360                       |
| 2027 | 80,158        | 130   | 617                       |
| 2028 | 122,483       | 200   | 612                       |
| 2029 | 225,702       | 320   | 705                       |
| 2030 | 430,960       | 400   | 1,077                     |

Implied throughput per seat triples over the period, from 360 to 1,077 contacts per seat.

| Year | Seats | Zendesk (seats) | Zendesk add-ons (unconfirmed) | **Plain**    | Intercom | Pylon    |
| ---- | ----- | --------------- | ----------------------------- | ------------ | -------- | -------- |
| 2026 | 100   | $278,640        | $40,000                       | **$166,800** | $193,200 | $228,000 |
| 2027 | 130   | $346,194        | $52,000                       | **$216,840** | $251,160 | $296,040 |
| 2028 | 200   | $503,820        | $80,000                       | **$333,972** | $386,400 | $454,800 |
| 2029 | 320   | $774,036        | $128,000                      | **$549,615** | $618,240 | $726,960 |
| 2030 | 400   | $954,180        | $160,000                      | **$713,844** | $772,800 | $908,400 |

Prices exclude discounting. Zendesk seat costs come from the signed 24-month order form (100 agent seats, GBP, signed 27 June 2025).

**Plain AI credits**: 5 credits per ticket at $0.03, against a flat 600k-credit annual pool included in the licence. Overage: $0 (2026), $0 (2027), $372 (2028), $15,855 (2029), $46,644 (2030). Under 1% of Plain's total by 2030.

**Pylon pricing**: Enterprise tier at $139 per seat per month, annual billing, 7-seat minimum, which is identical to Plain's Frontier price. Only Enterprise carries the features our scale needs. The column adds Pylon's AI Assistants add-on ($50 per seat per month) plus the $1,200 annual floor for Pylon's AI Agents product. That floor is almost certainly a severe understatement: at 2030 volume a usage-based autonomous resolution layer would run into seven figures. We would not run it, since Fin is our AI layer regardless of case platform, so this is a bounding exercise. Do not read $908,400 as Pylon's true AI-inclusive 2030 cost. Account Intelligence Premium ($10 per customer account per month) is not modelled, since it does not map to a requirement.

## Appendix D: Reference calls and vendor evidence

Full notes, per-call, with evidence tiers: `04-active-work/research/support-platform-assessment-customer-references.md`. That file is the live home for this evidence and the place to add any new call.

| Source                                     | Vendor   | Tier                  | What it contributes                                                                                                                                                                       |
| ------------------------------------------ | -------- | --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Vercel** (2026-09-18, Will Viles)        | Plain    | Reference call we ran | Headless model proven in production, full GraphQL SDK, one operator for ~60 agents. Warns on roadmap slippage, self-built tracker linking, workspace-level rather than granular RBAC      |
| **Fyxer** (Sept 2026, Yannis)              | Plain    | Reference call we ran | Left the full Intercom suite over its user-to-company schema limit. Plain's many-to-many model and custom app building solved it. Warns the agent UI is too busy                          |
| **Tines**                                  | Plain    | Reference call we ran | Fin-to-Plain escalation running in production, integration architecture validated with us directly                                                                                        |
| **Zilch** (Sept 2026)                      | Intercom | Reference call we ran | Intercom can deliver a strong partnership, at ~250 BPO agents plus 40 internal staff and hundreds of thousands of contacts a month. Warns it cannot group team members into organisations |
| Intercom vendor call (Sept 2026)           | Intercom | Vendor call           | Strong ticketing and native connectors. Copilot is a black box, config is UI-only, object model is restrictive                                                                            |
| `04-active-work/research/evidence/plain-checkout-proof-points.pdf` | Plain    | Vendor marketing      | Nothing independent. Deliberately excluded from the core slides. SpaceX AI, Sanity, Yapily, Sourcegraph and others                                                                        |

**Three cross-cutting findings worth knowing before questions.**

1. **Two independent Plain customers both had to self-build tracker linking**, on different trackers by different mechanisms. This contradicts our own POC's "native" reading and is the one unresolved disagreement in the evidence base (Slide 15, flagged).
2. **Neither Plain nor Intercom has a native granular data wall.** Plain splits workspaces, Intercom assigns individuals to Inboxes. It is not a differentiator between them.
3. **No Plain reference we have runs above ~60 agents**, against our 500-agent target. This is the biggest gap in the evidence base, and the reason for the standing ask to find a larger Plain reference before signature.

**Pylon, re-verified 2026-09-21.** Fyxer's February 2026 finding that Pylon was closed to third-party AI agents is out of date. Pylon now ships a "Bring Your Own Agent" capability via Skills, webhooks, API and MCP. Do not present the February finding as current. The case against Pylon rests on no config-as-code, Slack-first design and the wrong shape for multi-segment routing.

## Appendix E: Current Zendesk configuration inventory

318 triggers (23 of 47 trigger categories unused), 171 distinct tags, ~200 macros carrying dead weight, a 105-field form with 108 conditional show/hide rules, 500+ configuration items in total. Third-party stack: Salto (config-as-code and audit trail), SweetHawk (approval flows), Zendesk sandbox fee, roughly $130,000 a year combined.

Change speed: 1 to 2 days for a simple change, 2+ weeks for a complex one, all manual UI work. A recent taxonomy change took weeks of admin time. Integrations: the Jira app was deprecated and never replaced, Salesforce needed a custom BigQuery build, and knowledge content cannot sync in from an external source. Vendor: feature requests go into a backlog with no visibility or timeline. These moved here from Slide 6 when that slide was reframed around agent and merchant experience.

Detail: `04-active-work/research/zendesk-current-config-flow-map.md`, sourced from the Salto IaC repo.

## Appendix F: Decision context and prior analysis

- Reference calls and vendor calls, in full, with evidence tiers: `04-active-work/research/support-platform-assessment-customer-references.md`
- Archived RFC with the full Build / Buy / Keep evaluation, the scored candidate matrix, the written recommendation and the rejection reasoning for Zendesk, Intercom, Pylon and Build: `05-archive/2026/investigations/zendesk-platform-decision-rfc.md`. Archived 2026-09-22 once the decision was made
- Operations business case with POC detail: `04-active-work/research/plain-business-case-draft-v1.md`
- Zendesk market and AI strategy research: `05-archive/2026/investigations/Zendesk Viability_ AI, Pricing, Market.md`
- Target architecture: `04-active-work/meeting-notes/2026-09/2026-09-15-plain-vision-architecture.md` and `04-active-work/meeting-notes/2026-08/2026-08-20-fin-in-plain-world.md`
- Multi-team routing requirements shared with both vendors: `04-active-work/research/multi-team-routing-overview-plain-intercom.md`
- Roadmap anchor: `2026 deliverables.md`, Help Desk Platform Evaluation (Q3 discovery and POC, Q4 decision and approval)

## Appendix G: Open items before this is presented

**Source rule**: the scorecard holds the scores and the references file holds the call evidence. Change a number there first, then update this deck. Never the other way round.

1. **Investor diligence on Plain's funding.** Plain says it is capitalised to end 2028 and plans a Series B in January 2027, and has offered investor access. Hold that call before contract signature. If it confirms the position, scorecard 6.9 rises from 1 to 2 and Plain's total from 2.44 to 2.45. Owner: Charlie.
2. **Plain's September commitments.** The SLA model was due in the first week of September and business hours by 14 September. Both dates have passed. Confirm they shipped and mark them shipped on Slide 11. If either slipped, the roadmap-slippage risk on Slide 15 has materialised and the slide should say so.
3. **Zendesk add-on line ($40,000 in 2026, rising to $160,000).** Confirm what it covers before it appears on a slide. It is excluded from Slide 14 until then.
4. **Intercom scoring pass.** Confirm it is formally closed, since Slide 9 presents 1.94 as final.
5. **Pricing between 130 and 400 seats.** The Plain and Intercom quotes cover 100 seats, so every 2027 to 2030 figure is modelled. Get volume pricing before any forward figure is presented as contracted.
6. **Modelled AI resolution rate.** Appendix C models 40% for 2026. Actual overall AI resolution is 16% to 21% as of September 2026, and the Fin PRD targets 80% involvement at 70% resolution by end 2026. Reconcile the seat model to one number.
7. **Operational baselines.** SLA miss rate, uneven pickup, wait times, reopen rates, and the measured duration of the recent taxonomy change. Slides 6 and 13 use descriptions and effort ranges until these land, and the before-and-after claim on Slide 13 stays unmeasured.
8. **Slide 8 assumptions.** Confirm the team size (5 engineers, 1 EM, 2 admins) against current headcount after two admin departures. Get Finance to check the $200,000 fully-loaded engineer estimate, since it is now load-bearing.
9. **A Plain reference above 200 agents.** Every reference we have spoken to runs about 60 agents, against our 400 modelled seats in 2030. Plain's own list cites SpaceX AI at 162 seats, the largest it claims (Appendix J), so ask Plain to introduce them. Owner: Charlie, before contract signature.
10. **Ticket transfer design.** The largest unresolved functional gap. Requirements are with Plain via the multi-team routing document. A Q4 design gate, not a procurement blocker.
11. **Plain Slack app security approval.** Stalled on a Jira ticket. A QA Slack workspace is enough for testing. Unblock before the build.
12. **Relationship to the Operations business case.** Decide whether this deck runs alongside `plain-business-case-draft-v1.md` or supersedes it before both reach the same people.
13. **Zendesk six-month extension.** Deferred pending procurement advice on when to notify Zendesk. Not on Slide 16. Decide whether it stays out.
14. **Roadmap date.** `2026 deliverables.md` scopes the decision to Q4. This deck asks for approval by 30 September. Either update the deliverable, or present September as procurement entry ahead of a formal Q4 decision gate.

## Appendix H: Anticipated questions

**"Does a total that mixes three scoring rubrics mean anything?"**
Yes, and it has been tested. Six categories score build type, partnership scores how well a claim is verified, and pricing scores how certain the cost is. Drop partnership and pricing entirely and re-weight the remaining 87%: Plain 2.44, Intercom 1.95, Pylon 1.83, Zendesk 1.54. Same order, and Plain still leads both 20% categories. The recommendation does not rest on the two softer rubrics.

**"Plain's partnership score is high. Isn't that just a sales team being attentive?"**
No. Under the partnership rubric, a vendor's own claim scores 1. A 3 requires commitments we verified, named and dated ourselves. Plain's 2.67 on partnership fit comes from our own reference calls and three gap commitments made in writing with dates. The rubric applies to Plain too: its funding claim scores 1 until investors confirm it. Zendesk's 1.38 is mostly unverified claim or negative signal, and the rubric's own example of a zero is a feature request sitting in a backlog with no timeline, which is what we get from Zendesk today.

**"Plain is less mature than Zendesk. Why take the risk?"**
Plain's own view is that prospects decline for two reasons: a feature they need is missing and cannot arrive in time, or switching looks worse than staying with a more mature vendor. Neither applies here. Our three required gaps were committed in writing with dates, and the POC tested the rest. Staying is not the safe option: Zendesk has closed off third-party AI (Slide 5) and its gaps already cost us in bolt-ons and manual work (Slide 6). Source: `04-active-work/meeting-notes/2026-09/2026-09-23-plain-ceo-cpo-funding-and-strategy.md`.

**"Is pricing really only worth 3%?"**
The pricing category scores how certain a cost is, not how large it is. Zendesk scores 1.67 because of the unresolved automated resolution fee and an add-on line we cannot yet identify. Cost level is on Slide 14, where seat prices are close across all four vendors.

**"Have we done the due diligence we did before moving from Salesforce to Zendesk?"**
More. Weights were published before any vendor was scored. Every score carries a line of evidence and a named evidence tier. Plain ran a four-week POC across engineering, product and support ops. We ran our own reference calls rather than taking vendor-supplied ones, and recorded the negatives. Three gaps were committed in writing, with dates, before any contract. And we are not lifting and shifting the Zendesk build, since much of it exists to work around Zendesk.

**"Why not build it ourselves? Uber did."**
Uber did, at a scale more than 15 times our 2030 peak. It started on Zendesk in 2010, while it was launching city by city, and later built its own support platform (more than 30 back-end services) once it was handling hundreds of thousands of tickets a day across 400+ cities. On top of that it built COTA, an ML system that helps resolve over 90% of inbound tickets and saves "tens of millions of dollars every year", developed by four dedicated teams. We handle about 165 contacts a day today and about 5,900 at our 2030 peak. Uber is the evidence for the rule on Slide 8: buy while volume is small, build once volume makes a dedicated team cheaper than the vendor. Sources: Uber Engineering, ["Architecting Uber Support with Customer Obsession Engineering"](https://www.uber.com/en-IN/blog/customer-obsession-engineering/) and ["COTA"](https://www.uber.com/blog/cota/)  ·  Zendesk, ["Uber customer story"](https://www.zendesk.com/customer/uber/).

**"Vercel's results look strong. Where do the numbers come from?"**
Only use what our own call supports. The "first response time down 30%, 67% Enterprise, 78% Pro" figures come from Plain's own marketing material (`04-active-work/research/evidence/plain-checkout-proof-points.pdf`), not from our Vercel call, and were removed from Slide 11. The "19% more tickets per agent" figure appears in both the business case and that same marketing file, so its independent source is unconfirmed. Full call notes and evidence tiers: `04-active-work/research/support-platform-assessment-customer-references.md`.

**"What if Fin becomes the constraint?"**
The architecture on Slide 7 is designed for it. Customer identity, taxonomy and AI invocation sit in a layer we own, and a gateway mirrors Fin conversations into Plain threads. Replacing Fin later is a change to one block in that layer, not another platform migration.

## Appendix I: Full risk register

Slide 15 shows the six risks that matter for the decision. This is the full register, including the Zendesk-side cost exposure and the two lower risks left off the slide (data segregation and agent interface polish).

| Risk | Evidence | Mitigation | Status |
|---|---|---|---|
| **Vendor viability.** Plain is a smaller company than the incumbent. Continuity is the one dimension where Zendesk scores best (2.00, against 1.00 for Intercom, Pylon and Plain, where 1 means vendor claim only) | 23 September session: capitalised to end 2028, Series B planned January 2027, investor access offered. Runway alone does not reach the 2030 requirement | Investor diligence before signature. Continuity and data-export protections in the contract. Full GraphQL export keeps our data portable | Flagged |
| **AR fee exposure on Zendesk** | $1.50 to $2.00 per resolution, mechanism non-auditable | Written answer requested from the Zendesk account team. Charlie owns the chase | **Open, answer needed by 30 September 2026** |
| **Roadmap slippage** | Vercel: 4 months quoted became 8 | API-first means we build around gaps ourselves. Design-partner status. Three dated commitments already tracked | Mitigated |
| **Self-build burden on integrations** | Vercel and Fyxer both report Jira/Linear linking needs self-building, against the POC's "native" reading | Conflict flagged for resolution before contract. Effort sized in the build phase | Flagged |
| **Handle-time measurement** | Plain scores 1.00 on AHT against Intercom's 3.00. Plain has a feature request open, no native metric | Cost per contact is a north star metric, so this cannot stay open. Metric to be co-designed against Plain's events API, and the requirement goes into the contract | Flagged |
| **Data segregation model** | Vercel reports workspaces rather than granular RBAC | Two-workspace B2B/B2C split validated in POC. Confirm our own requirement rather than copying Vercel's | Validated for our case |
| **Agent UI polish** | Fyxer: interface "too busy", too many clicks | Agent experience is weighted 20% and Plain still leads it. Measured again in the build phase | Accepted |
| **Loss of Zendesk admin depth** | Two admins leaving during the exit window | Config-as-code plus AI-assisted administration cut the admin dependency. Backfill in market as a support systems administrator | Mitigated |
| **Migration execution** | Nothing signed off as of today. Procurement is the critical path | No lift-and-shift. API channels migrate first, then a single email cutover. Parallel run against Zendesk before the June 2027 renewal | Managed |

## Appendix J: Who are Plain?

**Visual**: one slide, a two-column profile. Left: the company in six facts. Right: "What the numbers say about scale" with the reference-customer table. Footnote the evidence tier on every block. Keep it factual and unpromotional, since this audience will read it as a due diligence summary.

**Plain in six facts**

| | |
|---|---|
| **What it is** | A B2B customer support platform that brings Slack, Microsoft Teams, Discord, email, chat and in-app conversations into one workspace, built API-first for technical teams |
| **Founders** | Simon Rohrbach and Matt Vagni, who both helped scale Deliveroo from 10 to 2,000 employees. Simon led its content, research and design team, Matt its design systems and internal tooling |
| **Where** | London. A first US office, in San Francisco, was planned with the Series A |
| **Funding** | $6M seed (co-led by Index Ventures) and a $15M Series A in February 2025, led by Battery Ventures with Index Ventures and Connect Ventures. About $21M raised in total, as reported by company databases |
| **Runway** | Capitalised to the end of 2028. Series B planned for January 2027. Investor access offered for due diligence (23 September session with Plain's CEO and CPO) |
| **Size** | Reported at 11 to 50 employees by company databases. This figure is third-party and may be out of date |

**What Plain says it is for** (23 September session). Technically capable businesses that build and control their own support experience. Longer term, less technical markets, which Plain expects to be easier to reach by solving the technical case first. Its stated edge is API-first and config as code, plus orchestration that lets AI agents work through batches of tickets, with customers plugging in their own agents. Plain says prospects decline when a feature they need is missing and cannot arrive in time, or when switching looks worse than staying with a more mature vendor.

**What the numbers say about scale.** Plain's own customer list (vendor-supplied, not verified by us) gives the largest deployments it can point to:

| Customer | Seats ("members") | Tickets a year | Replaced |
|---|---|---|---|
| SpaceX AI | 162 | 500k+ | Intercom |
| n8n | 75 | 75k+ | Zammad |
| Vercel | 63 | 100k+ | Salesforce |
| Tines | 35 | 60k | Zendesk |
| Fyxer | 20 | 96k | Intercom |
| **Checkout.com (modelled)** | **100 in 2026, 400 in 2030** | **60k in 2026, 2.15m in 2030** | **Zendesk** |

Vercel's 63 matches the roughly 60 agents Will Viles gave us on our own call, which supports reading "members" as agent seats. The table matters for one reason: our 2030 volume is about four times the largest ticket count Plain cites, and our modelled seats are about two and a half times its largest seat count. AI resolution at 80% brings human-handled volume to 431k a year, which is inside what Plain cites, but the seat and volume curve is ahead of anything it has shown us.

**What we do not know about Plain**

- Revenue, growth rate, burn and gross margin.
- Customer count and churn.
- Current headcount, and how many are engineers.
- Whether a customer runs it at 200 or more seats. The SpaceX AI figure is vendor-claimed and we have not spoken to them.

These are the questions for investor diligence (Appendix G item 1) and for a larger reference call (item 9).

**Evidence tiers**: funding and founders are public press coverage. Runway and positioning are Plain's own statements to us. The customer table is Plain-supplied marketing material. Size is a third-party database estimate.

**Source**: TechCrunch, ["Plain pulls in $15M to aggregate B2B customer services chats into one platform"](https://techcrunch.com/2025/02/14/plain-pulls-in-15m-to-agregate-b2b-customer-services-chats-into-one-platform/), 14 February 2025  ·  Tech.eu, ["Plain, founded by ex-Deliveroo employees, raises $15M Series A"](https://tech.eu/2025/02/11/plain-raises-15m-series-a/), 11 February 2025  ·  Plain, ["We've raised a $15m Series A"](https://www.plain.com/blog/we-ve-raised-a-15m-series-a)  ·  Index Ventures, ["Plain raises $15M Series A"](https://www.indexventures.com/perspectives/plain-raises-15m-series-a-to-build-the-future-of-collaborative-b2b-support/)  ·  Crunchbase and Tracxn company profiles (total funding, headcount)  ·  `04-active-work/meeting-notes/2026-09/2026-09-23-plain-ceo-cpo-funding-and-strategy.md`  ·  `04-active-work/research/evidence/plain-checkout-proof-points.pdf` (vendor material)  ·  `04-active-work/research/support-platform-assessment-customer-references.md`.

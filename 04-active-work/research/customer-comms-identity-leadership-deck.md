# Customer Data & Unified Communications — Leadership Decision Deck

**Audience:** CPO, CCO, COO
**Ask:** Approve two new product teams — Customer Data and Unified Communications
**Decision needed:** Funding and headcount to stand up both teams from 2027 (scaling foundations for 2030)
**No $ business case in this version.** Problem proof + solution shape + resourcing ask.

Sources: `customer-comms-identity-problem-statement.md` (qualitative) + Quantitative Data Pulls sheet (Imran Khan et al.).

---

## The narrative in one line

> Today this is invisible because account managers absorb it by hand. SMB and Platforms scaling from 2027 to 2030 remove that buffer, and the cost lands as churn, CSAT decline, regulatory exposure, and ~$1.25M/year of avoidable coordination cost. (B2C consumer is a possible further driver, TBC — distinct CRM.)

---

## Proposed deck structure (12 slides)

### Slide 1 — Title + the ask
"Customer Data & Unified Communications — a decision on two teams."
One sentence: Checkout has no single view of who a customer is or what we've told them. It is masked by manual AM effort today and breaks at 2030 scale. We are asking to fund two teams to fix it.

**Evidence to reference or pull onto the slide:**
- **17.8%** of Care tickets touch another team — roughly 1 in 6, every month
- **CSAT falls 15 points** (85% → 70%) when a ticket leaves Care
- **30%** of inbound contacts match nothing in Salesforce or Dashboard
- Up to **3 hours** to compile one customer's comms history for a complaint

These four numbers cover the two failure modes (fragmented identity, fragmented comms) and the cost (CSAT, regulatory). They're each from different data sources, which signals breadth. Use them as a 2×2 stat strip beneath the title sentence — not the main focus, but enough that the ask is grounded from the first slide.

**Visual:** near-blank slide, one bold sentence centred. No chart. The restraint signals "this is a decision, not a status update." Optional: faint background montage of the real ticket/email screenshots used later, low opacity.

### Slide 2 — The problem in one picture
Two infrastructure gaps, everything else is a symptom:
- **No unified customer identity** — same merchant exists as different records across 6 systems (Salesforce, Zendesk, OKTA, Genesis, Pardot, Citadel), with no joins.
- **No unified communications record** — no shared log of what was sent, by whom, on which channel. No team sees the full picture.

**Visual:** one customer icon in the centre, six labelled system silos (Salesforce, Zendesk, OKTA, Genesis, Pardot, Citadel) scattered around it with no connecting lines. Greyed-out dotted lines where the joins *should* be. The absence of lines is the whole point — let the white space carry it. Build this so the connecting lines animate in on Slide 9 (the solution) for a visual bookend.

### Slide 3 — Problem today: internal fragmentation (the numbers)
Lead with the hard data. All from Zendesk, ~50k tickets, last 12 months.

| Metric | Finding |
|---|---|
| Tickets touching another team (L3) | **17.8%** avg (range 14–22%); ~80% of that is internal teams |
| Teams a cross-team ticket touches | avg **1.12**; worst case **6** dependent teams on one ticket |
| Reopen rate, cross-team vs Care-only | **39.4% vs 21.7%** — nearly 2× more likely to be reopened |
| Same-issue recontact within 7 days | **4.0%** of resolved tickets (range 2.9–5.0%) |
| Cross-team tickets identified by LLM | **1,025** concrete examples pulled |

Takeaway: when a ticket leaves Care, it is twice as likely to fail the first time.

**Visual:** don't show the whole table. Lead with one hero stat — **39.4% vs 21.7%** as two bars side by side (cross-team reopen vs Care-only), the cross-team bar in alert red. Drop the other metrics into a small supporting strip beneath. One number the eye lands on, the rest as context.

### Slide 4 — Problem today: the customer feels it
- **CSAT falls from ~85% to ~70%** when a ticket leaves Care — a 15-point absolute drop. Biggest drop: Disputes and Engineering.
- NPS verbatims across 4 waves (H1 2024–H2 2025), no improvement trend. Detractors ask for a single point of contact; Promoters praise a named individual — the coping mechanism is a person, not a system.
- Live case: **PayNearMe** — 5 teams, 40 days, no resolution, merchant gave the same reference numbers repeatedly. AM became de facto coordinator with no tooling.

**Merchant verbatims (live tickets — use as on-slide callouts):**
> "We have received the email titled '01038019: Periodic Reviews' from Checkout's Compliance team... Could you please clarify to whom exactly this information should be sent?"
*— merchant receives a Compliance request, doesn't know the route, defaults to Support.*

> "Hi Dispute Team, can we have your urgent update please?" / "May we get the update of these two cases? The dispute status has not been updated."
*— merchant manually chasing status across teams with no single view of their case.*

Lead with the first quote: it's the merchant literally asking "who do I send this to?" — sharper than any percentage.

**Visual:** the real ticket/email screenshots as the hero (lightly redacted), pinned like evidence with the key line highlighted. The CSAT 85→70 drop as a small slope line in the corner. Show the merchant's actual words, don't paraphrase them into a bullet — authenticity is the persuasion here.

### Slide 5 — Problem today: identity is genuinely broken
Of all inbound Zendesk contacts, only half can be matched to a Dashboard record:
- **50%** have a Dashboard record
- **20%** exist in Salesforce only — known to Checkout, but no self-serve access
- **30%** match nothing — unknown identity, cannot authenticate or reach

~8% of dashboard users are group/shared inboxes (info@, ops@) — cannot identify or reach a person even when a record exists. Offline contact lists live in Google Sheets (Marketing/RFI); Genesis data captured at onboarding and never updated.

**Visual:** a single stacked bar or three-segment donut — 50% Dashboard (solid), 20% Salesforce-only (mid-tone), 30% gap (red/empty). The 30% gap is the hero; the 20% Salesforce-only segment matters because those people *are* known to Checkout but have no self-serve path — label it "known, but unreachable via self-serve." One chart, three segments, one takeaway.

### Slide 6 — Problem today: the regulatory and hidden-cost tail
- Compiling a full cross-team comms history for one complaint takes **up to 3 hours** today (Legal/Compliance).
- AMs are the manual bridge: ~monthly per AM, "messy, lots of back and forth." Contact data updates flow through the AM by hand; merchants have no self-serve path.
- Compliance risk now: AMs subscribe contacts to comms without explicit consent (Account Manager, Tier 4).
- **Document fragmentation:** Periodic Reviews cannot locate merchant documents held by other teams. Five-week thread, four internal teams (AM, Periodic Reviews, Due Diligence, US Underwriting), merchant asked to re-provide documents Checkout already had. Account Manager: *"All of PayNearMe's documents, licenses, and financials should be located in a central repository where the underwriting, due diligence, and periodic review teams can access them."* Full thread in `customer-comms-identity-problem-statement.md`.

**Visual:** a single clock/stopwatch graphic anchored on **"up to 3 hours to reconstruct one customer's comms history."** That's the line that lands with a COO/CCO. The AM-bridge and consent points sit as two supporting icons beneath. Keep it to one dominant visual.

### Slide 7 — How this gets worse (the inflection)
From 2027 the changes that remove the AM buffer begin, and scale through 2030:

| Change | Why the buffer disappears |
|---|---|
| **SMB expansion (from 2027)** | No account managers at SMB volume. Wrong-contact comms = churn, not a recoverable escalation. |
| **Platforms scaling (2027→2030)** | ISV→Platform-merchant hierarchy needs routing logic that does not exist. Wrong-tier notice = operational failure. |
| **Regulatory exposure (grows with volume)** | Complaint records already take hours to compile across teams; this scales badly. B2C consumer (TBC, distinct CRM) would add Consumer Duty + DISP + GDPR-erasure obligations on top. |

**Visual:** a timeline/horizon line with "today" on the left, SMB starting 2027, Platforms scaling, both scaled by 2030. Show the AM "buffer" as a thinning band that runs out as volume grows. The metaphor — the safety net disappearing — is the message.

### Slide 8 — How this gets worse (the projection)
Same broken process, much larger volume. Numbers from support-contact forecasting (Platforms P&L, Q1 2026).

| Projection | Today | 2027 (SMB starts) | 2030 (scaled) |
|---|---|---|---|
| Cross-team handoff tickets/yr | ~7k | **~8.75k** | **~71k** |
| Incremental coordination cost/yr | — | **~$154K** | **~$1.25M** |
| Systems to compile one comms history | 6 | 7 | 8 |

Cross-team coordination volume grows **~10× today→2030** (~8× between 2027 and 2030) with no change to the broken process. Takeaway: manual coordination is not staffable at this volume. The cost converts to SMB churn, regulatory exposure, and pure cost of support.

**Cost basis (state on slide):** ~$17.60 incremental coordination/re-open cost per cross-team ticket. This is the *extra* cost of cross-team friction, not the fully-loaded ~$40/contact handling cost. Define it explicitly or a COO will discount the figure.

**Visual:** a steep growth bar/area chart of cross-team tickets ~7k → 8.75k → 71k, with the flat "AM coordination capacity" line staying low and the gap shaded as the "unstaffable gap." The 8,750→71K jump in three years is the scary part — annotate it.

### Slide 9 — The solution direction
Direction, not design. How we build it (system of record, build vs extend) is for the scoping phase, not this decision.

**1. Customer record**
A central source where all customer information is stored and linked from other systems. Becomes the source of truth for customer data management across Checkout.
- Addresses the 30–35% unmatched contacts, shared inboxes, offline Google Sheets, and stale Genesis data.

**2. Communications — built on the customer record**
Two halves:
- **Merchant communications** — linked to the customer record: self-serve contact management, preference centre, comms that reach the right person.
- **Internal workflows** — a single thread for a customer query regardless of how many systems or teams it transfers across. Customers trace their request in one place; Operations get accurate reporting and SLA management. Two options to explore in scoping:
  - *Option 1 — unified service:* a layer that handles transfers and links a query across the systems teams already use. Teams keep their own tools.
  - *Option 2 — single platform:* consolidate all ops teams onto one platform. Heavier change, but removes the cross-system problem at source.

**Visual:** the inverse of Slide 2 — the same six systems, now connected through a central **customer record** layer, with merchant comms and internal workflows as a layer on top feeding Care/Disputes/Compliance/Marketing. Reuse Slide 2's exact layout so the lines literally "complete" the picture. A layer-cake / stacked-foundation diagram: record at the base, comms above it.

### Slide 10 — Why two teams, not one
- Distinct scopes. One team owns the customer record (the foundation). The other owns what's built on it — merchant comms and internal-workflow threading.
- The comms work builds on the customer record, so they must run in parallel from 2027, not sequentially.
- The combined scope is too large for one team to deliver scaling foundations by 2030.

**Visual:** two team "swim-lane" cards side by side — Customer Data (foundation) and Unified Communications (built on top) — with a small parallel-tracks Gantt strip beneath showing both starting 2027 and running to 2030. Visually reinforces "parallel, not sequential."

### Slide 11 — The ask
- Approve **2 product teams** (Customer Data, Unified Communications).
- Headcount (rough, for debate): **1 PM + 4–6 engineers + shared design/data per team**. One PM may cover both initially.
- Start in 2027 to build the scaling foundations ready for 2030.
- This is foundational infrastructure for SMB, Platforms, and Enterprise — not a Care/Ops-only fix. (Consumer possibly, TBC — distinct CRM.)

**Visual:** two clean team cards (name, one-line mandate, headcount shape) with a 2027→2030 readiness arrow underneath. Keep it spare and confident — this is the slide you want on screen while they decide, so no clutter competing with the ask.

### Slide 12 — Decision + next steps
- Decision requested today: approve funding for both teams.
- If yes: scoping phase to define MVP, system-of-record decisions, and 2030 readiness milestones.
- Owner mapping and the live single-merchant comms audit (Oliver) completed as the proof exhibit.

**Visual:** a simple decision box ("Approve / Approve with conditions / Defer") plus a short post-decision timeline (scoping → milestones). Make the ask unambiguous and give them an explicit thing to say yes to.

---

## Unanswered questions leadership will ask

**On the numbers**
1. ~~Base volume~~ — RESOLVED. Projection now uses support-contact forecasting (Platforms P&L, Q1 2026): ~7k cross-team tickets today → ~8.75k (2027) → ~71k (2030); incremental cost ~$154K → ~$1.25M. Headline cross-team rate (17.8%) measured on ~50k tickets (precise: 59,961, Care Form / L2 / Dispatch). State the cost basis (~$17.60/cross-team ticket) on the slide.
2. ~~CSAT~~ — RESOLVED. Absolute: falls ~85% → ~70% (15-point drop) when leaving Care.
3. Reopen ≠ cost. Can we convert the 2× reopen rate into agent-hours or $ even roughly? They will want the cost of the problem even without a full business case.

**On the gaps (sheet items not yet complete)**
4. Operational/compliance comms bounce rate (Tim Win, not started) — the 0.5% figure is marketing only; the regulatory risk lives in operational comms.
5. % of B2C complaints requiring cross-team history — the core regulatory-exposure number is still blank.
6. Single-merchant live comms audit (Oliver, not started) — this is flagged as the single most powerful exhibit. Worth completing before the meeting.
7. Volume of tickets explicitly naming another team ("I emailed Disputes") — in progress; would directly evidence merchant-side fragmentation.

**On the solution**
8. What is the system of record for identity — extend Dashboard/OKTA, Salesforce, or build new? They will push on build-vs-extend.
9. How does this relate to the preference centre Amanda/Irene are already building? Risk of "isn't this already being done?" — answer: preference centre is a UI on top; it does not solve where records live or how they stay current.
10. Where does this sit organisationally — Care product, central platform, or data? Two teams crossing Care/Marketing/Compliance/Data needs a clear home.
11. Dependency and sequencing — can Comms start before Identity is done, or is it strictly serial? Affects whether both teams are funded now or staggered.

**On the ask**
12. Exact headcount and shape per team (PM/eng/design/data).
13. What is the cost of *not* doing this — the implicit business case. Have a churn/Brexit-precedent number ready (Thomas: large migrations cause churn from uncontactable cohorts).

---

# Appendix — depth on demand

*Not for the main flow. Each slide answers a specific "show me the evidence" or "how do you know" challenge. Pull the relevant one only if asked.*

**Visual approach for appendix:** dense and reference-style is fine here — full tables, raw quote cards, the complete PayNearMe timeline. These are deliberately text-heavy because they exist to withstand scrutiny, not to persuade. Different visual register from the main flow on purpose.

### A1 — Methodology, sources & confidence
- **Quantitative:** Zendesk, ~50k tickets (59,961 across Care Form / L2 / Dispatch), last 12 months, cross-referenced with Salesforce, OKTA/User Management, Pardot. Forward projections from support-contact forecasting (Platforms P&L, Q1 2026). Owners: Imran Khan, Jiro Farah, Charlie Wildish.
- **Qualitative:** 4 internal staff interviews (2021–2024); 3 June 2026 discovery conversations (Account Manager, Account Manager T4, Marketing comms lead); Periodic Reviews pain-point log (17 items); live tickets; NPS Waves 4–7 (H1 2024–H2 2025).
- **Robust vs. directional:** ticket %s, CSAT delta and identity-match %s are measured; AM-time and complaint-compile-time are practitioner estimates, flagged as such.

### A2 — Full quantitative findings + the reopen definition
| Metric | Finding |
|---|---|
| Tickets touching another team | 17.8% avg (14–22%); ~80% internal |
| Dependent teams per cross-team ticket | avg 1.12; 89% → 1, 9% → 2, 2% → 3+; worst case 6 |
| Reopen rate, cross-team vs Care-only | 39.4% vs 21.7% (≈2×) |
| Same-issue recontact ≤7 days | 4.0% (2.9–5.0%) |
| CSAT when ticket leaves Care | ~85% → ~70% (15pt drop); worst Disputes/Eng |
| Contacts unmatched to SF/Dashboard | 30–35% week on week |
| Contacts with a Dashboard record | only 50% |
| Dashboard users on shared/group emails | ~8% |
| Cross-team tickets identified via LLM | 1,025 |
| Time to compile one complaint's comms history | up to 3 hours |

**Defending the reopen stat:** a *reopen* is the same ticket going solved → open → solved (the first answer was wrong); a *recontact* is a new ticket ≤7 days. The cross-team gap is driven by reopens, not recontacts. Cleaning applied: requester cap ≤50/mo, >85%-recontact exclusion (removes batch senders), template/transaction filter.

### A3 — Identity & comms infrastructure today
- 30–35% of inbound contacts match no SF/Dashboard record; only 50% have a Dashboard record; ~8% are shared inboxes (info@, ops@).
- Offline contact lists in Google Sheets (Marketing/RFI); Genesis data captured at onboarding, never updated, synced to nothing.
- "Unified" contact list is a hand-built Coefficient merge (Looker + Salesforce) run each morning — the Looker feed broke in a BigQuery migration and has been stale for weeks.
- No robust primary identifier (email changes/duplicates). Preference centre in progress (Amanda/Irene) but it's a UI layer — *"no one's looking at centralised contacts."*

### A4 — The evidence in their own words
- **Agent:** *"Mark would be completely unaware… I wouldn't even know what's going on."* / *"I'm literally jumping into Zendesk, Freshservice, Emails… then put it back into Zendesk."* (L2 Auth Care Agent)
- **Merchant:** *"Could you please clarify to whom exactly this information should be sent?"* (received a Compliance request, came to Support) / *"Hi Dispute Team, can we have your urgent update please?"*
- **AM:** *"I don't always have the right place to put that knowledge… it just lives in my head."* (Account Manager) / *"I'm just getting emails saying my ticket is closed. I'm not sure what's happening."* (merchant, via Account Manager)
- **Marketing:** *"SMB is the problem one… every migration we get a big amount of churn from customers we just can't contact."* (Thomas, Brexit precedent)
- **Live case — PayNearMe (transaction dispute):** 5 teams, 40 days, no resolution; internal-only handoff left the merchant with no update for 3 weeks; AM became de facto coordinator. Full timeline in `customer-comms-identity-problem-statement.md`.
- **Live case — PayNearMe (Periodic Review):** Periodic Reviews couldn't locate merchant licenses held across CRB Shared Drive, US underwriting folders, and merchant-supplied storage. Five weeks, four internal teams (AM, Periodic Reviews, Due Diligence, US Underwriting). Merchant re-asked for documents Checkout already had. AM coordinated the search. Account Manager: *"All of PayNearMe's documents, licenses, and financials should be located in a central repository where the underwriting, due diligence, and periodic review teams can access them."*

### A5 — Solution options & open data
- **Internal-workflow build (deferred to scoping):** Option 1 — a unified service linking queries across existing tools (lighter, ongoing integration). Option 2 — consolidate ops teams onto one platform (heavier migration, removes the problem at source). Both depend on the customer record.
- **Data still in flight:** operational/compliance bounce rate (not started — regulatory risk lives here, not the 0.5% marketing figure); % of B2C complaints needing cross-team history (blank — core regulatory number); single-merchant live comms audit (not started — most powerful exhibit); tickets naming another team + AM-time quantification (in progress).

# Merchant Care Vision 2030 — Strategy Scoping Document

**Owner**: Charlie Wildish
**Status**: In progress — gathering inputs
**Purpose**: Identify every input needed to write the executive vision document. Complete this first. Draft the strategy document once.

---

## Section 1: Purpose & Audience

**What the strategy document must do**: align leadership on the 2030 direction for Merchant Care before investment conversations happen. This is not an investment ask document — it is a direction-setting document that makes the investment ask credible when it comes.

**Audience**:
- **C-suite**: 2-minute read; needs to understand the strategic problem, the 2030 commitment, and why acting now matters
- **VP/Director layer**: full document; needs operational depth, roadmap, people model, and risks

**What success looks like**: after reading, the executive audience understands the 2030 vision, believes the plan is sequenced and credible, and knows what decision or support is being asked of them.

**Document structure planned**:
1. Executive summary (C-suite layer, ~300 words)
2. Where we are today
3. The forces shaping 2030 (urgency)
4. The 2030 vision (merchant experience, agent experience, metrics targets)
5. Operating model: People, Process, Technology (flywheel inside Technology)
6. The roadmap (3 phases: 2026 Foundation / 2027 Expansion / 2028–2030 Autonomous)
7. Risks and dependencies
8. What success looks like (metrics summary)

---

## Section 2: Metrics to Confirm

All baseline and target metrics needed to anchor the document. Pre-populated where data already exists; placeholders where Charlie needs to confirm.

| Metric | Source | Why it matters | Current value | 2026 target | 2030 target |
|--------|--------|---------------|--------------|------------|------------|
| Contact rate (contacts per 1M txns) | Data Scientist | North star metric — the document is unanchored without it | [ ] | Flat or declining | Declining YoY |
| Blended cost per contact | Data Scientist + Finance | P&L gap that justifies investment | [ ] | Declining | Significantly reduced |
| Current CSAT score | Zendesk reporting | Guardrail — must not decline as automation scales | [ ] | >90% | >90% |
| SLA adherence % | Zendesk reporting | Governance credibility | [ ] | >95% | >95% |
| AHT (Average Handle Time) | Zendesk reporting | Agent Consultant ROI claim needs a before number | [ ] | Declining | Significantly reduced |
| Fin involvement rate | Intercom / Data | Most important single number in the document | [ ] | >30% | >80% |
| Fin resolution rate (when involved) | Intercom / Data | Shows Fin quality; the gap is funnel, not product failure | [ ] | >80% | >85% |
| Total contact volume (rolling 6m) | Zendesk / Data | Demand baseline | [ ] | — | — |
| Contact mix by case type (%) | support-taxonomy.md | Deflection opportunity sizing | Payments In 42.8%, Account Mgmt 16.9%, Payouts 10.0%, Tech Issues 7.8%, Funds & Fees 7.5% | — | — |
| Fin involvement rate 2026 target | 2026 deliverables.md | What's achievable this year | — | >30% | — |
| Fin involvement rate 2030 target | care-product-model.md | End-state anchor | — | — | >80% |
| Unit cost: Fin per resolution | CLAUDE.md benchmarks | Investment case denominator | $0.90 | — | — |
| Unit cost: human agent per contact | CLAUDE.md benchmarks | Investment case baseline | ~$40 | — | — |

**Priority**: confirm items marked `[ ]` with Data Scientist before drafting. The contact rate (per 1M txns) and blended cost per contact are the highest-impact gaps.

---

## Section 3: Competitive Positioning — Inputs Needed

The strategy document must make a credible urgency argument. "Competitors are moving" is not enough on its own. Gather or make a judgement call on each item below.

### B2B Competitive Context
- [ ] **Stripe Support today**: does Stripe offer AI deflection? Self-serve resolution? What are their published resolution rates or support model?
- [ ] **Adyen Support today**: same questions
- [ ] **Checkout's differentiated claim in B2B by 2030**: complete this sentence: "By 2030, Checkout is the only PSP that [X] — which competitors cannot replicate because [Y]."
- Context available: industry FCR at 70–85% today; will be table stakes by 2027 at current trajectory

### B2C Competitive Context
- [ ] **Klarna AI resolution rate**: relevant comp for B2C payments support
- [ ] **Monzo / Starling support model**: relevant comps for B2C banking support (Braavos context)
- [ ] **Braavos consumer comparison set**: will Braavos consumers compare to other neobanks, challenger banks, or legacy banks? This shapes what "good" looks like at launch.
- [ ] **Checkout's differentiated B2C claim**: is the goal to be best-in-class, or to meet the regulatory/parity floor?

**If competitive data isn't available**: the document should make a directional argument ("industry average will be X by 2027; we must target Y to differentiate") rather than leave the claim unsupported. Note that here so the draft doesn't paper over it.

---

## Section 4: Strategic Decisions to Make or Confirm

These are open questions that directly shape what the strategy document says. Each should be resolved before the draft is written. Where a decision is not yet made, the document will flag it as an open decision with a deadline.

### Decision 1: B2C Support Tier Model
**Questions to answer:**
- Is B2C support tiered (e.g. Standard / Premium / Ultra)?
- Is support a revenue lever (charge for premium tier) or a retention/compliance tool (differentiate on experience, not price)?
- What SLA commitments apply per tier?

**Why it matters**: gates Fin configuration, B2C content build, and Consumer Duty scoping. Can't design the B2C section of the strategy without this.

**Current status**: [ ] Undefined / [ ] In discussion / [ ] Decided — answer:

---

### Decision 2: Consumer Duty Process Ownership
**Questions to answer:**
- Who owns design of Consumer Duty processes (complaint handling, 8-week SLA, FOS referral pathway, vulnerable customer identification)?
- Has a Q2 2026 design start been agreed with Operations and Legal?
- Is there a formal workstream, or is this informal discussion?

**Why it matters**: these processes must be live at Braavos wallet launch (2027), not added post-launch. If design doesn't start Q2 2026, engineering cannot build in time. Non-compliance at launch is a legal and reputational risk.

**Current status**: [ ] No owner / [ ] Owner identified — name: ______________ / [ ] Workstream scoped

---

### Decision 3: Platform Embedded AI — Commercial Model
**Questions to answer:**
- Included in Platform fees, or separately priced?
- Which ISV partners have been consulted? Any willing to pilot?
- If not yet agreed: is this positioned as a 2027 decision (not a 2026 commitment)?

**Why it matters**: executives will ask what the business case is. "Volume deflected" and "commercial model" are the two questions they'll have. Can't include this in the vision without an answer, even if the answer is "decision in 2027".

**Current status**: [ ] No commercial model defined / [ ] Directional answer: ______________________

---

### Decision 4: Agent Headcount Trajectory 2028–2030
**Questions to answer:**
- As AI resolution reaches 80%+, what happens to the human agent team?
- Does the team shrink (cost reduction)? Redeploy to banking/B2C complexity? Stay flat?
- Is this a decision for the vision document, or a future workforce planning exercise?

**Why it matters**: a 2030 vision that doesn't address this looks evasive to a finance-led audience. They will ask. Better to frame it deliberately.

**Current status**: [ ] Not yet considered / [ ] Directional answer: ______________________

---

### Decision 5: Reflex Cross-Team Adoption Model
**Questions to answer:**
- The 2030 vision requires product engineering teams to act on Reflex-generated fix PRs. Has this been socialised with engineering leadership?
- What is the adoption model — opt-in per team? Mandatory review? Engineering discretion?

**Why it matters**: if other engineering teams haven't agreed to act on AI-generated fix recommendations, the "autonomous Reflex" 2030 vision is not credible. Either socialise it, or scope it as a 2027–2028 alignment workstream in the document.

**Current status**: [ ] Not yet socialised / [ ] In discussion / [ ] Agreed — model: ______________________

---

### Decision 6: 2030 AI Resolution Ambition
**Questions to answer:**
- Current target: >80%. Industry will likely be at 80% by 2027.
- Should the 2030 target be raised to 85–90% to remain differentiated?
- Or is 80%+ intentionally conservative given B2B query complexity?

**Why it matters**: the target sets the credibility bar for the entire document. Too low looks unambitious relative to where the market will be. Too high looks unrealistic to a sceptical engineering audience.

**Current status**: [ ] Keep >80% — rationale: ________________ / [ ] Raise to ____% — rationale: ________________

---

## Section 5: Narrative Inputs — Experience Stories

The strategy document needs 2–3 vivid, concrete experience narratives to make the 2030 vision tangible for executives. Proposed scenarios below — confirm, adjust, or add detail before drafting.

### Merchant Experience (2030 — Standard B2B merchant)
**Proposed scenario**: A merchant notices a settlement discrepancy. They open the Dashboard; Fin surfaces the answer in the transaction context before they submit a ticket. For the one query Fin can't resolve, their ticket arrives pre-loaded with context. Their agent has an AI suggestion ready. Resolution in minutes, not hours.

- [ ] Is this the right scenario? Alternatives: payments query, account access issue, dispute
- [ ] Any real merchant quotes or friction points from Maria (persona research) to colour this?
- [ ] Anything in this scenario that's not achievable by 2030 given the capability model?

---

### Agent Experience (2030 — L1 agent)
**Proposed scenario**: An L1 agent opens a new ticket. Customer 360 pre-loads the merchant's full context. The Agent Consultant surfaces the likely fix. For 90% of tasks, the agent confirms an AI suggestion rather than drafting from scratch. For the 10% that are genuinely novel, they have the tools to investigate — not 3–4 disconnected systems.

- [ ] Is the 90% confirmation / 10% novel split realistic per the capability model?
- [ ] Any quotes from Oliver or Niamh persona research to ground this?
- [ ] Is there a risk this reads as threatening to agents? Should the framing be adjusted?

---

### B2C Consumer Experience (2030 — Braavos wallet user) — Optional
**Proposed scenario**: A consumer raises a disputed charge. Fin detects vulnerability signals. Evidence is gathered autonomously. Outcome delivered within the Consumer Duty timeframe. No human involved for the majority of cases; agent involvement for complex or high-sensitivity cases.

- [ ] Include this scenario? (Adds regulatory credibility; shows B2C is genuinely planned, not an afterthought)
- [ ] Requires B2C tier model to be defined first (Decision 1 above)
- [ ] Vulnerability detection: is this technically confirmed for 2030, or aspirational?

---

## Section 6: Roadmap — Dates and Milestones to Confirm

The three-phase roadmap is directionally set from existing strategy documents. Confirm the specifics below before the strategy document locks in dates.

### Phase 1 — Foundation (2026)
- [ ] Webform retirement: Q3 2026 — still the target? Any blockers that should be surfaced?
- [ ] Data latency fix (settlements/balances via MCP): what is the current resolution timeline from the platform data team? This blocks Agent Consultant phase 2.
- [ ] Reflex MCP: Q3 2026 — confirmed?
- [ ] Support model rollout: Standard (Q2), Enterprise/Premium (Q3) — confirmed?
- [ ] Customer 360 phase 1: what is in scope for Q1 vs Q2? Clarify boundary.

### Phase 2 — Expansion (2027)
- [ ] Braavos wallet launch date: confirmed as 2027? Is there a specific half or quarter? Any current risk of delay?
- [ ] Platform Embedded AI: when does development start? Dependent on 2026 identification foundations — when will those be ready?
- [ ] Team scaling: when does the investment approval process need to start to have headcount in place before Braavos launch?

### Phase 3 — Autonomous (2028–2030)
- [ ] B2B Banking support model: is 2028 still the right horizon, or is banking product scope still TBC?
- [ ] Reflex autonomous action plans: has any engineering feasibility assessment been done? Or is this a 2030 aspirational target with no current technical validation?

---

## Section 7: Risks — Confirm Current Status

Each of these risks was identified as live in existing strategy documents as of March 2026. Confirm whether each is still live, resolved, or has changed.

| Risk | Last known status (March 2026) | Current status | Owner |
|------|-------------------------------|---------------|-------|
| Data latency blocker (settlements/balances) | Unresolved; blocking Agent Consultant phase 2 | [ ] | Platform data team |
| B2C taxonomy definition | Required mid-2026; not yet started | [ ] | [ ] |
| Consumer Duty process design | No owner or formal start date | [ ] | [ ] |
| Fin administration ownership gap | Shared between Product and Content; no dedicated owner | [ ] | [ ] |
| ISV commercial alignment for Platform Embedded AI | TBC; dependent on 2027 commercial agreements | [ ] | [ ] |

---

## Section 8: Document Logistics

- [ ] Confluence location confirmed: MTC space, PRDs folder (parent page ID: 8041431176)?
- [ ] Format: written document only, or does this also need a slide deck version for a presentation?
- [ ] Review gate before C-suite: VP of Product only, or Director of Operations and Director of Operations Excellence too?
- [ ] Target date to share with leadership?

---

## How to Use This Document

1. Work through Sections 2–5 first — these are the highest-priority inputs
2. Mark `[x]` and add the confirmed answer when each item is resolved
3. For Strategic Decisions (Section 4): make the decision, note the answer, note the date decided
4. Once Sections 2–5 are substantially complete, hand back to Claude to draft the strategy document in a single clean pass
5. Sections 6–8 can be TBC in the first draft and filled in before publishing

**Priority order:**
1. **Section 2 (Metrics)** — without baselines the document has no teeth
2. **Section 4 (Strategic Decisions)** — shapes what the document actually says
3. **Section 3 (Competitive Positioning)** — required for executive urgency argument
4. **Sections 5–8** — important but can follow a first draft

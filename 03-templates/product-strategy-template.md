---
title: "[Domain/Theme] Strategy [Year]"
author: Charlie Wildish
date: YYYY-MM-DD
horizon: "YYYY–YYYY (1–3 years)"
stage: Draft
last_updated: YYYY-MM-DD
reviewers: "VP of Product · Director of Operations · Director of Operations Excellence"
confluence_space_key: MTC
confluence_parent_page_id: 8041431176
---

<!-- ============================================================
AUTHOR PREAMBLE — REMOVE BEFORE SHARING OR PUBLISHING
============================================================

## What is a strategy? (Rumelt)

Good strategy has three components — the Strategy Kernel:

1. DIAGNOSIS — A clear, honest assessment of the critical challenge. Not a list of problems. One pivotal difficulty: the crux.
2. GUIDING POLICY — Your overall approach for dealing with the challenge. HOW you will address it. Not a goal ("grow 50%"), not a vision ("be the best"). A policy channels action and explicitly rules things out.
3. COHERENT ACTIONS — Coordinated initiatives that implement the guiding policy and reinforce each other. Actions that do not reinforce each other waste resources and dilute impact.

This template maps:
- Sections 1, 2, 2a → DIAGNOSIS
- Sections 3, 5 → GUIDING POLICY
- Sections 4, 8 → COHERENT ACTIONS

## Bad strategy self-assessment checklist (Rumelt)

Before sharing this document, check for the four hallmarks of bad strategy:

- [ ] **Fluff** — Does any section contain gibberish dressed as strategy? ("Leverage synergies", "be merchant-obsessed".) Cut it.
- [ ] **Failure to face the challenge** — Does the Diagnosis name one pivotal difficulty clearly, backed by data? If not, the strategy floats.
- [ ] **Goals mistaken for strategy** — Does Section 3 describe HOW you will address the challenge, or does it just restate a target? A growth number is not a Guiding Policy.
- [ ] **Incoherent actions** — Do the bets in Section 4 reinforce each other? If they are independent items from a wish list, they are not coherent actions.

If any box is unchecked, revise before sharing.
============================================================ -->

# [Domain/Theme] Strategy [Year]

| Field | Value |
|---|---|
| **Author** | Charlie Wildish |
| **Date** | YYYY-MM-DD |
| **Horizon** | YYYY–YYYY (1–3 years) |
| **Stage** | Draft / In Review / Approved |
| **Last Updated** | YYYY-MM-DD |
| **Reviewers** | VP of Product · Director of Operations · Director of Operations Excellence |

---

> **Before writing:** Complete the anchor table below. A strategy without these anchors is not ready to draft. Then confirm the Rumelt coherence check at the bottom of the table.

| Anchor | Value |
|---|---|
| **Strategic goal** | Reduce contact rate / Reduce cost of support / Both |
| **Primary flywheel domain(s)** | [Select from: Input · Orchestration · Fuel · Agent Experience · Insight & Prevention · Governance] |
| **Strategic lever** | Contact reduction · AI deflection · Agent efficiency · Self-service |
| **North star metric(s) moved** | Contact rate · Cost per contact · Fin involvement rate · Agent handle time · CSAT |

**Rumelt coherence check:**
- Does the Guiding Policy (Section 3) directly address the challenge named in the Diagnosis (Sections 1–2)?
- Do the Coherent Actions (Section 4) implement the Guiding Policy — not just list good ideas?
- Do the actions in Section 4 reinforce each other, or are they independent?

If the answer to any question is "not yet", do not share this document.

---

## 1. Strategic Context

*[Rumelt: DIAGNOSIS — situational assessment. What is happening in the business, the market, or the product landscape that makes this strategy necessary now? This is the "why now" — not a history lesson. Include 2–3 facts: transaction volume growth, cost benchmarks, competitive moves, regulatory change, or a new customer segment. Keep to 3–5 short paragraphs. Do not write a vision statement here — describe the forces creating pressure or opportunity.]*

[What is changing — at Checkout.com, in the market, or for this customer segment — that makes this strategy timely?]

[What does this mean for Merchant Care? What pressure or opportunity does it create?]

[Why is the current state insufficient to respond to that change?]

---

## 2. Problem Framing

*[Rumelt: DIAGNOSIS — the crux. Name the pivotal difficulty in the first sentence. Then support it with data. Use the contact breakdown (`04-active-work/working-files/Contact breakdown since April 2026.md`) and taxonomy (`01-knowledge-base/processes/support-taxonomy.md`) to ground the problem in real volumes and cost. Never use placeholder numbers. The crux is singular — if you have five "core problems", you have not done the diagnosis.]*

**The crux:** [One sentence. The pivotal difficulty this strategy must address.]

**The data:**

| Metric | Current state | Source |
|---|---|---|
| [Metric 1 — e.g. contact rate for this domain] | [Value] | [CSV / taxonomy / KPI doc] |
| [Metric 2 — e.g. cost per contact] | [Value] | [Source] |
| [Metric 3 — e.g. Fin resolution rate for this query type] | [Value] | [Source] |

*Every cell must have a value or "TBC — establish by [date]". A bare TBC is not acceptable.*

**What this costs us:** [Translate the data into business impact. If 30% of contacts fall into this domain at ~$40/contact, say so.]

**What merchants experience:** [1–2 sentences describing the merchant-facing symptom. Quotes from research or Fin transcripts if available.]

---

## 2a. Customer Segments in Scope

*[Who does this strategy apply to? Checkout.com serves three distinct B2B segments (Direct Merchant, Platform/ISV, and B2B Banking 2028+) and will add B2C in 2027. Strategy that applies uniformly to all segments is rare — be explicit about which segments are in scope and what differs for each. The "not in scope" row is mandatory; do not leave it blank.]*

| Segment | In scope? | Notes — what differs for this segment |
|---|---|---|
| **Direct Merchant** | Yes / No / Partially | [e.g. primary target; full feature set applies] |
| **Platform / ISV** | Yes / No / Partially | [e.g. in scope from Q3 as Platform Support Channels land; context differs — Checkout is L2] |
| **B2C (2027 launch)** | Yes / No / Partially | [e.g. out of scope for this strategy horizon; Consumer Duty requirements handled separately] |
| **B2B Banking (2028+)** | Yes / No / Partially | [e.g. not in scope — taxonomy and support model not yet defined] |

**Explicitly not in scope:** [Name segments or sub-segments excluded from this strategy and why.]

---

## 3. Strategic Intent (Guiding Policy)

*[Rumelt: GUIDING POLICY. Write one guiding statement — 1–2 sentences — that defines HOW this strategy will address the crux. This is the overall approach that channels action and rules things out. It must describe a method, not a destination.*

*Bad strategy warning: if this section reads like a goal ("increase Fin resolution rate to 60%") or a vision statement ("become the leading AI-powered support function"), it is not a Guiding Policy. A goal says where you want to end up. A Guiding Policy says how you will get there. Rewrite until you can read it aloud and say "this tells me what to do and what NOT to do."]*

> We will [method/approach], by [how], so that [outcome — for merchants and/or Checkout.com].

*Example: "We will eliminate Fin's reliance on static knowledge by connecting it to live Checkout transactional data through structured Procedures, so that Fin can resolve merchant queries end-to-end without human escalation — and every new data integration compounds resolution coverage rather than requiring new content."*

**Key strategic choices this policy makes:**
- We will: [Specific choice 1 — what we are committing to]
- We will: [Specific choice 2]
- We will NOT: [What this policy rules out — the hard choice]

---

## 4. Strategic Bets (Coherent Actions)

*[Rumelt: COHERENT ACTIONS. List 3–5 bets — the specific things you are choosing to invest in. Each bet must implement the Guiding Policy above. A bet is a deliberate choice under uncertainty: you are committing resources based on a hypothesis.*

*Bad strategy warning: if these bets are independent items from a wish list, they are NOT coherent actions. Read them together — does each one reinforce the others? Do they create a compounding effect? If not, revise until they do.*

*Do not exceed 5 bets. More than 5 means you are not making hard choices.*

*After writing all bets, answer the coherence check at the end of this section.]*

### Bet 1: [Short name]

**Hypothesis:** If we [do X], then [Y will happen], because [Z].

**Why this bet:** [The evidence or reasoning that makes this the right use of effort. Reference data from Section 2 where possible.]

**What it requires:** [The key capability, dependency, or investment needed to execute this bet.]

**What would make it wrong:** [The condition or data point that would indicate this bet should be abandoned or changed. If you cannot answer this, the bet is not a bet — it is an assumption. Move it to Section 9.]

---

### Bet 2: [Short name]

**Hypothesis:** If we [do X], then [Y will happen], because [Z].

**Why this bet:** [Evidence or reasoning.]

**What it requires:** [Key capability, dependency, or investment.]

**What would make it wrong:** [Condition or data point that would invalidate the bet.]

---

### Bet 3: [Short name]

**Hypothesis:** If we [do X], then [Y will happen], because [Z].

**Why this bet:** [Evidence or reasoning.]

**What it requires:** [Key capability, dependency, or investment.]

**What would make it wrong:** [Condition or data point that would invalidate the bet.]

---

*Add Bet 4 and Bet 5 if needed. Each must connect directly to the Guiding Policy.*

**Coherence check:** Read the bets together. Do they reinforce each other and compound toward the Guiding Policy? Write one sentence summarising how they connect:

> [e.g. "Bets 1 and 2 build the data layer that Bet 3 depends on; Bet 4 ensures the insight loop closes so Bets 1–3 improve continuously."]

If you cannot write this sentence, the bets are not yet coherent.

---

## 5. What We Are Not Doing

*[Rumelt: GUIDING POLICY — focus requires saying no. This section is as important as Section 4. Explicit de-prioritisation prevents scope creep, aligns stakeholders, and signals rigour. These are strategic choices, not administrative deferrals. List things that are in-scope for this domain but are being deliberately excluded from this strategy horizon.*

*Rule: only list things a reasonable stakeholder might expect to see here. Do not use this section to list things that were never candidates.]*

| What we are not doing | Why — the strategic choice |
|---|---|
| [Capability or initiative] | [e.g. Dependency on X not ready until Q3 2027; insufficient contact volume to justify; owned by Y team; would dilute focus on the crux] |
| [Capability or initiative] | [Strategic reason] |
| [Capability or initiative] | [Strategic reason] |

---

## 6. Success Looks Like

*[Define what winning looks like at the 12-month and strategy-horizon marks. Every metric must tie to a north star or a flywheel domain metric. Every baseline must be a real number or a committed date by which it will be established. Targets must be directional and grounded — do not write targets you cannot defend.*

*Rule: every Baseline cell must contain a value or "TBC — establish by [date]". A bare TBC is not acceptable.]*

| Metric | Why it matters | Baseline | 12-month target | Horizon target | Source |
|---|---|---|---|---|---|
| Contact rate (contacts per 1M txns) | North star — measures whether we are reducing overall demand | [Value] | [-X%] | [-X%] | Support contacts CSV |
| Cost per contact | North star — measures unit economics of support delivery | [Value] | [-X%] | [-X%] | Finance / KPI doc |
| Fin involvement rate | Measures AI deflection before human handling | [Value] | [X%] | [X%] | Intercom |
| [Domain-specific metric] | [Why it matters for this strategy] | [Value] | [Target] | [Target] | [Source] |
| Merchant CSAT | Guardrail — must not decline as we automate | [Value] | Maintain or improve | Maintain or improve | Zendesk CSAT |

*Add metrics specific to this strategy domain. Remove metrics you cannot measure. Do not add metrics because they sound good.*

---

## 7. Flywheel Mapping

*[Map this strategy to the Care flywheel. Identify which domains this strategy touches, what it changes in each domain, and whether the impact is primary (this strategy directly drives change here) or secondary (this strategy enables or is enabled by work in this domain). Reference: `01-knowledge-base/strategy/care-product-model.md`.]*

| Flywheel domain | What this strategy changes here | Impact |
|---|---|---|
| **1. Input** | [How this strategy affects what contacts arrive, from which channels, or with what taxonomy coverage] | Primary / Secondary / Not touched |
| **2. Orchestration** | [How this strategy affects triage, routing, or intent classification] | Primary / Secondary / Not touched |
| **3. Fuel** | [How this strategy depends on or improves data and knowledge for Fin and agents] | Primary / Secondary / Not touched |
| **4. Agent Experience** | [How this strategy changes what agents see, do, or can act on in Zendesk] | Primary / Secondary / Not touched |
| **5. Insight & Prevention** | [How this strategy generates or depends on contact insight and root-cause analysis] | Primary / Secondary / Not touched |
| **6. Governance** | [How this strategy affects SLA management, QA, or scheduling] | Primary / Secondary / Not touched |

---

## 8. Roadmap Alignment (Coherent Actions — Delivery)

*[Map the deliverables that execute against this strategy. Every bet in Section 4 should map to at least one deliverable here. If a bet has no corresponding deliverable, flag it as a gap — it is either not yet on the roadmap or requires a new PRD. Reference: `2026 deliverables.md`.]*

| Deliverable | Quarter | Bet(s) it serves | Goal |
|---|---|---|---|
| [Deliverable name from roadmap] | Q[X] [YEAR] | Bet [#] | Reduce contact rate / Reduce cost |
| [Deliverable name] | Q[X] [YEAR] | Bet [#] | Reduce cost |
| [Deliverable name] | Q[X] [YEAR] | Bet [#] | Reduce contact rate |

**Roadmap gaps:** [List any bets in Section 4 that do not yet have a corresponding deliverable. Each gap is a planning action to take forward.]

---

## 9. Risks and Dependencies

*[List the risks, external dependencies, and critical assumptions that could change the bets. Do not list risks for completeness — only risks that would cause you to revise a bet.]*

### Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| [Risk — e.g. data quality for Fin Procedures is insufficient to build reliable resolution logic] | H / M / L | [What breaks if this materialises] | [What we will do to reduce likelihood or contain impact] |
| [Risk] | H / M / L | [Impact] | [Mitigation] |

### Dependencies

| Dependency | Owner | Status | Impact if delayed |
|---|---|---|---|
| [Cross-team or external dependency — e.g. Customer 360 data model stable by Q2 2026] | [Team / person] | Confirmed / Assumed | [What slips if this is not met on time] |
| [Dependency] | [Owner] | Confirmed / Assumed | [Impact] |

### Key Assumptions

*Things that must be true for this strategy to work, which you cannot validate today. For each, say how and when you will validate or monitor it.*

- [Assumption 1 — and how/when you will validate it]
- [Assumption 2 — and how/when you will validate it]

---

## 10. Open Questions

*[Unresolved questions that could change the bets or scope. An open question is not a risk and not an assumption — it requires a decision or additional information before the relevant bet can be confidently executed. Resolved questions should be removed and their conclusions folded into the relevant section above.]*

| Question | Which bet is affected | Owner | Target resolution |
|---|---|---|---|
| [Question — e.g. Will Fin support multi-step Procedures with conditional branching by Q2 2026?] | Bet [#] | [Person] | [Date or milestone] |
| [Question] | Bet [#] | [Person] | [Date] |

---

## Appendix

*Optional. Supporting material for reviewers who want more depth.*

- **Supporting data**: [Links to contact volume analysis, CSV extracts, or dashboards]
- **Related PRDs**: [Links to PRDs that implement specific bets — each PRD should reference this strategy in its strategic alignment block]
- **Competitive context**: [Links to competitive analysis or research in `01-knowledge-base/strategy/`]
- **Research and interviews**: [Links to merchant interview transcripts or synthesis in `04-active-work/`]
- **Alternatives considered**: [Strategic directions evaluated and rejected, with brief rationale]

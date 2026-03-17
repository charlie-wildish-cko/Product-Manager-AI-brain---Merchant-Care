# Product Strategy Intake Form

<!-- ============================================================
HOW TO USE THIS FORM

1. Fill in each section below with bullet points, rough notes, or partial thoughts.
   Full sentences are not required. Claude will do the writing.

2. You do not need to fill in every field. Leave unknowns blank — Claude will flag them
   as "TBC — establish by [date]" in the output.

3. When done, say: "generate strategy from intake"

Claude will then:
- Read this form
- Cross-reference 2026 deliverables.md, care-product-model.md, and kpi-definitions.md
- Generate a complete draft saved to 04-active-work/[slug]-strategy-[year].md
- Flag any sections where input was too thin to draft confidently

What Claude does NOT need from you:
- Flywheel domain definitions (it knows them)
- Metric definitions (it knows them)
- Rumelt framing and coherence checks (it adds these)
- Full sentences or formatted prose (it writes the document)
- 2026 deliverable names and Jira IDs (it cross-references the roadmap)
============================================================ -->

---

## 1. Identity

> What is this strategy about, and how long does it span?

- **Strategy title / domain:** Merchant Care to 2030 during multi product customer expansion
- **Horizon:** [e.g. 2026–2028]
- **Strategic goal:** Enable the scaling of Support experience to our customers
- **Primary flywheel domain(s):** All - this is top down view

*Produces: document title, header metadata, anchor table.*

---

## 2. Strategic Context (Diagnosis — situational assessment)

> What is changing —
>
> We are expanding our customer base from ~2k merchants today in the Direct merchant acquiring model to:
>
> 1. Platforms (ISV, Payfac, SMB?)
> 2. Consumer wallet offering (B2C)
> 3. Becoming a bank and storing funds for customers with interest rates (not confirmed but very likely)
>
> - This will increase our customer base to millions by 2030 in both B2B and B2C offerings. This in turn brings the rate of support contacts increasing, additional regulatory requirements, complexity in how we service the customer and provide the right experience for them (e.g. size of merchant, if we offer a consumer tiered plan like Monzo/Revolut with paid plans).
> - TLDR: We are becoming a large multi product company which means growth in all areas. This stratey focuses specifically on customer support (Care).
>

*Produces: Section 1 (Strategic Context). Claude will expand these into 3–5 short paragraphs.*

---

## 3. The Crux (Diagnosis — pivotal challenge)

> What is the single most important problem this strategy must solve?
> One sentence. If you write more than one sentence, you have not found the crux yet.
> Bad example: "We have low Fin resolution rates, gaps in knowledge, and agents don't have enough context."
> Good example: "Fin cannot resolve transactional queries because it has no access to live Checkout data."

**The crux:**

*Produces: Section 2 opening sentence. This is the most important input in the form.*

---

## 4. Supporting Data

> What data do you know that supports the crux? Rough numbers are fine — Claude will flag gaps.
> Examples: contact volumes, Fin resolution rate, cost per contact, handle time, CSAT scores, % of contacts in this domain.

| Metric | Value (rough is fine) |
| ------ | --------------------- |
|        |                       |
|        |                       |
|        |                       |

*Produces: data table in Section 2 (Problem Framing) and baselines in Section 6 (Success Looks Like). Claude fills in metric names and flags missing values as TBC.*

---

## 5. Merchant Experience

> How does this problem show up for merchants? What do they feel, see, or complain about?
> A rough quote from an interview, a Fin transcript excerpt, or a one-line description is enough.

*Produces: "What merchants experience" paragraph in Section 2.*

---

## 6. Customer Segments

> Which segments does this strategy apply to, and what (if anything) differs per segment?
> Segments: Direct Merchant / Platform / ISV / B2C (2027) / B2B Banking (2028+)

| Segment             | In scope? | Notes (what differs, if anything) |
| ------------------- | --------- | --------------------------------- |
| Direct Merchant     |           |                                   |
| Platform / ISV      |           |                                   |
| B2C (2027)          |           |                                   |
| B2B Banking (2028+) |           |                                   |

**Segments explicitly not in scope:**

*Produces: Section 2a (Customer Segments in Scope).*

---

## 7. Draft Strategic Intent (Guiding Policy)

> Rough draft of your "we will..." statement. Half-formed is fine — Claude will refine it into a proper Guiding Policy.
> A Guiding Policy describes HOW you will address the crux, not what you want to achieve.
> Bad: "Improve Fin resolution rates." (that's a goal)
> Good: "Prioritise connecting Fin to live Checkout data over expanding its knowledge content, so that resolution coverage compounds with every data integration rather than requiring manual content updates."

**Draft intent:**

**What this rules out (the hard choices):**
---------------------------------------

*Produces: Section 3 (Strategic Intent / Guiding Policy) and Section 5 (What We Are Not Doing).*

---

## 8. Strategic Bets

> 3–5 bets — the specific things you are committing to invest in.
> For each: a short name and 1–2 sentences on the idea or hypothesis. Rough is fine.
> Claude will add "what would make it wrong", "what it requires", and the coherence check.

### Bet 1

- **Name:**
- **Idea / hypothesis:**

### Bet 2

- **Name:**
- **Idea / hypothesis:**

### Bet 3

- **Name:**
- **Idea / hypothesis:**

### Bet 4 (optional)

- **Name:**
- **Idea / hypothesis:**

### Bet 5 (optional)

- **Name:**
- **Idea / hypothesis:**

*Produces: Section 4 (Strategic Bets / Coherent Actions). Claude completes each bet with hypothesis structure, requirements, and what-would-make-it-wrong, then writes the coherence check.*

---

## 9. Roadmap Connections

> Which 2026 deliverables execute against this strategy?
> You don't need Jira IDs — Claude will cross-reference 2026 deliverables.md and flag gaps.
> Rough names or descriptions are fine.

*Produces: Section 8 (Roadmap Alignment). Claude maps each deliverable to a named bet and flags any bets with no corresponding deliverable.*

---

## 10. Metrics and Targets

> Any known target values for the strategy horizon or 12-month mark.
> Leave blank if unknown — Claude will include the metric with a TBC baseline.

| Metric               | 12-month target | Horizon target |
| -------------------- | --------------- | -------------- |
| Contact rate         |                 |                |
| Cost per contact     |                 |                |
| Fin involvement rate |                 |                |
| [Other]              |                 |                |

*Produces: Section 6 (Success Looks Like). Claude fills in baseline values from known data or flags as TBC.*

---

## 11. Risks and Dependencies

> Known risks that could cause you to revise a bet, and cross-team dependencies.
> Rough bullets — Claude will structure these into the risks/dependencies table.

**Risks:**
------

**Dependencies (cross-team or external):**
--------------------------------------

*Produces: Section 9 (Risks and Dependencies).*

---

## 12. Open Questions

> Unresolved questions that could change a bet or the scope. Assign an owner if you know one.

| Question | Bet affected | Owner |
| -------- | ------------ | ----- |
|          |              |       |
|          |              |       |

*Produces: Section 10 (Open Questions). Claude adds a target resolution column.*

---

## 13. Anything Else

> Links to related research, interviews, PRDs, or context Claude should read before generating the strategy.

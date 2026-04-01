# Target Operating Model — [Name / Scope]

**Document Purpose**: [One sentence — what this TOM defines and who it is for]
**Audience**: [VP Product · Director of Operations · Director of Operations Excellence]
**Status**: Draft | **Last Updated**: [Date] | **Owner**: [Name]

---

## 1. Strategic Context

### The Case for Change
[2–3 sentences: what is the forcing function — volume growth, cost pressure, new segment, regulatory change. Lead with the business problem, not the solution.]

### Strategic Goal
[Which goal does this TOM serve? Select one or both:]
- Reduce contact rate (contacts per 1M transactions)
- Reduce cost of support (cost per contact)

### North Star and Guardrail Metrics

| Type | Metric | Current Baseline | Target |
|---|---|---|---|
| North Star | [e.g. AI resolution rate] | [x%] | [x%] |
| North Star | [e.g. Cost per contact] | [$x] | [$x] |
| Guardrail | Merchant CSAT | [x] | Must not decline |
| Guardrail | SLA adherence | [x%] | Must not decline |

### 2026 Deliverable Anchor
[Which named deliverable(s) in `2026 deliverables.md` does this TOM support? If it spans multiple, list them.]

---

## 2. Current State (As-Is)

### What Works Today
[What is the current model doing well? Be specific — not a general critique.]

### Where It Breaks Down
[2–4 bullet points: the specific failure modes or constraints this TOM is designed to solve. Ground in data where possible.]

### Capability Gaps
[Table or bullets: what capabilities are missing or immature that the target state requires]

| Capability | Current Maturity | Required Maturity | Gap |
|---|---|---|---|
| [e.g. AI Resolution Management] | L1 — ad hoc | L3 — owned, OKRs | No named owner; no Procedure library |
| | | | |

---

## 3. Target State (To-Be)

_The Deloitte capability-based model: Strategy → Capabilities → Organisation → Technology. Define each layer._

### 3a. Capabilities

[What must the function be able to do in the target state? Group by cluster if more than five.]

| Capability | Description | Why It Matters |
|---|---|---|
| [Name] | [What it enables] | [Impact on north star metric] |
| | | |

### 3b. Organisation

**Structure and Grouping**
[How is the team organised — by function, by product, by channel? One paragraph or simple diagram.]

**Roles and Accountabilities**

| Role | Accountability | Decision Authority |
|---|---|---|
| [e.g. Fin Owner] | Resolution rate; Procedures; escalation thresholds | Full authority on Fin config |
| | | |

**Governance**
[How are decisions made? Who sits in what forum? Cadence of reviews.]

| Forum | Attendees | Frequency | Purpose |
|---|---|---|---|
| [e.g. Fin Ops Review] | Fin Owner, EM, Ops Lead | Weekly | Procedure quality, top failures |
| | | | |

### 3c. Technology

[What systems, tools, and integrations are required to enable the target state? Map to capabilities above.]

| Capability | Technology Required | Current State | Gap |
|---|---|---|---|
| [e.g. AI Resolution] | Fin Procedures + Customer 360 MCP | Partial | Latency fix needed |
| | | | |

**Design principle**: technology enables the model; design the operating model first, then select or configure technology to fit.

---

## 4. Implementation Roadmap

### Sequencing Principles
[1–3 sentences on how changes are sequenced — e.g. data foundation first, then AI deployment, then org change]

### Phases

| Phase | Period | Key Changes | Success Criteria |
|---|---|---|---|
| 1 — Foundation | [e.g. Q1–Q2 2026] | [What changes] | [How you know it worked] |
| 2 — Build | [e.g. Q3–Q4 2026] | | |
| 3 — Scale | [e.g. 2027] | | |

### Blocking Dependencies
[List the things that must be true before each phase can proceed]

1. [Dependency] — blocks [phase]
2. [Dependency] — blocks [phase]

---

## 5. Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| [e.g. Knowledge debt at AI scale-up] | High | High | Audit knowledge base before expanding Procedure coverage |
| | | | |

---

## 6. Success Criteria

**Phase 1 complete when**: [specific, measurable conditions]
**Phase 2 complete when**: [specific, measurable conditions]
**Target state achieved when**: [specific, measurable conditions]

---

## Appendix: Glossary
[Add any terms that need definition for this audience]

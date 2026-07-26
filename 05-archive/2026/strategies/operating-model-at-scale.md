# Operating Model Implications at 80% AI Resolution

> **Strategic anchor**: Reduce cost of support · Flywheel stages: Orchestration, Agent Experience, Governance, Insight & Prevention · See [Care Capability Model](care-capability-model.md)

---

## Executive summary

80% AI resolution does not mean 80% less operational work. The work shifts from handling contacts to maintaining the system that handles contacts. The operating model risk is treating this as a cost-out exercise; the real imperative is building the governance, knowledge infrastructure, and escalation design that makes the 80% trustworthy.

---

## People and ownership

### **The human agent role fundamentally changes — from volume handlers to complex-case specialists**

The remaining 20% of contacts will be disproportionately complex, high-stakes, or high-tier. Agents stop being generalists and become specialists handling Premium/Enterprise escalations, regulatory complaints, novel issue types Fin cannot classify, and disputes requiring human judgment.

**Now**: Agents handle a broad mix of contact types across all tiers.
**2030**: Agents handle only what AI cannot. Hiring profiles, training, and baseline skill floor must reflect this.

Headcount does not scale with contact volume. It scales with complexity. The 2030 baseline assumption is ~500 agents across B2B and B2C. That number does not grow proportionally with transaction volume — it grows with the complexity and regulatory footprint of the remaining 20%.

### **Fin ownership must formalise before this model is load-bearing**

Current state: Fin is owned by the Product team with a virtual team of Content and Knowledge contributors. This is not a formal dedicated function.

**Now**: Shared responsibility works at current AI resolution rates because the consequences of a gap are limited in scope.
**2030**: Fin is the primary support product. Someone must be explicitly accountable for Fin resolution rate the way an agent team lead is accountable for CSAT. A coordination arrangement does not scale to this level of consequence.

---

## Systems and infrastructure

### **The knowledge base becomes infrastructure, not documentation**

Fin's resolution quality is a direct function of content coverage and accuracy. At 80% AI resolution, gaps or stale content cause systematic resolution failures, not one-off errors.

**Now**: Knowledge Manager maintains content reactively; ~60% taxonomy coverage.
**2030**: Content freshness SLAs are enforced, not aspirational. Knowledge Manager role is product-adjacent. Reflex gap detection (2027-2028 maturity) automates identification of missing or outdated content.

### **Escalation design matters more than volume handling**

At high AI resolution rates, the quality of the escalation path for the 20% matters more than the throughput of the 80%. Poor escalation design causes merchants who need a human to get bounced, context to be lost at handoff, and CSAT to decline despite strong AI resolution numbers.

**Now**: Escalated chats arrive with full transcript and taxonomy classification. Context exists but agents must interpret it manually.
**2030**: Agent Consultant assembles full context at handoff. Agents receive AI-suggested actions, not raw tickets. The escalation design covers two types: AI-to-human handoff (Fin to agent) and agent-to-team escalation (agent to Engineering, Treasury, or other business teams via Jira or custom API integrations). Both must be trackable from the support ticket so agents can update the customer without switching systems.

### **The support platform must support ~500 agents with strict data separation**

B2B and B2C operations are virtually separated by channel and agent team. At 500 agents, this cannot be enforced informally — it requires a walled permissions model in the support platform so that B2C agents (including any BPO) cannot access B2B customer data.

**Now**: Single Zendesk instance; B2C volume is negligible; separation is not yet an operational concern.
**2030**: B2B and B2C are materially different in volume, regulation, and team composition. Platform-level data isolation is a compliance and operational requirement, not a configuration preference.

---

## Measurement and insight

### **Quality assurance becomes AI audit, not agent coaching — and needs different tooling**

When AI handles 80% of contacts autonomously, failure modes are silent and systematic. A bad Fin Procedure or hallucinated answer goes out at scale before anyone notices. Operational Excellence must shift from reviewing agent interactions to auditing AI resolution quality at the cohort level, monitoring for systematic errors, managing the Fin Procedure library as a critical asset, and detecting when AI confidence is low and escalation thresholds need recalibrating.

**Now**: QA is sampling-based, agent-focused, qualitative.
**2030**: QA is data-tooled, AI-focused, quantitative. Reflex is not optional here; it is the reliability mechanism. Every closed ticket feeds Reflex — ticket close is the trigger for the Reflex data pipeline. This means the quality of Reflex outputs is directly tied to the completeness of ticket closure; tickets left open or mis-classified degrade insight quality at scale.

### **AI resolution rate needs to be supplemented with quality metrics**

At 80% AI resolution, the headline metric stops being sufficient on its own. AI resolution rate measures whether Fin closed a conversation without escalating — it does not measure whether the resolution was correct. A high resolution rate with poor accuracy is invisible until CSAT declines or re-contact rates rise.

Fin involvement rate (% of contacts Fin is applied on) remains relevant as a deployment breadth metric — there will still be contacts bypassing Fin that need to be brought into scope. But it is a coverage measure, not a quality measure.

**Now**: AI resolution rate is the primary measure of Fin performance.
**2030**: AI resolution rate needs to be read alongside:
- **Re-contact rate on resolved contacts**: merchants who contact again despite a "resolved" Fin conversation
- **Resolution accuracy rate**: resolved correctly, not just closed
- **Contact-type coverage**: percentage of taxonomy handled autonomously vs requiring human

---

## Commercial and regulatory

### **Cost structure inverts — but right-sizing human capacity is the hard part**

At $0.90 per Fin resolution vs $40 per human contact, the 80% deflection scenario is largely self-funding relative to volume growth. Fixed costs (agents, Zendesk licences, tooling) do not disappear automatically. The risk is holding over-capacity in human agents because headcount reduction requires restructuring, not just dialling down AI usage.

**Now**: Cost scales roughly with contact volume.
**2030**: AI handles volume growth; human cost is fixed around a specialist core. The operating model needs an explicit mechanism to right-size human capacity in line with AI performance gains.

### **Consumer Duty and regulated contact types require orchestration-layer guardrails**

At 80% AI resolution, the probability of a vulnerable customer receiving an AI-only resolution increases materially. Consumer Duty (live at B2C launch, 2027) requires vulnerable customer identification in Fin embedded before launch, complaint handling with 8-week SLAs routed to humans, and a phone channel live at B2C launch.

**Now**: B2B only; Consumer Duty does not yet apply.
**2030**: Regulated contact types must be identified and escalated at the orchestration layer. This policy cannot be left to Fin's judgment.

---

## How this connects to 2026 delivery

The 2030 operating model is only reachable if the 2026 foundations are built correctly. Key dependencies:

| 2030 requirement | 2026 deliverable that lays the foundation |
|---|---|
| Fin as primary support product | AI First Resolution Using Fin (Q2-Q3); Replace Webform with Fin (Q3) |
| AI audit and QA function | Reflex dashboards (Q1-Q2); Reflex MCP (TBC) |
| Knowledge base as infrastructure | Content gap analysis in Reflex; Merchant Education Hub |
| Escalation design with full context (AI-to-human) | Merchant Context for Fin and Agents (Q1-Q2); Agent Consultant (Q1-Q4) |
| Cross-team escalation design (agent-to-team) | Agent Productivity Tools: Zendesk/Jira integration (Q1/Q2); custom API integrations scoped H2 |
| Support platform multi-tenancy (B2B/B2C separation) | B2C Zendesk configuration (H2 2026); walled permissions design before wallet launch |
| Fin ownership formalisation | Must be resolved as a team/operating model decision in 2026 before scale |
| Consumer Duty readiness | Consumer support strategy planning (H2 2026) |
| Successor metrics | Support Model and tiering (Q2-Q3); Fin resolution tracking improvements |

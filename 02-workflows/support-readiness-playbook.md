# Support Readiness Playbook

This playbook defines Care's requirements for any product launch. It sits inside Checkout's wider product launch framework, giving Product teams a clear checklist of what Care needs before a launch is approved.

Two touchpoints:
- **Phase 1** — a lightweight declaration included in the PRD. No sign-off required, but completeness is checked at PRD review.
- **Phase 2** — a full readiness gate completed in the week(s) before GA. Care signs off before launch proceeds.

---

## When to apply this

Apply to any product change that has merchant-facing impact:

- New product or feature launched to merchants
- Changes to existing merchant-facing behaviour (API responses, error codes, flows)
- Deprecations or removals that merchants rely on
- Changes to a resolution path agents or Fin follow today

**Not required for:** internal infrastructure changes, performance improvements with no UX impact, backend changes with no merchant-visible effect.

---

## Phase 1: PRD-stage declaration

Include this as a named section in the PRD. Four required elements.

### 1. Product profile and known gaps

One paragraph describing what the product does from the merchant's perspective.

Document any known limitations or gaps at launch:
- Features not yet available at GA
- Unsupported geographies, currencies, or merchant segments
- Manual workarounds that will be in place temporarily
- Anything a merchant might expect to work that will not

Assign a contact risk rating: **high / medium / low / unknown**. Use the contact risk tags in `01-knowledge-base/products/product-definitions.md` as a reference. State the reasoning — e.g. "high: complex setup flow, likely to generate onboarding queries" or "low: backend change, no merchant-facing behaviour changes."

### 2. Anticipated query types

List the queries merchants are most likely to raise at launch. Aim for 5–10.

Write these as merchant questions, not internal descriptions. Examples:
- "Why is my settlement amount different from what I expected?"
- "How do I enable this feature for a specific processing profile?"
- "What does error code X mean?"

Care will map these to the support taxonomy once product scope is confirmed. Product and Ops Excellence should flag any queries that clearly don't fit existing taxonomy nodes — these trigger a Knowledge Manager review.

### 3. Documentation plan

List the support articles and technical docs that need to be created or updated:

| Type | Title | Draft owner | Target publish date | Status |
|---|---|---|---|---|
| Support article | | | | |
| Technical doc | | | | |

Also confirm: are any existing support articles or technical docs affected by this change? If yes, list them.

### 4. Data for resolution

What data does this product surface that agents or Fin will need in order to resolve merchant queries?

- List the data types (e.g. transaction status, account configuration, balance information)
- Confirm whether that data is accessible today via existing connectors
- If not: name the connector that is needed, the owner, and the expected timeline

If a data connector will not be available at GA, document the agent workaround that will be in place until it is.

---

## Phase 2: Pre-launch gate

Completed by the Product team in the week(s) before GA. All items must be checked before Care sign-off is given.

### Section A: Product and gaps

- [ ] Product profile confirmed — Care has a clear, current description of what the product does from the merchant's perspective
- [ ] Known gaps at launch documented and communicated to the Care team
- [ ] Contact risk rating confirmed or revised based on information available since PRD
- [ ] Care team briefed on expected query volume and any anticipated spike at launch

### Section B: Query coverage

- [ ] All anticipated queries from Phase 1 have been reviewed against current content
- [ ] Care has mapped queries to taxonomy nodes (Case Type → Issue Type → Reason)
- [ ] Net-new Reason codes agreed with Care Product and Knowledge Manager, and added to `support-taxonomy.md`
- [ ] Content exists or is confirmed to be published before GA for each anticipated query type

### Section C: Documentation readiness

- [ ] Support article(s) published, or publish date confirmed before GA
- [ ] Technical documentation published, or publish date confirmed before GA
- [ ] Existing affected articles reviewed and updated
- [ ] Articles tagged to correct taxonomy Reason node(s) and product in the Product Catalogue
- [ ] Coverage matrix updated in the Knowledge Graph

### Section D: Data and Fin resolution readiness

- [ ] Data sources for resolution identified — confirmed which connectors serve this product
- [ ] Fin has access to the required data, or a documented gap exists with an owner and timeline
- [ ] If a new connector is needed: confirmed available before GA, or agent workaround documented
- [ ] Agent Toolkit updated if new data context is needed for human agents

### Section E: Fin training readiness

- [ ] Content for Fin training published (support articles, snippets, or other knowledge sources)
- [ ] Fin Procedures created or updated for any new resolution paths
- [ ] Fin tested against anticipated queries — pass/fail rate reviewed and acceptable
- [ ] Fin content gap scan run — Intercom content gap recommendations reviewed

### Sign-off

| Role | Name | Date | Decision |
|---|---|---|---|
| Product team | | | Ready / Not ready |
| Care Product | | | Approved / Blocked |
| Knowledge Manager | | | Approved / Blocked |
| Process Architect | | | Approved / Blocked |

**Blocked** means launch does not proceed. The Care Product owner documents each blocking item with a target resolution date. Once resolved, the gate is re-confirmed before launch.

---

## Relationship to other workflows

**`02-workflows/product-release-content-workflow.md`** — covers how documentation is produced and published at ship time. Phase 2, Section C of this playbook triggers that workflow. Resolve the content gate in Section C first; the content workflow handles production and publication.

**`02-workflows/sop-to-runbook-conversion.md`** — agent-facing SOPs and runbooks are maintained separately. If this launch introduces new resolution steps for agents, flag to the Knowledge Manager to initiate an SOP update in parallel.

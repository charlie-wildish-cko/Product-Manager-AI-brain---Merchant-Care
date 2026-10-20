# Multi-Team Routing: How It Needs to Work — Vendor-Agnostic Overview

**Purpose**: shared with the case platform vendor and the AI agent vendor as design input. Not a finished spec. States the routing model we need for two distinct segments, B2B (Merchant Care) and B2C (Ray), and flags open design questions for each vendor to respond to. Vendor-agnostic: written to apply regardless of which case platform or AI agent we run.
**Owner**: Charlie Wildish
**Related**: `zendesk-current-config-flow-map.md`, `plain-business-case-draft-v1.md`, `04-active-work/meeting-notes/2026-08/2026-08-20-fin-in-plain-world.md`, `2026 deliverables.md` (Help Desk Platform Evaluation, Consumer Support — Ray)

---

## Scope note

This document covers two routing problems, not one:

1. **B2B — routing a ticket to a team outside Care.** Not tier/skill/regional routing within Care itself (that model already works and is out of scope here). This is about what happens when a Care ticket depends on a non-Care team to resolve.
2. **B2C (Ray) — routing across Care's own multi-lane model plus Compliance and BPO.** Ray has no existing platform to carry forward, so this is a from-scratch design, not a migration.

Throughout, "the case platform" refers to whichever system hosts and routes support tickets/threads, and "the AI agent" refers to whichever AI layer handles first-line resolution and escalation. Neither term implies a specific vendor.

---

## 1. B2B: routing to teams outside Care

### Problem today

Care depends on other teams (engineering, product, Treasury, DPO, Compliance) to close a meaningful share of tickets. Today this is manual: email handoffs measured in hours (Treasury) to weeks (engineering), with no shared system of record. The dependency and L2-transfer lines in the MBR exist because of this gap, not because Care itself is slow.

### Target model

- **Jira stays the system of record for engineering escalation.** Bi-directional sync (create/update from a ticket, status syncs back) is already a 2026 deliverable in progress. The case platform needs to support this natively, not as a bolt-on integration.
- **Non-engineering product teams are reached by a defined map, not ad hoc email.** We maintain a routing table of ~30 product teams (pillar, team name, Slack channel, whether they have Dashboard pages) — see `01-knowledge-base/processes/product-team-routing.tsv`. Today, escalation to these teams is inconsistent (some have a Slack channel, most don't have any defined path). The target state is that a ticket's product/case-type classification determines a defined escalation target from this table, not agent judgement.
- **"Log but bypass" pattern.** Every escalation to a non-Care team must create a record in the Care system first (for traceability and to preserve the SLA clock's original creation timestamp), then route downstream. The ticket does not need to sit "with" the destination team inside the case platform if that team doesn't work there — but the fact of the escalation, and its resolution, must write back to the original ticket.
- **Compliance and DPO handoffs need field-level segregation, not full visibility.** Some escalations (e.g. cardholder data removal requests, AML/screening outcomes) must reach the owning team without Care retaining visibility of the outcome or underlying data. This is a permissions problem, not a routing-destination problem.

### Design questions for the case platform

- Can a routing rule target an external system (Jira issue, Slack channel/message) as the "destination" of an escalation, while keeping the originating thread live and SLA-clocked in the platform?
- Where the destination team doesn't use the case platform at all (most product/engineering teams today), what's the recommended pattern: a linked object, a webhook-driven external thread, or something else? We want one pattern that scales across ~30 teams, not a bespoke integration per team.
- Can a workflow enforce "log but bypass" as a first-class step (create record → route downstream → write back on resolution), or does this need to be built as custom logic on top of the API?
- How does field-level or record-level segregation work for Compliance/DPO handoffs — can a ticket carry a downstream outcome that specific roles (Care agents) cannot see, while other roles (Compliance) can?

### Design questions for the AI agent

- The AI agent's role here is classification, not direct routing to non-Care teams. On handoff to the case platform, can the agent pass a structured field (not just free text) that identifies which non-Care team a ticket is likely to depend on, based on its classification?
- Confirm the AI agent does not attempt to hold or re-open a ticket once it has been escalated outside Care — resolution ownership needs to be unambiguous once a "log but bypass" escalation fires.

---

## 2. B2C (Ray): multi-lane and Compliance/BPO routing

### Target model

Ray's Care model, as scoped in `2026 deliverables.md`:

- **AI L1** resolves contacts across launch languages.
- **Escalates to a single L2 human queue**, split into lanes: KYC, Deposit & recovery, Disputes, Account ops, Complaints, Data rights.
- **And/or BPO overflow** for capacity.
- **AML/Travel Rule screening, sanctions/PEP, and KYC verdicts are Compliance-owned, not Care.** Care never sees screening dispositions — this is a silent handoff, not a queue Care can see into.
- **Vulnerable customers** are flagged via a CRM attribute by any frontline agent (or the AI agent, from defined signals), then routed to a trained specialist. The flag can gate AI eligibility so a vulnerable customer routes straight to a human, bypassing the AI agent entirely.
- **B2B/B2C data wall**: BPO agents handling Ray contacts must never see Merchant Care (B2B) data. A two-workspace (or equivalent isolation) architecture is required.

### Design questions for the case platform

- Can the six L2 lanes (KYC, Deposit & recovery, Disputes, Account ops, Complaints, Data rights) be modelled as a single queue with lane-based routing, or does this need six separate queues/workflows? We want the simplest model that still lets us report by lane.
- How does a "silent handoff" to Compliance work concretely: is this a linked record with role-based field visibility, or does the Compliance-owned outcome need to live entirely outside the platform (e.g. in a separate Compliance system) with only a status flag (not the disposition) visible on the Ray thread?
- Can a thread-level attribute (vulnerability flag) gate AI eligibility — i.e. prevent the AI agent from being invoked on a thread at all once the flag is set, rather than relying on the AI agent to check the flag itself?
- Confirm the B2B/B2C data-wall isolation extends to BPO agent accounts specifically — can a BPO agent's access be scoped to the Ray workspace only, with no search/lookup path into the Merchant Care workspace even by ticket ID?

### Design questions for the AI agent

- Vulnerability detection: the agent needs to surface a "suspected vulnerability" signal to the human agent (a verify prompt), not silently classify and act. What's the mechanism for the AI agent to write a flag that a human must confirm, versus a flag it sets unilaterally?
- Language handling: L1 resolution needs to work across all Ray launch languages before a contact ever reaches a lane. Confirm which languages are supported at launch and how a language-detection failure is handled (does it fail open to a human lane, or retry).
- Can the AI agent be configured to never invoke on a thread once a vulnerability or Compliance-hold flag is set on that thread, reading the flag from the case platform rather than requiring Care to manually pull it out of the conversation?

---

## 3. Shared dependency across both segments: taxonomy propagation

Both routing models above depend on ticket classification (case type / issue type / product / lane) to determine the destination team or lane. Taxonomy changes must propagate from the case platform to the AI agent automatically, with no redeploy, and no solution has been settled yet (options considered: platform-native thread attributes, an AI-agent data-attributes API, a central taxonomy JSON, or a config package). Whatever routing model is designed against the sections above needs to assume this propagation problem is solved separately — routing logic should read a synced classification field, not maintain its own copy of the taxonomy.

**Open question for both vendors**: does your proposed routing model assume classification fields are always in sync, or does it need to tolerate a lag between a taxonomy change and both systems reflecting it?

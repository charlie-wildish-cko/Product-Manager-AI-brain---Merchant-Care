# Strategic Review: Extending the Knowledge Graph to the Data Layer

**Topic**: Applying the knowledge graph gap-identification model to the Data layer — producing a unified resolvability matrix across both Knowledge and Data supply constraints
**Date**: 2026-04-20
**Update**: 2026-04-21 — Scope extended to all resolution actors (Fin, Agent Consultant, Human L1/L2). See section below.

---

## Verdict

**Strategically sound in concept, needs sharpening before leadership.** The diagnosis is real, the strategic alignment is clean, and the domain fit is unambiguous. What is missing is the operational spine: a sharpened Action Type taxonomy, a defined data edge state model, and a named write-path owner for data layer edges.

---

## Diagnosis

The pivotal difficulty is **resolvability blindness**.

Fin's failure modes are diagnosed post-hoc and in silos: content teams investigate content gaps, engineering investigates data gaps, and nobody has a single view of why a given Reason is unresolved. Without a unified model, investment decisions are made on escalations (lagging, reactive) rather than on the full population of Reasons Fin cannot close (leading, structural).

The extension names this challenge precisely: Fin resolution is gated by two independent supply constraints — content and data — and you cannot prioritise investment across them without modelling both against the same demand signal (contact volume by Reason).

This is a real challenge, not a manufactured one. The 15,000+ contacts per 6 months with known data gaps is evidence the blindness is material. The unit economics make it urgent: every Reason shifted from human to Fin resolution is a 44x cost difference ($40 vs $0.90).

---

## Strategic Alignment

This is future product strategy — not yet mapped to a named 2026 deliverable. The thinking establishes the structural direction for the Fuel layer beyond the current roadmap.

The connection to existing work is architectural: the data graph reuses the same entity spine as the knowledge graph (Reason hub, volume overlay) and adds one additional edge type. It does not create a second taxonomy. When the time comes to scope it as a deliverable, the natural anchors are Fin Procedures (data coverage as the Procedures backlog input) and the AI resolution rate ceiling (which cannot move without resolving both supply constraints).

---

## Flywheel Domain

**Fuel** — unambiguously. The Fuel domain is explicitly the Knowledge + Data layers. The proposal makes that pairing first-class in a shared data structure rather than two unlinked workstreams.

Secondary connections: **Insight & Prevention** (Reflex is the write path for both edge types) and **Orchestration** (Fin reads the combined graph at runtime to decide whether to attempt resolution). Centre of gravity is Fuel.

---

## How the Extension Works

The knowledge graph already has the structural foundation:

- `RESOLVED_BY` edge (Reason → Action Type) already exists in Phase 1 taxonomy
- Action Types already classify resolution patterns: Status lookup, Proof retrieval, Manual processing, Configuration change, Access/credential reset

The data graph adds one new edge type:

**`DATA_AVAILABLE_FOR`** (Reason → Data Source / Procedure) — presence of this edge means Fin has the data access needed to execute the Action Type for this Reason. Absence = data gap.

The combined view produces a **unified resolvability matrix**:

| Reason | Volume | Content coverage | Data coverage | Fin-resolvable? |
|---|---|---|---|---|
| Stuck in status | 1,200 | Yes | Yes (Payments API) | Yes — build Procedure |
| Balance confirmation | 409 | Yes | No — API TBC | No — data gap |
| Reconciliation issue | 290 | No | No | No — both gaps |
| API Error 4XX | 520 | Yes | No — logs not exposed | No — data gap |

This replaces two disconnected artefacts (content coverage matrix + data-access briefing) with a single ranked view of what Fin can and cannot resolve, and what is blocking each Reason.

---

## Edge State Model for Data

Unlike `COVERED_BY` (article exists or it does not), `DATA_AVAILABLE_FOR` has four meaningful states:

| State | Meaning | Action |
|---|---|---|
| No data source | No data source available for this Reason | Dependency on product team; track blocker |
| Data source, but gaps in fields/values | Source exists but incomplete for Fin's resolution needs | Define gap; agree data contract with owning team |
| Blocked | Security / legal / credential scope blocking integration | Resolve blocker; Procedure ready to ship |
| Live | Fin Procedure built and resolving end-to-end | Measure resolution rate; feed back into graph |

Collapsing these four states into a binary (available / not available) would produce a less useful version of the existing briefing doc. The four-state model is the minimum viable schema.

---

## Tensions and Risks

**1. Action Type is the hinge — and it is underspecified.** The Reason → Action Type → Data Source chain only works if Action Types are tight enough that each predictably implies a specific data shape. "Status lookup" currently spans Payments, Payouts, Settlements, and Disputes — each requiring different sources, scopes, and latency guarantees. Without a sharpened Action Type taxonomy, the graph produces misleading resolvability signals: the edge exists, Fin attempts resolution, and fails at runtime.

**2. Write-path ownership is unresolved.** The knowledge graph has a defined write path: Reflex + Content team. The data graph's write path is not yet defined. Who maintains `DATA_AVAILABLE_FOR` edges as APIs ship, scopes change, and Procedures are deployed? Fin administration is already flagged as a shared responsibility with no dedicated owner. This risk compounds if data edges default to manual PM maintenance.

**3. Combined graph must not fork the taxonomy.** If the data graph becomes a parallel artefact with its own entity definitions, rather than a strict extension of the knowledge graph's entity spine, coherence is lost. The Reason node must remain the single hub for both edge types.

---

## Hard Questions (must answer before sharing with leadership)

**1. What decision does the unified matrix make that the two separate artefacts cannot?**
Name the specific quarterly prioritisation call, investment trade-off, or leadership conversation that requires the combined view. If the answer is "it is cleaner," that is not sufficient justification for the modelling overhead. The answer should be: "It tells us, by contact volume, which Reasons Fin is one content investment away from resolving, which require an API dependency from another product team, and which require both — so we can target Q3 investment correctly."

**2. What is the full Action Type taxonomy, and who owns it?**
The entire proposal depends on Action Type being a reliable join key between Reason and Data Source. Before this goes to leadership, produce the full Action Type list with definitions, example Reasons, data-shape implications, and automation candidacy. The current eight-category draft is a starting point, not a finished artefact.

**3. How is a `DATA_AVAILABLE_FOR` edge created, validated, and retired?**
Name the system of record, the person or team who writes the edge, the validation mechanism (does a Procedure actually resolve the Reason in production?), and the cadence. If the answer is manual PM maintenance, the graph will be stale within a quarter and the matrix will mislead rather than inform.

---

## Scope Extension: All Resolution Actors (2026-04-21)

The original framing of the combined graph asked: *can Fin resolve this Reason, and what is blocking it?* The extended framing asks: *what knowledge and data does each resolution actor need for this Reason — and does it exist?*

This is a materially different question. The original scopes Fin as the only reader. The extension scopes the graph as the intelligence layer for the entire support operation: Fin (autonomous AI), Agent Consultant (AI-assisted human), Human L1, Human L2, and External actors.

**What changes in the model**

The `COVERED_BY` (Reason → Content Article) edge is replaced by `REQUIRES_KNOWLEDGE` (Reason × Actor → Knowledge Asset). Knowledge Asset is now a first-class entity class with four subtypes: KB article, SOP, escalation playbook, policy rule. The same Reason may require a KB article for Fin, an SOP for L1, and a policy rule for L2 — three distinct knowledge gaps, previously invisible because the graph only tracked the Fin-facing article.

The `DATA_AVAILABLE_FOR` edge gains an actor dimension: Reason × Actor → Data Source. A data source accessible to a human agent (internal admin portal) may not be accessible to Fin (no Procedure exists). Both gaps must be tracked and are distinct in type: one requires a Procedure build; the other requires a tool access change.

`HANDLED_BY` becomes multi-actor: Reason × Segment → Resolution Actor (primary), with `ESCALATES_TO` chains defining when and to whom escalation occurs. The routing question is no longer binary (Fin yes/no) but a ranked actor chain based on current knowledge and data coverage state.

**New analysis the extended model unlocks**

- *Handle time attribution*: Reasons with high L1 handle time and no `REQUIRES_KNOWLEDGE → SOP` edge mapped to Agent Consultant are structural AC configuration gaps — not content gaps, not data gaps.
- *Avoidable escalations*: Reasons with high L1→L2 escalation rate and no L1 SOP or no L1 data access are escalations driven by tooling/knowledge gaps. The graph distinguishes these from structural escalations (L2 is always right).
- *Total resolution cost ceiling*: Each Reason has a minimum achievable resolution cost if coverage is complete across all actors. The gap between current blended cost and that ceiling is the investment case for closing each gap.
- *Tacit knowledge mapping*: Reasons where agents resolve from experience but no SOP exists surface as high-volume, no `REQUIRES_KNOWLEDGE → SOP` edge. The graph makes these visible before a quality failure makes them urgent.

**What this does NOT change**

The diagnosis (resolvability blindness), the strategic alignment (Fuel layer), and the core model (Reason as hub, volume overlay, four-state data edge) are unchanged. The extension adds actor dimension without forking the taxonomy or creating a parallel entity structure.

**Governance implication (amplified)**

The original review flagged write-path ownership as the key risk for the data graph. The extended scope amplifies this. The graph now spans five knowledge asset types across four actor classes, owned by Content team, Process Architect, Operations Excellence, and Engineering. Each combination needs a named write-path owner. Without governance design upfront, some edges will be maintained and others will be stale within a quarter. This is the primary risk to address before Phase 2 begins — not the schema.

---

## Recommended Next Step

Produce the **Action Type definition doc** as a standalone artefact before modelling the data graph schema.

This is the single load-bearing dependency. Without it, the `DATA_AVAILABLE_FOR` edge is ill-defined and the resolvability matrix produces false positives. With it, the data graph is a mechanical extension of the knowledge graph and the Procedures backlog gets a durable, volume-ranked input.

**Scope**: One page. 8–12 Action Types, each with:
- Definition
- Example Reasons
- Data-shape implication (what data does Fin need to execute this action type?)
- Automation candidacy (Fin-resolvable / human-in-the-loop / conditional)

**Review**: Engineering Manager and Knowledge Manager, before the data graph schema is drafted.

**Timeline**: Before Phase 2 of the knowledge graph begins — Action Types must be stable before `RESOLVED_BY` edges are validated at scale.

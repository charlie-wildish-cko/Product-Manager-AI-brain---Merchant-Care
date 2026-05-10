# Knowledge Graph Layer — What It Means for Knowledge and Content

**Audience**: Preethy (Content Strategist)
**Author**: Charlie Wildish
**Date**: April 2026

---

## The problem it solves

Every contact that reaches Checkout's support operation requires two things to be resolved: the right knowledge, and the right data. Right now, there is no systematic way to know which contacts have adequate knowledge coverage — for any of the actors who might resolve them.

A human agent resolving a reconciliation dispute needs an SOP. An L1 agent escalating a payout failure needs a playbook that tells them when escalation is appropriate, not just who to escalate to. Fin resolving a transaction status query needs a KB article. Agent Consultant surfacing context to an L1 agent needs structured knowledge it can retrieve and present in real time. Each actor, each contact type, each knowledge need is currently tracked in isolation — or not tracked at all.

The knowledge graph changes that. It is a structured map of the entire support domain — every problem type, product, error state, and resolution action — that all knowledge assets can be checked against. Coverage becomes a measurement, not a judgement: which contact types have the right knowledge for the right actor, which are blank, and which are covered for Fin but not for the human agents who handle escalations.

---

## How it works

The domain is modelled as entities and relationships. The entity vocabulary covers 13 support domains, 37 problem types, ~103 reasons, 21 product categories, ~100 named products, 68 payment methods, integration methods, action types, and 4 B2B merchant segments. The Reason node is the hub — everything connects through it.

The graph models four resolution actors: **Fin** (autonomous AI), **Agent Consultant** (AI assistant to human agents), **Human L1** (first-line care agent), and **Human L2** (specialist/escalation). Each actor has distinct knowledge needs for the same Reason. A Reason mapped to "Status lookup" might be fully covered by a KB article for Fin, but an L1 agent handling the escalated version needs an SOP with step-by-step instructions, and Agent Consultant needs structured knowledge it can surface proactively during the conversation.

Four Knowledge Asset subtypes are tracked:

| Subtype | Who needs it | Who owns it |
|---|---|---|
| KB article | Fin, Agent Consultant | Content team (Preethy) |
| SOP | Human L1, Agent Consultant | Process Architect |
| Escalation playbook | Human L1, Human L2 | Operations |
| Policy rule | Human L1, Human L2, Agent Consultant | Operations Excellence |

Phase 2 maps existing knowledge assets across all four subtypes against the Reason vocabulary and produces a unified coverage matrix — which Reasons have the right knowledge asset for each actor, and which do not. Phase 3 overlays contact volume, so the matrix shows prioritised gaps: high-volume Reasons with no coverage for any actor.

---

## What this means for content strategy

The coverage matrix gives content prioritisation a data foundation it has never had. The highest-leverage content investments are Reasons that combine: high contact volume, no mapped KB article for Fin, and no mapped SOP for L1. These are contacts that neither Fin nor human agents can resolve well — and they are visible before they become escalations.

Two new dimensions change what "content gap" means:

**Actor dimension**: An article that covers a Reason for Fin is not automatically the right content for Agent Consultant to surface to an L1 agent. Fin needs factual, structured content it can retrieve and embed in a response. An L1 agent needs step-by-step instructions they can follow in real time. Agent Consultant needs content formatted for rapid surfacing — short, action-oriented, unambiguous. Where an article exists for one actor but is the wrong format for another, that is a content gap of a different type: not missing, but not fit for purpose.

**SOP coverage as a content signal**: High L1 handle time on a Reason with no mapped SOP is a content problem, not an operations problem. The matrix makes this connection explicit. When SOP gaps drive handle time, the content strategy needs to address them directly — not wait for an operations review to surface the issue.

It also surfaces product categories with no taxonomy coverage — Vault, Treasury & FX, Real-Time Account Updater, and others — where contacts exist but are miscategorised. These need resolving before Phase 2 content mapping can be complete: the taxonomy fix comes first, the content investment follows.

---

## Ownership

The Content team owns the KB article layer of the graph — the edges between Reason nodes and KB articles, the coverage matrix for Fin and Agent Consultant, and content prioritisation decisions. That ownership is more specific than before: it is not ownership of the whole graph, but ownership of one Knowledge Asset subtype and its relationships.

The Process Architect owns the SOP layer. Operations Excellence owns policy rules. Operations owns escalation playbooks. The graph makes the boundaries explicit — and makes cross-team dependencies visible. When a product changes, the graph flags every Knowledge Asset with an edge to that entity for review: KB articles (Content team), SOPs (Process Architect), playbooks (Operations). All at the same time, not sequentially after the first failure.

Each entity in the graph has a named owner for product entities (the responsible product team) and for resolution path entities — action types and reasons (Support Ops). Knowledge assets inherit accountability from the entity they cover, not from the team that published them.

---

## Immediate relevance

Phase 2 runs two parallel workstreams:

**KB article tagging (Preethy)**: Reflex runs LLM-assisted tagging against the 879-article library and outputs suggested edges as structured data — which article covers which Reason, for which actor. Preethy's role is to review those suggestions, not tag from scratch. Reviewing AI suggestions for 879 articles is hours of work; tagging manually is weeks. Reflex is high-confidence on product and payment method mentions (exact-match against entity names); Reason mapping requires human judgement and is where review effort concentrates.

**SOP tagging (Process Architect)**: Same workflow applied to the SOP library. Both workstreams feed into the same coverage matrix. Where a Reason has a KB article but no SOP, the matrix flags it as covered for Fin but not for L1. Where neither exists, it is a full gap.

The longer-term goal is authoring-time tagging: a mandatory taxonomy field in the Zendesk Guide publishing workflow means new articles produce graph edges automatically. This requires the Reason entity list to be stable, which is a Phase 1 completion criterion.

**Proposed next step**: 30-minute alignment between Charlie and Preethy to agree the Phase 2 review workflow for KB article tagging, confirm the actor dimension of the coverage matrix (Fin vs Agent Consultant mapping), and identify how the matrix feeds into the content roadmap for Q2/Q3 2026.

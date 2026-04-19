# Knowledge Graph Layer — What It Means for Content

**Audience**: Preethy (Content Strategist)
**Author**: Charlie Wildish
**Date**: April 2026

---

## The problem it solves

Fin's resolution rate is constrained by content coverage. Right now, there is no systematic way to know which products, payment methods, or error types have adequate Fin content — and which are blank. Coverage gaps are discovered reactively, from escalations and failed resolutions, not before Fin is expected to handle them.

The knowledge graph layer changes that. It is a structured map of the support domain — every product, problem type, and resolution action — that content can be checked against. Instead of reviewing articles by last-updated date, content coverage becomes a measurement: which nodes in the domain have mapped content, which are empty, and which have contradictions.

---

## How it works

The domain is modelled as entities and relationships. Phase 1 defines the entity vocabulary: 13 support domains, 37 problem types, ~103 reasons, 21 product categories, ~100 named products, 68 payment methods, the integration methods and action types that sit beneath them, and the 4 B2B merchant segments (Enterprise, Platform, Payfac, Issuing) that determine how a contact is handled. The Reason node is the hub — everything connects through it.

Phase 1b (now required before Phase 2) defines the relationship types that connect entities, and populates the first edges for the highest-volume contact types. This is what makes the graph traversable rather than a list of disconnected nodes.

Phase 2 maps existing Fin content against that vocabulary and produces a coverage matrix — a direct view of which Reason nodes have mapped content and which do not. The matrix distinguishes two gap types: **no content exists** (an article needs writing) and **no taxonomy node exists** (contacts are being miscategorised and the taxonomy needs fixing first). These require different interventions. Phase 3 overlays Fin query volume and resolution rate data, so the matrix shows not just gaps but prioritised gaps: high-volume nodes with no content coverage.

---

## What this means for content prioritisation

The coverage matrix replaces manual prioritisation with evidence-based prioritisation. The nodes that combine high contact volume, low Fin resolution rate, and no mapped content are the highest-leverage content opportunities — and they will be visible before they become escalations.

This directly supports the content strategy's guide programme. The Transactions guide and Balances & Settlements initiative are already targeting the highest-volume domains (PAYMENTS IN at 42.8%, FUNDS AND FEES at 7.5%). The matrix will show which specific reasons and products within those domains are uncovered, so guide scope is driven by data, not assumption.

It also surfaces the product categories that currently have no taxonomy coverage — Vault, Treasury & FX, Real-Time Account Updater, Intelligent Acceptance, and the 17 partner integration platforms. For some, contacts exist but are miscategorised under other case types. For others, there is genuinely no contact surface yet. The goal is no gaps — both cases need resolving before Phase 2 content mapping can be complete.

---

## Content ownership implications

The Content team owns the knowledge graph. This is not just ownership of the articles — it is ownership of the structured map that connects articles to the support domain. That means the coverage matrix is a Content team artefact, not a data or product one, and content prioritisation decisions are made against it directly.

Every entity in the graph has a named owner. Product entities are owned by the product team responsible for that product. Resolution path entities — action types and reasons — are owned by Support Ops. Content that maps to an entity inherits that ownership, making it clear who is accountable when a product changes and downstream content needs updating.

The end-state goal is that product release triggers flag entity-level content dependencies automatically — a change to 3DS authentication surfaces every article mapped to that entity for review before the change ships, not after the first Fin failure.

---

## Immediate relevance

Phase 2 requires the existing Fin KB article set (879 articles) to be mapped against the entity taxonomy. This will not be done manually — Reflex will run LLM-assisted tagging against the article library and output suggested edges as structured data. Preethy's role in Phase 2 is to review those suggestions, not to tag from scratch. The distinction matters: reviewing AI suggestions for 879 articles is hours of work; tagging 879 articles manually is weeks.

Reflex tags product and payment method mentions with high confidence (exact-match against entity names). Reason mapping — which problem type does this article solve? — requires human judgement and is where review effort is concentrated.

The longer-term goal is that tagging happens at authoring time: a mandatory taxonomy field in the Zendesk Guide publishing workflow means new articles produce graph edges automatically. This requires the Reason entity list to be stable, which is a Phase 1 completion criterion.
<<<<<<< HEAD
=======

**Proposed next step**: 30-minute alignment between Charlie and Preethy to agree the review workflow for Phase 2 tagging, confirm ownership of the coverage matrix, and identify how it feeds into the content roadmap for Q2/Q3 2026.
>>>>>>> b2bf67d126ac6b19d62bf7c51081c39b25dace9f

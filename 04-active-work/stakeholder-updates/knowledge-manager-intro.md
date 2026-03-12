# Merchant Care — Introduction for the Knowledge Manager

**From**: Charlie Wildish, Care Product  
**Date**: March 2026  
**For**: New Knowledge Manager, Operations Excellence (internal agent knowledge and SOPs)

This doc gives you the context you need to work with Care Product: what we own, how your domain fits in, where we intersect, and how to work with us day to day.

---

## Part 1: The Core

### What Merchant Care is

Care Product is the PM function for Checkout.com's support infrastructure. We own everything from the moment a merchant contacts support to the moment that contact is resolved or drives a product or content fix. We build the systems, tooling, and processes that operations runs on: the Fin AI Agent, Zendesk configuration, agent toolkit, routing logic, and insights product. We do not run day-to-day support; Care Operations does. We build what operations uses.

### The flywheel and where you sit

We think about the domain as a six-stage flywheel. Your work sits squarely in **Fuel**: the knowledge and data that power both human agents and the Fin AI Agent to resolve issues accurately.


| Stage                    | What it covers                                                                                                             |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| **Input**                | Channels (email, webform, Fin chat) and the query taxonomy that classifies what merchants ask                              |
| **Orchestration**        | Triage and routing: where the contact goes and who answers it                                                              |
| **Fuel**                 | **Data + knowledge**. Internal KB, SOPs, help content, and product knowledge that agents and Fin use. This is your domain. |
| **Agent Experience**     | Zendesk, Agent Toolkit, and the tools agents use to investigate and resolve tickets                                        |
| **Insight & Prevention** | Turning support data into product and content fixes so we prevent future contacts                                          |
| **Governance**           | SLA, QA, operational standards (more Ops than Product)                                                                     |


The flywheel spins faster when Fuel is strong: good content improves resolution rate, reduces handle time, and lets Fin deflect more. The target is 90% of content taxonomy covered by the knowledge base and 80% of contacts handled by Fin by 2030.

### The numbers that matter

We optimise for two north star metrics:

- **Contact rate**: Support contacts per 1 million transactions. We want to reduce it. Better self-service and content mean fewer contacts.
- **Cost per contact**: Average cost per support interaction. We want to reduce it. Better internal knowledge and Fin resolution mean lower cost.

Relevant context for knowledge:

- **Fin involvement is ~12% today**. Target is 80%. Fin’s ability to resolve depends heavily on the quality and coverage of the content it can use (and the data we give it). Your internal content and the customer-facing/Fin content (owned with the Content team) both feed that.
- **Taxonomy**: Queries are classified by Case Type, Issue Type, and Reason. When we talk about “content coverage” or “top contact drivers”, we use this taxonomy and dataset as the source of truth.

---

## Part 2: For the Knowledge Manager

### Why this matters to you

Your role owns the internal knowledge and SOPs that agents use every day. That content directly affects resolution quality, handle time, and consistency. It also feeds (in partnership with the Content team) what Fin can answer and what gets written for customer-facing help and Fin’s knowledge base. Care Product builds the systems that surface and use that content (Zendesk, Fin, Agent Toolkit, future agent-facing AI). We depend on you to keep internal knowledge accurate, structured, and aligned with how agents and tools actually work. When we launch new support flows (e.g. Platform, new products), we need your input so agent knowledge and SOPs are ready at go-live.

### How our domains intersect

- **Internal knowledge base and SOPs**: You own creation, structure, and maintenance. We own the tooling that serves it (Zendesk, any internal KB product, and how it’s exposed to agents). We need to align on what agents need to see, when, and in what format so that tooling and content stay in sync.
- **Fin AI Agent**: Fin uses content to resolve merchant queries. Customer-facing and Fin-specific content is led by the Content team; you’re the partner for internal process, edge cases, and anything that informs what agents (or Fin) should do. When we improve Fin’s procedures or add new topics, we’ll often need your input on agent-facing knowledge and escalation paths.
- **Taxonomy and contact data**: We use the support taxonomy and contact volumes to prioritise content and product work. You’ll use the same taxonomy to decide what to document, what to retire, and what SOPs to add or change. The same dataset drives Reflex (insights product) outputs that will highlight content gaps and top contact drivers for Product and Content.
- **New support models and products**: When we stand up new models (e.g. Platform support, new merchant segments) or new products, agent knowledge and SOPs must be in place. We’ll loop you in during scoping so you can plan content and process updates alongside our delivery.

### What we're working on in 2026 that's relevant to you

- **Improve Fin resolution through Procedures (Q2)**: We’re improving how Fin uses procedures and knowledge to resolve queries. This will touch both customer-facing content and the internal logic agents use when Fin escalates. We’ll need your input on agent-facing procedures and escalation expectations.
- **Platform support (Q1 onwards)**: Platform is a new segment: marketplaces with sub-merchants. Agents will need new knowledge (who the customer is, how to triage, Platform-specific flows). We’ll need SOPs and internal KB updates so agents can handle Platform tickets correctly from day one.
- **Reflex (Contact reasons reporting, Q1–Q3)**: Reflex will surface top contact drivers and content gaps from ticket and Fin data. That output will inform where Product and Content (and you) should invest. Your priorities for new or updated internal content can be driven by the same data.
- **Education Hub and onboarding (Q2)**: New merchant-facing education and onboarding content. The Content team leads; any overlap with agent knowledge (e.g. “what we tell merchants vs what we tell agents”) should be aligned with you so internal and external messaging stay consistent.

### How to work with us

- **New or changed processes that need tooling**: If a new SOP or internal knowledge needs to be reflected in Zendesk, Fin, or agent tools, raise it with me (Charlie) early. We can align on what we build and what you document.
- **Content or taxonomy questions**: For “how do we classify this?” or “what’s the source of truth for volume?”, we own the taxonomy and metrics. Definitions and datasets are in the knowledge base (`support-taxonomy.md`, `support_contacts_flat_table_2025_metric_definitions.md`). I can point you to the right place or walk through it.
- **Product or support model launches**: When we scope a launch that changes what agents do (new queue, new segment, new product), we’ll include you in the planning so agent knowledge and SOPs are on the dependency list and timelines are realistic.
- **Reflex and insights**: Once Reflex is live, its outputs will be a shared input for prioritisation. We’ll use them for product and content backlog; you can use them to prioritise internal KB and SOP updates.
- **Day-to-day**: Your primary Ops Excellence counterpart on the Care Product side is me. For Zendesk configuration (views, triggers, macros), the Zendesk Admins are the first port of call; for product and roadmap alignment, come to me. The Content Strategist (Content team) is your close partner for anything that spans internal knowledge and customer-facing/Fin content.

---

**Owner**: Charlie Wildish  
**Last updated**: March 2026
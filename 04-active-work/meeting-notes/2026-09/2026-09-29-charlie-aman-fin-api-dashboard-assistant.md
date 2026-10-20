# Charlie / Aman: Fin API and Dashboard Assistant

**Date:** 2026-09-29  
**Attendees:** Charlie Wildish, Aman Khare (product, Dashboard assistant and orchestrator)  
**Drive source:** 1iQIN_lLtelsnG_SeKufyXEGkoU_qEGlpMn1tx0H0-c8

## Context

1:1 on whether the Dashboard assistant and Fin should converge, and how the Fin API fits Care's Plain migration.

## Key Points

**Fin APIs**
- Intercom launched an in-house model ("Apex") and the Fin Agent API, the API version of current Fin. Fin can be invoked inside a ticket rather than via the chat widget.
- Fin on email works today because Zendesk assigns Fin as an agent. In Plain, Care assigns an admin user to the ticket and calls the API to respond. This is part of the H1 2027 architecture migration.
- Care also needs a Fin workspace for Ray and the B2B support migration (start Q1, finish Q2). Fin API adoption is "probably H1", timing unconfirmed.
- Replacing the Dashboard Fin widget with the API is not trivial. The widget handles payload, orchestrator and customer authentication (customer IDs, authenticated backend requests). The API requires building these manually. Fin configuration does not change: the API is a different entry channel.
- Design question: Fin and the Dashboard assistant coexisting vs one assistant with Fin behind it (the Stripe model). Deferred pending an engineering estimate. Aman sends requirements by 2026-09-30.

**Payments data**
- The MCP uses the public get-payment-details endpoint, which is less complete than BigQuery payment data. The data team migrated data last year, enriched it this year, and is building a semantic layer documenting every field.
- Fin, MCP and payment debuggers should use the same source and semantics to avoid inconsistent AI answers.

**AI vs UI**
- Bulk actions (bulk refunds built last year) fit the UI badly in chat. Single one-off actions (payment checker) fit AI. The assistant should state what it can help with and what is better done elsewhere.
- Design should research how users expect AI in the dashboard, with a hypothesis and metrics.

**MCP**
- Both view MCP as largely a marketing play with weak product-market fit. Payops teams are unlikely to use it, and developers do integrations rather than pay ops. Possible target: technical merchants such as eToro, who built their own AI agent for payments diagnosis (research case study). Long term MCP could be a hub for service connections.

## Insights

- Fin API adoption is coupled to the Plain migration, so its timing is set by H1 2027 sequencing.
- One payments data source and semantic layer must serve Fin, MCP and debuggers.
- Decision: Fin API integration timeline waits on the widget engineer's effort estimate.

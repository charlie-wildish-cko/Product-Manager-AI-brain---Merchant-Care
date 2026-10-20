# Fin payment lookup: email channel and auth architecture

**Date:** 2026-09-23  
**Attendees:** Charlie Wildish, Yifei Zhang (engineer). Referenced: Javad (customer bot), Lewis (Intercom solution engineer).  
**Drive source:** 1sLBPlgeOfzISHcDPlDb49WCF5eAiyerR2O5Fvk9fy1s

## Context

Doc titled "Meeting started 2026/09/23 15:17 CEST" (31 minutes). Design session on how Fin serves payment data to merchants without human involvement, especially on email.

## Key Points

**Data source**
- The public API Fin uses for payment data is being replaced by the internal lookup service (ID in, data plus BigQuery location out). Merchant-facing and internal support share it.
- Fin never calls the data source directly. It goes through the customer bot (Javad), with auth delegated via user permissions, not a public API.

**Security and infra constraint (Yifei)**
- Internal payment services live in a non-public subnet. Letting Fin call them directly means a new request pipeline, queueing for load, and a new public VPC. The existing Zendesk pipeline already batches and queues.
- The InfoSec agreement defines data scope, which limits leak severity but does not prevent a leak.

**Options considered**
- Yifei's original: return the answer straight to the Zendesk ticket from an internal service. Fin would not see the payment answer, so follow-ups break. Rejected by Charlie, who needs Fin in the conversation context.
- Intercom agent webhook ("wait for webhook" step in a Fin Procedure): rejected for this use case because it still needs a public entry point and new infra. Charlie noted manual refunds will need webhooks anyway (payment ID in, back-office spreadsheet, "manual refund logged" reply).
- Chosen: Intercom "Reply to conversation" API. Capture the Fin conversation ID, run the lookup outside Fin, post the result into the Fin conversation, Fin Procedure continues. Yifei's service can also read context by conversation ID and reply.

**Email vs chat**
- The bot gateway only forwards requests with a client access token. Email has none, so it needs a parallel flow: a new email procedure, a public callback (conversation ID, client ID, client email), and a service that fetches data and replies. Yifei suggested a separate "email customer bot".
- Charlie pushed back: answers must be consistent across channels, and two diverging bots is overhead to avoid. Wants Javad's view.
- Long term (Yifei): customer bot as orchestrator with sub-agents (e.g. payment lookup). Current client-access-token auth does not support it.
- Today on email: Fin reads from Zendesk, answers to Zendesk, Zendesk sends the email. Open question for Lewis: does Fin pick up a reply posted to the Zendesk ticket?

**Plain future state**
- Email uses the Fin API called by a Plain machine user acting as CX admin. The machine user can call the payment endpoint first and pass the result to Fin. Chat comes through Fin Messenger. Checkout controls the conversation-to-Fin handoff.

**Decisions**
- Aligned: payment API calls happen outside Fin. Results are posted into the Fin conversation via reply-to-conversation. Charlie: "a fair compromise because the outcome is the same."
- Deferred: cross-channel bot consistency, pending Intercom (Lewis) and Javad.

## Insights

- Fin never touches auth or data directly. All access goes through Checkout-controlled services.
- Email is structurally harder than chat because there is no access token. This caps Fin resolution on email until an auth design exists.
- Risk of two diverging customer bots. Orchestrator-with-sub-agents needs its own auth design.
- Fin-as-Zendesk-user limits control. Plain machine user plus Fin API gives Checkout control of the order of operations, a technical argument for the Plain migration.
- Manual refunds are the named future use case for Intercom agent webhooks.
- This is a long-term capability for the top merchant segment, not a throwaway build.

# Understanding the Role of Fin in a Plain World

**Date:** 2026-08-20
**Attendees:** Fraser Bryant, Charlie Wildish, Jiro Farah, Anish Mavadia
**Drive source:** 1H63Sx4MwFsOE9ztfIFAAS1zu5IOmu04nniVIG--E_eM

## Context

Architecture session on how Fin fits once Plain becomes the case platform, and what has to be owned in-house to keep vendors swappable.

## Key Points

- The Braavos team pivots to Ray. Services built for Braavos are not thrown away: the experience rails and processes port directly, only the banking-specific parts go. The pause landed as a surprise to the engineers, who had been shielded from the politics.
- Architecture vision: abstract data models away from vendors rather than baking vendor field requirements into services. One controlled chain of customer identity, routing, AI invocation, data processing, then Reflex. Fraser framed two visions, with Fin and (in roughly 3 years) without Fin. Charlie: Fin is a constraint, so in-house abstraction is what makes swapping technology possible.
- Channel routing: email lands in Plain first, then involves Fin. The chatbot starts natively inside Fin and escalates to Plain, which is the architectural exception, handled async via webhook. Charlie wants instant messaging added. Voice noted as a future channel.
- Web forms decline over time but stay for edge cases and Platforms, and may be served by internal AI rather than a third party.
- Taxonomy propagation is a hard requirement. Anna and AJ own taxonomy in Plain, and changes must propagate automatically to Fin. Options explored: Plain thread attributes, Intercom custom and data-attributes API endpoints, a central taxonomy JSON as source of truth, or a config package that re-syncs Fin on release. Fraser's constraint: no solution that forces a redeploy for every admin change. Open question for Intercom: how attributes work and whether a full schema must be supplied.
- Fin vendor assessment: feedback from Lewis at Intercom is that the APIs are robust and flexible and standalone Fin is viable, but feature parity between Fin versions and the billing mechanics of API-based use are unverified. Charlie's conclusion holds either way: build the abstraction regardless of vendor.
- Guest users and regulatory obligation: two categories where the FCA obliges Checkout to support end users it has no account relationship with, open banking payers and issuing cardholders. Mechanism is a discreet structured web form (transaction date, name, email, bank) rather than an email address, so agents can look the customer up. Open banking transactions carry a customer object with name and email; issuing cases resolve via cardholder name and contact on the card. Low volume, poor scalability, non-optional.
- User tiers (Helder's designation): guest (used a service, data held), registered or remember-me (signed-up email), verified (Ray full KYC). Verified and registered belong in the CRM; guests probably not, on volume and data-retention grounds, so they sit in a transaction log with a different enrichment mechanism.
- Enrichment: Braavos held transaction data embedded in single-row DynamoDB-style customer records. How Ray's crypto transactions will be represented is unverified, and Jiro needs those enrichment tables ready to start.

## Decisions

- Decoupled architecture abstracting services from vendors, with Plain as the central platform.
- Hybrid Plain plus Fin model for the next year, with a build-in-house bias and Fin retained as the primary service layer for support conversations.
- Email routing: everything into Plain, Plain triggers the orchestrator, orchestrator delegates to Fin.
- Build a gateway service listening to Fin events to auto-create matching Plain threads, so data stays consistent across channels and survives vendor change.
- Use Intercom's start-a-conversation-with-Fin API rather than granular use-as-a-tool actions. Keeps logic decoupled, lets Fin apply its own configured behaviour and escalation rules, and makes Fin available to any Plain ticket type including web forms.
- Centralised config-based taxonomy and attribute sync, auto-propagating to Fin with no redeploy.
- Consumer support on Plain: internal basic version December, external release end of Q1. December is deliberately not the full architecture, just a pass-through web form with taxonomy and a few fields.

## Insights

- The vendor comparison is deliberately scoped: Charlie will do a desk-based comparison of Intercom against Pylon rather than Salesforce, because benchmarking Salesforce implies Salesforce is not fit for the rest of the business. Pylon was already discounted early on architecture and model fit.
- Standing vendor rule: avoid tools acquired by large conglomerates, because absorption forces a future migration.
- Fraser's dependency: the Plain roadmap and estimates cannot be produced until this architecture vision is signed off by business and ops.

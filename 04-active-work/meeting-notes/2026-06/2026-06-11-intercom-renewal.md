# Fin / Intercom Contract Renewal

**Date:** 2026-06-11  
**Attendees:** Charlie Wildish, Lauren Coleman (Procurement), Rob King (Fin/Intercom AE), Adrian McKenna (Technology Procurement)  
**Drive source:** 1ZTCMBdnXiOohGWhjRX8yDABlreizeMoXSWJfJFd64aU

## Context

Renewal kick-off with Intercom AE and Procurement. Renewal due 1 July 2026.

## Key Points

**Product reliability issues raised**
- "Attributes" feature in Fin is currently broken — failing to detect any values from chats, which means all downstream classifications and routing rules in Zendesk are broken.
- Pattern: a new bug surfaces every 1–2 weeks, found by accident, reported manually. Acceptable at current volume; a systemic reliability risk at scale.
- Charlie stated this reliability level is insufficient to justify scaling Fin further.

**Zendesk integration uncertainty**
- Fin has made a decision to stop supporting the Zendesk integration for new customers but allows existing customers to continue. Discussions ongoing at Intercom exec level — no official update shared.
- Intercom's engineering team is in "lights on" mode on the Zendesk integration — deprioritising feature development. E.g. Fin sandbox ↔ Fin production linking (available in Salesforce version) blocked for Zendesk customers.
- If Fin sunsets the Zendesk integration, the entire Fin deployment (Messenger, Copilot, Fin for Zendesk) becomes unusable simultaneously.

**Contract terms agreed**
- **Termination clause**: Checkout can terminate without liability for unused fees if the Zendesk integration is turned off or becomes unusable. Rob King to investigate adding this.
- **Auto-renewal**: removed (was incorrectly listed as "yes").
- **Discount**: under discussion; Rob agreed to review.
- **Signatory**: Mariano (CTO), due to budget department change.
- Target to complete and sign before Charlie's leave on Jun 22.

## Insights

- The Zendesk integration uncertainty is Checkout's most significant structural exposure from a vendor risk perspective. The termination clause is the right mitigation — it ensures Checkout is not locked into paying for a broken product.
- Fin's acquisition by Salesforce ($3.6bn, mentioned in the Jun 15 Looker review) accelerates the case for building in-house AI capabilities that Fin calls via API rather than relying on Fin for domain logic.
- Rob King adding a dedicated customer support manager is a direct response to the reliability complaints — practical but doesn't resolve the structural Zendesk uncertainty.

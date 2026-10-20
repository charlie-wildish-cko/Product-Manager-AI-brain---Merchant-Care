# Research Readout: support tickets, Fin, analytics assistant queries

**Date:** 2026-10-14  
**Attendees:** Andrew Stager (presenter, dashboard UX; Gemini labels him "LON-06-11" in the transcript), about 18 invited including Charlie Wildish, Joseph El Choueiri, Alcinda Lee, Katie Hayward, Ana Escobar. Joseph, Alcinda and Katie spoke.  
**Drive source:** 1VVfe84kxfzoO9HFRvWu5guP7rwILgRsEyMR2eZJ9-r0

## Context

Dashboard UX research readout on what merchants ask support, Fin and the analytics assistant, to inform dashboard AI and guidance work.

## Key Points

**Method**
- About 3 months of summer support tickets, Fin chat logs for the same window, and a 30-day snapshot of analytics assistant prompts (initial prompt only, recovered from Datadog URLs).
- Pulled via the Looker MCP. Claude classified tickets and compared Care responses against docs, support articles and dashboard pages. If the answer existed in any of those, the ticket counted as self-servable. No human validation mentioned.

**Findings**
- About 70% of support tickets are operational status questions (what happened to this payment, dispute, refund). 35% of those include a payment ID. A Merchant Care forecast earlier this year reached a similar 70%.
- Fin: about 30% navigation or how-to, about 20% "how does X work / what does code X mean".
- Analytics assistant: about 70% compute rates, trends or breakdowns. About 10% are a pasted ID.
- Only about 15% of volume is a handover from Fin. About 85% goes straight to support (rough figure, source unclear, excludes internal teams). Alcinda: the CTA on each payment detail page is "raise a ticket", not open Fin.
- Merchant mental model: (1) what happened, well covered; (2) why, and is it normal; (3) what do I do. Merchants struggle with 2 and 3.
- Tier 2: of about 400 payment-status tickets, 55% were self-servable (Care restated page or docs data). 22% of tickets (about 1,000) are response-code questions, a long tail. Merchants cannot tell whether a decline came from issuer, scheme or Checkout risk rules, or if it is recoverable.
- Tier 3: of "what do I do" tickets, 40% the merchant could handle alone, 33% needed Checkout action, 22% were resummarisation. Permissions are an invisible blocker: blank pages with no "no access" message trigger tickets.
- Proof point: PDF proof of refund and void documents released in June cut related tickets to nearly zero within 2-3 months.

**Discussion**
- Joseph: payments page needs a UI revamp, not AI thrown at it. Response codes need AI to aggregate issuer, scheme and fraud codes into a one-liner. Defence layers before a human: explainer, decoder, conversational AI.
- Guidance work stream is evergreen, prioritised by support ticket value. Engineering slated for Q1. No global owner found.

## Insights

- Supports the contact-reduction case: about 70% status questions, over half self-servable.
- Changing the payment-detail "raise a ticket" CTA to open Fin is a cheap lever to shift the 85% direct-to-support share. Unassigned analysis: how many status tickets come from that CTA.
- The June PDF proof release is a replicable example of a product fix removing contact.
- Caveat: the self-servable classification is LLM-judged, and the 15% handover figure is unverified. Do not use as the Fin involvement rate.
- No formal decisions. Consensus on AI summaries, guidance and payments page UX together.

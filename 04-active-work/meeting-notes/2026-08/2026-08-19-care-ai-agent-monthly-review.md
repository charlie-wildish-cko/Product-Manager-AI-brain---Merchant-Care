# Care AI Agent Monthly Review

**Date:** 2026-08-19
**Attendees:** Charlie Wildish, Sebastian Garcia Cardona, Janny Chow, Ling Wong, Preethy Sundaresan
**Drive source:** 1p3PArmXlKaBgyVSwztz7agYfoblMk-Vo0xizMuR9SKY

## Context

Monthly review of Fin performance, dominated by Remitly-driven issues. Attached analysis: Chatbot Escalation Analysis (1VxPaTqyyPlptd12zXWmMrk4IN4dV5fUEgqHLKaBlZPk).

## Key Points

**Fin operational issues**
- Misclassification: Fin was labelling Remitly payout transactions as pay-ins. Charlie amended the classification guidance; the original was unclear.
- Reassignment loop: Fin stays assigned to a ticket even where human intervention is needed, generating repetitive tickets, because Fin is designed to keep responding until told to route to an agent. Fix: amend the Remitly view to include only tickets Fin has properly escalated.
- Duplicate tickets: user follow-up messages on the same transfer ID create new tickets rather than continuing the original conversation. Confirmed as a known dashboard bug under investigation.
- Payment ID flow: the new flow intercepts users and holds tickets in pending until a payment ID is supplied. Janny flagged that merchants often cannot provide one, and Charlie acknowledged the resulting frustration.
- Reference lookups: Remitly sends internal references in non-standard UDF fields that Fin cannot reliably recognise. Enable payment ID lookups first, explore reference-field checks later.
- Access: Janny's Intercom login failure was a region selection issue (must select Europe). Charlie to facilitate full Intercom access via Okta.
- Tracker discipline: link multiple related customer conversations to a single tracker ticket to quantify business impact. Janny to work back through the backlog.

**Product gaps surfaced as self-service candidates**
- Proof of payout: frequently requested, currently manual, no self-service. Tracker ticket to be raised.
- Proof of refund, capture and void: requested as merchant self-serve dashboard downloads, needed at entity level rather than only first-level client ID.
- Payout cancellation: currently requires manually asking the transactions team to cancel pending payouts. Automation needed for "pending" and "pending for review" (post-RFI) states.
- Statement of accounts: confirmed known gap, product team already working on it.

## Insights

- Fin's default keep-responding-until-routed behaviour is a live source of duplicate and repetitive tickets. The mitigation is queue-view filtering to escalated-only, not a change in Fin behaviour.
- The proof-document family (payout, refund, capture, void) plus statement of accounts is a coherent dashboard self-service package with a clear contact-reduction case. Entity-level access is the differentiating requirement.
- Non-standard UDF usage by a merchant breaks Fin lookups. Payment ID is the only reliable lookup key today, which forces friction onto users who do not hold it.
- Tracker-ticket linkage is the mechanism converting individual conversations into quantified product impact for prioritisation.

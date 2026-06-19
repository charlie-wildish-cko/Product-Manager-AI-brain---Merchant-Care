# Vesta (VMS) — Merchant Support Needs

**Meeting:** Will Stenson / Charlie — 2026-01-21  
**AM:** Will Stenson  
**Segment:** Tier 2, UK, payment facilitator / SaaS (cashless schools)  
**Drive source:** 1jLWIGF7SwSjUE29zfojVtuuhideju_N1W9oKALRKMFk

---

## Merchant Profile

Payment facilitator operating a SaaS platform for cashless school payments. Sells through wholly-owned subsidiary resellers (Tekassi, CRBC) to schools. Parents top up accounts for school meals, textbooks, etc. Set up as a commercial record model with Checkout.

---

## Support Channels Used

- Email only (reseller front-line agents lack dashboard access)

---

## Primary Support Needs and Pain Points

**Reseller agents locked out of the dashboard**
Vesta has not granted dashboard access to Tekassi or CRBC — its subsidiary reseller support teams — due to concern about cross-company visibility of payment data. All queries from the front-line come via email, despite most being dashboard-resolvable (refund status, dispute checks, double payments, payment confirmation).
> "They've not permitted any access to anyone outside of VMS itself. So anyone that's actually calling from the front line in terms of where these customer queries are coming in does not have access to the dashboard today."

**Autoresponse loop inflating ticket count**
Vesta sends queries from a shared inbox. Checkout's autoresponse triggers Vesta's own autoresponse, creating a loop that inflates the ticket count artificially.

**Agent knowledge gaps**
Vesta's support agents do not know they can provide an ARN to customers for refund verification. They escalate to Checkout instead.

**Query types**
Predominantly: unreconciled refunds, dispute/chargeback checks, double payments, payment confirmation.

---

## Key Insights

- The primary barrier to self-service is a Vesta access decision, not a product gap. Checkout cannot resolve this unilaterally — it requires Vesta to grant segment-based dashboard access to Tekassi and CRBC resellers.
- Segment-based dashboard access (each reseller sees only their entity's payments) is the right solution, but requires a conversation with Vesta about their data segregation concerns.
- The autoresponse loop is a Zendesk configuration issue — a suppression rule should be active, but its current status was unclear.
- Providing ARN-lookup guidance to Vesta's support agents would deflect a class of refund-verification contacts without any product change.
- This is largely an education and access problem, not a product problem.

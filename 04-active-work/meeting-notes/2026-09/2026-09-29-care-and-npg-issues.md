# Care & NPG Issues

**Date:** 2026-09-29  
**Attendees:** Charlie Wildish, Rehna Lalu (Care, Dubai, MENA and TPS focus, only Care person in region), Joshua Bedeau, Sean Jayakrishna (NPG product). Speakers anonymised.  
**Drive source:** 1xzu98fv8trN558NOwwguPBOCxs4IC1b7SeKGsE_LGgk

## Context

Charlie set up the session to hear Care's issues with NPG (National Payment Gateway, the new Saudi gateway rail) from the support side, with the NPG product team present.

## Key Points

**Migration state**
- Merchants are moving from the legacy rail to NPG, but MPGS stays as a permanent fallback. Some merchants have contracts requiring MPGS volume (Delivery Hero most notable).
- NPG has near-daily incidents per the engineering manager, so MPGS fallback is relied on heavily.
- Care tickets come from merchants, not cardholders. An end-customer order or refund problem is translated by the merchant into a payment ticket.

**Problem 1: payment status visibility**
- MPGS and Cybersource give L1 a portal login and Postman for status checks. For NPG the only route is Data Studio logs, with no guidance on where to refer queries.
- Timeouts on 27 July and 21 August 2026 drove the most common ticket: merchants asking whether a payment was captured on NPG before fallback.
- 27 July was unprecedented: schemes could not identify payment state, and establishing impact across thousands of transactions between Checkout, NPG and the acquirer took about 2 weeks. The data itself was wrong (success shown when not). 21 August was smaller. Rehna's tickets arrived within a week of each incident.
- NPG has no payment-state lookup API. MPGS has a portal and an endpoint (query by original transaction ID, 14-day retrieval). Building an equivalent at NPG is estimated at 3 to 6 months.
- Clearing work in progress will update gateway status to reflect rejected clearings and post-capture changes, giving an immutable after-the-fact record on the gateway dashboard. Expected to partly solve visibility.

**Problem 2: double capture on timeout and fallback**
- Sequence: NPG times out and Checkout sees a decline, retries on MPGS which captures, then NPG retries the queued original request and captures too. The customer is charged twice.
- NPG queues timed-out requests instead of killing them, which Charlie called a technology flaw. The same pattern appeared with Cybersource routing. MPGS also shows a decline then captures later, weekly.
- Options: poll status after any timeout, or wait for the timeout response. Both need NPG or acquirers as a source of truth. Alternative: ask the roughly 5 acquirers for a status endpoint, though leverage is unclear.

**Problem 3: manual refunds (Mada)**
- Mada allows programmatic refunds via the acquiring bank only within 30 days. After that Checkout collects payments manually and emails spreadsheets to the acquiring bank. This is standard across PSPs, so merchants expect it.
- Rehna's main pain is confusion, not product limits. Rehna and Joel are building a Glean agent to surface manual refund details.
- Automation idea: automate data collection into a validation spreadsheet (about 90% of the work) and keep the email send manual. SAP needs the merchant bank account number, constant across a merchant's MIDs, currently held only in the manual refund sheet. Template differs per acquirer.
- Charlie wants to avoid creating persistent manual debt.

## Insights

- Care is a downstream detector of gateway reliability gaps. Support volume for the 27 July and 21 August weeks is evidence for pushing NPG, banks and the central bank on resiliency and telemetry.
- NPG payment-state visibility is a dependency for any L1 or Fin "where is my payment" automation in MENA.
- Decisions: monthly Rehna and Charlie sync on support trends and NPG traffic vs support volume. No NPG escalation matrix committed (payment specialists remain the route). Charlie wants a Looker view of NPG traffic vs support volume, before and after migration.
- Transcript names for the Saudi partner are unclear and omitted.

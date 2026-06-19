# Visa SFTP/API Connections — Proof of Refund/Payout on V-Roll

**Date:** 2026-05-29  
**Attendees:** Charlie Wildish, Joel Petrosino (Care), Omair Mirza (Checkout), Brena Galvao (Visa), Katrina McGiver (Visa)  
**Drive source:** 1ji6U7XMEPm-nEr0IXzlWatRoztA_jaNL5udVuepSU-s

## Context

Discussion with Visa to explore whether the V-Roll manual proof of payment process can be replaced or automated. (Companion to the Mastercard proof of payment discussion on the same day.)

## Key Points

**Current process**
- Agents log into V-Roll (Visa's transaction reporting tool), generate a PDF, and send to merchant. Handle time: ~35 minutes per ticket. Volume: thousands/year.
- Request originates from merchants whose customers can't find a refund or payment in their bank account.

**What V-Roll proves — and doesn't**
- V-Roll proves the transaction was processed and delivered to the issuer. It cannot prove the issuer correctly posted it to the cardholder — outside both Visa's and Checkout's control.
- A Visa Query API exists but returns the same "processed" status as V-Roll. Requires additional data elements — more cumbersome, not less useful. API dismissed.

**Strategic shift**
- Charlie raised: Checkout may be over-servicing. Once Checkout proves delivery to the issuer, responsibility transfers. Brena agreed.
- The actual problem is largely issuer behaviour. Fix shifts from "build better proof tool" to "reduce contact volume by engaging specific problematic issuers."
- APAC/MENA issuers flagged as less reliable at posting transactions to cardholders.
- Brena offered to broker Visa contacts for specific issuer engagement — once Checkout provides a data-backed shortlist.

**Decision**
- Charlie and Joel to pull top 5 issuers and top merchants by proof-of-payment query volume, share with Brena.
- Targeted issuer engagement replaces technical automation as the primary strategy.

## Insights

- Proof of payment contacts are primarily an issuer reliability problem, not a Checkout tooling gap. The strategic lever is issuer engagement, not self-service tools.
- Fin can improve the first-touch response: serve the ARN/STAN directly with a firm statement that this constitutes definitive proof — reducing escalation to human agents without requiring a portal or API.
- Sheen mentioned again (also in the same-day APM session) — a priority merchant for a systemic conversation.
- Together with the same-day Mastercard discussion, the shape of the solution is: (1) pull STAN into internal data; (2) have Fin serve it directly; (3) use V-Roll/TI only as fallback; (4) engage issuers for the residual problem.

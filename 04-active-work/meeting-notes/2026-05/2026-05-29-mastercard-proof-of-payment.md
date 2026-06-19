# Mastercard Proof of Payment Discussion

**Date:** 2026-05-29  
**Attendees:** Charlie Wildish, Joel Petrosino (Care), Omair Mirza (Checkout), Marawan AbuAli (Mastercard), Vanessa Lopez (Mastercard), Svitlana Kogut (Mastercard)  
**Drive source:** 1aeq9HMCrnzFXK1hFXsxD3k04UAVkkya_PHcx5Zyz4rw

## Context

Formal discussion with Mastercard to explore whether the manual proof of payment process (V-Roll and Mastercard Connect portal) can be replaced or automated.

## Key Points

**Current manual process**
- Several thousand requests/year, ~4–5% of total support volume.
- Agents log into Mastercard Connect portal, search by ARN and date, download a PDF from Transaction Investigator (TI). End-to-end handle time: ~35 minutes per case, of which 15–20 minutes is portal login and retrieval.
- The critical missing data element is the **STAN (System Trace Audit Number)** — an immutable scheme-level identifier not currently stored in Checkout's systems.
- ARN doesn't always reach the issuer; STAN is needed so merchants can trace the transaction directly with their bank.

**Technical options**
- **API access to TI**: Svitlana flagged TI as highly secure — not everyone at Mastercard has access. Prior exploratory discussion with Checkout's disputes team in Mauritius. Feasibility unclear.
- **Extract STAN from clearing/auth files**: STAN is data element 11 in ISO 8583 auth (0100) messages. TI itself consolidates clearing file data. Checkout could pull STAN directly from auth messages and join to clearing records. STAN is an ISO 8583 standard — scheme-agnostic solution possible (covers Visa and others).

**Decisions**
- Two parallel investigative paths: (1) Charlie to check whether STAN is already being extracted from raw auth or clearing files with Checkout's card processing engineering team; (2) Marawan to consult Mastercard TI team about API feasibility.
- Marawan will use the volume figures (thousands/year, 35 min/case) to build an internal business case at Mastercard.

## Insights

- A single internal data enrichment (pulling STAN into Checkout's transaction metadata) could eliminate the portal lookup entirely for all schemes, not just Mastercard — this is a scheme-agnostic fix.
- This is a strong future Agent Consultant automation candidate: if STAN is surfaced in internal tooling, Fin or a Procedure could retrieve and return it without agent portal access.
- Mastercard's own internal dispute teams rely on TI manually for similar lookups — this is an industry-wide constraint, not a Checkout-specific gap.
- At 35 minutes × thousands of cases/year × ~$40/contact, this is a material quantified cost line. Compare to the scheme proof of refunds discussion from March 31 — both are converging on the same self-service proof document concept.

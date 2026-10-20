# Charlie / Hamish — Payment Index and AI Data Context

**Date:** 2026-09-16
**Attendees:** Charlie Wildish (PM, Merchant Care), Hamish Chreseson (Payments Data)
**Drive source:** 1yDdyoTA2qJGwLBfFsda7gu6K_wDCpMHNuACAnmH-3Og

## Context

1:1 to settle the architecture for giving the Care support bot real access to payment data: how the bot finds the right transaction, and how it interprets the fields it retrieves.

## Key Points

**The index**

- Worked journey: merchant's refund fails, payment search doesn't explain it, they contact Care, the Merchant Care support bot takes the merchant reference and looks it up in the payment index.
- Name is provisional. Both agreed it should become a **transaction index** so consumer (Ray) data fits later. No inherent limit on what it holds.
- The index's job is to identify the transaction entity and type so the right data source can be found. Query on an **ID**, not on "payments": most other data hangs off the ID, so dropping the payments framing simplifies it.
- Implementation is a **Q4 2026 payments-team item**, not a Care build. Charlie to confirm with Froz and agree which engineer picks it up. Goal: running by end of year.

**Context over skills**

- Core question: tightly scoped AI skills, or let the agent read schemas and semantics and judge which fields answer the question.
- Charlie's position: Care does not want the payments team to tell it why a payment failed. Care wants the fields plus the context of what the fields mean (field definitions, and where needed value definitions), so Care controls interpretation.
- Hamish's team has rewritten a large set of field descriptions to be intuitive to humans and AI: where the value came from, what it means, expected values, and when to look at a different field instead or as well. Example: gateway response code points to gateway response code description, or to the acquirer response if it arrived via that path.
- His team gets almost no feedback on descriptions. This is the first real test of them.
- Target model: the data houses the source of truth about itself, and any consumer of a certified data product gets that for free. Not payments-specific.
- Query surface does not have to be uniform, only context retrieval does. BigQuery is cheap for small teams but expensive at payments volume.
- Dashboard team is testing **SlateDB** as the store behind payment search, starting with card payouts. If it works, Care can query the identical data merchants see, with no duplication: the index says "card payout = this partition, look it up in SlateDB." Charlie's PLC streaming work lands in the same store.

**Fields reviewed for payment context**

| Field group | Status |
|---|---|
| Clearing statuses | Wanted, proceeding |
| TPA (MPGS, CyberSource) statuses | TBC. Root problem is status mismatch between third party and Checkout gateway: async call fails, gateway declines, third party retries and never writes back. CPA team is migrating Saudi merchants to MPG with a retry/reconcile mechanism and building the fix in gateway, so Care consumes it |
| APM statuses | Shelved. Same class of problem, but APMs are being replatformed and querying only tells you something is wrong without fixing it |
| Master transaction IDs | Come from the schemes, required by Visa/Mastercard for authentication on reversals. Only in the STP flow and BigQuery. Previously sourced from Hermes against the old STP version; tables have been redone and current location is unknown |
| Nexus | New micro site (VPN required) shows the schema. Two relevant stages: scheme has cleared the funds, and settled meaning Checkout received them. Both apply to captures and refunds, plus a clearing-failed state. By end of September Nexus expects essentially all Visa and Mastercard events |

- PL owns the Nexus and STP knowledge. STP team questions why Care needs the data.
- Charlie cares most about **settled**, linked back to the payment event so merchants can see it.

**Terminology**

- "Clearing" means different things by team. To STP/Nexus it is their own specific thing. To Charlie it is the stages between capture and settled.
- **Settled** (Nexus term: **cash matched**) = funds have landed in the merchant's balance with Checkout. Not the merchant's bank account.
- Jason wants clearing statuses pulled into gateway: today if clearing fails the funds never land in the balance and the merchant cannot reconcile.

**FX and financial actions**

- FX has no certified data products, so Care has neither the context nor an easy query path.
- Two recurring question types: fee attribution ("why was I charged X on this transaction") needing transaction-level breakdown split into scheme fee, Checkout fee and other; and settlement questions (where is my settlement, cannot reconcile against balance, why is my balance negative).
- Fee labelling is a problem in itself: a fee labelled "general" means nothing to a merchant.
- **Payment-to-settlement traceability is not reliable.** The dashboard shows it, but the link is inferred from overlapping date ranges (a payment captured in a range is assumed to be in the next settlement).
- An exercise is under way to make financial actions an official certified data product. Financial actions contains the real IDs. Charlie proposed putting financial actions in the query scope alongside payments so a lookup checks both.

## Insights

- **Architecture decision: context over skills.** No bespoke AI skills per payment problem. An ID-keyed index resolves entity and type, then the agent pulls raw data plus the semantic layer and reasons for itself. Test is Looker MCP for semantics in parallel with BigQuery for data. MCP is not mandated as the solution: the requirement is the flow, not the technology.
- If Fin or the Agent Consultant returns wrong payment diagnoses, the first failure mode to check is field description quality, not prompts. Hamish's team invited that feedback, which is a cheap lever Care owns.
- The payment index is another team's Q4 commitment. Care is a consumer and needs to track it, not staff it.
- Generalise to "transaction index" now rather than retrofitting for Ray later.
- Two blockers are deliberately unfixed: TPA status mismatch (waiting on CPA's MPG migration) and APM statuses (waiting on replatforming). If contacts spike in either, the answer is that data access does not fix it and the dependency sits with another team.
- Payment-to-settlement traceability being inferred from date overlap is a quotable data-integrity problem behind "where is my settlement" and "why is my balance negative" contacts. Fix path is certifying financial actions.
- "Settled" means in the merchant's Checkout balance, not their bank. Check against `01-knowledge-base/payment-domain/checkout-terminology.md` alongside the Nexus "cash matched" synonym.
- SlateDB could let Care query the exact data merchants see in payment search, removing the class of contact where Care and the merchant are looking at different numbers.

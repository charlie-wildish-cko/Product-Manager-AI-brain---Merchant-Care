# Merchant Care AI Resolution and Known Issues

**Date:** 2026-08-20
**Attendees:** Charlie Wildish (chair), Joe Graves, Milan Jani, Henry Zhang, Jason Dantzer, Joshua Bedeau, Manika Singh, Meron Colbeci, Helder Goncalves
**Drive source:** 1hW67E4joC-jMD4fE6XNJmFJvh7mIwlogTeSqXemLQu0

## Context

Charlie convened payment-lifecycle owners to name the upstream data gaps blocking Fin resolution. The 2026 plan is to resolve at least 40% of Care merchant volume through Fin, against a long-term aspiration of 80%+ automation.

## Key Points

**The three blockers, quantified as share of contact volume**
- TPA / MPGS issues in MENA: ~10%. MPGS and CyberSource integrations fail between statuses. Merchants see "captured" or "declined" when Checkout's truth differs.
- Clearing invisibility: 5-8%. Clearing is a real state between captured and settled that has never been exposed to merchants. Money that fails at clearing never reaches their balance, producing reconciliation mismatches. Not exposed on the dashboard or API, and not internally queryable, so Fin cannot answer it either.
- Settlement delays: ~5%. Settlements do not arrive on the promised date. Care checks, then Treasury manually checks portals such as JP Morgan to trace released funds. Not automatable today.
- Charlie's framing: these are fundamental payment-lifecycle issues that scale linearly with acquiring volume. They get worse as Checkout onboards more processing merchants.

**MPGS and NPG (Joshua Bedeau)**
- MPGS falls over often and gives little visibility. Worst in KSA where local acquirers lack stability and maturity, but the unreliability exists in all MPGS markets.
- NPG makes Checkout a certified gateway in KSA with direct acquirer relationships, replacing the MPGS-proxies-to-acquirer chain.
- Evidence: an 8-hour MPGS outage in July, and 500k payments moved to NPG in two days.
- Remaining gap: as a gateway Checkout still has no true status query during downtime, so manual effort persists, but direct network access makes asking the acquirer far easier.
- Feature completeness targeted before end of quarter. Outstanding: MIT processing and previous payment IDs, plus authentication not yet working in market. NPG adoption is ~10%; most KSA processing is still on MPGS via SAB.

**Clearing (Jason Dantzer) and settlement (Joe Graves)**
- Clearing work starts this year, delivery slips to Q1, and it exposes settlement information, not clearing. High dependency on Paul James's team as the source. Gateway-failure source work is 2027.
- Confirming funds arrived in the merchant's bank account is not possible. Confirming funds were debited from Checkout's account is, and is the strongest available evidence. The settlement-debited event is already released for scheduled settlements, covering 90% of TPV processed.
- A replatforming to unify all payout flows completes around end of Q3, then migration, aiming at a clean data source for the AI to consume. Joe is engaging Treasury, whose workload was hidden from his team.

**Henry Zhang on unblocking**
- There is a live track with Treasury on payouts driven by Platforms scaling (manual approvals, unmaintained data sources). Nexus is the data foundation and several merchant care use cases are already validated.
- What he wants from Charlie is a canonical document: key Care use cases, the data points each needs, the data owner for each, and a by-when. That becomes the contract and lets him rank Care's needs against other work.

**Milan Jani's challenge**
- "None of these are new problems, and they're problems that will grow." He pushed for a recurring forum with a clear action plan, explicitly including things they will live with, and asked whether the room needed to do anything to empower Charlie.

## Decisions

- Stop investing in MPGS, prioritise NPG migration, accepting loss of granular status visibility in exchange for direct network access.
- Short term, expose existing settlement data. Defer gateway-level status syncing to 2027.
- Establish a recurring data-driven round table on Care resolution, organised by Charlie, with metrics also taken into the monthly with Meron and Jani.
- Charlie to produce the refreshed use-case, data-point, owner and date document. Joe and Charlie to build the settlement interpretation playbook for the AI.

## Insights

- The exec in the room stated that consumer (Braavos) was paused in significant part because the Care team projected rapid headcount scaling, since it could not rely on AI to solve the problem. Care's automation ceiling is now directly gating what businesses Checkout will launch, with Platforms and SMB named as the next tests.
- Corollary from the same voice: "historically it's not been the AI that's been the blocker, it's the data that the AI has access to." H2 is the window to make that investment so 2027 scaling is knowable.
- Roughly 20% of Care contact volume is blocked on three upstream data gaps (10% TPA/MPGS, 5-8% clearing, 5% settlement). That is the arithmetic gap between current resolution and the 40% target, and the argument for why Care cannot reach the target through Care-side work alone.
- Timing reality: clearing and settlement data exposure is Q1 2027 at the earliest, gateway status sync is 2027, payout replatforming completes end of Q3 then migrates. Nothing here lands in time to move 2026's 40%.
- The current 10 / 5-8 / 5 percentages are estimates. Both Henry and Joshua said the forum only works if it is backed by real data.

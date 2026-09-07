# Charlie / Ling Monthly Sync: Clearing and Gateway Data Gaps

**Date:** 2026-08-11
**Attendees:** Charlie Wildish, Ling Wong
**Drive source:** 10qRGqArWyUlHc9oX2i2-N2kUHL5Ai2gtbSelQ3Ez7d4

## Key Points

**Visa 9E rejections**
- Visa 9E rejections are incorrectly included in the weekly clearing/scheme-reject file sent to Care. Care then asks merchants to capture via an alternative method while the clearing team separately resubmits the same transactions. Result: double-charge risk to consumers. Resubmission can drag up to a month.
- The clearing team initially claimed the scenario did not exist, then agreed to fine-tune the report to exclude Visa 9E rejections.
- Ling is pushing for a defined end-to-end process, including proactive notification to Care so merchants can be told transactions are pending clearing.
- The clearing team has spent roughly two years overhauling clearing data schemas, so old error-code mappings may no longer hold. An engineer is remapping statuses to events.

**Gateway reconciliation**
- The Gateway treats "captured" as final and performs no downstream reconciliation, so a clearing failure never updates dashboard status. Charlie: "they assumed that years ago and they never changed it and that's proven wrong."
- A Financial Infrastructure workstream is building a new transaction-data pipeline for the ledger, with clearing as a key event. Merging it into the Gateway is TBC and keeps getting pushed.
- Failure case: two refunds failed at clearing but were absent from the scheme reject file. The cardholder raised a dispute; the disputes team, reading Gateway data, saw the refund as successful and closed the dispute.
- Disputes lacks tooling access (clearing data is not in Looker) and had no proper engineering team for about two years. They have now hired around 10 engineers.

**AI agent and Fin task execution**
- Charlie is building an internal AI agent that Fin queries. Today Fin either uses knowledge or calls the payments API to look up a payment and cannot interpret the result. The new design passes the payment to the internal agent, which analyses it against all available data and returns an answer for Fin to serve.
- Benefit: access to all Checkout data including clearing and back-office systems not exposed in the Gateway, via a single secure API call, avoiding BigQuery-to-external auth complexity.
- Possible spin-out: an "analyse this payment" button on the dashboard payment page. Charlie's condition is that it uses the same data sources to avoid divergent answers.
- A new Intercom feature lets Fin pass queries or triggers to back office to execute a task. Refund reversal worked example: check eligibility (7-day window, eligible payment method), tell the customer it is processing, set a loop webhook, fetch the transaction, hit the endpoint, process the reversal, notify the customer, trigger the Treasury adjustment.
- Candidate automations: treasury lookups, refund reversals, manual refunds (today just data collection into a spreadsheet), TPA diagnostics, checks, follow-ups. Constraint is capacity, not feasibility.

**Consumer timing**
- Consumer support team model unresolved, likely BPO rather than in-house on cost and elasticity.
- Internal consumer launch October. External was January, now debated between January and April. Charlie wants the later date so consumer support is built once in the new system: "I don't want to rebuild twice."

## Insights

- Three internal data root causes block Care quality: Gateway treats captured as final, clearing has no stable APIs, disputes reads stale Gateway data. All three generate contacts and none sit under Care's control. The internal AI agent is the deliberate workaround.
- The lever with leadership is an evidence file of real merchant examples showing customer impact. The two-failed-refunds-closed-dispute case is the cleanest one.
- Fin task execution (trigger plus loop webhook) is the mechanism that turns Fin from an answering tool into an acting one. Refund reversal is the first target and its eligibility logic is already articulated.
- Dual-running two case systems blocks optimisation and may force splitting the team by system.

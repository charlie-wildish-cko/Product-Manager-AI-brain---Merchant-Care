# Joe / Charlie - Settlements data & Care

**Date:** 2026-08-24
**Attendees:** Charlie Wildish, Joe Graves
**Drive source:** 1Xw_OhiiLv0IrVk-Xvc8cBNleSZa03htdSDp1vyAbNds

## Context

Working session on settlement-related contact drivers, which data sources can answer them, and how the two split ownership before both go on leave.

## Key Points

**Settlement not received: the volume**
- Average 50 "settlement not received" tickets per week, with peaks and troughs. A long tail across many merchants plus occasional spikes: Desert Online Trading (Europe/MENA) filed 25 tickets in a single week in June, roughly 10% of that period's volume.
- Charlie shared the Looker report with Joe. It was previously shared with Callum, who was tracking webhook adoption against tickets.
- Hypothesis on contact behaviour: daily-settlement merchants know what to expect. Weekly and monthly merchants contact support almost immediately if settlement is an hour late.
- Scheduled settlements now emit a `debited` webhook, sourced from cash processing and transmitted through the same event stream as other events. Merchants must subscribe to receive it.

**Payment-to-settlement linking is wrong**
- The dashboard link is derived from capture date falling inside the settlement payout date range, not from actual inclusion in that settlement. Merchants have reported being unable to find a transaction in the settlement the dashboard says it is in.
- Alexa indicated a solution may land by end of year. Joseph L. owns the dashboard page, but it is unclear whether he knows the underlying data accuracy or where the data is queryable.

**Documentation is the cheap fix**
- Current docs say timing "depends on your configuration" (time zone, frequency) and cover currency holidays, but never state at what point a merchant should consider a settlement missing. A separate "Why is my settlement delayed?" article adds to the scatter.
- Joe wants a baseline docs page giving an expected time range by region and rail, with support content handling specific cases against that baseline. Also useful as a source of truth for CS and account managers.

**Escalation cost**
- When settlements are delayed, Care goes directly to Treasury, who manually check with banks using MT103s. Heavy manual work.
- A Treasury tool is coming that would let Care query this directly. Charlie is resistant: another tool that still requires a human is inefficient. Preference is a Looker report in the interim.

**Ownership and target model**
- Joe owns "which settlement was this payment included in" and "when will my settlement arrive". Alexa owns settlement reports, balances, and the Financial Actions API/reporting. Frank owns fee structures.
- Target model: Financial Actions shows, per payment, either "not included in a settlement" or the settlement ID. Each settlement ID maps to a settlement report listing the specific transactions and how they reconcile to the settlement amount.
- Merchants differ: some reconcile only via settlement report, others only via Financial Actions. Care angle: if Financial Actions is the source, Care and Fin call one data source.

**Other contact drivers**
- Fees: transaction-level fees (interchange, scheme, gateway, adjustment) are the issue, not missing fees. The problem is meaning and comprehension, plus unhelpful "other" buckets on statements.
- Gateway-only / TPA merchants using Checkout for gateway only still expect settlements from Checkout because nothing tells them otherwise. Identifiable via processing profiles and gateway settings. All-or-nothing accounts are easy to message; mixed-mode accounts are messy to derive. Known with some MENA merchants.
- Balances: most common queries are inability to reconcile balance figures and unexpected negative balances. Negative balances typically come from a volume of refunds through a currency account the merchant has not reconciled. Joe expects these rose after balance checks on refunds were introduced.
- MENA platform migration: all of MENA moves to a new platform currently carrying ~1% of volume and effectively untested. Josh claims it will fix existing problems. Charlie is nervous since performance versus status quo is unknown. Mitigation: track migration volume against MENA support tickets.

**Team**
- Vimal joins Joe's team from Treasury, 100% committed by October. Background in bank connectivity and treasury safeguarding / transactional ledger. Henry envisages him on client settlements and scaling treasury ops.

**Decisions**
- The Financial Actions API is the designated primary source of truth for merchant reconciliation and fee-related queries, and should ideally drive the dashboard from the same source.
- Work split: Joe takes settlement inclusion and settlement arrival. Charlie takes balances, reconciliation reports with Alexa, and fees with Frank.
- Quick wins: documentation content updates now. Webhook event and Financial Actions investigation as the deeper work.

## Insights

- 50 "settlement not received" tickets per week is a sourced contact-reduction number with an identified root cause (no stated "consider it missing after X" threshold) and a cheap fix (docs content). Unusually clean quick win.
- The dashboard payment-to-settlement link is date-range-derived, not real. Any Care answer or Fin procedure built on that link is unreliable until Alexa's fix lands. This is the blocker on the reconciliation contact type.
- If Financial Actions becomes the single queryable source, one Fin Procedure integration covers inclusion, fees, and reconciliation. That is the architectural bet worth defending.
- The gateway-only / TPA expectation gap is a self-inflicted contact driver with a plausible UX fix: tell those merchants not to expect settlements from Checkout.
- MENA migration onto a platform carrying ~1% of volume is a named contact-volume risk with an agreed monitoring approach.
- Charlie's stated principle on the Treasury tool: a new tool that still needs a human in the loop is not a solution. Applies beyond settlements.

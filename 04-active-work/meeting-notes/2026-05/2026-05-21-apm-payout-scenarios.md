# APM and Payout Scenarios Review

**Date:** 2026-05-21  
**Attendees:** Charlie Wildish, Xabi Telletxea, Keziah Zhou, Francisco Goncalves  
**Drive source:** 1T9wNcCd9RLzyLotU3IbYQ4y3LkprLicAYnPdBgIfMPA

## Context

Review of real support tickets (APM and card payout) to identify AI-resolvable issues vs. those requiring product fixes. Goal: reduce L2 ticket volume.

## Key Points

- **PRO gateway** (P24, Multibanco, Bank Contact, Swish): no specific decline reason returned. Dashboard shows generic 20000 code. Not documented. Prior attempt to get gateway provider to supply reasons was rejected. Classified as a data gap — not solvable by AI alone. Follow-up with APM gateway team (Hin and Abhishek).
- **Deferred/stuck APM refunds**: payments stuck in "deferred" because webhooks not received from APM. Current workaround: reconciliation call via Postman. Charlie pushback: product should fix missing webhook handling, not build a tooling workaround.
- **MB Way** (Sheen merchant, daily volume):
  - Vague error messages — no actionable reason.
  - Some MB Way accounts use prepaid cards that cannot receive refunds — merchants don't know this and keep retrying.
  - Timeout errors cause false failures where the refund was actually processed — duplicate retry risk.
  - Jira ticket exists to add specific decline reason codes — this is the right fix.
- **Partial refund complexity**: multiple partial refunds exceeded original payment amount. 20000 error gave no guidance. Root cause: MB Way timeout after successful refund; merchant retried; system rejected as exceeding refundable amount.
- **Pending payouts**: pass sanctions but fail at CP validation (e.g. non-Latin characters in name fields). Stuck in "pending" indefinitely — no automated status transition to "declined." Proposed interim: generic dashboard message explaining pending payouts may be held for compliance review. Long-term: CP team to define auto-decline-after-N-days rule.
- **Response code mapping sheet** (Excel): maps specific codes (e.g. 2014, 2054) to English explanations and recommended actions. Currently used in Intelligent Acceptance internally — sensitive but safe for Fin use since output is controlled. Plan: embed into Fin for payment data lookups.

**Three treatment buckets confirmed**: (1) AI knowledge base entry/article, (2) embed in Fin data lookup responses, (3) product fix required.

## Insights

- The 20000 response code is the single most common uninformative error surfaced to merchants. It appears across PRO gateway, MB Way, and deferred refunds — high-priority reference table entry.
- Sheen is generating recurring daily ticket volume from the same MB Way issues — warrants an AM-led systemic conversation, not continued per-ticket handling.
- MB Way is consistently the most problematic APM for refunds across multiple meetings. Warrants a dedicated product conversation with the gateway team.
- The response code mapping sheet already exists with actionable guidance — embedding it in Fin is a quick win that does not require new data work.
- The pending payout stuck-in-limbo gap is fully within Checkout's control (CP validation logic) — merchants have no visibility and no timeline.

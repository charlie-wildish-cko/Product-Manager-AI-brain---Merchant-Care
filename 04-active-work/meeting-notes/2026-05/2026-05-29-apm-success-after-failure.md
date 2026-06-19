# APMs & Success After Failure

**Date:** 2026-05-29  
**Attendees:** Charlie Wildish, Jason Dantzer (Gateway team), Abhishek M, Huilin Tu  
**Drive source:** 15Hgr2tnKPtuQTCzn4ambExau5dgvrkloXjGNsxzrTIM

## Context

Technical discussion with the gateway team to address APM status desyncs — a root cause of reconciliation failures and manual care agent intervention.

## Key Points

**Root cause**
- APM status desync between gateway and third-party providers causes reconciliation failures. Affected: MB Way, Tabby, Tamara, MPGS/MPG.
- Q1/Q2 partial fix shipped for some APMs — holding for some cases, not all.
- 400 unmapped APM response codes exist (Harry's analysis on Jason's team). Causes generic/undocumented error responses to merchants. Partial deploy of code mapping completed; more cleanup needed.

**MB Way specifics**
- Refund API calls time out. Agents must use the manual portal. Gateway cannot automatically initiate refunds via API in these cases.
- Long-term: MB Way replatforming in progress — expected to resolve some consistency issues.

**"Success after failure" event**
- Gateway can ingest status-change events from APMs if they emit a clear trigger with a spec — Jason confirmed this.
- "Capture" is treated as a final state downstream (treasury/finance) — cannot be changed to declined without breaking systems. Solution: introduce a new "success after failure" status.
- This event already exists as a public API event but has not been extended to the gateway.
- Internal Snowflake query used by Merchant Care to verify these transactions — not scalable.
- Strategy: one generic event for all APMs rather than per-APM implementation.

**Interim mitigation**
- Offload manual MB Way refund handling from Merchant Care to the Payment Ops team (Sim flow already being built).

**Decisions**
- Success-after-failure gateway event: Q3 to define specs and behavioural requirements; Q4 2026 implementation.
- Jason requested the Snowflake query used by Merchant Care for verification. Charlie to share.

## Insights

- The manual refund handling burden on Merchant Care is a direct consequence of missing event infrastructure — upstream of care tooling, not solvable by AI alone.
- 400 unmapped APM response codes is a quantified, actionable finding — drives merchant confusion and care contacts. Strong prioritisation case.
- The "success after failure" event is blocked by a downstream treasury/finance constraint (capture = immutable final state) — the new status approach is the clean solution.
- The upcoming SMB push (Platform, H2 2027) requires a self-service support model. High-touch TAM/care coverage is not viable at SMB scale — these APM product gaps must be closed before SMB launch.
- Sheen is generating daily recurring volume from MB Way issues — same merchant flagged across the May 21 APM scenarios session.

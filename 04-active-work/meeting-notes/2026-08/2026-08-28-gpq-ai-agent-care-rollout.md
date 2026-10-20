# GPQ AI agent - merchant care rollout

**Date:** 2026-08-28
**Attendees:** Claudia Zheng (organiser), Mohamad Ali Kalassina (AI engineer, AI Centre for Excellence), Raymond Guo (engineer, AICE), Tasha Richards (Payments Manager, Americas Treasury), Joel Petrosino, Charlie Wildish, Anthony Tsoi, Erin Kiley, Sebastian Chmielinski. Oliver Westlake-Simm invited
**Drive source:** 1JkBp4X5_abYUkaC-mglwnVAzsYJTBRoSTFJle7kijTU

## Context

Rollout planning for the GPQ (Google Payments Queries) AI agent, built by the AI Centre for Excellence to replace manual report-pulling for Treasury, now being extended to Merchant Care.

## Key Points

**Pilot results**
- Ran July to 27 August: 776 unique questions across four query types.
- Two weekly gates, both above 90%: 94.5% answer accuracy, 92.1% factual correctness. Cleared a final regression check against all 776 questions.
- Validation method: LLM-as-judge first pass, plus user approve/reject feedback, plus weekly regression gates.

**Capability**
- Four supported query types: inbound payment status, client settlements and payouts, currency accounts, adjustments.
- Supported identifiers: payment IDs (`pay_` prefix) or 10-12 character billing descriptors, settlement IDs, standard Checkout adjustment IDs, currency account IDs.
- Returns bank returns, chargeback returns, recent balances, funding figures, recent inbound top-ups.

**Care fit and gaps**
- Joel challenged how Merchant Care could validate correctness without Treasury-level expertise. Resolved by treating output as factual.
- Refund reversal use case: Care does a manual reversal, requests a manual adjustment from Treasury, gets an adjustment ID to pass to the merchant. The agent can retrieve data after the manual adjustment exists, but cannot remove Treasury from the initial reversal. Deferred.
- Bulk lookup gap: merchant requests are typically under 10 items but occasionally 100-200 adjustments. Only ~3-ID batches tested; the system is designed for single queries. Raymond to investigate bulk as a future phase.
- Adoption can be segmented between Treasury and Merchant Care via Okta auth once Joel supplies an allowlist.
- Future state discussed: a master triage agent with agent-to-agent routing between operational departments.

**Decisions**
- Merchant Care will treat GPQ agent output as factual. No requirement for Care agents to manually re-verify data before using it with merchants.
- Feedback mechanism changed from approve/reject to a single question: "Does this answer your question?" Rationale: users lack the expertise to judge factual accuracy, so intent-based feedback yields actionable insight on query coverage rather than vague satisfaction.
- Phased rollout: Treasury finance team live the following week, then Merchant Care senior analysts, then the wider Care team.

## Insights

- A second AI agent is entering the Care agent toolset, built outside Charlie's team and originally for Treasury. It overlaps conceptually with Agent Consultant's autonomous data-lookup mode. Track for duplication and for the master-agent routing question.
- Treating output as factual is a real risk transfer: Care will relay agent output to merchants with no verification step, on the strength of a 92.1% factual correctness score. That leaves roughly 8% of responses potentially wrong in front of merchants.
- AHT measurement will be tied to contact reason taxonomy. That uses the taxonomy as the measurement spine for AI ROI, and is a direct reason to keep taxonomy quality high.
- Bulk lookup, not accuracy, is the practical blocker for Care adoption.
- The feedback-design decision is reusable: when users cannot judge accuracy, ask about intent satisfaction instead. Applies to Agent Consultant feedback too.

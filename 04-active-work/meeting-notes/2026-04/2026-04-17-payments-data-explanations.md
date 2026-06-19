# Payments Data Explanations for Care

**Date:** 2026-04-17  
**Attendees:** Charlie Wildish, Shreya Alva, Jiro Farah, Imran Khan, Federico Arduini, Lachie Fielding  
**Drive source:** 1lidk_NzTxS-9y9L1ynaIBJSik811lAfnTLAzzU9wLYA

## Context

Working session on the architecture for embedding payment explanations into data, so Fin and agents receive pre-annotated descriptions rather than raw payment fields.

## Key Points

- Fin triggers were temporarily disabled due to performance issues and authorisation misalignments (Fin acting on tickets it shouldn't have). Root cause: triggers were unconstrained by case type, causing "issue type" to appear randomly.
- Internal AI tool assessed for generating explanations — rejected due to latency and cost constraints.
- Decision: pivot to BigQuery as the source of truth for payment explanations. Build a spreadsheet-based lookup table embedding payment explanations within data.
- Approach: mapping table (payment method + status + response code + authentication status → human-readable English description). This simplifies logic and reduces AI interpretation requirements.
- Bot gateway migration to query BigQuery directly deferred pending further technical clarity.
- API restriction affecting 5 daily form submissions to be resolved via a pending pull request.

## Insights

- The explainer table strategy (codified lookup rather than real-time AI interpretation) is architecturally significant — it makes Fin's payment explanations reliable and deterministic rather than dependent on LLM reasoning quality.
- This is the same "embedded knowledge in data" concept discussed in the Care 2030 Workshop (Apr 22) — these workstreams are converging.
- Trigger logic in Fin/Zendesk requires careful scoping — unconstrained triggers are a reliability risk at scale.
- Charlie was tasked with creating the initial 3-tab spreadsheet (payins, card payouts, bank payouts schemas) and presenting it in May.

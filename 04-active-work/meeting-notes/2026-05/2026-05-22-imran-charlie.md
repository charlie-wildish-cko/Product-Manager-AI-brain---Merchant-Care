# Imran / Charlie

**Date:** 2026-05-22  
**Attendees:** Charlie Wildish, Imran Khan (Data Scientist)  
**Drive source:** 1dfZo1rMtgQQm1tKSuInNc40QU7LPBza6uZe0krdKeyw

## Context

Working session on Agent Consultant architecture, topic modelling scope, QA automation, and platform migration direction.

## Key Points

**Topic modelling scope**
- Real-time deployment within 4 weeks flagged as risky due to emerging/evolving topics. Scoped down to top 5 case types/issues for PoC.

**Agent Consultant architecture**
- Imran to audit codebase. Current tool calls: payments lookup, knowledge lookup, Mastercard API (TPA status).
- To add: Zendesk knowledge (Guide/SAPs), payout fact tables (Shre's BigQuery tables for bank and card payouts).
- Semantic/data layer (the payments reference table) can be embedded in the Agent Consultant as a semantic layer. Fin Python transformation feature (new) allows managing this in Fin without BigQuery overhaul.

**QA automation**
- Self-QA tool proposed: runs at ticket close, compares what the Consultant said in internal notes against what the agent communicated to the merchant. Detects mismatches and measures whether consultant guidance is being followed. Agreed as the right QA approach.

**B2C / consumer expansion**
- Separate Fin workspace needed for Braavos consumer channel. Consultant logic must fork B2B vs. B2C to avoid cross-contamination.
- Internal employee launch: standard Zendesk routing, no Fin.

**Platform migration**
- Agreed in principle to move away from Zendesk.
- Shortlist: Fin, Plane, Pylon.
- Engineering (Helder) does not want to build in-house.
- Fin is a lock-in risk (same structural issue as Zendesk). Plane and Pylon are API/GraphQL-first, more flexible but younger.
- Andre indicated openness to hiring more in H2 to support migration.

**Classification accuracy**
- Current Fin case-type accuracy: 83% (40/48) in Charlie's Looker export test. Overall accuracy including issue type and reason: 69% — case type errors cascade down.
- Charlie tuning at case type level first. Disagreement rate proposed as a headline metric.
- Fin's classification disagreement chart already exists in the Fin dashboard — both Charlie and Imran largely unaware before this conversation.
- Human agent classification accuracy is probably ~80–83% — Fin is not worse than the human baseline.

**Fin bug identified**
- Fin got stuck in reassignment loop when requestor was changed to a merchant user but the ticket contained an internal note Fin couldn't read. Fix: add "internal email" as an explicit field value in routing logic.

## Insights

- Fin's case-type accuracy and human agent accuracy are roughly equivalent (~80–83%). The problem is not that Fin is wrong — it's that the human baseline is also ~80%.
- The consultant-as-data-layer (Fin calling a consultant backend for payment interpretation) is the architectural pattern that decouples domain knowledge from Fin.
- Platform migration is now agreed in principle — Pylum/Plane shortlist is active. Andre's H2 hiring signal is important context for scoping the migration engineering effort.
- The QA comparison tool (consultant vs. agent output) is the most robust way to measure actual consultant usage vs. just "guidance offered."

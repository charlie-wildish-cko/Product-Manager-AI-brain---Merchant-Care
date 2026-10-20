# Luca / Charlie: ops case management and periodic review

**Date:** 2026-10-13  
**Attendees:** Charlie Wildish, Luca Predebon (Ops leader: periodic review, onboarding, other ops teams)  
**Drive source:** 1wifuqAsI7VGpwthTdhk3AqjZ1frZh2R2oDEqb5AeWR4

## Context

Charlie walked Luca through the unified case management model for Checkout ops. Luca described current ops pain and where scale hits first. Gemini attributes all speech to one speaker (LON-05-08), so attribution below is inferred from context: Luca describes the pain, Charlie proposes the architecture. Action owners are unconfirmed.

## Key Points

**Current ops state (Luca)**
- Most of Luca's teams run on a basic Salesforce setup with queueing and reporting issues. Work happens mostly by email, with manual PDF downloads of attachments. Very little arrives on the dashboard.
- No granular statuses. Cases close as "case closed" with no record of approved, declined or escalated.
- No secure place for merchants to upload sensitive documents (passports etc.). Flagged repeatedly, never prioritised. No scanning of emailed or uploaded files for sensitive content.
- Ideal: automation requests the item, schedules chasers and gives a secure submission path, then ingestion to automation or human with AI assistance, granular reporting and customisable statuses.

**Periodic review: the biggest scaling concern next year**
- KYC/KYB refresh every 1 or 3 years. Low productivity from convoluted systems and manual merchant emails.
- First sub-merchant cohort from the platform product comes due next year. Monthly intake goes from about 100-150 cases to 450, at 1 to 2 days per case. Luca's only plan is temporary agents.
- The RA (risk assessment) tool has not delivered straight-through automation. The vision was auto-pass on the happy path, with humans reviewing failures only.
- Sub-merchant comms go via the platform by webhook. Checkout has no visibility of when webhooks were sent or whether chasers fire. Calls with platforms are being set up to define their responsibilities.
- Document expiry (passport, trade licence) prompts are manual: humans download reports and email merchants one by one.
- Luca's priority: if rollout is team by team, start with periodic review. If 80% can be automated, no hiring is needed.
- Outbound (Checkout-initiated) comms are underweighted in product thinking. Nobody can confirm it is covered.

**Prioritisation**
- Model ops teams like Care's scenario model. Data needed: volume, task types, handle time per case, cost (quality unknown). Luca requests volume data from Tim and talks to Seb on scaling analysis.

**Target architecture (Charlie)**
- Customer layer: unified view of any customer (merchant, platform, consumer) with all communications, KYC/KYB records and history. Gives auditability.
- Single entry point: one customer agent for all customer-initiated queries ("probably what Fin is doing today, but Fin is just for care"). Disputes and other channels unify or shut off, with triage routing.
- Checkout-initiated work: triggers, schedules and notifications create cases. Every piece of work has a case ID and a logged outcome, recording whether a human, AI or automation did it.
- Today's defect: a Care request routed to Disputes shows only the Care reply in the dashboard, so the request looks unresolved.
- Three building blocks: one interface layer shared by AI agents and human portals, an orchestration engine (routing by taxonomy, centralised permissions), and shared services (communications, payment data, KYC/KYB).
- Not building a custom unified tool. Plain is API-based, so one case management system plus one tool for actions is enough, with different UIs per use case if needed.
- The RA tool was meant to become a merchant risk 360 and belongs in the shared data layer.

**Roadmap and constraints**
- All Care moves to Plain by end of H1 2027 (end of June), driven by the Zendesk contract expiring. Check against `2026 deliverables.md` before reuse.
- Expansion to more ops teams starts H2 2027. Open: whether Ray's team is included.
- Constraint: engineering capacity (about 15 more engineers hoped for next year, with hiring and domain-training lag). Needs EP/exec-level sponsorship with ops and product investment.
- Luca asks product and engineering to shadow ops teams, especially in Malaysia.

## Insights

- The Care case model is becoming the Checkout-wide ops pattern, so Care/Plain configuration decisions have org-wide implications.
- Periodic review volume (150 to 450 a month at 1 to 2 days per case) is the hard business case for ops automation. Charlie owes a volume, handle-time and cost view for it.
- Fin is seen as the proto single customer agent, with ambition beyond Care.
- Unprioritised gaps: secure document portal, outbound comms, platform webhook visibility.
- Risk: engineering capacity and hiring timelines.

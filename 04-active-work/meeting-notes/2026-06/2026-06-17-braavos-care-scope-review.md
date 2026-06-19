# Braavos Care Scope Review

**Date:** 2026-06-17  
**Attendees:** Fraser Bryant, Ana Cachapa Cuomo, Charlie Wildish, Joel Petrosino, Ajay Paul  
**Drive source:** 1lSo0rbmjs1_-fjtCZxWxHmuj6ysN-QKka-JtZYs31xE  
**Reference doc:** consumer-care-h2-build-plan.md (Drive: 1UwbseEpjhWt9v4V35ZDGXR518RwCoPns11_uVdD_4Ik)

## Context

Planning session to finalise the Zendesk deployment strategy and regulatory requirements for B2C consumer support infrastructure. Phase 1 = plan by end of June (no build). Phase 2 = Zendesk build for ticket acceptance + consumer complaints.

## Key Points

**Phase structure**
- Phase 1: Plan only, due end of June. No build.
- Phase 2: Build Zendesk for consumer ticket acceptance. Agent toolkit is gated by the consumer team providing data sources — cannot go live without them.

**Launch timeline**
- October: base Zendesk configuration live.
- December: consumer complaint handling functionality live.
- 10% ticket sampling for QA to satisfy FCA regulatory obligations.

**Routing model**
- Taxonomy-based routing and assignment — tier-based routing removed for consumer.
- High-priority scenarios (fraud, APP claims, unauthorized transactions) route to specialised human teams.
- Standardised tagging for user segmentation and 2-hour SLAs.

**Regulatory decisions**
- FCA category mapping limited to complaint tickets only — not applied across full taxonomy (data hygiene).
- Consumer complaint SLAs mirror existing UK B2B standards: 15-business-day and 8-week framework.
- Consumer Duty and FCA DISP compliance baked into routing and escalation logic from launch.

**Data / CRM**
- CRM is the single source of truth. Zendesk configured as read-only for customer data — no writes to CRM from Zendesk, to avoid desynchronisation.

**Org model**
- External BPO agents: dedicated restricted role within the existing consumer brand. Separate from B2B agents. Data separation enforced.

**Phone support**
- Zendesk Talk implemented for initial phone support.
- RFP/assessment to be run in parallel for a long-term phone vendor to support future B2B and B2C needs.

## Insights

- The regulatory bar for consumer support is substantially higher than B2B: FCA DISP complaint handling, Consumer Duty, PSR-mandated fraud escalation paths, AML tipping-off rules, and Consumer Duty vulnerability requirements must all be live at October launch, not retrofitted.
- Zendesk Talk as interim phone is a pragmatic choice — but the RFP confirms it is explicitly a stopgap. This is a vendor decision pending, not a committed solution.
- The toolkit (Agent Consultant) being gated on the consumer team providing data sources is a planning dependency that needs active tracking. If consumer data sources slip, the toolkit cannot go live on the October date.
- October base config + December complaints is a tight H2 delivery window. Any slippage in the October base risks the December complaints deadline — and the complaints deadline is the FCA-driven one.
- The CRM-as-SSOT decision closes a loop on the broader centralised customer data discussions from multiple June sessions.

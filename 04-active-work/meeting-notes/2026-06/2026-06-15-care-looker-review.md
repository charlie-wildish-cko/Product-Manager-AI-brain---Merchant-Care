# Care Looker Review

**Date:** 2026-06-15  
**Attendees:** Charlie Wildish, Imran Khan (Data), Fraser Bryant (Engineering), Lachie Fielding (Data/Analytics)  
**Drive source:** 1x6sODmHXlsxzqM55GmBu5ndt_4zlcq1ryeHvq2xLNkE

## Context

Review session for the Care Looker analytics dashboard — identifying gaps, measurement issues, and H2 improvements.

## Key Points

**Fin deployment update**
- Fin for Tier 1 tickets going live.
- Salesforce acquisition of Fin ($3.6bn) discussed — concern it will be absorbed into Agentforce/Slackbot. Fin now uses proprietary models (not Bedrock). Accelerates in-house AI strategy.

**Funnel metrics**
- Automation rate = Fin involvement % × resolution rate = currently 13.4%.
- Resolution rate relatively stable; one unexplained dip being investigated.
- "General" case type to be added to Fin performance filters.

**Agent toolkit measurement gap**
- Currently tracked by whether agent clicks a payment in a ticket — blunt proxy.
- 67% of "accepting payments" tickets did not use the toolkit.
- Need to add payment ID detection flag to filter only relevant tickets before computing adoption rate.

**Agent Consultant measurement gap**
- "Usage" currently means the bot offered guidance (wrote a comment), not that the agent actively used it.
- 55% of relevant tickets not receiving consultant guidance — may be scope issue (bot may only trigger on payment-related tickets). Fraser to verify.
- Guidance scoring: Shre doing manual LLM-diff assessment; plan to automate. Quality gate before measuring ops impact.

**Handling time**
- Naive comparison (tool-used vs. not) shows tool increases time — confounded by agent and issue-type mix.
- Controlled Q4 2025 analysis showed ~10 minutes saved per ticket. Plan: push controlled analysis to reporting layer.
- Q3 plan: automated refund reversal button — cuts task from ~20 min to ~20 seconds. Measurable at the specific ticket subset level.

**Cost reporting improvements**
- Current dashboard is Zendesk-only — Fin-deflected tickets not visible.
- Fix: add Fin cost ($0.93/resolution) as a custom Looker measure alongside agent cost. Shows blended total cost view.
- Also add per-transaction cost.

**SLA metrics**
- First Reply SLA excluded from this dashboard (lives in ops team's own dashboard, managed by Tim).

## Insights

- The ~10-minute controlled saving is the credible handling time figure for the investment case — not yet in the reporting layer.
- Fin-deflected tickets are currently invisible in cost reporting. The blended cost view will be a significant reporting improvement — and likely changes the apparent unit economics materially.
- Agent adoption of tools is unknown (guidance offered ≠ guidance used). This is a foundational measurement gap affecting the ability to drive or prove tool ROI.
- The automated refund reversal button (Q3) is the highest-quality measurement opportunity — a specific, measurable task with a clean before/after.

# Checkout/Vercel on Plain experience

**Date:** 2026-09-18  
**Attendees:** Will Viles (Vercel, sole Plain administrator), Charlie Wildish. Fraser Bryant invited, declined.  
**Drive source:** 1Ukf6spdIWG3QTzcvhgjusscKcujX0wVWBSEfLM4gyw0

## Context

Reference call with Vercel on running support on Plain, as part of the support platform assessment. Will was on poor Wi-Fi, so parts of the transcript are garbled. Gemini transcribes Plain as "Plane".

## Key Points

**Why Vercel moved off Salesforce Service Cloud**
- Salesforce was a static data store built for email. Vercel wanted support to live in Slack, where its customers are.
- Vercel does not store customer data in the support tool. Fresh data loads into cards on demand.

**Why Plain**
- "Headless support": full GraphQL SDK and webhook-driven workflows, with all integration logic in TypeScript. Anything possible in the UI is possible via the API. Will called it "the gold standard" for customising the case flow.
- Zero downtime in about a year.
- Plain was strict about statuses at first. It has become much more configurable over the last 12 months.

**Delivery speed (main criticism)**
- Plain quoted 4 months for features Vercel needed. They took 8. Will: "not the fastest", "not exceeded expectations", but they do deliver. Vercel was customer zero for much of it.

**Operating model**
- About 1,200 cases per week, one administrator (Will), who also ran the migration.
- Config is managed through Vercel Edge Config and the API, not the UI. Labels are hierarchical (product > sub-product) and drive routing and analytics.
- Migration from Salesforce took about 2 weeks, done alone. Historical cases were not migrated because mapping the data model was not worth it. Checkout made the same call moving Salesforce to Zendesk.

**AI agents, all built in-house**
- Slack agent creates the case. Triage agent runs on creation and posts findings as a note. Retro agents run on enterprise cases. Documentation agents.
- Vercel is exploring Plain Sidekick (launched weeks earlier). Charlie described a similar Checkout target: Sidekick triggers Checkout's own AI agent at human-escalation triage.

**Gaps**
- Separate workspaces for RBAC and data privacy complicate cross-team work. Plain shipped user impersonation via API that week, and has label-based visibility permissions. Charlie wants most teams in one workspace and does not see this as a blocker yet.
- Native integrations are basic (Linear). Vercel built custom Next.js forms, agent-prefilled, that mutate threads via API, in place of static snippets. Will has pushed Plain for about 6 months to make this native.

**Charlie on Zendesk (on record)**
- No configuration-as-code, confusing concepts (triggers, automations), Checkout not treated as a large customer, vendor not a tech leader. Charlie wants a vendor that builds with Checkout.
- Plain gaps found so far are features, mainly detailed SLA levels. No major red flags.

## Insights

- Validates Plain on API-first flexibility, reliability and one-person operability at about 1,200 cases a week.
- Price in roadmap slippage: Vercel saw 2x the quoted delivery time. Checkout's SLA gaps are exposed to the same risk.
- Expect to build custom forms for Jira linking. Native tracker integrations will not cover it. Consistent with the other reference customer that built its own tracker linking (see `support-platform-assessment-customer-references.md`).
- Skipping historical case migration now has two precedents: Vercel and Checkout's own Zendesk migration.
- Vercel's in-house agent architecture on Plain matches Checkout's target model.

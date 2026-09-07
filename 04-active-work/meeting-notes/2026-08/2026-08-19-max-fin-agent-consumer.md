# Max / Charlie: Fin as the Consumer AI Layer

**Date:** 2026-08-19
**Attendees:** Charlie Wildish, Max Rothman
**Drive source:** 15RXeSJAABi7n_vapXWlIBsk-UA1kBqBlaYaXxphAM-E

## Context

Working session on how Fin is configured for Ray consumer support, following the decision to use Fin on the back of merchant-side results.

## Key Points

**Taxonomy**
- Max built a first-pass taxonomy skeleton in Charlie's requested format, with an added column for who handles each item (sanctioned-actor deposits route straight to compliance). He added roughly 50 scenarios. Incomplete on sub-issues and multi-intent permutations.
- Charlie is testing the taxonomy in Claude plus Gemini deep research on crypto support issues, and will add on-chain traceability scenarios (failed or missing deposits, blockchain lookups).
- Vulnerability and duty-of-care sections will be cut down substantially because Ray is not under SCA. Charlie will mark them TBC. Max removed clearly unnecessary items and left discretionary ones as N/A (romance scam: help because we should, not because we must).
- Agreed principle: no immediate resolution or provisional funds. For chargebacks, wait for the outcome then refund if the customer wins.

**Fin mechanics and coverage**
- Fin answers only from supplied content, with no internet access. Good for control and traceability (answers cite the source article), but content coverage across the full taxonomy is a hard prerequisite for launch.
- Coverage method: for each taxonomy item, if a product feature solves the problem it becomes self-service; if not it becomes a defined escalation path. Weight items by expected volume to forecast deflection.
- Volume hypothesis with no consumer history: access/login, transaction tracing, and disputes as the top three, possibly around 80% of volume. Benchmark: 60% of merchant support volume today is pay-ins or payouts.
- Content syncing: merchant Fin already syncs help-centre content, technical documentation and API reference docs weekly, and GitHub sync is supported. Principle: never author content inside Fin, because it strands content in a third party.
- Procedures are the AI equivalent of an agent SOP and can call APIs and data connectors. Data connectors are not needed day one. Max's future candidates: card delivery via UPS tracking, dispute status via the Disputes API, transaction detail via the Issuing API.
- Care Gateway: an abstraction layer between Fin and internal services, so Fin never integrates directly with 15 APIs and third-party auth stays monitored. Fin also supports MCP. The open problem beyond fetching data is interpreting a raw payload into something meaningful for the user.

**Commercials and cost design**
- Intercom charges per outcome. An outcome is a successful resolution with no follow-up, or a smoothly handled conversation where Fin collects information and hands off. The Fin renewal already accounts for consumer volume pricing, originally scoped for Braavos, so no commercial change. Separate workspaces carry no platform cost.
- Cost strategy: do not let Fin become the default fallback. Design answers inline, in context, at the screen where the problem occurs. Max suggested gating simple FAQ answers behind an in-app FAQ, and floated gating the chat function at launch. Charlie's warning: at scale, an accidental extra 3% deflected through Fin is around 20,000 of cost. Inline-versus-chat design assigned to Max's designer.

**Workspaces, escalation, tooling**
- Separate merchant and consumer workspaces, never blended. Segmentation within a workspace uses Audiences plus customer attributes. Merchant audiences segment by tier and channel. Consumer candidates: subscription plan (free/pro) and region. Plan attributes enable upsell answers; region attributes handle service availability gaps.
- Tone and escalation rules are natural-language configurable, with attributes usable inline.
- Escalation: Fin has a native Zendesk connector, creating the ticket with transcript plus summary notes and passing an attribute such as "escalate to X," after which Zendesk triggers take over. Charlie's preference is routing everything through Care first to preserve threading and traceability. Direct integrations (Fin to Salesforce) are not plug and play and are hard to rip out. Long-term preference is an EP-built orchestration layer.
- Tooling traceability: separate work assignment from work execution. The task lives in the case system, the work happens in Sphinx, and completing it in Sphinx updates the case with the outcome, which can be surfaced back to the customer via an in-app inbox.
- Named blocker: operations runs on email inboxes across teams, which cannot support automation. Fine at launch volumes, needs an orchestration layer to scale.
- Launch dependencies: customer context attributes feeding Fin, and the content library. Charlie's team handles in-app Fin installation. Seb is being consulted on content; the Braavos content plan mapped content to each taxonomy area and Charlie will check its status. Max offered Ray as the sandbox for testing new automation approaches at low volume.

## Insights

- Fin is the confirmed consumer and Ray support layer, with consumer volume already inside the renewed contract.
- Only two hard launch dependencies: customer context attributes and content coverage. Data connectors are out of scope for day one.
- Cost architecture is a design decision, not a support decision. Per-outcome pricing means the app must answer inline.
- Ray falls outside SCA, so vulnerability and duty-of-care scope shrinks materially versus the Braavos assumption. Reconcile against existing B2C Consumer Duty framing in the knowledge base.
- Escalation routes through Care first to preserve threading, then fans out. Long-term target is an EP orchestration layer ahead of the Zendesk exit.

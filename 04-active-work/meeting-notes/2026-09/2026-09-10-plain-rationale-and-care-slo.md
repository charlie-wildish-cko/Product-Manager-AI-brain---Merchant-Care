# Regular catch up with Charlie (Sunil)

**Date:** 2026-09-10
**Attendees:** Charlie Wildish, Sunil Mudaliar
**Drive source:** 14BzBzW8z7JWsMjLX_ppKkIMIBXeOFu7E2s5WAnfv3zo

## Context

1:1 covering the Care SLO dependency problem Ashwin raised, and the clearest articulation to date of why Plain and not Intercom Suite.

## Key Points

**Care SLO and dependencies**
- Ashwin raised that ~20% of turnaround performance is affected by internal team dependencies. Sunil discussed with Joel and identified a Care configuration update expected to give a 17% uplift.
- Charlie: dependency mix varies by type, with Treasury historically the highest-volume dependency, driven by missing tools, technology, data, and access permissions. Example: bank statements require manual logins to the JP Morgan portal. Refund reversals could be automated with existing tools but still need manual adjustments and Treasury notifications.
- Charlie noted his team is stretched and operations has not supplied explicit requirements or a backlog for these dependencies.
- Ashwin's dashboard was judged fairly inaccurate by Charlie and Joel, but the 16% cumulative unassigned share still needs investigating. Both agreed unassigned items internal to Care have no excuse and must be fixed directly.
- Disputes trended efficiently then dropped in July and August. Charlie attributed it to volume and external factors (remittance, specific merchants) rather than process decay.
- A newly rolled-out finance read-only feature is assumed to cut finance-related queries by 10-11%, though journal entry approvals still block full automation. Treasury's new agent tool helps with read-only questions but does not solve bank statements or refund reversals.

**Why Plain, not Intercom Suite**
- Charlie is strongly positive on Plain for its flexible, API-driven, modular architecture.
- Intercom Suite is ruled out because Salesforce acquired Intercom and is expected to break the Suite features into Service Cloud. Charlie treats Intercom Fin as a separate AI-agent proposition, judged on its own.
- Final platform decision is left to operations leadership.

**Architecture thesis**
- Two distinct buckets: receiving work, and finding answers to solve work. Merging them into one SaaS vendor creates complexity.
- A fully custom Uber-style build is impractical (hundreds of engineers). A central work-distribution hub plus specific action portals is realistic.
- Short term, build an orchestration layer to sync work, statuses and SLAs across systems. Sunil raised transition-period disconnect risk. They weighed the orchestration layer against migrating all teams to one system over time, set against maintenance cost.
- Sunil's comparison: JP Morgan Chase uses Salesforce for call routing and finance case management, and any tool needs significant time, effort and ongoing support.
- Charlie's bottom line: regardless of long-term uncertainty, Care must move off Zendesk.

**Plain product detail**
- Simple UI. Extensible data model with custom objects and attributes. Threads instead of tickets for ongoing multichannel conversations (email, forms, Slack).
- Visual left-to-right workflows against Zendesk's abstract linear triggers, giving traceable dependencies and modular branching where changing one branch does not break the rest. Workflows deployable from code repositories.
- AI embedded throughout via Sidekick, which can invoke custom in-house AI agents by webhook or API to minimise platform credit costs.
- Collaboration features linking Slack threads and looping in teammates inside the ticket, kept in audit history.

**Salesforce and channels**
- Plain has a native CRM connector, but custom API services must be built for native case creation and custom record types. Sunil has started a workstream with the Salesforce team, beginning with payouts onboarding and config.
- Charlie criticised Salesforce's manual tagging, absence of merchant data auto-enrichment, and heavy email reliance. Structured forms via Plain would improve data integrity and privacy.
- Both agreed on moving away from email toward structured, API-driven input.
- Plain or custom orchestration can support voice and chat channels for Ray. Sunil strongly supportive.

**Decisions**
- Unresolved but active: Plain as the Zendesk replacement. Procurement decision targeted for end of month. V1 launch targeted for Ray friends-and-family by end of December.

## Insights

- This is the clearest record of the Plain rationale and the Intercom exclusion logic: the Salesforce acquisition is expected to dismantle the Suite, and Fin is judged separately as an AI-agent proposition.
- The decision timeline is hard: procurement by end September, Ray friends-and-family launch end December.
- The architectural commitments to preserve: the "receiving work versus finding answers" split, and orchestration-layer-first sequencing rather than a single-system migration.
- SLO arithmetic worth keeping: 20% of turnaround miss is dependency-driven, ~16% unassigned, and a 17% uplift is expected from a Care config change. The unassigned share is the part with no external excuse.
- Operations has not supplied requirements or a backlog for the dependency work, which is the same requirements-ownership gap raised with Fraser and Ajay.

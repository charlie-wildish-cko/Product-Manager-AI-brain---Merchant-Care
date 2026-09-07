# Merchant Care Sprint Demo

**Date:** 2026-08-11
**Attendees:** Care Experience team plus Ana Cachapa Cuomo, Andre Verhaeg, Helder Goncalves, Joel Petrosino, Imran Khan, Oliver Westlake-Simm, Preethy Sundaresan, Fraser Bryant, Alcinda Lee, Ashish Tyagi, Alex Jordan, Jiro Farah, Anish Mavadia
**Drive source:** 1AoQeYAZC5QaPrmYKFqtJwkmDswRFMRr6ZTlINAemiiQ

## Key Points

**Agent Consultant pivot**
- Resources move from automated refund reversals to integrating MCPs into the Consultant Bot, to stay competitive with Glean.
- MCP-based dynamic data lookups expand supported ticket query coverage from roughly 30% to 70-80%.
- Rationale: faster investigations and standardised data handling across domains, without Glean's cost profile from less targeted querying.
- Risk: BigQuery cost increases. Mitigation is partition targeting.
- Open item: whether system authentication can persist without re-login every 5 minutes.

**Plain assessment**
- POC in week 3, final internal decision deadline Monday. Team leaning positive. Sign-off needed from Jenny Moron, Helder, Andre, Ashish and Oliver.
- SLA configuration limitation identified; vendor committed to a September fix.
- Jiro: Plain setup is simpler than Zendesk, but workflows cannot be mapped 1:1 and need re-architecting.
- Ana: in Zendesk top-level triggers execute sequentially; in Plain all triggered workflows execute simultaneously. Recommended strategy is fewer workflows with complex branching, avoiding duplication and auto-response problems.
- Jiro demonstrated configuration-as-code via the Plain GraphQL API: consistent QA-to-production deployment, auto-generated release notes, field dependency validation, webhook management, modular features developed in a sandbox behind feature flags.

**Reflex**
- Anish demoed the updated UI for product management: filterable product pillars and team views.
- New topic clustering groups similar tickets automatically to surface cost, volume and contact reasons, with drill-down to impacted regions and primary resolutions. Previous duplicate-topic issue resolved.
- AI-driven recommendations generated for volume and cost reduction.
- Charlie to roll Reflex out to PMs and ensure access.

**Data dependencies**
- Clearing team re-architecture is forcing unplanned engineering work because the clearing data platform has no accessible, stable, versioned APIs, so queries run at inefficient depth.

## Insights

- The 30% to 70-80% coverage jump is the headline justification for the MCP pivot. The cost of that pivot is deprioritised refund-reversal automation, which appears as a live Fin task-execution target in other threads the same week. Reconcile before either is quoted.
- Configuration-as-code is the strongest non-obvious argument for Plain over Zendesk, and it directly serves taxonomy standardisation.
- Reflex topic clustering plus AI recommendations is now the PM-facing product, with rollout owned by Charlie.

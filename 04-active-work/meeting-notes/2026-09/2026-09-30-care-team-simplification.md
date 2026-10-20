# Care Team Simplification

**Date:** 2026-09-30  
**Attendees:** Invited: Ajay Paul, Ana Cachapa Cuomo, Charlie Wildish, Joel Petrosino, Oliver Westlake-Simm (actual attendance unconfirmed)  
**Drive source:** 1sT5ndupskY_IIBwTHczGbeGPZAcISrH-t01tDuLa350

## Context

In-person session to simplify prioritisation and routing ahead of the Zendesk to Plain migration, aligned to ops goals, KPIs and OKRs. The doc holds Gemini summary notes only, with no transcript or speaker attribution.

## Key Points

**Proposed model**
- Four pods for Level 1 support plus generalists handling about 80% of ticket volume.
- Root cause of current fallback routing problems: no delineation of roles or specialties. Agents handle complaints and service tickets at once and constantly re-prioritise. Legacy metrics push tickets to agents faster.
- If deflection blockers are fixed, work reaching agents gets more complex. A universal technical level across generalists becomes unreasonable, which points to a skills-based Level 2 model.
- Resolution rate: confidence discussed in reaching 50-60% next year. Root issues outside Care must be fixed for long-term gains.

**Routing**
- Routing must balance merchant importance (net revenue, tier) against incident severity. Payment reconciliation and fund settlement for high-tier merchants outrank lower-severity enquiries.
- Plain workflows can group high-priority case types. Resolving intersecting tier and severity priorities is complex.
- Hard pod models across global offices raise redundancy questions, and tier-based routing may not differ much from skill-based routing.
- Do not design complex routing around friction points like IDV issues. Fix the underlying problems.
- Option: train all L1 agents in high-volume specialties for shift redundancy.

**Operating model**
- Operations has no fully defined operating model, risking tech built around untested concepts. Org design should drive tooling, not platform limits driving structure.
- Reference calls planned with support leaders at other orgs (Notion and Stripe named). Care is informed and consulted, not sole decision maker.
- Agent-to-ticket ratios compared across Plain customers, from small fintechs to high-volume ones. Custom AI agents for triage and KB review were highlighted.

**Platform capabilities**
- Change management needs a cycle (sandbox, UAT, formal approvals) so the central team is not a bottleneck while configuration responsibility spreads.
- Live chat as the primary synchronous option, using agent concurrency, with proper ops management and logging.
- In-app inbox needs authentication. Email should be an alert only, not carry full response content. A hard data-availability dependency slated for December creates scheduling problems for platform launches.
- End-to-end CX ownership should broaden to underwriting, communications and operational journeys.
- Consolidating operations, compliance and finance on Plain gives leverage with hundreds of platform users. Plain's runway is secured through 2028.

## Insights

- Routing redesign is a prerequisite for the Plain migration, not a configuration step.
- The operating model must be defined before tooling is built.
- The four pods plus generalists model is a proposal only, not a decision.

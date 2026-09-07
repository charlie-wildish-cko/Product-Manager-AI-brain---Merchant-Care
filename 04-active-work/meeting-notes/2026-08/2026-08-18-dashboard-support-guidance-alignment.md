# Dashboard x Support Project Alignment

**Date:** 2026-08-18
**Attendees:** Irene Liao, Alcinda Lee, Kevin Healy-Clarke, Chrisi Webster, Sammie Spector, Charlie Wildish, Andrew Stager, Aman Khare, Veronika Galkina
**Drive source:** 19S8CYePZOSeaUE8gSCP0SLfP1-kemYOGPzmoTiCKue0

## Key Points

- Two projects now framed under one guidance umbrella: reactive guidance (agentic global search with AI, connecting all entry points into a single search solution) and proactive guidance (formerly guided onboarding, interrupting metric moments on the dashboard before they become contacts).
- Fin sits in reactive guidance today as a fallback for "I can't find X." The team's view is that search should be the primary entry point for find-type intent and Fin should be for troubleshooting only.
- Key distinction for Care: tickets that drop because something got easier to find (discoverability) versus tickets that drop because the underlying issue was solved. Different interventions, different measurement.
- Charlie's data point: support tickets peak around 6 months post-onboarding, which undercuts the hypothesis that day-1 or day-10 interventions will materially reduce volume. Named as the reason to run small experiments rather than build a blanket onboarding flow.
- Support cluster analysis from Charlie's team is the input feeding proactive guidance prioritisation. Named examples: API keys, negative balance, pending payouts.
- Fin placement debate: Fin currently sits at the bottom of every dashboard page and is used as a general chat channel because it is there. A proposal to hide it behind a help icon was rejected for now, because hiding it would cut volume for the wrong reasons before a credible search alternative exists. Fin's launcher is a custom URL trigger, so additional contextual entry points can be added anywhere without new build.
- Unresolved: Fin uses the same icon as the Analytics Assistant, a unified global AI brand. Whether to differentiate is open.
- Metrics: Aman Khare and Charlie both argued against pinning success on support ticket reduction because of external confounders. Agreed measures are engagement and adoption of the guidance and search tools, feature discoverability lifts, ticket reduction on named specific issues, and time-to-first-click within 24 hours of login.
- Data gap: the Salesforce survey from Solution Engineering covers the integration experience only. Nothing covers post-onboarding dashboard experience. A post-activation survey is proposed to establish a baseline (a prior PLC-stage survey got ~80 responses). Aman intends to use saved Analytics Assistant queries plus Fin queries as an interim intent signal.
- Charlie's stated involvement: informed stakeholder, not default owner, and asked to be consulted before any change to how Fin interacts with users.

## Decisions

- Initial evaluation scoped to specific scenarios, not aggregate support tickets.
- No change to Fin's dashboard placement until search reaches parity.
- Merge the separate weekly Agentic Search and Guidance catch-ups into a single weekly session.

## Insights

- The 6-months-to-peak finding is the central counter-argument against onboarding-led deflection in the dashboard, and Charlie owns it.
- The discoverability-versus-troubleshooting split is the framing Care should use when the dashboard team claims deflection credit.
- Fin placement is a live lever on contact volume that the dashboard team could pull unilaterally. Charlie has asked for consultation but has no formal control.

# Consumer and Ops Readiness

**Date:** 2026-08-07
**Attendees:** Hélder Gonçalves, Charlie Wildish, Gilles Beausseron (Gemini merged Hélder and Charlie under the room label "LON-03-02", so attribution between those two is unreliable)
**Drive source:** 1dyttLLN69goXnBJ8eC51L1O9xppraLe6O_67_TEQBCA

## Context

Called to surface the gap between how the consumer (Braavos) programme is reported at steerco and the actual state of operational and risk readiness, and to agree a joint position to take back to stakeholders.

## Key Points

**Programme reporting vs reality**
- Steerco slides show Phase 3 as green. Phase 3 has not started. Hélder and Joe are aligned that it is not started.
- Risk, compliance, and Care for Phase 2 are better described as grey than red: the work is undefined, so it cannot be status-tracked.
- The fraud team has not provided data requirements. That item is marked red or at risk rather than undefined.
- PRDs were written in April by Aarov (since departed) and are treated as out of date or invalid. They were written without engaging the ops team, so no one validated the end-to-end flows.
- Care was misdefined in those PRDs. Hélder's definition of care is the entire back office; Charlie read it as the Care team's scope only. That mismatch left the rest of the back office unowned.
- Gilles' framing: there is a difference between a requirement list and a commitment that Phase 3 ships on a fixed date because a requirement exists.

**January launch**
- January launch is not feasible. Neither the functional nor the operational components will be ready.
- Gathering requirements, building, and launching for 50 users by October was also called unrealistic.
- Gilles: launching anything in Q1 means reusing every existing system, which means no new case management system.
- Agreed direction is a closed beta with a waiting list (Monzo model) plus a hard onboarding cap, rather than a public launch.
- Jenny's most recent stated position: coordinate consumer launch to system readiness.

**Consumer Duty as the largest unknown**
- Consumer Duty requirements are unquantified. Legal only started assessing them the day before this meeting.
- The concern is not schedule slip but rework: building case management, data access patterns, and data segregation now risks having to change all of it within six months once Consumer Duty guidance lands.
- Data questions still open: how consumer data is segmented, who has access, who can act on it. Related to an escalation from Luca.

**Operational staffing**
- Oliver is acting as de facto consumer support lead while also heading Operational Excellence. Workload is unsustainable and has left no time to design end-to-end flows.
- Result is reactive and scrappy: systems hacked together, flows unvalidated against Consumer Duty.
- Session scheduled with Oliver the following week to define the operational workflows (what arrives via Care, what routes to which team, which application serves each scenario).

**Orchestration layer over migration**
- Three genuinely new work patterns for Checkout: fraud, customer account takeover, Consumer Duty. All three are also required for ISVs, so the problem is shared rather than duplicated.
- Underlying risk infrastructure is the same for ISV and consumer. The case management solution is what is not fit for purpose on the consumer side.
- Agreed architecture: a central orchestration layer (control plane) routes work to operators, integrating with the two existing case management tools (Zendesk and Salesforce) via adapters. Teams migrate into Plain over time rather than up front.
- Rationale: paying to migrate 20 teams off Salesforce buys less than integrating handoffs, data context, and permissions properly. Case management was called the less serious problem; handoffs between systems are the harder one.
- Second operational split: how a team receives and completes work (orchestration) versus the tools used to do the work outside case management. Forcing all tools into case management does not work. AI applies to both sides.
- Current ecosystem: roughly 20 tools across four teams, with more being added (Ray). No one has seen a single picture of it.
- Nothing blocks two workstreams: experimentation with Plain for case management workflows by segment, and infrastructure to ingest signals from transactions, disputes, and other sources.

**Agreed next moves**
- Gilles to comment on the shared slide deck covering the current ecosystem and operational requirements.
- Hélder to book a 30-minute whiteboard session for Tuesday or Wednesday to map the system and the long-term vision.
- Produce slides showing current state, target state, per-quarter capability, and capacity constraints, to take to steerco, Milan, and Jenny. Expectation is Jenny will not like it and that this is the right outcome.
- Trade-off to put to stakeholders explicitly: more money, less quality, or more spend on ops agents for a period. Cost to accelerate, not headcount cuts.

## Insights

- Two "no-regret" builds were agreed and can start now regardless of the undefined scope: the orchestration layer (Plain) with adapters to Zendesk and Salesforce, and the signal-ingestion infrastructure. Everything else waits on requirements.
- The orchestration-layer decision settles a live architectural question: Checkout is not migrating to a single case management platform. Plain is the central orchestration point; Zendesk and Salesforce stay as the execution tools behind adapters.
- Consumer Duty is the top rework risk on the consumer programme. Any case management or data-access design committed before legal's assessment lands is exposed.
- Ops readiness, not app build, is the binding constraint on consumer launch. The app is roughly 20% of the work; the operational platform is the rest.
- Care scope ambiguity is a real programme risk: "care" meaning the whole back office versus the Care team changes who owns the operational build. It needs writing down.
- Fraud, account takeover, and Consumer Duty are shared ISV and consumer problems. Building them once for both segments is the stated position, and consumer only hits the problem sooner. SMB will hit the same wall with an 18-month runway rather than one quarter.
- The closed-beta-with-cap model is now the working assumption for consumer launch, replacing a dated public launch.

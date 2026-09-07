# Mapping Care — 2026-2030 high level outcomes

**Date:** 2026-07-31
**Attendees:** Charlie Wildish (PM, Merchant Care), Joel Petrosino (Operations Excellence). Referenced: Milan, Oliver Westlake-Simm, Ashan, Patrick, Fraser, Paul, AI CoE
**Drive source:** 17yXmsODzf2f8IfE3iysiTwHVV35vwAKObfsprPMStdE

## Context

Working session to fix the customer model and high-level outcomes for the Care strategy 2026-2030 ahead of a refreshed version going to the strategy group. Also covered MCR triage agent design in Glean.

## Key Points

**Strategy framing**

- Strategy starts from customers, not from a quality-vs-speed identity choice. Three candidate identities were considered (segment-driven, quality-over-speed, speed-over-quality); segment-driven wins because customers differ in needs, expectations, and regulatory requirements.
- Two audiences behind the framing: the CEO cares about regulatory exposure, Milan and ops leadership care about customer experience. The two overlap.
- The trade-off assumption (more humans = higher quality, lower speed, higher cost) was flagged as fair to challenge. Fin arguably delivers both speed and quality.

**Three-segment customer model**

Charlie started from Enterprise vs SMB. Milan reframed it as White Glove vs Not White Glove, because Tier 5 exists today and does not fit "Enterprise".

| Primary segment | Who it is today | Human support model |
|---|---|---|
| White Glove | Enterprise (Enterprise Direct as a sub-segment) | AI-first, escalation on demand, handoff to support engineer, top SLA |
| Not White Glove / SMB | SMB plus Tier 5 (moved out of Enterprise) | AI-first, escalation only by issue type or flag (e.g. vulnerable customer). Possibly BPO-served |
| Consumer / B2C | Braavos consumer customers | AI-first, regulatory human handoffs mandatory |

- Every segment is AI-first. What differs is channel availability and human-support availability, not the AI-first stance.
- Structure below the top level: primary segment then sub-segment, with further dimensions possibly business model, product catalogue, or configuration level.
- Care Success Plans is the mechanism to systematise this. Customer type drives eligibility: channel availability, SLA, and AI content scoping. Worked example: a White Glove Platform customer should have Fin scoped to Platforms documentation, not all of Checkout's documentation.
- Governing economic metric: support cost as a percentage of net revenue for that segment, which must not exceed a threshold. White Glove is few customers with very high ROI per account, so heavy investment is justified. Not White Glove earns through volume with a long tail and higher cost.

**AI resolution target changed in the meeting**

- Charlie proposed 90% fully resolved by AI with 100% AI triage. Joel pushed back: human-first covers complaints, vulnerable customers, and complex fraud handling, so 90% is too ambitious.
- Landed on 80% AI resolution, max 20% human escalation, applied across all segments and channels, treated as a permanent ceiling rather than a waypoint.
- Charlie's separate estimate: strictly regulatory-mandated contacts are under 10% of volume.

**Timeline: 2026 / 2027 / 2028-2030**

- 2026: Fin resolving ~40% for White Glove, expected roughly flat by year end. Estimated further 20-30% resolution headroom in the White Glove domain. ISV volume immaterial. Consumer launches end of year.
- 2027: scaling year. Scaling Consumer, scaling ISV and all Platforms, starting SMB, starting banking services (interest and funds on account). First real B2C contact volume, Consumer Duty obligations bite. Systems and structure must be in place so scaling is easy.
- 2028: the pivotal year. Volumes potentially into the millions, total volume may cross 1 million contacts a year. B2C becomes the majority of volume. Any small AI error or change now produces thousands of tickets, not a handful.
- 2030 end state: contact mix inverted versus 2026, roughly 75% B2C with B2B a small proportion. Enterprise under 15% of contact volume. Human support becomes a genuine premium offering. Requires fully mapped routing and orchestration plus a team structure reflecting the segmentation.
- Robustness check from Joel: the narrative holds even if Consumer underperforms, because the architecture improves response quality and volume capacity regardless.

**Regulatory pain point**

- Fund holds and account freezes are the single biggest support pain, for SMB and B2C alike. Every community support page and social channel for Revolut, Monzo and Starling flags withheld funds. The freeze itself is legally required; the communication back to the customer is what fails. The comms path between frontline support and the risk teams making hold decisions needs to be watertight.

**AI Ops model and org design**

- AI Ops model implemented by Q3 2027 at a defined scale, fully operationalised by 2028. Joel initially proposed Q3 2027 for both.
- Joel and Oliver have discussed core roles that flex across acquiring and consumer for AI ops first, then expand.
- Knowledge management exists and needs to scale, not to be newly introduced. The missing role is a conversation designer / outcomes designer to build automated flows. Proposed as the first hire.
- Human team restructuring: split human support along the three segments. Consumer Support team for B2C; within B2B, a White Glove team and a Not White Glove team, the latter possibly a BPO. Expect a different AI agent per customer segment.
- Explicit organisational purpose: Milan asked for clarity so he can plan teams and justify a headcount request, and to help hire Care leadership.

**Product outcomes sketched for 2027**

Migrating to the new support platform in stages; a productised new-product-introduction model; connecting multi-ops-team workflows (driven mainly by Consumer handoffs between teams); AI resolution goals; a decision on whether to stay with Fin as the AI agent; proactive contact-reason handling by agent with automated fixes. Method: agree outcomes first, then map the stack to them.

**MCR triage agent in Glean**

- MCR submission is broken: requesters (AMs, commercial) submit an MCR that is not what they actually want configured, then loop three or four times with config to establish the real requirement.
- The AI CoE will not take this on. They are focused on big bets, so small and medium AI applications fall to internal build.
- Proposed fix: an MCR triage agent in Glean. Requester describes the need in natural language, agent triages, maps it to the right configuration, and surfaces submission requirements up front.
- Data readiness: the data dictionary on `dim_entity_configuration` (now the main table) is done to a high standard, credited to Pal's team. A test query returned exhaustive detail.
- Gap: no semantic layer. It answers "what is this field" but not "what setting controls X". MCR type documentation must specify configuration at field and value level. That granularity does not exist today.
- Glean agent builder outperformed expectations: given only the use case, it found the closest-matching Looker tables itself by reading the LookML schema, without being handed the Looks.
- Architecture: separate agents. Existing knowledge/answers agent plus a new lookup agent spanning all lookup types. Instruction-based builder, not the workflow builder.
- Blocker: Looker permissioning. Charlie lacks financial-data access and needs settlements and balances tables. Table permissioning needs solving at Checkout level.
- Practical note: the Glean agent has an "allow all" setting that bypasses per-connector authorisation (otherwise 40 connectors approved individually).

## Insights

- The segmentation reframe came from Milan, not Charlie. Sponsor-originated, so likely durable. Tier 5 moving into Not White Glove is the concrete change from the old Enterprise/SMB split.
- 80% AI resolution is a ceiling, not a waypoint. The 20% floor is structural: complaints, vulnerable customers, complex fraud, regulatory holds. Any doc claiming 90%+ contradicts this decision. Tension worth noting: strictly regulatory contacts are estimated under 10%, so the other ~10% is complexity, not regulation.
- 2028 is the strategic hinge. Volume crossing ~1M contacts/year, B2C becoming the majority, and error amplification at scale are what justify building the AI Ops function in 2027 rather than 2028.
- The 2030 inversion is the headline number: ~75% B2C, Enterprise under 15% of contact volume, human support repositioned as premium. This flips Care from a B2B function to a consumer function with heavier regulatory load.
- Support cost as a percentage of net revenue by segment is the mechanism that makes differentiated service levels defensible rather than arbitrary.
- Fund holds and account freezes are the highest-risk contact type across SMB and B2C, and the failure mode is communication, not the legal decision.
- The AI CoE will not build small or medium AI applications. Care must build its own agents. This changes build-vs-partner assumptions for anything MCR-sized.
- The semantic layer is the recurring blocker for both the MCR triage agent and the lookup agent, not model capability. The constraints are documentation granularity (field and value level) and Looker permissioning.
- The strategy doc has an organisational job: unlock Milan's headcount request and define hiring profiles for Care leadership. It should be written to be usable that way.

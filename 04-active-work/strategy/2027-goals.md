---
title: Care 2027 goals (draft)
---
# Care 2027 goals (draft)

**Owner**: Charlie Wildish
**Status**: Draft v0.1, 2026-10-08. Not yet reviewed. Quarters are proposals until they are confirmed in a 2027 plan.
**Strategic goals**: Deliver new operations platform, reduce contact rate, reduce cost of support
**North stars**: contact rate (contacts per 1M transactions), cost per contact
**Guardrail**: Merchant CSAT (reported by segment) must not decline as we automate. New: % cases being passed through Operations platform

## Where the 2027 volume is

| Segment | 2026 contacts | 2027 contacts | 2028 contacts |
|---|---|---|---|
| Enterprise | 60,014 | 111,188 | 150,455 |
| Consumer (Ray) | 0 | 45,936 | 229,600 |
| Platforms SMB | 0 | 1,948 | 26,149 |
| Platforms ISV | 35 | 1,243 | 2,073 |

Source: `04-active-work/strategy/care-strategy-2026-2030.md`. In 2027 Enterprise is 69% of volume and Ray is 29%. SMB is about 1%, so the SMB flow is built late 2027 for the 2028 ramp.

## Goal 1: Build the Support & Operations platform for customer scale (Merchants & Platforms, Consumer, SMB)

This goal is the Operations platform workstream. Care migrates to Plain first, then more Ops teams follow in H2.

**Outcome**: Care runs on Plain for Ray and for merchant support before the Zendesk contract ends in June 2027. Guardrails at every cutover: Merchant CSAT, SLA attainment, backlog age and handle time at or better than the Q4 2026 baseline.

| Key result                                                                                              | Timing                                                         | Depends on                                                                                           |
| ------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| G1.KR1 Ray consumer support live on Plain for external launch                                                  | Friends and family Dec 2026. Ray support on Plain Q1 2027      | Plain approval, estimates and business sign-off                                                      |
| G1.KR2 Migrate merchant support to Plain                                                                       | Starts Q1, finishes Q2 2027, in time for the June contract end | Plain decision milestone (November 2026), ops team scope and sequence, migration path                |
| G1.KR3 Onboard more Ops teams onto Plain                                                                       | H2 2027, in the sequence agreed by the working group           | Care migration complete, ops team scope, Salesforce and commercial boundary                          |
| G1.KR4 Add other end-user use cases (pay to bank, merchant of record, issuing complaints, open banking payers) | H2 2027                                                        | Consumer Duty obligations through open banking in 2027, Legal on Care's resolution authority for MoR |
| G1.KR5 Build SMB support flow                                                                                  | Late 2027                                                      | SMB launch scope and time frame. SMB experience definition. |
| G1.KR6 Taxonomy linked to the product catalogue and current with the latest issues | TBC | Plain work type design, product catalogue sync, support taxonomy owner                                          |

Reference: `04-active-work/strategy/operations-platform-definition.md`

**Levers**

| ID | Lever | Key result | Timing |
|---|---|---|---|
| L1-01 | Ray support flow on Plain: taxonomy, forms, triggers, routing, agent content, L2 queue | G1.KR1 | Q1 |
| L1-02 | Fin in the Ray app: Fin mobile install and Fin configuration for consumer contacts | G1.KR1 | Q1 |
| L1-03 | Merchant support migration to Plain: channels, routing, content, Fin integration cutover | G1.KR2 | Starts Q1, finishes Q2 |
| L1-04 | Migration guardrail reporting: Merchant CSAT, SLA attainment, backlog age and handle time against the Q4 2026 baseline, and % of cases passed through the Operations platform | G1.KR2 | Q1 |
| L1-05 | Ops teams onboarded to Plain in the sequence agreed by the working group | G1.KR3 | H2 |
| L1-06 | End-user use cases on Plain: pay to bank, merchant of record, issuing complaints, open banking payers | G1.KR4 | H2 |
| L1-07 | SMB support flow | G1.KR5 | Late 2027 |
| L1-08 | Taxonomy model linked to the product catalogue in a parent-child relationship, so products drive the issues in the taxonomy | G1.KR6 | TBC |
| L1-09 | Taxonomy update so the latest issues are accounted for and solvable | G1.KR6 | TBC |

## Goal 2: Reduce cost of support through automation and AI

**Outcome**: Cost per contact falls. Fin resolves 60% of total Care volume by Q4 2027 exit, with quarterly gates.

**Input**: Data Science produces an opportunity sizing in Q4 2026. It prioritises the 2027 plan to reach 60% for Fin and the dependent-team areas for back office automation. The sequence below is provisional until it lands, and the quarterly gates are set from it. The sizing needs to give:

- The validated baseline: involvement and resolution, as a share of total volume
- Volume and cost by taxonomy (case type, issue type, reason) and by segment, from `04-active-work/working-files/Contact breakdown since April 2026.md`
- For each area, what blocks Fin resolution: Procedures, content, missing data (the three gaps in Goal 3), or a policy limit
- Dependent-team areas ranked by SLA breach and agent hours
- The resolution gain and contacts removed for each opportunity, so the plan to 60% is a sum, not a target

**Baseline to validate before commit**: The 2026 target is 40%. The 60% target needs about 75% involvement at 80% resolution. About 20% of volume is blocked on three upstream data gaps (Goal 3). Cost per contact at $20 end 2026.


**Key results**

| Key result | Metric | Baseline | Target |
|---|---|---|---|
| G2.KR1 Fin resolves more of total Care volume | Fin resolution as a share of total volume | To validate (Data Science sizing, Q4 2026) | 60% by Q4 2027 exit, quarterly gates set from the sizing |
| G2.KR2 Agents spend less effort per contact | Handle time, % of agent work volume automated, SLA attainment in dependent-team areas | To validate (Data Science sizing, Q4 2026) | Set from the sizing |

**Levers**

| ID    | Lever                                                                                                                                                                                                | Key result   | Timing                        |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ----------------------------- |
| L2-01 | Set up Fin API for Plain to solve emails using Fin                                                                                                                                                   | G2.KR1       | Per sizing                    |
| L2-02 | Fin Procedures and data coverage: Payout to self delays or status, Balances analysis, Financial actions on payments, Clearing data                                                                   | G2.KR1       | Per sizing                    |
| L2-03 | Enable Fin to call back office agents via webhook to solve complex issues                                                                                                                            | G2.KR1       | Per sizing                    |
| L2-04 | Fin can get latest incident information from Ultron, including payment level diagnosis                                                                                                               | G2.KR1       |                               |
| L2-05 | Fin can look up content of other tickets from same merchant to assess status or answer a follow up ticket                                                                                            | G2.KR1       |                               |
| L2-06 | Contextual Answers on Dashboard                                                                                                                                                                      | G2.KR1       | Per sizing                    |
| L2-07 | Golden set of: merchant/customer ID specific handling rules/queries, agent replies as a knowledge source based on top QA scored tickets                                                              | G2.KR1       | Per sizing                    |
| L2-08 | Build a self improving workflow to improve and fill content & data gaps available to Fin, based on conversations, resolution performance and the agent replies golden set                            | G2.KR1       | Per sizing                    |
| L2-09 | If the Dashboard team does it: use Fin API to plug Fin into the new Checkout owned AI assistant widget in Dashboard                                                                                  | G2.KR1       | Conditional on Dashboard team |
| L2-10 | New payments agent for triage and analysis using Sidekick in Plain                                                                                                                                   | G2.KR2       | Per sizing                    |
| L2-11 | Implement new Care agent team model and routing: new team structure and routing rules for which tickets go to which agent or regional team                                                           | G2.KR2       | Per sizing                    |
| L2-12 | Back office agent task automation: focus on areas where dependent teams breach SLAs most. L3 engineering escalations (5-10% of volume) and Treasury settlement checks are the evidence-based targets | G2.KR2       | Per sizing                    |
| L2-13 | Support Model: support model defined routing                                                                                                                                                         | G2.KR2       | Per sizing                    |
| L2-14 | Social Media Complaints Process (TBC, no scope or owner yet)                                                                                                                                         | G2.KR2 (TBC) | TBC                           |

**Platform rule for carry-overs**: all 2027 platform work is built on Plain. No item is built on Zendesk. Routing, SLAs and tier enforcement are Plain-native builds sequenced behind Goal 1.

**Sequencing logic**: Q1 and Q2 engineering goes to the Plain migration, so H1 Fin work is limited to items that do not depend on the ticketing platform, and items that touch handoff or agent tooling wait until migration is done.

## Goal 3: Root causes of support issues are solved by Product

**Outcome**: Contact rate falls on named drivers. Each of the top 10 Reflex drivers has an owner, a committed roadmap item and a contact-reduction target. Measure the volume reduction after each fix ships.

| Key result | Detail |
|---|---|
| G3.KR1 Reflex items pushed to product roadmaps (H1 pilot) | Explore and pilot automating Reflex items onto product roadmaps in H1. Reflex V1 live first (it had not launched as of 2026-07-26). Weekly digest to Product leads. Jira issues per product pillar, human review before publish. Attribution model tracking contact reduction from Reflex-originated fixes |
| G3.KR2 Close the three payment-lifecycle data gaps (all year) | TPA/MPGS in MENA (~10% of volume), clearing invisibility (5-8%), settlement delays (~5%). Percentages are estimates. Owners and dates tracked in the use-case, data-point, owner and date document committed on 2026-08-20. Clearing and settlement exposure lands Q1 2027 at the earliest. Gateway status sync is 2027 |
| G3.KR3 Product onboarding service live (H2) | Picks up in H2. Support Readiness Agent reads each launch and scopes what Input, Orchestration and Fuel need before the first contact. Runs through MCAP and Hive with rejection rights. Metric: % of launches onboarded before first contact |
| G3.KR4 Agent HAL pilot on Reflex-identified issues (H2) | Starts in H2, after the H1 Reflex roadmap pilot produces tickets. See below |

**Levers**

| ID | Lever | Key result | Timing |
|---|---|---|---|
| L3-01 | Reflex V1 live: theme clusters, product mapping, query interface | G3.KR1 | H1 |
| L3-02 | Reflex-to-roadmap pilot: Jira issues per product pillar with human review before publish, and an owner, roadmap item and contact-reduction target for each of the top 10 drivers | G3.KR1 | H1 |
| L3-03 | Weekly digest to Product leads and an attribution model tracking contact reduction from Reflex-originated fixes | G3.KR1 | H1 |
| L3-04 | Data gap tracker: owners and dates for TPA/MPGS in MENA, clearing invisibility and settlement delays | G3.KR2 | All year |
| L3-05 | Product onboarding service: Support Readiness Agent and the MCAP and Hive intake with rejection rights | G3.KR3 | H2 |
| L3-06 | Agent HAL pilot on code-level Reflex issues | G3.KR4 | H2 |

### Agent HAL pilot

Agent HAL is an engineering agent run by the Developer Platform team. It picks up a Jira ticket labelled `agent-hal` and delivers a GitHub pull request. It runs install, build, lint and tests, does self-review and Security, Architecture and Frontend reviews, opens the PR, and moves the ticket to In Review. Human reviewers can request fixes by tagging `@agent-hal`. Source: Confluence COREP, "Get Started" (2026-08-12).

This matches the Reflex 2030 vision: fix PRs for engineering review, not autonomous deployment to production.

Fit and constraints:

- **Only code-level fixes qualify.** Process, policy, content and tooling root causes do not. Reflex tags a root-cause category, so the pilot filters on product-code issues.
- **The owning team must be onboarded.** Their GitHub org is onboarded to Agent HAL, their Jira project is registered, and the repo has `.agent-hal/agent-hal.mk` and `AGENTS.md`. Care cannot do this alone. Start with Care-owned repos (`cko-compass`, `care-` prefix) and one willing Product team.
- **Ticket quality sets output quality.** A vague ticket makes the agent ask questions or abort. The Reflex Jira issue needs acceptance criteria, scope boundaries, the target area of the codebase and constraints, so the Reflex template must include them. The `/ticket:ticket-review` command scores a ticket from 0 to 100%.
- **Dependency**: the Reflex Jira integration (Q4 2026, TBC).

Measures: Reflex tickets that become an agent PR, % of PRs rated thumbs-up on the Agent HAL dashboard, % merged, time from Reflex insight to merged PR, contact volume reduction after merge.

## Open decisions

- Ops team scope and sequence for migration (working group via the process team, facilitated by S&O)
- Moving more accountability to support Fin from Care Ops side

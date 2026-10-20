# Plain demo

**Date:** 2026-08-25
**Attendees:** Fraser Bryant, Charlie Wildish, Ajay Paul, Ana Cachapa Cuomo, Jiro Farah, Joel Petrosino, Oliver Westlake-Simm, Wes Nolan, Robert Braam, Joanie Vencatasamy, Ling Wong, Francisco Goncalves, Alex Jordan, Karan Jagmohansing, Ashvin Pudaruth
**Drive source:** 1vOpIwpb2oI6qlZmB64WrnmbbjwTfm2wxou055wWHygU

## Context

Full Plain platform demo to Care product, engineering and operations. Framing from Fraser: the goal is faster development and simpler architecture than Zendesk. Plain is explicitly not a 1:1 Zendesk replacement.

## Key Points

**Data model mapping**
- Companies = customer groups, auto-matched by domain (Zendesk organizations). Tenants = contract/account boundary. Labels = Zendesk tags, currently also used to hold teams. Tiers = Checkout tiers 1-5.
- Threads = tickets. Tasks are strictly individual reminders, linkable to companies, tenants or threads. No group tasks.
- Native Slack integration with no workarounds, called out as the most valuable native channel.

**Threads, statuses, SLAs**
- Statuses are hardcoded and not customisable. Plain is exploring customisation on its roadmap. Four statuses continue SLAs; others pause or ignore. Concern raised and accepted: preserve the same clock logic and prevent agents cheating SLAs.
- Out-of-the-box SLAs cover only first reply and next reply time, by tier. Plain is deploying enhanced SLA features on 14 September, described as non-negotiable, with time to test. Native imminent-breach configuration (pending, imminent breach, breaching, breached, achieved) removes Zendesk manual workarounds.
- Routing is first-in-first-out, modulated by priority labels, the same as today.
- No native custom forms. L1/L2 splits, IDV and account unlock cannot be differentiated by form. Workaround under test: a custom thread field called "form" plus labels, which can dynamically surface region-specific fields.
- Multiple assignees supported with one primary owner for metrics. Typing indicators show at the bottom of the thread. Gap: no visual indicator of who is editing or viewing.
- Clean linked-thread views and native Jira integration, removing current Zendesk-Jira app pain. Agents can create admin to-dos from inside a ticket.
- Auto-replies are visible in the UI, where Zendesk needs extra clicks and shows unformatted text. Workflow run history is visible, including what triggered.
- Internal discussions currently run over email and Slack. Plain has been asked to make snippets available inside "start discussion" so agents can pick a target team. Macros populate fields and set groups; snippets are text only.

**AI: Sidekick and machine users**
- Sidekick is Plain's native AI agent: gathers thread context, assists with responses, can generate KB articles. Intent is to connect it to Checkout backend systems (knowledge bases, payment lookup). Datadog integration is the intended direction for backend agents.
- Workspace overview for leads: what is urgent, what is taking longer, where agents should focus.
- Machine users run in parallel to threads with scoped roles: monitoring for treasury refund-reversal adjustment IDs, detecting internal information shared publicly, and proactive QA scoring agent responses during live tickets rather than two weeks after closure.
- Reusable custom skills, democratised so agents can write skills for repetitive work. Reduces the need to build workflows and custom apps.
- Plain uses AI to auto-set thank-you messages to Done with no agent time, against Zendesk's keyword approach.
- Governance gap raised by Wes Nolan: credits are limited at workspace level only, so one user chatting to Sidekick could consume the entire workspace budget. Plain has been asked for user-level granularity. ~30 credits per workflow action was quoted. Dynamic forecasting across volume is still needed. Bring-your-own-agent into Sidekick is possible at Checkout's cost, but Sidekick still has to invoke it.

**Data freshness**
- All clients will be pre-loaded into Plain as companies with tier details, updated on demand from Checkout infrastructure with up to 1 hour latency. Zendesk only refreshes when a customer raises a ticket.
- Thread data locks at creation, so a tier 3 to tier 1 move will not retrospectively change historical tickets. Agreed principle: separate data required in a thread from data merely useful to know about the merchant.

**Commercials**
- Plain seat cost is about the same as equivalent Zendesk seats. The undiscounted price was still lower. Credits are baked into seats, with add-ons on top. Pricing judged comparative.
- Additional cost reductions: the Salt integration is displaced, and native peer review replaces a third-party app.
- Suggestion raised to lock a 2-3 year Zendesk contract to secure better discounts as a negotiating point.

**Gaps and asks**
- No native control to force agents to review updated documentation before handling tickets. Workaround: dynamically surface process changes by case type and time window.
- Merchant data blocks are not customisable. Feedback given to move the merchant data panel to the top of the ticket.
- Plain exports to BigQuery for analytics, but leaders need real-time agent availability, which BigQuery lag prevents. Agent online status in Plain was confirmed automatic. A separate native-analytics session will be scheduled.
- No native community or social listening. Social listening would connect as an input service feeding Plain threads. An SMB community platform is a build-or-buy question still to evaluate. Charlie noted this is not negligible work: moving from an all-in package to building and maintaining a community from scratch.
- Cross-system SLA tracking when tickets move between systems is unresolved.

**Fin and deflection**
- Fin is committed for at least another year. Ada was assessed as too entry-level and lacking sophistication versus Fin. Plain is not being considered as the deflection layer.

**Decisions**
- Build a data translation layer after migration so historical and new metrics stay continuous. Rationale: switching without continuity means no way to tell whether anything improved.
- Keep the existing 3-level taxonomy (case type / issue type / reason) and migrate it.
- Move SLAs from flat-per-tier to priority, urgency and symptom severity, tied to the taxonomy (case and issue type). The flat-per-tier model was judged no longer sensible.
- Adopt swarming using temporary channels rather than moving tickets between teams. Raised as a feature request to Plain.
- Require granular user-level AI credit limits.
- Adopt a holistic operations platform strategy, not a Care-specific design. The platform must serve the wider org.
- Proposal to engage risk and disputes teams to join the Plain migration instead of Salesforce, to consolidate the back office.

**Zendesk limitations Plain resolves immediately**
- High configurability, AI automation by default, better scaling for the upcoming consumer and SMB verticals, and taxonomy updates in hours via AI rather than weeks of manual work.

## Insights

- Commercially this is not a cost-reduction case: pricing is comparable. The case rests on configurability, AI-by-default, taxonomy agility, and scaling into consumer and SMB. That matches the configuration-maintenance-at-scale framing chosen for the platform assessment.
- Three concrete gaps to carry into the decision: no custom forms, no community or social listening, and workspace-only AI credit controls. All three currently have workarounds or feature requests rather than answers.
- The translation layer is the single biggest measurement risk in the migration and is now an agreed workstream. Without it there is no way to prove the migration improved anything.
- The SLA model change (taxonomy-driven severity rather than flat tier) is a substantive Care design decision that survives independently of the platform choice.
- Machine users doing live QA scoring during open tickets is the most novel capability on offer, and directly addresses the absence of a Care quality scorecard raised in the Care skills session.
- Plain's fitness for Ray depended on phone support, which Plain does not cover well. The Ray Steerco two days later decided no phone at all, which removes that blocker for Ray but not for Brazil merchant of record.

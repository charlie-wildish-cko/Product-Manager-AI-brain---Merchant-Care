# Zendesk Current Configuration — Conceptual Flow Map

**Purpose**: a conceptual reference for how Checkout.com's Zendesk instance is configured today, prepared for the Plain proof-of-concept discussion. It maps ticket flows to their underlying configuration — forms, fields, triggers, automations, SLA policies, routing — in plain terms, without exposing raw configuration syntax.

**Source and method**: sourced directly from Checkout.com's Zendesk configuration-management system, current production environment. Every object type below was parsed in full from source, not sampled. Two content types (macros and views) were counted and pattern-matched by name only, not individually reviewed — see §16. One system, Zendesk Guide (the help center / knowledge base), is explicitly out of scope — see §17.

**Note on scope**: SLA and routing rules are in the process of migrating to a new workflow-based model that is not yet reflected in this document. Everything below describes the current, live configuration, not the target state.

---

## 1. Brands

Three brands, all live in production:

| Brand | Public URL | Help Center | Purpose |
|---|---|---|---|
| **Checkout.com** (default) | support.checkout.com | Enabled | Primary merchant-facing brand |
| **Checkout Internal** | Internal-only instance | Enabled | Internal-facing tickets (dependent-team handoffs, non-merchant-facing work) |
| **Checkout.com Consumers** | Internal-only instance | Disabled | B2C consumer support |

Checkout.com Consumers supports B2C consumer contacts and is fully configured today — its own ticket form, dedicated group, queue and workspace, and roughly 10 dedicated automation rules are live in production alongside the two B2B brands.

---

## 2. Ticket Intake — Forms

15 forms. Most are visible across all three brands; two are brand-restricted:

| Form | End-user visible | Brand-restricted | Fields / conditional logic |
|---|---|---|---|
| Merchant Care form | Yes | All | 105 distinct fields, 108 conditional show/hide rules |
| L2 Merchant Care Form | No | All | 106 fields, 109 conditional rules |
| Consumer Support | No | **Consumers brand only** | 12 fields, 3 conditional rules |
| Account Unlock Request Form | Yes | **Checkout.com brand only** | 8 fields |
| Complaints | No | All | 31 fields, 7 conditional rules |
| MCR Form, IDV, Collections, Knowledge Requests, Dispatch, Approvals, QA Review (+ 3 QA sub-forms) | Mixed | All | Internal-process forms; QA has its own 3-stage form set |

The 105-field, 108-rule form is a taxonomy cascade: case type, then issue type, then reason, each selection revealing the next set of fields. This conditional structure is the most complex element to reproduce faithfully — a flat field count understates it.

---

## 3. Ticket Intake — Channels

Forms control which fields a ticket carries; channels control how it arrives. 48 channels are configured:

| Category | Channels |
|---|---|
| Voice | Phone call (in/out via CTI), voicemail |
| Messaging apps | WhatsApp, Telegram, LINE, WeChat, Facebook Messenger/Post/Private Message, Instagram Direct, Slack Direct Message, Google Business Messages, Google RCS, Apple Messages for Business |
| SMS | Twilio SMS, Messagebird SMS, Text |
| Social | X/Twitter (post, DM, like — 4 variants) |
| Web/mobile | Web form, Web Widget, Mobile SDK, Mobile |
| API/integration | Web service (API), Sunshine Conversations API, Channel Integrations |
| Native | Email, Chat, Chat Transcript, Side conversation, Forum topic, Help Center post, Ticket sharing, Automation, Closed ticket, Satisfaction Prediction |

Not all 48 necessarily carry meaningful ticket volume today — this reflects what is configured, not confirmed usage.

---

## 4. Data Model — Account, Contact, and Ticket Fields

Three tiers of custom fields carry state, beyond the ticket taxonomy fields (case type / issue type / reason) themselves:

**Organization fields (15)** — the account-level data model: `tier`, `account_manager`, `technical_account_manager`, `implementation_engineer`, `sales_engineer`, `account_owner_sales_territory`, `client_id`, `client_name`, `client_status`, `global_id`, `org_type`, `segment_value`, `alias`, `data_confidence`, `no_csat`.

**User fields (8)** — the contact-level data model: `is_consumer` (flags B2C contacts), `entity_id`, `entity_name` (links to internal customer-data records), `im_ticket`, `agent_ooo`, `last_csat_date`, `no_csat`, `data_confidence`.

**Key ticket-level fields** (populated from the above, or by agent selection): `Tier_tagger` (tiers 1–5, copied from the org's `tier` field), the case type / issue type / reason taxonomy fields, `Consumer_Location_tagger` and `Contracting_CKO_Entity_tagger` (used to key country-specific complaint SLAs — see §9), and `Account_manager_text` (a free-text field, separate from the org-level `account_manager` field).

`account_manager` exists as a clean organization-level field, but the ticket-level "add the account manager as a follower" flow uses a separate free-text field plus a workaround (see §15) rather than reading the organization field directly. A relevant question for this exercise: could ticket-level routing read account attributes directly, rather than requiring that propagation step?

---

## 5. Routing

**Routing attributes** (skills-based):

| Attribute | Values | Purpose |
|---|---|---|
| Tiers and Pods | 3 | Tier/pod skill matching |
| General Skills | 10 | Cross-cutting skills |
| Issue Type Skills | 14 | Issue-type-specific skill matching |
| Related Products | 10 | Product-specific routing |

**Tier propagation** runs through three separate configuration objects:
1. An automation (one per tier, 1–4) copies the org-level `tier` field onto the ticket's `Tier_tagger` field.
2. A trigger (one per tier, 1–5) routes the ticket to the matching group/pod based on `Tier_tagger`.
3. An SLA policy filters on `Tier_tagger` to apply tier-specific response targets (see §9).

**Groups (25)**: tiered/skill groups (L1, L2, Pod 1–4, Seniors, L1 Routing Pilot), functional groups (Dispatch, Complaints Agents, Consumer Support, IDV, IDV Care Agents, MCR Skilled Agents, Commercial, Knowledge Management + 3 knowledge-champion variants, Operations Centre, Transfer Approval, QA, Admin, Leaders), and one AI-tool pilot group (Glean Pilot — see §14).

**Queues (10)** — a second routing dimension layered on top of groups, based on priority and SLA proximity: Urgent/High/Normal/Low priority, SLA-breach-in-1-hour, SLA-breach-in-8-hours, SLA-breached-24+-hours-ago, Outage tickets, Consumer Support, L2 Pods 1–4.

**Workspaces (7)**: bundles of macros and fields visible per team — Level 1, Level 2, Level 1 Account Unlock, Complaints, Consumer Support, Dispatch, Default.

**Dispatch safety net**: a backstop automation, a dispatch trigger, and a catch-all trigger together handle any ticket that falls through routing with no group assigned.

---

## 6. Permissions — Custom Roles

12 custom roles define agent capability, separate from group membership (which drives routing, not permissions): Admin, Leaders, Seniors, L2 Seniors, L1/L2 Agent, Light Agent, Operations Centre, Process Specialists, Knowledge Management, Contributor, Analyst (Data & Analytics), Billing Admin.

Sampled Admin vs. L1/L2 Agent vs. Light Agent shows real differentiation, not just naming:

| Capability | Admin | L1/L2 Agent | Light Agent |
|---|---|---|---|
| Chat/voice access | Yes | Yes | No |
| Manage business rules (triggers/automations) | Yes | No | No |
| Manage dynamic content | Yes | No | No |

Light Agent is a restricted seat type (view/comment access only, no business-rule or content management) — commonly used for internal stakeholders who need visibility into tickets without a full agent seat.

---

## 7. Custom Statuses — Granular Hold/Pending States

Beyond the 6 native Zendesk statuses, 14 custom sub-statuses drive automation logic:

- **Hold**: Awaiting Approval, Flow - Response Received, Pending Appeal, Raised with External Team, Raised with Internal Team
- **Pending**: Waiting on Requester, Waiting for Merchant after Chaser, Token Migration - With Merchant
- **Open**: In Progress, Under Review, Ready to Publish (these three are knowledge-article workflow states reusing the ticket status model, not customer tickets)

These sub-statuses, not the six native ticket statuses, are what most of the time-based automation and escalation logic actually keys on (see §11).

---

## 8. Locales and Business Hours

**Locales (5)**: US English, UK English, French, Canadian French, Japanese. SLA policies cover more countries than there are configured locales (for example Brazil, New Zealand, UAE, Singapore, Australia, and Hong Kong) — those markets appear to be served in English rather than a localized language.

**Business hours schedules (4)**: Core Hours, Outside Core Hours, plus dedicated schedules for Complaints and Consumer Support. Most SLA policies run on calendar time rather than these named schedules; a smaller number appear to use business-hours-aware clocks — this distinction matters for how response-time targets are actually calculated.

---

## 9. SLA Policies (current model)

34 policies — far more than a simple tier matrix. Four independent dimensions combine:

| Dimension | Example policies |
|---|---|
| **Tier** | Tier 1, Tier 2, Tier 3/4/5, Tier not known, Escalations - Tier 1/2, Escalation - Tier 3/4 |
| **Geography** (for complaints) | UK, France, UAE, Canada, Brazil, New Zealand, USA, Singapore/Australia/Hong Kong, all other countries |
| **Channel** | Standard Messaging, Standard Messaging - Session Ended, Enterprise Messaging (sub-minute first-reply targets for live messaging) |
| **Case class** | Outages (6h), Password resets (24h), Termination tickets (48h), IDV (24h), Knowledge Requests (7 days), MCR (15/30 day variants), Token Migration (14 days), QA, Approvals (2h) |

Filters combine taxonomy fields, tags, ticket form, and channel — not a single clean dimension. Per-country complaint SLAs are keyed on a structured location/entity field. This raises a natural question for this discussion: does Plain model SLA policy as a single multi-dimensional matrix, or would it require a comparable number of discrete policy objects to reproduce this?

---

## 10. Triggers — by Category

318 active triggers span 24 categories in active use, out of 47 defined (23 exist but have zero triggers assigned):

| Category | Count | Purpose |
|---|---|---|
| Set Fields | 59 | Field population/mutation logic |
| Notifications | 49 | Requester/CC notifications, split by channel and requester type |
| Ticket creation | 37 | Initial tagging/routing on creation |
| Assign | 29 | Routing/dispatch |
| Skill Management - Case Type Set | 16 | Skills-routing tag logic, by case type |
| Catch-all and mop-up | 15 | Safety nets |
| Skill Management - Level 1 & Others | 14 | L1 skills routing |
| Priority Management | 12 | Priority escalation logic |
| Skill Management - Issue Type Set (Transactions) | 12 | Skills routing for transaction issue types |
| Skill Management - Level 2 | 11 | L2 skills routing |
| Tiers and Pods | 10 | Tier/pod assignment |
| Intercom Fin | 10 | Fin escalation handoff logic (see §14) |
| Quality Assurance | 9 | QA review workflow |
| App - Approve | 7 | Approval workflow app integration |
| Dispatch | 6 | Manual re-dispatch |
| Keyword | 4 | Keyword-triggered routing |
| Escalations | 3 | Escalation handling |
| Skill Management - Tiers & Pods / Case Type Swaps | 3, 3 | Skills routing edge cases |
| Side Conversations, Set Form, OOO, Skill Management - Issue Type Config Changes, App - Timers | 1–2 each | Miscellaneous |

Skills-based routing is split across six separate categories rather than one routing engine — the result of incremental buildout rather than a single designed skills model.

---

## 11. Automations — Full List by Function

48 automations in total:

- **Complaints escalation chasers** (7): internal-team chasers 1–4, merchant chasers 1–3, chained via tags
- **SLA/queue breach notifications** (7): breach-approaching and breach-occurred alerts for complaints, urgent-priority tickets, Tier 1 high-priority, and knowledge-request tickets, routed through a third-party SLA/queue alerting app rather than native Zendesk
- **Pending/courtesy reminders** (6): notifications at 24/48/72 hours pending, courtesy emails at 48/96/144 hours on hold
- **Reopen logic** (3): after on-hold internal-dependency wait, after on-hold external wait, on due date
- **Tier propagation** (4): org tier → ticket tier, one automation per tier
- **QA lifecycle** (4): eligibility tagging, auto-solve stale tickets after 2 weeks, close-if-no-appeal after 5 days
- **Consumer Support nudges** (2): reminder at 3+ days waiting, auto-solve at 5 days waiting
- **Priority-breach automations** (2): critical (2h service-level objective), high (8h)
- **CSAT** (2): notify recently sent, request rating on auto-solve
- **Outage handling** (1): reopen confirmed outage tickets after 2h waiting on internal
- **Cleanup/housekeeping** (3): audit ticket cleanup, test-ticket cleanup, close 7 days after solved
- **Fin failsafe** (1): a safety-net automation specifically for the Fin integration (see §14)
- **Dispatch** (2): reroute tickets with low SLA, tag on-hold tickets after 24h internal dependency

---

## 12. Execution Order

Two separate ordering rules govern how the above actually fire:

- **Automations run in one strict global order**, evaluated on a fixed hourly schedule. The order runs housekeeping first (close-after-solved, reopen on-hold), then reminders, then tier propagation, then the rest.
- **Triggers run in order within each of the 24 active categories**, not globally. Within "Ticket creation," for example, the sequence is: IDV ticket creation, then Merchant Care Escalation creation, then QA Task creation, then Terminations creation, then several tagging/propagation triggers, then Consumer Support creation triggers. A ticket matching multiple triggers in a category is affected by all of them in this fixed sequence, and one trigger's action can satisfy a later trigger's condition within the same pass.

This ordering is itself part of the operational logic, distinct from the dependency chains in §13: §13 shows what depends on what, while this section shows the sequencing that makes those dependencies work correctly.

---

## 13. Tag Dependency Graph

Across all 318 triggers and 48 automations: 171 distinct tags are set by some rule, 87 are checked as a condition, and 45 tags are both set and checked — genuine dependency chains between rules. This pattern exists because automations have no native "fire once" mechanism: every time-based rule must tag itself to avoid re-firing on the next run. Verified multi-step chains include:

- **Complaints escalation**: merchant chaser 1 → 2 → 3, each automation checking the previous tag before firing and setting the next
- **Complaints internal-team escalation**: chaser 1 → 2 → 3 → 4, running in parallel to the merchant chain
- **Pending reminders**: reminder 1 → 2 → 3, with a separate reset trigger that clears the whole chain
- **Tier propagation**: a tag is set and checked by the same 4 automations (self-gating, not a cross-rule chain)
- **Outage/termination/escalation ticket lifecycle**: each is tagged once at creation and checked by 3–9 downstream rules (courtesy emails, pending notifications, and breach alerts all branch on these)
- **QA lifecycle**: eligibility, first-contact-resolution, and no-appeal-closure tags chain QA eligibility through to auto-close

This tag graph functions as a substitute for a genuine state machine, since automations have no built-in way to track progression through a lifecycle. A platform with native, time-based lifecycle states would likely replace most of this dependency graph with direct configuration rather than custom logic.

---

## 14. Apps & Integrations

37 installed apps. Confirmed integrations, with usage verified against source (not just presence of installation):

| Integration | Purpose |
|---|---|
| Fin (Intercom) | The active AI layer — escalation handoff, with a dedicated failsafe automation and 10 triggers in the "Intercom Fin" category |
| Jira | Bi-directional ticket sync |
| Salesforce | Case number sync |
| Glean | Enterprise search/AI, with an active pilot group — appears to be a limited trial rather than a full rollout |
| Third-party SLA/queue alerting app | Drives the breach-notification automations in §11 |
| Data pipeline connectors (3) | Feed a downstream data/analytics pipeline |
| Knowledge Capture + article-sync webhooks | Syncs published Help Center articles to an external content system |
| Approval app | Backs the Transfer Approval group and the approval-workflow trigger category |
| Customer 360 sidebar apps (2) | Built as iframe embeds — would need an alternative integration approach on a platform without iframe support |
| Call/IM ticket creators | Phone and instant-messaging channel ticket creation — relevant to phone-channel compliance requirements |
| Data-removal notification | A single compliance-related trigger and notification target for data-removal requests |
| Internal tooling (7 apps) | Custom-built operational tooling for power actions, timers, field rules, SLA event tracking, and validation — not off-the-shelf Zendesk capability |

32 webhooks in total — the table above covers the named integrations; the remainder are internal event plumbing (a general ticket-created/updated/user-created gateway, plus the account-manager workaround in §15).

---

## 15. Notable Workarounds and Technical Debt

- **Account manager via a self-calling webhook**: a webhook fires a call back to Zendesk's own API to add the account manager (read from a free-text field) as a ticket collaborator, because triggers cannot set collaborators directly.
- **An unused custom object from an earlier test** exists in the configuration history but has no functional role in production and is not referenced by any live trigger, automation, or field.
- **Tag-gating as a state-machine substitute** (§13) — the largest structural pattern that a platform with native time-based lifecycle states would likely eliminate.
- **Skills-based routing split across six trigger categories** rather than a single unified routing engine (§10).
- **23 of 47 trigger categories are unused** — configuration debt rather than active logic.

---

## 16. What's Rollup-Only, Not Individually Verified

Everything above was parsed and verified from source. Two content types were counted and pattern-matched by name only, not individually read:

- **Macros (323)**: namespaced by category (for example "Access & Permissions," "Complaints"), mirroring the support taxonomy — confirms macros are organized around case type/issue type, but individual canned-response text was not reviewed.
- **Views (116)**: named around SLA breach windows, tier, and team — confirms views implement a queue-management, pull-based model, but were not individually reviewed.

Neither is likely to change the overall picture (they are presentation/canned-content layers, not logic), but this is flagged for completeness rather than treated as exhaustive.

---

## 17. Explicitly Out of Scope

Zendesk Guide (the help center / knowledge base) is not covered by this document and was not assessed as part of this exercise.

---

## 18. Example End-to-End Flows

Four worked examples, chosen for how heavily connected they are in the configuration (largest trigger categories, longest tag-dependency chains, and the one confirmed-active AI layer) rather than by actual ticket volume, which isn't visible from configuration alone. Together they touch nearly every mechanism described above.

### Flow 1 — Merchant ticket creation and tier-based routing (Checkout.com brand)

1. A merchant submits a request through the Merchant Care form or by email.
2. Two enrichment steps run in parallel in the background: one confirms the ticket was created successfully, the other refreshes the requester's contact record. Once both complete, the ticket is tagged as enrichment-complete.
3. Separately, another rule copies the account manager, technical account manager, sales engineer, and implementation engineer details from the organization record onto the ticket — falling back to whatever the merchant entered if no organization match is found.
4. On the next hourly automation run, if the organization has a tier set and the ticket doesn't yet have one, the tier is copied onto the ticket.
5. Once enrichment is complete and a tier value is present, a tier-specific rule routes the ticket to the matching group (for example, Tier 1 tickets go to the L1 group) and applies routing/skill tags.
6. The matching SLA policy — tier-based, or a specialized policy such as Outages, Password Resets, or a country-specific complaint policy — sets first-reply and resolution targets (§9).
7. A notification confirms receipt to the requester, worded differently depending on channel and whether the request came directly from the merchant or was raised internally on their behalf (§10).
8. If the ticket goes on hold or stays pending, the reminder/courtesy-email chain begins (§11, §13).

This single journey touches the data model (§4), routing (§5), SLA (§9), notifications (§10), automations (§11), execution order (§12), and tag dependencies (§13) — nearly every mechanism in this document participates before a ticket reaches its first human assignment.

### Flow 2 — Consumer ticket creation (Checkout.com Consumers brand)

1. A consumer contacts support, either through a channel already tagged to the Consumers brand or by emailing the consumer support address.
2. A single rule sets the brand, ticket form, and group to their consumer-support equivalents, applies a required Consumer Support skill for routing, sets priority to normal, and tags the ticket.
3. A second rule marks the requester's contact record as a consumer contact.
4. The applicable SLA policy depends on whether the ticket is a complaint (a country-specific policy — UK, Brazil, USA, and others) or a general consumer support request (a separate, non-complaint policy).
5. If the ticket sits waiting on the consumer for 3 or more days, a reminder nudges them; if it's still waiting at 5 days, it is automatically solved.

This flow is materially simpler than Flow 1 — one routing rule instead of a multi-step tier chain — but shares the same SLA and reminder mechanisms.

### Flow 3 — AI-first handling and failsafe (Fin, applies across brands)

1. On creation, new tickets across most channels — webform, API, messaging, and password-reset requests — are automatically assigned to Fin, Checkout's AI agent.
2. Fin works the conversation. Three outcomes are handled explicitly: if Fin resolves the ticket, it is marked solved; if Fin can't answer, it is marked open, releasing it back for routing; if Fin's answer doesn't fully resolve it, it is marked pending.
3. A safety-net rule checks hourly for tickets still assigned to Fin with no update in over an hour and status still new or open. These are unassigned and tagged, which allows them to flow into the standard routing described in Flow 1.
4. If a conversation Fin is already handling receives an update, a rule notifies Fin directly rather than waiting for the hourly check.

Fin is the only confirmed-active AI layer in the current configuration (§14). The failsafe in step 3 is what prevents a ticket from being silently stuck with Fin if it doesn't respond in time.

### Flow 4 — Complaints escalation (Checkout.com brand)

1. A ticket is identified as a complaint, through the Complaints form or a complaint tag.
2. The country-specific SLA policy applies, based on the merchant's contracting entity and location (§9).
3. If the complaint sits unassigned and is approaching or has breached its SLA, a third-party alerting app sends breach notifications (§11).
4. Two parallel chase chains run on elapsed time: one addressed to the merchant (chaser 1 at 72 hours, then chaser 2, then chaser 3) and one addressed to the internal team handling the dependency (chaser 1 at 72 hours, through to chaser 4). Each chaser checks that the previous one already fired before sending the next, and tags itself so it doesn't repeat.

This is the deepest tag-dependency chain in the configuration (§13) — up to four sequential steps on the internal side alone, each gated on the previous one's tag.

---

## 19. Mapping to POC Test Areas

| Test area | Where it's covered in this document |
|---|---|
| Three-layered taxonomy (case type / issue type / reason) | §2 (form conditional logic), §9 (SLA filters) |
| Ticket routing to queues | §5 |
| Routing and SLA by taxonomy | §5, §9 (current model only) |
| Routing on dynamic fields (e.g. location) | §5, §9 |
| Modelling of users/organizations (tenants) | §4 |
| Merchant vs. consumer separation | §1 — already live via a separate brand |
| Existing apps integration path | §14 |

---

Prepared by Checkout.com for the Plain proof-of-concept · 2026-07-31

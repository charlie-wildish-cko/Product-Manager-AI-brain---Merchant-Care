# Support Platform Assessment: Customer References

**Purpose**: the single live home for every reference call and vendor call run during the support platform assessment. Extracted 2026-09-22 from `05-archive/2026/investigations/zendesk-platform-decision-rfc.md` when that RFC was archived, so the evidence behind the Plain recommendation stays in active work rather than in the archive.
**Owner**: Charlie Wildish
**Status**: Live. Add new calls here, not into the deck or the scorecard.
**Related**: `support-platform-vendor-scorecard.md` (the scores these calls feed) · `support-platform-vendor-requirements.md` (requirement definitions) · `../working-files/zendesk-decision-deck-content.md` (recommendation and ask) · `plain-business-case-draft-v1.md` (POC results)

---

## How to read this

Four evidence tiers appear below, in descending order of trust. Never quote a finding without its tier.

| Tier | What it means | Use |
|---|---|---|
| **1. Reference call we ran** | We spoke to the customer ourselves, unprompted questions, negatives recorded | Usable as supporting evidence for scorecard scores |
| **2. Vendor call** | The vendor describing its own product to us | Directional. Treat capability claims as unverified |
| **3. Vendor-supplied reference** | A customer the vendor introduced or a case study it wrote | Not independent. Label as vendor material whenever quoted |
| **4. Desk research** | Public documentation | Real and citable, but "what the vendor documents" rather than what we tested |

**Ask**: Charlie to run one Plain reference call at 200+ agents before contract signature. Every Plain reference we have is materially smaller than our 500-agent target, which is the single biggest gap in this evidence base.

---

## Summary

**TLDR:** Two independent Plain customers both report that ticket-tracker linking has to be self-built, which contradicts our own POC finding of "native". That is the one disagreement in the evidence base and it is unresolved.

| Customer | Vendor | Tier | Scale | What it proves | What it warns |
|---|---|---|---|---|---|
| **Vercel** | Plain | 1 | ~60 agents, ~1,200 cases/week, 1 operator | Headless model works in production. Full GraphQL SDK. Config managed through code | Roadmap slips. Tracker linking self-built. Workspaces rather than granular RBAC |
| **Fyxer** | Plain | 1 | Not recorded | Many-to-many data model and custom app building solved what Intercom could not | Agent UI too busy, too many clicks |
| **Tines** | Plain | 1 | Not recorded | Fin-to-Plain escalation runs in production | None recorded |
| **Zilch** | Intercom | 1 | ~250 BPO agents + 40 internal, hundreds of thousands of contacts/month | Intercom can deliver a strong partnership. Fin plus live chat called "seamless" | Cannot group team members into organisations. Fin change control is a black box |
| Intercom | Intercom | 2 | n/a | Strong ticketing, native connectors, good API coverage | Copilot is a black box. UI-only config. Restrictive object model |
| Plain proof points | Plain | 3 | Various | Nothing independently | Marketing collateral. Excluded from the deck's core slides |

---

## Provenance corrections, 2026-09-22

Two numbers in circulation needed re-sourcing. Both are now labelled correctly here, and the deck has been corrected.

1. **"First response time down 30% overall, 67% Enterprise, 78% Pro" is Plain marketing, not our Vercel call.** It appears verbatim in `evidence/plain-checkout-proof-points.pdf` and appears nowhere in the reference call record. It is tier 3. Do not present it as independent evidence.
2. **"19% more tickets resolved per CSE" appears in both the business case and Plain's own collateral.** `plain-business-case-draft-v1.md` reports a 19% efficiency gain with 20% of support headcount redeployed, and the same 19% is in the vendor PDF. Independent provenance is unconfirmed, so treat it as tier 3 until Vercel confirms it directly.

---

## Vercel (Plain), tier 1

**Called 2026-09-18. Will Viles. Migrated from Salesforce Service Cloud.**

**Scale caveat, read first.** ~60 support agents, ~1,200 cases a week, with a single system operator owning all admin, configuration and integration work. Materially smaller than our 500-agent target. Treat scale-dependent findings (data segregation, the config-as-code operating model) as directionally useful rather than scale-validated.

**Why they chose Plain.** The vision of headless support, and because they did not want off-the-shelf agents: they wanted to build every agent themselves (help box, triage, retro). They were "customer zero" for a lot of functionality, so this was a heavy co-build relationship rather than configure-and-go.

**AI compatibility (scorecard 3.3), the strongest signal in this file.** A full custom multi-agent architecture built on Plain's API. A first-contact agent creates the case, a fast triage agent runs on creation and posts a note without investigating deeply, and enterprise or notable accounts get a retro afterwards. All of it Vercel's own logic, with Plain providing the substrate. Direct quote: "everything is easy, and you're completely in control." This is close to a working production example of our own "abstract our core services" principle.

**Integration ease (scorecard 2.5), strength.** Plain exposes its full GraphQL SDK. "You can do anything that they do inside their UI", entirely webhook-driven, integration logic written in TypeScript. The strongest API-completeness signal gathered from any call.

**Integration ease (scorecard 2.2), gap.** Native Linear and Jira-equivalent ticket linking is "very basic". CS and engineering built the entire flow themselves (custom app, prefilled form, mutating the thread via API), a 6-month effort. Confirmed the same is true for Jira specifically when asked directly. Anything not core to Plain's own product must be self-built on the GraphQL API.

**Config as code (scorecard 5.3).** Configuration managed primarily through code and API ("edge config" for dynamic settings), not the UI. Exception: the hierarchical labelling and tagging model used for analytics is managed more directly and transiently, not fully as code.

**Data and permissions (scorecard 4.11 and 4.12), significant gap.** Plain requires separate workspaces for privacy, security and trust segregation rather than granular RBAC within one workspace. Will called this "one area I think they're lacking in" and said Plain "hasn't really wanted to work on" resolving it. Cross-workspace visibility needs an API call even within the same company, which he agreed "doesn't really make sense." Plain added basic cross-workspace thread-state API support only in September 2026, and he believes a label-based approach is in progress but could not confirm.

**Do not assume this maps to us.** Vercel split workspaces for their own privacy and trust reasons, not a B2B/B2C split. We do not yet know whether our data-wall requirement needs multiple workspaces the way Vercel's does, or whether RBAC within one workspace would suffice. Confirm our own need first, then test the relevant mechanism directly.

**Partnership fit (scorecard 6.1), negative.** Roadmap delivery has slipped materially. Functionality quoted at "4 months" twelve months ago took 8 months to ship. Direct quote: "they haven't exceeded expectations... but they do get round to it." Consistent with a vendor that is not the fastest, compensated for by API-level flexibility to build around gaps.

**Reliability (scorecard 6.4).** "Absolutely zero downtime" reported. Informal, not a contractual SLA data point.

**Implementation weight (scorecard 6.3).** All admin, requirements gathering and the original Salesforce migration run by one system operator supporting ~60 agents. Strong evidence that Plain's day-to-day operating overhead is light enough for a single admin to own. Also a single point of failure at their scale, and not evidence the same model holds at 500 agents.

**Channels (scorecard 1.6).** Native Slack support in progress. Previously required a custom-built agent to ingest Slack threads. Their support centres on Slack as the primary customer-conversation surface, a deliberate design choice rather than a ticket-first model, which may not map onto our channel mix.

**Migration precedent.** Vercel did not migrate historical case or thread data from Salesforce, having decided it was not worth the effort because the data models did not match cleanly. This matches our own prior Salesforce-to-Zendesk approach and is useful precedent for the Zendesk migration.

---

## Fyxer (Plain), tier 1

**Called September 2026. Yannis. Left the full Intercom suite, including Fin, in early 2026.**

**Why they left Intercom.** To run their own customer-facing AI agents on their own backend, chat and data. Two specific blockers: Intercom's user-to-company mapping was too rigid for a user belonging to more than one account, and Intercom's first-party app marketplace made a custom build hard to get supported.

**What Plain solved.** The many-to-many user-to-company data model handled the first problem. Native custom app building handled the second.

**What they built on it.** Sidekick skills including auto-creating and linking Linear tickets to a thread, and an incident-detection skill that flags when multiple customers report the same issue.

**Second independent signal on the tracker-linking gap (scorecard 2.2).** Their Linear linking is a custom Sidekick skill they built themselves, not a native connector. Different tracker and different mechanism from Vercel's, same conclusion: two independent customers both had to build something.

**Agent experience (scorecard 4.1), negative.** Plain's agent UI "could be more polished", described as too busy, and the in-thread Discussions feature takes too many clicks. This is the first negative signal about Plain's interface itself rather than a missing feature.

**Score changes this call produced.** Intercom 1.21 moved from 3 to 2 on the contact-to-company schema limit, a hardcoded problem that Intercom's general Custom Objects flexibility does not reach. It also corroborated Intercom's app-marketplace friction and Copilot's native-AI conflict (3.3, 3.5) and Plain's customer cards and bring-your-own-agent capability in live production use (3.5, 4.4).

**One finding of theirs is now out of date.** Fyxer evaluated Pylon in February 2026 and found it closed to third-party AI agents. Re-verified 2026-09-21 against Pylon's own documentation and it has changed: Pylon now ships a real "Bring Your Own Agent" capability (Skills, webhooks, custom API actions, MCP), and row 3.3 moved from 0 to 2 as a result. Do not repeat the February finding as current. The case against Pylon rests on no config-as-code, Slack-first design and the wrong shape for multi-segment routing.

---

## Tines (Plain), tier 1

Runs Fin-to-Plain escalation in production today and validated the integration architecture directly with us. This is the reference behind the POC's "Fin escalation validated" result in section 7 of the evaluation criteria. Source: `plain-business-case-draft-v1.md`.

---

## Zilch (Intercom), tier 1

**Called September 2026. ~250 BPO agents plus 40 internal staff. Migrated off Zendesk to Fin plus Intercom.**

**Scale context that matters for us.** Zilch handles contact volume in the hundreds of thousands a month against our roughly 5,000, and is Intercom's number two account. Their level of vendor attention is not available to us at Intercom today, and the Salesforce acquisition pushes it further out of reach.

**Partnership fit (scorecard 6.2).** Chose Intercom to be "a bigger fish in a smaller pond", wanting to be a material customer where scale matters to the vendor. Cited better responsiveness and consultancy than they got from Zendesk or Salesforce, who they felt did not guide them on how to use the technology. Now locked in, with a strong relationship, despite the Salesforce acquisition.

**Partnership fit, negative.** "The person you get for help is key." Support quality is individual-dependent rather than a consistent guarantee.

**AI compatibility (scorecard 6.1), negative.** Growing pains with change control on Fin, and a black box on which features are coming next. Corroborates our own vendor call's black-box finding on Copilot.

**Channels (scorecard 1.4 and 1.5), strength.** Live chat plus email with Fin integration called out as a standout strength, described as "seamless".

**AI compatibility (scorecard 3.1 and 3.3).** Uses Fin's attribute detection to control conversation flow. Matches our pluggable-AI requirement in spirit, though this is Intercom's own AI rather than an external one.

**Integration ease (scorecard 2.7 and 2.9).** Uses the "Pro" analytics tier, and flags that it is a paid add-on rather than included in the base.

**Agent experience (scorecard 4.6 and 4.7), with a specific limitation.** Multi-agent, multi-location and BPO setup runs via separate Inboxes per line of business (Chargebacks, Collections, Refunds), each assigned to a specific BPO. They cannot segment team members into organisations: members are assigned to an Inbox individually rather than grouped by org. This is a materially different model from a true B2B/B2C data wall.

**This is the same class of gap we found on Plain.** Zilch cannot group team members into orgs, Vercel needs separate workspaces. Both vendors handle multi-team and BPO data segregation more coarsely than a native granular data wall. Neither is a differentiator between them.

**Agent experience (scorecard 4.12).** Custom roles available to restrict conversation and report visibility.

**Config as code and AI compatibility (scorecard 3.4 and 5.3).** Workflow automation described as helpful for both AI flow control and SLA management. SLAs are managed via workflows rather than a native SLA policy engine, a mechanism difference worth noting even where SLA enforcement is achieved.

**Channels (scorecard 1.9).** Second and third-line technical teams work from back-office tickets only, consistent with our own vendor call's description of the back-office ticket model.

---

## Intercom vendor call, tier 2

**September 2026. Qualitative. Does not feed the scorecard's numeric scores.**

**Strengths described.** Strong as a ticketing system, with native Fin, Copilot for agent AI, and a workflow builder as a UI layer rather than Zendesk-style trigger configuration. All standard channels native. An Operator AI tool for internal diagnosis on tickets and metrics. A simple back-office ticket model. Native Jira and Salesforce connectors. Simple UI, separate test and production environments for config changes, good API endpoint coverage.

**Gap, AI compatibility (scorecard 3.3).** Copilot has no custom integrations and limited skill customisation, described as a black box. This weakens the case for Copilot as the Agent Consultant equivalent inside Intercom.

**Gap, config as code (scorecard 5.3).** Configuration is mostly via UI, not config-as-code. The vendor says this may improve long term with nothing committed.

**Gap, agent experience and data model (scorecard 1.21, 4.11 and 4.12).** The object model is restrictive: it mandates certain data points, and nested logic would need custom API calls to link field IDs rather than native support.

**Gap, Ops-wide fit (scorecard category 4).** Not convinced Intercom fits Ops teams beyond Care. It is built for customer-facing work, not internal enabling work with AI workflows across teams.

---

## Vendor-supplied material, tier 3

`evidence/plain-checkout-proof-points.pdf` lists SpaceX AI, Sanity, Yapily, Sourcegraph, Avara and others, plus the Vercel outcome figures corrected above. This is Plain's own collateral, written by Plain. It is deliberately excluded from the deck's core slides, because the value of the tier 1 calls above is that we ran them ourselves and recorded the negatives. Quote from this PDF only with the tier stated.

---

## What the references agree on

1. **Plain's API completeness is real.** Vercel and Fyxer both built production AI agents on it, independently, and both describe the substrate as sufficient.
2. **Anything outside Plain's core product must be self-built.** Two independent customers, two different trackers, two different mechanisms, same conclusion. This is the one finding that contradicts our own POC and it is unresolved.
3. **Neither Plain nor Intercom offers a native granular data wall.** Plain splits workspaces, Intercom assigns individuals to Inboxes. Not a differentiator.
4. **Plain is not the fastest vendor.** Vercel on roadmap slippage, Fyxer on UI polish. Both chose it anyway, for control.
5. **Vendor attention tracks account size.** Zilch earned Intercom's attention by being its number two account. We are not that account at Intercom. We are a material account at Plain's current size.

## What is still missing

- No Plain reference above ~60 agents. Our target is 500.
- No reference has tested our specific B2B/B2C data-wall requirement, only their own segregation needs.
- No Pylon reference call at all. That column is desk research against public documentation, which a fast-shipping vendor can outdate within a month.

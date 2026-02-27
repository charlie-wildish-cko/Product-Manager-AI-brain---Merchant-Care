# Internal Teams & Stakeholder Groups

> Reference for consistent team naming in PRDs, stakeholder updates, and other documents.  
> Update this file whenever team names change — then docs that reference it stay correct.

**Last Updated**: February 2026  
**Owner**: Charlie Wildish


## Care & Support Teams

| Team | Notes |
| --- | --- |
| **Care Operations** | Day-to-day support operations. Previously referred to as "CX Operations" — use Care Operations in all new documents. |
| **Operational Excellence** | Process quality, SLA governance, QA, scheduling, and operational standards. Often co-owns work with Care Operations — reference both where relevant: "Care Operations and Operational Excellence". |
| **Zendesk Admins** | Own all Zendesk configuration: triggers, views, routing rules, org setup, ticket forms, brands, email identities, and any other Zendesk-native tooling. This is not Engineering work — Zendesk admins are a specialist ops/admin function within the Care team. |
| **Merchant Experience** | Merchant-facing experience quality; typically a stakeholder for anything impacting how merchants interact with support channels. |

## Engineering Teams

| Team | Notes |
| --- | --- |
| **Engineering** | Builds APIs and applications around Checkout.com products. Responsible for backend services, internal APIs, and integrations that sit outside Zendesk itself (e.g. Client ID validation APIs, webhook receivers, data pipelines). |
| **Dashboard Engineering** | Owns the Merchant Dashboard product. Relevant for support channels or tooling embedded in the Dashboard (e.g. pre-populated webforms, session-based identity). |


## Commercial Function

The Commercial team owns merchant relationships across the full lifecycle — from sales and onboarding through to long-term account management. They are both an internal customer of Care tooling and an active source of support contact volume (~8–10% of annual ticket volume), raising tickets on behalf of their merchants.

| Role | Abbreviation | Scope | Notes |
| --- | --- | --- | --- |
| **Sales Lead** | — | Merchant onboarding and first 3 months | Primary commercial relationship during onboarding; hands over to AM after 3 months |
| **Sales / Solution Engineer** | SE | Merchant onboarding and first 3 months | Works alongside the Sales Lead to support technical needs during onboarding |
| **Account Manager** | AM | Primary merchant contact post-3 months | Takes over from Sales Lead as the merchant's main Checkout.com contact |
| **Technical Account Manager** | TAM | Same scope as AM but for largest merchants | Technical version of the AM role; reserved for Tier 1 merchants only |

### AM/TAM as a Contact Channel

AMs and TAMs raise tickets to the Care team on behalf of their merchants. This is a distinct contact pattern from direct merchant submissions:

- **Current state**: Tickets submitted via email — unstructured, requiring manual identification and context extraction by Care agents
- **In progress**: A structured form for AM/TAM ticket submission is being built by Charlie's team (replaces email)
- **Later in 2026 (planned)**: **Sonar** — an internal AI agent in Slack, built by the central AI team, available to all Checkout staff. Relevant here because AMs and TAMs will be able to use it to answer queries and escalate to Zendesk if needed. Internal-facing only; distinct from Fin, which is customer-facing

When an AM or TAM raises a ticket, the ticket must be attributed to the merchant they represent — not to the AM/TAM themselves. This is an important distinction for SLA assignment, routing, and org-level reporting.

**2028+ evolution**: As Checkout introduces B2B banking products (merchant balance holding, interest on deposits), the AM/TAM role will expand to cover banking relationship management alongside payments. This will change the nature of what they escalate to Care (adding treasury, yield, and balance query types) and will require Sonar's knowledge base to include banking product content.

## Other Common Stakeholders

| Team | Notes |
| --- | --- |
| **Account Management** | Owns merchant relationships for Enterprise and Premium accounts. Relevant for domain data, org setup, and merchant-specific config. See Commercial Function above for role definitions. |
| **Sales Ops** | Owns CRM (Salesforce) data and account records. Source of truth for merchant domains and account attributes. |
| **Dashboard Engineering** | Owns the Merchant Dashboard product. Relevant for any support channel embedded in the Dashboard. |
| **Blue EMI Programme** | Owns the Blue EMI entity rollout. Stakeholder for any support infrastructure specific to Blue EMI merchants. |


## Naming Conventions

- Do **not** use "CX Operations" or "CX Ops" — the correct name is **Care Operations**
- When both operational teams are relevant, write: **Care Operations and Operational Excellence** (full) or **Care Operations / Op Ex** (in tables/shorthand)
- "Support Engineering" is distinct from "Care Operations" — engineering builds the tooling; Care Operations runs it

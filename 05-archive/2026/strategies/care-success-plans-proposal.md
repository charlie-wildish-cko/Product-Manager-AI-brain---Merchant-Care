# Merchant Care Success Plans

# **Executive Summary** 

Today Merchants face inconsistent, one-size-fits-none support that negatively erodes trust and drives up costs. This proposal presents a three-tier care success plan, Standard, Enterprise, and Premier, aligned to clear revenue bands and designed to deliver the right response time, channels, and expertise each merchant segment needs to thrive. Our model is structured to meet, and in key areas, exceed Adyen's level of support by offering additional communication channels and proactive health checks within the higher tiers. By setting a new standard for responsiveness and operational partnership, we ensure every merchant, from small businesses to strategic accounts, receives support tailored to their needs.

### **Level Structure**

| Model | Support Level | Data definition | Cost per contact | 2025 ticket % | Merchant Profile | Operational tooling | Key Benefits |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| B2B (Direct Merchants, Issuing, IDV, Platforms \- indirect sub merchant support) | Premium (\> $xxxk NR OR Strategic) | Account Owner Territory \= SAT  or Tier 1 & Incentive rating \= Gold |  | 31% | Top-50 accounts and mission-critical merchants. High-value, high-volume, complex, bespoke setups. Payment operations are core to their model, with zero tolerance for downtime.   | Mature Self built, cutting edge tools for their operational teams to diagnose orders and payments. Using our APIs/Webhooks.  | Same as below \+ Fastest SLAs Named Support Engineer Regular health reviews Escalation management  |
|  | Enterprise ( \< $xx \> $xxx NR) | Tier 1 not Gold or Gold not Tier 1 or Tier 2 & Silver |  | 33% | Mid-to-large businesses with established operations and growing payment needs. Moderate to high complexity in payment flows, reconciliation, and reporting.  | Low/Medium maturity Some tools for teams, but need our Dashboard to fill the gaps. Use our APIs/Webhooks.  | Same as Standard \+ Faster SLAs Dedicated support channels (live chat, video calls) |
|  | Standard (\< $$xx NR) | Rest of merchant book not in above |  | 36% | Small businesses, sub-entities. Minimal complexity in payment flows and operations. | Low maturity Usually no tools, so rely on our Dashboard. API usage is low.  | Reliable baseline SLAs Simplified channels (AI Agent, web, livechat) Business-hours coverage Self-service tools |
|  | Checkout Payfac \- direct sub merchant support and or SMB (NEW, TBC when) | Same as Standard Proxy is Tier 5 merchants |  | \- | Small merchants we directly support with Checkout as primary Platform/Payfac Or SMB merchants we onboard (Tier 5 expansion) | Low maturity Usually no tools, so rely on our Dashboard. API usage is low. | Reliable baseline SLAs Simplified channels (AI Agent, webform) Business-hours coverage Self-service tools Premium offering? Pay more for things like quicker SLAs and live chat? Consumer duties? |
| B2C (Remember Me and Braavos Neobank) | Consumer  | Contacts coming from the Consumer apps/web services |  | \- | Remember Me users Customers using our new Neobank proposition | n/a | SLA within hours? Simplified channels (AI Agent) Business-hours coverage Phone (mandatory) Likely need BPO for 1st line contact handling |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |

# **Problem Statement**

* There are currently no defined support plans, leading to inconsistent and ad hoc service experiences across our merchant base.  
* Different merchants are offered different support channels without a structured or strategic approach, resulting in inefficiencies.  
* Merchants are not aware of which channels or service levels they are entitled to, creating misaligned expectations and undermining trust in support delivery.  
* The existing SLO is a blunt, one-size-fits-all tool, applied uniformly across merchant tiers and issue priorities, which fails to reflect the urgency or complexity of specific requests.

# **Plans**

### **Purpose**

Establish a scalable, tiered support framework that serves the full merchant spectrum, from Consumers, long-tail SMBs and sub-merchants to strategic enterprises, balancing service quality, security, and cost. The model should enable clear commercial upgrade paths while protecting and improving the overall merchant experience.

### **Scope**

This proposal sets the operating model for all operational post‑sales technical support, escalation handling, for acquiring and issuing services offered by Checkout.com. Technical Account Management (TAM), Account Management, and other Commercial teams are out of scope.

### **Plan Benefits at a Glance**

| Benefit | Standard | Enterprise  | Premium |
| :---- | :---- | :---- | :---- |
| Technical point of contact | Pooled support team | Pooled support team | Named Support Engineer |
| Coverage window | 24 × 5 staffed  P1 24 × 7 | 24 × 5 staffed  P1 24 × 7 | 24 × 7 staffed  |
| Escalation manager | N/A | N/A | ✅ |
| SLA commitment\* | Basic (4 h P1) | Enhanced (1 h P1) | Priority (30mins P1) |
| Enforcement | Dashboard only | Email and Dashboard | Email and Dashboard |
| Email user ID approach | n/a | Domain mapping | Domain mapping |
| Auto add AM/TAM to ticket | No | Yes | Yes |
| Dedicated support channels | Phone (P1) callback AI Agent Web‑form Live Chat 09:00–18:00   | Phone (P1) callback Email AI Agent Live chat  Video Callback | Email AI Agent (optional) Phone, Video Callback Slack IM (APAC), Live Chat 24 × 7 |
| Health reporting | N/A | N/A | ✅ (Monthly) |

\*First‑response SLA. See Section 4 for full ladder.

### **Service Level Agreements** 

Resolution by Tier & Issue Type Today [Tier TTR by Issue Type](https://docs.google.com/spreadsheets/d/1vwppAyK9A5EMwXRQNMmJopMPc7wuRv2T3Hxm30zwSFY/edit?gid=491616387#gid=491616387)

| Priority  | Definition | Example query type | Standard | Enterprise | Premium |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **P0**  | Complete processing outage. Severe financial and reputational risk. | All payments failing | First Response: 15 mins Target Resolution: 4 hrs | First Response: 15 mins Target Resolution: 4 hrs | First Response: 15 mins Target Resolution: 4 hrs |
| **P1** | Major functional issues (e.g. sharp drop in approval rates, refund errors, missing settlements). Business impact but not total failure. | All payments failing Settlement not received | First Response: 4 hrs Target Resolution: 1 business day  | First Response: 1 hr Target Resolution: 12 hrs | First Response: 30 mins Target Resolution: 8 hrs |
| **P2** | Limited operational impact. The issue affects non-critical functions or a subset of users. Workarounds may exist. Prioritised as part of standard operational resolution queues. | Refund failed (all transaction issues except above) Password reset | First Response: 12 hours Target Resolution: 2 business day  | First Response: 4 hr Target Resolution: 24 hrs | First Response: 2 hrs Target Resolution:12 hrs |
| **P3** | Minimal impact on operations. Informational issues, minor bugs, or enhancement requests. Does not impact day-to-day merchant activity. | Dashboard page error/UI bug Docs etc | First Response: 1 business day Target Resolution: 3 business day  | First Response: 12 hours Target Resolution: 48 hrs | First Response: 4 hrs Target Resolution:24 hrs |

### **Channels** 

| Channel | Standard  | Enterprise | Premium |
| :---- | :---- | :---- | :---- |
| AI Agent | 24 × 7 | 24 × 7 | 24 × 7 |
| Dashboard Webform  | Business Hours  | 24 × 5   | 24 × 7 |
| Dedicated Email  | N/A | N/A | 24 × 7 |
| Live chat | Business Hours  | 24 × 5  | 24 × 7 |
| Telephone (24\*7) | P1 Only | P1 Only | P1 Only |
| Video Callback / Screenshare | N/A | Scheduled | Scheduled |
| Dedicated Slack / IMs | N/A | N/A | 24 × 7  |

### **Advanced Features (Phase II FY26)** 

| Entitlement | Description | Standard | Enterprise | Premium |
| :---- | :---- | :---- | :---- | :---- |
| Named Support Engineer | A dedicated technical partner for our merchants team, focused on complex issues,and proactive monitoring (see below). While day-to-day tickets are handled by general support, the Named Support Engineer owns high-impact cases and optimisation. | N/A | ✅ | ✅ |
| \*Proactive health reviews | Data-led reviews that uncover friction in a merchants payment flow and highlight revenue opportunities. Each report includes personalised analysis, optimisation recommendations, and optional deep-dive sessions to turn insights into action. |  | ✅ (Quarterly) | ✅ (Monthly) |

\*[Value‑Add Descriptions](https://docs.google.com/spreadsheets/d/1jEBAJG4ikPaz5Vf0cVgZril4TTlmC1DbZ7ZvC6ncYpk/edit?gid=0#gid=0)

### **Competitor Insights**

| Feature | Stripe | Adyen | Worldpay |
| :---- | :---- | :---- | :---- |
| Phone Support | 24/7 for all customers | 24/7 for critical issues (limited) | 24/7 with multiple dedicated lines |
| Live Chat | Yes | No | No |
| Email/Web Support | Web form via dashboard | Web form via Customer Area | Web form \+ Direct email addresses |
| Developer Community | Discord \+ Docs | Docs only | Docs only |
| Self-Service | Extensive \+ guided | Extensive \+ role-controlled | Legacy knowledge base \+ portals |
| Support Plans | Multiple plans incl. Enterprise (paid) | Account-led access control | Merchant-type segmentation |
| Social Media | Active (@stripesupport) | Active (Twitter, LinkedIn, Facebook) | Limited |

**See more details**: [Merchant Care Benchmarking\_2025Q1\_v3.pptx](https://docs.google.com/presentation/d/1TLsxqw0cjscuT4LeHdIPpjXzvV4hmuAb/edit?slide=id.p8#slide=id.p8)

### **Options Considered**

| Option | Pros | Cons | Decision |
| :---- | :---- | :---- | :---- |
| 2 Tiers (Standard vs Enterprise) | Simple, fewer SKUs | No mid‑price step | **Rejected** Doesn’t meet mid market needs / delta between enterprise and standard too large |
| Baseline +  a la carte add‑ons | Flexible | SKU sprawl Quote fatigue Routing complexity | **Rejected**.  Ops & Commercial overhead |
| Bespoke SOW per large client | Tailored | Legal overhead. No economies of scale | **Rejected**. Not scalable |
| 3 Tier ladder (Standard / Enhanced / Premium) | Smooth upgrade path. Matches competitors | Adds one more SKU to catalogue | **Recommended** |

### **Risks & Mitigations**

| Risk  | Description | Mitigation Strategies |
| :---- | :---- | :---- |
| Internal misalignment on entitlements | Lack of clarity across Support, Sales, and TAM/AM teams may lead to inconsistent messaging of care plans. | Create a cross-functional enablement pack and work with Michele to run mandatory training for frontline teams. Publish a merchant-facing matrix with entitlements. |
| Merchant confusion or reputational damage | Merchants may perceive the introduction of “support plans” as a downgrade or gating of previously available channels. | Proactively communicate value, emphasising enhancements. Actively grandfather existing support expectations where appropriate i.e. Tier 4  Discuss phasing and approach |
| SKU & catalogue friction | Sales and commercial teams may struggle with quoting or explaining additional SKUs. | Include plans in all standard commercial proposals with pricing logic. (Can be automated through CPQ)  |
| Inequitable merchant experience in Standard tier | Long-tail merchants may feel deprioritised or underserved compared to Enterprise/Premium. | True today \- continue investment in self-service and chatbot resolution capabilities. Monitor CSAT & NPS across all segmentations. |

### **Merchant examples \- research with AM/TAMs**

| Level | Examples | Operational tooling | Max Operational Dashboard logins a week | Support needs |
| :---- | :---- | :---- | :---- | :---- |
| Premium | Netflix Uber Spotify eBay Klarna Temu Shein Ant Financial | Mature Self built, cutting edge tools for their operational teams to diagnose orders and payments. Using our APIs/Webhooks.  | 5-10 \- biggest TPV 50-100 \- bottom end (e.g. Careem) | Infrequently contact Care for major issues, so expect rapid, quality service Big churn on teams, so use central support systems Self serve not expected |
| Enterprise | Delivery Hero eToro Plus500 | Low/Medium maturity Some tools for teams, but need our Dashboard to fill the gaps. Use our APIs/Webhooks.  | 50-200 | Ask repeat simple support issues, usually about several payments Willing to self serve in most cases |
| Standard | Small Tier 2 & Tier3-5  | Low maturity Usually no tools, so rely on our Dashboard. API usage is low.  | 25-50 | Ask range of simple support issues, across payment lifecycle and Dashboard usage/functionality Tries to self serve first |

**Research findings — Premium tier (January 2026 AM interviews):**

The Premium tier channel design is validated by direct AM research. Key findings per merchant:

| Merchant | Primary support channel | Dashboard? | Primary query types | Channel gap |
| :---- | :---- | :---- | :---- | :---- |
| eBay | Multiple dedicated Slack channels (AR, dev, P0/P1). Almost never raises Zendesk tickets. | Minimal — deliberate policy | AR drops by BIN/market, invoice reconciliation, proof of settlement, 3DS/compliance | Phone for P1; AM CC on tickets; AI agent responses that avoid directing to dashboard |
| Temu | Proprietary in-house IM (not WeChat — no external integration possible). Support email for reconciliation/disputes. | None — internal compliance block | Webhook status mismatches, AR monitoring, out-of-hours coverage (APAC, after 8pm) | After-hours coverage; accurate webhook data would eliminate most contacts |
| Shein | Email/tickets | None — compliance block on holding cardholder data | APM status/disputes (~60%), Pay to Card RFI (~40%) | APM dispute API; clearing process visibility; no self-serve path |
| Ant Financial | DingTalk/InTalk (proprietary in-house IM, 150-person chat group; no external integration) | Partial — known bug in webhook subscription view | Payment confirmation, webhook misconfiguration, Payback sub-merchant auth failures | IM channel is untrackable; webhook dashboard bug needs fixing |

**Implications for the Premium tier channel design:**
- Dashboard-based self-serve is not viable for this segment — these merchants deliberately bypass it. The Premium channel set (dedicated email, Slack/IM, phone) is correctly specified.
- The Slack/IM channel in Premium is confirmed as the primary contact channel for APAC accounts (Temu, Ant). Without it, support effort is invisible and absorbed by AMs.
- Phone for P1 is validated: eBay's AM reports merchants asking for phone support since she joined; current line is not fit for purpose.
- AM/TAM auto-CC on tickets is confirmed as important for Premium accounts — eBay specifically asked for the ability to interject if an AI response is incorrect.


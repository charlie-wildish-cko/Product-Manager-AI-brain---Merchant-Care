# B2C Fintech Support — Competitive Analysis (2026)

> Deep research report into customer support strategies at consumer fintech and BNPL competitors, in the context of Checkout.com's planned 2027 consumer wallet launch.  
> Sourced: February 2026. Refresh annually.
>
> **Competitors covered**: Monzo, Revolut, Starling, Zilch, Klarna  
> **Relevance**: B2C consumer wallet support model — AI-first architecture, rewards friction, tiered service, and agentic commerce. Reference when planning the 2027 consumer support model.  
> **Companion document**: `competitive-support-audit-2026.md` covers B2B PSP competitors (Stripe, Adyen, Worldpay).

**Last Updated**: February 2026  
**Owner**: Charlie Wildish


# **Strategic Framework for Next-Generation Customer Support: A Competitive Deep-Dive for the 2027 Checkout.com Consumer Wallet Launch**

The global financial technology landscape is currently navigating a pivotal transition from reactive service models toward a paradigm of agentic autonomy and proactive engagement. As Checkout.com prepares for the 2027 launch of its consumer wallet, the definition of "best-in-class" customer support has evolved beyond traditional metrics of availability and speed. In the contemporary market, support is no longer a cost center to be minimized but a core product feature that directly influences user retention, brand trust, and the successful adoption of complex financial instruments such as rewards-based wallets and Buy Now, Pay Later (BNPL) services. This analysis provides an exhaustive evaluation of the operational architectures, technological infrastructures, and strategic methodologies employed by the industry’s most prominent challengers—Monzo, Revolut, Starling, Zilch, and Klarna—to establish a roadmap for Checkout.com’s entry into the market.

## **The Evolution of Operational Architecture: Transitioning from Reactive to Agentic Support**

The foundational architecture of customer support in fintech has shifted from a "Human-in-the-loop" (HITL) necessity to a sophisticated orchestration of "Agentic AI" and specialized human expertise. Organizations that have successfully scaled to millions of users in the 2025-2026 period have done so by re-engineering their support hierarchies to prioritize "Containment Rate" and "First Contact Resolution" (FCR) through automated systems that possess the authority to execute actions, rather than merely providing information.1

### **Comparative Hierarchy: Monzo’s Contextual Chat vs. Revolut’s Automated Flow**

The operational philosophies of Monzo and Revolut represent the two primary schools of thought in digital-first support. Monzo has historically anchored its support model in a community-centric, human-led approach, characterized by its bespoke "Monzo Chat" software built from the ground up to handle the unique nuances of its UK banking customers.2 The Monzo hierarchy is designed as a graduated triage system. When a user encounters friction, they are first directed to a comprehensive "Help Screen" powered by a deep-linked knowledge base. If the user’s query is not resolved through these articles, they enter a chat flow where the system attempts to categorize the urgency of the issue.3 This architecture prioritizes "Human Context"; agents are equipped with the full transaction history and behavioral data of the user, allowing for a resolution that feels personalized even when response times vary during peak periods from 4 minutes to over 2 hours.5

In stark contrast, Revolut has pursued an aggressive "Automation-First" architecture designed for global scalability. By 2026, Revolut’s support model has transitioned into a sophisticated "Multilingual Conversational Agent" front line.6 Utilizing technologies such as ElevenLabs, Revolut has deployed voice-capable AI agents that handle live calls, detect and switch between 31 languages in real time, and connect securely to proprietary systems to resolve account-specific issues without human intervention.6 This model has enabled Revolut to achieve an 8x reduction in time to resolution while maintaining a call success rate of 99.7%.6 For Revolut, the human agent is reserved for "High-Stakes" or "Emotional" interactions, while the "Agentic AI" handles the vast majority of routine inquiries, such as card freezes, transaction disputes, and cross-border payment tracking.4

| Support Characteristic | Monzo Operational Model | Revolut Operational Model | Industry Benchmark (2026) |
| :---- | :---- | :---- | :---- |
| **Primary Channel** | In-App Chat (Bespoke) | Automated AI Voice & Chat | Omnichannel (Chat-First) 8 |
| **Initial Triage** | Article-led self-service | AI Agent-led dialogue | AI-driven intent detection 10 |
| **Human Escalation** | Specialist-led, context-rich | Priority-based (Paid tiers) | Confidence-based routing 1 |
| **Resolution Focus** | Empathy and accuracy | Speed and scalability | "Agentic" action execution 1 |
| **Response Time (SLA)** | Variable (minutes to hours) | Near-instant for AI; Tiered for humans | \< 2 minutes (Instant expectation) 1 |

### **Service Excellence Benchmarks for the 2025-2026 Period**

The benchmarks for success in 2026 reflect a market where consumers have zero tolerance for friction. First Contact Resolution (FCR) remains the gold standard, with the industry average sitting between 70% and 75%.11 However, top-performing fintechs are now targeting rates above 80% by utilizing "Agentic AI" that can process refunds and update account parameters autonomously.1

| Metric | Industry Average (2025/26) | High Performer Target (2027) | Implication for Checkout.com |
| :---- | :---- | :---- | :---- |
| **First Contact Resolution (FCR)** | 70% \- 75% | \>85% | Essential for reducing repeat ticket volume 11 |
| **Average Handle Time (AHT)** | 6.0 Minutes | 4.5 Minutes | Driven by LLM-powered agent copilots 9 |
| **Customer Satisfaction (CSAT)** | 75% \- 85% | \>90% | High correlation with self-service success 13 |
| **Net Promoter Score (NPS)** | \+32 | \+50 | Differentiator in a crowded wallet market 9 |
| **Self-Service Adoption** | 67% | \>80% | Users prefer immediate, bot-led resolution 9 |
| **Average Speed to Answer (ASA)** | 20 \- 40 Seconds | \<15 Seconds | Critical for "urgent" financial inquiries 12 |

## **Support as a Feature: The Integration of Proactive UX and Embedded Support**

One of the most profound shifts in fintech support is the move from reactive problem-solving to "Support as a Feature." In this model, the product UX is designed to anticipate failure points and provide "Proactive Support" before the user is required to initiate contact.8 This is particularly critical for a rewards-centric wallet where transaction friction can lead to immediate churn.

### **Proactive Support Examples in BNPL and Digital Banking**

Klarna and Zilch have established the industry standard for proactive support within the credit and BNPL sectors. Klarna’s "Dispute Management" workflow is a primary example of support being embedded directly into the transaction lifecycle. When a customer raises a dispute (e.g., goods not received or faulty items), Klarna’s AI-powered system automatically places the invoice on hold, ensuring the customer is not required to make payments while the investigation is active.15 This proactive "pause" eliminates the anxiety of accruing late fees during a merchant dispute, a feature that has been cited as a major driver of Klarna’s high trust ratings.16 Furthermore, Klarna utilizes "Sentiment Analysis" to assess user feedback in real-time, allowing the system to refine its tone and resolution pathways based on the emotional state of the user.16

Zilch has taken a similarly advanced approach by integrating 100% "AI Quality Assurance" across its customer interactions.17 This allows Zilch to identify "vulnerable customers" proactively—those who may be showing signs of financial distress—and adjust their credit limits or offer alternative repayment schedules before a default occurs. Zilch’s "Direct-to-Consumer" (D2C) model focuses on affordability, using its own proprietary scoring system to ensure that credit is only extended when the AI predicts a high probability of successful repayment without customer hardship.17

Starling Bank provides a compelling example of proactive support through its "Spending Intelligence" tool, built using Google Gemini and Vertex AI.19 By giving customers the ability to use natural language to query their own spending habits (e.g., "How much did I spend on groceries this month compared to last?"), Starling has effectively reduced customer service referrals by 50%.19 This feature transforms what would traditionally be a support query regarding balance discrepancies into an engaging, self-service product feature.

### **Embedded Support Workflows for Rewards Friction**

For a rewards-based wallet, "Missing Cashback" is a primary friction point. Monzo manages this by embedding a "Report Missing Cashback" workflow directly within the transaction view.21 Instead of forcing a user to navigate to a generic help menu, the user can click on the specific transaction and trigger a dedicated dispute flow. Most users report that these missing rewards are paid out within 4 to 5 days once the in-app dispute is logged.22 The success of this model lies in the "Single-View" architecture, where the support request is inextricably linked to the transaction metadata, reducing the need for the user to provide extensive documentation.

## **The Technical Infrastructure: The "Support-Tech" Stack of 2027**

The decision to build proprietary support engines versus leveraging third-party AI platforms is a defining strategic choice for 2027\. The research indicates a split between "Full-Stack Control" (Monzo, Starling) and "AI-Wrapper Agility" (Revolut, Zilch).

### **Proprietary NLP vs. Third-Party Wrappers**

Monzo and Starling have both prioritized proprietary technology to ensure total control over the user experience and data privacy. Monzo's "Monzo Chat" was built because generic solutions like Intercom were deemed insufficiently tailored to the complexities of banking regulations and internal workflows.2 Similarly, Starling Bank connects directly to payment schemes (FPS, Bacs) through its own proprietary software, removing any third-party "gateways" that could introduce latency or downtime.23 This "in-house" philosophy extends to their support stack, allowing them to iterate on features such as "Scam Intelligence" and "Spending Intelligence" in weeks rather than months.19

Conversely, firms like Revolut and Zilch are increasingly utilizing specialized "Agentic AI" platforms that offer a higher "Time-to-Value" (TTV). Platforms like Fini, Ada, and Intercom Fin are now capable of 70% to 85% autonomous resolution by connecting directly to a company’s internal APIs and executing multi-step workflows.1 These platforms utilize the latest LLMs (GPT-4, Claude 3, Llama 3\) to provide a level of conversational nuance that was previously impossible for rule-based chatbots.24

| Platform | Best For | Key "Agentic" Feature | Est. Resolution Rate |
| :---- | :---- | :---- | :---- |
| **Fini** | Highest Automation | \< 48-hour deployment; multi-platform sync | 70% \- 85% 1 |
| **Intercom Fin** | Sales-Support Hybrid | "Stringing together" multiple data connectors | 55% \- 65% 1 |
| **Zendesk AI** | Omnichannel Suites | "Agent Copilot" for macro suggestions | 45% \- 55% 1 |
| **Ada CX** | Complex Workflows | Strong e-commerce/transactional focus | 50% \- 60% 1 |
| **Proprietary** | Regulated Stability | Deep integration with core ledger/rails | 60% \- 80% (Custom) 2 |

### **The Role of "Support Agent Copilots" in AHT Reduction**

Even when a human agent is required, the "Tech Stack" of 2026-2027 relies heavily on LLM-powered "Copilots" to reduce Average Handle Time (AHT). These tools, such as Zendesk’s "Agent Copilot" or Intercom’s "Copilot," act as a personal assistant to the human agent, summarizing long ticket histories, suggesting response tones (professional, empathetic, or simple), and even drafting entire replies based on internal knowledge bases.10 This eliminates the "Hunting Time"—the time an agent spends searching for information across various systems—which research shows has dropped by 54% in organizations that have adopted CRM-native AI routing.7

## **Rewards & Loyalty Support: Managing Friction and Tiered Expectations**

A rewards-focused wallet introduces a specific set of support challenges, primarily related to "Cashback Anxiety" and "Tiered Entitlements." As Checkout.com enters this space, it must account for how users react when their perceived financial incentives are not instantly realized.

### **Handling Reward-Related Friction**

Friction in rewards programs typically stems from three areas: expired offers, merchant processing delays, and technical "tracking" failures. User data from Monzo and Revolut forums suggests that users are highly sensitive to "Missing Cashback" because it feels like a direct loss of expected income.21 Top-tier fintechs manage this through:

1. **Automatic Verification**: Using real-time transaction data to confirm eligibility the moment a card is swiped.  
2. **Visual Status Tracking**: Moving rewards from "Pending" to "Available" with clear timelines in the UI, reducing the urge for the user to "ask where it is."  
3. **Dedicated Dispute Channels**: Creating a non-urgent support path specifically for rewards, keeping the high-priority chat lines clear for critical banking issues.

### **Support Tier Differentiation**

Monetizing support through premium tiers (e.g., Revolut Metal, Ultra) has become a vital revenue stream. This creates a "Support Tier" hierarchy where the value of the customer determines the level of human access.

| Tier | Primary Support Channel | Support SLA | Key Benefit |
| :---- | :---- | :---- | :---- |
| **Standard** | AI Agent / Self-Service | 2 \- 4 Hours | 24/7 Availability via Bot 3 |
| **Premium / Metal** | Priority In-App Chat (Human) | \< 5 Minutes | Dedicated human expert 3 |
| **Ultra / VIP** | Priority Voice \+ Direct Callback | Instant | Account Management / Personal Assistant 3 |

For Checkout.com, a similar differentiation will be necessary. "Standard" users should experience a highly competent, "Agentic AI" that can solve 80% of issues, while "Premium" wallet holders should have the security of knowing a human expert is a "single tap" away for complex merchant disputes or missing high-value rewards.

## **2027 Future-Proofing: Navigating the Era of Agentic Commerce**

By the time Checkout.com launches in 2027, the role of the "Customer" will have expanded to include "AI Agents" acting on behalf of humans. Checkout.com’s own research indicates that by 2026, 47% of consumers will have used an AI agent for shopping, and millennials are increasingly comfortable with AI agents spending money on their behalf (72%).28 This "Agentic Commerce" shift requires a fundamental rethinking of support and liability.

### **Handling AI Agent Purchase Errors**

The most complex support challenge for a 2027 wallet will be resolving issues where an AI agent—not the human—made a purchase and an error occurred. The support model must be equipped to handle several "Agentic Failure" scenarios:

1. **Misinterpreted Instructions**: The user asked for "cheap flights," and the AI booked a flight with a 24-hour layover that the human finds unacceptable.30  
2. **Unauthorized Autonomous Activity**: A "rogue agent" makes a purchase that falls outside of pre-set parameters or budget limits.31  
3. **Technical Protocol Failures**: The agent initiates a transaction using the "Universal Commerce Protocol" (UCP) or "Agentic Commerce Protocol" (ACP), but the merchant’s system fails to deliver the goods.33

To manage this, the 2027 support model must distinguish between **Unauthorized Transactions** (fraud, where the bank is liable) and **Unintended Transactions** (agent error, where the human may be liable depending on the terms of service).30 The wallet must maintain a "Cryptographic Proof of Consent"—a signed log of what the user authorized the agent to do—to act as the "source of truth" during disputes.30

## **Competitive SWOT Analysis**

### **Monzo: The Community Specialist**

* **Strengths**: Best-in-class UI/UX that simplifies complex banking; deep brand trust in the UK market; bespoke proprietary support tech allows for high flexibility.2  
* **Weaknesses**: Scalability challenges with human-led support; response times can be inconsistent during peak periods 5; lack of international multi-currency depth compared to Revolut.4  
* **Opportunities**: Expansion into "Social Banking" features where support is community-assisted; leveraging AI to provide "Financial Health" coaching.  
* **Threats**: Aggressive automation from global players could make Monzo's "human-first" approach feel slow to digital natives.

### **Revolut: The Global Super-App**

* **Strengths**: Massive global footprint and multi-currency dominance 4; world-leading AI voice agents (ElevenLabs) reducing resolution times 6; aggressive product diversification (crypto, stocks, insurance).37  
* **Weaknesses**: Mixed reputation for customer empathy; "bot-heavy" support can feel dismissive 38; frequent reports of unexpected account freezes during verification.38  
* **Opportunities**: Leading the "Agentic Commerce" space by building personal shopping assistants 27; capturing the "B2B CX" market with real-time spending analytics.42  
* **Threats**: Regulatory scrutiny in multiple jurisdictions regarding AI decision-making and e-money license protections.3

### **Starling Bank: The Reliability Powerhouse**

* **Strengths**: Full UK banking license with 24/7 human support across phone, chat, and email 3; proprietary in-house payment rails ensure high uptime 23; successful Google AI partnership for consumer spending insights.19  
* **Weaknesses**: "Conservative" app design may not resonate with Gen Z as strongly as neobank competitors 35; limited international presence outside of BaaS offerings.20  
* **Opportunities**: Selling its "Engine" (BaaS) platform to traditional banks, effectively becoming the support infrastructure for other firms.20  
* **Threats**: Rising competition from traditional banks (e.g., Chase UK, Lloyds) that are copying neobank features.36

### **Klarna: The BNPL Experience Leader**

* **Strengths**: "Invoice Hold" feature creates unique consumer protection; AI-powered dispute resolution is a model for frictionless finance 15; massive merchant network provides deep data on consumer behavior.16  
* **Weaknesses**: Regulatory uncertainty surrounding BNPL consumer protections 43; support is heavily dependent on merchant cooperation.  
* **Opportunities**: Transitioning into a full "Shopping Hub" where the AI agent manages the entire journey from discovery to return.  
* **Threats**: New entrants (including Apple and banks) offering integrated BNPL features with lower friction.45

### **Zilch: The Affordability Innovator**

* **Strengths**: D2C model ownership allows for deep customer context 18; "Affordability" focus builds long-term trust; early adoption of "Agentic Commerce" solutions.17  
* **Weaknesses**: High cost of customer acquisition in a crowded market; brand identity is heavily tied to "Zero Credit" which may limit expansion into other wallet services.  
* **Opportunities**: Leveraging its advertising-subsidized model to offer rewards that are better than traditional bank cashback.  
* **Threats**: Rising interest rates making the "Interest-Free" model more expensive to maintain.

## **The Customer Support Maturity Model**

A successful support strategy for 2027 must be mapped against a "Support Maturity Model" to identify where Checkout.com can leapfrog incumbents.

| Level | Maturity Stage | Operational Characteristics | Technological Foundation |
| :---- | :---- | :---- | :---- |
| **1** | **Static / Reactive** | Support is a cost center; generic messaging to all users; reactive ticketing.46 | Basic CRM, Shared Email Inbox. |
| **2** | **Automated** | Introduction of basic chatbots for FAQ; siloed data sources; first attempt at segmentation.47 | Rule-based Bots, Web Tags. |
| **3** | **Personalized** | Scheduled and triggered segments based on user lifecycle; human agents have some customer context.46 | Knowledge Bases, Intercom/Zendesk. |
| **4** | **Adv. Omnichannel** | Unified data platform (CDP); 360° view of customer; proactive alerts for common friction points.8 | AI Copilots, Integrated Helpdesk Suite. |
| **5** | **Agentic Champion** | AI agents resolve 80% of issues autonomously; predictive resolution; agent-to-agent negotiation.1 | Agentic Protocols (UCP/ACP), LLM-native Engines. |

## **Recommended "Day 1" Support Roadmap for Checkout.com**

To ensure a successful launch in 2027, the consumer wallet support model must be "Agentic-First" from the design phase.

### **Phase 1: Pre-Launch (Foundation)**

* **Tech Stack Selection**: Partner with an "Agentic AI" platform (e.g., Fini or Ada) to build the autonomous core. Ensure the system is "Action-Oriented," capable of querying the Checkout.com ledger and performing refunds or adjustments without human intervention.1  
* **Data Readiness**: Implement "Structured Data Excellence" (Schema.org) across the wallet’s merchant feeds to ensure future AI agents can parse and recommend rewards accurately.33  
* **Policy Development**: Draft "Agentic Liability" terms that clearly define who is responsible when an AI shopping agent makes an unintended purchase.30

### **Phase 2: Day 1 (Execution)**

* **Launch "Support as a Feature"**: Embed the support interface directly into the transaction and rewards screens. Implement "Auto-Pause" for disputed merchant transactions, mirroring Klarna’s success.15  
* **Priority Tiering**: Enable 24/7 "Priority Chat" for premium wallet holders, utilizing LLM-summarized ticket context to ensure human agents have zero "hunting time".7  
* **Real-Time Cashback Verification**: Ensure that any missing reward triggers an immediate automated query to the merchant API, with a "Status Tracker" visible to the user.22

### **Phase 3: Post-Launch (Optimization & Future-Proofing)**

* **AI Quality Assurance**: Use AI to review 100% of support interactions, identifying patterns of friction and "Vulnerability Signals" in the user base.17  
* **Agentic Commerce Integration**: Launch support for UCP and ACP protocols, allowing the Checkout.com wallet to act as the "Trust Layer" for a user's personal shopping agents.33  
* **Proactive Spending Insights**: Integrate natural language querying of transaction data (similar to Starling’s "Spending Intelligence") to turn "where did my money go?" inquiries into an engaging product feature.19

The 2027 wallet market will be defined not by who has the most features, but by who provides the most "Frictionless Trust." By building an operational architecture that prioritizes agentic resolution and proactive intervention, Checkout.com can establish a superior customer experience that serves as the primary differentiator in the next generation of global finance.

#### **Works cited**

1. The 10 Best AI Customer Support Tools in 2025: Complete ... \- Fini AI, accessed February 25, 2026, [https://www.usefini.com/blog/the-10-best-ai-customer-support-tools-in-2025-complete-comparison-guide](https://www.usefini.com/blog/the-10-best-ai-customer-support-tools-in-2025-complete-comparison-guide)  
2. Introducing Monzo Chat, accessed February 25, 2026, [https://monzo.com/blog/2018/11/02/monzo-chat](https://monzo.com/blog/2018/11/02/monzo-chat)  
3. Starling vs Monzo vs Revolut Review: Which Digital Bank is Best for You? \- Plouta, accessed February 25, 2026, [https://www.plouta.com/financial-wellness-hub/starling-vs-monzo-vs-revolut-which-bank-is-best-for-you](https://www.plouta.com/financial-wellness-hub/starling-vs-monzo-vs-revolut-which-bank-is-best-for-you)  
4. Revolut vs Monzo: Which Is Better for Businesses in 2026? | Statrys, accessed February 25, 2026, [https://statrys.com/reviews/revolut-vs-monzo-business-account](https://statrys.com/reviews/revolut-vs-monzo-business-account)  
5. Monzo 1 \- Revolut 0: please AVOID REVOLUT AT ALL COSTS, accessed February 25, 2026, [https://community.monzo.com/t/monzo-1-revolut-0-please-avoid-revolut-at-all-costs/33160](https://community.monzo.com/t/monzo-1-revolut-0-please-avoid-revolut-at-all-costs/33160)  
6. Revolut selects ElevenLabs Agents to bolster customer support, accessed February 25, 2026, [https://elevenlabs.io/blog/revolut](https://elevenlabs.io/blog/revolut)  
7. Contact Center Benchmarks 2026 | Annual Natterbox Study, accessed February 25, 2026, [https://natterbox.com/contact-center-benchmarks-2026-report/](https://natterbox.com/contact-center-benchmarks-2026-report/)  
8. CX trends for 2026 \- Capita, accessed February 25, 2026, [https://www.capita.com/news-and-insights/insights/2026/cx-trends-for-2026](https://www.capita.com/news-and-insights/insights/2026/cx-trends-for-2026)  
9. 14 Call Center Industry Trends & Stats For 2026 & Beyond \- Alpharun, accessed February 25, 2026, [https://www.alpharun.com/blog/call-center-industry-trends](https://www.alpharun.com/blog/call-center-industry-trends)  
10. 2025 recap: What's new in Zendesk – Zendesk help, accessed February 25, 2026, [https://support.zendesk.com/hc/en-us/articles/10140103140122-2025-recap-What-s-new-in-Zendesk](https://support.zendesk.com/hc/en-us/articles/10140103140122-2025-recap-What-s-new-in-Zendesk)  
11. Important Metrics Every Call Center Should Track in 2026, accessed February 25, 2026, [https://callcenterstudio.com/blog/important-metrics-every-call-center-should-track-in-2026/](https://callcenterstudio.com/blog/important-metrics-every-call-center-should-track-in-2026/)  
12. Top 15 Call Center KPI Benchmarks for 2026 \- BlueTweak, accessed February 25, 2026, [https://bluetweak.com/blog/call-center-kpi-benchmarks/](https://bluetweak.com/blog/call-center-kpi-benchmarks/)  
13. 7 Most Important Customer Service Metrics to Track in 2026 \- BlueTweak, accessed February 25, 2026, [https://bluetweak.com/blog/customer-support-metrics/](https://bluetweak.com/blog/customer-support-metrics/)  
14. The Truth About AI Customer Support: What Actually Works in 2025 \- Helply, accessed February 25, 2026, [https://helply.com/blog/the-truth-about-ai-customer-support](https://helply.com/blog/the-truth-about-ai-customer-support)  
15. Klarna through klarna \- Klarna Docs, accessed February 25, 2026, [https://docs.klarna.com/acquirer/klarna/after-payments/disputes/disputes-management-v1-v2/dispute-management-overview/](https://docs.klarna.com/acquirer/klarna/after-payments/disputes/disputes-management-v1-v2/dispute-management-overview/)  
16. AI-Powered Dispute Resolution: Klarna's Approach to Customer Complaints \- Twig, accessed February 25, 2026, [https://www.twig.so/blog/ai-powered-dispute-resolution-klarna](https://www.twig.so/blog/ai-powered-dispute-resolution-klarna)  
17. Zilch Holdings Limited 2025 Annual Report, accessed February 25, 2026, [https://www.zilch.com/pdf/financial-statements/zilch-technology-limited-annual-report-and-financial-statements-FY-2025.pdf](https://www.zilch.com/pdf/financial-statements/zilch-technology-limited-annual-report-and-financial-statements-FY-2025.pdf)  
18. Zilch: A Buy Now Pay Later Model With a Difference \- Netguru, accessed February 25, 2026, [https://www.netguru.com/blog/zilch-a-different-bnpl-model](https://www.netguru.com/blog/zilch-a-different-bnpl-model)  
19. Starling case study \- Google Cloud, accessed February 25, 2026, [https://cloud.google.com/customers/starling](https://cloud.google.com/customers/starling)  
20. Starling launches pioneering AI banking tool in mission to help UK be 'Good with money', accessed February 25, 2026, [https://www.starlingbank.com/news/starling-launches-pioneering-ai-banking-tool/](https://www.starlingbank.com/news/starling-launches-pioneering-ai-banking-tool/)  
21. Cashback doesn't work? : r/monzo \- Reddit, accessed February 25, 2026, [https://www.reddit.com/r/monzo/comments/18je3oo/cashback\_doesnt\_work/](https://www.reddit.com/r/monzo/comments/18je3oo/cashback_doesnt_work/)  
22. Cashback not received : r/monzo \- Reddit, accessed February 25, 2026, [https://www.reddit.com/r/monzo/comments/1eyfe98/cashback\_not\_received/](https://www.reddit.com/r/monzo/comments/1eyfe98/cashback_not_received/)  
23. How Starling provides you with access to real-time payments, accessed February 25, 2026, [https://www.starlingbank.com/banking-services/how-starling-provides-you-with-access-to-real-time-payments/](https://www.starlingbank.com/banking-services/how-starling-provides-you-with-access-to-real-time-payments/)  
24. Top 8 AI Agents for Customer Service in 2025 \- Ema, accessed February 25, 2026, [https://www.ema.co/additional-blogs/addition-blogs/top-ai-agents-customer-service](https://www.ema.co/additional-blogs/addition-blogs/top-ai-agents-customer-service)  
25. How Zendesk AI Agents and Intercom Fin Stack Up in Real Customer Support Scenarios, accessed February 25, 2026, [https://swifteq.com/post/zendesk-ai-agents-vs-intercom-fin](https://swifteq.com/post/zendesk-ai-agents-vs-intercom-fin)  
26. The \#1 AI Agent and next-gen Helpdesk for customer service \- Intercom, accessed February 25, 2026, [https://www.intercom.com/suite](https://www.intercom.com/suite)  
27. Revolut building AI agents for sales, customer service and more | Sifted, accessed February 25, 2026, [https://sifted.eu/articles/revolut-ai-agents-voice-calls](https://sifted.eu/articles/revolut-ai-agents-voice-calls)  
28. Checkout.com research signals first AI Christmas, with consumers set to embrace agentic commerce in 2026, accessed February 25, 2026, [https://www.checkout.com/newsroom/checkout-com-research-signals-first-ai-christmas-with-consumers-set-to-embrace-agentic-commerce-in-2026](https://www.checkout.com/newsroom/checkout-com-research-signals-first-ai-christmas-with-consumers-set-to-embrace-agentic-commerce-in-2026)  
29. The $200 checkout: What consumers expect from agentic AI, accessed February 25, 2026, [https://www.checkout.com/blog/what-consumers-expect-agentic-commerce](https://www.checkout.com/blog/what-consumers-expect-agentic-commerce)  
30. Five questions in-house counsel should ask about agentic ..., accessed February 25, 2026, [https://www.torys.com/fr-ca/our-latest-thinking/publications/2026/02/five-questions-in-house-counsel-should-ask-about-agentic-commerce](https://www.torys.com/fr-ca/our-latest-thinking/publications/2026/02/five-questions-in-house-counsel-should-ask-about-agentic-commerce)  
31. Agentic AI: rogue agents, real liability \- King & Wood Mallesons, accessed February 25, 2026, [https://www.kwm.com/au/en/insights/latest-thinking/agentic-ai-rogue-agents-real-liability.html](https://www.kwm.com/au/en/insights/latest-thinking/agentic-ai-rogue-agents-real-liability.html)  
32. When AI Clicks “Pay”: The Emerging Compliance Risks of Agentic Commerce \- NASCUS, accessed February 25, 2026, [https://www.nascus.org/2026/02/12/when-ai-clicks-pay-the-emerging-compliance-risks-of-agentic-commerce/](https://www.nascus.org/2026/02/12/when-ai-clicks-pay-the-emerging-compliance-risks-of-agentic-commerce/)  
33. What Is Agentic Commerce? 45% of Shoppers Use AI (2026 ..., accessed February 25, 2026, [https://www.ekamoira.com/blog/what-is-agentic-commerce-the-complete-2026-guide-to-ai-shopping-agents](https://www.ekamoira.com/blog/what-is-agentic-commerce-the-complete-2026-guide-to-ai-shopping-agents)  
34. Agentic AI Payments: Navigating Consumer Protection, Innovation, and Regulatory Frameworks, accessed February 25, 2026, [https://consumerbankers.com/wp-content/uploads/2026/01/CBA-Agentic-Symposium-White-Paper-2026-01v2.pdf](https://consumerbankers.com/wp-content/uploads/2026/01/CBA-Agentic-Symposium-White-Paper-2026-01v2.pdf)  
35. Starling vs Monzo vs Revolut Business Account: 2026 Comparison, accessed February 25, 2026, [https://anna.money/blog/guides/starling-vs-monzo-vs-revolut-business-account/](https://anna.money/blog/guides/starling-vs-monzo-vs-revolut-business-account/)  
36. Does Monzo have any truly unique features anymore?, accessed February 25, 2026, [https://community.monzo.com/t/does-monzo-have-any-truly-unique-features-anymore/186782](https://community.monzo.com/t/does-monzo-have-any-truly-unique-features-anymore/186782)  
37. Top 10: Digital Banks | FinTech Magazine, accessed February 25, 2026, [https://fintechmagazine.com/top10/top-10-digital-banks-2025](https://fintechmagazine.com/top10/top-10-digital-banks-2025)  
38. Monzo VS Revolut \- Looking for real world experience of using both. : r/UKPersonalFinance, accessed February 25, 2026, [https://www.reddit.com/r/UKPersonalFinance/comments/1ee5oiq/monzo\_vs\_revolut\_looking\_for\_real\_world/](https://www.reddit.com/r/UKPersonalFinance/comments/1ee5oiq/monzo_vs_revolut_looking_for_real_world/)  
39. \[US\] I can't stand Revolut's business support. It's an AI bot and then if you request a person, its an LLM again but this time it assures you that it's a real person meanwhile instantly spitting out paragraphs and making very obvious LLM mistakes. \- Reddit, accessed February 25, 2026, [https://www.reddit.com/r/Revolut/comments/1qxddnj/us\_i\_cant\_stand\_revoluts\_business\_support\_its\_an/](https://www.reddit.com/r/Revolut/comments/1qxddnj/us_i_cant_stand_revoluts_business_support_its_an/)  
40. Does Revolut Suffer from Chatbot-Based Customer Service?, accessed February 25, 2026, [https://www.financemagnates.com/trending/does-revolut-suffer-from-chatbot-based-customer-service/](https://www.financemagnates.com/trending/does-revolut-suffer-from-chatbot-based-customer-service/)  
41. Revolut vs Monzo (2026): Feature, Fees & Best Choice Explained \- Xflow, accessed February 25, 2026, [https://www.xflowpay.com/blog/revolut-vs-monzo](https://www.xflowpay.com/blog/revolut-vs-monzo)  
42. European B2B CX Benchmark Report 2025-2026: Regional Strategies for Competitive Advantage, accessed February 25, 2026, [https://ecxo.org/european-b2b-cx-benchmark-report-2025-2026/](https://ecxo.org/european-b2b-cx-benchmark-report-2025-2026/)  
43. What Rights Do Buy Now, Pay Later Purchasers Have? \- NCLC, accessed February 25, 2026, [https://www.nclc.org/resources/what-rights-do-buy-now-pay-later-purchasers-have/](https://www.nclc.org/resources/what-rights-do-buy-now-pay-later-purchasers-have/)  
44. Borrow Now, Pay Later? Attorney General Bonta Has Questions | State of California, accessed February 25, 2026, [https://oag.ca.gov/news/press-releases/borrow-now-pay-later-attorney-general-bonta-has-questions](https://oag.ca.gov/news/press-releases/borrow-now-pay-later-attorney-general-bonta-has-questions)  
45. Payments industry trends for 2025 \- Checkout.com, accessed February 25, 2026, [https://www.checkout.com/blog/payment-industry-trends](https://www.checkout.com/blog/payment-industry-trends)  
46. Customer Experience Maturity for Financial Institutions, accessed February 25, 2026, [https://static.thefinancialbrand.com/uploads/2021/09/Customer-Experience-Maturity-for-Financial-Institutions.pdf](https://static.thefinancialbrand.com/uploads/2021/09/Customer-Experience-Maturity-for-Financial-Institutions.pdf)  
47. How to Use a Customer Experience Maturity Model \- Acquia, accessed February 25, 2026, [https://www.acquia.com/blog/cx-maturity-model](https://www.acquia.com/blog/cx-maturity-model)  
48. The Five-Stage Road to Customer Experience Maturity: Where is Your Organization | NiCE, accessed February 25, 2026, [https://www.nice.com/blog/the-five-stage-road-to-customer-experience-maturity-where-is-your-organization](https://www.nice.com/blog/the-five-stage-road-to-customer-experience-maturity-where-is-your-organization)  
49. White paper: The Reconciliation Maturity Model \- FinTech Futures, accessed February 25, 2026, [https://www.fintechfutures.com/fintech/white-paper-the-reconciliation-maturity-model](https://www.fintechfutures.com/fintech/white-paper-the-reconciliation-maturity-model)
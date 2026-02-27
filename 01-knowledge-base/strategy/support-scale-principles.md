# Support Scale Principles (to 2030)

> Principles for scaling from 10,000s of contacts to millions. Support as a product, not just a cost centre.
>
> **Competitive context (B2B)**: See `01-knowledge-base/strategy/competitive-support-audit-2026.md` for how Stripe, Adyen, Worldpay, Razorpay, and Braintree approach support — and the four gaps Checkout.com needs to close.  
> **Competitive context (B2C)**: See `01-knowledge-base/strategy/B2C Fintech Support Competitive Analysis.md` for consumer fintech benchmarks (Monzo, Revolut, Starling, Zilch, Klarna) relevant to the 2027 wallet launch. Key implications for these principles are captured in the B2C Launch Considerations section of `care-product-model.md`.

> **P&L context**: Care/Support sits on the Loss (L) side of the Product department P&L. The strategic goal is for unit costs (cost per contact, cost per $1M processed) to decrease over time as AI deflection, contact reduction, and agent tooling compound. The flywheel below is the mechanism for achieving that. Full reporting framework: `01-knowledge-base/metrics/kpi-definitions.md` → P&L Reporting section.


## The Flywheel

These principles form a reinforcing loop: each stage accelerates the next.

```
         ┌─────────────────────────────────────────────────────────┐
         │                                                         │
         ▼                                                         │
   ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
   │  HANDLE  │ ──► │  LEARN   │ ──► │   FIX    │ ──► │  SCALE   │
   └──────────┘     └──────────┘     └──────────┘     └──────────┘
   AI first,        Automated        Product gaps     Fewer contacts,
   humans premium   insights from    + content        better data,
                    support data     improvements    more capacity
         │                                                         │
         └─────────────────────────────────────────────────────────┘
```

| Stage | Principles | What happens |
|-------|------------|--------------|
| **Handle** | 2, 4, 5 | AI Agent takes volume; humans focus on complex/VIP. Good data (MCPs, low latency) powers both. |
| **Learn** | 3 | Support data → root causes, prevention tactics → automated output for Product/Content (even PRs). |
| **Fix** | 1, 6 | Product fixes gaps; content improves. Knowledge embedded in Checkout DNA. |
| **Scale** | — | Fewer contacts, higher quality remaining volume, more capacity for the next cycle. |

The flywheel spins faster as data quality improves and insights flow into fixes.


## Relation to Care Product Model

The [Care Product Model](care-product-model.md) defines the operational domains. The Support Scale Principles are the strategic lens for scaling them to 2030. Mapping:

| Support Scale Flywheel | Care Product Model Domain | How principles apply |
|------------------------|---------------------------|------------------------|
| **Handle** | **Input** + **Orchestration** + **Agent Experience** | Fin AI Agent as majority channel (2). Humans for complex/VIP only (4). Routing to right owners; AI solving 80% (2, 4). Agent tools powered by good data (5). |
| **Learn** | **Insight and prevention** | Automated outputs for Product/Engineering on top contact drivers (3). Support data → root causes, prevention tactics; even PRs (3). |
| **Fix** | **Fuel** + outcomes of **Insight and prevention** | Product gaps fixed to prevent contacts (1). Content improved via automated insights (6). MCPs, APIs for data access (5). Content covers 90% of taxonomy (6). |
| *Enabler across all* | **Fuel** (Data, Knowledge Base) | Accurate, complete, low latency data (5). Knowledge embedded in Checkout DNA (6). MCPs/AI Agents to query any source. |

**Governance** (Care domain 6) sits outside the flywheel — operational excellence (SLA, QA, CSAT) underpins the loop but doesn’t drive the scale trajectory.


## 1. Solve for the Root Cause, not just the Ticket

Fix product gaps to prevent contacts in the first place. Every ticket is a signal; the goal is to eliminate the need for the ticket.


## 2. Automation / AI First

- Most contact volume passes through the customer AI Agent first
- For human agents: use a **human-in-the-loop** approach for Agent approval of internal AI Agent–based actions


## 3. Automated Insights and Feedback Loops

Use support data to surface:
- Contact root causes
- Prevention tactics

Publish in an automated output for Content or Product teams to review — including as far as code base Pull Requests.


## 4. Keep Human Agents as Premium Support

Human agents only solve:
- Complex issues
- VIP customers


## 5. Accurate, Complete, Low Latency Data

Access to accurate data and content must be easy and with minimal delay for the customer waiting on it — for both AI Agent and Agent tools.

*Example: MCPs (Model Context Protocol).*


## 6. Well Managed Content

- Use automated insights for faster content improvement
- Embed Knowledge into Checkout people DNA


**Horizon**: Scale to 2030

> **Note on banking transition**: The flywheel assumptions above are based on the current payments-only B2B model. The 2027 B2C consumer wallet launches as a banking product (Consumer Duty, complaint handling, phone channel obligations apply from day one). B2B banking products follow from 2028 — at that point, the taxonomy, Fuel, and Agent Experience components of the flywheel will need to be replanned for the new query types and regulatory obligations banking introduces. See `care-product-model.md` → B2B Banking Evolution and B2C Launch Considerations.

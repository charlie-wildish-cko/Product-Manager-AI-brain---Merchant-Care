# Welcome to Merchant Care

**For**: [NAME]
**From**: Charlie Wildish (PM, Merchant Care)
**Last updated**: [DATE]

This is a simple guide to what our team does and what we're working on. It assumes no prior knowledge of Checkout.com.

---

## What Checkout.com does

Checkout.com is a payment service provider (a PSP). Businesses ("merchants") use us to accept and process payments from their customers — a checkout on a website, a card machine, a subscription charge. We move the money and handle everything that has to happen safely and correctly around that: fraud checks, currency conversion, sending merchants their money, handling refunds and disputes.

Merchants manage their account through our **Dashboard** — a web app where they see their transactions, balances, and settings.

## What our team does

We're **Merchant Care** — the team responsible for support. When something goes wrong or a merchant has a question (a payment failed, money hasn't arrived, "how do I set this up"), they contact us. Our job is to answer them, well and cheaply.

We call each of those questions a **contact**. Every contact comes in through one of a few **channels**: email, a form in the Dashboard, or an AI chat assistant called **Fin**. If Fin can't resolve it, it becomes a **ticket** in a system called **Zendesk**, and a human agent handles it.

We measure ourselves on two things:
- **Contact rate** — how many contacts we get per 1 million transactions. Lower is better — it means merchants are running into fewer problems.
- **Cost per contact** — how much it costs us to resolve one contact. A human agent costs about $40; Fin costs about $0.90. Getting more contacts resolved by Fin, without hurting quality, is one of our biggest levers.

We also watch **CSAT** (customer satisfaction) as a guardrail — we're not allowed to let quality drop while we cut cost or volume.

## Who we support

We split merchants into two groups, based on one simple question: **do they have a named Account Manager at Checkout.com?**

- **White Glove (commercial name: Enterprise)** — has an Account Manager. These merchants get more channels and a faster, more direct path to a human when our AI can't help. This group includes large direct merchants, Platforms, and Card Issuing customers.
- **Not White Glove (commercial name: SMB)** — no Account Manager. Support here is AI-first by design, with a human only as a tightly controlled fallback.

Within White Glove, **Platforms** are a distinct case: a Platform is a company that embeds Checkout.com's payments inside its own product and resells it to its own merchants (think: a booking software company that also handles payments for its restaurant customers). We support the Platform directly; the Platform supports its own merchants.

- **Consumers** are a separate customer type altogether — not a business, an individual person. Checkout.com already runs a small consumer product called **Remember Me** (card saving). A bigger consumer launch is coming: **Ray**, a digital wallet + card, launches internally by the end of 2026 and externally (beta) in Q1 2027. This is a new, separate type of support we're building for.

## Getting a new product ready for support ("Stage 0")

Before any of the above can happen, a product needs to actually be *ready* for us to support it — someone has decided what kind of questions it will generate, who answers them, and what information they'll need. We call this **Stage 0**, and it happens once per product, before its first customer contact ever arrives (not something we figure out live, contact by contact, once launched).

If Stage 0 is skipped, we find out what a product needs the hard way — from real merchants hitting real problems with no answer ready. Getting Stage 0 done properly, before launch, is one of the more foundational (if less visible) pieces of what we do.

## How a support contact flows through our team

Once a product has been through Stage 0 above, think of what happens to each contact as six steps, in order:

1. **Input** — the contact arrives and we work out what it's about.
2. **Orchestration** — we decide who or what should handle it (Fin, or a specific team of human agents).
3. **Fuel** — whoever's handling it needs the right information (data, help articles) to actually solve the problem.
4. **Agent Experience** — if a human agent is handling it, this is the tools and screens they use to do it well and quickly.
5. **Insight & Prevention** — we look at what people are contacting us about and try to fix the underlying product problem, so it stops happening.
6. **Governance** — making sure all of the above happens to a consistent standard (response times, quality checks).

Every project we work on fits into one or more of these steps.

## What we're working on right now (2026)

A few of the headline efforts this year:

- **Getting Fin to resolve more contacts** — giving it the right information and permissions so more questions get answered instantly, without a human agent.
- **Reflex** — a tool that analyses support tickets to spot the most common problems, so we can tell Product teams what to fix.
- **Merchant Education Hub** — tutorials and articles on our support site so merchants can solve simple things themselves.
- **Ticket visibility in Dashboard** — letting merchants see and track their own support requests in one place, rather than only by email.
- **Getting ready for Ray** — our first real consumer product. Internal launch is end of 2026; external beta is Q1 2027. We need Stage 0 done properly for this: a support model, a taxonomy of what consumers will contact us about, and content, before real customers arrive.

(For the full, detailed roadmap, see `2026 deliverables.md` — you won't need this on day one.)

## The team

| Role | What they do |
|---|---|
| **PM (Charlie)** | Sets the roadmap and priorities for Merchant Care |
| **Engineers** | Build the systems and integrations that power support |
| **Care Operations** | Run day-to-day support — the agents actually talking to merchants |
| **Operational Excellence** | Own quality, process, and service standards |
| **Zendesk Admins** | Configure and maintain our ticketing system |
| **Knowledge Manager** | Owns the help articles and content Fin and agents rely on |

If you're ever unsure who owns something, ask — this is a small team and everyone's approachable.

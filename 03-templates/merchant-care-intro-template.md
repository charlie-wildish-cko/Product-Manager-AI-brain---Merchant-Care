# Merchant Care: Introduction for [Audience]

**From**: Charlie Wildish, Care Product  
**Date**: [Date]  
**For**: [Name / Team / Role]

---

> **How to use this template**
>
> This template has two parts:
>
> **Part 1: The Core** is pre-written. Copy it verbatim into every briefing you produce. It does not change per audience.
>
> **Part 2: The Audience Lens** is where you tailor the document. Replace the `[bracketed guidance]` with content specific to the person or team you're writing for. The four sub-section headers are fixed; only the content inside them changes.
>
> **Reference example**: See `04-active-work/merchant-care-b2c-briefing.md` for a completed instance tailored to a Consumer PM.
>
> Delete this instruction block before sharing.

---

## Part 1: The Core

> Copy this section verbatim. Do not tailor it per audience.

### What Merchant Care is

Care Product is the PM function for Checkout.com's support infrastructure. The domain covers everything that happens from the moment a merchant contacts support to the moment that contact drives a product improvement or is deflected entirely. We build the systems, tooling, and processes that let Checkout.com handle support at scale: the AI Agent, the Zendesk configuration, the agent toolkit, the routing logic, the insights product. We do not run day-to-day support operations — that's Care Operations. We build what operations runs on.

### The flywheel

We think about the domain as a six-stage flywheel. Each stage enables the next, and the loop compounds over time:

| Stage | What it covers |
|---|---|
| **Input** | The channels merchants use to contact us, and the query taxonomy that classifies what they're asking |
| **Orchestration** | Triage logic and routing rules: where the contact goes and who is best placed to answer it |
| **Fuel** | The data and knowledge content that powers both AI and human agents to resolve issues accurately |
| **Agent Experience** | The tooling human agents use inside Zendesk to investigate and resolve tickets |
| **Insight & Prevention** | Translating support contact data into product and content fixes that prevent future contacts |
| **Governance** | SLA management, QA, and operational standards: the baseline below which we don't go |

The flywheel spins faster as data quality improves and insights flow into fixes. The goal is not just to handle contacts well — it's to reduce the need for contacts in the first place.

### The numbers that matter

- **Fin AI Agent involvement is 9.2% today** across all contact channels. Target is 80% by end of 2026. The gap is structural: Fin only runs on Dashboard chat today; email (45% of contacts) and the webform (22%) have no AI deployed.
- **Three merchant support tiers**: Standard, Enterprise, and Premium, assigned based on Salesforce CRM data (revenue, growth potential, strategic value). Each tier has defined SLAs, channel entitlements, and (for Enterprise/Premium) proactive support features.
- **~23,500 B2B merchant contacts in the last 6 months** (full-year equivalent ~47,000). Premium and Enterprise each generate ~30% of volume despite being a small fraction of the merchant base.

### The strategy

The operating principle is: Handle → Learn → Fix → Scale.

- **Handle**: AI Agent takes the volume first. Humans focus on complex issues and the highest-value merchants. Good data powers both.
- **Learn**: Support contact data flows automatically into root cause analysis and outputs for Product and Content teams. We're building Reflex, an AI-powered insights product, to do this at scale.
- **Fix**: Product and content teams act on those outputs to close the gaps that generated the contacts. Every ticket prevented saves cost and improves merchant experience.
- **Scale**: Fewer contacts, higher quality remaining volume, more capacity for the next cycle.

The target by 2030 is AI handling 80%+ of contacts, with human agents reserved for complex issues and the highest-value merchants.

---

## Part 2: The Audience Lens

> Replace everything in [square brackets] with content for your specific audience.
> The four sub-section headers below are fixed. Only the content changes.
> Aim for 1-2 paragraphs or 3-5 bullets per sub-section — concise and specific, not comprehensive.

### Why this matters to you

[One paragraph. State the specific reason this person's work connects to Care. Start with the direct link, not background context. Avoid generic framing like "support is important for every team" — say exactly why it's relevant to this role or domain.]

### How our domains intersect

[2-4 specific touchpoints. Concrete, not abstract. For each one, name what we build that they use, what they build that we depend on, or where we need each other's input. Use bullets. No vague overlap statements.]

### What we're working on in 2026 that's relevant to you

[2-3 bullets from the 2026 roadmap. Only include items that directly affect this audience's work. Name the initiative, say what it changes for them, and note any dependency or ask on their side if there is one.]

### How to work with us

[Practical guidance: how to raise something with Care Product, what to expect, who to contact. Keep it short — 3-5 bullets or a short paragraph. If there are specific processes or forms they should use, name them.]

---

**Owner**: Charlie Wildish  
**Last Updated**: [Date]

---

## Audience Lens Examples

> Reference examples for the three priority audiences. Use these as a starting point and update as the roadmap evolves.

---

### Example: Product PM

**Why this matters to you**

Every feature your team ships generates support contacts. Whether those contacts are preventable, deflectable by AI, or require a human agent is shaped by product design decisions made long before launch. Care Product is the team that translates contact patterns back into product gaps — and we're building the tooling to do that automatically via Reflex. The earlier you involve us in feature design, the less support debt you create.

**How our domains intersect**

- **Insight & Prevention loop**: Reflex surfaces the top contact drivers per product area. Your backlog should be consuming this output — contact reduction is a product metric, not just a support ops metric.
- **Query taxonomy**: When your product introduces a new flow or feature, we need to classify the support queries it generates. New query types that aren't in the taxonomy can't be routed, reported on, or resolved by AI. Flag new features to us before launch.
- **Support model design**: If your feature affects a specific merchant tier or segment, the support model for that segment determines what channel, SLA, and agent knowledge is available. We need to align before you commit to a user-facing support experience.
- **Fin AI Agent content**: Any new flow we want Fin to resolve needs content and data access. If your feature is launching and you want Fin to handle queries about it, we need to be in scope during your build, not after it.

**What we're working on in 2026 that's relevant to you**

- **Reflex (AI insights product)**: By Q3, we're targeting automated weekly contact driver reports per product area. Your team will start receiving structured output on the top contact reasons your product is generating, with suggested fixes. This is an input to your roadmap, not an optional read.
- **Merchant success plans rollout**: Standard / Enterprise / Premium tier model is live in 2026. If your feature has a tier-differentiated experience, the support SLAs and channels those merchants receive are now defined. We can tell you what to expect per segment.
- **Fin involvement rate push to 80%**: We're deploying Fin on email and webform in H1. If your product generates queries Fin can't answer today (content gaps, data access gaps), now is the time to surface them.

**How to work with us**

- **New feature with support implications**: Ping Charlie Wildish before design is locked. Even a 30-minute conversation at the scoping stage prevents rework.
- **Contact driver you want fixed**: Raise it with us directly or wait for the Reflex output. If it's urgent, share the Zendesk query data and we can triage.
- **Taxonomy question** (what to call a new query type, how to classify it): Come to us — we own the taxonomy and the routing rules that depend on it.

---

### Example: Software Engineer

**Why this matters to you**

Care Product sits at the intersection of Zendesk (configured, not coded) and the engineering-built tools that power agent and AI workflows. The Agent Toolkit (User Profile and Payment Tool) is built by Engineering to our specification. Fin AI Agent's effectiveness depends on data APIs that Engineering owns. When we scope a new support capability, we need to know what's feasible, what data is available, and what the right integration point is. You're a key input to our delivery, and we're a key consumer of what you build.

**How our domains intersect**

- **Agent Toolkit**: Engineering builds the User Profile and Payment Tool that agents use inside Zendesk. We specify what the tools need to surface; Engineering builds and maintains the underlying data connections. Changes to our support model (new entities, new merchant types) often require changes to these tools.
- **Fin AI Agent data access**: Fin's ability to resolve queries autonomously depends on accessing merchant and payment data via APIs. The authentication model, data latency, and API design are Engineering dependencies. The current 9.2% involvement rate is partly a data access constraint — unlocking Fin on email requires resolving this.
- **Zendesk integrations**: Zendesk is configured by Zendesk Admins, not Engineering. But integrations between Zendesk and external systems (e.g. ticket creation from internal tools, org data sync, session-based identity for the Dashboard webform) are Engineering work.
- **Dashboard webform**: The webform inside the merchant Dashboard is a Dashboard Engineering surface. Migrating it to Fin chat (Lever 3 in our Fin involvement plan) is a Dashboard Engineering dependency — it's in scope for H1 2026.

**What we're working on in 2026 that's relevant to you**

- **Fin on email (Q2)**: Deploying Fin on the merchant email channel requires an auth classifier and data policy sign-off. The data access component (merchant and payment data for Fin) is an Engineering dependency. We'll need scoping input on what's buildable within the Q2 window.
- **Agent Toolkit — Blue EMI support (Q2)**: The User Profile and Payment Tool need to support Blue EMI client IDs and data sources alongside existing Checkout data. This is an Engineering build. Scope not yet assessed — active dependency.
- **Dashboard webform migration to Fin (Q2-Q3)**: Fin needs to replicate the structured intake and routing that the webform currently provides. Dashboard Engineering owns the surface. We'll need cross-team scoping in H1.

**How to work with us**

- **Engineering spec or scoping request**: Come to Charlie Wildish for requirements before estimating. We own the "what"; you own the "how".
- **Data access question** (can Fin or the Agent Toolkit access X): Raise with us first — we can tell you what we need and why, then scope jointly with the data team.
- **Zendesk configuration vs. Engineering work**: If you're unsure whether something is a Zendesk config task or an engineering build, ask. The distinction matters for routing work to the right team.

---

### Example: Care Agent

**Why this matters to you**

Care Product builds the tools you use every day: the Zendesk configuration, the Agent Toolkit (User Profile and Payment Tool), the Fin AI Agent that handles queries before they reach you, and the routing logic that determines what lands in your queue. We don't run your queue — Care Operations does — but we own the infrastructure underneath it. When a tool doesn't work the way you need it to, or when a routing rule sends the wrong things your way, that's our problem to fix. Your feedback is one of the most important inputs we have.

**How our domains intersect**

- **Agent Toolkit**: User Profile (merchant identity and context) and Payment Tool (payment metadata lookup) are built to make your triage faster and more accurate. If they're missing data, pulling the wrong information, or slow, that's a Care Product issue.
- **Fin AI Agent**: Fin handles queries before they reach you. What Fin can and can't resolve affects your queue mix. If Fin is escalating things it should be able to resolve, or resolving things incorrectly, that feedback shapes our content and configuration improvements.
- **Routing rules and views**: How tickets are assigned to queues, which tickets surface in your views, and how priority is set are all Zendesk configuration decisions we own. If something is landing in the wrong place, tell us.
- **SLAs**: The SLA policies attached to your tickets are set by Care Product in Zendesk, based on the merchant tier model. If SLA clocks are starting at the wrong time or the wrong tier is being applied, that's a configuration issue to raise with us.

**What we're working on in 2026 that's relevant to you**

- **Fin involvement rate push to 80%**: We're deploying Fin across email and webform. This means Fin will intercept more contacts before they become tickets. Your queue should get smaller, and what remains should be more complex or higher-priority. The query mix in your queue will change — more Enterprise/Premium, more technical issues.
- **Merchant success plans**: The Standard / Enterprise / Premium tier model is being formalised this year. Your queue views and SLA clocks will be updated to reflect this. Standard merchants are not entitled to email — if Standard email contacts are landing in your queue after the policy change, flag it.
- **Retool internal form (AM/TAM submissions)**: AMs and TAMs are moving off email to a structured Retool form for raising tickets. Tickets from this channel will be better structured and auto-mapped to the right merchant org, reducing the Dispatch work you do for AM-submitted contacts.

**How to work with us**

- **Tool gap or bug** (Agent Toolkit, Fin, routing): Raise via your team lead or directly with Charlie Wildish. Include a specific ticket example where possible — it's the fastest way to diagnose.
- **Routing issue** (wrong queue, wrong SLA, wrong merchant attached): Flag to Zendesk Admins for immediate fix, and copy Care Product so we can identify whether it's a recurring config issue.
- **Fin feedback** (wrong resolution, missing content, bad escalation): The Content team reviews Fin conversations regularly, but surfacing specific examples directly speeds up fixes.
- **Feature request or improvement idea**: Bring it to your team lead for the quarterly feedback cycle. Care Product reviews this input when planning roadmap items.

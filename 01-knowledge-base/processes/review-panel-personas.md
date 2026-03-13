# Review Panel Personas (Customer Support Angle)

> Ten reviewer personas for multi-perspective document review. Use when you want to “inhabit” a reviewer, brief someone else, or simulate a panel (e.g. with AI). Primary use: [Document Review Panel](../../02-workflows/document-review-panel.md); also reusable for stakeholder comms, exec prep, and any doc that benefits from these perspectives.

**Convention (Document Review Panel)**: When running the panel, assume any data in the document (metrics, numbers, baselines, tables, splits) originated from or was validated by the Product Data Scientist. The Data Scientist persona therefore reviews “their” output for clarity, correct definitions, and interpretability.

These personas are written with customer support impact in mind so review naturally surfaces support readiness, agent experience, and customer-facing risk.

---

## When to Run Each Persona

**Always run — every PRD:**
- **Oliver** (Support Agent) — primary support lens
- **Casey** (Operations) — ops readiness and capacity
- **Imran** (Data Scientist) — metrics and measurability
- **Preethy** (Content) — content dependencies
- **Taylor** (VP of Product) — exec alignment

**Conditional:**
| Persona | Run when... |
|---|---|
| Sam — PM | PRD touches another product team's area or has cross-team scope |
| Fraser — Engineering | PRD has technical depth (APIs, integrations, error handling) or is post-scoping |
| Georgios — Designer | PRD includes any UI component (agent tools, merchant dashboard, webforms) |
| Morgan — CPO | Big-bet, roadmap-level, or exec-facing doc |
| Ajana — Zendesk Admin | PRD touches ticketing, routing, taxonomy, macros, or Zendesk config |

---

### Persona 1: Sam — Product Manager

**Role**: Senior Product Manager, owns a product area that generates steady support volume.

**Background**: 5 years in product; has had to explain messy launches to support and leadership. Thinks in problems, metrics, and “what does support need to say?”

**Goals**: Ship things that are understandable and defensible; avoid “why did we ship this?” support spikes.

**Customer support angle**: Wants the doc to give support a clear story: what problem we’re solving, for whom, and what’s in/out of scope so agents can set expectations and deflect confidently.

**In documents they look for**: Problem statement support can reuse; success metrics that might show up in tickets or feedback; explicit scope so support knows what we’re not doing; priorities that match what we tell customers.

**Typical questions**:
- “Can a support agent explain *why* we’re doing this in one sentence?”
- “What will we tell customers who ask for the thing we’re explicitly not building?”
- “Do the success metrics line up with what support will see (e.g. fewer tickets, fewer escalations)?”

---

### Persona 2: Fraser — Software Engineering / Tech Lead

**Role**: Software engineering tech lead for a service that support often troubleshoots (payments, onboarding, integrations).

**Background**: Software engineer by trade; used to get DMs from support when something broke. Now insists on runbooks and clear error behaviour so support isn’t guessing.

**Goals**: Ship reliably, document failure modes, and make sure support has the technical context they need.

**Customer support angle**: Cares what agents will see in the UI, in logs, and in error messages; wants runbooks and escalation paths to exist before launch so support isn’t the canary.

**In documents they look for**: Clear acceptance criteria that imply testable behaviour; called-out error states and edge cases; any new APIs or flows that need agent-facing docs or runbooks; dependencies that could cause support-visible outages.

**Typical questions**:
- “What error messages or states will the customer (and agent) see when X fails?”
- “Do we have a runbook or escalation path for the new flow before we ship?”
- “What do we need to add to the support knowledge base or internal docs so agents can troubleshoot?”

---

### Persona 3: Georgios — Product Designer

**Role**: Product designer; owns UX and UI for product surfaces that support and customers use (dashboard, webforms, agent tools).

**Background**: Has seen launches where "it works" technically but confuses users or creates support volume; cares about flows, states, and consistency. Works with PM and Eng so that requirements are buildable and usable.

**Goals**: User flows and UI that are clear, consistent, and accessible; edge states and copy considered before build; design system and content ownership explicit so nothing falls through the cracks.

**Customer support angle**: Evaluates whether the product experience will create avoidable questions or friction (merchant-facing) and whether agent-facing UI is usable so support can do their job. Surfaces UX risks that could drive tickets or escalations.

**In documents they look for**: Clear user flows and journeys; specification of key screens and states (happy path, errors, empty, loading); accessibility and design-system alignment; ownership of in-UI copy and microcopy; consideration of different devices or contexts.

**Typical questions**:
- "Who is the primary user, and what does 'good' look like for them in the UI?"
- "Are we designing for all key states (errors, empty, loading) or only the happy path?"
- "Does this fit our design system, or do we need new components or patterns?"
- "Who owns copy and microcopy, and is it in the timeline?"
- "Where could users get stuck or confused in this flow, and could that create support volume?"

---

### Persona 4: Oliver — Operations Agent (Frontline Support)

**Role**: Support agent (or team lead) who handles live chats, tickets, and escalations daily.

**Background**: Knows what confuses customers and what questions always come up after a release; has seen good and bad rollouts from the frontline.

**Goals**: Not be blindsided by changes; have playbooks and answers so they can help customers and avoid unnecessary escalations.

**Customer support angle**: The primary “support lens”—everything is evaluated by “can I use this doc to do my job and answer a merchant?”

**In documents they look for**: Plain-language description of the change; new or changed customer-facing behaviour; likely questions and suggested answers; handoffs and escalation paths; impact on tools (Zendesk, macros, internal KB) and workflows.

**Typical questions**:
- “What’s the one sentence I’d use to explain this to a merchant?”
- “What will customers get wrong or ask about most? Do we have answers?”
- “Who do I escalate to if something goes wrong, and what do I need to include?”
- “Does this change how I use our tools or which playbook I follow?”

---

### Persona 5: Morgan — Chief of Product

**Role**: CPO; owns product strategy and how product work ties to company goals.

**Background**: Has had to answer for support meltdowns and “why did we ship without support readiness?” in exec meetings.

**Goals**: Strategy and narrative that stand up to “why this, why now?” and that don’t ignore support and operational reality.

**Customer support angle**: Wants to see that we’re not shipping something that will blow up support volume or trust; strategy should acknowledge support readiness and customer impact.

**In documents they look for**: Clear “so what” and business impact; fit with strategy; explicit trade-offs; risks and unknowns (including support impact) so decisions are informed; a crisp ask or recommendation.

**Typical questions**:
- “If we ship this, what’s the one thing we want everyone (including support) to remember?”
- “Are we being honest about support impact and what we don’t know?”
- “What would we cut or delay if we had to protect support capacity or customer trust?”

---

### Persona 6: Casey — Chief of Operations

**Role**: COO or Head of Operations; owns support capacity, training, and run-the-business cost.

**Background**: Signs off on headcount, training, and process changes; has been in the room when launches happened without ops readiness.

**Goals**: No surprise demand spikes; training and playbooks in place before go-live; docs that ops leadership can use to plan and communicate.

**Customer support angle**: Evaluates every doc for “what does support need to have in place before this goes live?” and “what could make our support cost or risk worse?”

**In documents they look for**: Implications for capacity, headcount, or process; support and compliance impact; scalability and “what could get worse at scale”; run-the-business cost (not just build); clarity so ops can plan and tell teams what “good” looks like.

**Typical questions**:
- “What’s the impact on support when this goes live—volume, new ticket types, new skills?”
- “What do we need to have in place before launch (training, playbooks, tools, comms)?”
- “Is the timeline realistic for ops and support readiness, not just engineering?”
- “Would our teams know what ‘good’ looks like and how to handle the first week?”

---

### Persona 7: Imran — Product Data Scientist

**Role**: Product data scientist embedded in the team; owns metrics, instrumentation, and reporting for the product area.

**Background**: Works with PM and Eng to define metrics, build dashboards, and interpret trends; has seen launches where “success” wasn’t measurable or baselines were missing. When used in the Document Review Panel, any data cited in the document (metrics, numbers, tables, splits) is assumed to have originated from or been validated by the data scientist—so this persona is reviewing “their” output for clarity and correctness.

**Goals**: Every target and success metric should be measurable with available (or planned) data; avoid “we’ll know it when we see it” and ambiguous denominators.

**Customer support angle**: Cares that support-related metrics (involvement rate, resolution rate, volume by channel) are well-defined, instrumentable, and reportable so we can track support impact and prove or disprove the strategy.

**In documents they look for**: Clear metric definitions (numerator, denominator, dimensions); data sources and instrumentation plan; baselines and targets that are comparable; anything that could break or confound measurement (e.g. channel reclassification, definition drift); feasibility of reporting (cadence, ownership, tooling).

**Typical questions**:
- “Can we actually measure this with the data we have (or will have)? What’s the source of truth?”
- “Is the denominator and numerator defined so we’re comparing apples to apples over time?”
- “What’s the baseline today, and how will we know when we’ve hit the target?”
- “What could change in the data or definitions that would make this metric misleading or uninterpretable?”
- “Who owns the report, how often do we refresh it, and can support/ops use it to make decisions?”

---

### Persona 8: Ajana — Zendesk Administrator

**Role**: Zendesk admin (or support systems owner); owns configuration, tagging, routing, reporting, and agent tooling in Zendesk.

**Background**: Configures triggers, views, macros, and fields; maintains taxonomy and reporting so support can route, track, and measure. Has been caught short when launches added new ticket types or behaviours without time to add tags, views, or KB articles.

**Goals**: No last-minute config scrambles; taxonomy and reporting that match how we actually work and measure; agents can find and route tickets so the right data shows up in Explore and leadership reports.

**Customer support angle**: Cares that new or changed behaviour is reflected in Zendesk so we can route correctly, report on it, and give agents the right macros/views. Evaluates docs for "what do I need to configure before go-live and how does this fit our tagging/reporting strategy?"

**In documents they look for**: New or changed ticket types, tags, or fields needed; impact on triggers, routing, or views; reporting requirements (what we need to measure in Zendesk); KB or macro updates; timeline for config work before launch; consistency with existing taxonomy and tagging conventions.

**Typical questions**:
- "Do we need new tags, fields, or ticket types for this? What's the taxonomy?"
- "What triggers, routing, or views need to change before launch?"
- "How will we report on this in Zendesk (Explore, dashboards)—and is that in scope for this launch?"
- "What internal KB articles or macros do agents need, and who's writing them?"
- "When do config changes need to be done so we're ready when this ships?"
- "Does this align with our existing tagging and reporting strategy, or do we need to adjust?"

---

### Persona 9: Preethy — Content Strategist

**Role**: Content strategist (or content team lead); owns the content roadmap that feeds the support site, docs, and Fin's knowledge base. Drives proactive guides, reactive content improvements, and the agent/customer feedback loop.

**Background**: Prioritises content using ticket and Fin conversation data; has seen initiatives succeed or fail depending on whether the right content existed for deflection and resolution. Works with PM, Ops, and Zendesk to align content with product launches and support readiness.

**Goals**: No launches that assume content exists when it doesn't; clear ownership and dependencies so content can be planned; alignment with the content strategy (guides, Fin resolution rate, coverage) so we hit resolution and deflection targets.

**Customer support angle**: Cares that docs, help articles, and Fin answers exist and are accurate so merchants can self-serve and Fin can resolve. Evaluates every doc for "what content does this depend on or create, and who owns it?"

**In documents they look for**: Content dependencies (what must be written or updated for this to work); impact on resolution rate, deflection, or self-serve; fit with content strategy themes (e.g. Transactions, Balances & Settlements); who owns content for this initiative; timeline for content work before or alongside launch; any new flows or behaviours that need help articles or Fin KB updates.

**Typical questions**:
- "What content does this depend on—and does it exist yet? Who owns it?"
- "Does this create or change anything that needs a help article, guide, or Fin KB update?"
- "How does this align with our content strategy (e.g. guide programme, resolution rate target)?"
- "What do we need to write or update so agents, Fin, and customers have the right answers?"
- "Is the timeline realistic for content work, not just engineering and ops?"
- "If we're tracking resolution or deflection, is content explicitly in the dependency list?"

---

### Persona 10: Taylor — VP of Product

**Role**: VP of Product; manages the Senior PM and sits between them and the Chief of Product. Owns the product org or a major product area and represents it upward.

**Background**: Translates team-level work into exec narrative and vice versa; has had to defend or clarify PM work in leadership forums. Knows when a doc will land with the CPO and when it will raise questions they can't answer.

**Goals**: Team's work is clearly articulated and defensible; no surprises for the CPO; priorities and trade-offs visible so they can represent the team upward and allocate wisely. Support and ops impact acknowledged so they can speak to it in leadership conversations.

**Customer support angle**: Wants to know support/ops impact is considered so they can represent it honestly to the CPO and avoid "why didn't we think about support?" in the room.

**In documents they look for**: Clear "so what" that works in a 2-minute read; alignment between problem, goals, scope, and recommendation; risks and trade-offs surfaced; ask or recommendation explicit so they can advocate for it; support/ops impact called out so they can represent it.

**Typical questions**:
- "Would my CPO understand this and the ask in 2 minutes?"
- "Are we being honest about trade-offs and support impact so I can represent it accurately?"
- "What would we cut or delay if we had to—and have we said it?"
- "Is the recommendation clear enough that I can advocate for it with leadership?"
- "What's the one thing we want everyone to remember, and is it stated?"

---

**Owner**: Charlie Wildish  
**Last Updated**: Feb 2026

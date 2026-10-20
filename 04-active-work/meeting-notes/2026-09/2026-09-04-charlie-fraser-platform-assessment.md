# Charlie / Fraser - hiring, Zendesk exit, Fin data design

**Date:** 2026-09-04
**Attendees:** Charlie Wildish, Fraser Bryant
**Drive source:** 1pmJLMWHC-JcTiZDMf23cmkNUPLEwRV45e6CzYzs4-sI

## Context

1:1 covering AJ's resignation and how to backfill it, the Zendesk platform assessment Charlie is about to write, and how deterministic payment data should reach Fin.

## Key Points

**Personnel**
- AJ has resigned, moving to Spain. He asked to transfer to the Barcelona office; rejected as impractical on tenure criteria plus reluctance to grow a remote sub-team while the London office shrinks. He has accepted a Barcelona role titled "Zendesk architect", which he was reportedly unhappy about having been glad to move away from Zendesk. Notice period ~2 months.
- The team is down to one Zendesk admin (Anna). Fraser's stated concern: Anna could go on maternity leave at any point, leaving the team exposed.
- Kunal Patel is also leaving. Charlie's read: a chance for freshness in the entity team, where Kunal was weary.
- Graduates Holly and Frankie are onboarding. Fraser ran a session on reactive / deflective / proactive support concepts mapped to solutions, then had them categorise each.

**Hiring strategy**
- Agreed: replace AJ but reposition the role. It goes to market as "support systems administrator" or "operations admin", with Zendesk deliberately kept off the job description. Two reasons: avoid Zendesk inferring the transition from job postings, and the platform is changing anyway.
- Target profile: junior to mid, a couple of years' experience, enthusiastic and coachable. They will be learning a new system regardless, so prior platform depth matters less.
- Charlie's reasoning: there will always be an administrator-versus-engineer role. Engineers will not do queue and routing watching or stakeholder response work, and would leave. Anna is the model: multi-skilled, handles the team, understands requirements, and implements.
- Market concern: this talent is largely remote-only and hard to place in an office role. One prior candidate reacted very badly to the office requirement. Salesforce admin is the analogue, but Salesforce specialists are a closed cottage industry who will not cross-train.
- Ops boundary: Oliver is positioning Joel as the owner of requirements on the ops side. Charlie and Fraser agreed product and tech should not absorb requirements ownership: if the non-customer team defines requirements, the relationship breaks. Karolina reportedly shares the view that product and tech implement what the operations business wants.

**Zendesk exit and Plain migration**
- Charlie's priority for the following week: write the platform assessment document. He has a skeleton. It must land the narrative for change, the selection criteria, and why those criteria matter.
- Primary argument identified: scale. Specifically the number of configuration items expected to need maintenance over time, and how hard that is manually today versus code-deployed config at scale. That is the argument for a platform supporting agentic workflows.
- Customer experience is framed as a consequence, not the headline: "we can ensure a good customer experience at scale", not "this is a CX change".
- Charlie wants Anna or AJ to pull configuration metrics and expected maintenance volumes at scale as evidence.
- Fraser has been working with Jirro and Anish on the vision and has started slicing the work, but has no estimates yet.
- Hélder suggests extending the Zendesk contract by 6 months to buy time. Not decided. Charlie needs procurement advice on tactics, including when to formally notify Zendesk, since notification will generate noise and degrade whatever support Zendesk provides.
- Tension aired: a 6-month extension would be enormously useful for gotchas, but immediately signals to Zendesk that something is up and drags spend across the year boundary, which Charlie wants to avoid. Fraser's position: start in Q4 and push.
- If asked whether the work can be done before the Zendesk contract expires, Fraser's position is to say yes. Plan to split scope by consumer support and merchant support.

**Looker MCP and Fin data**
- Charlie's concern: if using Looker MCP for the customer-facing Fin integration requires hand-building deterministic Looker queries or prompts for every query type, it is unworkable. Hundreds of prompts, unmaintainable.
- Second objection: you do not know the payment data until you have looked it up, so it would need two lookups (fetch, inspect, query again to interpret).
- Fraser's understanding from Shri: the MCP generates the queries and you only execute them. Fraser to confirm.
- Both rejected the earlier idea, attributed to Adrian who has now left, of replying to a merchant with a dashboard link to view the payment themselves. That loses the resolution: it depends on the user clicking, and they will escalate anyway.
- Agreed target design: pass controlled, deterministic data into Fin via attributes. Precedent exists from the agent-side data return. Keep it simple and Zendesk-agnostic apart from checking user verification. Reflect the verification outcome as a field or flag, and Fin executes a data connector or procedure when the attribute equals a given value. The same pattern works in Plain. Charlie to tell infra what data types will be shared and get sign-off. Exposure is minimal because Care controls exactly what is passed.

**Other**
- Entity data quality: a thread reported messy entity data affecting platform merchant onboarding, surfacing wrong details to the merchant and causing risk checks to behave oddly, due to something implemented that should not have been.
- The winning hackathon project was built on Braavos (crypto commerce, buying products inside the wallet), two weeks before the Braavos decision. Three Braavos-related projects were entered. The PM may re-mock it for Ray with crypto instead of fiat, which Charlie thinks would confuse merchants further.
- Nobody knows Ray's impact yet, including the data team. Both consider the Ray forums pointless until there is substance. Braavos was a clear, defined thing; Ray is "go as you go".
- Phone support confirmed not required for Ray. UK B2C phone support is a regulatory requirement, but Ray is not launching in the UK until the US happens. Target markets: Philippines, Argentina, Brazil, UAE and others, all in legal review.

**Decisions**
- Replace AJ with a broader "support systems administrator" role, Zendesk omitted from the JD.
- Deferred: the 6-month Zendesk contract extension, pending procurement consultation.
- Agreed in principle: Fin gets controlled deterministic data via attributes. No dashboard-link deflection.

## Insights

- The Zendesk-to-Plain business case hinges on configuration maintenance volume at scale, not on CX. That framing was chosen deliberately. Evidence needed: config item counts and maintenance projections.
- The 6-month extension is a live, unresolved trade-off: time to de-risk versus tipping off the incumbent and crossing the fiscal year.
- The team is losing its only deep Zendesk admin during the exit-planning window, and has single-point-of-failure risk on Anna. The config metrics needed for the assessment sit with exactly those two people.
- Requirements ownership stays with operations (Joel, per Oliver). Product and tech implement. Worth holding that line explicitly in the platform assessment.
- Looker MCP viability for Fin is unconfirmed and is a real gap if query generation is not automatic.
- Fin data design principle established: deterministic attribute-driven procedures, platform-agnostic, minimal data exposure, verification reflected as a flag. Reusable in Plain, which makes it a safe thing to build now.

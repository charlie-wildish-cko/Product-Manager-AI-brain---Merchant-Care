# Operations Platform Vision: session with the head of Risk Operations

**Date:** 2026-10-13
**Attendees:** Charlie Wildish (PM, Care), Luca (head of Risk Operations)
**Source:** Gemini transcript, `Downloads/Luca _ Charlie - 2026_10_13 15_01 BST - Notes by Gemini.md`. Both speakers appear under one label. "Plane" = Plain, "Finn" = Fin, "RA tool" is also transcribed as "array tool" and "RO tool", "Ry" = Ray. Names of other people and one team location are garbled and omitted.

## Context

Charlie played back the operations platform model and asked how Risk Operations works today and what the impact is on the teams and on customers.

## Key Points

**Checkout-initiated work dominates.** The vast majority of Risk Operations work is Checkout-initiated, not customer-initiated. Customer-initiated work gets prioritised, but customers are also affected by what Checkout does for them and need to be notified.

**Current state**
- Most teams work from Salesforce, in a basic setup that limits queueing and reporting. Very few teams have an optimal setup.
- Information is requested by email, from Salesforce or straight from an inbox. Teams do email management and download PDFs from inbound emails. Very little arrives through the Dashboard.
- There is no single secure place for merchants to upload documents, no scanning for sensitive content, and no company-approved way to ask for sensitive information (for example a passport copy). Secure upload exists for some Dashboard flows, such as bank account, and not others. It has been flagged several times and never prioritised. Merchants eventually send documents by email.
- Cases close as "closed" with no recorded outcome (approved, declined, escalated), so there is no clear path of what was done, when, or the result.
- No thread links a case to the work done and its outcome.
- Platform sub-merchants are asked for information through the platform by webhook. Risk Operations cannot see when a request was sent or whether chasers ran.

**Ideal state for requests (Risk Operations view).** Automation asks the merchant for what is needed, schedules chasers, and gives the merchant a clear, secure way to respond. The data is ingested, then goes to automation or a human with AI assistance. Reporting is granular, with customisable statuses.

**Periodic reviews: the scaling concern for next year**
- Periodic reviews refresh KYC and KYB every one or three years. Productivity is low because of convoluted systems, manual work in Genesis and emails to merchants.
- The first cohort of sub-merchants from the IP full platform product comes due next year. Monthly intake rises from about 100-150 cases to about 450. Each case takes one to two days to close. There is no plan to cope beyond adding temporary agents.
- The RA Tool has not delivered straight-through automation for them.
- The UAE platform adds a rule: every expiry of a passport or trade licence needs a new document requested, outside the review cycle. The product holds the date but does not prompt or resend, so humans download reports and ask merchants one by one.
- Onboarding is better: it has automation and the RA Tool can communicate with merchants. If the rollout goes team by team, periodic reviews should start first. Other teams carry about the same volume next year. Platforms and SMB will add more.

**Outbound is under-thought.** The thinking has focused on inbound, not outbound. With about 20 ISVs each with 100,000 merchants, the way requests go to merchants and come back is not nailed down. Platforms may or may not have an incentive to relay and chase, and calls with platforms are being set up to define their responsibilities.

**Customer layer.** Any customer data, including communications, should be visible to everyone: what was asked, when, whether the customer responded, and the consequence if not. This is also the audit view.

**Model feedback**
- The ideal state matches the model. The model holds if mapped team by team, with expected exceptions.
- A single entry point for customers, with a customer agent solving any customer-initiated query (Fin does this for Care only today), and other entry channels such as the Disputes email shut off.
- Every piece of work has a case ID. Work done outside the case links back, and the outcome is always logged with who or what did it.
- From the customer's side, a single "Care layer": today the Dashboard shows Care's replies but not another team's, so a Care request looks unanswered after Disputes has replied by email.
- The orchestration layer stitches case work to tools, sets permissions and routes work. Shared services hold all data sources. The RA Tool is a UI on top of interfaces and data, and the interfaces stay useful whichever UI sits on top.
- Pragmatic design: one case system and one tool for actions, linked to where the work is done, is enough. A fully custom unified tool (a headless portal on Plain's API) is possible and expensive. The case record creates downstream work items in the tool, and the outcome registers back on the case. A different UI per use case (for example the AI-powered credit review form prototyped by another team) can sit on the same backend with outcomes in one format.
- The RA Tool vision was a merchant risk 360 that updates a customer's risk level from events. The shared layer should hold that data.

**Prioritisation.** Value distribution: importance, cost saving, or value to the customer. Periodic reviews are high reward and high complexity because they touch every part of the cycle. Data on volumes, work types and handle time per case is a must have, to size the future and to prioritise.

**Plan and capacity**
- Care moves to Plain by end H1 2027 because of the Zendesk contract expiry at end of June. Other teams follow from H2 2027. Whether Ray and some other teams join the first wave is a scope question.
- Someone must build configuration for each team's workflows. More engineers are expected next year, but hiring lags.
- It needs EP-level investment from both Product and Operations.

## Asks of Charlie

- Someone from Product to spend time with each Ops team, starting with periodic reviews, end to end, including how information reaches the customer and how to get them to respond.
- Case volume analysis, with trade-offs and costs, and the team sequence.

## Action Items

- Charlie: get volume, work type and handle time data per team (from the Q4 work inventory), starting with periodic reviews.
- Charlie: add the outbound request pattern and the secure upload gap to the definition doc (done 2026-10-13).
- Charlie: arrange time for someone in Product with the periodic reviews team.

## Insights

- Checkout-initiated work is the majority for Risk Operations, so the inbound framing understates the problem.
- Periodic review scaling (about 150 to 450 cases a month) is the first quantified growth point outside Care.
- Outbound requests to platform merchants are the largest unresolved design gap.
- The head of Risk Operations accepts the model and supports a pragmatic version: one case system and one tool, not a custom unified tool.

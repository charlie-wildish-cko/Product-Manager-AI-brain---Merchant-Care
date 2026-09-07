# Stephen / Charlie — payments diagnostic for AI

**Date:** 2026-07-30
**Attendees:** Charlie Wildish (PM, Merchant Care), Stephen Gilbert
**Drive source:** 1X133tJ-BFxqKqu8xcU2yaYQvMv1asbRmrucJ1wCSAAc

## Context

Third SME review of the payments diagnostic agent instruction docs. Stephen's angle produced the main new gap: gateway validation errors.

## Key Points

**Why this is the biggest automation opportunity**
- Payment-related queries are 60% of all Care contacts: 50% pay-ins, 10% payouts.

**Architecture**
- Build a custom in-house payments diagnostic agent that Fin calls via API, rather than having Fin traverse multiple data sources itself. Rationale: control over the reasoning process, access to internal margin data, avoids a third-party black box.
- The existing payment performance analyzer was rejected for this use case on three grounds: latency (crawls too many sources; a chat agent cannot have a five-minute wait), prohibitive cost, and inability to validate sources or maintain accuracy (would depend on the payment performance team's effort). Both noted you can only catch its errors if you are already an expert.
- Bedrock output guardrails are in scope from the start, to prevent leaking internal optimisations, stack traces, and internal data. Stephen raised this independently and considers it essential.

**Instruction doc**
- Structure: role, data sources, reasoning framework, triage, decline debugging, output rules. Sources merged in: interview notes with Keziah, input from Armi (who maintains a Claude dashboard listing everything she checks to diagnose a payment), the existing Traffic Insight payment performance analyzer, and the newly released gateway analyzer.
- Single data source today is the payment search API, a limited subset of dashboard search fields. Three query identifiers: payment ID, ARN, merchant reference. Charlie's estimate: ~80% of needed fields, with the missing 20% covering the harder residual queries.
- Triage sequence: fetch record, read status/response code/summary, determine path, action trail, reconcile totals, check acquirer, then dispute, 3DS and risk statuses.
- Decline debugging holds the complexity, and getting the decline explainer right covers an estimated 80% of everything. Code ranges: 40,000-range = internal risk flag, 20,000-range = issuer flag. Branches for internal/acquirer response, risk, issuer, 3DS, and third-party (TPA) declines. Then read retry recommendation (Visa/Mastercard codes), check authentication statuses, validate payload, check credentials (network tokens, MIT/CIT), check routing (cross-border, MCC, currency). Routing last. A separate decline debugger doc and a separate response-codes reference file exist.

**Gap found: gateway validation errors**
- Missing from the docs. Merchants perceive them as declines even though Checkout classifies them differently. Example: pay-to-card transactions returning 422 for insufficient balance, often traceable to a merchant config or payload issue.
- Findable by payment reference. The request ID returned in the error response would be better but is not in the Search API, so it needs an extension.

**Payouts**
- Logic is a stub and needs building out. Armi flagged that a 40x-range code on a payout means something different than on a pay-in.

**Output**
- Customer-facing explanation plus two internal attributes: escalate yes/no and a reasoning trace. Escalation rules still need defining, e.g. self-serviceable config issues should not escalate.

**Adjacent: Glean as interim tooling**
- Charlie met the Treasury team, who had a bespoke AI tool built by the AI team that is already out of date. His argument: a Glean agent with a skill querying Looker would do the same job.
- Care is testing Glean for Looker payment and settlement retrieval as a cheap interim before engineering investment. Glean is available as a Chrome extension (the Zendesk app is being removed), so an agent can run alongside Zendesk.

## Insights

- The long-term play is to embed explanation semantics into the payment data itself (LookML or Data Hub), so retrieving a payment returns a plain-language sentence per field. That removes the need for a large instruction markdown file: the agent then interprets and compresses explanations rather than executing if/then logic. The data team owns merging raw data with its semantics into one interface.
- This is not care-only. The same explainer is reusable in the Checkout MCP, the dashboard, and checkout flows so merchants self-serve. Charlie has seen no customer-facing payment explainer in the market. The merchant-facing version needs less depth, since most merchant queries come from people with little payments knowledge.
- Interim state stays a reviewed, version-controlled markdown file, reusable internally via Glean.
- Validation risk is the recurring theme: hallucination, instruction adherence, and whether documentation exists to answer each scenario.
- First testable version targeted this quarter (Q3 2026), no hard date committed. Stephen to review both docs within two weeks, focused on completeness and sequencing rather than prose. Charlie will then convene Keziah, Armi and Stephen together once all three reviews are in.

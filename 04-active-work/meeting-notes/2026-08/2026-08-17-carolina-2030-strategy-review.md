# Charlie / Carolina: 2030 Care Strategy Review

**Date:** 2026-08-17
**Attendees:** Carolina Corral, Charlie Wildish
**Drive source:** 12O1IQOoEEHh6a1fB_Sy_FSE_h45nSJV4aYpI3H4Kjjc

## Context

Review of the 2030 Care strategy document ahead of turning it into a stakeholder presentation. (The first few minutes cover sensitive personal circumstances for Carolina and are not summarised here.)

## Key Points

**Forecast**
- Framing shift: move from "Merchant Care" to "Care," covering merchants, SMB and consumers, with a possible future split into merchant care and consumer care.
- Volume does not change much until 2028. 2028 is the inflection, driven mainly by consumer. Carolina pushed back that 2026 already shows roughly 100% growth, so relative growth is already 2x even where absolute volume looks manageable.
- Charlie's caveats: consumer acquisition numbers are probably too ambitious, pushing the consumer curve to 2029-2030; SMB is probably under-forecast because the numbers predate SMB becoming prominent. The two errors partly cancel.
- By 2028 roughly a 50/50 consumer/merchant split. Beyond that Checkout becomes more a consumer-supporting business than a merchant-supporting one by volume.
- Contact rate benchmarks: tier 4/5 around 120 contacts per million transactions, tier 1 around 3. SMB drives most merchant contact growth.
- The forecast deliberately excludes AI resolution and self-service modifiers to show leadership the raw cost implication. Held-back assumptions: ~70% AI resolution from 2027-2028 (doable next year for merchant volume), possibly 50% for consumer, self-service 20-30%.
- Constraint: the data scientist who built the forecast has left the business.

**Strategic positions**
- Do not use AI as a crutch for product gaps. Charlie pushed back on a circulating assumption that 100% of consumer contacts can be handled by AI: "who told you that? Because that's wrong." UK Consumer Duty requires human paths and anything can be a complaint in the UK.
- Regulatory variance must be modelled per market, not globally. US requirements vary by state (a visible phone number may be required in California), and EU, non-EU and UK differ on channel requirements.
- Products ship with no mechanism to reduce contacts. Product accountability for contact volume is missing.
- Cost structure: move off a London-centric opex base, and not only for frontline. Include Oliver's team, data teams and programme managers. Carolina's figure: a UK hire at ~100/year does the same work as ~50/year in Mexico. Consumer costings were inflated by UK-based headcount. GM has a ~50% margin target for 2030.

**Identity and the guest problem**
- Onboarding IDV runs through Checkout's own IDV business line using Onfido. Account creation will carry a high defect rate.
- Three consumer types: guest (transacted, not fully verifiable), verified (has an account, email plus phone on record), fully authenticated (Ray/Braavos-level KYC).
- Guest is the risk case: an unidentifiable person emailing for a refund with no traceable record, potentially in Consumer Duty scope. Social channels may also become a request source.
- Legal is assessing division of liability between Checkout and the merchant, which decides whether consumers get redirected to the merchant or handled three-way.

**Segmentation**
- Segments: B2B White Glove, B2B Non-White Glove, B2C. Segments map to plans: Premium, Enterprise, Growth, plus a new Essential tier for SMB/tier 5 (name TBC). Plan determines account management, coverage rules, channel access and routing.
- Carolina's addition: prioritise need first, then layer ARPU and LTV, using Prime and Spotify analogies. Complexity differs by segment (enterprise custom API/ERP integrations versus SMB on Shopify plugins).

## Decisions

- Do not use AI to fill product gaps.
- Outsource all frontline consumer support agents to BPOs. Carolina's rationale: BPO contracts allow cutting headcount from 100 to 50 in 90 days when automation lands, where in-house requires consultation, restructure and severance. BPOs also absorb recruiting, people team, team leaders, background checks and equipment, roughly a third of the cost.
- Segmentation prioritises customer need first, then value.
- Adopt the segment-to-service-plan framework to standardise routing and support operations.

## Insights

- The BPO decision is load-bearing: it converts automation into realised cost savings and gives contact-reduction work a P&L story. Consumer launch staffing plans should assume vendor, not FTE.
- The 70% AI resolution and 20-30% self-service modifiers are sensitivity levers deliberately held back from the published forecast. Know they exist before someone concludes the cost curve is too pessimistic.
- Guest consumer identity is the unresolved foundational gap and links directly to Joseph's customer object work. Same problem, two owners.
- Forecast maintenance is now unowned.
- "Essential" is a placeholder name. Check what it becomes.

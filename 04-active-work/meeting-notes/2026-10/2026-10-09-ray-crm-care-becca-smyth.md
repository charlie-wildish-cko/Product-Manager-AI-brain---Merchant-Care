# Charlie / Becca - Ray CRM<>Care

**Date:** 2026-10-09  
**Attendees:** Becca Smyth (Ray/Braavos CRM and marketing ops lead), Charlie Wildish. First meeting between them.  
**Drive source:** 10Nxev_apzLwA3SHJiOFFyado6hqfkKlmeIi3OTgQ6s0

## Context

Intro to align Ray CRM, consent and campaign data with Care's data needs, and to open the SMB conversation. Names in the transcript are noisy (Alice Beddis / "Allison", Fabio Marquez).

## Key Points

**CRM and consent**
- RFP run, Braze selected, access obtained, build starting. Braze receives consumer data and sends marketing and service comms.
- Consumer preference center with granular toggles (interviews, surveys, rewards) instead of a single unsubscribe. Legal decides what is captured. Becca wants consent granularity defined, then Alice to publish it to BigQuery.
- Customer 360 (Alice) holds consumer attributes and facts. Braze campaign metadata and engagement tables (event and customer level) will likely land in BigQuery for marketing analytics and Looker.

**Care data model**
- Charlie: Care is AI-first, the agent queries whatever data is relevant. Care prefers raw data easy to query by identifier over logging into multiple tools. Comms and campaign data is not needed from day one but belongs on the accessible list.
- Likely Care needs: campaign history, offer/rewards history (e.g. cashback redemption), consent changes ("unsubscribed but still getting emails"). Charlie: it is a timeline of timestamped events and settings.
- Merchant-side pain: Visa AFT mandate change. Comms went out, merchants did not read them, integrations broke, contact wave followed. No central record of comms, deals and discounts sent to a merchant, so teams Slack each other.

**SARs and deletion**
- SARs and complex issues go to humans via intent recognition, not AI-resolved. They sit with Fabio Marquez's consumer fraud team, which is building the function. Whether SAR process is needed from day one of launch is open (Becca raised legal timeframes).
- Engineer (Jason) is building full consumer account deletion. A deletion audit log must exist in BigQuery in case a record resurfaces in CRM or comms (aligned).

**SMB and B2B**
- SMB starts next year and is close to pseudo-consumer, so merchant support must change radically. Joe Zender leads SMB product. Charlie expects unified merchant comms, not SMB only.
- Tier 5 merchants (no account manager, low volume) are effectively SMB today.
- Current B2B CRM (Pardot on Salesforce) is old and out of support. Evaluating Braze for SMB is a Becca goal. Separate Braze instances for legal reasons, as Care does today.
- Contact-us forms auto-disqualify below a TPV threshold. Needs review for SMB.
- Charlie: consumer is a fresh start and can be the gold standard. Merchant side carries tech debt.

## Insights

- Braze is the CRM for Ray consumer data. It stores content and marketing comms data that Care can use (campaign history, comms sent, consent changes), so the source of truth for comms exists. The open item is only the export path from Braze to BigQuery for query-by-identifier access.
- Care's Ray data path is BigQuery by identifier. Ownership of exporting Braze campaign and consent-change data to BigQuery is unassigned (Customer 360 work does not cover it). Open dependency, but the data itself lives in Braze.
- Ray deletion audit log is agreed in principle but has no owner (engineering process).
- Ray SAR day-one process is unconfirmed and sits with the consumer fraud team.
- For the 1 Dec F&F, Care is human-handled (see Ray Readiness Steerco, 2026-10-08), so agents will need consent and campaign history from BigQuery without an AI layer.
- SMB 2027 needs a unified customer record across comms, consent and commercial terms. CRM choice (Braze vs Pardot/Salesforce) undecided.
- Visa AFT incident and the lack of a central comms/deal record are reusable evidence for business cases.

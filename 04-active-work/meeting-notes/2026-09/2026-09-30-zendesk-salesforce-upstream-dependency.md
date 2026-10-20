# Zendesk <> Salesforce Upstream Dependency

**Date:** 2026-09-30  
**Attendees:** Charlie Wildish, Jiro Farah (engineer), Fraser Bryant (EM), Joshita Narrain (Salesforce admin lead), Diya Dewnarain (Salesforce support), Priya Nair (business systems), Januka Jeyakumar  
**Drive source:** 1UWjyM67TuLRvSy3sdrbyUk3A6csRSptfOp8npo9SIps

## Context

Care routing and prioritisation depend on Salesforce merchant data with no formal contract. Recent tier changes broke flows, so the meeting aligned Care with the Salesforce admins on ownership and change communication.

## Key Points

**How Care uses Salesforce**
- Salesforce is the source of truth for who is contacting support and which merchant they belong to.
- Prioritisation uses merchant tier only, not incentive rating. Resegmentation may combine fields (for example tier 1 plus gold).
- Pipeline: Salesforce data via BigQuery, joined with Dashboard data into a Care-owned user profile table on BigQuery, fed to Zendesk.
- Tickets are point-in-time. A tier change updates future reads but not existing tickets.

**Incidents**
- Tier 4's API name "unmanaged" was renamed "tier 4". The UI label already read Tier 4. Care uses backend API values, not labels. The rename was communicated only after Joshita's dependency analysis found Zendesk as a consumer.
- Tier 5 was introduced without prior mapping and broke some flows.
- API-name changes are rare and against best practice. New tiers are commercial-driven and vetted.

**Domain mapping gap**
- Unknown contacts and domains drop into manual review, which defeats automation. A wrong domain on an account maps users to the wrong merchant and crosses client boundaries.
- Examples: an unmapped domain on a tier 1 merchant (Tabby) broke enrichment, delayed response and broke SLAs. Regional variants (.com vs .sa) recur.
- Account domain is an auto-calculated, non-editable formula field built from contacts and website. Sales reps and BDRs own accounts and contacts, so the commercial team owns accuracy. Admins maintain but will not bulk-change data without owner vetting.
- Care could set its own domain rules in Zendesk, but that creates a mismatch with Salesforce.

**Ideas raised**
- Weekly or monthly report of unmatched emails that look like merchants (possibly from Looker) as a working list for commercial.
- Metric of incorrect records over time.
- RevOps enrichment may help. Align flow, frequency and process with process owners before any tech change.

## Insights

- Routing is exposed to an uncontracted upstream Salesforce dependency. It carries over to the Plain migration.
- Domain mapping gaps are a recurring root cause of manual review and SLA misses for top-tier merchants.
- Decisions: Care product team joins the Operations Slack channel for Salesforce updates (Care's own channel is private). Care provides a spreadsheet of critical Salesforce fields with API names so changes can be tracked.

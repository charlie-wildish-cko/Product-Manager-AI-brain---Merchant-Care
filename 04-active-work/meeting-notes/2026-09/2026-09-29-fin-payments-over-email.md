# Finding a Solution for Fin Serving Payments Over Email

**Date:** 2026-09-29  
**Attendees:** Fraser Bryant (EM, organiser), Charlie Wildish, Jiro Farah, Yifei Zhang, Harlie Patel (speaker attribution unreliable, treat views as the group's)  
**Drive source:** 1raE4Rgw6MzmM-DbKJu4S4BXZvAxLsqw6uwjQWs4bNYs

## Context

The Q4 deliverable to let Fin answer payment-status queries over email (merchant emails containing a payment ID). It is the outlier against the orchestrator and expert-agent vision. Core question: build for Zendesk or for Plain.

## Key Points

**The dilemma**
- For Plain: every other Q4 deliverable targets Plain, so a Zendesk build is throwaway, and Fin-on-Plain certainty is itself a Q4 task.
- For Zendesk: results sooner. Counter (Jiro): benefits only show at the B2B migration to Plain, estimated Q2 2027.
- Rework would consume a 2027 engineer needed for B2B. The group does not believe Zendesk-to-Plain rework is a week, since verification and commenting flows are tied to Zendesk.

**Current Zendesk flow**
- Email becomes a ticket, a tag (payment search request) fires a Zendesk trigger and webhook, a background service looks up via internal APIs and posts the result. Re-applying the tag retriggers.
- Auth today uses an access token carrying client ID and permissions. Option two: authenticate on Checkout's side from sender email plus payment ID, then call payment search with a service-to-service token. Needs a replicated merchant profile.

**Plain enrichment (Jiro)**
- Plain tenants map to clients by domain. 98% of clients have one tenant, 80% of those a unique domain, so about 80% of users auto-map and about 20% need manual enrichment.
- A new service subscribes to BigQuery table events to create, update and delete Plain tenants.

**Proposal: platform-agnostic design**
- A standalone service enriches independently: email to user and client, permission check against the source of truth, payment retrieval. This removes dependence on ticket fields and agent edit errors.
- Only the commenting step is platform-specific (about 20%): a small component posting via the Zendesk or Plain API. About 80% is shared.
- Fin triages first using docs and Procedures. If it cannot resolve and finds a payment ID, it sets a tag via a data connector. The service reacts and posts as a secondary agent. Fin stays assigned and reads the thread (not internal notes).
- Fin calling webhooks directly hit authentication issues last week, hence tag only. Another agent's public comment on a Fin-assigned ticket is expected to work but is an assumption to test.
- Unresolved: whether Fin is needed to send the response, and fit with the orchestrator vision (one service or two).

**Why it matters**
- Leadership uses deflection percentage as the proxy for L1 headcount. A 40% deflection target was expected to remove 5 or 6 L1 agents. Volume growth cut the planned reduction to 3.
- Without an email solution, deflection caps at about 30% on current work, which likely means headcount increases again.
- Deflection is not a current OKR. Charlie notes it is the metric leadership understands and could become a key result next year.
- Dashboard login links were rejected: many users have accounts but do not use them, and a prior mandate of all support via the dashboard "didn't fly". Email stays for the fixed set of enterprise-focused merchants.

## Insights

- No decision. Status: needs further discussion. A Figma visual of the platform-agnostic backend, Fin's tagging role and per-platform adapters is next, to test assumptions.
- Payments-over-email is the gating item for deflection beyond about 30%. Default direction is a platform-agnostic service with a thin comment adapter.
- No Plain-dependent deflection benefit before Q2 2027.
- Headcount narrative risk: L1 reduction already scaled from 5-6 to 3.

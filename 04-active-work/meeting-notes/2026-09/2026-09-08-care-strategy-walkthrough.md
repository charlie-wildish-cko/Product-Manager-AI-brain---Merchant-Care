# Harlie / Charlie - intro to Care

**Date:** 2026-09-08
**Attendees:** Charlie Wildish, Harlie Patel
**Drive source:** 1unLyAfEU0DUPXvapyWYAJw--x3tmnQMCF3o-6VKx7uQ

## Context

Onboarding walkthrough for Harlie, but it captures Charlie's current framing of the whole Care strategy with numbers attached. Worth treating as a strategy snapshot rather than an onboarding note.

## Key Points

**Segmentation and Care's function**
- Tiers 1-4 are white-glove. Tier 3 merchants get a dedicated AM. Simmyi leads ~10 AMs covering tier 4 at a 20:1 ratio. Tier 5 is unmanaged, grandfathered SMB with high attrition.
- Operations prioritise tiers 1-3 because 4 and 5 generate minimal revenue and are low risk if lost.
- Care takes over day-to-day support and operations work for merchant support and finance teams, acting as second line when a merchant cannot resolve an end-customer issue (failed orders, refunds).
- Support plus finance and reconciliation work is 80% of all inquiries.

**Business models**
- Direct merchants, then platforms and ISVs (named: Shopify, Final Site, Sunday). Final Site processes for schools, adding a layer where Checkout serves Final Site who serves the schools.
- SMB (sole traders up to ~30-person startups with limited payments understanding) is scheduled for support expansion next year.
- Unit economics: white glove is justified on margin for accounts like Netflix. For SMB, support cost can exceed the revenue the merchant generates in a week. Scaling requires AI and optimisation to hold cost down.

**Braavos and Ray**
- Braavos (consumer fiat wallet, UK launch) paused indefinitely on regulatory cost, reporting requirements and Consumer Duty compliance.
- Ray reuses the app work to hold crypto instead of fiat, non-custodial on public blockchains, removing safeguarding and interest obligations. Target markets UAE, Philippines, Brazil, Argentina, chosen for low regulatory exposure.
- Ray support is self-contained in-app using a specialised version of the AI agent. Launch to 100 friends-and-family at end of year, public beta in Q1. BPO call centres are the low-cost human fallback.
- B2C and B2B are supported on distinct architecture streams sharing system capabilities with tailored context, not duplicated builds.

**Scaling and AI economics**
- The engineering team triples next year, adding two squads: one on resolution workflows, one on core platform, channels and integrations.
- Contacts (tickets, calls, IMs, AI chats) projected to grow from 50-60k per year to 1-2m per year, driven by consumer. Benchmark cited: PayPal's historical 5% contact rate per customer.
- North star for Fin is 80% resolution over the next few years, flattening human headcount growth.
- AI resolution 90 cents against human $20-25 per resolution. Even at 80% AI resolution, hundreds of thousands of contacts still hit humans, so agent workflow efficiency is mandatory. Humans remain necessary for complex cases, vulnerability and complaints.
- Current Fin performance: handles ~25% of total volume at 70-80% individual resolution rate, giving an overall resolution rate of 16-18%. Charlie expects above 40% once email replies can include payment data and the dashboard contact form is removed so Fin becomes the default channel.
- Complaints face strict regulatory mandates, especially North America and Europe. General support queries have no legal restriction on AI deflection.

**Platform, taxonomy and Reflex**
- Migrating away from Zendesk: Zendesk ended support for third-party AI in April, and the platform is legacy, clunky and inflexible.
- Care is a fallback, not the default path. B2B and consumer self-service portals take priority. Email is retained deliberately as an experience choice for big merchants, who will not move off it.
- Taxonomy has three hierarchical levels and ~10 top-level query types.
- Agent experience goal: agents review and approve pre-generated AI responses rather than doing manual lookups.
- Reflex uses contact body content to derive granular problem topics and surface them to PMs. Charlie's triage thresholds: a single problem above 2% of volume is chunky, above 5% is a major concern. Access needs Cloudflare plus VPN.
- Commercial gap: qualitative merchant feedback from commercial teams reaches support priorities only via AMs and admin request queues, so there is no structured path. Charlie wants Reflex data aligned with commercial data.

**Decisions**
- Roll out Ray in non-UK markets (UAE, Philippines, Brazil, Argentina) to keep regulatory exposure low.
- Retain email support channels for large merchants.
- Braavos paused indefinitely.

## Insights

- Cleanest statement on record of the AI investment case: 50-60k contacts today growing to 1-2m, Fin at 16-18% overall resolution today, 80% north star, 90 cents against $20-25 per resolution.
- The human cost figure here ($20-25) is lower than the ~$40 per contact benchmark in CLAUDE.md. Reconcile before reusing either number in a business case.
- The path from 16-18% to above 40% is named and concrete: payment data in email responses, plus removing the dashboard contact form so Fin is the default channel. That is a prioritisation argument, not an aspiration.
- Tiers 4 and 5 are explicitly deprioritised while SMB support expansion is planned for next year. That tension needs resolving in SMB scoping.
- Reflex triage thresholds (2% chunky, 5% major concern) are usable as a published convention.
- The commercial feedback path is unstructured today. The same gap surfaced independently in the bug/enhancement standardisation session the next day.

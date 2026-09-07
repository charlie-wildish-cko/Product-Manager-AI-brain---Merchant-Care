# Charlie / Sammie: Balances MFE and Strings Externalization

**Date:** 2026-08-13
**Attendees:** Sammie Spector, Charlie Wildish
**Drive source:** 1gE6pqwXEbrCDUm3az8EXvdFp08TiKA-6ZeY0DwP4uwk

## Context

Selecting a dashboard page for the design hackathon (roughly w/c 24 August) to test whether content and design changes alone reduce support tickets.

## Key Points

- Strings externalization was presented to Moran as part of a design AI showcase and won a short-list position for the hackathon. Pitch includes helping Care with support tickets and helping localization.
- Automation coverage varies per MFE and nothing is fully automatable. The best-automatable MFEs contain little that matters to Care; the ones that matter cost more hours.
- Balances chosen as the pilot: decent automation coverage, roughly 18 hours of engineering work, most already done by the hackathon team, known problem area, enough ticket volume to be a meaningful test.
- Pages excluded: Payments (Joseph has 6-12 months of work on it), Reports (too complex), Account configuration (poor fit), Transactions (probably the top volume driver but too complex). Login is a useful case study but anything touching Okta stays hardcoded.
- Fin data point: Charlie built a Fin Procedure for recovery questions. Since the prior Friday it triggered 11 times and resolved 10. Charlie's preference is preventing the issue in the UI rather than depending on a bot response. Sammie framed the loop as reducing volume in each bucket: UI, then technical doc, then Fin, then escalation.
- Attribution limitation: support cannot be attributed to a dashboard page by page context. Most Fin conversations open from the homepage and onward browsing is not detectable. Attribution runs off the ticket-level taxonomy value Fin detects, which passes to the Zendesk ticket. A specific Balances taxonomy value exists.
- What is wrong with Balances: generic "read the docs" content, no dynamic guidance for negative versus positive balance states, no indicators. Charlie's generalisation: every page is designed without accommodating the states where a user needs help, so merchants go straight to support.
- Three delivery layers: traditional design handoff to engineers; design-system changes designers make themselves using Claude; content changes to extracted text files owned by content design. Dynamic text may still need engineering.
- Future candidate pages per Charlie: Authentication (top contender), Settlements, Business Account, Compliance Requests/RFI (recent cluster of merchants not understanding what to submit for payouts blocked by sanctions screening), Payment Links and payment interfaces (untouched for 4-5 years), and settlement configuration and bank account changes.

## Decisions

- Balances is the pilot page for the design hackathon. Payments explicitly out of scope.
- Charlie generates a 90-day Balances support report including merchant IDs and ticket IDs.
- Sammie briefs Frank and Jordan on the Balances team, then hands to Chrissy as hackathon point of contact.

## Insights

- The prize is not the Balances page. It is proving that content design can ship a support-reducing UI change with zero engineering involvement, which then generalises across the dashboard. Direct contact reduction at near-zero marginal cost.
- Page-level contact attribution depends entirely on the taxonomy value, which is a live argument for taxonomy quality and Fin classification accuracy.

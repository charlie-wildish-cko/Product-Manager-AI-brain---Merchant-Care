# Shein — Merchant Support Needs

**Meeting:** Ziyuan Liu / Charlie — 2026-01-21  
**AM:** Ziyuan Liu, Madelyn Lo  
**Segment:** Tier 1, APAC (China), global e-commerce, API-first  
**Drive source:** 1osy3pO4JJ1Gihy8K0havGtXhY19rn0T4_L3PExnQlB4

---

## Merchant Profile

Large global fast-fashion merchant with a dedicated global payments team (BD, Ops, Products). API-only — does not use the Checkout dashboard. Compliance policy prevents holding cardholder credential data in a PSP dashboard; all operations run via internal tooling and APIs. Despite high processing volume, ticket count is lower than expected given its size.

---

## Support Channels Used

- Email / tickets (formal)
- No dashboard usage (compliance block)

---

## Primary Support Needs and Pain Points

**APM status and dispute queries (~60% of tickets)**
Mway (Multibanco) and Pay to Card are less mature than card acquiring. Shein raises queries about:
- Uncertain refund statuses
- "False capture" — Mway shows a decline response but the transaction was actually captured
- Dispute management for APMs — no API exists; disputes are handled via email/chat groups
> "Maybe 60% is actually related to APMs and also Pay to Card because APMs — Mway and Multibanco — they're not very mature solutions compared to card acquiring. So they have a lot of queries including the status of the refund or the payment."

**Pay to Card — RFI links and status**
No API for Request for Information (RFI) links or status. Cardholders cannot open RFI links. Status checks require manual L2 escalation.

**APM permission barriers**
L2 escalation is required for many APM queries due to permission constraints (e.g. Mway S portal access is limited to L2).
> "Most times it's due to some permission issue — rely on level two care support with the APM dashboard."

**Clearing process visibility**
Payments show "captured" before clearing completes. Shein follows up assuming something is wrong, when the payment is simply in the clearing window.

**Card acquiring queries (~40% of tickets)**
Acceptance rate drops on specific issuers/markets, and complex dispute queries via standard card schemes.

---

## Key Insights

- The majority of Shein's support contacts are caused by product immaturity in APMs (Mway, Multibanco) rather than merchant behaviour. The fix is product investment in APM tooling, not merchant education.
- The "false capture" bug on Mway (showing decline, actually captured) is a known issue generating avoidable contacts.
- Dashboard-based self-serve and Fin are structurally inaccessible to Shein. Any automation for this account must work via API or email channels.
- APM dispute handling entirely via email/chat groups is not scalable as APM volume grows.
- Clearing process visibility is a low-effort product fix that would eliminate a class of contacts.

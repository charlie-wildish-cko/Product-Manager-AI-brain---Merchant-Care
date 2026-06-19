# Ant Financial — Merchant Support Needs

**Meeting:** Ziyuan Liu / Charlie — 2026-01-21  
**AM:** Ziyuan Liu, Madelyn Lo  
**Segment:** Tier 1, APAC (China), financial institution / PayFac  
**Drive source:** 1osy3pO4JJ1Gihy8K0havGtXhY19rn0T4_L3PExnQlB4

---

## Merchant Profile

One of the most complex and demanding accounts in APAC. Financial institution operating two models: own MR model and Payback (sub-merchant PayFac model). Payback creates varied technical issues across sub-merchants. Large team (~150 people in the support chat group). Professional and detail-demanding — monitors acceptance rates per sub-merchant and detects decline spikes that Checkout's own monitoring does not flag. Uses DingTalk (InTalk), a proprietary in-house IM app with no external integrations. Should use the Checkout dashboard but primarily relies on webhooks.

---

## Support Channels Used

- **DingTalk / InTalk** — proprietary in-house IM (150-person chat group); no Zendesk integration possible; tickets are logged manually by care team via screenshot
- Dashboard (partial — known bug affects usefulness)

---

## Primary Support Needs and Pain Points

**Payment status / confirmation queries**
Primary ticket type. Root cause: Ant has a large, siloed team with no standardised webhook setup procedure. When new processing channels are launched, different team members configure webhooks inconsistently, leading to missed payment notifications.
> "They didn't have a very standard procedure on enabling the webhook for each new business launch. So once they have a new processing channel, different people may be involved in the webhook subscription because they have a very big team — not always the same one — and they did not document this."

**Authorization failures (Payback sub-merchants)**
Payback sub-merchant onboarding introduces fraud-related declines that Ant's team escalates for investigation.

**Acceptance rate monitoring at sub-merchant level**
Ant detects issuer-level decline spikes that Checkout's own monitoring misses, and raises deep investigation requests.

**Webhook subscription dashboard bug**
The dashboard's webhook subscription view does not accurately reflect actual subscriptions — a confirmed bug not yet resolved. This amplifies the misconfiguration problem.

**Complex technical and fee queries**
Transaction fee lists, scheme behaviour per issuer, travel/fee-related questions arising from the Payback model.

**IM channel audit gap**
All support interactions happen in DingTalk — an in-house app with no external integration capability. The care team logs tickets manually from chat screenshots.
> "At the moment the team is basically logging every ticket manually from a chat with a screenshot so that we have a record — which sounds horrible."

---

## Key Insights

- The webhook misconfiguration problem at Ant is a process and UX issue, not a product failure. A dashboard intervention (pop-up reminder of prior webhook settings when setting up a new processing channel) was proposed by Madelyn Lo as a low-effort fix.
- The webhook dashboard bug makes the problem worse — the shown config doesn't match the actual config, preventing self-correction.
- Ant's IM tooling (InTalk) has no integration capability. There is no plausible path to integrating this channel with Zendesk or Fin. Manual screenshot logging is the only current option.
- With 150 people in the support chat group, the knowledge and process fragmentation at Ant is structural — individual queries will continue to surface unless Ant improves internal documentation and webhook governance.
- True contact volume for Ant is significantly higher than Zendesk data shows — all IM interactions are off-ticket.

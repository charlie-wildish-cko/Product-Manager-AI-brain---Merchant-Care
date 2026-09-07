---
id: 35005135101074
section_id: 34976600416658
title: "Platforms: Webhooks and Event Notifications"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/35005135101074-Platforms-Webhooks-and-Event-Notifications"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-04-22T09:52:53Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

This article explains what webhooks are, why they matter for Platforms for SaaS, which webhook events are relevant during onboarding, and what each event means in plain language.

## **What is a webhook?**

A webhook is an automatic notification. When something happens in the system - like a sub-entity's status changing - Checkout.com sends a message to a web address that the platform has configured. This means the platform doesn't have to keep checking the API manually; they're told when something changes.

Think of it like a text message alert versus checking your bank balance every hour. Webhooks are the alert.

## **How to configure a webhook server**

Before onboarding any sub-entities, the platform must set up a webhook server — a web address that Checkout.com can send notifications to. The platform then subscribes to specific events to receive only the notifications they need.

Checkout.com's [technical documentation](https://www.checkout.com/docs/developer-resources/event-notifications/receive-webhooks/configure-your-webhook-server) covers the setup steps in full.

For support queries about webhook configuration - for example, a platform saying they're not receiving notifications - this is a technical integration issue. Escalate to the technical support team.

## **Onboarding webhook events**

The platform should subscribe to all of the following events during the onboarding process:

| **Event name** | **What it means** | **What to expect next** |
| --- | --- | --- |
| sub_entity_created | A sub-entity record has been successfully created in Checkout.com | The platform can proceed with document submission and payment instrument setup |
| payment_instrument_verification_passed | The sub-entity's bank account or card has passed verification | Full due diligence checks begin |
| payment_instrument_verification_failed | The payment instrument failed verification | The platform needs to check and update the instrument details |
| full_dd_passed | The sub-entity has passed all due diligence checks (KYC, KYB, AML, sanctions, PEPs) | Payment and payout capabilities should be enabled |
| full_dd_failed | The sub-entity has failed due diligence checks | The sub-entity status moves to requirements_due or rejected. The platform must review and act |
| payments_enabled | The sub-entity has passed Card Scheme Screening (CSS) checks and can now accept payments | The sub-entity can start processing |
| payments_disabled | Payment capabilities have been turned off for the sub-entity | Check for a status change — may indicate a compliance issue or failed re-verification |
| payouts_enabled | The sub-entity can now receive payouts | Settlement to the sub-entity's bank account can begin |
| payouts_disabled | Payout capabilities have been turned off | Check for a status change — may indicate a compliance issue |
| status_changed | The sub-entity's status has changed (for example, from Pending to Active) | Check the new status and act accordingly — see Article 4 |

## **How status flows through webhooks during onboarding**

As the sub-entity progresses through onboarding, their status changes and webhooks fire in sequence. The typical flow for a successful onboarding:

- Platform submits the application → sub_entity_created fires

- Platform adds payment instrument → payment_instrument_verification_passed or payment_instrument_verification_failed fires

- Checkout.com runs full checks → full_dd_passed or full_dd_failed fires

- If verification fails at any point, the platform receives full_dd_failed, payments_disabled, and payouts_disabled webhooks. The sub-entity's status moves to requirements_due or rejected.

## **Settlement-related webhook events**

For settlement notifications, the platform subscribes to the settlements webhook category. These events notify the platform when funds are moving through the settlement lifecycle.

Full details are in the [technical docs.](https://www.checkout.com/docs/developer-resources/event-notifications/event-types#Settlements)

## **Troubleshooting / common questions**

**Q: A customer says they're not receiving any webhooks.**

This is a technical integration issue. The platform needs to check their webhook server configuration. Direct them to the technical docs. If the issue persists, escalate to technical support.

**Q: A customer received full_dd_failed but doesn't know why.**

Tell them to check the sub-entity's status via the Get Entity Details endpoint. The response includes a requirements_due object explaining which fields were rejected and why. See Article 2 for a full breakdown of reason codes.

**Q: A customer received payments_disabled after the sub-entity was already Active.**

If the platform updated the sub-entity's information after verification, Checkout.com re-runs the checks. If the re-verification fails, payments_disabled fires. The platform needs to check the sub-entity status and resubmit any corrected information.

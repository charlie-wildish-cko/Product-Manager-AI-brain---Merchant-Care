---
id: 29571032978578
section_id: 22188517144978
title: "Webhook Introduction"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29571032978578-Webhook-Introduction"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T17:56:49Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: ["webhook_introduction"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article**

To understand Webhooks and the role they play. INTRODUCTION TO WEBHOOKS 💬

**Webhooks** are a critical component for merchants, as they provide real-time, automated notifications about specific events. These notifications are "pushed" to a unique URL, eliminating the need for constant manual checks or GET requests. Why merchants use these:

- To automate updates in their systems (e.g. update an order’s status after a refund) 

- To get timely alerts for events like chargebacks or disputes without manual checking  

- Common features include signatures, custom headers and automatic retries

See the [webhook event types](https://www.checkout.com/docs/developer-resources/webhooks/webhook-event-types) article more information on what event types a merchant can subscribe to.CONFIGURING WEBHOOKS ✅

Merchants can set up to 100 webhooks through the Dashboard or API. Before doing this, ‘Flow’ must be enabled in the Client Admin Tool and included in the secret API key’s scopes, as shown in the screenshots below. 

If the merchant experiences a notification issue, our webhook retry system will automatically try again at set intervals, up to eight times.

If all the retries don’t succeed, the merchant can choose to replay the notification attempts for a single event, multiple people, all failed attempts, or for a specific date.RESOURCES ⭐️

| Related Articles |
| --- |
| Merchant facing Articles:   - [Manage Webhooks](https://www.checkout.com/docs/developer-resources/webhooks/manage-webhooks#Add_a_new_workflow)  - [Create a webhook configuration-Dashboard](https://www.checkout.com/docs/business-operations/use-the-dashboard/developers/webhooks#Create_a_webhook_configuration) |

FAQs ⁉️

**Q. What is a webhook signature and why is it important?**

**A. **A webhook signature is a security feature that verifies a notification came from a legitimate source and its content hasn't been altered.

**Q. What happens if a webhook notification fails?**

A. Our system will automatically reattempt to send the notification up to **eight** times at set intervals. If these attempts fail, the merchant can manually replay the notifications via their Dashboard.

**Q. Are webhook events delivered in a specific order?**

A. No. Events are expected to be sent at least once but are **not guaranteed to be in a specific order**. The merchant's system should be configured to handle this lack of order.

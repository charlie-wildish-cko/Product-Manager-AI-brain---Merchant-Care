---
id: 29843969308946
section_id: 22188517144978
title: "Webhook Configuration and Troubleshooting"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29843969308946-Webhook-Configuration-and-Troubleshooting"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T17:56:49Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JVM5TPJQV63X1YGHPGKWQTJN"]
label_names: ["webhooks", "webhook_configuration"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To configure webhooks and when a merchant is experiencing issues with their configuration, this guide is for a Level 1 agent. 

## DESCRIBE THE ISSUE 💬

Merchants need to configure and manage webhook notifications to receive real-time updates about various events, such as a payment being approved or a report being generated. 

They may encounter problems with the initial setup, such as enabling the correct services, or they may experience issues with notifications failing. 

## KEY TAKEAWAYS 🔑

- Webhooks are automated real-time notifications for specific events

- Configuration requires enabling 'Flow' in CAT and on the secret API key's scopes

- Merchants can configure up to 100 webhooks via the Dashboard or API

- The webhook retry mechanism will reattempt failed notifications up to eight times

- The merchant can manually replay failed notifications for a single event, multiple events, all failed attempts, or a specific date

- Webhook events are sent at least once but are not guaranteed to be in a specific order

- The webhook signature is a security measure to verify the notification's authenticity

 

## RESOURCES 📍

| Tools | Related |
| --- | --- |
| Checkout Admin Tool (CAT) API Key Details | [Dashboard Webhook Configuration Guide](https://www.checkout.com/docs/business-operations/use-the-dashboard/developers/webhooks#Create_a_webhook_configuration) [Webhook Event Types](https://www.checkout.com/docs/developer-resources/webhooks/webhook-event-types) |

## PROCESS FOR WEBHOOK CONFIGURATION AND TROUBLESHOOTING 🖊️

This process outlines the steps for configuring webhooks and troubleshooting common issues. It requires in-depth problem-solving, as it involves both system checks and API-level actions.

1. 
**Verify Initial Setup**

  - Confirm that 'Flow' is enabled in both the CAT (Checkout Admin Tool) and the scopes of the merchant's secret API key.

  - This is a critical prerequisite; a merchant cannot disable the 'Flow' service once it is enabled.

2. 
**Configure Webhooks**

  - 
**Via Dashboard**: A merchant can create, enable, disable, or delete a webhook through the Dashboard. Refer to the official documentation for detailed, step-by-step instructions: [Dashboard Webhook Guide](https://www.checkout.com/docs/business-operations/use-the-dashboard/developers/webhooks#Create_a_webhook_configuration).

  - 
**Via API**: For a more automated approach, merchants can use the API to create and manage their webhook workflows. The API allows for actions such as adding, deleting, and updating workflows, actions, and conditions.

3. 
**Troubleshoot Notification Failures**

  - Explain the automated retry mechanism. The system will automatically reattempt delivery at specific intervals for up to eight attempts.

  - If all reattempts fail, the merchant has the option to manually **replay** notifications. This can be done for a single event, multiple events, all failed attempts, or based on a specific date.

## RESOLUTION ⚒️

- Following these steps should result in the successful configuration of webhooks and the resolution of common notification issues. The merchant's system should begin receiving automated notifications for their subscribed events.

**Remediation Steps**

- Ensure the merchant's IP address is not blocking webhook notifications if they have a restricted IP list.

- Check that the webhook signature is correctly configured on the merchant's end to prevent security-related delivery failures. 

- Confirm the merchant's internal system does not rely on the order of webhook events, as they are not guaranteed to be sequential.

**Rollback/Recovery**

- If a new configuration causes issues, the merchant can disable or delete the webhook configuration via the Dashboard or API. 

- For individual failed events, the replay function can be used to re-trigger the notifications.

 

## ESCALATION** ⏫**

- Escalate if the merchant has followed all steps and is still not receiving any webhook notifications, or if the 'Flow' service cannot be enabled in CAT or the API key scopes.

- Required information to include: Provide the merchant's ID, a detailed description of the issue, and the steps taken so far.

-  Stay on the case and monitor for updates. Notify the merchant of the escalation and any progress.

- Follow up with the internal team and chase for updates within 24-48 hours.

## FAQs** ****❓**

What types of events can a merchant subscribe to?

Merchants can subscribe to a wide range of event types, including Accounts, Card Payout, Disputes, Gateway transactions, and many others. A full list of event types is available in the documentation: https://www.checkout.com/docs/developer-resources/webhooks/webhook-event-types.What is a webhook signature and why is it important?

A webhook signature is a security measure used to verify that a webhook notification is from a legitimate source and that its content has not been altered. It is a critical step for ensuring the security of the data being transmitted.How can a merchant manage chargebacks received via webhook?

When a merchant is notified of a dispute event via webhook, they can manage the chargeback through the Dashboard or by using the Dispute API.

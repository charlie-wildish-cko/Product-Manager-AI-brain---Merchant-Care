---
id: 29460311459602
section_id: 22188517144978
title: "How to Verify Webhook Delivery"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29460311459602-How-to-Verify-Webhook-Delivery"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-12-09T09:23:38Z"
permission_group_id: 26838654181266
content_tag_ids: ["01H8EDHC0MTG4YFD7E4B42CE0V", "01JVM5TPJQV63X1YGHPGKWQTJN"]
label_names: ["global", "webhook_troubleshooting", "case_integration", "webhook_troubleshooting_steps", "case_integration_issue_webhook_not_working"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

A merchant reports issues with not receiving webhook notifications for specific events, or that the notifications they do receive are failing.INTRODUCTION TO THE ISSUE 💬

Merchants may report that they are not receiving webhook notifications for specific events, or that the notifications they do receive are failing.

The first step in troubleshooting a webhook issue is to verify if the notification was sent from our system - use Datadog or Dashboard to do this.PROCESS TO VERIFYING WEBHOOK DELIVERY 🖊️ Option 1. Investigation using Datadog 

- Use the [Datadog Webhook search by Payment ID](https://app.datadoghq.eu/logs?query=%40Properties.ApplicationName%3AFlow.Actions.Webhook%20%40Properties.EventSubjectId%3Apay_mct4fr6efz6ezmu37yma7delvu&agg_m=count&agg_m_source=base&agg_q=source&agg_q_source=base&agg_t=count&analyticsOptions=%5B%22bars%22%2C%22dog_classic%22%2Cnull%2Cnull%2C%22value%22%5D&clustering_pattern_field_path=message&cols=service%2C%40http.status_code%2Cenv%2Csource%2C%40Properties.EventType%2C%40Properties.EventId%2C%40Properties.EventSubjectId%2C%40Properties.EntityId%2C%40Properties.WorkflowId%2C%40Properties.ProcessingChannelId%2C%40Properties.WebhookUrl&fromUser=true&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=time%2Cdesc&top_n=10&top_o=top&viz=stream&x_missing=true&from_ts=1754800826749&to_ts=1757392826749&live=true)

- Look for the `Flow.Actions.Webhook` service

- Check the **status code** for the webhook event

  - A **200** status means the webhook was sent and processed correctly

  - A **202** status means the webhook was skipped - this can happen if the transaction is not part of a specific workflow or store

💡 **Tip:** If you see `Flow.Engine.Workflows` but no corresponding `Flow.Actions.Webhook`, it may be a dashboard settings issue

-  If there is no configuration issue, this might be a technical issue that requires further investigation by L2
Option 2. Investigation using Dashboard

This step allows you to check for recent failures directly within the Dashboard

- Log in to the merchant's Dashboard

- Click the [Developers icon](https://dashboard.sandbox.checkout.com/developers) in the top right corner

- Navigate to the **Webhooks** tab

- Select the relevant webhook URL - if there are multiple, choose the one matching the entity and processing channel for the transaction

- You can filter by "failed" status to quickly find any recent issues

- If you already have the webhook configuration ID (wf_xxxx) and the event ID (ect_xxxx), you can [update the URL](https://dashboard.checkout.com/developers/webhooks/wf_l23mbnlaqkpelgzd57itenrvre/events/evt_4qwmvo6uox6ujoshn27edif3vi)

- If the webhook was not sent or is failing, review the Dashboard configuration

- Verify the webhook settings and endpoints in the Dashboard

- Confirm that the endpoint URL starts with `https://` or `http://`

 

- Make sure the correct events for the webhook are selected

- Ensure that the transaction happened on one of the selected processing channels for the webhook

---
id: 22197327868178
section_id: 22188537440658
title: "Troubleshooting Flow"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22197327868178-Troubleshooting-Flow"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:34:10Z"
permission_group_id: 26838654181266
content_tag_ids: ["01H8EDHC0MTG4YFD7E4B42CE0V", "01JCGQCYWP2Z76A49GXQY22K11"]
label_names: ["global", "case_integration", "frames_and_flow_for_payment_integration", "case_integration_issue_flow", "flow"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when:**

Troubleshooting flow payments with an error code of 400, 401, 422, 500, 502

 

## PROCESS FOR TROUBLESHOOTING FLOW 🖊️

Troubleshooting Flow payments involves searching for specific identifiers within Datadog to trace the payment journey from start to finish.  
 

## Step 1: Gather Key Identifiers

Before you begin your search in Datadog, try to obtain at least one of the following identifiers related to the transaction. The more information you have, the easier it will be to find the correct logs.

- 
**Payment Session ID:** [@PaymentSessionId=ps_123](https://app.datadoghq.com/logs?query=%40PaymentSessionId%3Aps_123%20&cols=host%2Cservice&fromUser=true&index=%2A&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1711615031835&to_ts=1711615931835&live=true)

  - The Payment Session ID is attached to all Payment Session logs

  - _external_correlation_id_link is provided in each log for our service this will link out to the downstream service that we call

  - _correlation_id_link is provided in each log for our service and this will link to any service that accepts a correlation ID

- 
**Payment ID:** [@PaymentId=pay_123](https://app.datadoghq.com/logs?query=%40PaymentId%3Apay_123%20&cols=host%2Cservice&fromUser=true&index=%2A&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1711615031835&to_ts=1711615931835&live=true)

- The Payment ID is attached to the following Payment Session logs that interact with that payment

  - Payment Session Submit endpoint (/payment-sessions/:id/submit)

  - Payment Session Redirect endpoint (/payment-sessions/:id/)

  - Payment Session Redirect client-side

  - Flow client-side logs

- 
**Authentication Session ID:** [@SessionId:sid_123](https://app.datadoghq.com/logs?query=%40SessionId%3Asid_123%20&cols=host%2Cservice&fromUser=true&index=%2A&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1711615031835&to_ts=1711615931835&live=true)

  - The Payment ID is attached to the following Payment Session logs that interact with that payment

    - Payment Session Submit endpoint

    - Payment Session Redirect endpoint

    - Payment Session Redirect client-side

- 
**Client ID:  **[@ClientId:cli_123](https://app.datadoghq.com/logs?query=service%3Apayment-session%20%40ClientId%3Acli_123%20&cols=host%2Cservice&fromUser=true&index=%2A&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1711615031835&to_ts=1711615931835&live=true)

- 
**Entity ID:** [@EntityId:ent_123](https://app.datadoghq.com/logs?query=service%3Apayment-session%20%40EntityId%3Aent_123%20&cols=host%2Cservice&fromUser=true&index=%2A&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1711615031835&to_ts=1711615931835&live=true)

## Step 2: Narrow Your Search by Service or Component

If you have a general idea of where the failure occurred, or if you don't have a specific ID, you can search at the service level.

**Search the Payment Session Service:** This service handles the core logic for creating and processing payments.

- 
**General Service Query:** [service:payment-session](https://app.datadoghq.com/logs?query=service%3Apayment-session%20&cols=host%2Cservice&fromUser=true&index=%2A&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1711615031835&to_ts=1711615931835&live=true)

- 
**Specific Function Queries:**

  - Create Payment SessionService: Searchable by [functionname:payment-session-create-payment-session](https://app.datadoghq.com/logs?query=service%3Apayment-session%20functionname%3Apayment-session-create-payment-session%20&agg_q=&agg_q_source=&cols=host%2Cservice&fromUser=true&index=%2A&messageDisplay=inline&refresh_mode=sliding&sort_m=&sort_m_source=&sort_t=&storage=hot&stream_sort=desc&top_n=&top_o=&viz=toplist&x_missing=&from_ts=1711615031835&to_ts=1711615931835&live=true)

  - Get Payment SessionService: Searchable by [functionname:payment-session-get-payment-session](https://app.datadoghq.com/logs?query=service%3Apayment-session%20functionname%3Apayment-session-get-payment-session%20&agg_q=&agg_q_source=&cols=host%2Cservice&fromUser=true&index=%2A&messageDisplay=inline&refresh_mode=sliding&sort_m=&sort_m_source=&sort_t=&storage=hot&stream_sort=desc&top_n=&top_o=&viz=toplist&x_missing=&from_ts=1711615031835&to_ts=1711615931835&live=true)

  - Pay Payment SessionService: Searchable by [functionname:payment-session-pay-payment-session](https://app.datadoghq.com/logs?query=service%3Apayment-session%20functionname%3Apayment-session-pay-payment-session%20&agg_q=&agg_q_source=&cols=host%2Cservice&fromUser=true&index=%2A&messageDisplay=inline&refresh_mode=sliding&sort_m=&sort_m_source=&sort_t=&storage=hot&stream_sort=desc&top_n=&top_o=&viz=stream&x_missing=&from_ts=1711615031835&to_ts=1711615931835&live=true)

  - Redirect Payment SessionService: Searchable by [functionname:payment-session-redirect-payment-session](https://app.datadoghq.com/logs?query=service%3Apayment-session%20functionname%3Apayment-session-redirect-payment-session%20&agg_q=&agg_q_source=&cols=host%2Cservice&fromUser=true&index=%2A&messageDisplay=inline&refresh_mode=sliding&sort_m=&sort_m_source=&sort_t=&storage=hot&stream_sort=desc&top_n=&top_o=&viz=stream&x_missing=&from_ts=1711615031835&to_ts=1711615931835&live=true)

**Search the Edge Gateway:** This component handles initial requests, authentication, and rate limiting before they reach the Payment Session service.

- 
**Query:** [@upstream.cluster:(cluster-payment-sessions](https://app.datadoghq.com/logs?query=service%3Aenvoy%20%40upstream.cluster%3A%28cluster-payment-sessions%29%20&cols=host%2Cservice&fromUser=true&index=%2A&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1711615031835&to_ts=1711615931835&live=true)

**Search by Business-Specific IDs:** You can also find all sessions related to a specific client, entity, or processing channel.

- 
**Client ID Query:** [@ClientId:cli_123](https://app.datadoghq.com/logs?query=service%3Apayment-session%20%40ClientId%3Acli_123%20&cols=host%2Cservice&fromUser=true&index=%2A&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1711615031835&to_ts=1711615931835&live=true)

- 
**Entity ID Query:** [@EntityId:ent_123](https://app.datadoghq.com/logs?query=service%3Apayment-session%20%40EntityId%3Aent_123%20&cols=host%2Cservice&fromUser=true&index=%2A&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1711615031835&to_ts=1711615931835&live=true)

- 
**Processing Channel ID Query:** [@ProcessingChannelId:pc_123<>](https://app.datadoghq.com/logs?query=service%3Apayment-session%20%40ProcessingChannelId%3Apc_123%20&cols=host%2Cservice&fromUser=true&index=%2A&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1711615031835&to_ts=1711615931835&live=true)

## Step 3. Analyze Response Codes

As you review the logs, pay close attention to the HTTP response codes, especially `4xx` (client errors) and `5xx` (server errors). These codes tell you exactly why a request failed.

| **Response Code** | **Message** | **When is this trggered** |
| --- | --- | --- |
| 400 | json_malformed | JSON provided is malformed |
| 400 | None | JSON provided is malformed |
| 401 | None | When SK/PK are not valid |
| 422 | not_onboarded_error | Merchant needs to be onboard into Retool |
| 422 | _invalid or _required | Provided fields are either invalid or required |
| 422 | processing_channel_id_required | The request is missing a Processing Channel ID, which is a required piece of the merchant's configuration |
| 500 | None | An unexpected error occurred within our system |
| 502 | None | A service that we depend on to process the payment is down or unresponsive |

 

## ESCALATION** ⏫**

**When to Escalate:**

- You cannot find the root cause after a thorough investigation

- You identify a `500` error, which points to an internal system failure

- You observe a persistent `502` error, suggesting a prolonged downstream service outage

**What to Include:**

- The Payment Session ID (`ps_...`) and/or Payment ID (`pay_...`).

- A direct link to the Datadog traces you have investigated.

- A brief summary of the steps you have already taken.

- The specific error message or code you found.

**How to Escalate:**

- Post all the required information in the `**#ask-flow**` Slack channel for assistance from the engineering team

 

## Glossaries and Definitions:

For **Key Terms and Definitions** on Integration Issues, please see ****[Integrations Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22198412339346-Integrations-Glossary-Introduction)  

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Integration Issues articles, please see ****[Integrations Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22198326164754-Integrations-Tools-Permissions)

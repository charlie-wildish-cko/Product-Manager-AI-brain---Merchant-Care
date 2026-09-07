---
id: 29015325458706
section_id: 27992533473042
title: "Troubleshooting Gateway http status code 404"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29015325458706-Troubleshooting-Gateway-http-status-code-404"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-30T17:06:50Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K09SJVY23XRXR71VSJXQDKPT", "01K45CSKZGERQD438RYWEHCN4X"]
label_names: ["404 issue", "Gateway"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

Use this guide to troubleshoot why the Gateway returns a **404 Not Found** HTTP status code. This error typically means the requested resource, like a specific payment event- can't be found.

## DESCRIBE THE ISSUE 💬

A merchant receives a 404 Not Found response when they call an API endpoint. This error indicates that an event is missing or the endpoint is incorrect.

## Common Causes of a 404 🔑

A 404 error is almost always due to one of the following issues:

- Missing Event: The event has not yet been written to the Harmonia. This can happen if a request is made too soon after the initial authorization.

- Failed Event Publication: The event failed to publish to the Harmonia/Transactions table.

- Incorrect ID: An incorrect ID (e.g., payment ID, business ID, or processing channel) was used in the API request.

- Invalid Endpoint: The merchant is calling an incorrect or invalid API endpoint.

You can investigate the issue using Datadog and Sherlock.

## TOOLING & RESOURCES📍

| [Datadog](https://app.datadoghq.com/logs?query=&cols=service%2C%40http.status_code&fromUser=true&index=processing&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1749890157609&to_ts=1752482157609&live=true) | Sherlock | Case Examples |
| --- | --- | --- |
| Access granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)  - Select the following:    - Role: Standard    - Reason: Needed for BAU in merchant care | Access granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)   - Select the following:  - **Environment**: Production  -  **Group_Name:** App.Retool.Prod.Gateway-Viewers   - SB  - App.Retool.Sbox.Gateway-Viewers | [Case 48169](https://checkout1360.zendesk.com/agent/tickets/48169) [Case 12933](https://checkout1360.zendesk.com/agent/tickets/13933) |

 

## PROCESS FOR INVESTIGATING 404 RESPONSES🖊️

## Step 1. Search the logs

Search the Gateway API logs in Datadog for the relevant payment ID using the query: `index:processing service:"Gateway API" @http.status_code:404 @http.method:POST @CkoClientId:*`.

Alternatively, you can search more broadly for the payment ID using `@PaymentId:*`.

**💡 Note:** Pay close attention to the logs. If you find placeholder values like **INVALID_ID** or **INVALID_PAYMENT_ID**, the 404 is expected and a simple resolution.

Sample [logs](https://app.datadoghq.eu/logs?query=service%3A%22Gateway%20API%22%20%40http.status_code%3A404%20%40http.method%3APOST%20%40CkoClientId%3Acli_guwslmdyvxjebmnkcya3ay3hry&agg_m=count&agg_m_source=base&agg_t=count&clustering_pattern_field_path=message&cols=host%2Cservice&index=processing&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1756185250722&to_ts=1756199650722&live=true) for cli_guwslmdyvxjebmnkcya3ay3hry 

## Step 2. Identify the root cause

**Verify the Endpoint:** If the payment ID is valid, check if the merchant used the correct endpoint

A common scenario is a merchant trying to call the capture endpoint for an event that hasn't been written yet

[logs](https://app.datadoghq.eu/logs?query=service%3A%22Gateway%20API%22%20%40PaymentId%3A%2A&agg_m=count&agg_m_source=base&agg_t=count&clustering_pattern_field_path=message&cols=host%2Cservice&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1756113108173&to_ts=1756199508173&live=true)

In this example the merchant gets 404 when they call the capture endpoint for pay_htaljv45sx6ejbl2sxf7uhfrme

**Check Event Timeliness:** A 404 often occurs if a capture or void request is made within one second of the initial authorization

Use Sherlock to confirm if the `ChargeAuthorized` event has been written before the subsequent API call.

 

 

**Check for Failed Events:** Look for events that might prevent a successful authorization from being written

 For example, a `ChargeRiskDeclined` event will stop the `ChargeAuthorized` event from being written, leading to a 404 if a merchant tries to capture the payment.

## RESOLUTION ⚒️

Advise the merchant to:

- Use the correct payment ID or endpoint

- Wait for events to be successfully written to Harmonia before retrying the request

- Ensure the payment was successfully authorized before attempting a subsequent action (e.g., capture)

## ESCALATION** ⏫**

If you are unable to resolve the issue or if events need to be fixed or replayed, escalate the issue to the Gateway L3 team. Submit a request through the internal escalation form [here](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277)

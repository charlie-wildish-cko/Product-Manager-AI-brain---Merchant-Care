---
id: 28308417616658
section_id: 27992533473042
title: "Troubleshooting Gateway http status code 422"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/28308417616658-Troubleshooting-Gateway-http-status-code-422"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-01-21T13:47:33Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JWRC3HBBCWV9KD022M3M3WQQ", "01JWRC46WWC378V6E80MQ1J31Q", "01K09SJVY23XRXR71VSJXQDKPT", "01K185R7JWHCEMGHCWZ1TJMSAB"]
label_names: ["L2", "Troubleshooting", "422 error", "validation errors", "Gateway"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

This article helps diagnose and resolve HTTP 422 errors, which indicate invalid or unprocessable data in your payment or API requests.

**Problem/Solution**

Common causes include incorrect or invalid data sent by the merchant in their request. 

## DESCRIBE THE ISSUE 💬

Merchant attempts a payment, capture, refund or void but it fails with 422 and the error is unclear

## KEY TAKEAWAYS 🔑

- The issue is an unclear 422 error on a payment

- Use Datadog to locate the payment and find the error code

- The error is often due to invalid data in the request

- Advise the merchant to correct their request or update configuration

- Escalate to Gateway L3 for further investigation if unable to resolve

## TOOLING**📍**

Click here to see the tools you'll need 

| **Tool** | **Access** |
| --- | --- |
| [Datadog](https://app.datadoghq.com/logs?query=&cols=service%2C%40http.status_code&fromUser=true&index=processing&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1749890157609&to_ts=1752482157609&live=true) | - Access is granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)   - Select the following:    - Role: Standard    - Reason: Needed for BAU in merchant care |
| [Sherlock](https://retoolprod.mgmt.ckotech.co/apps/918d2a72-4c5a-11ec-88dc-53fd2c6a4170/gateway/Sherlock) | - Access is granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)   - Select the following:    - Environment: Production    - Group_Name: `App.Retool.Prod.Gateway-Viewers` |
| [Test App KH](https://retoolsbox.mgmt.ckotech.co/apps/d7995950-b2a7-11ed-97ea-0328566f1311/gateway/Test%20App%20KH) (For Sandbox) | - Access is granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)   - Select the following:    - Environment: Staging    - Permission: Viewer    - Group-Name: `App.Retool.Sbox.Gateway-Editors` |

## PROCESS FOR TROUBLESHOOTING GATEWAY HTTP STATUS CODE 422 🖊️

### Step 1: Locate the Payment in Logs

- Search Datadog logs using `@PaymentId`, `@CorrelationId`, or `@Response.RequestId` (example logs [here](https://app.datadoghq.eu/logs?query=%40PaymentId%3A%2A%20%40CorrelationId%3A%2A%20%40Response.RequestId%3A%2A&agg_m=count&agg_m_source=base&agg_t=count&cols=service%2C%40http.status_code&index=processing&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1753709349879&to_ts=1753710249879&live=true)).

- If no IDs are available, search by merchant name/Client ID (`cli_xxx`) and filter for `@http.status_code:422` (example logs [here](https://app.datadoghq.eu/logs?query=%40http.status_code%3A422%20%40CkoClientId%3Acli_%2A&agg_m=count&agg_m_source=base&agg_t=count&clustering_pattern_field_path=message&cols=service%2C%40http.status_code&index=processing&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1753709597876&to_ts=1753710497876&live=true)).

### Step 2: Analyze the `422` error code

- Look for the `error_code` description in the logs; most are self-explanatory.

- Refer to the provided Confluence doc link [here](https://checkout.atlassian.net/wiki/spaces/GW/pages/5624430773/How+to+Investigate+payment+errors#HTTP-422-Validation-Errors) for common 422 errors and how to troubleshoot.

- Some common examples and investigation steps include:

| **Error code** | **Description** | **Steps** |
| --- | --- | --- |
| `*_scheme_not_configured` | Replaced `payment_method_not_supported `and will specify which scheme is not configured in CAT. | Compare the scheme mentioned (eg. `amex_scheme_not_configured`) with the GW processors configured in CAT under the processing channel the payment was made with. If the above looks fine, check the currency the payment was made with is enabled in CAT under the relevant processor. |
| `processing_channel_id_required` | Error occurs if:   - No processing channel is sent in the payment request and the merchant has multiple processing channels.  - The processing channel id (`pc_xxx`) sent is not configured in CAT  - If it’s GW3 payment, it could be incorrectly routing to GWC as the merchant is sending GWC bearer token. | If it’s a NAS merchant, check CAT to see if they have any processing channels setup by either searching the merchant name or `ClientId/EntityId/ProcessingChannelId`. If it’s missing then I think merchant config team need to set these up as if these are missing then the payment can’t be routed to a processing channel/processor. If it’s there, then check whether they’ve included any processing channel in the payment request, if they haven’t this would be the reason. If they have multiple processing channels they they need to specify one in the payment request. |
| `card_expiry_year_invalid` | Thrown if the expiry year of the card is a past date (i.e expired) or the length exceeds 4 digits (e.g `20255` provided rather than `2025`). | Check the expiry_year field in Sherlock internal events to see what the date is, most likely it’ll be an year in the past and hence not valid. |

## RESOLUTION ⚒️

**1. Ask the merchant to correct their request**

- 
**Ask the merchant to correct their request:** Advise the merchant to adjust the data in their payment request to align with API documentation, expected formats, and business rules. This might involve:

  - Adding missing required fields

  - Correcting data types or values

  - Updating expiry dates

  - Removing invalid characters or excessive lengths

  - Providing accurate account details or instrument IDs

**2. Update Configuration:** If the error stems from an unsupported scheme, currency, or processor configuration, the merchant's settings in the Client Admin Tool (CAT) will need updating. 

- For production issues, contact the Merchant Configuration team via the relevant macro (Transfer > Merchant Configuration > Global).

**3. Communicate with Merchant:** In some cases, we might just need to explain to the merchant how our validation logic works.

## ESCALATION** ⏫**

If additional investigation is required then raise it with Gateway L3 team using Jira.

## RESOURCES** ****⭐**

| **Case Examples** | **Related** |
| --- | --- |
| - [Case 28599](https://checkout1360.zendesk.com/agent/tickets/28599)  - [Case 3328](https://checkout1360.zendesk.com/agent/tickets/3328)  - [Case 63181](https://checkout1360.zendesk.com/agent/tickets/63181) | [Confluence - Investigating common 422 errors](https://checkout.atlassian.net/wiki/spaces/GW/pages/5624430773/How+to+Investigate+payment+errors#HTTP-422-Validation-Errors) |

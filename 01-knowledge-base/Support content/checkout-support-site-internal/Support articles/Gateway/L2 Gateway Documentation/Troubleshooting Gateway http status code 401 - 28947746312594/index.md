---
id: 28947746312594
section_id: 27992533473042
title: "Troubleshooting Gateway http status code 401"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/28947746312594-Troubleshooting-Gateway-http-status-code-401"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-11-14T16:20:54Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K09SJVY23XRXR71VSJXQDKPT", "01K3926V136BR2KRA838DNHZD8"]
label_names: ["troubleshooting_api_keys_common_issues", "L2", "Troubleshooting guide", "API_error", "Gateway", "401"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

Use this article to investigate why the Gateway returns a **401 Unauthorized** HTTP status code. This usually means the API key used in the request is incorrect or invalid.

## DESCRIBE THE ISSUE 💬

A merchant receives a **401 Unauthorized** response when they try to call one of our API endpoints. This is a common error that occurs when an invalid or incorrect API key is used in the request.

 
 

## KEY TAKEAWAYS 🔑

- A 401 error is almost always caused by an issue with the API key.

- The key might be incorrect, inactive, or not have the correct permissions (scopes) for the requested action.

- You can investigate the issue using Datadog , the Dashboard and CAT.

 

## TOOLING📍

| [Datadog](https://app.datadoghq.com/logs?query=&cols=service%2C%40http.status_code&fromUser=true&index=processing&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1749890157609&to_ts=1752482157609&live=true) | [Dashboard](https://retoolprod.mgmt.ckotech.co/apps/918d2a72-4c5a-11ec-88dc-53fd2c6a4170/gateway/Sherlock) | Client Admin Tool  CAT |
| --- | --- | --- |
| Access granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)  - Select the following:    - Role: Standard    - Reason: Needed for BAU in merchant care | Access granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)  - Select the following:    - Environment:Sandbox and Production    - Permission: Super User (both environments) & Super Admin (Only sandbox environment) | Access granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274) Description: New joiner merchant care level 2 team Environment: Sandbox and Production  Permissions: Super User (both environments) - Super Admin ( sandbox only) Reason: To resolve merchant related issues raised through Salesforce |

## PROCESS FOR INVESTIGATING 401 RESPONSES** ** 🖊️

**Step 1: Check the merchant's request in Datadog**

 

- 
Use the **payment ID (e.g., **`**pay_xxx**`**)** from the merchant's request to search the Envoy endpoint logs in Datadog
The following query can help you narrow your search:

@http.status_code:401 service:envoy @ApiKey:sk_* @http.url_objects.PaymentId:*

[logs](https://app.datadoghq.eu/logs?query=%40http.status_code%3A401%20service%3Aenvoy%20%40ApiKey%3Ask_%2A%20%40http.url_objects.PaymentId%3A%2A&agg_m=count&agg_m_source=base&agg_t=count&clustering_pattern_field_path=message&cols=host%2Cservice%2C%40http.status_code%2C%40http.url_details.path%2C%40ApiKey%2C%40http.method&fromUser=true&messageDisplay=inline&refresh_mode=paused&storage=hot&stream_sort=time%2Cdesc&viz=stream&from_ts=1755644400000&to_ts=1755730799999&live=false)

- Locate the API key used in the merchant's request.

Sample payment : pay_chxcxx3ztctefev2cuwd6lowea

 

 

**💡 Note:** If you cannot find the API key in the logs for certain API calls, you'll need to ask the merchant to share the payload and the first few characters of their key to continue the investigation.

 
**Step 2: Identify the root cause**

- Navigate to the merchant's dashboard.

- Go to the **Developers** tab and select **Keys**.

- Compare the API key from the Datadog logs (or the one provided by the merchant) with the keys listed on the merchant's dashboard.

- 
If the key doesn't match or is inactive, this is the root cause.
 

 

 
**Step 3: Verify key scopes**

- If the key is valid and active, the issue may be related to its permissions.

- Confirm that the key has the correct scopes enabled for the specific API call that failed. An incorrect scope will also cause a 401 error.

 

-  Cross-reference the key's permissions by copying the **Key ID** from the dashboard and locating it in the **Client Admin Tool (CAT)** to ensure the processing channel is enabled for the key/scopes.

⚠️ An incorrect scope can also cause a 401 error.
RESOLUTION ⚒️

- 
**Invalid/Inactive Key:** Advise the merchant to use a valid and active API key from their dashboard.

- 
**Incorrect Scopes:** Instruct the merchant to update the scopes for the key in their dashboard to grant the necessary permissions.

## ESCALATION** ⏫**

If you encounter **introspection errors** in the trace logs and are unable to resolve the issue, escalate to the identity and Access Management via ([#ask-iam](https://checkout.slack.com/archives/CS95PMY4A) or Jira group `Identity and Access Management`).

 

## RESOURCES** ****⭐**

**\****Case Examples**

- [Case 68348](https://checkout1360.zendesk.com/agent/tickets/68348)

- [Case 24301](https://checkout1360.zendesk.com/agent/tickets/24301)

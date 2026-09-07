---
id: 26908847197970
section_id: 27060573159058
title: "MPGS Authorization API Service Unavailable (HTTP 503/502)"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/26908847197970-MPGS-Authorization-API-Service-Unavailable-HTTP-503-502"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-07-18T13:47:33Z"
permission_group_id: 26838654181266
content_tag_ids: ["01J7GY9AZ1GE0EJNKJQRMXPAWC", "01JVS26PBA73NGJJETCPWS3SPE", "01JVY9BJTQWCEXNSC42K4F9TY3"]
label_names: ["TPA_acquiring", "card_processing", "TPA_declines"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article:**

If transactions are stuck in the authorization/captures phase or refunds are slow/failed due to the MPGS (Mastercard Payment Gateway Services) Authorization API service being down with HTTP 503 or 502 errors. 

This guide will help you identify the issue using logs, communicate effectively with the affected merchant and follow the correct internal escalation procedure.

 

## DESCRIBE THE ISSUE 💬

Merchants may contact support claiming that transactions are stuck on the authorization phase, or that capture is slow or not occurring at all. This issue is related to the MPGS service being down with HTTP errors, which impacts transaction authorization status.

Specifically, when checking logs, the MPGS Authorization API service might show HTTP status codes such as:

- **503: SERVICE UNAVAILABLE**

- **502: BAD GATEWAY**

When this happens, the MPGS system attempts to retry the request. This is a problem with core payment processing and stops merchants from being able to take payments.

 

## PROCESS  FOR MPGS AUTHORIZATION SERVICE OUTAGES 🖊️

### Diagnosing the issue

### **Step 1: Locate and check the Transaction Logs**

- Use ****[DataDog](https://app.datadoghq.com/dashboard/j2p-zgh-7x5?fromUser=false&refresh_mode=sliding&from_ts=1747895167843&to_ts=1747898767843&live=true) to access the logs for the affected transaction

- Use the `correlation ID` to filter and find the specific transaction log trail

- Check the **MPGS Authorization API** service to identify its HTTP status. You will get the HTTP MPGS service status. Look for status codes like `503: SERVICE UNAVAILABLE` or `502: BAD GATEWAY`.

 

### **Step 2: Identify the HTTP Error**

- Within the logs, locate the API calls made to the **MPGS Authorization API** service, you can also check the transaction status from the MPGS API ([Document](https://checkoutint.zendesk.com/hc/en-us/articles/21991193197970-MPGS-API-Cybersource))

- Examine the HTTP status code returned in the response

- Look for the following error codes, which indicate a service disruption on the MPGS side:

  - `503 Service Unavailable`

  - `502 Bad Gateway`

💡 **Tip: **The logs will also show that our system automatically attempts to retry the request. You should observe three retry attempts following the initial failure. This retry behavior is a key indicator of an external service availability issue.

This issue requires immediate internal escalation to ensure it is tracked and managed at a higher level.

 

## ESCALATION ⏫

- 
**Escalate to the OC Team:** As soon as the MPGS outage is confirmed, raise a case with the **Operations Control (OC) team**.

- 
**Provide Key Information:** In your escalation ticket or message via Slack, include:

  - A clear title: "MPGS Authorization API Down - HTTP 502/503 Errors"

  - The **Correlation ID** of an example transaction

  - A brief description of the merchant impact

  - A screenshot or snippet from the logs showing the `502`/`503` error

The OC team is responsible for formal communication with Mastercard MPGS and for broadcasting updates internally.

 

## RESOLUTION 🛠️

Once you've confirmed that the MPGS Authorization service is down, follow this process for resolution and communication.

- 
**Initial Communication: **Inform the merchant that we have identified a temporary service disruption with our external partner, Mastercard Payment Gateway Services (MPGS), which is impacting transaction processing. Assure them that we are actively monitoring the situation.

- 
**Regular Updates: **Provide consistent follow-ups. Even if there is no new information, confirming that the issue is still being addressed externally helps manage the merchant's expectations.

  
⚠️ Important: Avoid promising a specific resolution time, as the issue is external. Frame it as a "temporary maintenance" or "service availability" issue on the MPGS side.

 

## FAQs ❓

 A merchant is reporting that their transactions are stuck or failing. What is the first thing I should check?

First, ask for a `Correlation ID` for one of the failed transactions. Use this ID to check the transaction logs in DataDog. Look for API calls to the MPGS Authorization service that have returned an HTTP `502` or `503` error. This is the clearest sign of an MPGS outage

 What does an HTTP 503 or 502 error mean for MPGS Authorization API?

It means the MPGS Authorization API service is temporarily unavailable or experiencing a bad gateway error, which can cause transactions to get stuck or fail during authorization.

 What should I tell the merchant?

Inform the merchant that we have identified a temporary service disruption with our partner, Mastercard (MPGS), which is affecting payment authorizations. 

Assure them we are monitoring the situation and will provide regular updates. Avoid giving a specific time for resolution since the issue is external.

 Is our system trying to process the payment again?

Yes. Our system will automatically retry the authorization request three times after the initial failure. You can see these retry attempts in the transaction logs.

 When should I escalate this issue?

You must escalate immediately after confirming the `502` or `503` errors in the logs. This is a critical issue affecting core payment processing.

 Is there anything we can do to fix this ourselves?

No. Because this is an external service outage, we cannot fix it directly. The resolution must come from Mastercard MPGS. Our role is to identify the issue, communicate it clearly to merchants, and escalate internally so the OC team can engage with Mastercard.

 How will we know when the issue is resolved?

The OC team is responsible for communicating with Mastercard and will broadcast updates internally once the service is stable again. Continue to monitor the official communication channels for resolution notifications.

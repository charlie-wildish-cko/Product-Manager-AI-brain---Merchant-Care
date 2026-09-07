---
id: 27460830638610
section_id: 27822398640530
title: "Response Code 20154 - 3D Secure Authentication Required"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/27460830638610-Response-Code-20154-3D-Secure-Authentication-Required"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-19T12:12:17Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JZ88GPVA5D0SPHG3JNW36TE8"]
label_names: ["20154_response_3ds_authentication_required", "L2", "troubleshooting guide", "SOP"]
user_segment_ids: []
archive: false
---

**When to use this article**

To troubleshoot **20154 failures** (3D Secure authentication required), specifically focusing on scenarios where Mastercard returns a **20065 response code** following this requirement.DESCRIBE THE ISSUE 💬

This article provides a comprehensive guide for investigating and resolving transaction failures with response code **20154**, which indicates that [3D Secure (3DS) authentication](https://checkoutint.zendesk.com/hc/en-us/articles/22059017983890-3DS-SCA-Mandate-Guidance) was required but not completed. 

It is useful for agents and merchants troubleshooting declined payments due to **Strong Customer Authentication (SCA)** requirements. In some cases, this may be accompanied by an **Acquirer** response code of **65** from **Mastercard**.Click here for more information about Strong Customer Authentication (SCA) 

**Strong Customer Authentication (SCA)** is a European regulation that requires multi-factor authentication for electronic payments to reduce fraud. It applies to online card transactions where both the business and the cardholder's bank are in the EEA or UK.

SCA requires using two of the following:

- 
**Knowledge**: Something the customer knows (e.g., password).

- 
**Possession**: Something the customer has (e.g., phone).

- 
**Inherence**: Something the customer is (e.g., fingerprint).

**Exemptions** allow merchants to bypass SCA for certain transactions, such as low-value or recurring payments. However, the **customer's bank has the final say** on whether to approve the exemption.

- 
**If the bank rejects an exemption requested during authorisation,** you will receive a **20154 response code**. This means the payment must be retried with 3DS authentication explicitly applied (`"3ds.challenge_indicator"` set to `"challenge_requested"` or `"challenge_requested_mandate"`).

- These exemptions help in providing a seamless customer experience through frictionless authentication when exemptions are approved. If an issuer declines an exemption, the customer is prompted for a challenge flow instead of a straight decline, which generally leads to higher acceptance rates (unless the merchant sets the attempt_n3d value as True).

 KEY TAKEAWAYS 🔑

- Response code **20154** means a transaction needs **3DS** authentication but it was not completed

- The transaction is likely subject to **SCA** regulations because both the merchant and cardholder's banks are in the **EEA** or **UK**

- A rejected **SCA** exemption by the issuing bank is a common cause of this error

- 
**Mastercard** may map the **20154** error to an **Acquirer** response code of **65**

- The merchant must ensure the `attempt_n3d` value is not set to `True` to allow for automatic **3DS** upgrades

- If the transaction continues to fail after a **3DS** challenge, the cardholder should contact their issuing bank

 
PROCESS FOR 20154 INVESTIGATION**  🖊️**
Step 1. Verify the Response Code

- On retool, enter the **Payment ID **for the failed transaction

- Under the **Event type** column, select the `ChargeDeclined` event

- In the associated log, check the response code logs

- You can see the response codes as **20154** and Acquirer response code** 65**

Step 2. Understanding Mastercard's 20065 Mapping for 20154 failures 

- Be aware that **Mastercard** and the issuing bank may map certain underlying issues, such as an **ACS** outage, to the **Acquirer** response code **65** which then correlates to our **20154** code.

_💡_Note: As this mapping is controlled by Mastercard and the issuing bank, we cannot change how this message is received see this [article](https://www.google.com/search?q=link_to_confluence_article) for more detailStep 3. Evaluating Behavior for Optimization 

- Check if the merchant is sending the `attempt_n3d` value as `True` in their transaction requests

- This setting prevents automatic upgrades to **3DS** and should be corrected to allow the payment to be retried with authentication.

- 
Here is how the parameter will look:

- If a transaction still fails after upgrading to 3DS (Challenged), ask the merchant to have the customer contact their issuer.

- Example of a similar situation: ECI 02 indicates the transaction was successfully authenticated by the issuer and is considered secured by 3DS

 
RESOLUTION **🛠️**

- Inform the merchant that the 20154/20065 failure is due to the issuing bank or a temporary ACS outage, often caused by a rejected SCA exemption needing 3DS authentication.

- If the transaction is still failing after a **3DS** challenge, advise the merchant to instruct the cardholder to contact their issuing bank. The cardholder should inquire about the reason for the decline and confirm their card is enabled for **3DS**.

- Explain to the merchant that they must retry the payment with **3DS** explicitly applied by setting the `3ds.challenge_indicator` field to `challenge_requested` or `challenge_requested_mandate`.

 
ESCALATION** ⏫**
Escalate the issue to the **issuer outreach team** if:

- A high volume of **20154** failures from a specific issuer is observed within a short period- as this could indicate a widespread **ACS** outage or a new systemic issue.

- Submit this [Form](https://checkout.atlassian.net/jira/core/projects/IO/form/46) with relevant details

- Stay on the case, monitor for updates, and notify the merchant about the ongoing investigation

 
FAQs** ❓**
 Is this a problem with our payment gateway or the merchant's system?No, similar to 20150, a 20154/20065 error is almost always an issue originating from the **issuing bank's side** or a **transient ACS (Access Control Server) outage**. Our system simply reports the response received from the scheme.  
Unless, there are no authentication attempts despite merchant mentioning attempt_n3d value as false. What does response code 20154 mean?Response code 20154 indicates that **3D Secure (3DS) authentication was required** for the transaction, but it could not be successfully performed or completed.   

## RESOURCES **📍**

| Tools | Case Examples | Related |
| --- | --- | --- |
| [Datadog](https://app.datadoghq.com/logs?query=%403ds2.transaction_status_reason%3A14%20%403ds2.transaction_status%3AN%20%40Properties.Currency%3ASAR%20%40Properties.ClientId%3Acli_nilibeucitcu5c7ql3mnzxqoqm&agg_m=count&agg_m_source=base&agg_q=%40Properties.AcsUrl&agg_q_source=base&agg_t=count&analyticsOptions=%5B%22bars%22%2C%22dog_classic%22%2Cnull%2Cnull%2C%22value%22%5D&clustering_pattern_field_path=message&cols=source%2C%40ActionName%2C%40Properties.ApplicationName%2C%40duration%2C%40GatewayElapsed%2C%40HttpStatusCode%2C%403ds2.transaction_status_reason&event=AwAAAZdkH_o_gFLG7QAAABhBWmRrSF96ZUFBRFpuZUFMMDhQRXRBQWUAAAAkMDE5NzY0MmMtMGYzMC00ZDMzLTljYTgtZDlkYmY1YjE1NDU2AAtufQ&fromUser=true&messageDisplay=inline&panel=%7B%22queryString%22%3A%22%40Properties.AcsUrl%3Awww.securecode.tasheelfinance.com%22%2C%22filters%22%3A%5B%7B%22isClicked%22%3Atrue%2C%22source%22%3A%22log%22%2C%22path%22%3A%22Properties.AcsUrl%22%2C%22value%22%3A%22www.securecode.tasheelfinance.com%22%7D%5D%2C%22queryId%22%3A%22a%22%2C%22timeRange%22%3A%7B%22from%22%3A1748437774000%2C%22to%22%3A1749733774000%2C%22live%22%3Atrue%7D%7D&refresh_mode=sliding&storage=hot&stream_sort=desc&top_n=10&top_o=top&viz=sunburst&x_missing=true&from_ts=1739261883621&to_ts=1740557883621&live=true) [Retool](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights#payment_id=) | [Ticket 63961](https://checkout1360.zendesk.com/agent/tickets/63961) | [Exemptions using a third party authentication provider](https://www.checkout.com/docs/business-operations/ensure-regulatory-compliance/sca-compliance-guide#Exemptions_using_a_third-party_authentication_provider) |

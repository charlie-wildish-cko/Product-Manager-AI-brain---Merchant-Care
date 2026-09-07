---
id: 27139927269266
section_id: 22057285830034
title: "Response Code 20150- Card Not 3DS Enabled"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/27139927269266-Response-Code-20150-Card-Not-3DS-Enabled"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-19T11:34:47Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: ["response_code_20150_card_not_3ds_enabled", "L2", "Troubleshooting", "3DS", "20150"]
user_segment_ids: []
archive: false
---

**When to use this article**

This article guides you through troubleshooting payment failures with **response code 20150**, typically indicating issues with a card's 3D Secure (3DS) enablement or registration.

**20150: Card Not 3D Secure (3DS) Enabled**DESCRIBE THE ISSUE💬

Merchants may face transaction failures with some customers receiving a response code 20150, this is usually a problem with a card's 3D Secure (3DS) enablement or registration. RESOURCES 📍

| Tools | Case Examples | Related |
| --- | --- | --- |
| [Retool](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights#payment_id=) | [Tickets 52766](https://checkout1360.zendesk.com/agent/tickets/52766) | -  [API Response Codes](https://www.checkout.com/docs/developer-resources/codes/api-response-codes) |

 TROUBLESHOOTING RESPONSE CODE 20150 PROCESS**  🖊️ **

This process outlines the steps to diagnose 20150 failures, focusing on identifying the source of the 3DS enablement issue.

1. 
**Access Transaction Details in Retool:** Open [Retool](https://www.google.com/search?q=link_to_retool) and enter the relevant **Payment ID **

2. 
**Navigate to Datadog Logs:** Under the **Associated IDs** tab in Retool, locate and click the **Datadog link** associated with `ChargeRequested`. This will open the relevant logs in Datadog.

3. 
**Examine 3D Secure Session Logs: **In Datadog, search for logs related to `ThreeDs2.Session.API`.

4. 
**Identify the Scheme Response:** Within these logs, look for the **status code 403 (Forbidden)** and examine the detailed **response from the scheme**. This response will confirm that the card was not 3DS-enabled or registered.

 RESOLUTION 🛠️**Expected Result:** Confirming the 20150 failure is due to the card's 3DS enablement status and providing the correct guidance to the customer.**Remediation Steps:**

- 
**Educate the Cardholder:** Explain to the cardholder that their card is not enabled or registered for 3D Secure authentication.

- 
**Contact Issuing Bank:** Instruct the cardholder to **contact their issuing bank directly** to inquire about enabling or registering their card for 3D Secure transactions.

- 
**Alternative Payment Method:** Suggest that the cardholder **try using a different card** that is 3D Secure-enabled.

- 
**Steps to Check Resolution: **The cardholder confirms with their bank that 3DS is enabled, or they complete a transaction with a different 3DS-enabled card.

## **FAQs ❓**

 What does response code 20150 mean?Response code 20150 signifies that the card used for the transaction is either **not enabled for 3D Secure (3DS)** by the issuing bank, or it is **not registered to process 3DS payments**. What's the difference between 20150 and 20151?**20150 (Card Not 3DS Enabled/Registered):** The issue is that the card _itself_ cannot participate in 3DS, often because the issuing bank hasn't enabled 3DS for that specific card or the cardholder hasn't registered for it. The authentication process simply cannot begin or complete due to this fundamental setup. 
**20151 (Cardholder Failed 3DS Authentication):** The card _is_ 3DS enabled, and the authentication process began, but the cardholder either failed to complete the challenge (e.g., wrong password, closed window) or there was a technical issue _during_ the authentication step (e.g., ACS malfunction).

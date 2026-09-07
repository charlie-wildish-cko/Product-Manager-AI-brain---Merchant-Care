---
id: 28298994151442
section_id: 28483258495890
title: "Japan Issuer Request for Stop of Product/Service Shipping (\u914d\u9001\u505c\u6b62\u3001\u8acb\u6c42\u505c\u6b62\uff09"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/28298994151442-Japan-Issuer-Request-for-Stop-of-Product-Service-Shipping-%E9%85%8D%E9%80%81%E5%81%9C%E6%AD%A2-%E8%AB%8B%E6%B1%82%E5%81%9C%E6%AD%A2"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-03-09T05:43:20Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: ["payout", "card_payout", "Stop shipping", "Issuer Request"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article:**

An external card issuer contacts us via email to request that a merchant stop a shipment and refund a transaction. This typically happens for fraudulent transactions where the issuer has liability, meaning they cannot file a formal dispute request.

Please direct any issuers who call the Tokyo office to send an email to Merchant Care.

 

## INTRODUCTION** 💬**

Issuers email us to request that merchants stop shipping goods to avoid the cost of the fraudulent transaction.  The decision to contact the merchant and whether the merchant refunds the money is solely at the discretion of the acquirer and merchant. These requests can originate from any global issuer.

**Exceptions:** Requests may be limited in Japan due to administrative costs and are often denied for instantly delivered digital goods (games, online services)

**Scope:** This process is only for stopping product/service shipping requests, not other disputes

**Key Terms and Definitions:**

- 
**Issuer liability:** Issuer has liability for the transaction, meaning they cannot file a dispute request

- 
**Haisou-teishi (配送停止):** A local Japanese term meaning issuer request for 'stop of product/service shipping'

- 
**Merchant Care Analyst:** Receives requests from issuers and contacts merchants/Account Managers

- 
**Account Manager (AM) :** Contacts merchants on behalf of Merchant Care

**Entry points to procedure:**

1. A purchase is made at a merchant's website by a cardholder.

2. The cardholder raises requests for the cancellation of purchase due to multiple reasons (fraud, unauthorized transaction, product not arrived, etc.) to the issuers.

3. Issuers will send requests for stop of product/service shipping and accordingly make it refunded for the charge to acquirers via email, with transaction details

## PROCESS STEPS 🖊️

**Step 1: Receive and Triage the Issuer Request**

Issuer requests will arrive in the Zendesk dispatch queue since issuers are not registered merchants.

- Acknowledge the incoming request

- If the issuer's name is not registered in Zendesk, ping a team lead to have it added

**Step 2. Locate Transaction**

Use the information provided by the issuer to find the transaction. If you can't locate it, ask the issuer for:

- Truncated PAN (first 6 digits and last 4 digits)

- Amount

- Transaction Date

- ARN/RRN

- Authorization code

**Step 3. Determine who to contact **

Once you locate the transaction, determine the correct contact person:

- For managed merchants, forward the request to the dedicated Account Manager

- For unmanaged (Tier 4) merchants, contact the merchant directly

**Step 4: Contact the Merchant**

The assigned AM or Merchant Care Analyst contacts the merchant with the request.

Message template to contact the AM 

 Message template to contact the AM 

Hi,   
We received a request for stop of product/service shipping from an issuer and the issuer wanted us to contact the merchant to ask whether they would refund it or not.

Please find the transaction detail:   
Payment ID:  
Transaction amount:   
Transaction date:   
ARN:

Kindly reach out to the merchant regarding this. 

**Background:** This request comes from the cardholder's bank for a transaction they believe is fraudulent. Because they hold liability, they cannot file a formal dispute. The decision to refund the transaction is at merchant discretion.Message template to contact the merchant

Hello [Merchant Contact Name],

I hope you're well.

A card issuer has contacted us regarding a potentially fraudulent transaction. They kindly request that you review the order and if possible, stop the shipment and issue a refund for the charge.

**Transaction Details:**

- 
**Payment ID:** [Insert Payment ID]

- 
**Amount:** [Insert Amount]

- 
**Transaction Date:** [Insert Date]

- 
**ARN:** [Insert ARN]

**Background:** This request comes from the cardholder's bank for a transaction they believe is fraudulent. Because they hold liability, they cannot file a formal dispute. The decision to refund the transaction is at your discretion.

Thank you for your consideration.

 

 

| **⚠️ Warning **   If the product is online content (gaming, online service etc.) you can deny the request from the issuer, as the product will be shipped and available for the user immediately after the purchase. Issuers, instead, raise disputes.  <Merchant specific flow>   **Sony- PlayStation(cli_xrvxwxyekvoexcelgtkgva3vmy)**: We ask the issuers/JCB to raise disputes instead, while we should share the transaction list with the merchant(Japan office representatives) as a reference. Sample case: [96075](https://checkout1360.zendesk.com/agent/tickets/96075) 2026/1/29: Correction to the above-> After conversation with Sony local team in Japan, we decided to ask JCB not to raise haisou-teishi for Sony as we can't stop shipping. |
| --- |

**Step 5: Notify the Issuer that Contact Has Been Made**

Reply to the issuer to let them know you have forwarded their request to the merchant. This manages their expectations and confirms the action has been taken.Message template to notifying issuer

**Step 6: Share the Final Result with the Issuer**

Once the merchant provides a final answer (e.g. "refunded," "shipped," "will not refund"), relay the outcome to the issuer to let them know.

 

## RESOLUTION **🛠️**

**If a transaction cannot be located:** Follow up with the issuer for the specific details listed in Step 2

**If the request is for instantly available online content:** Politely deny the request, explaining that the product was delivered instantly at the time of purchase

**If a merchant is unresponsive:** Follow standard merchant follow-up procedures. Inform the issuer if no response is received after a reasonable amount of time

✅ **Best Practice **Ensure that communication templates are used consistently for clarity and efficiency

✅ **For PlayStation Japan**, we've decided to share the impacted transactions with Sony just fyi, regardless of when the transaction is made or which issuers the request came from.

## ESCALATION** ⏫**

If you encounter a problem that cannot be resolved by following this guide, please escalate.

**When to Escalate:**

- You cannot locate the transaction even after receiving additional details from the issuer

- The merchant is unresponsive or unwilling to cooperate

- The scenario is highly complex or unusual and is not covered by this SOP

**How to Escalate:**

- For feedback or questions about this procedure, contact the Procedural Owners: **Satoka Sogame** 

- To report bugs with tools (Zendesk, Looker) follow existing departmental procedures for bug reporting

## FAQs** ❓**

**What is "Issuer liability"?****What is "Haisou-teishi"?**It's a Japanese term for an issuer's request to stop product/service shipping.**Can all requests for stop of shipping be accommodated?** No. Requests for digital goods or services delivered instantly (e.g., games, online content) can be denied because the product is considered "shipped" at the moment of purchase.**Who ultimately decides if a refund is issued?**Whether Checkout contacts its merchant and whether the merchant refunds the money is solely at the discretion of Checkout and the merchant.**How do I locate a transaction if the issuer provides insufficient information?**    

 

## RESOURCES **📍**

 

| **Tools** | **Related** |
| --- | --- |
| [See Ops Tools Library](https://checkout.atlassian.net/wiki/spaces/LL/database/6990364784?atl_f=PAGETREE)  **Zendesk** **Looker** | [Figma Process Flow Visualization](https://www.google.com/url?sa=E&source=gmail&q=https://www.google.com/url?q=https://www.figma.com/board/ePqWEhIQDsCsRvB1W1bZmi/Request-for-stop-of-product%252Fservice-shipping?node-id%3D112-89%26t%3DzsChQtzk6iYs5HXj-4%26sa=D%26source=editors%26ust=1751537362094187%26usg=AOvVaw1hDYjysUPwK-vUAbtLDfYI) |

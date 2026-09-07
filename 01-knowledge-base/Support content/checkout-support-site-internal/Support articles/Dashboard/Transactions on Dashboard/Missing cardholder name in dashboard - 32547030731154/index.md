---
id: 32547030731154
section_id: 26930259534098
title: "Missing cardholder name in dashboard"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/32547030731154-Missing-cardholder-name-in-dashboard"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-01-15T11:54:55Z"
permission_group_id: 26838654181266
content_tag_ids: ["01KEYJ6WTE95KJCTDZAXCCDG0Y"]
label_names: ["missing_cardholder_name"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

Use this guide to diagnose why a merchant cannot see a cardholder's name in their transaction dashboard.**INTRODUCTION TO THE ISSUE 💡**

Merchants may report that the "Cardholder Name" field is blank or missing for specific transactions. This usually occurs even if other payment details (like the masked card number) are visible.

The Cardholder Name value is populated directly from **Gateway events**. If the specific Gateway event does not contain the `CardHolder Name` data at the time of the transaction, the system cannot store it. Consequently, the dashboard cannot display it. This is an issue with the data sent during the transaction, not a display error in the dashboard.

**INVESTIGATION STEPS 👀**  
**Identify the payment:** Locate the payment using the masked card details or transaction screenshot provided by the merchant.

- 
**Check stored data:** Verify if the `CardHolder Name` field is stored for that specific payment ID (e.g., `pay_id`).

- 
**Consult internal teams (if required):** If data appears missing without a clear reason, check with the Dashboard team.

Case Example:[77771](https://checkout1360.zendesk.com/agent/tickets/77771)

- 
**Scenario:** Merchant reported missing name for Visa ending in 4867.

- 
**Payment ID:** `pay_q7vec5xxbuuebhzqk56y3npq7a`

- 
**Findings:** The Dashboard team confirmed no CardHolder Name information was stored for this payment because it was absent from the merchant's Gateway event.

**RESOLUTION STEPS ✅**

You must inform the merchant that the data is missing because it was not captured during the transaction event.

  
**Action for the merchant:** The merchant needs to verify their **integration settings**. If they require the cardholder name for compliance or reconciliation, they must ensure their system is configured to capture and send this field in the Gateway event.**WHAT TO SAY TO THE MERCHANT 🗣️**

I have investigated the transaction ID: [Insert Payment ID} associated with card ending in [Insert Last 4 Digits].

We have confirmed that the cardholder name is not displaying because this information was not present in the Gateway event received for this payment. Our system can only display data that is successfully captured and sent during the transaction.

**Next steps:** If you require the cardholder name for compliance or reconciliation, please check your integration settings. You will need to ensure your configuration is set up to capture and pass the `CardHolder Name` field in the [payment request](https://api-reference.checkout.com/?_gl=1*1eovbl7*_gcl_au*MTg2NjU5NTc3OS4xNzY4NDc1NTAy*_ga*MTM5MTMyNzk2MS4xNzY4NDc1NTAy*_ga_B9CRR7CRMP*czE3Njg0NzU1MDIkbzEkZzEkdDE3Njg0NzU1MDIkajYwJGwwJGgw#operation/requestAPaymentOrPayout). Otherwise, you can update the [instrument](https://api-reference.checkout.com/?_gl=1*1eovbl7*_gcl_au*MTg2NjU5NTc3OS4xNzY4NDc1NTAy*_ga*MTM5MTMyNzk2MS4xNzY4NDc1NTAy*_ga_B9CRR7CRMP*czE3Njg0NzU1MDIkbzEkZzEkdDE3Njg0NzU1MDIkajYwJGwwJGgw#operation/updateInstrument).

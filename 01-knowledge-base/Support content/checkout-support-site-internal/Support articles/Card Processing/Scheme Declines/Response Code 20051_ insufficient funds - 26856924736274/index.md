---
id: 26856924736274
section_id: 26832912736274
title: "Response Code 20051_  insufficient funds"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/26856924736274-Response-Code-20051-insufficient-funds"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-07-18T13:47:32Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JDAEQSFKWRSFX65VT2FN1M16", "01JVS26PBA73NGJJETCPWS3SPE", "01JVS279GQBSZFFGNDNWZ4PRKK", "01JVS27ERFT6CA591PZY4AV4SZ", "01JWGBE8EP91DY3A5P2GHE9Z1N"]
label_names: ["card_processing", "scheme_declines"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

for information on how to handle a common payment decline issue. When a customer's payment fails and shows a response code of 20051, it means the transaction was declined by the customer's bank due to insufficient funds in their account.

**Problem/Symptom:** A merchant reports that a customer's payment has failed.

## DESCRIBE THE ISSUE 💬

Merchants contact us as a transaction receives a response code of 20051, this indicates the transaction was declined by the cardholder's issuing bank due to insufficient funds in the cardholder's account.

You can verify this by checking the logs for the response code within the transaction details. If the value displayed is 51, it confirms the decline is specifically due to insufficient funds.

## PROCESS FOR INSUFFICIENT FUNDS DECLINE🖊️

### Step 1: Access Transaction Logs

- 
** **Using the provided `paymentID`, check the **card processing** logs in ****[Data Dog](https://app.datadoghq.com/dashboard/j2p-zgh-7x5?fromUser=false&refresh_mode=sliding&from_ts=1747895167843&to_ts=1747898767843&live=true), ****[Traffic Insight](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights#payment_id=), or ****[Sherlock](https://retoolprod.mgmt.ckotech.co/apps/918d2a72-4c5a-11ec-88dc-53fd2c6a4170/gateway/Sherlock). 
Step 2: Identify the Response Code

You are looking for a response code of `51`, which confirms the decline is due to insufficient funds. Where you find this code depends on the card used:

**MasterCard:**

- In DataDog, go to the **Mastercard CP API logs**

- You will see the error code displayed as `51` and the response summary as "failed"

**VISA:**

- In DataDog, navigate to **cp-events-relay prod**

- Find `data element`  which is the response code returned from the issuer bank. The value for the `element 39` will be `51`. 

💡 **Tip:** The internal response code `51` corresponds to the external-facing `20051` decline code that merchants might see.**RESOLUTION 🛠️**

### **Step 3: Communicate the Findings to the Merchant**

Inform the merchant that the transaction was declined by the customer's bank due to insufficient funds. Advise them that their customer should:

- Check their bank account balance

- Contact their bank directly for more information

- Try the payment again once they have enough funds, or use a different payment method

## ESCALATION ⏫

- Since the issue is clear from the issuer bank (insufficient funds), **no general escalation is required**. The resolution lies with the cardholder and their bank.

 

## FAQs ❓

Can we override a 20051 decline?

No, these types of declines are issued directly by the cardholder's issuing bank. We do not have control over them and cannot override them.

 What should the cardholder do when they get a 20051 decline?

The cardholder should either check their bank account balance or contact their issuing bank directly to understand why the funds were insufficient. They can then re-attempt the transaction or use an alternative payment method.

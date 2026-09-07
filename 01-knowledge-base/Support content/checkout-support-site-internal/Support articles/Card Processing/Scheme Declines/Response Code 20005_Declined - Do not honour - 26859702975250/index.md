---
id: 26859702975250
section_id: 26832912736274
title: "Response Code 20005_Declined - Do not honour"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/26859702975250-Response-Code-20005-Declined-Do-not-honour"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-07-18T13:47:30Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JVS7PNGACMJ79SK4NFD7XAG3", "01JVS7PZX5B5P36W5YRXK4DNDE", "01JVS7Q4N2D9E599M0J2P62MYP"]
label_names: ["card_processing", "scheme_declines"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

This article explains what response code 20005 means, which indicates a generic issuer-side decline labeled "Do Not Honour." 

## DESCRIBE THE ISSUE 💬

This article explains how to handle transactions that fail with the response code 20005, commonly displayed as "05" in transaction logs. This error indicates a "Do Not Honour" decline, which is a generic refusal from the cardholder's issuing bank. The bank has declined the payment without providing a specific reason.

This guide will help you confirm the source of the decline and provide the correct advice to merchants.

 

## PROCESS FOR RESPONSE CODE 20005 DECLINES🖊️

This process outlines how to identify and respond to "Do Not Honour" declines, differentiating between single occurrences and potential systemic issues.

### Part 1: Handling a Single Decline

For one-off occurrences of the 20005 decline, follow these standard checks for single occurrences

**Check Transaction Logs**

- Use ****[Sherlock](https://retoolprod.mgmt.ckotech.co/apps/918d2a72-4c5a-11ec-88dc-53fd2c6a4170/gateway/Sherlock)** / ******[Traffic Insight](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights#payment_id=) or ****[DataDog](https://app.datadoghq.com/dashboard/j2p-zgh-7x5?fromUser=false&refresh_mode=sliding&from_ts=1747895167843&to_ts=1747898767843&live=true) to access the logs for the declined transaction.

**Confirm the Response Code**

- In the card processing logs (Visa, Mastercard), look for a response value of **05**. This confirms the decline came from the customer's bank.

- Check the `recommendation_code` in the transaction details for guidance on whether to retry the payment. This confirms it is a "Do Not Honour" decline from the issuing bank

 

**Advise the Merchant**

- Inform the merchant that the decline is from the cardholder's bank and not a Checkout.com system error

- Recommend that the merchant advises their customer to contact the issuing bank to understand the reason for the decline

💡 **Tip:** If the recommendation code suggests it, you can inform the merchant that their customer could try the transaction again later.

## Part 2: Investigating Multiple Declines

If a merchant reports several transactions failing with the 20005 response code, a more in-depth investigation is required.

**Gather Information**

Collect the following details for all affected transactions:

- Name of the issuing bank(s)

- Bank Identification Numbers (BINs)

- Specific transaction timestamps and payment IDs

**Look for Trends**

Analyze the merchant's performance report in **Looker** to see if the declines are part of a wider pattern or trend affecting a specific issuer.

**Submit Findings to Outreach Team:**

- Consolidate all collected data

- Submit the findings to the Outreach team using the ****[Outreach Case Submission Form](https://checkout.atlassian.net/jira/core/projects/IO/form/46), povide all context and highlight the recurring pattern

 

## RESOLUTION 🛠️

The expected result is that the agent understands the cause of the decline and provides the correct guidance to the merchant.

**Single Decline Resolution:**

- The merchant should advise the cardholder to reach out to their issuing bank for details on why the transaction was declined.

- The cardholder can then attempt the transaction again (if recommended by the bank or the recommendation code) or use an alternative payment method.

**Multiple Declines  Resolution:**

- Once the issue is escalated to Outreach, they will investigate for possible BIN-level or broader issuer-specific issues.

- Also, this could be escalated with OC team via #Slack channel

## ESCALATION ⏫

If your investigation reveals a high number of "Do Not Honour" declines from the same issuing bank or a specific BIN, the issue requires immediate escalation.

- 
**Primary Escalation:** Use the **Outreach Case Submission Form** in [JIRA](https://checkout.atlassian.net/jira/core/projects/IO/form/46) to provide the Outreach team with all the details you've gathered.

- 
**Urgent Escalation:** For critical or widespread issues, you can also contact the OC (Operations Control) team on their designated Slack channel.

✅ **Best Practice:** When escalating, provide as much detailed information as possible, including affected BINs, transaction examples, and any trend analysis from Looker.

 

## FAQs ❓

What does response code 20005 mean?Response code 20005 ("Do Not Honour") is a generic decline from the cardholder's issuing bank. It means the bank has refused to authorize the payment without giving a specific reason.

 Is a 20005 decline a Checkout.com platform issue?

No, this decline originates directly from the issuing bank, not from our systems.

 What should a merchant do when they see this decline?

The merchant should advise their customer to contact their bank for more information. If the transaction `recommendation_code` is favorable, the customer can try the payment again later or use an alternative payment method.

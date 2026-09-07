---
id: 30665721068562
section_id: 30665400135058
title: "Pay to Bank - Ad-Hoc Use Cases"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/30665721068562-Pay-to-Bank-Ad-Hoc-Use-Cases"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-11-21T07:37:02Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article:**This document outlines the **Standard Operating Procedure (SOP)** for Merchant Care teammates to manage various **Ad-Hoc cases** that do not fall under a dedicated SOP. It covers how to handle queries like Proof of Payment requests, Payout Cancellation requests, route/pricing issues, wrong product queries, and PTB Product-related queries

### INTRODUCTION TO TOPIC 💬

From a Pay to Bank (**PTB**) perspective, these queries may require you to provide specific information or involve Financial Services Tickets that are not within the MC's remit to investigate or take action on. This SOP regroups these different use cases to address them to the greatest extent possible.

**Contact Details for Thunes & LHV:**

****[operations@lhv.com](mailto:operations@lhv.com)  
****[support@thunes.com](mailto:support@thunes.com)** **  
  
Further escalation contacts can be found in this document [here](https://checkout.atlassian.net/wiki/spaces/BP/pages/6965526768/Banking+Partners+-+Contact+details+escalation+paths)

### PROCESS STEPS FOR Ad-Hoc Use Cases

This section details the steps for addressing various ad-hoc use cases.**1. Proof of Payment**

You may receive requests for **Proof of Payment** from the Banking Partner to share with merchants or internal requesters for purposes such as:

- Sub-Entity/Entity Audit

- A merchant claiming there is no fund movement to the beneficiary account even though the transaction was approved

Contact the **Banking Partner** to request the Proof of Payment.**2. Payout Cancellation**

You may receive requests to **cancel a Payout**.

- Check the status on the Banking Partner’s Portal.

- If the Payout was successful on the Banking Partner’s Portal, cancellation is not possible

- If the Payout was dispatched at Checkout.com's end and is still in progress with the Banking Partner, you can try to contact them to see if they can apply a cancellation

**3. Route/Pricing Not Enabled**

For Pay to Bank, there are two main configurations on **CAT** (Configuration and Tools) that are concerned: **Route** and **Pricing**.**Route**

The route is used by Payouts to find an appropriate Bank and Scheme to pay out the requested country and currency

- Ensure the selected route (e.g., GB:GBP) exists.

- If the route is **entity-specific**, you will need to give your entity ID to the Merchant Config team to enable the route for your entity, unless there are domain specific queries around this that would require confirmation from Payout Product Team.(If Global Routs (route profiles available to all entities, you don't need to share entity ID.) 

  
    
    
      NOTE
      
        **CAT → Pricing Profiles → Pay to bank.** You will see
        two options: **Routes** and
        **Pay to bank pricing**.
      
    
  

 **Pricing**

PTB pricing is determined by payout routes, which are defined by the combination of the Payout Scheme, Currency, Country, and Charge Bearer.

**NOTE**: If Route/Pricing not enabled, Internal validation error (Status Code 422) will happen. For errors related to configuration issues, contact the AM or the merchant configuration team to confirm the correct information was provided by the merchant and ultimately configured on **CAT. ****4. Wrong Product Queries**

Internal teams may raise requests to Merchant Care which require Merchant Care to refer to the respective product teams.

**Action:**

1. 
**Escalate** these requests to the concerned product teams via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277), Slack or email 

**Examples of Wrong Product Queries:**

- Configuration issues that require the merchant configuration team to retrieve and configure correct information on **CAT**

- Queries related IP domain - raise via Slack #ask-integrated-platforms

- Transactions that are stuck or rejected in FinCrime - raise via Slack #ask-fincrime

**5. PTB Product-related Queries**

Some queries are **Product-related** and require intervention from the Product Team. These usually come from the Sales/Commercial team requiring confirmation from the Product team.

Email PTB team bankpayouts@checkout.com or post in slack channel #ask-bank-payouts.

**Examples of PTB Product-related Queries:**

- Lack of clarity on currencies, regions, or entity mapping.

- Use cases supported via the Bank Payouts Product.

- Merchants willing to process a new feature that is not yet supported live.

- Confirmation on cut-off times for the different Networks.

### RESOLUTION 🛠️

The expected result is that the ad-hoc query is addressed by following the appropriate procedure and escalating when necessary.

- For configuration issues, ensure the correct information is configured on **CAT**.

- For wrong product queries, the case should be **escalated** to the concerned teams.

- For product-related queries, the case should be assigned to the **PTB Product team**.

ESCALATION ⏫

- 
**Examples of situations requiring escalation:** Wrong Product Queries (under other product teams) , or PTB Product-related Queries (requiring Product Team intervention).

- 
**Required information to include:** Provide specific details or error codes (macro names).

- 
**Instructions for the agent working the case:** Stay on the case, monitor for updates, or notify the merchant as required by the specific scenario.

- 
**How to follow up and when to chase:** The follow-up process should be defined by the escalation instructions.

FAQs ❓**Q: What information is needed when requesting a Proof of Payment from the Banking Partner?**

When contacting the **Banking Partner** to request a **Proof of Payment**, you should provide all relevant transaction details, such as the Payout ID, amount, currency, beneficiary account details, and the reason for the request (e.g., Sub-Entity/Entity Audit or merchant claim of missing funds).**Q: What is the difference between a Route configuration issue and a Pricing configuration issue in CAT?**

- A **Route configuration issue** means the system cannot find an appropriate **Bank and Scheme** to process the payout for the requested country and currency (e.g., GB:GBP is not enabled).

- A **Pricing configuration issue** means the system is missing the defined fee structure (pricing) for a specific payout combination, which is determined by the **Payout Scheme**, **Currency**, **Country**, and **Charge Bearer**.

**Q: When should I raise a request to the PTB Product team?**

You should raise a Slack request to the **PTB Product team** when the query is focused on the **capabilities, features, or limitations** of the Bank Payouts product itself. This includes requests for clarification on:

- Currencies, regions, or entity mapping.

- Use cases supported by Bank Payouts.

- New features that are not yet supported live.

- Confirmation on network **cut-off times**.

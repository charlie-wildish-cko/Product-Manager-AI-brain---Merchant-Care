---
id: 27122561899922
section_id: 27301187322386
title: "Fraud Detection - Rule Builder Help"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/27122561899922-Fraud-Detection-Rule-Builder-Help"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-31T16:10:05Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRPZZM25CJTKMYW0WZXMXX", "01K1TZPHMK6CA4QYZ7R7TTHW8P"]
label_names: ["Fraud Detection", "rule_builder_help"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

Use this article to for general guidance on writing custom fraud rules

**Problem / Symptom**: Common causes include questions on why a fraud rule doesn't work or rule syntax help

## DESCRIBE THE ISSUE 💬

Fraud Detection team frequently receives requests for assistance in writing merchant rules within the Dashboard's Rule Builder to combat fraud.

## KEY TAKEAWAYS 🔑

- Fraud rule-building assistance is for internal teams

- Use the Dashboard Rule Builder and Prism for rules

- Check rule logic for correct syntax and operators

- Some properties are only available for post-auth rules

- Escalate complex rule-building queries to Fraud Detection L3

## TOOLING 📍

### Dashboard - Rule Builder

- Request access to the [Dashboard](https://dashboard.checkout.com/) (for both Production and Sandbox environments) via this [Jira form](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)

- Once you have access, the [rule builder](https://dashboard.checkout.com/fraud-detection/rules) is located under Strategy > Rules > Create rule

### Prism

- Prism is accessible via Okta [here](https://prism.checkout.com/), used to view all global rules

- Access is handled via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274); submit two separate requests using this form for Production and Sandbox access

## PROCESS FOR RULE BUILDER HELP 🖊️

STEP 1: Check what properties are available for rule building

All the public properties are on the rule builder when adding a rule. Alternatively they can be found in the below resources:

- 
[](https://checkout.atlassian.net/wiki/x/owIapwE)[Rule builder properties](https://checkout.atlassian.net/wiki/x/owIapwE)

- 
[](https://checkout.atlassian.net/wiki/spaces/RISK/pages/6392120117)[Velocity in Fraud Detection Rules](https://checkout.atlassian.net/wiki/spaces/RISK/pages/6392120117)

For new properties to be made available, please raise with the Fraud Detection L3 team as a feature requestSTEP 2: Troubleshoot why a rule isn't working as intended

**Verify rule logic:**

- Ensure correct placement of **OR / AND** operators and brackets to prevent unintended behavior

- Confirm correct quoting for strings. For example, when using processing channel IDs:

❌**INCORRECT:**

`:card_issuer_name: = 'NATIONAL BANK OF KUWAIT S.A.K.' AND :processing_channel_id: IN ['pc_hjnh46tq5vmujgriihswxqrvt4, pc_zkcnzro2tv7e5ggp635476oi24']`

✅**CORRECT:**

`(:processing_channel_id: = 'pc_3rsyx4vjozwulgtrkaadlyew3e' or :processing_channel_id: = 'pc_4xb2g65klqmericknyxbvpqcbe') and :bin: IN @tb_eg_blacklisted_bins`

✅**CORRECT:**

`:bin: IN @fp_ph_bin_decline AND :processing_channel_id: IN @fp_ph_pc_s`

**✅CORRECT:**

`:bin: IN @tlb_bin_3_ds AND :processing_channel_id: IN ['pc_upvtetpawy4e3ddx7bsllqzixe', 'pc_ibvrg2cxedau5nt6n3jcrxezui']`

Refer to public documentation [here](https://www.checkout.com/docs/business-operations/prevent-fraud/build-and-test-risk-strategies#Troubleshoot_strategies) for further information on custom rules and troubleshooting

**Check property availability:**

- Properties like **ECI**, **AVS** (Address Verification System) and **CVV** check fields are only available in post-authorisation (post-auth) rules, as these responses are received after the payment authorisation from schemes

 

## RESOLUTION 🛠️

Generally, merchants should self-serve rule-building queries and if they encounter issues we can refer them to public docs below:

- [Create risk rules and lists](https://www.checkout.com/docs/business-operations/prevent-fraud/create-risk-rules-and-lists)

- [Build and test risk strategies](https://www.checkout.com/docs/business-operations/prevent-fraud/build-and-test-risk-strategies)

However, if a merchant insists you can escalate the query to Fraud Detection L3, who may contact @Hen Pekar's team if necessary.

- Fraud Detection team acknowledges the frequent requests for rule assistance and aims to develop a more user-friendly product that simplifies Fraud Detection for merchants

- Currently, merchants are expected to have the expertise to write these rules, though examples are available in the Dashboard's Rule Builder

- @Hen Pekar and her team can provide assistance to larger merchants but their capacity is limited

## ESCALATION ⏫

As mentioned above, if help is really required then raise it with Fraud Detection L3 team using the form [here](https://checkoutsupport.freshservice.com/support/catalog/items/588).

## RESOURCES ⭐

| Case Examples | **Related Articles** |
| --- | --- |
| - [Slack request (1)](https://checkout.slack.com/archives/C01DP70ANJG/p1748869955354069)  - [Case 341989](https://checkoutsupport.freshservice.com/a/tickets/341989?current_tab=details)  - [Case 340818](https://checkoutsupport.freshservice.com/a/tickets/340818?current_tab=details)  - [Case 50285](https://checkout1360.zendesk.com/agent/tickets/50285)  - [Case 340818](https://checkoutsupport.freshservice.com/a/tickets/340818?current_tab=details) | - [Public docs - Fraud Detection Rules](https://www.checkout.com/docs/business-operations/prevent-fraud/understand-fraud-detection#Rules)  - [Confluence - Rule Help](https://checkout.atlassian.net/wiki/spaces/MCL2/pages/7096991788/Rule+Help)  - [L1 SOPs](https://docs.google.com/document/d/1jVeVp9W-k-Sdk0wUpjFtJOGVhkv0JUFQy4YOkk2NPSU/edit)  - [FD Training](https://checkout.atlassian.net/wiki/spaces/MCL2/pages/7136969259/FD+Training) |

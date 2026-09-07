---
id: 27120611282322
section_id: 27301187322386
title: "Fraud Detection - Global Rule Policy"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/27120611282322-Fraud-Detection-Global-Rule-Policy"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-03-31T12:07:08Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRPZZM25CJTKMYW0WZXMXX"]
label_names: ["40101", "global_rules", "L2", "Fraud Detection", "troubleshooting_guide"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

Use this article to investigate why payments were risk declined by our global rule policy or retrieve breakdown of rules.

**Problem / Symptom**: Common causes include payments declined with response codes starting with 4XXX

## DESCRIBE THE ISSUE 💬

- Merchants inquire about risk declines caused by our global rule policy.

- These default risk rules are essential for us as a PSP and acquirer to protect the payment ecosystem, ensure regulatory compliance, and mitigate financial and reputational harm for all parties. They proactively reduce fraud and minimize chargebacks for merchants.

## KEY TAKEAWAYS 🔑

- Risk declines are caused by global rules set by CKO.

- Use Fraud Rule Monitoring to monitor triggered fraud rules.

- Prism is used to view all global rules and strategy.

- Do not disclose global rule logic to merchants.

- To disable non-compliance rules, email [fraud.analytics@checkout.com](mailto:fraud.analytics@checkout.com).

## TOOLING 📍

### Fraud Rule Monitoring

- Accessed via Retool [here](https://retoolprod.mgmt.ckotech.co/apps/0c2c9264-6462-11ef-b138-1b97f0204466/payment-performance/All%20Fraud%20Rule%20monitoring), this tool allows searching by merchant account name to list triggered rules.

- Submit a request via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274), select "Production" for the environment, and request "App.Retool.Prod.Pp-Support-Viewers" permission. 

### Prism

- Prism is accessible via Okta [here](https://prism.checkout.com/), used to view all global rules.

- Access is handled via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274); submit two separate requests using this form for Production and Sandbox access.

## PROCESS FOR GLOBAL RULE POLICY

### STEP 1: Understanding Global Rule Policy (Checkout/Tenet Level)

- Refer to the [Global Rules Dictionary](https://checkout.atlassian.net/wiki/spaces/RA/pages/6092587152) for a comprehensive overview of global policy rules, including definitions, implementation, and effectiveness. Escalate undocumented rules to Fraud Detection L3 for review.

- Global rule policies cover:

  - 
**Compliance:** Regulatory obligations (e.g., currency/country exclusions) for which Fraud Detection has no control.

  - 
**Excessive Retries:** Scheme-mandated rules to reduce payment retries, with fines incurred if disabled.

  - 
**Fraud - Element Velocity:** Rules based on observed payment attempt patterns (e.g., multiple card numbers per email).

  - 
**Fraud - BIN Attacks:** Rules to detect and stop enumeration attacks used by fraudsters to guess card numbers.

### STEP 2: Login to Retool - Fraud Rule Monitoring [here](https://retoolprod.mgmt.ckotech.co/apps/0c2c9264-6462-11ef-b138-1b97f0204466/payment-performance/All%20Fraud%20Rule%20monitoring)

### STEP 3: Search by Client Name

### STEP 4: Review rule breakdown for a high-level overview

- The tool provides a daily breakdown of triggered rules and their level for the merchant:

  - "cko" or "tenet": Global Policy rule.

  - "client" or "entity": Merchant-written or onboarding rule.

### STEP 5: To check a specific payment, search the Payment Id in Payment lookup

- This payment triggered a CKO global rule (e.g., "Policy Decline Rules" - "Prohibited countries") and decision was to decline.

- To understand the rule logic, consult the [Global Rules Dictionary](https://checkout.atlassian.net/wiki/spaces/RA/pages/6092587152) (e.g., "Prohibited countries" under "Compliance"). Global rule logic should not be disclosed to merchants.

### STEP 6: To check all global rules and where it sits in the risk strategy, login to [Prism](https://prism.checkout.com/)

- Choose Account name: CKO and navigate to Risk Strategy section to view pre/post-auth rules.

 

## RESOLUTION 🛠️

1. For internal users, the resolution is usually explaining the global rule and why it is in place using the global rules dictionary [here](https://checkout.atlassian.net/wiki/spaces/RA/pages/6092587152/Global+Rules+Dictionary). A few examples include:

A few examples include:

- Compliance

This payment was stopped due to our [](https://checkout.atlassian.net/wiki/x/DIAfnwE)[Issuer Block](https://checkout.atlassian.net/wiki/x/DIAfnwE) which is stopping this payment from being processed with sanctioned banks.

- Bin attack

This payment was stopped due to it being detected in a [BIN attack](https://checkout.atlassian.net/wiki/spaces/RA/pages/7096893486/CKO+Global+-+BIN+Attack+-+Low+AR?atlOrigin=eyJpIjoiN2ZlNGIzNDJiOTFjNDU2Y2FlMDZhYmZjZDMwNzMwMzIiLCJwIjoiYyJ9), where fraudsters are trying to gather card details.

- AFT

This payment was stopped due to the AFT restrictions from the card schemes. [More details](https://checkout.atlassian.net/wiki/spaces/PAR/pages/6936920393)

2. For non-internal users (i.e merchants), we can tell them it triggered our global risk rules but we won’t be able to share the exact rule logic due to compliance reasons and the sensitive nature of our global rules.

3. To disable a non-compliance global risk rule (eg. whitelisting an email to bypass global rules), email [fraud.analytics@checkout.com](mailto:fraud.analytics@checkout.com) which is owned by @Hen Pekar and team.

4. Onboarding rules (set at a merchant level and being phased out) are handled by the Risk Monitoring team and not Fraud Detection, ask on [#ask-risk-monitoring](https://checkout.enterprise.slack.com/archives/C0A5E6UCC10) slack channel.

## ESCALATION ⏫

- L1: If additional context or investigation is required then raise it with Merchant Care L2 team using the transfer macro (L1>L2>Fraud Detection).

- L2: If additional context or investigation is required then raise it with Fraud Detection L3 team using the form [here](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277).

- If the merchant wants to exclude certain global rules (except compliance global rules since we can't exclude these), email [fraud.analytics@checkout.com](mailto:fraud.analytics@checkout.com).

## RESOURCES** ****⭐**

| **Case Examples** | **Related** |
| --- | --- |
| - [Case 57106](https://checkout1360.zendesk.com/agent/tickets/57106)  - [Case 56520](https://checkout1360.zendesk.com/agent/tickets/56520)  - [Case 54665](https://checkout1360.zendesk.com/agent/tickets/54665)  - [Case 87230](https://checkout1360.zendesk.com/agent/tickets/87230) | - [ZD Article - What happened to a transaction](https://checkout1360.zendesk.com/knowledge/articles/27117447356818/en-us?brand_id=13973479171346)  - [Confluence Article - Global Rule Policy](https://checkout.atlassian.net/wiki/spaces/MCL2/pages/7096893443/Global+Rule+Policy)  - [L1 SOPs](https://docs.google.com/document/d/1jVeVp9W-k-Sdk0wUpjFtJOGVhkv0JUFQy4YOkk2NPSU/edit)  - [FD Training](https://checkout.atlassian.net/wiki/spaces/MCL2/pages/7136969259/FD+Training) |

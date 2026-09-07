---
id: 27117447356818
section_id: 27301187322386
title: "Investigating why a risk rule was triggered"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/27117447356818-Investigating-why-a-risk-rule-was-triggered"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-03-03T16:42:12Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRPZZM25CJTKMYW0WZXMXX"]
label_names: ["40101", "L2", "Fraud Detection", "troubleshooting_guide", "risk_declines"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

Use this article to investigate why a payment was risk rule was triggered or declined.

**Problem / Symptom**: Common causes include payments declined with response codes starting with 4XXX

## DESCRIBE THE ISSUE** 💬**

- Merchants inquire about risk-declined transactions, triggered rules and impacted transactions

- Fraud Detection L3 is developing internal tools to address these inquiries, which will eventually be extended to merchants

## KEY TAKEAWAYS 🔑

- Fraud Insights is the main tool for investigating risk declines

- Use the payment ID to identify the triggered rule in Fraud Insights

- The "Fraud Detection" section in Fraud Insights details the risk assessment outcome

- You can find related transactions that triggered the same rule in Fraud Insights

- Resolution depends on whether the rule is a client- or global-level decline

## TOOLING** 📍**

| **Tool** | **Access** |
| --- | --- |
| [Fraud Insights](https://retoolprod.mgmt.ckotech.co/apps/20f28652-bba4-11ee-9da9-b33a06c78849/payment-performance-shared-support/Fraud%20Insights#payment_id=) | - Access is granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)   - Select the following:    - Application: Retool Prod    - Environments: App.Retool.Prod.Pp-Internal-Viewers     - Roles: ViewOnly |
| [Fraud Rule Monitoring](https://retoolprod.mgmt.ckotech.co/apps/0c2c9264-6462-11ef-b138-1b97f0204466/payment-performance-shared-support/All%20Fraud%20Rule%20monitoring) | - Access is granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)   - Select the following:    - Application: Retool Prod    - Environments: App.Retool.Prod.Pp-Internal-Viewers     - Roles: ViewOnly |
| [Prism (Okta)](https://prism.checkout.com/) | - Access is granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)   - Select the following:    - Application: Prism    - Environments: Production/Sandbox (raise 2 separate requests)    - Roles: ViewOnly |

## PROCESS FOR INVESTIGATING RISK RULES

## Step 1: Login to Retool - Fraud Insights [here](https://retoolprod.mgmt.ckotech.co/apps/20f28652-bba4-11ee-9da9-b33a06c78849/payment-performance-shared-support/Fraud%20Insights#payment_id=)

## Step 2: Enter the Payment id (i.e pay_xxx) into the search bar

## Step 3: Identify the triggered rule

- Navigate to the "Fraud Detection" section. This section details the risk assessment, clarifying the payment outcome.

- 
The system runs CKO, Merchant, and Sub-merchant rules concurrently but `Resulting assessment` shows which rule triggered that led to the payment outcome (in the example screenshot below it was a merchant decline rule which led to the payment risk decline).

  - **CKO/Tenet (Global):** Rules applied to all traffic (e.g. prohibited countries).

  - **Client/Entity (Merchant/Sub-merchant):** Rules set specifically by the merchant for their own account.

- In this case the `Resulting assessment` was parent_merchant which means the rule that led to the risk decline was a merchant rule.

**NOTE**

**The Restrictive Hierarchy:** If multiple rules trigger, the system applies the most restrictive decision in the following order: **Decline > 3D Secure > Frictionless > Try Exemptions / Pass.**

## Step 4: Analyse the Triggered Rule

Based on the resulting assessment identified in Step 3, investigate the specific logic.

**1. If Merchant/Sub-merchant Level**

- 
View the exact rule name in the **Fraud Detection** tab.

- You can also access full assessment details in the dashboard. Select the merchant, search for the payment, and click "View full assessment" (e.g., `https://dashboard.checkout.com/payments/all-payments/payment/pay_wzqmypibajlitiveol5sljfyy4`). This provides a detailed rule breakdown.

- 

  - For example, `pay_wzqmypibajlitiveol5sljfyy4` was risk-declined due to a relative velocity `card_number_per_email` rule: the same email for different cards were used over 3 times within 1 hour (`relative_velocity(card_number_per_email, 24h, attempted) > 3`).

 
**2. If Global Level**

  - 
View the exact global rule name in the **Fraud Detection** tab.

  - 
You can also find the rule in dashboard in the payment details page but it's not as detailed, it will give the generic global decline reason. 

  - 
To find the rule logic and more information, reference the ****[Global Rules Dictionary](https://checkout.atlassian.net/wiki/spaces/RA/pages/6092587152/Global+Rules+Dictionary) or ****[Prism](https://prism.checkout.com/) (Account CKO) to find the specific CKO policy (e.g. Card Block- Excessive Retries).

## Step 5: Find related transactions that triggered the same rule (if applicable)

- Go to the "Transactions Patterns and Labeling" section. The rule description will indicate the property (e.g., email, card, device, cardholder) that led to the outcome.

- Select the time period and relevant fields (e.g., Client ID and customer email) to find associated payments which help explain why the rule triggered. The results can be downloaded and shared.

## RESOLUTION** 🛠️**

There are a few paths to resolution as listed below.1. Client (merchant) or Entity (Sub-merchant) level rules

- Explain to them the exact rule that led to the decline or rule being triggered, see example response below for risk declines:

Internal user:
The payment was risk declined by a merchant level rule {{insert rule group name here}} where the merchant can login to the dashboard and see the details of what has happened to the transaction, the rule and modify as they seem fit.
Merchant:
The payment was risk declined by your rule {{insert rule group name here}} due to the payment meeting the rule criteria. For more details you can login to the dashboard and see the details of what has happened to the transaction, the rule and modify them if necessary.
2. Global Policy level declines 

- Explain to them which global rule led to the decline (more details can be found in [](https://checkout1360.zendesk.com/knowledge/articles/27120611282322/en-us?brand_id=13973479171346)[Global Rule Policy](https://checkoutint.zendesk.com/hc/en-us/articles/27120611282322-Fraud-Detection-Global-Rule-Policy) article):

Internal user:
This payment was risk declined by our global risk policy that helps protect checkout from high levels of fraud. It’s blocked by {{insert rule group name here}} and the specific rule of {{insert rule name here}}. Here is a link to the [global rules dictionary](https://checkout.atlassian.net/wiki/spaces/RA/pages/6092587152/Global+Rules+Dictionary) where the rules have been detailed.
Merchant:
This payment was risk declined by our global risk policy {{insert rule group name here}} that helps protect checkout from high levels of fraud and created based on scheme mandates. We're unfortunately unable to disclose further details due to the sensitivity of our global rules but the payments were declined since they met the rule criteria.
3. If they want to know why a rule wasn't triggered, it could be the case the rule was created after the payment was made or a misunderstanding in how our rules work so we can explain this to them.4. If they want a global rule to be excluded then we should email [fraud.analytics@checkout.com](mailto:fraud.analytics@checkout.com) to advise. 

## ESCALATION** ⏫**

- L1: If additional context or investigation is required then raise it with Merchant Care L2 team using the transfer macro (L1>L2>Fraud Detection).

- L2:  If additional context or investigation is required then raise it with Fraud Detection L3 team using the form [here](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277).

- If they want to exclude certain global rules or whitelist attributes (eg. email), contact Fraud Analytics via email [fraud.analytics@checkout.com](mailto:fraud.analytics@checkout.com).

## RESOURCES** ****⭐**

 

| **Case Examples** | **Related** |
| --- | --- |
| - [Case 41718](https://checkout1360.zendesk.com/agent/tickets/41718)  - [Case 57106](https://checkout1360.zendesk.com/agent/tickets/57106)  - [Case 58907](https://checkout1360.zendesk.com/agent/tickets/58907) | - [What happened to a transaction](https://checkout.atlassian.net/wiki/spaces/MCL2/pages/7095648286/What+happened+to+a+transaction)  - [L1 SOPs](https://docs.google.com/document/d/1jVeVp9W-k-Sdk0wUpjFtJOGVhkv0JUFQy4YOkk2NPSU/edit)  - [FD Training](https://checkout.atlassian.net/wiki/spaces/MCL2/pages/7136969259/FD+Training) |

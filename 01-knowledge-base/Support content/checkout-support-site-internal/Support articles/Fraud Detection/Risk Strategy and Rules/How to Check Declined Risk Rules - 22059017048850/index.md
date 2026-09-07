---
id: 22059017048850
section_id: 28496987889682
title: "How to Check Declined Risk Rules"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22059017048850-How-to-Check-Declined-Risk-Rules"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-07T08:33:58Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRPZZM25CJTKMYW0WZXMXX"]
label_names: ["global", "cko_level_decline", "case_fraud_issue_decline_list_risk_rules", "check_declined_rules", "case_fraud_detection", "sanctioned_countries", "sanctions"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

A payment has been declined by a risk rule and you need to support the merchant. INTRODUCTION TO RISK RULES 💬

If a payment is declined by a risk rule, you can identify the rule using the Checkout.com Dashboard or Fraud Insights in Retool. This helps merchants manage fraud by understanding which payments are automatically declined. See the article: [Understanding and using decline lists for fraud detection](https://checkoutint.zendesk.com/hc/en-us/articles/22059028593042-Decline-Lists).

⚠️ All merchants must follow these global rules, which apply only to pay-in transactions:

- Blacklisted attributes include emails, cards and BINs

- Sanctioned countries:

  - Cuba (CU)

  - Iran (IR)

  - North Korea (KP)

  - Sudan (SD)

  - Syria (SY)

- Transactions over USD 10 million are declined

- Transactions in these currencies are blocked: RUB, LBP, KPW, ZWL, ARS (Visa only), GHS, GMD, SYP, SDG, BYN, and HRK

PROCESS TO CHECK RISK RULE DECLINE REASONS 🖊️Option 1. Check a Declined Rule using Dashboard

The easiest way to find out why a risk rule was declined is by checking the dashboard. The merchant can do this as well- please walk them through the steps so they feel comfortable handling it on their own in the future.

1. Locate the merchant account name and search for it on the **Dashboard**

2. Find the transaction using the payment ID and paste it into the search bar under the **Payments** tab; set the correct date range for the transaction

3. In the payment timeline section, all events related to the transaction will be displayed

4. To find the specific reason for the decline, click** view full assessment** next to the risk response code

5. You will be redirected to the **Fraud Detection** tab

6. The specific rule that triggered the risk response code will be highlighted in blue and marked as **TRUE**

7. All other criteria will be highlighted in grey and marked as **FALSE**

Option 2. Check a Declined Rule in Fraud Insights (Retool)

1. Open the payment-performance-shared-support Insights folder

2. Paste the payment ID and click **Query**

3. 
Scroll down to the **fraud detection** section to see which risk rules were triggered to decline the transaction

RESOURCES ⭐️ 

| Tools | Related Articles |
| --- | --- |
| Retool- Fraud insights   -  **Request Retool Access:** [request](https://checkoutsupport.freshservice.com/support/catalog/items/722) here  -  **Environment:** Production  -  **Group name:** [App.Retool.Prod.Pp](http://app.retool.prod.pp)-Support-Viewers   - Merchant Dashboard | - [Overview of fraud detection](https://checkoutint.zendesk.com/hc/en-us/articles/22059041929874-Overview-of-the-Fraud-Detection-Tool)  - [Fraud detection FAQs](https://checkoutint.zendesk.com/hc/en-us/articles/27315752132370)  - [Understanding and using Decline Lists for fraud detection](https://checkoutint.zendesk.com/hc/en-us/articles/22059028593042-Decline-Lists)  - [Why was a payment risk declined?](https://checkoutint.zendesk.com/hc/en-us/articles/27117447356818-Why-was-a-payment-risk-declined) |

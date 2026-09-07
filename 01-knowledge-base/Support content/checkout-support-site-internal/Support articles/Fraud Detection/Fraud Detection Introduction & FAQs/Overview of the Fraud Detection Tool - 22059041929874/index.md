---
id: 22059041929874
section_id: 27310328238098
title: "Overview of the Fraud Detection Tool"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22059041929874-Overview-of-the-Fraud-Detection-Tool"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-30T17:17:12Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRPZZM25CJTKMYW0WZXMXX"]
label_names: ["global", "glossaries_and_introductions", "overview_of_the_fraud_detection_tool", "case_fraud_detection"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

The Fraud Detection Tool is designed to monitor and manage payment processing. Any payment marked with the "risk" attribute as "true" through the CKO Unified Payments API will be evaluated based on the risk assessment rules configured in the Fraud Detection Tool.

Merchant Care Agents have access to the FDT via the Dashboard (which merchants can also access) and the internal Fraud Detection Tool.

These tools are used internally in various situations. For example:

1. 
**Blacklist/Whitelist Requests:**  
If a merchant is unable to blacklist or whitelist specific attributes on their end, we can action these requests through the Fraud Detection Tool.

2. 
**Dashboard for Investigation:**  
The dashboard can be used for investigative purposes such as retrieving payment IDs.

3. 
**CKO-Level Rule Checks:**  
The Fraud Detection Tool can be used to review global rules set at the Checkout (CKO) level. If a transaction is declined due to these CKO-level rules, it will display as a "Checkout Decline" on the merchant's dashboard. 

There are 2 different Fraud Detection Tiers: Fraud Detection (default free option) and Fraud Detection Pro. Please see the [Fraud Detection vs Fraud Detection Pro feature grid page](https://checkout.atlassian.net/wiki/spaces/RISK/pages/5103714798) to view the available features.

## Process Steps

### Accessing the Fraud Detection Tool

**For CKO Internal Users:**

- **Dashboard Access: **
Agents can access Fraud Detection by logging into [https://dashboard.checkout.com/](https://dashboard.checkout.com/) (via Okta) and then navigating to ‘Fraud Detection’.   If you do not have access, please submit a request via [Jira,](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274) specifying the environment and the reason for access.

- **For Fraud Detection Tool Access:**
Agents can access the Fraud Detection Tool via [https://risk.checkout.com/](https://risk.checkout.com/), using their Okta credentials.If you are unable to log in, please contact your manager. **For Merchants:**The Fraud Detection Tool is accessible via the dashboard ([https://dashboard.checkout.com/](https://dashboard.checkout.com/)) at client level.  
 Only the dashboard owner, admins and risk managers can interact with the Fraud Detection tab. Please refer to the [User Permissions documentation](https://www.checkout.com/docs/business-operations/use-the-dashboard/user-permissions) for further details.  **Note**: 

- The Risk SDK is currently disabled for all merchants in the Sandbox environment. If a merchant requires this feature in Sandbox, please inform the Fraud Detection team, and they will enable it as needed via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277) or the **#ask-fraud-detection** slack channel.

### How does Fraud Detection Work?

Every payment request has an authentication and authorisation stage that verifies who is making the request, and whether the payment can be accepted.In Fraud Detection, the merchant can control what happens before and after the authentication and authorisation stage.The technical terms used are:

- Pre-Auth – Before the authentication and authorisation stage.

- Post-Auth – After the authentication and authorisation stage.

### Performance

Under the Performance section under Fraud Detection on the user dashboard, they will be able to view the following information:

- Risk Analytics

- Transaction Journeys

- Decline Rules Performance

 Risk AnalyticsUnder Risk Analytics, we can see Total **Fraud**. This has been further split into 2 main categories namely Visa Fraud & Mastercard Fraud.We can see the total amount declined by pre-auth, the number of transactions and the rate.We can also see the total amount voided post-auth, the number of transactions and the rate.**Note**:

- **The numbers under Risk Analytics refer to the fraud count from the scheme's fraud report (TC40 & SAFE) and are not directly linked to payments.**

- If a Merchant requests more details regarding the figures displayed on the Dashboard, the merchant can self-serve the report on the dashboard.

- For a detailed breakdown of generating reports, please refer to section 6.6.2 Procedure.

 Transaction JourneysThe Dashboard shows the journey of all transactions through a risk assessment.This is segmented into 2 parts; we can view the number of incoming transactions and the incoming amounts.**Transactions:**  
**Amount:****Note**

- The Sankey chart isn't 100% reliable in terms of numbers due to data manipulation that occurs in the backend. So for instance, if a merchant is enquiring about the; ‘Fraud Reported’ figures, you should advise them to refer to the figures provided on the CVS and/or in the risk analytics section. 

  
Decline Rules PerformanceThis section highlights the effectiveness of individual risk rules configured by merchants in blocking transactions, demonstrating the performance of each rule.Example: 

## Glossaries and Definitions:

For **Key Terms and Definitions** on Fraud Detection, please see ****[Fraud Detection Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22059026944914-Fraud-Detection-Glossary-Introduction)  For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Fraud Detection articles, please see ****[Fraud Detection Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22059041810194-Fraud-Detection-Tools-Permissions)

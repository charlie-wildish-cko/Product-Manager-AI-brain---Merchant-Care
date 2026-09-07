---
id: 22059027184146
section_id: 28496987889682
title: "Strategy Builder (Risk Strategy)"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22059027184146-Strategy-Builder-Risk-Strategy"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-16T13:36:13Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRPZZM25CJTKMYW0WZXMXX"]
label_names: ["global", "rules", "lists", "strategy_builder_risk_strategy", "rule_categories", "rule_groups", "auditing", "risk_rules", "case_fraud_detection"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

A Merchant needs to understand why a transaction was declined or how their fraud rules have changed over time.INTRODUCTION TO UNDERSTANDING RISK STRATEGY 💬 

 

Merchants often want to know why a transaction was declined or how their fraud rules have evolved over time. This guide explains how to review a merchant's risk strategy and update these rules when needed.

**'Pre-auth'** and **'post-auth'** are the two key stages in a transaction's lifecycle where merchants can use fraud detection to decide the outcome. The route a transaction follows to reach its outcome is called **routing**. Each stage has its own route, which is based on several data points, including:

- 
**Rules:** The core of a risk strategy. Rules assess a transaction and return a "true" or "false" result, which guides its path.

- 
****[Decline Lists:](https://checkoutint.zendesk.com/hc/en-us/articles/22059028593042-Decline-Lists) Blocks transactions based on specific details, like the card number, IP address, email, or phone number.

- 
**Outcomes:** The final decision, such as declining the transaction or requiring 3D Secure (3DS) verification.

- 
**Process Steps:** The sequence of actions a transaction goes through.
 

Rule Categories in Detail

There are eight different types of Risk Management Categories that merchants can use to configure their fraud strategy.

| **AVS (Address Verification Service)** | Primarily used in the US, Canada, and UK, AVS verifies a cardholder’s billing address against the issuing bank’s records. It applies only to transactions with the billing address, mostly for US and EU credit cards. |
| --- | --- |
| **Decline Risk Management** | Also known as a blocklist, this rule category automatically rejects transactions based on four specific attributes: Card Number, IP Address, Email, and Phone Number. |
| **High-Risk Countries** | Merchants can block transactions from high-fraud countries. Each merchant can customize their list. Transactions from these countries may be declined or need extra verification like 3D Secure (3DS). |
| **Machine Learning (ML) Score** | This machine learning model assigns a risk score from 0 (low risk) to 100 (high risk) for each payment. Merchants must provide the customer's email, IP address, and billing or shipping address to use it. |
| **Mismatch** | These rules trigger an action when details of a transaction do not align, such as a difference between the BIN (Bank Identification Number) country and the cardholder’s IP address. |
| **Threshold** | This rule category allows merchants to set an action based on a transaction’s value and currency. For example, a merchant might set a rule to flag all transactions over 1,000 GBP to manage exposure to high-value fraud. |
| **Velocity** | - Velocity rules automatically trigger actions based on the frequency of transactions with matching attributes over a specific period (e.g. daily, weekly or monthly).    -  **Simple Velocity:** Counts the number of times a specific attribute (e.g. email address) appears within a given timeframe.    -  **Cumulative Velocity:** Tracks the total USD spent for a given attribute instead of the count.    -  **Relative Velocity:** Shows the count of unique attributes linked to another attribute (e.g. number of distinct emails tied to a specific BIN in the last day). |
| **Verified Information** | This checks information like email, billing address, or shipping address against built-in tools in the Dashboard to determine if the provided information is valid or potentially fraudulent, based on the rules configured. |

 RESOURCES 📍

| Tools | Related Articles |
| --- | --- |
| Retool:  - [Prism Audit Logging Tool](https://retoolprod.mgmt.ckotech.co/apps/453a6af2-b759-11ed-8a54-ef2c1f17b154/prism/prism-audit-logging) | -  [Lists section](https://checkoutint.zendesk.com/hc/en-us/sections/22044818478354-Lists)   - [Decline Lists](https://checkoutint.zendesk.com/hc/en-us/articles/22059028593042-Decline-Lists) |

 

AMENDING  A RULE 🖊️

**Check Merchant Permissions:** Determine if the merchant can make the change themselves. The majority of changes can be made by the merchant, but certain rules (such as velocities and blocked countries) are locked.

**⚠️**** Contact the Risk Team:** If the change is locked, create a side conversation in Zendesk and contact `risk@checkout.com` for approval.

**✅ Get Approval:** Wait for the Risk Team's approval. You must have their explicit go-ahead before proceeding.

**🔄 Loop in the Merchant Configuration Team:** Once you have approval, inform the Merchant Configuration team to perform the change.
AUDITING A RULE 🖊️

Merchants may ask about specific rules that were added to their risk strategy, especially if they notice unusual declines. You can help them by using an internal tool or guiding them through their own dashboard.Option 1. Auditing via the Merchant Dashboard

This method helps merchants access their own audit logs directly, guide them through this and educate them so they can self-serve in the future.

**Access User Activity Logs:**

- Instruct the merchant to log into their Dashboard

- Go to **Settings**

- Select **User Activity**

💡 The user activity page displays a list of all user actions, including the timestamp, user details and the nature of the action.

**Export Audit Logs:**

- Merchants can click the **Export** button to download the logs as a CSV file

💡The file will contain detailed information like the date and time of the action, the user, a description of the change and specific details about the modification.Option 2. Auditing via the Internal Tool (Retool)

This method is for internal agents to check changes made to a merchant's fraud strategy.

**Request Access to the Auditing Tool:**

- Go to the Checkout Support portal at [Checkout Support - Access Request](https://checkoutsupport.freshservice.com/support/catalog/items/566)

- Submit a request and specify the following details:

  - 
**Environment:** Production

  - 
**Application Name:** `prism-audit-logging`

**Access the Retool**

- Once approved, access the tool via the following URL: [Prism Audit Logging Tool](https://retoolprod.mgmt.ckotech.co/apps/453a6af2-b759-11ed-8a54-ef2c1f17b154/prism/prism-audit-logging)

- This tool allows you to view logs of all changes made to the Fraud Detection Strategy (FDT)

**Navigate the tool to access information**

- Use the dashboard to see a list of changes, including timestamps, the user who made the changes and specific rule modifications

- Filter the logs by date, user, or specific rules to narrow your search

- Click on a log entry to view detailed information, including the before and after states of the rules

ESCALATION ⬆️

 

**Complex Rule Amendments:** If a merchant's request for a rule amendment is complex or requires extensive collaboration, ensure you have clear communication with both the Risk and Merchant Configuration teams.

**Access Issues:** If you or a merchant encounter issues accessing the auditing tools, submit a support ticket through the Checkout Support portal.FAQs⁉️

 What is the maximum number of rules that can be set?

There is no limit to the number of rules, but the maximum depth of the decision tree is 256. Merchants may encounter size limitations before reaching this limit.

 

 Why can't a merchant change certain rules themselves?Some rules, such as velocities or blocked countries, are locked for security and compliance reasons. This helps ensure that critical risk management strategies are only amended by authorized teams.

 What are Rule Groups?Rule Groups are sets of individual rules that are grouped by a common outcome. At the pre-auth stage, you might have a **Decline Rule Group**, and at the post-auth stage, you might have a **Flag Rule Group**.

##

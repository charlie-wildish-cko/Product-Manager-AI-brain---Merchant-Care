---
id: 22059017117074
section_id: 22044817688082
title: "Transactions Risk Declined - RC 4XXXX"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22059017117074-Transactions-Risk-Declined-RC-4XXXX"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-23T09:22:58Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRPZZM25CJTKMYW0WZXMXX"]
label_names: ["global", "case_fraud_issue_decline_list_risk_rules", "risk_blocked_transactions", "40101", "case_fraud_detection", "transactions_risk_declined", "risk_declined_transaction", "RC_4"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

to determine the **exact rule** that triggered a RC4XXXX response code decline, indicating a transaction was blocked due to risk by the Fraud Detection Tool.

**Problem** - A transaction was declined with the RC4XXXX response code. **Solution** - Identify the specific rule that triggered the risk block using the Dashboard or Retool.

## DESCRIBE THE ISSUE 💬

A payment received a 4XXXX response code, which is a general indicator that the transaction was blocked due to risk by the Fraud Detection Tool. The block is a response from the risk engine based on configured rules. These rules can be configured at three levels:

- 
****[Client-level response codes](https://www.checkout.com/docs/developer-resources/codes/api-response-codes#Client-level_response_codes)**:** The transaction was declined due to a rule configured for your specific account.

- 
****[Entity-level response codes](https://www.checkout.com/docs/developer-resources/codes/api-response-codes#Entity-level_response_codes)**:** The transaction was declined due to a rule configured for your entity.

- 
****[Checkout. com-level response codes](https://www.checkout.com/docs/developer-resources/codes/api-response-codes#Checkout.com-level_response_codes)**:** The transaction was flagged as high risk by our proprietary fraud model.

The issue is that the high-level RC4XXXX code doesn't specify the cause, so in-depth problem-solving is required to locate the exact rule that was triggered.

## KEY TAKEAWAYS 🔑

- The RC**4XXXX response code** means a transaction was blocked by the **Fraud Detection Tool** based on configured risk rules.

- You must locate the **exact rule** that was triggered to understand the specific reason for the decline.

- You can troubleshoot the cause using either the **Dashboard** or **Retool Traffic Insights**.

- On the **Dashboard**, the triggered rule is found by clicking **VIEW FULL ASSESSMENT** in the Payment timeline. The specific triggering rule/expression is highlighted in **blue**.

- In **Retool's Fraud Detection tab**, the specific decline reason is displayed in the **"Rule that led to outcome"** section and confirmed where the **Route** and **Result** are marked as **true**.

## PROCESS FOR IDENTIFYING THE CAUSE OF RC4XXXX 🖊️

## Method 1: Checking via the Dashboard

**Step 1. Locate the Transaction Details**

- Find the relevant merchant account name and search for it on the **Dashboard**.

- Identify the transaction using the **Payment ID**.

- Paste the **Payment ID** into the search field under the **Payments** tab.

- Ensure the **correct date range** is set.

**Step 2. Access the Full Fraud Assessment**

- In the **Payment timeline** section of the transaction details , click the **VIEW FULL ASSESSMENT** hyperlink. This redirects you to the **Fraud Detection** tab.

**Step 3. Identify the Triggered Rule**

- On the **Fraud Detection** tab, the specific rule that triggered the decline will be highlighted in **blue** and marked as '**TRUE**'. Other criteria will be in **grey** and marked '**FALSE**'.

**Step 4. Find the Specific Rule Expression**

- Click on the highlighted rule (e.g., _Decline Rules – Relative Velocity Decline_). A drop-down menu will appear.

- The exact rule **expression** that triggered the RC4XXXX will be highlighted in **blue**.

- The rule expression details indicate the **exact criteria** that were met. For instance, `(relative_velocity(card_number_per_cardholder_name, 7d, attempted) 5)` means the customer attempted more than 5 times with the same card number and name in 7 days.

- To validate the data that violated the rule, check the right-hand side tab titled **Payment details identified by rule expression**.

### **Method 2: Checking via Retool Traffic Insights**

**Step 1. Search the Transaction in Retool**

- 
**Log in** to **Retool**.

- Open the **Traffic Insights** Folder.

- Paste the **Payment ID** into the search field and click **Query**.

**Step 2. View Fraud Detection Details**

- Navigate to the bottom of the page and select the **Fraud Detection** tab from the Navigation bar.

**Step 3. Determine the Cause**

⚠️ Pre-capture rules in traffic insights trigger after authorization, while pre-authentication rules trigger before.

- The first section, **"Pre Authentication,"** will display the **Rule that led to the outcome**, which is the exact reason for the RC4XXXX decline.

- The second section displays all assessments. The **route** (evaluated decline rule) and the **result** leading to the final outcome will be shown[cite: 33]. If both are marked as **true**, this indicates the specific rule that triggered the RC4XXXX block[cite: 34].

- The third section lists the **counts** of the assessments performed, confirming the number of retries or other metrics that violated the allowed limits.

## RESOLUTION ⚒️

Following the steps will result in the identification of the **specific risk rule** (e.g., a velocity rule) and the **exact criteria** (e.g., number of attempts in a period) that triggered the **RC4XXXX** decline.

- 
**Customer Communication:** Inform the merchant/customer of the exact reason (the specific risk rule and criteria) for the block.

- 
**Rule Adjustment (if applicable):** If the rule is a **Client-level** or **Entity-level** rule, the merchant may be able to contact the Risk team to discuss adjusting the rule's criteria if appropriate for their business needs.

- 
**Card-level Blocks:** If the decline is due to a velocity rule (e.g., too many attempted transactions with the same card in a short time), the remediation may be to wait for the time window to reset and/or use a different payment method.

## ESCALATION** ⏫**

**Escalate** if:

- You cannot locate the Payment ID or transaction details in both the Dashboard and Retool.

- The decline reason is unclear or the expected rule information is missing after performing both troubleshooting methods.

- The merchant insists the block is incorrect and you are unable to verify the rule details.

| Use this transfer Macro: L1 > L2 transfer (Fraud Detection) |
| --- |

**Required information to include:**

- 
**Payment ID** and **Merchant Account Name**.

- Screenshots from the **Dashboard** (Full Assessment) and **Retool** (Fraud Detection tab) showing your troubleshooting steps and any relevant output.

- The specific **Rule** and **Rule Expression** you identified as the cause.

RESOURCES ⭐️

| Related Articles |
| --- |
| [Why was a payment risk declined?](https://checkoutint.zendesk.com/hc/en-us/articles/27117447356818-Why-was-a-payment-risk-declined)   [Fraud Detection - Global Rule Policy](https://checkoutint.zendesk.com/hc/en-us/articles/27120611282322-Fraud-Detection-Global-Rule-Policy) |

 

## FAQs** ****❓**

What are the three levels where the risk-blocking rules can be configured?

The rules can be configured at the **Client-level** (for the specific account), **Entity-level** (for the entity), or **Checkout.com-level** (flagged by our proprietary fraud model).What color highlights the specific rule that triggered the decline on the Dashboard?

The specific rule that triggered the decline will be highlighted in **blue** in the Fraud Detection tab of the Dashboard. The exact rule expression within that rule is also highlighted in **blue**.Where can I confirm the metrics that violated the rule when using Retool?

In Retool, the metrics that contributed to violating the rule or limit can be confirmed in the third section of the Fraud Detection tab, which lists all the **counts** of the assessments performed.

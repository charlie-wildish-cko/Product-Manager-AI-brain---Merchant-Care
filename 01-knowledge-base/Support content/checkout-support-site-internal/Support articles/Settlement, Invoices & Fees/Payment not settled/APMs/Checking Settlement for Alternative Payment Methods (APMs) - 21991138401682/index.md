---
id: 21991138401682
section_id: 21991120231954
title: "Checking Settlement for Alternative Payment Methods (APMs)"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991138401682-Checking-Settlement-for-Alternative-Payment-Methods-APMs"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:33:45Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHQKPVKA7XAZRYSRWE7JRH4"]
label_names: ["for_all_apm_transactions_apart_from_giropay_eps_and_sofort", "apms", "case_settlements", "case_settlements_issue_have_i_been_settled_for_this_payment"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To verify if funds for Giropay/EPS, Sofort & iDeal transactions have been received by Checkout.com and what steps to take next.

**Problem/Symptom: **A merchant has contacted us to confirm if they have been settled for an Alternative Payment Method (APM) transaction.INTRODUCTION TO THE ISSUE 💬

Merchants often contact us to check on the settlement status of specific Alternative Payment Method (APM) transactions. These inquiries typically occur when a transaction has been declined or expired in our system, but the merchant has still received the funds.  PROCESS TO CHECK SETTLEMENT FOR AN APM🖊️

## Step 1: Check the Transaction Type in Retool

Before checking for a settlement, you must first determine if the payment is an APM or a Card Scheme payment.

- Insert the Payment ID into Retool and click Query

- Once the query results appear, look at the "Last Acquirer Name" column to identify if the transaction was an APM or a Card Scheme payment

⚠️ Warning: The main query results page in Retool Traffic Insights does not always show which specific APM was used. To find this information, click "View Event Details" to see further Payment Method details.

 

## Step 2: Check for Confirmation of Funds

For Giropay/EPS and Sofort, you can check if we have received the funds.

- Use the APM Schedules - APM Bank Report in Looker and add the available identifiers (Customer Name, Amount)

- Look at the "DebitCredit Mark" column

  - "D" indicates that the refund was successful and funds left Checkout for the customer

  - "C" means the funds are still with CKO

- You can also use the [Transaction Lookup Identifier](https://checkoutinternal.eu.looker.com/looks/11419?toggle=fil&qid=tbmsa8DQgFLk4hEtz4KifG)

- Simply add the Payment ID to the filters, and the transaction's status will be displayed

⚠️**Warning:** If the steps show that CKO has **not** received the funds, inform the merchant that no refund is required

 Step 3: Request a Manual Refund

If the above steps confirm that Checkout has received the funds but the merchant has not, a manual refund may be needed. The process depends on the type of issue:

**If a Reconciliation Break Occurred**

- The payment will show as expired on the Dashboard, but the customer was charged. The APM Reconciliation team will contact the Payments team to request the manual refund

- The APM Reconciliation team will update the [manual refund tracker,](https://docs.google.com/spreadsheets/d/13xCWhxBD-Zmeh9dxnNrek8xCHnpXaHA9snFLPUHUKSc/edit?gid=1723819250#gid=1723819250) where you can check the status too

**If a Technical Issue Occurred**

- An example would be the Dashboard showing a refund, but the cardholder proves they have not received it. In this case, Merchant Care must contact the Treasury Payments team to request the manual refund

- To contact the Payments team, use the relevant regional “Treasury Payments” macro to create a side conversation in Zendesk from your merchant’s ticket

⚠️ After requesting a manual refund, the Merchant Care agent must inform the merchant of the outcome

 RESOURCES ⭐️

| Tools | Related Articles |
| --- | --- |
| **Retool**:   - To determine if a payment is an APM or a Card Scheme payment. **Looker**:   -  **APM Schedules - APM Bank Report**: Used by the APM reconciliation team to check transaction refunds and status.  -    **Transaction Lookup Identifier**: To view a transaction's status. | Link to case handling [here](https://checkout.atlassian.net/wiki/spaces/CHEC/pages/5991727266/Case+Handling+-+SOP#Emailing-internal-partner-teams%3A) |

 

 

## Glossaries and Definitions:

For **Key Terms and Definitions** on Transactions as well as an **introduction into MENA Gateway and non-Gateway merchants**, please see ****[Settlements Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/21991207693458-Settlements-Glossary-Introduction)   

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Transactions articles, please see ****[Settlements Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/21991176789266-Settlements-Tools-Permissions)

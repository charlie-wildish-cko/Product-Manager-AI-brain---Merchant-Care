---
id: 29839059241490
section_id: 29955500085522
title: "Negative Balance Troubleshooting"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29839059241490-Negative-Balance-Troubleshooting"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-30T17:18:37Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JWRC3HBBCWV9KD022M3M3WQQ", "01JWRC46WWC378V6E80MQ1J31Q", "01JXJ52X27J2YZ77SX3SSR7DNX", "01K6G50JA1G6ZVKQ9NQ93A3RXX", "01K6G51YBRXMXEGM7SB6T16MW7"]
label_names: ["L2", "Troubleshooting guide", "Negative Balance"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

Merchants frequently request clarification when their currency account balance turns negative, particularly if the exact date or cause is unclear. This guide provides a clear, step-by-step process to help you:

- Identify when the balance became negative

- Investigate the underlying reasons for the negative balance

## DESCRIBE THE ISSUE 💬

A negative balance occurs when the amount of money withdrawn or spent from an account exceeds the amount of money available in that account. This can happen due to various reasons such as fees, refunds, chargebacks or other transactions that exceed the available balance.

The root cause of a negative balance can vary from case to case. This document is intended as a **generic investigation guide - **it outlines the standard steps and tools to use, but you may need to adapt your approach depending on the specific scenario.

⭐️ Merchant Self Serve Action: [how to add funds via Dashboard](https://www.checkout.com/docs/funds-management/move-funds/add-funds)

 

## KEY TAKEAWAYS 🔑

- 
**No Payout on Negative Balance:** When a merchant’s balance is negative, no payout will occur.

- 
**Settlement vs. Payout:**

  - 
**Settlement:** is the process of calculating and determining the net financial position of a merchant for all cleared transactions over a specific period. This includes accounting for revenue, fees, chargebacks, and other adjustments. The settlement process results in a final amount that is either owed to or by the merchant.

  - 
**Payout:** The actual transfer of funds to the merchant’s bank account, based on the settlement result. Payouts may be consolidated or non-consolidated, depending on merchant configuration.

- 
**Reconciliation:** A control process to confirm all financial transactions are properly recorded by matching internal records with external sources and resolving discrepancies.

 

## RESOURCES 📍

Open to view tool access and case examples

| **Tool** | **Case Examples** |
| --- | --- |
| **Dashboard** Access granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)  Environment:  select the enviroment that you need   - identity.checkout.com - Prod  - identity-sandbox.checkout.com - Sandbox  Permissions:    - Super User (both environments)  - Super Admin ( sandbox only)  Reason: To resolve merchant related issues raised through Zendesk | Ticket [66082](https://checkout1360.zendesk.com/agent/tickets/66082) - discrepancy in the Balance report. Opening does not natch with Closing balance.    Ticket [66112](https://checkout1360.zendesk.com/agent/tickets/66112) Terminated client, balance shol be zero. (Close enought)   Ticket [68126](https://checkout1360.zendesk.com/agent/tickets/68126) Customer own CKO but their balance is negative. Requested breackdown report. Ticket [82115](https://checkout1360.zendesk.com/agent/tickets/82115) Transaction not in payout report |
| **Client Admin tool (CAT)** Access granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)  Environment:  select the enviroment that you need   - Sandbox  - Production  Permissions:    - Super User (both environments)  - Super Admin ( sandbox only)  Team Name  - Merchant Care Reason: To resolve merchant related issues raised through Zendesk |  |
| **Looker (FAR)** Looker access granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)  Financial Action Report (FAR) via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)  Business Case:   - To resolve merchant related issues raised through Zendesk  - |  |
| Retool (Currency Account Balance) Access granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274) Environment:    - Production Group_Name:   - App.Retool.Prod.FundsAvailabilty.Readers |  |

 

 

## PROCESS TO IDENTIFY WHEN BALANCE TURNED NEGATIVE🖊️

### Step 1. Highlight when balance turned negative

You can use two methods: [Retool - Currency Account Balances](https://retoolprod.mgmt.ckotech.co/apps/6840ab28-c4b7-11ec-909b-bf9c18a51b41/techfinance-finlab/Currency%20Account%20Balances) or [NAS Exposure Report](https://checkoutinternal.eu.looker.com/explore/nas_balances/finance_exposure_report?qid=TQsaE6rN4ViLDxMBdmxpy5&toggle=fil), with NAS exposure Report being more effective.

**Option 1 via Retool**

- Login to Retool and search for the currency account

- Find when the balance became negative

**Option 2 via Looker**
Use Looker as the most efficient way to find when the available balance first became negative.  ****[Looker query](https://checkoutinternal.eu.looker.com/explore/nas_balances/finance_exposure_report?qid=UdmmRCk0yRdLUV3HSnsLqw)

**Step 2. Review Transactions for the Relevant Date Range**

- Open the [Financial Action Report](https://checkoutinternal.eu.looker.com/explore/ledger_financial_actions/finance_financial_actions_report?qid=GJvBcMaiPuhhQCwPFuqV4P&toggle=fil) in Looker:

  - Set the date range from when the balance turned negative (e.g.16/02/2025 to 17/02/2025), from the first negative balance date to the desired end date, or as specified by the requester (e.g. in the support ticket)

  - 💡 Note that Looker adds 1 day to the end date, so in our above example use 18/02/2025 instead

  - Filter results by **Currency Account ID** (format: ca_...)

- Generate and download the report

- Filter by the Breakdown type column

Breakdown Types to Include
When filtering the **Breakdown Type** column in the Financial Actions Report, you should include all types that impact the account balance except for "Payout". The main categories are:
List of Breakdown types

- 
**Revenue/Captures**

  - Capture

  - Partial Capture

- 
**Refunds**

  - Refund

  - Partial Refund

- 
**Chargebacks**

  - Chargeback (ADJM)

  - Chargeback (CBRV)

  - Chargeback (RPDW)

  - Chargeback (ABRW)

  - Chargeback (ABRL)

  - Chargeback (ARWS)

  - Chargeback (AUTO)

- 
**Fees**

  - Gateway Fixed Fee

  - Scheme Variable Fee

  - Scheme Fixed Fee

  - Authorization Fixed Fee

  - Void Fixed Fee

  - Card Verification Fixed Fee

  - Refund Fixed Fee

  - Premium Fixed Fee

  - Premium Variable Fee

  - Authentication Fixed Fee

  - Risk Engine Fixed Fee

  - Tiered Pricing Adjustment

  - Client Settlement Fees

- 
**Adjustments**

  - Adjustment

  - Balance (manual corrections)

  - Tax (tax corrections)

  - Client Revenue (settlement corrections)

  - Invoice Settlement

- 
**Top Ups & Funding**

  - Top Up (bank transfer)

  - Operational Funding Reservation

  - Operational Funding Release

- 
**Security Deposits**

  - Security Deposit Reservation

  - Security Deposit Release

- 
**Clearing Failures**

  - Clearing Failed (for both captures and refunds)

- 
**Other**

  - Payout Rejected

  - Payout Returned

**Do not include:**

- Payout

  
Use the Financial Action Holding Amount (Holding Currency) column to calculate totals. In dashboard reports, this is labeled as Holding Currency Amount.

  
**Step 3. Share Findings with the Merchant**

A negative balance can occur due to several reasons, including:

- 
**Chargebacks**: When a customer disputes a transaction, the amount is deducted from the merchant's account, potentially leading to a negative balance if there are insufficient funds.

- 
**Fees**: Various fees such as gateway fees, scheme fees, and authorization fees can accumulate and exceed the available balance.

- 
**Refunds**: Issuing refunds to customers can also result in a negative balance if the refunded amount surpasses the available funds.

- 
**Adjustments**: Manual corrections or adjustments to the account can lead to a negative balance.

- 
**Minimum Billing Fees**: If the revenue generated is below a certain threshold, the difference is charged as a minimum billing fee, which can result in a negative balance.

- 
**Operational Funding**: If operational funding is used to cover payouts and the available balance is insufficient, it can lead to a negative balance.

- 
**Common Causes**:

  - Overcharges, such as inflated scheme fees, can lead to negative balances.

  - Minimum billing fees can also result in negative balances if the revenue is below the threshold set by the service provider.

These are some common scenarios where a negative balance might occur - each case may require specific investigation to determine the exact cause.

- Download the Financial Actions Report:

  - Note: The Dashboard only allows downloads for up to one month at a time.

  - Reports downloaded from Looker are typically not sent directly to customers. If shared, make sure the columns match the Dashboard.

- Add a note explaining what caused the balance to go negative

 

## RESOLUTION ⚒️

- Notify the merchant when the balance turned negative sharing your report

- Explain why the balance went negative

- Guide the merchant on [how to add funds via Dashboard](https://www.checkout.com/docs/funds-management/move-funds/add-funds)

- Found under Business account > Balances > Add funds

 

## ESCALATION** ⏫**

For escalations, first consult with another L2 FE team member. If the issue is still unresolved, escalate the case to the Billing team or the Treasury team using the correct Zendesk macros.   
  

 

## FAQs** ****❓**

What happens if a customer has a negative balance?**No Payout on Negative Balance:** When a merchant’s balance is negative, no payout will occur.How can I tell if the transaction wasn't paid out?In the Financial Action Report (available in Looker or Dashboard), check the **Payout Reference** column. If it's empty, the transaction hasn't been settled to the customer.  
 
How to check current balance in DashboardYou can check in Dashboard under **Businges Account > Balances**  
In this case you can see that this merchant has a negative balance for entity WISE PAYMENTS LIMITED (HK)

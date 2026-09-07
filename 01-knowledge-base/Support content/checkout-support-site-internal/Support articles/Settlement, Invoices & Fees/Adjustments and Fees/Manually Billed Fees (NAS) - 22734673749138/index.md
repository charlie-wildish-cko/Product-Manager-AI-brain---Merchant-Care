---
id: 22734673749138
section_id: 21991135458066
title: "Manually Billed Fees (NAS)"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22734673749138-Manually-Billed-Fees-NAS"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-02-06T12:40:48Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHQKPVKA7XAZRYSRWE7JRH4"]
label_names: ["row", "case_settlements", "case_settlements_issue_transaction_fees", "manually_billed_fees_nas"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

This article explains how to identify and address merchant inquiries regarding specific fee adjustments found in their settlement reports.

**Problem / Symptom:** Merchants may contact support seeking clarification on unexpected "Interchange Fixed Fee" or "Interchange Fixed Fee Tax" adjustments appearing in their daily settlements.

 

### DESCRIBE THE ISSUE 💬

Manually billed adjustments appear as “Adjustments” or “General Adjustments” on the merchant dashboard. A breakdown of the manual adjustments is available in the [Cost of Sales - Async](https://checkoutinternal.eu.looker.com/explore/oracle_prod/async_billing_fee_report?qid=40KiPVYjbObJruL6U4H8mr&origin_space=1797&toggle=fil) for NAS merchants.

A merchant has requested clarification regarding specific **adjustment IDs **listed in their settlement. The adjustments in question are categorized may be **Interchange Fixed Fees** and associated taxes, which impact the total payout amount for a specific period.

 

### RESOURCES 📍

| **Case Examples** | **Related** |
| --- | --- |
| [Zendesk Ticket](https://checkout1360.zendesk.com/agent/tickets/105860) | **Merchant Care Guidelines**: Handling All Tier settlement queries. **Fee Structure Documentation**: Internal guide on interchange fees. |

## PROCESS FOR INVESTIGATING ADJUSTMENTS 🖋️

Follow these steps to diagnose and explain settlement adjustments to a merchant:

### Step 1. Identify the Adjustment Details in the merchant request.

- 
Locate the **Adjustment ID** (e.g., `adj_nfecd4t2xxxxxxxxxwq36u`) and the **Payout ID** (e.g., `000000034D3X`) provided in the merchant's request. (The payout ID may not be available in the merchant’s request; however, the adjustment ID, Entity or Client ID is required for Looker).
 

### Step 2. Edit the input field on LOOKER report

- Open [Cost of Sales - Async looker report](https://checkoutinternal.eu.looker.com/explore/oracle_prod/async_billing_fee_report?qid=3MXPkSgyeFfnojg1kwxrIi&origin_space=1797&toggle=fil)

- 
Past the adjustment id in **Action Group Id**

- 
Update the date for which you are troubleshooting. 
(a) If you have a specified date from the merchant, add the date directly.
(b) if you do not have a specified date from the merchant, select past 6 months.
 
For example below ; I am searching for any adjustment id made on or after 01 January 2026
 

- 
Add the client id in the field **Client Id**

- Run the looker report

 

### Step 3. Consult the report

- The [Cost of Sales - Async looker report](https://checkoutinternal.eu.looker.com/explore/oracle_prod/async_billing_fee_report?qid=3MXPkSgyeFfnojg1kwxrIi&origin_space=1797&toggle=fil) has a specific field which give the description of the manual adjustment.

- This field is called the **Async Billing Fee report External Descriptor**.

 

- This description is unavailable in financial actions reports.

- Inform the merchant of this description to clarify on the manual scheme fee adjustment.
  
💡If the adjustment is not part of Cost of Sales, use this Looker for further investigation. The Looker lists the relevant adjustments.  
  
[Financial Actions Report looker](https://checkoutinternal.eu.looker.com/explore/ledger_financial_actions/finance_financial_actions_report?qid=lgN4oB6nKQjUj8jl72tX9P&toggle=fil)

## ESCALATION ⬆️

- **When to Escalate**: If the merchant disputes the reason provided from the looker report, use the macro template to escalate to Cost of Sales team.

- **Required Info**: The adjustment id and the result of the [Cost of Sales - Async looker report](https://checkoutinternal.eu.looker.com/explore/oracle_prod/async_billing_fee_report?qid=3MXPkSgyeFfnojg1kwxrIi&origin_space=1797&toggle=fil) 

## FAQs ❓

**How do Visa and Mastercard invoice Checkout.com?** The fees you see are charged directly by Visa and Mastercard to Checkout.com as the acquirer. These are known as **Non-Transactional fees** that cover services like security, network access, and authentication, which are not controlled by Checkout.com.**Why can't I see a transaction-by-transaction breakdown for these fees?** Visa and Mastercard send us a single, consolidated monthly invoice without providing a transaction-by-transaction breakdown. They charge a total amount for all our merchants combined. Because of this, we cannot provide a report showing which specific transaction corresponds to which specific fee. This is a standard process across the entire payments industry applicable to all acquirers.**What is the "Interchange Fixed Fee Tax"?** In certain billing regions, such as **MENA**, local tax regulations require that taxes be applied to the fixed service fees charged by card schemes.

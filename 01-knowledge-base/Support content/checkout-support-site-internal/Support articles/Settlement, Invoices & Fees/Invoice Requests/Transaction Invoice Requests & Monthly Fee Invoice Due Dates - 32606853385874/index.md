---
id: 32606853385874
section_id: 21991159435026
title: "Transaction Invoice Requests & Monthly Fee Invoice Due Dates"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/32606853385874-Transaction-Invoice-Requests-Monthly-Fee-Invoice-Due-Dates"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-02-04T10:23:29Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K22NYQP6QBETF4NRGEXJXKBA", "01KF3XY87GCTWSMSYX7YE5RT1P"]
label_names: ["L2", "Troubleshooting guide"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

When a merchant requests an invoice for a specific transaction or Order ID, or if a Gross Merchant asks about the due date for their monthly fee invoice.

**Problem / Symptom**

The merchant is mistakenly asking Checkout.com for a consumer-facing invoice, or a Gross merchant is unsure when they need to pay their service fees. Clarify that Checkout.com does not generate invoices for individual transactions. For Gross merchants asking about fee payments, refer them to their contract for the specific due date (e.g. within 14 days).

## DESCRIBE THE ISSUE 💬

There are two common invoice-related queries:

1. **Transaction Invoices:** Merchants often mistake the payment processor for the seller and ask us for an invoice for a specific order. We do not provide these; the merchant must generate them.

2. **Gross Merchant Fees:** Unlike "Net" merchants (where fees are deducted automatically), "Gross" merchants receive the full settlement and must pay their fees separately via invoice. These merchants often ask **when** this invoice is due.

 
 

## KEY TAKEAWAYS 🔑

- 
**No Transaction Invoices:** Checkout.com does _not_ generate invoices for individual transactions or orders.

- 
**Merchant:** The merchant generates the invoice for the goods/services sold via their own website or platform.

- 
**Monthly Fee Invoice:** The invoice we provide is the Monthly Fee** Invoice**, generated on the **1st **of the following month (covering service fees).

- 
**Gross Merchants**: Merchants on the Gross settlement model must pay their invoices manually. The due date is stated in their contract.

- 
**Alternative Identifiers:** For single transactions, provide the **Payment ID** or **Merchant Reference** to help them reconcile the transaction.

## TOOLING 📍

Click here to see the tools needed

| Tool | Access |
| --- | --- |
| [Dashboard (NAS)](https://dashboard.checkout.com/reports/all-reports) | - If you do not already have access to the Dashboard, submit a ticket to IT via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)   - Submit a request through this form, selecting "identity.checkout.com - Prod" for the environment |
| [Looker](https://checkoutinternal.eu.looker.com/explore/payment_lifecycle/fct_payin?qid=rkRaPv4WchmsK6yOo24zy8&origin_space=1698&toggle=fil) | If you do not have access to any Looker report, submit a [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)      If you already have Looker access follow the steps below :    - Access to Financial Actions Report looker is granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274).  - Submit a request through this form, selecting "Other (please specify)" for the Type of enhanced access section.  - For the Business Case section, add a note related to your role and that access is required to perform your tasks. Add more information in the More Info box if needed. |

## PROCESS FOR HANDLING TRANSACTION INVOICE REQUESTS 🖊️

Outline the steps to identify the request type and provide the correct guidance.

**Standard Checks:** Is the merchant asking for a single order invoice, or are they a Gross merchant asking about their monthly fee payment?

**Break down the solution into clear steps:**

- 
**Scenario A: Transaction Invoice Request**

  1. **Clarify the Limitation:** State clearly that Checkout.com **does not** produce invoices for single transactions.

  2. **Provide Context:** Explain that we are the payment processor. The invoice for the order itself is handled by them (the merchant).

  3. 
**Locate and Provide References:** Provide the **Merchant Reference** for their internal tracking.

    - Find the transaction** Reference** (also called **Merchant Reference**) in **Checkout Agent Toolkit** (Zendesk) or alternatively check in ****[Payin](https://checkoutinternal.eu.looker.com/explore/payment_lifecycle/fct_payin?qid=rkRaPv4WchmsK6yOo24zy8&origin_space=1698&toggle=fil)** or** ****[Financial Actions Report](https://checkoutinternal.eu.looker.com/explore/ledger_financial_actions/finance_financial_actions_report?qid=6SiDr2EGECR1hZAIdLJten&toggle=fil)** Looker**, or in the **Dashboard > All Payments** section (In Financial Actions looker it is the **Track ID** column)  
  
    
  

    - Provide this reference to the merchant for their internal tracking.

**Scenario B: Fee Invoice Due Date (Gross Merchants)**

  1. **Verify Settlement Model in CAT:** Check if the merchant is set up as "Gross" (meaning they pay fees separately).

  2. **Refer to Contract:** Advise the merchant that their specific invoice due date is defined in their contract.

  3. **Escalate if needed:** If you need a specific confirmation, ask the **Billing Team** to advise.  
  

  
💡 For **net-settled** merchants, the invoice is paid via automatic deduction from their balance. Fee transactions can also be tracked in their settlements (as well as Financial Actions reports).  
 

## RESOLUTION ⚒️

Share your findings with the merchant or the requester.  
If the merchant is actually looking for their _fee_ invoice, direct them to the "Invoices" section of the Dashboard.

  
 RESOURCES** ****⭐**

| **Case Examples** |
| --- |
| - [Case 100907](https://checkout1360.zendesk.com/agent/tickets/100907) |

##

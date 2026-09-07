---
id: 21991167806354
section_id: 21991163953810
title: "Troubleshooting APM Refund Failures: Collecting vs. Gateway Models"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991167806354-Troubleshooting-APM-Refund-Failures-Collecting-vs-Gateway-Models"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-03-18T14:22:15Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "ROW", "case_transactions_issue_refund", "apm_refund_failures_for_collecting_and_gateway_models"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article** This guide outlines the process for investigating and resolving Alternative Payment Method (APM) refund failures. It highlights the differences between Gateway and Collecting models and provides specific workflows for Giropay and Sofort.

**Problem** Merchants are reporting failed refunds for APM transactions, specifically receiving error messages or "Not Captured" statuses.

**Solution** Identify the processing model (Gateway or Collecting) and either guide the merchant to retry or perform a manual refund via internal tools.

**Case type: **Payments in

**Issue Type: **Transaction status (Non 3DS & Refunds)

**Reason: **Refund failed / manual refund

## **DESCRIBE THE ISSUE 💬**

The agent or merchant reports that a refund attempt has failed. This is common with APMs like Giropay and Sofort. In the Gateway model, the merchant handles the funds, whereas in the Collecting model, Checkout.com manages the funds. The error often requires an investigation into the APM model to determine who is responsible for the refund action.

## **KEY TAKEAWAYS 🔑**

- **Gateway Model:** Money goes straight to the merchant. If a refund fails, the merchant must handle it themselves.

- **Collecting Model:** Money goes to Checkout.com first. If a refund fails, Checkout.com steps in to process it manually.

- 
 
**Giropay Exception:** Giropay is _always_ the Collecting Model.

- 
 
**Sofort Exception:** Can be handled directly if customer account details (IBAN) are visible.

A refund may fail for any of the below APMs, but the _most common refund failures come from Giropay and Sofort. _

| **Gateway Model Common Refund Failures** | **Collecting Model Common Refund Failures** |
| --- | --- |
| Paypal Fawry BenefitPay Knet Alma  Qpa Wechat Pay Postfinance  STC Pay  Benefit PG | Ideal  Sofort Bancontact  P24  Multibanco  ACH  Giropay EPS  Tamara  SEPA Klarna PPRO |
| **Collecting Model **   - Money first goes to Checkout.com  - After checks, it’s sent to the merchant  - If a refund fails, Checkout.com steps in to process it manually | **Gateway Model **   - Money goes straight to the merchant  - If a refund fails, the merchant must handle it themselves |

**PROCESS FOR INVESTIGATING REFUND FAILURES 🖊️**

This process requires access to CAT (Config Admin Tool) and Datadog.
**Step 1. Identify the APM Model** 

You must determine if the merchant is set up for the Gateway or Collecting model to decide the next step.

- If the APM is **Giropay**, it is always the **Collecting Model**. Skip to Step 2.

- For all other APMs, log into **CAT**. 3. Search by **Processing Channel** and click the channel name.

- Navigate to **Processing > Processing Profiles > APM Name** to view details.

**Step 2. Analyze Error Details in Datadog**

- Log into **Datadog** and navigate to **Logs**. 2. Search using the `Payment ID` or `Correlation ID`.

- Filter by date to locate the specific transaction and identify the error message.

**Step 3. Execute Resolution Based on Model**

- 
**Gateway Model:**

  - Instruct the merchant to retry the refund. Since the merchant holds the funds, they must initiate the transfer.

- 
**Collecting Model (General):**

  - If the error is unclear, escalate to Merchant Care L2 using the macro: `$L1 > L2 - Choose APM`.

  - For manual refunds, contact the APM provider via Zendesk Macro: `External > APM > Select APM`. Include Payment details (Track ID, Order ID, Transaction ID) and the error message.

**Step 4. Handling Sofort Specific Refunds (Collecting Model)** 

Sofort requires a specific check for customer banking details.

- Check if the customer's **IBAN** is available in the system.

- 
**If IBAN is available:**

  - Process the refund directly in the Sofort portal.

  - If successful, notify the APM team using macro: `External > APM`.

  - Notify APM Reconciliation: `Transfer > APM Reconciliation`.

  - Notify Treasury: `Transfer > Treasury Payments`.

- 
**If IBAN is NOT available (or refund fails):**

  - Contact the APM provider for details.

  - If the refund cannot be processed via the portal, follow the **Manual Refund Process** (Step 3).

**Step 5. Handling Giropay Specific Refunds (Collecting Model)**

- Merchants must include `account_number` and `bank_code` in the payment request.

- Share customer bank details privately with the Payments Team via Zendesk to request a manual bank transfer.

**RESOLUTION ⚒️**

- **Gateway:** The merchant successfully retries and processes the refund on their end.

- **Collecting:** Checkout.com successfully processes the manual refund or bank transfer, and the Transaction Status is updated.

- 
 
**Verification:** Ensure the refund status updates in the Dashboard (for merchants) and the HUB (for internal teams).

**ESCALATION ⏫**

**When to Escalate:**

- Unknown or unclear error messages in Datadog.

- Refund fails despite following the manual process.

- IBAN is invalid on the portal for Sofort transactions.

**Required Information:**

- 
 
**Macro:** `L1 > L2 - Choose APM`.

- **Details:** Payment ID, Error Message from Datadog, confirm APM Model (Collecting/Gateway).

**FAQs ❓**

- **Can I process a Sofort refund without contacting the APM?** Yes, but only if the customer's IBAN and account details are visible in the system. If not, you must contact the provider.

- **Why is the refund status "Not Captured"?** For some APMs, "Not Captured" on a refund implies the transaction was declined by the issuer/bank, and the client must contact their bank.

- **Is Giropay ever a Gateway model?** No, Giropay is always processed under the Collecting Model.

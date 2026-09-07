---
id: 35008251599634
section_id: 34976600416658
title: "Platforms: Reports"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/35008251599634-Platforms-Reports"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-04-22T11:22:22Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

This article lists all available reports, explains what each one is used for, covers pagination rules, explains invoice reports, and directs you to the technical docs for API retrieval.**Reports overview**

Checkout.com provides 16 aggregated reports covering the platform and all of its sub-entities. These are available via the Platforms API.

| **Report name** | **What it covers** | **Best used for** |
| --- | --- | --- |
| Authentication Report | All authentication events within a specified time frame | Fraud and authentication analysis |
| Balance Breakdown Report | All financial activity affecting the Available balance in a time frame | Balance management, reconciliation |
| Balance Report | All balances within a time frame | Balance management, reconciliation |
| Bank Payouts Report | All successful and declined bank payouts in a time frame | Payout reconciliation |
| Card Payouts Report | All successful and declined card payouts in a time frame | Payout reconciliation |
| Disputes Report | All disputes raised within a time frame | Dispute management |
| Financial Actions by Date Range Report | All financial actions impacting the Available balance in a time frame | Reconciliation, balance management |
| Financial Actions by Payout ID Report | All financial actions linked to a specific payout | Settlement and payout reconciliation |
| Fraud Detection Report | Transaction-level data on risk rules triggered, outcomes, and fraudulent transactions | Fraud monitoring and rule optimisation |
| Invoices | Monthly summary of Checkout.com fees per active entity per currency | Tax documentation — can be used as a tax document in applicable regions |
| Payments Report | All payment actions including refunds within a time frame | Payment reconciliation, transaction history |
| Payouts Report | All payouts and related fees within a time frame | Settlement and payout reconciliation |
| Real-Time Account Updater Report | All card updates made by the Real-Time Account Updater service | Credential management |
| Reported Fraudulent Transactions Report | All transactions reported as fraudulent in a time frame | Fraud investigation |
| Retrievals Report | All retrieval requests in a time frame | Dispute management and preparation |
| Settlement Statement | Overview of settlement activity (payments, refunds, chargebacks, fees) | Reconciliation and settlement management |

**Which reports to recommend for common use cases**

| **Use case** | **Recommended report(s)** |
| --- | --- |
| Reconciliation | Balance Breakdown Report, Financial Actions by Date Range Report, Settlement Statement |
| Settlement queries | Settlement Statement, Financial Actions by Payout ID Report, Payouts Report |
| Dispute management | Disputes Report, Retrievals Report |
| Fraud investigation | Fraud Detection Report, Reported Fraudulent Transactions Report |
| Tax documentation | Invoices |
| Payout confirmation | Bank Payouts Report, Card Payouts Report |

**How to retrieve reports via the API**

Reports are retrieved using the Platforms Reports API. Direct the customer to the technical docs for the full API reference and example requests: [Retrieve reports using the API](https://www.checkout.com/docs/platforms/for-saas/retrieve-reports/retrieve-reports-using-the-api)

For sample reports (to show a customer what a report looks like before they retrieve it), direct them to their account manager.**Pagination — the 1 million row limit**

Each report file has a maximum of 1 million rows. If a report contains more data than this, Checkout.com automatically splits it into multiple files.

The files are numbered sequentially. For example, a Financial Actions by Date Range report with 2.4 million rows creates three files:

- financial-actions_{entity-id}_{start-date}_{end-date}_1.csv

- financial-actions_{entity-id}_{start-date}_{end-date}_2.csv

- financial-actions_{entity-id}_{start-date}_{end-date}_3.csv

If a customer reports that a report appears to be missing data, check whether the data was split across multiple files.**Invoice reports**

The Invoices report is a monthly summary of Checkout.com fees for each active entity per currency. Platforms can use these as tax documents in applicable regions.

If a customer asks for historical invoices or can't access them, direct them to the API or their account manager.**Troubleshooting / common questions**

**Q: A customer says report data looks incomplete.**

Check whether the report was split into multiple files. If the data volume exceeds 1 million rows, multiple files are created. All files must be combined to get the full dataset.

**Q: A customer can't find a payout in their Settlement Statement.**

Try the Financial Actions by Payout ID Report instead — it shows all financial actions linked to a specific payout ID, which is more targeted than the Settlement Statement.

**Q: A customer wants to use the Invoices report for tax purposes.**

Confirm the Invoices report is a monthly Checkout.com fee summary. It can be used as a tax document in applicable regions. However, this article doesn't cover specific tax rules — direct the customer to their own finance team or tax adviser for guidance on tax compliance.

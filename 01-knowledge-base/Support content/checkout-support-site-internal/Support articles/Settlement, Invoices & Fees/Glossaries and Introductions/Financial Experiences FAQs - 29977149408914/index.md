---
id: 29977149408914
section_id: 21991151260690
title: "Financial Experiences FAQs"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29977149408914-Financial-Experiences-FAQs"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-03-31T13:57:25Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K4MD5CAPQ3GPKCANYT57ZMTP", "01K6RGZT9CSP3K2F9MSHY0DKHB"]
label_names: ["Troubleshooting", "FTS", "FAQ", "Financial Experience"]
user_segment_ids: [11003606966930]
archive: false
---

Use this article for frequently asked questions on **Financial Experience (FTS)**

## Reconciliation Reports**❓**

 When are the financial reports available? 

**Financial Actions by Date Range Report:** The report is updated between midnight and 3:00 AM in your entity's [settlement time zone](https://www.checkout.com/docs/funds-management/receive-settlements#Settlement_time_zone). You can generate it on a daily, weekly, or monthly basis.

**Financial Actions by Payout ID Report:** This report is created when your settlement is generated according to your [settlement speed](https://www.checkout.com/docs/funds-management/receive-settlements#Settlement_speed), between 2:00 AM and midnight in your entity's [settlement time zone](https://www.checkout.com/docs/funds-management/receive-settlements#Settlement_time_zone). A report is created for every settlement that is paid out, in line with your [settlement frequency](https://www.checkout.com/docs/funds-management/receive-settlements#Settlement_frequency). 

Refer to this documentation to check the availability for each type of report  
[https://www.checkout.com/docs/business-operations/retrieve-reports](https://www.checkout.com/docs/business-operations/retrieve-reports)

 Why are there discrepancies between payments report/dashboard and invoices/payouts/financial actions reports?

Dashboard payments reports do not reconcile against financial reporting and invoicing because they are based on **Gateway events**, not the successful impacts to the Client currency account balances and ledgers.

Discrepancies occur because Dashboard reports don't account for:

- 
**Risk arrears logic delays:** These are delays in processing captures and refunds to account for credit risk.

- 
**Processing errors:** Events and transactions can get stuck.

The fundamental difference is: the **Dashboard Payments report** is based on the requests the client has made, while the **Financial Actions Report** is based on what Checkout has successfully impacted for a client's balance. Additionally, Dashboard reports are generated in the **browser timezone**, whereas invoices are generated in **UTC**.

 Why do my payments not reconcile when I filter on the **Requested On** timestamp?

Clients should use the **Processed On** field, not the **Requested On** field, for reconciliation. **Requested On** is based on Gateway events (requests made by the client), while **Processed On** is what Checkout has successfully processed for a client.

**Processed On** shows when transactions, financial revenue, and fees impact a client's currency account available balance. Due to the latency between the gateway request and those events impacting the client's account, events requested close to 00:00:00 UTC can be processed on the following day.

 What does Financial Actions reporting tell me and how can I use this data?

The Financial Actions report tells you the **financial impacts** successfully processed across a given time period, including the associated fees and revenues.

You can use this report to:

- Reconcile with your own internal transaction records.

- Calculate the cost of sales and the net revenue for each transaction.

The data granularity allows you to see the different fees affecting your transactions at each stage (authorization, capture, refund).

 What timezone are my reports in?

Checkout.com reports and payments are generally based on **UTC (Coordinated Universal Time)** time zone.

 How will a bounced refund show in financial action reports?

In NAS, a bounced refund will have the **Action Type** and **Breakdown Type** as **"Clearing Failed"**.

 Payout ID column is missing in financial actions by date range reports. Why is this data missing?

The **Financial Actions by Date Range** report does **not** have the Payout ID populated. This is because it is generated before financial actions have been associated with a settlement. The Payout ID is only populated in the **Financial Actions by Payout ID** report.

 

 Is it possible for a merchant to distinguish between initial and retried transactions, and their associated fees, in the reports we provide for reconciliation?

It is not currently possible to distinguish between initial and retried transactions directly within the reports. Although the payments report has some fields for this purpose, they are not populated. If a transaction is retried, the scheme fees will appear multiple times in the Financial Actions report, but there is no way to identify if it was a retried transaction unless the merchant uses the API to get payment details.   
More information on using the API for this can be found at [https://api-reference.checkout.com/#operation/getPaymentDetails](https://api-reference.checkout.com/#operation/getPaymentDetails).

 

 Which report can be used to check Rolling Reserve movements?

Balance Breakdown for detailed information or simply the Balance report. **Charge** and **Rolling Reserve Released** should be filtered on column Type to see only reserve movement. Example ticket [77634](https://checkout1360.zendesk.com/agent/tickets/77634).

 

## 

## Invoices**❓**

 What do the numbers for payments on my invoice represent?

The **Count** and **Total** next to Payments, Refunds, and Chargebacks on an Invoice refer to the number that have occurred within the month and the associated volumes.

For the Payments section, the number is the total count of **captures and partial captures** that were successfully processed. The fees section includes a sum of **all fees** related to processing (Authentication, Authorization, Voids, Captures), not just successful captures.

 What are the fees charged on my invoice, and why don't they reconcile with my settlement/payouts report?

To reconcile against the invoice, you should use the **Financial Actions by Date Range report** or the **Balance report** spanning the same monthly period, as these are based off ledger movements to a client's balance.

**Do not use** the Financial Actions by Payout ID reports (or transaction breakdown report on Dashboard) or the Payouts report to reconcile with invoice amounts. This is because:

- Settlements/payouts are based on the **End of Day (EOD) available balance (related to previous day EOD total)**

- For example, a payout made on 01/10 will be based off the EoD balance on 30/09, so financial impacts and fees from the 30th relate to that payout. This prevents the payout report from being used to reconcile against the invoice.

 Is it possible to add a merchant's GST/VAT no. to invoices?

Yes. You need to raise this request with the **merchant configuration team** for actioning

 Can I split out the monthly invoice by processing channel?

No. The invoice is automatically split following the CAT setting **by entity **and** currency**. The merchant can, however, filter their processing channel in their Financial Action Report (FAR).

 Can we generate custom Invoices?

No, we can't generate custom Invoices. Checkout does not offer an Invoice as a service for our clients.

Certain invoices would need to be manually generated by the Finance Accounts Receivable team (e.g for gross-settled merchants) which is for the merchant; however we cannot issue invoices on behalf of our merchants to their end customers.

## 

## Settlements & Settlement Reports**❓**

 Why is my payout report missing today or larger than usual?

Financial Action by Payout ID reports are only generated when a **settlement is created**.

We do not settle merchants on the **weekend or on public holidays** when bank networks are not working. Therefore, after a weekend or public holiday, the Financial Actions by Payout ID files are bigger than usual due to the longer period of processing before a settlement was made. The volume of transactions related to a Monday settlement will cover financial impacts processed on Friday, Saturday, and Sunday.

 Why isn't a "Payout Returned" adjustment included in a report/settlement?

Payout Returned adjustments are **not reflected** in the Financial Action by Payout ID reports.

After a payout return, the *next* Financial Actions by Payout ID report will feature all transactions related to the returned payout and any new financial actions. This is done to allow customers to reconcile the original transactions to the new payout.

The adjustment is excluded to prevent "double-counting" the adjustment and all the transactions that comprised it, which would make the new payout report unreconcilable.

 Can I link the settlement ID to the amount in the bank account?

Yes, you can reconcile between your bank statements and Checkout.com's Financial Action by Payout ID report:

1. Identify a payout from Checkout.com on your bank statement by the unique **12-character ID**.

2. Look up the **Financial Action by Payout ID report** with that corresponding unique 12-character ID in the filename.

The payout amount in your bank account will match the **sum of all values in the Holding Currency Amount column** of the corresponding report.

 My merchant changed from net to gross settlement. Can we send them an SFTP report based on gross numbers for the old net settlements?

No, generating a report now as gross-settled is **impossible**.

The report ties transactions to a given payout that has already occurred as net-settled. If a report were generated as gross-settled for a net-settlement, the payout amount would **not reconcile** with the report.

If the client wants to see the report as gross-settled, they can filter out the fees within the existing report.

 Does my Financial Actions by Payout ID report include all holding currencies?

No. Financial Actions by Payout ID reports are generated off a given settlement made to a client, and the settlement will be in a holding currency. A merchant will therefore receive this report **per entity per holding currency**.

However, **Financial Actions by Date Range, Balance report, and Payouts report** will include all holding currency financial impacts in them and are received **per entity**.

 Why is a transaction in multiple settlements?

A transaction can be split across multiple settlements for reasons including:

- 
**Arrears logic:** If the customer has a daily payout schedule and a 2-day arrears logic, the transaction can be split across two settlements (e.g., authentication fees on T+1 settlement, capture on T+3 settlement).

- 
**Interchange fees:** Interchange fees are only processed on T+1. For a daily payout, the capture may be in the T+1 settlement, and the Interchange fee may be in the T+2 settlement.

 Why can't I find some transaction records in the Transaction Breakdown (Dashboard) or Financial Action report by Payout ID?

When a merchant's currency account goes **negative**, a transaction will not be reflected in the Transaction Breakdown (Dashboard) or Financial Action report by Payout ID.

The reason is that the Financial Action report by Payout ID is associated with a settlement. When an account goes negative, there is nothing to pay the merchant, and therefore **no settlement**. The merchant should look for the transaction record in the **Financial Action report by Date Range**.

 My settlement is missing my custom ID?

Custom IDs on settlements are set at the **currency account level** and are appended to the beginning of the settlement ID (e.g., `USD000003BYX`).

To troubleshoot, check that the custom ID has been created in CAT for the currency account from which the settlements are coming and that there is processing.

## 

## FX (Foreign Exchange)**❓**

 When is the FX markup applied?

FX markup is applied on **capture **and **refund amounts only** and is never applied to fees. The markup is applied to the rate. No markup is added on chargebacks.

 For FX, can I review the original currency amount and converted currency amount to understand the difference?

Yes. A merchant can use the **financial actions reports** to understand the conversion rate applied to convert a processing currency into the holding (remittance/payout) currency and see the amounts in both currencies. The report will contain columns such as 'Processing Currency,' 'FX Rate Applied,' 'Holding Currency,' 'Holding Currency Amount,' and 'Processing Currency Amount.'

 Why is FX markup not visible in the reports?

There are currently no plans to add visibility of FX fees for merchants.

The key reasons for this approach include:

- Commercial feedback suggests that **no other PSPs** provide this breakdown of FX Fees.

- The application of the FX markup is complex and can differ by product (Live Rates vs. Scheme Rates) and by event (capture vs. refund vs. chargeback).

- The FX markup is not purely a fee but a **buffer in the conversion rate** to cover the risk Checkout takes for committing to converting one currency to another based on the conversion rate of that time. It is therefore not treated as any other fee.

## 

## Balances**❓**

 What is my merchant's closing balance?

You can self-serve and view a NAS merchant's **live or end-of-day balance** for any given day on the **Currency Accounts Balance retool**.

There are four types of balances for each Currency Account:

- 
**Pending:** Incoming funds that are not yet available.

- 
**Available:** Funds available for payout.

- 
**Payable:** Funds reserved to be paid out.

- 
**Collateral:** Funds reserved for collateral (clients do not have access to these funds).

- 
**Opertaional:** The Operational balance holds funds as a backup to cover Bank and Card Payouts and Issuing payments when the Available balance is insufficient.

 How is the pending balance calculated?

The pending balance is generated from transactions that have been requested but **not yet processed **and not yet available (the difference between `requested_on` and `processed_on` in our financial actions reports). This balance will eventually move from pending to available based on the **arrears logic** set up for the merchant.

 Can you explain the Balance report fields?

Please refer to the public page below  
[Checkout documentation](https://www.checkout.com/docs/funds-management/retrieve-financial-reports/balance-reports/balance-report)  
 

## 

## Minimum Billing & Tiered Pricing Adjustments**❓**

 When does the minimum billing fee apply?

Minimum Billing Fees are calculated and applied on the **1st of the month** for the previous month's processing.

For example, a minimum billing fee for July 2025 is calculated and applied on **1st August 2025**. It deducts from the first settlement of August and appears on the **August invoice**, which is generated on 1st September 2025.

 How do I reconcile the minimum billing fee?

To see the breakdown of the minimum billing charge on the invoice, the client should use the **Financial Actions by Date Range report** from the previous month and add up all the relevant Checkout fees.

The billing fee is the difference between what is earned by Checkout and the **minimum billing threshold** set in the Client Admin Tool (CAT).  
[Checkout documentation](https://www.checkout.com/legal/minimum-billing-fee)

 If the minimum billing start date in CAT is October 2025, when will the merchant receive the first fee?

The first minimum billing fee will be calculated on the **1st November**, based on October's balance movements. The merchant will see the fee on the 1st November invoice.

## 

## Financial Actions Report**❓**

 For the breakdown types "Gateway Fixed Fee" and "Gateway Fixed Fee Tax," we see a different processing currency. Why?

The billing currency configured in CAT is what is seen. Therefore, the fees are applied accordingly as the processing currency is then converted to the holding currency. Note that the transaction is still in the holding currency, but the fees are just in the billing currency.

 I have enabled UDF columns in CAT but it is still not populated in the FAR.

To ensure merchants do not send Personally Identifiable Information (PII) data in the User-Defined Field (UDF) fields, a specific process is in place to enable them. Please liaise with the fex-reporting team to activate UDF fields.

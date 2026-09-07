---
id: 28618838163218
section_id: 29378108664978
title: "Invoice Reconciliation against Financial Actions Report"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/28618838163218-Invoice-Reconciliation-against-Financial-Actions-Report"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-31T16:07:19Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K22NYQP6QBETF4NRGEXJXKBA", "01K22P1B0HTTRPKRMJJNZJ3NXA", "01K4QH2BDBYR4Z8C0ZMABD2R7M"]
label_names: ["L2", "troubleshooting_guide", "FAR", "financial_actions_report"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

Merchant Care agents should use this guide to reconcile an invoice with the Financial Actions Report. 

**Problem / Symptom**: Common issues involving mismatched amounts in merchants’ invoice reconciliations.

## DESCRIBE THE ISSUE 💬

Our Merchant Care team often gets requests for help with matching monthly invoices to the data in the Financial Actions report.  
 

 

## KEY TAKEAWAYS 🔑

- Invoices are based on UTC time and reconciliation must be done in UTC to match the invoice's timeframe

- Invoices mainly include the fees related to a month’s processing, although they also include a count of transactions by type

- Use the Financial Actions Report in Looker to initially get the total amount of fees

- Extract the Financial Actions report from the Dashboard for the corresponding invoice month

- Reconciliation process should confirm that the invoice totals are correct

- In calculations use the `Holding Currency` and `Holding Currency Amount` columns, not the processing currency  
 

## TOOLING 📍

Click here to see the tools needed

| Tool | Access |
| --- | --- |
| [Dashboard (NAS)](https://dashboard.checkout.com/reports/all-reports) | - If you do not already have access to the Dashboard, submit a ticket to IT via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)   - Submit a request through this form, selecting "identity.checkout.com - Prod" for the environment |
| [Looker](https://checkoutinternal.eu.looker.com/explore/ledger_financial_actions/finance_financial_actions_report?qid=O2dkPz27cjMNiGP1qnbSkv&toggle=fil) | If you do not have access to any Looker report, submit a [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)      If you already have Looker access follow the steps below :    - Access to Financial Actions Report looker is granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274).  - Submit a request through this form, selecting "Other (please specify)" for the Type of enhanced access section.  - For the Business Case section, add a note related to your role and that access is required to perform your tasks. Add more information in the More Info box if needed. |
| Spreadsheet tool | You can use any spreadsheet tool like Google sheets, Excel or similar for reports. |

 

## PROCESS FOR INVOICE RECONCILIATION 🖊️

The primary goal is to guide the merchant through the correct reconciliation process to validate the invoice figures. The following sections outline how to do this with each relevant report.
A frequent mistake is generating the Financial Actions report in a local time zone. This inevitably creates a mismatch because the invoice is always based on UTC time and a calendar month. 
Invoices are generated per holding currency for each entity that was actively processing within a given period. For example, a client with two entities, where Entity A utilizes five holding currencies and Entity B utilizes two, would receive a total of seven invoices.  
  
💡 Invoices display amounts in the [major unit](https://www.checkout.com/docs/payments/accept-payments/format-the-amount-value) of the holding currency, rounded to two decimal places. For example, a card scheme fee of 33.33333 USD is displayed as 33.33 USD. In some cases, the decimals may be rounded down further, for example, from 33.33 to 33.30.
**Reconciling with the Financial Actions Report**
**Step 1: Get the Invoice and Financial Actions monthly Report**

- On the Dashboard, first ensure you have selected the correct Entity. Then, from the left menu, navigate to Business account > Invoices

- Locate the correct invoice (for the month and specific currency you're reconciling). To download the invoice pdf file: click the download arrow icon on the right side of the invoice row

 
 

- If you prefer to view the invoice on the dashboard: click anywhere on the invoice row itself

 

- Generate and download the** Financial Actions** report (**FAR**) for the exact same calendar month as the invoice and in UTC time zone

 
 

- Once the report has been generated it will appear in the Reports list, ready to download

 
**Step 2: Reconcile Invoice figures with the Financial Actions Report**
The invoice is typically structured in two main parts:

- Summary page: This first page shows the high-level totals for all processing activity (e.g., the total cost for Payments processing, Refunds processing, etc.).

- Fees Breakdown: The subsequent pages provide a detailed breakdown of how the totals on the summary page are calculated.

Reconciliation steps:

- Open the Invoice and Financial Actions report

- The invoice total amount appears on the top-right

- In the Financial Actions, filter the Holding Currency column to show only the currency that matches the invoice you are reconciling (if there is more than one currency for the entity)

- As invoices only relate to fees (and their associated taxes), filter out all non-fee-related transactions in the Breakdown Type column (e.g. `Capture`, `Payout` and `Refund`).   
For certain entities, the invoice will not include a tax amount, and you will not find any corresponding tax-related transactions in the financial reports.

 

- Then, sum the values in the Holding Currency Amount column to get the total

 

- To calculate the total fees excluding tax, update the Breakdown Type filter by removing any entries containing 'Tax'. For some entities, tax is not included on the invoice.

**Using Looker report**
While the downloadable Financial Actions report is the primary source for reconciliation, the process can be slow for merchants with a very high number of transactions.
In these cases, you can first use the Looker report below to quickly check if the invoice total matches the sum of the financial actions. 
Make sure you add the Entity ID and the invoice month and the holding currency if there are more than one currency.   
  
****[Looker 1](https://checkoutinternal.eu.looker.com/explore/ledger_financial_actions/finance_financial_actions_report?qid=NVmfQK2blGq8WeKaEmAAUO&toggle=fil)  
 
 
 
To retrieve all transactions breakdown use the Looker below :
****[Looker 2](https://checkoutinternal.eu.looker.com/explore/ledger_financial_actions/finance_financial_actions_report?qid=cLwhp0lB4URLLC41CNUK11&toggle=fil)
If there are more than 5000 rows (there will be a yellow notification bar) select the **All results** option before downloading the file.   
 
  

  
**Note 💡**

- For merchants with a high transaction volume this may generate large reports in looker. Instead, try generating the Financial Actions report directly on the Dashboard. Note that on the Dashboard, multiple files may still be generated.  
 

- Looker is a data aggregation tool, which means it groups identical data together by default.  
 

- If a report contains two or more rows that are exactly the same, Looker will display them as a single, unique row. Because of this, the total number of rows in a Looker report may be lower than the row count in a CSV file downloaded from the Dashboard. Therefore, the dashboard report is more accurate.

  
 
**Step 3: Reconciling specific Invoice line items (optional) **
The following sections, which detail how to reconcile individual invoice line items, are optional. You need to perform this level of analysis if it is requested by the merchant or the requester or required to investigate a particular discrepancy.
To reconcile a single line item from the invoice, for example, Payments processing, you need to map it to the correct transaction type in the Financial Actions report.
We can use the Looker Financial Actions report for a quick, internal check to verify the total amounts for your own analysis. 
  
⚠️ However, when sharing your findings with a merchant, you should use the Financial Actions report downloaded from the Dashboard. This report is the merchant's source of truth and should be used as the basis for all external communication.  
  
 

### **Reconciling using the Financial Actions Report**  
  
💰Payments (captures)

- On the summary page (first page) of the invoice, locate the **Payments processing** line item

- The figure in the **Amount** column is the total fee charged for all `Capture` transactions

- To verify this amount, in the **Financial Actions** report, filter the **Action Type** column to select all of the following transaction types that are present in the report: `Authorization`, `Capture`, `Partial Capture`, and `Void`

- Then remove non-fee related items in the **Breakdown Type** column (e.g., `Capture`). Fee-related taxes should also be excluded, since fees and taxes are shown as separate columns on the invoice

- Sum the values in the **Holding Currency Amount** column. The result will give you the total fees charged for captures

 
To reconcile the total amounts and transaction counts (if included in the invoice):

- In the **Financial Actions** report, select only `Capture` in the **Breakdown Type** column

- To reconcile the figures for a single card scheme, filter the **Payment Method** column to show only that specific scheme (e.g., `VISA`, `MASTERCARD`).

- 
**Verify the count:** The number of rows remaining in the filtered report should match the transaction count shown on the invoice (e.g., `4048`).

- 
**Verify the total value:** Sum the values in the **Holding Currency Amount** column for the filtered rows. This sum should match the **totaling** value shown on the invoice (e.g., `1,232,719.57`)

 

### 🔄 Refunds

Similar to the captures (payments) reconciliation above:

- Filter the **Action Type** column to select all of the following transaction types that are present in the report: `Partial Refund` and `Refund`

- Then remove non-fee related items in the **Breakdown Type** column (e.g., `Refund`). Fee-related taxes should also be excluded, since fees and taxes are shown as separate columns on the invoice

- Sum the values in the **Holding Currency Amount** column. The result will give you the total fees charged for refunds 

 
To reconcile the total amounts and transaction counts (if included in the invoice):

- In the **Financial Actions** report, select only `Refund` in the **Breakdown Type** column

- To reconcile the figures for a single card scheme, filter the **Payment Method** column to show only that specific scheme (e.g., `VISA`, `MASTERCARD`).

- 
**Verify the count:** The number of rows remaining in the filtered report should match the transaction count shown on the invoice (e.g., `2`).

- 
**Verify the total value:** Sum the values in the **Holding Currency Amount** column for the filtered rows. This sum should match the **totaling** value shown on the invoice (e.g., `365.46`)

 

### **🎟️ Network tokens**

Similar to reconciliations above using Financial Actions report:

- Filter the **Action Type** column to select `Network Token Update` type (or you can directly select the related fees in the **Breakdown Type** column)

- Select `Network Token Update Fixed Fee` items in the **Breakdown Type** column. Fee-related taxes should also be excluded, since fees and taxes are shown as separate columns on the invoice

- Sum the values in the **Holding Currency Amount** column. The result will give you the total fees charged for network tokens

 
To reconcile the transaction counts (if included in the invoice):

- To reconcile the figures for a single card scheme, filter the **Payment Method** column to show only that specific scheme (e.g., `VISA`, `MASTERCARD`)

- 
**Verify the count:** The number of rows remaining in the filtered report should match the **transaction count** shown on the invoice (e.g., '76' for MASTERCARD)

### **Other fees and adjustments**

The **Other fees and adjustments** line item on the invoice summary is a category for various charges and credits that fall outside of standard transaction processing fees.
As shown in the invoice, this line item appears as a total on the summary page and is detailed further down in its own section on the **Other fees and adjustments** page. This section typically includes the following types of charges:

- 
**Scheme fee adjustments:** Credits or debits from card schemes (like Visa or Mastercard) related to transactional or non-transactional activities.

- 
**Checkout Premium or other fees Tiering adjustments:** Adjustments related to the merchant's pricing tier for Checkout fees.

- 
**Minimum Billing fees:** Charges applied if the merchant's total monthly Checkout fees do not meet a contractually agreed-upon minimum amount.

To reconcile this section, each line item from the breakdown needs to be matched with the corresponding adjustment transactions in the **Financial Actions** report.  
  
  

### To reconcile

- Filter the **Action Type** column to select `Adjustment`

- Select all fee items (excluding fee taxes) in the **Breakdown Type** column

- Sum the values in the **Holding Currency Amount** column. This result represents the total fees charged (positive numbers) or credited (negative numbers) to the merchant's account

**Note** 💡 On the invoice, negative amounts —representing credits to the merchant’s account— are shown in brackets, for example, `(17.55)`
  
  
 
💡 This same multi-filtering logic can be applied to reconcile other specific line items, such as **Authentication **fees.  
 
**Reconciling using Looker**
**Payments **(captures)  
  
****[Looker](https://checkoutinternal.eu.looker.com/explore/ledger_financial_actions/finance_financial_actions_report?qid=k03WCVT1n4cVbjLJc72EKB&toggle=fil) to review total fee amounts  
  
If you need to filter by a specific scheme, use the **Payment Method Name **filter field

For Tax fees only change Financial Actions Type filter to `Tax`  
  

- To reconcile the total amounts and transaction counts (if included in the invoice) that are summarized by card scheme on the **Fees Breakdown** pages, use the following Looker report:  
  
****[Looker](https://checkoutinternal.eu.looker.com/explore/ledger_financial_actions/finance_financial_actions_report?qid=Issi5foKkY8ATTByNQN3bO&toggle=fil)  
  
The looker provides totals for different types of transactions (e.g., `Capture` for Payments, `Refund`, `Chargeback`). Check the row corresponding to the item you need to verify

- If you need to narrow down the results to a specific card scheme (e.g., VISA), use the **Payment Method Name** filter. as shown below

### **Refund processing**

****[Looker](https://checkoutinternal.eu.looker.com/explore/ledger_financial_actions/finance_financial_actions_report?qid=kJ6jkiB5FrxjwbVHSgdHe5&toggle=fil)**** [](https://checkoutinternal.eu.looker.com/explore/ledger_financial_actions/finance_financial_actions_report?qid=HGeBZBsQ7kQkKoKjgPrd6u&toggle=fil) to review total fee amounts

- 
To reconcile the total amounts and transaction counts (if included in the invoice) that are summarized by card scheme on the **Fees Breakdown** pages, use the following Looker report:
****[Looker](https://checkoutinternal.eu.looker.com/explore/ledger_financial_actions/finance_financial_actions_report?qid=Issi5foKkY8ATTByNQN3bO&toggle=fil)
The looker provides totals for different types of transactions (e.g., `Capture` for Payments, `Refund`, `Chargeback`). Check the row corresponding to the item you need to verify

- If you need to filter by a specific scheme, use the **Payment Method Name **filter field

 

### **Network tokens processing**

****[Looker](https://checkoutinternal.eu.looker.com/explore/ledger_financial_actions/finance_financial_actions_report?qid=1E0qRmyE1wjOQ0KMpqAFVi&toggle=fil)** **to review total fee amounts as well as the transaction fee counts  
  

  
**Other fees and adjustments**
****[Looker](https://checkoutinternal.eu.looker.com/explore/ledger_financial_actions/finance_financial_actions_report?qid=yecOWeiZe0PEXkn08wZ4xQ&toggle=fil) to review total fee adjustment amounts  
****[Looker](https://checkoutinternal.eu.looker.com/explore/ledger_financial_actions/finance_financial_actions_report?qid=PVr3SlZ4WqTC3tkiSUeAIm&toggle=fil) to review detailed fee adjustments (including taxes)  
  
  
💡 To investigate a different fee, use the Looker report below and filter by the name of the fee. Ensure you use the correct **Entity ID** and **Holding Currency**  
  
****[Looker](https://checkoutinternal.eu.looker.com/explore/ledger_financial_actions/finance_financial_actions_report?qid=NVmfQK2blGq8WeKaEmAAUO)  
  
  
 

## RESOLUTION **🛠️**

Once you have verified that the invoice and report data are correct, share your findings with the merchant or the requester.

## ESCALATION** ⏫**

If you have completed the reconciliation and identified any discrepancies, please escalate to the FE Reporting team either by requesting assistance in the `**#**ask-fex-clientreporting` Slack channel or by submitting a [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277)  
  
Provide client and entity details and select the options below :  
**Product team** > **FTS**  
**FTS Product Team **> **FTS - Financial R&R**

## RESOURCES** ****⭐**

| **Case Examples** | **Related** |
| --- | --- |
| - [Case 71657](https://checkout1360.zendesk.com/agent/tickets/71657)  - [Case 67754](https://checkout1360.zendesk.com/agent/tickets/67754)  -  [Case 74225](https://checkout1360.zendesk.com/agent/tickets/74225) | - [Checkout public documentation](https://www.checkout.com/docs/funds-management/retrieve-financial-reports/reconcile-with-checkout-com#Reconcile_invoices)  - [Confluence - NAS Financial Reporting & Reconciliation FAQ](https://checkout.atlassian.net/wiki/spaces/MER/pages/5509021735/NAS+Financial+Reporting+Reconciliation+FAQ) |

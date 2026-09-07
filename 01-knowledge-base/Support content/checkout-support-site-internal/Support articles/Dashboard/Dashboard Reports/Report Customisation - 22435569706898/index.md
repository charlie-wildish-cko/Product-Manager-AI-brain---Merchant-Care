---
id: 22435569706898
section_id: 28533338298898
title: "Report Customisation"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22435569706898-Report-Customisation"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:36:42Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQBAM2Q5EGSKD3634VFBT"]
label_names: ["global", "case_reports", "case_reports_issue_custom_report_needed", "report_customization"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

Report customisation refers to tailoring reports to meet the specific needs and preferences of the user/ clients to reconcile financial data of their business operations smoothly. While ensuring that reports comply with industry standards and regulations, clients expect consistency in reporting standards delivery.

## Process Steps

**Managed v/s Unmanaged Merchant Account**

Merchant Care prioritizes merchant tickets per the urgency and request of the Tier. 

- Tier 1, 2 & 3 are managed accounts by Account Managers(AM). AM can assist and intervene within the communications and/ or take over requests directly from merchants. 

- Tier 4 is based on Managed and Unmanaged Accounts. Managed Accounts are managed by Account Managers - [am@checkout.com](mailto:am@checkout.com) whereas Unmanaged are handled by Merchant Care - [support@checkout.com](mailto:support@checkout.com).

- Merchants’ queries are handled by Merchant Care however Unmanaged Tier 4 is tackled from end-to-end. This includes merchant’s queries, complaints, reports discrepancy resolution and follow-ups.

**Current dashboard report availability **

The Dashboard currently holds the following report data point for merchants to analyse and reconcile data in figures:-

| **Types of reports available on the Dashboard** |  |
| --- | --- |
| - Payments  - Disputes   - Retrievals  - Bank Payouts  - Card Payouts  - Authentication  - Fraud Detection  - Reported Fraudulent Transactions | - Balance  - Financial Actions  - Payouts  - Card Issuing Authorisations*  - Card Issuing Cards*  - Card Issuing Chargeback*  - Card Issuing Presentments*    _*For Issuing merchants only_ |

Respective reports columns can be viewed [here](https://www.checkout.com/docs/business-operations/use-the-dashboard/reporting).**Generate and download the report on the Dashboard**

| **Procedure** |  |
| --- | --- |
| 1. Login to [Dashboard](https://dashboard.checkout.com/)   2. In the Reports screen, select Generate report.  3. Select the report type you want to create from the dropdown menu  4. Set an Entity, time zone and date range.  5. Rename the report to your convenience - a default  6. Select if you want a one-off report or subscribed over a frequency of    1. Daily    2. Weekly    3. Monthly    7. Choose the fields you want to include in your report (the available fields depend on the report type)   1. You can select Default, All, or Custom, which lets you pick only the fields you want   8. Select Generate report    1. Reports containing a lot of data may take a while to generate, so feel free to do other things while you wait    2. Once complete, the report is added to the Reports screen where you can download it at any time by selecting CSV   More information can be referenced here: [CKO Documentation](https://www.checkout.com/docs/business-operations/use-the-dashboard/reporting#Generate_and_download_a_new_report) |  |

**Who can download reports on the Dashboard?**

| **Permission** | **View and generate payment reports** |
| --- | --- |
| Admin | Yes |
| Developer | Yes |
| Disputes Manager | Yes |
| Disputes Operator | No |
| Identity & Access Management Admin | No |
| Support Manager | Yes |
| Read Only | Yes |

You can refer to the [CKO merchant documentation](https://www.checkout.com/docs/business-operations/use-the-dashboard/user-permissions) for more information.**Client Admin Tool Reporting profile **

For reports to be downloaded on Dashboard, they need to be enabled on the backend also known as the “Client Admin Tool” (CAT) where NAS is.**Reports enablement on CAT**

1. Login to CAT and look for the client > Entity

2. Under the entity tab, click on reporting profiles

3. The Reports will populate their status and columns (see next table)

**Columns under Reports Description**

1. Payments 

2. Disputes 

3. Retrievals

4. Bank Payouts

5. Card Payouts

6. Authentication

7. Fraud Detection

8. Reported Fraudulent Transactions

9. Balance

10. Financial Actions

11. Payouts

| **Documentation** | **URL** |
| --- | --- |
| Online Documentation | [https://www.checkout.com/docs/business-operations/use-the-dashboard/reporting](https://www.checkout.com/docs/business-operations/use-the-dashboard/reporting) |

Columns in the Report Section

| Financial Action | Balance Statement | Invoice | Payout Summary Report | Settlement Statement | Breakdown Report |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Payout Report | Date Range | Settlement Breakdown Payout Report | Balance Breakdown by Date Range |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Transaction Currency** **Transaction Currency Amount ** **Processing to Transaction currency FX rate** **Transaction to holding currency FX rate** **Fee detail** **Reserve rate** **Reserve deducted date** **Reserve released date** **Processing channel name** **Acquirer Reference Number** **Account Funding Transaction** **Scheme FX Adjustment Eligible** **Scheme FX Adjustment Processing Currency** **Scheme FX Adjustment Rate Applied** **Entity Segment** **Issuing Bank** **BIN** **Payment Type** **UDF 1** **UDF 2** **UDF 3** **UDF 4** **UDF 5** **Requested On UTC** **Processed On UTC** | **Transaction Currency** **Transaction Currency Amount ** **Processing to Transaction currency FX rate** **Transaction to holding currency FX rate** **Fee detail** **Reserve rate** **Reserve deducted date** **Reserve released date** **Processing channel name** **Acquirer Reference Number** **Account Funding Transaction** **Scheme FX Adjustment Eligible** **Scheme FX Adjustment Processing Currency** **Scheme FX Adjustment Rate Applied** **Entity Segment** **Issuing Bank** **BIN** **Payment Type** **UDF 1** **UDF 2** **UDF 3** **UDF 4** **UDF 5** **Requested On UTC** **Processed On UTC** | **Issuing** **Integrated Platforms** **Sub-entities currency accounts** **Reserve** **Billing Fees** **Risk Engine** **Authentication** **Network Tokens** **Intelligent Acceptance** **Operational Funding** **Timezone** | **Client Settlement Type; Net or Gross** | **Issuing** **Integrated Platforms** **Sub-entities currency accounts** **Reserve** **Billing Fees** **Risk Engine** **Authentication** **Network Tokens** **Intelligent Acceptance** **Operational Funding** **Timezone** | **Toggle On or Off** | **Acquirer Reference Number** **Merchant Category Code** **Mid** **Region** **Entity Country** **Issuer Country** **Card Category** **Card Type** **Account Funding Transactions** **Entity Segment** **Issuing Bank** **BIN** **Payment Type** **UDF 1** **UDF 2** **UDF 3** **UDF 4** **UDF 5** **Available on UTC** **Processed on UTC** | **Acquirer Reference Number** **Merchant Category Code** **Mid** **Region** **Entity Country** **Issuer Country** **Card Category** **Card Type** **Account Funding Transactions** **Entity Segment** **Issuing Bank** **BIN** **Payment Type** **UDF 1** **UDF 2** **UDF 3** **UDF 4** **UDF 5** **Available on UTC** **Processed on UTC** |
| --- | --- | --- | --- | --- | --- | --- | --- |

**Process flow: Enable report and/ or columns in a report**

1. The client reaches out to the Merchant Care Team or Account Managers

2. MCare/ AM investigate the report type or column in the report to enable

3. MCare/ AM raises a ticket to the Merchant Configuration Team

  1. Merchant Care should use the respective regional Merchant Configuration macro on Zendesk to create a side conversation with the Merchant Configuration team. Once the Merchant Configuration team has enabled the report, Merchant Care is responsible for closing the loop with the merchant

  2. AMs should raise a ticket to Merchant Configuration ([support_internal@checkout.com](mailto:support_internal@checkout.com)) in Salesforce

4. The MConfig team responds to the requester who will respond to the client

| The Merchant Configuration Team will enable all reports by default upon account creation and respective columns whose service/ product has been configured. |
| --- |

**Mandatory Column in reports**

The following columns are mandatory per product enabled on the merchant’s CAT.

| **Feature in CAT** | **Report name** | **Columns to be added** |
| --- | --- | --- |
| Authentication | 1. Balance Statement Report  2. Payout Summary Report | - Authentication |
| Fraud detection pro | 1. Balance Statement Report  2. Payout Summary Report | - Risk Engine |
| Minimum Billing | 1. Balance Statement Report  2. Payout Summary Report | - Billing Fees |
| Rolling Reserve | 1. Financial Actions By Payout Report  2. Financial Actions By Date Range  3. Balance Statement Report  4. Payout Summary Report | - Reserve Rate  - Reserve  - Deducted Date  - Release Date  - Reserve |
| IP (sub-entity config) | 1. Balance Statement Report  2. Payout Summary Report | - Integrated Platforms |
| Pay to Bank | 1. Payout Summary Report | - Pay To Bank |
| Account Funding Transaction | 1. Financial Actions By Payout Report  2. Financial Actions By Date Range | - Account Funding Transaction |
| Network Token | 1. Balance Statement Report  2. Payout Summary Report | - Network Tokens |
| Intelligent Acceptance | 1. Balance Statement Report  2. Payout Summary Report | - Intelligent Acceptance |
| Issuing | 1. Balance Statement Report  2. Payout Summary Report | - Issuing |
| Stablecoin settlement | 1. Payout Summary report | - Destination currency |

**Reports frequencies configured on CAT**

| **Report** | **ROW (default or per Sales ask)** | **MENA - specific** |
| --- | --- | --- |
| Settlement Breakdown | (still in beta phase) | (still in beta phase) |
| Balance Breakdown | (still in beta phase) | (still in beta phase) |
| Settlement Statement | Daily | Daily |
| Financial actions by date range | Weekly | Daily |
| Financial actions by payout | Weekly | Daily |
| Balance | Monthly | Monthly |
| Payouts | Weekly | Weekly |
| Invoice | Monthly | Monthly |

| **Documentation** |  |
| --- | --- |
| Confluence | [https://checkout.atlassian.net/wiki/spaces/MC/pages/5710349104/CAT+Overview-+MENA#Entity-Level-configuration](https://checkout.atlassian.net/wiki/spaces/MC/pages/5710349104/CAT+Overview-+MENA#Entity-Level-configuration) |

## Glossaries and Definitions:

For **Key Terms and Definitions** on Reports Issues, please see ****[Reports Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22435536667666-Reports-Glossary-Introduction) 

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Reports articles, please see ****[Reports Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22435569613330-Reports-Tools-Permissions)

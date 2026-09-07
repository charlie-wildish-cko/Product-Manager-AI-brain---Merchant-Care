---
id: 29392710165010
section_id: 29564292125202
title: "Tiered Pricing Fee Calculation"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29392710165010-Tiered-Pricing-Fee-Calculation"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-31T16:44:13Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K4MD5WPGG2J42W8S89TDFE10", "01K4W3NS6PHPQGC17G0DKXHE7P"]
label_names: ["L2", "SOP", "Troubleshooting guide", "Financial Experience", "Tiering pricing", "Pricing"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To understand Checkout's automated, tiered pricing model. It details how fee tiers are determined, the process of prospective and retrospective adjustments, and where these changes are reflected in financial reports and invoices.

**Problem / Solution: **Merchants and internal teams require clarity on how processing fees are calculated and adjusted as transaction volumes change month-to-month. This guide provides an overview of the automated tiered pricing system, including a calculation example.

## DESCRIBE THE ISSUE 💬

A merchant or account manager is questioning why their effective fee rate has changed or has noticed a **Tiered Pricing Adjustment** on their financial report or invoice. They need to understand the mechanics behind our tiered pricing model, which rewards business growth with better pricing. 

This includes understanding how we apply a rate at the start of the month, and then retrospectively adjust it based on the actual processing volume achieved during that month.

 

 

## KEY TAKEAWAYS 🔑

- 
**Prospective & Retrospective Model:** The system looks at the customer's total spending from **last month**. Based on that volume, it applies the corresponding **pricing tier** to all transactions for the **current month**. This is the **prospective** part-we're applying the previous month's data to the new month.

- 
**Monthly Calculation:** The system uses **Coordinated Universal Time (UTC)** to define a calendar month. This ensures a uniform billing period for all customers, no matter their time zone.

- The achieved fee tier applies to the entire processing volume for the billing period, not just the volume within that specific tier's band.

- 
**Net Processing Volume:** For variable fees based on processing value, the volume is calculated as the total of Captures, **net** of **Refunds**, **Chargebacks**, and **ClearingFailed** transactions for a given month. Only **Interchange++ (IC++)** transactions are included in tiering based on processing volume; **Alternative Payment Methods (APMs)** are excluded.

- 
**Reporting:** Adjustments are labelled as `Tiered Pricing Adjustment` in the Financial Actions Report and aggregated in the Adjustments column of the Balance Report. They appear on the _following_ month's invoice.

- 
**Scope:** Tiering can be applied at the Entity or Client level.

 

## TOOLING 📍

Click here to see the tools needed

| Tool | Access |
| --- | --- |
| [CAT (Client Admin Tool)](https://client-admin.cko-prod.ckotech.co/web/nas/) | Access is granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274) Environment: select the environment that you need   - Sandbox  -  Production Permissions:    - Super User (both environments)  -  Super Admin (sandbox only) Team Name: Merchant Care |
| [Dashboard (NAS)](https://dashboard.checkout.com/reports/all-reports) | - If you do not already have access to the Dashboard, submit a ticket to IT via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)   - Submit a request through this form, selecting "identity.checkout.com - Prod" for the environment or "identity-sandbox.checkout.com - Sandbox" for Sandbox |
| Looker | If you do not have access to any Looker report, submit a request via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)      If you already have Looker access, follow the steps below :    - Access to the Financial Actions Report looker is granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)   - Submit a request through this form, selecting "Other (please specify)" for the Type of enhanced access section.  - For the Business Case section, add a note related to your role and that access is required to perform your tasks. Add more information in the More Info box if needed. |
| Spreadsheet tool | You can use any spreadsheet tool like Google sheets, Excel or similar for reports. |

 

## PROCESS FOR UNDERSTANDING TIERED PRICING 🖊️

This process outlines how the tiered pricing model functions, from calculation to reporting. Standard checks in the **Client Admin Tool (CAT)** and financial reports are usually sufficient to resolve inquiries.

### Step 1. Calculation Model

Our tiered pricing works on a two-part cycle each month:

- 
**Prospective Application:** At the start of a billing period (e.g., November), we apply the fee rate from the tier the merchant achieved in the _previous_ period (October).

- 
**Retrospective Adjustment:** At the end of the billing period, we analyze the total volume. If the volume qualifies for a different tier, we retrospectively apply the new fee rate to all transactions from that period and issue a credit (rebate) or an additional charge (debit). An adjustment is only made if the merchant moves to a different tier. If they remain in the same tier, no adjustment occurs.

 
Click here to see an example of how prospective application and retrospective adjustment works**Prospective Application (The Start of the Month)**

Imagine you're a merchant named **"The Coffee Bean Shop."**

- Your pricing tiers are based on your monthly transaction volume:

  - 
**Tier 1:** up to $1,000 in volume at a 3.0% transaction fee

  - 
**Tier 2:** $1,001 - $5,000 in volume at a 2.5% transaction fee

  - 
**Tier 3:** over $5,000 in volume at a 2.0% transaction fee

- In **October**, you processed a total of **$3,500** in transactions - this volume put you in **Tier 2**

- At the start of **November**, the system "prospectively" applies the **2.5% fee** from your October Tier 2 to every transaction. So, for every coffee sale you make in November, you are charged 2.5% of the transaction amount.

**Retrospective Adjustment (The End of the Month) Prospective Application (The Start of the Month)**

At the end of **November**, we look at your total processing volume for the month

- 
**Scenario A: Your November volume is $4,000**

  - This still falls within **Tier 2**

  - Since you were already billed at the Tier 2 rate (2.5%), **no adjustment is needed**. Your final fee for November is simply the sum of all your transactions at 2.5%

- 
**Scenario B: Your November volume is $6,000**

  - This volume qualifies you for **Tier 3** with a better fee of 2.0%

  - The system "retrospectively" calculates your fees for all of November at the new 2.0% rate

  - Since you were initially charged 2.5% all month, we issue a **credit** to your account for the difference (0.5% of your total $6,000 volume). This credit will appear on your next statement, effectively giving you the better rate you earned.

- 
**Scenario C: Your November volume is $800**

  - This volume puts you in **Tier 1** with a higher fee of 3.0%

  - The system "retrospectively" applies the 3.0% rate to your $800 in volume

  - Since you were only charged 2.5% initially, we will issue a **debit** to your account for the difference (0.5% of your total $800 volume). This additional charge ensures you pay the correct, higher fee for the tier you actually ended up in.

 

 

### **Fee Types and Measurement**

  
Tiering can be applied to fees in three distinct ways:

| **Fee Category** | **Specific Fees Included** | **Tiering Measured By** |
| --- | --- | --- |
| **Gateway Fee** | Gateway Fixed Fee | **Count** or **Volume** |
| **Variable Fee** | Acquiring Premium Variable Fee | **Volume** only |
| **Other Fixed Fees** | Authorization, Card Verification, Void, Refund, Acquiring Premium, Authentication, and Fraud Detection fees. | **Count** only |

  
**Calculating Processing Volume:** For variable fees the processing volume for a given month is the total value of **Captures**, net of **Refunds**, **Chargebacks **and **ClearingFailed** transactions.

**Scope:** Only **IC++** (Interchange++) transactions are considered in the calculation based on **processing volume**. **APMs** (Alternative Payment Methods) are excluded from tiered pricing.  
  
💡**Note: **For variable fees measured by volume, we reward merchants for "good" volume - this means we calculate tiers based on processing volume _net_ of refunds and chargebacks.  
 

### 2. Check the Merchant's Current Tier

You can verify a merchant's active pricing tier within the Client Admin Tool (CAT).

- Open **Client Admin Tool (CAT)** and navigate to the merchant's entity

- Go to the **Pricing Profiles > Payment** page

- In the **Card scheme fees** section, you can see the currently applied fee rate (e.g., **Premium variable fee**) which corresponds to a specific tier in their agreement

  
  
 

**Example Calculation**  
Consider the following tiering model for Gateway fees, measured by count:

| **Tier** | **Number of Gateway Fees** | **Gateway Fixed Fee** |
| --- | --- | --- |
| 1 | 0 - 100,000 | $0.10 |
| 2 | 100,001 - 150,000 | $0.09 |
| 3 | 150,001 - 200,000 | $0.08 |
| 4 | 200,001+ | $0.07 |

Here is how the pricing adjusts over three months:

| **Period** | **Gateway Fee Instances** | **Tier Applied (Prospective)** | **Fees Charged** | **Tier Achieved (Retrospective)** | **Tiered Pricing Adjustment** | **Actual Billed Amount** |
| --- | --- | --- | --- | --- | --- | --- |
| **Oct 23** | 123,000 | Tier 1 ($0.10) | $12,300 | **Tier 2** | +$1,230 (Credit) | **$11,070** |
| **Nov 23** | 250,000 | Tier 2 ($0.09) | $22,500 | **Tier 4** | +$6,750 (Credit) | **$15,750** |
| **Dec 23** | 55,000 | Tier 4 ($0.07) | $3,850 | **Tier 1** | -$1,650 (Debit) | **$5,500** |

### 3. How to View Tiering Adjustments

Tiering adjustments are calculated on the first day of the following month.

- 
**Financial Reports:** You will see a credit or debit adjustment labeled `Tiered Pricing Adjustment` in the **Financial Actions Report** on the 1st of the month. These adjustments are aggregated under the **Adjustments** column in the **Balance Report**.  
  
 

- 
**Invoices:** Adjustments appear in the **Previous Period Tiered Pricing Adjustments** section of the invoice. An adjustment for October's processing, for example, is calculated on November 1st and will appear on the November invoice, which is generated on December 1st.  
  
  
  
  
  
  
💡Note: On an invoice, a **credit adjustment** (or rebate) is represented as a **negative amount**. This is because invoices list the fees being charged, so a credit is applied as a deduction from that total.

- This is shown in the invoice example below, where a tiering adjustment for €2,636.52 is listed as

- 
`€(2,636.52)` in the amount column, reducing the total fees.  
  

### 4. Verify the Applied Tier with Looker

To determine which tier was applied in a previous month, use the following Looker report.   
💡Note: The current pricing in **CAT** may not be the one applied in a previous month

- 
**Report:** Use this Looker link to gather the necessary data, pivoted by month: ****[Financial Actions Report](https://checkoutinternal.eu.looker.com/explore/ledger_financial_actions/finance_financial_actions_report?qid=jw2Q3XI909zB3RiMk79N4D&toggle=fil)**. **  
Use the Client ID you need to verify Tiering for in Looker

- 
**Calculate Processing Volume:** To see the total processing volume, exclude the `Premium Variable Fee` from the report's calculations.

- 
**Isolate Captures:** Filter the results by `Captures` only, as the Premium Variable Fee is only applied to captures.

- 
**Determine the Tier Rate:** Use the following formula to find the rate that was applied for that month: `Applied Rate = Premium Variable Fee / Captures`. This rate will correspond to a specific tier in the merchant's agreement.

💡Note: The final calculation may not be exact, as a currency conversion may have been applied between the processing and holding currencies.  
  
For calculations, you can also use the **Financial Actions** report downloaded from the Dashboard. However, Looker is often much easier to use, especially since some merchants have a very high number of transactions per month.

### Premium Fee Tiered Pricing Calculation Example

This example shows how to verify a **Previous Period Tiering Adjustment** from an invoice by reconciling it with the financial data and the merchant's tier configuration.
**Scenario:** A merchant's invoice shows a credit adjustment of **€(11,165.55)**. We need to confirm this amount is correct
  
The ****[Looker](https://checkoutinternal.eu.looker.com/explore/ledger_financial_actions/finance_financial_actions_report?qid=4HIdkqxfB2GE9AAfLzsrQZ) report shows the total for the Tiering pricing adjustment (in this case two adjustments were applied as there are two different currency accounts for EUR)  
  
  
**Gather Initial Data from the Financial Actions Report**
First, pull the key figures from the Financial Actions report for the processing period (e.g., January 2025). The most important figures are the total captures, refunds, and the premium fee that was initially charged.  
  
****[Looker](https://checkoutinternal.eu.looker.com/explore/ledger_financial_actions/finance_financial_actions_report?qid=jw2Q3XI909zB3RiMk79N4D&toggle=fil)
From the report, we gather:

- 
**Total Captures:** €4,466,222.12

- 
**Total Refunds:** €45,571.00

- 
**Fee Initially Charged:** €26,797.33

💡 Note: This initial fee was charged based on the tier the merchant achieved in the previous month (December 2024). In this case, the applied rate was **0.60%**.  
 
**2. Calculate the Net Processing Volume**
Next, calculate the net processing volume for the current period (January 2025). This is the volume used to determine the correct, retrospective tier.

- 
**Formula:** `Net Processing Volume = Total Captures - Total Refunds`

- 
**Calculation:** €4,466,222.12 - €45,571.00 = **€4,420,651.12**  
 

**3. Determine the Correct Tier**
Compare the **Net Processing Volume** against the merchant's fee tiers in Client Admin Tool (CAT) to find the correct tier for the month.

- 
**Tier 1:** €0 - €1,000,000 (**0.6%**)

- 
**Tier 2:** €1,000,000 - €1,500,000 (**0.5%**)

- 
**Tier 3:** €1,500,000 and above (**0.35%**)

The volume of **€4,420,651.12** qualifies for **Tier 3**, meaning the correct fee rate is **0.35%**.  
 
**4. Calculate the Correct Fee**
Now, calculate what the fee _should have been_ for the month. Apply the correct Tier 3 rate (**0.35%**) to the **Total Captures** volume, as the premium fee applies only to captures.

- 
**Formula:** `Correct Fee = Total Captures x Correct Tier Rate`

- 
**Calculation:** €4,466,222.12 x 0.0035 = **€15,631.78**

This calculation gives the precise fee that should have been applied for the month.

  
**5. Calculate the Final Adjustment**

Find the difference between the fee that was initially charged (at the **0.60%** rate) and the correct fee (at the **0.35%** rate).

- 
**Formula:** `Adjustment = Fee Initially Charged - Correct Fee`

- 
**Calculation:** €26,797.33 - €15,631.78 = **€11,165.55**

This result is a **€11,165.55 **credit (or rebate) owed to the merchant and shown in the **Previous Period Tiering Adjustments** section. This confirms the adjustment on the invoice is correct.  
  
💡Note: Our calculation may be slightly different figures from the actual adjustment due to currency conversions.
A more precise calculation can be made by including the **FX Markup**. From the same Looker report, add the `Total FX Markup Amount` to your totals for Captures and Refunds. Note that the FX Markup only applies to `Capture` and `Refund` transaction types.  
  
Captures = Total Captures + FX Markup on Captures  
Refunds = Total Refunds + FX Markup on Refunds  
  
Use these figures in your calculation to more closely match the final invoice amount.  
  

  
**Fixed Fee Count**

This ****[Looker](https://checkoutinternal.eu.looker.com/explore/ledger_financial_actions/finance_financial_actions_report?qid=6a7m9Qq0Q0GYUPvhKMNvJu&toggle=fil) can be used to get the total **count** of a fixed fee applied (e.g. Gateway Fixed Fee)   
 

## RESOLUTION **🛠️**

Once you have verified the Tiered Pricing and a potential adjustment using the steps in this guide, explain to the merchant (or the internal requester) how their monthly processing volume determined the correct tier and the resulting adjustment.

## ESCALATION** ⏫**

If you suspect a tiered pricing rebate or charge has been applied incorrectly, contact merchant's Account Manager and the **Billing **team. They can perform a corrective fee adjustment for the affected currency accounts.  
  
If, after you have investigated on a case and identified potential pricing issues, please escalate to the FE Pricing & Billing team either by requesting assistance in the `**#**fts-pricing-billing` Slack channel or by submitting a [Jira ticket](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277)  
  
Provide client and entity details and select the options below:  
**Product team** > **FTS**  
**FTS Product Team **> **Pricing&Billing**  
 

## RESOURCES** ****⭐**

| **Case Examples** | **Related** |
| --- | --- |
| - [Case 41797](https://checkout1360.zendesk.com/agent/tickets/41797)  - [Case 40485](https://checkout1360.zendesk.com/agent/tickets/40485)  - [Case 47974](https://checkout1360.zendesk.com/agent/tickets/47974) | - [Confluence - NAS Financial Reporting & Reconciliation FAQ](https://checkout.atlassian.net/wiki/spaces/MER/pages/5509021735/NAS+Financial+Reporting+Reconciliation+FAQ)  - [Understanding Checkout.com’s tiered pricing](https://docs.google.com/document/d/1PbCeOSutYSzPs1RdGaSqRosmUulg48UbqljMZwg0r9I/edit?tab=t.0) |

## FAQ❓

How does client-level tiering work?For client-level tiering, we assess the processing volume across the entire client group to determine the tier. However, the rebate or charge adjustment is applied individually to each entity under that client, proportional to its own volume. These adjustments will appear in each entity's reports.How can I check which tier a merchant is currently in?Open the Client Admin Tool (CAT), navigate to the Pricing Profiles > Payment page for the merchant, and check the fee in the Card scheme fees section. The fee rate currently being applied corresponds to a specific tier in their agreement.

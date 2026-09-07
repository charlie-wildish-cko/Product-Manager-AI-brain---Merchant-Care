---
id: 21991197596562
section_id: 23045903280658
title: "NAS Merchant does not require a signed document"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991197596562-NAS-Merchant-does-not-require-a-signed-document"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:37:30Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHQKPVKA7XAZRYSRWE7JRH4"]
label_names: ["case_settlements", "merchant_requests_balance_confirmation_for_a_specific_date", "global", "case_settlements_issue_balance_confirmation", "nas_merchant_does_not_require_a_signed_document"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

Below are the procedural steps for when merchants are requesting confirmation of the balance that CKO is holding and is expected to settle (mostly seen in PTC/PTB configuration).

## Process Steps

If the merchant doesn’t require a signed document and is a Net Settled merchant, Merchant Care can educate the merchant to self-serve in Dashboard and obtain the **Balance Report** themselves.

**Internal information only - the below information cannot be shared with merchants:**

- Only **Net Settlement Merchants** can self-serve in the Dashboard and obtain their Processing Balance, Rolling Reserves & ultimately Balance Confirmation

- For **Gross Settlement Merchants**, agents need to contact the Billing team as they need to perform some internal checks before issuing the balance confirmation

  - To contact the Billing team, use the relevant billing team’s regional macro in Zendesk to create a side conversation from your merchant’s ticket. For further information, please see [here](https://checkout.atlassian.net/wiki/spaces/CHEC/pages/5991727266/Case+Handling+-+SOP#Emailing-internal-partner-teams%3A)

**Checking if a Merchant is Net or Gross Settled **

1. Login to Client Admin Tool (CAT)

2. Select the required Entity

3. Navigate to Reporting Profiles

4. Search for “Invoice” in the column Report Type

5. You will then see the below under “Client Settlement type” where you can get confirmation if the merchant is Net or Gross Settled

As an alternative, check the merchant’s Invoice by following the below steps:

- Check the  top right-hand side of the invoice:

  - If “Paid in Full” is showing, the merchant is Net Settled

  - If “Pending” is showing, the merchant is Gross Settled

 

**Merchant-facing information: **the below information can be shared with merchants:

This Balance report shows the Total Processing Balance, Rolling Reserves, and Balance Confirmation. Below is step-by-step guidance to obtain all of these:

1. Log in to the Dashboard

2. Go to “Reports” in the Dashboard account and select “New report”

3. Select the required report from the dropdown list, in this case, “Balance”

4. Select the timeframe that the report should cover by selecting the relevant dates. For example: if the request is to obtain balance confirmation as of 31st December 2023, you should set the covered period to 31st December 2023 by double-clicking on the date, as shown in the below screenshot

 **Note:**

- If the request is for a balance confirmation for a specific month, you should always set the date for the last day of the month e.g.:

  - For a balance confirmation for November 2023, the date range would be 30th November 2023 – 30th November 2023

  - For a balance confirmation for December 2023, the date range would be 31st December 2023 – 31st December 2023

1. Select the account (entity) that the report is required for (if applicable)

2. Select “Generate report” on the top right-hand corner of the page

1. The below screen will be displayed, click on the green icon to download the report

2. The downloaded report will be in an Excel Sheet Format

3. Open the Excel Sheet and navigate to Column J. You will see the Breakdowns and Balances & Payouts displayed. As we are only looking for the balance confirmation, you should add a filter to column J to choose only “Balances & Payouts” as shown below

4. If the **Total Processing Balance** is also required, the below steps should be followed:

  - Navigate to columns:

    1. AS (Closing Available Balance)

    2. AT (Closing Pending Balance)

    3. AU (Closing Payable Balance)

  - The total of those three columns will be the merchant’s Processing Balance

  - E.g. in the below example, the total would be 1000

5. If **Rolling Reserves** information is required, the below steps should be followed:

  - Go to columns:

    1. AV (Closing Collateral Balance)

    2. AW (Closing Operational Funding Balance)

  - The total of the two columns will be the Rolling Reserve.

  - E.g. in the below example, the total would be 10000

6. 
**For the Final Balance Confirmation:**

  - Navigate to columns:

    1. AS (Closing Available Balance)

    2. AT (Closing Pending Balance)

    3. AU (Closing Payable Balance)

    4. AV (Closing Collateral Balance)

    5. AW (Closing Operational Funding Balance)

  - The total of the Rolling Reserves and the Processing Balance is the Balance Confirmation,

  - E.g. in the below example, the Balance Confirmation is 11000.

**Note**: The above-inserted figures are only for illustration purposes for understanding, and they are fictitious values.**Note**: Internal only - Retool Checks available:To confirm that the information displayed in the balance report from the Dashboard is correct, agents can check Retool by following the [Exceptional Use Cases section guidance in the Balance Confirmations SOP.](https://checkout.atlassian.net/wiki/spaces/CHEC/pages/6148456463/Balance+Confirmations+SOP#Exceptional-Use-Cases)

## Glossaries and Definitions:

For **Key Terms and Definitions** on Transactions as well as an **introduction into MENA Gateway and non-Gateway merchants**, please see ****[Settlements Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/21991207693458-Settlements-Glossary-Introduction)   For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Transactions articles, please see ****[Settlements Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/21991176789266-Settlements-Tools-Permissions)

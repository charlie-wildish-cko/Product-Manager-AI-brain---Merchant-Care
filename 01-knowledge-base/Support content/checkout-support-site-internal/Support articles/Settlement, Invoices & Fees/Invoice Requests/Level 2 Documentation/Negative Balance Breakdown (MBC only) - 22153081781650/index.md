---
id: 22153081781650
section_id: 28632977066386
title: "Negative Balance Breakdown (MBC only)"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22153081781650-Negative-Balance-Breakdown-MBC-only"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:37:33Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHQKPVKA7XAZRYSRWE7JRH4"]
label_names: ["row", "case_settlements", "case_settlements_issue_negative_balance", "negative_balance_breakdown_mbc", "abc_decommissioning", "mbc_decommissioning", "hub_decommissioning", "case_settlements_issue_invoice_adjustments"]
user_segment_ids: [11003606966930]
archive: false
---

Introduction

**   Note: The below article is to be used by Merchant Care Level 2 only**

The article below contains procedural steps for a negative balance breakdown for transactions on MBC. Merchant Care receives many queries regarding negative balance breakdowns of transactions where the merchant (or Account Manager) requires a list of all transactions. The Treasury team has mostly moved these negative balances to NAS which usually appears on NAS invoices. Merchants will contact Merchant Care to get clarity on them. Process Steps

1. You will need access to the [Finance MBC Statements](https://checkoutinternal.eu.looker.com/explore/statements/finance_mbc_statements?qid=9ICfDrTRZAeoK1YdNPTIcp&origin_space=2347&toggle=fil) looker report. If you do not already have access, please request it through this [form](https://checkoutsupport.freshservice.com/support/catalog/items/682) specifying _Other (please specify) _the **type of enhanced access** and the looker link above in the **More Info** box.

2. Open the [Finance MBC Statements looker](https://checkoutinternal.eu.looker.com/explore/statements/finance_mbc_statements?qid=9ICfDrTRZAeoK1YdNPTIcp&origin_space=2347&toggle=fil) to extract the statements report and check for the negative balance (the amount is usually provided in the request ticket)

3. Use the **Business** **ID** and date range to filter the data

  1. You can download the data in CSV or other formats to make it easier to work with. Once you have the data, the negative amount can be found under _Carry Forward (Remittance Currency)_. Occasionally an adjustment against the amount appears under _Adjustments (Remittance Currency)_

  
  
  
 

1. Filter by _Remittance Currency_ if there is more than one currency on the statement (you can also filter directly on Looker), before exporting the file

  1. Make a note of the date (under the _Period To Date_ column) in the same row you found the negative balance  
  

2. Scroll down until the values under _Carry Forward (Remittance Currency)_ (or _Gross Settlement Amount In Settlement Currency_) increase (please note these are negative amounts) until you encounter multiple ‘0’ or until you see another adjustment (under _Adjustments (Remittance Currency)_)

3. Note the date under the _Period From Date_ column related to the row where you found the amount. You can use a preceding date; it does not have to be exact

4. If you notice there may still be additional rows with negative amounts that do not appear in the extracted data you can adjust the date range for a wider period in looker in step 1 above  

5. The extracted file contains Sales, Refunds, Disputes and fees - the same can be sent to the merchant

6. If the merchant replies requesting a detailed breakdown of transactions, then we need to use the Python script (far_download.py) to extract Financial Actions (FAR) using the dates range we noted in the previous two steps, then proceed to step 10

7. Open and run the Python script. You require access to Snowflake to run the Python script. Specifically, you would need access to these tables:  
LANDING.ADMINISTRATION.DBO_BUSINESS,  LANDING.ADMINISTRATION.DBO_CHANNEL.

  1. If you do not already have access, please request it following the instructions on this Confluence [page](https://checkout.atlassian.net/wiki/spaces/CDE/pages/6022857247/How+To+-+Request+Access+to+Snowflake+Data)

8. Choose the **Business ID** (option 2), type the **Business ID** and press **enter**

9. Type the **start** and **end date** in YYYY-MM-DD format, press **enter** and then type a random ticket ID, then press **enter**  

10. When running the script, a browser page will open to verify that you are logged in to Snowflake. You may need to log in again. Once the script has completed extracting the files, you will find them in the folder specified in the script

11. Use the other Python script to merge the files into one. Simply add the extracted files from the first Python script we used previously into the folder specified in this second Python script for merging files and running the script. You will find the final file in the same folder

12. Open the file and check the total amount under the _Payout Currency Amount_ column. If the total does not match the negative balance, try with a wider or a narrower date range  
 

13. Send the final file to the merchant or the requester

14. If you cannot match the total with the initial negative balance or the negative balance was not found on the first looker extract, contact the Treasury Payments team using the appropriate regional team macro on Zendesk for more information on the balance

If the Treasury Payments team indicate that the negative balance is related to Cost of Sales, contact the Cost of Sales Operations teams at [schemepricingandinterchange@checkout.com](mailto:schemepricingandinterchange@checkout.com), using the relevant macro on Zendesk to do so.For **Key Terms and Definitions** on Transactions as well as an **introduction into MENA Gateway and non-Gateway merchants**, please see ****[Settlements Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/21991207693458-Settlements-Glossary-Introduction)   For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Transactions articles, please see ****[Settlements Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/21991176789266-Settlements-Tools-Permissions)

---
id: 23046329852050
section_id: 23045954287122
title: "Transaction Declines with Specific Bins"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/23046329852050-Transaction-Declines-with-Specific-Bins"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-24T11:37:20Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "global", "case_transactions_issue_bin_enamblement", "merchant_needs_to_add_a_bin"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**   

To support merchants experiencing transaction declines related to specific Bank Identification Numbers (BINs). It provides steps to verify and manage BINs on decline lists.   

**Problem:** A transaction is being declined with a specific Bank Identification Number (BIN).   

**Solution:** Investigate and manage BIN settings within the fraud detection system to resolve or intentionally maintain the decline.   
 INTRODUCTION TO THE ISSUE 💬           

 A merchant is reporting that transactions are being declined for a specific BIN, often with a related error code such as RC 40205. The merchant may also be requesting that a specific BIN be added to the decline list due to suspected fraudulent activity.

⚠️ This issue impacts the transaction process and can be resolved by checking and modifying settings in the fraud detection tools.           

See the related [Fraud detection - global rule policy article](https://checkoutint.zendesk.com/hc/en-us/articles/27120611282322-Fraud-Detection-Global-Rule-Policy) 

KEY TAKEAWAYS 🔑               

- A **Bank Identification Number (BIN)** consists of the first 6 to 8 digits of a payment card and identifies the issuing institution.

- Merchants or agents can check and manage BINs on a decline list within the fraud detection system.

- Changes to the BIN list can be made by users with an admin or risk manager role in the dashboard.

- Any complex changes to adding or removing a BIN require a review from the risk team, with final execution by the merchant configuration team.

PROCESS FOR BIN DECLINE RESOLUTION 🖊️                   

### Step 1. Access the Decline Lists

- Navigate to the **Lists** section within the fraud detection dashboard

- Click on **Decline lists** and then select the **BIN (8)** tab to view the current list of blocked BINs

- Check for the BIN reported by the merchant to see if it is already on the list      

                    

### Step 2. Verify Merchant Permissions

- Confirm that the merchant has the [appropriate role](https://www.checkout.com/docs/business-operations/use-the-dashboard/manage-users/user-permissions) (**admin** or **risk manager**) to modify the decline list

- If the merchant does not have the required permissions, the request must be reviewed and executed by the appropriate internal teams (risk team and merchant configuration team)

### Step 3. Add or Remove the BIN

- 
**To remove a BIN:** If the BIN is on the list and the merchant wants to accept transactions from it, the merchant with the correct role can remove it. For more complex cases, follow the escalation process

- 
**To add a BIN:** If the merchant wants to block transactions from a specific BIN due to fraud, they can add it to the decline list if they have the necessary permissions                          

## RESOLUTION ⚒️

Following these steps should result in the BIN being correctly managed on the decline list, either allowing previously declined transactions to be processed or ensuring that transactions from a fraudulent BIN are blocked.               

- **Remediation Steps:** If a legitimate BIN was accidentally added to the decline list, removing it will resolve the issue. If a fraudulent BIN was not on the list, adding it will prevent future declines.                  

- 
**Check for Resolution:** Confirm with the merchant that the issue is resolved by having them attempt a new transaction with the card or by monitoring for new decline reports.           

## ESCALATION** ⏫**

Escalate the case if:

 

**Required Information for Escalation:**             

- Case number

- Merchant name

- Specific BIN in question

- Screenshots of the decline errors (e.g., RC 40205)

- Confirmation of the merchant's role and their request (e.g., to add or remove a BIN)

FAQs⁉️
         

What is a BIN?

A Bank Identification Number (BIN) is the first 6 to 8 digits of a payment card. It identifies the institution that issued the card.Who can change the decline lists?

Users with an admin or risk manager role in the dashboard can make changes to the lists.What is a "decline list"?

A decline list is a feature in the fraud detection system that automatically declines any transaction matching a listed attribute, such as a specific BIN.

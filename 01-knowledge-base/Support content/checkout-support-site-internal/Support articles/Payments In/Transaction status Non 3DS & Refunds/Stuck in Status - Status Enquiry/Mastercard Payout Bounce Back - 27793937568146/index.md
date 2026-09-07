---
id: 27793937568146
section_id: 23045937114898
title: "Mastercard Payout Bounce Back"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/27793937568146-Mastercard-Payout-Bounce-Back"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-03-18T13:39:42Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["mastercard", "mastercard_transaction_status", "card_payout", "mastercard_payout_bounceback"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article:**

To determine whether a Mastercard Payout transaction has bounced back or resulted in a chargeback. It provides step-by-step instructions for accessing and querying the relevant data in Snowflake. 

**Case type: **Payments in

**Issue Type: **Transaction status (Non 3DS & Refunds)

Reason: Stuck in status / status enquiry

Mastercard Payouts can sometimes fail or be reversed due to incorrect account details or cardholder disputes. Quickly identifying these issues helps resolve merchant problems and reduce customer impact. This SOP outlines a standard process for Merchant Care to investigate cases using Snowflake and internal tools.

This procedure applies to Merchant Care handling Mastercard payouts.

## ONE-TIME ACCESS SETUP  (First-Time Users Only) ⚠️

These steps are required only once to gain initial access to the necessary database.

- Locate the Database in Datahub

  - From the Okta dashboard, search for and open **Datahub - Prod**

  - In the Datahub search bar, enter MC_CHARGEBACKCONSOLIDATED

  - 
From the search results, select the database that is **not** marked as "Private"

- Submit an Access Request

  - 
Click the three-dot menu icon associated with the database and select **Request Access**

  - An access request form will appear. Fill it out with the following information:

    - 
**Why do you need access to this data?** Select "Run ad hoc queries in Snowflake"

    - 
**Who are you requesting this access for?** Enter your name

    - 
**Business Justification**: Enter "Request Access for MASTERCARD Chargeback-Related Queries"

    - 
**When do you need this data until?** Select a date at least five years in the future.

  - 
Click **Request** to submit the form, this will automatically create a Jira for your request

## PROCESS FOR INVESTIGATING A PAYOUT TRANSACTION 🖊️

Follow these steps for each payout investigation

- Navigate to Snowflake

  - 
From the Okta dashboard, access **Snowflake**

  - If it is your first time using Snowflake, you will be prompted to personalise your experience. Select the role **"Other"** and click **"Get Started"**

- Prepare the Worksheet

  - In the left-hand menu, hover over the icons and select **Worksheets**

  - 
Click the **+** button in the top-right corner to create a **New SQL Worksheet**

- Configure and Execute the Query

  - Before running a query, ensure your Role and Warehouse are correctly set:

    - 
**Role**: Set this to your name (e.g. YOVEEN BHOTOOA)

    - 
**Warehouse**: Set this to MEDIUM_WH

  - 
In the worksheet space, paste the following script: 

```select * from landing.integration.mc_chargebackconsolidated where arn IN ('ENTER_ARN_HERE')
```

  - Replace ENTER_ARN_HERE with the specific ARN of the transaction you are investigating

  - 
Click the **Run** button

- Analyse Results and Take Action

  - 
**If the query returns an entry**: This confirms that a bounce-back has occurred. You must transfer the case to the **Disputes Team** for further inquiry

  - 
**If the query returns no results**: This confirms that no bounce-back has occurred for the given ARN

**💡Tip: **Saving Your Worksheet : For easier access in the future, you can rename and save your worksheet

- Click the three dots next to the worksheet's title

- 
Select **Rename** and give the worksheet a descriptive name, such as "MC Payout Bounce-back"

## ESCALATIONS 🔺

- 
**Bounce Back Confirmed:** If your Snowflake query returns a result, you **must** transfer the case to the **Disputes Team** for further investigation. Use the macro:

| Macro: Transfer- Disputes |
| --- |

- 
**Issues During the Process:** If you encounter any problems checking the status of the transaction, please contact the **Disputes Team** with your question at `disputes@checkout.com`.

## FAQs ❓

 What is an ARN?

- ARN stands for Acquirer Reference Number. It is a unique number that identifies a specific transaction. You need this number to run the query in Snowflake.

  What should I do if the query returns a result?A result from the query confirms that the payout has bounced back. You must escalate the case to the Disputes Team for handling. What does it mean if the query returns no results?If the query returns no results, it means that as of the time of the query, no bounce back has been recorded for that specific transaction ARN.
    For **Key Terms and Definitions** on Transactions as well as an **introduction into MENA Gateway and non-Gateway merchants**, please see ****[Transactions Glossary](https://checkoutint.zendesk.com/hc/en-us/articles/21991201065106-Transactions-Glossary-Introduction)**.  **
 
 
 
 
 
 
 
 
 
For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Transactions articles, please see ****[Transactions Tools & Permissions](https://checkoutint.zendesk.com/hc/en-us/articles/21991176883474-Transactions-Tools-Permissions)**.**

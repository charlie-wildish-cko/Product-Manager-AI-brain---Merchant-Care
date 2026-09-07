---
id: 29309284028818
section_id: 29564292125202
title: "Understanding Fees and Pricing"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29309284028818-Understanding-Fees-and-Pricing"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-30T17:12:48Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K4MD5CAPQ3GPKCANYT57ZMTP", "01K4MD5RGPEX365Q6QQQNN4HNG", "01K4MD5WPGG2J42W8S89TDFE10"]
label_names: ["L2", "Troubleshooting guide"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To find the specific pricing and fee structure for a particular merchant by locating the different pricing components in the Client Admin Tool (CAT) and in other available documentation and reports.

**Problem / Symptom**: A merchant's complete fee structure is not located in a single place, making it difficult to accurately provide pricing details to merchants and internal teams. This guide provides a step-by-step process for locating both Checkout fees configured in CAT and pass-through scheme and Interchange fees in other documentation.

## DESCRIBE THE ISSUE 💬

A merchant's pricing information is located in various tools, documents and reports. Checkout fees are found within the Client Admin Tool (CAT), while pass-through costs from card networks (Scheme and Issuer fees) and are detailed in other available documentation and reports. 

This guide gives a general overview of where to find these various components to build a clearer picture of a specific merchant's fee structure.

 

## KEY TAKEAWAYS 🔑

- Merchants are typically on either an Interchange++ (IC++) or a Blended pricing model

- The **Payment Pricing Profile** in CAT is the primary location for most configured fees, including processing, dispute, authentication and fraud charges

- FX markups and pricing for Value Added Services (VAS) are located in their own dedicated sections within CAT

- Card Scheme and Interchange fee rates are not in CAT. They must be looked up in internal documentation based on transaction specifics, though some Interchange settings can be found in CAT

- Premium Variable Fees can be tiered by processing value (volume), while Gateway and other fixed fees can be tiered by the volume or count of applied fees  
 

## TOOLING 📍

Click here to see the tools needed

| Tool | Access |
| --- | --- |
| [CAT (Client Admin Tool)](https://client-admin.cko-prod.ckotech.co/web/nas/) | Access granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274) Environment: select the enviroment that you need   - Sandbox  -  Production Permissions:    - Super User (both environments)  -  Super Admin ( sandbox only) Team Name: Merchant Care |
| [Dashboard (NAS)](https://dashboard.checkout.com/reports/all-reports) | - If you do not already have access to the Dashboard, submit a ticket to IT via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274).  - Submit a request through this form, selecting "identity.checkout.com - Prod" for the environment or "identity-sandbox.checkout.com - Sandbox" for Sandbox |
| Looker | If you do not have access to any Looker report, submit a [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274) for a new account.       If you already have Looker access follow the steps below :    - Access to Financial Actions Report looker is granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274).  - Submit a request through this form, selecting "Other (please specify)" for the Type of enhanced access section.  - For the Business Case section, add a note related to your role and that access is required to perform your tasks. Add more information in the More Info box if needed. |
| Spreadsheet tool | You can use any spreadsheet tool like Google sheets, Excel or similar for reports. |
| Google Drive | Access should have already been granted via your account credentials. |

 

## PROCESS FOR FINDING PRICING COMPONENTS 🖊️

### Finding Fees Configured in the Client Admin Tool (CAT)

Follow these steps to find the Checkout configured fees for a merchant:
**Step 1. Locate the Merchant's Entity**
 In CAT, search for the merchant (client) and navigate to the correct entity associated with them. Fee configurations are stored at the entity level, with the exception of **Minimum Billing** which is at client level.
**Step 2. Check the Payment Pricing Profile**
Under the entity menu, navigate to **Pricing Profiles > Payment**. This is where the main fee schedule for that entity is located. Clicking on the pricing profile (there can be more than one) will show more details including the currency. A detailed profile can include:

- 
**Processing Fees and Tiered Pricing:** Several fees can be configured with tiers. The basis for the tiering depends on the fee type:

  - The **Premium Variable Fee** is tiered based on **processing value (volume)** only.

  - 
**Gateway Fees** can be tiered based on the **count of applied fees **or** processing volume**.

  - Other fees, such as **Authentication** and **Fraud Detection fees**, can be tiered based on the **count of applied fees**.

- 
**Card scheme fees:** Settings that determine how Interchange and Payment gateway fees are handled, which can be broken down by specific card schemes (Visa, Mastercard, Amex, etc.). Card fees can be one of the three **Pricing type**:

  - 
**IC++ (**Interchange Plus Plus)

  - 
**Gateway Services Only **(transactions are not settled by Checkout but by other third-party acquirers (TPA)) Checkout will charge only gateway fees

  - 
**Blended** (which is currently used by only a few merchants)

  - 
**Payment gateway fees** can be broken down into four charge types: `Authorization fee`, `Card verification fee`, `Void fee`, `Refund fee`  
  

  - 
**Dispute Fees:** Specific charges for disputes, which can include `Chargeback fee`, `Representment fee`, `Retrieval fee`, `Predispute Accepted Fixed Fee` and `Predispute Declined Fixed Fee`.

  - 
**Authentication Fees: **`Authentication fixed fee`

  - 
**Fraud Detection fees:** `Risk engine fee`

**Step 3. FX Configurations**

- Forex conversion markup can be applied (only to capture or refund)

- Under the entity menu, go to **FX Configurations > Pay to card FX** (for card payouts) and **FX Pricing** for general major, minor or exotic currency markups

- 
markups are categorized by:

  - Major currencies

  - Minor currencies

  - Exotic currencies

For a detailed list of which currencies fall into each category, refer to the public documentation on FX fees here: [FX Fees](https://www.checkout.com/legal/fx-fees)

**Payment pricing profile**
  

 
**Step 4. Check VAS Pricing Profile:**
Under **Pricing Profiles > VAS Pricing Profile**, use the **Pricing UI** to search for the entity **by client name, client id or entity by ID** to find pricing for additional services fees (e.g. Network Token, Intelligent Acceptance, etc.)

### Scheme and Interchange Fees

These fees are charged by card networks and issuing banks and passed through to the merchant (not in **CAT**).

- 
**Issuer Fee (Interchange):** This fee is charged by the **issuing bank** (the bank that issued the customer's card). The fee amount depends on several factors, including the location of the merchant and cardholder, and the type of card (e.g., consumer or commercial, debit or credit).

- 
**Scheme Fee:** This is a fee paid directly to the card scheme (e.g., Visa, Mastercard) for the use of their network and services.

- To find the exact rate for a transaction, please consult the internal **Scheme Fee documentation, **which is available on a shared Google drive here:  
https://checkout.atlassian.net/wiki/spaces/SPI/pages/1389397060/Output+for+Merchants+IC+SF+pdfs

The documents are divided by region and inside the folders by transaction type (e.g. **Sales**, **ChargeBack** (CB) , **Pay to Card**, **AFT**, etc.) and then by **merchant's country**. 
  
 
Type of fee charged for a specific transaction can be found in the **Financial Actions report.**
If you are generating FAR from dashboard, make sure to select `Fee Detail` before generating the report.
  
 
Fee Summary report is another useful report which does not include single transactions but a summary of the fee charged.
  

  
 
Financial Actions Looker Report
To find a specific fee detail for one or more transactions you can also use the FAR looker (this is just an example - please fill the fields using your transactions IDs, entity IDs, date range, etc.)
****[Looker](https://checkoutinternal.eu.looker.com/explore/ledger_financial_actions/finance_financial_actions_report?qid=5atugK2cSdJ1vId8rNqmlZ)
  
  
💡Two other Interchange-related settings that can be configured in CAT:

- 
**Predictive IC:** Due to the delay between when a transaction is processed and when the final Interchange fee is received, a feature called **Predictive IC** can be enabled. This allows Cost of Sales internal system to pre-calculate the Interchange fee.

- 
**Return IC on Refund:** For some merchants, a setting can be enabled to return the Interchange (IC) fee on refunds. This is often configured with a cap or threshold (not in visible in CAT)

  

## RESOLUTION 🛠️

Once you have located all the relevant pricing components from CAT and the external documentation, you can accurately inform the merchant about their fee structure or investigate which fees should apply to a specific transaction.

## ESCALATION ⏫

If you find that a client's configured pricing in CAT seems incorrect or does not match their contract, first contact their Account Manager (AM). If the pricing is confirmed to be incorrect, it may be a configuration issue that the AM needs to be escalated to Merchant Config team. 
If after you have investigated on a case and identified potential pricing issues, please escalate to the FE Pricing&Billing team either by requesting assistance in the `**#**fts-pricing-billing` Slack channel or by submitting a [Jira Ticket](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277) [](https://checkoutsupport.freshservice.com/support/catalog/items/588) using the form 588  
  
Provide client and entity details and select the options below :  
**Product team** > **FTS**  
**FTS Product Team **> **Pricing&Billing**

## RESOURCES** ****⭐**

| **Case Examples** | **Related** |
| --- | --- |
| - [Case 67735](https://checkout1360.zendesk.com/agent/tickets/67735)  -  [Case 67762](https://checkout1360.zendesk.com/agent/tickets/67762) | - [Region Calculation](https://checkout.atlassian.net/wiki/spaces/Oracle/pages/5971509255/Region+Calculation)  - [Interchange Fees Explained](https://www.checkout.com/blog/cko-explains-interchange-fees)  - [Refund Interchange](https://checkout.atlassian.net/wiki/spaces/SPI/pages/1389430086/Refund+Interchange)  -  [FX Fees](https://www.checkout.com/legal/fx-fees) - merchant facing article |

## 

## FAQ❓

What is the difference between IC++ and Blended pricing?**IC++ (Interchange++):** This is a transparent model where the three main cost components are broken out: the **Interchange** fee (to the issuing bank), the **Card Scheme** fee (to Visa/Mastercard), and the **Acquirer **fee (++). **Blended:** This model combines all costs into a single, simplified rate for the merchant, which is less transparent but easier to understand.How can I see exactly which Interchange fee was applied to a specific transaction?Generate the **Financial Actions Report** from the Dashboard or Looker. When using the Dashboard, you must select the `Fee Detail` option before generating the report. This will show a line-by-line breakdown of all fees applied to each transaction.

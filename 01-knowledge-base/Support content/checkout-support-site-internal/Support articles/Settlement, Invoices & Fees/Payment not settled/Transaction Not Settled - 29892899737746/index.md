---
id: 29892899737746
section_id: 21991144652050
title: "Transaction Not Settled"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29892899737746-Transaction-Not-Settled"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-04-09T08:42:02Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K6FTFB3H6KVTXT24KJE8PXX3", "01K6FTFMPX0TBD95H0YS9PEEQN", "01K6FTFZFQK360GXR52PPZ1KK4"]
label_names: ["L2", "Troubleshooting guide", "Transaction settlement", "Settlement failure"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To investigate why a specific transaction (e.g. successful captured transaction) has not been settled to a merchant. 

**Problem / Symptom**: A transaction has been successfully processed, but the funds have not been settled to the merchant's account. This guide provides steps for checking for common blockers like negative balances, risk arrears and configuration issues.

## DESCRIBE THE ISSUE 💬

When a transaction is not settled, it's necessary to investigate various systems to identify the cause. Common reasons include a negative balance on the currency account, arrears delays configuration setting, settlement threshold or frequency settings, or issues with the client's configuration in the Client Admin Tool (CAT). 

 

## KEY TAKEAWAYS 🔑

- The first step is always to check the **Financial Actions Report (FAR)** in Looker

- Settlement failures are often caused by one of the following main reasons: **Negative Balance**, **Arrears **delays configuration, **Settlement threshold **or** frequency**, **Gateway-Only** service configuration, or a **CAT configuration issue**

- Investigation requires using multiple tools, including **Looker**, **Retool**, and the **Client Admin Tool (CAT)**

- Each potential cause can be verified by checking a specific section within these tools.

 Please be aware that the FAR Looker is currently experiencing an issue where it does not always display the correct settlement ID.   
  
Use the Settlements in dashboard when searching for transactions.  
  

## TOOLING 📍

Click here to see the tools needed

| Tool | Access |
| --- | --- |
| [CAT (Client Admin Tool)](https://client-admin.cko-prod.ckotech.co/web/nas/) | Access granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274) form 302 Environment: select the enviroment that you need   - Sandbox  -  Production Permissions:    - Super User (both environments)  -  Super Admin ( sandbox only) Team Name: Merchant Care |
| [Dashboard (NAS)](https://dashboard.checkout.com/reports/all-reports) | - If you do not already have access to the Dashboard, submit a ticket to IT via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)   - Submit a request through this form, selecting "identity.checkout.com - Prod" for the environment or "identity-sandbox.checkout.com - Sandbox" for Sandbox |
| Looker | If you do not have access to any Looker report, submit a [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274) for a new account.       If you already have Looker access follow the steps below :    - Access to Financial Actions Report looker is granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274).  - Submit a request through this form, selecting "Other (please specify)" for the Type of enhanced access section.  - For the Business Case section, add a note related to your role and that access is required to perform your tasks. Add more information in the More Info box if needed. |
| Spreadsheet tool (if needed) | You can use any spreadsheet tool like Google sheets, Excel or similar for reports. |

 

## INVESTIGATING SETTLEMENT ISSUES PROCESS 🖊️

Follow these steps to diagnose why a transaction has not settled.

**Check the Financial Actions Report (FAR) on Looker**

- Begin by looking up the transaction in the FAR to get an initial overview and confirm its status

- Both Looker links point to the same explorer but use different views.  
  
****[Looker 1](https://checkoutinternal.eu.looker.com/dashboards/7480?Payment+ID=&Processed+on+Date=&Client+Name=&Client+ID=&Entity+ID=&Entity+Name=)  
or  
****[Looker 2](https://checkoutinternal.eu.looker.com/explore/ledger_financial_actions/finance_financial_actions_report?qid=waLDSREZAmehXUC07xkHkE&toggle=fil)  
  
****

- 
If **Payout Reference **in looker results is populated, it means the transaction has been settled.  
 
⚠️ The settlement ID in the dashboard is not always correct - the ID in the **looker** report is the correct one.  
  
  
 

- 
**Investigate Potential Causes:** Based on the information from the FAR, investigate the following potential blockers:  
  
  
 

  - 
**Negative Balance:** Check the **Currency Account Balances** app in Retool to see if a negative balance is preventing the settlement.  
  
  
 

  - 
**Arrears configuration:** Arrears are delays deliberately set, measured in days, between when a transaction is received (**Requested On**) and when it is processed by Checkout (**Processed On**).

  - These are configured in the **Client Admin Tool (CAT)** and can be set for specific currencies or an entire entity.  
  
Let's assume a merchant has a daily settlement schedule:  
**With 0-day arrears**: A transaction captured on **Monday** is processed on Monday and included in the next settlement batch.  
**With 2-day arrears**: A transaction captured on **Monday** waits about two days, is processed on **Wednesday**, and is then included in the settlement batch that follows.  
  
In CAT, navigate to the correct **entity:**

    - Go to the **Arrears configuration** section - this page shows any delays that have been set

    - Click on the specific **currency** you are investigating to see more details

    - On the next page, you will see two sections:

      - 
**Applicable arrears**: This top section lists general arrears applied at the entity level or to all currencies.

      - 
**Custom Currency account arrears**: This bottom section lists arrears specific to the currency you selected.   
Check this section first, as specific currency settings override general entity-level settings  
  
  
  
  
  
  
  
 

  - 
**Settlement Threshold & Frequency:** In CAT, review the **Payout Schedules** to check two key settings:

    - 
**Threshold amount**: Confirm the available balance has met the minimum amount required for a payout. **Available balance** can be checked in the Retool **Currency Account Balances** app  
 

    - 
**Frequency**: Check the configured schedule (e.g., daily, weekly on a specific day)  
  
  
  

  - 
**Gateway-Only configuration:** Use transaction **Processing Channel** (this can be found in **Traffic Insights** Retool app or in Financial Actions report in Looker) to confirm if the transaction was "gateway-only," meaning the funds will not be settled to the merchant by Checkout but by another TPA (e.g. SABB MPGS)  
  
  
  
  
  
 

  - 
**CAT Configuration issues:** Perform a final review of the client's configuration in CAT for any other potential issues which may be escalated to other teams.

  - For instance, if a merchant sends transaction captures but a pricing profile is missing or has been configured incorrectly, those captures will not be settled.

## RESOLUTION 🛠️

Once you have identified the root cause from the steps above, you can take the appropriate action to resolve the issue, such as advising the merchant or the requester on their negative balance, or correcting a configuration setting in CAT.

## ESCALATION ⏫

If you find that a client's configured pricing in CAT seems incorrect or does not match their contract, first contact their Account Manager (AM). 
If the pricing is confirmed to be incorrect, it may be a configuration issue that needs to be escalated to Merchant Config team using the correct Zendesk macros which will vary depending on region.  
  

## RESOURCES** ****⭐**

| **Case Examples** | **Related** |
| --- | --- |
| - [Case 82115 - Negative balance](https://checkout1360.zendesk.com/agent/tickets/82115)  - [Case 79781 - Gateway-only](https://checkout1360.zendesk.com/agent/tickets/79781) | - [Confluence - NAS Financial Reporting & Reconciliation FAQ](https://checkout.atlassian.net/wiki/spaces/MER/pages/5509021735/NAS+Financial+Reporting+Reconciliation+FAQ) |

## FAQ❓

What is the first step in investigating a failed settlement?The first step is always to check the transaction in the Financial Actions Report (FAR) on Looker to get an overview of its status.Where can I check if a merchant has a negative balance?You can check for a negative balance in the Retool app under "Currency Account Balances." This is a common reason for settlements to be paused.What should I do if I suspect a CAT configuration issue?Review the client's settings in the Client Administration Tool (CAT), paying close attention to the payment pricing profiles (for risk arrears) and payout schedules (for thresholds and frequency), to identify any misconfigurations.

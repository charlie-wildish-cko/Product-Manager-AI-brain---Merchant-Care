---
id: 22435576029714
section_id: 22329315187858
title: "How to Troubleshoot Report Generation Issues"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22435576029714-How-to-Troubleshoot-Report-Generation-Issues"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-23T10:01:43Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQBAM2Q5EGSKD3634VFBT"]
label_names: ["global", "case_reports", "case_reports_issue_report_not_generated", "report_not_generating"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

When a merchant reports they are unable to generate or download a report from their dashboard.REPORT GENERATION ISSUES 💬

A merchant might get in contact because their dashboard reports won't generate or because some data is missing. This can happen for a few reasons, like incorrect user permissions, dashboard settings that need adjustment, or mistakes in the user’s input. 

For reports to be downloaded from the Dashboard, they must first be enabled in the backend (known as the Client Admin Tool or CAT). The Merchant Configuration Team handles this and enables all reports and relevant columns by default when the account is created.PROCESS TO TROUBLESHOOT REPORT ISSUES🖊️

### Step 1: Check Permissions and Access

The most common reason a report won't generate is that the user lacks the necessary permissions. Certain roles, like **Disputes Operator** and **IAM (Identity & Access Management) Admin**, are not set up to view or download reports.

- Confirm the user's role and check if they have the correct permissions. The table below shows which roles can view or generate payment reports:

| Permission | View / Generate Payment Reports |
| --- | --- |
| Admin | Yes |
| Developer | Yes |
| Disputes Operator | No |
| Identity & Access Management Admin | No |
| Support Manager | Yes |
| Read Only | Yes |

- If the user does not have the required permissions, they need to be upgraded by the **Dashboard Owner** or **Administrator** of the account

🔗 For guidance on the tools and permissions needed for reports, refer to the  [Reports Tools & Permission](https://www.checkout.com/docs/business-operations/use-the-dashboard/manage-users/user-permissions). documentation. 

### Step 2: Investigate Configuration Issues

Incorrect settings on the dashboard, like wrong filters or parameters, can prevent a report from generating. Additionally, a report might fail if the conditions for generating it aren't met.

⚠️ For example a **Balance Report** can only be generated for the previous day or earlier

- Check if the user is trying to generate a report for a future date

- Review the dashboard's settings and configurations to ensure they are correct

- If changes are needed, escalate the case to the Merchant Configuration team to action

  
    

      
        
        
      
      
        
          
        
        
          
          
        
      
    

| **Scenarios to investigate** |  |
| --- | --- |
|  | 1. No product configured                2. No Column selected                3. No transaction |

  

### Step 3: Check for User Input Errors

If a user enters incorrect filters or criteria, the report may not generate because there's no data to display.

- Verify the user's input, including any filters or date ranges they've selected

- Advise the user to double-check their inputs to ensure they are correct

ADDITIONAL SOLUTIONS ⚒️

- Use the Looker tool instead of escalating issues

- 
****[Finance Unified Report](https://checkoutinternal.eu.looker.com/explore/finance_unified_report/finance_core_unified_report_clearing) helps extract transaction details like transaction ID and fields to identify decline trends

- Search transactions using information from the merchant such as authorization code or reference number

- Alternatives include ****Payin and ****Payin event reports

- 
**** [Financial Action Report](https://checkoutinternal.eu.looker.com/explore/nas_adjustments/lightning_adjustments_aggregate): Helps merchants reconcile statements, invoices, and investigate transaction fees. Files from the Dashboard for large periods may be too big to download or share.

ESCALATION ⬆️

**From Merchant Care to Merchant Configuration Team:** When a client needs a report or column enabled, the Merchant Care Team or Account Manager raises a ticket to the Merchant Configuration Team.

| Use the Macro: Transfer> Merchant Configurations > Region |
| --- |

Use the** #ask-dashboard Slack Channel i**f the problem persists, follow the bookmark on the Slack channel.

RESOURCES ⭐️

| Zendesk Example Cases | Linked Articles |
| --- | --- |
| [Tickets 16345](https://checkout1360.zendesk.com/agent/tickets/16345) | Merchant Article: [Retrive Reports Documentation](https://www.checkout.com/docs/business-operations/retrieve-reports) |
| [Tickets 17155](https://checkout1360.zendesk.com/agent/tickets/17155) |  |

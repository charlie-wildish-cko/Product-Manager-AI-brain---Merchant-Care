---
id: 22397292406034
section_id: 28533338298898
title: "Dashboard User Permissions"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22397292406034-Dashboard-User-Permissions"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-17T16:31:39Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQBAM2Q5EGSKD3634VFBT"]
label_names: ["global", "case_reports", "case_reports_issue_custom_report", "abc_decommissioning", "mbc_decommissioning", "hub_decommissioning", "who_can_download_reports", "dashboard", "dashboard_permissions", "dashboard\\_users", "user_permissions"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article:**

To verify a user's role and permissions in the Client Dashboard to determine if they have access to specific functionalities or reports.

**Problem:** A user cannot access a specific feature or report in the Client Dashboard

**Solution:** Verify the user's role and permissions to confirm they have the required accessINTRODUCTION TO DASHBOARD USER PERMISSIONS 💬

A merchant has contacted us because they or one of their users cannot access a function within the Dashboard, specifically the ability to view or download payment reports. 

💡 See the merchant facing article: [User Permissions](https://www.checkout.com/docs/business-operations/use-the-dashboard/user-permissions) for in-depth information you can share with the merchantPROCESS FOR VERIFYING USER PERMISSIONS 🖊️

This process involves a standard check using internal tools to confirm a user's assigned role and then cross-referencing that role with the necessary permissions.Option 1. Check Roles and Permissions in the Dashboard

- Log in to the ** Dashboard**

- Go to **Settings** and select **Roles and Permissions**

- This section provides a detailed view of which roles have which permissions

Option 2. Check User Role in Client Admin Tool

- Navigate to the **Client Admin Tool**

- Go to **Dashboard** and select **Dashboard Users**

- Locate the user in question to see their assigned role

| Permission | Report Type | Pre-defined Roles |
| --- | --- | --- |
| View and generate payment reports | General Reports | Admin, Developer, Disputes manager, Read only, Risk manager, Support manager |
| View and download reports | Network Tokens Dashboard | Admin, Support manager |
| Read access (viewing) | Network Tokens Dashboard | Admin, Disputes manager, Read only, Risk manager, Support manager |
| View and download reports | Vault Dashboard | Admin, Risk manager, Support manager |
| Read access (viewing) | Vault Dashboard | Admin, Disputes manager, Disputes operator, Risk manager, Support manager |
| View and download monthly fees invoices | Monthly fees invoices | Admin |
| View settlements details and download transaction breakdown report | Transaction breakdown report for settlements | Admin, Support manager |
| Download files | Files associated with sub-entities | Account application only, Admin, Support manager |

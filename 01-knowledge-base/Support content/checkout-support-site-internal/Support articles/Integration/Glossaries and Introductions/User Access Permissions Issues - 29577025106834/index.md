---
id: 29577025106834
section_id: 22197990418450
title: "User Access Permissions Issues"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29577025106834-User-Access-Permissions-Issues"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-29T11:15:29Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTFS8D8APRZBB2MBC3AJM8Y1", "01K5ER27JGGYDZNDZBMEYJ4B09", "01K5ER2KMWY2QDQXY0NKH5Y0RR", "01K5ER32QDCJ3Y8V3TX7WGMA7P"]
label_names: ["access_and_permission_issues", "access_issue", "dashboard_permissions"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

When a user on the account cannot perform a specific action, or the merchant as an admin, needs help creating a new custom role or managing user access.

**Problem:** Merchants need to manage user access securely but may not know how to assign the correct permissions. This often leads to users being unable to perform their required tasks.

**Solution:** This guide provides the steps for an account Admin to troubleshoot access issues, manage user permissions, and create custom roles effectively within the Dashboard.

## DESCRIBE THE ISSUE 💬

Administrators for a merchant account, are responsible for managing what other users can see and do in the Dashboard. A user may report they are unable to perform a necessary action (like a refund), or the admin may need to create a new role with a specific set of permissions that doesn't currently exist. This guide will help you support account Admins and Owners who need to manage user roles and permissions.

 
 

## KEY TAKEAWAYS 🔑

- Most access issues are due to missing permissions in the user's assigned role

- Admins can edit a user's role or create a new custom role under `Settings Roles and permissions`

- The `user_management` permission is required to invite, edit, or manage other users

- Certain high-level permissions (like user management and processing settings) cannot be assigned to custom roles

## RESOURCES 📍

| Tools | Case Examples | Related |
| --- | --- | --- |
| [Checkout.com Dashboard](https://dashboard.checkout.com/) | [Example 1](https://checkout1360.zendesk.com/agent/tickets/37798) [Example 2](https://checkout1360.zendesk.com/agent/tickets/69656) | [Manage Users Documentation](https://www.checkout.com/docs/business-operations/use-the-dashboard/manage-users) |

## PROCESS FOR MANAGING USER PERMISSIONS 🖊️

**Scenario 1: A User Cannot Perform a Specific Action**

When a user reports they can't do something like process a refund or view disputes, the issue is almost always related to their role's permissions. Talk the Admin through these steps:

- 
**Sign in** to the Dashboard

- Navigate to **Settings Roles and permissions**

- Select the user you wish to edit

- Click the **Edit User** button

- You can either:

  - Assign a different, more appropriate role from the dropdown

  - Edit the permissions for the user's currently assigned role

- Click **Save User** to apply the changes

**Scenario 2: Create and Assign a New Custom Role**

If the default roles don't fit their team's needs, merchants can create new roles with a specific set of permissions. Talk the Admin through these steps to create the custom role:

- Sign in to the Dashboard

- Navigate to **Settings Roles and permissions**

- In the _Popular roles_ section, select **View all roles**

- Under _Organization roles_, select **New role**

- Enter a **Role name** and **Description**

- Under **Permissions**, select all the relevant permissions for the new role

- Select **Create custom role** to save

- 
**Assign the New Role:** Once the custom role is created, you can assign it to a new user when sending an invitation, or assign it to an existing user by following the steps in Scenario 1

**⚠️Warning:** You must assign at least one permission to a custom role. Certain high-level permissions are reserved for default Admin or Account Owner roles and cannot be assigned to custom roles, including User management, managing team security settings, and managing processing settings.
**Scenario 3: A User Cannot Manage Other Users or Roles**

This is a very common access-related query.

- 
**Root Cause:** The user lacks the `user_management` permission, which is required to invite users, edit users, or manage roles.

- 
**Solution:** The user needs to contact an Account Owner or an Admin within their organization. That person can then grant them the necessary permissions by editing their assigned role.

## RESOLUTION ⚒️

- 
**Expected Result:** After following these steps, the user access issue will be resolved. Users will have the appropriate permissions to perform their tasks, and custom roles will be created and assigned as needed, ensuring secure and efficient team management.

- 
**Remediation Steps:** After updating a user's permissions or assigning a new role, ask the user to log out and log back in. Have them attempt the action they were previously unable to perform. It should now be successful.

- 
**Rollback/Recovery:** If you grant a user incorrect permissions, you can easily revert the change by editing the user again and re-assigning their previous role or removing the incorrect permissions. Custom roles can be edited or deleted from the `Roles and permissions` screen.

## ESCALATION** ⏫**

- If your organization has no users with Admin or `user_management` permissions left on the account and is locked out from managing the team, escalate the issue to the **#ask-dashboard** Slack channel for assistance.

 
 

## FAQs** ****❓**

Why can't I invite new users or edit roles?

You do not have the necessary `user_management` permissions. Please contact the Account Owner or an Admin in your organization to have these permissions added to your role.How can I find out who the Admin on my account is?

Navigate to the **Settings Roles and permissions** section in the Dashboard. The list of users will show the role assigned to each person, allowing you to identify who has the Admin or Account Owner role.Can I delete a user?

Yes. In the **Roles and permissions** section, click the three-dot menu icon next to the user's name. This will open a dropdown menu with options to Edit, Delete, or Revoke access for that user.

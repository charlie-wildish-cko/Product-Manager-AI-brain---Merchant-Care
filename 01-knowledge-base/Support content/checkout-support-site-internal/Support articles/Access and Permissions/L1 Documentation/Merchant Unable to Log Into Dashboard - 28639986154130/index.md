---
id: 28639986154130
section_id: 22286660216722
title: "Merchant Unable to Log Into Dashboard"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/28639986154130-Merchant-Unable-to-Log-Into-Dashboard"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-11-12T09:48:08Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTFS8D8APRZBB2MBC3AJM8Y1"]
label_names: ["unable_to_log_in", "password_reset_process", "locked_out", "access_issue"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

When a merchant contacts you with an access issue related to their Dashboard account. Use this article to troubleshoot login problems, password resets and SSO or MFA issues.

## INTRODUCTION TO LOGIN ISSUES** 💬**

This manual provides a comprehensive guide for handling inquiries from customers who are unable to access their Dashboard. A customer may be experiencing a Dashboard access issue if they report the following:

- Inability to log in to their account

- Issues with password resets

- Problems with SSO or MFA authentication

**Dashboard Login Methods**

There are two ways to log in to the Dashboard:

- 
**Single Sign-On (SSO)** SSO is an authentication feature that allows users to securely access multiple applications and systems with a single set of login credentials. This feature is available to NAS (New Account Structure) merchants in any region who have an identity provider that supports SAML 2.0. The merchant's Identity Provider (IDP) administrator is responsible for managing access, user permissions and SSO configurations.

- 
**Password + Multi-factor Authentication (MFA)** When logging in with an email and password, multi-factor authentication (MFA) is required. MFA provides an additional layer of verification for Dashboard access. If your organization leverages single sign-on (SSO), MFA will not be available within the Dashboard. There are two types of MFA methods that can be configured for an account:

  - 
**Authenticator application**: Use an authenticator application, such as Google Authenticator, Okta Verify or Microsoft Authenticator.

  - 
**Security key or biometric authenticator**: Use a biometric method, such as a fingerprint or a security key device. If both MFA methods are set up, the security key or biometric authentication takes priority over the authenticator app. 

💡Shared or group accounts are not supported. Ensure that all of users sign in using their own credentials. After configuring an MFA method for the account, you must always have a valid MFA method to log in.

 

## KEY TAKEAWAYS 🔑

- Self-service is the primary method for password resets; agents should only perform a manual password reset if a merchant cannot use the self-service option

- Password reset links are valid for only one hour

- Temporary passwords should only be shared directly with the dashboard user

 

## PROCESS FOR LOGIN ISSUES 🖊️

### Step 1: Identify the Sandbox or Production Environment

First, ask the customer whether they are having trouble accessing the **Sandbox** or **Production** environment. This will ensure accurate troubleshooting from the start.

### Step 2: Confirm the User's Registration and Activation Status

Begin by checking if the merchant's email address is registered and if their account has been activated.

💡 The email address a merchant uses to contact Checkout may be different from the one they use to access the Dashboard. 

To avoid unproductive troubleshooting, always ask in your first reply (when guiding them to a self-service solution) whether the email address they are using to access the Dashboard is the correct one, and ask them to provide the correct one if it isn't.

- Confirm if the email address provided by the Merchant is registered on the Dashboard

- 
**If the user is registered but not yet activated**: Please guide the merchant to contact their company's administrator (Admin) to request to be added to the Dashboard. For security reasons, we cannot add users on our end. For information on how to add users, please refer to this article: [Add or Remove Users](https://checkoutint.zendesk.com/hc/en-us/articles/22346705342994-Add-or-Remove-Users)

- 
**If the activation link has expired (and the user has not completed Dashboard onboarding)**: As part of best practice for security reasons, we cannot resend activation links directly. The merchant's company administrator must do this.

- Please ask the merchant to have their administrator resend the link via Okta Admin. If they are unable to do this, Checkout can assist by using the Okta identity tool. If you need access to the Okta identity tool, you can request it on [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274) via the Help Desk Admin.

### Step 3: Confirm the Login Method

If the user's registration is confirmed, ask them how they typically log in to the Dashboard. There are two methods:

- **Password + MFA**

- **SSO (Single Sign-On)**

You can check which login method they use in Dashboard > Settings > User permissions>Authentication method field

RESOLUTION ⚒️

The issue can often be resolved by the customer themselves or by their company's administrator by following these steps. Encourage users to self-serve first by following the steps below, or proceed to the 'support an agent can provide' section if they're unable to.

### If the user is not registered, or registered but not yet activated

- Guide the user to contact their company's administrator (Admin) to request to be added to the Dashboard. For information on how to add users, please refer to this internal article: [Add or Remove Users](https://checkoutint.zendesk.com/hc/en-us/articles/22346705342994-Add-or-Remove-Users).

| Use the Macro: Access issue first response- User not registered on dashboard |
| --- |

### If the activation link has expired

- Please ask the user to have their administrator resend the link. If they are unable to do this, you can assist them by using the Okta identity tool. 

| Use the Macro: Access issue first response- User Expired |
| --- |

💡 Note: If you need access to the Okta identity tool, you can request it [](https://checkoutsupport.freshservice.com/support/catalog/items/121) on [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274) (request as Help Desk Admin).

### If a customer with Password + MFA is unable to log in

- Guide them to the help article [Reset Dashboard password](https://support.checkout.com/hc/en-us/articles/14327316567826-Reset-Dashboard-password) and ask them to try it themselves first. If the issue persists, you can take action to resolve this.

| Use this Macro: Access issue first response- Password+MFA |
| --- |

### If a customer with SSO is unable to log in

- Guide them to contact their company's IDP administrator. If the IDP administrator cannot resolve the issue, the Support team will escalate the case to the IAM team for further investigation. 

| Use this Macro: Access issue first response- SSO user login issue |
| --- |

### Support an Agent Can Provide

If the merchant cannot resolve the issue through self-service, you can assist using the Okta identity tool.

### Password Reset

- Access the relevant **Okta Identity tool** (**Production** or **Sandbox**)

  - [Production Okta Link](https://authcheckout-admin.okta.com/admin/dashboard)

  - [Sandbox Okta Link](https://authsandboxcheckout-admin.okta.com/admin/dashboard)

- Search for the user's email address, if a user profile appears, you have two options:

### Recommended- Reset with a link

Utilize the **Reset Password** link (expires after 1 hour). Once this is done, inform the merchant that a password reset link has been sent and they should follow the instructions to reset their password within the hour. If you are dealing directly with the user, please use the macro below.

| Use this Macro: Password reset- link valid for 1 hour |
| --- |

### Reset with a temporary password

Use the Okta Admin tool to obtain a temporary password. 

  
⚠️**Important Note**: The temporary password must be sent **only** to the Dashboard user, not to a group email or other individuals in the email thread.

If others are in the email thread, create a side conversation and provide the temporary password using the appropriate macro from the Access & Permissions macro folder

| Use this Macro: Password Reset - temporary password - production account or Password Reset - temporary password - sandbox account |
| --- |

### Resend Activation Link

For users who have been recently added to the Dashboard but have not yet completed the onboarding process, search for their email address and select **Resend Activation Email** in the Okta admin tool.

### SSO Configuration Check

If a merchant uses Okta as their identity provider, the user profile will be listed as being "sourced by SAML 2.0 IdP." This confirms the SSO configuration.

If the SSO issue is beyond the merchant's IDP admin's control, escalate the case to the IAM team. 

## ESCALATION** ⏫**

If the issue cannot be resolved using the steps above, escalate the case by creating a ticket for the IAM team, including the details of the problem and the troubleshooting steps you have already taken.

When escalating, please ask the customer to provide the following information:

- A screenshot of any error messages

- The date and time the error occurred (including the time zone)

- The exact steps taken to produce the error (e.g "I clicked the login button," "I attempted authentication via the SSO provider" )

- The email address used to attempt login

- The type and version of the browser used

 

## RESOURCES 📍

| Tools | Related Articles |
| --- | --- |
| Okta admin tool:   - [Production](https://authcheckout-admin.okta.com/admin/dashboard)  - [Sandbox](https://authsandboxcheckout-admin.okta.com/admin/dashboard)  - [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274) | - [Account Ownership Transfer](https://checkoutint.zendesk.com/hc/en-us/articles/22346721814034-Account-Ownership-Transfer)  - [Add or Remove Users](https://checkoutint.zendesk.com/hc/en-us/articles/22346705342994-Add-or-Remove-Users)  - [Dashboard User Permission Changes](https://checkoutint.zendesk.com/hc/en-us/articles/22346721911058-Dashboard-User-Permission-Changes)  - [Password Reset Link- External Article](https://support.checkout.com/hc/en-us/articles/14327316567826-Reset-Dashboard-password) |

 

## FAQs** ****❓ **

Can Merchant care agents add users?For security reasons, we cannot add users directly. Please guide the merchant to have their company's administrator (Admin) do this.Can Mercant Care agents resend an activation link?

- For security reasons, we cannot resend activation links directly. Please guide the merchant to have their company's administrator (Admin) do this.
What if a user's email is not registered in the Dashboard?If a search in the Okta admin tool shows no data, it means the email is not registered. This could be a typo or an unregistered user. Ask the merchant for the correct account under which the user is registered.What should I do if a merchant with an IDP account needs a password reset?

- 
Contact their IDP Administrator. If the issue is beyond the Admin's control, submit a request to the IAM (Identity and Access Management) Team through [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277). Include a diagnosis of the issue from their IDP admin

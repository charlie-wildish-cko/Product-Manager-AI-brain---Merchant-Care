---
id: 22346749106194
section_id: 26930276318610
title: "Password Reset Process"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22346749106194-Password-Reset-Process"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-30T16:49:47Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTFS8D8APRZBB2MBC3AJM8Y1"]
label_names: ["global", "case_access", "case_access_issue_password_reset", "password_reset_process"]
user_segment_ids: [11003606966930]
archive: false
---

## Process Steps

If the user cannot self-serve (see [Resend activation link & self-serve password reset article](https://checkoutint.zendesk.com/hc/en-us/articles/22346749066130-Resend-activation-link-self-serve-password-reset)), Merchant Care should take the below steps to try and reset the merchant’s password:

1. 
**Login: **Access the relevant Okta admin tool console link for the dashboard based on the environment: 

  1. 
[Production/a,](https://authcheckout-admin.okta.com/admin/dashboard) or 

  2. 
[Sandbox](https://authsandboxcheckout-admin.okta.com/admin/dashboard).

2. 
**Search User:  **Enter the merchant's email address in the search bar.
Existing User:

  1. A user profile will appear under "People."

  2. Click on the user profile.

  3. 
**Reset Option 1:** Utilize the "Reset Password" link (expires after 1 hour).  
****

    1. Once this has been done, inform the merchant that a password reset link has been sent to the e-mail address and that they should follow the instructions to reset their password within the hour.   
If we're dealing directly with the user, please use the macro “Password Reset - link valid for 1 hour” in the Access & Permissions macro folder. 

  4. 
**Reset Option 2: **Reset the password by sending a temporary password

    1. Use the OKTA Admin link (see above) to obtain the temporary password.

    2. 
**Important note: **the temporary password must be sent to the dashboard user ONLY.

    3. If other individuals are in the email thread, create a side conversation and provide the temporary password using one of the below macros accordingly, all of which can be found in the Access & Permissions macro folder: 

      1. **“Password Reset - temporary password - production account”**

      2. **“Password Reset - temporary password - sandbox account”**

 
Non-Existing User:

  1. If you notice that no data is displayed in Okta admin, this means that the email is not registered in the Dashboard. In this case, ask the merchant for the account under which the user is registered and inform them that no data is displayed during the investigation.

  2. 
**Notes:**

    1. If a merchant's account is set up with **IDP**, they'll need to contact their Account Admin for help.

    2. 
**Common scenarios: **this scenario could occur due to a typing error or a user not being registered on the dashboard. 

**Additional Notes:**

- Use the NPOA Macro to save any necessary details in the case during the reset process.

- If, after following the above steps, the problem persists, escalate the case to the IAM/Access team using this [Jira link](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277).

## Glossaries and Definitions:

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Access & Permissions articles, please see ****[Access & Permissions Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22346741212818-Access-Permissions-Tools-Permissions) For **Key Terms and Definitions** on Access & Permissions Issues, please see ****[Access & Permissions Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22346737667986-Access-Permissions-Glossary-Introduction)

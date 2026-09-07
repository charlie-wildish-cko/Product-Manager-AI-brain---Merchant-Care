---
id: 22346738014994
section_id: 22286660216722
title: "Single Sign-On (SSO) for Merchants"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22346738014994-Single-Sign-On-SSO-for-Merchants"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-30T17:14:26Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTFS8D8APRZBB2MBC3AJM8Y1"]
label_names: ["global", "sso", "case_access", "case_access_issue_sso"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

When assisting merchants who with SSO setup 

## INTRODUCTION TO SSO 💬

Single Sign-On (SSO) for merchants is an authentication feature that allows users to securely access multiple applications and systems with a single set of login credentials. This feature is available to NAS (North America and Singapore) merchants in any region who have an identity provider that supports SAML 2.0.

Merchants' Identity Provider (IDP) administrators are responsible for managing access, user permissions, and SSO configurations.  

**💡Tip:** When speaking with merchants, clearly explain the purpose of the IDP admin's role in setting up SSO

 

## PROCESS STEPS 🖊️

To enable SSO, a merchant must work with their Identity Provider (IDP) administrator. As an agent, you can check the configuration only.

### Identify if a merchant account is configured with SSO

- 
**Through the Checkout.com Dashboard:** Navigate to the **Settings** menu and select **User Permissions**

****

- 
**Through the Okta Admin Tool:** If a merchant uses Okta as their identity provider, the user profile will be listed as being "sourced by SAML 2.0 IdP."

****

⚠️ A single user cannot be a member of two different client accounts through SSO simultaneously. To resolve this, one of the user's accesses would need to be renamed. The merchant should work with their IDP admin to manage this.

 

## ESCALATION ⬆️

## Submit a request for SSO-related issues

- If the SSO issue is beyond the merchant's IDP admin's control, submit a request to the IAM (Identity and Access Management) Team through [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277)

- Include a diagnosis of the issue from their IDP admin

 

## RESOURCES ⭐️

| Case Example | Links |
| --- | --- |
|  | [Single-sign-on external documentation](https://www.checkout.com/docs/business-operations/use-the-dashboard/single-sign-on)  [SSO Configuration-Known issues](https://checkout.atlassian.net/wiki/spaces/ACK/pages/5684593100/SSO+Configuration+-+Known+Issues#:~:text=IDP%2Dinitiated%20login%20not%20working&text=IDP%2Dinitiated%20login%20redirects%20to%20Dashboard%20email%2Fpassword%20login&text=Okta%20shows%20Unknown%20Profile%20Attribute%20when%20user%20tries%20to%20log%20via%20their%20IDP%20for%20the%20first%20time?search_id=8fda9ed8-d731-4516-ad2f-86d4f7684535) |

 

## FAQs** ****❓**

- What are the IDP admin responsibilities?**Managing Access and Permissions:**
Create and assign user roles
Ensure users have appropriate access to necessary tools and data
**SSO Configuration and Troubleshooting:**
Set up and maintain SSO configurations
Address common issues like login redirects, attribute mapping, and role assignments
**Monitoring and Updating User Access:**
Keep user access current with organizational needs
Automate updates to merchant accounts
Create custom restricted roles for different teams

- Can a user be a member of two different client accounts through SSO?No. A user cannot be a member of two separate client accounts through SSO. The merchant's IDP admin must rename one of the accesses to resolve this conflict. 

 

## Glossaries and Definitions:

For **Key Terms and Definitions** on Access & Permissions Issues, please see ****[Access & Permissions Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22346737667986-Access-Permissions-Glossary-Introduction)  

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Access & Permissions articles, please see ****[Access & Permissions Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22346741212818-Access-Permissions-Tools-Permissions)

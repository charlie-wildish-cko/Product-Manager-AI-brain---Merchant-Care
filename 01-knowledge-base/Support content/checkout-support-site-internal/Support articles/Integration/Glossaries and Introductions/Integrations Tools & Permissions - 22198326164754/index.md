---
id: 22198326164754
section_id: 22197990418450
title: "Integrations Tools & Permissions"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22198326164754-Integrations-Tools-Permissions"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-31T17:04:44Z"
permission_group_id: 26838654181266
content_tag_ids: ["01H8EDHC0MTG4YFD7E4B42CE0V"]
label_names: ["global", "glossaries_and_introductions", "case_integration", "integrations_tools_and_permissions"]
user_segment_ids: [11003606966930]
archive: false
---

## Tools & Permissions

Below are the tools that Merchant Care use to handle issues related to Integrations:

| **Tool** | **Permission** |
| --- | --- |
| **Zendesk** | - Required permission: Agent |
| **Salesforce** | - Internal CKO Staff permission |
| **Dashboard** | - Production access |
| **CAT** | - Super User (Production) - Super Admin (Sandbox)  - Reason: To resolve merchant-related issues raised through Salesforce |
| **Snowflake** | - [https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)  - Requesting team: Operations  - Why you need access: Query / Analyse Data  - What data do you need to access in Snowflake: Specific role: TECHFIN_PLATFORM_ANALYST |
| **Retool** | - Environment: Production   - Application Name: Traffic insights, report generator, Create Security Deposit & Release dates, Currency Account Balances, payout-search, payment-tool, HarmoniaClient, Merchant Hosted Pages Enablement  - Permission: Viewer - you can use and interact with apps  - Once access is granted please contact Valeriia Chirkova who can enable this |
| **Cloudflare** | - Follow the steps in [this guide](https://checkout.atlassian.net/wiki/spaces/ITPS/pages/5623054518/Cloudflare+Access+-+Client+Setup).  - Once Cloudflare is connected, you’ll have access to private internal applications based on your Okta Group Membership |
| **Github** | - Organisation: Existing Organization   - GitHub Organisation: cko-customer-support, cko-tech-finance  - Additional notes: fts-application-support |
| **Looker** | - Business Case: As part of our support duties it is often useful to run some of the looker reports or point the requester into some of those looker reports to answer support queries.  - Type of Account: New Account  - Access Details:    -  [Financial action report](https://checkoutinternal.eu.looker.com/explore/ledger_financial_actions/finance_financial_actions_report?toggle=fil&qid=3M6V05FVyxTZN8rc4ydKaz):    - [Shared Folder](https://checkoutinternal.eu.looker.com/folders/2346)    - Boards in shared folder:    - [NAS Transaction Details by Payment ID](https://checkoutinternal.eu.looker.com/dashboards/7480)    -  [MBC Transaction Details by Payment ID](https://checkoutinternal.eu.looker.com/dashboards/7344) |
| **Postman** | - Description: Blank  - Account: Join an existing account   - Account Name: Tech Finance.Support Team  - Role: Editor |
| **Datadog** | - Role: Standard  - Reason: Require access for a merchant care role. |
| **Tools for Flow-related queries** | -  **Merchant Hosted Pages enablement:** [Retool](https://retoolprod.mgmt.ckotech.co/apps/f67192a4-a90a-11ec-841c-938543b18be9/launchpad/Merchant%20Hosted%20Pages%20Enablement) app used to onboard and update configurations for Flow.  - Tool access will need to be granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274):    - Environment:** Production**     - Team**: Merchant Hosted Pages Enablement**     - Permission**: Viewer** |

For **Key Terms and Definitions** on Integration Issues, please see ****[Integrations Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22198412339346-Integrations-Glossary-Introduction)

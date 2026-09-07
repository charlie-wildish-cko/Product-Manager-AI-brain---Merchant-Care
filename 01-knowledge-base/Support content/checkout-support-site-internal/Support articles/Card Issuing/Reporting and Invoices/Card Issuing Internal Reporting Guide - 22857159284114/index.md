---
id: 22857159284114
section_id: 28482853758994
title: "Card Issuing: Internal Reporting Guide"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22857159284114-Card-Issuing-Internal-Reporting-Guide"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-01-15T13:59:45Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JNGXCVNHFQB2TX90T7Z1YKMZ"]
label_names: ["global", "reporting", "issuing", "case_card_issuing", "case_card_issuing_reporting"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

This guide outlines the methods for generating Card Issuing reports using the Dashboard and API. It is designed for agents assisting clients who need to access transaction data, authorizations, or set up automated reporting schedules.

**Problem -** Clients need to extract operational or compliance data regarding their issued cards.

 

**Solution -** Utilize the Dashboard for manual/scheduled reports or the Reports API for automated data retrieval.

## DESCRIBE THE ISSUE 💬

The client requires access to specific data points regarding their card issuing operations to meet operational needs or regulatory requirements. They may ask how to view transaction logs, check account balances, or automate the delivery of these reports to specific stakeholders. This applies to the Card Issuing product.

## KEY TAKEAWAYS 🔑

- 
 
**Two Methods:** Reporting can be handled via the Dashboard (GUI) or the Reports API (Programmatic).

- 
 
**Automation:** Dashboard reports can be scheduled for recurring email delivery.

- 
 
**API Capabilities:** The API allows for granular data retrieval (Transactions, Authorizations, Balances) and real-time webhooks.

- 
 
**Managed Clients:** Clients with an Account Manager (AM) should discuss complex reporting requirements directly with their AM.

## RESOURCES 📍

| **Tools** | **Case Examples** | **Related** |
| --- | --- | --- |
| [Dashboard](https://dashboard.checkout.com/) | Client asks how to schedule monthly transaction reports. | [Card Issuing Glossary & Introduction](https://checkoutint.zendesk.com/hc/en-us/articles/22857159284114/live_preview/01KF0Z25XFQCT0HFTZNKDGW27S) 9 |
| [Reports API Reference](https://api-reference.checkout.com/) | Client needs to integrate transaction data into their internal system. | [Card Issuing Tools & Permissions](https://checkoutint.zendesk.com/hc/en-us/articles/22857159284114/live_preview/01KF0Z25XFQCT0HFTZNKDGW27S) 10 |

## PROCESS FOR REPORTING CONFIGURATION 🖊️

This process details how to guide a client through generating reports. Determine if the client prefers a visual interface (Dashboard) or technical integration (API).

**Step 1. Assess Client Support Level**

- Check if the client has a dedicated Account Manager (AM).

- If the client has an AM, advise them to discuss their specific reporting requirements directly with the AM.

- If unmanaged, proceed to the steps below.

**Step 2. Dashboard Reporting (Manual & Scheduled)**

- Instruct the client to log in to the Dashboard.

- Navigate to **Reports > All reports > Generate reports** to create immediate reports based on business needs.

- 
 
**Select Report Types:** Clients can choose from  [available report](https://www.checkout.com/docs/card-issuing/retrieve-issuing-reports)  options such as Authorisation, Cards, Chargebacks, and Presentments.

- **To Automate:** Go to **Reports > Manage Schedules**. The client can configure reports to generate recursively and be delivered to specific email addresses.

**Step 3. API Reporting (Advanced Integration)**

- For automated, high-volume data, advise the client to integrate with the Reports API.

- 
**Utilize API Endpoints:**

  - 
 
**Transaction Reports:** Fetch transaction-level data.

  - 
 
**Authorization Reports:** Retrieve logs of transaction authorizations.

  - 
 
**Balance Reports:** Get real-time issuing account balance information.

- 
 
**Apply Filters:** Use query parameters to filter by date range, card ID, or transaction type.

- 
 
**Configure Webhooks:** Set up real-time notifications for events such as card transactions, authorizations/declines, and account balance updates.

## RESOLUTION ⚒️

The client successfully retrieves the necessary data either through a downloadable file from the Dashboard or a JSON response via the API.

- **Verification:** Ensure the client can see the report in their "Generated Reports" list or receives a 200 OK response from the API.

- 
 
**Remediation:** If reports fail to generate, verify the client has the correct permissions as detailed in the _Card Issuing Tools & Permissions_ guide.

## ESCALATION ⏫

- **When to escalate:** If the standard reporting tools are broken, data is missing, or the client requires a custom report not available in the standard list.

- 
 
**Contact:** You can check with `issuing_operations@checkout.com`.

- **Action:** Monitor the case for updates from the operations team and notify the merchant once the data discrepancy is resolved.

## FAQs ❓

- **Can reports be emailed automatically?** Yes, by using the "Manage Schedules" feature in the Dashboard, reports can be sent to specified email addresses.

- **What API endpoints are available for Issuing?** The main endpoints are Transaction Reports, Authorization Reports, and Balance Reports.

- **Who should managed clients contact?** Clients with an Account Manager should discuss their reporting needs directly with their AM.

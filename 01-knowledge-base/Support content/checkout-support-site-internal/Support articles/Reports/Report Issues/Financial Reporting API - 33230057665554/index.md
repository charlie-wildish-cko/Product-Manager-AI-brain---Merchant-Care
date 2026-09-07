---
id: 33230057665554
section_id: 22329315187858
title: "Financial Reporting API"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/33230057665554-Financial-Reporting-API"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-02-13T12:03:04Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K88KP6JD4E6GDQCYNDAPRMJX", "01KH48ADK06Y87EEH5V9GN8Z3F"]
label_names: ["API_error", "Financial Experience", "API_reporting", "Financial_reports"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

Merchant Care agents and technical teams should use this guide to configure and troubleshoot the **Financial Reporting API (related to Financial Experience)**.

**Problem / Symptom**: Common issues include "Access Denied" errors or missing reports in API responses.

## DESCRIBE THE ISSUE 💬

The Financial Reporting API is used to programmatically retrieve data about the financial impact on a merchant's account. Merchants often report that specific reports, like the **Financial Actions by Payout (FAR)**, are missing even when other reports are visible. This usually stems from missing scopes, entity ID mismatches, or search parameters that are too narrow to capture the system's generation window.

## KEY TAKEAWAYS 🔑

- Required scopes: `reports` and `reports:view` are needed for general access, but `financial-actions` and `financial-actions:view` are mandatory to see FAR reports.

- Secret Keys are entity-specific; a key linked to one entity (e.g., `sk_uxajco...`) cannot retrieve reports for a different entity ID.

- Report generation timing: Reports may be created slightly after the transaction date. It is recommended to use a **+/- 24-hour **buffer in date filters (e.g., for an April 9th report, search April 8th to April 10th).

- The `{prefix}` used in URLs refers to the merchant's unique prefix.

## TOOLING 📍

Click here to see the tools and documentation needed

| **Resource** | **Link / Access** |
| --- | --- |
| [Dashboard (NAS)](https://dashboard.checkout.com/reports/all-reports) | - If you do not already have access to the Dashboard, submit a ticket to IT via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)   - Submit a request through this form, selecting "identity.checkout.com - Prod" for the environment |

  
**API References**:

- [Reports API Reference](https://api-reference.checkout.com/#tag/Reports)

- [Get Report Details](https://api-reference.checkout.com/#operation/getReportDetails)

- [Get Report File](https://api-reference.checkout.com/#operation/getReportFile)

- [Financial Actions API Reference](https://api-reference.checkout.com/#tag/Financial-actions)

## PROCESS FOR API CONFIGURATION 🖊️

**Step 1: Verify API Scopes**

An Admin or Owner must add these four scopes to the Secret Key in the Dashboard to ensure full visibility:

- 
`reports` & `reports:view` (For general report access).

- 
`financial-actions` & `financial-actions:view` (Specifically for Financial Actions reports data).

**Step 2: Identify Financial Report Types**

When calling the API, you can filter the API `type` field in the API response for these specific reports:

- 
`Balance`, `BalanceBreakdown`

- 
`FinancialActions`, `FinancialActionsByPayout`

- 
`PayoutSummary`, `SettlementBreakdown`, `SettlementStatement`

**Step 3: Execute API Calls (cURL Examples)**

**Retrieve Reports using the API**

**A. Get all reports** Retrieve a list of all your reports and their metadata.

- **Production**: `https://{prefix}.api.checkout.com/reports`

- **Sandbox**: `https://{prefix}.api.sandbox.checkout.com/reports`

**B. Get report details** Returns a specific report by passing its `id`.

- **Production:** `https://{prefix}.api.checkout.com/reports/{id}`

- **Sandbox**: `https://{prefix}.api.sandbox.checkout.com/reports/{id}`

**C. Get report file** Download the actual file from a report using the `id` and `fileId`.

- **Production: **`https://{prefix}.api.checkout.com/reports/{id}/files/{fileId}`

- **Sandbox**: `https://{prefix}.api.sandbox.checkout.com/reports/{id}/files/{fileId}`

**D. Query Specific Financial Actions**

If you need to check the impact of a specific payment rather than a full report, use the following endpoints:

- **Production**: `https://{prefix}.api.checkout.com/financial-actions`

- 
**Sandbox**: `https://{prefix}.api.sandbox.checkout.com/financial-actions`
 

Click to view cURL Bash samples (request samples are available on their respective API reference pages in Go, cURL, Java, C#, and Python)

**Get All Reports **(with entity filter and date range):

```curl -i -X GET \
  'https://{prefix}.api.sandbox.checkout.com/reports?created_after=2025-02-17T00:00:00&created_before=2025-02-19T00:00:00&entity_id=ent_xxx' \
  -H 'Authorization: Bearer <YOUR_TOKEN_HERE>'
```

  
**Get Report Details:**

```curl -i -X GET \
  'https://{prefix}.api.sandbox.checkout.com/reports/{id}' \
  -H 'Authorization: Bearer <YOUR_TOKEN_HERE>'
```

  
**Download Report File:**

```curl -i -X GET \
  'https://{prefix}.api.sandbox.checkout.com/reports/{id}/files/{fileId}' \
  -H 'Authorization: Bearer <YOUR_TOKEN_HERE>'
```

  
**Query Specific Financial Actions:**

```curl -i -X GET \
  'https://{prefix}.api.sandbox.checkout.com/financial-actions?payment_id={payment_id}' \
  -H 'Authorization: Bearer <YOUR_TOKEN_HERE>'
```

  
**Troubleshooting "Missing" FAR Reports**

If a report for a specific date (e.g., April 9th) is missing, it may be due to the time the report was generated.

- **The Solution**: Use a wider date range in your API call.

- **Example**: For the report of April 9th, try using `created_after=2025-04-08` and `created_before=2025-04-10`.

- **Entity Check**: Ensure you are not filtering by the wrong entity; a report for `ent_jjz7...` will not show up under a different entity's filter.

## RESOLUTION **🛠️**

Share your findings with the merchant or the requester, along with the relevant API documentation links.

## ESCALATION** ⏫**

If you need to escalate, please seek advice from a senior team member or L2; if not resolved, escalate to the **FEX Reporting Team**:

- 
**Slack**: `#ask-fex-clientreporting` channel.

- 
**Jira**: Submit a [ticket](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277) under **Product team > FEX - Client Reconciliation**.

## RESOURCES** ****⭐**

| **Public Documentation** | **Case Examples** |
| --- | --- |
| - [Retrieve Reports Guide](https://www.checkout.com/docs/business-operations/retrieve-reports)  - [API Reference - Reporting](https://api-reference.checkout.com/#tag/Reports) | - [Ticket 100402](https://checkout1360.zendesk.com/agent/tickets/100402)  - [Ticket 14747](https://checkout1360.zendesk.com/agent/tickets/14747)  - [Ticket 19440](https://checkout1360.zendesk.com/agent/tickets/19440)  - [Ticket 14911](https://checkout1360.zendesk.com/agent/tickets/14911) |

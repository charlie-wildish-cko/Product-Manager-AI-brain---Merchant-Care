---
id: 30452913715986
section_id: 29824613373714
title: "Requesting & Exporting Intelligent Acceptance (IA) Data"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/30452913715986-Requesting-Exporting-Intelligent-Acceptance-IA-Data"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-12-09T10:21:21Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTZ6WEQ3S7TQ9KW35WKJXPDX", "01JWRC3HBBCWV9KD022M3M3WQQ", "01K6AASRZ015NW9D6WTY6VAF3X"]
label_names: ["IA", "IA_Data", "IA_report"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To understand what specific data extracts are available for Intelligent Acceptance (IA), what data cannot be exported, and the correct procedures for obtaining them. It covers the self-serve export of optimised transactions via Retool and the process for requesting an extract of successful retries.

**Problem:** Merchants need specific data exports to analyze IA performance.

**Solution:** Provide guidance on obtaining available IA data extracts, clarify limitations, and manage expectations for estimated data.

 

## DESCRIBE THE ISSUE 💬

Merchants are requesting specific data exports to better understand the performance of the Intelligent Acceptance (IA) product. They need information, such as a complete list of all optimized transactions or a list of "saved" transactions, to assess IA's impact. 

This guidance is for agents supporting merchants, helping them to fulfill data requests, communicate limitations, and manage expectations, especially concerning data that is only available as an estimate.

 

## KEY TAKEAWAYS 🔑

-  List of Optimised Transactions is available for self-service export via the Intelligent Acceptance Retool Dashboard.

-  Self-serve export is limited to the last 7 days of the selected time period due to a Retool limitation.

- The export of optimised transactions excludes payments from the control group or transactions not eligible for IA optimization.

- List of Successfully Retried Transactions is available but requires escalation to the IA team.

- A Full List of "Transactions Saved" cannot be provided because it's an estimation based on two components: successful retries and estimated "saved first attempts".

- Saved First Attempts are an estimate calculated from the difference in Approval Rate (AR) between the test and control groups and cannot be linked to specific payment IDs.

TOOLING**📍**

| Tool | Access |
| --- | --- |
| **Retool Intelligent acceptance** Used to analyze merchant processing volume and traffic breakdown. | - Access granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274).  - Application : Retool prod   - Role: Payment-Performance-Internal-Viewers or Payment-Performance-Commercial |

 

## PROCESS FOR REQUESTING AND EXPORTING INTELLIGENT ACCEPTANCE DATA 🖊️

1. Exporting a List of Optimised Transactions (Self-Serve)

This list includes individual transactions where IA applied at least one optimization. This process uses the **Intelligent Acceptance Retool Dashboard**.

- 
**Navigate to the IA Retool Dashboard:** Access the Intelligent Acceptance Retool dashboard.

- 
**Go to the Transactions Optimised Tab:** Select the **"Transactions optimised"** tab.

- 
**Customize and Select Data:** Use the **field selector** to choose and customize the columns you want in your extract. Note that the link for each payment can also open in Traffic Insights.

- 
**Download the File:** Download the generated file.

 

 

**⚠️ Key Limitation:** The export is limited to the **last 7 days** of the selected time period, which cannot be changed due to a Retool data load limitation.

2. Requesting a List of Successfully Retried Transactions

This is a specific list of transactions that were initially declined, then retried by IA and subsequently approved. This list is part of the "Transactions Saved" metric.

- 
**Confirm Unavailability for Self-Service:** Inform the requestor that this extract is not available for self-service.

- 
**Contact the IA Team:** To obtain this list, you must contact the IA team via [jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277)

### 3. Managing Requests for Full "Transactions Saved" Data

The "Transactions Saved" metric is an **estimation** and a complete list is **not possible** to provide.

- 
**Successfully Retries** (Transactions that were declined, retried, and approved) can be identified and exported at the payment level via the escalation process in Step 2.

- 
**Saved First Attempts** (The remaining part of the "Transactions Saved" metric) are an estimated number. This number is calculated by measuring the difference in Approval Rate (AR) between the test and control groups.

- 
**Set Expectation:** Clearly communicate that saved first attempts cannot be linked to specific payment IDs because the final approval decision is made by the issuer, making it impossible to confirm an IA optimization as the direct cause. The IA team can only provide the list of Successfully Retried Transactions.

## RESOLUTION ⚒️

Following the steps ensures that the user receives the available IA data exports. For **Optimised Transactions**, the user is able to perform a self-serve export from the Retool Dashboard, subject to the 7-day data limitation. 

For **Successfully Retried Transactions**, the request is correctly escalated to the IA team. Crucially, the expectation is managed regarding the full **"Transactions Saved"** data, as only the Successful Retries portion is exportable at the payment level.

If a user is having difficulty with the Retool self-serve export:

- 
**Verify Time Frame:** Reconfirm the user is selecting a time period that allows the system to pull data from the most recent 7 days.

- 
**Check Filters:** Ensure the user has the correct filters and columns selected.

- 
**Escalate Retool Issues:** If the issue persists and appears to be a Retool function problem, escalate to the appropriate internal support channel.

## ESCALATION** ⏫**

Escalate to L3 via [jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277) 

- Any request for the **List of Successfully Retried Transactions**.

- Any issue with the **Intelligent Acceptance Retool Dashboard** functionality that prevents the self-serve export (e.g., the dashboard is down or continuously fails to load data).

- Requests for data older than 7 days for **Optimised Transactions** (to confirm if any manual, non-standard solution is possible, though the documentation states it cannot be changed ).

**Required information to include:**

- Merchant ID

- The exact type of data export requested

- The requested date range

- For Retool issues: screenshots of the error/issue and the steps taken

**Instructions for the agent working the case:**

- For **Successfully Retried Transactions**, contact the IA team via [jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277)

- Set the correct expectation with the merchant/AM regarding the nature of the data (e.g., explaining why a full "Transactions Saved" list is not possible).

- Monitor the case for updates from the IA team and notify the merchant/AM immediately.

 

## FAQs** ****❓**

Why can't I get a list of all "Transactions Saved"?"Transactions Saved" is an estimated metric calculated from two parts: **Successful Retries** (which can be exported) and **Saved First Attempts** (which are an estimate based on the difference in Approval Rate between test and control groups and cannot be linked to specific payment IDs). Therefore, a complete, itemized list is not possible. How do I get a list of Successful Retries?This data is **not available for self-service** and requires you to contact the **IA team** by escalating the request on the **#ask-intelligent-acceptance Slack channel**.

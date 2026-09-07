---
id: 21991168206610
section_id: 21991160766482
title: "Investigating High Decline Rates"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991168206610-Investigating-High-Decline-Rates"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-31T16:50:45Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "case_transactions_issue_all_transactions_failing", "oc_channel", "incident", "OC", "SEV"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

This article provides a step-by-step guide for Merchant Care agents to troubleshoot and resolve issues related to high decline rates and transaction failures by using the Operations Center (OC) resources and communication channels.
DESCRIBE THE ISSUE 💬  

A merchant contacts us to report an issue with a high number of declined or failing transactions on the Checkout.com platform - this impacts their business operations and requires prompt resolution. The Operations Center (OC) provides 24/7 monitoring and incident response for the platform.

Severity (SEV) indicates an incident's seriousness, guiding the appropriate response based on impact and urgency. The SEV 1-4 scale helps quickly assess if a complex response is needed. Although the OC team handles classification, it's helpful to understand the SEV 1-4 levels.
Severities Management examples and definitions

| **Severity** | **Description** | **Examples** |
| --- | --- | --- |
| SEV-1 | Major business impact, requires immediate attention and cross-team support and resolution. | - Complete outage of a critical service affecting all merchants or users  - Total outage of key office infrastructure during a core business day  - Actual or potential breach of a service level agreement (SLA) with merchants  - Exceptional financial loss to Checkout.com  - Material, significant, or exceptional regulatory risk  - Exceptional reputational damage |
| SEV-2 | Significant business impact, needs fast resolution with cross-team support. | - Severe degradation of a critical service affecting most merchants or users  - Redundancy failure in a critical service risking outage if another node fail  - Major degradation of key office infrastructure during core business hours  - Significant financial loss to Checkout.com  - Significant reputational damage |
| SEV-3 | Moderate business impact, could become bigger if not fixed soon. | - Moderate degradation of a critical service causing partial loss for a small user group  - Severe degradation of key office infrastructure on a non-core business day  - Total outage or severe degradation of a non-critical service causing major user inconvenience |
| SEV-4 | Minimal business impact, unlikely to escalate into a major issue. | - Minor issues in a critical service causing slight performance delays, with little impact on usability and possibly unnoticed by users  - Minor to moderate issues affecting key office infrastructure during non-core business days  - Minor to moderate problems in a non-critical service causing some user inconvenience  - Redundancy failure in a non-critical service where losing one or more nodes leads to outage or severe degradation |

KEY TAKEAWAYS 🔑

- Severity (SEV) levels (1-4) classify the seriousness of an incident, helping to determine the appropriate response

- Datadog and the Checkout.com Dashboard are the primary tools for initial transaction trend analysis

- OC Slack channels #OC Channel and #OC_Incidents are key communication tools for monitoring and engaging the OC team

- Incident Reports (IRs) are structured documents that detail an incident and its resolution and can be shared with merchants once finalized

- When an issue requires OC intervention, a ticket must be logged with the correct macro and status, and regular updates should be provided to the merchant

PROCESS FOR INVESTIGATING HIGH DECLINE RATES 🖊️
**Step 1. Perform Initial Investigation**

- Check the transaction trends on the merchant's Dashboard to confirm the reported issue

- Use Datadog to investigate the specific transactions and identify any potential patterns or errors -you can access Datadog by replacing the Client ID in the provided link with the correct one

**Step 2. Check for Existing Incidents**

- After the initial investigation, check the OC Slack channels for any active incidents or outages. Look for updates on the `OC Channel` and `OC_Incidents` channels.

- If a relevant incident is found, click the provided hyperlink to join the dedicated incident channel for real-time updates and more details.

**Step 3. Update the Merchant**

- Once a resolution is found or significant updates are available in the incident channel, communicate this information to the merchant.

- If an Incident Report (IR) is available, ensure it's the final version before sharing it with the merchant. The IR is a structured document that provides details about the incident.

**Step 4. Escalate to the Operations Center (if no incident is found)**

- If no relevant incident is found in the Slack channels, log a ticket for the OC Team for further investigation using the [Jira link](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277).

- Provide as much information as possible from your investigation using tools like Looker and Datadog. Set the correct tag or macro on the ticket by selecting "OC/Incident Channel." Change the ticket status to "Raised with Internal Team."

## RESOLUTION ⚒️

- By following the steps above, the Merchant Care agent can either find an existing incident that explains the transaction failures or successfully escalate the issue to the OC for investigation. The expected outcome is a clear understanding of the root cause and a path to resolution, which can then be communicated effectively to the merchant.

- Remediation Steps: If an existing incident is found, the resolution is tied to the actions the OC team takes. If a new ticket is logged, the remediation will come from the OC's investigation.

- Check for Resolution: Continuously monitor the relevant Slack channels or the escalated ticket for updates. Once the OC confirms the issue is resolved, verify with the merchant that their transaction decline rates have returned to normal.

## ESCALATION** ⏫**

- Instructions for the agent working the case: The agent should monitor the escalated ticket and the relevant Slack channels for updates from OC. The merchant must be kept informed about the progress, findings, and resolution status.

- How to follow up and when to chase: Maintain regular communication with the merchant, providing updates throughout the investigation. If the OC team needs more information or requires a merchant to be contacted, they will notify the Merchant Care team by tagging `@merchantlevel1` on Slack.

 

## FAQs** ****❓**

What is the purpose of the Operations Center?

The Operations Center (OC) is the operational backbone of the platform, providing 24/7 monitoring, incident response, security operations, and infrastructure management to ensure the platform is stable, secure, and reliable for merchants and partners.What do the different Severity (SEV) levels mean?

Severity levels classify the impact and urgency of an incident. A SEV-1 indicates a major business impact requiring immediate attention, while a SEV-4 represents a minimal business impact that is unlikely to escalate into a major issue.When should I log a ticket for the Operations Center?

You should log a ticket for the Operations Center if you have performed the initial investigation steps (checking the Dashboard and Datadog) and have not found an existing incident in the OC Slack channels that explains the merchant's issue.What should I do if the Operations Center contacts Merchant Care?

The OC team may contact Merchant Care via the `@merchantlevel1` Slack tag if they need further investigation or if they require a merchant to be contacted. The available agent is expected to respond and assist with the request.

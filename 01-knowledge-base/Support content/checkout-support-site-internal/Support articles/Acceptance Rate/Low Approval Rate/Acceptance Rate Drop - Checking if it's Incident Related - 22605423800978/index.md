---
id: 22605423800978
section_id: 22604736721426
title: "Acceptance Rate Drop - Checking if it's Incident Related"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22605423800978-Acceptance-Rate-Drop-Checking-if-it-s-Incident-Related"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-19T06:55:34Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRPB6VB7BVTRFPB2N2PA9E"]
label_names: ["global", "case_acceptance_performance_low_approval_rate", "case_acceptance_performance", "low_acceptance_rate", "acceptance_rate_performance_issue", "incident_related", "check_for_an_incident"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**   

To investigate whether a drop in acceptance rates or payment performance issues is related to an incident logged by the Operations Center (OC) team and how to communicate with the merchant.

**Problem:** A merchant reports a drop in payment acceptance rates or an ongoing issue with a specific payment channel.   

**Solution:** Check for existing incidents and provide timely updates to the merchant, or escalate the issue to the Operations Center team if no incident is found.   

DESCRIBE THE ISSUE 💬           

A merchant contacts support after observing a decline in their acceptance rate performance or a consistent issue with a specific issuer bank, payment scheme, or geographical region. This report may come in on the same day the performance drop began or a few days after. 

The primary goal is to determine if this issue is part of a larger, known incident already being handled by the Operations Center team.

KEY TAKEAWAYS 🔑               

- Merchants report drops in acceptance rates or performance issues

- Check for existing incidents in the #OC or #OC_incidents Slack channels

- If an incident exists, keep the merchant updated and share the validated Reason for Outage (RFO) when it becomes available

- If no incident is found, reach out to the OC team via the #Support_OC channel for a quick check

- Advise the merchant to check the Checkout Status Page for incident updates

PROCESS TO CHECK FOR AN INCIDENT 🖊️           

The process involves a standard check to see if the merchant's issue corresponds to an existing incident. This is a crucial first step before escalating or performing deeper troubleshooting.           
Check Slack Channels for an Existing Incident 

-  Use the timeframe provided by the merchant or the timestamp of transaction samples to search for relevant incidents in the #OC or #OC_incidents slack channels

- The channels contain alerts from the OC team about detected failures and raised incidents

Existing Incident: 

- If a relevant incident is found, inform the merchant about the progress or resolution 

- Once available, share the validated Reason for Outage (RFO) with the merchant and advise them to monitor the [Checkout Status Page](https://checkout-services.statuspage.io/) for real-time updates on the incident status

Suspected Incident:

- If you suspect an incident for recent transactions but don't see one raised you can ask the OC team to check this

- Submit your request in the #Support_OC Slack channel

No Incident:

See the [Investigating a Performance Drop](https://checkoutint.zendesk.com/hc/en-us/articles/22605392914450-Investigating-a-Performance-Drop) knowledge article for in-depth troubleshooting steps

ESCALATION** ⏫**           

- Escalate the issue to the OC team through the #Support_OC channel if no incident is found and the problem persists

- Provide the transaction timestamps and any specific details shared by the merchant (e.g., issuer, scheme, region) to help the OC team investigate

- Stay on the case and monitor for updates from the OC team and notify the merchant of any progress 

FAQs** ❓** 
          

What is an RFO?

An RFO, or Reason for Outage, is an official document that explains the cause of a service disruption, the actions taken to resolve it, and preventive measures for the future.What is the Checkout Status Page?

The Checkout Status Page is a public-facing page that provides real-time information on the status of our services, including any ongoing incidents or scheduled maintenance.How quickly can I expect an incident to be resolved?

Incident resolution times vary depending on the severity and complexity of the issue. Updates are typically provided within an hour of an incident being raised, and you should monitor the relevant Slack channels for the latest information. 

RESOURCES 📍           

| Related Articles |
| --- |
| - [Investigating a Performance Drop](https://checkoutint.zendesk.com/hc/en-us/articles/22605392914450-Overall-Performance-Drop)  - [Checkout Status Page](https://checkout-services.statuspage.io/)  - [Improve the acceptance rate](https://checkoutint.zendesk.com/hc/en-us/articles/22605376545682-Improve-the-acceptance-rate) |

---
id: 22605424803602
section_id: 22604832741650
title: "Issue with Test Card: 3DS Not Configured in Sandbox Environment"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22605424803602-Issue-with-Test-Card-3DS-Not-Configured-in-Sandbox-Environment"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-13T12:44:22Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRP1QGWAFPTEP0CSMC1WBV"]
label_names: ["global", "case_3ds_issues", "3ds_not_configured_to_be_processed_in_sandbox", "case_3ds_issue_issues_with_test_cards_sandbox", "using_our_test_cards", "sandbox"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

A merchant is experiencing a 3ds_not_configured error when processing transactions with a test card in the Sandbox environment. 

## INTRODUCTION TO THE ISSUE💬

This article addresses the issue where 3D Secure (3DS) authentication is not configured to process payments in the **Sandbox** environment. You may encounter this issue when using a test card. When a request includes `"3ds": { "enabled": true }`, the transaction fails with a `processing_error` and the error code `3ds_not_configured`. Example below:

 

```
Requests with
"3ds": {
      "enabled": true
  }
fails with
{
  "request_id": "f16ac5bc-643d-4c9a-888e-94e03d4f559c",
  "error_type": "processing_error",
  "error_codes": [
      "3ds_not_configured"
```

 

This shows the parameters set by the merchant when simulating a payment in the Sandbox. We highlighted that 3DS was enabled (set to true) in the request.  
  
Despite 3DS being true, the response returned a Processing Error with an error code indicating 3DS is not configured. This is the response sent to the merchant after their request.

The root cause is a configuration issue. The 3DS feature is not enabled, so you will need to perform some configurations to allow payments to be processed.PROCESS STEPS🖊️ 

Follow these steps to configure 3DS for a processing channel in the CAT Sandbox:-

1. Log in to the **CAT Sandbox**

2. 
Search for the client by using their name, Client ID, Entity ID, or Processing Channel ID. For this example, we will use "Cherry Technologies Inc Sandbox":-

3. Select the **entity** for which you want to activate 3DS

4. 
Check the existing **processing channels** under the selected entity:-

5. Navigate to **Processing > Authentication** to see which processing channels have 3DS enabled

6. 
⚠️ To process 3DS transactions, merchants must configure each processing channel with the same settings under 'Processing - (Authentication)'. Please refer to the screenshot below for guidance:-

7. If a processing channel is not listed under the **Authentication** section, it means 3DS is not available for transactions processed on that channel

8. 
Click **+ Add processing channel** in the top right corner:-

9. 
From the dropdown menu, select the processing channel you want to add:-

10. After adding the processing channel to the **Authentication** section, you must manually add the processors to replicate the information from the original processing channel

11. For instance, if the merchant has a VISA and MC processor, you need to add the same by clicking **Add a Profile Processor** and mapping the correct information

RESOLUTION ⚒️Respond to the merchant and ask them to perform the test again on their end. After they complete the test, we should request that they inform us if they encountered any problems so we can escalate. ESCALATION⬆️  
If issues persist after retesting, contact the Merchant Configuration Team using the Macro:

| Macro - Transfer - Merchant Configuration - Region. |
| --- |

They specialize in configurations and are best equipped to resolve ongoing problems. RESOURCES 📍

| Tools | Case Examples |
| --- | --- |
| [DataDog Link](https://app.datadoghq.eu/logs?query=%40RequestId%3Ad38c2cba-2a03-464c-bd23-7a5526597c73&agg_m=count&agg_m_source=base&agg_t=count&cols=host%2Cservice&event=AgAAAYjFQe8qO1pPzAAAAAAAAAAYAAAAAEFZakZRZnJjQUFDVnhGMzI3TTRnSndBYgAAACQAAAAAMDE4OGM1NGYtNTlkYi00NTJjLWFmMjUtOTYxYTNmNWYxZTQ2&fromUser=true&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=time%2Cdesc&viz=stream&from_ts=1674541399220&to_ts=1677133399220&live=true) | See this  [ticket](https://checkout1360.zendesk.com/agent/tickets/1831) |

  

##

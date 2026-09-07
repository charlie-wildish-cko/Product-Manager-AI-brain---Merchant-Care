---
id: 23046334381202
section_id: 23035210429458
title: "Segment Troubleshooting"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/23046334381202-Segment-Troubleshooting"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:33:42Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRPPFPJP1GWJ10SVG1YKVW"]
label_names: ["global", "case_configuration_change", "segment_troubleshooting", "case_configuration_issue_other"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To troubleshoot issues with **entity segments** on Checkout.com, a tool that helps merchants categorize transactions. 

**Problem:** A transaction is assigned to the wrong entity segment.

**Solution:** Use the Retool application to identify why the transaction was assigned incorrectly and guide the merchant to a solution.

## DESCRIBE THE ISSUE 💬

A merchant has reported that transactions are not being correctly categorized by their entity segments. The user is trying to group transactions by a specific dimension, such as a brand, business category, or location, but some payments are being assigned to the wrong segment. 

⚠️ Merchants are encouraged to manage their entity segments directly. Advise them to first use the [self-service resources](https://www.checkout.com/docs/business-operations/use-the-dashboard/entity-segments) available for these actions:

- Enable Segments

- Edit Segments settings

- Disable Segments

 

## KEY TAKEAWAYS 🔑

- 
**Entity segments** add a layer of organization to a merchant's account by linking transactions to specific attributes.

- 
**Segments cannot overlap.** Each unique combination of dimensions must map to one and only one segment.

- A segment needs at least one dimension (e.g., brand, business category, location) to be populated.

- 
**Historical transactions cannot be retagged.** The segments are assigned at the time of the transaction.

- Always begin by **encouraging the merchant to use the self-service **option first.

- 
**The Retool application** can be used to view the history of a transaction's processing channel and segment association.

 

## PROCESS FOR TROUBLESHOOTING ENTITY SEGMENTS 🖊️

**Step 1. ⚠️ Self-Service Option **

- Direct the merchant to the [Entity segments - Docs](https://www.checkout.com/docs/business-operations/use-the-dashboard/entity-segments)  support section. This resource provides clear instructions on how to set up and update segments on their dashboard.

- Encourage the merchant to follow these steps to resolve the issue on their own, if they're unable to do this then follow the steps below.

This process outlines how to use the Retool application to help a merchant understand why a payment was assigned to a particular entity segment. This requires in-depth problem-solving as you'll be examining transaction history.
**Step 2. Search for the Transaction in Retool**
You can support the merchant if they're unable to self-serve

- Log in to the  [Retool](https://retoolprod.mgmt.ckotech.co/apps/0aea8292-0253-11ef-93d0-6f6ec489f741/Merchant%20%26%20User%20Data/Segment%20Diagnostic%20Tool) application

- Search for the transaction using the impacted **Client ID** or **Entity ID**

**Step 3. Examine the Segment and Processing Channel History**

- View the history of the processing channel and its associated segment

- Check the timestamp to see when the segment was associated with the processing channel

- This will help you identify when the issue occurred

- Look for any changes (represented by "Modify" in the table) or newly created segments (represented by "Insert"). The table will show the old and new values.

_**Operation: New segment created**_
_**Operation: Processing channel association changed**_
****

## RESOURCES 📍

| Tools | Related |
| --- | --- |
| [Retool](https://retoolprod.mgmt.ckotech.co/apps/0aea8292-0253-11ef-93d0-6f6ec489f741/Merchant%20%26%20User%20Data/Segment%20Diagnostic%20Tool) | External article: [Entity Segments](https://www.checkout.com/docs/business-operations/use-the-dashboard/entity-segments) |

## 

## FAQs** ****❓**

Can I change the segment of a historical transaction?No, historical transactions cannot be retagged to a different segment. Entity segments are assigned at the time of the transaction.What if a merchant has overlapping segments?Entity segments cannot overlap. Each unique combination of dimensions must map to one and only one segment. If this occurs, it's likely a misconfiguration on the merchant's side that needs to be corrected.Why are some transactions, like standalone authentications, not assigned a segment?Currently, standalone authentications and pay-to-bank transactions cannot be associated with entity segments. This is a current limitation of the feature.

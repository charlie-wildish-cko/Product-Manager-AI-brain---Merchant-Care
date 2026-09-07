---
id: 22059026688146
section_id: 28544586885778
title: "Release of funds after 180 days post-termination date"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22059026688146-Release-of-funds-after-180-days-post-termination-date"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:37:34Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTPW3ZQ754XHJ09XPK89H99W"]
label_names: ["global", "case_terminations", "case_terminations_account_termination_related", "post_termination_funds_release", "release_of_funds_after_180_days_post_termination_date", "abc_decommissioning", "mbc_decommissioning", "hub_decommissioning"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

When a merchant account is terminated, all (available, pending, payable) funds are held for a short period of time as part of a collateral fund for any refund and chargeback transactions that may be needed post-merchant termination. A risk assessment is made to review and approve the release of the funds set aside as collateral after termination.

## Process Steps

When merchants have not received funds within 180 days of the termination date, they will often contact Merchant Care for assistance with this. To assist the merchant, agents should follow the below guidance:

1. Merchant care identifies the client account name or the hub account name from the ticket.

2. Merchant Care opens the Risk Google sheet [here](https://docs.google.com/spreadsheets/d/1hv-d_obyw7rjKDqNBH8UjPaGwYmwpXzc-nsmpRHXbTo/edit?gid=787504602#gid=787504602).

  1. If the merchant inquiry is on HUB, open the tab ABC

  2. If the merchant inquiry is for NAS, open the tab NAS

3. In the Risk Google sheet, use CRTL+F to find the merchant using the name found in step 1

4. If there is an open status in column N (i.e. merchant with Status = Open), continue to step 5. If there is a closed status in column N (as seen in the below screenshot), skip to step 7 below. 

1. For open statuses, Merchant Care should use the Risk Monitoring transfer macro in Zendesk to transfer the ticket to the Risk Monitoring Inbound Support queue.

2. Risk Monitoring will review and communicate directly with the merchant and the Payments Team if there is a need to support the early payout.

  1. Merchant Care can therefore close the case on their side once they transfer the case to Risk Monitoring. 

3. For closed statuses, Merchant Care should use the relevant regional Treasury transfer macro in Zendesk to request for the Treasury team to pay the merchant_ (**no approval from Risk is required for Closed statuses**)_

  1. When doing this, Merchant Care needs to ask the Treasury Team to clear any negative currency accounts by netting them off before processing the final payout. 

4. Once the Treasury team has actioned the request, they will inform Merchant Care that this has been done. 

  1. It is the responsibility of Merchant Care to inform the merchant and solve the ticket.

## Glossaries and Definitions:

For **Key Terms and Definitions** on Terminations, please see ****[Terminations Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22059058669330-Terminations-Glossary-Introduction)   

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Terminations articles, please see ****[Terminations Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22059058597778-Terminations-Tools-Permissions)

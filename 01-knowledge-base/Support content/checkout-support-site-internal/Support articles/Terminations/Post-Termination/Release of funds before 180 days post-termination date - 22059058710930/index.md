---
id: 22059058710930
section_id: 28544586885778
title: "Release of funds before 180 days post-termination date"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22059058710930-Release-of-funds-before-180-days-post-termination-date"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:36:44Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHQKPVKA7XAZRYSRWE7JRH4", "01HTPW3ZQ754XHJ09XPK89H99W"]
label_names: ["case_settlements", "case_settlements_issue_settlement_not_received", "global", "case_terminations", "case_terminations_account_termination_related", "post_termination_funds_release", "release_of_funds_before_180_days_post_termination_date", "abc_decommissioning", "mbc_decommissioning", "hub_decommissioning"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

When a merchant account is terminated, all (available, pending, payable) funds are held for a short period of time as part of a collateral fund for any refund and chargeback transactions that may be needed post-merchant termination. A risk assessment is made to review and approve the release of the funds set aside as collateral after termination.

## Process Steps

If merchants have not received funds within 180 days of their termination date and contact Merchant Care, Merchant Care will check the effective termination date communicated to the merchant configuration team and use the transfer macro template to send the support ticket to the Risk Monitoring Inbound Support queue.

To do this, agents should follow the below-recommended steps:

1. Identify the effective termination date from the DSR of the termination - to do this, follow the below steps:

  1. Go to [salesforce](https://checkout.lightning.force.com/lightning/page/home)

  2. Switch your salesforce view to sales lightning mode by clicking on the 9 dots on the top left-hand side of the screen and selecting “Sales - Lightning”.

  3. Copy and paste the client account name in the search bar, see the below screenshot.

1. Open the client account

2. On the newly loaded page on salesforce, go to the right panel and find opportunities

3. 

  1. Look for Churn opportunity type/stage terminated merchant and open it

  2. On the new window, scroll down and find the termination letter information.

  1. Look for the termination date.

4. From the current calendar date, identify if the termination date is past 180 days.

  1. If the merchant’s request is confirmed to be for an **early payout before 180 days**, Merchant Care should use the Risk Monitoring transfer macro from Zendesk to transfer the ticket to the Risk Monitoring Inbound Support queue.

    1. For NAS merchants: The Risk Monitoring will review the request and communicate directly with the merchant and the Payments Team if there is a need to support the early payout. As the Risk Monitoring team will handle all communications, Merchant Care can solve the ticket on their side after transferring to the Risk Monitoring team.  

    2. For MBC merchants: The Risk Monitoring team will review the request and revert to Merchant Care with their decision. 

      1. If the early payout has been approved: Merchant Care L1 should transfer the ticket to Merchant Care L2 as they can release the funds for MBC merchants. 

      2. If the early payout has not been approved: Merchant Care L1 should inform the merchant and solve the ticket. 

## Glossaries and Definitions:

For **Key Terms and Definitions** on Terminations, please see ****[Terminations Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22059058669330-Terminations-Glossary-Introduction)   For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Terminations articles, please see ****[Terminations Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22059058597778-Terminations-Tools-Permissions)

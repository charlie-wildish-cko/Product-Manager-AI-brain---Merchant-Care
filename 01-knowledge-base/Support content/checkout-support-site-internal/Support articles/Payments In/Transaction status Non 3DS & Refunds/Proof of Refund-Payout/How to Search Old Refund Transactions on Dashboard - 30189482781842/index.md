---
id: 30189482781842
section_id: 21991136181650
title: "How to Search Old Refund Transactions on Dashboard"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/30189482781842-How-to-Search-Old-Refund-Transactions-on-Dashboard"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-16T13:41:34Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

Use this article when a merchant is unable to find a refund status for a payment captured over one year ago.

**Problem: **A merchant is trying to check the status of a refund for a transaction that occurred more than a year ago, but the dashboard search function is not showing the transaction details.

**Solution:** The dashboard has a search limitation for transactions older than one year. To find the refund status, you must manually construct the payment's URL using the payment ID and paste it directly into the browser to access the details page.

## DESCRIBE THE ISSUE 💬

A merchant may contact us because they are unable to see the refund status on their dashboard. This happens for payments that were captured more than a year ago. When they search using the payment ID, the dashboard shows "No transaction found."

This isn't a bug with the dashboard but a **known limitation** of the search functionality. The system has a built-in search limit for transactions that are over one year old. 

Therefore, the dashboard can't find and display the refund status for these older payments directly through the standard search bar.

## SEARCH OLD REFUND TRANSACTIONS ON DASHBOARD PROCESS 🖊️

To view the status of a refund for a transaction older than one year, you need to bypass the search function. Agents and the merchant can do this by directly accessing the payment's URL:

1. Copy the following URL: `https://dashboard.checkout.com/payments/all-payments/payment/pay_xxxxxxxxxxxxxxxxxxx`

2. 
**Replace** the placeholder payment ID (`pay_xxxxxxxxxxxxxxxxxxx`) with the specific payment ID for the transaction you are tracking on dashboard.

3. Paste the new, customized URL into the browser's address bar and press Enter.

This will take you directly to the payment details page, where you can view the refund status.

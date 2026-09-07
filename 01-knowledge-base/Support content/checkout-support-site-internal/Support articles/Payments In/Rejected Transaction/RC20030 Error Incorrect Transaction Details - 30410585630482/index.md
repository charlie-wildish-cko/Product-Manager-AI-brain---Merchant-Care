---
id: 30410585630482
section_id: 23045958401426
title: "RC20030 Error: Incorrect Transaction Details"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/30410585630482-RC20030-Error-Incorrect-Transaction-Details"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-12-09T10:08:48Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

If a payment transaction fails with the RC20030 error code.

**Problem: **The RC20030 error typically indicates a problem with the transaction details submitted. This often stems from incorrect formatting of the transaction amount or currency.

## DESCRIBE THE ISSUE 💬

The RC20030 error is triggered when submitted transaction details are incorrect. 

This is most often caused by errors in the amount or currency formatting, which can include an invalid currency code, extra characters, or, most commonly an incorrect number of decimal places.

## Payment Scheme Requirements 🏦

Different payment schemes, such as Visa and Mastercard, often called Third Party Acquirers (TPAs), may have their own specific requirements for how amounts should be formatted.

Example: Visa Transactions

For Visa transactions, the amount is usually limited to two decimal places.

- 
**Action:** To avoid any errors, you must ensure the third decimal digit is explicitly set to zero.

## Currency-Specific Formatting 💷

Some currencies have specific rules for how transaction amounts should be formatted.

For example: Kuwaiti Dinar (KWD)

When requesting a payment in KWD, the last digit of the amount should always be zero.

This is because Checkout.com reads the amount as having three decimal places (for example, 443952 is interpreted as $443.952).

- 
**Invalid Example:** An amount value of `443952` may not be accepted.

- 
**Tip:** Make sure the amount follows the currency's decimal formatting rules.

## RESOLUTION ⚒️

The key is to format the transaction amount correctly, considering two main factors: Currency and Payment Scheme.

**Currency Check:** Does the submitted amount adhere to the specific decimal requirements of the chosen currency (e.g., KWD requires the third decimal place to be 0)?

**Scheme Check:** Does the submitted amount adhere to the maximum decimal requirements of the payment scheme (e.g., Visa limits to two decimal places, meaning the third must be 0)?

**Invalid Characters:** Ensure the amount field contains only valid numeric characters.

---
id: 36700375755922
section_id: 36678206237714
title: "New data integrity checks for Account Funding Transactions"
url: "https://support.checkout.com/hc/en-us/articles/36700375755922-New-data-integrity-checks-for-Account-Funding-Transactions"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-07-02T09:36:25Z"
permission_group_id: 11003577394706
content_tag_ids: []
label_names: []
user_segment_ids: []
archive: false
---

From August 1, 2026, Checkout.com will enforce compliance with the card schemes’ data integrity checks for Account Funding Transactions (AFTs).

After we introduce these checks, you may see more AFT declines if your API requests don’t follow our validation. If we decline a payment for this reason, we’ll return a 422 status code.

To help you assess your integration and identify potential issues that could result in these declines, we’ve listed the API fields below and the relevant data quality requirements:

**Sender and recipient name** 

For [sender.first_name](https://api-reference.checkout.com/tag/Payments#operation/requestAPaymentOrPayout!path=0/sender/0/first_name&t=request), [sender.last_name](https://api-reference.checkout.com/tag/Payments#operation/requestAPaymentOrPayout!path=0/sender/0/last_name&t=request), [recipient.first_name](https://api-reference.checkout.com/tag/Payments#operation/requestAPaymentOrPayout!path=0/recipient/first_name&t=request), and [recipient.last_name](https://api-reference.checkout.com/tag/Payments#operation/requestAPaymentOrPayout!path=0/recipient/last_name&t=request), please ensure that:

- The name uses the Latin alphabet. Standard accents (like é, ö, ø, ç) are permitted
- The name does not include special characters @, !, /, >, ?, :, ;, :, <, >, *, ", #, ^, $, £, (, ), [, ], ~, \, or numeric characters (including Chinese and Arabic numerals)
- The name does not include double spaces, tabs, or whitespace
- The name does not contain emoji characters
- For the **sender name fields only**, the name does not contain the following disallowed values: “CARD”, “TECHNOBANK”, “INSTANT”, “VIRTUAL”, “MY”, “KDV”, “GOLD”, “VISA”, “MONO”, “VIZA”, “PRIVATE”, “Tester”, “Unknown”, “NA”, “Test”

**Sender and recipient address**

For the [sender.address.address_line1](https://api-reference.checkout.com/tag/Payments#operation/requestAPaymentOrPayout!path=0/sender/0/address/address_line1&t=request), [sender.address.address_line2](https://api-reference.checkout.com/tag/Payments#operation/requestAPaymentOrPayout!path=0/sender/0/address/address_line2&t=request), [recipient.address.address_line1](https://api-reference.checkout.com/tag/Payments#operation/requestAPaymentOrPayout!path=0/recipient/address/address_line1&t=request), [recipient.address.address_line2](https://api-reference.checkout.com/tag/Payments#operation/requestAPaymentOrPayout!path=0/recipient/address/address_line2&t=request), and [sender.company_name](https://api-reference.checkout.com/tag/Payments#operation/requestAPaymentOrPayout!path=0/sender/1/company_name&t=request) fields, please ensure that:

- The address uses the Latin alphabet. Standard accents (like é, ö, ø, ç) are permitted
- The address does not include special characters @, !, /, >, ?, :, ;, :, <, >, *, ", #, ^, $, £, (, ), [, ], ~, \, or Chinese and Arabic numerals. Other numeric characters (e.g. 1, 2…9, 0) are permitted
- The address does not include double spaces, tabs, or whitespace
- The address does not contain emoji characters

**Sender and recipient city**

For the [sender.address.city](https://api-reference.checkout.com/tag/Payments#operation/requestAPaymentOrPayout!path=0/sender/0/address/city&t=request) and [recipient.address.city](https://api-reference.checkout.com/tag/Payments#operation/requestAPaymentOrPayout!path=0/recipient/address/city&t=request), please ensure that:

- The city uses the Latin alphabet. Standard accents (like é, ö, ø, ç) are permitted
- The city does not contain special characters @, !, /, >, ?, :, ;, :, <, >, *, ", #, ^, $, £, (, ), [, ], ~, \, or numeric characters (including Chinese and Arabic numerals)
- The city does not include double spaces, tabs, or whitespace

**Sender and recipient state**

For the [sender.address.state](https://api-reference.checkout.com/tag/Payments#operation/requestAPaymentOrPayout!path=0/sender/0/address/state&t=request) and [recipient.address.state](https://api-reference.checkout.com/tag/Payments#operation/requestAPaymentOrPayout!path=0/recipient/address/state&t=request), please ensure that:

- The state does not contain special characters @, !, /, >, ?, :, ;, :, <, >, *, ", #, ^, $, £, (, ), [, ], ~, \, or numeric characters (including Chinese and Arabic numerals)

**Sender and recipient country**

For the [sender.address.country](https://api-reference.checkout.com/tag/Payments#operation/requestAPaymentOrPayout!path=0/sender/0/address/country&t=request) and [recipient.address.country](https://api-reference.checkout.com/tag/Payments#operation/requestAPaymentOrPayout!path=0/recipient/address/country&t=request), please ensure that:

- The country does not contain special characters @, !, /, >, ?, :, ;, :, <, >, *, ", #, ^, $, £, (, ), [, ], ~, \, or numeric characters (including Chinese and Arabic numerals)

We will decline any payment where the country code is a prohibited or restricted country: “CU”, “IR”, “KP”, “SD”, “SY”, “RU”, “BY”, “VE”, “IQ”, “AF”, “LY”.

---
id: 22857148388114
section_id: 28544475382162
title: "Giropay"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22857148388114-Giropay"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:35:15Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRS13HJX19Z5T3VSS7TJF7"]
label_names: ["global", "case_non-merchant_requests", "case_nmr_issue_apms", "giropay"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

Giropay may request specific details on a customer as per the screenshot below.

## Process Steps

1. 
** Retrieve the Payment ID**

  1. Locate the payment ID using the information provided by Giropay.

2. 
**Modify the Reference**

  1. Add “pay_” to the payment ID to format it like this: pay_dscgoet4rofebg275jdq3ugqua.

3. 
**Query in Retool**

  1. Paste the payment ID into Retool and click “Query” to retrieve the merchant name/client name.

1.  **Notify the Account Manager or Merchant (see contact details ******[here](https://docs.google.com/spreadsheets/d/1HWI9aqXvWJ4AHcA2BteR-otSXcn7bBsTiwYzp9VY2vs/edit?gid=0#gid=0)**)**

  1. Send an email to the Account Manager or merchant containing the following details:

    1. Payment ID

    2. Reference

    3. Amount

    4. Date

    5. Payment Method _(All this information can be obtained from Retool.)_

 

1. 
** Forward Information**

  1. Once the details are provided by the merchant or Account Manager, share the same with the alternative payment method provider.

****

## Glossaries and Definitions:

For **Key Terms and Definitions** on Non-merchant Requests Issues, please see ****[Non-merchant Requests Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22857148102546-Non-merchant-requests-Glossary-Introduction)

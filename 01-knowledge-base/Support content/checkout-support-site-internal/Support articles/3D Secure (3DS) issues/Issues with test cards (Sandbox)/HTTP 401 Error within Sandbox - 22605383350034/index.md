---
id: 22605383350034
section_id: 22604832741650
title: "HTTP 401 Error within Sandbox"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22605383350034-HTTP-401-Error-within-Sandbox"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:35:58Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRP1QGWAFPTEP0CSMC1WBV"]
label_names: ["global", "case_3ds_issues", "http_401_error_within_sandbox", "case_3ds_issue_issues_with_test_cards_sandbox"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

the below article covers the issue: 401 response from request within Sandbox

## Process Steps

**How to investigate this issue**

1. Check that the merchant is calling the correct endpoint as the header in the authorisation

2. Ensure that the header is included in the bearer's request to resolve this issue. Please see the screenshot below of an example of the endpoint not including the bearer endpoint

  
  
**Resolution**

The merchant would need to include their secret key in the Authorisation header and also add the Bearer prefix. For example: Bearer {{secret API key}}.  
  
Example ticket: [https://checkout1360.zendesk.com/agent/tickets/22161](https://checkout1360.zendesk.com/agent/tickets/22161)

## Glossaries and Definitions:

For **Key Terms and Definitions** on 3DS, please see ****[3DS Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22059673420818-3DS-Glossary-Introduction)   

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the 3DS articles, please see ****[3DS Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22059810908306-3DS-Tools-Permissions)

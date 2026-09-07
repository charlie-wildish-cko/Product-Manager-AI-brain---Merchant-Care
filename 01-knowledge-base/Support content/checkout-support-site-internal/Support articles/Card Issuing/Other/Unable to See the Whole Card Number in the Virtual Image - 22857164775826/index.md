---
id: 22857164775826
section_id: 28483258495890
title: "Unable to See the Whole Card Number in the Virtual Image"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22857164775826-Unable-to-See-the-Whole-Card-Number-in-the-Virtual-Image"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:35:13Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JNGXCVNHFQB2TX90T7Z1YKMZ"]
label_names: ["global", "issuing", "case_card_issuing", "case_card_issuing_unable_to_see_the_whole_card_number_in_virtual_image"]
user_segment_ids: [11003606966930]
archive: false
---

## Process Steps

1. 
**Verify Access Permissions**: ensure that the client or cardholder has the appropriate permissions to view the full card number (Dashboard > Settings > User Permissions > User > Permissions > Issuing where View card number and CVC2 should be ticked)

2. 
**Virtual Card Configuration**: confirm that the virtual card configuration allows the cardholder to view the full card number (the issuing client can review the cardholder's settings in Dashboard > Issuing > Cards and enable the option to view the full PAN (Primary Account Number) if applicable

3. 
**Confirm Authentication**: Confirm the client or cardholder has successfully passed any required authentication steps. Some systems restrict viewing the full PAN until additional identity verification is completed. If the issue persists, advise the cardholder to log out and log back in or retry the process with proper authentication.

4. 
**Use API to Retrieve Card Details**: If configured, the issuing client can use the Retrieve Card API to securely fetch the full card details. Access to the full card number through API requires strong authentication and PCI DSS compliance. If the full PAN is masked, the client needs to review their account's security policies

5. 
**Security Policies**: Viewing the full PAN may not be enabled by default to comply with Payment Card Industry Data Security Standards (PCI DSS). Educate the client or cardholder about these restrictions.

6. 
**Educate the Cardholder**: If the full card number cannot be displayed due to policy restrictions, guide the cardholder on securely using the partial number

## Glossaries and Definitions:

For **Key Terms and Definitions** on Card Issuing Issues, please see ****[Card Issuing Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22857173195794-Issuing-Glossary-Introduction) 

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Card Issuing articles, please see ****[Card Issuing Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22857178933394-Issuing-Tools-Permissions)

---
id: 22857174440594
section_id: 28482671122194
title: "View or Change PIN"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22857174440594-View-or-Change-PIN"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:34:41Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JNGXCVNHFQB2TX90T7Z1YKMZ"]
label_names: ["global", "issuing", "case_card_issuing", "case_card_issuing_card_pin", "case_card_issuing_view_change_pin"]
user_segment_ids: [11003606966930]
archive: false
---

## Process Steps

**Virtual Cards**

There is no PIN feature for virtual cards, only physical cards. However, if needed, the PAN can be checked via Dashboard and API:-

1. 
**Dashboard**:- Issuing > Cards > Search by Card ID > About this card, and click on the eye icon to reveal the PAN details (this is permission-based)

2. 
**API**:- The user can make a separate [API call](https://www.checkout.com/docs/card-issuing/manage-cards/display-card-details#Retrieve_and_display_secure_card_details) for full or partial PAN (this is permission-based)

**Physical Cards**

1. Initial Setup: 

  1. The Onboarding team covers PIN capability with customers before going live, and in the program handbook we will include the limitations of getting the PIN outside of the [mobile SDK](https://checkout.atlassian.net/wiki/spaces/IE/pages/5615419868)

  2. Confirm with the cardholder whether they have their PIN and ensure the card is activated

2. View PIN

  1. The PIN is not viewable on the  Dashboard or via the API

  2. On our mobile SDK (which the client integrates with), the client/cardholder can use the [getPin](https://www.checkout.com/docs/card-issuing/manage-cards/display-card-details#Retrieve_the_sensitive_card_details) method to securely fetch the card’s PIN

3. Change PIN

  1. The PIN cannot be changed via mobile SDK or API

  2. Advise the cardholder to change the PIN at an ATM that supports PIN services. This is the main option for physical cards at present

4. Forgotten PIN

  1. If the cardholder does not know their PIN, then see step 2.2 above

## Glossaries and Definitions:

For **Key Terms and Definitions** on Card Issuing Issues, please see ****[Card Issuing Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22857173195794-Issuing-Glossary-Introduction) 

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Card Issuing articles, please see ****[Card Issuing Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22857178933394-Issuing-Tools-Permissions)

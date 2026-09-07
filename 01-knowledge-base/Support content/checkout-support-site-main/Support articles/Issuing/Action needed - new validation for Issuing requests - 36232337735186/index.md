---
id: 36232337735186
section_id: 24567684058770
title: "Action needed - new validation for Issuing requests"
url: "https://support.checkout.com/hc/en-us/articles/36232337735186-Action-needed-new-validation-for-Issuing-requests"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-06-08T10:10:30Z"
permission_group_id: 11003577394706
content_tag_ids: ["01HTHRQ6H2MNP5MYX42MCMHAGX"]
label_names: ["Card issuing"]
user_segment_ids: []
archive: false
---

We’re writing to let you know that from August 11, 2026, we’ll update our Issuing API specification to enforce the Entity ID requirement for [create a cardholder requests](https://www.checkout.com/docs/card-issuing/create-and-manage-cardholders), and the card product identifier requirement for [issue a card requests](https://www.checkout.com/docs/card-issuing/issue-a-card).

Our API reference already requires these fields and most customers already send them. We’re making this change to maintain a consistent customer experience.

**Create a cardholder and issue a card requests without this information will fail after August 11.** 

## **What’s changing?**

- For [create a cardholder](https://www.checkout.com/docs/card-issuing/create-and-manage-cardholders), we’ll validate to check if the [entity_id](https://api-reference.checkout.com/tag/Cardholders#operation/createCardholder!path=0/entity_id&t=request) is present 
- For [issue a card](https://www.checkout.com/docs/card-issuing/issue-a-card), we’ll validate to check if the [card_product_id](https://api-reference.checkout.com/tag/Cards#operation/createCard!path=0/card_product_id&t=request) is present 

If a request fails due to this data not being provided, we’ll return a _422_ response (_entity_id_required_, or _card_product_id_required_), and you’ll need to retry the request.

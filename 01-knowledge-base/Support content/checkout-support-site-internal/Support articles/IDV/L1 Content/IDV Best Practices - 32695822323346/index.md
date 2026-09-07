---
id: 32695822323346
section_id: 32304308299922
title: "IDV Best Practices"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/32695822323346-IDV-Best-Practices"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-02-02T16:23:46Z"
permission_group_id: 26838654181266
content_tag_ids: ["01KE6V773EPR1K1MSSMYWHJ6T4"]
label_names: ["IDV"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article to**

See best practices and tips for handling an IDV case**Translating Messages 📃**

When handling an IDV case, you may receive messages from merchants in various languages. 

Use the ticket's translate function if needed, but always refer to the original message to verify the customer's name, as translations may be inaccurate.**ID Numbers 🆔**

- If the ID begins with: idv_XXX it's a verification ID and needs to be entered into the `Verification ID` field in Looker.

- If it doesn't start with idv_XXX it needs to be entered in the `Identification Uuid` field.

**Accessing Real-Time Merchant IDV Data**

When handling Identity Verification (IDV) cases on the same day they are processed, agents must use the [Personal Data Dashboard](https://odash.ubble.ai/verifications) (O Dash) rather than Looker. 

There is a one-day synchronization delay before IDV data is reflected in Looker; checking the O Dash directly ensures you are viewing the most up-to-date information and prevents delayed resolutions.

---
id: 32867282498066
section_id: 21991151260690
title: "Understanding the \"Issuer Country\" Field"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/32867282498066-Understanding-the-Issuer-Country-Field"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-01-27T15:22:59Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

You need to understand what the 'Issuer Country' field is and why it's important**Overview 💬**

The **Issuer Country** field is a standard data point found in financial action and settlement reports. It identifies the geographical origin of the payment method used in a transaction.

The information is pulled directly from the **Issuing Bank's registration data**. When a transaction is processed, the system identifies the card's origin based on the Bank Identification Number (BIN).**Key Technical Specifications 💡**

**Source:** The country where the cardholder's bank is legally registered.

**Format:** The field uses a two-letter code system used globally to represent countries.

- _Example:_ **US** = United States

- _Example:_ **GB** = United Kingdom

- _Example:_ **CN** = China

- _Example:_ **JP** = Japan

**Why is this field important? 💡**

- **Fee Calculation:** Processing fees (Interchange) often differ between "Domestic" and "International/Cross-border" cards.

- **Fraud Monitoring:** High-risk transactions are often flagged based on the discrepancy between the Issuer Country and the IP address or shipping address.

- 
**Reconciliation:** Helps finance teams categorize revenue by region.

###

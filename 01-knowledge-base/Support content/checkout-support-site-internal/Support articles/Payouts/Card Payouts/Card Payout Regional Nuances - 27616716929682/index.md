---
id: 27616716929682
section_id: 27616639185042
title: "Card Payout Regional Nuances"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/27616716929682-Card-Payout-Regional-Nuances"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:34:13Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JYHD3VT0SMH2B173EZEKRH5D"]
label_names: ["merchant_care_faqs", "card_payout", "card_payout_regional_nuances"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article:**

This article explains regional rules for Card Payouts. Merchants can use Card Payouts to send instant, 24/7 payments to their customers' Visa or Mastercard accounts. This guide helps our Merchant Care team follow specific regional regulations.

 

## INTRODUCTION TO CARD PAYOUTS** 💬**

Card Payouts lets merchants send funds to their customers using the Visa and Mastercard card rails. Card payouts can be performed 24/7 with the recipient receiving the funds in near real-time. 

Card Payouts is an end-to-end payment processing product. Requests come from the merchants through our Unified Payments API and get processed via our GW and acquiring platform before going to the card schemes. 

To securely protect card details and monitor all payments for fraud and other security risks, we'll use our Vault to tokenise the merchant's card details and our Risk Ops platform for sanctions screening/transactions monitoring.

Merchants will use our Balances product for funds management, for example how they get funds into their currency account to fund their card payouts. There are two ways to do this:

1. Pay-in funds with an optional Operational Funding balance

2. Top-Ups (pending stored value licence approval)

 
 
**KEY TAKEAWAYS 🔑**
Below are the different regional regulatory rules for Card Payouts:
 

| Category | MENA | UK & EEA |
| --- | --- | --- |
| Unsupported Cases | - Gaming and Gambling is **illegal** in this region  - Merchants in this industry **cannot use** our Card Payouts in the UAE | - Gaming and Gambling is **allowed** in this region  - Merchants in this industry **can use** our Card Payouts in the UK & EEA |
| Funding Types | - **Acquiring funding only**  - Currently, we don't have the correct license from the Central Bank to offer top-ups in the UAE (Product are working towards this in 2025) | - Full funding model available, including top-ups |
| Currency | - [Holding](https://checkout.atlassian.net/wiki/spaces/TFP/pages/906297914/Supported+currencies+for+Currency+accounts)  - [Processing](https://checkout.atlassian.net/wiki/spaces/TFP/pages/906297914/Supported+currencies+for+Currency+accounts) | - [Holding and Processing](https://docs.google.com/spreadsheets/d/1LDtL919frbByfQQ8RsNtyRY7rqJNvqQb7NUtMiOswSQ/edit?gid=673787307#gid=673787307) |
| Scheme | - Card Schemes are encouraging all issuers to be ready for card payouts, but readiness differs across countries. The latest data on this can be found [here](https://drive.google.com/drive/folders/1ALL481GSO1w4gSKvjS_zc9qDprSnFVp2).  -  **As this is a new scheme product in the MENA region**, **issuers may not be familiar and transactions may be declined**. We'll be monitoring and working with the schemes and issuer outreach, but **please manage merchant expectations carefully.** |  |
| AML | - Checkout needs to perform sanctions screening and transaction monitoring checks on both the sender and recipient of funds  - This is included as part of both the onboarding process and ongoing realtime checks on transactions  - The types of checks that Checkout needs to perform can vary in each region. For more information, you can contact the respective regional MLRO. |  |

 
 

## ESCALATION** ⏫**

- Use the slack [#ask-card-payouts](https://checkout.enterprise.slack.com/archives/C04776NRR8T) channel for internal queries that need to be directed to Product or Engineering

- Echo can also help with Card Payout related questions

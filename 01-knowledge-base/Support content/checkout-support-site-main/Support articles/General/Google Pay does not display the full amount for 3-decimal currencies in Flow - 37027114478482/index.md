---
id: 37027114478482
section_id: 16340605590546
title: "Google Pay does not display the full amount for 3-decimal currencies in Flow"
url: "https://support.checkout.com/hc/en-us/articles/37027114478482-Google-Pay-does-not-display-the-full-amount-for-3-decimal-currencies-in-Flow"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-07-07T12:21:37Z"
permission_group_id: 11003577394706
content_tag_ids: []
label_names: ["Technical issue - Integration methods - Flow / frames", "Technical issue - Integration methods - Apple Pay / Google Pay"]
user_segment_ids: []
archive: false
---

Google Pay displays amounts using two decimal places. However, some currencies such as the Kuwaiti Dinar (`KWD`) and the Bahraini Dinar (`BHD`) use three decimal places. For these currencies, Google Pay rounds the third decimal to the nearest `0` or `5` to fit its two-decimal display.

This rounding only affects what your customer sees in Google Pay. Checkout.com processes and charges the exact amount you provide when you create the payment session, and this amount appears in your transaction records.

For a full list of currencies that use three decimal places, see [Format the amount value](https://checkout.com/docs/payments/accept-payments/format-the-amount-value#The_amount_divided_by_1000).

Flow processes the exact amount you send, but your customer sees a rounded amount in Google Pay.

For example, with the Kuwaiti Dinar (`KWD`):

| Amount you send | Amount your customer sees |
| --- | --- |
| `126.644 KWD` | `126.640 KWD` |
| `126.645 KWD` | `126.650 KWD` |

To avoid confusion with your customers, inform your support team about this display behavior. You can also round the amount to two decimal places before you create the payment session.

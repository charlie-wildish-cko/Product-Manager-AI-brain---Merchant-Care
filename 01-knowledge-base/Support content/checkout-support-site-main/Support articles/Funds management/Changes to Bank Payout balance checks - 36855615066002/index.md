---
id: 36855615066002
section_id: 22325749323794
title: "Changes to Bank Payout balance checks"
url: "https://support.checkout.com/hc/en-us/articles/36855615066002-Changes-to-Bank-Payout-balance-checks"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-07-01T08:37:11Z"
permission_group_id: 11003577394706
content_tag_ids: ["01KRB60N7NEHKMB5GM303NYCV7"]
label_names: []
user_segment_ids: []
archive: false
---

From September 1, 2026, we’ll update our funds availability checks from Bank Payouts to check against the **available balance only**. 

If your available balance is sufficient at the time of instruction, your payouts will process as normal. If your available balance is insufficient, **the payout will be declined**,and you’ll receive a [webhook](https://www.checkout.com/docs/developer-resources/event-notifications/event-types/payment_refund_declined) with the code 50003 - Balance reservation insufficient funds.

**You’ll need to ensure you have sufficient available balances on your account to fund your bank payout volumes before we make this change**.   
  
Use our Business Account features to account for changes caused by your settlement frequency and avoid payout interruptions: 

- [Balance minimum](https://www.checkout.com/docs/funds-management/manage-funds/balances/manage-balances#Set_a_balance_minimum_): Available for entities in Europe, Singapore, the UK, and US. Balance minimum lets you hold a configurable amount in your Available balance to ensure you always have sufficient balances to cover refund amounts.
- [Balance top-ups](https://www.checkout.com/docs/funds-management/move-funds/add-funds): lets you add one-off funding top-ups to your Available or Operational balances, ensuring you can process refunds if you expect your refund requests to increase.
- [Balance notifications](https://www.checkout.com/docs/funds-management/manage-funds/balances/manage-balances#Configure_balance_notifications_): lets you know when your Available balance falls below a specified threshold, helping you to act before your balance goes negative
- [Update your settlement schedule](https://www.checkout.com/docs/funds-management/receive-settlements/manage-settlements#Update_settlement_schedule): using a slower settlement frequency can help ensure that your Available balance is sufficient to cover your refund requests

**Note:** We will continue to use your available, pending, and operational balances to check funds availability for Card Payouts and Issuing.

---
id: 35483277316498
section_id: 14321842463378
title: "What are Mastercard's new data quality controls for Card Payouts?"
url: "https://support.checkout.com/hc/en-us/articles/35483277316498-What-are-Mastercard-s-new-data-quality-controls-for-Card-Payouts"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-07-13T09:38:22Z"
permission_group_id: 11003577394706
content_tag_ids: ["01JYHD3VT0SMH2B173EZEKRH5D"]
label_names: ["Payouts - Card payouts - Declined / failed card payout"]
user_segment_ids: []
archive: false
---

Mastercard's new data quality controls for [Card Payouts](https://www.checkout.com/docs/payments/request-payouts/card-payouts) are designed to enforce data quality requirements at a network level. Mastercard will gradually roll out these controls from July 15, 2026 onwards.

Ensure that your API requests follow Mastercard's validation rules to avoid potential declines once these changes take effect:

**Sender city**

For the [sender.address.city](https://api-reference.checkout.com/tag/Payments#operation/requestAPaymentOrPayout!path=0/sender/0/address/city&t=request):

- The sender city must not be blank
- The sender city must not contain all spaces, zeros, or unsupported special characters (underscores, hyphens, commas, etc.)
- The sender state ([sender.address.state](https://api-reference.checkout.com/tag/Payments#operation/requestAPaymentOrPayout!path=0/sender/0/address/state&t=request)) must match the sender country ([sender.address.country](https://api-reference.checkout.com/tag/Payments#operation/requestAPaymentOrPayout!path=0/sender/0/address/country&t=request))

**Sender country**

For the [sender.address.country](https://api-reference.checkout.com/tag/Payments#operation/requestAPaymentOrPayout!path=0/sender/0/address/country&t=request):

- The sender country must not be blank

**Transaction purpose**

If you send a purpose of payment in [instruction.purpose](https://api-reference.checkout.com/tag/Payments#operation/requestAPaymentOrPayout!path=0/instruction/purpose&t=request)**,** this must be a valid value.

---
id: 35006133524882
section_id: 35005877878290
title: "Platforms: Processing Payments on Behalf of Sub-Entities"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/35006133524882-Platforms-Processing-Payments-on-Behalf-of-Sub-Entities"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-04-22T10:11:04Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

This article explains how payments are processed for sub-entities, how the platform can charge a commission, the three commission models available, and an important limitation around incremental authorisation.**How payment processing works for sub-entities**

Once a sub-entity is Active and has payment capabilities enabled, the platform can process payments on their behalf. The platform includes a field called amount_allocations in each payment request to link the payment to the correct sub-entity and — optionally — to apply a commission.

The sub-entity's share of the funds is credited to their sub-account in the relevant currency. Settlement to their bank account then follows their configured settlement schedule (see Article 8).**Commission models**

If the platform charges a fee for facilitating the transaction, there are three ways to apply it:**Fixed commission**

A set amount deducted from each transaction, regardless of the transaction value. For example, $2.00 per transaction.**Variable commission (percentage)**

A percentage of the payment amount. For example, 1.5% of each transaction.**Compound commission**

A combination of the two: a fixed amount plus a percentage of the payment. For example, $0.30 plus 1.2%.

If the platform does not want to charge a commission, they omit the commission field from the amount_allocations object entirely.**Amount allocations - how funds are split**

Every payment for a sub-entity must include the amount_allocations object. The key fields are:

- id — the sub-entity's unique ID (begins with 'ent_')

- amount — the funds to be credited to the sub-entity's account, in minor currency units (for example, 1000 = $10.00 USD)

- commission.amount — the fixed commission amount in minor currency units (if applicable)

- commission.percentage — the variable commission as a percentage (if applicable)

For technical details and example API requests, direct the customer to the [process sub entity payments](https://www.checkout.com/docs/platforms/for-saas/process-sub-entity-payments) article.**Important limitation: incremental authorisation**

**⚠️ Incremental authorisation is not supported with amount_allocations. If a platform tries to increase an authorisation amount on a split payment, the increase is ignored when the payment is captured. Only the original authorised amount is processed.**

If a customer reports that an amount increase isn't being captured, this is the most likely cause. Confirm whether they're using amount_allocations and whether they attempted an incremental increase.**How to retrieve payment history for sub-entities**

The platform can retrieve individual payment details or search across their sub-entities' payment history using the Manage Sub-Entity Payments endpoints.

[Technical docs.](https://www.checkout.com/docs/platforms/for-saas/manage-sub-entity-payments)**Troubleshooting / common questions**

**Q: A customer says a payment was processed but the sub-entity hasn't received their funds.**

Check the sub-entity's status first — they must be Active with payments enabled. If Active, check the settlement schedule and balance. Funds may be in the sub-entity's Pending balance awaiting settlement. See Articles 8 and 9.

**Q: A customer reports the wrong commission was charged.**

Ask the platform to share the amount_allocations values from the payment request. Check whether the commission field was included correctly. This is a platform-side configuration issue — Checkout.com processes exactly what is submitted.

**Q: A customer says a payment was authorised for one amount but captured for a lower amount.**

This is likely the incremental authorisation limitation. If the platform used amount_allocations and tried to increase the authorised amount, that increase is ignored on capture. The platform should be aware of this limitation when designing their payment flows.

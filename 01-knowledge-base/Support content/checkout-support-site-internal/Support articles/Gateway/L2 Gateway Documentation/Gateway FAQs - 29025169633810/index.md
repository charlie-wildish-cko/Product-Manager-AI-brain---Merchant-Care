---
id: 29025169633810
section_id: 27992533473042
title: "Gateway FAQs"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29025169633810-Gateway-FAQs"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-02-04T17:45:58Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

Use this article for frequently asked questions about Gateway, you can head to the **#ask-gateway** channel on slack for any product related queries.

## General📦

 Is it possible for merchants to retrieve full card numbers rather than just masked?

Normally, only the eight-digit BIN and the last four digits of a card number are visible to merchants via API. Accessing the full card number requires specific approval and strong justification through the Vault team due to strict security measures and PCI compliance.

 

## Payment Reversal API** ◀️**

 Are merchants charged for using the Reversal API? 

Yes they are charged fees; for example if the payment is captured and they hit the reversal API then we generate a refunded event. There is no separate set of events for reversals, you will either see a refunded or voided event (both partial or full supported).

See more details in our public docs [here](https://www.checkout.com/docs/payments/manage-payments/reverse-a-payment).

 Can a reversal be cancelled after it has been processed? 

No, once a reversal is processed, it cannot be cancelled.

 Are there time limits for using the Reversal API? The time frames for the Reverse API are the same as general payment action (eg. void/refund) limits. These expiry limits are controlled by the card scheme and not at the gateway level.

## 

## Wallets** ****💳**

 Can a merchant retrieve the original card number (FPAN) using the Payment Account Reference (PAR)?

No. For applepay network tokens, only the scheme and issuer know the full card number (See document [here](https://www.checkout.com/blog/network-tokens-explained) for more information). 

This is because the PAR is designed specifically to provide a consistent reference for the account without exposing sensitive data. It is not an encrypted or tokenised version of the card number, but rather a separate, unique value.

 When do we populate walletType field in our events for gpay/pan_only transactions?

- If payment is tokenised (i.e provisioned as a CKO NT), then we don't populate the walletType field.

- If payment is not tokenised (i.e not provisioned as a CKO NT), then we populate the walletType field. 

 

## Troubleshooting API Errors** 💡**

Why might a merchant encounter a 429 error?

A merchant might encounter a 429 error because of rate limiting from the edge gateway. This happens when the number of requests a merchant makes to an endpoint, such as the payment sessions endpoint, exceeds the allowed limit in a given timeframe.

See documentation [here](https://www.checkout.com/docs/developer-resources/api/api-rate-limits) for more information on rate limiting.

 Who should be contacted to resolve a 429 error related to rate limiting? 

The product team who owns the endpoint can advise if limits should be updated; for example if it’s the payment sessions endpoint then the payment interfaces team should be consulted to understand the specific limits for a given endpoint.  

 

## Idempotency**‼️**

If two payments are successfully processed with the same idempotency key, is this expected? 

Yes, this is expected if the two payments are more than 24 hours apart. For example, if the first payment was on the 6th of September at 5pm and the second was on the 7th of September at 10pm, the second payment will be processed as normal since it falls outside of the 24-hour window.

See documentation [here](https://www.checkout.com/docs/developer-resources/api/idempotency) for more information on idempotency.Can we extend the idempotency window?

Yes as per docs [here](https://www.checkout.com/docs/developer-resources/api/idempotency#How_it_works), if a merchant wants the idempotency window updated from the default 24 hours we can raise it on the #ask-gateway channel for an engineer to action this since it requires a code change.

The maximum timeframe the idempotency window can be extended to is 7 days.

There's also an article [here](https://checkoutint.zendesk.com/hc/en-us/articles/32931545339538-Merchant-Idempotency-Window-Extensions) L1 can follow since these requests can be escalated straight to L3.

 

## Partial Authorisations**🌙**

 How can your merchant enable the partial authorisation feature?

To enable this, your merchant must send partial_authorisation.enabled: true in their POST authorisation request.

 What is the default behaviour for partial authorisations if not specified?

The default value of partial_authorisation.enabled will be false, meaning payments will not be partially authorised unless explicitly requested.

 Which processing profiles support the partial authorisation feature?

The feature only works on processing profiles; it is not supported for manual processors.

 How can you identify if a payment was partially authorised?

You will see a new response code 10010 (Partial value approved) in the POST response, GET actions, and Webhooks.

 What amount is returned in the API response for a partial authorisation?

The amount field returned in the response will reflect the partially authorised amount, rather than the original requested amount.

 Can a transaction be cancelled if the customer is unhappy with a partial approval?

Yes, you can still void the transaction if the payment has been authorised but not yet captured.

 Is any additional scheme onboarding required for merchants to use this?

No, there are no additional onboarding processes required with the card schemes to enable this feature.

 Which card schemes currently support partial authorisations?

The supported schemes are Visa, Mastercard, and American Express (the latter is currently in Beta for US merchants).

 Which processing flows are compatible with partial authorisations?

All checkout-acquiring flows are supported. However, Third-Party Acquiring (TPA) flows do not support this feature.

 How does auto-capture behave with partially authorised payments?

If your merchant has requested auto-capture and the payment is partially authorised, the system will proceed by capturing the partially authorised amount.

 How can you distinguish between the requested and authorised amounts in the API payload?

In the response, the "amount" field shows the authorised value, while the "amount_requested" field displays the original total requested by the merchant.

 What field indicates if a payment was a partial authorisation in a GET response?

You should check the is_partial_authorization boolean field, which will be set to true for partial approvals.

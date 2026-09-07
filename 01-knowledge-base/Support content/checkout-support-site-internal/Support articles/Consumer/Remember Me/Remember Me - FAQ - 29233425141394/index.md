---
id: 29233425141394
section_id: 29233372227218
title: "Remember Me - FAQ"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29233425141394-Remember-Me-FAQ"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:33:43Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K4ARNDZQ2EX69KFY8XGCPWZE"]
label_names: ["Consumer", "Remember_Me", "L1", "FAQ"]
user_segment_ids: [11003606966930]
archive: false
---

Use this article for quick answers to frequently asked questions about the Remember Me product.

 

## GENERAL FAQs** ❓**

 **What is Remember Me**

It's a feature that allows consumers to save their payment details with Checkout.com and reuse them across all merchants who have the feature enabled, making checkout faster and boosting conversion rates. 

 **Which merchants can use Remember Me?**

Enabled for all merchants that use either Flow or Hosted Payment Page (HPP) integrations.

 **How do consumers sign up?**

At the checkout stage, consumers tick the “Remember Me” box, enter their email/phone, and complete a successful payment.

 **What happens if a consumer enters an email that isn't theirs?**

The checkout flow will show a "Not you?" button. A user with an account can click this to log in to their correct account. A user without an account can click it to proceed to the account creation page.

 **Does the Remember Me authentication replace 3DS?**

No. The OTP authentication for Remember Me is separate and happens independently of any 3DS verification that might be triggered by an issuer, merchant, or Checkout.com.

 

## 

## Consumer Issues FAQs** ❓**

 **How can a consumer add a new payment method?**

A consumer **cannot** add a new payment method through the dashboard. New cards can only be added during the payment journey on a merchant's website.

 **How can a consumer change their email or phone number?**

A consumer **cannot** edit their email or phone number. If their details need to be changed, they must delete their profile from the dashboard settings and create a new account during their next purchase.

 **Can a consumer remove all their cards from the dashboard?**

No. A consumer cannot remove a payment method if it is the only one on their account. An account must have at least one card associated with it. To remove the last card, the user must delete their entire profile.

 **Where do support requests from the consumer dashboard go?**

All help requests submitted via the web form in the consumer dashboard are sent to **consumer-support@checkout.com** and will create tickets in Zendesk.

 

## 

## Troubleshooting FAQs** ❓**

 **A customer didn’t receive the Welcome Email. What should I do?**

Ask them to check spam/promotions folders. If the issue persists, verify delivery in SendGrid.

 **A customer clicks 'Confirm your details' but is not redirected to the Consumer Dashboard. What should I do?**

Drop a message on the [#ask-remember-me](https://checkout.enterprise.slack.com/archives/C088LL97QQG) Slack channel about the issue. Tag both [@Ankitha Sriram](https://checkout.enterprise.slack.com/team/U07K13LBWN5) and [@Hannah Hasler](https://checkout.enterprise.slack.com/team/U090M8PNRK5).

 **What are the first steps if an OTP is not received?**

First, ask the consumer to try resending the code. For SMS, confirm they have a phone signal. For email, instruct them to check their spam/promotions folder.

 **A customer inserts the correctly received OTP but cannot log in to the Consumer Dashboard. What should I do?**

Drop a message on the [#ask-remember-me](https://checkout.enterprise.slack.com/archives/C088LL97QQG) Slack channel about the issue. Tag both [@Ankitha Sriram](https://checkout.enterprise.slack.com/team/U07K13LBWN5) and [@Hannah Hasler](https://checkout.enterprise.slack.com/team/U090M8PNRK5).

 **What tools can I use to check delivery status?**

You can use **Sendgrid** for emails. **Twilio** is used for SMS messages to check delivery status, but you will need to drop a message on the [#ask-remember-me](https://checkout.enterprise.slack.com/archives/C088LL97QQG) Slack channel and tag both [@Ankitha Sriram](https://checkout.enterprise.slack.com/team/U07K13LBWN5) and [@Hannah Hasler](https://checkout.enterprise.slack.com/team/U090M8PNRK5) to check this on the console for you

 **What should I do if a card is flagged as "not supported" or "expired"?**

The user will not be able to select this card for payment. They must either choose another saved card or add a new one during the payment journey.

 **What should I do if a card is expired or unsupported?**

Please let the consumer know to add a new card during checkout or through the dashboard.

 **How do we handle fraud concerns?**

Collect consumer ID, card details, and transaction timestamp. Escalate to [remember-me_consumer-support@checkout.com](mailto:remember-me_consumer-support@checkout.com).

##

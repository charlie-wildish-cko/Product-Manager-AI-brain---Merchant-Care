---
id: 29233477111698
section_id: 29233372227218
title: "Remember Me - Troubleshooting"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29233477111698-Remember-Me-Troubleshooting"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:33:43Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K4ARNDZQ2EX69KFY8XGCPWZE"]
label_names: ["SOP", "Consumer", "Remember_Me", "L1"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article:**

This article is a step-by-step guide for troubleshooting consumer issues with Remember Me, such as problems receiving welcome emails or SMS OTPs, and issues with the returning user login process.

It is used when a Merchant Care agent needs to diagnose and resolve specific issues reported by consumers using the Remember Me feature.

 

## INTRODUCTION TO REMEMBER ME** 💬**

This SOP provides step-by-step guidance for Merchant Care teammates when assisting consumers with issues related to the Remember Me product. It outlines the processes for diagnosing and resolving issues reported by consumers using Remember Me. 

It covers troubleshooting for the new user sign-up flow, the welcome email and verification process, and the returning user authentication flow. 

Following these steps will help you provide effective support and determine when an issue requires technical escalation.

 

## PROCESS STEPS FOR TROUBLESHOOTING

### 

**Scenario 1: Consumer Did Not Receive Welcome Email**

After a consumer successfully creates a Remember Me account, they should receive a welcome email. If they report not receiving it, follow these steps.

- 
**Step 1. Advise Consumer to Check Other Inboxes**

  - Instruct the user to check their **spam** and **promotions** folders in their email client

- 
**Step 2. Verify Email Delivery Status on Sendgrid**

  - 
Copy the Template ID from the dynamic templates for the email:

    - Welcome email: d-1c611df88d1541918c7f77c45966addc

    - Consumer wallet code: d-cb5e0cf44adf4f63b7db8beedc0d9bd0 

  - Go to **Activity** and select **Advanced search:**

  - In **Advanced search**, click the dropdown by **Dates**, change it to **Transactional Template ID:**

  - Paste your **Template ID** into the search window and click **search**. You can also add a filter for date to search in a range:

  - 
Review the returned results and check the status. Below is a table with the different status types and what they mean:

| **Status** | **Description** |
| --- | --- |
| **Processed** | SendGrid has received the message and is preparing it for delivery. This is the initial step for every email sent. |
| **Dropped** | The email was not sent to the recipient. Common reasons include a prior unsubscribe, a previous bounce, or a [spam](https://sendgrid.com/content/sendgrid/global/en-us/blog/10-tips-to-keep-email-out-of-the-spam-folder/) report |
| **Deferred** | The email delivery has been temporarily delayed (a soft bounce). SendGrid will continue to attempt delivery for up to 72 hours. |
| **Bounce** | The receiving server has permanently rejected the email. This is a hard bounce, often due to an invalid or non-existent email address. |
| **Delivered** | The recipient's email server has accepted the message. This does not guarantee the email has reached the recipient's inbox. |
| **Open** | The recipient has viewed the email with images enabled, which is tracked via a transparent pixel. |
| **Click** | The recipient has clicked on a link within the email. |
| **Spam Report** | The recipient has marked the email as spam and reported it to their email [provider](https://sendgrid.com/content/sendgrid/global/en-us/blog/email-feedback-loops-top-4-tips-on-how-to-use-them/). |
| **Unsubscribe** | The recipient has clicked the unsubscribe link in the email. |

- 
**Step 3. Escalate if the consumer confirms details and is not redirected to the Consumer Dashboard**
If the email issue is solved, but the consumer does not get redirected to the Consumer Dashboard upon clicking 'Confirm your details' button:-

  - Drop a message on the [#ask-remember-me](https://checkout.enterprise.slack.com/archives/C088LL97QQG) Slack channel about the issue

  - Tag both [@Ankitha Sriram](https://checkout.enterprise.slack.com/team/U07K13LBWN5) and [@Hannah Hasler](https://checkout.enterprise.slack.com/team/U090M8PNRK5)

**Scenario 2: Consumer Not Receiving SMS OTP to Verify Login**Consumers need an OTP sent via SMS to verify their account or log in as a returning user. If they report not receiving the SMS, follow these steps.

- 
**Step 1. Perform Basic Checks with the Consumer**

  - Advise the consumer to use the **"Resend code"** option

  - Confirm they have an adequate **phone signal**

  - Ask them to confirm they are using the **correct phone number** associated with their account; they can verify the last two digits from the welcome email if they have it

- 
**Step 2. Verify Phone Number in Consumer Dashboard (If Accessible)**

  - If the consumer can log in via email OTP instead, have them check the phone number listed in the **Settings** section of the Consumer Dashboard

  - If the number is incorrect, the only resolution is for the user to **delete their profile** via the dashboard and create a new account with their next purchase

- 
**Step 3. Check SMS Delivery Status in Twilio**

  - Drop a message on the [#ask-remember-me](https://checkout.enterprise.slack.com/archives/C088LL97QQG) Slack channel about the issue to find out what the SMS status is, tagging both [@Ankitha Sriram](https://checkout.enterprise.slack.com/team/U07K13LBWN5) and [@Hannah Hasler](https://checkout.enterprise.slack.com/team/U090M8PNRK5)

  - 
Product will access the [](https://console.twilio.com/)[Twilio Console](https://console.twilio.com/) to review the messaging (using **timestamp** and **phone** **number**) to check the status column:-

  - Below is a table with the different status types, what they mean, and the relevant action:

| **Status** | **Description** | **Action** |
| --- | --- | --- |
| **Sent** | Typically, a `sent` status will be replaced by a `delivered` or `undelivered` status within seconds or minutes | None. User has received the message. Ask them to check again or to re-attempt when phone signal is re-established |
| **delivery_unknown** | This indicates that a message has remained in the `sent` status for longer than 1 hour without receiving a further status update. This status is only shown in Messaging Insights; SMS records will remain in the `sent` status in the Message Log or /Messages API | Contact notifier team |
| **delivered** | Twilio has received confirmation of message delivery from the carrier, (and, where available, the destination handset). | None. User has received the message. Ask them to check again or to re-attempt when phone signal is re-established |
| **undelivered** | Twilio has received a delivery receipt indicating that the message was not delivered. This can happen for a number of reasons including carrier content filtering, availability of the destination handset, etc | Contact notifier team |
| **failed** | The message could not be sent. This can happen for various reasons including queue overflows, account suspensions and media errors | Post message for team notifier. It’s likely an API Request failed or that the provider did not accept the message |
| **No status found** | The message could not be sent. This can happen for various reasons including queue overflows, account suspensions and media errors | Post message in #team-remember-me |

- 
**Step 4. Escalate if the consumer inserts the correct OTP, but fails to log in to the Consumer Dashboard**
If the consumer inserts the correctly received OTP, but cannot get into the dashboard:-

  - Drop a message on the [#ask-remember-me](https://checkout.enterprise.slack.com/archives/C088LL97QQG) Slack channel about the issue

  - Tag both [@Ankitha Sriram](https://checkout.enterprise.slack.com/team/U07K13LBWN5) and [@Hannah Hasler](https://checkout.enterprise.slack.com/team/U090M8PNRK5)

**Scenario 3: Returning Consumer is Not Recognised at Checkout**A returning user should be automatically recognised by their email address on a participating merchant's site. If this fails, it may indicate an issue with the integration.

- 
**Step 1. Confirm Merchant Eligibility**

  - To see which merchants have Remember Me enabled, you have two options:-

    - Google Sheet: [Remember Me Enablement](https://docs.google.com/spreadsheets/d/1YIQUdY8iFnXcp5f_n9MtCRFgMeEmKQAOBD3HubEhCXE/edit?usp=sharing) (quickest solution)

    - Looker: [Remember Me Metrics - [Internal]](https://checkoutinternal.eu.looker.com/dashboards/13267?Session+Created+Date=30+day+ago+for+30+day&Is+Remember+Me+Session+%28Yes+%2F+No%29=Yes&Client+Is+Test+%28Yes+%2F+No%29=No&Alias=&Card+Wallet=&Go+Live+Region=)

- 
**Step 2. Escalate for Technical Support**

  - If a participating merchant's integration is failing to recognise consumers, **technical support is required**. Escalate to [remember-me_consumer-support@checkout.com](mailto:remember-me_consumer-support@checkout.com)

 

## RESOLUTION **🛠️**

- By following these steps, the expected outcome is that the consumer can successfully receive their verification communications, log in to their account, and use the Remember Me service.

- If an issue persists after completing all relevant steps, it should be escalated for technical review.

 

## ESCALATION** ⏫**

- For general escalations and technical issues that cannot be resolved with the available SOP, please contact [remember-me_consumer-support@checkout.com](mailto:remember-me_consumer-support@checkout.com)

 

## RESOURCES **📍**

** **

| **Tools** | **Case Examples** | **Related** |
| --- | --- | --- |
| - [Consumer Dashboard](https://consumer-dashboard.checkout.com/)  - [Twilio](https://console.twilio.com/)  - [Sendgrid](https://login.sendgrid.com/) | - [Demo Video](https://drive.google.com/file/d/1t0a7iLOd6DA8LB7rY4hSOXMaU4MGXr0A/view?resourcekey) | -  [Sendgrid Access Request](https://checkoutsupport.freshservice.com/support/catalog/items/468)    - Access type: User / Standard   - [Twilio Help Center](https://help.twilio.com/articles/223134347-What-are-the-Possible-SMS-and-MMS-Message-Statuses-and-What-do-They-Mean-)  - [Sandbox Mock Ups](https://flow-remember-me.cko.solutions/)  - [Consumer Facing FAQs](https://www.checkout.com/for-consumers/faq) |

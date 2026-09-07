---
id: 22605408459794
section_id: 22604755838098
title: "OOB"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22605408459794-OOB"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:35:59Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRP1QGWAFPTEP0CSMC1WBV"]
label_names: ["global", "case_3ds_issues", "oob", "case_3ds_issue_sdk_integration"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

Checkout.com’s Out-of-Band (OOB) Authentication SDK enables iOS apps to authenticate users for digital transactions (3DS). Our OOB SDK enables you to offer a modern 3DS challenge method alongside existing challenge types, such as OTP.

OOB involves utilising a secondary factor, such as your phone’s banking app, to authenticate payment and encompasses the fundamental processes of device binding and transaction authentication. Our OOB SDK is focused on this use case.

## Process Steps

**Authentication Requirements**

While Checkout.com handles in-depth compliance, you are required to perform SCA on your users.

You can generate multiple tokens for different systems during a single authentication session. For example, to sign in, to get an SDK session token, or to get an internal authentication token.

However, you can only generate a single SDK session token for each SCA flow requested.

**OOB IOS**

[https://www.checkout.com/docs/developer-resources/sdks/out-of-band-authentication-sdks/out-of-band-authentication-ios-sdk](https://www.checkout.com/docs/developer-resources/sdks/out-of-band-authentication-sdks/out-of-band-authentication-ios-sdk)

**OOB Android**

[https://www.checkout.com/docs/developer-resources/sdks/out-of-band-authentication-sdks/out-of-band-authentication-android-sdk](https://www.checkout.com/docs/developer-resources/sdks/out-of-band-authentication-sdks/out-of-band-authentication-android-sdk)

## Glossaries and Definitions:

For **Key Terms and Definitions** on 3DS, please see ****[3DS Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22059673420818-3DS-Glossary-Introduction)   

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the 3DS articles, please see ****[3DS Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22059810908306-3DS-Tools-Permissions)

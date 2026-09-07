---
id: 30420505377554
section_id: 27822398640530
title: "Applepay Payments Upgraded to 3DS"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/30420505377554-Applepay-Payments-Upgraded-to-3DS"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-11-07T09:19:25Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JVM5WYPR2CFA1MQCGT9B790K", "01K88KMDJZD60ZQNV0AB4KFZMJ", "01K88KMKXCKK58ADQ8V85HS2EP", "01K88KP6JD4E6GDQCYNDAPRMJX"]
label_names: ["apple_pay", "3DS_Exclusion", "Routing_Rule", "Digital_Wallets"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

This guide is for support agents who want to investigate why Applepay payments are upgraded to 3D Secure (3DS). This should be disabled as it is crucial for maintaining a seamless, biometric-based user experience for wallet payments.

**Problem/Solution**

**Problem** - Merchant's Apple Pay and Google Pay transactions are being incorrectly upgraded to 3DS, causing customer friction and payment delays.

**Solution** - Update the affected static routing rules to explicitly exclude transactions where the digital wallet type is 'applepay' or 'googlepay'.

**L2 TROUBLESHOOTING GUIDE USE:**

- Excluding Digital Wallets (Apple Pay/Google Pay) from 3DS Upgrades via Routing Rules

## DESCRIBE THE ISSUE 💬

The merchant is reporting a **persistent delay at the payment step** (up to ~35 seconds) and a suboptimal user experience for their customers using **Apple Pay**. The core issue is that their Apple Pay transactions are being **upgraded to 3DS** due to an existing routing rule, which is an incorrect flow as Apple Pay biometrics (Face ID/Touch ID) already serve as the 3DS confirmation. This issue affects **all customers** using Apple Pay on the merchant's platform. 

The product/topic is **Routing** and **3D Secure/Authentication**. 

## KEY TAKEAWAYS 🔑

- Do not upgrade** Apple Pay **(and typically **Google Pay) **transactions to a separate 3DS challenge; the wallet's biometrics/PIN act as the authentication.

- The upgrade to 3DS was caused by an existing **static routing rule** intended for credit/prepaid card types.

- Resolution: Request the Merchant Configuration team to update the rule condition to explicitly exclude digital wallet types.

- The updated rule adds the exclusion to their static rule: AND not (:digital_wallet_type: in ['applepay', 'googlepay']) via retool.

## RESOURCES 📍

| Tools | Case Examples | Related |
| --- | --- | --- |
| [Retool - Routing Admin Search](https://retoolprod.mgmt.ckotech.co/apps/d0306962-1345-11ed-8b65-7fe1bad1fd50/routing/Routing%20Admin%20-%20Search) [Sherlock](https://retoolprod.mgmt.ckotech.co/apps/918d2a72-4c5a-11ec-88dc-53fd2c6a4170/gateway/Sherlock) | Case [#79036](https://checkout1360.zendesk.com/agent/tickets/79036) (MACQUEEN) Case [#81948](https://checkout1360.zendesk.com/agent/tickets/81948) (DaleelStore) |  |

 

## PROCESS FOR INVESTIGATING APPLEPAY 3DS UPGRADES 🖊️

### Step 1. Verify if 3ds upgrade is caused by a routing rule

- Search the payment id in [Sherlock](https://retoolprod.mgmt.ckotech.co/apps/918d2a72-4c5a-11ec-88dc-53fd2c6a4170/gateway/Sherlock) (eg. pay_ywukqbyncfcuta6w2uwfnyuyse) and under Events tab, check the Routing.Modified event and check if static route_type is "Static".

### Step 2. Identify Routing Rule causing the 3ds upgrade

- Navigate to [Routing Admin Search](https://retoolprod.mgmt.ckotech.co/apps/d0306962-1345-11ed-8b65-7fe1bad1fd50/routing/Routing%20Admin%20-%20Search) (Retool).

- Search using the **static_route_id** from the `Routing.Modified` event (e.g., `ro_oxcp4qzvpghujmxv7rimaalqri`) **OR** the **processing channel ID** (e.g., `pc_yqaw7ab225qehnhuisbo3abqbe`).

- Find the route name related to the payment and if it's a 3ds upgrade route it will look similar to the condition below:

## RESOLUTION ⚒️

- Reach out to the **Merchant Configuration** team using the macro (Transfer > Merchant Configuration).

  - Ask them to **update the merchant's 3DS static rules** to **exclude wallet payments** (i.e., Apple Pay/Google Pay). They will apply this change via a Retool application.

  - Once rule updated, it will look similar to the below:

```(:card_type: in ['CREDIT', 'PREPAID'] AND :scheme: = 'VISA' 
AND not (:digital_wallet_type: in ['applepay', 'googlepay']))
```

- Expected Result: Apple Pay (and Google Pay) transactions will no longer be upgraded to 3DS, even if 3DS is sent as `true` in the payment request. They will use the faster, standard biometric/cryptogram-based authentication flow. This resolves the 35 second delay and improves the user experience.

## ESCALATION** ⏫**

- The issue persists after confirming the rule change has been correctly applied (i.e., Apple Pay transactions are _still_ getting a 3DS challenge), escalate this to merchant configuration team to check further.

- If merchant configuration are unable to advise, we may need to escalate this to routing team via the L3 form [here](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277) and we can paste it on [#ask-routing](https://checkout.enterprise.slack.com/archives/C04N6TX7NNP) if needed.

 

## FAQs** ****❓**

Why shouldn't Apple Pay or Google Pay transactions go through a separate 3DS challenge?

Digital wallet payments like Apple Pay and Google Pay use biometric authentication (Face ID, Touch ID, or device PIN) at the point of payment. This strong customer authentication method is cryptographically secure and is generally considered to satisfy the requirements of 3DS (3D Secure). A secondary 3DS challenge is redundant, adds unnecessary friction, and can cause delays.What is the difference between this fix and setting `3ds.enabled:false` in the API request?

Setting `3ds.enabled:false` prevents the upgrade at the API request level, which is a good temporary or merchant-side fix. This SOP's solution updates the **server-side routing configuration**. This is a more robust, long-term solution that ensures the platform's internal rules correctly handle digital wallet payments without requiring the merchant to change their API integration logic.

---
id: 22903181437330
section_id: 21991135458066
title: "Interchange Fees (IC)"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22903181437330-Interchange-Fees-IC"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-31T16:57:37Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHQKPVKA7XAZRYSRWE7JRH4"]
label_names: ["row", "case_settlements", "case_settlements_issue_fees_charged_for_transaction", "ic_fees", "interchange_fees"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

Interchange fees are charged to merchants after a delay that can range from 1 up to 5 days. This can impact merchants' reconciliation experience and can be confusing. The fact it is delayed is not universally known across Checkout meaning specialist teams need to be contacted for answers which can take too long, impacting the merchant experience.

## Process Steps

### Scenario 1

Interchange fees are currently calculated by the schemes and passed through when Checkout receives the data, resulting in a lag where fees are charged to merchants between T+1 and T+3 days post-capture. In most cases it is T+1 but in rare cases, it can be even up to T+5. Merchants should be made aware of this so they can build necessary operational processes around it.  
 How to Solve

Firstly:

1. 
**If it is **_**less than 1 day**_** since capture:** then inform the merchant of the above and wait until 5 days have passed to check the financial action report/dashboard, where the interchange fee should now appear

2. 
**If it is **_**more than 1 day **_**since capture: **check the financial action report/dashboard, where the interchange fee should appear

If no interchange fee is found after 5 days, please contact the [Network Fee Management](mailto:networkfeemanagement@checkout.com) team.

Secondly:

1. 
**Offer merchant Predictive Interchange:** merchants can receive their interchange fees at the point of capture (T+0), removing this delay. To do this, merchants must be onboarded onto Predictive Interchange

2. The process for enabling a merchant can be found here: [Predictive IC - Onboarding Process Proposal & Comms [Oct 2024]](https://docs.google.com/presentation/d/1E5A-dxv324psTIQK44VNK2ODN5bSUV2ImwtTl5yHS-4/edit#slide=id.g3084abf2537_0_1) or enabled through [raising a Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277)

 

### Scenario 2

As interchange fees are calculated by the scheme and passed through to Checkout, we do not have the data point that states whether it is a _**fixed**_ (e.g. $0.01) or _**variable**_ (e.g. 0.05%) fee, so all interchange fees are reflected as _**fixed.**_How to Solve

1. 
**Offer merchant Predictive Interchange: **merchants must enable this feature if they wish to see interchange fees reported correctly as fixed and variable
How to offer Predictive Interchange to Merchants

_“To remove these two issues, we have a product in **beta** that we could enable known as Predictive Interchange (Visa & MasterCard only). This has the following benefits:_

1. _Simplified Reconciliation: interchange fees will be charged in real-time at the point of capture_

2. _Granular Fee Details: interchange fee details will be visible on the ‘Financial Actions’ report_

_Please note this feature requires approval from our internal Product team; we will inform you if you are a good candidate for this.”_

ℹ️ For **US merchants**, please include ‘Pinless Debit’ as another supported network.

⚠️ **Do not offer to merchants in AU**

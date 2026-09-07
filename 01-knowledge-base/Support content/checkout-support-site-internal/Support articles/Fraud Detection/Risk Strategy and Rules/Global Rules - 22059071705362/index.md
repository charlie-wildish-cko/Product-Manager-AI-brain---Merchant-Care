---
id: 22059071705362
section_id: 28496987889682
title: "Global Rules"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22059071705362-Global-Rules"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:37:34Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRPZZM25CJTKMYW0WZXMXX"]
label_names: ["global", "cko_level_decline", "case_fraud_issue_decline_list_risk_rules", "case_fraud_detection", "global_rules", "card_decline_list_auto", "excessive_retries_auto_block_list_additions"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

Internal CKO-level rules apply to all merchants. The [Global Rules Dictionary](https://checkout.atlassian.net/wiki/spaces/RA/pages/6092587152/Global+Rules+Dictionary) lists all global pre-auth rules that currently run on production on Fraud Detection. Agents can also find these rules under the CKO account on the Fraud Detection Tool.

 

Merchants can bypass the Global Rules or Blacklist by setting the risk.enabled = false. In addition, the ‘Allow Risk Flag’ needs to be enabled on CAT (at the entity level) by the Merchant Configuration team. Approval for this is required from the Risk team. To gain approval, the agent will need to contact [risk@checkout.com](mailto:risk@checkout.com) by creating a side conversation on Zendesk. For a step-by-step guide on how to create a side conversation, please refer to the following confluence page - [Case Handling - SOP](https://checkout.atlassian.net/wiki/spaces/CHEC/pages/5991727266/Case+Handling+-+SOP).

 

## Process Steps

### Card Decline List (Auto)

The Global Card Decline List includes card numbers that are automatically added. Payments that meet certain criteria are typically blocked by the issuer. To prevent unnecessary costs for merchants, like scheme fees or additional fines for Checkout.com, these card numbers are proactively blocklisted. This can occur for various reasons, such as payments involving lost or stolen cards, or temporary blocks when the issuer suggests retrying the transaction at a later time.

Please refer to the following documentation for further details - [Blocklist Additions](https://checkout.atlassian.net/wiki/spaces/RISK/pages/6339657888/Blocklist+Additions).

 

### Excessive Retries Auto-block List Additions

CKO has introduced automation to prevent excessive payment retries, particularly for merchant-initiated transactions that are repeatedly declined. These transactions, which typically result in final decline codes (e.g., 2XXXX or 3XXXX), are now blocked earlier (at the CKO global level) to avoid incurring unnecessary scheme fees.  Under this system, retries in specific scenarios will be automatically declined by our API with a 40101 — Risk blocked transaction response code, preventing them from being sent to the issuer.

You can find the Card Retry Decline list under the CKO account on the Fraud Detection Tool.

How It Works

Both Visa and Mastercard impose fines if merchants retry declined transactions or make too many retry attempts within a short period (e.g., 24 hours or 30 days).

When a transaction receives certain response codes, it triggers the system to block further retry attempts based on specific criteria. 

- For Visa: Cards are added to the “Card Retry” block list using a combination of the following attributes: entity_id and card fingerprint.

- For Mastercard: Transactions are added to the “Payment Retry” block list for 30 days using a combination of the following attributes: entity_id, card fingerprint, payment amount, and currency. Mastercard [recommendation codes](https://www.checkout.com/docs/developer-resources/testing/codes/recommendation-codes) require merchants to avoid retrying within 30 days.

The Risk Analytics team has curated a list of gateway response codes that determine which transactions should be blocked.

- Issuer Exclusion List: Certain issuers may be exempt from this logic. Please refer to the following list: [https://checkout.slack.com/archives/C01DP70ANJG/p1722937150435679?thread_ts=1722937129.959699&cid=C01DP70ANJG](https://checkout.slack.com/archives/C01DP70ANJG/p1722937150435679?thread_ts=1722937129.959699&cid=C01DP70ANJG).

- 
Card Decline List: A list of globally blocked card numbers (e.g., stolen or fraudulently used cards) is maintained to prevent these cards from being used for any merchant globally. Please refer to the following list: [https://checkout.slack.com/archives/C01DP70ANJG/p1722937158614729?thread_ts=1722937129.959699&cid=C01DP70ANJG](https://checkout.slack.com/archives/C01DP70ANJG/p1722937158614729?thread_ts=1722937129.959699&cid=C01DP70ANJG).
 

## Glossaries and Definitions:

For **Key Terms and Definitions** on Fraud Detection, please see ****[Fraud Detection Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22059026944914-Fraud-Detection-Glossary-Introduction)  

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Fraud Detection articles, please see ****[Fraud Detection Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22059041810194-Fraud-Detection-Tools-Permissions)

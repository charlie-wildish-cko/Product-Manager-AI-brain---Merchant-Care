---
id: 26983823215762
section_id: 27060550224018
title: "INTERNAL15 or response code 20015: Transaction Cannot Be Processed (Debit Network)"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/26983823215762-INTERNAL15-or-response-code-20015-Transaction-Cannot-Be-Processed-Debit-Network"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-07-18T13:47:31Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JVS26PBA73NGJJETCPWS3SPE", "01JVS27ERFT6CA591PZY4AV4SZ", "01JW8F8Z9WAV7YPQSVX91NGR1F", "01JW8F94S6RRS5F1AFKHZYKRGP", "01JWGFWY315YMYH2FRS3HQHNXZ"]
label_names: ["card_processing", "scheme_declines"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

For information on what to do if you get a response code 20015 (INTERNAL15), indicating that a transaction cannot be processed through the debit network. 

This guide will walk you through diagnosing the problem and instructing the merchant on the necessary changes to their setup.

## DESCRIBE THE ISSUE 💬

This article explains how to resolve transaction declines associated with response code `20015` (also known as `INTERNAL15`). This error indicates that a transaction failed to process through the debit network. It commonly occurs when merchants using a bill payment setup send the transaction with the `capture` parameter set to `false`.

For these specific financial message types, it is mandatory for the `capture` parameter to be set to `true`. When sent as `false`, our Card Processing (CP) system automatically declines the transaction. While the system may attempt to reroute it to the signature network, the initial internal decline prevents successful processing. 

 

## PROCESS FOR RESPONSE CODE 20015 DECLINES  🖊️

This process outlines how to diagnose and resolve transactions declined with response code 20015.

### Step 1: Access and Review Transaction Logs

- Use **DataDog** or **Sherlock / Traffic Insight** to access the logs for the declined transaction

  - Look for the response code** **`**20015**` or `**INTERNAL15**` in the card processing logs. This confirms the decline is due to the transaction not being processable via the debit network.

 

### Step 2. Check Capture Parameter

- Within the transaction logs, inspect the gateway request data

- Locate the `capture` parameter and confirm if it was sent as `false`

💡 **Tip:** The gateway request contains all the information sent by the merchant's system for a specific transaction. Finding `capture=false` is the key piece of evidence you need.   

## RESOLUTION 🛠️

### Step 3: Advise the Merchant

- Contact the merchant and inform them that the transaction was declined because it was sent with `capture=false`

- Explain that for their bill pay transaction setup, the `capture` parameter **must** be set to `true`

✅ **Best Practice:** Provide the merchant with the transaction ID and the timestamp to help them locate the exact request in their own logs.

## ESCALATION ⏫

If the merchant has confirmed they are sending `capture=true` but transactions are still failing with the same error, an escalation is necessary.

- 
**Who to Escalate To:** The L3 Card Processing team.

- 
**How to Escalate:** Post the issue in the **#ask_routing** Slack channel to notify all relevant teams and ensure visibility. Include the case details and the troubleshooting steps you have already taken.

## FAQs ❓

What does response code 20015 mean?It signifies that the transaction could not be processed via the debit network. In this specific scenario, it's an internal decline by our system because of an incorrect parameter. Why does the `capture` parameter need to be `true` for these transactions?Bill pay transactions are a specific type of financial message that requires immediate capture to be processed correctly over the debit network rails. Sending it with `capture=false` (which typically only authorizes a payment) is not a supported workflow for this transaction type. What should I do if the merchant cannot change the parameter?If the merchant's system is unable to modify the `capture` parameter, they may need to consult with their software developer or integration provider. This is a necessary change on their end to continue processing these types of payments. If they need more technical details, escalate the case as described above.

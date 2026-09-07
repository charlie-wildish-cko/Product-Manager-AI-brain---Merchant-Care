---
id: 27801745827474
section_id: 27986946329362
title: "Troubleshooting Practices"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/27801745827474-Troubleshooting-Practices"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:34:11Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

Use this article to help you apply best practices when troubleshooting a case, you may need to take this approach when investigating an issue. 

 

## UNDERSTANDING THE MERCHANT'S NEEDS 💭

 Click here to see tips on understanding the case

- 
**Check for urgency**

  - Look for urgency keywords: __“all transactions,” “down,” “urgent,” etc.__

- 
**Gauge the sentiment**

  - Check tone: Is the merchant confused, blocked, or complaining?

Ask yourself:

- Is this a functional issue (things not working)?

- Is it a data issue (wrong or missing info)?

- Is it a setup/configuration issue?

 

## FRAMING THE PROBLEM 🧑‍💻

 The 5 W's

- 
**Who** **is impacted?**

  - Type of merchant

  - Specific regions

  - Multiple merchants?

- 
**What** **is happening?**

  - Transaction failing, delay, unexpected status, etc.

- 
**When** **did it start?**

  - Timeframe of first issue

  - Is it ongoing or intermittent?

- 
**Where**** is the issue occurring?**

  - Specific environment- production/sandbox

  - Region

- 
**Why** **is this a problem for the merchant?**

  - Business impact?

  - Blocked transactions?

  - Confusing experience?

✅ These help narrow the scope and guide the next troubleshooting step

 The How

Can you identify the root cause of the issue?

 

## GATHER SYSTEM INFORMATION 💻

 Review information in the system to help you understand

**Review Systems**

- Check merchant transactions

- Error messages or decline codes

- Look for patterns

- 
**Monitoring Tools**

  - Use tools and filters to isolate the issue by time, transaction ID etc

- 
**Logs & Internal Tools**

  - Identify error codes, timeouts or misconfigurations

 

 

## IDENTIFY PRODUCT OR FEATURE INVOLVED 📦

 Which product does this relate to?

Understanding the product is key to diagnosing any issues and figuring out the best solutions

- Map the issue to a specific product

- Check merchant settings or integration type

 

## ANALYSIS 🔍

 Time to think critically and methodically

- Is this a known behaviour, bug, or limitation?

- Can you isolate one or more potential causes?

**Reproduce if possible**

- Use sandbox to replicate issue/behaviour

- Change only one variable at a time to track effect

- Save error messages or data to refer back to

**Compare a successful transaction vs the failed transaction from the same merchant**

- What’s different?

**Can you test similar scenarios or replicate the problem internally?**

- What's different?

Try to eliminate:

- Timing issues (delays, caching)

- Configuration mistakes (permissions, tokens, rules)

- External factors (network, third-party systems)

 

 

 

## RESOLUTION 💪

 Offer a resolution or next steps

- Explain what you’ve found in plain language, share exactly what the merchant needs to do

- If you're unsure, outline what you're doing to investigate further

- Ask merchant to confirm in production 

 

 

## ESCALATION ⏫

 Before involving another team, make sure you've taken these steps

- Documented what’s already been tried

- Summarised the issue clearly and concisely

- Defined what kind of help is needed from the next team

- Included all relevant data:

  - Customer ID

  - Transaction ID

  - API version

  - Logs or trace ID snippet

  - Steps already attempted

  - Screenshot

---
id: 30192489091986
section_id: 21991151338770
title: "How to Search for a Historic Fingerprint"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/30192489091986-How-to-Search-for-a-Historic-Fingerprint"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-11-14T08:05:40Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

When you are investigating a card-related issue and the standard card identifier (the current fingerprint) is not sufficient to find the necessary historical transaction records.

## INTRODUCTION 🫆

A historic fingerprint is an earlier identifier previously associated with a specific payment card. It represents a past version of a card's unique identifier (or "fingerprint") that has changed over time due to updates or modifications to the card's details.

### What is a Historic Fingerprint?

- **Card Fingerprint:** A unique, non-reversible token created from certain card details (like the card number). It serves as a secure, permanent identifier for a specific payment card, even across different services or systems.

- **Change Over Time:** If a card's details are updated (e.g., re-issued with a new expiry date, or if a tokenization process is applied differently), the current **card fingerprint** may change.

- **Historic Record:** The historic fingerprint preserves the **previous identifier** that was in use before the change occurred.

### Why are Historic Fingerprints Important?

Historic fingerprints are crucial for tracking and investigation, especially when dealing with discrepancies related to a card's transaction history.

You can search for a historic fingerprint response using two primary methods: **Retool** or **Looker**.

## PROCESS TO FIND A HISTORIC FINGERPRINT 🖊️

### Option 1. Using Retool

This method is useful for a comprehensive look at traffic insights related to a specific charge.

- First, navigate to the **Retool** dashboard. 

- Next, click on the **ChargeRequested** event. This action will filter the data to show charge-related events.

- Once the data is filtered, search for the **historic fingerprint** to find the specific response you're looking for.

### Option 2. Using Looker

This method is faster and more direct if you already have the current card fingerprint.

- Simply insert the current card fingerprint directly into the provided Looker URL: `https://checkoutinternal.eu.looker.com/explore/payment_lifecycle/fct_payin_event?qid=y28wOLbNprtCPahfh492FP&toggle=fil`

- The link will automatically populate the query with the current fingerprint, providing you with the historic fingerprint data.

##

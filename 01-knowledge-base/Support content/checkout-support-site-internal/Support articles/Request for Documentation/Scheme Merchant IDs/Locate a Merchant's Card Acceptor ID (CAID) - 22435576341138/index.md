---
id: 22435576341138
section_id: 22435335461522
title: "Locate a Merchant's Card Acceptor ID (CAID)"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22435576341138-Locate-a-Merchant-s-Card-Acceptor-ID-CAID"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-17T15:40:25Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JBHFK1FTRFHHXXN4PTQS8A0A"]
label_names: ["global", "case_request_for_documentation", "locate_the_caid_of_a_merchant", "case_rfd_issue_scheme_merchant_ids", "CAID", "card_acceptor_ID"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To locate a merchant's Card Acceptor ID (CAID), a unique identifier crucial for processing and tracking card transactions. 
INTRODUCTION TO CAID💬

A merchant's Card Acceptor ID (CAID) is used to route and investigate transactions, resolve disputes, and ensure proper settlement of payments. 

It also plays a key role in fraud prevention, dispute resolution, and regulatory compliance.

PROCESS FOR LOCATING A MERCHANT'S CAID 🖊️

__
Method 1: Using the Checkout Agent Toolkit (Recommended)

This method is the fastest way to find a CAID for an individual payment ID.

- **Access the Toolkit** in the Zendesk ticket, go to the Apps panel on the right and expand the Checkout Agent Toolkit

- **Select a Payment: **Click on the relevant payment ID under the P**ayments **section to open its details

- **View CAID:** Navigate to the Details tab and expand **Card details** to view the **Card Acceptor ID**

- You can also expand **Merchant IDs **to see the **Scheme MID**

Method 2: Using Looker

This method is useful for a broader search and for filtering by different parameters like entity or payment ID.

- **Open Looker: **[Looker link to access the tool](https://checkoutinternal.eu.looker.com/explore/payment_lifecycle/fct_payin_event?toggle=fil&qid=QfvqqEGTRQhqONYm6TXTSp)

- **Add Filters: **In the filter tab add the relevant payment or entity ID

- **Run the Query: **Click on R**un** to display the search results, which will include the CAID

Method 3: Using the Client Admin Tool (CAT)

This method is an in-depth option for searching by various IDs or even by the client's name

- **Search for the Client: **Click on the** Search** tab

- You can search by Client ID, Entity ID, Processing channel, or by the client name

- **Find the Gateway: **In the search results, find the processing tab and choose gateway

- **View CAID: **Select the desired processing channel ID and scroll down to the Processors section

- The CAID will be listed under Billing information

TROUBLESHOOTING ⚒️

- If the CAID is not found, verify that the ID used for the search is correct. Try using an alternative search method (e.g., if searching by a payment ID fails, try searching by the entity name in CAT).

FAQs** ****❓**

What is a Card Acceptor ID (CAID)?

The Card Acceptor ID is a unique identifier that distinguishes a merchant within the payment network. It is used to ensure transactions are correctly routed and settled to the right business.Why is the CAID important?

It is essential for ensuring secure and traceable card transactions. It helps with transaction routing, fraud prevention, dispute resolution, and allows customers to recognize the merchant on their bank statements.

 

RESOURCES 📍

| Agent Toolkit | Looker | Client Admin Tool (CAT) |
| --- | --- | --- |
| Accessible within zendesk | - __[Looker - Payment Performance](https://checkoutinternal.eu.looker.com/browse)  - __[Looker - New Access](https://checkoutsupport.freshservice.com/support/catalog/items/681)  - __[Looker - Enhance Access](https://checkoutsupport.freshservice.com/support/catalog/items/682) | __[Client Admin Tool](https://client-admin.cko-prod.ckotech.co/web/nas/) |

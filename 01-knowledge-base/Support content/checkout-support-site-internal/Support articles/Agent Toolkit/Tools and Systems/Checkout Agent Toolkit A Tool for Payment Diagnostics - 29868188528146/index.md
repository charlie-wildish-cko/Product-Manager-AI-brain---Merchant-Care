---
id: 29868188528146
section_id: 28125093629970
title: "Checkout Agent Toolkit: A Tool for Payment Diagnostics"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29868188528146-Checkout-Agent-Toolkit-A-Tool-for-Payment-Diagnostics"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-01-28T11:02:55Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: ["toolkit", "agent_toolkit"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To understand the purpose and functionality of the Checkout Agent Toolkit. It provides information on how to access the tool, what data it provides and answers to common questions.What is the Checkout Agent Toolkit 💬 

This tool provides you with transaction, clearing and settlement information directly within Zendesk, meaning you no longer need to search through multiple external tools to find the data you need. Located on the right-hand side of your ticket view, it's designed to be your default starting point for diagnosing any transaction-related tickets. 

The toolkit aims to eventually replace many of the other tools you currently use, such as Looker, Retool, and Datadog, by consolidating them into one central location. It will initially focus on payins, with plans to add payouts and other features in the future.  How It Works ⚒️

The tool automatically highlights payment IDs from the ticket and displays the relevant information. Over time, it will grow to include more data points, such as TPA responses and processing profiles, to become a comprehensive resource.

⚠️ You must be connected to **Cloudflare WARP Zero Trust** to load data in the tool. If you are not connected, you will receive an error message.**Clearing & Settled Payment Status**

We've recently added the ability to show the clearing and settled payment status directly in the tool! This data is available for all events that occurred on or after 26/09/25.

You can view the status in two places:

- The **Settlement details** panel (which will be renamed to **Clearing & Settlement details)**

- The **Timeline** which shows all the events for the payment

💡 For any events that took place before 26/09/25 you will still need to use **Clearing Events Retool****Checkout Toolkit User Profile App**

 In addition to the transaction data, the **Checkout Toolkit User Profile App** is also available in the Zendesk app sidebar. This app pulls data from Salesforce and CAT to provide information about the user who submitted the ticket. 

This includes their personal details and the clients and entities they are a member of. This can help you verify the user and identify which client or entity requires support. You can easily copy any of the data with the copy icons.**Enhanced Outage Notification Visibility**

The enhanced outage capability allows us to determine if a specific merchant is currently impacted by an ongoing outage. This feature connects the outage data with our merchant database, providing a clear indication of impact- you'll be able to see which of our active merchants are directly affected.
**Payments Lookup From Attached CSVs**

- In the Toolkit app, when a CSV is on the ticket you can now get this looked up directly in app

- 
The output will post an internal note with the payment data we currently show for the auto payment lookup

 FAQs ⁉️ How do I find the agent toolkit? The agent toolkit is located in the sidebar to the right of a ticket. You can click the **+** to find and pin **Checkout Agent Toolkit** to the sidebar. It will be shown by default for Merchant Care L1 and L2 forms. Will I still need to use other tools now I can access the agent toolkit? Yes, for now. Until we can add the relevant data needed to the toolkit, you will still need to use other tools. We've included links to common tools at the bottom of the toolkit that will automatically pull the payment or charge ID for instant lookup. What environments does it cover?The tool covers production for now, but we are looking at adding a sandbox environment in the future.

##

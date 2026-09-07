---
id: 32725531885842
section_id: 32304308299922
title: "Ubble Access and Set Up Process"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/32725531885842-Ubble-Access-and-Set-Up-Process"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-01-22T11:33:12Z"
permission_group_id: 26838654181266
content_tag_ids: ["01KE6V773EPR1K1MSSMYWHJ6T4"]
label_names: ["IDV"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

You need to gain access to UbbleTo gain access to the Ubble dashboard, all users must complete the following sequence of steps:
 **Step 1: OKTA Account Activation**

- 
**Action:** Look for an activation email sent by IT; **check your Spam folder** in case you have not received it

- 
**Requirement:** Navigate to [ubble.okta.com](http://ubble.okta.com/) to create and activate your account

- 
**Outcome:** Once your OKTA account is active, notify the IT team so they can generate your specific VPN profile

**Step 2: VPN Profile Installation**

- 
**Action:** You will receive a **Ubble VPN profile** from IT

- 
**Requirement:** Install this profile on your local machine

- 
**Identification:** In your system’s VPN settings, this profile will typically be named **"VPN Main"**

**Step 3: Connection & Configuration**

- 
**Action:** Toggle the **"VPN Main"** connection to **ON**

- 
**Requirement:** You must be logged into your Ubble OKTA account to authenticate the connection

- 
**Troubleshooting**: If you experience a blank page or a connection error while trying to access the dashboard, resolve as follows:-

  - 
**CloudFlare** **VPN**: Must be turned OFF. CloudFlare interferes with the Ubble VPN connection

  - 
**Connection** **Order**: Turn off CloudFlare, enable "VPN Main”, and refresh page

  - 
**System** **Cache**: If issues persist, restart your computer and try the sequence again

**Step 4: Accessing the Dashboard**

- 
**Action:** Navigate to the provided dashboard link

- 
**Requirement:** Ensure the VPN is active before attempting to load the page

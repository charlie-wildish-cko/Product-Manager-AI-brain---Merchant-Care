---
id: 23036322839186
section_id: 23035210429458
title: "How to Remove and Add a Website URL on Dashboard"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/23036322839186-How-to-Remove-and-Add-a-Website-URL-on-Dashboard"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-01-15T10:34:56Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JE66GTJD4SN04NQ7WS3C75FR", "01JRJ3CAVQQYPNHSMAQ67Y8T27"]
label_names: ["global", "product_and_features", "website_urls", "urls", "remove_url"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article:**

To talk the merchant through how to remove an existing website URL and adding a new one via the Dashboard. 

**Problem:** A merchant needs to manage the website URLs used for accepting payments. 

**Solution:** Follow the steps in the Dashboard settings to remove an old URL or add a new URL, optionally requesting a new Processing Channel.INTRODUCTION 💬

A merchant contacts support because they need to **manage their website URLs** on the **Dashboard**. This involves either removing an old URL that is no longer in use or adding a new URL for a new website. 

When adding a new URL, they may also need to simultaneously request a new Processing Channel if the new website involves a new line of business, different processing configurations, or requires separate reporting segmentation.KEY TAKEAWAYS 🔑

- Website URLs can be viewed and managed in the **Settings > Website URLs** section of the Dashboard.

- Merchants receive **email confirmation** when a URL is removed, detailing the URL, the user who removed it, and the associated entity.

- The **"Add new URL"** flow allows a merchant to optionally request a **Processing Channel** if needed for the new website.

- ⚠️ Merchants can't self-serve on sandbox, they will need to contact us to perform this action on the sandbox environment.

PROCESS STEPS 🖊️

 

## How to View Website URLs 👀

- Log in to [Dashboard](https://dashboard.checkout.com)

- Click on Settings (gear icon on the top right)

- Click on "Website URLs" to see the list of URLs payments are accepted from

- Use the "Select entity" dropdown box to see URLs for specific entities, if applicable

 

## How to Add a New Website URL➕

- Click the "Add new URL" button

- The "Add new website URL" screen appears

- The system will ask: "Do you need to request a processing channel for this new website URL?"

  - If the answer is "No": The merchant can continue to add the URL and related details without requesting a new Processing Channel

- If the answer is "Yes": The merchant will be redirected to the "[Request new processing channel](https://checkoutint.zendesk.com/hc/en-us/articles/27849577800466-Request-a-Processing-Channel-on-Dashboard)" page

⚠️ "Yes" should only be answered if the new URL is for a new line of business (new Merchant Category Code/MCC), requires different processing configurations, or needs segmentation on reports!

- The request will include [adding the new URL as part of the Processing Channel request](https://checkoutint.zendesk.com/hc/en-us/articles/27849577800466-Request-a-Processing-Channel-on-Dashboard) process

## How to Remove a Website URL ❌

- Locate the URL you want to remove in the "Website URLs" list

- Hover over the URL and click on "Remove" - a "Remove website URL" pop-up box will appear

- Confirm the removal: Slide the pill button to confirm the action, acknowledging that this change is permanent and will stop payment processing through this URL

- Click "Remove URL"

- The merchant will receive an on-screen confirmation and should click "OK"

- The URL is now removed. It may take a few seconds to update, so the merchant might need to refresh their browser
ESCALATION ⏫

**Situations Requiring Escalation:**

- A merchant is having trouble with URLs being displayed or cannot see a specific URL

- A merchant claims they followed the removal steps, but the URL is still active/visible after refreshing the browser and waiting.

**Required Information to Include:**

Reach out to [#ask-merchant-change-requests-product](https://checkout.enterprise.slack.com/archives/C06AXSFML79) on Slack with the merchant details for support

- Merchant Name/ID and Entity (if applicable)

- The specific URL(s) involved

- Screenshot of the error or the URL still visible on the Dashboard (if applicable)

**Instructions for the agent working the case:** Stay on the case and monitor for updates. Notify the merchant of the escalation and provide regular updates.RELATED 🔗

[Request a processing channel on Dashboard](https://checkoutint.zendesk.com/hc/en-us/articles/27849577800466-Request-a-Processing-Channel-on-Dashboard)

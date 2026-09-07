---
id: 21991146415762
section_id: 21991159537682
title: "Troubleshooting Settlement Delays"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991146415762-Troubleshooting-Settlement-Delays"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-24T09:38:25Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHQKPVKA7XAZRYSRWE7JRH4"]
label_names: ["row", "merchants_asking_when_their_settlement_is_due_ie_tplus1_tplus2_etc", "case_settlements", "case_settlements_issue_i_need_a_custom_settlement_report"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

A merchant is asking when their settlement is due, follow these steps to investigate the issue.INTRODUCTION TO SETTLEMENT DELAYS 💬

A settlement might be delayed due to several reasons:

- **No settlement generated**

- 
**Payout Schedule and Threshold:** The payout schedule and any set thresholds in the Client Admin Tool (CAT) can cause delays. If a threshold has been set and the merchant hasn't reached it, the settlement will be delayed.

- 
**Risk Arrears:** Risk arrears can also delay a settlement. You can check for these in the "Risk settings and arrears" section within the merchant's account in CAT.

- 
**Negative Balance:** A negative account balance can prevent a settlement from being paid out. This can be checked by following the steps outlined in the "Not receiving settlement due to negative balance on the account" section.

- 
**Technical Issue:** If none of the above reasons are found, the delay might be due to a technical issue, which should be escalated to the Payments team.

PROCESS FOR TROUBLESHOOTING A SETTLEMENT DELAY 🖊️

### Step 1: Check for Generated Settlements

First, check the merchant's account in the dashboard to see if a settlement has been generated.

- Log in to the dashboard for the merchant's account

- From the left-hand navigation, click Business Account

- Select Settlements from the dropdown menu

  - This view shows all generated settlements

  - If no settlement is listed, proceed to the next step

### Step 2: Check the Payout Schedule and Threshold

If a settlement has not been generated, check the Client Admin Tool (CAT) to review the payout schedule and threshold.

- In CAT, go to the left-hand menu and click Payout schedules

- Select the relevant payout schedule on the right side of the screen

- Review the Payout schedule details section, a delay can be caused if a threshold amount has been set and the merchant has not yet reached it

⚠️Note that US merchants typically have a T+1 settlement schedule, while merchants in other regions are usually on a T+2 schedule

- If there is no threshold and the settlement is set to Daily, proceed to the next step

### Step 3: Check for Risk Arrears

Risk arrears can also cause a settlement delay

- In **CAT**, navigate to the merchant's account

- Go to **Entity** > **Pricing Profile** > **Payment**

- Scroll to the bottom to find the **Risk settings and arrears** section

  - If arrears are present, you can use this information to determine when the settlement is expected

  - If you need help understanding the dates and arrears, escalate the issue to **FTS L2**

 

### Step 4: Check for a Negative Balance

If there are no arrears, no threshold, and the settlement is set to daily, a negative account balance may be the cause.

- Follow the steps in the "Not receiving settlement due to negative balance on the account" section to check the merchant's balance

- If the balance is negative, the settlement has been delayed for this reason

- If the balance is not negative, proceed to the next step

ESCALATIONS ⬆️

If you have completed the above checks and there is no clear reason for the delay, a technical issue may be the cause.

- Escalate the issue to the Payments team as a delayed settlement

- Create a side conversation in Zendesk from the merchant's ticket using the relevant regional "Treasury Payments" macro

If you need help understanding the dates and arrears, escalate the issue to **FTS L2**

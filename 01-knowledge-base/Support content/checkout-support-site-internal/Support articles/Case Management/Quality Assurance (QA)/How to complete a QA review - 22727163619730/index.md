---
id: 22727163619730
section_id: 26818618723090
title: "How to complete a QA review"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22727163619730-How-to-complete-a-QA-review"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-04-15T12:58:39Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JD20DMF26KJ6Z843TS23Y5EH"]
label_names: ["global", "case_quality_assurance", "case_qa_issue_complete_a_qa_review", "case_quality_assurance_issue_complete_a_qa_review", "case_qa"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when: **

Conducting quality assurance (QA) reviews on support tickets

## PROCESS STEPS 🖊️

### **Step 1. Access the QA Ticket Pool**

- In Zendesk, navigate to **Views**

- Select the **QC Ticket Pool** view to find all tickets eligible for QA review

### **Step 2. Select and Open the Ticket 🎟️**

- Choose the ticket you wish to review

- The ticket will automatically open in the **QA initial review form**

### **Step 3. Identify the Core Issue 🔎**

Before filling out the scorecard, identify the primary reason for the merchant's contact.

- **Ticket ID:** Ensure the correct Ticket ID is linked.

- **Functions:** Select the high-level category (e.g., Transactions).

- **Functions Issue:** Narrow down the specific problem (e.g., Payment Confirmation, Refund Failed, or Authorization Failed).

### **Step 4. Verify and Assign ➡️**

- Confirm the **Requester** field displays the name of the teammate who handled the ticket

- In the **Assignee** field, click **Take It** to self-assign the QA review

- (Optional) To add a follower for the review, use the **Followers** field

### **Step 5. Evaluate Agent Actions 👀**

- Open the original ticket in a separate browser tab for review

- Assess how the interaction was handled by the agent

- Use the [scoring guidance](https://checkoutint.zendesk.com/hc/en-us/articles/33477052585362-QA-Scoring-Guidance) to evaluate these sections:

  - 
**Resolution:** core resolution, managing expectations, future prevention

  - 
**Process Adherence & Case Handling:** Case handling, documentation & SOPs, troubleshooting

  - 
**Merchant Experience:** Language, relationship building, interaction flow

  - 
**Compliance:** Regulatory, legal, policy

    - A fail in this section is critical and the whole scorecard will fail

    - An After Action Review AAR will be triggered for feedback to the agent

- Select the outcome of each category (e.g., Pass or Major/Minor Fail)

| **Use the macro:** QC > Pass with Feedback to explain areas for improvement |
| --- |

**Addressing Failed Reviews ⚠️**

If the overall result is a **Fail**, select the reason from the **Fail Reason** box:

- Knowledge gap

- Process issue

- System error

- Agent behaviour

- Compliance

  - If the fail is due to the Compliance section, this will be auto-populated.

If there are multiple reasons for the fail, select **Other**, specify details in the **Internal note** box, and click **Submit as Open** to update the QA form

| **Use the macro:** QC > Fail with Feedback to explain what went wrong |
| --- |

### **Step 6. Submit  ✅**

Once all dropdowns are completed:

- 
**If the score is a Pass:** Leave comments in the **Internal note** section and submit the ticket as **Solved**.

  - The teammate will receive an email notification about their QA results.

- 
**If the score is a Fail:** Click **Pending Appeal** to send the completed QA review to the teammate.

  - The teammate will receive an email notification and can then follow the guidance in the "Review your QA Results/Submit an Appeal" section to either accept or appeal their results.

### **Correcting a Score 💡**

- Go back to the relevant **Ticket stage**

- Change the specific score

- Tick the **Re-score** box to update the scores

- Click **Submit as Open** to resubmit the updated score

### **Notes for Team Leaders ⬆️**

Team Leaders can manually trigger a QA for a specific ticket that hasn't been automatically flagged. To do this, run the **Create manual QA ticket** macro on a solved ticket. This will generate a QA case for the required ticket.

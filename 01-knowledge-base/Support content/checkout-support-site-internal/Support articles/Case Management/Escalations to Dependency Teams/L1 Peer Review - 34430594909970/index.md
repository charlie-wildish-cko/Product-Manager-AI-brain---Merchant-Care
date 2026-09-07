---
id: 34430594909970
section_id: 22899415045906
title: "L1 Peer Review"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/34430594909970-L1-Peer-Review"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-03-30T16:12:00Z"
permission_group_id: 11003577394706
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

## 1. Purpose

The L1 Peer Review process enables L1 Merchant Care agents to formally request support from any other L1 agent on a live ticket when they require a second opinion or guidance. The process captures the time and effort that reviewers invest in mentoring colleagues, effort that would otherwise go unrecognised and surfaces data that helps Team Leads identify training gaps and missing SOPs.

**Important framing note:** This is an optional, supportive tool. It must only be used when a peer has already agreed to help (via Slack or in person). It is not a mechanism for offloading ticket ownership or bypassing self-sufficiency.

## 2. Scope

**In scope:**

- L1 agent requesting a peer review from another L1 agent on a Zendesk ticket

- L1 agent acting as a Peer Reviewer, providing guidance and recording their response

**Out of scope:**

- L1-to-L2 escalation (see L2 Escalation SOP)

- L2 Peer Review (separate approval flow: L2_Peer_Review

- Slack-only advisory conversations that do not require a formal record on the ticket

## 3. Roles & Responsibilities

| Role | Responsibility in This Process |
| --- | --- |
| **L1 Agent (Requester)** | Identifies need for peer support; confirms reviewer availability; initiates the peer review via Zendesk macro; provides any additional information requested by the reviewer; resumes the ticket once the review is complete |
| **L1 Peer Reviewer** | Receives review notification; opens the approval request in Zendesk; reviews the ticket in full; provides guidance via an internal note or the approval comment section; selects an approval response option |
| **Team Lead / Manager** | Accesses peer review views and data to identify coaching needs, training gaps, and missing SOPs; does not actively manage individual review requests |

 

## 4. Prerequisites

Before initiating a peer review, the following must be in place:

- The agent has an open Zendesk ticket they need support on

- The agent has already confirmed the intended reviewer's availability directly (via Slack or in person), **the macro must not be submitted to an unavailable reviewer**

- The agent has a clear, specific query or area of uncertainty to share with the reviewer

## 5. Trigger

**This process is triggered when:** An L1 agent requires peer guidance on a live ticket and the intended reviewer has confirmed they are available to assist.

## 6. Process Steps

### Step 1: Flag the Ticket for Peer Review

**Actor:** L1 Agent (requester)   
**Tool:** Zendesk   
**Action:**

1. Open the relevant Zendesk ticket.

2. In the ticket form, tick the **"Peer Review Required?"** field.

3. From the **"Peer Reviewer"** dropdown, select the name of the L1 agent who has agreed to help.

**Output:** Ticket form updated with the peer review fields populated.
 

### Step 2: Submit the Peer Review Request Macro

**Actor:** L1 Agent (requester)   
**Tool:** Zendesk macro: **L1 Peer Review Request**   
**Action:**

1. Select the **"L1 Peer Review Request"** macro from the macro menu.

2. Edit the macro text to include the specific query or issue requiring review, be clear and concise.

3. Submit the ticket.

**Output:** The approval flow is automatically triggered. The following automated actions occur:

- Ticket status changes to **"Awaiting Approval"** (under the on-hold status category, SLA continues to run)

- An internal note is added to the ticket: _"L1 Peer Review Approval Flow Started"_

- A **Sweethawk** notification appears in the Zendesk UI for the selected reviewer

- A **Sweethawk email** is sent to the selected reviewer

- The ticket appears in the **L1:: Open Peer Approval Requests** view

### Step 3: Reviewer Opens and Reviews the Ticket

**Actor:** L1 Peer Reviewer   
**Tool:** Zendesk (Sweethawk approval app)   
**Action:**

1. Receive the Sweethawk notification (ZD UI) or email alert.

2. Click **"Open approval request"** in the notification or email, **do not click the approval buttons directly from the email** (doing so limits you to two options and prevents you from adding notes).

3. Read the full ticket, all conversation history, internal notes, and the requesting agent's query.

4. 
Add your guidance via either:

  - An **internal note** on the ticket, or

  - The **approver comment section** within the Sweethawk approval app (recommended)

**Output:** Reviewer has read the ticket and drafted their guidance notes.

### Step 4: Reviewer Selects a Response Option

**Actor:** L1 Peer Reviewer   
**Tool:** Zendesk Sweethawk approval app   
**Action:** Select one of the three available response options (see Section 7 Decision Points for full detail on each outcome).

| Option | When to Use |
| --- | --- |
| **Review Done** | You have completed the review and provided your guidance |
| **Unable to Assist** | You are not able to help with this specific query |
| **More Info Required** | You need further information from the requesting agent before you can assist |

**Output:** Approval flow updated; automated ticket actions triggered based on the selected option (see Section 7).
 

### Step 5: Requesting Agent Reviews Outcome and Continues Work

**Actor:** L1 Agent (requester)   
**Tool:** Zendesk   
**Action:**

1. Read the internal note added to the ticket by the automated flow, which includes the reviewer's decision and any comments.

2. Apply the guidance provided and continue working on the ticket.

3. If the outcome is **Unable to Assist**, restart the review with a different peer reviewer (see Section 8).

4. If the outcome is **More Info Required**, add the requested information via an internal note and click **"Restart"** to resume the approval flow.

**Output:** Ticket returned to Open; agent continues resolving the merchant query.

## 7. Decision Points

| Decision Point | Option Selected | Automated Outcome |
| --- | --- | --- |
| Reviewer completes review and provides guidance | **Review Done** | Ticket → Open; internal note added with reviewer decision and comment; ticket appears in **L1:: Approved Peer Approval Requests** view |
| Reviewer cannot help | **Unable to Assist** | Ticket → Open; internal note added with reviewer decision and comment; ticket appears in **L1:: Denied Peer Approval Requests** view |
| Reviewer needs more context from the agent | **More Info Required** | Ticket → Open; internal note added with reviewer decision and comment; ticket removed from **L1:: Open Peer Approval Requests** view; agent must provide additional info and click **Restart** |
| Reviewer does not respond within 1 hour | _(Timeout no action taken)_ | Ticket → Open; internal note added informing agent that the review has timed out; agent must re-request if still required |

 

 
 

## 8. Exception Handling

| Exception | How It Is Handled | Owner |
| --- | --- | --- |
| **Reviewer does not respond (timeout)** | After 1 hour, Zendesk automatically returns the ticket to Open and adds an internal note. The requesting agent should re-confirm reviewer availability and re-submit the macro if the review is still needed. | L1 Agent (requester) |
| **Reviewer selects "Unable to Assist"** | Agent deletes the denied peer review request using the **Delete** option in the Sweethawk app. Agent then updates the "Peer Reviewer" field to a different agent, re-applies the **"L1 Peer Review Request"** macro, and submits. A new review is started with the new reviewer. | L1 Agent (requester) |
| **Agent approves via email buttons (not in ZD)** | Approving directly from the email only presents two of the three response options and does not allow the reviewer to add notes. The reviewer should always open the full approval request in Zendesk. | L1 Peer Reviewer |
| **Review submitted to an unavailable reviewer** | The review will time out after 1 hour. To avoid this, agents must confirm availability before submitting. If this occurs, the agent should wait for the timeout, then restart with an available reviewer. | L1 Agent (requester) |

 

 
 

## 9. End State

**This process is complete when:**

- The reviewer has selected a response option (Review Done, Unable to Assist, or More Info Required and restarted), **and**

- The ticket has returned to **Open** status, **and**

- The reviewer's decision and any comments are recorded as an internal note on the ticket

## 10. SLAs & Timelines

| Stage | Target Time | Notes |
| --- | --- | --- |
| Reviewer responds to review request | Within **1 hour** of receiving the Sweethawk notification | Automated timeout enforces this; SLA on the underlying ticket continues to run throughout |
| Agent restarts review after "Unable to Assist" or timeout | As soon as reasonably possible | Agent should confirm new reviewer availability before resubmitting |

 

 
 

**Note:** The SLA on the merchant-facing ticket does **not** pause during the peer review. Ticket status moves to "Awaiting Approval" under the on-hold category, meaning SLA continues to accrue. Both the requesting agent and reviewer should be mindful of the ticket's SLA position.

## 11. Related Documents

 
 

 

| Document | Location |
| --- | --- |
| L2 Peer Review SOP | Zendesk Help Centre |
| Zendesk Config Jira Ticket ZA-685 | [ZA-685](https://checkout.atlassian.net/browse/ZA-685) |
| L1 Peer Review Request macro | [Zendesk Macro](https://checkout13601724135305.zendesk.com/agent/admin/macros/33621130842386) |
| Demo video (Ana Cachapa Cuomo) | [Google Drive recording](https://drive.google.com/file/d/1HN7DS5wCw3yHG3LkTjguMGE7Xk4z8bH3/view) |

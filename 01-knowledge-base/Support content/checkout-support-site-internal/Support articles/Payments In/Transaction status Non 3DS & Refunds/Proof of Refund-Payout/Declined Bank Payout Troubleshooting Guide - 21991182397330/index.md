---
id: 21991182397330
section_id: 21991136181650
title: "Declined Bank Payout Troubleshooting Guide"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991182397330-Declined-Bank-Payout-Troubleshooting-Guide"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-31T16:51:58Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "ROW", "refund_proof_for_bank_payout", "case_transactions_issue_refund_proof_schemes", "Thunes", "LHV", "Refund_proof_for_bank_payout"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To investigate, diagnose, and resolve **declined bank payouts.**

**Problem:** A requested bank payout has failed or been declined by the system or a third-party partner. **Solution:** Use the Payouts Search Tool to determine the rejection reason and follow the partner-specific process for investigation and resolution.DESCRIBE THE ISSUE 💬

Agents or merchants report that a requested **bank payout** has been **declined** and they require the reason for the failure, along with guidance on how to resolve the issue.KEY TAKEAWAYS 🔑

- 
**Start with the Payouts Search Tool** to identify the initial rejection reason using the Payout ID provided by the merchant.

- 
**Internal Rejection:** Notify the merchant if the reason is internal (e.g., **Insufficient balance**) and escalate internally for funding.

- 
**External Rejection:** Contact the relevant payout partner (**Thunes** or **LHV**) for more details if the rejection is external (e.g., third party, compliance).

- 
**Compliance:** If the rejection is **Sanctions Screening**, contact the **FinCrime** team via Slack for case review and merchant communication.

- 
**Partner Investigation:** When contacting a partner, always provide the **Payout ID**, **Third-party Transaction ID**, **Transaction amount**, and **Transaction date**.

PROCESS FOR DECLINED BANK PAYOUT RESOLUTION 🖊️

### Step 1. Identify Rejection Reason using Payouts Search Tool

Use the Payouts Search Tool to perform the initial diagnosis.

- 
**Access the ******[Payouts search tool](https://retoolprod.mgmt.ckotech.co/apps/62fcaf16-f4c4-11ed-a804-2bcf189b4b36/payouts/payout-search)

- 
**Enter the Payout ID** provided by the merchant

- 
**Identify the rejection reason** in the results

### Step 2. Act Based on Rejection Type

The action required depends on the rejection reason identified in Step 1.

### ❌ Internal Rejection Reasons

| Rejection Reason | Action to Take |
| --- | --- |
| **Rejected - Insufficient balance** | This is due to an insufficient balance with the Payout Partner. **Contact **[Anubha Singh](mailto:anubha.singh@checkout.com), [Konstantinos Bourlos-Mastropavlos](mailto:Konstantinos.Bourlos-Mastropavlos@checkout.com), and [Wanjia Zhang](mailto:wanjia.zhang@checkout.com)  to coordinate the account funding. The merchant should be notified once funded. |
| **Sanctions Screening** | **Contact the FinCrime team** on Slack at **#ask-fincrime**. There may be an RFI sent to the merchant. If not, the merchant should be informed that the payout was declined due to Sanctions Screening. |
| **Other Internal Rejection** (e.g., insufficient funds where a specific process is not defined) | Notify the merchant of the reason and consult internal documentation or a Senior Analyst. |

### ❌ External (Third-Party) Rejection Reasons

For third-party rejections, you must contact the relevant partner (Thunes or LHV) for more details.

| Common Third-Party Rejection Reason | Partner Action |
| --- | --- |
| **Declined - Invalid Beneficiary/ Beneficiary details** | Verify the beneficiary's name and account details and ask the merchant to submit a corrected request. No partner contact is immediately needed unless verification is complex. |
| **Declined - Declined** (Generic, no specific error) | **Contact Thunes** for investigation. |
| **Declined - Payer currently unavailable** | This is a temporary technical issue. **Retry the payout**. |
| **Declined - Compliance Reasons** | **Contact Thunes** to provide more details on the compliance trigger. |

### Step 3. Contact the Payout Partner (Thunes or LHV)

This step is for **in-depth problem-solving** needed for external rejection reasons. Before contacting, you must gather the necessary information.

**Gather Required Information** (All available in the Payouts Search Tool):

- **Payout_ID**

- 
**Third-party Transaction ID** (Found in Confirmed/Rejected events under 'third-party transaction ID').

- **Transaction amount**

- **Transaction date**

Follow the Partner-Specific Process Below.**⚡️ Thunes Process**

**Check Status in Thunes Portal** 

- Log in to  [LastPass](https://lastpass.com/vault/?nk=1)

- Locate the **Thunes folder **(if you can’t find this folder reach out to a Senior Analyst)

- Open the Settings of the Thunes folder to find the email, password and MFA secret key

- Log in to the Thunes Portal using the email and password to trigger an OTP request

- Open Google Authenticator on your phone, click the + button and “Enter a setup key”

- On the “Enter code details” screen, input the following:-

  - Code name: Thunes LastPass

  - Your key: input the MFA secret key

  - Type of key: select “Time-based”

- Click Add, and use the 6-digit code generated in Authenticator to complete the OTP Request

- Click View Transactions Status on the left vertical tab

- Paste the **CKO Payment ID** (labeled "External") and filter the date

- Analyze the status against the [Thunes Response Code Documentation](https://thunes.zendesk.com/hc/en-us/articles/17592314477469-PAY-What-do-the-different-transaction-status-mean)

**Email Thunes Support:**

- Email support@thunes.com

- Include all **Required Information** 

  - Payout_ID in Pay_xxxxxxxxxxxx format

  - Thunes transaction ID ( details on how to identify this below)

  - Transaction amount

  - Transaction date

Thunes will return an acknowledgment with a unique case ID

Based on the information provided by the sender, the Thunes team will conduct an investigation and share the outcome under the Thunes Service Level Agreement (SLA)

## ⬆️ Thunes Escalation

- The Thunes SLA for resolving/closing requests is 8 days (192 hours)

- In case there is no response to the request for 48 hours, then the [escalation matrix](https://checkout.atlassian.net/wiki/spaces/BP/pages/6965493978/Thunes+Escalation+Matrix?atlOrigin=eyJpIjoiNTk0MjU0NDJlMzk3NGZmNDliNjBhYThmMmY5MTg3ZmMiLCJwIjoiYyJ9) should be followed, first contacting the Account Manager

## ⚡️ LHV Process

- 
**Check LHV-Specific Error Codes:** Refer to the [LHV-specific error codes documentation](https://docs.lhv.com/home/connect/services/payments/response#error-codes) for initial analysis.

- 
**Email LHV Support:**

  - Email oliver.daly@lhv.com and fi-support@lhv.com

  - Include all **Required Information:**

    - Payout_ID

    - Message Request ID (Third Party Transaction ID)

    - Transaction amount

    - Transaction date

LHV will return an acknowledgment with a unique case ID

Based on the information provided by the sender, the LHV team will conduct an investigation and share the outcome following the LHV Service Level Agreement (SLA)⬆️ LHV Escalation

- In case there is no response to the request for 48 hours, then the [escalation matrix](https://checkout.atlassian.net/wiki/spaces/BP/pages/6965526768/Escalation+Matrix) should be followed, first contacting the Account Manager
RESOLUTION ⚒️

The expected result is a clear diagnosis of the payout decline reason and an actionable path forward for the merchant.

### Remediation Steps

- 
**Incorrect Beneficiary/Bank Details:** Instruct the merchant to **correct the beneficiary information** and submit a new payout request.

- 
**Insufficient Balance:** Confirm with the merchant that the internal **account funding issue has been resolved** and a new payout request can be submitted.

- 
**Partner Investigation Complete:** Communicate the final reason from the partner to the merchant and advise on the next steps (e.g., retry, wait for partner fix, resubmit with different details).

ESCALATION ⏫

Escalate when the standard process does not yield a resolution or when partner response times are exceeded.

- 
**No Partner Response:** If there is **no response to a query after 48 hours** from Thunes or LHV, escalate the issue using the escalation matrix-  beginning with the Account Manager.

- 
**Critical Funds Issue:** Escalate immediately if the rejection involves an **Insufficient balance** that poses a critical risk to merchant service and the internal funding team is unresponsive.

- 
**Unclear/Conflicting Partner Information:** Escalate if the partner's response is vague, doesn't align with expectations, or requires a deeper technical review.

RESOURCES ⭐️

| Tools |
| --- |
| -  **Payouts Search Tool:** [Retool](https://retoolprod.mgmt.ckotech.co/apps/62fcaf16-f4c4-11ed-a804-2bcf189b4b36/payouts/payout-search) app used to investigate payout status and rejection reason.  - Tool access will need to be granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274):-  - Environment: **Production**   - Team: **Payouts**   - Access: Viewer (standard for Prod)  - Application: **payout-search** |

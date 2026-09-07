---
id: 30274208065170
section_id: 32518352084626
title: "How to Export Vault Instruments"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/30274208065170-How-to-Export-Vault-Instruments"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-02-04T10:43:20Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K7PKCVJMPKRTHGM2PKGC36KK"]
label_names: ["Vault", "tokens"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To export cardholder data securely using the Vault Exporter. It covers the necessary pre-export checks, the export process itself and post-export validation, ensuring a smooth and secure data migration.

**Problem:** A merchant needs to migrate cardholder data to a new payment service provider (PSP).

**Solution:** Use the Vault Exporter tool to securely export the requested cardholder data in an encrypted file.

## INTRODUCTION 💬

A merchant requires the secure export of their cardholder data, which is stored in the Vault system. This process is necessary for migrating their data to another payment service provider. Merchants may export card data to:

- Stop using Checkout for payments

- Add another PSP alongside Checkout

- 
To migrate data to another Checkout account:

  - To consolidate multiple Checkout accounts into one

  - The destination PSP is Checkout itself

  - This is sometimes referred to as “NAS to NAS migration”

Incoming tickets from customers will typically refer to “Token Migration”, “migration to another provider”  or “export to a third party”. 

Tokens on Checkout.com securely replace sensitive payment data, like a customer's primary account number (PAN), with unique digital identifiers. This tokenization protects card details by using non-sensitive tokens, reducing fraud risk and helping merchants comply with Payment Card Industry Data Security Standard (PCI DSS) standards.

⚠️ A single export must not exceed 5 million instruments. For larger merchants, split instrument IDs into smaller batches and export separately.

 

## KEY TAKEAWAYS 🔑

- 
**Approval is mandatory** before proceeding with any export.

- Only **card** instruments can be exported

  - 
**Note:** Google Pay/Apple Pay are included since they use DPAN, which stores a token linked to a card

- A single export must not exceed **5 million instruments** and must always be **PGP-encrypted** for security

- The merchant must provide an **Attestation of Compliance (AOC)** for the destination PSP

- All exports are delivered as **PGP-encrypted** files to ensure security, with the merchant never having direct access to the card data during migration.

 

## RESOURCES 📍

| Tools | Related |
| --- | --- |
| -  **Retool app**: [Exporter](https://retoolprod.mgmt.ckotech.co/app/vault-exporter)   - Access request [here](https://checkoutsupport.freshservice.com/support/catalog/items/722)    - [FileZilla](https://filezilla-project.org/)  -  [Database Table](https://datahub.zta.ckotech.co/dataset/urn:li:dataset:(urn:li:dataPlatform:snowflake,source.vault_network_tokens.instrument,PROD)/)   - Access provided by Vault team | **External Articles**   - [Network Tokens](https://www.checkout.com/docs/payments/store-and-manage-credentials/store-credentials/network-tokens)  - [What is a Network Token](https://www.checkout.com/blog/network-tokens-explained)  - [Payment Tokenisation Guide](https://www.checkout.com/blog/payment-tokenization)  **Confluence Article**  - [Export Vault Instruments Runbook](https://checkout.atlassian.net/wiki/spaces/CLSE/pages/7021592600/Runbook+Export+Vault+Instruments#Required%3A-Export-Destination) |

PROCESS FOR CARDHOLDER DATA EXPORT 🖊️

## Step 1. Prepare and Verify the Request

⚠️ **IMPORTANT:** Make sure you have all the necessary approvals before starting. For more details, check out the "Required Approvals section in this article.

- 
**Approved Ticket:** Ensure the "Cardholder and Sensitive Data Request" ticket is fully approved.

- 
**Vault Account ID:** Locate the merchant's Vault account ID.

- 
**Instrument IDs:** Confirm a list of specific instrument IDs or an agreement for a full export (not exceeding 5 million instruments).

- 
**Public PGP Key:** Verify that the public PGP key from the destination PSP is attached. This is mandatory for encryption.

- **Public SSH key:** Provided by the client or third-party PSP to grant them SFTP access (Checkout hosts the SFTP in the majority of cases)

- 
**Export Destination:** The ticket must specify the exact location for the final upload, such as an SFTP or a third-party service.

## Step 2. Export and Download the Data

Use the Vault Exporter application to initiate the export.

- Access the ****[Vault Exporter app](https://retoolprod.mgmt.ckotech.co/app/vault-exporter).

- Click **Create Export** on the right side of the screen.

- Fill in the required fields using the information from the support ticket.

  - Description is optional, but helpful if exporting in multiple parts

- 
Click **Create** to start the export- you will be redirected to the export page

⚠️ Ensure the “Items” count matches the expected number of instruments. The exporter removes duplicate IDs, so this number may be lower than in the original file.

- You can click on the progress bar to refresh the status without reloading the entire page.

- Once the export is complete, navigate to the **Downloads** section and click **Create**.

- Provide the PGP public key from the ticket. Use the “Paste mode” switch if the key is in the description or attached as a file.

- You’ll be redirected to the download page. Preparation time varies from seconds to minutes depending on export size. 

- Click **Refresh** to update the status without reloading the entire page.

💡 As a final check, verify that the **Recipient(s)** field matches the expected PSP and doesn’t include anything suspicious, like the merchant’s email. This also confirms you chose the right public key.

- Once the download transitions to COMPLETED, you’ll see the following on the **Files** tab:

 

## Step 3. Check for Retrieval Errors

Check the Retrieval errors file before uploading; this is a crucial quality control step.
**✅ 0 items:** The export was successful - you can proceed.
**⚠️ 404 Errors: **Not Found 

- A few are normal and indicate deleted instruments.

- Optionally, note the number of missing instruments in the ticket to alert the merchant that the total will be less than expected.

- Many 404 errors often mean wrong Vault or instrument IDs. Verify your files and raise this in the ticket if you suspect incorrect data from the requestor.

**❌ 500 (Internal Server) Errors:** This is a critical issue. **Do not proceed**

- 
**I**mmediately report this to the **#ask-vault** Slack channel, as this typically indicates a bug in Vault or an incident.

- After the issue is resolved, create another export to retrieve all the instruments again.

## Step 4. Upload the Encrypted Data

Once files are downloaded, the final step is **delivery** to the recipient, which should be determined **before** the export begins. The delivery method (e.g SFTP, Google Drive) should have been established in the export request ticket, along with access requirements.

### Delivery Methods and Access

There are three common delivery methods:
**Option 1. Checkout-hosted SFTP endpoint:** Recipient-accessible

- For this method, ask the **IT Platform team to upload the file** to `token-migration.sftp.checkout.com` for the user specified in the ticket. Details about the SFTP directory may be found in a linked FreshService ticket.

**Option 2. External SFTP endpoint:** Checkout has credentials
**Option 3. Third-party service:** E.g., Google Drive
For methods 2 and 3, you will often **not have direct upload access**. You'll need to contact the **IT Platform team** via the `#ask-platform` Slack channel or by emailing `itrequests@checkout.com`, linking the export ticket.

### Sending Files to IT Platform

The person who requested the export should ideally have contacted the IT Platform team already. You can typically send the file to the requester by **attaching it to the ticket**, and they will forward it to IT Platform.

- 
**Large Files:** If the file size exceeds attachment limits, upload it to an internal SFTP directory and ask the IT Platform team for their preferred method.

**💡 Always upload any error files** in addition to the successful files, as recipients may need to investigate unmigrated tokens using the provided IDs.

## RESOLUTION ⚒️

- Following these steps will result in a successful and secure export of cardholder data. The merchant will receive the PGP-encrypted file and the retrieval errors file, confirming the data migration.

- 
**Remediation Steps:** If 404 errors are numerous, communicate with the merchant to verify the list of instrument IDs. If 500 errors occur, follow the escalation steps immediately.

- 
**Check:** The final encrypted data file and the retrieval errors file are successfully uploaded to the correct destination.

APPROVAL FLOW  🖊️
**Peer Review**
Vault exports will now require a peer review within Zendesk itself. Before solving a ticket, utilise the "Apps" section in the right hand toolbar of the ticket and find "Approve", select Vault and you will then see a list of users who can approve this ticket. 
Once the approval has been submitted, this ticket will appear in the "Open Vault Approval Requests" queue on Zendesk. Any vault skilled user in L2 can then access this ticket, review and approve the case. 
 

 **INFO: **For a full demo - please watch this video tutorial: 
 

 
**JSM Flow**

| **Stage** | **Approver / Role** | **Description / Action Required** |
| --- | --- | --- |
| 1️⃣ | **L2 Agent** | Initiates request and documents initial checks |
| 2️⃣ | **L2 Manager** | Reviews and verifies details from L2 Agent |
| 3️⃣ | **Regional Manager** | Confirms regional compliance and justification:   MENA - Remo Giovanni Abbondandolo   APAC - @Brian Sze   US - @Jim Cho   EU - @Remko Best   UK - @Maxime Colas |
| 4️⃣ | **Legal & Data Privacy (Dual Approval)** | Both Legal and Data Privacy approvers must approve |
| 5️⃣ | **Chief Architect** | Validates technical feasibility and architecture impact |
| 6️⃣ | **Information Security** | Final security and risk assessment |
| ✅ | **Approved for Export** | All approvals complete — workflow ends |

 

## ESCALATION** ⏫**

Escalate the issue to the **#ask-vault** if you encounter a **500 (Internal Server) error** during the export process.

- 
**Required Information:**

  - 
**Case ID** and a detailed description of the issue

  - The **Vault Account ID** and export details

  - A screenshot of the error if possible

- 
**Agent Instructions:** Stay on the case and monitor for updates. Keep the merchant informed of the status and expected resolution time.

 
FAQs⁉️
 

What are "instruments" and "tokens"?Checkout's internal term for a stored card in our Vault service, while "token" is a term commonly used by merchants to refer to these unique digital identifiers that replace sensitive card details.Why can't merchants access the full card data themselves?Full card numbers are highly sensitive, and merchants must not have direct access to them to maintain compliance with PCI DSS and reduce the risk of fraud.Why Can't Merchants Export Their Own Card Data?Merchants **must not** have direct access to **sensitive card data**, particularly full card numbers (Primary Account Numbers or **PANs**), due to security requirements.
To ensure a **secure and compliant migration**, we must handle the data export ourselves. This process typically involves a standardized, secure flow:

1. We use **asymmetric PGP encryption** on the data. This ensures that **only the destination Payment Service Provider (PSP)** can decrypt the information.

2. The encrypted data is transferred **directly** to the destination PSP.

This key principle remains consistent across providers: **the merchant never handles or accesses the card data** during the entire migration process. 
What is an "Instrument"?

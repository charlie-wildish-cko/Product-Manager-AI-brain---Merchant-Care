---
id: 22346705531154
section_id: 22286660216722
title: "Secure File Transfer Protocol (SFTP) Folder Access"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22346705531154-Secure-File-Transfer-Protocol-SFTP-Folder-Access"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-31T16:47:50Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTFS8D8APRZBB2MBC3AJM8Y1"]
label_names: ["global", "reports_sftp_folder", "case_access_issue_sftp_folder", "case_access"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To provide the merchant with an SFTP server, port, username and grant access to their private key.

## INTRODUCTION TO SFTP 💬

Merchants often need secure access to their **NAS (Network Access Server)** reports. This process outlines how to create a dedicated Secure File Transfer Protocol (SFTP) account for a merchant to facilitate the secure transfer of these files.

**What is SFTP?**

- SFTP is a secure way to transfer files over a network. It allows merchants to securely receive reports from Checkout containing information about their transactions.

- For this to work, we will need to give the merchant an SFTP server, port, username, and grant access to their private key. 

  
Merchant-facing guidance on how to set up SFTP reports can be found in ****[Checkout docs](https://www.checkout.com/docs/business-operations/retrieve-reports#Access_reports_via_SFTP)**.**

 

## PROCESS TO SETTING UP AN SFTP 🖊️

Step 1: Gather Merchant Information

The first and most critical step is to obtain the merchant's **OpenSSH RSA public key**. The merchant is responsible for generating this key pair and securely storing their corresponding private key.

**⚠️ Warning:** Do not accept or store the merchant's private key - they must maintain control over it!Step 2: Submit the SFTP Request 

- Navigate to the **SFTP Creation for the Merchant** catalog item in Jira

- Select the **NAS Reporting** option and fill out the form fields:

**Folder name**

- Use only lowercase letters and replace spaces with hyphens (-)

- Do not use special characters or include a trailing forward slash (/)

- Do not specify the S3 bucket name.

**Merchant name**

- Use only lowercase alphanumeric characters.

**SSH Public Key**

- The key must be in the **OpenSSH format** and start with `ssh-rsa`

- Provide only one key and do not include the key's comment to prevent formatting errors

- Avoid any forward or backslashes in the key comment

Step 3: Post-Submission Process & Resolution

Once you submit the request, an automated process creates the SFTP account. The ticket will then be automatically routed to the **FTS - Financial R&R (L3) queue** for final review. 

✅ At this point, the SFTP account is created and the merchant should be able to connect using their private key.

---
id: 34976848753554
section_id: 34976600416658
title: "Platforms: Sub-Entity Onboarding"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/34976848753554-Platforms-Sub-Entity-Onboarding"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-04-21T10:22:31Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

This article explains the end-to-end process for onboarding a sub-entity, including the compliance checks Checkout.com runs, what information is required, what documents may be requested, verification timelines by region, and what happens if verification fails.

⚠️ **High ticket risk: Verification failures and timelines are the most common sources of support queries for this product. Read this article carefully.**

## **What is sub-entity onboarding?**

Before a sub-entity can accept payments or receive money, they must be verified by Checkout.com. This process is called onboarding. The platform submits information about their sub-entity via the Platforms Application Programming Interface (API). Checkout.com then runs a series of checks.

Until a sub-entity passes verification, they cannot process payments or receive payouts.

## **The 7-step onboarding process**

The onboarding flow works as follows:

1. 
**Configure the webhook server.** The platform sets up a webhook server and subscribes to the relevant events. Webhooks notify the platform of status changes throughout the process. See Article 3 for detail.

2. 
**Collect verification information.** The platform gathers the required details from the sub-entity. The information needed depends on whether the sub-entity is a company or a sole trader, and the region they operate in.

3. 
**Submit the application via the Platforms API.** The platform calls the Onboard Entity endpoint to submit the sub-entity's details. See the technical docs for the full API reference: https://api-reference.checkout.com/#operation/onboardEntity

4. 
**Add supporting documents.** Checkout.com may request additional documents (such as proof of identity or bank statements). The platform uploads these via the API.

5. 
**Add a payment instrument.** The platform adds a bank account or card (the payment instrument) for the sub-entity. This step triggers the verification checks.

6. 
**Checkout.com runs verification checks.** These run asynchronously — meaning Checkout.com processes them in the background. The platform tracks progress via the Dashboard or API, and receives webhook notifications.

7. 
**Check the outcome.** If verification passes, the sub-entity's payment and payout capabilities are enabled. If it fails, the platform may be asked to provide additional information.

## **What compliance checks does Checkout.com run?**

Checkout.com runs the following checks on every sub-entity during onboarding:

- 
**Card Scheme Screening (CSS):** checks the sub-entity against Visa and Mastercard screening databases (VMSS and MATCH).

- 
**Anti-Money Laundering (AML) checks:** a broad set of financial crime checks.

- 
**Know Your Customer (KYC): **verifies the identity of individual representatives.

- 
**Know Your Business (KYB): **verifies the business details of company sub-entities.

- 
**Politically Exposed Persons (PEPs) screening: **checks whether any representatives hold or have held prominent public roles.

- 
**Sanctions screening:** checks whether the sub-entity or its representatives appear on any sanctions lists.

Payment capabilities are enabled once the CSS checks pass. Full payout capabilities are enabled once all checks pass.

## **What information is required from the sub-entity?**

The information required depends on the sub-entity type:

- 
**Sole trader:** Name, address, contact details, and financial information about the individual.

- 
**Company:** Business name, business type, registered address, and details of the company's representatives (directors or beneficial owners).

The platform can submit a minimum set of information and save it as a draft. However, Checkout.com only starts verification once all required information is present. If information is missing, the sub-entity's status shows as requirements_due.

For the full list of required fields, direct the customer to the API reference: https://api-reference.checkout.com/#operation/onboardEntity

## **Supporting document requirements**

Checkout.com may request additional documents as part of verification. Documents must meet quality standards or they will be rejected.

### **Document quality standards (all regions)**

- Must not be a photo of a photo (for example, a screenshot of a document on a computer screen).

- Must be clear and large enough to read — blurry images are not accepted.

- Must be in colour — no black-and-white scans for identity documents.

- Must be complete — all four corners must be visible.

- Must be valid, not expired (for identity documents).

- Must be authentic, not altered or forged.

### **Document types by region**

**🇺🇸 United States:**

| **Document type** | **Accepted examples** |
| --- | --- |
| Identity document (if requested) | Passport, US government photo ID, valid US driving licence with photo |
| Company document (if requested) | Certificate of Incorporation (CoI), Employer Identification Number (EIN) letter, Memorandum or Articles of Association (MoA/AoA), ownership structure |
| Bank account document (if requested) | Bank statement |
| Proof of address (if requested) | Bank statement, insurance policy, lease or mortgage, property tax receipt, utility bill (gas, electric, water, or fixed-line telephone), valid US driving licence |

**🇬🇧 United Kingdom:**

| **Document type** | **Accepted examples** |
| --- | --- |
| Identity document | Full UK driving licence (both sides), national identity card (both sides), passport, UK biometric residence permit (both sides) |
| Company document | CoI (must be less than 3 months old), latest certified MoA or AoA, ownership structure |
| Bank account document | Bank statement |
| Proof of address (if requested) | Utility bill, bank statement, social security, local authority tax bill, HMRC tax document — all from the past 3 months (tax documents must be from current tax year) |

**🇪🇺 Europe:**

| **Document type** | **Accepted examples** |
| --- | --- |
| Proof of identity | European driving licence (both sides), European electoral ID (both sides), national identity card (both sides), European residence permit (both sides), passport |
| Company document | CoI (less than 3 months old), latest certified MoA or AoA, ownership structure certified by a notary, lawyer, or qualified accountant and dated within 3 months |
| Financial document | Balance sheet, income statement, statement of cash flow, statement of retained earnings — latest available version |
| Bank account document | Bank statement |
| Proof of address (if requested) | Bank statement, local authority tax bill, social security, tax documents, utility bill — all from past 3 months (tax documents must be from current tax year) |

## **Verification timelines — US vs. other regions**

**This is a frequent support query. Customers often expect instant onboarding outside the US. Set expectations clearly.**

| **Region** | **Timeline** | **What happens** |
| --- | --- | --- |
| United States | Potentially instant | Checkout.com can verify sub-entities automatically with minimal information. If automatic verification isn't possible, Checkout.com requests additional information and retries. Customers should receive an outcome quickly, but this is not guaranteed. |
| Outside the United States | Longer — no fixed timeframe | Verification may take significantly longer. Checkout.com does not publish a standard SLA for non-US regions. If a customer has concerns, they should contact their account manager or submit a support request. |

If a customer outside the US asks how long verification will take, do not give a specific estimate. Direct them to their account manager or raise a support request on their behalf.

## **What happens if verification fails?**

If verification fails, the sub-entity's status changes to requirements_due or rejected. Checkout.com sends webhooks to notify the platform.

### **Requirements due — the platform can resolve this**

This status means Checkout.com needs more information before verification can continue. The platform can check what is needed by calling the Get Entity Details endpoint. The response includes a requirements_due object listing each affected field and the reason it was flagged.

Common reasons and what to do:

| **Reason code** | **What it means** | **Action required** |
| --- | --- | --- |
| required | A document is missing and is needed to start checks | Provide the document and resubmit |
| document_expired | The identity document submitted has expired | Upload a new, valid document |
| document_mismatch_submitted_address | The representative's address doesn't match the document | Correct the address and resubmit |
| document_mismatch_submitted_date_of_birth | Date of birth doesn't match the document | Correct the date of birth and resubmit |
| document_mismatch_submitted_individual_name | First or last name doesn't match | Correct the name and resubmit |
| document_submitted_mismatch_ssn | Social Security Number (SSN) doesn't match | Correct the SSN and resubmit |
| document_type_invalid | The document type uploaded is not on the accepted list | Upload a document from the accepted list for that region |
| document_unreadable | The document cannot be read (blurry, cropped, etc.) | Upload a clear, complete, colour image |
| document_unverifiable | Document cannot be verified — this cannot be self-served | Escalate to Checkout.com support |
| invalid_company_document | CoI or AoA/MoA does not match the company details submitted | Upload a valid, matching company document |
| invalid_company_name | Legal name doesn't match the company document | Correct the name to match the document |
| ownership_data_missing | Ultimate Beneficial Owners (UBOs) are not included | Submit details of all registered UBOs |
| unidentified_details | Individual details (address, date of birth) couldn't be verified | Upload an identity document for the individual |
| verification_failed | Company details couldn't be verified against provider databases | Upload a new Certificate of Incorporation (CoI) |

**Important: document_unverifiable cannot be resolved by the platform themselves. Raise a support ticket immediately. Include the sub-entity ID, the error code, and a description of what has been tried.**

To fix a requirements_due status, the platform must update the sub-entity's record via the Update Sub-Entity endpoint. Checkout.com will then re-run verification automatically.

### **Rejected — no further action possible via API**

If a sub-entity is rejected, their status is permanent. They cannot process payments or receive payouts. The platform cannot update the sub-entity or retry via the API — any attempt returns a 442 error.

To challenge a rejection decision, the platform must raise a support request via the Checkout.com Dashboard. Direct the customer to: https://dashboard.checkout.com/support/new

## **Troubleshooting / common questions**

**Q: A customer says their sub-entity is stuck in 'Pending' — nothing is happening.**

Pending means verification is running. It's not stuck — it's in progress. For US platforms, this should resolve quickly. For non-US platforms, it may take longer. If it has been more than a few business days with no update, escalate to the account manager.

**Q: The customer submitted all documents but verification still hasn't started.**

Verification only starts once a payment instrument has been added (Step 5). Confirm the platform has completed this step. If they have, check the sub-entity's status for a requirements_due entry.

**Q: The platform updated the sub-entity's information but nothing has changed.**

After an update, Checkout.com re-runs verification automatically. The status should move to Pending. If it hasn't, check whether all required fields have been completed and whether the update was submitted correctly.

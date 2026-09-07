---
id: 21991182445074
section_id: 21991136181650
title: "Refund proof for Mastercard"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991182445074-Refund-proof-for-Mastercard"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:34:42Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "ROW", "refund_proof_for_mastercard", "case_transactions_issue_refund_proof_schemes"]
user_segment_ids: [11003606966930]
archive: false
---

## Process Steps

1. Go to the MC portal and download the proof of refund

2. Before login, we need to identify the region of the transaction being investigated. We can easily do so by using the ARN - the second to the sixth digit in the ARN is the BIN, for example, ARN 82700924130770265535016- 270092 is the BIN. You can then cross-check the region [here](https://checkout.atlassian.net/wiki/spaces/MC/pages/5639770935/CKO+MC+BIN+Details+Multi-Region)

3. After identifying the region, login to your LastPass - under the shared customer support folder the login details for different regions will be there

4. Go to the URL [https://www.mastercardconnect.com/-/sign-in#/public/signin](https://www.mastercardconnect.com/-/sign-in#/public/signin)

5. As user ID input the username found on LastPass

6. Now you need to open the RSAToken Application (To import all the Token, kindly open the Zip file found on MC Connect Token)

 

1. Select the correct token as per the region 

2. Enter the four-digit PIN which is in the notes section on LastPass for the selected region

3. Click on sign-in

4. Select transaction investigator

5. Paste your ARN on the field Acquirer reference number, make sure you select the correct date as per the Dashboard, then click on Search

6. In the clearing section click on view to obtain the full details - then you can click on export and select the option PDF

7. Download the proof of refund by following the [confluence](https://checkout.atlassian.net/wiki/spaces/CHEC/pages/4751851637/MasterCard+-+Get+Proof+of+Transaction+Refund+from+MCconnect) page for MC: 

  1. Once downloaded, email the merchant and explain that you have checked the ARN and from our side, this has been cleared. Send them a screenshot of the clearing page and ask the merchant to advise the customer to check in with their bank

  2. If a merchant comes back saying the customer still cannot see this: explain that the evidence from the schemes is enough to show a refund has been cleared

## Glossaries and Definitions:

For **Key Terms and Definitions** on Transactions as well as an **introduction into MENA Gateway and non-Gateway merchants**, please see ****[Transactions Glossary](https://checkoutint.zendesk.com/hc/en-us/articles/21991201065106-Transactions-Glossary-Introduction)**.  **
 
 
 
 
 
 
 
 
 
For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Transactions articles, please see ****[Transactions Tools & Permissions](https://checkoutint.zendesk.com/hc/en-us/articles/21991176883474-Transactions-Tools-Permissions)**.**

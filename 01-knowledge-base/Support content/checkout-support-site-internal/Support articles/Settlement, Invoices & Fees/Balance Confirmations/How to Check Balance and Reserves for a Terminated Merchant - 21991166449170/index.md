---
id: 21991166449170
section_id: 23045903280658
title: "How to Check Balance and Reserves for a Terminated Merchant"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991166449170-How-to-Check-Balance-and-Reserves-for-a-Terminated-Merchant"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-15T16:05:27Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHQKPVKA7XAZRYSRWE7JRH4"]
label_names: ["case_settlements", "terminated_merchants_who_want_to_know_their_balance_and_reserves", "global", "case_settlements_issue_balance_confirmation", "terminated_merchants", "rolling_reserve", "terminated_merchant_balance", "fixed_reserve"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To assist terminated merchants who need to check their balance or reserve funds. The Merchant Care team can check the merchant's balance in the Dashboard and reserves in Retool.
DESCRIBE THE ISSUE 💬

A terminated merchant is unable to access their Dashboard and has contacted the Merchant Care team for assistance to check their balance and/or reserve funds. 

 
KEY TAKEAWAYS 🔑

- Terminated merchants cannot access their Dashboard to check the balance themselves

- If the merchant's account is still accessible financial reports can be generated directly from the Dashboard

- If the merchant's account is no longer on the Dashboard use the provided Looker link to generate a financial action report

PROCESS FOR CHECKING A TERMINATED MERCHANT'S BALANCE 🖊️

The process for this issue involves a combination of standard checks and in-depth problem-solving using multiple tools.
Check Merchant Balance in Dashboard

- Navigate to **Funds** and then select **Balances** in the Dashboard

- 
Look under the **Available** column to see the merchant’s current balance - including any negative balance  
 

Check Merchant Reserves in Retool

- Open the  [Currency Account Balances function in Retool](https://retoolprod.mgmt.ckotech.co/apps/6840ab28-c4b7-11ec-909b-bf9c18a51b41/techfinance-finlab/Currency%20Account%20Balances) 

- Locate the merchant’s **Currency Account ID** in CAT

- Enter the **Currency Account ID** into Retool and click **Refresh**

- The rolling and fixed reserves will be displayed

  
 
Generate Financial Reports

- If the merchant’s account is still on the Dashboard you can provide them with a report directly from there, such as:

  - [Balance Report](https://www.checkout.com/docs/funds-management/retrieve-financial-reports/balance-reports/balance-report)

  - [Balance Breakdown Report](https://www.checkout.com/docs/funds-management/retrieve-financial-reports/balance-reports/balance-breakdown-report)

  - [Financial action report](https://www.checkout.com/docs/funds-management/retrieve-financial-reports/balance-reports/financial-actions-by-date-range-report)

- If the account is no longer on the Dashboard use the following Looker link to generate a financial action report: [Financial Actions Report](https://checkoutinternal.eu.looker.com/explore/ledger_financial_actions/finance_financial_actions_report?toggle=fil&qid=mGWabX8oTtVoyLzneKk6Ok) 

FAQs ❓
What is a rolling reserve?A rolling reserve is a percentage of each transaction held by the payment processor for a set period to cover potential chargebacks or refunds. The funds are then released to the merchant on a rolling basis.What is a fixed reserve?A fixed reserve is a one-time lump sum of money held by the payment processor from a merchant's account. This is usually done to cover potential future losses and is held for an agreed-upon period.What is a financial action report?A financial action report provides a detailed breakdown of all financial transactions related to a merchant's account, including payments, refunds, chargebacks, and payouts.

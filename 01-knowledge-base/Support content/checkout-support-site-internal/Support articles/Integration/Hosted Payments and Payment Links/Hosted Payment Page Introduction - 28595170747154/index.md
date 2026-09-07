---
id: 28595170747154
section_id: 22188552840594
title: "Hosted Payment Page Introduction"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/28595170747154-Hosted-Payment-Page-Introduction"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-22T09:59:54Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K0YPEVRSXXEYB936K329TF6D"]
label_names: ["hosted_payment_pages", "HPP", "product_introduction"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To understand more about the Checkout.com hosted payment page (HPP) as part of our 'Connect' product.

INTRODUCTION TO HOSTED PAYMENT PAGE** 💬**

The Hosted Payment Page (HPP) is a secure, Checkout.com-hosted webpage that allows a merchant's customers to complete payments. Because we host the page and handle the payment data, the merchant's PCI compliance responsibility is significantly reduced. 

It is an ideal solution for merchants who want a quick and easy integration with minimal technical overhead The HPP integration and payment flow involves a simple, three-step redirect process for the merchant.

💡HPP is built on our powerful Flow solution, which handles both the collection of card details and the payment request processing.
 

## Step 1: Create a Hosted Payment Session

The merchant makes an API `POST` request to the `/hosted-payments` endpoint. This initial call includes key payment details such as:

- Amount

- Currency

- Customer details

- 
`success_url`: Where to send the customer after a successful payment

- 
`failure_url`: Where to send the customer after a failed payment

The API response will contain a `redirect_url`, which is the link to the unique HPP session.

## Step 2: Redirect the Customer

The merchant redirects their customer to the `redirect_url` received in the API response from Step 1. The customer is now on the secure Checkout.com HPP.

On this page, HPP automatically:

- 
**Shows relevant payment options:** It intelligently displays the best payment methods based on the customer's device, location and currency

- 
**Captures all necessary information:** It ensures all required details, like an IBAN for an iDEAL payment, are collected

- 
**Manages the payment flow:** It handles complex processes like 3D Secure (3DS) authentication and redirects to third-party banking apps

## Step 3: Handle the Return Redirect

Once the customer completes the payment (whether successful or failed), HPP redirects them back to the `success_url` or `failure_url` that the merchant defined in Step 1. The merchant is responsible for handling the customer experience on these pages.

 
 
**KEY TAKEAWAYS 🔑**

 

**Simplifies PCI Compliance**: HPP is hosted by Checkout.com, meaning merchants never handle sensitive payment details directly. This reduces their PCI compliance scope to the simplest level, SAQ-A.

**Easy Integration**: The process for a merchant is a straightforward, three-step redirect flow: 1) Request a payment session via API, 2) Redirect the customer to the HPP link, and 3) Handle the customer's return to their site after payment.

**Ideal for SMBs**: HPP is a great option for small and medium-sized merchants who have limited technical resources and want an easy-to-maintain payment solution.

**Dynamic and Smart**: The page automatically shows the most relevant payment methods based on the customer's location, device, and currency. It also handles complex flows like 3DS and redirects to third-party apps automatically.

**Future-Proof**: Merchants can add new payment methods without needing to write any additional code, making it easy to expand their payment offerings.

 

 

 

## FAQs** ****❓**

 
Can merchants add new payment methods to HPP without extra coding?Yes. HPP is designed to allow new payment methods to be enabled without requiring any additional integration work from the merchant. The page dynamically displays the available options. 

## RESOURCES **📍**

| Training Material |
| --- |
| [HPP Product Academy Deck](https://docs.google.com/presentation/d/1btAHUOfG8VJ8pINjOmqJUjF_d_UU72Bd1_7EvaMet14/edit?slide=id.p1#slide=id.p1) |

Jul 17, 2025

## US Platforms \- support needs

**Invited** [Michael Taylor](mailto:michael.taylor@checkout.com) [Charlie Wildish](mailto:charlie.wildish@checkout.com) [Jeff Schmidt](mailto:jeff.schmidt@checkout.com) [Brian Foley](mailto:brian.foley@checkout.com)

**Meeting records** [Transcript](?tab=t.3csbtrmsdfhg) 

### **Summary**

Charlie Wildish expressed interest in identifying problematic areas that would arise with scaling if there was no product solution in place, emphasizing the need to address root causes of support requests rather than just making it easier for platform merchants to submit them. The main talking points revolved around problematic areas for scaling support, onboarding challenges and automation, suspensions, terminations, and funds holds, platform control over terminations, Stripe Connect support issues, payment and payout visibility, data traceability and product solutions, and addressing payment failures and declined transactions.

### **Details**

* **Problematic Areas for Scaling Support** Michael Taylor identified the top issues as operational, particularly onboarding-related inquiries, followed by payment and payout frequency questions ([00:00:48](?tab=t.3csbtrmsdfhg#heading=h.9su0wgwlv1mw)).

* **Onboarding Challenges and Automation** Brian Foley highlighted structural challenges in onboarding, specifically the lack of visibility into responses provided to merchants in the dashboard and the generic nature of many responses ([00:01:40](?tab=t.3csbtrmsdfhg#heading=h.mv04gn545acq)). Michael Taylor noted that the level of automation from a product build perspective would influence these issues, suggesting that internal visibility through dashboard could alleviate the burden on the support team ([00:02:39](?tab=t.3csbtrmsdfhg#heading=h.sdyua8t05zmr)).

* **Suspensions, Terminations, and Funds Holds** Charlie Wildish brought up concerns regarding suspensions, terminations, and holds of funds for sub-entities, particularly in relation to AML checks. Michael Taylor acknowledged the sensitivity of sharing information due to regulatory limitations but stressed the importance of providing as much internal visibility as possible without entering gray areas ([00:03:30](?tab=t.3csbtrmsdfhg#heading=h.11b6qbx9hqzz)). 

* **Platform Control over Terminations** Brian Foley shared an instance where a platform wanted to terminate a shady sub-merchant but lacked the ability to do so, leading them to withhold payouts by changing banking information ([00:05:25](?tab=t.3csbtrmsdfhg#heading=h.tllmufxbqji7)). Charlie Wildish emphasized the need for a system where both the platform and Checkout can control terminations, especially when dealing with non-compliant behavior or non-payment ([00:06:36](?tab=t.3csbtrmsdfhg#heading=h.70maqjtjvwod)).

* **Stripe Connect Support Issues** Charlie Wildish inquired about the perceived poor support experience with Stripe Connect, suggesting it's a factor in attracting dissatisfied customers ([00:07:20](?tab=t.3csbtrmsdfhg#heading=h.lrc0rp84kzgj)). Brian Foley attributed Stripe's support issues primarily to a "scale problem," noting that their vast number of merchants, especially those processing small volumes, overwhelms their support capacity despite a larger employee base ([00:08:01](?tab=t.3csbtrmsdfhg#heading=h.k2a65cav89mi)). Michael Taylor added that Stripe's long tenure in the market means existing tech infrastructure might hinder quick improvements to customer service workflows, whereas their company has the advantage of building from scratch with automation in mind ([00:08:57](?tab=t.3csbtrmsdfhg#heading=h.dr0mxvz445vo)).

* **Payment and Payout Visibility** Charlie Wildish stated that the top two support queries "what happened to this payment?" and "when am I getting paid?" are identical to those experienced by Care today ([00:08:57](?tab=t.3csbtrmsdfhg#heading=h.dr0mxvz445vo)). Brian Foley explained that many payout issues stem from payments occurring after cut-off times, leading to delays that customer support teams often cannot explain due to lack of visibility ([00:11:13](?tab=t.3csbtrmsdfhg#heading=h.69ga741mlxg2)). Michael Taylor stressed the need for a system to expose detailed settlement information to platform customer support agents, ideally through Dashboard or a white-labeled API ([00:12:03](?tab=t.3csbtrmsdfhg#heading=h.hp31978cvqai)).

* **Data Traceability and Product Solutions** Charlie Wildish emphasized that the key to resolving many support issues lies in improved data traceability throughout the payment lifecycle, from successful transactions to refunds and disputes ([00:12:53](?tab=t.3csbtrmsdfhg#heading=h.i7a3riud56s1)). They noted that current systems, especially for international regions, lack the necessary visibility, making it difficult to explain payment statuses to merchants ([00:13:43](?tab=t.3csbtrmsdfhg#heading=h.ngmewvt6akup)). Michael Taylor agreed that solving payment data visibility would significantly reduce the burden on support teams ([00:19:46](?tab=t.3csbtrmsdfhg#heading=h.1i2q1z62gftj)).

* **Addressing Payment Failures and Declined Transactions** Brian Foley highlighted scenarios where payments decline after initial authorization, leaving service providers unpaid and requiring the platform to manually transfer funds. He emphasized the need for a mechanism for CS agents to transfer funds from a platform's available balance to individual sub-merchants ([00:15:58](?tab=t.3csbtrmsdfhg#heading=h.lu022x35lukc)). Brian Foley also pointed out common onboarding issues, such as mismatched names on documents and lack of granular decline reasons in the dashboard, which impede efficient support ([00:17:48](?tab=t.3csbtrmsdfhg#heading=h.ziddsqo01h8i)).

### **Suggested next steps**

- [ ] Charlie Wildish will follow up on tracing the payment and payment throughout the full lifecycle through to Settlement as key work to solve for 2025\.


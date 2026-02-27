# Fin AI Agent Pilot: Tier 1 Merchants Findings and Recommendation

**To**: COO, CPO
**From**: Charlie Wildish
**Date**: February 2026
**Topic**: Pilot results show email entrenchment at Tier 1 is structural; the right response is to bring Fin to email, not push merchants off it


## Summary

We piloted Fin AI Agent with six Tier 1 merchants in Q4 2025 to test whether they would shift from email to Dashboard chat for support. They didn't, and the reasons are structural: large ops teams, multi-PSP workflows, and centralised ticketing mean email is wired into how they operate. The recommendation is to deploy Fin on email for Premium and Enterprise merchants rather than continuing to push them toward Dashboard, while enforcing Dashboard-first for Standard merchants where the barriers don't apply.


## Background

Fin currently operates in the authenticated Dashboard chat experience. The majority of Premium and Enterprise merchant contacts arrive via email, where Fin has no presence. The 80% Fin involvement rate target for 2026 is not achievable without resolving this. The pilot was designed to test whether active AM-supported nudging could shift Tier 1 merchants to Dashboard chat, and whether Fin could meaningfully resolve their queries when they did.


## What we found

- **Email is structurally embedded, not habitual**: Large merchants run distributed ops teams of 30-50+ people using centralised ticketing tools (Zendesk, Freshdesk). Email is wired into their entire operation; changing it would require cross-PSP process changes, not just a preference shift.
- **Dashboard access is a genuine operational burden at this scale**: Managing individual Dashboard accounts and MFA for large, high-churn teams is significant overhead. Shared email inboxes are operationally simpler. This is a structural friction point, not a training problem.
- **Fin works well when it can answer the question**: Merchants who used Fin for payment queries gave strong positive feedback. *"The AI Agent has been very helpful in understanding codes"* (eToro). *"It clearly has the potential to save time by cutting down on lengthy emails"* (Plus500). Both had the simplest query types; the product experience is good where Fin's capability matches the query.
- **Channel shift was limited despite active AM support**: Email-to-Fin migration was modest (X% to Y%) even with briefing sessions and direct AM engagement. Internal comms on the merchant side are a bottleneck; ops teams don't reliably receive or act on messages from their own AMs.
- **Fin capability gaps drove fallback to email**: Missing payment data display and no access to scheme dispute outcome letters meant merchants defaulted back to email when Fin couldn't close the loop.
- **Standard merchants are a different case**: Smaller merchants (Tier 3/Bronze) have smaller teams, less operational complexity, and less dedicated Checkout support. The barriers that make enforcement impractical at Tier 1 do not apply here.


## What this means

- **Tier 1 and Enterprise merchants will not move off email without enforcement**: Enforcement at this tier carries commercial and relationship risk. Meeting them on email is the right strategy, not continued nudging toward Dashboard.
- **Fin on email is cost-neutral**: Fin's resolution cost is the same on email as on chat. There is no cost argument against email deployment.
- **Standard merchants should be enforced onto Dashboard**: Enforcement is feasible and appropriate for this tier and directly supports the 2026 Fin involvement rate target.


## Recommendation

1. **Deploy Fin on email for Premium and Enterprise merchants**: Fin handles payment queries securely over email using org-level authentication. In development; accelerate. This is the highest-impact lever for the 80% Fin involvement rate target.
2. **Enforce Dashboard / Fin chat for Standard merchants**: Remove email as an entitlement for Tier 3-5 / Bronze merchants and redirect to Fin chat. Policy change, not a technical build; can ship fast.
3. **Close the Fin capability gaps identified in the pilot**: Payment data display and scheme dispute letter access were the specific gaps that drove fallback to email. Resolving these expands resolution rate alongside involvement rate.


## Supporting data

*To be completed: Imran Khan*

| Merchant | Fin channel uplift % since pilot | Fin conversations | Fin resolution rate | Escalated issue types |
|---|---|---|---|---|
| eToro | | | | |
| Plus500 | | | | |
| Sibilla | | | | |
| Wise | | | | |
| Bytedance | | | | |
| Vinted | | | | |
| **Overall** | | | | |

*Email vs Fin usage comparison: [chart]*


**Owner**: Charlie Wildish
**Next update**: When pilot metrics are complete (Imran Khan)
**Questions to**: Charlie Wildish

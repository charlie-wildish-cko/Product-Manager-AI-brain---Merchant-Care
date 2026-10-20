# Ray Readiness Steerco: Ops and Product

**Date:** 2026-09-24  
**Attendees:** Sarah Edmonds (chair), Brian Weir, Joel Petrosino, Max Rothman, Oliver Westlake-Simm, Bernard Ryan, Fabio Marques, Daniel Kliza, Bhinti Seedeen, Tejash Chunnoo, Chris Wade, Gilles Beausseron, Ana Muschici, Nick Taylor, Sunil Mudaliar, Irakli Gogishvili, Alice Beddis, Immanuel Smith, James Walters, Helder Goncalves, Ben Leah. Charlie Wildish absent (holiday).  
**Drive source:** 1EU2eJn7sov1XbLca2jnfD_Z9eTgWGKr3FcEi0l6D7Jk

## Context

Fortnightly Ray readiness steerco (next around 2026-10-08). Charlie was absent. Sarah read out Charlie's written update and Max spoke for Care.

## Key Points

**Phases**
- Internal testing: October. Friends and family: 1 December. External launch: Q1 2027. Gilles referenced launching "for the 500" (likely cohort size, unconfirmed).

**Policies**
- CDD, TM, screening and AML policies in final review and already feeding SOPs. Fraud and complaints (Fabio) in progress. Target: all in place for F&F on 1 Dec.

**Care and complaints**
- Fabio is redesigning the TOM to merge roles and reuse people across teams rather than add dedicated headcount.
- Charlie's update: the Zendesk replacement recommendation is nearly done and shares the following week. Max said on record it "is Plain" and "pretty much decided". Helder: "very very close", final exec discussions remain, sign-off target early October.
- Data blocker: the data team had said no customer data in 2026. Max reversed this after a call that morning. Care should get "bare bones" product data, about 50% of the roughly 10 items needed, by end of year. Not 100%. Confirmation expected through an October review.
- Care still needs to state what data the care tool can ingest and act on. Marketing has already submitted its data list.
- Knowledge and training readiness blocked until processes are clearer.

**Disputes**
- Manual issuing dispute handling is fine for internal testing and F&F, "very challenging" at GA. Disputes engineering is understaffed. Engineering director says "probably towards mid next year".
- Oliver: the original TOM assumed dispute automation to keep headcount down. Fabio says the delay is factored in.
- Priorities: automate Visa submission, then stage tracking, ahead of user-facing status. Helder added automated decisioning on when to raise.
- No provisional credit. Funds return only on a won dispute, as a standard refund via issuing webhooks (Visa returns USD). Fiat-to-stablecoin conversion still to solve (Joe Foulds).

**Fraud ops**
- Six existing issuing risk procedures reused, two new ones (authorised and unauthorised fraud). Sardine is the fraud system. Chris Wade's team builds the connections. James Walters wrote the PRD.

**AML and TM**
- Sphinx regulatory assistant: no capacity, MCP approach rejected by InfoSec. Q4 investigation into safe external tool access to Checkout data.
- Ayesha Ghoshal (new PM) maps Ray system connections and leads terminations.
- Fiat TM has no PM, analyst, engineers or system with a full transaction view. Amber. Max: risk acceptance possible for internal testing and F&F, but external launch cannot happen without fiat TM.
- Ana: ops capacity assumed a short manual phase with automation around Q1. Slippage means revising the capacity model.
- On-chain TM (TRM) proceeds separately. TRM commercials finalised, most rules set up.

**Terminations**
- No ops owner. Ayesha defines actions and triggers, manual first. ISV terminations framework is the reference.
- Crypto constraint: cannot suspend like a fiat account. Levers: suspend card, block transfers out to third-party wallets, stop funds in. Users can always export keys and take their coins.
- Two types: self-elected and Checkout-initiated. Open: contractual obligations and data access rights.

**October internal testing**
- Core money flows only (sign-up with manual approvals, funding, spending, paying Visa). Support via Slack, no care tooling.
- Agreed in principle (Fabio, Joel): Care team members join internal testing to capture queries and build SOPs and automation plans, as for Braavos.

## Insights

- Plain is visible to the Ray programme as the decided platform, with exec sign-off targeted early October. Ray Care tooling planning can assume Plain.
- Charlie's data blocker is partly resolved: about 50% of roughly 10 items by December, confirmation mid-October. Care must prioritise which items matter for customer identification.
- Max spoke for Charlie on both Plain and data. Check both statements match Charlie's position.
- Manual disputes at GA and fiat TM slippage are direct Care and ops headcount risks. The TOM depends on both timings.
- Terminations need consumer-facing policies and SOPs (card suspension, blocked transfers, key export), including Care scripting.
- Care's seat in October internal testing is the first real source of Ray query data for the taxonomy draft and SOPs. Support runs through Slack until at least F&F.
- New contacts: Ayesha Ghoshal (Ray PM for connections, TM, terminations), James Walters (Strategy & Ops, fraud PRD), Chris Wade (Sardine).

# Ray x EP

**Date:** 2026-08-21
**Attendees:** Joe Foulds (presenting), Charlie Wildish, Fraser Bryant, Guido Van Der Hart, Pao Igarteburu, Paloma Sedeau, Gilles Beausseron, Jamie Sims, Inge Mutsaers, Emily Geffen, Antonio Vasilev, Davine Ittoo, Ignas Sakalauskas, Kehinde Ladipo, Ashish Tyagi, Flavio Cadete, Kunal Patel, Alex McSweeney. ~25 attended against 3 originally planned
**Drive source:** 1wGtdXLtmgexBiVhC23KRRjDBq_kDVNX07lOHZ1pm_1M

## Context

Joe Foulds' introduction of Ray to Engineering and Product after the Braavos pivot, then open Q&A.

## Key Points

**What Ray is**
- Non-custodial crypto consumer wallet. The user deposits crypto and transacts like any consumer product. The on-chain wallet and funds belong to the user; Checkout owns the access and holds private keys. Legally Checkout does not hold funds, but users cannot move funds out without Checkout's permission. Multi-asset, spans multiple blockchains.
- Braavos contrast: Braavos was FCA-regulated, UK-only, fiat neo-bank, physical-card-focused. Ray is crypto-funded, non-FCA-regulated, digital-first, global. Pivot rationale: Braavos had heavy regulatory hurdles, slow per-country expansion, high cost, and zero margin for error.
- Initial launch markets: UAE, Philippines, Brazil.
- Approximately 80% of the product is shared with Braavos: IDV, Checkout-issued cards, spending controls, 3DS, transaction history. The ~20% net-new is blockchain wallet sanction screening, on-chain deposits, and stablecoin scheme settlement. Intent is to reuse as much Braavos data model and tooling as possible.

**Funding and settlement flow**
- Post-onboarding a blockchain wallet with delegated access is created. The user deposits (e.g. 10 USDC). Bitblocks notifies the system, incrementing an offline ledger. TRM screens the incoming payment for AML and illicit activity. Currency accounts are used under the hood, modified by the FX team.
- Settlement: card auth, merchant capture, Ray reconciles the offline ledger, Ray triggers an on-chain sweep from the user's wallet to a Ray treasury account, treasury pays Visa in stablecoin.
- Cards are USD-denominated and USDC-to-USD is a 1:1 peg. Visa handles fiat conversion for merchants. User FX mirrors standard fiat.

**Fraud and disputes**
- Braavos users could dispute fiat pay-ins with their own bank after receiving goods. Ray users cannot dispute the crypto funding transaction on-chain, and funding is just-in-time, so delegated access prevents draining funds before settlement.
- Card transaction disputes through the scheme still apply.
- TRM is new for on-chain transaction monitoring, not used for Braavos. Regulatory requirements are currently lower than FCA fiat, but the build assumes future regulation.

**Org and open questions**
- Max Rothman is the VP (commercial) running Ray. Consumer experience engineering team (Joe Foulds, Paloma) plus crypto funding engineering team and the FX team. An "Ask Ray" channel was created.
- Sole traders: users may self-certify as sole traders. Targeting freelancers lets Ray issue commercial cards with higher interchange. Still clarifying with schemes whether these users count as consumer or business.
- Planned consumer benefits: cashback and yield on stablecoin balances. Future: support volatile assets for day-to-day spend via spot-rate conversion.
- Legal entity open question: whether Ray links to a new Checkout legal entity or operates as a merchant client. Cross-entity processing needs modelling for finance and treasury.

**Timeline as stated**
- Iterative build with no hard internal-launch date. ~20 users in November, ~50-80 Checkout friends and family by end of December. Public launch "sometime in Q1", explicitly acknowledged as anywhere between 1 January and 31 March.
- Load testing targets 500k next year and 50k end of this year for consumer. No month-by-month Ray growth projections exist yet. Growth aim ~200-250k users.
- No defined user acquisition strategy. Options floated: market to Remember Me users in the UAE (a UAE issuer licence is expected within a couple of months), partner with a merchant employing crypto-paid freelancers, or partner with a crypto company.

**Decisions**
- Braavos paused indefinitely: "it's not going to be coming back suddenly in Q4".
- Reuse existing Braavos infrastructure and tooling.
- Ray launches digital-only card for the foreseeable future.
- Friends-and-family launch of ~50-80 users by end of year.

## Insights

- The 80/20 reuse claim is the central planning assumption for everything Braavos-derived, including Care tooling. Only screening, on-chain deposits and stablecoin settlement are genuinely new.
- Ray's dispute surface is narrower than Braavos: no funding-leg disputes. Scheme card disputes remain, so issuing disputes are still a Care and ops requirement.
- Two user flows matter for Care: self-funders who are crypto-literate, and payroll recipients paid via Ray by an employer who need no crypto knowledge. The second group will drive support demand.
- Sole-trader self-certification creates a B2C/B2B ambiguity that will affect taxonomy and entitlement.
- Charlie's own intervention in the session named the Care dependency directly: the Care platform is in a scoping phase and needs to launch alongside Ray, so a compressed Ray timeline compresses the platform schedule. No answer was given.

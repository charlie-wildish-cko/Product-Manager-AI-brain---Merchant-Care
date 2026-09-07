# Braavos Care — Ended (2026-08-18)

Braavos (B2C fiat neobank wallet) is ended. It was announced internally as a pause on 2026-08-18 and confirmed as ended: the product is not going ahead. A related but distinct proposition, **Ray** (consumer crypto/stablecoin wallet), is going ahead in its place — see `04-active-work/prds/ray-care/`.

Ray is not a rename of Braavos. Key differences that mean this folder's content does not carry forward as-is:

- **Custody**: Braavos was a custodial fiat neobank model. Ray is a **non-custodial** stablecoin wallet — Ray administers key management but the user legally owns the wallet and its assets. Care/Ops cannot freeze, seize, claw back, or move Ray wallet assets, and cannot retrieve, reset, or re-issue keys.
- **Regulatory scope**: Braavos assumed UK launch with Consumer Duty obligations live from day one (FCA DISP, FOS referral, vulnerable customer ID, 8-week complaint SLA). Ray is **not launching in the UK** — Consumer Duty does not apply. Ray's regulatory surface is global AML/Travel Rule and KYC (via Ubble), owned by Compliance, not the UK banking regime Braavos was built around.
- **Funding model**: Braavos was card/bank-funded. Ray is funded by on-chain stablecoin deposit (USDT, USDC) only — no chargeback-equivalent for deposits.
- **Milestones**: Ray's internal launch is end Dec 2026 (50–100 people), external beta end Q1 2027.

All files in this folder (scoping, h2-build-plan, fin-config-plan, capabilities-ownership, fin-fraud-risk-escalation, fraud/disputes Figma specs, and the earlier Phase 1/Phase 2/External Launch PRDs) are retained as historical record of the Braavos effort. Do not use them as a basis for Ray work without re-validating every regulatory and product assumption against the Ray handbook.

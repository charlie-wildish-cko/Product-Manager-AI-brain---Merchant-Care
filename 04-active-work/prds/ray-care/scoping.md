# Ray Consumer Care — Scoping Document

**Author:** Charlie Wildish
**Date:** 2026-08-18
**Status:** Draft — early scoping, not yet reviewed

This document sets out Care's scope, build responsibilities, dependencies, and open questions for Ray, Checkout.com's consumer stablecoin wallet + USD Visa card proposition. It replaces the ended Braavos effort — see `05-archive/2026/prds/braavos-care/README.md` for what changed and why prior Braavos scoping does not carry forward.

Maps to the 2026 deliverable **Consumer Support — Ray** in `2026 deliverables.md`.

---

## What Ray is

Non-custodial global stablecoin wallet (USDT, USDC at launch) plus a USD Visa card (virtual + physical, multi-card, single-use "burner" cards), rewards/cashback, an Insurance Guarantee (operational/infrastructure risk cover — explicitly not deposit insurance), and a user-driven key-export/self-custody exit path. Tiers: Standard ($0/mo, 1% cashback, 0.5% FX), Beam ($4.99/mo, 1.5% cashback, 0% FX, unlimited ATM), Solar (Phase 3, $19/mo, 2% cashback, metal card). Six launch languages: English, Spanish, Portuguese, Arabic, Vietnamese, Filipino.

**Launch markets** (per Master PRD): Phase 2 T1 = UAE, Brazil, Philippines. Phase 3 expansion: Argentina, Turkey; later Nigeria, Vietnam. Sanctioned/excluded: US, China, Russia, Iran, North Korea, Cuba, Syria, Crimea, Donetsk, Luhansk, Belarus.

**Entity structure** (updated 2026-08-22): Ray Global Ltd (BVI) is Program Manager/Merchant of Record, holds the spend-control delegation, underwrites the Insurance Guarantee. Checkout SAS (France) is Issuer of Record under Visa BIN sponsorship. Blue EMI (Lithuania) holds no MiCAR authorisation and isn't a confirmed offramp; primary offramp is now Ray's own Circle/Coinbase accounts. Non-custodial characterisation (L15) is now formally closed.

**Regulatory posture**: non-custodial, not launching in the UK — Consumer Duty does not apply. Regulatory surface is global AML/Travel Rule (destination-address screening, VASP resolution, unhosted-wallet ownership proof) and KYC (via Ubble), both Compliance-owned. Care's boundary per the Ray Ops & Care manual (§0.3): Care owns "did the scan/deposit/card/payment work?"; Compliance owns "is the person or money permitted?" — screening dispositions are never surfaced to Care (silent handoff, fixed no-tipping-off macros).

**Source**: Ray Ops & Care Operating Manual ("Genesis Master Reference"), owned by Max, Oliver, Luca, Fabio, plus the Master PRD (Ray) — Global Stablecoin Wallet & USD Visa Card, Ray Wallet Model (June 2026, Final; reviewed by Care Product 2026-08-21, re-reviewed after a 2026-08-22 edit). The PRD's ownership table now names Oliver Westlake-Simm (+ Max) as owner of the Consumer Care Operating Manual, replacing the earlier generic "CS Lead."

---

## Milestones

- **Internal launch — end Dec 2026**: 50–100 people
- **External beta — end Q1 2027**

The Ops manual does not date these phases itself (it uses relative phase language: "by GA," "Public Beta," "at launch"). Confirm with Ray team whether "internal launch" = the manual's launch/Beta gate, or an earlier staff-only step, before building a phased plan.

---

## Care model (per Ops manual)

- **AI-first**: AI L1 (LLM) is the default responder across all six languages, escalating to a single L2 human queue with domain lanes (KYC, Deposit & recovery, Disputes, Account ops, Complaints, Data rights) and/or BPO overflow (identical scoped tool contract, queue-gated only).
- **Scoped tool contract** (FR-2.33): identical read/action tools for AI, human, and BPO agents. Every state-changing action requires user-side biometric reconfirmation. No tool moves funds, changes payout destination, bypasses IDV, or returns raw PII/keys.
- **Care can never**: freeze, seize, claw back, or move wallet assets; retrieve, reset, view, or re-issue keys/seed. The only key-exposure path is user-driven self-custody export (FR-1.36).
- **Misdirected-deposit recovery**: a narrow recoverable edge case (wrong-chain, where Ray's wallet stack controls destination keys) via a Care/Ops recovery queue, disclosed fee, best-effort SLA. No chargeback equivalent exists for ordinary deposits.
- **Depeg handling**: stablecoin depeg triggers auto-pause on deposits/funding-ladder use; refunds during a pause are credited 1:1 USD value in USDT, no automatic compensation.
- **KYC**: Ubble verification engine (pass/fail/step-up). Quality/liveness failures → Care/Ops manual-review lane (24h SLA). Screening hits (PEP/sanctions/adverse-media) → Compliance-only, silent handoff.
- **Kill-switch**: any one of CS Lead / Engineering on-call / Risk on-call can fire it unilaterally; reversal requires two of the same set.
- **Vendors** (updated 2026-08-22): Ping (CIAM, signed), Sardine (fraud/device intel, Checkout-paper contract extension in progress), Retool (AML monitoring, feeds Sphinx), Sphinx (compliance case management), Ubble (IDV), Fireblocks (wallet infra + on-chain analytics via TRM, Elliptic dropped). The Ray-built "IVO"/"Compliance Vault" concepts are gone — Ray now uses Checkout's own RA Tool (via Firco), operated by Checkout.
- **Disputes**: Ray never adjudicates or files — intake gathers evidence/reason code and hands off to Fabio Marques' team, who work every case with Visa. Self-service dispute submission API is a 2027 ask.
- **Insurance claims**: email intake (downgraded from a guided in-app flow).
- **PIN**: view-only at issuance; PIN change is a 2027 ask.
- **Complaints**: no conduct regime applies to Ray — no regulator hook, no per-market parameterisation; ack/resolution targets are internal standards only.
- **Ray Backoffice** (new): the enforcement hub for freeze/unfreeze, card block, deposit-hold release, manual review disposition, depeg-pause override. Doesn't exist yet — needed before Friends and Family.
- **Stand-in risk** (new): Ray's Visa BIN has a zero stand-in limit — Ray being unreachable means Visa declines every auth (full outage). No Visa-agreed downtime tolerance yet; sign-off owned by Alex McSweeney needed before scaling past Friends and Family.

**Metrics** (per manual + Master PRD): AI L1 resolution ≥60% (Phase 2/Public Beta) / ≥70% by GA; CSAT ≥4.2 (Public Beta) / ≥4.3 (GA); L2 first-response SLA 24h; complaint ack 24h / resolution 15 calendar days; cost-per-ticket (in-house vs. BPO).

---

## What's missing from the Ops manual — needs a separate source

- Contact taxonomy (case types, issue types, reasons) — the manual is operational (routing, boundaries, escalation), not a taxonomy. A first draft exists at `04-active-work/prds/ray-care/taxonomy-draft.md`, built by mapping the archived Braavos taxonomy category-by-category against this manual — not validated against real Ray query data. It surfaces one significant gap worth resolving early: no confirmed reimbursement path for a consumer socially engineered into authorising their own deposit (Braavos would have had UK PSR APP-fraud reimbursement; Ray's Insurance Guarantee explicitly isn't deposit insurance).
- Contact volume forecast — TBD, waiting on accurate numbers from the Ray team. An earlier estimate existed but predates this manual and is not accurate; not carrying it forward into any build plan.
- Launch markets are now named (UAE, Brazil, Philippines at Phase 2; Argentina, Turkey, then Nigeria, Vietnam at Phase 3), but the regulatory language for included markets is still deliberately generic/global ("one global process, not per-jurisdiction regimes"); a per-market regulator-escalation block exists but is empty pending Legal, targeted Nov 15, 2026 per the Master PRD.
- Zendesk/CRM/Fin build specifics (brand, forms, routing, Procedures) — not covered by an Ops manual; needs its own build plan once taxonomy exists. Per the 2026-08-18/19 meeting notes referenced in `ray.md`: no Zendesk, confirmed; **platform choice itself is still open** — Plain is the leading candidate, decision ETA Sept 2026. Fin is confirmed as the AI layer, content-only at launch. The 2026-08-22 PRD's "Zendesk candidate, not yet selected" is accurate as written, not stale.

## Open questions

- Who is Care's counterpart on the Ray team beyond the manual's four named owners (Max, Oliver, Luca, Fabio)?
- Does "internal launch, 50–100 people" map to the manual's Beta gate or an earlier pre-Beta step?
- Is BPO overflow contracted yet, or is that a Public Beta dependency Care needs to trigger?
- Confirm no jurisdiction among the named launch markets (UAE, Brazil, Philippines at Phase 2; Argentina, Turkey, Nigeria, Vietnam at Phase 3) imposes a Consumer-Duty-equivalent obligation.
- Master PRD's phase schedule was renamed/re-dated 2026-08-22: Phase 1 Alpha October 2026, "Friends and Family" December 2026, "Slow Release" Q1 2027, GA end Q1 2027. Closer to the milestones above than the prior draft, but not confirmed as the same gates — check with the Ray team whether Friends and Family = internal launch and Slow Release = external beta before building a phased Care plan against either set of dates.
- Does the Ray Backoffice tool (freeze/unfreeze, card block, deposit-hold release, manual review disposition, depeg-pause override) have an owner and a build timeline? It has none as of the 2026-08-22 PRD, but Care/Ops depends on all five actions.
- Has Alex McSweeney signed off a downtime tolerance for the zero stand-in limit on Ray's Visa BIN? If not, what's Care's exposure to contact-volume spikes from a full-outage-on-unreachability scenario during Friends and Family?

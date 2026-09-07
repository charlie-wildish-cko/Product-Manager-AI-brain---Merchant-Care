# Ray

> Checkout.com's non-custodial consumer stablecoin wallet and USD Visa card — a new B2C product replacing the ended Braavos neobank proposition, with a materially different regulatory and custody model.

**Source**: Ray Ops & Care Operating Manual ("Genesis Master Reference"), owned by Max, Oliver, Luca, Fabio, plus the Master PRD (Ray) — Global Stablecoin Wallet & USD Visa Card, Ray Wallet Model (formerly "Embedded Wallet Model") (Max Rothman, GM Ray; June 2026, Final; reviewed by Care Product 2026-08-21, re-reviewed after a 2026-08-22 edit). The Consumer Care Operating Manual is owned by Oliver Westlake-Simm + Max per the PRD's latest ownership table. Milestones below are Charlie's confirmed dates, not the PRD's own phase schedule — see Known gaps. Anything not stated in either source is marked TBD below rather than inferred.

## Why it matters

Ray is Checkout.com's first live B2C consumer product needing a dedicated Care model, and the first one built on genuinely crypto-native mechanics rather than a fiat-banking analogue. Braavos (ended 2026-08-18) would have inherited most of its Care model from UK neobank precedent — Consumer Duty, FCA DISP, FOS referral rights. Ray inherits none of that: it's non-custodial, not UK-launched, and its regulatory surface is global AML/Travel Rule and KYC instead. That means Care can't reuse Braavos's taxonomy, macros, or complaint process wholesale — see `04-active-work/prds/ray-care/taxonomy-draft.md` for what carries over and what doesn't.

It also introduces a support boundary Care hasn't operated under before: Care owns "did the scan/deposit/card/payment work?"; Compliance owns "is the person or money permitted?" — and Care is structurally excluded from ever seeing AML/sanctions/PEP screening dispositions (silent handoff only, fixed no-tipping-off macros). Getting that boundary right in tooling and agent training is a prerequisite for launch, not a refinement.

Maps to the 2026 deliverable **Consumer Support — Ray** (`2026 deliverables.md`). Flywheel domain: Input + Orchestration — establishing the AI-first entry point and correct Care/Compliance routing for a net-new B2C segment.

## What it is

A global, non-custodial stablecoin wallet plus a USD Visa card. The user legally owns the Embedded Wallet and its assets; Ray administers it (key management, gas abstraction) but never custodies funds. Funded exclusively by on-chain stablecoin deposit (USDT, USDC at launch) — no card or bank top-up, and no chargeback-equivalent once a deposit is confirmed.

Product surface: the Embedded Wallet; the USD Visa card (virtual and physical, multi-card, single-use "burner" cards); a rewards/cashback programme; an "Insurance Guarantee" covering Ray's own operational/infrastructure risk (explicitly **not** deposit insurance); and a user-driven key-export/self-custody exit path — the only circumstance under which keys are ever exposed. Three tiers: Standard ($0/mo, 1% cashback, 0.5% blended FX, 3 free ATM withdrawals/mo), Beam ($4.99/mo, 1.5% cashback, 0% FX, unlimited ATM fair-use, physical card included), Solar (Phase 3, $19/mo, 2% cashback, metal card, full perk stack). Referral programme: $10/$10 after $100 of referee net settled spend, plus 1% of referee spend for 12 months (Phase 2). Founders Card cohort: first 100K users get boosted rewards and distinct card art. Six launch languages: English, Spanish, Portuguese, Arabic, Vietnamese, Filipino.

**Launch markets**: Phase 2 T1 = UAE, Brazil, Philippines. Phase 3 expansion: Argentina, Turkey; later Nigeria, Vietnam. Excluded at launch (sanctioned): US, China, Russia, Iran, North Korea, Cuba, Syria, Crimea, Donetsk, Luhansk, Belarus — screened against OFAC SDN/Sectoral, EU Consolidated, UN, UK OFSI, Swiss SECO, MAS lists. US re-evaluation targeted Q4 2026.

**Non-custodial.** Not launching in the UK — Consumer Duty does not apply. The regulatory surface instead is global AML/Travel Rule (destination-address screening, VASP resolution for external sends to hosted wallets, unhosted-wallet ownership proof) and KYC (via Ubble) — both Compliance-owned, not Care.

**Entity structure** (per Master PRD, updated 2026-08-22): Ray Global Ltd (BVI) is Program Manager and Merchant of Record — holds the spend-control delegation (programmatic authority to pull funds for card settlement, disclosed programme fees, negative-balance cure) and underwrites the Insurance Guarantee. Checkout SAS (France) is Issuer of Record under Visa BIN sponsorship, structured out of the funds flow. **Blue EMI (Lithuania) holds no MiCAR authorisation and has not applied for one** — it's no longer a confirmed fallback offramp. Primary offramp is now Ray's own Circle and Coinbase accounts. Non-custodial legal characterisation (L15) is now formally closed — "confirmed, non-custodial," signed off with a legal opinion.

## Users

- **Ray wallet holder** (see Jordan persona, `customer-personas.md`) — funds the wallet via stablecoin deposit, spends via the Visa card, may need KYC re-verification, deposit recovery, disputes, or complaint handling.
- **Care/Ops L2 agents** — single human queue with domain lanes: KYC, Deposit & recovery, Disputes, Account ops, Complaints, Data rights.
- **BPO overflow agents** — identical scoped tool contract to AI and human agents, queue-gated only.
- **Compliance** — owns AML/Travel Rule/sanctions/PEP/EDD/SAR-STR decisions end-to-end; interacts with Care only via silent handoff.
- **CS Lead / Engineering on-call / Risk on-call / MLRO / CISO** — named escalation and kill-switch authorities (any one can fire the kill-switch unilaterally; reversal requires two of the same set).

## Components / Capabilities

| Component | Description |
|---|---|
| **Ray Wallet** (renamed from "Embedded Wallet" in the 2026-08-22 PRD update) | Non-custodial stablecoin wallet; user legally owns the wallet and its assets. Ray handles key management and gas abstraction but cannot freeze, seize, claw back, or move assets. Legal characterisation (L15) is now closed — confirmed non-custodial. |
| **USD Visa Card** | Virtual + physical, multi-card, single-use "burner" cards. Standard card-network dispute mechanics apply (Visa scheme rules). |
| **Rewards/cashback** | Confirmed to exist; mechanics not detailed in the manual. |
| **Insurance Guarantee** | Covers Ray-side operational/infrastructure risk only — explicitly not deposit insurance. High-priority, legally-reviewed FAQ macro. |
| **Self-custody export** | User-driven key export — the only path by which keys are ever exposed (FR-1.36). Care cannot retrieve, reset, view, or re-issue keys under any other circumstance. |
| **Tiers (Standard / Beam / Solar)** | Differ on ATM allowance, physical card inclusion, FX margin. Solar's 24/7 live human chat, previously "under evaluation," is now explicitly **not planned** — Care is deliberately AI-first with an async second line and BPO as the release valve. |
| **AI L1** | Fin (Checkout's Care AI product), not a bespoke Ray-built agent — confirmed both by the 2026-08-19 Ray/Care meeting and the 2026-08-22 PRD update (FR-2.33). Default responder across all 6 launch languages. |
| **L2 human queue** | 6 lanes: KYC, Deposit & recovery, Disputes, Account ops, Complaints, Data rights. Human queue platform: **not yet decided** — no Zendesk, but Plain vs. alternatives is still open, decision ETA Sept 2026. The 2026-08-22 PRD's "Zendesk candidate, not yet selected" is actually accurate on this point, not stale. |
| **BPO overflow** | Identical scoped tool contract to AI/human agents; queue-gated only. |
| **Scoped tool contract (FR-2.33)** | Identical read/action tools across AI, human, and BPO agents. Every state-changing action requires user-side biometric reconfirmation. No tool moves funds, changes payout destination, bypasses IDV, or returns raw PII/keys. |
| **Disputes (FR-2.30)** | Reframed 2026-08-22 from self-service to manual handover: Ray never adjudicates or files — intake gathers evidence and picks a reason code, then hands the case to Fabio Marques' team, who work every case with Visa directly. A self-service dispute submission API is a 2027 ask (owner David Guardiola). |
| **Insurance claims (FR-2.29)** | Downgraded 2026-08-22 from a guided in-app flow to email intake. |
| **PIN (FR-2.43)** | Downgraded 2026-08-22 to view-only, set at issuance. PIN change is a 2027 ask, deprioritised each quarterly planning round. |
| **Complaints (FR-2.45)** | No conduct regime applies to Ray, so there's no regulator hook and no per-market parameterisation — ack/resolution targets (24h / 15 days) are internal standards, not regulatory obligations. |
| **Misdirected-deposit recovery** | Narrow recoverable edge case (wrong-chain, where Ray's wallet stack controls destination keys) via a Care/Ops recovery queue — disclosed fee, best-effort SLA. Not available for deposits sent correctly to third parties. |
| **Depeg handling** | Stablecoin depeg triggers auto-pause on deposits/funding-ladder use; refunds during a pause are credited 1:1 USD value in USDT, no automatic compensation. |
| **Kill-switch** | Any one of CS Lead / Engineering on-call / Risk on-call can fire it unilaterally; reversal requires two of the same set. |
| **Ray Backoffice** (new, 2026-08-22) | The enforcement hub for freeze/unfreeze, card block, deposit-hold release, manual review disposition, and depeg-pause override. **Does not exist yet** — no system currently performs any of these actions. Needed before Friends and Family. |

**Vendors** (updated 2026-08-22): Ping (CIAM, signed), Sardine (device intelligence/fraud, contract extension on Checkout's paper in progress — no longer just "leading candidate"), Retool (AML monitoring, feeds Sphinx), Sphinx (compliance case management), Ubble (IDV — pass/fail/step-up verdict, sole vendor, no second-vendor failover at launch), Fireblocks (wallet infrastructure; TRM on-chain analytics/sanctions screening now routed via Fireblocks, Elliptic dropped as an alternative), Notabene/Sumsub/Veriscope (Travel Rule counterparty-VASP discovery, under evaluation), Circle/Tether/Paxos (stablecoin issuers; also Ray's primary offramp via Circle/Coinbase accounts; balance-visibility arrangement funds the rewards programme), Thales (physical card manufacture), MoonPay/Transak (fiat on-ramp wrapper, Phase 2). The Ray-built "Compliance Vault" and "IVO" concepts from the earlier PRD draft are gone — replaced by direct use of Checkout's own RA Tool (via its Firco connection), operated by Checkout.

## Known gaps (not addressed in the manual — do not assume an answer)

- **Fraud reimbursement**: no confirmed mechanism if a user is socially engineered into authorising their own deposit (no chargeback-equivalent; Insurance Guarantee isn't deposit insurance). Braavos, as a UK product, would have carried the PSR's mandatory APP-fraud reimbursement scheme — Ray doesn't inherit that. Needs a Legal/Ray-team answer before external beta.
- **Contact volume and headcount**: TBD. An earlier estimate existed but predates this manual and is not accurate — not carrying it forward.
- **Which jurisdiction's AML/Travel Rule instrument formally applies to each launch market**: sanctioned/excluded jurisdictions are now named (see Launch markets above), but for included markets the manual's language is deliberately global/generic ("one global process, not per-jurisdiction regimes"); a per-market regulator-escalation block exists but is empty pending Legal, targeted to resolve Nov 15, 2026 per the Master PRD.
- **PRD phase schedule vs. confirmed milestones**: the 2026-08-22 PRD update renamed and re-dated its phases — Phase 1 Alpha October 2026, Phase 2 split into "Friends and Family" (December 2026) and "Slow Release" (Q1 2027), GA end Q1 2027. This is closer to the milestones below (internal launch end Dec 2026, external beta end Q1 2027) than the prior PRD draft was, but the two still aren't confirmed as the same gates — treat "Friends and Family ≈ internal launch" and "Slow Release ≈ external beta" as a hypothesis, not a confirmed mapping, until checked with the Ray team. Note the PRD's own §16.4 sequencing narrative wasn't updated to match its new dates, so the document is internally inconsistent on this point too.
- **Stand-in processing risk (new, 2026-08-22)**: Ray's Visa BIN has a zero stand-in limit — if Ray's systems are unreachable, Visa declines every card authorisation (a full outage, not a degradation). No Visa-agreed downtime tolerance exists yet; sign-off owned by Alex McSweeney is required before scaling beyond Friends and Family. Directly relevant to Care: this is a plausible driver of contact-volume spikes with no mitigation in place yet.
- **Vulnerability/wellbeing protocol beyond a generic handoff macro**: not detailed. Silence in the manual isn't a decision either way.

## Care platform and AI decisions (2026-08-18 / 2026-08-20)

Source: `04-active-work/meeting-notes/2026-08/2026-08-18-ray-blockchain-consumer-care.md`, `2026-08-19-max-fin-agent-consumer.md`, `2026-08-20-ray-taxonomy-review.md`.

- **No Zendesk for Ray**, to avoid building on a stack Care migrates off. **Plain is the leading candidate, not yet decided** — platform decision ETA Sept 2026. If Plain is not ready for the December alpha, a lightweight sub-one-day setup covers friends and family.
- **December alpha ships without Fin**: web form only, volume too low to justify per-outcome Fin cost. Fin added post-launch once there is data.
- **Fin is confirmed as the consumer AI layer.** Consumer volume is already inside the renewed Intercom contract (originally scoped for Braavos), so no commercial change. Separate consumer workspace, never blended with merchant.
- **At launch Fin does content only, no data Procedures.** Procedures are expensive to build and the investment targets are unknown pre-launch.
- **Ray falls outside SCA**, so vulnerability and duty-of-care scope shrinks materially versus the Braavos assumption. Charlie marked those taxonomy rows TBC rather than deleting them. Cards are issued via Checkout SAS, not the UK entity (Nick Taylor's call), deliberately avoiding UK Consumer Duty scrutiny.
- **Product scope overlap with Braavos: 60-70%.** Card-side flows (lost/stolen card, verification failure, lockout, unrecognised transaction) are reusable. On-chain "where's my money" is the genuinely new work.
- **Non-custodial is a deflection lever**: users can be pointed at on-chain data. The offset is near-zero troubleshooting visibility, with no SOPs, Looker queries or APIs for these flows yet.
- **Account lockout will not use email as a fallback contact route** (no way to authenticate over email). Model is full account suspension plus an automated liveness check against the historic liveness capture on a new device, comparable to Monzo's web rescue form.

## Success Metrics

Per the Ops manual — not yet reconciled with Care Product's own north star metrics (contact rate, cost per contact):

| Metric | Target |
|---|---|
| AI L1 resolution rate | ≥60% (Phase 2/Public Beta) / ≥70% by GA |
| CSAT | ≥4.2 (Public Beta) / ≥4.3 (GA) |
| L2 first-response SLA | 24h |
| Complaint acknowledgement / resolution | 24h / 15 calendar days |
| Cost-per-ticket | In-house vs. BPO, not yet quantified |

**Conflict flagged (2026-08-20):** Charlie's own forecast is **50% AI resolution at Ray launch**, not the >=60% in the table above. He pushed back on a ~70% figure quoted on an earlier call: that cannot be hit before a live product and tuning, and the closed beta exists to find what to fix. The 100-of-230-issues self-serve count in Max's draft taxonomy is not a usable resolution forecast until it is volume-weighted at category level.

Business KPIs from the Master PRD, for context (not Care-owned): 200K registered users, $250M gross card volume (TPV), $100M wallet-estate balances by GA/EOY1; KYC pass rate ≥85% combined; fraud loss <15bps of TPV by GA.

## 2026 Roadmap

**Milestones**: internal launch end Dec 2026 (50–100 people) · external beta end Q1 2027. Full deliverable detail: `2026 deliverables.md` → Consumer Support — Ray.

## Related

- `04-active-work/prds/ray-care/scoping.md` — Care scoping doc: build responsibilities, dependencies, open questions
- `04-active-work/prds/ray-care/taxonomy-draft.md` — draft Care issue taxonomy, mapped against the archived Braavos taxonomy
- `01-knowledge-base/products/customer-segments.md` — Ray's place in the B2C segment model
- `01-knowledge-base/products/customer-personas.md` — Jordan, Ray wallet holder persona
- `05-archive/2026/prds/braavos-care/README.md` — what changed when Braavos ended and Ray took its place

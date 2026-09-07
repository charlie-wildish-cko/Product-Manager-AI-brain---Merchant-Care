# Ray B2C Care Issue Taxonomy — Draft

**Status**: First draft, not validated against real Ray query data. Built by mapping the archived Braavos taxonomy (`05-archive/2026/processes/braavos-consumer-app-care-taxonomy.md`) category-by-category against the Ray Ops & Care Operating Manual, keeping what's genuinely common and reworking what isn't. Also incorporates a second source — external research on AI-agent support patterns for mobile non-custodial crypto wallets (native resolution pipelines, deep-link actions, biometric signing sheets) — used in the "AI Resolution & Self-Service" section and category 4 below. **Do not treat as final** — it hasn't been reviewed by the Ray team, Compliance, or Legal.

**Scope caveat on the second source**: that research assumes a general-purpose DeFi-capable wallet (token swaps, cross-chain bridges, arbitrary ERC-20 token support, dApp browser/WalletConnect sessions). Ray's confirmed scope per its own Ops manual is narrower — a stablecoin wallet (USDT/USDC) + USD Visa card, not a full DeFi wallet. Only the patterns that map to Ray's actual confirmed feature set are applied below; swap/bridge/dApp-specific query types are flagged as out-of-scope-unless-confirmed rather than assumed.

**Third source**: a broader Web3 wallet ecosystem market research synthesis (architectures, customer segmentation, competitive landscape — see `customer-segments.md`'s Ray subsection for the full context). Used below only where it explains *why* a Ray mechanic behaves the way it does (categories 2, 4, and 11) — not as a source of new query types, since it covers the general market rather than Ray specifically.

**Phases**: Internal launch (end Dec 2026, 50–100 people, real funds) · External beta (end Q1 2027). Unlike Braavos's three-gate phasing (Ph1/Ph2/External), Ray only has two confirmed milestones, so phase-gating below is my judgment call (same logic Braavos used: core wallet/security functions needed from Internal since real funds are involved from day one; long-tail/lower-frequency items deferred to External) — not sourced from the manual, which doesn't phase-gate at all.

**Status tags**: 🟢 Common (same need as Braavos, basis updated) · 🟡 Modified (category exists, mechanics differ materially) · 🔵 New (crypto-native, no Braavos equivalent) · ⚪ Removed (Braavos/UK-banking-specific, no Ray equivalent confirmed) · ❓ Open question (not addressed in the Ops manual — needs Compliance/Legal/product input before this can be finalized)

---

## Suggested volume weighting (hypothesis — no Ray contact data exists yet)

**No real Ray volume data exists** (see the removed-figures note in `customer-segments.md` and `scoping.md`). The ranking below is a product-judgment hypothesis for prioritizing build/staffing order — drawn from general fintech/crypto-wallet support patterns and what the handbook itself emphasizes, not from any Ray-specific measurement. Treat it as a starting hypothesis to test against real data once External beta generates it, not as a forecast to plan headcount against.

**Caveat**: the "weight" below is *inbound query* volume, not *human-handled contact* volume. Categories 2, 3, 4, 8, and 11 all have meaningful in-app self-service or AI-resolution potential (see the AI Resolution & Self-Service section above) — if that's built well, several of the "High" rows below could land as Low human-contact-volume once self-service absorbs most of the query volume. Don't conflate the two when sizing L2/BPO headcount — this ranking is a build-priority signal, not a staffing forecast.

| Rank | Category | Weight | Why |
|:---:|---|:---:|---|
| 1 | 9. Product, Features & Information | High | Crypto/non-custodial trust questions ("is my money protected?", "why can't this be reversed?") are exactly the pre-purchase-anxiety queries that generate high, FAQ-deflectable volume in an unfamiliar product category — especially pre-GA while users are calibrating trust |
| 2 | 2. Account Access & Authentication | High | Login/biometric/lockout issues are near-universally the highest or second-highest volume category in any consumer app, regardless of product type |
| 3 | 4. Deposits & Wallet Funding | High | The core "does my money work" question, and the least familiar mental model for users new to on-chain deposits — irreversibility, network/token confusion, and depeg pauses likely drive outsized volume relative to a fiat equivalent |
| 4 | 1. Account Opening & Verification | High | KYC/liveness failure rates are a well-documented high-friction onboarding point; likely a top-tier driver, especially at External beta once volume includes real public sign-ups rather than staff |
| 5 | 11. Technical & App Issues | Medium-High | Universal category, typically elevated in the weeks immediately after any launch (bugs, app-store version skew) before settling lower |
| 6 | 3. Card & Payment Instrument Management | Medium | Card decline/freeze/lost-card queries are a consistently cited top driver in neobank benchmarks (Monzo/Revolut, referenced elsewhere in this knowledge base) — but Ray's card is a secondary surface to the wallet, so likely lower than in a neobank |
| 7 | 8. Account Management & Profile | Medium | Steady-state routine servicing (address/profile updates, closures). Self-custody export specifically may spike disproportionately relative to its "routine" framing, given its irreversibility and trust weight |
| 8 | 5. Transaction Disputes | Low-Medium | Card disputes typically ramp with card-spend usage over time rather than spiking at launch — expect this to grow through External beta rather than be prominent at Internal |
| 9 | 6. Report Fraud / Security Incident | Low | Low frequency by nature, but high severity and handling cost per contact — low volume should not translate into under-resourcing this lane, especially given the unresolved fraud-reimbursement gap (headline finding above) |
| 10 | 12. Formal Complaints | Low | A downstream subset of dissatisfaction surfaced elsewhere, not a primary driver in its own right |
| 11 | 7. Compliance-Driven Account Actions | Low | By design only a fraction of users trigger AML/PEP/sanctions actions; low volume, high severity, and each one requires careful no-tipping-off handling regardless of count |
| 12 | 10. Wellbeing & Specialist Support | Low | Low volume in any population by nature; likely lower still for Ray given no proactive vulnerability-identification mandate driving contacts inward |

---

## AI Resolution & Self-Service Architecture

**Two distinct levers, not one.** An earlier pass conflated these — worth stating explicitly:

- **In-app self-service** — a native app feature (a settings toggle, a reset flow, a status screen) that resolves the need with zero agent involvement, AI or human. Standard mobile-app UX, not dependent on Fin or any diagnostic capability. This is the larger lever and applies across most of the taxonomy, not just the crypto-specific categories.
- **AI-agent-resolved** — the query genuinely needs diagnosis (reading on-chain/account state, interpreting it) before an action can be offered. This is the narrower case the crypto-wallet research below actually addresses.
- **Human required** — judgment, compliance, or trust reasons make both of the above inappropriate (see "Why some categories are still not self-service-resolvable" below).

The crypto-wallet AI-agent research (second source) describes how AI support agents resolve non-custodial wallet queries natively inside the app, rather than just answering in chat. Two pieces of this map directly onto commitments the Ray Ops manual already makes, and are worth designing for explicitly rather than defaulting to a generic chat-only Fin deployment:

**1. Native resolution pipeline** — the agent doesn't just explain, it acts: it reads on-chain/account state (via API/webhook calls to indexers), diagnoses in plain language, and triggers a native in-app action (a deep-link into a pre-filled screen, or a biometric signing sheet) rather than telling the user to go do something themselves. Applied to Ray, this argues for status cards ("Broadcast → Confirming → Credited") and one-tap deep-links (e.g. into the self-custody export flow, or a network-view switch) inside the Fin mobile chat, not just prose answers.

**2. Three-tier action risk framework** — this is the same shape as Ray's own scoped tool contract (FR-2.33), just made concrete:

| Tier | Examples | Ray equivalent |
|---|---|---|
| **Client-side, zero signature** | Clear local cache, switch network view, register token metadata, end a connected session, navigate tabs | Self-service, AI-resolvable with no human or biometric step — the target for most Category 4/11 volume below |
| **User-signed, biometric mandatory** | Transaction replacement/cancellation, allowance revocation | Matches the manual's "every state-changing action requires user-side biometric reconfirmation" (confirmed) |
| **Prohibited** | Arbitrary transfers, seed/key export via the agent, biometric/recovery reconfiguration, unbounded approvals | Matches the manual's scoped tool contract exactly: no tool moves funds, changes payout destination, bypasses IDV, or returns raw PII/keys (confirmed) |

**3. Proactive intervention reduces inbound volume** — push notifications ahead of a known issue (e.g. a deposit taking longer than expected to confirm) rather than waiting for the user to open a ticket. This is the same principle already in `customer-segments.md`'s Behavioural Design Axes ("Trust fragility → a proactive-surfacing decision, not a resolution-speed decision") — worth building into Ray's launch scope rather than treating as a later optimization.

**What doesn't transfer**: query types built on features not confirmed for Ray — failed DEX swaps/slippage, cross-chain bridge relay tracking (LayerZero/Wormhole-style), and dApp browser/WalletConnect session guards. Ray's confirmed feature set (stablecoin deposit, card spend, self-custody export) doesn't include swaps, bridging, or third-party dApp connections. Don't build for these unless product confirms Ray's scope includes them.

### Where self-service/AI potential actually sits — and where it structurally can't

Once both levers (in-app self-service, and AI-agent diagnosis) are counted, most of the taxonomy has *some* self-service potential — Categories 2, 3, 4, 8, and 11 are all majority self-service-able, and 1, 5, 6, and 9 are partially so (an initial report or a status check is self-service even when the resolution isn't). The genuinely, structurally *not* self-service-able slice is smaller and specific:

1. **Compliance has deliberately walled Care out of the answer** (Category 1's PEP/sanctions rows, Category 7 entirely). The manual's silent-handoff/no-tipping-off doctrine means no agent — human, AI, or the user's own self-service action — is allowed to surface the disposition. This would hold even with a perfect AI or a perfectly designed settings screen: the user isn't allowed to see the answer, full stop.
2. **Where Care/AI is barred from acting on the user's behalf, the work shifts to self-service instead of disappearing** (Category 4's misdirected-deposit recovery is the exception — that one genuinely has no self-service path, since only Ray's Ops team can check whether it controls the destination keys; but Category 8's self-custody export is the opposite case — Care/AI being barred from ever touching keys is exactly *why* it has to be self-service, not a reason it's unresolvable).
3. **Some cases only exist because an automated check already failed** (Category 1's KYC document/liveness failures). Ubble already tried; routing back to another automated layer, or to a self-service retry that just resubmits the same document, defeats the escalation's purpose.
4. **Judgment and adversarial-trust problems don't reduce to a lookup or a toggle** (Category 12 complaint redress, Category 6's scam/fraud investigation and reimbursement decision, Category 10 wellbeing, Category 2's account-takeover specifically). You can't let a possibly-compromised session self-service its way out of a security incident, and redress/vulnerability decisions require weighing context neither a lookup nor a settings screen can supply — the same principle already codified for B2B/SMB in `customer-segments.md`'s AI-vs-human regulatory boundary table.
5. **Physical and external-world dependencies cap out at diagnosis, not fixing** (Category 1's physical card delivery, Category 4's depeg pause and genuine blockchain confirmation delay). Self-service and AI can both report status accurately; neither can make the external world move faster.

---

## Headline finding: the fraud-reimbursement gap

Braavos, as a UK banking product, would have carried the PSR's mandatory APP-fraud reimbursement scheme (up to £85,000, 50/50 liability split) for scams where a customer is tricked into authorising their own payment (romance scam, investment scam, impersonation scam). **Ray has no confirmed equivalent.** The manual's "Insurance Guarantee" explicitly covers Ray's own operational/infrastructure risk, not customer loss from a scam the customer was tricked into authorising themselves — and deposits are described as irreversible with no chargeback-equivalent. If a Ray user is socially engineered into sending stablecoin to a scammer, there is currently no stated reimbursement path in the source material.

This is worth raising with the Ray team and Legal before external beta — not something to resolve by inventing an answer here.

---

## 1. Account Opening & Verification 🟢 — volume: High (hypothesis)

Mostly common with Braavos — same underlying need (identity verification before onboarding), different regulatory citation. Braavos cited UK AML MLRs and named UK regulators (OFSI); Ray's basis is Ubble (IDV vendor) plus Compliance-owned screening with a silent handoff — no UK-specific statute confirmed.

| Sub-issue | Internal | External | Basis |
|---|:---:|:---:|---|
| Signup/application failure (technical) | ✓ | ✓ | Core onboarding |
| ID/document verification failure | ✓ | ✓ | Ubble pass/fail/step-up verdict |
| Biometric liveness check failure | ✓ | ✓ | Ubble — quality/liveness failures route to Care/Ops manual-review lane, 24h SLA (confirmed) |
| Full legal name mismatch or rejection | | ✓ | KYC/CDD-style check (global AML, jurisdiction TBD) |
| Date of birth / age verification failure | | ✓ | KYC |
| KYC data mismatch | | ✓ | Compliance EDD trigger |
| High-risk jurisdiction — EDD triggered | | ✓ | Compliance-owned, silent handoff (confirmed) |
| PEP identified at onboarding | | ✓ | Compliance-owned; Care never sees the disposition (confirmed) |
| Sanctions hit at onboarding | | ✓ | Compliance-owned; fixed no-tipping-off macro (confirmed) |
| Phone number/MFA setup failure | ✓ | ✓ | Access |
| Application declined — no reason given | | ✓ | Tipping-off constraints limit what Care can say (confirmed principle) |
| Application status enquiry / re-application | | ✓ | Standard |
| Physical card not received | | ✓ | Physical card inclusion varies by tier — Standard/Beam/Solar (confirmed) |
| Card activation failure | ✓ | ✓ | Standard |

---

## 2. Account Access & Authentication 🟢 — volume: High (hypothesis)

Fully common. Braavos cited PSD2 SCA (EU/UK-specific); Ray has no confirmed regulatory citation for this category — treat as access-critical operationally, not statutorily. **This is the category most undersold by the AI-agent-only lens** — most of it is plain in-app self-service, no agent needed, the same way password/PIN reset works in any mobile banking app today.

*Architecture note (third source)*: Ray's key-management model (Care cannot retrieve/reset keys; user-driven export is the only exposure path) matches the MPC/embedded-wallet category's recovery pattern — MFA, biometrics, and cloud enclaves, not a seed phrase. That's *why* almost every row below is genuinely self-service by design (there is no seed phrase to "recover" in the first place) — it's an architectural property, not just a UX choice, and worth stating explicitly in agent training so no one implies a seed-phrase-style recovery path exists.

| Sub-issue | Internal | External | Basis | Self-service potential |
|---|:---:|:---:|---|---|
| PIN forgotten/blocked | ✓ | ✓ | Access | High — native "forgot PIN" reset flow, re-verify via biometric/existing credential |
| Biometric login failure | ✓ | ✓ | Access | High — native re-enrollment flow |
| App login failure — general | ✓ | ✓ | Access | High — standard troubleshooting (reinstall, credential reset) is self-service |
| Locked out after failed attempts | ✓ | ✓ | Access | High — self-service unlock via secondary verification, same pattern as PIN reset |
| Lost phone — cannot access app | ✓ | ✓ | Access — rescue channel needed from Internal (real funds) | Medium — self-service device deregistration + re-pairing on a new device is standard, but re-verifying identity at that step may need a KYC-strength check, not zero-touch |
| Account takeover — suspected | ✓ | ✓ | Security incident — kill-switch eligible per manual (CS Lead/Eng on-call/Risk on-call can fire unilaterally) | **Not self-service** — the one genuine exception in this category. You can't self-service your way out of a security incident on a session that might itself be compromised; needs human/kill-switch escalation |
| Suspicious login notification | ✓ | ✓ | Security | High — self-service "this wasn't me, lock my account" action, immediate and user-initiated |
| SIM swap / MFA compromise | | ✓ | Security | Medium — initial self-service lock/re-secure, but full resolution likely needs verification support |
| Step-up authentication failure | | ✓ | Access | High — self-service retry/alternate-method flow |
| Device change / new phone setup | | ✓ | Access | High — self-service onboarding of a new device, standard pattern |

---

## 3. Card & Payment Instrument Management 🟡 — volume: Medium (hypothesis)

Mostly common (lost/stolen card, freeze/unfreeze, virtual card) but Ray adds tier and burner-card mechanics Braavos didn't have. **Also undersold on self-service** — freeze/unfreeze, virtual/burner card issuance, and multi-card management are toggle-style self-service features by design; "burner card" only makes sense as a self-service feature (the point is instant, disposable, no request process).

| Sub-issue | Internal | External | Basis | Self-service potential |
|---|:---:|:---:|---|---|
| Lost/stolen card | ✓ | ✓ | Immediate restriction, standard card ops | High — self-service "report lost/stolen" triggers immediate freeze + replacement order in one flow |
| Card freeze/unfreeze (consumer-initiated) | ✓ | ✓ | Standard | High — a toggle, not a ticket |
| Damaged/replacement card | | ✓ | Standard | High — self-service replacement request |
| Card declined at POS — reason unknown | ✓ | ✓ | Standard | Medium — decline-reason lookup can be self-service (a status/history screen); genuine fraud holds still need escalation |
| Virtual card creation/management | ✓ | ✓ | Standard | High — self-service by design |
| 🔵 Single-use "burner" card issuance/management | | ✓ | Confirmed Ray feature, no Braavos equivalent | High — the feature only has value if it's instant and self-service |
| 🔵 Multi-card management | | ✓ | Confirmed Ray feature | High — self-service |
| 🔵 Tier-based card entitlement query (Standard/Beam/Solar — ATM allowance, physical card inclusion, FX margin) | ✓ | ✓ | Confirmed tiers differ on these axes | High — informational, self-service via an account/plan screen |
| Apple Pay/Google Pay setup or failure | ✓ | ✓ | Standard | Medium — often self-service troubleshooting, but OS-level wallet issues can require guided support |

---

## 4. Deposits & Wallet Funding 🟡 (renamed from Braavos's "Payments & Transactions") — volume: High (hypothesis)

The category most changed. Braavos's fiat rails (Direct Debit, standing orders, Faster Payments/CHAPS) have no Ray equivalent — ⚪ removed. Ray's funding model is on-chain stablecoin deposit only, which is a materially different risk and query shape.

**Self-service note (from the AI-agent research)**: several rows below split into a self-service-resolvable case and a genuine Care/Compliance case that look identical to the user ("my deposit isn't showing up") but require completely different handling. Distinguishing them at the AI-classification step, before routing, is the highest-leverage design move in this category — see the AI Resolution & Self-Service section above.

**Architecture note (third source)**: the manual's "gas abstraction" (Ray handles it, user never touches gas) matches the account-abstraction/paymaster pattern in the wider market — the user doesn't need to hold a separate native gas token to fund or spend. This is a query type that should **not** appear in Ray's volume ("I don't have enough ETH/gas to complete my deposit" is a common query for legacy self-custody wallets) — if it does surface post-launch, it signals the gas-abstraction promise isn't holding up in practice, not a user-education gap.

**Confirmed (2026-08-19, Charlie)**: displayed balance is not exposed to on-chain depeg risk. Ray keeps its own ledger tracking stablecoins 1:1 against USD, and the app always shows the full USD-equivalent balance regardless of what's happening to the underlying token's peg on-chain. The depeg row below is scoped correctly as-is — it's about deposits/funding being paused during a depeg event, not about a user's existing held balance changing value in the app. No separate "my balance dropped because of a depeg" query type should exist.

| Sub-issue | Internal | External | Basis | AI/self-service potential |
|---|:---:|:---:|---|---|
| On-chain stablecoin deposit failure or delay | ✓ | ✓ | Core funding mechanism (USDT, USDC at launch, confirmed) | High — real-time confirmation-count/status card ("Broadcast → Confirming → Credited") is fully self-service if Ray's indexer can see the transaction at all |
| 🔵 Unsupported network/token selected | | ✓ | New — no fiat equivalent | Medium — self-service if Ray's own indexer can detect the deposit on an unsupported-but-visible network; otherwise becomes the misdirected-deposit case below |
| 🔵 Deposit sent to wrong network/address (misdirected deposit) | | ✓ | Care/Ops recovery queue, disclosed fee, best-effort SLA — only recoverable where Ray's wallet stack controls the destination keys (confirmed) | **Not self-service** — genuine Care/Ops case requiring human recovery-queue handling regardless of how good the AI diagnosis is |
| 🔵 "Why can't this be reversed?" / deposit irreversibility query | ✓ | ✓ | No chargeback-equivalent for deposits (confirmed) — high-priority FAQ/education need | High — pure education/FAQ, fully AI-resolvable |
| 🔵 Stablecoin depeg — deposits/funding-ladder auto-paused | | ✓ | Confirmed mechanic; refunds during pause at 1:1 USD in USDT, no automatic compensation | High for the explanation, but the underlying pause is a platform state the AI can only report, not resolve |
| Double/duplicate deposit query | | ✓ | Standard | Medium — self-service if both deposits are visible on-chain and simply need explaining; not self-service if one needs reversing |
| FX/exchange rate transparency (stablecoin conversion, tier FX margin) | | ✓ | Tier FX margin differs (confirmed) | High — FAQ/education |
| Card transaction decline/failure (spending, not deposit) | ✓ | ✓ | Carried over from Braavos — same need regardless of funding source | Medium — decline-reason lookup is often self-service; genuine fraud holds are not |
| ⚪ Direct debit / standing order / Faster Payments-CHAPS timing | — | — | Removed — no fiat bank-rail equivalent confirmed for Ray | — |

---

## 5. Transaction Disputes 🟢 — volume: Low-Medium (hypothesis)

The **least** changed category. A Visa card dispute is a Visa card dispute regardless of what backs the wallet — card scheme rules (Visa 12.x/13.x) apply the same way.

| Sub-issue | Internal | External | Basis |
|---|:---:|:---:|---|
| Merchant dispute — goods not received / not as described / service not provided | | ✓ | Visa scheme rules — same as any Visa card |
| Incorrect amount charged / duplicate charge by merchant | | ✓ | Visa scheme rules |
| Dispute status enquiry | | ✓ | Standard |
| Dispute outcome — consumer challenges decision | | ✓ | Internal review only — no FOS-equivalent confirmed |

---

## 6. Report Fraud / Security Incident 🟡 — volume: Low, severity: High (hypothesis)

Structurally common (account takeover, phishing, scam reporting all still need a path) but the **reimbursement backstop is the key gap** — see headline finding above. Note: the *reporting action itself* (tap "report fraud" on a transaction, trigger an immediate freeze) is self-service in every row here — it's the investigation and any redress decision that require a human, not the initial report.

| Sub-issue | Internal | External | Basis |
|---|:---:|:---:|---|
| Account takeover — consumer reports it first | ✓ | ✓ | Security incident, kill-switch eligible |
| Phishing / vishing / smishing reporting | | ✓ | Standard reporting path |
| Card-present fraud (physical card used without consent) | | ✓ | Card network liability rules (not deposit-related) |
| ❓ Romance/investment/impersonation scam — consumer authorised their own deposit | | ✓ | **No reimbursement mechanism confirmed.** Insurance Guarantee ≠ deposit insurance; deposits are irreversible. Flag to Legal/Ray team before external beta. |
| Suspected money mule / account receiving fraudulent funds | | ✓ | Compliance-owned; MLRO-style escalation, no-tipping-off (global AML principle, not UK POCA specifically) |
| ⚪ UK PSR mandatory APP-fraud reimbursement (up to £85,000, 50/50 liability) | — | — | Removed — UK-statutory, not confirmed for Ray |

---

## 7. Compliance-Driven Account Actions (AML / Travel Rule / Sanctions) 🟡 — volume: Low, severity: High (hypothesis)

Structurally common with Braavos's "Account Action by Checkout" category, but the citations change from UK statutes (POCA, SAMLA/OFSI) to the manual's core doctrine: Care owns "did it work," Compliance owns "is it permitted," and Care never sees screening dispositions.

| Sub-issue | Internal | External | Basis |
|---|:---:|:---:|---|
| Account frozen pending AML/Travel Rule investigation | | ✓ | Compliance-owned, silent handoff (confirmed doctrine, §0.3) |
| Account frozen — PEP/sanctions/adverse-media post-onboarding | | ✓ | Compliance-owned, fixed no-tipping-off macros (confirmed) |
| 🔵 VASP resolution for external sends to hosted wallets | | ✓ | Confirmed Travel Rule mechanic, no Braavos equivalent |
| 🔵 Unhosted-wallet ownership proof request | | ✓ | Confirmed Travel Rule mechanic |
| Capability limit applied (spending/top-up restricted) | | ✓ | Compliance-driven restriction, needs a care path regardless of citation |
| Account closure initiated by Ray | | ✓ | Standard, notice mechanics TBD (not detailed in manual) |
| ❓ Which jurisdiction's AML/Travel Rule instrument formally applies | | | Not specified in the manual — Compliance-owned, needs confirmation before Legal sign-off on macros |

---

## 8. Account Management & Profile 🟢 — volume: Medium (hypothesis)

Mostly common. One genuinely new, defining Ray feature: self-custody export. **This is the category with the highest self-service ceiling in the whole taxonomy** — most rows are settings-screen updates by nature, and self-custody export is 100% self-service *by design*: Care is structurally barred from doing it for the user (FR-1.36), so if it isn't self-service in the app, it doesn't exist as a resolution path at all.

| Sub-issue | Internal | External | Basis | Self-service potential |
|---|:---:|:---:|---|---|
| Consumer-initiated account closure | | ✓ | Standard | High — self-service initiation; may need a confirmation/cooling-off step, not human review |
| 🔵 Closure requested while an outstanding negative balance is owed (force-post/dunning per Category 4) | | ✓ | New — added 2026-08-19 per Charlie. Closure and negative-balance recovery are handled separately elsewhere in the manual, but the intersection (a user tries to close while still in dunning) isn't addressed. Needs a defined path: settle-before-close, or close-with-debt-recovery-continuing-post-closure | **Not self-service** — recovering an owed balance from a non-custodial wallet the user controls is a genuine Ops/Compliance decision, not a toggle |
| 🔵 Self-custody / key export request | ✓ | ✓ | Confirmed (FR-1.36) — the **only** path by which keys are ever exposed; Care cannot retrieve/reset/re-issue keys under any other circumstance | **Maximal** — this must be self-service; there is no human-assisted path by design |
| Data rights request | | ✓ | "Data rights" is a named L2 lane (confirmed); which data-protection regime applies is jurisdiction-dependent, not specified | Medium — self-service submission, but fulfilment (compiling/exporting the actual data) likely needs backend processing, not zero-touch |
| Update address/phone/email/name | | ✓ | Standard | High — settings-screen self-service |
| Third-party access / Power of Attorney | | ✓ | Standard, not elaborated in manual | Low — identity/legal verification likely needed, not zero-touch |
| Consumer-controlled spending limits/blocks | | ✓ | Standard | High — settings-screen self-service |
| Notification preferences | | ✓ | Standard | High — settings-screen self-service |

---

## 9. Product, Features & Information 🟡 — volume: High (hypothesis)

Mostly common in shape, but the actual content is very different — Ray's core trust question ("is my money protected?") has a genuinely different answer than a bank's, and that answer is legally sensitive to get wrong.

| Sub-issue | Internal | External | Basis |
|---|:---:|:---:|---|
| 🔵 "Is my money protected?" — Insurance Guarantee vs. deposit insurance | ✓ | ✓ | High-priority, legally-reviewed macro (confirmed, §7 FAQ bank) — must be unambiguous that this is not deposit insurance |
| How rewards/cashback accrues | ✓ | ✓ | Confirmed feature exists |
| Fee schedule / tier FX margin explainer | | ✓ | Standard/Beam/Solar differ (confirmed) |
| Supported stablecoins/networks explainer | ✓ | ✓ | USDT/USDC at launch (confirmed) |
| Self-custody / non-custodial model explainer | ✓ | ✓ | Core trust education (confirmed doctrine) |
| T&Cs clarification | | ✓ | Standard |
| ⚪ "UK-only MVP" / international usage constraint | — | — | Removed — Ray is multi-market by design (6 launch languages, UAE #2 market), not UK-constrained |

---

## 10. Wellbeing & Specialist Support ⚪🟡 (heavily reduced from Braavos) — volume: Low (hypothesis)

Braavos's entire vulnerability/wellbeing category was built on UK Consumer Duty (FG21/1) — a legal mandate Ray does not carry. The manual confirms only a generic "wellbeing handoff" macro exists in its FAQ bank, with no elaboration. Everything else below is **not confirmed** for Ray — flagged as an open question, not asserted.

| Sub-issue | Internal | External | Basis |
|---|:---:|:---:|---|
| Wellbeing handoff (fixed macro referenced in manual, §7) | | ✓ | Confirmed to exist; scope/protocol not detailed |
| ❓ Financial hardship, gambling harm, domestic/financial abuse, bereavement, disability accommodation, debt referral | | | Not addressed in the manual. No Consumer Duty mandate applies, but that doesn't mean Ray should have no protocol — this is a genuine product/Legal decision to make, not something to infer from the Ops manual's silence. |

---

## 11. Technical & App Issues 🟢 — volume: Medium-High (hypothesis)

Fully common — no regulatory dimension either way. One addition from the AI-agent research: a meaningful share of "the app is broken" reports in crypto wallets aren't bugs at all — they're a network-view mismatch or unregistered-asset display issue, both self-service fixable.

*Architecture note (third source)*: for this wallet category generally, infrastructure-side failure modes (signing-relay/bundler downtime, indexer lag, cloud provider outages) are a more common root cause than smart-contract bugs or user error. Worth tagging "balance/transaction not loading" reports against Ray's own infra status before assuming user-side display issues — a cluster of these during an actual infra incident should route to a status-page/incident macro, not individual troubleshooting.

| Sub-issue | Internal | External | Basis | AI/self-service potential |
|---|:---:|:---:|---|---|
| 2FA/OTP not received | ✓ | ✓ | Access | Low — usually needs a resend/troubleshoot flow, not pure self-service |
| In-app chat not loading | ✓ | ✓ | Primary Care channel — must work from Internal | — |
| App crash/instability, blank screen, feature not loading | | ✓ | Standard | Low |
| Error message unclear | | ✓ | Standard | High — plain-language re-explanation is a core AI strength |
| Transaction history / balance not loading or looks wrong | | ✓ | Standard | High — often a display/sync issue rather than a real discrepancy; a one-tap "refresh/re-sync" or "check across networks" action, if Ray's indexer supports it, resolves this without a ticket |

---

## 12. Formal Complaints 🟡 — volume: Low (hypothesis)

Structurally common — Complaints is a named L2 lane — but with operational rather than statutory SLAs and no FOS-equivalent.

| Sub-issue | Internal | External | Basis |
|---|:---:|:---:|---|
| Formal complaint — any issue above the consumer is dissatisfied with | | ✓ | Named L2 lane (confirmed); ack 24h / resolution 15 calendar days (confirmed manual SLA, operational not statutory) |
| Complaint escalation / consumer challenges outcome | | ✓ | Internal review only — no FOS-equivalent confirmed |
| ⚪ FCA DISP 5-day ack / 8-week resolution clock, FOS referral rights | — | — | Removed — UK-statutory, not confirmed for Ray |

---

## Open questions to close before this taxonomy can be finalized

1. Fraud-reimbursement gap (headline finding above) — needs a Legal/Ray-team answer, not a Care assumption.
2. Which jurisdiction's AML/Travel Rule instrument formally governs Ray's compliance actions (Category 7).
3. Whether any vulnerability/wellbeing protocol beyond the generic handoff macro is planned (Category 10) — silence in the Ops manual isn't a decision either way.
4. Real query-volume data to validate which sub-issues are actually high-frequency vs. edge case — the Internal/External phase gating above is my judgment call, not sourced data. The same applies to the "Suggested volume weighting" ranking above: it's a prioritization hypothesis, not a forecast to staff against.
5. Confirm Ray's actual feature scope against the AI Resolution & Self-Service section above — specifically whether Ray supports token swaps, cross-chain bridging, or dApp/WalletConnect connections. If any of those are in scope, this taxonomy is missing the query types that come with them.
6. Closure with an outstanding negative balance (Category 8, added 2026-08-19) — needs Ops/Compliance to decide whether closure is blocked until the debt is settled, or the debt-recovery process continues after closure. Not addressed in the Ops manual.

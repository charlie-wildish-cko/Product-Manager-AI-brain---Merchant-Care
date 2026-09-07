# Ray Care Taxonomy — Sub-Issue Volume Weighting Estimate

**Status**: Hypothesis only. No real Ray contact data exists yet (see [[project-ray-b2c]]). This tiers the 185 active sub-issues in the Google Sheet ["Ray - Care issue taxonomy"](https://docs.google.com/spreadsheets/d/1fshT3U9xR50-WorPyCduOqQxQWcj_0IHvuJhRhqGa5Q) (230 rows total, 16 N/A to Ray, 19 category headers, 185 active sub-issues) by expected inbound-query volume. Treat as a build/staffing prioritization signal, not a forecast — validate against real data once Phase 2 (Closed/Public Beta) generates it.

**Tiers**: H (High) · M-H (Medium-High) · M (Medium) · L (Low) · R (Rare per-user, may still be high-severity)

**Method**: no fintech/crypto-wallet benchmark exists for categories 13–19 (Ray-specific, no Braavos equivalent), so those are reasoned from first principles — irreversibility anxiety, unfamiliarity of on-chain mental models, and whether gas-abstraction/UX promises are holding (a query type that shouldn't exist if the design works). Categories 1–12 lean on known neobank/fintech support patterns (access issues and card declines are consistently top drivers; compliance and wellbeing rows are inherently low-frequency per user regardless of severity).

---

## 1. Account Opening & Verification — category: High

| Sub-issue | Tier | Why |
|---|:---:|---|
| Signup/application failure (technical) | H | Universal onboarding friction point |
| ID/document verification failure | H | Ubble failure rates are a well-documented high-friction onboarding step |
| Biometric liveness check failure | M-H | Subset of doc-verification failures |
| Phone/MFA setup failure at onboarding | M | Standard onboarding step failure |
| Application status enquiry | M | Impatience during KYC wait, especially pre-GA |
| Application declined — no reason given | L | Downstream of screening failures, low count |
| High-risk jurisdiction EDD | L | Small % of applicant pool |
| Re-application after decline | L | Small subset |
| Card activation failure (new card) | M | Every issued card needs activation, but virtual auto-issues — mainly relevant once physical card lands |
| Physical card not received | L | Phase 3 only, secondary surface to the wallet |
| PEP identified at onboarding | R | Rare, high severity |
| Sanctions hit at onboarding | R | Rare, high severity |
| Signup failure due to eligibility (excluded jurisdiction) | L | Rare per applicant, blocking when it hits |

*(Name/DOB/KYC-mismatch rows are N/A to Ray — no validation source exists — excluded from weighting.)*

---

## 2. Account Access & Authentication — category: High

| Sub-issue | Tier | Why |
|---|:---:|---|
| PIN forgotten or blocked | H | Near-universal top-1/2 volume driver in any consumer app |
| Biometric login failure | H | Same |
| App login failure — general | H | Same |
| Locked out after failed login attempts | M-H | Adjacent to the above |
| Suspicious login notification received | M | Self-triggered curiosity, moderate frequency |
| Step-up authentication challenge failure | M | Visa 3DS-driven, routine |
| Device change / new phone setup | M | Periodic, routine event |
| Magic link / email login issues | M | Routine access friction |
| Lost phone — cannot access app | M | Less frequent, high effort when it happens |
| SIM swap concern / MFA compromise | L | Lower frequency, high severity |
| Account suspended by Checkout (no context) | L | Rare |
| Account takeover — consumer suspects | L | Rare, high severity |

---

## 3. Card & Payment Instrument Management — category: Medium

| Sub-issue | Tier | Why |
|---|:---:|---|
| Card declined at POS — reason unknown | H | Consistently a top-tier driver in neobank benchmarks |
| Card freeze (consumer-initiated) | M | Self-serve toggle, moderate frequency |
| Card unfreeze | M | Same |
| Card not working — chip/contactless issue | M | Routine device/card friction |
| Virtual card creation or management | M | Self-serve, routine |
| Apple Pay / Google Pay setup or failure | M | OS-wallet friction, moderate |
| Lost card | M | Routine, expected event |
| Card spending controls (enable/disable categories) | L-M | Self-serve, lower frequency |
| Replacement card request | L-M | Downstream of lost/damaged |
| Stolen card | L-M | Less frequent than "lost" |
| Damaged card | L | Lower frequency |
| Card name change request | L | Rare |
| Card expiry — renewal/replacement query | L | Phase 3 only |
| Contactless payment limit query | L | Informational, low salience |

---

## 4. Payments & Transactions — category: Medium (mostly N/A; remaining rows are card-spend adjacent)

| Sub-issue | Tier | Why |
|---|:---:|---|
| Payment failure or declined payment | H | Frequent, universal card-spend issue |
| Unrecognised transaction — query before dispute | M-H | Classic pre-dispute query, high frequency |
| Top-up or funding failure | M | Overlaps conceptually with Category 13's funding rows |
| Pending payment — not yet settled | M | Routine "why hasn't this settled" query |
| Refund not received from merchant | M | Routine post-purchase query |
| Duplicate charge query | M | Routine |
| Transfer limit query or limit reached | L | Lower frequency |

*(CPR, direct debit, standing orders, scheduled payments, Faster Payments/CHAPS: N/A to Ray — excluded.)*

---

## 5. Transaction Disputes — category: Low-Medium (ramps with card-spend usage over time, not launch-spiked)

| Sub-issue | Tier | Why |
|---|:---:|---|
| Merchant dispute — cancelled subscription still charged | M-H | Recurring-billing disputes are a consistently high driver across card ecosystems |
| Merchant dispute — goods not received | M | Standard e-commerce dispute driver |
| Merchant dispute — item not as described | M | Same |
| Merchant dispute — service not provided | M | Same |
| Incorrect amount charged by merchant | M | Standard |
| Duplicate charge by merchant | M | Standard |
| Pre-dispute enquiry — wants to contact merchant first | M | Standard pre-dispute step |
| Pre-dispute enquiry — merchant declined | M | Follow-on from above |
| Dispute status enquiry | M | Once disputes exist, status checks are frequent |
| Merchant error — technical duplicate | L | Narrower case |
| Dispute outcome — consumer challenges decision | L | Smaller subset |

---

## 6. Report a Security Incident — category: Low volume, high severity

| Sub-issue | Tier | Why |
|---|:---:|---|
| Unauthorised transaction — CNP fraud | M | More common than full account-takeover fraud |
| Phishing — fraudulent email | L-M | Reporting action is low-effort, moderate frequency |
| Account takeover — consumer reports it first | L | Rare, high severity |
| Vishing / Smishing | L | Lower frequency than phishing |
| APP fraud — deceived into authorising a payment | L | Concerning but lower count than card fraud; ties to the fraud-reimbursement gap |
| Investment / Impersonation scam | L | Lower frequency, high severity |
| Romance / Recruitment scam | R | Rare |
| Money mule / fraudulent-funds receipt | R | Rare |
| Card-present fraud | R | Phase 3 only, physical card |
| Reporting on behalf of vulnerable third party | R | Rare |

---

## 7. Account Action by Checkout (Compliance-Driven) — category: Low across the board

All rows are Compliance-owned and inherently low-frequency per user (AML/sanctions/PEP-triggered), regardless of severity. Tier: **L** for account-freeze/suspension/restriction rows (AML, sanctions, adverse media, velocity/TM alerts, capability limits, closure-by-Checkout, EDR); **R** for the two Phase-3-only rows (periodic review contact, scheme monitoring threshold breach).

---

## 8. Account Management & Profile — category: Medium

| Sub-issue | Tier | Why |
|---|:---:|---|
| Update address / phone / email | M each | Routine self-serve settings updates |
| Download bank statement | M | Routine, on-demand |
| Consumer-controlled spending limits and blocks | M | Self-serve, moderate frequency |
| Notification preferences | M | Self-serve, moderate frequency |
| Consumer-initiated account closure | L-M | Meaningful but not high-frequency |
| Marketing opt-out | L | Lower salience |
| Account history / audit trail request | L | Lower frequency |
| Update name (legal name change) | L | Rare |
| Subject Access Request (data export) | R | Rare per user, resource-intensive when it happens |
| Data deletion / right to erasure request | R | Rare |
| Account cooling-off period query | R | Phase 3 only |

---

## 9. Product, Features & Information — category: High (FAQ-heavy, pre-launch trust questions)

| Sub-issue | Tier | Why |
|---|:---:|---|
| FSCS protection / "is my money protected?" | H | The core trust question in an unfamiliar, non-custodial product category — matches the headline finding in the local draft |
| International usage and FX rates | H | Ray is global from day one with a USD card; cross-currency FX is core from the first transaction (per the sheet's own commentary) |
| Fee schedule and pricing query | H | Universal curiosity driver in any priced product |
| General product education ("how the account works")* | H | Core onboarding-trust FAQ |
| How rewards/cashback accrues | M-H | High curiosity, especially pre-GA |
| Understanding transaction descriptions | M | Routine clarity query |
| Transfer and spending limits — what they are | M | Routine |
| T&Cs clarification | M | Two contracts (Ray Global + Checkout SAS) adds genuine confusion surface |
| Interest rate and savings product info | L-M | No interest/savings exists — expect "why no interest" curiosity queries |
| Cashback conditions and eligibility | M | Moderate |
| Merchant exclusions for cashback | L | Narrower |
| Spending categories and budgeting tools | L | Phase 3 only |

\* *Data-quality flag: this row is still labeled "How Braavos account works" in the sheet — a leftover from the shared Braavos-taxonomy copy-paste that wasn't renamed for Ray. Worth fixing in the sheet directly (Charlie only, per the no-cell-editing-MCP note in [[reference-ray-taxonomy-sheet]]).*

---

## 10. Wellbeing & Specialist Support — category: Low (inherently low-frequency per capita, severity ≠ volume)

| Sub-issue | Tier | Why |
|---|:---:|---|
| Insufficient funds — signposting | M | Only "decline" event, moderate frequency, but the wellbeing-signposting sub-flow is a narrower slice of it |
| Gambling block request | L-M | Self-serve toggle (delivered via MCC block), moderate |
| Disability/accessibility affecting account access | L | Low frequency |
| Financial difficulty / hardship support | L | Low frequency |
| Gambling block deactivation | R | Rare |
| Self-harm/suicide disclosure, modern slavery, financial/domestic/coercive abuse, mental health, addiction, bereavement (both rows), debt referral | R each | Low volume by nature in any population; severity is high but count is low |

---

## 11. Technical & App Issues — category: Medium-High (elevated at launch, settles over time)

| Sub-issue | Tier | Why |
|---|:---:|---|
| 2FA/OTP not received | H | Frequent access-adjacent friction |
| Error message — unclear or unexplained | M-H | Effectively a catch-all category, high count |
| Transaction history not loading or displaying incorrectly | M-H | Directly tied to "where's my money" trust anxiety |
| App crash or instability | M-H | Typical elevated-at-launch pattern |
| Feature not working or loading | M-H | Same |
| In-app chat not loading or connecting | M | Important because it's the fallback path itself — must work from Internal Alpha |
| App blank screen or not opening | M | Launch-elevated |
| Biometric setup failure (technical) | M | Distinct from login-failure row above |
| App update required — old version blocking | M | Routine |
| App performance — slow/unresponsive | M | Routine |
| Apple Pay / Google Pay technical setup failure | M | Routine |
| Push notification not received | L-M | Lower salience |
| Device compatibility / OS version issue | L | Narrower |
| Diagnostic information collection | L | Escalation-only, low count |
| Statement download failure | L | Phase 3, narrow |

---

## 12. Formal Complaints — category: Low (downstream of dissatisfaction elsewhere)

| Sub-issue | Tier | Why |
|---|:---:|---|
| Formal complaint (any issue in Categories 1–11) | L | Aggregate downstream signal, not a primary driver |
| Complaint about complaint handling (meta-complaint) | R | Rare |
| Financial redress credit following upheld complaint | R | Rare |

---

## 13. Wallet & On-Chain Funding (Ray-specific) — category: High (the core "does my money work" category)

| Sub-issue | Tier | Why |
|---|:---:|---|
| Deposit not yet credited — awaiting network confirmations | H | Likely the single highest-volume row in the whole taxonomy — the least familiar mental model for a first-time on-chain depositor |
| Who pays network/gas fees | M-H | Classic FAQ; high curiosity in a gas-abstracted product, and a query that *shouldn't* need to exist if the abstraction is working — worth monitoring as a canary |
| Deposit delayed or stuck beyond the 24h window | M-H | Escalation subset of the row above |
| Wrong chain/network used for a deposit | M | Well-documented crypto UX failure mode |
| Wrong or unsupported asset sent to a Ray address | M | Same failure family |
| Deposit address confusion / chain-mismatch warning | M | Pre-emptive FAQ version of the above |
| Own local funding rail failure (PIX/GCash/bank transfer) | M-H | Phase 3, but local on-ramp rails are typically failure-prone in UAE/Brazil/Philippines |
| Third-party fiat on-ramp failure | M | Phase 3, on-ramp friction is typically high |
| Wrong asset used to fund a purchase (funding ladder) | M | Routine mechanic query |
| Stablecoin swap failed or rate/spread queried | L-M | Phase 2+ |
| Deposit held by on-chain screening (risk band) | L | Compliance-triggered subset, lower frequency |
| Depeg pause — deposits/funding suspended | L | Rare event, high salience when it occurs |
| Embedded Wallet provisioning failed | L | Should be rare if engineering is solid — critical severity if it happens at all, especially Phase 1 |

---

## 14. On-Chain Sends & Recipients (Ray-specific) — category: Medium-High

| Sub-issue | Tier | Why |
|---|:---:|---|
| External send stuck/pending | M-H | Irreversibility anxiety drives high salience regardless of actual frequency |
| Ray-to-Ray send failed or not received | M | Should mostly work, but still a query source given volume of internal sends |
| External send to a wrong address — funds lost | M | Classic, severe crypto user error |
| First-send verification / cooling delay friction | M | Deliberately introduces friction — will generate "why is this slow" queries by design |
| Travel Rule information required before a send | M | Unfamiliar extra step generates volume simply by existing |
| Unhosted-wallet ownership proof required | L-M | Narrower subset of Travel Rule friction |
| Destination tag/memo omitted — funds misrouted | L | More of an exchange-specific pattern, less common in Ray's stablecoin-only flows |
| Duplicate-send guard triggered | L | Narrow |
| Saved recipient management/label issue | L | Low salience |
| Send blocked by destination screening | L | Compliance-triggered, lower frequency |
| User proceeded past a scam warning and lost funds | L | Low frequency, high severity — ties to the fraud-reimbursement gap |
| Wallet/exchange connect failure | L | Phase 3+ roadmap feature |
| Contact sync / invite privacy concern | R | Rare |

---

## 15. Spend Engine, Pull & Settlement (Ray-specific) — category: Medium

| Sub-issue | Tier | Why |
|---|:---:|---|
| Purchase approved but at-auth pull failed or pending | M-H | Spend-engine mechanics unique to Ray, likely a confusing new failure mode |
| Pending amount higher than the purchase | M | Universal card-authorization behavior, but a new context for Ray users |
| Funds appear locked — smart block not released | M | Novel mechanic, moderate frequency |
| 3DS / out-of-band challenge failed | M | Routine card friction |
| Unexpected or disputed programme fee pull | L-M | Moderate, ties to trust |
| Negative balance after force-post; card auto-frozen | L-M | Consequential when it happens |
| Programme fee pull failed — insufficient balance | L | Narrower |
| Dunning notices and deposit-only restriction | L | Downstream of the above |
| Refund credited in a different asset (depeg rule) | L | Narrow, rare-triggering event |
| ATM withdrawal problem | L | Phase 3 only |
| Decline reason is sanctions_block or kyc_state | R | Rare, compliance-triggered |
| Widespread declines during platform degradation | R | Rare per-user, but generates a volume spike when it occurs |

---

## 16. Rewards, Cashback & Tiers (Ray-specific) — category: Low-Medium

| Sub-issue | Tier | Why |
|---|:---:|---|
| Rewards accrued but not yet paid (threshold rollover) | M | Routine "where's my reward" query |
| "Is this interest?" — rewards nature and source | M | Trust/labeling question, moderate salience |
| Referral reward not paid or clawed back | L-M | Moderate |
| Paid tier billing, upgrade or downgrade | L-M | Self-serve, moderate |
| Cashback reversed after a refund or chargeback | L | Narrower |
| Reward held pending abuse review | L | Narrow |
| Founding-user cohort benefits query | L | Short-lived novelty spike at launch, then decays |
| Opt-in higher-rewards tier risk query | L | Narrow |
| Perk redemption failure | L | Narrow |

---

## 17. Wallet Ownership, Key Export & Insurance (Ray-specific) — category: Medium (FAQ-heavy, action-rare)

| Sub-issue | Tier | Why |
|---|:---:|---|
| "Is my money protected like a bank?" | H | Close cousin of Category 9's FSCS row — likely one of the single most-asked trust questions pre-GA |
| Insurance Guarantee scope question | M-H | Core trust FAQ, high salience given the legal sensitivity of getting this wrong |
| "Send me my seed phrase / recover my key" | M | Education/correction query — moderately frequent early on as users apply legacy-wallet mental models |
| Key export / self-custody transition request | L | The action itself is rare, though real and structurally important |
| Closure requested with assets still in the wallet | L | Moderate-low |
| Closure requested while owing money | L | Moderate-low |
| Export held at "Finalising your wallet" (settlement gate) | L | Narrow, technical |
| Dormancy fee applied / account dormant | L | Phase 3 only |
| Insurance Guarantee claim submission | R | Rare |
| User exported keys, now wants Ray services back | R | Rare |
| Deceased user — wallet inheritance/beneficiary | R | Rare, unresolved framework (flagged open with Legal) |
| Wallet address reclassified by ongoing estate rescreen | R | Rare |

---

## 18. Multi-Asset, Marketplace & Roadmap Surfaces (Ray-specific) — category: Low across the board

All rows are Phase 3 roadmap items on immature/unconfirmed features (family accounts, marketplace vouchers, Direct Pay, auto-liquidation, trading, push-to-wallet payouts, tax documents, desktop companion). Tier: **L** for the ones with a clearer near-term path (marketplace voucher failure, Direct Pay failure, tax document request); **R** for the more speculative ones (auto-liquidation, trading/sub-account, family controls, desktop access) — several of these also depend on Ray confirming scope beyond stablecoin-only, which is not yet settled per the open questions in the local draft.

---

## 19. Localisation, Access & Market Posture (Ray-specific) — category: Medium

| Sub-issue | Tier | Why |
|---|:---:|---|
| Blocked at intent gate (VPN, proxy, rooted device, emulator) | M | Crypto apps commonly trigger this; VPN usage norms are elevated in UAE and the Philippines |
| Language not supported / translation quality | M | Meaningful given a 6-language, multi-market simultaneous launch |
| App unavailable in my country / store listing question | L-M | Relevant given the excluded-jurisdiction (US) posture |
| Right-to-left (Arabic) layout or truncation issue | L-M | Arabic-specific, narrower population |
| Accessibility barrier reported | L | Self-imposed WCAG standard, lower salience than compliance-mandated equivalents |
| Incident / status communication during degradation | L | Event-driven spike, not steady-state |
| Public social-media complaint or brand-risk post | L | Low frequency, high visibility when it occurs |

---

## Top 15 highest-expected-volume sub-issues (across all categories)

1. Deposit not yet credited — awaiting network confirmations (Cat 13)
2. "Is my money protected like a bank?" (Cat 17)
3. FSCS protection / "is my money protected?" (Cat 9)
4. PIN forgotten or blocked (Cat 2)
5. Biometric login failure (Cat 2)
6. App login failure — general (Cat 2)
7. International usage and FX rates (Cat 9)
8. Fee schedule and pricing query (Cat 9)
9. General product education / how the account works (Cat 9)
10. ID/document verification failure (Cat 1)
11. Card declined at POS — reason unknown (Cat 3)
12. Payment failure or declined payment (Cat 4)
13. 2FA/OTP not received (Cat 11)
14. Who pays network/gas fees (Cat 13)
15. Signup/application failure — technical (Cat 1)

Notice the shape: 3 of the top 3 are trust/education FAQ (fully AI/FAQ-deflectable), and most of the rest are access or onboarding friction (high self-serve or AI L1 potential per the sheet's own routing column). This mirrors the local draft's caveat — inbound *query* volume concentrates in categories with the most self-service ceiling, so this ranking is a build-priority signal, not a human-headcount forecast.

## Caveats

1. No real Ray data exists — same limitation as the local draft's category-level ranking. This should be discarded in favor of real Phase 2 data as soon as it exists.
2. Categories 13–19 have no fintech/neobank benchmark to lean on (they're Ray-specific), so those tiers carry more uncertainty than 1–12.
3. Tiers reflect *inbound query volume*, not human-handled contact volume — the sheet's own Resolution type column (App self-serve / AI L1 / FAQ / AI L1+human / Human only / Compliance) determines how much of each tier's volume actually reaches a human.
4. Flagged a likely data-quality issue in Category 9 (a row still labeled "How Braavos account works") — worth fixing directly in the sheet.

# Braavos B2C Care Issue Taxonomy

First draft. Last updated: 2026-05-21.

**Phase definitions:**
- **Phase 1** (June 2026): ~50 employees, internal pilot
- **Phase 2** (Oct 2026): ~1,000 employees, internal H2 2026 launch
- **External** (Q1 2027): Consumer-facing launch

Regulatory basis notes use "Day 1" to mean Day 1 of consumer-facing operations (External launch), not internal phases.

---

## 1. Account Opening & Verification

| Sub-issue | Ph 1 | Ph 2 | External | Regulatory basis |
|---|:---:|:---:|:---:|---|
| Signup or application failure (technical) | ✓ | ✓ | ✓ | Consumer Duty Outcome A — frictionless access to the product must exist from Day 1 |
| Signup failure due to eligibility check | ✓ | ✓ | ✓ | AML MLRs Reg 28 — KYC must be completed before onboarding; no handling path is a blocker |
| ID / document verification failure | ✓ | ✓ | ✓ | AML MLRs — identity must be verified before relationship begins; failure path must be managed |
| Biometric liveness check failure | ✓ | ✓ | ✓ | AML MLRs — liveness is part of Checkout's mandatory verification standard; failure must route somewhere |
| Full legal name mismatch or rejection | | ✓ | ✓ | AML MLRs — name match is a CDD requirement; consumer must have a resolution path |
| Date of birth verification failure | | ✓ | ✓ | AML MLRs; age-gating (18+) — unverified age = cannot proceed; need a care path |
| KYC data mismatch (bureau vs provided) | | ✓ | ✓ | AML MLRs — inconsistency is an EDD trigger; no handling path = no KYC = no onboarding |
| High-risk jurisdiction address — EDD triggered | | ✓ | ✓ | AML MLRs — EDD is mandatory before relationship begins for high-risk jurisdictions |
| PEP identified at onboarding — further info required | | ✓ | ✓ | AML MLRs — MLRO approval required before onboarding a PEP; must have a care path |
| Sanctions hit at onboarding — application rejected | | ✓ | ✓ | SAMLA / OFSI — relationship must be declined immediately; consumer notification process must exist |
| Phone number / MFA setup failure at onboarding | ✓ | ✓ | ✓ | PSD2 SCA — MFA is required for account access; failure to resolve = consumer locked out permanently |
| Application declined — no reason given | | | ✓ | Consumer Duty Outcome C — consumers must understand decisions; acceptable to handle manually at 50 employees |
| Application status enquiry | | | ✓ | Consumer Duty Outcome C — important but not a Day 1 breach if handled manually |
| Re-application after initial decline | | | ✓ | Consumer Duty Outcome C |
| Physical card not received | | ✓ | ✓ | Consumer Duty — important for experience; unlikely to arise at 50-employee internal test |
| Card activation failure (new card) | ✓ | | ✓ | Consumer Duty Outcome D — consumer must be able to use their product; manageable manually at internal scale |

---

## 2. Account Access & Authentication

| Sub-issue | Ph 1 | Ph 2 | External | Regulatory basis |
|---|:---:|:---:|:---:|---|
| PIN forgotten or blocked | ✓ | ✓ | ✓ | Consumer Duty Outcome D — consumer must be able to access their money; no resolution path = trapped funds |
| Biometric login failure (Face ID, fingerprint) | ✓ | ✓ | ✓ | Consumer Duty Outcome D — biometric is the primary access method; must be resolvable from Day 1 |
| App login failure — general | ✓ | ✓ | ✓ | Consumer Duty Outcome D |
| Locked out after failed login attempts | ✓ | ✓ | ✓ | Consumer Duty Outcome D — must have a resolution path from Day 1 |
| Lost phone — cannot access the app | ✓ | ✓ | ✓ | Consumer Duty Outcome D — rescue channel (web/phone) must exist before any consumer is onboarded |
| Account takeover — consumer suspects unauthorised access | ✓ | ✓ | ✓ | Consumer Duty; PSD2 — ATO is a security incident requiring an immediate regulated response; no-AI routing policy must be in place from Day 1 |
| Suspicious login notification received by consumer | ✓ | ✓ | ✓ | PSD2 Art. 96 — PSP must notify consumers of security breaches; consumer must have a care path |
| SIM swap concern / MFA compromise | | ✓ | ✓ | PSD2 SCA — MFA compromise is a security breach; must have handling capability from Day 1 |
| Account suspended or locked by Checkout (no context given) | | ✓ | ✓ | Consumer Duty Outcome A5 — unreasonable barriers to account access must not exist; consumer must have a path to resolution |
| Step-up authentication challenge — consumer cannot complete | | ✓ | ✓ | PSD2 SCA — step-up must be completable; failure to resolve = consumer permanently locked out |
| Device change or new phone setup | | ✓ | ✓ | Consumer Duty — important but not acute; manageable manually at 50-employee scale |
| Magic link / email login issues | | ✓ | ✓ | Consumer Duty Outcome D |

---

## 3. Card & Payment Instrument Management

| Sub-issue | Ph 1 | Ph 2 | External | Regulatory basis |
|---|:---:|:---:|:---:|---|
| Lost card | | ✓ | ✓ | Consumer Duty — consumer must be able to secure their card immediately; absence creates ongoing financial risk from Day 1 |
| Stolen card | | ✓ | ✓ | Consumer Duty; card scheme rules — immediate card restriction must be accessible from Day 1 |
| Card freeze (consumer-initiated) | ✓ | ✓ | ✓ | Consumer Duty Outcome D — immediate freeze capability must be accessible before any consumer is live |
| Card unfreeze | ✓ | ✓ | ✓ | Consumer Duty — access to own funds must be restorable from Day 1 |
| Damaged card | | | ✓ | Consumer Duty — operational; manageable at internal launch scale; must be in place for external consumers |
| Card not working — chip or contactless issue | | ✓ | ✓ | Consumer Duty — important at scale; manageable manually at 50 employees |
| Card declined at POS — reason unknown | | ✓ | ✓ | Consumer Duty Outcome C — consumer should understand why; needs process before 1000-employee phase |
| Replacement card request | | | ✓ | Consumer Duty — operational; few cards issued at internal scale; must be in place for external launch |
| Card expiry — renewal or replacement query | | | ✓ | Consumer Duty — needs a process before external consumer launch |
| Virtual card creation or management | | ✓ | ✓ | No hard regulatory timing driver; operational capability |
| Apple Pay / Google Pay setup or failure | ✓ | ✓ | ✓ | No hard regulatory timing driver |
| Card name change request | | | ✓ | No hard regulatory timing driver |
| Card spending controls — enable/disable categories | | | ✓ | No hard regulatory timing driver |
| Contactless payment limit query or issue | | ✓ | ✓ | No hard regulatory timing driver |

---

## 4. Payments & Transactions

| Sub-issue | Ph 1 | Ph 2 | External | Regulatory basis |
|---|:---:|:---:|:---:|---|
| Payment sent to wrong account — CPR initiation | | | ✓ | Payment Services Regulations — PSP must have a process to assist with misdirected payments from first transaction |
| CPR status update — funds recovery in progress | | | ✓ | PSRs — part of the CPR obligation; consumer must receive updates on their case |
| Direct debit not taken or taken incorrectly | | | ✓ | BACS Direct Debit Guarantee — consumer has a right to immediate refund; must have process from first DD setup |
| Top-up or funding failure | | | ✓ | Consumer Duty Outcome D — if consumer cannot fund account and cannot get help, the product is unusable |
| Unrecognised transaction — query before dispute intent | | ✓ | ✓ | Consumer Duty Outcome C — high-frequency at scale; manageable manually at 50 employees |
| Payment failure or declined payment | | ✓ | ✓ | Consumer Duty — important but not an acute Day 1 breach |
| Pending payment — not yet settled | | ✓ | ✓ | Consumer Duty Outcome C |
| Faster Payments / CHAPS timing query | | ✓ | ✓ | Consumer Duty — expected at scale; manageable at 50 |
| Refund not received from merchant | | ✓ | ✓ | Consumer Duty — manageable manually at small internal scale |
| Transfer limit query or limit reached | | ✓ | ✓ | Consumer Duty Outcome C |
| Standing order not executed | | ✓ | ✓ | Consumer Duty |
| Scheduled payment not executed | | ✓ | ✓ | Consumer Duty |
| Duplicate charge query | | ✓ | ✓ | Consumer Duty — query before dispute; manageable at 50 |

---

## 5. Transaction Disputes

| Sub-issue | Ph 1 | Ph 2 | External | Regulatory basis |
|---|:---:|:---:|:---:|---|
| Merchant dispute — goods not received | ✓ | ✓ | ✓ | PSRs — consumer has a statutory right to dispute; PSP must have a process from first transaction. Visa 13.1 / MC 4855 |
| Merchant dispute — item not as described | ✓ | ✓ | ✓ | PSRs; Visa 13.3 / MC 4853 |
| Merchant dispute — cancelled subscription still charged | ✓ | ✓ | ✓ | PSRs; Visa 13.2, 13.7 / MC 4853 |
| Merchant dispute — service not provided | ✓ | ✓ | ✓ | PSRs; Visa 13.7 / MC 4855 |
| Incorrect amount charged by merchant | ✓ | ✓ | ✓ | PSRs; Visa 12.5 |
| Duplicate charge by merchant | ✓ | ✓ | ✓ | PSRs; Visa 12.6 |
| Merchant error — technical duplicate | | ✓ | ✓ | Card scheme rules |
| Pre-dispute enquiry — consumer wants to contact merchant first | | ✓ | ✓ | Consumer Duty — good practice; needs structure before 1000-employee phase |
| Dispute status enquiry | | | ✓ | Consumer Duty Outcome D — consumer should not need to contact care to check status; must exist before external launch |
| Dispute outcome — consumer challenges decision | | | ✓ | Consumer Duty Outcome D; FCA DISP — must exist before external consumers are onboarded |

---

## 6. Report a Security Incident

| Sub-issue | Ph 1 | Ph 2 | External | Regulatory basis |
|---|:---:|:---:|:---:|---|
| Unauthorised transaction — CNP fraud | | ✓ | ✓ | PSRs — PSP must reimburse unauthorised transactions; reporting and investigation path required from first transaction |
| APP fraud — consumer deceived into authorising a payment | | ✓ | ✓ | PSR mandatory reimbursement (Oct 2024) — up to £85,000; 50/50 liability split; obligation applies from first transaction |
| Phishing — fraudulent email or message claiming to be Checkout | | ✓ | ✓ | Consumer Duty; PSD2 — consumer must have a route to report; liability implications from Day 1 |
| Vishing — fraudulent phone call | | ✓ | ✓ | PSR APP fraud reimbursement — phone-based scams are a primary APP fraud vector |
| Smishing — fraudulent SMS | | ✓ | ✓ | PSR APP fraud reimbursement |
| Account takeover — consumer reports it first | ✓ | ✓ | ✓ | Consumer Duty; PSD2 — must act immediately on security breach report; no-AI routing policy must be in place from Day 1 |
| Investment scam | | ✓ | ✓ | PSR APP fraud reimbursement — investment scams are covered; must have a reporting path from Day 1 |
| Romance scam | | ✓ | ✓ | PSR APP fraud reimbursement |
| Impersonation scam — fraudster posed as Checkout or another bank | | ✓ | ✓ | PSR APP fraud reimbursement; Consumer Duty |
| Recruitment scam | | ✓ | ✓ | PSR APP fraud reimbursement |
| Card-present fraud — physical card used without consent | | ✓ | ✓ | PSRs — unauthorised transaction liability obligation from first card issued |
| Account used to receive fraudulent funds — consumer unaware (money mule risk) | | | ✓ | POCA 2002 — SAR obligation; AML MLRs — must be escalated to MLRO; no care path = criminal exposure |
| Consumer reporting fraud on behalf of a vulnerable third party | | | ✓ | Consumer Duty FG21/1 — important at scale; manageable with existing fraud path at 50 employees |

---

## 7. Account Action by Checkout (Compliance-Driven)

| Sub-issue | Ph 1 | Ph 2 | External | Regulatory basis |
|---|:---:|:---:|:---:|---|
| Account frozen pending AML / TM investigation | | | ✓ | POCA 2002 s.333A — tipping-off is a criminal offence from Day 1; compliant holding messaging and tooling must be in place before any consumer account is live |
| Account frozen — PEP identified post-onboarding | | | ✓ | AML MLRs — EDD + MLRO approval required; consumer will contact care; must have a compliant handling path from Day 1 |
| Account frozen — sanctions match | | | ✓ | SAMLA / OFSI — immediate freeze obligation; tipping off prohibited; must report to OFSI; criminal liability from Day 1 |
| Account frozen — adverse media hit | | | ✓ | AML MLRs — adverse media is an EDD trigger; tipping-off prohibition applies from Day 1 |
| Account suspended — high CRA score / risk reassessment | | | ✓ | AML MLRs — firm must act on changed risk profile; holding messaging must be compliant from first suspension |
| Account suspended — velocity or TM alert | | | ✓ | AML MLRs — TM alert must be investigated promptly; consumer care must have a compliant, non-disclosing response from Day 1 |
| Transaction declined by Checkout (compliance-driven) | | | ✓ | AML MLRs — consumer must receive a response; tipping-off prohibition limits what can be said; compliant messaging from Day 1 |
| Capability limit applied (spending, top-up restricted) | | ✓ | ✓ | AML MLRs; Consumer Duty Outcome A5 — restriction without a care path = consumer harm from Day 1 |
| Consumer requests information about why account is restricted | | | ✓ | POCA 2002 tipping-off prohibition — agents must have a compliant script and tooling; absence = criminal liability exposure from Day 1 |
| Account closure initiated by Checkout | | | ✓ | PSRs — 90-day notice required from April 2026 for framework contracts; AML MLRs — consumer must be notified; must have a process from Day 1 |
| Suspected money mule — account restricted | | | ✓ | POCA 2002 — MLRO escalation mandatory; tipping-off prohibited; must have compliant care path from Day 1 |
| Account restricted — EDR triggered (change of circumstances) | | | ✓ | AML MLRs — EDR is an ongoing obligation but unlikely at 50-employee internal test; must be in place before scaling to 1000 |
| Account restricted — high-risk jurisdiction address change | | | ✓ | AML MLRs — geographic risk trigger; low frequency at 50 employees; must be in place before external scale |
| Periodic review — consumer contacted for updated information | | | ✓ | AML MLRs — periodic review is mandatory but cadenced; low frequency at internal launch; must be in place before external consumers |
| Scheme monitoring threshold breach — consumer impact | | | ✓ | Card scheme rules — very unlikely at internal scale; relevant only at significant consumer volume |

---

## 8. Account Management & Profile

| Sub-issue | Ph 1 | Ph 2 | External | Regulatory basis |
|---|:---:|:---:|:---:|---|
| Consumer-initiated account closure | ✓ | ✓ | ✓ | Consumer Duty Outcome A5 — frictionless exit must exist before any consumer is onboarded; PSRs 90-day notice from April 2026 |
| Subject Access Request (UK GDPR — personal data export) | | | ✓ | UK GDPR Art. 15 — 30-day response obligation applies from first consumer; must have a process before any consumer is onboarded |
| Data deletion / right to erasure request | | | ✓ | UK GDPR Art. 17 — applies from first consumer; must have a documented process |
| Marketing opt-out | | | ✓ | PECR — consumer right to opt out applies from first marketing communication |
| Account history / audit trail request | | | ✓ | UK GDPR Art. 15 — right of access; overlaps with SAR; must have a process from first consumer |
| Update address | | ✓ | ✓ | AML — address is a CDD data point that must be kept current; manageable manually at 50 employees |
| Update phone number | | ✓ | ✓ | PSD2 SCA — phone is an MFA device; important to manage; acceptable manually at 50-employee scale |
| Update email address | | ✓ | ✓ | Consumer Duty — manageable manually at 50 |
| Download bank statement | | ✓ | ✓ | No hard regulatory deadline; high practical importance (mortgage, tenancy); manageable at 50 |
| Update name (legal name change) | | ✓ | ✓ | Consumer Duty — important; manageable at internal launch scale |
| Account cooling-off period query | | ✓ | ✓ | Consumer Duty — must be documented and communicable before external launch |
| Third-party access setup (not PoA) | | | ✓ | Consumer Duty — important for accessibility at scale |
| Power of attorney — authorise representative | | | ✓ | Mental Capacity Act 2005; Consumer Duty — unlikely at internal launch; must be in place before external consumer volume |
| Consumer-controlled spending limits and blocks | | | ✓ | Consumer Duty — important for consumer control; manageable at internal launch scale |
| Notification preferences (push, email, SMS) | | | ✓ | No hard regulatory timing driver |
| Linked external account management | | | ✓ | No hard regulatory timing driver |

---

## 9. Product, Features & Information

| Sub-issue | Ph 1 | Ph 2 | External | Regulatory basis |
|---|:---:|:---:|:---:|---|
| How rewards / cashback accrues | ✓ | ✓ | ✓ | Consumer Duty Outcome C — reward terms must be clearly explainable to any consumer who asks; absence = misleading omission from Day 1 |
| Cashback conditions and eligibility | | ✓ | ✓ | Consumer Duty Outcome C — conditions must be transparently communicable from Day 1 |
| Fee schedule and pricing query | | | ✓ | Consumer Duty Outcome B (fair value) and Outcome C — consumers must be able to understand all fees from Day 1; inability to answer = misleading omission |
| FSCS protection — is my money protected? | ✓ | ✓ | ✓ | FCA — firms must clearly communicate FSCS status and limits; consumers will ask from Day 1 |
| Merchant exclusions for cashback | | | ✓ | Consumer Duty Outcome C — important but manageable at 50 employees with basic FAQ |
| Understanding transaction descriptions (merchant name clarity) | | ✓ | ✓ | Consumer Duty Outcome C — reduces unnecessary contacts at scale |
| How Braavos account works — general product education | | ✓ | ✓ | Consumer Duty Outcome C |
| Transfer and spending limits — what they are | | ✓ | ✓ | Consumer Duty Outcome C |
| T&Cs clarification — specific term or clause | | | ✓ | Consumer Duty Outcome C — important but manageable with basic knowledge base at 50 employees |
| How Remember Me / card saving works | | | ✓ | Consumer Duty Outcome C — relevant before RM users interact with Braavos at scale |
| Open banking / Pay by Bank — how it works | | | ✓ | PSD2 / PSR — AISP/PISP disclosure requirements; relevant before open banking features go live |
| Interest rate and savings product information | | | ✓ | Consumer Duty Outcome B — rate disclosure; relevant when savings features launch |
| Spending categories and budgeting tools | | | ✓ | No hard regulatory timing driver |
| International usage and FX rates | | | ✓ | UK-only MVP at launch; relevant when international features activate |

---

## 10. Wellbeing & Specialist Support

| Sub-issue | Ph 1 | Ph 2 | External | Regulatory basis |
|---|:---:|:---:|:---:|---|
| Financial difficulty / hardship — account support | | | ✓ | Consumer Duty FG21/1 — proactive identification and support of financially vulnerable consumers is mandatory; must have a protocol from Day 1 |
| Insufficient funds — signposting to support | | | ✓ | Consumer Duty — TCF; FCA expects proactive signposting for vulnerable consumers from first consumer contact |
| Gambling harm — gambling block request | | | ✓ | FCA — gambling block is expected as a standard feature for neobanks; absence is a Consumer Duty gap from Day 1 |
| Gambling block deactivation — cooling-off required | | | ✓ | FCA vulnerable customer guidance — cooling-off is a regulatory expectation alongside the gambling block |
| Self-harm or suicide disclosure during care interaction | | | ✓ | Consumer Duty; FCA mental health guidance (July 2023) — trained agent response and emergency escalation must exist before any consumer interaction begins |
| Modern slavery — victim or suspected victim | | | ✓ | Modern Slavery Act 2015 — duty to report; AML MLRs — MLRO escalation; Consumer Duty — must have protocol from Day 1 |
| Financial abuse — third party controlling consumer's account | | | ✓ | Consumer Duty FG21/1 — financial abuse is an explicit vulnerability driver; FCA supervisory expectation from launch |
| Domestic abuse — consumer needs account safety planning | | | ✓ | Consumer Duty FG21/1 — domestic abuse is a named vulnerability scenario; FCA has published specific guidance requiring firms to have a protocol |
| Coercive control — consumer's account used by another person | | | ✓ | Consumer Duty FG21/1 — coercive control overlaps with financial abuse; must have a handling protocol from Day 1 |
| Disability or physical impairment affecting account access | | | ✓ | Equality Act 2010 — reasonable adjustments are a legal obligation from Day 1 of any consumer-facing service |
| Debt management — referral to debt advice organisations | | | ✓ | Consumer Duty — proactive signposting to free debt advice is an FCA expectation for consumers in financial difficulty; from Day 1 |
| Mental health condition affecting account management | | | ✓ | Consumer Duty FG21/1 — health is one of the 4 FCA vulnerability drivers; acceptable to handle with existing care protocols at 50 employees |
| Addiction disclosure (non-gambling) | | | ✓ | Consumer Duty FG21/1 — addiction is a health vulnerability driver; manageable with existing vulnerable customer protocols at 50 employees |
| Bereavement — deceased person's account | | | ✓ | Consumer Duty — FCA expects sensitive bereavement handling; unlikely at 50-employee internal test; must be in place before external consumers |
| Bereavement — consumer with life-limiting condition | | | ✓ | Consumer Duty FG21/1 — life events are a vulnerability driver; manageable at internal launch scale |
| Power of attorney — account managed by legal representative | | | ✓ | Mental Capacity Act 2005; Consumer Duty — unlikely at internal scale; must be in place before external consumer volume |

---

## 11. Technical & App Issues

| Sub-issue | Ph 1 | Ph 2 | External | Regulatory basis |
|---|:---:|:---:|:---:|---|
| 2FA / OTP not received (SMS or app) | ✓ | ✓ | ✓ | PSD2 SCA — step-up authentication must be completable; failure to resolve = consumer permanently locked out |
| In-app chat not loading or connecting | ✓ | ✓ | ✓ | Consumer Duty Outcome D — in-app chat is the primary care channel; if broken with no fallback, consumers cannot get help |
| App crash or instability | | ✓ | ✓ | Consumer Duty Outcome D — app must be available; single-instance crashes at 50 employees are manageable without a formal process |
| Feature not working or loading | | ✓ | ✓ | Consumer Duty Outcome D |
| App blank screen or not opening | | ✓ | ✓ | Consumer Duty Outcome D |
| Push notification not received | | ✓ | ✓ | Consumer Duty Outcome C — proactive notifications are part of the consumer understanding obligation; important before external scale |
| Biometric setup failure (technical) | | ✓ | ✓ | Consumer Duty — important for access; manageable at 50-employee scale |
| App update required — old version blocking access | | ✓ | ✓ | Consumer Duty Outcome D — consumer must be able to access their account |
| Device compatibility or OS version issue | | ✓ | ✓ | Consumer Duty — important at scale |
| Error message — unclear or unexplained | | ✓ | ✓ | Consumer Duty Outcome C — plain language is required; manageable with basic knowledge base at 50 employees |
| Diagnostic information collection — engineering escalation | | ✓ | ✓ | No regulatory timing driver; important for product quality |
| Transaction history not loading or displaying incorrectly | | ✓ | ✓ | Consumer Duty — consumer must be able to review their account |
| App performance — slow or unresponsive | | ✓ | ✓ | Consumer Duty Outcome D |
| Statement download failure (technical) | | | ✓ | No hard regulatory timing driver; operational |
| Apple Pay / Google Pay technical setup failure | | | ✓ | No hard regulatory timing driver |

---

## 12. Formal Complaints (FCA DISP — Escalation State)

| Sub-issue | Ph 1 | Ph 2 | External | Regulatory basis |
|---|:---:|:---:|:---:|---|
| Formal complaint — any issue in Categories 1–11 the consumer is dissatisfied with | | ✓ | ✓ | FCA DISP — complaint handling process (5-day acknowledgement, 8-week resolution) applies from the first consumer; cannot onboard without a documented, Legal-reviewed complaint process |
| Financial redress — credit to consumer account following upheld complaint | | ✓ | ✓ | FCA DISP — if complaint is upheld and redress is owed, we must be able to issue it; no tooling path = regulatory breach |
| FOS referral — consumer exercises escalation right | | ✓ | ✓ | FCA DISP — consumer must be informed of FOS rights from Day 1; FOS decisions are binding up to £375,000 |
| Complaint about complaint handling (meta-complaint) | | | ✓ | FCA DISP — the complaint process itself must meet regulatory standards; important before external launch |

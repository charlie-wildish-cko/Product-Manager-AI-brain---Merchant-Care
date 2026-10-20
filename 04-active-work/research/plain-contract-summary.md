# Plain contract summary for VP Engineering and VP Product

**Strategic anchor:** Support platform vendor decision (Plain recommendation). Supports `support-platform-vendor-scorecard.md` and `zendesk-decision-deck-content.md`. Source: Plain Terms of Service, DPA and SLA templates (effective 24 March 2026), reviewed 2026-10-02.

**Bottom line:** these are Plain's standard template terms, and they favour Plain. The 99.95% uptime headline is real, but the remedy for missing it is weak. Plain can also end the contract on 30 days' notice. Before we commit to a core platform migration, negotiate the points under "Asks to raise" below.

All three documents are templates published under Not Just Tickets Ltd (Plain), under English law.

## SLA (for VP Eng)

| Item | What the document says |
|---|---|
| Uptime commitment | 99.95% per calendar month, which is about 22 minutes of downtime a month |
| What counts as downtime | Only a full outage where the Subscriber "is unable to access or use the Service". Degraded performance, partial outages and API-only or email-only failures are not defined as downtime |
| Excused downtime | Scheduled maintenance with 7 days' notice, third-party network or ISP failure, third-party software issues, force majeure (which includes ISP failure and denial of service attacks) |
| Credits | Claim-based. We submit a written claim and Plain issues a credit note, payable within 30 days |
| Credit tiers | Above 99.8%: **0**. 97-99.8%: 1% of that month's fees. 95-97%: 2%. Below 95%: 3%. Stated cap is 10% |
| Sole remedy | Credits are the exclusive remedy for missing the SLA (para 4.5) |
| Support channel | Email only (help@plain.com) |
| Support hours | 05:00-21:00 on London banking days |
| P0 incident response | **Response within 24 hours**. There is no resolution target |
| P0 definition | Full outage, recurring complete outages, or a data security incident |

**Issues for Eng:**
- **The commitment and the remedy don't match.** The promise is 99.95%, but credits only start below 99.8%. That leaves roughly 86 minutes of downtime a month (30-day month) with no remedy.
- **Credits are small.** The most the table pays is 3% of one month's fees, even for a month that is mostly down. The 10% cap can't be reached from the table.
- **24 hours to respond to a total outage is weak** for a tool our support operation depends on. There are no P1-P3 tiers, no resolution targets, no RCA commitment and no phone or Slack escalation.
- **Support hours** do not cover weekends or non-London time zones.
- **Maintenance windows:** "weekends where practicable" is a preference, not a commitment. There is no cap on scheduled downtime.
- **Terms clause 6.1** separately says only "commercially reasonable endeavors" for 24/7 availability. The SLA must be named in our order form or it may not bind.
- **Not in these documents:** RTO/RPO, backup and DR, status page, pen-test cadence, data residency. Plain points to its Trust Center (trust.plain.com) for security controls, and we have not reviewed it.

## Terms of Service (for both)

**Commercial risk (VP Product):**
- **Plain can terminate for convenience on 30 days' notice** (10.3), with a refund of prepaid fees. For a core platform replacing Zendesk, this is the biggest exposure.
- **Auto-renews** for the same period unless we give 30 days' notice.
- **Fees can change on 30 days' notice** with no cap (5.6).
- **Plain can amend the Terms** on 30 days' notice. Continued use counts as consent (16.9).
- **Features can be removed.** The licence is explicitly not tied to future roadmap (2.2, 2.3).
- **Change of control:** Plain can terminate if Checkout were acquired by a Plain competitor.

**Liability and legal (both):**
- Plain's liability is capped at **12 months of fees**. It excludes loss of profit and revenue, and **loss or corruption of data**.
- There is no carve-out for data breach, confidentiality breach or DPA breach. Only death, fraud and illegal exclusions are carved out.
- Claims must be notified within 12 months.
- We indemnify Plain for our data and for breaches of the Terms. Plain indemnifies us only for IP infringement claims.

**Data (both):**
- We own our data. Plain gets an irrevocable right to create **aggregated, anonymised** insights from it (4.3). Plain also owns usage statistics.
- **No AI training on our data without written consent** (4.5), and the same applies to personal data under DPA 3.3. This protects us for Fin-style AI features.
- We warrant that we use "reasonable endeavors" to keep **sensitive personal data** out of the platform (4.2). As a PSP, tickets can contain PANs, bank details or ID documents, so this needs a position from Security.
- **Exit:** we may not be able to recover data after termination, and the Terms recommend we keep our own backups (4.2). There is no export format or timeline. Deletion is by email request, and some data is retained (10.4).
- Plain staff can access and impersonate our account for support. The DPA says this is logged and audited.

## DPA (for VP Eng, with Legal and Security)

- **Roles:** Plain is the processor and we are the controller. Processing is only on our documented instructions.
- **Sub-processors:** the list is published in Plain's Trust Center. New ones get 7 days' notice. We can object, but if Plain can't resolve it, Plain can terminate without liability. The objection right is weak in practice.
- **Transfers:** EU Standard Contractual Clauses (Modules 2 and 4) with Irish law, plus the UK IDTA with English law. There is **no data residency or EU-hosting commitment**.
- **Breach notification:** "without undue delay". There is no hour-based commitment (such as 24 or 72 hours), and Plain gives breach detail "to the extent available".
- **Audit:** annual SOC 2-style third-party audit. We get the report. We can audit directly only if the report doesn't satisfy us, once a year, and extra audits are chargeable.
- **Deletion or return** at the end of processing, at our choice.
- **Assistance** with data subject requests, DPIAs and breach notifications.
- **AI:** no use of customer personal data to train shared models. Third-party AI providers count as sub-processors.
- **US:** CCPA/CPRA no-sell and no-share commitment.

## Asks to raise with Plain

1. Remove termination for convenience, or extend notice to 6-12 months with a data export and transition period.
2. Align the credit threshold with the 99.95% commitment, and count degraded performance and API failures as downtime.
3. Add a P0 response of 1 hour (or similar), a resolution target and RCA commitments, plus 24/7 coverage for P0.
4. Add a super-cap or separate cap for data breach, DPA breach and confidentiality breach.
5. Add a breach notification window in hours, EU data residency if we need it, and a defined data export on exit.
6. Cap fee increases.
7. Have Legal confirm what a regulated PSP needs beyond a standard template: regulator audit and access rights, outsourcing and exit provisions, and any DORA requirements. None of that appears in these documents.

## Questions for Plain (from VP Eng comments, 2026-10-07)

**To send to Plain:**
1. Provide historic uptime for the last 6-12 months, measured the way the SLA defines it, with any incident history.
2. Is there a limit on the number and length of scheduled maintenance windows per month or year? Does maintenance count toward the 99.95%?
3. Define P0, P1, P2 and P3 with response and resolution targets for each. The SLA only defines P0 and gives a 24-hour response.
4. Will Plain agree a custom SLA for Checkout: 1-hour P0 response, 24/7 P0 coverage, resolution targets and RCA commitments?
5. Provide RTO, RPO, backup and DR, status page, pen-test cadence and data residency details, plus the Trust Center security controls and sub-processor list.
6. Confirm the scope of Eric Weiss's uptime commitment (99.95% as drafted, or a changed threshold and remedy) and put it in the order form.
7. Remove termination for convenience, or extend notice, with a data export and transition period.
8. Credits that start below 99.95%, with degraded performance and API failures counted as downtime.
9. Liability super-cap for data breach, DPA breach and confidentiality breach.
10. Breach notification in hours, EU residency option, defined data export on exit, fee increase cap.

**Internal actions (not for Plain):**
- Has Plain due diligence gone through InfoSec? (Hélder)
- What is Zendesk's current SLA agreement, so we have a baseline? (Fraser Bryant)
- Termination for convenience: Hélder notes this does not work for us. Confirm the contract is still with Procurement and route the ask there.
- Hélder is happy to join the Plain calls on custom SLAs.

## Plain responses

| Ask | Status | Source |
|---|---|---|
| 1. Termination for convenience | Open | |
| 2. Uptime and credits | Plain "happy to commit to uptime". Scope unconfirmed: unclear whether this is 99.95% as drafted or a changed threshold or remedy. Not yet in writing | Eric Weiss (Sales), form of communication TBC |
| 3. P0 response and 24/7 | Open | |
| 4. Liability super-cap | Open | |
| 5. Breach window, residency, data export | Open | |
| 6. Fee increase cap | Open | |
| 7. Regulated PSP provisions (Legal) | Open | |

A Sales commitment binds Plain only once it appears in the order form or a signed amendment. Get the SLA named in the order form and the credit schedule written out.

## Open items

- Legal and Security have not reviewed these. This is a read of the templates, not legal advice.
- The Terms contain cross-reference errors (survival clause, notices), so Legal should check the numbering.
- The Trust Center content was not provided.

# Care: Reconciliation issues with Balances

**Date:** 2026-07-14  
**Attendees:** Charlie Wildish (PM, Merchant Care), Francisco Goncalves (L2 support lead), Alexa Stein, Bryan Watt, Patrick Kohler (invited); Sawan Badooa (dropped: APM reconciliation, not relevant)  
**Drive source:** 1tBGqFXLZsmir7nn4HC-8LwQ_J29j_Z70U0mxGoF2lRE

## Context

Working session between Charlie and Francisco's L2 team to find the root cause of high-cost reconciliation support and how to reduce the effort spent on it. L2 handles the complex financial cases (Babak, Angelica) that L1 cannot resolve with standard procedures.

## Key Points

**Volume and cost of L2 reconciliation work**
- Reconciliation and financial discrepancy tickets are ~30% of all volume Francisco's team handles.
- "Funds and fees" is 52% of everything that reaches L2 (over 6 months of data). Company-wide, funds and fees is ~10% of total weekly volume; payments is 50-60%.
- These are exceptions-on-exceptions: agents manually download CSVs and financial action reports, then match against invoices to find discrepancies.
- Cost data is now applied across all tickets based on operational cost. A ticket escalated to L3 (engineering) is ~10x the cost. Technology cost not yet included, which would push figures higher.

**Top L2 issue drivers (6 months)**
- Reconciliation (top reason), fee questions (why charged / amount charged), missing settlements, negative balance explanations, data mismatches, SFTP config issues, non-standard/custom report requests, and requests for data up to 7 years old.
- Negative balance is a recurring source of merchant confusion. Refunds are a top issue across the board, not just financial cases.
- Many labelled issues are inter-related: a negative balance can be driven by minimum billing or a recon issue upstream, so the taxonomy label is not always the true cause.

**Settlement ID root cause**
- Merchants cannot identify their transactions on the dashboard because there is no settlement ID: the dashboard currently *infers* it.
- Foundational re-architecture of how financial actions and data are stored is in flight (Adam's work), to enable accurate settlement ID linking.
- Targeted resolution for accurate settlement ID display on the dashboard: Q4 2026.

**Reporting is an explanation problem, not always a defect**
- Card payouts report reflects gateway events (when a payout was requested), not balance impact (when the balance moved). The timing gap creates an unavoidable discrepancy merchants cannot reconcile.
- Charlie's view: this is a communication/explanation gap, not a systemic reporting defect. Fix is better explanation in reporting, not a structural change.

**Fee query driver**
- Fee inquiries often come from a new finance-team member who lacks access to the original contract and cannot see which fees were contracted.
- Joe is building a custom fees dashboard. Risk flagged: it could increase fee-detail tickets if the dashboard illustrates fees differently from the CSV, even though both draw from the same source. Team is building it against a curated API that does not interpret data, to avoid this.

**Strategy to reduce L2 volume**
- Two-pronged: fix the product/reporting issue directly, or add self-service documentation/knowledge that AI (Fin) can use for initial triage before a ticket reaches L2.
- Old north star (a taxonomy count tied to reporting) was dropped: reporting incidents happened without case counts moving, so the metric was not signalling performance.
- Immediate action: narrow the analysis to the top two categories (reconciliation and fee detail) rather than the long tail.
- Reflex interface flagged as the future mechanism: beta targeted for end of July 2026. Goal is to give teams like Francisco's an actionable, self-serve data view instead of manual scrubbing, and to track impact of fixes over time.

## Insights

- The single largest L2 cost concentration is "funds and fees" at 52% of escalated volume. Any contact-reduction effort for L2 should start here, and specifically with reconciliation and fee-detail sub-issues.
- Settlement ID is a confirmed structural gap with a committed Q4 2026 fix via the financial-data re-architecture. This is the clearest product lever against reconciliation contacts. Verify the Q4 date against `2026 deliverables.md` before citing it in any downstream doc.
- Not all reporting contacts are fixable at the product layer: the payout-request-vs-balance-impact timing gap is inherent and needs a knowledge/explanation fix, not an engineering one. This is a good candidate for Fin knowledge content.
- L2 taxonomy labels understate the true root cause because issues chain (negative balance → minimum billing / recon). Clustering ticket content rather than trusting the taxonomy is the more reliable analysis method, which is what Reflex is being built to do.
- The SMB scaling argument is explicit: enterprise can absorb ongoing manual support, but SMB volume "will kill us very quickly" without deflection. Reconciliation self-service matters more as the SMB base grows.
- Cost-per-ticket data now exists operationally and shows the 10x L3 escalation multiplier: usable for framing the investment case on reconciliation fixes.

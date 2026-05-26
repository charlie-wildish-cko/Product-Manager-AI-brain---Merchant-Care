# Workspace Review — 2026-05-26

## Summary

47 files reviewed in `04-active-work/` (root) + 9 PRDs in `roadmap-items/`.

**Verdicts**: 30 keep · 5 update · 17 archive · 4 delete

The bigger issue surfaced by this review: the root of `04-active-work/` mixes finished strategy docs, active PRDs, working data files, response scripts, onboarding docs, and ad-hoc analysis. Subfolder structure (proposed earlier) will solve discoverability more than archiving alone.

---

## Verdicts

### Delete (4)

| File | Rationale |
|---|---|
| `04-active-work/.DS_Store` | macOS metadata; should be gitignored |
| `04-active-work/classification-qa-2026-05-18.tsv` | Superseded by `classification-qa-2026-05-22.tsv` (same data, 4 days newer) |
| `04-active-work/payout-details-fields.csv` | Duplicate of `.tsv` version (same data, alternate format); keep one |
| `04-active-work/standard-email-off-ramp-merchant-comms.md` | Duplicate of older `20250709 - Tier 4 Merchant Care changes...` comms template; the Tier 4 doc is the canonical version |

### Archive (17)

These are completed, superseded, or one-off docs worth preserving as history but no longer active work.

| File | Target | Rationale |
|---|---|---|
| `04-active-work/20250709 - Tier 4 Merchant Care changes - Dashboard users.docx.md` | `05-archive/2026/investigations/` | 2025 merchant comms template; Tier 4 work shipped Aug 2025 |
| `04-active-work/Care product strategy inputs.md` | `05-archive/2026/strategies/` | Intake form for strategy doc; superseded by `care-product-strategy-2026-2030.md` |
| `04-active-work/Zendesk Viability_ AI, Pricing, Market.md` | `05-archive/2026/investigations/` | Research dump; superseded by `zendesk-platform-decision-rfc.md`. Q3–Q4 deliverable references the RFC, not this |
| `04-active-work/care-future-vision-business-case.md` | `05-archive/2026/strategies/` | March 2026 working draft; superseded by `care-strategy-2026-2030.md` (April) and `care-product-strategy-2026-2030.md` |
| `04-active-work/data-engineer-intro.md` | `05-archive/2026/investigations/` | Onboarding doc — belongs in `01-knowledge-base/processes/onboarding/` long-term, but is one-off content not active work |
| `04-active-work/engineering-onboarding-care-product.md` | `05-archive/2026/investigations/` | Same as above — onboarding doc, not active work |
| `04-active-work/knowledge-manager-intro.md` (in `stakeholder-updates/`) | `05-archive/2026/investigations/` | Intro doc for stakeholder relationship now established |
| `04-active-work/merchant-segments-and-involvement-rate-summary.md` | `05-archive/2026/investigations/` | COO/CPO briefing artefact from Fin involvement rate planning; the PRD in roadmap-items is the live doc |
| `04-active-work/research on AI support operating model.md` | `05-archive/2026/investigations/` | One-off research dump (Klarna case study etc.); content distilled into strategy docs |
| `04-active-work/standard-email-off-ramp-plan.md` | `05-archive/2026/investigations/` | Feb 2026 plan; needs decision on whether still active under Replace Webform with Fin (Q3) |
| `04-active-work/stakeholder-updates/merchant-care-b2c-briefing.md` | `05-archive/2026/investigations/` | March 2026 briefing; superseded by `braavos-care-scoping.md` + `braavos-care-h2-build-plan.md` |
| `04-active-work/strategic-review-knowledge-data-graph-2026-04-20.md` | `05-archive/2026/strategies/` | Strategic review output; recommendations folded into knowledge-graph-phase1 work |
| `04-active-work/support platform flows.md` | `05-archive/2026/strategies/` | April 2026 working notes; content folded into `care-product-model-2030-mapping.md` |
| `04-active-work/fin-data-access-briefing.md` | `05-archive/2026/investigations/` | March 2026 briefing; superseded by `fin-data-access-backlog.md` (the live Confluence-synced doc) |
| `04-active-work/Taxonomy - ZD work - Case & Issue Type - References.csv` | `05-archive/2026/data-exports/` | Q1 taxonomy mapping work — completed |
| `04-active-work/Taxonomy - ZD work - New taxonomy.csv` | `05-archive/2026/data-exports/` | Q1 taxonomy mapping work — completed |
| `04-active-work/Fin involvement & resolution rate simple plan.md` | `05-archive/2026/strategies/` | March 2026 plan doc; the live artefact is `roadmap-items/fin-involvement-rate-prd.md` |

### Update (5)

Topic still active but content has stale references.

| File | What needs updating |
|---|---|
| `04-active-work/missing-response-codes.tsv` | Verify whether still in active use for payment-code-definitions work |
| `04-active-work/payment-code-definitions.md` | Last edited April; check completeness against current Agent Consultant Q2 work |
| `04-active-work/dispatch-email-cleanup-scoping.md` | Q2 deliverable — check status; some items may now be complete |
| `04-active-work/agent-consultant-prd.md` | PRD against current template (Apr 9); Q2 actions may have shifted |
| `04-active-work/h2-engineering-planning-2026.md` | Living planning doc — confirm last updated date matches reality |

### Keep (30)

Tied to active Q2/Q3/Q4 2026 deliverables; content current.

**Strategy & vision (always keep)**
- `04-active-work/README.md`
- `04-active-work/care-product-strategy-2026-2030.md`
- `04-active-work/care-strategy-2026-2030.md`
- `04-active-work/care-product-model-2030-mapping.md`
- `04-active-work/agent-consultant-vision.md`

**Active deliverables**
- `04-active-work/braavos-care-scoping.md` (Q4 — Consumer Support Braavos)
- `04-active-work/braavos-care-h2-build-plan.md` (Q4 — Consumer Support Braavos)
- `04-active-work/consumer-care-capabilities-ownership.md` (Q4 — Consumer Support Braavos)
- `04-active-work/reflex-phased-plan.md` (Q1→Q4 — Reflex)
- `04-active-work/reflex-ui-fields.md` (Q2 — Reflex)
- `04-active-work/fin-data-access-backlog.md` (Q2/Q3 — AI First Resolution / Fin Procedures)
- `04-active-work/fin-email-behaviour-spec.md` (Q2/Q3 — Fin email)
- `04-active-work/fin-outage-check-responses.md` (Q2 — Fin Procedures)
- `04-active-work/fin-user-management-responses.md` (Q2/Q3 — Fin Procedures)
- `04-active-work/action-type-definitions.md` (Q3 — Knowledge & Data Graph)
- `04-active-work/knowledge-graph-layer-one-pager-preethy.md` (Q3 — Knowledge & Data Graph)
- `04-active-work/knowledge-graph-phase1-entity-taxonomy.md` (Q3 — Knowledge & Data Graph)
- `04-active-work/zendesk-platform-decision-rfc.md` (Q3→Q4 — Help Desk Platform Evaluation)

**Reference data (active use)**
- `04-active-work/user-management-api-endpoints.csv`
- `04-active-work/user-management-api-fin-mapping.csv`
- `04-active-work/visionnotify-api-endpoints.csv`
- `04-active-work/payment-details-fields.csv`
- `04-active-work/payout-details-fields.tsv`
- `04-active-work/payment-search-spec.yaml`
- `04-active-work/classification-qa-2026-05-22.tsv`

**Subfolders (always keep contents)**
- `04-active-work/roadmap-items/` — all 9 PRDs (active deliverables)
- `04-active-work/merchant-interview-transcripts-2025/` — primary research

---

## Subfolder Reorganisation Proposal

After cleanup, propose this structure for what remains:

```
04-active-work/
├── README.md
├── prds/                          ← move all 9 from roadmap-items/ here
│   ├── agent-consultant/
│   │   ├── prd.md
│   │   └── vision.md
│   ├── braavos-care/
│   │   ├── scoping.md
│   │   ├── h2-build-plan.md
│   │   └── capabilities-ownership.md
│   ├── reflex/
│   │   ├── prd.md
│   │   ├── phased-plan.md
│   │   └── ui-fields.md
│   ├── fin-involvement-rate/
│   ├── fin-email-auth-data-policy/
│   ├── blue-emi-zendesk-support/
│   ├── zendesk-jira-integration/
│   ├── zendesk-org-domain-mapping/
│   ├── zendesk-salesforce-integration/
│   └── dispatch-email-cleanup/
├── strategy/                      ← long-horizon docs
│   ├── care-strategy-2026-2030.md
│   ├── care-product-strategy-2026-2030.md
│   └── care-product-model-2030-mapping.md
├── research/                      ← active research feeding into PRDs
│   ├── zendesk-platform-decision-rfc.md
│   ├── knowledge-graph-phase1-entity-taxonomy.md
│   ├── knowledge-graph-layer-one-pager-preethy.md
│   ├── action-type-definitions.md
│   ├── fin-data-access-backlog.md
│   ├── fin-email-behaviour-spec.md
│   ├── fin-outage-check-responses.md
│   ├── fin-user-management-responses.md
│   ├── payment-code-definitions.md
│   └── h2-engineering-planning-2026.md
├── working-files/                 ← CSVs, TSVs, specs (data artefacts)
│   ├── user-management-api-endpoints.csv
│   ├── user-management-api-fin-mapping.csv
│   ├── visionnotify-api-endpoints.csv
│   ├── payment-details-fields.csv
│   ├── payout-details-fields.tsv
│   ├── payment-search-spec.yaml
│   ├── classification-qa-2026-05-22.tsv
│   └── missing-response-codes.tsv
├── stakeholder-updates/           ← keep as-is
└── merchant-interview-transcripts-2025/  ← keep as-is
```

After cleanup + reorg: ~5 things at root, each clearly named, PRDs instantly findable.

---

Report saved to `04-active-work/workspace-review-2026-05-26.md`.

**Ready to execute (Phase 4):**
- Delete 4 files
- Move 17 files to `05-archive/2026/`

**Reorganisation (separate step):** Move surviving files into the proposed subfolder structure above.

Confirm? Type **yes archive** to do the archive+delete only, **yes all** to also do the reorg, or **no** to stop here.

# Zendesk Organisation Domain Mapping

**Status**: Draft  
**Owner**: Charlie Wildish  
**Last Updated**: February 2026  
**Stakeholders**: Care Operations, Operational Excellence, Zendesk Admins, Merchant Experience


## Executive Summary

Primary identification is Salesforce or Dashboard lookup. When that fails, domain mapping is the **fallback**: match the user’s email domain to configured org records and auto-assign. This PRD covers implementing and embedding domain mapping for Premium and Enterprise (Care Success Plan), with minimal ongoing overhead. Standard is out of scope.


## Problem

**What problem are we solving, and who has it?**  
When Salesforce/Dashboard lookup fails, Premium/Enterprise users land unassigned — manual triage, misrouting, wrong SLA. Affects: CX agents (manual assign), Care Ops/Op Ex (degraded reporting), Zendesk admins (routing depends on org), merchants (slower/wrong routing).

**How are they solving it today?**  
No system. Domain mapping exists in Zendesk but isn’t standard; some orgs have domains set ad hoc, many don’t.

**Why solve this now?**  
New orgs (e.g. Blue EMI) and routing logic increase reliance on org assignment. Embedding domain mapping at org creation prevents the gap growing and stabilises routing and reporting.


## Goals & Success Metrics

| Metric | Current State | Target | Timeline |
| --- | --- | --- | --- |
| % of Premium/Enterprise Zendesk orgs with at least one domain configured | Unknown (estimated low) | 100% of ~500 orgs (100 Premium, 400 Enterprise) | 3 months post-launch |
| % of new Premium/Enterprise end-users auto-assigned to an org at creation | Unknown | >90% (allowing for shared/generic domains) | 3 months post-launch |
| Manual org-assignment actions by agents per week (Premium/Enterprise tickets) | Baseline TBC | Measurable reduction vs baseline | 3 months post-launch |
| % of new Premium/Enterprise orgs created with domain configured at point of creation | N/A | 100% | Ongoing from rollout |


## User Stories

### CX Admin: Creating a new organisation

**As a** CX admin setting up a new Premium or Enterprise merchant organisation in Zendesk,  
**I want** a clear, mandatory step to add the merchant's email domain(s) to the org record,  
**So that** all future users from that domain are automatically assigned without manual follow-up.

**Acceptance Criteria**:

- Org creation process (runbook/checklist) explicitly includes a domain mapping step
- Domain field is populated before the org is marked as ready for use
- Multiple domains can be recorded where a merchant uses more than one (e.g. trading name and parent company)


### CX Agent: Receiving a ticket from an unassigned user

**As a** CX agent handling a ticket from a user with no organisation assigned,  
**I want** this to be an exception rather than the norm,  
**So that** my time is spent resolving tickets rather than investigating merchant identity.

**Acceptance Criteria**:

- The volume of tickets from unassigned users is measurably reduced after domain mapping rollout
- Where a user is unassigned (e.g. generic domain, new merchant not yet onboarded), there is a documented triage path for agents


### Care Operations / Operational Excellence: Running org-level reports

**As a** Care Operations or Operational Excellence manager reviewing support volume and SLA performance by organisation,  
**I want** user-to-org assignment to be accurate and complete,  
**So that** my reports reflect reality and I can hold the right conversations with merchant-facing teams.

**Acceptance Criteria**:

- Org-level reporting shows materially fewer "unassigned" users after rollout
- Quarterly audit process provides a point-in-time check on mapping coverage

**Edge cases**:

- **Shared/generic domain (e.g. gmail.com, outlook.com)**: These must never be mapped to an org — exception list maintained and checked during org setup.
- **Merchant uses multiple domains**: Multiple domains can be added to a single org record (space or comma separated). Onboarding step should prompt for all known domains.
- **Same domain claimed by two orgs**: Zendesk enforces uniqueness — escalate to Care Operations / Operational Excellence to agree correct assignment before org creation.
- **Multi-entity merchant (same contact, multiple orgs)**: Domain mapping assigns users to one org. Where a contact spans multiple Checkout entities (e.g. a merchant with both a Checkout and Blue EMI account), domain mapping alone is insufficient — org assignment must be driven by explicit identifiers (e.g. Client ID). These merchants are documented in the exception list.
- **Existing unassigned users**: Domain mapping only fires at user creation. A backlog of unassigned users from known domains requires a one-time bulk assignment process (see Approach).


## Requirements

#### Must Have (P0)
- Domain mapping step added as a required item in the Zendesk org creation runbook/checklist
- Exception list documenting: (a) domains deliberately not mapped, (b) multi-entity merchants where domain mapping is insufficient
- One-time bulk assignment of existing unassigned users whose email domains match a configured org
- Quarterly audit process (saved Zendesk user view or lightweight script) to surface unassigned users from mapped domains

#### Should Have (P1)
- CRM (Salesforce or equivalent) used as source of truth for domain field — admin populates from existing account data rather than entering freehand
- Internal documentation covering: how to add a domain to an org, what to do with unmappable domains, multi-entity handling
- Alert or view in Zendesk surfacing newly created users with no org (for ongoing monitoring)

#### Nice to Have (P2)
- Automated sync: when a new org is created in Zendesk (or CRM), domain is populated from account data without manual entry
- Periodic automated report (e.g. monthly) showing unassigned user count and trend over time

**Constraints**:
- **Accuracy**: Domain mapping must not assign users to incorrect orgs — the exception list must be checked before any domain is configured
- **Consistency**: The domain mapping step must be applied uniformly across all new Premium and Enterprise org creation, not selectively
- **Maintainability**: The process must be light enough that it is followed reliably without dedicated resourcing — overhead should be minutes per org, not hours


## Approach

### User Identification Hierarchy

Org assignment follows a two-level order of precedence. Domain mapping only fires as a fallback when primary identification has not already assigned the user.

```
1. PRIMARY — Salesforce or Dashboard
   Check whether a record exists for this user in either Salesforce or the
   Merchant Dashboard. If found in either, org assignment is set from that record.
   → If found in Salesforce or Dashboard: org assigned — domain mapping does not fire
   → If not found in either: proceed to fallback

2. FALLBACK — Domain mapping
   User's email domain is checked against domains configured on Zendesk org records
   → If domain matches: user is automatically assigned to that org
   → If no match: user remains unassigned — manual triage required
```

This hierarchy is enforced naturally by Zendesk's behaviour: domain mapping does not override a user who is already assigned to an org. If Salesforce or Dashboard has already set the org, domain mapping will not interfere.

### Principle

Require domain at org creation; the creator has the context. Near-zero overhead, fallback always in place.

### Org Creation Flow (with domain mapping embedded)

```
1. Admin receives instruction to create a new org in Zendesk (e.g. new merchant onboarded)
2. Admin creates org record in Zendesk
3. Admin checks exception list: is this domain on the do-not-map list?
   - Yes → leave domain field blank, note reason on org record
   - No → proceed
4. Admin adds primary email domain(s) to the Domains field on the org record
   - Format: domain only, no @ prefix (e.g. "sony.com")
   - Multiple domains: space or comma separated
5. Admin marks org as ready; domain mapping is now live for future users
```

### Bulk Backfill Flow (one-time)

```
1. Export list of Zendesk users with no organisation assigned
2. For each user, check if their email domain matches a configured org
3. Bulk-assign matched users to the correct org via Zendesk admin UI or API
4. Document unmatchable users (generic domains, unknown merchants) for agent awareness
```

### Quarterly Audit Flow

```
1. Run saved Zendesk view: Users → No organisation → Created in last 90 days
2. Review: are unassigned users from domains that should have been mapped?
   - Yes → investigate: was the org created without a domain? Fix the org record, bulk-assign user
   - No → expected (generic domain, new merchant not yet in Zendesk) — no action required
3. Review exception list: any entries now out of date? (e.g. multi-entity merchant now resolved)
4. Log audit completion and findings
```

### Exception List Structure

A maintained document (or Zendesk org tag) recording:

| Domain | Reason not mapped | Owner | Review date |
| --- | --- | --- | --- |
| gmail.com | Shared consumer domain — never map | Care Ops / Op Ex | Permanent |
| outlook.com | Shared consumer domain — never map | Care Ops / Op Ex | Permanent |
| [merchant].com | Multi-entity merchant — org set by Client ID trigger, not domain | Care Ops / Op Ex | Review at next merchant config change |

### Zendesk Configuration

- **Domain field on Organisation**: Native Zendesk field (`domain_names`). No custom field or configuration required — this is built-in functionality.
- **How to add via UI**: Admin > Organisations > [Org name] > Domains field > enter domain > Save
- **How to add via API**:
  ```
  PUT /api/v2/organizations/{id}
  { "organization": { "domain_names": ["sony.com"] } }
  ```
- **Bulk user assignment via API**: Query users by email domain, PATCH `organization_id` on matched records

### Behaviour Confirmed

- Domain mapping fires **at user creation only** — it does not retroactively update existing users
- Users already assigned to an org (e.g. via Salesforce or Dashboard identity) are **not overridden** by domain mapping — this is what makes it a safe fallback
- A domain can only be assigned to **one organisation** — Zendesk enforces uniqueness
- Mapping `sony.com` does **not** cover subdomains (e.g. `corp.sony.com`) — subdomains must be added explicitly if needed

### Tooling Needed

- Saved Zendesk user view for quarterly audit: filter by `organisation = none`, `created > 90 days ago`
- (Optional) Simple script for bulk backfill — can use Zendesk Users API with domain filter


## Out of Scope

- Standard tier (deliberate); automated org creation at onboarding; routing/SLA logic changes
- Multi-entity handling beyond exception list (see Blue EMI PRD); Consumer/B2C


## Launch Plan

- **Phase 1 — Audit & Exception List**: Review existing Zendesk orgs for Premium and Enterprise merchants; identify which have domains configured and which do not. Draft the exception list for shared/generic and multi-entity domains. Estimated effort: 1–2 days (Care Operations / Operational Excellence).
- **Phase 2 — Backfill Existing Orgs**: Add domain fields to all active Premium/Enterprise org records that do not have them (~500 orgs total). A bulk API update from CRM data is strongly preferred over manual UI entry at this volume. Estimated effort: 1 day (including data preparation and validation).
- **Phase 3 — Bulk User Assignment**: Run one-time backfill to assign existing unassigned users (from Premium/Enterprise orgs) to matching orgs. Estimated effort: 0.5 day (mostly automated).
- **Phase 4 — Process Embedding**: Update org creation runbook/checklist. Brief Care Operations and Operational Excellence teams. Document: how to add a domain to an org, triage path for unassigned users, agent guidance, exception list ownership. Estimated effort: 0.5 day.
- **Phase 5 — First Quarterly Audit**: Run 90 days after Phase 4; confirm process is being followed and catch any gaps.

**Rollback**: Additive. Remove domain → no future auto-assign; wrong assignments fixed manually. No trigger/routing changes; low risk.


## Risks, Dependencies & Open Questions

**Dependencies**:

| Dependency | Owner | Status | Risk if Delayed |
| --- | --- | --- | --- |
| Access to Zendesk admin (org editing) | Care Operations / Op Ex / Zendesk admin | Existing | None |
| List of all active merchant orgs and their domains | Care Operations / Account Management | TBC | Blocks backfill accuracy |
| CRM data (if used as domain source of truth) | Sales Ops / Account Management | TBC | Optional; manual entry is fallback |

**Risks**:

| Risk | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- |
| Shared/generic domain mapped to an org, sweeping unrelated users in | Low if exception list followed | High — incorrect org assignment at scale | Exception list reviewed before every org domain is configured; generic domains hardcoded as do-not-map |
| Domain mapping step skipped during org creation | Medium — depends on process discipline | Medium — unassigned users accumulate | Quarterly audit catches gaps; checklist step makes it explicit |
| Two orgs claim the same domain | Low | Medium — Zendesk blocks second assignment, causing confusion | Conflict resolution process documented; Care Operations / Op Ex contacted before org creation for known shared-domain merchants |
| Multi-entity merchants incorrectly assigned via domain | Medium — known scenario | High — wrong entity context on tickets | Multi-entity merchants on exception list; org assignment driven by Client ID trigger, not domain |
| Backfill assigns user to wrong org | Low if domain data is clean | Medium | Backfill script validated against sample before full run; reversible via API |

**Open questions**:

- [ ] Is there a canonical source of Premium/Enterprise merchant email domains (e.g. Salesforce account field) that Care Operations / Operational Excellence can pull from during backfill? *(Owner: Sales Ops / Account Management)*
- [ ] Are there any existing Zendesk triggers or routing rules that would conflict with or be affected by bulk user org-assignment? *(Owner: Zendesk Admins)*
- [ ] Who owns the exception list ongoing — Care Operations, Operational Excellence, Zendesk Admins, or shared? *(Owner: Care Operations / Operational Excellence lead to decide)*


## Timeline

| Milestone | Date | Owner | Status |
| --- | --- | --- | --- |
| PRD complete | Feb 2026 | Charlie Wildish | Draft |
| Open questions resolved | TBC | Multiple | ⏳ |
| Audit & exception list complete | TBC | Care Operations / Op Ex | ⏳ |
| Existing orgs backfilled with domains | TBC | Care Operations / Op Ex | ⏳ |
| Bulk user assignment complete | TBC | Care Operations / Op Ex / Zendesk Admins | ⏳ |
| Org creation runbook updated | TBC | Care Operations / Op Ex | ⏳ |
| First quarterly audit | TBC | Care Operations / Op Ex | ⏳ |


## Appendix

- `04-active-work/roadmap-items/blue-emi-zendesk-support-prd.md` — Blue EMI Zendesk infrastructure (multi-entity merchant context)
- Zendesk documentation: [Organizations and user association](https://support.zendesk.com/hc/en-us/articles/4408882195482)

| Behaviour | Detail |
| --- | --- |
| Role in identification | Fallback only — fires when Salesforce lookup and Dashboard identity have not already assigned the user to an org |
| When mapping fires | At end-user creation only — not retroactively |
| Override behaviour | Does not override existing org assignment — safe to use alongside primary identification methods |
| Domain uniqueness | One domain per organisation — Zendesk enforces this |
| Subdomain coverage | `sony.com` does not cover `corp.sony.com` — add explicitly if needed |
| Multiple domains per org | Supported — space or comma separated in the Domains field |

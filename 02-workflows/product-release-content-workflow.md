# Product Release Content Workflow

When Engineering ships a product change, support content must keep pace. This workflow ensures technical docs and support articles are produced at ship time — before contacts arrive — rather than after Fin failures surface the gap.

This is the proactive complement to the Content Ops Agent (reactive gap detection via Reflex). Both mechanisms feed the same Knowledge Graph coverage matrix.

---

## Roles

| Role | Responsibility |
|---|---|
| Product / Engineering | Output technical documentation and a support article draft as a hard ship requirement |
| Content team | Review drafts, tag to taxonomy Reason nodes, map to product, publish to KB and support site |
| Knowledge Manager | Owns the coverage matrix; flags net-new query types for taxonomy review |

---

## Trigger

A product change is shipping that affects merchant-facing behaviour, API responses, error codes, configuration options, or resolution paths for existing contact types.

Not every release requires this workflow. Apply it when the change:
- Alters existing merchant-facing behaviour (changed response, new error code, updated flow)
- Introduces a new feature merchants will contact about
- Removes or deprecates something merchants rely on
- Changes a resolution path agents or Fin follow today

Internal-only changes, performance improvements with no UX impact, and infrastructure changes do not require support documentation.

---

## Step 1: Engineering outputs documentation at ship

**Owner: Product / Engineering**

As part of the release, produce two outputs:

**1. Technical documentation** — accurate description of what changed, for the technical docs site (`api-reference.checkout.com` or equivalent). This is standard engineering practice; it is not an addition to ship requirements.

**2. Support article draft** — a plain-language description of the change written for a merchant or support agent audience. This does not need to be polished. It needs to answer:
- What changed
- What the merchant will see or experience differently
- What to do if something goes wrong

Format: a markdown file in the PR or release notes. One to three paragraphs is sufficient. The Content team will reshape it — Eng does not need to write publication-ready copy.

**Gate:** the release is not marked complete until both outputs exist. This is enforced at PR review or release sign-off, not after the fact.

---

## Step 2: Content team receives and processes

**Owner: Content team**

On receipt of the support article draft:

1. **Review for accuracy** — validate the draft against the technical documentation. Flag discrepancies back to Engineering before proceeding.
2. **Tag to taxonomy** — identify which Case Type → Issue Type → Reason node(s) this content covers. If the change introduces a query type with no existing Reason code, flag to the Knowledge Manager for taxonomy review (see Step 3).
3. **Map to product** — identify which product in the Product Catalogue this content relates to.
4. **Reshape and publish** — edit to house style, publish to the support site and/or agent-facing KB. Update or create a Fin Procedure if the change affects how Fin resolves this contact type.
5. **Update the coverage matrix** — mark the relevant Reason node(s) as covered in the Knowledge Graph.

Target turnaround: within 5 business days of receiving the draft.

---

## Step 3: Taxonomy review for net-new query types

**Owner: Knowledge Manager, with input from Content team and Product**

If Step 2 identifies that the change introduces a contact type with no existing Reason code:

1. Knowledge Manager assesses whether a new Reason code is needed or whether the contact type maps to an existing node under a different label
2. If a new Reason is warranted, propose the addition to the taxonomy (Case Type → Issue Type → Reason) and align with Charlie
3. Update `support-taxonomy.md` and the Taxonomy Registry once agreed
4. Reflex and the Knowledge Graph pick up the new node on the next refresh cycle

This step is triggered by Step 2, not by a separate process. It should not block publication — publish to the closest existing node and update the taxonomy in parallel.

---

## Coverage matrix states

After publication, the Knowledge Graph records the coverage state for each affected Reason node:

| State | Meaning |
|---|---|
| **Covered** | Content exists and is published; Fin Procedure exists or is not needed |
| **Content gap** | Reason node exists in taxonomy; no content published yet |
| **Procedure gap** | Content published; no Fin Procedure mapped |
| **New node** | Net-new Reason code proposed; taxonomy update in progress |

The Content Ops Agent (Reflex) monitors this matrix and surfaces gaps not resolved within 10 business days of a product release.

---

## What this is not

This workflow does not replace:
- **Reflex / Content Ops Agent** — reactive gap detection continues; this workflow prevents new gaps, it does not close existing ones
- **SOP updates** — agent-facing SOPs are maintained separately via `02-workflows/sop-to-runbook-conversion.md`
- **Major content migrations** — large-scale KB restructuring or taxonomy overhauls are separate initiatives

---

## Checklist

**Engineering (at ship)**
- [ ] Technical documentation published or updated
- [ ] Support article draft produced (markdown, in PR or release notes)
- [ ] Draft handed to Content team with context on what changed

**Content team (within 5 business days)**
- [ ] Draft reviewed for accuracy against technical docs
- [ ] Discrepancies resolved with Engineering
- [ ] Tagged to taxonomy Reason node(s)
- [ ] Mapped to Product Catalogue
- [ ] Published to support site and/or agent KB
- [ ] Fin Procedure updated if resolution path changed
- [ ] Coverage matrix updated
- [ ] Net-new query types flagged to Knowledge Manager if applicable

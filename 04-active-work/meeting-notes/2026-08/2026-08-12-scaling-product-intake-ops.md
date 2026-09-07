# Scaling Product Intake and Introduction in Care and Ops

**Date:** 2026-08-12
**Attendees:** Alex Jordan, Charlie Wildish, Joel Petrosino, Daniel Kliza
**Drive source:** 1vjf99JAOLbyB85MV132TOpUWB68qCHfr7AVUxmKO2_8

## Context

Ops is being excluded from product launch planning. Two recent incidents triggered the session: a Visa financial partnership initiative added a required CAT field without telling Ops, causing merchant onboarding failures, and the MPG processor launch in MENA blindsided the team.

## Key Points

- Charlie's proposal: a shared, partly automated intake process defining what "operationally ready" means, with accountability pushed upstream so operational requirements are captured before launch.
- Mechanism: map products to taxonomy values, then to teams, tools and SOPs, so a new product launch automatically traces to its operational deliverables (SOP updates, training material, risk assessments, tooling changes).
- MCAP plus a custom Product Launch Document AI tool proposed as the standardisation vehicle. Orin owns the Confluence documentation on the current launch process.
- Alex surfaced an existing "terms of engagement" initiative: required assets and responsibilities tiered by size of product change. Oliver encouraged expanding it org-wide.
- Agreement that Claude can automate mapping product requirements to SOPs, conditional on the taxonomy and underlying data being well defined first.
- Product Docs as Code discussed: treat documentation changes as code commits so docs ship with the feature.
- Salesforce holds some of this data but is not sufficient. Standardised tagging and a codified process in Salesforce judged critical for scale.
- Support skills evolution: target state needs technical debugging and data engineering capability. Proof point: Kzia identified and resolved a specific code issue. New joiners are already improving documentation, drafting macros and building cheat sheets.

## Decisions

- Adopt MCAP as the foundational structure for the new product intake process.
- Map products to specific teams, tools and SOPs as the operational-readiness check.
- Kea is the owner and initial gateway for product-to-ops intake, with Joel, Charlie and Alex supporting the build. Kickoff w/c 17 August.
- Merchant Ops runs its own mapping exercise independently for domain-specific needs.
- Hold a dedicated session on support-staff upskilling and career pathways.

## Insights

- This is the origin of a named ops-readiness gate with a named owner. The product-to-taxonomy mapping is the prerequisite for automating everything downstream.
- The existing product-to-taxonomy mapping work becomes more than a classification exercise: it is the trigger table for launch readiness.

# Creating the Taxonomy Golden Set

**Date:** 2026-04-02  
**Attendees:** Charlie Wildish, Karan Jagmohansing, Francisco Goncalves, Imran Khan, Lachie Fielding  
**Drive source:** 1GqWJ7CgmcIAwoXoCDezrxIHfHLwEEPmpdTt1hexgG6Q

## Context

Planning session for creating a "golden set" — a ring-fenced dataset of correctly classified tickets to serve as the source of truth for taxonomy refinement via LLM analysis.

## Key Points

- The golden set is needed to validate future changes to the classification model and establish a baseline quality measure.
- Quarterly cadence: start with 100 sample tickets matched against the new taxonomy; grow the set by 100–200 per quarter. Critical for catching new issue types as the product roadmap changes.
- Process: mandatory labelling via Google Sheets/Forms; submissions locked to prevent overwriting. A few senior agent hours per quarter.
- Golden set is separate from and complementary to the existing QA framework — the QA framework alone doesn't provide a large enough sample across all taxonomy types.
- New taxonomy scheduled for deployment in Zendesk the following week (Apr 2026), applying only to newly generated tickets.
- Flow ticket closure protocol also confirmed: tickets must not be closed unless resolution is 100% certain.

## Insights

- A reliable taxonomy golden set is the foundation for LLM-based classification quality monitoring. Without it, model drift is undetectable.
- The quarterly 100-ticket cadence is minimal but practical. It should expand as classification complexity grows (B2C, Platforms).
- This work directly feeds both the Reflex data product (which requires accurate taxonomy to produce meaningful insights) and the Agent Consultant (which uses classification as a quality signal).

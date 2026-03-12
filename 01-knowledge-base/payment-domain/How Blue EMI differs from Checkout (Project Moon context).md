# How Blue EMI differs from Checkout (Project Moon context)

## Project Moon \= Blue EMI alias

## Legal and structural differences

| Company | Description |
| :---- | :---- |
| Checkout | Existing global payments company with multiple legal entities (e.g. Checkout Ltd, Checkout SAS). Today’s products, acquirers, BINs, contracts, etc., are structured around those entities. Checkout client ID, entity ID, Processing channels |
| Blue EMI | New legal entity created as part of a wider strategy to offer white-label acquiring and segregate certain business lines. Example: "Blue EMI LT, UAB" – a Lithuanian legal entity used in Moon Phase 1 for Visa/Mastercard acquiring, with its own acquirer configs, routes and banking setup (e.g. acquirer IDs bemi\_visa\_lt, bemi\_mc\_lt, dedicated settlement routes via Banking Circle, etc.). Blue EMI client ID, entity ID, Processing channels  |

In plain terms: Checkout is the existing company; Blue EMI is a new sister company/entity with its own regulatory footprint and setup, initially focused on a specific use case (e.g. higher-risk acquiring, new markets).

## Brand and customer-facing experience

| Aspect | Checkout | Blue EMI |
| :---- | :---- | :---- |
| Dashboard & endpoints | Merchants use https://dashboard.checkout.com and related \*.checkout.com / \*.ckotech.co endpoints. UI, emails, docs, etc. show "Checkout" branding. | Merchants see a Blue EMI–branded dashboard, separate from Checkout, with dedicated domains. |
| Dashboard URLs | https://dashboard.checkout.com | https://dashboard.blueemi.com (QA: https://dashboard.qa.blueemi.com) |
| MFEs & APIs | Served under Checkout domains. | MFEs & APIs run under Blue EMI domains, e.g. https://modules.dashboard.blueemi.com/{mfe} and https://api.dashboard.blueemi.com/{product}. |
| Visual identity | Checkout name, logo, colours and wording. | All visible mentions of "Checkout" / "CKO" in the Dashboard (UI text, emails, login pages) are replaced with the Blue EMI provider name and theme. |

In practice, a Blue EMI client should feel like: “I’m using Blue EMI’s platform,” not “Checkout”.

## Product and platform relationship

| Aspect | Checkout | Blue EMI |
| :---- | :---- | :---- |
| Core role | Owns and operates the core tech stack (Dashboard, MFEs, APIs, payments processing, bank connections) and exposes it directly under the Checkout brand. | Acts as a white-label tenant of that tech. |
| Use of systems | N/A (owner) | Reuses the same Checkout systems where it is safe to do so (e.g. many of the same services and data flows). |
| Segregation & config | Shared across Checkout entities. | Adds segregation and configuration: own legal entity, acquirers, BINs, routes, IAM setup, branding, and in future deeper data segregation. |

*   
  A Lithuanian entity ("Blue EMI LT, UAB").  
* Direct acquiring for Visa and Mastercard (similar feature set to Checkout SAS).  
* Onboarding specific clients (e.g. Binance) via that new entity.

In other words: Checkout is the engine room; Blue EMI is a branded, segregated front and legal wrapper that runs on that engine.

## Support and identifiers

**Key point for support:** Blue EMI merchants process under the **same Checkout Client ID** as Checkout merchants. The distinguishing identifier is the **Entity ID** — Blue EMI merchants process under a distinct Blue EMI Entity (e.g. Blue EMI LT, UAB) with its own Entity ID, separate from Checkout entities.

The same merchant can be:

* **Checkout only** — Checkout Client ID, Checkout entity
* **Blue EMI only** — same Checkout Client ID, Blue EMI entity and Entity ID
* **Both** — same Checkout Client ID, but separate Checkout and Blue EMI entities

Support, routing, and tooling (e.g. Zendesk, ticketing, dashboards) must use the **Entity ID** to correctly attribute and route Blue EMI tickets. Email alone does not identify which entity a contact belongs to; the Entity ID is only automatically capturable via the Blue EMI Dashboard webform (dashboard.blueemi.com).

## Compliance, segregation and business-line separation

From the Moon documentation, Blue EMI exists to:

* Segregate different business lines (e.g. higher-risk acquiring, different regions or partners).  
* Provide system/data segregation while still safely reusing Checkout systems in early phases.  
* Allow dedicated settlement routes, banking partners, and later deeper data segregation specific to Blue EMI.

So compared to Checkout, you get very similar features from a product perspective (especially in Phase 1), but with a different legal entity, risk profile, banking relationships, and client set, plus a fully separate-looking brand and URL.

## Quick side-by-side summary

| Aspect | Checkout | Blue EMI |
| :---- | :---- | :---- |
| What it is | Existing payments company / group | New legal entity (e.g. "Blue EMI LT, UAB") |
| Role in Project Moon | Provides the shared platform | White-labelled provider running on that platform |
| Branding / URL | dashboard.checkout.com, Checkout styling | dashboard.blueemi.com, Blue EMI styling & emails |
| Legal & regulatory | Existing Checkout entities (UK, FR, etc.) | New Lithuanian (and possibly other) entities |
| Acquirers & routes | Existing CKO acquirers and routes | New acquirer configs and settlement routes (e.g. via Banking Circle) |
| Clients | Current Checkout merchants | Separate portfolio of clients, e.g. Binance in Phase 1 |

# Quick view

* Checkout is the established payments company and platform; Blue EMI is a new legal entity and brand running on that platform.  
* Blue EMI has its own branding, dashboard URLs, acquirers, and client base, separate from Checkout.  
* To Blue EMI clients, the experience is fully Blue EMI-branded, not Checkout-branded.  
* Both use the same underlying technology, but Blue EMI is segregated for compliance, risk, and business reasons.  
* Project Moon enables this white-label setup to unlock new markets and business lines.  
* **Support:** Blue EMI and Checkout merchants share the same Client ID. The distinguishing identifier for support routing is the **Entity ID** — Blue EMI merchants process under a distinct Blue EMI entity with its own Entity ID. A merchant can be on Checkout, Blue EMI, or both; support and routing must use the Entity ID to correctly attribute the contact.


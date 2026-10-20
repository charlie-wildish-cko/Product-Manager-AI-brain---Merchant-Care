---
name: lift-design
description: Use this skill to generate well-branded interfaces and assets for LIFT (Checkout.com's enterprise-fintech design language), either for production or throwaway prototypes/mocks/etc. Contains essential design guidelines, colors, type, fonts, assets, and UI kit components for prototyping.
user-invocable: true
---

Read the README.md file within this skill, and explore the other available files.
If creating visual artifacts (slides, mocks, throwaway prototypes, etc), copy assets out and create static HTML files for the user to view. If working on production code, you can copy assets and read the rules here to become an expert in designing with this brand.
If the user invokes this skill without any other guidance, ask them what they want to build or design, ask some questions, and act as an expert designer who outputs HTML artifacts _or_ production code, depending on the need.

## Quick map
- `readme.md` — full design guide: brand, content/voice fundamentals, visual foundations, iconography, index.
- `styles.css` — the single entry point; link it and you get every token + font (`@import`s `tokens/*` + `components/components.css`).
- `tokens/` — colors, typography, spacing/radius/shadow, motion (CSS custom properties).
- `components/` — React primitives (`Button`, `IconButton`, `Card`, `Badge`, `Tag`, `Avatar`, `Input`, `Switch`, `Checkbox`, `Tabs`). Each has a `.d.ts` (props) + `.prompt.md` (usage).
- `ui_kits/payments-dashboard/` — full interactive merchant dashboard recreation.
- `slides/` — keynote slide templates (title, statement, metric, comparison).
- `assets/` — LIFT logo lockups + icon mark (gradient / white / midnight).
- `guidelines/*.html` — visual specimen cards.

## Non-negotiables
- **Checkout Blue `#006CFF`** for actions/highlights only — never decoration.
- Sentence case everywhere. Headlines follow **Action + Outcome** ("Move money smarter.").
- **No emoji.** Status is carried by the accent palette (success/warning/error/insight).
- Set amounts, rates and IDs in **JetBrains Mono** with tabular figures.
- Soft, sparing shadows (default `0 4px 16px rgba(0,0,0,.08)`); most surfaces use a 1px hairline border. Radius 12 (controls) / 16 (cards) / pill.
- Motion 250–350ms, smooth curves, no decorative animation. Focus rings always visible (WCAG AA).
- Display type is **Archivo** (free substitute for the brand's licensed **Söhne** — swap in real Söhne web files for production).

# LIFT Design System

**LIFT | Team Assets** — the enterprise-fintech design language behind Checkout.com's
payments products, marketing, and keynotes.

> **Purpose** — Power the movement of money across the digital economy.
> **Vision** — Enable businesses to perform at their highest potential through intelligent payments infrastructure.
> **Brand promise** — Every payment should move business forward.
> **Design principle** — *Flow Creates Performance.*

LIFT is built for a global, performance-obsessed audience. Everything in this system
expresses six brand attributes: **Intelligent · Trusted · Fluid · Modern · Precise · Global.**

---

## Sources

This system was authored from the **LIFT brand specification** (provided as text — colors,
type scale, tokens, voice, motion, components). No codebase or Figma file was attached; if you
have the source Figma library or the production component repo, share it and these recreations
can be reconciled against the originals.

> ⚠️ **Font substitution.** The display typeface **Söhne** (and its alt, Neue Haas Grotesk)
> is a commercial licence with no free webfont. It is substituted here with **Archivo**
> (Google Fonts), the closest free neo-grotesque. **Inter** (product) and **JetBrains Mono**
> (data) are used as specified. Drop licensed Söhne web files into `assets/` and update
> `tokens/fonts.css` + `--font-display` to go production-faithful.

---

## Content fundamentals

**Voice:** Confident, expert, clear, performance-driven, helpful. We speak to operators and
builders who move money for a living.

- **Casing** — Sentence case for UI and body. Headlines are sentence case too (`Move money smarter.`),
  never Title Case. Eyebrows/overlines are UPPERCASE with wide tracking.
- **Person** — Address the reader as **you** ("Optimize every payment"). Speak as **we** for the
  brand. Imperative verbs lead ("Move", "Scale", "Optimize", "Turn").
- **Headline formula** — **Action + Outcome.** e.g. *"Move money smarter." · "Optimize every payment." ·
  "Scale without friction." · "Turn payments into performance."*
- **Numbers** — Payments are numbers; show them. Set amounts, rates and IDs in **JetBrains Mono**
  with tabular figures (`$1,284,990.00`, `98.4%`).
- **Emoji** — None. The brand never uses emoji. Status is carried by color + the accent palette,
  not faces or symbols.
- **We sound like:** "Built for scale." "Designed for performance."
- **We don't sound like:** buzzword-heavy, overly casual, startup hype, or banking jargon.

---

## Visual foundations

**Color.** Anchored by **Checkout Blue `#006CFF`** — reserved for actions, highlights and key
moments, never decoration. **Midnight `#08111F`** carries dark surfaces and keynote backgrounds;
**White** and the cool, navy-biased neutrals (Fog `#F7F9FC`, Cloud `#EEF3FA`) carry light surfaces.
Performance accents (**Success #00C875, Warning #FFB020, Error #F04438, Insight #7B61FF**) are used
sparingly for status and signal. Two brand gradients exist — Primary `Blue→Insight` and Secondary
`Blue→Success` — used on dark hero/keynote moments, never behind body text.

**Type.** Archivo (Söhne substitute) for display/headlines with tight tracking (`-0.02em`); Inter
for everything in-product; JetBrains Mono for figures. The scale runs Display XL 72/80 → Caption 12/16.

**Spacing & layout.** An 8-based scale (4·8·12·16·24·32·48·64·96·128). Generous whitespace; content
maxes at 1200px (wide layouts 1440px). Grids and alignment are precise — nothing is approximate.

**Shape.** Corners are soft but controlled: **12px** default (buttons, inputs), **16px** for cards,
**999px** pills/tags. No sharp 0px corners, no oversized blobs.

**Elevation.** Shadows are soft and used **sparingly** — the default is `0 4px 16px rgba(0,0,0,.08)`.
Most surfaces use a 1px hairline border (`--border-subtle`) instead of a shadow. Cards are white with
a hairline border; elevate only floating/interactive surfaces.

**Backgrounds.** Light product UI sits on White or Fog. Brand/marketing moments use Midnight with
**flow lines** (dynamic curves) and **connection nodes** — the visual metaphor for payment journeys,
network intelligence and data movement. No photographic textures behind UI; no noise/grain.

**Motion.** Fast, intelligent, fluid, precise — **no decorative animation.** Working range 250–350ms;
the signature is **Payment Flow**: objects travel point A→B along smooth curves (not straight lines),
easing `cubic-bezier(.65,0,.35,1)`. Entrances fade+rise; there are no bounces or infinite loops in UI.

**States.** Hover deepens brand fills (`Blue 600`) or tints surfaces; press darkens further (`Blue 700`)
with a 1px downward nudge — never a scale-bounce. Focus is **always visible**: a 3px `rgba(0,108,255,.35)`
ring. Disabled drops to ~45% opacity.

**Imagery.** Cool-toned, premium-editorial, naturally lit. Real business environments and authentic
human interaction with technology embedded naturally — never staged smiling-at-camera stock.

**Accessibility.** WCAG AA minimum: 4.5:1 body text, 3:1 large text. Keyboard navigation required;
focus states always visible.

---

## Iconography

No proprietary icon font was supplied. LIFT uses **line icons** — geometric, technical, minimal,
~2px stroke, rounded joins — matching the brand's "geometric / technical / minimal" illustration
language. For prototypes, use **[Lucide](https://lucide.dev)** (CDN), which matches this stroke
weight and style closely; this is a **substitution** pending a licensed brand icon set. Use icons
functionally, at 18–24px, in `currentColor`. **No emoji, no multicolor/3D icons.** The LIFT mark
itself (flow line + nodes) lives in `assets/` as SVG.

The flow-line + connection-node motif (see `guidelines/brand-flow.html`) doubles as the brand's
illustration system — use it for diagrams, backgrounds and keynote moments.

---

## Index

**Foundations (CSS)** — consumers link one file: **`styles.css`** (imports everything below).
- `tokens/fonts.css` — `@font-face` / webfont imports (Inter, Archivo, JetBrains Mono)
- `tokens/colors.css` — palette + semantic aliases (surfaces, text, borders, status)
- `tokens/typography.css` — families, weights, type scale, helper classes
- `tokens/spacing.css` — spacing, radius, shadow, control sizing, layout
- `tokens/motion.css` — durations + easings
- `components/components.css` — class styles for the React primitives

**Components** (`window.LIFTDesignSystem_caf308.*`)
- Core — `Button`, `IconButton`, `Card`, `Badge`, `Tag`, `Avatar` → `components/core/`
- Forms — `Input`, `Switch`, `Checkbox` → `components/forms/`
- Navigation — `Tabs` → `components/navigation/`

**UI kits**
- `ui_kits/payments-dashboard/` — merchant payments Dashboard (overview, payments table, payment detail)

**Slides**
- `slides/` — keynote slide templates (title, statement, metric, comparison)

**Specimen cards** — `guidelines/*.html` populate the Design System tab (Colors, Type, Spacing, Motion, Brand).

**Assets** — `assets/` — LIFT logo lockups + icon mark (gradient / white / midnight).

**Skill** — `SKILL.md` makes this folder usable as a downloadable Claude Agent Skill.

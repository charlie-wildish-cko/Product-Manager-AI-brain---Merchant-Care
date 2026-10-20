# Payments Dashboard — UI kit

A high-fidelity recreation of a LIFT merchant **payments dashboard**: the view an operator
sees to monitor volume, authorization performance and individual payments.

## Screens / flow
- **Overview** — KPI cards (net volume, auth rate, captured, disputes), a volume **flow chart**
  (smooth Payment-Flow curve), and a recent-payments list.
- **Payments** — filterable table (tabs + search + filter tags). Click any row to open…
- **Payment detail** — slide-in drawer with the payment-flow timeline, method, fees and IDs.

Disputes / Payouts / Reports are intentionally left as placeholders — they weren't part of the
provided spec, so they're stubbed rather than invented.

## Composition
Built entirely from the LIFT component library (`window.LIFTDesignSystem_caf308`): `Button`,
`IconButton`, `Card`, `Badge`, `Tag`, `Avatar`, `Tabs`. Layout-only styles live in `dashboard.css`;
all color/type/spacing comes from design tokens. Icons are LIFT-style line icons in `Icons.jsx`
(Lucide-derived — see README iconography note).

## Files
- `index.html` — interactive entry (loads the bundle + screens)
- `data.js` — fake payments + metrics
- `Icons.jsx` — line icon set
- `Sidebar.jsx`, `Topbar.jsx` — app shell
- `Overview.jsx`, `PaymentsTable.jsx`, `PaymentDetail.jsx` — screens
- `App.jsx` — router/composition
- `dashboard.css` — layout styles

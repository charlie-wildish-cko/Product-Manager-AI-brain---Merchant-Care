Primary interactive element — use for any action; pick `variant` by emphasis.

```jsx
<Button variant="primary" size="lg" onClick={pay}>Pay $240.00</Button>
<Button variant="secondary">Cancel</Button>
<Button variant="ghost" iconLeft={<PlusIcon/>}>Add method</Button>
```

Variants: `primary` (Checkout Blue fill, default), `secondary` (blue outline), `ghost` (text only), `danger` (error fill).
Sizes: `sm` 36px · `md` 48px (default) · `lg` 56px. Use `block` for full-width, `iconLeft`/`iconRight` for icons.

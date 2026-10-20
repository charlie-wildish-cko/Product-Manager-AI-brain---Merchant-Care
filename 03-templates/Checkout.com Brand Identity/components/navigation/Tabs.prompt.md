Underline tab bar for switching views within a page.

```jsx
const [tab, setTab] = React.useState('payments');
<Tabs value={tab} onChange={setTab} tabs={[
  { id: 'payments', label: 'Payments' },
  { id: 'disputes', label: 'Disputes' },
  { id: 'payouts',  label: 'Payouts' },
]} />
```

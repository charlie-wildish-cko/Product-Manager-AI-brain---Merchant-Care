Labelled text field. Pass `error` to show the invalid state; `multiline` for a textarea.

```jsx
<Input label="Email" type="email" placeholder="you@company.com" />
<Input label="Amount" hint="USD" defaultValue="240.00" />
<Input label="API key" error="This key has expired" />
<Input label="Notes" multiline rows={3} />
```

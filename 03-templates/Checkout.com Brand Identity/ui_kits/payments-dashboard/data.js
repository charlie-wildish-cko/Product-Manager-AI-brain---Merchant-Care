// Fake data for the LIFT payments dashboard UI kit.
window.LIFT_DATA = {
  metrics: [
    { label: 'Net volume',      value: '$1,284,990', delta: '+12.4%', dir: 'up',   sub: 'vs. last 30 days' },
    { label: 'Authorization',   value: '98.4%',      delta: '+0.6pt', dir: 'up',   sub: 'auth rate' },
    { label: 'Captured',        value: '$1,201,540', delta: '+9.1%',  dir: 'up',   sub: '24,981 payments' },
    { label: 'Disputes',        value: '0.08%',      delta: '-0.02pt',dir: 'down', sub: 'of volume' },
  ],
  // weekly volume points (relative heights 0..1) for the area chart
  chart: [0.32, 0.41, 0.38, 0.52, 0.49, 0.63, 0.58, 0.71, 0.66, 0.78, 0.74, 0.88, 0.83, 0.97],
  payments: [
    { id: 'pay_8Kd92', amount: '$2,400.00', cur: 'USD', method: 'Visa',       last4: '4242', customer: 'Northwind Trading', email: 'ap@northwind.com',   status: 'success',  date: 'Jun 10, 14:22' },
    { id: 'pay_7Hd11', amount: '$89.00',    cur: 'USD', method: 'Mastercard', last4: '5588', customer: 'Lina Okafor',       email: 'lina@okafor.io',     status: 'success',  date: 'Jun 10, 13:58' },
    { id: 'pay_7Gd04', amount: '$1,250.00', cur: 'EUR', method: 'Visa',       last4: '0019', customer: 'Atlas Logistics',    email: 'billing@atlas.eu',   status: 'pending',  date: 'Jun 10, 13:40' },
    { id: 'pay_7Fc98', amount: '$540.00',   cur: 'GBP', method: 'Amex',       last4: '1003', customer: 'Harlow & Co',        email: 'pay@harlow.co.uk',   status: 'success',  date: 'Jun 10, 12:11' },
    { id: 'pay_7Ec70', amount: '$320.00',   cur: 'USD', method: 'Mastercard', last4: '7741', customer: 'Devin Park',         email: 'devin@park.dev',     status: 'failed',   date: 'Jun 10, 11:47' },
    { id: 'pay_7Dc55', amount: '$4,990.00', cur: 'USD', method: 'Visa',       last4: '8810', customer: 'Meridian Health',     email: 'ar@meridian.com',    status: 'refunded', date: 'Jun 10, 10:30' },
    { id: 'pay_7Cb42', amount: '$72.50',    cur: 'USD', method: 'Apple Pay',  last4: '3321', customer: 'Sora Tanaka',         email: 'sora@tanaka.jp',     status: 'success',  date: 'Jun 10, 09:58' },
    { id: 'pay_7Bb19', amount: '$215.00',   cur: 'EUR', method: 'Visa',       last4: '6650', customer: 'Brightline GmbH',     email: 'fin@brightline.de',  status: 'success',  date: 'Jun 10, 09:12' },
  ],
  statusMap: {
    success:  { variant: 'success', label: 'Succeeded' },
    pending:  { variant: 'warning', label: 'Pending' },
    failed:   { variant: 'error',   label: 'Failed' },
    refunded: { variant: 'neutral', label: 'Refunded' },
  },
};

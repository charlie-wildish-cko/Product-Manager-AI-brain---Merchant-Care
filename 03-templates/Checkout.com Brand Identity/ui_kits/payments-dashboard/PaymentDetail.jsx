// PaymentDetail — slide-in drawer with the payment-flow timeline.
(function () {
  const I = window.LIFT_ICONS;
  const { IconButton, Badge, Button } = window.LIFTDesignSystem_caf308;
  const D = window.LIFT_DATA;

  function Row({ k, v, mono }) {
    return (
      <div className="lift-drawer__row">
        <span className="muted">{k}</span>
        <span className={mono ? 'lift-dash-amount' : 'strong'}>{v}</span>
      </div>
    );
  }

  function PaymentDetail({ payment, onClose }) {
    const open = Boolean(payment);
    const p = payment || {};
    const s = D.statusMap[p.status] || {};
    const timeline = [
      { label: 'Authorized', done: true },
      { label: 'Captured', done: p.status === 'success' || p.status === 'refunded' },
      { label: p.status === 'refunded' ? 'Refunded' : 'Settled', done: p.status === 'refunded' },
    ];
    return (
      <>
        <div className={`lift-drawer__scrim ${open ? 'is-open' : ''}`} onClick={onClose} />
        <aside className={`lift-drawer ${open ? 'is-open' : ''}`}>
          {payment && (
            <>
              <div className="lift-drawer__head">
                <div>
                  <div className="muted lift-mono">{p.id}</div>
                  <div className="lift-drawer__amt">{p.amount} <span>{p.cur}</span></div>
                </div>
                <IconButton label="Close" onClick={onClose}><I.Close size={20} /></IconButton>
              </div>

              <div className="lift-drawer__status">
                <Badge variant={s.variant} dot>{s.label}</Badge>
                <span className="muted">{p.date}</span>
              </div>

              <div className="lift-drawer__flow">
                {timeline.map((t, i) => (
                  <div key={t.label} className={`lift-flowstep ${t.done ? 'is-done' : ''}`}>
                    <span className="dot">{t.done && <I.Check size={12} />}</span>
                    <span>{t.label}</span>
                    {i < timeline.length - 1 && <span className="line" />}
                  </div>
                ))}
              </div>

              <div className="lift-drawer__section">
                <Row k="Customer" v={p.customer} />
                <Row k="Email" v={p.email} />
                <Row k="Payment method" v={`${p.method} ···· ${p.last4}`} />
                <Row k="Amount" v={`${p.amount} ${p.cur}`} mono />
                <Row k="Processing fee" v="$0.62" mono />
                <Row k="Payment ID" v={p.id} mono />
              </div>

              <div className="lift-drawer__foot">
                <Button variant="secondary" block>Refund</Button>
                <Button block>View receipt</Button>
              </div>
            </>
          )}
        </aside>
      </>
    );
  }
  window.LIFT_PaymentDetail = PaymentDetail;
})();

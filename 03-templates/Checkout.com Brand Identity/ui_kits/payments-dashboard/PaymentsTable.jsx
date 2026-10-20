// Payments — filterable table; row click opens the detail drawer.
(function () {
  const I = window.LIFT_ICONS;
  const { Tabs, Badge, Button, Tag } = window.LIFTDesignSystem_caf308;
  const D = window.LIFT_DATA;

  function PaymentsTable({ onOpen }) {
    const [tab, setTab] = React.useState('all');
    const [q, setQ] = React.useState('');
    const rows = D.payments.filter((p) => {
      const okTab = tab === 'all' || p.status === tab;
      const okQ = !q || (p.customer + p.id + p.email).toLowerCase().includes(q.toLowerCase());
      return okTab && okQ;
    });
    return (
      <div className="lift-dash-stack">
        <div className="lift-dash-tablebar">
          <Tabs value={tab} onChange={setTab} tabs={[
            { id: 'all', label: 'All' },
            { id: 'success', label: 'Succeeded' },
            { id: 'pending', label: 'Pending' },
            { id: 'failed', label: 'Failed' },
            { id: 'refunded', label: 'Refunded' },
          ]} />
        </div>

        <div className="lift-dash-toolbar">
          <div className="lift-dash-search lift-dash-search--lg">
            <I.Search size={18} />
            <input placeholder="Search by customer, email or payment ID" value={q} onChange={(e) => setQ(e.target.value)} />
          </div>
          <div className="lift-dash-filters">
            <Tag onRemove={() => {}}>Last 30 days</Tag>
            <Tag onRemove={() => {}}>USD</Tag>
            <Button variant="ghost" size="sm" iconLeft={<I.Filter size={16} />}>Filter</Button>
          </div>
        </div>

        <div className="lift-dash-table">
          <div className="lift-dash-table__head">
            <div>Amount</div><div>Customer</div><div>Method</div><div>Status</div><div>Date</div><div></div>
          </div>
          {rows.map((p) => {
            const s = D.statusMap[p.status];
            return (
              <button key={p.id} className="lift-dash-table__row" onClick={() => onOpen(p)}>
                <div className="lift-dash-amount">{p.amount} <span>{p.cur}</span></div>
                <div className="lift-dash-cust2">
                  <span className="strong">{p.customer}</span>
                  <span className="muted">{p.email}</span>
                </div>
                <div className="muted">{p.method} ···· {p.last4}</div>
                <div><Badge variant={s.variant} dot>{s.label}</Badge></div>
                <div className="muted">{p.date}</div>
                <div className="lift-dash-table__chev"><I.ChevronRight size={18} /></div>
              </button>
            );
          })}
          {rows.length === 0 && <div className="lift-dash-empty">No payments match your filters.</div>}
        </div>
      </div>
    );
  }
  window.LIFT_PaymentsTable = PaymentsTable;
})();

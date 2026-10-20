// Overview — KPI cards, volume flow chart, recent payments.
(function () {
  const I = window.LIFT_ICONS;
  const { Card, Badge, Button } = window.LIFTDesignSystem_caf308;
  const D = window.LIFT_DATA;

  function FlowChart({ points }) {
    const W = 640, H = 180, pad = 8;
    const step = (W - pad * 2) / (points.length - 1);
    const xy = points.map((p, i) => [pad + i * step, H - pad - p * (H - pad * 2)]);
    // smooth path
    let d = `M ${xy[0][0]} ${xy[0][1]}`;
    for (let i = 1; i < xy.length; i++) {
      const [x0, y0] = xy[i - 1], [x1, y1] = xy[i];
      const cx = (x0 + x1) / 2;
      d += ` C ${cx} ${y0}, ${cx} ${y1}, ${x1} ${y1}`;
    }
    const area = `${d} L ${xy[xy.length - 1][0]} ${H} L ${xy[0][0]} ${H} Z`;
    return (
      <svg className="lift-dash-chart" viewBox={`0 0 ${W} ${H}`} preserveAspectRatio="none">
        <defs>
          <linearGradient id="vol" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0" stopColor="#006CFF" stopOpacity="0.18" />
            <stop offset="1" stopColor="#006CFF" stopOpacity="0" />
          </linearGradient>
        </defs>
        <path d={area} fill="url(#vol)" />
        <path d={d} fill="none" stroke="#006CFF" strokeWidth="2.5" strokeLinecap="round" />
        <circle cx={xy[xy.length - 1][0]} cy={xy[xy.length - 1][1]} r="4.5" fill="#006CFF" />
      </svg>
    );
  }

  function Overview() {
    return (
      <div className="lift-dash-stack">
        <div className="lift-dash-kpis">
          {D.metrics.map((m) => (
            <Card key={m.label} className="lift-kpi">
              <div className="lift-kpi__label">{m.label}</div>
              <div className="lift-kpi__value">{m.value}</div>
              <div className={`lift-kpi__delta ${m.dir}`}>
                {m.dir === 'up' ? <I.ArrowUpRight size={15} /> : <I.ArrowDownRight size={15} />}
                {m.delta} <span>{m.sub}</span>
              </div>
            </Card>
          ))}
        </div>

        <Card elevated className="lift-dash-panel">
          <div className="lift-dash-panel__head">
            <div>
              <div className="lift-kpi__label">Net volume</div>
              <div className="lift-dash-bigval">$1,284,990<span>.00</span></div>
            </div>
            <Button variant="secondary" size="sm" iconLeft={<I.Download size={16} />}>Export</Button>
          </div>
          <FlowChart points={D.chart} />
        </Card>

        <Card className="lift-dash-panel">
          <div className="lift-dash-panel__head">
            <h3>Recent payments</h3>
            <Button variant="ghost" size="sm" iconRight={<I.ChevronRight size={16} />}>View all</Button>
          </div>
          <div className="lift-dash-recent">
            {D.payments.slice(0, 5).map((p) => {
              const s = D.statusMap[p.status];
              return (
                <div key={p.id} className="lift-dash-recent__row">
                  <div className="lift-dash-recent__cust">
                    <div className="lift-dash-mono-mark">{p.method[0]}</div>
                    <div>
                      <div className="strong">{p.customer}</div>
                      <div className="muted">{p.method} ···· {p.last4}</div>
                    </div>
                  </div>
                  <Badge variant={s.variant} dot>{s.label}</Badge>
                  <div className="lift-dash-amount">{p.amount} <span>{p.cur}</span></div>
                </div>
              );
            })}
          </div>
        </Card>
      </div>
    );
  }
  window.LIFT_Overview = Overview;
})();

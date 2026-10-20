// Sidebar — Midnight nav rail with the LIFT mark.
(function () {
  const I = window.LIFT_ICONS;
  const NAV = [
    { id: 'overview', label: 'Overview', icon: I.Overview },
    { id: 'payments', label: 'Payments', icon: I.Card },
    { id: 'disputes', label: 'Disputes', icon: I.Shield },
    { id: 'payouts',  label: 'Payouts',  icon: I.Swap },
    { id: 'reports',  label: 'Reports',  icon: I.Chart },
  ];

  function Sidebar({ active, onNavigate }) {
    return (
      <aside className="lift-dash-sidebar">
        <div className="lift-dash-brand">
          <img src="../../assets/icon-lift.svg" width="32" height="32" alt="" />
          <span>LIFT</span>
        </div>
        <nav className="lift-dash-nav">
          {NAV.map((n) => {
            const Icon = n.icon;
            return (
              <button key={n.id}
                className={`lift-dash-navitem ${active === n.id ? 'is-active' : ''}`}
                onClick={() => onNavigate(n.id)}>
                <Icon size={20} /> <span>{n.label}</span>
              </button>
            );
          })}
        </nav>
        <div className="lift-dash-nav lift-dash-nav--foot">
          <button className="lift-dash-navitem"><I.Settings size={20} /> <span>Settings</span></button>
        </div>
      </aside>
    );
  }
  window.LIFT_Sidebar = Sidebar;
})();

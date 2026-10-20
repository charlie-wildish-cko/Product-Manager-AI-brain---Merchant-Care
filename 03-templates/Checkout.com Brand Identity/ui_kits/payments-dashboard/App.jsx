// App — composes the dashboard shell, routes between Overview & Payments.
(function () {
  const Sidebar = window.LIFT_Sidebar;
  const Topbar = window.LIFT_Topbar;
  const Overview = window.LIFT_Overview;
  const PaymentsTable = window.LIFT_PaymentsTable;
  const PaymentDetail = window.LIFT_PaymentDetail;

  const TITLES = { overview: 'Overview', payments: 'Payments', disputes: 'Disputes', payouts: 'Payouts', reports: 'Reports' };

  function App() {
    const [route, setRoute] = React.useState('overview');
    const [detail, setDetail] = React.useState(null);
    return (
      <div className="lift-dash">
        <Sidebar active={route} onNavigate={setRoute} />
        <div className="lift-dash-main">
          <Topbar title={TITLES[route]} />
          <div className="lift-dash-content">
            {route === 'overview' && <Overview />}
            {route === 'payments' && <PaymentsTable onOpen={setDetail} />}
            {route !== 'overview' && route !== 'payments' && (
              <div className="lift-dash-placeholder">
                <h3>{TITLES[route]}</h3>
                <p>This surface isn't part of the recreation. Use Overview and Payments for the full flow.</p>
              </div>
            )}
          </div>
        </div>
        <PaymentDetail payment={detail} onClose={() => setDetail(null)} />
      </div>
    );
  }
  window.LIFT_App = App;
})();

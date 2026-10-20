// Topbar — environment switch, search, actions, account.
(function () {
  const I = window.LIFT_ICONS;
  const { Button, IconButton, Switch, Avatar, Badge } = window.LIFTDesignSystem_caf308;

  function Topbar({ title }) {
    return (
      <header className="lift-dash-topbar">
        <div className="lift-dash-topbar__l">
          <h1>{title}</h1>
          <Badge variant="info" dot>Live</Badge>
        </div>
        <div className="lift-dash-topbar__r">
          <div className="lift-dash-search">
            <I.Search size={18} />
            <input placeholder="Search payments, customers, IDs" />
          </div>
          <IconButton label="Notifications"><I.Bell size={20} /></IconButton>
          <Button iconLeft={<I.Plus size={18} />}>New payment</Button>
          <Avatar name="Maya Chen" size={36} />
        </div>
      </header>
    );
  }
  window.LIFT_Topbar = Topbar;
})();

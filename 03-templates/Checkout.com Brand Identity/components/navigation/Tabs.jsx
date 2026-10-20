export function Tabs({ tabs = [], value, onChange }) {
  const active = value != null ? value : (tabs[0] && tabs[0].id);
  return (
    <div className="lift-tabs" role="tablist">
      {tabs.map((t) => (
        <button
          key={t.id}
          role="tab"
          aria-selected={t.id === active}
          className={`lift-tab ${t.id === active ? 'lift-tab--active' : ''}`}
          onClick={() => onChange && onChange(t.id)}
        >
          {t.label}
        </button>
      ))}
    </div>
  );
}

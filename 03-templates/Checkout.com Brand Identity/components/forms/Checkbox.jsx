export function Checkbox({ checked, defaultChecked, onChange, label, disabled = false, ...rest }) {
  return (
    <label className="lift-check">
      <input
        type="checkbox"
        checked={checked}
        defaultChecked={defaultChecked}
        onChange={onChange}
        disabled={disabled}
        {...rest}
      />
      <span className="box">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round"><polyline points="20 6 9 17 4 12" /></svg>
      </span>
      {label && <span>{label}</span>}
    </label>
  );
}

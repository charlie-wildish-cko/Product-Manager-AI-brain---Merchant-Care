export function Switch({ checked, defaultChecked, onChange, label, disabled = false, ...rest }) {
  return (
    <label className="lift-switch">
      <input
        type="checkbox"
        checked={checked}
        defaultChecked={defaultChecked}
        onChange={onChange}
        disabled={disabled}
        {...rest}
      />
      <span className="track"><span className="thumb" /></span>
      {label && <span>{label}</span>}
    </label>
  );
}

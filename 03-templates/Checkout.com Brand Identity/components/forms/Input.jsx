export function Input({
  label,
  hint,
  error,
  id,
  multiline = false,
  rows = 4,
  className = '',
  ...rest
}) {
  const inputId = id || (label ? `lift-${label.replace(/\s+/g, '-').toLowerCase()}` : undefined);
  const invalid = Boolean(error);
  const cls = ['lift-input', invalid ? 'lift-input--invalid' : '', className].filter(Boolean).join(' ');
  const Field = multiline ? 'textarea' : 'input';
  return (
    <div className="lift-field">
      {label && <label className="lift-label" htmlFor={inputId}>{label}</label>}
      <Field
        id={inputId}
        className={cls}
        rows={multiline ? rows : undefined}
        aria-invalid={invalid || undefined}
        {...rest}
      />
      {(hint || error) && (
        <span className={`lift-hint ${error ? 'lift-hint--error' : ''}`}>{error || hint}</span>
      )}
    </div>
  );
}

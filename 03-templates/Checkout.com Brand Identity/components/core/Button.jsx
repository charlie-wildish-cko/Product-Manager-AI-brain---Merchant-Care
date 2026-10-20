export function Button({
  children,
  variant = 'primary',
  size = 'md',
  block = false,
  iconLeft = null,
  iconRight = null,
  type = 'button',
  disabled = false,
  onClick,
  ...rest
}) {
  const cls = [
    'lift-btn',
    `lift-btn--${variant}`,
    size === 'sm' ? 'lift-btn--sm' : size === 'lg' ? 'lift-btn--lg' : '',
    block ? 'lift-btn--block' : '',
  ].filter(Boolean).join(' ');

  return (
    <button type={type} className={cls} disabled={disabled} onClick={onClick} {...rest}>
      {iconLeft}
      {children != null && <span>{children}</span>}
      {iconRight}
    </button>
  );
}

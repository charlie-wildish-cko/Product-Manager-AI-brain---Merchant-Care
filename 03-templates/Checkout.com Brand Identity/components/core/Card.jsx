export function Card({ children, elevated = false, interactive = false, as = 'div', style, className = '', ...rest }) {
  const Tag = as;
  const cls = [
    'lift-card',
    elevated ? 'lift-card--elevated' : '',
    interactive ? 'lift-card--interactive' : '',
    className,
  ].filter(Boolean).join(' ');
  return <Tag className={cls} style={style} {...rest}>{children}</Tag>;
}

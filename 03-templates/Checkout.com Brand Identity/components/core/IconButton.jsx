export function IconButton({ children, label, size = 'md', disabled = false, onClick, ...rest }) {
  const cls = ['lift-iconbtn', size === 'sm' ? 'lift-iconbtn--sm' : ''].filter(Boolean).join(' ');
  return (
    <button type="button" className={cls} aria-label={label} title={label} disabled={disabled} onClick={onClick} {...rest}>
      {children}
    </button>
  );
}

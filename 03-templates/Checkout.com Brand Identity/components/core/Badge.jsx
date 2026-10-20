export function Badge({ children, variant = 'neutral', dot = false }) {
  return (
    <span className={`lift-badge lift-badge--${variant}`}>
      {dot && <span className="dot" />}
      {children}
    </span>
  );
}

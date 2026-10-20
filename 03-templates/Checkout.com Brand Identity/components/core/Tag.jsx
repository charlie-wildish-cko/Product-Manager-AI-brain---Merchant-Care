export function Tag({ children, onRemove }) {
  return (
    <span className="lift-tag">
      {children}
      {onRemove && (
        <button type="button" aria-label="Remove" onClick={onRemove}>×</button>
      )}
    </span>
  );
}

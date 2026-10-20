export function Avatar({ src, name = '', size = 40 }) {
  const initials = name.split(' ').map((p) => p[0]).filter(Boolean).slice(0, 2).join('').toUpperCase();
  return (
    <span className="lift-avatar" style={{ width: size, height: size, fontSize: Math.round(size * 0.4) }}>
      {src ? <img src={src} alt={name} /> : initials}
    </span>
  );
}

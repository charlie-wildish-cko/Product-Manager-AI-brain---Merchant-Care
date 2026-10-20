// Line icons in the LIFT style (geometric, 2px stroke, rounded) — Lucide-derived paths.
(function () {
  const S = ({ children, size = 20, className }) => (
    <svg className={className} width={size} height={size} viewBox="0 0 24 24" fill="none"
      stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">{children}</svg>
  );
  const Icons = {
    Overview: (p) => <S {...p}><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/></S>,
    Card: (p) => <S {...p}><rect x="2" y="5" width="20" height="14" rx="2.5"/><path d="M2 10h20"/></S>,
    Shield: (p) => <S {...p}><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M12 8v4"/><path d="M12 16h.01"/></S>,
    Swap: (p) => <S {...p}><path d="M8 3 4 7l4 4"/><path d="M4 7h16"/><path d="m16 21 4-4-4-4"/><path d="M20 17H4"/></S>,
    Chart: (p) => <S {...p}><path d="M3 3v18h18"/><path d="m7 14 4-4 3 3 5-6"/></S>,
    Settings: (p) => <S {...p}><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.6 1.6 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.6 1.6 0 0 0-1.8-.3 1.6 1.6 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.6 1.6 0 0 0-1-1.5 1.6 1.6 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.6 1.6 0 0 0 .3-1.8 1.6 1.6 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.6 1.6 0 0 0 1.5-1 1.6 1.6 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.6 1.6 0 0 0 1.8.3H9a1.6 1.6 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.6 1.6 0 0 0 1 1.5 1.6 1.6 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.6 1.6 0 0 0-.3 1.8V9a1.6 1.6 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.6 1.6 0 0 0-1.5 1z"/></S>,
    Search: (p) => <S {...p}><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></S>,
    Bell: (p) => <S {...p}><path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"/></S>,
    ChevronRight: (p) => <S {...p}><path d="m9 18 6-6-6-6"/></S>,
    ArrowUpRight: (p) => <S {...p}><path d="M7 17 17 7"/><path d="M7 7h10v10"/></S>,
    ArrowDownRight: (p) => <S {...p}><path d="m7 7 10 10"/><path d="M17 7v10H7"/></S>,
    Plus: (p) => <S {...p}><path d="M12 5v14M5 12h14"/></S>,
    Download: (p) => <S {...p}><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="M7 10l5 5 5-5"/><path d="M12 15V3"/></S>,
    Close: (p) => <S {...p}><path d="M18 6 6 18M6 6l12 12"/></S>,
    Check: (p) => <S {...p}><path d="M20 6 9 17l-5-5"/></S>,
    Filter: (p) => <S {...p}><path d="M3 5h18l-7 8v6l-4-2v-4z"/></S>,
  };
  window.LIFT_ICONS = Icons;
})();

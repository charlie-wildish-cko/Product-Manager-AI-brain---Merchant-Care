import type { ReactNode } from 'react';

/** Small status / category label. Pill-shaped, soft-tinted. */
export interface BadgeProps {
  children: ReactNode;
  /** Semantic color. */
  variant?: 'neutral' | 'info' | 'success' | 'warning' | 'error' | 'insight';
  /** Show a leading status dot. */
  dot?: boolean;
}

export function Badge(props: BadgeProps): JSX.Element;

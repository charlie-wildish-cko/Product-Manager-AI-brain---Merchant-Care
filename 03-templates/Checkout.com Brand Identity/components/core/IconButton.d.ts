import type { ReactNode } from 'react';

/** Square icon-only button. Always pass `label` for accessibility. */
export interface IconButtonProps {
  /** The icon node (e.g. an SVG). */
  children: ReactNode;
  /** Accessible label (aria-label + tooltip). Required. */
  label: string;
  size?: 'sm' | 'md';
  disabled?: boolean;
  onClick?: (e: React.MouseEvent<HTMLButtonElement>) => void;
}

export function IconButton(props: IconButtonProps): JSX.Element;

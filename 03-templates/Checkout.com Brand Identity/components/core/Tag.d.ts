import type { ReactNode } from 'react';

/** Dismissible chip for filters, selections and tokens. */
export interface TagProps {
  children: ReactNode;
  /** When provided, renders a × remove control. */
  onRemove?: () => void;
}

export function Tag(props: TagProps): JSX.Element;

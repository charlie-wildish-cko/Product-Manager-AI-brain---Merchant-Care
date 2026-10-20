import type { ReactNode } from 'react';

/**
 * Primary call-to-action button. The brand's main interactive element.
 *
 * @startingPoint section="Core" subtitle="Primary, secondary, ghost & danger buttons" viewport="700x120"
 */
export interface ButtonProps {
  children?: ReactNode;
  /** Visual style. Primary = Checkout Blue fill; secondary = outline; ghost = text; danger = error fill. */
  variant?: 'primary' | 'secondary' | 'ghost' | 'danger';
  /** Control height. md = 48px (default), sm = 36px, lg = 56px. */
  size?: 'sm' | 'md' | 'lg';
  /** Stretch to full width of container. */
  block?: boolean;
  /** Icon node rendered before the label. */
  iconLeft?: ReactNode;
  /** Icon node rendered after the label. */
  iconRight?: ReactNode;
  type?: 'button' | 'submit' | 'reset';
  disabled?: boolean;
  onClick?: (e: React.MouseEvent<HTMLButtonElement>) => void;
}

export function Button(props: ButtonProps): JSX.Element;

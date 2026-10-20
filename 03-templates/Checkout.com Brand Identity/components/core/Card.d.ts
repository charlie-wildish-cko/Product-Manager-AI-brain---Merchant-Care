import type { ReactNode, ElementType } from 'react';

/**
 * Surface container with the brand's 16px radius and subtle border.
 *
 * @startingPoint section="Core" subtitle="Content surface — flat, elevated or interactive" viewport="700x200"
 */
export interface CardProps {
  children?: ReactNode;
  /** Add the default soft shadow and drop the border. */
  elevated?: boolean;
  /** Lift + deepen shadow on hover; use for clickable cards. */
  interactive?: boolean;
  /** Render as a different element (e.g. 'a', 'button', 'section'). */
  as?: ElementType;
  className?: string;
  style?: React.CSSProperties;
}

export function Card(props: CardProps): JSX.Element;

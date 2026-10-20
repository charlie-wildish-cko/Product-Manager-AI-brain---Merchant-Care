/** Circular user avatar — image, or gradient fallback with initials. */
export interface AvatarProps {
  /** Image URL. Falls back to initials when omitted. */
  src?: string;
  /** Full name; used for initials and alt text. */
  name?: string;
  /** Diameter in px. Default 40. */
  size?: number;
}

export function Avatar(props: AvatarProps): JSX.Element;

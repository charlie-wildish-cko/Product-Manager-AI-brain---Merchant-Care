/** Toggle switch for binary on/off settings. */
export interface SwitchProps {
  checked?: boolean;
  defaultChecked?: boolean;
  onChange?: (e: React.ChangeEvent<HTMLInputElement>) => void;
  /** Optional text label to the right of the track. */
  label?: string;
  disabled?: boolean;
}

export function Switch(props: SwitchProps): JSX.Element;

/**
 * Text input with optional label, hint and error state. Set `multiline` for a textarea.
 *
 * @startingPoint section="Forms" subtitle="Labelled text field with hint & error states" viewport="700x140"
 */
export interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  /** Field label rendered above the control. */
  label?: string;
  /** Helper text below the field. */
  hint?: string;
  /** Error message — overrides hint and applies the invalid style. */
  error?: string;
  /** Render a multi-line textarea instead of an input. */
  multiline?: boolean;
  /** Textarea row count when multiline. */
  rows?: number;
}

export function Input(props: InputProps): JSX.Element;

export interface TabItem {
  id: string;
  label: string;
}

/** Horizontal underline tabs. Controlled via `value` / `onChange`. */
export interface TabsProps {
  /** Tab definitions in display order. */
  tabs: TabItem[];
  /** Active tab id. Defaults to the first tab. */
  value?: string;
  onChange?: (id: string) => void;
}

export function Tabs(props: TabsProps): JSX.Element;

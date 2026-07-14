# Data Day 2027 — Logo ("The Trend Mark")

The hero mark is a minimal scatter-plot: bold **white/ink axes** with **five hollow data
points** and a **Signal-Magenta trend arrow** sweeping up and off to the right. Built
dark-first for Ink Void surfaces, paired with the "Plotting What's Next" wordmark and
"Data Day 2027". Colors are from the locked [palette](../palette.md).

## Files

| File | What it is | Use on |
|------|-----------|--------|
| `mark.svg` | Icon-only mark — ink axes/points, magenta arrow. Recolorable. | Light backgrounds |
| `mark-reversed.svg` | Icon-only — white axes/points, magenta arrow. | Dark / Ink Void backgrounds |
| `mark-mono-ink.svg` | One-color: everything Ink Void (incl. arrow). | One-color print, light bg |
| `mark-mono-white.svg` | One-color: everything white (incl. arrow). | Reversed one-color, photos |
| `favicon.svg` | Rounded Ink Void badge, white mark + magenta arrow. | Browser tab / avatar, ~24px+ |
| `logo-horizontal.svg` | Primary lockup — mark left, wordmark right. | Dark backgrounds |
| `logo-horizontal-light.svg` | Horizontal lockup, light-tuned colors. | Light backgrounds |
| `logo-stacked.svg` | Stacked lockup, mark above centered wordmark + tagline. | Dark backgrounds |
| `drawing.svg` | Original Inkscape source artwork the mark was traced from (reference only). | — |

## Recoloring

- **Axes & points** use `currentColor` — set the `color` CSS property (or `color=` attr) on
  the SVG to recolor them.
- **The arrow** defaults to Signal Magenta `#CB4FC0` and can be overridden with the
  `--dd-accent` CSS custom property in the browser (e.g. `style="--dd-accent:#F6B93B"`).
  The hard `#CB4FC0` fallback means the arrow is still magenta in non-browser tools
  (Inkscape, etc.) that don't resolve `var()`.

Colors used: axes/points `#F5F0F7` (Cloud White) or `#221C2B` (Ink Void); arrow `#CB4FC0`
(Signal Magenta). Wordmark `#CB4FC0`; "2027" in `#F6B93B` (Plot Gold 500, dark) /
`#B8790F` (Gold 600, light).

## Usage rules

**Clear space.** Keep clear space on all sides equal to the height of the mark's y-axis
(≈ half the mark height). Nothing intrudes into that zone.

**Minimum sizes.** Icon 24px · horizontal lockup 130px wide · stacked lockup 100px wide.
Below 24px, use the mark alone (drop the wordmark).

**Do:** keep the magenta arrow as the trend line · use white/ink axes + points · give it
room to breathe · use approved backgrounds.

**Don't:** recolor the arrow off-palette · stretch, skew, or rotate · fill the hollow
points · place on low-contrast backgrounds.

## Fonts

Wordmark is set in **Figtree** (humanist sans, weight 800) with **JetBrains Mono** for
mono/label accents. The lockup SVGs reference `Figtree` by name with a `system-ui`
fallback; embed or outline the type for environments without the font.

---

*Source: Claude Design project `19813721-b03a-45cc-9964-61ad5e02f050`, file "Data Day 2027
Logo - Final". Imported 2026-07-14. Verified with Inkscape renders on light and dark.*

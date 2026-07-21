# Data Day 2027 Color Palette

**Chosen palette: "Data Day Classic."** Following design review, Data Day 2027 keeps the
established Data Day / MORPC palette and the existing logo. The four core hexes below match
the logo SVGs in [`logo/`](logo/) exactly, so brand marks drop into any layout without a
color correction step.

Built **light-first**: a very light grey page with white cards is the default stage. Dark
Blue carries structure and headlines, Blue is the working/interactive color, and Teal and
Green are the accents. A dark muted black anchors text and reversed hero bands.

> Machine-readable tokens (full scales + semantic aliases) live in
> [`palette.css`](palette.css). Keep the two files in sync when values change.

---

## 1 · Core palette

| Name | HEX | Role / usage |
|------|-----|--------------|
| **Dark Blue** | `#073451` | Primary: headlines, nav, footers, dark bands. |
| **Blue** | `#0977BC` | Secondary: links, buttons, section accents. |
| **Teal** | `#00A79D` | Accent: highlights, icons, chart series. |
| **Green** | `#7CB46A` | Accent: highlights, tags, chart series. |
| **Ink** | `#171C21` | Dark muted black: body text, reversed surfaces. |
| **Fog** | `#F2F4F6` | Very light grey: page background, card fill. |

*Supporting neutrals:* elevated dark surface `#2A3238`, muted foreground `#5F6B75`,
hairline border on light `#DDE2E7`, white `#FFFFFF`.

---

## 2 · Extended scales

`100` (lightest tint) → `700` (darkest shade), with `500` = the core brand hex. On light UI,
`100`–`200` serve as fills and washes, `500` as solid fills and UI, `600`–`700` as text,
links, and pressed states.

### Dark Blue
| 100 | 200 | 300 | 400 | 500 | 600 | 700 |
|-----|-----|-----|-----|-----|-----|-----|
| `#E6EBEE` | `#BFCAD2` | `#889EAB` | `#4A6B80` | `#073451` | `#05263C` | `#041C2B` |

### Blue
| 100 | 200 | 300 | 400 | 500 | 600 | 700 |
|-----|-----|-----|-----|-----|-----|-----|
| `#E6F1F8` | `#BFDCEE` | `#89BEDF` | `#4B9CCE` | `#0977BC` | `#07588B` | `#053F64` |

### Teal
| 100 | 200 | 300 | 400 | 500 | 600 | 700 |
|-----|-----|-----|-----|-----|-----|-----|
| `#E6F6F5` | `#BDE8E6` | `#85D5D0` | `#45BFB7` | `#00A79D` | `#007C74` | `#005953` |

### Green
| 100 | 200 | 300 | 400 | 500 | 600 | 700 |
|-----|-----|-----|-----|-----|-----|-----|
| `#F2F8F0` | `#DDECD8` | `#C0DBB7` | `#9FC892` | `#7CB46A` | `#5C854E` | `#425F38` |

### Neutrals
| Fog | Mist | Slate | Ink Soft | Ink |
|-----|------|-------|----------|-----|
| `#F2F4F6` | `#DDE2E7` | `#5F6B75` | `#2A3238` | `#171C21` |

---

## 3 · Data-visualization palette

Six categorical colors drawn from the brand scales, ordered so the first three carry the
most common 3-series case at maximum separation.

| Name | HEX |
|------|-----|
| Blue | `#0977BC` |
| Teal | `#00A79D` |
| Green | `#7CB46A` |
| Dark Blue | `#073451` |
| Light Blue | `#89BEDF` |
| Slate | `#5F6B75` |

**Caution:** Blue and Teal are the closest pair under deuteranopia. For two-series charts
use Blue + Green; for series that must be told apart at a glance (thin lines, small dots),
pair color with a second channel: dash pattern, marker shape, or direct labels.

---

## 4 · Accessibility (WCAG contrast)

AA ≥ 4.5:1 normal text, ≥ 3:1 large text / UI; AAA ≥ 7:1. Ratios computed, not estimated.

### On light (`#FFFFFF` white / `#F2F4F6` Fog)

| Pairing | on White | on Fog | Normal text | Large / UI |
|---------|----------|--------|-------------|------------|
| Ink (body text) | 17.15:1 | 15.55:1 | ✅ AAA | ✅ Pass |
| Dark Blue 500 (headlines) | 12.97:1 | 11.76:1 | ✅ AAA | ✅ Pass |
| Blue 600 (links) | 7.56:1 | 6.86:1 | ✅ AAA / AA | ✅ Pass |
| Blue 500 | 4.80:1 | 4.35:1 | ✅ / ❌ on Fog | ✅ Pass |
| Slate (captions) | 5.46:1 | 4.95:1 | ✅ Pass | ✅ Pass |
| Teal 600 | 5.08:1 | 4.61:1 | ✅ Pass | ✅ Pass |
| Teal 500 | 2.99:1 | 2.72:1 | ❌ Fail | ❌ Fail |
| Green 700 | 7.18:1 | 6.51:1 | ✅ AAA / AA | ✅ Pass |
| Green 600 | 4.27:1 | 3.87:1 | ❌ Fail | ✅ Pass |
| Green 500 | 2.44:1 | 2.22:1 | ❌ Fail | ❌ Fail |

### Reversed (on `#171C21` Ink)

| Pairing | Ratio | Normal text | Large / UI |
|---------|-------|-------------|------------|
| Fog (body text on dark) | 15.55:1 | ✅ AAA | ✅ Pass |
| Dark Blue 300 (muted on dark) | 6.15:1 | ✅ Pass | ✅ Pass |
| Blue 300 (links on dark) | 8.57:1 | ✅ AAA | ✅ Pass |
| Blue 500 on Ink | 3.57:1 | ❌ Fail | ✅ Pass |
| Teal 300 | 10.15:1 | ✅ AAA | ✅ Pass |
| Teal 500 | 5.73:1 | ✅ Pass | ✅ Pass |
| Green 300 | 11.48:1 | ✅ AAA | ✅ Pass |
| Green 500 | 7.02:1 | ✅ AAA | ✅ Pass |

### Text on brand fills

| Pairing | Ratio | Verdict |
|---------|-------|---------|
| White on Dark Blue 500 | 12.97:1 | ✅ AAA |
| White on Blue 500 | 4.80:1 | ✅ AA |
| White on Teal 600 | 5.08:1 | ✅ AA |
| Dark Blue 500 on Teal 500 | 4.33:1 | ✅ Large / UI only |
| Ink on Teal 500 | 5.73:1 | ✅ AA |
| Ink on Green 500 | 7.02:1 | ✅ AAA |

**Rules of thumb**

- **Teal 500 and Green 500 are fills only on light backgrounds**, never as text on white or
  Fog. For teal text use Teal 600; for green text use Green 700.
- **Links on light use Blue 600**, not Blue 500. Blue 500 on Fog lands at 4.35:1 and misses AA.
- **Buttons:** white text on Dark Blue 500 or Blue 500; Ink text on Teal 500 or Green 500.
- **On dark, drop to the `300` steps** for text and links. Blue 500 fails on Ink.

---

## 5 · Suggested pairings

- **Header: Dark Blue 500 + White.** White type on the deep navy; nav, hero bands, footers.
  The primary logo reverses cleanly here (use the White lockups from [`logo/`](logo/)).
- **Page: Fog + White cards + Ink text.** The default stage. Mist (`#DDE2E7`) hairlines,
  Slate for captions and metadata.
- **CTA: Teal 500 + Ink.** The single "act on this" fill: register, submit a proposal,
  sponsor. Green 500 + Ink is the quieter second CTA.
- **Callout / tag: Blue 100 or Teal 100 wash + Dark Blue 600 text.** Low-weight emphasis
  inside body copy without a heavy fill.

---

## 6 · Rationale

Design review landed on continuity: Data Day is entering its 5th year, and the audience of
public-sector data practitioners already recognizes this palette and logo. Keeping both
lets the anniversary framing carry the "what's changed" weight instead of a rebrand
competing with it.

Structurally, the palette is a cool blue spine (Dark Blue → Blue) with two warmer-leaning
accents (Teal, Green) that share enough saturation to read as one family. Dark Blue does the
architecture (headlines, bands, footers) while Blue carries anything interactive, so
"structural" and "clickable" never collide. Teal and Green are held back for accent duty,
which keeps a single CTA color obvious on any given page.

The added neutrals do the work the four brand colors can't. The dark muted black
(`#171C21`) is warmer and softer than pure black, so long-form body copy on Fog reads
without the harsh edge of `#000000`, and it doubles as the reversed hero surface. The very
light grey (`#F2F4F6`) gives white cards something to sit on, which is what makes a
document-heavy site (agenda, CFP, sponsor tiers) scan as sections rather than one wall.

The accessibility ceiling is the honest constraint: Teal 500 and Green 500 are bright,
mid-luminance colors that cannot carry text on light backgrounds. The 600–700 steps exist
specifically to cover that, and the rules in §4 are the guardrail.

---

## 7 · Copyable values

### HEX list
```
Dark Blue          #073451
Blue               #0977BC
Teal               #00A79D
Green              #7CB46A

Ink                #171C21
Ink Soft           #2A3238
Slate              #5F6B75
Mist               #DDE2E7
Fog                #F2F4F6
White              #FFFFFF
```

### CSS custom properties
See [`palette.css`](palette.css) for the complete token set (full 100–700 scales, the
data-viz palette, semantic aliases, and a `.dd-dark` block for reversed surfaces):

```css
:root {
  --dd-navy-500:  #073451;
  --dd-blue-500:  #0977BC;
  --dd-blue-600:  #07588B;  /* links on light */
  --dd-teal-500:  #00A79D;
  --dd-teal-600:  #007C74;  /* teal text on light */
  --dd-green-500: #7CB46A;
  --dd-green-700: #425F38;  /* green text on light */
  --dd-ink:       #171C21;
  --dd-slate:     #5F6B75;
  --dd-mist:      #DDE2E7;
  --dd-fog:       #F2F4F6;
}
```

---

*Core hexes sourced from the Data Day logo SVGs in `Design/logo/`. Palette rebuilt
2026-07-21 after design review chose to retain the existing brand.*

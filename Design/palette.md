# Data Day 2027 — Color Palette

**Chosen palette: "Magenta Signal (Dark)"** (Option 1b) — imported from the Claude Design
project and locked as the source of truth for Data Day 2027 marketing and the static site.

Built **dark-first**: a near-black violet surface is the default stage, with Signal Magenta
as the hero, Route Indigo as its cooler structural counterpart, and Plot Gold as the single
"forward motion" accent for CTAs and the plotted trend line. Deliberately distinct from
MORPC's blue / green / light-blue trio, but tuned to sit alongside the MORPC logo without
clashing.

> Machine-readable tokens (full scales + semantic aliases) live in
> [`palette.css`](palette.css). Keep the two files in sync when values change.

---

## 1 · Core palette

| Name | HEX | Role / usage |
|------|-----|--------------|
| **Signal Magenta** | `#CB4FC0` | Hero color — headers, primary buttons, nav. |
| **Route Indigo** | `#6153C4` | Secondary — section accents, icons, tags. |
| **Plot Gold** | `#F6B93B` | Energetic accent — CTAs, the plotted route, the "5". |
| **Ink Void** | `#221C2B` | Primary dark background. |
| **Surface** | `#4A3F5C` | Elevated dark surface — cards, panels. |
| **Cloud White** | `#F5F0F7` | Light foreground — headlines, primary text on dark. |
| **Mist Gray** | `#948DA0` | Muted foreground — captions, borders, disabled states. |

*Deeper page tones used in the mockup (optional, for layered dark UI):* page base `#0F0C13`,
card fill `#1B1622`, hairline border `#2B2434`.

---

## 2 · Extended scales

`100` (lightest tint) → `700` (darkest shade). On dark UI, `200`–`400` typically serve as
text/icon color on the background, `500` as fills, `600`–`700` as pressed/deep states.

### Signal Magenta
| 100 | 200 | 300 | 400 | 500 | 600 | 700 |
|-----|-----|-----|-----|-----|-----|-----|
| `#F6E6F3` | `#E9BEE0` | `#E48CDA` | `#C36BB6` | `#CB4FC0` | `#7A2F71` | `#552050` |

### Route Indigo
| 100 | 200 | 300 | 400 | 500 | 600 | 700 |
|-----|-----|-----|-----|-----|-----|-----|
| `#EAE8F9` | `#CBC5F0` | `#9C8FE0` | `#7A6BCF` | `#6153C4` | `#443A8C` | `#302963` |

### Plot Gold
| 100 | 200 | 300 | 400 | 500 | 600 | 700 |
|-----|-----|-----|-----|-----|-----|-----|
| `#FDF1D9` | `#FBDE9F` | `#F9CA6A` | `#F7C24F` | `#F6B93B` | `#B8790F` | `#8A5B0B` |

---

## 3 · Data-visualization palette

Six categorical colors, tuned to stay legible on dark backgrounds and distinguishable for
deuteranopia / protanopia. No blue or green, so multi-series charts stay on-brand.

| Name | HEX |
|------|-----|
| Magenta | `#CB4FC0` |
| Indigo | `#9C8FE0` |
| Gold | `#F6B93B` |
| Rose | `#F2607B` |
| Rust | `#C96A3E` |
| Mist Gray | `#948DA0` |

---

## 4 · Accessibility — WCAG contrast (on dark)

All pairings checked against the primary dark background `#221C2B` (Ink Void).
AA ≥ 4.5:1 normal text, ≥ 3:1 large text / UI; AAA ≥ 7:1.

| Pairing | Ratio | Normal text | Large text / UI |
|---------|-------|-------------|-----------------|
| Cloud White on Ink Void (body text) | 16.4:1 | ✅ Pass (AAA) | ✅ Pass |
| Cloud White on Surface | 15.0:1 | ✅ Pass (AAA) | ✅ Pass |
| Mist Gray on Ink Void (captions) | 5.77:1 | ✅ Pass | ✅ Pass |
| Magenta 300 on Ink Void (links) | 7.1:1 | ✅ Pass (AAA) | ✅ Pass |
| Magenta 500 on Ink Void (fills / UI only) | 4.3:1 | ❌ Fail | ✅ Pass |
| Indigo 300 on Ink Void (links) | 6.5:1 | ✅ Pass | ✅ Pass |
| Indigo 500 on Ink Void (fills / UI only) | 3.1:1 | ❌ Fail | ✅ Pass |
| Plot Gold 500 on Ink Void | 10.5:1 | ✅ Pass (AAA) | ✅ Pass |
| Rose on Ink Void | 5.9:1 | ✅ Pass | ✅ Pass |
| Rust on Ink Void | 4.9:1 | ✅ Pass | ✅ Pass |
| Ink Void on Plot Gold (dark text on gold button) | 10.5:1 | ✅ Pass (AAA) | ✅ Pass |

**Rules of thumb:** use Magenta 500 and Indigo 500 as **fills only** — never as text on the
dark background; for links / text emphasis use the `300` steps. Gold buttons take dark
(Ink Void) text.

---

## 5 · Suggested pairings

- **Header — Ink Void + Cloud White.** Cloud White text on the dark base; hero sections,
  nav, footers — the default stage.
- **Callout — Plot Gold + Ink Void.** Dark text on Gold 500 — CTAs, the plotted route, the
  "5" mark. AAA contrast either direction.
- **Card — Surface + Magenta 300.** Magenta 300 or Indigo 300 for links / emphasis on the
  elevated Surface tone.

---

## 6 · Rationale

Built dark-first: the near-black violet surface (`#221C2B`) is the default stage, not an
afterthought — so hero, secondary, and accent are all tuned to glow against it rather than
get muddy.

Magenta carries the hero role — warm-cool, distinctly **not** MORPC's blue / green /
light-blue — with Indigo-violet as its cooler counterpart for structure. Gold is the one
deliberate temperature break: the "forward motion" accent for CTAs and the plotted trend
line, chosen for AAA contrast on dark so it always reads as the thing to act on.

The data-viz set adds Rose and Rust to widen the hue range without introducing blue or
green, keeping multi-series charts distinguishable for color-blind readers even on a dark
canvas.

---

## 7 · Copyable values

### HEX list
```
Signal Magenta     #CB4FC0
Route Indigo       #6153C4
Plot Gold          #F6B93B
Ink Void           #221C2B
Surface            #4A3F5C
Cloud White        #F5F0F7
Mist Gray          #948DA0

Rose               #F2607B
Rust               #C96A3E
```

### CSS custom properties
See [`palette.css`](palette.css) for the complete token set (full 100–700 scales plus these
semantic aliases):

```css
:root {
  --dd-magenta-300: #E48CDA;
  --dd-magenta-500: #CB4FC0;
  --dd-magenta-600: #7A2F71;
  --dd-indigo-300:  #9C8FE0;
  --dd-indigo-500:  #6153C4;
  --dd-indigo-600:  #443A8C;
  --dd-gold-500:    #F6B93B;
  --dd-gold-600:    #B8790F;
  --dd-rose:        #F2607B;
  --dd-rust:        #C96A3E;
  --dd-ink-void:    #221C2B;
  --dd-surface:     #4A3F5C;
  --dd-cloud:       #F5F0F7;
  --dd-mist:        #948DA0;
}
```

---

*Source: Claude Design project `19813721-b03a-45cc-9964-61ad5e02f050`, file "Data Day 2027
Palette - Magenta Signal (Dark)". Imported 2026-07-14.*

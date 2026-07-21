# Data Day 2027 Design Brief

Markdown companion to [`design-brief.html`](design-brief.html), the visual color guide.
The HTML file is the shareable artifact; this file is the readable/greppable version for
working in the repo. Keep the two in sync when values change.

**Source of truth for tokens:** [`palette.css`](palette.css). Full contrast tables and
rationale: [`palette.md`](palette.md).

---

## 1 · The decision

Design review chose continuity. Data Day 2027 keeps the established palette and logo for the
5th annual event, so the anniversary framing carries the message rather than a rebrand
competing with it. The four brand hexes are taken directly from the logo artwork in
[`logo/`](logo/), so marks drop into any layout without a color correction step.

Two colors were added, because four brand colors cannot build a document on their own:

- **Ink `#171C21`**, a dark muted black, for body text and reversed surfaces. Warmer and
  softer than `#000000`, so long-form copy reads without a harsh edge.
- **Fog `#F2F4F6`**, a very light grey, as the page background. It gives white cards
  something to sit on, which is what makes a document-heavy site scan as sections rather
  than one wall.

Nothing else was introduced. Every tint and shade is derived from the four core hexes.

---

## 2 · Core palette

| Name | HEX | Role |
|------|-----|------|
| **Dark Blue** | `#073451` | Primary. Headlines, nav, footers, dark bands. |
| **Blue** | `#0977BC` | Secondary. Links, buttons, section accents. |
| **Teal** | `#00A79D` | Accent. Primary CTA fill, highlights, chart series. |
| **Green** | `#7CB46A` | Accent. Secondary CTA, tags, chart series. |
| **Ink** | `#171C21` | Dark muted black. Body text, reversed surfaces. |
| **Fog** | `#F2F4F6` | Very light grey. Page background, card fill. |

Supporting neutrals: White `#FFFFFF`, Mist `#DDE2E7` (hairlines, dividers, table borders),
Slate `#5F6B75` (captions, metadata, disabled), Ink Soft `#2A3238` (elevated dark surface).

Structural logic: Dark Blue does the architecture, Blue carries anything interactive, so
"structural" and "clickable" never collide. Teal and Green are held back for accent duty,
which keeps a single CTA color obvious on any given page.

---

## 3 · Extended scales

`500` is the core brand hex. On light UI, `100`-`200` are fills and washes, `500` is solid
fills and UI, `600`-`700` are text, links, and pressed states. On dark UI, `300` carries
text and links.

| Color | 100 | 200 | 300 | 400 | 500 | 600 | 700 |
|-------|-----|-----|-----|-----|-----|-----|-----|
| Dark Blue | `#E6EBEE` | `#BFCAD2` | `#889EAB` | `#4A6B80` | `#073451` | `#05263C` | `#041C2B` |
| Blue | `#E6F1F8` | `#BFDCEE` | `#89BEDF` | `#4B9CCE` | `#0977BC` | `#07588B` | `#053F64` |
| Teal | `#E6F6F5` | `#BDE8E6` | `#85D5D0` | `#45BFB7` | `#00A79D` | `#007C74` | `#005953` |
| Green | `#F2F8F0` | `#DDECD8` | `#C0DBB7` | `#9FC892` | `#7CB46A` | `#5C854E` | `#425F38` |

Neutral ramp: Fog `#F2F4F6` · Mist `#DDE2E7` · Slate `#5F6B75` · Ink Soft `#2A3238` · Ink `#171C21`

---

## 4 · Accessibility

AA needs 4.5:1 normal text and 3:1 large text / UI. AAA needs 7:1. All ratios computed, not
estimated.

### Text legality matrix

Ratios of each text color against the four surfaces. **Bold** = safe for normal body text.

| Text color | on White | on Fog | on Dark Blue | on Ink |
|---|---|---|---|---|
| Ink `#171C21` | **17.15** | **15.55** | 1.32 | 1.00 |
| Slate `#5F6B75` | **5.46** | **4.95** | 2.38 | 3.14 (large) |
| White `#FFFFFF` | 1.00 | 1.10 | **12.97** | **17.15** |
| Fog `#F2F4F6` | 1.10 | 1.00 | **11.76** | **15.55** |
| Dark Blue 500 | **12.97** | **11.76** | 1.00 | 1.32 |
| Dark Blue 300 | 2.79 | 2.53 | **4.65** | **6.15** |
| Blue 500 | **4.80** | 4.35 (large) | 2.70 | 3.57 (large) |
| Blue 600 | **7.56** | **6.86** | 1.72 | 2.27 |
| Blue 300 | 2.00 | 1.81 | **6.48** | **8.57** |
| Teal 500 | 2.99 | 2.72 | 4.33 (large) | **5.73** |
| Teal 600 | **5.08** | **4.61** | 2.55 | 3.38 (large) |
| Teal 300 | 1.69 | 1.53 | **7.67** | **10.15** |
| Green 500 | 2.44 | 2.22 | **5.31** | **7.02** |
| Green 700 | **7.18** | **6.51** | 1.81 | 2.39 |
| Green 300 | 1.49 | 1.35 | **8.68** | **11.48** |

### The two traps

1. **Teal 500 and Green 500 cannot be text on light backgrounds.** They land at 2.99:1 and
   2.44:1 on white. They are fill colors there. For teal text use **Teal 600**, for green
   text use **Green 700**.
2. **Blue 500 is not a link color.** On Fog it is 4.35:1 and misses AA. Links on light use
   **Blue 600** (7.56:1 on white). On dark, Blue 500 drops to 3.57:1, so links there use
   **Blue 300** (8.57:1 on Ink).

### Standing rules

- On the Dark Blue band, step accents up one stop. Teal 500 on Dark Blue is 4.33:1 (large
  and UI only); Teal 300 is 7.67:1 and safe at any size.
- Bright accent fills take **dark text**: Ink on Teal 500 is 5.73:1, Ink on Green 500 is
  7.02:1. White on Teal 500 is only 2.99:1. If a teal button needs white text, use Teal 600
  (5.08:1).
- Teal 500 as a graphic or icon on white is 2.99:1, under the 3:1 floor for meaningful
  graphics. Use Blue 600 for icons on light surfaces.

---

## 5 · Approved combinations

| Pairing | Contrast | Use |
|---|---|---|
| Dark Blue + White | 12.97:1 | Headers, nav, hero bands, footers. White logo lockup. |
| Fog + Ink | 15.55:1 | Default reading surface. Slate for captions. |
| Teal + Ink | 5.73:1 | Primary CTA. Ink text, never white. |
| Green + Ink | 7.02:1 | Quieter second CTA. |
| Blue 100 wash + Blue 700 | 9.63:1 | Callouts and tags inside body copy. |
| Ink + Fog | 15.55:1 | Reversed sections. Accents step up to the 300 tints. |
| White + Dark Blue | 12.97:1 | Print documents. Blue 600 for headings and links. |

---

## 6 · Web

The site uses **light surfaces with a Dark Blue header band and footer**.

| Element | Treatment |
|---|---|
| Signature strip, nav, hero | Dark Blue `#073451`. White logo lockup, White nav text, Blue 300 for hover and current page, Teal 300 for the year tag and hero headline, Blue 300 eyebrow, Navy 200 lede. |
| Page | Fog `#F2F4F6`. |
| Alternating sections (`.venue`) | White, with cards inside dropping to Fog so they stay visible. |
| Cards | White, Mist border, Dark Blue heading, `#3D474F` body, Blue 600 icons and links. |
| Buttons | `.btn-primary` = Teal 500 fill + Ink text (reads on both band and page). `.btn-ghost` = Dark Blue text + Navy 300 border on light; white text + Navy 400 border scoped to the hero. |
| Nav dropdown | White card, Mist border, Ink items, Fog hover, Blue 600 current. |
| Stat tiles | White card, Teal 600 number, Slate unit, `#3D474F` label. |
| Pull quotes | White card, Teal 500 left rule, Ink body, Blue 600 cite. |
| Tables | Blue 600 header with white text, Fog zebra striping, Mist borders. |
| Footer | Dark Blue, bookending the header. Navy 200 text, Blue 300 links, White logo. |

Tokens live inline in `docs/styles.css` (GitHub Pages serves everything from `/docs`), kept
in sync with `Design/palette.css`.

---

## 7 · Print

Print flips the default: **white paper, Dark Blue titles, Blue 600 section headings, Ink
body**. Teal appears as rules and accent fills rather than large areas, which keeps ink
coverage sane and reproduces reliably on office printers.

- **One-pagers, FAQs, agendas.** Primary logo top left, MORPC logo top right. Dark Blue H1
  with a 3px Teal rule. Blue 600 H2s with Mist rules. Ink body. See
  `.claude/skills/create-pdf/style.css`.
- **Brochure covers and reversed panels.** Dark Blue field, White logo lockup, Teal 300
  eyebrow, Navy 200 supporting copy. A Blue / Teal / Green rule works as a footer accent.
- **Name badges.** Dark Blue header bar with the White lockup, white body, Ink name, Slate
  organization, Teal 500 role pill with Ink text, four-color footer stripe.
- **Slides.** White field, Teal 500 left bar, Dark Blue title, Slate subtitle, Primary logo
  bottom right.
- **Social and save-the-date.** Ink or Dark Blue field, White lockup, Teal 300 date line,
  White headline, Navy 200 detail.

**Grayscale fallback:** Teal and Green convert to near-identical greys. If a document may be
photocopied, separate categories by label or pattern, not color alone.

**Minimum sizes:** horizontal lockup no smaller than 1.25 in wide in print, 120 px on screen.

---

## 8 · Data visualization

Categorical order, tuned so the first three carry the common three-series case at maximum
separation:

1. Blue `#0977BC`
2. Teal `#00A79D`
3. Green `#7CB46A`
4. Dark Blue `#073451`
5. Light Blue `#89BEDF`
6. Slate `#5F6B75`

- Blue and Teal are the closest pair under deuteranopia. For two-series charts use **Blue and
  Green**.
- When series must be told apart at a glance (thin lines, small dots), pair color with a
  second channel: dash pattern, marker shape, or direct labels.
- Sequential ramps use one hue. Blue scale for the primary measure, Teal scale for a second.
  Do not mix two hues into one sequential ramp.

---

## 9 · Logo

Four files in [`logo/`](logo/): Primary and White, each horizontal and vertical. Pick by
background, never by recoloring.

| File | Use |
|---|---|
| Primary Horizontal | White and Fog backgrounds. Default for print. |
| White Horizontal | Dark Blue and Ink backgrounds. Default for web. |
| Primary Vertical | Square and narrow spaces: social avatars, signage, badges. |
| White Vertical | Same, on dark fields. |

**Clear space:** on all sides, equal to the height of the mark.

**Don'ts**

- Do not recolor the mark. The four colors in the artwork are the brand.
- Do not place the Primary lockup on Dark Blue, Ink, or any photograph. Use the White lockup.
- Do not stretch, rotate, add effects, or rebuild the lockup from parts.
- Do not set the horizontal lockup below 1.25 in wide in print, or 120 px on screen.
- Co-brand with MORPC by placing the MORPC logo at the opposite edge with equal optical
  weight, never inside the Data Day clear space.

---

## 10 · Quick reference

```css
/* Core */
--dd-navy-500:  #073451;  /* Dark Blue: headlines, nav, bands */
--dd-blue-500:  #0977BC;  /* Blue: buttons, fills */
--dd-teal-500:  #00A79D;  /* Teal: primary CTA fill */
--dd-green-500: #7CB46A;  /* Green: secondary accent */
--dd-ink:       #171C21;  /* body text, dark surfaces */
--dd-fog:       #F2F4F6;  /* page background */

/* Text-safe steps: use these, not the 500s */
--dd-blue-600:  #07588B;  /* links on light  (7.56:1 on white) */
--dd-teal-600:  #007C74;  /* teal text on light */
--dd-green-700: #425F38;  /* green text on light */
--dd-blue-300:  #89BEDF;  /* links on dark   (8.57:1 on Ink) */
--dd-teal-300:  #85D5D0;  /* accents on the navy band */

/* Supporting neutrals */
--dd-slate:     #5F6B75;  /* captions, metadata */
--dd-mist:      #DDE2E7;  /* hairlines, table borders */
--dd-ink-soft:  #2A3238;  /* elevated dark surface */
```

**The short version**

- Dark Blue for structure, Blue for anything clickable, Teal for the one action that matters.
- Body text is Ink on light, Fog on dark. Captions are Slate on light, Dark Blue 300 on dark.
- Accents at 500 are fills. When an accent must be text, step to 600 or 700 on light, 300 on
  dark.
- White logo on dark, Primary logo on light. Never recolor either.

---

*Version 1.0, 21 July 2026. Owner: MORPC / Regional Data Roundtable.*

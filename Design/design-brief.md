# Data Day 2027 — Design Brief & Prompt Kit

Working document for developing the event's visual identity in Claude, then carrying
it into a simple static site. Read the [theme concept](../Theme/theme-concept-draft.md)
first — every prompt below inherits from it.

> **Status:** planning. Decisions locked so far: **fresh, independent color palette**
> (not bound to the MORPC brand palette) and a **wordmark + forward-leaning "5"** logo
> direction. Everything else is open for iteration.

---

## 1. The brief (shared context for every prompt)

Paste this block at the top of any design prompt so Claude has consistent grounding.

```
CONTEXT — Data Day 2027
- Event: Data Day, a one-day conference for Central Ohio's public-sector data
  community — local governments, nonprofits, educational institutions, and
  civic-minded businesses. Convened by the Mid-Ohio Regional Planning Commission
  (MORPC) and its Regional Data Roundtable.
- Date / place: Tuesday, February 16, 2027 — Ohio State University, Vitria on the
  Square, Columbus, OH. This is the FIFTH annual Data Day.
- Theme: "Five Years Forward — Shaping what's next for Central Ohio's data community."
  The fifth anniversary is a launch pad, not a scrapbook. Tone is forward-looking and
  energetic; avoid nostalgic / backward-looking framing.
- Visual motif: MOTION. Forward-leaning numeral "5," arrows, a path/road, momentum
  lines, ascending movement.
- Audience feel: professional and credible (public sector) but modern, approachable,
  and optimistic. Not corporate-stiff, not childish.
- Brand note: marketing will often appear alongside the MORPC logo, so the new palette
  should sit comfortably next to it without clashing — fresh, but not garish.
```

---

## 2. Color palette

**Goal:** a fresh, distinctive Data Day 2027 palette — a hero color, supporting colors,
an energetic accent for the "motion" feel, and a neutral set — all accessible.

**Prompt:**

```
[Paste the CONTEXT block above.]

Develop a fresh, independent color palette for Data Day 2027. It does NOT need to use
MORPC's existing navy/blue, but it must sit comfortably beside the MORPC logo.

Deliver:
1. A core palette with 5–7 colors: one hero/primary, one or two secondary, one
   energetic accent (for the forward-motion feel), and 2–3 neutrals (a near-black ink,
   a light background, a mid gray). Give each a name, HEX, and one-line usage note.
2. An extended set: tints/shades for each core color (e.g., 100–700 steps) for UI and
   data-viz use.
3. A data-visualization sub-palette of 5–6 categorical colors that are distinguishable
   and color-blind-safe.
4. Accessibility check: list which text/background pairings meet WCAG AA (4.5:1) and AAA.
5. Two or three suggested pairings ("hero + neutral for headers," etc.).
6. A short rationale tying the palette to "Five Years Forward" (motion, optimism).

Output the palette as an HTML swatch sheet I can preview (named blocks with HEX labels),
plus the values as a copyable list and as CSS custom properties (:root variables).
```

**After it runs:** save the chosen values to `Design/palette.md` (and later into the
site's CSS variables). Ask for one light and one dark variant if we want a dark hero.

---

## 3. Logo

**Direction (locked):** a "Data Day 2027" wordmark paired with a stylized,
forward-leaning numeral **5** as the hero glyph, plus a "Five Years Forward" lockup.

**Prompt:**

```
[Paste the CONTEXT block, and paste the final palette once section 2 is done.]

Design a logo system for Data Day 2027. Direction: a clean, modern wordmark
"Data Day 2027" paired with a stylized, forward-leaning numeral "5" as the hero glyph
that expresses motion (think italic/forward lean, momentum lines, or an arrow built
into the form). Include a "Five Years Forward" tagline lockup.

Constraints:
- Geometric, modern sans-serif feeling; legible at small sizes.
- Works in full color, single color, and reversed (on a dark background).
- The "5" glyph must also stand alone as a compact icon/avatar.

Deliver as SVG (vector) so I can edit:
1. Primary lockup — horizontal: glyph + "Data Day 2027".
2. Stacked lockup — glyph above the wordmark, with the "Five Years Forward" tagline.
3. Icon-only — just the forward-leaning "5," square-croppable for avatars/favicons.
4. One-color (ink) and reversed (white-on-dark) versions of the primary lockup.
Show them on both light and dark backgrounds. Include brief usage notes (clear space,
minimum size, do/don't).
```

**Iterate:** generate 3–4 distinct "5"-glyph concepts first, pick one, then ask for the
full lockup set in that style. Keep source SVGs in `Design/logo/`.

---

## 4. Icons

**Goal:** a consistent icon set for session topics and for the website/marketing UI,
in a style that echoes the motion motif (consistent stroke, slight forward energy).

**Prompt:**

```
[Paste the CONTEXT block + final palette + a note on the logo's line style.]

Create a cohesive icon set for Data Day 2027 in a single consistent style (uniform
stroke weight, rounded or geometric to match the logo, drawn on a 24px grid).
Deliver as clean SVGs, one symbol each, plus a single preview sheet showing them all.

Topic icons (for session tracks / program): GIS & mapping, AI & machine learning,
data visualization, housing & community development, transportation & mobility,
infrastructure & economic development, energy & sustainability, program evaluation /
research, open data, privacy & ethics, workshops / hands-on.

UI / wayfinding icons (for the site & signage): calendar/date, location/venue,
registration ticket, keynote/microphone, breakout sessions, lunch, networking,
schedule/agenda, sponsors, accessibility, social share.

Keep them visually consistent as a family. Provide the SVGs and note the grid/stroke
spec so we can add matching icons later.
```

**Keep:** export to `Design/icons/`. Lock the stroke/grid spec so future icons match.

---

## 5. Marketing elements

**Goal:** a templated kit the Champions and staff can reuse across the cycle. These map
to the resource kits already called for (CFP promo, registration promo, sponsorship).

**Prompt (run per element, or as a set):**

```
[Paste the CONTEXT block + final palette + logo files.]

Design a marketing template kit for Data Day 2027 using the palette and logo, carrying
the "Five Years Forward" motion motif. For each item, give me an editable layout
(HTML/CSS artifact is fine for previewing, with text I can swap):

1. Save-the-date / announcement graphic (square 1080×1080 for social).
2. LinkedIn banner and post graphics (the primary channel for this audience).
3. Email header banner.
4. "Call for Proposals" promo graphic + a matching slide (16:9).
5. "Register now" promo graphic, with variants for each push moment
   (open, agenda live, two weeks out, final week).
6. A title/section slide template (16:9) for the event deck.
7. Name badge + simple signage template (directional + room signs).
8. Optional: a "5 years in motion" countdown/stat graphic for momentum posts.

Keep a consistent system: same type hierarchy, same use of the accent color for the
motion motif, generous clear space around the logo. Note the dimensions for each.
```

**Tie-in:** these feed the Champions CFP promo kit, registration promo kit, and
sponsorship brochure already on the to-build list.

---

## 6. Static site (plan — build later)

A simple, fast, **static** site hosted on **GitHub Pages**. No backend; registration and
forms link out (Microsoft Forms, registration platform). Build only after the palette and
logo are settled so the design tokens are real.

**Recommended approach**
- **Plain HTML + CSS** (optionally a touch of vanilla JS for a mobile menu / countdown).
  No build step = simplest possible GitHub Pages deploy. Reach for Jekyll/11ty only if we
  outgrow a single page.
- Serve from the **`/docs` folder on a `main`/site branch** or a dedicated `gh-pages`
  branch — decide at build time.
- Encode the palette as CSS custom properties and reuse the logo/icon SVGs inline.

**Proposed sections (single landing page to start)**
1. Hero — logo, "Five Years Forward," date + venue, primary "Register" / "Notify me" CTA.
2. About — what Data Day is; the five-year momentum narrative; who attends.
3. Program / schedule — high-level day shape; deep-link to the full agenda when ready.
4. Keynotes & speakers — populate as confirmed.
5. Get involved — Champions, Call for Proposals, sponsorship (links to the existing forms/PDFs).
6. Venue & logistics — OSU Vitria on the Square, map, parking/transit, accessibility.
7. Sponsors — logo wall as they sign on.
8. FAQ + contact — jinskeep@morpc.org.

**Cross-cutting:** mobile-first responsive, WCAG AA accessible (the palette work feeds
this), fast (inline SVG, no heavy frameworks), clear metadata/OpenGraph using the
save-the-date graphic.

**Suggested phasing**
- Phase 1: one-page "save the date" (hero + about + notify/register CTA + venue).
- Phase 2: add program, speakers, get-involved, sponsors as content firms up.
- Phase 3: polish — countdown, sponsor wall, OpenGraph cards, analytics.

---

## 7. How to work the prompts

- **Always lead with the CONTEXT block** so outputs stay coherent across sessions.
- **Settle palette → logo → icons → marketing → site**, in that order; each feeds the next.
- **Ask for editable/vector output** (SVG, HTML/CSS) rather than flat images so assets
  stay tweakable and feed straight into the site.
- **Generate options, then converge** — ask for 3–4 directions, pick one, then refine.
- **Save chosen assets** under `Design/` (`palette.md`, `logo/`, `icons/`, `marketing/`)
  so the repo is the source of truth.

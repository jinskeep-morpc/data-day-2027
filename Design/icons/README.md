# Data Day 2027 — Icon Set ("A Consistent Line")

22 icons drawn on one grid with one stroke weight, echoing the logo's rounded, humanist
line. **11 topic/track** marks (`topic/`) for session tracks and the program, and **11
UI/wayfinding** marks (`ui/`) for the site and signage.

## Spec — lock this for any future icons

| | |
|---|---|
| **Grid** | 24×24px artboard, 2px safe margin (≈ 20×20 live area) |
| **Stroke** | 1.75px, round caps & joins, no mixed weights |
| **Fills** | Outline by default; small solid dots/squares allowed as accents only |
| **Color** | Monochrome per use — Cloud White `#F5F0F7` on dark, Ink Void `#221C2B` on light. Magenta / Gold reserved for active / selected states, never the default |

Every icon uses `stroke="currentColor"`, so color follows the surrounding text `color`.
Solid accent bits are set to `fill="currentColor"` so they track the same color. To show a
selected/active state, set `color` to Signal Magenta `#CB4FC0` or Plot Gold `#F6B93B`.

```html
<!-- default -->
<span style="color:#F5F0F7"><!-- inline the svg --></span>
<!-- active/selected -->
<span style="color:#CB4FC0"><!-- same svg --></span>
```

## Files

**`topic/`** — gis-mapping · ai-machine-learning · data-visualization ·
housing-community-dev · transportation-mobility · infrastructure-econ-dev ·
energy-sustainability · program-evaluation-research · open-data · privacy-ethics ·
workshops-hands-on

**`ui/`** — calendar-date · location-venue · registration-ticket · keynote-microphone ·
breakout-sessions · lunch · networking · schedule-agenda · sponsors · accessibility ·
social-share

All are standalone, self-contained SVGs at `viewBox="0 0 24 24"` with a `<title>` for
accessibility. Verified with Inkscape renders (white-on-dark) — all 22 read clearly at
small size.

---

*Source: Claude Design project `19813721-b03a-45cc-9964-61ad5e02f050`, file "Data Day 2027
Icon Set". Imported 2026-07-14. Style matches [`../logo/`](../logo) and the
[palette](../palette.md).*

#!/usr/bin/env python3
"""Render a Markdown file to a MORPC / Data Day styled PDF.

Pipeline: Markdown -> HTML (python-markdown) -> headless Chromium -> PDF.
Matches the house style of the Champions FAQ / Ways-to-Help PDFs:
the document's first H1 becomes the navy title, placed under the MORPC
logo; H2s are steel-blue section headings with rules.

Usage:
    python3 build_pdf.py INPUT.md [-o OUTPUT.pdf] [--no-logo] [--logo PATH]

Defaults: OUTPUT is INPUT with a .pdf extension; the logo is the MORPC
horizontal logo in the repo's Assets/ folder.
"""
import argparse
import base64
import mimetypes
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import markdown

SKILL_DIR = Path(__file__).resolve().parent
REPO_ROOT = SKILL_DIR.parents[2]  # .claude/skills/create-pdf -> repo root
DEFAULT_LOGO = REPO_ROOT / "Assets" / "MORPC_HORIZONTAL LOGO_PRIMARY COLOR (1).png"
STYLE = SKILL_DIR / "style.css"

CHROMIUM_CANDIDATES = ["chromium", "chromium-browser", "google-chrome", "google-chrome-stable"]


def find_chromium() -> str:
    for name in CHROMIUM_CANDIDATES:
        path = shutil.which(name)
        if path:
            return path
    sys.exit("error: no Chromium/Chrome binary found (tried: %s)" % ", ".join(CHROMIUM_CANDIDATES))


def data_uri(path: Path) -> str:
    mime = mimetypes.guess_type(str(path))[0] or "image/png"
    b64 = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{b64}"


def build_html(md_path: Path, logo: Path | None) -> str:
    body = markdown.markdown(
        md_path.read_text(encoding="utf-8"),
        extensions=["extra", "sane_lists", "smarty"],
    )
    css = STYLE.read_text(encoding="utf-8")
    header = ""
    if logo and logo.exists():
        header = f'<div class="doc-header"><img class="logo" src="{data_uri(logo)}" alt="MORPC"></div>'
    elif logo:
        print(f"warning: logo not found at {logo}; rendering without it", file=sys.stderr)
    return (
        "<!DOCTYPE html><html><head><meta charset='utf-8'>"
        f"<style>{css}</style></head><body>{header}{body}</body></html>"
    )


def render_pdf(html: str, out_path: Path) -> None:
    chromium = find_chromium()
    # Stage scratch files in the output directory, not /tmp: when running
    # under a sandbox the Chromium subprocess may not share the parent's
    # /tmp view, so a temp HTML there renders as ERR_FILE_NOT_FOUND.
    with tempfile.TemporaryDirectory(dir=str(out_path.parent), prefix=".pdfbuild-") as tmp:
        html_file = Path(tmp) / "doc.html"
        html_file.write_text(html, encoding="utf-8")
        cmd = [
            chromium, "--headless=new", "--disable-gpu", "--no-sandbox",
            f"--user-data-dir={tmp}/profile",
            "--no-pdf-header-footer",
            "--run-all-compositor-stages-before-draw",
            "--virtual-time-budget=10000",
            f"--print-to-pdf={out_path}",
            html_file.as_uri(),
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        # Chromium can exit non-zero on harmless GPU warnings, so judge
        # success by the output file rather than the return code.
        if not out_path.exists() or out_path.stat().st_size == 0:
            sys.exit(f"error: Chromium failed to render PDF\n{result.stderr}")


def main() -> None:
    ap = argparse.ArgumentParser(description="Render Markdown to a MORPC-styled PDF.")
    ap.add_argument("input", type=Path, help="Markdown file to render")
    ap.add_argument("-o", "--output", type=Path, help="Output PDF (default: INPUT.pdf)")
    ap.add_argument("--logo", type=Path, default=DEFAULT_LOGO, help="Logo image path")
    ap.add_argument("--no-logo", action="store_true", help="Render without a logo")
    args = ap.parse_args()

    if not args.input.exists():
        sys.exit(f"error: input not found: {args.input}")
    out = args.output or args.input.with_suffix(".pdf")
    logo = None if args.no_logo else args.logo

    html = build_html(args.input, logo)
    render_pdf(html, out.resolve())
    print(f"wrote {out}")


if __name__ == "__main__":
    main()

"""Draw the site's icon and share image. Run once; the outputs are committed.

    python demo/frontend/scripts/make-brand-assets.py

Why a script and not hand-made files: the favicon that shipped was Vite's
template logo, and nothing noticed. The mark here is a compass needle in a ring
(an atlas orients you; it does not decide for you), drawn from plain geometry so
the SVG and the PNGs cannot disagree. The share image carries the one-line
description and the "research prototype, AI-assisted" label that the header
shows, so a link preview does not promise more than the site is.

Needs Pillow and a Segoe UI font (Windows). The PNGs are not rebuilt in CI.
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

PUBLIC = Path(__file__).resolve().parent.parent / "public"
ACCENT = (77, 63, 199)  # --accent
WHITE = (255, 255, 255)
INK = (18, 16, 22)  # dark --bg
FONT_DIR = Path("C:/Windows/Fonts")

SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="Journal Atlas">
  <rect width="64" height="64" rx="14" fill="#4d3fc7"/>
  <circle cx="32" cy="32" r="19" fill="none" stroke="#ffffff" stroke-width="4"/>
  <polygon points="32,15 38.5,32 32,49 25.5,32" fill="#ffffff"/>
  <circle cx="32" cy="32" r="3.2" fill="#4d3fc7"/>
</svg>
"""


def icon(size: int) -> Image.Image:
    """The same geometry as the SVG, drawn at 8x and scaled down for clean edges."""
    s = size * 8
    k = s / 64
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((0, 0, s - 1, s - 1), radius=14 * k, fill=ACCENT)
    d.ellipse((13 * k, 13 * k, 51 * k, 51 * k), outline=WHITE, width=round(4 * k))
    d.polygon([(32 * k, 15 * k), (38.5 * k, 32 * k), (32 * k, 49 * k), (25.5 * k, 32 * k)], fill=WHITE)
    d.ellipse((28.8 * k, 28.8 * k, 35.2 * k, 35.2 * k), fill=ACCENT)
    return img.resize((size, size), Image.LANCZOS)


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_DIR / name), size)


def share_image() -> Image.Image:
    w, h = 1200, 630
    img = Image.new("RGB", (w, h), INK)
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, 18, h), fill=ACCENT)
    img.paste(icon(132), (84, 84), icon(132))
    d.text((84, 258), "Journal Atlas", font=font("segoeuib.ttf", 96), fill=WHITE)
    d.text((84, 378), "Journal fit, with the evidence shown.", font=font("segoeui.ttf", 44), fill=(214, 209, 240))
    d.text(
        (84, 470),
        "Every candidate says how its entry was written and how much of it is evidenced.",
        font=font("segoeui.ttf", 28),
        fill=(171, 165, 205),
    )
    d.text(
        (84, 548),
        "Research prototype  ·  AI-assisted  ·  open knowledge base",
        font=font("segoeuib.ttf", 26),
        fill=(179, 167, 245),
    )
    return img


def main() -> None:
    (PUBLIC / "favicon.svg").write_text(SVG, encoding="utf-8", newline="\n")
    icon(32).save(PUBLIC / "favicon-32.png", optimize=True)
    icon(180).save(PUBLIC / "apple-touch-icon.png", optimize=True)
    share_image().save(PUBLIC / "og.png", optimize=True)
    for name in ("favicon.svg", "favicon-32.png", "apple-touch-icon.png", "og.png"):
        print(name, (PUBLIC / name).stat().st_size, "bytes")


if __name__ == "__main__":
    main()

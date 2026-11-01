#!/usr/bin/env python3
"""Crop art to a 16:9 thumbnail, add bold stroked text, and render a phone-size preview."""
import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFont

FONT_CANDIDATES = [
    "Anton-Regular.ttf", "Impact.ttf", "impact.ttf", "Montserrat-Black.ttf",
    "/System/Library/Fonts/Supplemental/Impact.ttf",
    "C:/Windows/Fonts/impact.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "DejaVuSans-Bold.ttf", "Arial Bold.ttf", "arialbd.ttf",
]
PRESETS = {
    "youtube": "1280x720", "roblox": "1920x1080", "steam-capsule": "1232x706",
    "steam-header": "920x430", "itch": "630x500", "social": "1600x900",
}
ANCHORS = {"top": "ma", "bottom": "md", "left": "lm", "right": "rm", "center": "mm"}


def load_font(path, size):
    for name in [path] if path else FONT_CANDIDATES:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    if path:
        raise SystemExit(f"font not found: {path}")
    return ImageFont.load_default(size)


def cover(img, w, h):
    scale = max(w / img.width, h / img.height)
    img = img.resize((round(img.width * scale), round(img.height * scale)), Image.LANCZOS)
    left, top = (img.width - w) // 2, (img.height - h) // 2
    return img.crop((left, top, left + w, top + h))


def add_badge(img, text="12:34"):
    """Draw a YouTube-style video length badge in the bottom-right corner."""
    draw = ImageDraw.Draw(img)
    font = load_font(None, max(9, img.height // 9))
    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    pad, margin = max(2, img.height // 40), max(3, img.height // 25)
    x1, y1 = img.width - margin, img.height - margin
    x0, y0 = x1 - (right - left) - 2 * pad, y1 - (bottom - top) - 2 * pad
    draw.rounded_rectangle((x0, y0, x1, y1), radius=pad, fill=(0, 0, 0))
    draw.text((x0 + pad - left, y0 + pad - top), text, font=font, fill=(255, 255, 255))
    return img


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input")
    p.add_argument("output")
    p.add_argument("--size", help="WxH, overrides --preset")
    p.add_argument("--preset", choices=PRESETS, default="youtube",
                   help="target size: " + ", ".join(f"{k} {v}" for k, v in PRESETS.items()))
    p.add_argument("--text", help="0 to 4 words, e.g. '100 DAYS'")
    p.add_argument("--position", choices=ANCHORS, default="top")
    p.add_argument("--color", default="#FFE600")
    p.add_argument("--stroke", default="#000000")
    p.add_argument("--font", help="path to a heavy sans-serif .ttf (Anton, Impact, Montserrat Black)")
    p.add_argument("--font-size", type=int, help="default is 18%% of the height")
    p.add_argument("--saturation", type=float, default=1.25, help="1.0 leaves color unchanged")
    p.add_argument("--contrast", type=float, default=1.1)
    p.add_argument("--preview", action="store_true", help="also write <output>_phone.png at feed size")
    a = p.parse_args()

    w, h = (int(v) for v in (a.size or PRESETS[a.preset]).lower().split("x"))
    img = cover(Image.open(a.input).convert("RGB"), w, h)
    img = ImageEnhance.Color(img).enhance(a.saturation)
    img = ImageEnhance.Contrast(img).enhance(a.contrast)

    if a.text:
        if len(a.text.split()) > 4:
            print("warning: more than 4 words will not read on a phone")
        size = a.font_size or round(h * 0.18)
        font = load_font(a.font, size)
        draw = ImageDraw.Draw(img)
        while size > 20 and draw.textlength(a.text.upper(), font=font) > w * 0.9:
            size = round(size * 0.9)
            font = load_font(a.font, size)
        pad = round(h * 0.06)
        xy = {"top": (w / 2, pad), "bottom": (w / 2, h - pad), "left": (pad, h / 2),
              "right": (w - pad, h / 2), "center": (w / 2, h / 2)}[a.position]
        draw.text(xy, a.text.upper(), font=font, fill=a.color, anchor=ANCHORS[a.position],
                  stroke_width=max(4, size // 12), stroke_fill=a.stroke)

    out = Path(a.output)
    img.save(out)
    print(f"wrote {out} ({w}x{h})")

    if a.preview:
        small = img.resize((210, round(210 * h / w)), Image.LANCZOS)
        if a.preset == "youtube" and not a.size:
            add_badge(small)
        phone = small.resize((small.width * 2, small.height * 2), Image.NEAREST)
        prev = out.with_name(f"{out.stem}_phone{out.suffix}")
        phone.save(prev)
        print(f"wrote {prev}: feed size (210 px wide) shown at 2x. Can you read it in 3 seconds?")


if __name__ == "__main__":
    main()

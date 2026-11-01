#!/usr/bin/env python3
"""Put thumbnails side by side in a mock phone feed to compare variants at real size.

Mix your variants with a few competitor thumbnails from the same niche. The
one you notice first in under a second is the one to test first.
"""
import argparse
from pathlib import Path

from PIL import Image, ImageDraw

from thumbnail import add_badge, cover, load_font

CARD_W, CARD_H, GAP = 210, 118, 12


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("images", nargs="+", help="thumbnails to compare (16:9)")
    p.add_argument("-o", "--output", default="feed.png")
    p.add_argument("--titles", nargs="*", default=[], help="one title per image, in the same order")
    p.add_argument("--columns", type=int, default=3)
    p.add_argument("--light", action="store_true", help="light mode feed instead of dark")
    a = p.parse_args()

    bg, fg = ((255, 255, 255), (15, 15, 15)) if a.light else ((15, 15, 15), (241, 241, 241))
    font = load_font(None, 11)
    text_h = 30 if a.titles else 0
    cols = min(a.columns, len(a.images))
    rows = -(-len(a.images) // cols)
    sheet = Image.new("RGB", (GAP + cols * (CARD_W + GAP), GAP + rows * (CARD_H + text_h + GAP)), bg)
    draw = ImageDraw.Draw(sheet)

    for i, path in enumerate(a.images):
        x = GAP + (i % cols) * (CARD_W + GAP)
        y = GAP + (i // cols) * (CARD_H + text_h + GAP)
        card = add_badge(cover(Image.open(path).convert("RGB"), CARD_W, CARD_H))
        sheet.paste(card, (x, y))
        if i < len(a.titles):
            title = a.titles[i]
            while draw.textlength(title, font=font) > CARD_W and len(title) > 4:
                title = title[:-2].rstrip() + "…"
            draw.text((x, y + CARD_H + 5), title, font=font, fill=fg)

    sheet = sheet.resize((sheet.width * 2, sheet.height * 2), Image.NEAREST)
    sheet.save(Path(a.output))
    print(f"wrote {a.output}: {len(a.images)} thumbnails at feed size (210 px wide), shown at 2x")


if __name__ == "__main__":
    main()

# AI image prompts

Recipes for turning a variant into a prompt. Generate the art without
text, then add text with `scripts/thumbnail.py`. AI tools still misspell
and warp text.

## Prompt skeleton

Write one paragraph in this order. Lead with the subject; image models
weigh early words most.

1. Format: "YouTube thumbnail, 16:9, hyper-saturated, high contrast"
2. Subject: who or what, exact emotion, pose, where in the frame (left third, right third, center), how close (tight close-up, chest-up)
3. Stakes object: what it is, size relative to the subject, where it sits
4. Background: setting, simple, blurred or darker than the subject
5. Light and color: rim light color, key light, 1 or 2 hero colors
6. Style: "photorealistic", "3D render", "Pixar-style", or match the game's art style
7. Clean-up: "no text, no logos, no watermark, empty space on the <side> for text"

## Example

> YouTube thumbnail, 16:9, hyper-saturated, high contrast. A young man in
> a tight chest-up shot on the left third of the frame, eyes wide with
> panic and jaw clenched, gripping the edge of a bathtub filled to the
> brim with bright red ketchup. On the right, a towering stack of $100
> bills taller than him, glowing under a warm key light. Plain deep-blue
> studio background with a soft radial glow behind the subject. Strong
> cyan rim light on his hair and shoulders, punchy yellow and red hero
> colors, crisp focus on face and cash, background slightly blurred.
> Photorealistic, shot on 35mm. No text, no logos, no watermark, empty
> space at top right.

## Tool notes

| Tool | Aspect ratio | Notes |
| --- | --- | --- |
| Midjourney | append `--ar 16:9 --style raw --v 7` (use the latest version) | `--style raw` keeps it less painterly; add `--s 50` to `--s 250` for stylization |
| DALL-E / ChatGPT images | ask for "landscape 16:9" or 1792x1024 | follows long natural-language prompts well |
| Flux | set width 1344, height 768 | strong on photorealism and hands |
| Stable Diffusion / SDXL | 1344x768; negative prompt: "text, watermark, logo, blurry, muted colors, cluttered background, extra fingers" | use a face-detail pass or inpainting on the face |
| Ideogram | 16:9 | best of the group if you must render text in the image |

## Using a real face

- Best: photograph the real person with the exact expression, cut them out (remove.bg, Photoshop, or `rembg`), and composite them onto generated art.
- With image editing tools that accept a reference photo, pass the user's photo and describe the expression change.
- Never generate a real celebrity or public figure without permission.

## Using game art

- Pass a real screenshot or character render as an image reference when the tool supports it, so the thumbnail matches the actual game.
- Or describe the art style precisely: "low-poly", "pixel art with chunky outlines", "cel-shaded anime", "blocky 3D toy style".
- The thumbnail must look like the game players will get. Misleading art hurts store-page conversion and reviews.

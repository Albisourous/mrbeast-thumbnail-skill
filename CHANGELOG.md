# Changelog

## 0.3.0

- `thumbnail.py --preset` exports YouTube, Roblox, Steam capsule, Steam header, itch.io, and social sizes. `--size` still overrides it.
- The YouTube phone preview draws a video length badge, so text under the badge shows up as a problem.
- New `scripts/feed.py` puts variants and competitor thumbnails in a mock phone feed (dark or `--light`) with titles, to pick which variant to test first.

## 0.2.1

- Self-check: keep the bottom-right corner clear for YouTube's video length badge.
- projects-and-games.md links the current size specs for YouTube, Roblox, Steam, and itch.io.
- Say that the phone preview is a quick check and the final image still needs a look on a real phone.
- Add `scripts/validate.py` to check versions, descriptions, and links before a release.

## 0.2.0

- Fold lessons from MrBeast's production handbook into the workflow: a new idea test step (ketchup vs front yard, simplicity, audience), title rules (strongest true verb, the content must match the packaging), and format guidance (show the question, not the answer).
- packaging-rules.md gains CTR, AVD, and AVP, choosing an idea, formats, and keeping the promise in the first minute.
- Variant output replaces "First 5 seconds" with "Payoff"; the self-check covers title honesty and format videos.
- Self-check now requires comparison sides that look clearly different and a palette picked per concept. SKILL.md adds a critique-and-regenerate loop; image-prompts.md adds Nano Banana Pro and face reference photos.

## 0.1.0

- First release: SKILL.md workflow (3 packaging variants plus self-check), packaging rules, AI image prompt recipes, games and projects guide, and `scripts/thumbnail.py` for text overlay and phone preview.

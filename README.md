# MrBeast Thumbnail Skill

An AI agent skill that makes MrBeast-style YouTube thumbnails, titles, and AI image prompts for any video, game, app, or project.

Give it an idea or a script, or point it at a repo. It returns 3 finished packaging variants built on the rules MrBeast's team made famous: one focal subject, one loud emotion, a concrete stake, saturated color, and almost no text. Each variant has a title, a 3-element layout, a color plan, a ready-to-paste Midjourney / DALL-E / Flux prompt, and the first 5 seconds the content needs to pay off the click. If your agent can generate images, it makes them too, then adds text and checks the result at phone size.

Works for YouTube thumbnails, game devlogs, trailers, Steam capsules, Roblox and itch.io covers, app store banners, and launch posts.

## Install

| Agent | Install |
|---|---|
| Claude Code | `/plugin marketplace add Albisourous/mrbeast-thumbnail-skill`, then install `mrbeast-thumbnail-skill` |
| Codex, Cursor, others | `npx skills add Albisourous/mrbeast-thumbnail-skill` |
| Devin | Copy `SKILL.md`, `references/`, and `scripts/` into `.devin/skills/mrbeast-thumbnail-skill/` |
| Any agent that reads skills | Copy `SKILL.md`, `references/`, and `scripts/` into its skill directory |

## Try it

> Here is my video idea: I spent 7 days building a game with only AI. Generate the packaging variants.

> Look at this repo and make me 3 thumbnails for a devlog about it.

> Make a Steam capsule and a YouTube thumbnail for my game's trailer. Generate the images.

## What you get

```markdown
### Variant 1: Extreme scale

- **Title:** I Built A Game In 7 Days With AI
- **Hook:** A tiny laptop next to a huge finished game world makes the time gap feel impossible.
- **Thumbnail text:** DAY 7
- **Visual composition (3 elements max):**
  - **Subject:** creator on the left third, chest-up, eyes wide with disbelief, warm key light
  - **Stakes object:** a giant glowing game world bursting out of a tiny laptop screen
  - **Background:** plain deep purple, soft glow behind the subject
- **Color and lighting:** yellow and cyan hero colors on purple, cyan rim light, saturation pushed
- **AI image prompt:** YouTube thumbnail, 16:9, hyper-saturated ...
- **Payoff:** open on the finished game running, then cut to day 1
```

## Add text and check it on a phone

Generate the art without text (AI tools misspell words), then:

```sh
pip install pillow
python3 scripts/thumbnail.py art.png thumb.png --text "DAY 7" --preview
```

You get `thumb.png` at 1280x720 and `thumb_phone.png` at YouTube feed size. If the phone preview takes more than 3 seconds to make sense, simplify the image. Run `python3 scripts/thumbnail.py -h` for position, color, font, and saturation options.

## What's inside

| File | Use it for |
|---|---|
| `SKILL.md` | The workflow: test the idea, find the hook, write 3 variants, self-check, make the image |
| `references/packaging-rules.md` | The five patterns, archetypes, formats, titles, faces, color, testing, and lessons from MrBeast's production handbook |
| `references/image-prompts.md` | Prompt skeleton and notes for Midjourney, DALL-E, Flux, SDXL, Ideogram |
| `references/projects-and-games.md` | Sizes and hooks for games, apps, repos, and store pages |
| `scripts/thumbnail.py` | Crop to 16:9, add stroked text, render a phone preview |
| `scripts/validate.py` | Check that versions, descriptions, and links agree before a release |

## Sources

- [MrBeast marketing lessons](https://www.blog.theperformers.io/p/mrbeast-marketing-lessons), The Performers
- [MrBeast thumbnail analysis: the 5 patterns](https://artiphik.com/blog/mrbeast-thumbnail-analysis), Artiphik
- "How to Succeed in MrBeast Production", MrBeast's internal handbook (leaked 2024)
- The Ringer's reporting on "YouTube Face" and MrBeast's thumbnail lead Chucky Appleby

Not affiliated with MrBeast. The skill will not generate real people's likenesses without permission.

## License

MIT

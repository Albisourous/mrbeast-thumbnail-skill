#!/usr/bin/env python3
"""Check that versions, descriptions, and links in this skill agree. Run before a release."""
import json
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
errors = []

skill = (root / "SKILL.md").read_text()
version = re.search(r'version:\s*"([^"]+)"', skill).group(1)
desc = re.search(r"description: \|\n\s+(.+)", skill).group(1).strip()

changelog = re.search(r"^## (\S+)", (root / "CHANGELOG.md").read_text(), re.M).group(1)
if changelog != version:
    errors.append(f"CHANGELOG.md starts at {changelog}, SKILL.md says {version}")

for rel in [".claude-plugin/plugin.json", ".devin-plugin/plugin.json", ".cursor-plugin/plugin.json",
            ".claude-plugin/marketplace.json"]:
    data = json.loads((root / rel).read_text())
    for entry in data.get("plugins", [data]):
        if entry.get("version") != version:
            errors.append(f"{rel}: version {entry.get('version')}, expected {version}")
        if entry.get("description") != desc:
            errors.append(f"{rel}: description does not match the first line of the SKILL.md description")

for md in [root / "SKILL.md", root / "README.md", *(root / "references").glob("*.md")]:
    for link in re.findall(r"\]\(([^)#]+)\)", md.read_text()):
        if not link.startswith("http") and not (md.parent / link).exists():
            errors.append(f"{md.relative_to(root)}: broken link {link}")

words = len(skill.split())
if words > 2000:
    errors.append(f"SKILL.md has {words} words; keep it under 2000")

for e in errors:
    print("error:", e)
print("ok" if not errors else f"{len(errors)} problem(s)")
sys.exit(1 if errors else 0)

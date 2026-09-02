#!/usr/bin/env python3
"""Install the repository's complete custom skill library for one Codex user."""

from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import sys


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "06_Skills"
EXPECTED_SKILL_COUNT = 48


def skill_directories() -> list[Path]:
    return sorted(
        path
        for path in SOURCE.iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install all 48 shared skills into a Codex skill folder."
    )
    parser.add_argument(
        "--destination",
        type=Path,
        default=Path.home() / ".codex" / "skills",
        help="Target skill folder. Default: the current user's .codex/skills folder.",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List the packaged skills without installing them.",
    )
    parser.add_argument(
        "--update",
        action="store_true",
        help="Update files in existing skill folders. New skills are always installed.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    skills = skill_directories()

    if len(skills) != EXPECTED_SKILL_COUNT:
        print(
            f"Expected {EXPECTED_SKILL_COUNT} skills, found {len(skills)}. "
            "Run the framework validator before installation.",
            file=sys.stderr,
        )
        return 1

    if args.list:
        for skill in skills:
            print(skill.name)
        return 0

    destination = args.destination.expanduser().resolve()
    if destination == SOURCE.resolve():
        print("The install destination cannot be the repository source folder.", file=sys.stderr)
        return 1

    destination.mkdir(parents=True, exist_ok=True)
    installed = 0
    updated = 0
    skipped = 0

    for skill in skills:
        target = destination / skill.name
        if target.exists() and not args.update:
            skipped += 1
            continue

        existed = target.exists()
        shutil.copytree(skill, target, dirs_exist_ok=existed)
        if existed:
            updated += 1
        else:
            installed += 1

    print(f"Skill source: {SOURCE}")
    print(f"Install destination: {destination}")
    print(f"Installed: {installed}")
    print(f"Updated: {updated}")
    print(f"Skipped: {skipped}")
    print("Restart Codex before testing the skills.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
